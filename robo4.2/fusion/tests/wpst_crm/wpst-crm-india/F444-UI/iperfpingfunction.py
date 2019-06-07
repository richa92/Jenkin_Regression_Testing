#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.api.common.request import HttpVerbs
import requests
from RoboGalaxyLibrary.data import test_data
import sys
import json
import re
import os
import types
import imp
import copy
from robot.libraries.BuiltIn import BuiltIn
import paramiko

class iperfpingfunction(object):

    def server_ipassignment_ping(self, server_obj):
        ''' This function is exclusively written to handle the case where it will login to the server with ssh ip mentioned
    in the data file for the server. Then it performs a series of actions like grepping for the interface using mac address
    and assigning ip to it, after assigning it runs ping to the other server ip mentioned in the datafile. This function is written to
    execute ping commands and also iperf commands depending on the "action" option selecetd by the user in data file,.

    Arguments:
        commmand = requirement specific command for iperf/ping
        command1 = requirement specific command for iperf/ping
        command2 = requirement specific command for iperf/ping
        command3 = requirement specific command for iperf/ping
        command4 = requirement specific command for iperf/ping
        command5 = requirement specific command for iperf/ping
        iLoip = server ip to ssh to the server
        username = username of ssh
        password = password for ssh session
        action = enter the action you want here i,e., either iperf/ping

        Example od Data file:
        For ping:
         <server iLOIP="10.10.3.125" username="root" password="hpvse1" action = "ping" command="ifconfig -a|grep -i -B 2 D0:BF:9C:03:BB:96|cut -d ' ' -f 1|sed 's/:$//'>interface|echo $?"
          command1="ip addr flush `cat interface`|echo $?" command2="ifconfig `cat interface` 80.0.0.5 netmask 255.0.0.0 up|echo $?" command3="ping -c 5 80.0.0.15"
          command4="service firewalld stop"  command5="ping -c 5 80.0.0.15|echo $?"/>

         For iperf:
        <server iLOIP="10.10.3.125" username="root" password="hpvse1" action = "iperf" command="ip route list|grep -i default|cut -d ' ' -f 3 > defaultgw"
        command1="route del default gw `cat defaultgw`" command2="route add default gw 60.0.0.15|echo $?"  command3="service firewalld stop"
        command4="iperf3 -b 5g -c 60.0.0.15" command5="echo $?"/>
     '''

        
        if hasattr(server_obj, "command"):
            logger._log_to_console_and_log_file('Entering prompt')  
                           
        command = server_obj.command
        command1 = server_obj.command1
        command2 = server_obj.command2
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        hostname = server_obj.iLOIP
        username = server_obj.username
        password = server_obj.password
        port = 22
        client.connect(hostname, port=port, username=username, password=password)
        # open channel to the leaf node
        chan = client.invoke_shell()
        BuiltIn().sleep(10)
        logger._log_to_console_and_log_file('Executing %s' %command)
        chan.send(command + '\n')
        resp = chan.recv(999)
        BuiltIn().sleep(5)
        logger._log_to_console_and_log_file('Response is %s' %resp)
        logger._log_to_console_and_log_file('Executing %s' %command1)
        chan.send(command1 + '\n')
        BuiltIn().sleep(5)
        resp = chan.recv(999)
        BuiltIn().sleep(5)
        logger._log_to_console_and_log_file('Response is %s' %resp)
        logger._log_to_console_and_log_file('Executing %s' %command2)
        chan.send(command2 + '\n')
        resp = chan.recv(999)
        BuiltIn().sleep(5)
        logger._log_to_console_and_log_file('Response is %s' %resp)
        command3 = server_obj.command3
        command4 = server_obj.command4
        command5 = server_obj.command5
        logger._log_to_console_and_log_file('Executing %s' %command3)
        BuiltIn().sleep(5)
        chan.send(command3 + '\n')
        BuiltIn().sleep(5)
        data1 = chan.recv(999)
        logger._log_to_console_and_log_file("Data is %s"%data1)
        logger._log_to_console_and_log_file('Executing %s' %command4)
        BuiltIn().sleep(5)
        chan.send(command4 + '\n')
        BuiltIn().sleep(5)
        data1 = chan.recv(999)
        logger._log_to_console_and_log_file("Data is %s"%data1)
        logger._log_to_console_and_log_file('Executing %s' %command5)
        BuiltIn().sleep(5)
        chan.send(command5 + '\n')
        BuiltIn().sleep(5)
        datareceived = chan.recv(999)
        iscommandsuccess = datareceived.splitlines()[1]
        logger._log_to_console_and_log_file("Command sucess value is %s" %iscommandsuccess)
        action = server_obj.action
        logger._log_to_console_and_log_file("Action performed is %s" %action)
        if(action == "ping"):
            if iscommandsuccess != '0':
                logger._log_to_console_and_log_file("Seems ping is not working")
                chan.send('exit \n')
                return False
            else:
                logger._info("ping is successfull")
                chan.send('exit \n')
                return True
        if(action == "iperf"):
            fullreport = data1.splitlines()[-1]
            bandwidth = fullreport.split()[6]
            logger._log_to_console_and_log_file("bandwidth is: %s" %bandwidth)           
            return bandwidth
            client.close()