import os
import re
import sys
import pdb
import traceback
import paramiko
import time
import json
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class VspLibrary(object):

    def __init__(self, traffic_data):
        self.traffic = traffic_data
        self.ansi_escape = re.compile(r'\x1b[^m]*m')
        self.ssh = None

    def _ansi_escape(self, string):
        return self.ansi_escape.sub('', string)

    def _send_and_receive(self, channel, send, expect, timeout=30):
        if channel.send_ready():
            channel.send(send)
        else:
            logger.console('Send is not ready')
            return False

        buff = ''
        start_time = time.time()
        while not buff.endswith(expect):
            if channel.recv_ready():
                resp = channel.recv(9999)
                resp = self._ansi_escape(resp)
                # resp = re.sub(r'\x1b\[(?:K|\d*;\d*H)?', "\n", resp)
                buff += resp
                logger.info(resp, also_console=True)

            if (time.time() - start_time) > timeout:
                logger.console('Timed out..' + buff)
                return False
        return buff

    def _exec_command(self, channel, send, timeout=1):

        if channel.send_ready():
            channel.send(send)
        else:
            logger.console('Send is not ready')
            return False

        buff = ''
        start_time = time.time()
        while (time.time() - start_time) < timeout:
            if channel.recv_ready():
                resp = channel.recv(9999)
                resp = self._ansi_escape(resp)
                logger.info(resp, also_console=True)
                buff += resp
                time.sleep(0.5)

        return buff

    def login_to_ilo_vsp_console(self, ilo_ip, ilo_cred, os_cred):

        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ov_ip = self.traffic.data['fusion']['ip']
            user_name = self.traffic.data['fusion']['cliCredentials']['userName']
            password = self.traffic.data['fusion']['cliCredentials']['password']
#            ov_ip = '192.168.148.98'
#            userName = 'root'
#            password = '12iso*help'
#            ov_ip = '16.114.211.88'
#            userName = 'root'
#            password = 'hpvse1'
            self.ssh.connect(hostname=ov_ip, username=user_name, password=password)
            chan = self.ssh.invoke_shell()

            # Ssh and wait for the password prompt.
            out = self._exec_command(chan, '\r\r')
            time.sleep(2)
            to_send = 'ssh {USER}@{IP}\r'.format(USER=ilo_cred['user_name'], IP=ilo_ip)
            out = self._exec_command(chan, to_send, timeout=5)
            if out.endswith('# '):
                pass
            else:
                if out.endswith('(yes/no)? '):
                    self._send_and_receive(chan, 'yes\r', 'password: ')

                self._send_and_receive(chan, ilo_cred['password'] + '\r', 'hpiLO-> ')

            self._send_and_receive(chan, 'stop /system1/oemhp_VSP1\r', 'hpiLO-> ')

            out = self._exec_command(chan, 'VSP\r', timeout=5)
            out = self._exec_command(chan, '\r')

            if out.endswith('login: '):     # RHEL7.3
                self._send_and_receive(chan, os_cred['userName'] + '\r', 'Password: ')
                time.sleep(1)
                self._send_and_receive(chan, os_cred['password'] + '\r', '# ')
                time.sleep(1)

            out = self._send_and_receive(chan, '\r', '# ')
            if out.endswith('# '):
                logger.info("Login successful !!", also_console=True)
                return chan
            else:
                raise AssertionError("Failed to connect VSP console, Please check VSP console is enabled properlly in server hardware")

        except:
            logger.debug(traceback.format_exc())
            raise AssertionError("login_to_ilo_vsp_console failed")

    def logout_ilo_vsp_console(self, handle):
        try:
            self._exec_command(handle, 'exit\r', timeout=3)
            self._exec_command(handle, '\x1b(\r')
            self._exec_command(handle, 'exit\r')
            self._exec_command(handle, 'exit\r')
        except:
            logger.debug(traceback.format_exc())
            raise AssertionError("Failed to logout iLO")

    def _get_from_nic_list(self, nic_list, mac_id, vlan_id):
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

    def _parse_adapter_raw_output(self, source_server, ip_address_output):

        connections = self.traffic.data['serversAndCredentials'][source_server]['connections']
        interfaces = dict()

        items = re.findall(r'\d+\:\s([\-\w]+)(?:\.(\d+)@\w+)?\:\s[\w\W]*?link\/[\s\w]+((?:\w{2}\:){5}\w{2})\sbrd\s(?:\w{2}\:){5}\w{2}(?:\s*inet\s((?:\d{1,3}\.){3}\d{1,3})\/(\d{1,2})\sbrd\s((?:\d{1,3}\.){3}\d{1,3}))?', ip_address_output, re.I)
        if not items:
            raise AssertionError("Error while parsing raw 'ip address show' output")

        nic_details = list()
        for item in items:
            logger.info(item)

            if re.search(r'lo|virb', item[0], re.I):
                continue

            temp = dict()
            temp['vlan'] = item[1]
            if temp['vlan'] != '':
                temp['interface'] = item[0] + '.' + item[1]
            else:
                temp['interface'] = item[0]
            temp['mac'] = item[2]
            temp['ip'] = item[3]
            temp['subnet'] = item[4]
            temp['broadcast'] = item[5]

            nic_details.append(temp)

        for conn in connections:
            if 'portId' in conn:
                port = conn['portId'].replace('Mezz ', '')
                interfaces[port] = dict()
                interfaces[port]['macAddress'] = conn['mac']

                network_addresses = list()
                if 'networks' in conn['network']:
                    for net in conn['network']['networks']:
                        network = dict()
                        network['ovVlanId'] = net['vlanId']
                        nic_info = self._get_from_nic_list(nic_details, mac_id=conn['mac'], vlan_id=net['vlanId'])
                        network.update(nic_info)
                        network_addresses.append(network)
                else:
                    network = dict()
                    if 'functionType' in conn and conn['functionType'] == 'Ethernet':
                        network['ovVlanId'] = conn['network']['vlanId']
                        nic_info = self._get_from_nic_list(nic_details, mac_id=conn['mac'], vlan_id=conn['network']['vlanId'])
                        network.update(nic_info)
                        network_addresses.append(network)
                    else:
                        network['functionType'] = conn['functionType']
                        network['wwnn'] = conn['wwnn']
                        network['wwpn'] = conn['wwpn']
                        network_addresses.append(network)

                interfaces[port]['ipAddress'] = network_addresses

        self.traffic.data['serversAndCredentials'][source_server]['interfaces'] = interfaces
        # logger.info(json.dumps(interfaces, indent=4, separators=(',', ': ')))

    def get_all_server_interface_through_ilo_vsp_console(self):
        try:
            logger.debug("get_all_server_interface_through_ilo_vsp_console entered")
            for server, data in self.traffic.data['serversAndCredentials'].iteritems():
                if 'iLO' not in data:
                    raise AssertionError("Server: '{}' not having iLO information, Please check".format(server))

                logger.info("Getting information for server: '{0}' & its iLO: '{1}'".format(server, data['iLO']), also_console=True)
                handle = self.login_to_ilo_vsp_console(ilo_ip=data['iLO']['IPv4'], ilo_cred=data['iLOUserLoginCredentials'], os_cred=data['osUserLoginCredentials'])
                ip_address_output = self._send_and_receive(handle, 'ip address show\r', '# ')
                ifconfig = self._send_and_receive(handle, 'ifconfig\r', '# ')

                self._parse_adapter_raw_output(server, ip_address_output)
                # logger.info(json.dumps(self.traffic.data['serversAndCredentials'], indent=4, separators=(',', ': ')), also_console=True)

                self.logout_ilo_vsp_console(handle)

        except:
            BuiltIn().fail(traceback.format_exc())

        finally:
            logger.debug("get_all_server_interface_through_ilo_vsp_console exited")
