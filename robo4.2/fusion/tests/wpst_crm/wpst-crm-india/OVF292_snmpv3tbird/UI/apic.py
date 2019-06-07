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

    def filter_default_users(self, datalist):
        # This function is to validate the Management Ip displayed in Leaf switches of CiscoAPIC
        FilteredList = []
        filter_words = ['templateMD5', 'templateSHA', 'noAuthUser', 'OneView', 'netop']
        data = datalist.splitlines()
        for lines in data:
            if not any(filter_word in lines for filter_word in filter_words):
                logger.info("Line is %s" % lines)
                FilteredList.append(lines)
        return FilteredList
