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

class apic(object):
    # FVT_CRM_India: F702- The below functions are specific to F702 test execution related to Cisco APIC

    def loginApic(self, host, cred):
        import json
        import requests

        base_url = 'https://%s/api/' % (host)
        json_credentials = json.dumps(cred)
        # log in to API
        login_url = base_url + 'aaaLogin.json'
        resp = requests.post(login_url, data=json_credentials, verify=False)
        logger._log_to_console_and_log_file("Resp is %s" % resp)
        logger._log('Response is %s' % (resp), level='DEBUG')
        auth = json.loads(resp.text)

        logger._log_to_console_and_log_file("Auth is %s" % auth)
        login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
        logger._log_to_console_and_log_file("Auth is %s" % login_attributes)
        token = login_attributes['token']
        logger._log("Token is %s" % token)
        return token

    def Apic_FabricNode_get(self, APPLIANCE_IP, token, IPList):
        # This function will get the fabric nodes and validate the nodes Ip returned is equal to the IPList passed in this function
        import json
        import requests
        error = 0
        requestObj = HttpVerbs()
        GETurl = 'https://%s/api/node/class/fabricLooseNode.json' % (APPLIANCE_IP)
        cookies = {}
        cookies['APIC-Cookie'] = token
        logger._log("url is %s" % GETurl)
        Getresponse = requests.get(GETurl, cookies=cookies, verify=False)
        response = Getresponse.json()
        logger._log("json response is %s" % response)
        nodecount = response['totalCount']
        logger._log("node count is %s" % int(nodecount))
        nodeiplists = []
        i = 0
        j = int(nodecount) - 1
        while i <= j:
            if 'imdata' in response:
                imdata = response['imdata']
                fabricnode = imdata[i]
                fabricLooseNode = fabricnode['fabricLooseNode']
                attributes = fabricLooseNode['attributes']
                id = str(attributes['id'])
                if (id != '78:48:59:61:39:63' and id != '169.254.57.19' and id != '10.10.5.185' and id != '10.10.0.208' and id != '15.212.137.13' and id != '15.212.137.14' and id != '15.212.137.17' and id != '15.212.137.18' and id != '15.212.137.18' and id != '15.212.137.19' and id != '15.212.137.20' and id != '15.212.137.21' and id != '15.212.137.22'):
                    nodeiplists.append(id)
                i = i + 1
                continue
        logger._log('Node ip list from json Response is %s' % nodeiplists)
        nodeiplists1 = ",".join(nodeiplists)
        logger._log('Node ip list from data file is  %s' % IPList)
        if nodeiplists1 in IPList:
            logger._log("NodeIp list  matches %s" % nodeiplists1)
        else:
            logger._log("NodeIp list did not match %s" % nodeiplists1)
            error = error + 1
        if error != 0:
            logger._log("Node Ip did not match ")
            return False

    def leaf_validate(self, switch):
        # This function is to validate the Management Ip displayed in Leaf switches of CiscoAPIC
        import paramiko

        error = 0
        client = None
        logger.info('Entering prompt')
        logger.info("Message is %s" % switch.command)
        command = switch.command
        command1 = switch.command1
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        hostname = switch.hostname
        username = switch.username
        password = switch.password
        ip_list_exp = [(switch.ip1), (switch.ip2)]
        logger.info("ip list is %s" % ip_list_exp)
        port = 22
        ip_list = []
        client.connect(hostname, port=port, username=username, password=password)
        chan = client.invoke_shell()
        BuiltIn().sleep(5)
        chan.send(command + '\n')
        BuiltIn().sleep(5)
        chan.send(command1 + '\n')
        resp = chan.recv(999)
        BuiltIn().sleep(5)
        logger.info('Response is %s' % resp)
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
                matchtemp = line.split(":")
                ip1 = str(matchtemp[1].strip())
                logger.info("ip is %s" % ip1)
                ip_list.append(ip1)
                logger.info("ip list is %s" % ip_list)
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
                matchtemp = line.split(":")
                ip2 = matchtemp[1].strip()
                logger.info("ip is %s" % ip2)
                ip_list.append(ip2)
                logger.info("ip list is %s" % ip_list)
        # Sleep for console to return the output
        BuiltIn().sleep(5)
        chan.send('exit \n')
        client.close()

        for ip in ip_list:
            if ip in ip_list_exp:
                logger.info("Ip compared %s" % ip)
                logger.info("Ip Expected compared %s" % ip_list_exp)
                return True
            else:
                logging._warn("Ip mismatch")
                error += 1
        if error > 0:
            return False
        return True

    def validate_Apic_topology(self, APPLIANCE_IP, token, APIC_TOPOLOGY, NodeIp):
    # This function will get the fabric nodes and validate the nodes Ip returned is equal to the IPList passed in this function
        import json
        import requests
        error = 0
        requestObj = HttpVerbs()
        GETurl = 'https://%s/api/node/mo/topology/lsnode-%s.json?query-target=children&target-subtree-class=fabricLooseAttLink' % (APPLIANCE_IP,NodeIp)
        cookies = {}
        cookies['APIC-Cookie'] = token
        logger._log("url is %s" % GETurl)
        Getresponse = requests.get(GETurl, cookies=cookies, verify=False)
        response = Getresponse.json()
        logger._log("json response is %s" % response)
        nodecount = response['totalCount']
        logger._log("node count is %s" % int(nodecount))
        i = 0
        j = int(nodecount) - 1
        if int(nodecount) > 0:
            while i <= j:
                if 'imdata' in response:
                    imdata = response['imdata']
                    fabricnode = imdata[i]
                    fabricLooseNode = fabricnode['fabricLooseAttLink']
                    attributes = fabricLooseNode['attributes']
                    hostDn = str(attributes['hostDn'])
                    logger._log("Host DN from response is %s"%hostDn)
                    logger._log("Expected toplogy is %s"%APIC_TOPOLOGY)
                    if hostDn:
                        if str(hostDn) == str(APIC_TOPOLOGY):
                            logger._log("Topology graph established %s"%hostDn)
                        else:
                            return False
                    else:
                        return False
                    i = i + 1
                    continue
            return True
        else:
            return False