'''
This module contains the code to get the IP's of the
ethernet networks. Using the IP's it can login to the
server and execute the diskspd commands to start the traffic.
Diskspd result or ouput will be redirected to the log file

'''
import signal
import paramiko
import os
import time
import re
import threading
import subprocess
import Queue


class Server:

    def __init__(self, linux_mach_details, enc_details=None):

        # remote Linux Details
        self._host_ip = linux_mach_details['hostip']
        self._host_username = linux_mach_details['username']
        self._host_password = linux_mach_details['password']
        self._ssh_obj = None
        self._sftp_obj = None
        self._pycmd = linux_mach_details['python_cmd']
        self._dir_location = linux_mach_details['dir_location']

        # Enclosure Details
        self._ilo_ip = enc_details['ilo_ip']
        self._ilo_username = enc_details['username']
        self._ilo_password = enc_details['password']

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
            print (self._pycmd + " " + self._dir_location + "/" + module_file +
                   " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " +
                   self._ilo_password)
            stdin, stdout, stderr = self._ssh_obj.exec_command(self._pycmd + " " + self._dir_location + "/" + module_file +
                                                               " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " +
                                                               self._ilo_password)

            time.sleep(20)
            output = stdout.readlines()
            ip_list = [pattern.match(i).groups(1)[0] for i in output if
                       pattern.match(i)]
            print (ip_list)
            return ip_list
        except Exception as e:
            print (e)

    def execute_mcastcmd(self, ip, username, passwd, mcast_cmd):
        '''
        Execute the mcreceive tool Command
        '''
        try:
            single_cmd = "PsExec \\\\" + ip + " -u " + username + " -p " + passwd + " " +\
                mcast_cmd
            sleep_timer = int(mcast_cmd.split('>')[0].split(' ')[-2]) * 3
            print sleep_timer
            proc = subprocess.Popen(single_cmd, shell=True)
            time.sleep(sleep_timer)
            proc.terminate()
            os.system("taskkill /IM PsExec.exe /F")
            return (proc)
        except Exception as e:
            return (e)

    def execute_windows_commands(self, ip, username, passwd, wcmd):
        '''
        Execute any windows commands
        '''
        try:
            build_cmd = "PsExec \\\\" + ip + " -u " + \
                username + " -p " + passwd + " " + wcmd
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
    cmds = ["cmd /c wmic csproduct list /format > C:\\temp_uuid.txt",
            "powershell /c Get-InitiatorPort > C:\\temp_wwn.txt", "cmd /c ipconfig /all >C:\\temp_mac.txt"]
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
    This method will be called as the Keyword from the robogalxy for IO traffic test cases
    '''
    serv_obj = Server(linux_details, oa_details)
    serv_obj.connect_linux_machine()
    ip_list = serv_obj.get_server_ips(module_file_path)
    value = serv_obj.execute_diskspd(
        ip_list[0], server_cred[0], server_cred[1], diskspd_cmd)
    print "Executed diskspd command"
    output_dict = {}
    if value != 0:
        print "I/O traffic failed"
        return output_dict, "FAIL"
    column_headers = ['bytes', 'I/Os', 'MB/s',
                      'I/O per s', 'AvgLat', 'LatStdDev']
    with open(diskspd_cmd.split('>')[-1], 'r') as fp:
        for line in fp.readlines():
            if "actual test time:" in line:
                output_dict['duration'] = line.split(':')[-1].lstrip().rstrip()
            if 'thread count' in line:
                output_dict['thread_count'] = line.split(
                    ':')[-1].lstrip().rstrip()
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


def get_server_ip_win(linux_details, Ilo_details, module_file_path, exec_mcast=False):
    '''
    This method will be called as the Keyword from the robogalxy for IO traffic test cases
    '''
    serv_obj = Server(linux_details, Ilo_details)
    serv_obj.connect_linux_machine()
    ip_list = serv_obj.get_server_ips(module_file_path)
    return ip_list


def execute_teaming(ip, username, passwd, cmd_1):
    '''
    Execute the Teaming PS Command
    '''
    try:
        single_cmd1 = "PsExec \\\\" + ip + " -u " + username + " -p " + passwd + " " +\
            cmd_1
        output1 = os.system(single_cmd1)
        print (single_cmd1)
        return output1
    except Exception as e:
        return (e)


def start_capture_interface_traffic(cmd):
    try:
        os.system(cmd)
    except Exception as e:
        return e


def capture_interface_traffic(windows_details, wdump_cmd, interface_id, out_file):
    '''
    Execute windump command
    '''
    try:
        wdump_cmd = wdump_cmd + "\\Device\\NPF_" + interface_id + " > " + out_file
        single_cmd = "PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " +\
            wdump_cmd
        thread = threading.Thread(
            target=start_capture_interface_traffic, args=(single_cmd,))
        thread.start()
        time.sleep(10)
    except Exception as e:
        return e


def get_interface_guid(windows_details, cmd, bay_num):
    '''
    Execute windump command
    '''
    try:
        cmd = cmd + "guid_for_server_" + str(bay_num) + ".txt"
        single_cmd = "PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " +\
            cmd
        output = os.system(single_cmd)
        return output
    except Exception as e:
        return e


def extract_interface_guid(file_name):
    try:
        guids = dict()
        temp = list()

        with open(file_name) as f:
            for i in f.readlines():
                if "Ethern" in i:
                    guids[i.split(' ')[2]] = i.split(' ')[0]
        return guids
    except Exception as e:
        return e


def verify_mulitcast_traffic_received_by_interface(mcast_cmd, wdump_file):
    try:
        fname = wdump_file
        mcast_ip = mcast_cmd.split('> ')
        print mcast_ip
        with open(fname) as f:
            if mcast_ip[0].split(' ')[-4] + '.' + mcast_ip[0].split(' ')[-3] in f.read():
                return "0"
            else:
                return "1"
    except IndexError as err:
        return "-1"
    except Exception as e:
        return e


def verify_multicast_traffic(mcast_cmd):
    try:
        fname = mcast_cmd.split('> ')
        print fname[0].split(' ')[-4]
        f = open(fname[1])
        if fname[0].split(' ')[-4] in f.readlines()[-1]:
            f.close()
            return "0"
        else:
            f.close()
            return "1"
    except IndexError as err:
        f.close()
        return "-1"
    except Exception as e:
        return e


def send_multicast_traffic(msender):
    try:
        output = os.system(msender)
    except Exception as e:
        return e


def start_multicast_sender(msend):
    thread = threading.Thread(target=send_multicast_traffic, args=(msend,))
    thread.start()
    time.sleep(20)


def stop_multicast_sender():
    os.system("taskkill /IM msender.exe /F")


def execute_command_in_blade(cmd):
    try:
        os.system(cmd)
    except Exception as e:
        return e


def start_traffic_in_blade(windows_details, traffic_cmd):
    '''
    Execute Commands to Start traffic in blade server
    '''
    try:
        single_cmd = "PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " +\
            traffic_cmd
        thread = threading.Thread(target=execute_command_in_blade, args=(single_cmd,))
        thread.start()
        time.sleep(10)
    except Exception as e:
        return e


def extract_mac_address(file_name):
    try:
        with open(file_name) as f:
            return [i.split(' ')[0] for i in f.readlines() if "\\Device" in i]
    except Exception as e:
        return e


if __name__ == '__main__':

    linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                     "python_cmd": "python2.7"}

    ilo_details = {'ilo_ip': '15.186.15.11',
                   "username": 'Administrator', "password": 'hpvse123'}

    module_file_path = "C:\\Orange_Works\\Initial_workS_3.10\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\IGMP\\GetServerIPs.py"

    windows_server_cred = ["Administrator", 'password@123']
    mcast_cmd = "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 5 > C:\\multicast_traffic_server3.dat"
    wdump_cmd = "C:\\Multicast\\mk_mc\\WinDump.exe -c 200 > C:\\interface_traffic_of_server3.dat"

    # s= get_server_vlan_ip(linux_details,ilo_details,module_file_path, mcast_cmd,windows_server_cred )
    # s = capture_interface_traffic("192.168.10.25", "Administrator","password@123","C:\\Multicast\\mk_mc\\WinDump.exe -c 200 > C:\\interface_traffic_of_server1.dat")
    s = verify_mulitcast_traffic_received_by_interface(mcast_cmd, wdump_cmd)
    windows_server = {'win_ip': '192.168.10.27',
                      "username": 'Administrator', "password": 'password@123'}
    s = get_interface_guid(
        windows_server, "C:\\Multicast\\mk_mc\\mk_get_guid.bat > ", 2)
    s2 = extract_interface_guid("guid_for_server_2.txt")
    print s
    print s2


'''
if __name__ == '__main__':

    linux_dict = {"hostip":"15.186.21.149","username":"root","password":"password",
                  "dir_location":"/root/pexpect/pexpect-u-2.5.1/",
                  "python_cmd":"python2.7"}
    oa_detail = {'oa_ip':"15.186.27.232","username":"Administrator",
                 "password":"compaq","server_bay":"10"}
    s = Server(linux_dict,oa_detail)
    # s.connect_linux_machine()
    module_file_path = "C:\\Robogolaxy_Reps\\mk_rg_repo\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\GetServerIPs.py"
    # p_list = s.get_server_ips("C:\\Robogolaxy_Reps\\mk_rg_repo\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\GetServerIPs.py")
    # print ip_list
    # disk_s = "C:\\disk\\Diskspd-v2.0.17\\" \
    #         "amd64fre\\diskspd.exe -c10M -d10 -r -w50 -t5 " \
    #         "-o5 -b8K -h -L E:\\multi4.dat >C:\\Operation9.dat"
    windows_server_cred = ["Administrator",'password@123']
    s =get_server_mac_wwn_uuid(linux_dict,oa_detail,module_file_path,windows_server_cred)
    print s
    # uri = "/rest/interconnects/a815d241-11cb-41f9-a90f-5100c1302f37"
    # oupt = s.execute_diskspd('15.186.15.82',"Administrator",'password@123',disk_s)
    # oupt = execute_IO_and_disable_enable_ports(linux_dict,oa_detail,module_file_path,disk_s,windows_server_cred,uri,a,[2,3],'false')
    # print "The return value is \n "
    # print oupt
    # output = ""
    # with open(disk_s.split('>')[-1],'r') as fp:
    #    output = (fp.read())
    # print output
    # module_file_path ="C:\\Robogolaxy_Reps\\mk_rg_repo\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\GetServerIPs.py"
    # a = execute_IO_and_effuse_OA(linux_dict,oa_detail,module_file_path,disk_s,['Administrator','password@123'])
    # print a
'''
