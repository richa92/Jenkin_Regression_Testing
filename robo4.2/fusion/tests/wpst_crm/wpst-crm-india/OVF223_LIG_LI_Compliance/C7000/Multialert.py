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
import itertools
from robot.libraries.BuiltIn import BuiltIn
# from FusionLibrary.api.common.request import HttpVerbs
import paramiko


class Multialert(object):
    # FVT_CRM_India: F702- The below functions are specific to F702 test execution related to Cisco APIC

    def combine_sublist(self, event_item_values):
        Combinedlist = []
        for i in event_item_values:
            Combinedlist += i
        return Combinedlist
