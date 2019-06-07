'''
This module contains the code to perform io operation through Server iLO->VSP->SAC->cmd.
Executes the diskspd command to start the traffic.
Fetches the Diskspd results saved to the output  log file.

'''

import paramiko
import time
import re


class Server:

    def __init__(self, linux_mach_details, ilo_details=None, server_details=None):
        # Remote Linux Details
        self._host_ip = linux_mach_details['hostip']
        self._host_username = linux_mach_details['username']
        self._host_password = linux_mach_details['password']
        self._ssh_obj = None
        self._sftp_obj = None
        self._pycmd = linux_mach_details['python_cmd']
        self._dir_location = linux_mach_details['dir_location']
        # Server Details
        self._ilo_ip = ilo_details['ilo_ip']
        self._ilo_username = ilo_details['username']
        self._ilo_password = ilo_details['password']
        self._server_username = server_details['username']
        self._server_password = server_details['password']

    def connect_linux_machine(self):
        '''
        Connect to the linux machine to execute other
        modules.
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

    def perform_io(self, module_file_location, diskspd_cmd):
        '''
        Starts IO traffic in the Server
        '''
        try:
            module_file = module_file_location.split('\\')[-1]
            self._sftp_obj.put(module_file_location,
                               self._dir_location + "/" + module_file)
            print ("sneha!!!")
            # print ("_dir_location"%_dir_location)
            stdin, stdout, stderr = self._ssh_obj.exec_command(
                (self._pycmd + " " + self._dir_location + "/" + module_file +
                 " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " +
                 self._ilo_password + " -us " + self._server_username +
                 " -ps " + self._server_password + " -c " + diskspd_cmd))
            time.sleep(40)
            output = stdout.readlines()
            print ("output!!!" % output)
            return output
        except Exception as e:
            print (e)

    def fetch_io(self, module_file_location, output_file):
        '''
        Fetches IO traffic results from the Server
        '''
        try:
            module_file = module_file_location.split('\\')[-1]
            self._sftp_obj.put(module_file_location,
                               self._dir_location + "/" + module_file)
            self._ssh_obj.exec_command("clear")
            stdin, stdout, stderr = self._ssh_obj.exec_command(
                (self._pycmd + " " + self._dir_location + "/" + module_file +
                 " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " +
                 self._ilo_password + " -us " + self._server_username +
                 " -ps " + self._server_password + " -o " + output_file))
            time.sleep(20)
            output = stdout.readlines()
            return output
        except Exception as e:
            print (e)


def executes(linux_details, ilo_details, server_details, module_file_path, diskspd_cmd):
    '''
    Starts IO traffic in the Server and
    returns diskspd command and output file
    '''
    serv_obj = Server(linux_details, ilo_details, server_details)
    serv_obj.connect_linux_machine()
    output = serv_obj.perform_io(module_file_path, diskspd_cmd)
    output_dict = {}
    print output
    strout1 = str(output[0])
    strout = re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K|H]?', '', strout1)
    time.sleep(5)
    print strout
    cmd = re.findall(r'(.\\disk.*.dat)', strout)
    fileout = re.findall(r'([0-9][0-9]-.*.txt)', strout)
    print cmd
    print fileout
    try:
        if not fileout:
            return str(re.findall(r'(.Drive.*.!)', strout)[0]), fileout, None
        if fileout[0]:
                return str(cmd[0]), str(fileout[0]), "PASS"
    except IndexError as e:
            print e
            output_dict['result'] = None
            return output_dict['result']


def ioresults(linux_details, ilo_details, server_details, module_file_path, output_file):
    '''
    Fetches IO traffic results from the Server and
    returns the results
    '''
    serv_obj = Server(linux_details, ilo_details, server_details)
    serv_obj.connect_linux_machine()
    output = serv_obj.fetch_io(module_file_path, output_file)
    output_dict = {}
    print output
    strout = str(output[0])
    strout = re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K|H]?', '', strout)
    time.sleep(5)
    print strout
    cmd = re.findall(r'(.\\disk.*.dat)', strout)
    exeout = re.findall(r'(Test .*.ms)', strout)
    print cmd
    print exeout
    m = exeout[0].split(',')
    print m[6]
    try:
        if m[6] == " ":
            return str(cmd[0]), str(exeout[0]), None
        else:
            actual_duration = m[6].split('.')[-2].rstrip().lstrip()
            disk_pat = re.compile(r'.*-d([\d]+).*-t([\d]+).*')
            pattern_obj = disk_pat.match(cmd[0])
            print pattern_obj.group(1)
            if pattern_obj.group(1) == actual_duration:
                return str(cmd[0]), str(exeout[0]), "PASS"
            else:
                return str(cmd[0]), str(exeout[0]), None
    except IndexError as e:
        print e
        output_dict['result'] = None
        return output_dict['result']

'''
if __name__ == '__main__':

    linux_details = {"hostip": "15.245.132.33 ", "username": "root", "password": "hpvse123", "dir_location": "/root/", "python_cmd": "python2.7"}
    ilo_details = {'ilo_ip': '15.245.132.58', 'username': 'Administrator', "password": 'hpvse123'}
    server_details = {'username': 'Administrator', "password": 'hpvse1'}
    diskpsd_cmd = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60.ps1"

    module_file_path1 = "E:\\Robogalaxy\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\F119\\PerformIO.py"
    module_file_path2 = "E:\\Robogalaxy\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\F119\\FetchIO.py"
    '''
