"""
Virtual Serial Console Module
"""
import os
import re
import time
import json
import traceback
import paramiko
import platform
import subprocess
from random import randint
from robot.api import logger
from netaddr import IPNetwork, IPAddress
from robot.libraries.BuiltIn import BuiltIn


class VspLibrary(object):
    """
    VSP object
    """

    def __init__(self, traffic_data):
        """
        initialization method
        :param traffic_data:
        """
        self.traffic = traffic_data
        self.ssh = None
        self.i = 0

    def _send_and_receive(self, channel, send, expect, timeout=30):
        """
        SSH channel listener and writer
        :param channel:
        :param send:
        :param expect:
        :param timeout:
        :return:
        """
        if channel.send_ready():
            channel.send(send)
        else:
            logger.trace('Send is not ready')
            return False

        buff = ''
        start_time = time.time()
        while not buff.endswith(expect):
            if channel.recv_ready():
                resp = channel.recv(9999)
                # resp = re.sub(r'\x1b\[(?:K|\d*;\d*H)?', "\n", resp)
                buff += resp
                logger.trace(resp)

            if (time.time() - start_time) > timeout:
                logger.trace('Timed out..' + buff)
                return False
        return buff

    def _exec_command(self, channel, send, timeout=1):
        """
        Method to execute the remote command
        :param channel:
        :param send:
        :param timeout:
        :return:
        """
        if channel.send_ready():
            channel.send(send)
        else:
            logger.trace('Send is not ready')
            return False

        buff = resp = ''
        start_time = time.time()
        while (time.time() - start_time) < timeout:
            if channel.recv_ready():
                resp = channel.recv(9999)
                buff += resp
                # time.sleep(0.5)
        logger.trace(buff)

        return buff

    def _execute_linux_command(self, channel, command, stdout_log=False):
        """
        Executes a linux based shell command
        :param channel:
        :param command:
        :param stdout_log:
        :return:
        """
        logger.trace("_execute_linux_command entered")

        try:
            logger.trace("Executing: '%s'" % command)

            sin, sout, serr = channel.exec_command(command=command)

            count = 0
            while not sout.channel.exit_status_ready():
                count += 1
                if count % 5 == 0:
                    logger.trace('Please wait for the remote command completion')
                time.sleep(0.2)

            sout.channel.recv_exit_status()

            response = ""
            if stdout_log:
                for l in sout:
                    response += l
                    logger.trace(l.strip())

            return response.strip()
        except:
            logger.debug('Input: {}\tOutput: {}\tError:{}'.format(sin, sout,
                                                                  serr))
            logger.trace(traceback.format_exc())
            return False

        finally:
            logger.trace("_execute_linux_command exited")

    def _connect_using_ssh(self, machine_ip, username, password):
        """
        Method to establish connections
        :param machine_ip:
        :param username:
        :param password:
        :return:
        """
        logger.trace("_connect_using_ssh entered")

        try:
            ssh = None
            for _ in xrange(10):
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(hostname=machine_ip, username=username, password=password)

                    break
                except:
                    logger.trace(traceback.format_exc())
                    time.sleep(5)
                    logger.trace("Failed to take SSH connection, please wait for next attempt")
            else:
                logger.console("Failed to take SSH connection")
                return False

            logger.trace("SSH connection to '%s' successful" % machine_ip)
            return ssh

        finally:
            logger.trace("_connect_using_ssh exited")

    def login_to_ilo_vsp_console_get_handle_and_platform(self, ilo_ip, ilo_cred):
        """
        Method to perform Virtual Serial Port console actions
        :param ilo_ip:
        :param ilo_cred:
        :return:
        """
        try:
            osType = None

            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            self.ssh.connect(hostname=ilo_ip, username=ilo_cred['user_name'], password=ilo_cred['password'], look_for_keys=False)
            chan = self.ssh.invoke_shell()

            # Ssh and wait for the password prompt.
            out = self._exec_command(chan, '\r')

            self._send_and_receive(chan, 'stop /system1/oemhp_VSP1\r', 'hpiLO-> ')

            out = self._exec_command(chan, 'VSP\r', timeout=5)
            out = self._exec_command(chan, '\r')

            if out.strip().endswith('SAC>'):  # Windows2016
                osType = 'Windows'
            else:
                osType = 'Linux'

            return chan, osType

        except:
            logger.trace(traceback.format_exc())
            raise AssertionError("login_to_ilo_vsp_console failed")

    def _login_to_os_serial_console_get_ip_address_output(self, chan, os_cred):
        """
        Retrieves the IP address of the target system.
        :param chan:
        :param os_cred:
        :return:
        """
        try:
            out = self._exec_command(chan, '\r', timeout=3)

            if out.endswith('$ ') or out.endswith('# '):
                logger.trace("Already logged in to OS !!")
            elif out.endswith('login: '):
                self._exec_command(chan, os_cred['user_name'] + '\r', timeout=2)
                time.sleep(1)
                self._exec_command(chan, os_cred['password'] + '\r', timeout=2)
                time.sleep(1)
                out = self._exec_command(chan, '\r')

            if out.endswith('$ ') or out.endswith('# '):
                logger.trace("Login successful !!")

            return self._exec_command(chan, 'ip address show\r', timeout=2)

        except:
            raise AssertionError("Failed to get ip address output")

    def _login_to_sac_console_get_sac_os_interface_output(self, chan):
        """
        Returns the serial access console output
        :param chan:
        :return:
        """
        try:
            sac_os_interface_output = None

            out = self._exec_command(chan, '\r', timeout=2)

            if re.match(r'[\w\W]*?SAC\s*>\s*$', out):
                self._exec_command(chan, 'ch\r', timeout=1)
                sac_os_interface_output = self._exec_command(chan, 'i\r', timeout=2)

            else:
                raise AssertionError("CRITICAL: Login failed with the Windows server, please check")

            return sac_os_interface_output

        except:
            raise AssertionError("Failed to get ip address output")

    def logout_ilo_vsp_console(self, handle):
        """
        Closes the Virtual Serial Port connection established.
        :param handle:
        :return:
        """
        try:
            self._exec_command(handle, 'exit\r', timeout=3)
            self._exec_command(handle, '\x1b(\r')
            self._exec_command(handle, 'stop /system1/oemhp_VSP1\r')
            self._exec_command(handle, 'exit\r')
        except:
            logger.trace(traceback.format_exc())
            # raise AssertionError("Failed to logout iLO")

    def _get_from_nic_list(self, nic_list, mac_id, vlan_id):
        """
        Returns the list of NIC
        :param nic_list:
        :param mac_id:
        :param vlan_id:
        :return:
        """
        matches = list()
        for ll in nic_list:
            if ll['mac'].lower() == mac_id.lower():
                matches.append(ll)

        block = None
        for ll in matches:
            if ll['vlan'] == '':
                block = ll
                block['vlan'] = 'untagged'
            elif str(ll['vlan']).lower() == str(vlan_id).lower():
                block = ll
                break
            else:
                continue
                # logger.warn("Error in nic mapping, please check {}".format(block))

        return block

    def _parse_linux_adapter_raw_output(self, source_server, ifconfig):
        """
        Renders the NIC output
        :param source_server:
        :param ifconfig:
        :return:
        """
        data = self.traffic.data['serversAndCredentials'][source_server]
        interface = []

        # For general interface parsing
        if 'os:' in source_server:
            items = re.findall(r'\d+\:\s([\-\w]+)(?:\.(\d+))?(?:\.(\d+)@\w+)?\:\s([\w\W]*?)link\/[\s\w]+((?:\w{2}\:){5}\w{2})\sbrd\s(?:\w{2}\:){5}\w{2}(?:\s*inet\s((?:\d{1,3}\.){3}\d{1,3})\/(\d{1,2})\sbrd\s((?:\d{1,3}\.){3}\d{1,3}))?', ifconfig, re.I)
            for item in items:

                if re.search(r'lo|virb', item[0], re.I):
                    continue

                interface_name = item[0]
                interface_vlan = item[2]
                interface_mac = item[4]
                interface_ip = item[5]
                interface_mask = item[6]
                interface_gw = item[7]

                tmp_list = dict()
                tmp_list['Ip'] = interface_ip
                tmp_list['Subnet'] = interface_mask
                tmp_list['Gateway'] = interface_gw
                tmp_list['vlan'] = 'untagged' if str(interface_vlan) == '' else interface_vlan

                if any(interface_name in int for int in interface):
                    # If interface already exists
                    for index in xrange(len(interface)):
                        each = interface[index]
                        if interface_name in each:
                            tmp_list['interface'] = interface_name if str(interface_vlan) == '' else str(interface_name + '.' + interface_vlan)
                            interface[index][interface_name]['IpAddress'].append(tmp_list)
                            break
                else:
                    # If interface is found in first time
                    interface_tmp = dict()
                    interface_tmp[interface_name] = dict()
                    interface_tmp[interface_name]['MacAddress'] = interface_mac
                    interface_tmp[interface_name]['IpAddress'] = list()
                    tmp_list['interface'] = interface_name
                    interface_tmp[interface_name]['IpAddress'].append(tmp_list)

                    interface.append(interface_tmp)

        else:
            # Parsing with OV connection input
            self.i = 0
            m = 0
            port = []
            items = re.findall(
                r'\d+\:\s([\-\w]+)(?:\.(\d+))?(?:\.(\d+)@\w+)?\:\s([\w\W]*?)link\/[\s\w]+((?:\w{2}\:){5}\w{2})\sbrd\s(?:\w{2}\:){5}\w{2}(?:\s*inet\s((?:\d{1,3}\.){3}\d{1,3})\/(\d{1,2})\sbrd\s((?:\d{1,3}\.){3}\d{1,3}))?',
                ifconfig, re.I)

            new_connections = list()
            for index in xrange(0, len(data['connections'])):
                if data['connections'][index]['functionType'] == 'Ethernet':
                    new_connections.append(data['connections'][index])
            data['connections'] = new_connections

            for x in data['connections']:
                b = 0
                dic = {}
                interface1 = re.search(r'\d:\d-\w', x['portId'])
                port.append(interface1.group(0))
                dic = {interface1.group(0): {'MacAddress': x['mac'], 'IpAddress': []}}
                for item in items:
                    if re.search(r'lo|virb', item[0], re.I):
                        continue
                    if re.search(r'bond.', item[0], re.I):
                        continue
                    match_bond = re.findall(r'bond\d+', item[3], re.I)
                    if x['mac'].lower() == item[4].lower():
                        if match_bond:
                            y = self._check_bonded_interface(data, items, match_bond[0], item[0], dic, interface1.group(0), m)
                            m += 1
                            dic.update(y)
                        else:
                            if not b:
                                b = self._check_no_bonded_interface(data, items, dic, interface1.group(0))
                                dic.update(b)

                self.i += 1
                m = 0
                if not b:
                    match = re.findall(r'(\d):(\d)-(\w)', interface1.group(0))
                    for c in port:
                        match1 = re.findall(r'(\d):(\d)-(\w)', c)
                        if (match[0][0] == match1[0][0]) and \
                                (match[0][1] != match1[0][1]) and \
                                (match[0][2] == match1[0][2]):
                            j = 0
                            for d in interface:
                                if c in d.keys():
                                    if len(interface[j][c]['IpAddress']) == 0:
                                        for ll in range(len(dic[interface1.group(0)]['IpAddress'])):
                                            interface[j][c]['IpAddress'].append(dic[interface1.group(0)]['IpAddress'][ll])
                                    else:
                                        for lx in range(len(interface[j][c]['IpAddress'])):
                                            dic[interface1.group(0)]['IpAddress'].append(interface[j][c]['IpAddress'][lx])
                                        break
                                j += 1
                interface.append(dic)
        return interface

    def _check_bonded_interface(self, data, items, match_bond, int_name, interface, interface1, m):
        """
        Returns the bonded interface status
        :param data:
        :param items:
        :param match_bond:
        :param int_name:
        :param interface:
        :param interface1:
        :param m:
        :return:
        """
        i = self.i
        d = 0
        if m == 0:
            if 'networks' in data['connections'][i]['network']:
                for net in data['connections'][i]['network']['networks']:
                    network = dict()
                    network['ovVlanId'] = net['vlanId']
                    network['interface'] = list()
                    for item in items:
                        if str(match_bond) == str(item[0]) and \
                                str(net['vlanId']) == str((item[2])):
                            network['vlan'] = net['vlanId']
                            z = item[0] + '.' + str(network['ovVlanId'])
                            network['interface'].append(z)
                            network['interface'].append(int_name)
                            network['Broadcast'] = item[7]
                            network['Subnet'] = item[6]
                            network['Ip'] = item[5]
                        elif (str(match_bond) == str(item[0])) and \
                                (str((item[2])) == '') and \
                                ('nativeNetwork' in net):
                            if d == 1:
                                continue
                            network['vlan'] = 'untagged'
                            network['interface'].append(item[0])
                            network['interface'].append(int_name)
                            network['Broadcast'] = item[7]
                            network['Subnet'] = item[6]
                            network['Ip'] = item[5]
                            d = 1
                    interface[interface1]['IpAddress'].append(network)
            else:
                network = dict()
                network['interface'] = list()

                if data['connections'][i]['network']['ethernetNetworkType'].lower() == 'tunnel' and data['connections'][i]['functionType'] == 'Ethernet':
                    # For tunnel network..
                    for item in items:
                        if str(match_bond) == str(item[0]):
                            network1 = dict()
                            network1['interface'] = list()

                            network1['ovVlanId'] = 'Tunnel'
                            z = item[0] + '.' + item[2] if item[2] != '' else item[0]
                            network1['vlan'] = '0' if item[2] == "" else item[2]
                            network1['interface'].append(z)
                            network1['interface'].append(int_name)
                            network1['Broadcast'] = item[7]
                            network1['Subnet'] = item[6]
                            network1['Ip'] = item[5]

                            interface[interface1]['IpAddress'].append(network1)

                elif ('functionType' in data['connections'][i]) and (data['connections'][i]['functionType'] == 'Ethernet'):
                    for item in items:
                        if str(match_bond) == str(item[0]):
                            network['ovVlanId'] = data['connections'][i]['network']['vlanId']
                            network['vlan'] = 'untagged'
                            network['interface'].append(item[0])
                            network['interface'].append(int_name)
                            network['Broadcast'] = item[7]
                            network['Subnet'] = item[6]
                            network['Ip'] = item[5]

                            interface[interface1]['IpAddress'].append(network)
                else:
                    for item in items:
                        if str(match_bond) == str(item[0]):
                            network['functionType'] = data['connections'][i]['functionType']
                            network['wwnn'] = data['connections'][i]['wwnn']
                            network['wwpn'] = data['connections'][i]['wwpn']
                    interface[interface1]['IpAddress'].append(network)

            return interface
        if m == 1:
            for a in range(len(interface[interface1]['IpAddress'])):
                interface[interface1]['IpAddress'][a]['interface'].append(int_name)
            return interface

    def _check_no_bonded_interface(self, data, items, interface, interface1):
        """
        Returns True when the provided interface is not bound.
        :param data:
        :param items:
        :param interface:
        :param interface1:
        :return:
        """
        i = self.i
        d = 0
        if 'networks' in data['connections'][i]['network']:
            for net in data['connections'][i]['network']['networks']:
                network = dict()
                network['ovVlanId'] = net['vlanId']
                for item in items:
                    if (item[4].lower() == interface[interface1]['MacAddress'].lower()) and (str((item[2])) == str(net['vlanId'])):
                        network['vlan'] = net['vlanId']
                        network['interface'] = item[0] + '.' + item[2]
                        network['Broadcast'] = item[7]
                        network['Subnet'] = item[6]
                        network['Ip'] = item[5]
                    elif (item[4].lower() == interface[interface1]['MacAddress'].lower()) and (str((item[2])) == '') and ('nativeNetwork' in net):
                        if d == 1:
                            continue
                        network['vlan'] = 'untagged'
                        network['interface'] = item[0]
                        network['Broadcast'] = item[7]
                        network['Subnet'] = item[6]
                        network['Ip'] = item[5]
                        d = 1
                interface[interface1]['IpAddress'].append(network)
        else:
            network = dict()
            network['interface'] = list()
            if ('functionType' in data['connections'][i]) and (data['connections'][i]['functionType'] == 'Ethernet'):
                for item in items:
                    if item[4].lower() == interface[interface1]['MacAddress'].lower():
                        network['ovVlanId'] = data['connections'][i]['network']['vlanId']
                        network['vlan'] = 'untagged'
                        network['interface'] = item[0]
                        network['Broadcast'] = item[7]
                        network['Subnet'] = item[6]
                        network['Ip'] = item[5]
            else:
                for item in items:
                    if item[4].lower() == interface[interface1]['MacAddress'].lower():
                        network['functionType'] = data['connections'][i]['functionType']
                        network['wwnn'] = data['connections'][i]['wwnn']
                        network['wwpn'] = data['connections'][i]['wwpn']
            interface[interface1]['IpAddress'].append(network)
        return interface

    def _get_matches_from_mac_address(self, mac, blocks):
        """
        Returns the list of matched NIC MAC
        :param mac:
        :param blocks:
        :return:
        """
        mac = re.sub(r':', '-', mac)
        matches = list()
        for block in blocks:
            if ': ' + mac in block:
                matches.append(block)

        return matches

    def _get_ip_data_from_block_data(self, block):
        """
        Returns the IP information
        :param block:
        :return:
        """
        interface = dict()
        regex = r'adapter\s*([^\:]+?(?:\s*\-\s*VLAN\s*(\d+))?)\s*\:[\w\W]*?IPv4\s*Address[\w\W]*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b[\w\W]*?Subnet[\w\W]*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b[\w\W]*?Gateway[\w\W]*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))?\b'
        match = re.search(regex, block, re.I)
        if match:
            # if not match.group(3).startswith('169'):
            interface['interface'] = match.group(1)
            interface['vlan'] = '0' if match.group(2) is None else match.group(2)
            interface['Ip'] = match.group(3)
            interface['Subnet'] = match.group(4)
            interface['Gateway'] = '' if match.group(5) is None else match.group(5)

        return interface

    @staticmethod
    def _get_os_config_list(lines):
        """
        Returns the network address information for each adapter as a list
        Example of a block

        Ethernet adapter vEthernet (DockerNAT):

           Connection-specific DNS Suffix  . :
           Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
           Physical Address. . . . . . . . . : 00-15-5D-5D-18-00
           DHCP Enabled. . . . . . . . . . . : No
           Autoconfiguration Enabled . . . . : Yes
           Link-local IPv6 Address . . . . . : fe80::2134:8f0f:4a65:3875%9(Preferred)
           IPv4 Address. . . . . . . . . . . : 10.0.75.1(Preferred)
           Subnet Mask . . . . . . . . . . . : 255.255.255.0
           Default Gateway . . . . . . . . . :
           DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                               fec0:0:0:ffff::2%1
                                               fec0:0:0:ffff::3%1
           NetBIOS over Tcpip. . . . . . . . : Enabled

        Wireless LAN adapter Wi-Fi:

           Media State . . . . . . . . . . . : Media disconnected
           Connection-specific DNS Suffix  . : dlink.router
           Description . . . . . . . . . . . : Intel(R) Dual Band Wireless-AC 7265
           Physical Address. . . . . . . . . : 48-45-20-86-CB-26
           DHCP Enabled. . . . . . . . . . . : Yes
           Autoconfiguration Enabled . . . . : Yes

        :param lines: IP Config output
        :return: List
        """
        net_config = list()
        block = list()

        for line in lines.split('\n'):
            if re.match(r'^\w', line) and block:
                net_config.append('\n'.join(block))
                block = list()

            if line.strip():
                block.append(line)

        if block:
            net_config.append('\n'.join(block))

        return net_config

    def _parse_windows_adapter_raw_output(self, server_key, server_data, ipconfig):
        """
        Renders the Windows adapter information
        :param server_key:
        :param server_data:
        :param ipconfig:
        :return:
        """
        interfaces = list()
        # For general os parsing..
        if 'os:' in server_key:
            items = re.findall(r'adapter\s*([^\:]+?)(?:\s*\-\s*VLAN\s*(\d+))?\s*\:[\w\W]*?Physical\sAddress[^:]*?:\s*((?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2})[\w\W]*?IPv4\s*Address[\w\W]*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b[\w\W]*?Subnet[\w\W]*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b[\w\W]*?Gateway[^:]*?:\s*\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))?\b', ipconfig, re.I)
            for item in items:
                interface_name = item[0]
                interface_vlan = item[1]
                interface_mac = item[2]
                interface_ip = item[3]
                interface_mask = item[4]
                interface_gw = item[5]
                interface_mac = re.sub(r':', '-', interface_mac)
                tmp_list = dict()
                tmp_list['Ip'] = interface_ip
                tmp_list['Subnet'] = interface_mask
                tmp_list['Gateway'] = interface_gw
                tmp_list['vlan'] = 'untagged' if str(interface_vlan) == '' else interface_vlan

                if any(interface_name in i for i in interfaces):
                    # If interface already exists
                    for index in xrange(len(interfaces)):
                        each = interfaces[index]
                        if interface_name in each:
                            tmp_list['interface'] = interface_name if str(interface_vlan) == '' else str(interface_name + '.' + interface_vlan)
                            interfaces[index][interface_name]['IpAddress'].append(tmp_list)
                            break
                else:
                    # If interface is found in first time
                    interface_tmp = dict()
                    interface_tmp[interface_name] = dict()
                    interface_tmp[interface_name]['MacAddress'] = interface_mac
                    interface_tmp[interface_name]['IpAddress'] = list()
                    tmp_list['interface'] = interface_name if str(interface_vlan) == '' else str(interface_name + '.' + interface_vlan)
                    interface_tmp[interface_name]['IpAddress'].append(tmp_list)

                    interfaces.append(interface_tmp)

        else:
            new_connections = list()
            for index in xrange(0, len(server_data['connections'])):
                if server_data['connections'][index]['functionType'] == 'Ethernet':
                    new_connections.append(server_data['connections'][index])
            server_data['connections'] = new_connections

            # Interate each connection and identify addresses
            for each_conn in server_data['connections']:
                # Split port ID
                flex_port = re.search(r'\d:\d-\w', each_conn['portId']).group(0)
                flex = {flex_port: {'MacAddress': each_conn['mac'], 'IpAddress': []}}

                matches = self._get_matches_from_mac_address(each_conn['mac'],
                                                             self._get_os_config_list(ipconfig))
                # Not a teamed/bonded interface
                if len(matches) == 1:
                    data = self._get_ip_data_from_block_data(matches[0])

                    # Append OV VLAN ID into the dictionary data
                    if 'networks' not in each_conn['network']:  # tagged but not netset
                        data['ovVlanId'] = str(each_conn['network']['vlanId'])
                    else:   # netset assigned flex
                        for net in each_conn['network']['networks']:
                            if str(net['vlanId']) == str(data['vlan']):
                                data['ovVlanId'] = net['vlanId']
                                break
                        else:
                            data['ovVlanId'] = net['vlanId']
                    flex[flex_port]['IpAddress'].append(data)

                # Teamed/bonded interface
                elif len(matches) > 1:
                    addresses = list()
                    for match in matches:
                        data = self._get_ip_data_from_block_data(match)
                        addresses.append(data)

                    if 'ethernetNetworkType' in each_conn['network'] and each_conn['network']['ethernetNetworkType'] == 'Tunnel' and each_conn['functionType'] == 'Ethernet':
                        for index in xrange(len(addresses)):
                            net2 = addresses[index]
                            addresses[index]['ovVlanId'] = 'Tunnel'
                            flex[flex_port]['IpAddress'] = addresses
                    else:
                        for net1 in each_conn['network']['networks']:
                            ov_vlan = str(net1['vlanId'])
                            for index in xrange(len(addresses)):
                                net2 = addresses[index]
                                # try:
                                os_vlan = ''
                                if net2:
                                    os_vlan = str(net2['vlan'])
                                # except:
                                #     logger.info(matches, also_console=1)
                                #     logger.info(addresses, also_console=1)
                                #     logger.info(net1, also_console=1)
                                #     logger.info(net2, also_console=1)
                                #     exit()
                                if ov_vlan == os_vlan:
                                    addresses[index]['ovVlanId'] = ov_vlan
                                    break
                                elif os_vlan == '0' and 'nativeNetwork' in net1:    # Mapping untagged network
                                    addresses[index]['ovVlanId'] = ov_vlan
                                    break
                        flex[flex_port]['IpAddress'] = addresses

                else:
                    logger.trace("MAC Address '{mac}' not assigned to any OS interface in server '{server}', This interface might be a teamed interface".format(server=server_key, mac=each_conn['mac']))

                interfaces.append(flex)

            # Map redundant ports using physical port-1 data
            temp = dict()
            for interface in interfaces:
                temp.update(interface)

            for index in xrange(len(interfaces)):
                each_interface = interfaces[index]
                flex_port = each_interface.keys()[0]
                port_splits = re.match(r'(\d)\W(\d)\W(\w)', flex_port, re.I).groups()
                redundant_flex_port = str(port_splits[0] + ':1-' + port_splits[2]) if port_splits[1] == '2' else str(port_splits[0] + ':2-' + port_splits[2])

                if len(temp[flex_port]['IpAddress']) == 0 and len(temp[redundant_flex_port]['IpAddress']) > 0:
                    interfaces[index][flex_port]['IpAddress'] = temp[redundant_flex_port]['IpAddress']

            return interfaces

        return interfaces

    def _run_system_command(self, cmd):
        """
        Executes the command using subprocess module
        :param cmd:
        :return:
        """
        output = subprocess.check_output(cmd, shell=True)
        return output

    def _get_current_host_networks(self):
        """
        Returns the current host networks
        :return:
        """
        ipconfig = self._run_system_command(cmd='ipconfig')
        try:
            # Below regex return like => E.g. [('15.212.160.244', '255.255.252.0'), ('192.168.146.143', '255.255.248.0')]
            networks = re.findall(r'IPv4.*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b\s*Subnet\s*Mask.*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b', ipconfig, re.I)
            if len(networks) < 1:
                logger.warn("Failed to parse current host network information, and networks count < 1")
                return False
        except:
            logger.warn("Failed to parse current host network information")
            return False

        return networks

    def _find_reachable_network_from_current_test_head(self, ipv4_networks):
        """
        Return the reachable network information
        :param ipv4_networks:
        :return:
        """
        reachable_networks = list()
        my_networks = self._get_current_host_networks()

        for ipv4_nework in ipv4_networks:
            net1 = IPNetwork(ipv4_nework[0] + '/' + ipv4_nework[1])
            for my_network in my_networks:
                net2 = IPNetwork(my_network[0] + '/' + my_network[1])
                if net1 == net2:
                    reachable_networks.append(ipv4_nework)
                else:
                    continue
        count = len(reachable_networks)
        if count < 1:
            logger.warn("Failed to find reachable IPv4 network from the current test head to given input list")
            return False
        else:
            logger.trace("Found reachable network from the current host, networks are: {0}".format(reachable_networks))
            return reachable_networks

    def _find_reachable_ip_from_current_test_head(self, ipv4_ips):
        """
        Returns the reachable network information of the current system.
        :param ipv4_ips:
        :return:
        """
        reachable_ips = list()
        my_networks = self._get_current_host_networks()

        for ipv4_ip in ipv4_ips:
            ip1 = IPAddress(ipv4_ip)
            for my_network in my_networks:
                net = IPNetwork(my_network[0] + '/' + my_network[1])
                if ip1 in net:
                    reachable_ips.append(ipv4_ip)
                else:
                    continue
        count = len(reachable_ips)
        if count < 1:
            logger.warn("Failed to find reachable IPv4 IP from the current test head to given input list")
            return False
        else:
            logger.trace("Found reachable IP from the current host, IP's are: {0}".format(reachable_ips))
            return reachable_ips

    def _check_ip_reachability(self, host):
        """
        Returns True when the IP is reachable
        :param host:
        :return:
        """
        logger.trace("\n_check_ip_reachability entered..")
        try:
            logger.trace("Trying to ping: '%s'" % host)
            ping_str = "-n 2" if platform.system().lower() == "windows" else "-c 2"
            command = "ping " + ping_str + " " + host
            logger.trace(command.split())
            try:
                output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT, universal_newlines=True)
                logger.trace(output)
                if 'ttl' in output.lower():
                    return True
                else:
                    return False

            except subprocess.CalledProcessError:
                logger.trace(traceback.format_exc())
                logger.trace("Getting CalledProcessError")
                return False
        except:
            logger.trace(traceback.format_exc())
            return False
        finally:
            logger.trace("_check_ip_reachability exited..\n")

    def _run_psexec_command_accept_eula(self):
        """
        Accept the first EULA when executing PsExec
        :return:
        """
        try:
            logger.trace("_run_psexec_command_accept_eula entered..")

            psExec_Location = os.path.join(self.traffic.data['tools'], 'psExec.exe')

            cmd = '{psexec} /accepteula'.format(psexec=psExec_Location)
            logger.trace("Running : '%s'" % cmd)
            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            output = iter(process.stdout.readline, b"")
            responce = ''
            for li in output:
                responce += li

            logger.trace(responce)

            return True

        except:
            raise Exception(traceback.format_exc())

        finally:
            logger.trace("_run_psexec_command_accept_eula exited..")

    def _execute_command_using_psexec_sync(self, server_data, command, drive, name):
        """
        Run the parameter using PsExec and wait till task is completed
        :param server_data:
        :param command:
        :param drive:
        :param name:
        :return:
        """
        logger.trace("_execute_command_using_psexec_sync entered..")

        random_number = str(randint(100, 200))
        temp_file = 'tmp' + random_number + '.bat'
        out_file = 'tmp' + random_number + '.out'
        pid_file = 'tmp' + random_number + '.pid'

        working_dir = '{0}\\{1}'.format(drive, name)

        try:
            logger.trace("Executing command: '{cmd}'".format(cmd=command))

            psExec_Location = os.path.join(self.traffic.data['tools'], 'psExec.exe')

            # Create a batch file
            bat = open(temp_file, 'w')
            bat.write('@echo off\n')
            bat.write('{cmd} > {output_log}\n'.format(cmd=command, output_log=out_file))
            bat.write('echo TASK__COMPLETED >> {output_log}'.format(output_log=out_file))
            bat.close()

            # Frame psexec command..
            # E.g.
            # psexec.exe \\192.168.148.159 -u Administrator -p 12iso*help
            #            -w c:\share -d -c -f currentHostBatch.bat 2 >
            #            PID_Output.out
            _ = '{} \\\\{} '.format(psExec_Location, server_data['reachableIp'])
            _ += '-u {}'.format(server_data['osUserLoginCredentials']['user_name'])
            _ += ' -p {}'.format(server_data['osUserLoginCredentials']['password'])
            _ += ' -w {} -s -d -c '.format(working_dir)
            cmd = '{} -f {} 2>{}'.format(_, temp_file, pid_file)
            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            process.communicate()

            time.sleep(1)
            # Get file content using xcopy/robocopy
            cmd = 'XCOPY \\\\{host}\\{share_name}\\{out_file} {destination}'.format(host=server_data['reachableIp'], share_name=name, out_file=out_file, destination='.')

            content = None
            for _ in xrange(60):
                try:
                    stdout = self._run_system_command(cmd)
                    logger.trace(stdout)
                except:
                    time.sleep(1)
                    continue

                try:
                    with open(out_file, 'r') as F:
                        content = F.read()
                    os.system('del /f %s' % out_file)
                except:
                    continue

                if 'TASK__COMPLETED' in content:
                    content = re.sub(r'TASK__COMPLETED', '', content)
                    break

                time.sleep(1)
            else:
                logger.warn("Failed to get remote execution response. Command: '{}'".format(command))
                return False

            return content

        except:
            logger.debug('{}'.format(process))
            raise Exception(traceback.format_exc())

        finally:
            os.system('del /f %s' % temp_file)
            os.system('del /f %s' % out_file)
            os.system('del /f %s' % pid_file)
            logger.trace("_execute_command_using_psexec_sync exited..")

    def _execute_command_using_psexec_no_sync(self, server_data, command):
        """
        Method runs a PsEXEC command but does not wait for return status
        :param server_data:
        :param command:
        :return:
        """
        logger.trace("_execute_command_using_psexec_no_sync entered..")

        random_number = str(randint(100, 110))
        temp_file = 'tmp' + random_number + '.bat'
        out_file = 'tmp' + random_number + '.out'
        pid_file = 'tmp' + random_number + '.pid'

        try:
            logger.trace("Executing command: '{cmd}'".format(cmd=command))

            psExec_Location = os.path.join(self.traffic.data['tools'], 'psExec.exe')

            # Create a batch file
            bat = open(temp_file, 'w')
            bat.write('@echo off\n')
            bat.write('{cmd} > {output_log}\n'.format(cmd=command, output_log=out_file))
            bat.close()

            # Frame psexec command..
            # E.g.
            # psexec.exe \\192.168.148.159 -u Administrator
            #            -p 12iso*help -w c:\share -d -c
            #            -f currentHostBatch.bat 2 > PID_Output.out
            _ = '{} \\\\{} '.format(psExec_Location, server_data['reachableIp'])
            _ += '-u {}'.format(server_data['osUserLoginCredentials']['user_name'])
            _ += ' -p {}'.format(server_data['osUserLoginCredentials']['password'])
            cmd = '{} -s -d -c -f {} 2>{}'.format(_, temp_file, pid_file)

            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            process.communicate()

            for _ in xrange(30):
                time.sleep(2)
                with open(pid_file, 'r') as AA:
                    response = AA.read()

                    if response.find('process ID') >= 0:
                        break

                    elif response.find('user name or password is incorrect') >= 0:
                        raise Exception("The user name or password is incorrect for reachableIp: {res}".format(res=server_data['reachableIp']))

                    elif response.find('could not start') >= 0:
                        raise Exception("psExec failed to run and returned below: \n{res}".format(res=response))

            return response

        except:
            raise Exception(traceback.format_exc())

        finally:
            os.system('del /f %s' % temp_file)
            os.system('del /f %s' % pid_file)
            logger.trace("_execute_command_using_psexec_no_sync exited..")

    def get_all_host_os_interface_configurations(self):
        """
        Retrieves all host information
        :return:
        """
        try:
            logger.trace("get_all_host_os_interface_configurations entered")

            # self.traffic.data = abc

            # Adding current host key in server list
            self.traffic.data['serversAndCredentials']['CURRENT_HOST'] = dict()

            for server_key, server_data in self.traffic.data['serversAndCredentials'].iteritems():

                current_platform = "windows" if platform.system().lower() == "windows" else "linux"
                if current_platform == 'linux' and 'platform' in server_data and server_data['platform'].lower() == 'windows':
                    logger.error("Implementation required - If current platform is 'linux' then for Windows traget, traffic generation wont work. Try using windows as a current platform Or remove Windows entities")
                    raise Exception("Windows traget from linux environment not supported")

                # Check input host/vm OS is within LE or general type
                if 'os:' in server_key:
                    logger.trace("Server key '{}' not with the pattern le:<le-name>/encl:<encl-number>/bay:<bay-number>; General traffic implementation choosen".format(server_key))
                elif 'current_host' in server_key.lower():
                    continue
                elif 'iLO' not in server_data:
                    logger.error("Server: '{}' not having iLO information in OV, Please check input and particularly make sure LE name is proper".format(server_key))
                    continue

                logger.trace('=' * 100)
                logger.info("=>>Getting information for server: '{0}'".format(server_key), also_console=1)

                if 'reachableIp' in self.traffic.data['serversAndCredentials'][server_key] and 'interfaces' in self.traffic.data['serversAndCredentials'][server_key]:
                    logger.trace("Server '{}' data already been collected".format(server_key))
                    # Removing 'commands', 'statistics'from the global dict. To avoid future run conflicts
                    if 'commands' in self.traffic.data['serversAndCredentials'][server_key]:
                        self.traffic.data['serversAndCredentials'][server_key].pop('commands')
                    if 'statistics' in self.traffic.data['serversAndCredentials'][server_key]:
                        self.traffic.data['serversAndCredentials'][server_key].pop('statistics')
                    continue

                if 'reachableIp' in self.traffic.data['serversAndCredentials'][server_key]:
                    test_ip = self.traffic.data['serversAndCredentials'][server_key]['reachableIp']
                    if not self._check_ip_reachability(test_ip):
                        logger.error("Server: {server} => Failed to reach given reachable IP '{ip}'".format(server=server_key, ip=test_ip))
                        raise Exception("Server: {server} => Failed to reach given reachable IP '{ip}'".format(server=server_key, ip=test_ip))

                # If 'reachableIp' & 'platform' key given as input then skip iLO VSP calls
                ip_address_output = ''
                if 'reachableIp' not in server_data and 'platform' not in server_data:

                    logger.trace("Server not having reachableIp and platform in input data, trying to collect it from VSP console")
                    if 'iLOUserLoginCredentials' not in server_data:
                        logger.error("'reachableIp' & 'platform' not given in server block; keyword expecting atleast 'iLOUserLoginCredentials' key value to get OS interface configuration through VSP console")
                        raise Exception("'reachableIp' & 'platform' not given in server block; keyword expecting atleast 'iLOUserLoginCredentials' key value to get OS interface configuration through VSP console")

                    handle, type_of_platform = self.login_to_ilo_vsp_console_get_handle_and_platform(ilo_ip=server_data['iLO']['IPv4'], ilo_cred=server_data['iLOUserLoginCredentials'])
                    self.traffic.data['serversAndCredentials'][server_key]['platform'] = type_of_platform

                    if 'windows' in server_data['platform'].lower():

                        sac_interface_output = self._login_to_sac_console_get_sac_os_interface_output(chan=handle)
                        logger.trace(sac_interface_output)

                        # Extract IPv4 from the sac interface output
                        try:
                            # Below regex return like => E.g. [('15.212.160.244', '255.255.252.0'), ('192.168.146.143', '255.255.248.0')]
                            networks = re.findall(r'Ip=\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b\s*Subnet=\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b', sac_interface_output, re.I)
                            if len(networks) != 0:
                                logger.trace("Parsed IPv4 from SAC interface output")
                            else:
                                logger.warn("SAC interface not having any IPv4. Seems IPv4 not configured in OS or library failed to parse IPv4 values from SAC output")
                                continue
                        except:
                            logger.warn("Failed to parse IPv4 from SAC interface output")
                            continue

                        # Find rechable IP from current test head host
                        response = self._find_reachable_network_from_current_test_head(ipv4_networks=networks)
                        if response is False:
                            logger.warn("Server '{0}' needs to have reachable IP configured from the test head/current host".format(server_key))
                            continue

                        # Check reachable IP is pinging from current test head
                        # response has : <type 'list'>: [('192.168.148.159', '255.255.248.0')]
                        for reachableIp in response:
                            if self._check_ip_reachability(reachableIp[0]):
                                self.traffic.data['serversAndCredentials'][server_key]['reachableIp'] = reachableIp[0]
                                break
                        else:
                            test_name = BuiltIn().get_variable_value("${TEST_NAME}")
                            logger.warn("Test case: '{1}': Found reachable network IP's '{0}', But not reachable from current test head, please check IP reachability".format(str(response), test_name))

                    elif 'linux' in server_data['platform'].lower():
                        ip_address_output = self._login_to_os_serial_console_get_ip_address_output(handle, server_data['osUserLoginCredentials'])
                        logger.trace(ip_address_output)

                    # Once job with the server completed closing session
                    self.logout_ilo_vsp_console(handle)

                elif 'platform' in server_data and 'linux' in server_data['platform'].lower():
                    # reachableIp given, trying to collect it by taking SSH call to the server
                    # Connecting to host using its reachable IP

                    ssh = self._connect_using_ssh(machine_ip=server_data['reachableIp'], username=server_data['osUserLoginCredentials']['user_name'], password=server_data['osUserLoginCredentials']['password'])

                    # Collect 'ip address show' stdout from OS
                    ip_address_output = self._execute_linux_command(ssh, '/sbin/ip address show', stdout_log=True)
                    logger.trace(ip_address_output)

                    # Disconnect SSH session
                    ssh.close()

                if 'platform' in server_data and 'windows' in server_data['platform'].lower():
                    # Create folder for collecting logs/stdout from host OS,. C:\TrafficExecutorLogs. If folder exists remove and recreate..
                    folder_drive = 'C:'
                    folder_name = 'TrafficExecutorLogs'
                    folder_path = '{drive}\\{log_folder_name}'.format(log_folder_name=folder_name, drive=folder_drive)
                    if os.path.exists(folder_path):
                        os.system("RMDIR /S /Q " + folder_path)
                        os.system('MKDIR ' + folder_path)
                    else:
                        os.system('MKDIR ' + folder_path)

                    # Collect 'ipconfig /all' output from OS using psExec

                    # Accept psExec EULA
                    self._run_psexec_command_accept_eula()

                    # Before doing anything create folder share to use it for log redirect and other process
                    # Create renote folder
                    command = 'RMDIR /S /Q {path} & MKDIR {path}'.format(path=folder_path)
                    response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

                    # Share remote folder
                    command = 'NET SHARE {share_name}={share_path} /GRANT:Everyone,FULL'.format(share_name=folder_name, share_path=folder_path)
                    response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

                    # Run ipconfig in remote and retrive its stdout
                    # Note: Once share has been created in remote windows machine, its recommended to use _execute_command_using_psexec_sync()
                    command = 'ipconfig /all'
                    ipconfig_output = self._execute_command_using_psexec_sync(server_data=server_data, command=command, drive=folder_drive, name=folder_name)
                    logger.trace(ipconfig_output)

                    # Parse ipconfig output and create summarized disctionary
                    interfaces = self._parse_windows_adapter_raw_output(server_key, server_data, ipconfig_output)
                    logger.trace(json.dumps(interfaces, indent=4))

                    self.traffic.data['serversAndCredentials'][server_key]['interfaces'] = interfaces

                elif 'platform' in server_data and 'linux' in server_data['platform'].lower():

                    # Parse 'ip address show' command output..
                    interfaces = self._parse_linux_adapter_raw_output(server_key, ip_address_output)
                    self.traffic.data['serversAndCredentials'][server_key]['interfaces'] = interfaces

                    if 'reachableIp' not in server_data:
                        # Find reachable IP from current test host
                        ips = dict()
                        for ip in re.findall(r'\'Ip\'\s*\:\s*u?\'\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b\'', str(interfaces), re.I):
                            ips[ip] = ip
                        response = self._find_reachable_ip_from_current_test_head(ips)
                        if response is False:
                            logger.warn("Server '{0}' needs to have reachable IP configured from the test head/current host".format(server_key))
                            continue

                        # Check reachable IP is pinging from current test head
                        for reachableIp in response:
                            if self._check_ip_reachability(reachableIp):
                                self.traffic.data['serversAndCredentials'][server_key]['reachableIp'] = reachableIp
                                break
                        else:
                            logger.warn("Found reachable network IP's({0}) are not pinging from current test head network, please check".format(str(response)))

                    else:
                        logger.trace("'reachableIp' & 'platform' key exists in global dictionary")

                else:
                    raise Exception("Unsupported OS !!")

        except:
            BuiltIn().fail(traceback.format_exc())

        finally:
            logger.trace("get_all_host_os_interface_configurations exited")
