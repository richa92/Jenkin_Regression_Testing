#!/usr/local/bin/python
import json
# from RoboGalaxyLibrary.utilitylib import logging as logger
# from RoboGalaxyLibrary.utilitylib import logging
from robot.api import logger
import requests
# from RoboGalaxyLibrary.data import test_data
import sys
import json
import re
import os
import types
import imp
import copy
from robot.libraries.BuiltIn import BuiltIn
# from FusionLibrary.api.common.request import HttpVerbs
import paramiko


class apic(object):
    # FVT_CRM_India: F702- The below functions are specific to F702 test execution related to Cisco APIC

    def leaf_validate(self, switch, ip_addr_list, mode):
        # This function is to validate the Management Ip displayed in Leaf switches of CiscoAPIC
        import paramiko

        error = 0
        client = None
        logger.info('Entering prompt')
        # command = switch.command
        # command1 = switch.command1
        logger.info('mode is %s' % mode)

        if(mode == "enablelldp"):
            # logger.info('inside lldp')
            ip_list_exp = [(ip_addr_list[0]), (ip_addr_list[0])]

        elif(mode == "poweroff"):
            # logger.info('inside loop')
            ip_list_exp = [(ip_addr_list[0])]
            logger.info('ip exp is %s' % ip_list_exp)

        elif(mode == "disablelldp"):
            # logger.info('inside disableloop')
            ip_list_exp = [(ip_addr_list[0]), (ip_addr_list[0])]

        elif(mode == "efuse"):
            # logger.info('inside efuseloop')
            ip_list_exp = [(ip_addr_list[0])]
        else:
            logger.info("no ip passed")

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        hostname = switch.hostname
        username = switch.username
        password = switch.password

        port = 22
        ip_list = []
        client.connect(hostname, port=port, username=username, password=password)
        chan = client.invoke_shell()
        BuiltIn().sleep(5)
        # chan.send(command + '\n')
        # BuiltIn().sleep(5)
        # chan.send(command1 + '\n')
        # resp = chan.recv(999)
        # BuiltIn().sleep(5)
        # logger.info('Response is %s' % resp)
        command2 = switch.command2
        logger.info('Executing %s' % command2)
        chan.send(command2 + '\n')
        BuiltIn().sleep(15)
        datalist = chan.recv(99999)
        logger.info("Data is %s" % datalist)
        data = datalist.splitlines()
        for line in data:
            line = line.strip()
            match1 = re.match("Management", line)
            if match1:
                logger.info("Match line is %s" % line)
                matchtemp = line.split(" ")
                logger.info("MatchTemp is %s" % matchtemp)
                ip1 = str(matchtemp[2].strip())
                logger.info("ip is %s" % ip1)
                ip_list.append(ip1)
                logger.info("ip listdata is %s" % ip_list)
        command3 = switch.command3
        logger.info('Executing %s' % command3)
        chan.send(command3 + '\n')
        # Sleep for console to return the output
        BuiltIn().sleep(10)
        datalist = chan.recv(99999)
        logger.info("Response is %s" % datalist)
        data = datalist.splitlines()
        for line in data:
            line = line.strip()
            match1 = re.match("Management", line)
            if match1:
                logger.info("Match line is %s" % line)
                matchtemp = line.split(" ")
                ip2 = str(matchtemp[2].strip())
                logger.info("ip is %s" % ip2)
                ip_list.append(ip2)
                logger.info("ip listresponse is %s" % ip_list)
        # Sleep for console to return the output
        BuiltIn().sleep(5)
        chan.send('exit \n')
        client.close()

        if ip_list == ip_list_exp:
            return True
        else:
            logger.info("Ip mismatch")
            return False

    def management_address_output(self, datalist):
        # This function is to retrieve the management address TLV value
        data = datalist.splitlines()
        for line in data:
            line = line.strip()
            match1 = re.match("Management Address:", line)
            if match1:
                logger.info("Match line is %s" % line)
                matchtemp = line.split(" ")
                ip1 = str(matchtemp[2].strip())
                logger.info("ip is %s" % ip1)

        return ip1

    def management_address_output_both_modes(self, datalist):
        # This function is to retrieve the management address TLV value
        data = datalist.splitlines()
        ip_list = []
        for line in data:
            line = line.strip()
            match1 = re.match("Management Address:", line)
            if match1:
                matchtemp = line.split(" ")
                ip1 = str(matchtemp[2].strip())
                logger.info("ip is %s" % ip1)
                ip_list.append(ip1)
        return ip_list
