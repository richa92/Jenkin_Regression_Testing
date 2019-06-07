'''
This module contains the code to get the IP's of the
ethernet networks. Using the IP's it can login to the
server and execute the diskspd commands to start the traffic.
Diskspd results or ouput will be redirected to the log file

'''

import paramiko
import time
import re
import os
import threading
import Queue
import time
from robot.libraries.BuiltIn import BuiltIn


def execute_windows_commands(ip, username, passwd, ip1, q):
    '''
    Execute any windows commands
    '''
    try:
        build_cmd = "paexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + "ping" + " " + ip1
        print build_cmd
        output = os.system(build_cmd)
        print output
        q.put(output)
    except Exception as e:
        return e


def execute_linux_command(ip, username, password, ip1, q):
    port = 22
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password)
    except Exception as e:
        print ("Unexpected Error Occured in Connecting the linux server!!!")
        print (e)
    linux_cmd = "ping -c 10 " + ip1
    stdin, stdout, stderr = ssh.exec_command(linux_cmd)
    error = stderr.readlines()
    output = stdout.readlines()
    lines = ''.join(output)
    searchObj = re.search(r'(\d)%', lines, re.M | re.I)
    print "Output for Linux %s" % searchObj.group(1)
    result = searchObj.group(1)
    q.put(result)


def execute_commands(ip, username, passwd, ip1, OS_Type, q):
    '''
    Execute any of windows commands
    '''
    if OS_Type == 'W1':
        output_final = execute_windows_commands(ip, username, passwd, ip1, q)
    elif OS_Type == 'RH':
        output_final = execute_linux_command(ip, username, passwd, ip1, q)
    return output_final


def execute_traffic_parallel(server_details, IP_List, OS_Type):
    q = Queue.Queue()
    threads = [threading.Thread(target=execute_commands, args=(server_details['ip'], server_details['username'], server_details['password'], j['ip1'], OS_Type, q))
               for j in IP_List]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    output = [q.get() for _ in xrange(len(threads))]
    print 'results %s' % output
    return output


def checkservicehealth(no, ip, name, OS_Type):
    print "start"
    if OS_Type == "W1":
        print "Pinging in Windows"
        print os.system("ping -n %s %s > %s" % (no, ip, name))
        time.sleep(2)
    elif OS_Type == "RH":
        print "Pinging in Linux"
        print os.system("ping  %s > %s" % (ip, name))
        time.sleep(2)
    else:
        print "Please provide valid OS_Type value to ping"


def startthread(no, server_IPs_global, name, OS_Type):
    q = Queue.Queue()
    t1 = [threading.Thread(target=checkservicehealth, args=(no, i['ip1'], j['name'], k['OS']))
          for i, j, k in map(None, server_IPs_global, name, OS_Type)]
    for thread in t1:
        thread.start()
    for thread in t1:
        thread.join()


def Remove_Whitespace(instring):
    return instring.strip()
