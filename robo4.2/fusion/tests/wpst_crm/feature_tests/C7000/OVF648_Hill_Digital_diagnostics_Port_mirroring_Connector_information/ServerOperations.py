'''
This module contains the code to get the IP's of the
ethernet networks. Using the IP's it can login to the
server and execute the diskspd commands to start the traffic.
Diskspd results or ouput will be redirected to the log file

'''

import paramiko
import os
import time
import re
import threading
from OAOperations import *
import Queue


class Server:

    def __init__(self, linux_mach_details, enc_details=None):

        # remote Linux Detailss
        self._host_ip = linux_mach_details['hostip']
        self._host_username = linux_mach_details['username']
        self._host_password = linux_mach_details['password']
        self._ssh_obj = None
        self._sftp_obj = None
        self._pycmd = linux_mach_details['python_cmd']
        self._dir_location = linux_mach_details['dir_location']

        # Enclosure Details
        self._oa_ip = enc_details['oa_ip']
        self._oa_username = enc_details['username']
        self._oa_password = enc_details['password']
        self._server_bay = enc_details['server_bay']

    def connect_linux_machine(self):
        '''
        Connect to the linux machine to get the IP
        Address of the sever blades.
        '''

        try:
            self._ssh_obj = paramiko.SSHClient()
            self._ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self._ssh_obj.connect(self._host_ip, username=self._host_username,
                                  password=self._host_password)
            self._sftp_obj = self._ssh_obj.open_sftp()
        except Exception as e:
            print ("Unexpected Error Occured in Connecting the linux server!!!")
            print (e)

    def get_server_ips(self, module_file_location):
        '''
        This method will return the server IPs.
        '''

        try:
            pattern = re.compile(r'.*Ip=(.*) \s.* \s.*')
            module_file = module_file_location.split('\\')[-1]
            self._sftp_obj.put(module_file_location,
                               self._dir_location + "/" + module_file)
            stdin, stdout, stderr = self._ssh_obj.exec_command(self._pycmd + " " + self._dir_location + "/" + module_file +
                                                               " -i " + self._oa_ip + " -u " + self._oa_username + " -p " +
                                                               self._oa_password + " -b " + self._server_bay)
            time.sleep(20)
            output = stdout.readlines()
            ip_list = [pattern.match(i).groups(1)[0] for i in output if
                       pattern.match(i)]
            print (ip_list)
            return ip_list
        except Exception as e:
            print (e)

    def execute_diskspd(self, ip, username, passwd, diskspd_cmd):
        '''
        Execute the DiskSPD tool Command
        '''
        try:
            single_cmd = "psexec \\\\" + ip + " -u " + username + " -p " + passwd + " " +\
                diskspd_cmd
            output = os.system(single_cmd)
            return (output)
        except Exception as e:
            return (e)

    def execute_windows_commands(self, ip, username, passwd, wcmd):
        '''
        Execute any windows commands
        '''
        try:
            build_cmd = "psexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + wcmd
            output = os.system(build_cmd)
            return output
        except Exception as e:
            return e


def get_server_mac_wwn_uuid(linux_details, oa_details, module_file_path, server_cred):
    '''
    This method will return the WWN ,MAC and UUId of the servers
    '''

    serv_obj = Server(linux_details, oa_details)
    serv_obj.connect_linux_machine()
    ip_list = serv_obj.get_server_ips(module_file_path)
    cmds = ["cmd /c wmic csproduct list /format > C:\\temp_uuid.txt", "powershell \
    /c Get-InitiatorPort > C:\\temp_wwn.txt", "cmd /c ipconfig /all >C:\\temp_mac.txt"]
    temp_dict = {"uuid": "", "wwn": "", "mac": "", "serial_number": ""}

    for i in range(len(cmds)):
        if i == 0:
            output = serv_obj.execute_windows_commands(ip_list[0],
                                                       server_cred[0], server_cred[1], cmds[i])
            with open("C:\\temp_uuid.txt") as f:
                lines = f.readlines()
                uuid = [i.split("=")[-1] for i in lines if "UUID" in i]
                sn = [i.split("=")[-1] for i in lines if
                      "IdentifyingNumber" in i]
            temp_dict['serial_number'] = sn[0].rstrip()
            temp_dict['uuid'] = uuid[0].rstrip()
        if i == 1:
            output = serv_obj.execute_windows_commands(ip_list[0],
                                                       server_cred[0], server_cred[1], cmds[i])
            with open("C:\\temp_wwn.txt") as f:
                wwn = [i.split()[-3].rstrip() for i in f.readlines()
                       if "Fibre Channel" in i]
            temp_dict['wwn'] = wwn
        if i == 2:
            output = serv_obj.execute_windows_commands(ip_list[0],
                                                       server_cred[0], server_cred[1], cmds[i])
            with open("C:\\temp_mac.txt") as f:
                mac = [i.split(':')[-1].strip() for i in f.readlines()
                       if "Physical Address" in i]
            temp_dict['mac'] = mac

    return temp_dict


def executes(linux_details, oa_details, module_file_path, diskspd_cmd,
             server_cred, q=None):
    '''
    This method will be called as the Keyword from the
    robogalxy for IO traffic test cases
    '''
    serv_obj = Server(linux_details, oa_details)
    serv_obj.connect_linux_machine()
    ip_list = serv_obj.get_server_ips(module_file_path)
    value = serv_obj.execute_diskspd(ip_list[0], server_cred[0], server_cred[1], diskspd_cmd)
    print "Executed diskspd command"
    output_dict = {}
    if value != 0:
        print "I/O traffic failed"
        return output_dict, "FAIL"
    column_headers = ['bytes', 'I/Os', 'MB/s', 'I/O per s', 'AvgLat', 'LatStdDev']
    with open(diskspd_cmd.split('>')[-1], 'r') as fp:
        for line in fp.readlines():
            if "actual test time:" in line:
                output_dict['duration'] = line.split(':')[-1].lstrip().rstrip()
            if 'thread count' in line:
                output_dict['thread_count'] = line.split(':')[-1].lstrip().rstrip()
            if "total:" in line:
                temp = line.split(':')[-1].split('|')
                temp_values = [j.lstrip().rstrip() for j in temp]
                output_dict.update(dict(zip(column_headers, temp_values)))
            if "Read IO" in line:
                break
    disk_pat = re.compile(r'.*-d([\d]+).*-t([\d]+).*')
    pattern_obj = disk_pat.match(diskspd_cmd)
    try:
        if pattern_obj.group(1) == output_dict['duration'].split('.')[0] and \
                pattern_obj.group(2) == output_dict['thread_count']:
            if q is None:
                pass
            else:
                output_dict['result'] = 'PASS'
                q.put(output_dict)
            return output_dict, "PASS"
        else:
            if q is None:
                pass
            else:
                output_dict['result'] = None
                q.put(output_dict)
            return output_dict, None
    except KeyError as e:
        print "KeyError is done"
        output_dict['result'] = None
        q.put(output_dict)
        return output_dict['result']


def execute_IO_and_effuse_OA(linux_details, oa_details, module_file_path,
                             diskspd_cmd, server_cred):
    '''
    This method will perform the Efuse ICM and start the
    IO traffic
    '''
    q = Queue.Queue()
    io_thread = threading.Thread(target=executes, args=(linux_details,
                                                        oa_details, module_file_path, diskspd_cmd, server_cred, q))
    oa_obj = OAOperations()
    effuse_thread = threading.Thread(target=oa_obj.efuse_device, args=(oa_details['oa_ip'], oa_details['username'], oa_details['password'],
                                                                       'oa', '1', 'off'))
    failover_thread = threading.Thread(target=oa_obj.forceFailOver, args=(oa_details['oa_ip'], oa_details['username'], oa_details['password']))
    io_thread.start()
    time.sleep(20)
    effuse_thread.start()
    time.sleep(600)
    print "sleeping Before start failover_thread"
    failover_thread.start()
    time.sleep(220)
    result = q.get()
    print result
    return result


def execute_IO_and_disable_enable_ports(*args):
    '''
    This method will disable and enable the ports
    and start the IO traffic
    '''

    linux_details, oa_details = args[0], args[1]
    module_file_path, diskspd_cmd = args[2], args[3]
    server_cred = args[4]
    uri, output, portno = args[5], args[6], args[7]

    q = Queue.Queue()
    io_thread = threading.Thread(target=executes, args=(linux_details,
                                                        oa_details, module_file_path, diskspd_cmd, server_cred, q))
    oa_obj = OAOperations()
    io_thread.start()
    time.sleep(20)
    iter = 1

    while iter < 205:
        if iter % 2 == 0:
            port_thread = threading.Thread(target=oa_obj.disable_enable_interconnect_ports,
                                           args=(uri, output, portno[0], 'true'))
            port_thread_1 = threading.Thread(target=oa_obj.disable_enable_interconnect_ports,
                                             args=(uri, output, portno[1], 'false'))
        else:
            port_thread = threading.Thread(target=oa_obj.disable_enable_interconnect_ports,
                                           args=(uri, output, portno[1], 'true'))
            port_thread_1 = threading.Thread(target=oa_obj.disable_enable_interconnect_ports,
                                             args=(uri, output, portno[0], 'false'))
        port_thread.start()
        time.sleep(60)
        port_thread_1.start()
        time.sleep(60)
        time.sleep(300)
        iter += 1

    port_thread_1 = threading.Thread(target=oa_obj.disable_enable_interconnect_ports,
                                     args=(uri, output, portno[1], 'true'))
    port_thread_1.start()
    result = q.get()
    return result

'''
if __name__ == '__main__':

    linux_dict = {"hostip":"15.186.21.149","username":"root","password":"password",
                  "dir_location":"/root/pexpect/pexpect-u-2.5.1/",
                  "python_cmd":"python2.7"}
    oa_detail = {'oa_ip':"15.186.27.232","username":"Administrator",
                 "password":"compaq","server_bay":"10"}
    s = Server(linux_dict,oa_detail)
    #s.connect_linux_machine()
    module_file_path = "C:\\Robogolaxy_Reps\\mk_rg_repo\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\GetServerIPs.py"
    #p_list = s.get_server_ips("C:\\Robogolaxy_Reps\\mk_rg_repo\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\GetServerIPs.py")
    #print ip_list
    #disk_s = "C:\\disk\\Diskspd-v2.0.17\\" \
    #         "amd64fre\\diskspd.exe -c10M -d10 -r -w50 -t5 " \
    #         "-o5 -b8K -h -L E:\\multi4.dat >C:\\Operation9.dat"
    windows_server_cred = ["Administrator",'password@123']
    s =get_server_mac_wwn_uuid(linux_dict,oa_detail,module_file_path,windows_server_cred)
    print s
    #uri = "/rest/interconnects/a815d241-11cb-41f9-a90f-5100c1302f37"
    #oupt = s.execute_diskspd('15.186.15.82',"Administrator",'password@123',disk_s)
    #oupt = execute_IO_and_disable_enable_ports(linux_dict,oa_detail,module_file_path,disk_s,windows_server_cred,uri,a,[2,3],'false')
    #print "The return value is \n "
    #print oupt
    #output = ""
    #with open(disk_s.split('>')[-1],'r') as fp:
    #    output = (fp.read())
    #print output
    #module_file_path ="C:\\Robogolaxy_Reps\\mk_rg_repo\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\GetServerIPs.py"
    #a = execute_IO_and_effuse_OA(linux_dict,oa_detail,module_file_path,disk_s,['Administrator','password@123'])
    #print a
'''
