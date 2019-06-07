'''
This module will be executed in the linux / unix environment
It will be used / called by the server_operations.py
This module will run the diskspd command from the SAC command prompt
of the server and return the results output file.
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
parser.add_argument('-c', '--diskcmd', help="diskspd command")
args = parser.parse_args()


def perform_io():
    path = "cd C:\\Users\\Administrator\\Desktop\\Diskspd" + CRLF
    cmd = args.diskcmd + CRLF
    child = pexpect.spawn("ssh " + args.username + "@" + args.ipaddress + "\n")
    index = child.expect(".* (yes/no)?")
    if index == 0 or index == 1:
        child.send("yes" + "\r")
    child.expect(".* password: ")
    child.send("hpvse123" + "\r")
    child.expect(".*hpiLO-> ")
    child.send("stop /system1/oemhp_VSP1" + "\r")
    time.sleep(2)
    child.expect(".*hpiLO-> ")
    child.send("vsp" + "\r")
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
    child.send("\r")
    child.expect('.*>')
    for x in path:
        child.send(x)
        time.sleep(2)
    child.expect('.*>')
    child.expect('.*H')
    child.send("cls" + CRLF)
    child.expect('.*>')
    for y in cmd:
        child.send(y)
        time.sleep(2)
    time.sleep(20)
    index = child.expect(['.*Starting IO Test', '.*mapped!', pexpect.TIMEOUT])
    if index == 0 or index == 1:
        s = child.after
    print(s)
    child.send("\x1b\t\t\r")
    time.sleep(3)
    child.expect('SAC>')
    child.send("\x1b(\r")
    time.sleep(3)
    child.expect('</>hpiLO->')
    child.close()
    return (s)
if __name__ == '__main__':
    perform_io()

'''
    #child.send("PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s.ps1"+CRLF)
    #child.send(".\\diskspd.exe -c1G -d60 -r -w0 -t6 -o16 -b8K -h -L D:\\TestDiskSpd\\testfile.dat >.\\output.txt"+CRLF)
'''
