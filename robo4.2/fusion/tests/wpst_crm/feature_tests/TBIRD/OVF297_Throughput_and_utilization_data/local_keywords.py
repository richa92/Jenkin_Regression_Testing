#!/usr/local/bin/python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import paramiko
import logging
import sys
import tempfile
import os
import re
import time
import string
from os import write
libLogger = "api-logger"
from robot.libraries.BuiltIn import BuiltIn


def vaildate_port_statistics(port_no, output,total_samples,expected_samples):
	list_val = [output['portStatistics'][i] for i in range(len(output['portStatistics'])) if output['portStatistics'][i]['portName'] == port_no]
	keys_list =  ['receiveKilobytesPerSec','transmitKilobytesPerSec','receivePacketsPerSec','transmitPacketsPerSec']
	return_output = {}
	s = []
	for i in keys_list:
		attr_values = list_val[0]['advancedStatistics'][i].split(':')
		if len(attr_values) != int(total_samples) :
			return False, " Failed to verify the number of samples, it is not matching with the expected number of samples"
		else:
			return_output[i]=list_val[0]['advancedStatistics'][i].split(':')
	return	True, return_output
