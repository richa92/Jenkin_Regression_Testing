#!/usr/bin/env python

###########################################################################
# InternalFunctions.py
# All the Internal functions required during
# Potash Functional Automation Testing should be defined in this file.
###########################################################################
import sys
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
    ssh.connect(host, username=user, password=password, port=22)
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
    ssh_cmd = "mv -f /root/.ssh/known_hosts /root/.ssh/know_hostsorg; ssh -o StrictHostKeyChecking=no " + potash_user + "@" + potash_ip + "\n"
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


def Download_ICM_Firmware(linuxip, user, password, firmwareurl, firmwareupdatepackage, PotashIP1, PotashIP2, randompassword):

    ssh = ssh_connect(linuxip, user, password)

    channel = ssh.invoke_shell()
    time.sleep(7)
    channel.send("ls\n")
    time.sleep(5)
    cmd = "wget " + firmwareurl + "package.json " + "\r"
    channel.send(cmd)
    time.sleep(10)
    cmd = "wget " + firmwareurl + firmwareupdatepackage + "\r"
    channel.send(cmd)
    time.sleep(60)

    cmd = "/bin/cp -rf " + firmwareupdatepackage + " hpe_icm.pkg " + "\r"
    channel.send(cmd)
    time.sleep(5)

    cmd = "scp hpe_icm.pkg -o StrictHostKeyChecking=no OneView@" + PotashIP1 + ":/upload " + "\r"
    channel.send(cmd)
    time.sleep(5)
    channel.send("yes" + "\r")
    time.sleep(2)
    channel.send(randompassword + "\r")
    time.sleep(2)

    cmd = "scp package.json -o StrictHostKeyChecking=no OneView@" + PotashIP1 + ":/upload " + "\r"
    channel.send(cmd)
    time.sleep(5)
    channel.send("yes" + "\r")
    time.sleep(2)
    channel.send(randompassword + "\r")
    time.sleep(4)

    cmd = "scp hpe_icm.pkg -o StrictHostKeyChecking=no OneView@" + PotashIP2 + ":/upload " + "\r"
    channel.send(cmd)
    time.sleep(5)
    channel.send("yes" + "\r")
    time.sleep(2)
    channel.send(randompassword + "\r")
    time.sleep(4)

    cmd = "scp package.json  -o StrictHostKeyChecking=no OneView@" + PotashIP2 + ":/upload " + "\r"
    channel.send(cmd)
    time.sleep(5)
    channel.send("yes" + "\r")
    time.sleep(2)
    channel.send(randompassword + "\r")
    time.sleep(2)

    cmd_output = channel.recv(20000)
    print cmd_output

    return cmd_output
