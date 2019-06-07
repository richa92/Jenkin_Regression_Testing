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


class twofaloginfunction(object):

    def twofa_login_function(self, api_version, file_location, appip):

        logger.info("Fucntion to verify 2FA through curl")
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = "15.212.136.29"
        username = "root"
        password = "hpvse1"
        port = 22
        command = 'curl -i -X POST -H "Accept-Language:en-US" -H "X-Api-Version:%s" --cert %s https://%s/rest/login-sessions/smartcards -k' % (api_version, file_location, appip)
        client.connect(hostname, port=port, username=username, password=password)
        chan = client.invoke_shell()
        BuiltIn().sleep(10)
        logger._log_to_console_and_log_file('Executing %s' % command)
        input, output, error = client.exec_command(command)
        data = output.read()
        d = data.split("\n")
        return d
