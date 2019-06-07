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


class snmp_tbird(object):
    # FVT_CRM_India: OVfF292- The below functions are specific to OVF292 test execution related to Synergy snmpv3

    def filter_default_users(self, datalist):
        # This function is to validate the Management Ip displayed in Leaf switches of CiscoAPIC
        FilteredList = []
        filter_words = ['templateMD5', 'templateSHA', 'noAuthUser', 'OneView', 'netop']
        data = datalist.splitlines()
        for line in data:
            if not any(filter_word in line for filter_word in filter_words):
                logger.info("Line is %s" % line)
                FilteredList.append(line)
        return FilteredList
