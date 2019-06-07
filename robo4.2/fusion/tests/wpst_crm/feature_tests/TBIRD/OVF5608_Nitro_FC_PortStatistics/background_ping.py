import time
import re
import os
import threading


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    Execute any windows commands
    '''
    try:
        build_cmd = "psexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + wcmd
        output = os.system(build_cmd)
        return output
    except Exception as e:
        return e


def execute_traffic(ip, username, passwd, wcmd):
    io_thread = threading.Thread(target=execute_windows_commands, args=(ip, username, passwd, wcmd))
    io_thread.start()


def execute_traffic_list(ip_list, username, passwd, wcmd):
    io_thread1 = threading.Thread(target=execute_windows_commands, args=(ip_list[0], username, passwd, wcmd))
    io_thread1.start()
    io_thread2 = threading.Thread(target=execute_windows_commands, args=(ip_list[1], username, passwd, wcmd))
    io_thread2.start()
