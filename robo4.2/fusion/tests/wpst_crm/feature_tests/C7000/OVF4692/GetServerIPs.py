'''
This module will be executed in the linux / unix environment
It will be used / called by the server_operations.py
This module will return the Ethernet n/w Ip's of the server
by logging to the OA.
'''


import pexpect
import time
import argparse
import re


parser = argparse.ArgumentParser(description="ssh into the OA")
parser.add_argument('-i', '--ipaddress', help="OA IP of the Enclosure")
parser.add_argument('-u', '--username', help="OA username of the Enclosure")
parser.add_argument('-p', '--password', help="Password of the Enclosure")
parser.add_argument('-b', '--bayno', help="Bay number of the server")
args = parser.parse_args()


def get_server_ips():

    pexp_obj = pexpect.spawn("ssh " + args.username + "@" + args.ipaddress + "\n")
    pexp_obj.expect(".* password: ")
    pexp_obj.send(args.password + "\r")
    pexp_obj.expect(".*> ")
    pexp_obj.send("connect server " + args.bayno + "\r")
    time.sleep(10)
    pexp_obj.expect(".*> ")
    pexp_obj.send("vsp\r")
    pexp_obj.expect('SAC>')
    pexp_obj.send("i\r")
    pexp_obj.expect('SAC>')
    print (pexp_obj.after)
    s = pexp_obj.before
    print (s)
    pexp_obj.close()


if __name__ == '__main__':
    get_server_ips()
