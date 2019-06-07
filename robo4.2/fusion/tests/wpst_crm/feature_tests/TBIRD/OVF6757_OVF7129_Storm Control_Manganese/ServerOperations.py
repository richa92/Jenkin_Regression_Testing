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
import subprocess


class Server:
    '''
    Class server
    '''

    def __init__(self, linux_mach_details, enc_details=None):
        '''
        init function
        '''

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
            print "Unexpected Error Occured in Connecting the linux server!!!"
            print e

    def get_server_ips(self, module_file_location):
        '''
        This method will return the server IPs.
        '''

        try:
            pattern = re.compile(r'.*Ip=(.*) \s.* \s.*')
            module_file = module_file_location.split('\\')[-1]
            self._sftp_obj.put(module_file_location,
                               self._dir_location + "/" + module_file)
            print self._pycmd + " " + self._dir_location + "/" + module_file + " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " + self._ilo_password
            stdout = self._ssh_obj.exec_command(self._pycmd + " " + self._dir_location + "/" + module_file + " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " + self._ilo_password)
            time.sleep(20)
            output = stdout.readlines()
            ip_list = [pattern.match(i).groups(1)[0] for i in output if
                       pattern.match(i)]
            print ip_list
            return ip_list
        except Exception as e:
            print e

    def execute_diskspd(self, ip, username, passwd, diskspd_cmd):
        '''
        Execute the DiskSPD tool Command
        '''
        try:
            single_cmd = "PsExec \\\\" + ip + " -u " + username + " -p " + passwd + " " +\
                diskspd_cmd
            output = os.system(single_cmd)
            return output
        except Exception as e:
            return e


if __name__ == '__main__':

    ilo_details = {'ilo_ip': '15.186.15.11',
                   "username": 'Administrator', "password": 'hpvse123'}

    windows_server_cred = ["Administrator", 'password@123']


def execute_mcastcmd(ip, username, passwd, mcast_cmd):
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
        return proc
    except Exception as e:
        return e


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    This will execute the windows commands
    '''
    try:
        build_cmd = "PsExec \\\\" + ip + " -u " + \
            username + " -p " + passwd + " " + wcmd
        output = os.system(build_cmd)
        return output
    except Exception as e:
        return e


def get_server_vlan_ip(linux_details, Ilo_details, module_file_path, mcast_command, server_cred, exec_mcast=False):
    '''
    This method will be called as the Keyword from the robogalxy for IO traffic test cases
    '''
    serv_obj = Server(linux_details, Ilo_details)
    serv_obj.connect_linux_machine()
    ip_list = serv_obj.get_server_ips(module_file_path)
    # return ip_list
    if exec_mcast:
        output = serv_obj.execute_mcastcmd(
            ip_list[0], server_cred[0], server_cred[1], mcast_command)
        return output, ip_list
    return None, ip_list


def execute_command_in_blade(cmd):
    '''
    Execute Commands in blade server
    '''
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
    '''
    Extract the mac address
    '''
    try:
        with open(file_name) as f:
            return [i.split(' ')[0] for i in f.readlines() if "\\Device" in i]
    except Exception as e:
        return e
