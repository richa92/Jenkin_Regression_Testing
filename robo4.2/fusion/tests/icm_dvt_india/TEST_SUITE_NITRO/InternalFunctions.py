#!/usr/bin/env python

###########################################################################
# InternalFunctions.py
# All the Internal functions required during
# Potash Functional Automation Testing should be defined in this file.
###########################################################################
import sys
import os
import string
import paramiko
import time


##########################################################################
# This function returns OID of Interface.
# Complete list of all OIDs passed as arguments to this function.
##########################################################################
def oid_of_interface(all_oids, Interface):
    print Interface
    print all_oids
    for single_oid in all_oids.split('\n'):
        print single_oid
        if (Interface in single_oid):
            oid_interface = single_oid.split('IF-MIB::ifName.')[1].split(' =')[0]
            print oid_interface
            return oid_interface
    return "NULL"

##########################################################################
# This function is used to do ssh connect using Paramiko library
##########################################################################


def ssh_connect(host, user, password):
    print (host + user + password)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password, port=22, allow_agent=False, look_for_keys=False)
    time.sleep(5)
    return ssh

##########################################################################
# This function is used to execute a cmd using ssh object created from
# paramiko library
##########################################################################


def execute_cmd(ssh, cmd):
    channel = ssh.invoke_shell()
    time.sleep(5)
    channel.send(cmd + "\n")
    time.sleep(20)
    cmd_output = channel.recv(8000)
    print cmd_output
    return cmd_output

##########################################################################
# This function tests whether we can ssh to ICM from appliance
##########################################################################


def ssh_icm(ssh, potash_ip, potash_user, potash_random_password):
    channel = ssh.invoke_shell()
    time.sleep(7)
    channel.send("ls\n")
    time.sleep(5)
    ssh_cmd = "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o GSSAPIAuthentication=no " + potash_user + "@" + potash_ip + "\n"
    print ssh_cmd
    channel.send(ssh_cmd)
    time.sleep(5)
    channel.send(potash_random_password + "\n")
    time.sleep(5)
    cmd_output = channel.recv(15000)
    print cmd_output
    return cmd_output

###############################################################################
# This function closes the ssh object previously created using paramiko library
###############################################################################


def ssh_close(ssh):
    ssh.close()

###############################################################################
# This function used to capture ping command output through Psexec command
###############################################################################


def execute_windows_commands(ip, username, passwd, pingip):

    build_cmd = "start psexec \\\\" + ip + " -u " + username + " -p " + passwd + " ping " + pingip + " -t -w 1 > trafficOut.txt"
    print build_cmd
    output = os.system(build_cmd)
    return output


###############################################################################
# This function logs into server in sac prompt and executes commands,
# And used in issu feature.
###############################################################################
def serverlogin(SERVERIP, SERVERUSER, SERVERPASSWORD, SERVERDOMAINPWD, cmd):
    ssh = ssh_connect(SERVERIP, SERVERUSER, SERVERPASSWORD)

    channel = ssh.invoke_shell()
    time.sleep(7)
    channel.send("ls\n")
    time.sleep(5)
    channel.send("stop /system1/oemhp_vsp1" + "\r")
    time.sleep(5)
    channel.send("vsp" + "\r")
    time.sleep(5)
    cmd_output = channel.recv(15000)
    print cmd_output

    if (("system32" in cmd_output) or
            ("Desktop" in cmd_output) or
            ("ISSURESULTS" in cmd_output)):
        print "Directly Logged in:"
        channel.send(cmd + "\r")
        time.sleep(5)
        cmd_output = channel.recv(15000)
        print cmd_output
        return cmd_output

    print "SAC PROMPT"
    channel.send("\r")
    time.sleep(5)
    channel.send("cmd" + "\r")
    time.sleep(5)
    channel.send("ch -si 1" + "\r")
    time.sleep(10)
    channel.send("\r")
    time.sleep(5)
    channel.send(SERVERUSER + "\r")
    time.sleep(5)
    channel.send("\r")
    time.sleep(5)
    channel.send(SERVERDOMAINPWD + "\r")
    time.sleep(5)

    channel.send("\r")
    time.sleep(5)
    channel.send(cmd + "\r")
    time.sleep(5)
    cmd_output = channel.recv(15000)
    print cmd_output
    return cmd_output

###############################################################################
# This function is used to download packages for issu firmware upgrade
###############################################################################


def Download_ICM_Firmware(linuxip, user, password, firmwareurl, firmwareupdatepackage, NitroIP):

    ssh = ssh_connect(linuxip, user, password)

    channel = ssh.invoke_shell()
    time.sleep(7)
    channel.send("cd /root/dump\n")
    time.sleep(5)
    cmd = "wget " + firmwareurl + "package.json " + "\r"
    channel.send(cmd)
    time.sleep(10)
    cmd = "wget " + firmwareurl + firmwareupdatepackage + "\r"
    channel.send(cmd)
    time.sleep(60)


def Copy_Firmware_to_ICM(linuxip, user, password, firmwareurl, firmwareupdatepackage, NitroIP):

    ssh = ssh_connect(linuxip, user, password)

    channel = ssh.invoke_shell()
    time.sleep(7)
    channel.send("cd /root/dump\n")
    cmd = "mv -f /root/.ssh/known_hosts /root/.ssh/know_hostsorg; scp -o StrictHostKeyChecking=no " + firmwareupdatepackage + " fwupdate@[" + NitroIP + "]:. " + "\r"
    channel.send(cmd)
    time.sleep(5)
    #channel.send("yes" + "\r")
    #time.sleep (2)
    channel.send("fwupdate" + "\r")
    time.sleep(7)

    cmd = "mv -f /root/.ssh/known_hosts /root/.ssh/know_hostsorg; scp -o StrictHostKeyChecking=no package.json  fwupdate@[" + NitroIP + "]:. " + "\r"
    channel.send(cmd)
    time.sleep(5)
    #channel.send("yes" + "\r")
    #time.sleep (2)
    channel.send("fwupdate" + "\r")
    time.sleep(4)

    cmd_output = channel.recv(20000)
    print cmd_output
    return cmd_output

###############################################################################
# Update ICM Firmware using release notes
###############################################################################


def FirmwareUpgrade_Release_Notes(linuxip, user, password, firmwareurl, firmwareupdatepackage, NitroIP):

    ssh = ssh_connect(linuxip, user, password)

    channel = ssh.invoke_shell()
    time.sleep(7)
    channel.send("cd /root/dump\n")
    time.sleep(5)

    cmd = "mv -f /root/.ssh/known_hosts /root/.ssh/know_hostsorg; ssh -o StrictHostKeyChecking=no fwupdate@" + NitroIP + " apply.update " + firmwareupdatepackage + "\r"
    channel.send(cmd)
    time.sleep(4)
    channel.send("fwupdate" + "\r")
    time.sleep(200)

    cmd = "mv -f /root/.ssh/known_hosts /root/.ssh/know_hostsorg; ssh -o StrictHostKeyChecking=no fwupdate@" + NitroIP + " activate.update \r"
    channel.send(cmd)
    time.sleep(4)
    channel.send("fwupdate" + "\r")
    time.sleep(200)

    cmd_output = channel.recv(20000)
    print cmd_output
    return cmd_output

###############################################################################
# Below functions are used in SNMPV3 scripts
###############################################################################


def GetAsciiValue(username):
    return '.'.join((str(ord(char)) for char in username))


def HexvalueForIP(ip):
    print ip


def GetUserNames(out):
    # out = 'SNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."netop" = STRING: netop\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."OneView" = STRING: OneView\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUbblI" = STRING: HPEUbblI\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUcFlh" = STRING: HPEUcFlh\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUdzcO" = STRING: HPEUdzcO\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUdztG" = STRING: HPEUdztG\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUelXi" = STRING: HPEUelXi\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUesyE" = STRING: HPEUesyE\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUhfOm" = STRING: HPEUhfOm\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUhrjs" = STRING: HPEUhrjs\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUiJgj" = STRING: HPEUiJgj\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUibEH" = STRING: HPEUibEH\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUjinz" = STRING: HPEUjinz\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUjnak" = STRING: HPEUjnak\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUktqD" = STRING: HPEUktqD\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUkwnn" = STRING: HPEUkwnn\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUlurV" = STRING: HPEUlurV\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUlvFv" = STRING: HPEUlvFv\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUmILa" = STRING: HPEUmILa\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUmTky" = STRING: HPEUmTky\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUmjeR" = STRING: HPEUmjeR\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUmkgs" = STRING: HPEUmkgs\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUnHTN" = STRING: HPEUnHTN\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUoaXJ" = STRING: HPEUoaXJ\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUoggN" = STRING: HPEUoggN\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUrFiM" = STRING: HPEUrFiM\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUskkA" = STRING: HPEUskkA\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUsyxP" = STRING: HPEUsyxP\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUtwzS" = STRING: HPEUtwzS\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUvElu" = STRING: HPEUvElu\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUvFAK" = STRING: HPEUvFAK\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUwQge" = STRING: HPEUwQge\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUyGgi" = STRING: HPEUyGgi\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."HPEUzPCe" = STRING: HPEUzPCe\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."noAuthUser" = STRING: noAuthUser\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."templateMD5" = STRING: templateMD5\nSNMP-USER-BASED-SM-MIB::usmUserSecurityName.".....\\..(.."."templateSHA" = STRING: templateSHA'
    out1 = out.split('\n')
    # print out1
    listUser = []
    for line in out1:
        # print line
        user = line.split("STRING: ")
        listUser.append(user[1].strip())
    listUser.remove('netop')
    listUser.remove('noAuthUser')
    listUser.remove('templateMD5')
    listUser.remove('templateSHA')
    listUser.remove('OneView')
    return listUser
