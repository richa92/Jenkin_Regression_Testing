
'''
This module contains the code to get the IP's of the
ethernet networks. Using the IP's it can login to the
server and execute the diskspd commands to start the traffic.
Diskspd results or ouput will be redirected to the log file

'''


import os
import paramiko
import re


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    Execute the diskSPD tool Command
    '''
    try:
        single_cmd = "C:\\PSTools\\PaExec \\\\" + ip + " -u " + username + " -p " + passwd + " " + \
                     wcmd
        print single_cmd
        output = os.system(single_cmd)
        return (output)
    except Exception as e:
        return (e)


def validate_windows_lun_count(ip, username, passwd):
    diskpart_cmd = ["cmd /c powershell \
    /c \"Get-disk | Select-Object -Property Number,FriendlyName\">Windowslun.txt"]
    output = execute_windows_commands(ip,
                                      username, passwd, diskpart_cmd[0])
    with open("Windowslun.txt") as f:
        lines = f.readlines()
        print lines
        count = 0
        for i in lines:
            if "3PARdata" in i:
                count = count + 1
                print count
        return count


def discover_lun_esxi(server_details, lsscsi_cmd):
    '''
    Connect to the linux machine to execute other
    modules.
    '''
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_details['ip'], username=server_details['username'], password=server_details['password'])
    except Exception as e:
        print ("Unexpected Error Occured in Connecting the linux server!!!")
        print (e)

    stdin, stdout, stderr = ssh.exec_command(lsscsi_cmd)
    output = stdout.readlines()
    return output


def validate_windows_BFS(ip, username, passwd):
    diskpart_cmd = ["cmd /c powershell \
    /c \"Get-Partition -DriveLetter C\">WindowsBFS.txt"]
    output = execute_windows_commands(ip,
                                      username, passwd, diskpart_cmd[0])

    with open("WindowsBFS.txt") as f:
        lines = f.readlines()
        print lines
        count = 0
        disk_size = []
        for i in lines:
            if "Basic" in i:
                print i
                disk_size = (str(i).split("GB")[0]).split(" ")[-2]
                print disk_size

    return disk_size
