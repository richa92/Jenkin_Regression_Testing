'''
This module contains the code to get the IP's of the
ethernet networks. Using the IP's it can login to the
server and execute the diskspd commands to start the traffic.
Diskspd results or ouput will be redirected to the log file

'''
import signal
import paramiko
import os
import time
import re
import threading
# from OAOperations import *
import subprocess
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
        self._ilo_ip = enc_details['ilo_ip']
        self._ilo_username = enc_details['username']
        self._ilo_password = enc_details['password']
        # self._server_bay = enc_details['server_bay']

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
            # pattern = re.compile(r'.*Ip=(.*) \s.* \s.*')
            pattern = re.compile(r'.*Ip=(172.*) \s.* \s.*')
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

    def execute_diskspd(self, ip, username, passwd, diskspd_cmd):
        '''
        Execute the DiskSPD tool Command
        '''
        try:
            single_cmd = "PsExec \\\\" + ip + " -u " + username + " -p " + passwd + " " +\
                diskspd_cmd
            output = os.system(single_cmd)
            return (output)
        except Exception as e:
            return (e)

    def execute_mcastcmd(self, ip, username, passwd, mcast_cmd):
        '''
        Execute the mcreceive tool Command
        '''
        try:
            single_cmd = "PsExec \\\\" + ip + " -u " + username + " -p " + passwd + " " +\
                mcast_cmd
            sleep_timer = int(mcast_cmd.split('>')[0].split(' ')[-2]) * 20
            print sleep_timer
            # output = os.system(single_cmd)
            proc = subprocess.Popen(single_cmd, shell=True)
            time.sleep(sleep_timer)
            proc.terminate()
            # os.kill(proc.pid,signal.SIGINT)
            # print "done"
            os.system("taskkill /IM PsExec.exe /F")
            return (proc)
        except Exception as e:
            return (e)

    def execute_windows_commands(self, ip, username, passwd, wcmd):
        '''
        Execute any windows commands
        '''
        try:
            build_cmd = "PsExec \\\\" + ip + " -u " + username + " -p " + passwd + " " + wcmd
            output = os.system(build_cmd)
            return output
        except Exception as e:
            return e


def start_mcreceive(linux_details, Ilo_details, module_file_path, mcast_command, server_cred, exec_mcast=True):
    try:
        thread = threading.Thread(target=get_server_vlan_ip, args=(linux_details, Ilo_details, module_file_path, mcast_command,
                                                                   server_cred, exec_mcast))
        thread.start()
        # time.sleep(10)
    except Exception as E:
        return E


def get_server_vlan_ip(linux_details, Ilo_details, module_file_path, mcast_command,
                       server_cred, exec_mcast=False):
    '''
    This method will be called as the Keyword from the
    robogalxy for IO traffic test cases
    '''
    serv_obj = Server(linux_details, Ilo_details)
    serv_obj.connect_linux_machine()
    ip_list = serv_obj.get_server_ips(module_file_path)
    # return ip_list
    if exec_mcast:
        output = serv_obj.execute_mcastcmd(ip_list[0], server_cred[0], server_cred[1], mcast_command)
        return output, ip_list
    return None, ip_list


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
        print wdump_cmd
        single_cmd = "PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " +\
            wdump_cmd
        thread = threading.Thread(target=start_capture_interface_traffic, args=(single_cmd,))
        thread.start()
        time.sleep(10)
    except Exception as e:
        return e


def Start_mreceive_traffic(windows_details, mcast_cmd, out_file):
    '''
    Execute Windump command
    '''
    try:

        print mcast_cmd
        single_cmd = "PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " +\
            wdump_cmd
        thread = threading.Thread(target=start_capture_interface_traffic, args=(single_cmd,))
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
        print cmd
        single_cmd = "C:\PSTools\PSTools\PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " +\
            cmd
        print single_cmd
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

            # name,guid  = lines[-5].split(' ')[2], lines[-5].split(' ')[0]
            # print name, guid
            # guids[name]=guid
            # name1,guid1  = lines[-3].split(' ')[2], lines[-3].split(' ')[0]
            # guids[name1]=guid1
        return guids
    except Exception as e:
        return e


def verify_mulitcast_traffic_received_by_interface(mcast_cmd, wdump_file):
    try:
        # fname = wdum_cmd.split('> ')
        fname = wdump_file
        mcast_ip = mcast_cmd.split('> ')
        print mcast_ip
        ip = mcast_ip[0].split(' ')[-4] + '.' + mcast_ip[0].split(' ')[-3]
        with open(fname) as f:
            if ip in f.read():
                return "0"
            else:
                return "1"
    except IndexError as err:
        return "-1"
    except Exception as e:
        return e


def verify_multicast_traffic(mcast_cmd):
    """fname = mcast_cmd.split('> ')
    print fname
    print fname[0]
    print fname[1]
    ip = fname[0].split(' ')[-4]
    f = open(fname[1])
    print f
    str1 = f.readlines()[-1]
    if ip in str1:
        f.close()
        return "0"
    else:
        f.close()
        return "1"

    """
    try:
        fname = mcast_cmd.split('> ')
        print fname
        print fname[0]
        print fname[1]
        mcast_ip = fname[0].split(' ')[-4]
        print mcast_ip
        f = open(fname[1])
        print f
        file_line = f.readlines()[-1]
        print file_line
        if mcast_ip in file_line:
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


def delete_route_DL_server(cmd):
    output = os.system(cmd)
    return output


def dl_ipconfig(cmd, IP):
    cmds = ["cmd /c ipconfig > C:\\dl_ip.txt"]
    output = os.system(cmds[0])
    print output
    with open("C:\\dl_ip.txt") as f:
        lines = f.readlines()
        print lines
        ip_list = [i.split(":")[1] for i in lines if "IPv4 Address" in i]
        print (ip_list)
        data_ip = re.findall("\d+\.\d+\.\d+\.", IP)
        print data_ip
        for IPS in ip_list:
            a = re.findall("\d+\.\d+\.\d+\.", IPS)
            if a == data_ip:
                print IPS
                return IPS


def add_route_DL_server(ip):
    '''
    Execute windump command
    '''
    cmd = "route add 224.0.0.0 mask 240.0.0.0" + " " + ip
    output = os.system(cmd)
    return output


def delete_route(windows_details, cmd):
    '''
    Execute windump command
    '''
    try:
        single_cmd = "PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " + cmd
        print single_cmd
        output = os.system(single_cmd)
        return output
    except Exception as e:
        return e


def add_route(windows_details, ip):
    '''
    Execute Windump command
    '''
    try:
        cmd = "route add 224.0.0.0 mask 240.0.0.0" + " " + ip
        single_cmd = "PsExec \\\\" + windows_details['win_ip'] + " -u " + windows_details['username'] + " -p " + windows_details['password'] + " " + cmd
        print single_cmd
        output = os.system(single_cmd)
        return output
    except Exception as e:
        return e


if __name__ == '__main__':

    linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                     "python_cmd": "python2.7"}

    ilo_details = {'ilo_ip': '15.186.15.11', "username": 'Administrator', "password": 'hpvse123'}

    module_file_path = "C:\\Orange_Works\\Initial_workS_3.10\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\IGMP\\GetServerIPs.py"

    windows_server_cred = ["Administrator", 'password@123']
    mcast_cmd = "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 5 > C:\\multicast_traffic_server3.dat"
    wdump_cmd = "C:\\Multicast\\mk_mc\\WinDump.exe -c 200 > C:\\interface_traffic_of_server3.dat"

    # s= get_server_vlan_ip(linux_details,ilo_details,module_file_path, mcast_cmd,windows_server_cred )
    # s = capture_interface_traffic("192.168.10.25", "Administrator","password@123","C:\\Multicast\\mk_mc\\WinDump.exe -c 200 > C:\\interface_traffic_of_server1.dat")
    s = verify_mulitcast_traffic_received_by_interface(mcast_cmd, wdump_cmd)
    windows_server = {'win_ip': '192.168.10.27', "username": 'Administrator', "password": 'password@123'}
    s = get_interface_guid(windows_server, "C:\\Multicast\\mk_mc\\mk_get_guid.bat > ", 2)
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
