'''
This module will be executed in the linux / unix environment
It will be used / called by the server_operations.py
This module will read the results file of diskspd execution
from the SAC command prompt of the server and return the results
'''
import pexpect
import time
import argparse
from nntplib import CRLF

parser = argparse.ArgumentParser(description="ssh into the iLO")
parser.add_argument('-i', '--ipaddress', help="iLO IP of the Server")
parser.add_argument('-u', '--username', help="Username of iLO")
parser.add_argument('-p', '--password', help="Password of iLO")
parser.add_argument('-us', '--serverusername', help="Username of Server")
parser.add_argument('-ps', '--serverpassword', help="Password of Server")
parser.add_argument('-o', '--outputfile', help="diskspd output file")
args = parser.parse_args()


def fetch_io():
    child = pexpect.spawn("ssh " + args.username + "@" + args.ipaddress + "\n")
    child.expect(".* password: ")
    child.send(args.password + "\r")
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
    child.send("cd C:\\Users\\Administrator\\Desktop\\Diskspd" + CRLF)
    child.expect('.*H')
    child.send("cls" + CRLF)
    child.expect('.*>')
    child.send("TYPE " + args.outputfile + CRLF)
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
