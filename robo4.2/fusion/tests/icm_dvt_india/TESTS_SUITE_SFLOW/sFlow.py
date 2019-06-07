#!/usr/bin/env python

###########################################################################
# sFlow.py
# All the functions required during
# sFlow feature execution are defined in this file.
###########################################################################

import sys
import paramiko
import re
import time
from RoboGalaxyLibrary.utilitylib import logging


def ifNameIndex(*input):
    ifnameDict = {}
    DictValues = re.findall("IF-MIB::ifName.(\d+)\s+=\s+STRING:\s+([^S].*)\n", input[0])
    if(DictValues != []):
        for value in DictValues:
            ifnameDict[value[1]] = value[0]
    print ifnameDict
    if not ifnameDict:
        print ("ERROR: ifName Dictionary is Empty!!!")
        return False
    elif input[1] in ifnameDict:
        return(ifnameDict[input[1]])
    else:
        print ("ERROR: Given Counter Poller Interface does not present in Potash!!! Please provide valid Interface")
        return False


def Get_CounterPoller_Details(input):

    PollingStatus = re.findall("Counter Poller Polling Status\s+:\s+(.*)\r\r\n", input)
    CounterPollerStatus = re.findall("Counter Poller Status\s+:\s+(.*)\r\r\n", input)
    CounterPollerTXCount = re.findall("Counter Poller TX Count\s+:\s+(.*)\r\r\n", input)

    if PollingStatus[0] == 'Polling' and CounterPollerStatus[0] == 'Enabled':
        return CounterPollerTXCount[0]
    else:
        return False


def Get_FlowSampler_Details(input):
    FlowSamplingStatus = re.findall("Flow Sampler Sampling Status\s+:\s+(.*)\r\r\n", input)
    SamplerStatus = re.findall("Flow sampler Status \s+:\s+(.*)\r\r\n", input)
    FlowSamplerTXCount = re.findall("Flow Sampler TX Count\s+:\s+(.*)\r\r\n", input)

    if FlowSamplingStatus[0] == 'Sampling' and SamplerStatus[0] == 'Enabled':
        return FlowSamplerTXCount[0]
    else:
        return False
