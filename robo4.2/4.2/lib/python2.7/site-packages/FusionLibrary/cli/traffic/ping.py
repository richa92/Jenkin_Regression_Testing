import os
import re
import json
import paramiko
import traceback
import time
import subprocess
from robot.api import logger


class PingLibrary(object):

    def __init__(self, traffic_data):
        self.traffic = traffic_data

    def _get_input_server_data_from_source_name(self, source):

        p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', source, re.I)
        if not p:
            logger.warn("Input format is wrong, please check entity '{}'".format(source))
            return False

        if p.group(1):
            server_location = 'le:{le}/encl:{encl}/bay:{bay}'.format(le=p.group(1), encl=p.group(2), bay=p.group(3))
        else:
            server_location = 'encl:{encl}/bay:{bay}'.format(encl=p.group(2), bay=p.group(3))

        logger.info("Processing server : '{}'".format(server_location))

        if server_location in self.traffic.data['serversAndCredentials']:
            return self.traffic.data['serversAndCredentials'][server_location]
        else:
            raise AssertionError("Input data error: Server source mismatch in input, please check entity '{}'".format(server_location))

    def _get_interface_port_data(self, source, port):

        p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', source, re.I)
        if not p:
            logger.warn("Input format is wrong, please check entity '{}'".format(source))
            return False

        if p.group(1):
            server_location = 'le:{le}/encl:{encl}/bay:{bay}'.format(le=p.group(1), encl=p.group(2), bay=p.group(3))
        else:
            server_location = 'encl:{encl}/bay:{bay}'.format(encl=p.group(2), bay=p.group(3))

        # logger.info("Processing server : '{}'".format(server_location))

        if server_location in self.traffic.data['serversAndCredentials']:
            server_data = self.traffic.data['serversAndCredentials'][server_location]
        else:
            raise AssertionError("Input data error: Server source mismatch in input, please check entity '{}'".format(server_location))

        if 'interfaces' not in server_data:
            raise AssertionError("Input data error: No interfaces avail, please check entity '{}'".format(server_location))

        if port not in server_data['interfaces']:
            raise AssertionError("Port not present for given server entity")

        return server_data['interfaces'][port]

    def _get_ip_address_from_interface_port_block(self, port_block, valn_list):

        if 'ipAddress' not in port_block:
            raise AssertionError('Input data error: please check')

        ips = list()

        if len(port_block['ipAddress']) == 1:
            ips.append(port_block['ipAddress'][0]['ip'])

        else:

            valn_list_temp = [str(lan).lower() for lan in valn_list]

            for ipBlock in port_block['ipAddress']:
                if str(ipBlock['vlan']).lower() in valn_list_temp:
                    ips.append(ipBlock['ip'])

        return ips

    def _execute_system_command(self, command):
        logger.debug("_execute_system_command entered..")
        try:
            logger.info("Executing: '%s'" % command)
            output = ''
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = iter(proc.stdout.readline, b"")
            for i in out:
                output += i
            logger.debug(output)
            return True

        except:
            raise Exception(traceback.format_exc())

        finally:
            logger.debug("_execute_system_command exited..")

    def _connect_using_ssh(self, machine_ip, username, password):
        logger.debug("_connect_using_ssh entered")

        try:
            ssh = None
            for _ in xrange(10):
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(hostname=machine_ip, username=username, password=password)

                    break
                except:
                    logger.debug(traceback.format_exc())
                    time.sleep(5)
                    logger.debug("Failed to take SSH connection, please wait for next attempt")
            else:
                logger.debug("Failed to take SSH connection")
                return False

            logger.debug("SSH connection to '%s' successful" % machine_ip)
            return ssh

        finally:
            logger.debug("_connect_using_ssh exited")

    def _convert_string_as_file_and_send_to_server(self, channel, string):
        logger.debug("_convert_string_as_file_and_send_to_server entered")

        try:
            # Creating temp file with content
            file_name = str(int(time.time())) + '.sh'
            fo = open(file_name, 'w')
            fo.write(string)
            fo.close()

            sftp = channel.open_sftp()
            sftp.put(file_name, '{}'.format(file_name))

            try:
                if os.path.isfile(file_name):
                    os.remove(file_name)
            except:
                logger.debug(traceback.format_exc())

            return file_name

        except:
            logger.debug(traceback.format_exc())
            return False

        finally:
            logger.debug("_convert_string_as_file_and_send_to_server exited")

    def _execute_command(self, channel, command, stdout_log=False):
        logger.debug("_executeCommand entered")

        try:
            logger.info("Executing: '%s'" % command)

            sin, sout, serr = channel.exec_command(command=command)

            count = 0
            while not sout.channel.exit_status_ready():
                count += 1
                if count % 5 == 0:
                    logger.debug('Please wait for the remote command completion')
                time.sleep(5)

            sout.channel.recv_exit_status()

            response = ""
            if stdout_log:
                for l in sout:
                    response += l
                    logger.info(l.strip(), also_console=True)

            return response.strip()
        except:
            logger.debug(traceback.format_exc())
            return False

        finally:
            logger.debug("_execute_command exited")

    def _run_ping_with_windows(self, command, target_ip, output_file):
        logger.debug("_run_ping_with_windows entered..")
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

            logger.debug("####### Running : '%s'" % command)

            process = subprocess.Popen(batch_file_path, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            pid = process.pid

            return pid

        except:
            raise Exception(traceback.format_exc())

        finally:
            logger.debug("_run_ping_with_windows exited..")

    def generate_commands_to_execute(self):
        try:
            logger.debug("generate_commands_to_execute entered")

            new_entity = list()
            for entity in self.traffic.data['entities']:

                temp = entity
                commands = list()

                logger.info("Processing server interface : '{}'".format(entity['source']))

#                source_server_data = self._get_input_server_data_from_source_name(source=entity['source'])

                for target in entity['destination']:

                    if re.match(r'^\d+\.\d+', target):
                        if self.traffic.data['platform'].lower() in ('windows'):
                            cmd = 'ping -t {}'.format(target)
                        elif self.traffic.data['platform'].lower() in ('windows'):
                            cmd = 'ping -t 10 {}'.format(target)
                        logger.info(cmd, also_console=True)
                        commands.append({'source': entity['source'], 'target': target, 'commands': cmd})

                    else:
                        p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', target, re.I)
                        if p:
                            if p.group(1):
                                server_location = 'le:{le}/encl:{encl}/bay:{bay}'.format(le=p.group(1), encl=p.group(2), bay=p.group(3))
                            else:
                                server_location = 'encl:{encl}/bay:{bay}'.format(encl=p.group(2), bay=p.group(3))

                            target_interfaces = self._get_interface_port_data(source=target, port=p.group(4))

                            target_ip_addresses = self._get_ip_address_from_interface_port_block(port_block=target_interfaces, valn_list=entity['vlan'])

                            for ip in target_ip_addresses:
                                cmd = 'ping -t {}'.format(ip)
                                logger.info(cmd, also_console=True)
                                commands.append({'source': entity['source'], 'target': ip, 'commands': cmd})

                        else:
                            raise AssertionError("Wrong entity input")

                temp['commands'] = commands
                new_entity.append(temp)

            self.traffic.data['entities'] = new_entity

        except:
            pass

        finally:
            logger.debug("generate_commands_to_execute exited")

    def _get_server_ip_and_credentials(self, source):

        server_data = self._get_input_server_data_from_source_name(source)
        logger.debug(server_data)
        s = server_data['reachableIp'].copy()
        s.update(server_data['osUserLoginCredentials'])
        logger.debug(server_data)
        return s

    def _format_line(self, line):
        return line.replace('\x00', '').replace('\xff\xfe', '')

    def _get_date_time_object(self, line):
        try:
            m = re.search(r'(\d{1,2}[/|-]\d{1,2}[/|-]\d{4}\s*\d{1,2}:\d{1,2}:\d{1,2}(?:.\d{2,3})?)', line)  # 04/09/2017  0:18:06
            if m:
                date = m.group(0)
                if '.' not in date:
                    date = date + '.0'

                fmt = '%m/%d/%Y %H:%M:%S'
                if date.find('/') > 0:
                    return time.strptime(date, "%m/%d/%Y %H:%M:%S.%f")
                elif date.find('-') > 0:
                    return time.strptime(date, "%m-%d-%Y %H:%M:%S.%f")
                else:
                    return False
            m = re.search(r'(\d{1,2}[/|-]\d{1,2}[/|-]\d{2}\s*\d{1,2}:\d{1,2}:\d{1,2}(?:.\d{2,3})?)', line)
            if m:
                date = m.group(0)
                if '.' not in date:
                    date = date + '.0'

                if date.find('/') > 0:
                    return time.strptime(date, "%m/%d/%y %H:%M:%S.%f")
                elif date.find('-') > 0:
                    return time.strptime(date, "%m-%d-%y %H:%M:%S.%f")
                else:
                    return False
            return False
        except:
            logger.debug(traceback.format_exc())
            return False

    def start_traffic(self):
        logger.debug("start_traffic entered")
        try:

            logger.debug("start_traffic entered")
            source_server = dict()
            server_location = dict()

            list_of_commands = list()
            list_of_pids = list()
            for entity in self.traffic.data['entities']:
                # server_location = self._get_input_server_data_from_source_name(entity['source'])
                #  source_server['hostIP'] = server_location['reachableIp']
                #   source_server['username'] = server_location['osUserLoginCredentials']['userName']
                # source_server['password'] = server_location['osUserLoginCredentials']['password']
                commands = list()
                commands = entity['commands']
                for c in commands:
                    cc = c['commands']
                    list_of_commands.append(cc)
                logger.debug(list_of_commands)

                if self.traffic.data['platform'].lower() in ('windows'):

                    logger.info('*W' * 60, also_console=True)
                    for command in list_of_commands:
                        destination_ip = command[8:]
                        log_name = destination_ip + '_' + str(int(time.time())) + '.txt'

                        pid_output = self._run_ping_with_windows(command, destination_ip, log_name)
                        list_of_pids.append({'destination_ip': destination_ip, 'pid': pid_output, 'log_name': log_name})

                    self.traffic.data['pids'] = list_of_pids
                    logger.info('*' * 60, also_console=True)
                    logger.info(json.dumps(self.traffic.data, indent=4, separators=(',', ': ')), also_console=True)
                    logger.debug("PING Started for destination IPs")

                elif self.traffic.data['platform'].lower() in ('linux'):
                    source_server = {'hostIP': '16.114.220.185', 'username': 'root', 'password': 'wpsthpvse1', 'platform': 'windows'}
                    logger.info('*' * 60, also_console=True)
                    for command in list_of_commands:
                        # SSH to server
                        ssh_obj = self._connect_using_ssh(source_server['hostIP'], source_server['username'], source_server['password'])
                        destination_ip = command[11:]
                        log_name = destination_ip + '_' + str(int(time.time())) + '.txt'

                        command = """
nohup {command} | while read pong; do echo "$(date +"%m/%d/%Y %H:%M:%S"): $pong"; done >{log_name} &
echo $!
""".format(command=command, log_name=log_name)
                        logger.debug(command)
                        fn = self._convert_string_as_file_and_send_to_server(ssh_obj, command)
                        response = self._execute_command(ssh_obj, 'bash %s' % fn, stdout_log=True)
                        list_of_pids.append({'destination_ip': destination_ip, 'pid': response, 'shell_file_name': fn, 'log_name': log_name})
                        logger.info("=>>PING Started for '%s' and PID: '%s'" % (destination_ip, response), also_console=True)
                        logger.debug("PING Started for destination IPs")
                        ssh_obj.close()

                    self.traffic.data['pids'] = list_of_pids
                    logger.info(json.dumps(self.traffic.data, indent=4, separators=(',', ': ')), also_console=True)
                else:
                    logger.warn("Only windows/Linux platform supported..")

        except:
            logger.debug("Got exception")
            raise Exception(traceback.format_exc())

        finally:
            logger.info("Generate Ping Traffic Exited..]]\n", also_console=1)
            logger.debug("start_traffic exited")

    def stop_traffic(self):
        try:
            logger.debug("stop_traffic entered")

        except:
            pass

        finally:
            logger.debug("stop_traffic exited")

    def analyse_traffic(self):
        try:
            logger.debug("analyse_traffic entered")

#            source_server = {'hostIP':'16.114.220.185','username':'root','password':'wpsthpvse1','platform':'windows'}
#            if source_server['platform'].lower() in ('windows'):
            if self.traffic.data['platform'].lower() in ('windows'):
                folder_path = 'C:\\'
                for index, data in enumerate(self.traffic.data['pids']):
                    logger.info("Killing process of '{}' & its PID: '{}'".format(data['destination_ip'], data['pid']), also_console=True)
                    os.system("taskkill /T /F /pid '%s'" % data['pid'])
                    # subprocess.call("taskkill /pid '%s'" % data['pid'])

#            elif source_server['platform'].lower() in ('linux'):
            elif self.traffic.data['platform'].lower() in ('linux'):
                source_server = {'hostIP': '16.114.220.185', 'username': 'root', 'password': 'wpsthpvse1', 'platform': 'windows'}
                folder_path = ''
                ssh_obj = self._connect_using_ssh(source_server['hostIP'], source_server['username'], source_server['password'])
                sftp = ssh_obj.open_sftp()
                folder_path = '{drive}\\{log_folder_name}'.format(log_folder_name='TrafficExecutorLogs', drive='C:')
#               try:
#                   shutil.rmtree(folder_path)
#               except:
#                   logger.debug(traceback.format_exc())

                try:
                    os.mkdir(folder_path)
                except:
                    logger.debug(traceback.format_exc())

                for index, data in enumerate(self.traffic.data['pids']):
                    logger.info("Killing process of '{}' & its PID: '{}'".format(data['destination_ip'], data['pid']), also_console=True)
                    self._execute_command(ssh_obj, "kill -9 %s" % data['pid'])
                    sftp.get(data['log_name'], os.path.join(folder_path, data['log_name']))
                    self._execute_command(ssh_obj, "rm -f %s" % data['log_name'])
                    self._execute_command(ssh_obj, "rm -f %s" % data['shell_file_name'])
                ssh_obj.close()

            else:
                logger.warn("Only windows/Linux platform supported..")

            # Parse log file and report result..
            for index, data in enumerate(self.traffic.data['pids']):
                file_path = os.path.join(folder_path, data['log_name'])
                logger.info("Processing log file => '{}'".format(file_path))
                try:
                    statistics = dict()
                    statistics['losses'] = list()

                    with open(file_path, 'r') as File:
                        total = received = failed = 0
                        start_time = end_time = None

                        line = previous_line = ''
                        id = 1
                        loss_dict = dict()

                        file_content = File.readlines()
                        if not re.search(r'\w', file_content[-1], re.I):
                            file_content.pop()

                        for line in file_content[:]:
                            line = self._format_line(line)
                            if line.startswith('ping') or 'Pinging' in line or 'bytes of data' in line or not re.search('[a-z]', line, re.IGNORECASE):
                                continue
                            if 'Ping statistics' in line:
                                break

                            total += 1
                            if total == 1:
                                dt = self._get_date_time_object(line)
                                # logger.debug(line)
                                statistics['startTime'] = str(dt) if dt else ''

                            if 'unreachable' in line or 'timed out' in line or 'failure' in line:
                                # logger.debug(line)
                                if 'start' not in loss_dict:
                                    dt = self._get_date_time_object(line)
                                    loss_dict['start'] = str(dt) if dt else ''
                                    loss_dict['count'] = 1
                                else:
                                    loss_dict['count'] += 1

                            if line.lower().find('ttl') >= 0:
                                received += 1
                                if 'start' in loss_dict and 'end' not in loss_dict:
                                    dt = self._get_date_time_object(line)
                                    loss_dict['end'] = str(dt) if dt else ''
                                    loss_dict['id'] = id

                                    statistics['losses'].append(loss_dict)
                                    loss_dict = dict()
                                    id += 1
                            else:
                                failed += 1

                        if line:
                            dt = self._get_date_time_object(line)
                            statistics['endTime'] = str(dt) if dt else ''
                            if 'start' in loss_dict and 'end' not in loss_dict:
                                loss_dict['end'] = str(dt) if dt else ''
                                loss_dict['id'] = id
                                statistics['losses'].append(loss_dict)

                        statistics['logFile'] = 'Available'
                        statistics['Sent'] = total
                        statistics['Received'] = received
                        statistics['Lost'] = failed

                except:
                    logger.warn("File '%s' not present in log location, something went wrong" % file_path)
                    statistics['logFile'] = 'Not Available'

                self.traffic.data['pids'][index]['statistics'] = statistics

            logger.info("\n\n\n")

            logger.info('*' * 60, also_console=True)
            logger.info(json.dumps(self.traffic.data, indent=4, separators=(',', ': ')), also_console=True)
            logger.info("PING STATISTICS FROM SERVER: \n", also_console=True)

            for index, item in enumerate(self.traffic.data['pids']):

                if item['statistics']['logFile'] == 'Not Available':
                    logger.info("\tIP: {0:>16} =>> Log file is missing, Please check".format(item['targetIP']), also_console=True)
                    continue
                logger.info("\tIP: {0:>16} =>> Sent: {1:<7}, Received: {2:<7}, Lost: {3:<7}".format(item['destination_ip'], item['statistics']['Sent'], item['statistics']['Received'], item['statistics']['Lost']), also_console=True)
                # remove log files
                if self.traffic.data['platform'].lower() in ('windows'):
                    folder_path = 'C:\\'
                    batch_file_name = item['destination_ip'] + '.bat'
                    batch_file = os.path.join(folder_path, batch_file_name)
                    logger.info("Removing batch file: '%s'" % batch_file, also_console=True)
                    os.remove(batch_file)
                    out_file_name = item['log_name']
                    out_file = os.path.join(folder_path, out_file_name)
                    logger.info("Removing output file: '%s'" % out_file, also_console=True)
                    # fo = open(out_file, 'w')
                    # fo.close()
                    # os.remove(out_file)

            logger.info('*' * 60, also_console=True)
            logger.debug("analyse_traffic exited with Pass")
            return self.traffic.data['pids']

        except:
            logger.debug("Analyse traffic Got exception")
            raise Exception(traceback.format_exc())
