#!/usr/sbin/python
# Blame: Eric Conrad (eric.conrad@hpe.com)
# 2/27/2018
#
# Parse the tbrid-em-credentials.json file for the EM serial numbers and IPv6 addresses
# This script should be run from the TCS server that has access to the appliance

import os
import argparse
import ast

ip = ''
datadict = {}


def argSetup():
    global ip
    parser = argparse.ArgumentParser(description="Retrieve EM serial numbers and IPv6 addresses")
    parser.add_argument("-i", "--ip", "--i", dest="ip", help="Applicance IPv4 address", default=ip, required=True)
    args = parser.parse_args()
    ip = args.ip


def getjson():
    os.system("scp root@%s:/ci/pre-ha-data/tbird/tbird-em-credentials.json ." % ip)


def filetodict():
    global datadict
    with open('tbird-em-credentials.json', 'r') as f:
        s = f.read()
        datadict = ast.literal_eval(s)


def outputdata():
    for x in range(0, len(datadict['credentials'])):
        print "Serial Number: %s ..... IPv6 Address: %s" % (datadict['credentials'][x]['sn'], datadict['credentials'][x]['ipAddr'])

if __name__ == '__main__':
    argSetup()
    getjson()
    filetodict()
    outputdata()
