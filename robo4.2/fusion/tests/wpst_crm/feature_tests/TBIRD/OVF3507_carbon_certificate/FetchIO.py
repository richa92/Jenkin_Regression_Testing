'''
This module will be executed in the linux / unix environment
It will be used / called by the server_operations.py
This module will read the results file of diskspd execution
from the SAC command prompt of the server and return the results
'''
import pexpect
import time
import argparse
import os
import re
from nntplib import CRLF

parser = argparse.ArgumentParser(description="ssh into the iLO")
parser.add_argument('-i', '--ipaddress', help="iLO IP of the Server")
parser.add_argument('-u', '--username', help="Username of iLO")
parser.add_argument('-p', '--password', help="Password of iLO")
parser.add_argument('-us', '--serverusername', help="Username of Server")
parser.add_argument('-ps', '--serverpassword', help="Password of Server")
# parser.add_argument('-o', '--outputfile', help="diskspd output file")
args = parser.parse_args()


def fetch_io():
    path = "cd C:\\Users\\Administrator\\Desktop\\Diskspd" + CRLF
    list_file = "dir /b *.txt" + CRLF
    child = pexpect.spawn("ssh " + args.username + "@" + args.ipaddress + "\n")
    child.expect(".* password: ")
    child.send("hpvse123" + "\r")
    child.expect(".*hpiLO-> ")
    child.send("stop /system1/oemhp_VSP1" + "\r")
    time.sleep(2)
    child.expect(".*hpiLO-> ")
    child.send("vsp\r")
    index = child.expect(['SAC>', '.*Diskspd>', pexpect.TIMEOUT])
    if not index == 0:
        child.send("\x1b\t\t\r")
        time.sleep(3)
        child.expect('SAC>')
    child.send("ch -ci 1\r")
    child.expect('SAC>')
    child.send("cmd\r")
    child.expect('SAC>')
    child.send("ch -si 1\r")
    child.send("\r")
    child.expect('Username:')
    child.send(args.serverusername + "\r")
    child.expect('Domain  :')
    child.send("\r")
    child.expect('Password:')
    child.send(args.serverpassword + "\r")
    child.expect('.*H')
    for x in path:
        child.send(x)
        time.sleep(1)
    child.expect('.*>')
    child.expect('.*H')
    child.send("cls" + CRLF)
    child.expect('.*>')
    child.send("cls" + CRLF)
    for y in list_file:
        child.send(y)
        time.sleep(1)
    time.sleep(3)
    child.expect('.*>')
    file_name = child.after
    file_name = file_name.strip()
    file = re.search("\d+-\d+-\d+-\d+_output.txt", file_name)
    cmd = "TYPE " + file.group(0) + CRLF
    for z in cmd:
        child.send(z)
        time.sleep(1)
    time.sleep(3)
    child.expect('.*>')
    s = child.after
    child.send("\x1b\t\t\r")
    time.sleep(3)
    child.expect('SAC>')
    child.send("\x1b(\r")
    time.sleep(3)
    child.expect('</>hpiLO->')
    print (s)
    child.close()
    return (s)
if __name__ == '__main__':
    fetch_io()
