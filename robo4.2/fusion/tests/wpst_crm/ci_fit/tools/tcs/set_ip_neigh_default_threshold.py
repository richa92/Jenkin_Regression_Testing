#!/usr/bin/python
"""
Edits /etc/sysctl.conf and set the values for net.ipv4.neigh.default.gc_thresh{1,2,3} to the values specified in the command-line.

Example:
    ./set_ip_neigh_default_threshold.py -m ipv4 -t1 8192 -t2 32768 -t3 65536


Author: Jason Mascarinas Pernito <jason.mas.pernito@hpe.com>

HPE CI-FIT Testing Tools

(C) Copyright 2019 Hewlett-Packard Development Company, L.P.
All Rights Reserved
"""


import argparse
import os
import re
import fileinput
import sys

MODE = "ipv4"
THRESHOLD1 = "8192"
THRESHOLD2 = "32768"
THRESHOLD3 = "65536"


def parseArguments():
    """
        Parse command line arguments and set global variables for it.
    """
    global MODE, THRESHOLD1, THRESHOLD2, THRESHOLD3

    parser = argparse.ArgumentParser(description="Script reads the /etc/sysctl.conf file and update or set the default threshold to what was specified in the command line arguments.")
    parser.add_argument("-m", "--ipmode", dest="MODE", help="[Optional] IP Mode of threshold to set", default=MODE, required=False)
    parser.add_argument("-t1", "--threshold1", dest="THRESHOLD1", help="[Optional] Threshold 1", default=THRESHOLD1, required=False)
    parser.add_argument("-t2", "--threshold2", dest="THRESHOLD2", help="[Optional] Threshold 2", default=THRESHOLD2, required=False)
    parser.add_argument("-t3", "--threshold3", dest="THRESHOLD3", help="[Optional] Threshold 3", default=THRESHOLD3, required=False)

    args = parser.parse_args()
    MODE = args.MODE
    THRESHOLD1 = args.THRESHOLD1
    THRESHOLD2 = args.THRESHOLD2
    THRESHOLD3 = args.THRESHOLD3


if __name__ == "__main__":
    parseArguments()

    cmd_args = {
        'ipv4': {
            'net.ipv4.neigh.default.gc_thresh1': THRESHOLD1,
            'net.ipv4.neigh.default.gc_thresh2': THRESHOLD2,
            'net.ipv4.neigh.default.gc_thresh3': THRESHOLD3
        },
        'ipv6': {
            'net.ipv6.neigh.default.gc_thresh1': THRESHOLD1,
            'net.ipv6.neigh.default.gc_thresh2': THRESHOLD2,
            'net.ipv6.neigh.default.gc_thresh3': THRESHOLD3
        }
    }

    found = {}
    for sysctl in fileinput.input("/etc/sysctl.conf", inplace=True):
        sysctl.rstrip('\n')
        if not re.match(r'.*=.*', sysctl):
            sys.stdout.write(sysctl)
            continue
        [key, sep, val] = sysctl.partition("=")
        val = val.strip()
        pristine_key = key
        key = key.strip()
        if key in cmd_args[MODE].keys():
            sysctl = "%s %s %s\n" % (key, sep, cmd_args[MODE][key])
            found[key] = val
        sys.stdout.write(sysctl)
    with open("/etc/sysctl.conf", "a") as f:
        for k in cmd_args[MODE].keys():
            if k in found:
                continue
            else:
                f.write("%s = %s\n" % (k, cmd_args[MODE][k]))

    returned_value = os.system("sysctl -p")
    print('returned value:', returned_value)
