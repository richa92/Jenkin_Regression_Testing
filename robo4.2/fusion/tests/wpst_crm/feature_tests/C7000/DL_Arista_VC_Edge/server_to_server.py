import paramiko
import time
import re
# import os
# import threading
import subprocess


def execute_commands(ip, user_cred, ip1):
    '''
    Execute any of windows commands
    '''
    try:
        Error_Code = 0
        try:
            output_final = execute_windows_command(ip, user_cred[0], ip1)
        except subprocess.CalledProcessError as grepexc:
            print "error code", grepexc.returncode, grepexc.output
            Error_Code = grepexc.returncode
        if Error_Code == 6:
            output_final = execute_linux_command(ip, user_cred[1], ip1)
        return output_final
    except Exception as e:
        print "exception is %s" % (e)
        return e


def execute_windows_command(ip, user_credential, ip1):
    username = user_credential.get("username")
    passwd = user_credential.get("password")
    build_cmd = "psexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + " ping " + ip1
    output = subprocess.check_output(build_cmd)
    return output


def execute_linux_command(ip, user_credential, ip1):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=user_credential['username'], password=user_credential['password'])
    except Exception as e:
        print ("Unexpected Error Occured in Connecting the linux server!!!")
        print (e)
    linux_cmd = "ping -c 10 " + ip1
    stdin, stdout, stderr = ssh.exec_command(linux_cmd)
    error = stderr.readlines()
    output = stdout.readlines()
    print "Output for Linux %s" % (output)
    return str(output)
