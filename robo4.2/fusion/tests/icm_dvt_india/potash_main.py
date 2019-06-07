#!/usr/bin/env python

#############################################################################
# potash_main.py
# Main Automation suite file to trigger features like
# PrivateNetworks , AuditLogging, SNMPV3enhancements
#############################################################################

import sys
import os
import string
import time
import potash_privatenetworks
import potash_auditlogging
import potash_snmpv3enhancements
import potash_1gbsupport
############################################################################
# if there are no command line arguments
# then Execute all the sections by default
# Example - ./potash_main.py
#
# Example - ./potash_main.py PRIVATENETWORKS
# In this case only the PRIVATENETWORKS feature gets executed
#
#############################################################################
if (len(sys.argv) > 5):
    print "Arguments passed to script are not correct. \n"
    print "Example1: python potash_main.py \n"
    print "Example2: python potash_main.py AUDITLOGGING. \n"
    print "Example3: python potash_main.py AUDITLOGGING PRIVATENWTWORKS SNMPV3ENHANCEMENTS 1GBSUPPORT. \n"
    sys.exit()


command_line_arguments = str(sys.argv)

execute_all = "false"
if (len(sys.argv) == 1):
    execute_all = "true"

if ((execute_all == "true") or ("PRIVATENETWORKS" in command_line_arguments)):
    potash_privatenetworks.execute_tests()
if ((execute_all == "true") or ("AUDITLOGGING" in command_line_arguments)):
    potash_auditlogging.execute_tests()
if ((execute_all == "true") or ("SNMPV3ENHANCEMENTS" in command_line_arguments)):
    potash_snmpv3enhancements.execute_tests()
if ((execute_all == "true") or ("1GBSUPPORT" in command_line_arguments)):
    potash_1gbsupport.execute_tests()
