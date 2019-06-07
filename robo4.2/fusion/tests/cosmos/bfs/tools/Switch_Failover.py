import paramiko
import os
import sys

from paramiko import SSHClient
from time import sleep
from RoboGalaxyLibrary.utilitylib import logging as log


def connect_to_remote_hp5900Switch(ip, port, username, password):
    try:
        log.info("Connecting to HP5900 Switch....")
        ssh = paramiko.Transport((ip, port))
        ssh.connect(username=username, password=password)
        return ssh
    except paramiko.AuthenticationException:
        log.info("Authentication Failed")
        quit()
    except:
        log.info("Unable to connect to Remote machine using SSH")
        quit()


def close_connection(ssh):
    try:
        log.info("Closing Connection HP5900 Switch")
        ssh.close()
    except:
        log.info("Could not close connection")
        quit()


def execute_command_on_switch(ssh, command):
    try:
        nbytes = 4096
        stdout_data = []
        stderr_data = []
        session = ssh.open_channel(kind='session')
        session.exec_command(command)
        paramiko.util.log_to_file("filename.log")
        sleep(2)
        while True:
            if session.recv_ready():
                stdout_data.append(session.recv(nbytes))
            if session.recv_stderr_ready():
                stderr_data.append(session.recv_stderr(nbytes))
            if session.exit_status_ready():
                break
        log.info('exit status: ', session.recv_exit_status())
        log.info(''.join(stdout_data))
        return stdout_data
        session.close()
    except:
        log.info("Command exit with error")


def turn_on_port_switch_hp5900(ssh, port_name):
    search = "UP"
    log.info("Turn on Port " + port_name)
    execute_command_on_switch(
        ssh, 'system-view \n interface ' + port_name + '\n undo shutdown \n quit \n quit')
    log.info("Breath in & out for 20 seconds")
    sleep(20)
    value = execute_command_on_switch(
        ssh, 'system-view \n interface ' + port_name + '\n display interface ' + port_name + ' brief \n quit \n quit')
    for each_value in value:
        log.info(each_value + "\n")
        if each_value.find(search) != -1:
            log.info("Port " + port_name + "is successfully turned on")
            break
        else:
            continue
    close_connection(ssh)


def turn_off_port_switch_hp5900(ssh, port_name):
    search = "ADM"
    log.info("Turn off Port " + port_name)
    value = execute_command_on_switch(
        ssh, 'system-view \n interface ' + port_name + '\n shutdown \n display interface ' + port_name + ' brief \n quit \n quit')
    for each_value in value:
        log.info(each_value + "\n")
        if each_value.find(search) != -1:
            log.info("Port " + port_name + "is successfully turned off")
            break
        else:
            continue
    close_connection(ssh)

if __name__ == "__main__":
    if(len(sys.argv) <= 6):
        log.info("Not enough arguements Please Supply Switch_IP, Switch_Port, Switch_username, Switch_Password, Port_Name(eg:Ten-GigabitEthernet1/0/7), Port_State=0/1(Where 0 - Off, 1- ON)")
        exit()
    ssh = connect_to_remote_hp5900Switch(
        sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4])
    if sys.argv[6] == '1':
        turn_on_port_switch_hp5900(ssh, sys.argv[5])
    else:
        turn_off_port_switch_hp5900(ssh, sys.argv[5])
