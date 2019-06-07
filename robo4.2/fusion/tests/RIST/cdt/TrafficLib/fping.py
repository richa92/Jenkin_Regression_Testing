import os
import re
import json
import time
import glob
import shutil
import tempfile
import datetime
import platform
import paramiko
import traceback
import collections
from random import randint
import subprocess
from robot.api import logger
from netaddr import IPNetwork, IPAddress
from robot.libraries.BuiltIn import BuiltIn


class FpingLibrary(object):

    def __init__(self, traffic_data):
        self.traffic = traffic_data
        self.fping_rpm = 'fping-3.10-4.el7.x86_64.rpm'
        self.fping_exe = 'Fping.exe'
        self.psExec = 'psExec.exe'

    def _install_fping_in_host_os(self, platform, reachable_ip, binary_location, cred=None):
        ''''''
        try:
            logger.trace("_install_fping_in_host_os entered")

            if platform.lower() == 'windows':
                cmd = 'XCOPY /F /S /Y {local} \\\\{host}\\{share_name}\\*'.format(host=reachable_ip,
                                                                                  share_name='TrafficExecutorLogs',
                                                                                  local=binary_location)
                self._execute_system_command(cmd)

            elif platform.lower() == 'linux':

                rpm = os.path.basename(binary_location)
                # Connecting to host using its reachable IP
                ssh = self._connect_using_ssh(machine_ip=reachable_ip, username=cred['user'], password=cred['passwd'])

                logger.trace("Verifying fping is installed")
                a, b, c = ssh.exec_command('fping -v')
                stdout = b.read()
                stderr = c.read()
                logger.trace(stdout)
                logger.trace(stderr)

                if 'command not found' in stderr or 'command not found' in stdout:
                    pass
                else:
                    logger.trace("Fping installed successfully in host OS")
                    ssh.close()
                    return True

                sftp = ssh.open_sftp()

                logger.trace("Uploading fping rpm")
                sftp.put(binary_location, rpm)

                logger.trace("Installing fping rpm")
                ssh.exec_command('rpm --force -ivh {}'.format(rpm))
                time.sleep(2)

                logger.trace("Verifying fping is installed")
                a, b, c = ssh.exec_command('fping -v')
                stdout = b.read()
                stderr = c.read()
                logger.trace(stdout)
                logger.trace(stderr)

                ssh.close()

                if 'No such file' in stderr or 'command not found' in stderr:
                    logger.error("Failed to install fping in host OS, please check")
                    BuiltIn().fail("Failed to install fping in host OS, please check")
                else:
                    logger.trace("Fping installed successfully in host OS")

            else:
                pass

        finally:
            logger.trace("_install_fping_in_host_os exited")

    def _get_input_server_data_from_source_name(self, source):
        server_location = None
        # For 'source': 'le:LE1/encl:2/bay:1/port:1:1-a'
        p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', source, re.I)
        if p:
            if p.group(1):
                server_location = 'le:{le}/encl:{encl}/bay:{bay}'.format(le=p.group(1), encl=p.group(2), bay=p.group(3))
            else:
                server_location = 'encl:{encl}/bay:{bay}'.format(encl=p.group(2), bay=p.group(3))

        # For 'source': 'os:vm1/os_port:bond0'
        p = re.match(r'^os:([\w\W]+)?/(?:os(?:_|-)?)?(?:port|int|interface):[\w\W]+?$', source, re.I)
        if p:
            server_location = 'os:{unique_identity_of_os}'.format(unique_identity_of_os=p.group(1))

        logger.trace("Processing server : '{}'".format(server_location))

        if server_location and server_location in self.traffic.data['serversAndCredentials']:
            return self.traffic.data['serversAndCredentials'][server_location]
        else:
            BuiltIn().fail(msg="Input/Config error: Server config not available, please check entity '{}'".format(server_location))

    def _get_interface_port_data(self, source, port):

        server_data = self._get_input_server_data_from_source_name(source)

        if 'interfaces' not in server_data:
            raise AssertionError("Input data error: No interfaces avail, please check source '{}'".format(source))

        for port_block in server_data['interfaces']:
            if port in port_block:
                return port_block[port]

        return False

    def _get_ip_address_from_interface_port_block(self, port_block, vlan_list, entity_index):

        test_name = BuiltIn().get_variable_value("${TEST_NAME}")

        if 'IpAddress' not in port_block:
            raise AssertionError('Input data error: please check')

        ips = list()

        vlan_list = [str(vlan).lower() for vlan in vlan_list]

        for each_vlan_ip in port_block['IpAddress']:

            if 'vlan' in each_vlan_ip and str(each_vlan_ip['vlan']).lower() == 'untagged':
                each_vlan_ip['vlan'] = '0'

            # If VLAN filter exists then take matched values alone
            if 'ovVlanId' in each_vlan_ip and str(each_vlan_ip['ovVlanId']).lower() in vlan_list:
                if 'Ip' in each_vlan_ip:
                    ips.append(each_vlan_ip['Ip'])
                else:
                    logger.warn("Test case '{name}': Please check input data - Target OS not having configuration for VLAN ID: '{id}' and check entity index: '{index}' and VLAN list: '{vlan_list}'".format(id=str(each_vlan_ip['ovVlanId']), index=entity_index, vlan_list=vlan_list, name=test_name))

            elif 'vlan' in each_vlan_ip and str(each_vlan_ip['vlan']).lower() in vlan_list:
                if 'Ip' in each_vlan_ip:
                    ips.append(each_vlan_ip['Ip'])
                else:
                    logger.warn("Test case '{name}': Please check input data - Target OS not having configuration for VLAN ID: '{id}' and check entity index: '{index}' and VLAN list: '{vlan_list}'".format(id=str(each_vlan_ip['vlan']), index=entity_index, vlan_list=vlan_list, name=test_name))

            elif not vlan_list:
                # If no vlan key in input then take all IP's belongs to the particular flex port
                if 'Ip' in each_vlan_ip:
                    ips.append(each_vlan_ip['Ip'])
            else:
                continue

        return ips

    def _get_server_key_from_entity_source_name(self, entity_source):
        server_key = None
        p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', entity_source, re.I)
        if p:
            if p.group(1):
                server_key = 'le:{le}/encl:{encl}/bay:{bay}'.format(le=p.group(1), encl=p.group(2), bay=p.group(3))
            else:
                server_key = 'encl:{encl}/bay:{bay}'.format(encl=p.group(2), bay=p.group(3))

        p = re.match(r'^os:([\w\W]+)?/(?:os(?:_|-)?)?(?:port|int|interface):[\w\W]+?$', entity_source, re.I)
        if p:
            server_key = 'os:{unique_identity_of_os}'.format(unique_identity_of_os=p.group(1))

        if server_key:
            return server_key
        else:
            logger.warn("Input format is wrong, please check entity '{}'".format(entity_source))
            return False

    def _execute_system_command(self, command):
        logger.trace("_execute_system_command entered..")
        try:
            logger.trace("Executing: '%s'" % command)
            output = ''
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = iter(proc.stdout.readline, b"")
            for i in out:
                output += i
            logger.trace(output)
            # return True
            return output

        except:
            raise Exception(traceback.format_exc())

        finally:
            logger.trace("_execute_system_command exited..")

    def _run_ping_with_windows(self, command, target_ip, output_file):
        logger.trace("_run_ping_with_windows entered..")
        try:

            ping_option1 = '|cmd /q /v /c "(pause&pause)>nul & for /l %%a in () do (set /p "data=" && echo(!date! !time! !data!)&ping -n 2 '
            ping_option2 = '>nul"'
            ping_str = command + ping_option1 + target_ip + ping_option2

            batch_file_name = target_ip + '.bat'
            file_path = 'C:\\'
            batch_file_path = os.path.join(file_path, batch_file_name)
            out_file_path = os.path.join(file_path, output_file)

            batch_file_str = ping_str + " > " + out_file_path

            f = open(batch_file_path, "w")
            f.write(batch_file_str)
            f.close()

            logger.trace("####### Running : '%s'" % command)

            process = subprocess.Popen(batch_file_path, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            pid = process.pid

            return pid

        except:
            raise Exception(traceback.format_exc())

        finally:
            logger.trace("_run_ping_with_windows exited..")

    def _apply_stream_options(self, platform, stream, destination_ip, log_name, source_ip=None, executable_location=None):
        ''''''
        cmd = None

        # Default interval time is 100ms
        interval = int(stream['interval']) if 'interval' in stream else 100

        if platform.lower() == 'windows':

            if executable_location:
                cmd = '{exe_loc} {ip} -c -D -T -c -t {interval} -w {interval} > {log}'.format(ip=destination_ip, log=log_name, interval=interval, exe_loc=executable_location)
            else:
                cmd = '.\\fping {ip} -c -D -T -c -t {interval} -w {interval} > {log}'.format(ip=destination_ip, log=log_name, interval=interval)

            cmd = '''powershell -Command "& {}"'''.format(cmd)

        elif platform.lower() == 'linux':

            # Based on stream options, form command
            if source_ip:
                cmd = 'fping -S {source_interface} {ip} -l -i {interval} -p {interval} -D'.format(ip=destination_ip, source_interface=source_ip, interval=interval)
            else:
                cmd = 'fping {ip} -l -i {interval} -p {interval} -D'.format(ip=destination_ip, interval=interval)

            # Adding timestamp option
            # cmd = cmd + " | xargs -L 1 -I '{}' date '+%Y-%m-%d %H:%M:%S.%3N: {}'"

            # Format command to run as background job E.g. 'nohup ping -i 0.1 localhost | xargs -L 1 -I '{}' date '+%Y-%m-%d %H:%M:%S: {}' > fileName.txt &'
            # E.g. log_name = TrafficAutomation_fping_x.x.x.x_xxxxxxxx.txt

            cmd = 'nohup {cmd} 2>&1 > {log} &'.format(cmd=cmd, log=log_name)

        else:
            raise AssertionError("Unsupported platform, please check server data input")

        return cmd

    def _find_source_interface_ip_from_server_block(self, ip, flex_port, ip_block, vlan_list=list()):
        ''''''
        flex_block = None

        # Grep matching flex_port values
        for each_flex_block in ip_block:
            if flex_port in each_flex_block:
                flex_block = each_flex_block[flex_port]
                break
        else:
            logger.warn("Source interface IP's are not available for flex nic : '{}'".format(flex_port))

        vlan_list = [str(vlan).lower() for vlan in vlan_list]

        # Compare with network and find IP belongs to which network and if matched return its IP
        matched_ip = None
        matched_vlan = None
        ip_object = IPAddress(ip)
        for sub_interface in flex_block['IpAddress']:
            if 'Ip' not in sub_interface or 'Subnet' not in sub_interface:
                continue

            if sub_interface['Ip'] == "":
                continue

            net_ip = sub_interface['Ip']
            net_mask = sub_interface['Subnet']

            if 'ovVlanId' in sub_interface:
                if sub_interface['ovVlanId'] == 'Tunnel':
                    vlan = sub_interface['vlan']
                else:
                    vlan = sub_interface['ovVlanId']
            elif 'ovVlanId' in sub_interface:
                vlan = sub_interface['ovVlanId']
            else:
                vlan = '0'

            net_object = IPNetwork(net_ip + '/' + net_mask)

            if ip_object in net_object:
                # If VLAN given in input then needs to validate it
                if len(vlan_list) > 0 and str(vlan) in vlan_list:
                    matched_ip = net_ip
                    matched_vlan = str(vlan)
                else:
                    matched_ip = net_ip
                break
        else:
            logger.trace("Source interface not found for '{ip}' & its VLAN '{vlan_list}'".format(ip=ip, vlan_list=str(vlan_list)))

        return matched_ip, matched_vlan

    def _get_current_host_networks(self):
        ''''''
        ipconfig = self._execute_system_command(command='ipconfig')
        try:
            # Below regex return like => E.g. [('15.212.160.244', '255.255.252.0'), ('192.168.146.143', '255.255.248.0')]
            networks = re.findall(
                r'IPv4.*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b\s*Subnet\s*Mask.*?\b((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b',
                ipconfig, re.I)
            if len(networks) < 1:
                logger.warn("Failed to parse current host network information, and networks count < 1")
                return False
        except:
            logger.warn("Failed to parse current host network information")
            return False

        return networks

    def _find_reachable_source_interface_ip_from_current_test_head(self, ipv4_ips):
        ''''''

        if not isinstance(ipv4_ips, type(list())):
            ipv4_ips = [ipv4_ips]

        reachable_ips = list()
        my_networks = self._get_current_host_networks()

        for ipv4_ip in ipv4_ips:
            ip1 = IPAddress(ipv4_ip)
            for my_network in my_networks:
                net = IPNetwork(my_network[0] + '/' + my_network[1])
                if ip1 in net:
                    reachable_ips.append(my_network[0])
                else:
                    continue
        count = len(reachable_ips)
        if count < 1:
            logger.trace("Failed to find reachable IPv4 IP from the current test head to given input list")
            return False
        else:
            logger.trace("Found reachable IP from the current host, IP's are: {0}".format(reachable_ips))
            return reachable_ips

    def generate_commands_to_execute(self):
        try:
            logger.trace("generate_commands_to_execute entered")

            test_name = BuiltIn().get_variable_value("${TEST_NAME}")

            # From entity block removing all commands key, Bcz every run requires new command generation
            for index in xrange(len(self.traffic.data['entities'])):
                if 'commands' in self.traffic.data['entities'][index]:
                    self.traffic.data['entities'][index].pop('commands')
                if 'statistics' in self.traffic.data['entities'][index]:
                    self.traffic.data['entities'][index].pop('statistics')

            current_platform = "windows" if platform.system().lower() == "windows" else "linux"

            # In localhost redirect output into c:\TrafficExecutorTestHeadLogs
            folder_path = '{drive}\\{log_folder_name}'.format(log_folder_name='TrafficExecutorTestHeadLogs', drive='C:')
            try:
                if os.path.exists(folder_path):
                    os.system("RMDIR /S /Q " + folder_path)
                    os.system('MKDIR ' + folder_path)
                else:
                    os.system('MKDIR ' + folder_path)
            except:
                pass

            for index in xrange(len(self.traffic.data['entities'])):

                entity = self.traffic.data['entities'][index]
                if entity['profile']['trafficgen'].strip().lower() != 'fping':
                    continue

                commands = list()

                logger.trace("Processing server interface : '{}'".format(entity['source']))

                # If target is flex port then vlan is required
                if 'vlan' not in entity:
                    logger.warn("Test case '{name}': Entity index '{index}' not having vlan key to filter flex port "
                                "networks. Session will get generated for all configured networks without filtering "
                                "VLAN".format(index=index, name=test_name))
                    entity['vlan'] = []

                # Check if entity source is an test head to target ping
                try:
                    current_host = re.match(r'^\s*(CURRENT(?:_|-)?HOST|TEST(?:_|-)?HEAD)\s*$', entity['source'], re.I)
                except:
                    current_host = None

                general_fping = True if 'os:' in entity['source'] else False

                # If source is not a test head OR current host
                if not current_host:
                    server_key = self._get_server_key_from_entity_source_name(entity['source'])

                    if 'commands' not in self.traffic.data['serversAndCredentials'][server_key]:
                        self.traffic.data['serversAndCredentials'][server_key]['commands'] = list()

                    if server_key not in self.traffic.data['serversAndCredentials']:
                        logger.error("Test case '{name}': Please check input data - Server source mentioned in entity index '{index}' is wrong".format(index=index, name=test_name))
                        raise Exception("Test case '{name}': Please check input data - Server source mentioned in entity index '{index}' is wrong".format(index=index, name=test_name))

                    # Get source server data's from global dictionary
                    source_server = self._get_input_server_data_from_source_name(source=entity['source'])

                    # For general_fping flex_port not supported, OS interface pattern. E.g. 'source': 'os:vm1/os_port:bond0'
                    if general_fping:
                        p = re.match(r'^.+?(?:os(?:_|-)?)?(?:port|int|interface):\s*([\w\s]+)?\s*$', entity['source'], re.I)
                        if not p:
                            BuiltIn().fail(
                                msg="Wrong entity input, please check entity value '{}'".format(entity['source']))
                        source_flex_port = p.group(1)
                    else:
                        p = re.match(r'^.+?port:\s*([1-9a-z:-]+)?\s*$', entity['source'], re.I)
                        if not p:
                            BuiltIn().fail(
                                msg="Wrong entity input, please check entity value '{}'".format(entity['source']))
                        source_flex_port = p.group(1)
                # If source is a test-head to target
                else:
                    logger.trace("Entity index '{index}' type is from current-host/test-head to target ping")

                    if 'commands' not in self.traffic.data['serversAndCredentials']['CURRENT_HOST']:
                        self.traffic.data['serversAndCredentials']['CURRENT_HOST']['commands'] = list()

                if 'description' not in entity:
                    entity['description'] = ''

                # For each target generate a command
                for target in entity['destination']:
                    if re.match(
                            r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
                            target):
                        # Target is an IPv4
                        log_name = 'TrafficAutomation_fping_' + target + '_' + str(int(time.time())) + str(
                            randint(1001, 1100)) + '.txt'

                        # If target is IP and entity source is CURRENT_HOST then
                        if current_host:
                            log_name = os.path.join(folder_path, log_name)
                            executable_location = os.path.join(folder_path, 'Fping.exe')
                            cmd = self._apply_stream_options(platform=current_platform, stream=entity['profile'],
                                                             source_ip=None, destination_ip=target, log_name=log_name, executable_location=executable_location)

                        else:
                            source_ip, source_vlan = self._find_source_interface_ip_from_server_block(ip=target,
                                                                                                      flex_port=source_flex_port,
                                                                                                      ip_block=source_server[
                                                                                                          'interfaces'], vlan_list=entity['vlan'])

                            if not source_ip:
                                logger.warn(
                                    "Test case '{name}': Config/Input error - Source interface/IP not available for "
                                    "target: '{target}',  Entity Index: '{index}', Entity Source: '{source}' & its "
                                    "VLAN: {vlan}".format(
                                        index=index, source=entity['source'], target=target, vlan=entity['vlan'],
                                        name=test_name))
                                continue

                            if not source_vlan:
                                if 'vlan' in entity and len(entity['vlan']) == 1:
                                    source_vlan = entity['vlan'][0]
                                elif 'vlan' in entity and len(entity['vlan']) > 1:
                                    source_vlan = 'Too many to display'

                            cmd = self._apply_stream_options(platform=source_server['platform'],
                                                             stream=entity['profile'], source_ip=source_ip,
                                                             destination_ip=target, log_name=log_name)

                        logger.trace(cmd)

                        commands.append(
                            {'entity_id': index, 'source': entity['source'], 'target': target, 'command': cmd,
                             'log_name': log_name, 'trafficgen': entity['profile']['trafficgen'].strip().lower(),
                             'target_ipv4': target, 'vlan': source_vlan, 'description': source_vlan, 'description': entity['description']})

                    else:

                        # Else entity target is a flex port patten OR general os pattern, e.g. le:LE1/encl:1/bay:11/port:1:1-a

                        destination_flex_port = None
                        p = re.match(r'^.+?(?:os(?:_|-)?)?(?:port|int|interface):\s*([\w\s]+)?\s*$', target, re.I)
                        q = re.match(r'^.+?port:\s*([1-9a-z:-]+)?\s*$', target, re.I)
                        if p:
                            destination_flex_port = p.group(1)
                        elif q:
                            destination_flex_port = q.group(1)
                        else:
                            BuiltIn().fail(msg="Wrong entity input, please check entity value '{}'".format(target))

                        if destination_flex_port:
                            target_interfaces = self._get_interface_port_data(source=target, port=destination_flex_port)
                            target_ip_addresses = self._get_ip_address_from_interface_port_block(port_block=target_interfaces, vlan_list=entity['vlan'], entity_index=index)

                            # If no target IP to ping then throw a warning
                            if len(target_ip_addresses) < 1:
                                logger.warn("Config/Input error - Target IP not available for Entity Index: '{index}', Entity Source: '{source}', Entity Target: '{target}' & its VLAN: {vlan}".format(index=index, source=entity['source'], target=target, vlan=entity['vlan']))
                                continue

                            for target_ip in target_ip_addresses:

                                log_name = 'TrafficAutomation_fping_' + target_ip + '_' + str(int(time.time())) + str(randint(1001, 1100)) + '.txt'

                                if current_host:
                                    log_name = os.path.join(folder_path, log_name)
                                    executable_location = os.path.join(folder_path, 'Fping.exe')
                                    cmd = self._apply_stream_options(platform=current_platform, stream=entity['profile'], source_ip=None, destination_ip=target_ip, log_name=log_name, executable_location=executable_location)

                                else:
                                    source_ip, source_vlan = self._find_source_interface_ip_from_server_block(ip=target_ip, flex_port=source_flex_port, ip_block=source_server['interfaces'], vlan_list=entity['vlan'])
                                    if not source_ip:
                                        logger.warn("Test case '{name}': Config/Input error - Source interface/IP not available for target: '{target_ip}',  Entity Index: '{index}', Entity Source: '{source}' , Entity Destination: '{target}' & its VLAN: {vlan}".format(index=index, source=entity['source'], target_ip=target_ip, vlan=entity['vlan'], name=test_name, target=target))
                                        continue
                                    cmd = self._apply_stream_options(platform=source_server['platform'], stream=entity['profile'], source_ip=source_ip, destination_ip=target_ip, log_name=log_name)
                                logger.trace(cmd)
                                commands.append({'entity_id': index, 'source': entity['source'], 'target': target, 'command': cmd, 'log_name': log_name, 'trafficgen': entity['profile']['trafficgen'].strip().lower(), 'target_ipv4': target_ip, 'vlan': source_vlan, 'description': entity['description']})

                        else:
                            BuiltIn().fail(msg="Failed to parse destination flex port from target: '{}'".format(target))

                self.traffic.data['entities'][index]['commands'] = commands
                if current_host:
                    self.traffic.data['serversAndCredentials']['CURRENT_HOST']['commands'].extend(commands)
                else:
                    self.traffic.data['serversAndCredentials'][server_key]['commands'].extend(commands)

        except:
            raise Exception(traceback.format_exc())

        finally:
            logger.trace("generate_commands_to_execute exited")

    def _get_server_ip_and_credentials(self, source):

        server_data = self._get_input_server_data_from_source_name(source)
        logger.trace(server_data)
        s = server_data['reachableIp'].copy()
        s.update(server_data['osUserLoginCredentials'])
        logger.trace(server_data)
        return s

    def _format_line(self, line):
        return line.replace('\x00', '').replace('\xff\xfe', '').lower()

    def _get_date_time_object(self, line):
        try:
            m = re.search(r'(\d{4}[/|-]\d{1,2}[/|-]\d{1,2}\s*\d{1,2}:\d{1,2}:\d{1,2}(?:.\d{2,3})?)',
                          line)  # 2017-09-20 16:23:45.123
            if m:
                date = m.group(0)
                if '.' not in date:
                    date = date + '.0'

                formatted = None
                if date.find('/') > 0:
                    formatted = datetime.datetime.strptime(date, "%Y/%m/%d %H:%M:%S.%f")
                elif date.find('-') > 0:
                    formatted = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
                else:
                    return False

                return formatted.strftime("%Y/%m/%d %H:%M:%S.%f")  # Not for ms

            else:
                # For linux epoch fping time conversion..
                m = re.search(r'^\s*\[([\.\d]+)?\]', line)  # [1234567890.123456] 12.21.0.1 : [1] , 84 bytes
                if m:
                    date = m.group(1)
                    if '.' not in date:
                        date = date + '.0'

                    date = datetime.datetime.fromtimestamp(float(date)).strftime('%Y-%m-%d %H:%M:%S.%f')
                    formatted = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

                    return formatted.strftime("%Y/%m/%d %H:%M:%S.%f")  # Not for ms

                return False
        except:
            logger.trace(traceback.format_exc())
            return False

    def _connect_using_ssh(self, machine_ip, username, password):
        ''''''
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
                logger.trace("Failed to take SSH connection")
                return False

            logger.trace("SSH connection to '%s' successful" % machine_ip)
            return ssh

        finally:
            logger.trace("_connect_using_ssh exited")

    def _convert_string_as_file_and_send_to_server(self, channel, string):
        logger.trace("_convert_string_as_file_and_send_to_server entered")

        try:
            # Creating temp file with content
            file_name = str(int(time.time())) + str(randint(1001, 1100)) + '.sh'
            fo = open(file_name, 'w')
            fo.write(string)
            fo.close()

            sftp = channel.open_sftp()
            sftp.put(file_name, '{}'.format(file_name))

            try:
                if os.path.isfile(file_name):
                    os.remove(file_name)
            except:
                logger.trace(traceback.format_exc())

            return file_name

        except:
            logger.trace(traceback.format_exc())
            return False

        finally:
            logger.trace("_convert_string_as_file_and_send_to_server exited")

    def _execute_linux_command(self, channel, command, stdout_log=False):
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
            logger.trace(traceback.format_exc())
            return False

        finally:
            logger.trace("_execute_linux_command exited")

    def _start_traffic_on_linux_platform(self, server_key, server_data):
        ''''''

        # Check reachableIp key in server data block
        if 'reachableIp' not in server_data:
            logger.warn("Server '{0}' not having 'reachableIp' key in its data".format(server_key))
            return False

        platform = server_data['platform']
        reachable_ip = server_data['reachableIp']
        user = server_data['osUserLoginCredentials']['user_name']
        passwd = server_data['osUserLoginCredentials']['password']

        # COnnecting to host using its reachable IP
        ssh = self._connect_using_ssh(machine_ip=reachable_ip,
                                      username=user,
                                      password=passwd)

        # Kill all ping instance if anything is running..
        self._execute_linux_command(ssh, 'killall fping', stdout_log=False)

        # Remove older log files if any
        self._execute_linux_command(ssh, 'rm -f TrafficAutomation_fping_*.txt', stdout_log=False)

        # Install fping into RHEL variation host OS
        binary_location = os.path.join(self.traffic.data['tools'], self.fping_rpm)
        response = self._install_fping_in_host_os(platform, reachable_ip, binary_location, cred={'user': user, 'passwd': passwd})

        # Run ping generate command
        for command in server_data['commands']:

            if command['trafficgen'] != 'fping':
                continue

            logger.info("Executing command: '{}'".format(command), also_console=1)
            self._execute_linux_command(ssh, command['command'], stdout_log=False)
            time.sleep(1)

        # Disconnect SSH session to the host
        ssh.close()

        return True

    def _execute_command_using_psexec_no_sync(self, server_data, command):
        ''''''
        logger.trace("_execute_command_using_psexec_no_sync entered..")

        random_number = str(randint(100, 200))
        temp_file = 'tmp' + random_number + '.bat'
        out_file = 'tmp' + random_number + '.out'
        pid_file = 'tmp' + random_number + '.pid'

        try:

            ps_exec_location = os.path.join(self.traffic.data['tools'], self.psExec)

            # Create a batch file
            bat = open(temp_file, 'w')
            bat.write('@echo off\n')
            bat.write('{cmd} > {output_log}\n'.format(cmd=command, output_log=out_file))
            bat.close()

            # Frame psexec command.. E.g. psexec.exe \\192.168.148.159 -u Administrator -p 12iso*help -w c:\share -d
            # -c -f currentHostBatch.bat 2 > PID_Output.out
            cmd = '{ps_path} \\\\{host} -u {user} -p {pwd} -d -c -f {bat_file} 2>{pid_file}'.format(
                ps_path=ps_exec_location, host=server_data['reachableIp'],
                user=server_data['osUserLoginCredentials']['user_name'],
                pwd=server_data['osUserLoginCredentials']['password'], bat_file=temp_file, pid_file=pid_file)

            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

            time.sleep(2)
            with open(pid_file, 'r') as AA:
                responce = AA.read()

            return responce

        except:
            raise Exception(traceback.format_exc())

        finally:
            os.system('del /f %s' % temp_file)
            os.system('del /f %s' % pid_file)
            logger.trace("_execute_command_using_psexec_no_sync exited..")

    def _execute_fping_command_using_psexec_no_sync(self, server_data, command, drive, name):
        ''''''
        logger.trace("_execute_fping_command_using_psexec_no_sync entered..")

        random_number = str(randint(100, 200))
        temp_file = 'tmp' + random_number + '.bat'
        out_file = 'tmp' + random_number + '.out'
        pid_file = 'tmp' + random_number + '.pid'

        working_dir = '{0}\\{1}'.format(drive, name)

        try:
            ps_exec_location = os.path.join(self.traffic.data['tools'], self.psExec)

            # Create a batch file
            bat = open(temp_file, 'w')
            bat.write('@echo off\n')
            bat.write('cd {dir}\n'.format(dir=working_dir))
            bat.write('{cmd}\n'.format(cmd=command))
            bat.close()

            # Frame psexec command.. E.g. psexec.exe \\192.168.148.159 -u Administrator -p 12iso*help -w c:\share -d
            # -c -f currentHostBatch.bat 2 > PID_Output.out
            cmd = '{ps_path} \\\\{host} -u {user} -p {pwd} -w {working_dir} -d -c -f {bat_file} 2>{pid_file}'.format(
                ps_path=ps_exec_location, host=server_data['reachableIp'],
                user=server_data['osUserLoginCredentials']['user_name'],
                pwd=server_data['osUserLoginCredentials']['password'], bat_file=temp_file, pid_file=pid_file,
                working_dir=working_dir)

            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

            time.sleep(2)
            with open(pid_file, 'r') as AA:
                responce = AA.read()

            return responce

        except:
            raise Exception(traceback.format_exc())

        finally:
            os.system('del /f %s' % temp_file)
            os.system('del /f %s' % pid_file)
            logger.trace("_execute_fping_command_using_psexec_no_sync exited..")

    def _start_traffic_on_windows_platform(self, server_key, server_data):
        ''''''

        # Check reachableIp key in server data block
        if 'reachableIp' not in server_data:
            logger.warn("Server '{0}' not having 'reachableIp' key in its data".format(server_key))
            return False

        # Before doing anything create folder share to use it for log redirect and other process
        folder_drive = 'C:'
        folder_name = 'TrafficExecutorLogs'
        folder_path = '{drive}\\{log_folder_name}'.format(log_folder_name=folder_name, drive=folder_drive)

        # Killall fping process if any
        command = 'powershell -Command "& Stop-Process -ProcessName fping -ErrorAction SilentlyContinue"'
        response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

        # Killall cmd process if any
        # command = 'powershell -Command "& Stop-Process -ProcessName cmd -ErrorAction SilentlyContinue"'
        # response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)
        #
        # Killall powershell process if any
        # command = 'powershell -Command "& Stop-Process -ProcessName powershell -ErrorAction SilentlyContinue"'
        # response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

        # Share remote folder
        if 'share_folder_in_host' in server_data and server_data['share_folder_in_host'] is True:
            logger.trace("Share folder already created in host, skipping remove folder call")
            command = 'DEL /F /Q {path}\\TrafficAutomation_fping_*'.format(path=folder_path)
            response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)
        else:
            command = 'NET SHARE {share_name}={share_path} /GRANT:Everyone,FULL'.format(share_name=folder_name, share_path=folder_path)
            response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)
            server_data['share_folder_in_host'] = True

        # Install/Copy Fping into Windows OS
        platform = server_data['platform']
        reachable_ip = server_data['reachableIp']
        binary_location = os.path.join(self.traffic.data['tools'], self.fping_exe)
        response = self._install_fping_in_host_os(platform, reachable_ip, binary_location)

        # Run ping generate command
        for command in server_data['commands']:

            if command['trafficgen'] != 'fping':
                continue

            logger.info("Executing command: '{}'".format(command), also_console=1)
            self._execute_fping_command_using_psexec_no_sync(server_data=server_data, command=command['command'],
                                                             drive=folder_drive, name=folder_name)
            time.sleep(1)

        return True

    def _start_traffic_in_current_host(self, server_key, server_data):
        ''''''

        # Killall ping process if any
        command = 'powershell -Command "& Stop-Process -ProcessName fping -ErrorAction SilentlyContinue"'
        subprocess.Popen(command, shell=True)

        # Supported current_host is windows now, copying Fping.exe into the proper location..
        folder_path = '{drive}\\{log_folder_name}'.format(log_folder_name='TrafficExecutorTestHeadLogs', drive='C:')
        binary_location = os.path.join(self.traffic.data['tools'], 'Fping.exe')
        cmd = 'XCOPY /F /S /Y {local} {path}\\*'.format(path=folder_path, local=binary_location)
        self._execute_system_command(cmd)

        # Run ping generate command
        for command in server_data['commands']:

            if command['trafficgen'] != 'fping':
                continue

            logger.info("Executing command: '{}'".format(command['command']), also_console=1)
            time.sleep(0.5)
            subprocess.Popen(command['command'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        return True

    def start_traffic(self):
        logger.trace("start_traffic entered")
        try:

            for server_key, server_data in self.traffic.data['serversAndCredentials'].iteritems():
                if 'commands' in server_data and len(server_data['commands']) > 0:

                    if 'platform' in server_data and server_data['platform'].lower() == 'windows':
                        res = self._start_traffic_on_windows_platform(server_key, server_data)
                        if res is False:
                            logger.warn("Failed to generate traffic")

                    elif 'platform' in server_data and server_data['platform'].lower() == 'linux':

                        res = self._start_traffic_on_linux_platform(server_key, server_data)
                        if res is False:
                            logger.warn("Failed to generate traffic")

                    elif server_key.lower() == 'current_host':

                        res = self._start_traffic_in_current_host(server_key, server_data)
                        if res is False:
                            logger.warn("Failed to generate traffic")

                    else:
                        logger.warn("Unsupported OS platform")
                else:
                    logger.trace("Sever '{0}' not having any ping target, nothing to start".format(server_key))

        except:
            logger.trace("Got exception")
            raise Exception(traceback.format_exc())

        finally:
            logger.trace("Generate Ping Traffic Exited..]]\n")
            logger.trace("start_traffic exited")

    def _stop_traffic_on_linux_platform(self, server_key, server_data):
        ''''''

        if 'reachableIp' not in server_data:
            logger.warn("Server '{0}' not having 'reachableIp' key in its data".format(server_key))
            return False

        # Connect to host using its reachableIp
        ssh = self._connect_using_ssh(machine_ip=server_data['reachableIp'],
                                      username=server_data['osUserLoginCredentials']['user_name'],
                                      password=server_data['osUserLoginCredentials']['password'])

        if not ssh:
            return False

        # Killall fping PID's
        res = self._execute_linux_command(ssh, 'pgrep -x fping', stdout_log=True)
        logger.trace("List of ping PID's going to kill are: '{0}'".format(res))

        self._execute_linux_command(ssh, 'killall -e fping', stdout_log=False)

        # Disconnect SSH session to the host
        ssh.close()

        return True

    def _stop_traffic_on_windows_platform(self, server_key, server_data):
        ''''''

        if 'reachableIp' not in server_data:
            logger.warn("Server '{0}' not having 'reachableIp' key in its data".format(server_key))
            return False

        # Killall ping process if any
        command = 'powershell -Command "& Stop-Process -ProcessName fping -ErrorAction SilentlyContinue"'
        response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

        # Killall cmd process if any
        command = 'powershell -Command "& Stop-Process -ProcessName cmd -ErrorAction SilentlyContinue"'
        response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

        # Killall powershell process if any
        command = 'powershell -Command "& Stop-Process -ProcessName powershell -ErrorAction SilentlyContinue"'
        response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

        return True

    def _check_server_data_has_command(self, type, commands):
        for each in commands:
            if each['trafficgen'] == type:
                return True

        return False

    def _stop_traffic_in_current_host(self, server_key, server_data):
        ''''''

        # Killall ping process if any
        command = 'powershell -Command "& Stop-Process -ProcessName fping -ErrorAction SilentlyContinue"'
        self._execute_system_command(command)

        # Killall powershell process if any
        # command = 'powershell -Command "& Stop-Process -ProcessName powershell -ErrorAction SilentlyContinue"'
        # response = self._execute_command_using_psexec_no_sync(server_data=server_data, command=command)

        return True

    def stop_traffic(self):
        try:
            logger.trace("stop_traffic entered")

            for server_key, server_data in self.traffic.data['serversAndCredentials'].iteritems():

                if 'commands' in server_data and len(server_data['commands']) > 0:

                    if not self._check_server_data_has_command('fping', server_data['commands']):
                        logger.info("Sever '{0}' not having any fping session, nothing to stop".format(server_key))
                        continue

                    if 'platform' in server_data and server_data['platform'].lower() == 'windows':

                        res = self._stop_traffic_on_windows_platform(server_key, server_data)
                        if res is False:
                            logger.error("Failed to stop traffic for host '{host}'. Please check the reachability and related traces and if possible stop traffic manually to the corresponding HOST".format(host=server_key))
                        else:
                            logger.info("Stopped fping traffic for Sever '{0}'".format(server_key))

                    elif 'platform' in server_data and server_data['platform'].lower() == 'linux':

                        res = self._stop_traffic_on_linux_platform(server_key, server_data)
                        if res is False:
                            logger.error("Failed to stop traffic for host '{host}'. Please check the reachability and related traces and if possible stop traffic manually to the corresponding HOST".format(host=server_key))
                        else:
                            logger.info("Stopped fping traffic for Sever '{0}'".format(server_key))

                    elif server_key.lower() == 'current_host':

                        res = self._stop_traffic_in_current_host(server_key, server_data)
                        if res is False:
                            logger.error("Failed to stop traffic for host '{host}'. Please check the reachability and related traces and if possible stop traffic manually to the corresponding HOST".format(host=server_key))
                        else:
                            logger.info("Stopped fping traffic for Sever '{0}'".format(server_key))

                    else:
                        logger.warn("Unsupported OS platform")

                else:
                    logger.info("Sever '{0}' not having any fping session, nothing to stop".format(server_key))

        except:
            logger.trace(traceback.format_exc())

        finally:
            logger.trace("stop_traffic exited")

    def _get_fping_logs_from_linux_host(self, server_key, server_data, folder_path):
        ''''''

        if 'reachableIp' not in server_data:
            logger.warn("Server '{0}' not having 'reachableIp' key in its data".format(server_key))
            return False

        # Connect to host using its reachableIp
        ssh = self._connect_using_ssh(machine_ip=server_data['reachableIp'],
                                      username=server_data['osUserLoginCredentials']['user_name'],
                                      password=server_data['osUserLoginCredentials']['password'])

        if not ssh:
            return False

        # Open SFTP handle
        sftp = ssh.open_sftp()

        for each_command in server_data['commands']:
            # Get all logs from OS
            logger.trace("Getting log file : '{}'".format(each_command['log_name']))

            for _ in xrange(5):
                try:
                    sftp.get(each_command['log_name'], os.path.join(folder_path, each_command['log_name']))
                    sta = sftp.stat(each_command['log_name'])
                except:
                    pass

                if os.path.exists(os.path.join(folder_path, each_command['log_name'])):
                    break
                else:
                    time.sleep(1)
                    logger.trace("Trying to get log file : '{}'".format(each_command['log_name']))

        # Disconnect SSH session to the host
        ssh.close()

        return True

    def _get_fping_logs_from_windows_host(self, server_key, server_data, remote_share_name, local_folder):
        ''''''

        if 'reachableIp' not in server_data:
            logger.warn("Server '{0}' not having 'reachableIp' key in its data".format(server_key))
            return False

        for each_command in server_data['commands']:

            if each_command['trafficgen'] != 'fping':
                continue

            # Get all logs from OS
            logger.trace("Getting log file : '{}'".format(each_command['log_name']))

            # Mount remote share
            cmd = 'NET USE \\\\{host}\\C$ /USER:{username} {password}'.format(host=server_data['reachableIp'], username=server_data['osUserLoginCredentials']['user_name'], password=server_data['osUserLoginCredentials'][
                'password'])
            self._execute_system_command(cmd)

            # Get file content using xcopy
            for _ in xrange(5):
                cmd = 'XCOPY /S /Y \\\\{host}\\{share_name}\\{out_file} {local_absolute_path}'.format(host=server_data['reachableIp'], share_name=remote_share_name, out_file=each_command['log_name'], local_absolute_path=os.path.join(local_folder, '.'))
                res = self._execute_system_command(cmd)
                if re.search(r'0 File\(s\) copied', res, re.I):
                    time.sleep(1)
                    logger.trace("Failed to copy file from remote machine OR file not exists in remote server")
                else:
                    break

        return True

    def _get_statistics_from_a_file_linux_platform(self, file_absolute_path, threshold):
        ''''''
        logger.trace("_get_statistics_from_a_file_linux_platform entered..")

        try:
            statistics = dict()
            statistics['losses'] = list()
            continuous_failure = 0

            print("Processing log file => '{}'".format(file_absolute_path))

            with open(file_absolute_path, 'r') as File:
                total = received = failed = 0
                start_time = end_time = None

                line = previous_line = ''
                id = 1
                error = 0
                loss_dict = dict()

                file_content = File.readlines()

                if len(file_content) == 0:
                    logger.warn("File '%s' exists with empty content." % file_absolute_path)
                    return

                # Skipping first line if it is empty
                if not re.search(r'\w', file_content[-1], re.I):
                    file_content.pop()

                last_seq_number = 0
                for index in xrange(len(file_content)):
                    line = self._format_line(file_content[index])

                    if line.strip() == '':
                        continue

                    total += 1
                    if total == 1:
                        dt = self._get_date_time_object(line)
                        # logger.debug(line)
                        statistics['startTime'] = str(dt) if dt else ''

                    try:
                        seq_number = re.search(r'\[(\d+)\],', line, re.I).group(1)

                        # Used for removing duplicates
                        if total != 1 and last_seq_number == int(seq_number):
                            total -= 1
                            continue

                        if 'count' in loss_dict and loss_dict['count'] > 0:
                            total = int(seq_number) + 1
                            loss_dict['count'] = int(seq_number) - last_seq_number - 1

                        last_seq_number = int(seq_number)

                    except:
                        seq_number = None

                    if seq_number and total == int(seq_number) + 1:

                        if 'start' in loss_dict and 'end' not in loss_dict:
                            dt = self._get_date_time_object(line)
                            loss_dict['end'] = str(dt) if dt else ''
                            loss_dict['id'] = id

                            # check continuous failure threshold
                            if loss_dict['count'] >= int(threshold['fping']['numberOfContinuousAllowedFailures']):
                                loss_dict['continuous_failure'] = True
                                continuous_failure += 1
                            else:
                                loss_dict['continuous_failure'] = False

                            statistics['losses'].append(loss_dict)
                            failed += loss_dict['count']

                            loss_dict = dict()
                            id += 1

                    elif total == 1 and total != int(seq_number) + 1:

                        current_line = file_content[index]

                        dt = self._get_date_time_object(current_line)
                        loss_dict['start'] = str(dt) if dt else ''

                        dt = self._get_date_time_object(current_line)
                        loss_dict['end'] = str(dt) if dt else ''

                        seq_number1 = 0
                        seq_number2 = re.search(r'\[(\d+)\],', current_line, re.I).group(1)

                        loss_dict['count'] = int(seq_number2) - int(seq_number1)
                        failed += loss_dict['count']

                        # check continuous failure threshold
                        if loss_dict['count'] >= int(threshold['fping']['numberOfContinuousAllowedFailures']):
                            loss_dict['continuous_failure'] = True
                            continuous_failure += 1
                        else:
                            loss_dict['continuous_failure'] = False

                        loss_dict['id'] = id
                        id += 1

                        statistics['losses'].append(loss_dict)
                        loss_dict = dict()

                        total = int(seq_number) + 1

                    elif last_seq_number and seq_number and last_seq_number == int(seq_number):

                        current_line = file_content[index]
                        previous_line = file_content[index - 1]

                        dt = self._get_date_time_object(previous_line)
                        loss_dict['start'] = str(dt) if dt else ''

                        dt = self._get_date_time_object(current_line)
                        loss_dict['end'] = str(dt) if dt else ''

                        seq_number1 = re.search(r'\[(\d+)\],', previous_line, re.I).group(1)
                        seq_number2 = re.search(r'\[(\d+)\],', current_line, re.I).group(1)

                        loss_dict['count'] = int(seq_number2) - int(seq_number1) - 1
                        failed += loss_dict['count']

                        # check continuous failure threshold
                        if loss_dict['count'] >= int(threshold['fping']['numberOfContinuousAllowedFailures']):
                            loss_dict['continuous_failure'] = True
                            continuous_failure += 1
                        else:
                            loss_dict['continuous_failure'] = False

                        loss_dict['id'] = id
                        id += 1

                        statistics['losses'].append(loss_dict)
                        loss_dict = dict()

                        total = int(seq_number) + 1

                    else:

                        if 'start' not in loss_dict:
                            dt = self._get_date_time_object(file_content[index])
                            loss_dict['start'] = str(dt) if dt else ''
                            loss_dict['count'] = 1
                        else:
                            loss_dict['count'] += 1

                if line:
                    dt = self._get_date_time_object(line)
                    statistics['endTime'] = str(dt) if dt else ''
                    if 'start' in loss_dict and 'end' not in loss_dict:
                        loss_dict['end'] = str(dt) if dt else ''
                        loss_dict['id'] = id

                        # check continuous failure threshold
                        if loss_dict['count'] >= int(threshold['fping']['numberOfContinuousAllowedFailures']):
                            loss_dict['continuous_failure'] = True
                            continuous_failure += 1
                        else:
                            loss_dict['continuous_failure'] = False

                        statistics['losses'].append(loss_dict)

                statistics['logFile'] = 'Available'
                statistics['Sent'] = total
                statistics['Lost'] = failed
                statistics['Received'] = total - failed

                logger.info("Number of losses '{}'".format(str(failed)), also_console=1)

                # Check threshold limit and add its state
                check = 0
                if 'numberOfAllowedFailures' in threshold['fping'] and threshold['fping']['numberOfAllowedFailures'] is not None and int(statistics['Lost']) > threshold['fping']['numberOfAllowedFailures']:
                    statistics.update({'thresholdCheck': 'Exceeds', 'continuous_failure': 0})
                    check = 1

                if 'numberOfContinuousAllowedFailures' in threshold['fping'] and threshold['fping']['numberOfContinuousAllowedFailures'] is not None and continuous_failure > 0:
                    statistics.update({'thresholdCheck': 'Exceeds', 'continuous_failure': continuous_failure})
                    logger.info("Number of continuous failures comparing with the threshold value : '{}'".format(str(continuous_failure)), also_console=1)
                    check = 1

                if check == 0:
                    statistics.update({'thresholdCheck': 'Acceptable Limit', 'continuous_failure': 0})

                # Finding max 1 & max2 continuous outage..
                max1 = {'count': 0}
                max2 = {'count': 0}

                for j in xrange(len(statistics['losses'])):
                    stat = statistics['losses'][j]

                    stat['count'] = int(stat['count'])

                    if stat['count'] > max1['count']:
                        max2.update(max1)
                        max1.update(stat)
                    elif stat['count'] > max2['count']:
                        max2.update(stat)

                statistics['max1'] = max1
                statistics['max2'] = max2

        except:
            logger.warn("File '%s' not present in log location, something went wrong" % file_absolute_path)
            statistics['logFile'] = 'Not Available'
            logger.trace(traceback.format_exc())

        finally:
            logger.trace("_get_statistics_from_a_file_linux_platform exited..")
            return statistics

    def _get_statistics_from_a_file_windows_platform(self, file_absolute_path, threshold):
        ''''''
        logger.trace("_get_statistics_from_a_file_windows_platform entered..")

        statistics = dict()
        statistics['losses'] = list()
        continuous_failure = 0

        logger.trace("Processing log file => '{}'".format(file_absolute_path))

        try:
            with open(file_absolute_path, 'r') as File:
                total = received = failed = 0
                start_time = end_time = None

                line = previous_line = ''
                id = 1
                error = 0
                loss_dict = dict()

                file_content = File.readlines()

                if len(file_content) == 0:
                    logger.warn("File '%s' exists with empty content." % file_absolute_path)
                    return

                # Skipping first line if it is empty
                if not re.search(r'\w', file_content[-1], re.I):
                    file_content.pop()

                for line in file_content[:]:
                    line = self._format_line(line)

                    if not re.match('^\d', line):
                        continue

                    total += 1
                    if total == 1:
                        dt = self._get_date_time_object(line)
                        # logger.debug(line)
                        statistics['startTime'] = str(dt) if dt else ''

                    try:
                        seq_number = re.search(r'reply\[(\d+)\]', line, re.I).group(1)
                    except:
                        seq_number = None

                    if seq_number and total == int(seq_number):
                        received += 1

                        if 'start' in loss_dict and 'end' not in loss_dict:
                            dt = self._get_date_time_object(line)
                            loss_dict['end'] = str(dt) if dt else ''
                            loss_dict['id'] = id

                            # check continuous failure threshold
                            if loss_dict['count'] >= int(threshold['fping']['numberOfContinuousAllowedFailures']):
                                loss_dict['continuous_failure'] = True
                                continuous_failure += 1
                            else:
                                loss_dict['continuous_failure'] = False

                            statistics['losses'].append(loss_dict)
                            loss_dict = dict()
                            id += 1

                    else:
                        failed += 1

                        if 'start' not in loss_dict:
                            dt = self._get_date_time_object(line)
                            loss_dict['start'] = str(dt) if dt else ''
                            loss_dict['count'] = 1
                        else:
                            loss_dict['count'] += 1

                if line:
                    dt = self._get_date_time_object(line)
                    statistics['endTime'] = str(dt) if dt else ''
                    if 'start' in loss_dict and 'end' not in loss_dict:
                        loss_dict['end'] = str(dt) if dt else ''
                        loss_dict['id'] = id

                        # check continuous failure threshold
                        if loss_dict['count'] >= int(threshold['fping']['numberOfContinuousAllowedFailures']):
                            loss_dict['continuous_failure'] = True
                            continuous_failure += 1
                        else:
                            loss_dict['continuous_failure'] = False

                        statistics['losses'].append(loss_dict)

                statistics['logFile'] = 'Available'
                statistics['Sent'] = total
                statistics['Received'] = received
                statistics['Lost'] = failed

                logger.info("Number of losses '{}'".format(str(failed)), also_console=1)

                # Check threshold limit and add its state

                if 'Lost' in statistics:
                    check = 0
                    if 'numberOfAllowedFailures' in threshold['fping'] and threshold['fping']['numberOfAllowedFailures'] is not None and int(statistics['Lost']) > threshold['fping']['numberOfAllowedFailures']:
                        statistics.update({'thresholdCheck': 'Exceeds', 'continuous_failure': 0})
                        check = 1

                    if 'numberOfContinuousAllowedFailures' in threshold['fping'] and threshold['fping']['numberOfContinuousAllowedFailures'] is not None and continuous_failure > 0:
                        statistics.update({'thresholdCheck': 'Exceeds', 'continuous_failure': continuous_failure})
                        logger.info("Number of continuous failures comparing with the threshold value : '{}'".format(str(continuous_failure)), also_console=1)
                        check = 1

                    if check == 0:
                        statistics.update({'thresholdCheck': 'Acceptable Limit', 'continuous_failure': 0})
                else:
                    logger.trace("Seems file with empty content found !!")

                # Finding max 1 & max2 continuous outage..
                max1 = {'count': 0}
                max2 = {'count': 0}

                for stat in statistics['losses']:

                    stat['count'] = int(stat['count'])

                    if stat['count'] > max1['count']:
                        max2.update(max1)
                        max1.update(stat)
                    elif stat['count'] > max2['count']:
                        max2.update(stat)

                statistics['max1'] = max1
                statistics['max2'] = max2

        except:
            logger.warn("File '%s' not present in log location, something went wrong" % file_absolute_path)
            statistics['logFile'] = 'Not Available'
            logger.trace(traceback.format_exc())

        finally:
            logger.trace("_get_statistics_from_a_file_windows_platform exited..")
            return statistics

    def _parse_log_file_and_update_statistics(self, server_key, server_data, folder_path, threshold):
        ''''''
        try:
            logger.trace("_parse_log_file_and_update_statistics entered")

            for each_command in server_data['commands']:

                if each_command['trafficgen'] != 'fping':
                    continue

                log_name = each_command['log_name']

                if server_key.lower() == 'current_host':
                    log_absolute_path = log_name
                else:
                    log_absolute_path = os.path.join(folder_path, log_name)

                logger.info("=>> Processing log file '{}'".format(log_absolute_path), also_console=1)

                # Check for each command with its corresponding file name exists
                if not os.path.exists(log_absolute_path):
                    logger.warn(
                        "File name '{0}' belongs to server '{1}' not available in local Or failed to download log from host OS".format(
                            log_name, server_key))

                statistics = dict()

                # If linux
                if 'platform' in server_data and server_data['platform'].lower() == 'linux':

                    # If file exists calculate statistics
                    statistics = self._get_statistics_from_a_file_linux_platform(file_absolute_path=log_absolute_path,
                                                                                 threshold=threshold)

                elif 'platform' in server_data and server_data['platform'].lower() == 'windows':

                    # If file exists calculate statistics
                    statistics = self._get_statistics_from_a_file_windows_platform(file_absolute_path=log_absolute_path,
                                                                                   threshold=threshold)

                elif server_key.lower() == 'current_host':

                    current_platform = "windows" if platform.system().lower() == "windows" else "linux"

                    # If file exists calculate statistics
                    if current_platform == 'windows':
                        statistics = self._get_statistics_from_a_file_windows_platform(file_absolute_path=log_absolute_path, threshold=threshold)

                    elif current_platform == 'linux':
                        # NOt tested !!
                        statistics = self._get_statistics_from_a_file_linux_platform(file_absolute_path=log_absolute_path, threshold=threshold)

                else:
                    logger.warn("Unsupported OS !!")
                    continue

                statistics.update(each_command)

                # Update statistics to its corresponding entity_id
                entity_id = each_command['entity_id']
                if 'statistics' not in self.traffic.data['entities'][entity_id]:
                    self.traffic.data['entities'][entity_id]['statistics'] = list()

                self.traffic.data['entities'][entity_id]['statistics'].append(statistics)

                # Update statistics to its corresponding server block
                if 'statistics' not in self.traffic.data['serversAndCredentials'][server_key]:
                    self.traffic.data['serversAndCredentials'][server_key]['statistics'] = list()

                self.traffic.data['serversAndCredentials'][server_key]['statistics'].append(statistics)

            return True

        except:
            raise AssertionError(traceback.format_exc())

        finally:
            logger.trace("_parse_log_file_and_update_statistics exited")

    def analyse_traffic(self, threshold):
        ''''''
        logger.trace("analyse_traffic entered..")

        try:
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")

            if 'fping' not in threshold and 'numberOfAllowedFailures' not in threshold['fping']:
                logger.warn(
                    "Threshold value not exists in input data, following default option. 'Test case will fail for minimum one loss'")
                threshold = {'fping': {'numberOfAllowedFailures': 0, 'numberOfContinuousAllowedFailures': 0}}

            folder_name = 'TrafficExecutorLogs'
            temp_location = tempfile.gettempdir()
            current_platform = "windows" if platform.system().lower() == "windows" else "linux"
            folder_path = os.path.join(temp_location, folder_name)

            # Remove and Create folder..
            if current_platform == 'windows':
                if os.path.exists(folder_path):
                    os.system("RMDIR /S /Q " + folder_path)
                    os.system('MKDIR "{pa}"'.format(pa=folder_path))
                else:
                    os.system('MKDIR "{pa}"'.format(pa=folder_path))
            else:
                if os.path.exists(folder_path):
                    os.system("rm -rf {0}; mkdir {0}".format(folder_path))
                else:
                    os.system("mkdir {}".format(folder_path))

            for server_key, server_data in self.traffic.data['serversAndCredentials'].iteritems():

                if 'commands' in server_data and len(server_data['commands']) > 0:

                    if not self._check_server_data_has_command('fping', server_data['commands']):
                        logger.trace("Test case '{test}': Sever '{server}' not having any fping output, nothing to analyse".format(server=server_key, test=test_name))
                        continue

                    if 'platform' in server_data and server_data['platform'].lower() == 'windows':
                        # Getting log files from host OS
                        res = self._get_fping_logs_from_windows_host(server_key, server_data, remote_share_name=folder_name, local_folder=folder_path)
                        if res is False:
                            logger.error("Failed to get traffic log file for host '{host}'. Please check the reachability and related traces and if possible stop traffic manually to the corresponding HOST".format(host=server_key))

                        # Parse log and update its statistics to the server data dictionary
                        res = self._parse_log_file_and_update_statistics(server_key, server_data, folder_path, threshold)
                        if res is False:
                            logger.warn("Failed to parse log output for host: '{host}'".format(host=server_key))

                    elif 'platform' in server_data and server_data['platform'].lower() == 'linux':
                        # Getting log files from host OS
                        res = self._get_fping_logs_from_linux_host(server_key, server_data, folder_path)
                        if res is False:
                            logger.trace("Failed to get traffic log file for host '{host}'. Please check the reachability and related traces and if possible stop traffic manually to the corresponding HOST".format(host=server_key))

                        # Parse log and update its statistics to the server data dictionary
                        res = self._parse_log_file_and_update_statistics(server_key, server_data, folder_path, threshold)
                        if res is False:
                            logger.warn("Failed to parse log output for host: '{host}'".format(host=server_key))

                    elif server_key.lower() == 'current_host':

                        res = self._parse_log_file_and_update_statistics(server_key=server_key, server_data=server_data, folder_path=None, threshold=threshold)
                        if res is False:
                            logger.warn("Failed to parse log output for host: '{host}'".format(host=server_key))

                    else:
                        logger.warn("Unsupported OS platform !!")

                else:
                    logger.trace("Test case '{test}': Sever '{server}' not having any fping output, nothing to analyse".format(server=server_key, test=test_name))

            # Copy all log for reference..
            output_dir = BuiltIn().get_variable_value("${OUTPUT_DIR}")
            log_output_dir = os.path.join(output_dir, folder_name)

            if not os.path.exists(log_output_dir):
                os.system('mkdir "{pa}"'.format(pa=log_output_dir))

            this_log_folder = re.sub('[^0-9a-zA-Z\s]+', '', test_name)
            this_log_folder = re.sub('\s\s+|\t', ' ', this_log_folder)
            this_log_folder = this_log_folder[:60]
            this_log_folder = os.path.join(log_output_dir, this_log_folder)

            if not os.path.exists(this_log_folder):
                os.system('mkdir "{pa}"'.format(pa=this_log_folder))
                # os.system("RMDIR /S /Q " + this_log_folder)

            if current_platform == 'windows':
                cmd = 'XCOPY /S /Y "{fp1}" "{fp2}"'.format(fp1=folder_path, fp2=this_log_folder)
                res = self._execute_system_command(cmd)
            else:
                for fn in glob.glob(os.path.join(folder_path, '*')):
                    shutil.copy(fn, this_log_folder)

            logger.trace("{tc}: Log files are copied to '{fp}'".format(tc=test_name, fp=this_log_folder))

            # Check threshold and return test status
            failure_count = 0
            loss_entities = dict()
            for index in xrange(len(self.traffic.data['entities'])):
                each_entity = self.traffic.data['entities'][index]
                if 'statistics' in each_entity:
                    for each_command in each_entity['statistics']:
                        if 'thresholdCheck' in each_command and each_command['thresholdCheck'] == 'Exceeds':
                            failure_count += 1
                            if index in loss_entities:
                                loss_entities[index] = loss_entities[index] + 1
                            else:
                                loss_entities[index] = 1
                            # logger.warn("Entity ID: '{ref}' => Fping session to target '{t}' from source '{s}' has some failures and Overall loss count '{lost}'".format(t=each_command['target_ipv4'], s=each_command['source'],ref=each_command['entity_id'], lost = each_command['Lost']))
                        else:
                            logger.trace("'thresholdCheck' is in acceptable limit")
                else:
                    logger.trace("'statistics' key not exists in entity, please check")

            if failure_count > 0:
                loss_entities = ['Entity - ' + str(x) + ' & number of session has losses - ' + str(y) for x, y in
                                 loss_entities.iteritems()]
                logger.error("Test case '{name}': Entities {losses} has losses which exceeds threshold limit.".format(
                    losses=str(loss_entities), name=test_name))
                BuiltIn().fail(
                    msg="Test case '{name}': Entities '{losses}' has losses which exceeds threshold limit".format(
                        losses=str(loss_entities), name=test_name))
            else:
                return True

        finally:
            logger.trace("analyse_traffic exited..")

    def report_traffic_statistics(self):
        ''''''
        logger.trace("report_traffic_statistics entered..")

        try:
            html_content = '<html><head><style>table#t01, th#t01, td#t01 {border: 1px solid black;border-collapse: collapse;}th#t01, td#t01 {padding: 5px;text-align: left;}table#t01 {width: 100%;}</style></head><body><table id="t01">'
            html_content += '<tr><th id="t01">#SNO</th><th id="t01">ENTITY ID</th><th id="t01">SOURCE</th><th id="t01">TARGET</th><th id="t01">VLAN</th><th id="t01">DESCRIPTION</th><th id="t01">START TIME</th><th id="t01">END TIME</th><th id="t01">SENT</th><th id="t01">RECEIVED</th><th id="t01">LOST</th><th id="t01">MAX_CONT_OUTAGE_1</th><th id="t01">MAX_CONT_OUTAGE_2</th><th id="t01">THRESHOLD CHECK</th></tr>'

            SNO = 0
            for index in xrange(len(self.traffic.data['entities'])):

                each_entity = self.traffic.data['entities'][index]

                if each_entity['profile']['trafficgen'].strip().lower() != 'fping':
                    continue

                logger.info('=' * 50 + ' ENTITY INDEX (' + str(index) + ') ' + '=' * 50, also_console=1)

                if 'statistics' not in each_entity:
                    test_name = BuiltIn().get_variable_value("${TEST_NAME}")
                    logger.trace(
                        "Test case '{1}': No statistics report for entity index: '{0}'".format(index, test_name))
                else:
                    # Printing input entity
                    temp = collections.OrderedDict()
                    temp['trafficgen'] = each_entity['profile']['trafficgen']
                    temp['source'] = each_entity['source']
                    temp['destination'] = each_entity['destination']
                    temp['vlan'] = each_entity['vlan']
                    temp['profile'] = each_entity['profile']

                    logger.info('=' * 10 + ' ENTITY INPUT' + '=' * 10, also_console=1)
                    logger.info(json.dumps(temp, indent=4), also_console=1)

                    # Formatted print
                    ordered = list()
                    logger.info('=' * 10 + ' ENTITY OUTPUT' + '=' * 10, also_console=1)
                    for i in xrange(len(each_entity['statistics'])):
                        SNO += 1

                        try:
                            each_stat = each_entity['statistics'][i]

                            temp = collections.OrderedDict()

                            temp['Entity_id'] = each_stat['entity_id']
                            temp['Source'] = each_stat['source']
                            temp['Target'] = each_stat['target']
                            temp['Target IPv4'] = each_stat['target_ipv4']
                            temp['Vlan'] = each_stat['vlan']
                            temp['Description'] = each_stat['description']
                            temp['Fping Session Started At'] = each_stat['startTime']
                            temp['Fping Session Ended At'] = each_stat['endTime']
                            temp['Sent'] = each_stat['Sent']
                            temp['Received'] = each_stat['Received']

                            temp_list = list()

                            for j in xrange(len(each_stat['losses'])):
                                each_loss = each_stat['losses'][j]

                                temp_dict = collections.OrderedDict()
                                temp_dict['ID'] = each_loss['id']
                                temp_dict['Number Of Failures'] = each_loss['count']
                                if each_loss['continuous_failure']:
                                    temp_dict['Is Threshold Exceeds ?'] = each_loss['continuous_failure']
                                temp_dict['Loss Started At'] = each_loss['start']
                                temp_dict['Loss Ended At'] = each_loss['end']

                                temp_list.append(temp_dict)

                            temp['losses'] = temp_list
                            ordered.append(temp)

                            max1 = "Nil"
                            if each_stat['max1']['count'] > 0:
                                s = datetime.datetime.strptime(each_stat['max1']['start'], "%Y/%m/%d %H:%M:%S.%f")
                                e = datetime.datetime.strptime(each_stat['max1']['end'], "%Y/%m/%d %H:%M:%S.%f")
                                diff = (e - s).total_seconds()

                                max1 = "#{count} count loss between {s} & {e} & taken time '{t}s'".format(s=each_stat['max1']['start'], e=each_stat['max1']['end'], count=each_stat['max1']['count'], t=diff)

                            max2 = "Nil"
                            if each_stat['max2']['count'] > 0:
                                s = datetime.datetime.strptime(each_stat['max2']['start'], "%Y/%m/%d %H:%M:%S.%f")
                                e = datetime.datetime.strptime(each_stat['max2']['end'], "%Y/%m/%d %H:%M:%S.%f")
                                diff = (e - s).total_seconds()

                                max2 = "#{count} count loss between {s} & {e} & taken time '{t}s'".format(s=each_stat['max2']['start'], e=each_stat['max2']['end'], count=each_stat['max2']['count'], t=diff)

                            html_content += '<tr><td id="t01">{SNO}</td><td id="t01">{ENTITY_ID}</td><td id="t01">{SOURCE}</td><td id="t01">{TARGET}</td><td id="t01">{VLAN}</td><td id="t01">{DESCRIPTION}</td><td id="t01">{START_TIME}</td><td id="t01">{END_TIME}</td><td id="t01">{SENT}</td><td id="t01">{RECEIVED}</td><td id="t01">{LOST}</td><td id="t01">{MAX_CONT_OUTAGE_1}</td><td id="t01">{MAX_CONT_OUTAGE_2}</td>{THRESHOLD_CHECK}</tr>'.format(
                                ENTITY_ID=temp['Entity_id'],
                                SNO=SNO,
                                SOURCE=temp['Source'],
                                TARGET=temp['Target'] if re.search(r'^\d+\.', temp['Target']) else temp['Target'] + '/ipv4:' + temp['Target IPv4'],
                                VLAN=temp['Vlan'],
                                START_TIME=temp['Fping Session Started At'],
                                END_TIME=temp['Fping Session Ended At'],
                                SENT=temp['Sent'],
                                RECEIVED=temp['Received'],
                                LOST=int(temp['Sent']) - int(temp['Received']),
                                MAX_CONT_OUTAGE_1=max1,
                                MAX_CONT_OUTAGE_2=max2,
                                THRESHOLD_CHECK='<td id="t01" style="color:red;"><b>FAIL</b></td>' if 'thresholdCheck' in each_stat and each_stat['thresholdCheck'] == 'Exceeds' else '<td id="t01" style="color:green;"><b>PASS</b></td>',
                                DESCRIPTION=temp['Description']
                            )
                        except:
                            logger.trace("Log output/statistics not available..")
                            logger.trace(traceback.format_exc())
                            html_content += '<tr><td id="t01">{SNO}</td><td id="t01">{ENTITY_ID}</td><td id="t01">{SOURCE}</td><td id="t01">{TARGET}</td><td id="t01">{VLAN}</td><td id="t01">{DESCRIPTION}</td><td id="t01">{START_TIME}</td><td id="t01">{END_TIME}</td><td id="t01">{SENT}</td><td id="t01">{RECEIVED}</td><td id="t01">{LOST}</td><td id="t01">{MAX_CONT_OUTAGE_1}</td><td id="t01">{MAX_CONT_OUTAGE_2}</td>{THRESHOLD_CHECK}</tr>'.format(
                                ENTITY_ID=temp['Entity_id'],
                                SNO=SNO,
                                SOURCE=temp['Source'],
                                TARGET=temp['Target'] if re.search(r'^\d+\.', temp['Target']) else temp['Target'] + '/ipv4:' + temp['Target IPv4'],
                                VLAN=temp['Vlan'],
                                START_TIME='NO DATA',
                                END_TIME='NO DATA',
                                SENT='NO DATA',
                                RECEIVED='NO DATA',
                                LOST='NO DATA',
                                MAX_CONT_OUTAGE_1='NO DATA',
                                MAX_CONT_OUTAGE_2='NO DATA',
                                THRESHOLD_CHECK='<td id="t01" style="color:red;"><b>ERROR</b></td>',
                                DESCRIPTION=temp['Description']
                            )

                    logger.info(json.dumps(ordered, indent=4), also_console=1)

                logger.trace("\n\n")
            html_content += '</table></body></html>'
            logger.info("""{}""".format(html_content), html=True)

            return True

        except:
            raise Exception(traceback.format_exc())

        finally:
            logger.trace("report_traffic_statistics exited..")