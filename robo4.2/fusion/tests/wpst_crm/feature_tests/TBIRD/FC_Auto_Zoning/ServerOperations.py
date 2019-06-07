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
        # server Details
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
            stdin, stdout, stderr = self._ssh_obj.exec_command(
                (self._pycmd + " " + self._dir_location + "/" + module_file +
                 " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " +
                 self._ilo_password + " -us " + self._server_username +
                 " -ps " + self._server_password + " -c " + diskspd_cmd))
            time.sleep(40)
            print("tttt")
            output = stdout.readlines()
            print(output)
            print("tttt")
            return output
        except Exception as e:
            print (e)

    def get_disk(self, module_file_location):
        '''
        Starts IO traffic in the Server
        '''
        try:
            print ("get disk data")
            print module_file_location
            module_file = module_file_location.split('\\')[-1]
            print module_file
            print module_file_location
            self._sftp_obj.put(module_file_location,
                               self._dir_location + "/" + module_file)
            stdin, stdout, stderr = self._ssh_obj.exec_command(
                (self._pycmd + " " + self._dir_location + "/" + module_file +
                 " -i " + self._ilo_ip + " -u " + self._ilo_username + " -p " +
                 self._ilo_password + " -us " + self._server_username +
                 " -ps " + self._server_password))
            print ("get data")
            time.sleep(40)
            output = stdout.readlines()
            output1 = stderr.readlines()
            print ("output in perform io is" % output)
            print output1
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
            time.sleep(40)
            print("tttt")
            output = stdout.readlines()
            print("output in fetch_io %s" % output)
            print("tttt")
            return output
        except Exception as e:
            print (e)


def lun_discovery(linux_details, ilo_details, server_details, module_file_path):
    '''
    Returns the lun disk through list disk
    '''
    # print ("try to discover the lun")
    serv_obj = Server(linux_details, ilo_details, server_details)
    print ("try to discover the lun")
    serv_obj.connect_linux_machine()
    print ("try to discover the lun")
    output = serv_obj.get_disk(module_file_path)
    output_dict = {}
    print output
    print output[0]
    strout1 = str(output[0])
    print strout1
    cmd = re.findall(r'(Disk \d)', strout1)
    print cmd
    return cmd

    # print ("output1 in lun_disk is %s" % output1)
    # strout = re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K|H]?', '', output1)
    # split_text = " ".join(strout.split())
    # print ("split_text is %s" % split_text)
    # disk_list = re.findall(r"\b3P[\w].*?GB\s+\w+", split_text)
    # print ("Lun_disk list is %s" % disk_list)
    # count = len(disk_list)
    # return (disk_list, count)


def get_lun_volume(linux_details, ilo_details, server_details, module_file_path, get_volume_cmd):
    '''
    Returns the lun Volume
    '''
    output_dict1 = {}
    output_dict2 = {}
    output_list = []
    serv_obj = Server(linux_details, ilo_details, server_details)
    serv_obj.connect_linux_machine()
    output = serv_obj.get_disk(module_file_path, get_volume_cmd)
    output1 = str(output[0])
    strout = re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K|H]?', '', output1)
    print ("output1 in lun_disk is %s" % strout)
    pattern_obj = re.compile(r'(\w\s+\d+.\d+)')
    volume_list = pattern_obj.split(strout)
    split_list1 = re.split(r'\s+', volume_list[1])
    split_list2 = re.split(r'\s+', volume_list[3])
    output_dict1['Drive'] = split_list1[0]
    output_dict1['Size'] = split_list1[1]
    output_list.append(output_dict1)
    output_dict2['Drive'] = split_list2[0]
    output_dict2['Size'] = split_list2[1]
    output_list.append(output_dict2)
    print ("output_list is %s" % output_list)
    return output_list


def executes(linux_details, ilo_details, server_details, module_file_path, diskspd_cmd):
    '''
    Starts IO traffic in the Server and
    returns diskspd command and output file
    '''
    serv_obj = Server(linux_details, ilo_details, server_details)
    serv_obj.connect_linux_machine()
    output = serv_obj.perform_io(module_file_path, diskspd_cmd)
    output_dict = {}
    # print output
    strout1 = str(output[0])
    strout = re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K|H]?', '', strout1)
    time.sleep(5)
    print ("\n\n\n\n\nstrout is %s" % strout)
    cmd = re.findall(r'(.\\disk.*.dat)', strout)
    # Output file is:07 - 20 - 2017 - 0728_output.txt
    fileout = re.findall(r'Test\s+Output\s+file\s+is\s+:(.*.txt)', strout)
    # fileout = re.findall(r'Output\s+file\s+is\:([0-9][0-9]-.*.txt)', strout)
    print ("cmd is %s" % cmd)
    print ("fileout is %s" % fileout)
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
    print ("output in ioresult %s" % output)
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


def discover_lun_linux(server_details, lsscsi_cmd):
    '''
    Connect to the linux machine to execute other
    modules.
    '''
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_details['linux_ip'], username=server_details['username'], password=server_details['password'])
    except Exception as e:
        print ("Unexpected Error Occured in Connecting the linux server!!!")
        print (e)
    stdin, stdout, stderr = ssh.exec_command(lsscsi_cmd)
    output = stdout.readlines()
    length = len(output)
    disk_list = []
    for x in range(0, length):
        strout = str(output[x])
        print ("strout is %s" % strout)
        disk_pat = re.compile(r'\[\d+\:\d+:\d+:\d+\]\s+disk\s+3PARdata\sVV\s+\d+\s+(\/\w+\/\w+)+')
        pattern_obj = disk_pat.search(strout)
        disk_list.append(pattern_obj.group(1))
    print ("lsscsi output is %s" % disk_list)
    return disk_list


def write_to_lun(server_details, dd_cmd):
    '''
    Connect to the linux machine to execute other
    modules.
    '''
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_details['linux_ip'], username=server_details['username'], password=server_details['password'])
    except Exception as e:
        print ("Unexpected Error Occured in Connecting the linux server!!!")
        print (e)
    stdin, stdout, stderr = ssh.exec_command(dd_cmd)
    output = stdout.readlines()
    dd_output = stderr.readlines()
    # dd command output will be captured only in stderr.So returning stderr
    return (output, dd_output)

if __name__ == '__main__':

    linux_details = {"hostip": "15.199.235.170", "username": "root", "password": "hpvse123", "dir_location": "/root/", "python_cmd": "python2.7"}
    ilo_details = {'ilo_ip': '15.245.132.72', 'username': 'Administrator', "password": 'compaq'}
    server_details = {'username': 'Administrator', "password": 'hpvse1'}
    module_file_path = "C:\\Tamil\\fusion\\tests\\wpst_crm\\wpst-crm-india\\F118\\FetchIO_1.py"
    output_file = "11-05-2016-0941_output.txt"
    ioresults(linux_details, ilo_details, server_details, module_file_path, output_file)
