#!/usr/local/bin/python
# ----------------------------------------------------------------------------
# (C) Copyright 2017 Hewlett Packard Enterprise Development LP
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Description
# ----------------------------------------------------------------------------
# This script performs "shutdown" and then "undo shutdown" repeatly, until the
# /root/stop_toggle file exist, on the provide interfaces.
# It initial targets for HPE 5900CP, 5900AF, and 5930 switches only with the
# following FCoE modes: FCF, and NPV
#
# Usage:
#   ./ports_toggle.py <IP> <user> <password> <interface> [interface ...]
#
# Assumption:
#   System is in the good condition.  All VFCs attached to the target toggle
#   interfaces are up.
#
# e.g.
# ./ports_toggle.py 15.186.x.x admin password FortyGigE1/0/50 FortyGigE2/0/50
# ./ports_toggle.py 15.186.x.x admin password Bridge-Aggregation3
#   Bridge-Aggregation4
# ./ports_toggle.py 15.186.x.x admin password Ten-GigabitEthernet1/0/29
#   Ten-GigabitEthernet1/0/30 Ten-GigabitEthernet1/0/31
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Switch Port Toggle TODO List
#
# Add and track key TODO items here for the Switch Port Toggle
# ----------------------------------------------------------------------------
# - Support Cisco Nexus and/or other switches if needed
# - Handle CLI's unrecognized command properly in execute_clis()
# - May need to handle other HPE FCoE modes in get_switch_type() if applicable
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------
import threading
import paramiko
import argparse
import re
import os
import time
from time import gmtime, strftime

# ----------------------------------------------------------------------------
# ssh Class
# ----------------------------------------------------------------------------


class ssh:
    shell = None
    client = None
    output = None
    interval = 2

    # ------------------------------------------------------------------------
    # init
    # ------------------------------------------------------------------------
    def __init__(self, ip_address, username, password):
        print ("Connecting to switch ip ... {0}").format(str(ip_address))
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(
            paramiko.client.AutoAddPolicy())
        retry_count = 1
        retry = 3
        while True:
            try:
                # initiate SSH connection
                self.client.connect(ip_address, username=username,
                                    password=password, look_for_keys=False)
                print("\nSSH connection established successfully to {0}")\
                    .format(ip_address)
                break
            except Exception as e:
                print e
                if retry_count < retry:
                    retry_count += 1
                    time.sleep(self.interval)
                else:
                    print ("\nERROR: Unable to connect to {0} after {1} retries")\
                        .format(ip_address, retry)
                    exit(1)

    # ------------------------------------------------------------------------
    # closeConnection
    # ------------------------------------------------------------------------
    def closeConnection(self):
        if(self.client is not None):
            self.client.close()

    # ------------------------------------------------------------------------
    # openShell
    # ------------------------------------------------------------------------
    def openShell(self):
        try:
            # Establish a SSH interactive session
            self.shell = self.client.invoke_shell()
            self.output = self.shell.recv(1024)
        except Exception as e:
            print ("\nERROR: Unable to establish a SSH interactive session.\n "
                   "{0} ").format(e)

    # ------------------------------------------------------------------------
    # sendShell
    # ------------------------------------------------------------------------
    def sendShell(self, command):
        if(self.shell):
            try:
                self.shell.send("\n" + command)
                time.sleep(self.interval)
                while not self.shell.recv_ready():
                    f.write("NOT READY " + str(self.shell.recv_ready()) + ", \
                            wait for couple seconds\n\n")
                    time.sleep(self.interval)
                self.output = self.shell.recv(65000)
            except Exception as e:
                print ("\nERROR: Unable to send the \"{0}\" command via SSH"
                       " connection.\n {1} ").format(command, e)
                exit(1)
        else:
            print ("\nERROR: Shell not opened.\n")
            exit(1)

# ----------------------------------------------------------------------------
# delete_proxy_environment_variables
#
# Delete proxy environment to avoid delay if exist
# ----------------------------------------------------------------------------


def delete_proxy_environment_variables():

    delete_environment_variable("http_proxy")
    delete_environment_variable("https_proxy")
    delete_environment_variable("HTTP_PROXY")
    delete_environment_variable("HTTPS_PROXY")

    return

# ----------------------------------------------------------------------------
# delete_environment_variable
#
# Delete environment variable
# ----------------------------------------------------------------------------


def delete_environment_variable(environment_variable):

    if os.environ.get(environment_variable) is None:
        # Doesn't exist
        return

    del os.environ[environment_variable]

    return

# ----------------------------------------------------------------------------
# disable_paging
#
# Disable paging on a router/switch
# ----------------------------------------------------------------------------


def disable_paging(remote_conn, cmd):

    remote_conn.sendShell(cmd)
    f.write(remote_conn.output)

# ----------------------------------------------------------------------------
# convert_port
#
# Convert HPE switch short interface name (e.g. FGE) to long interface
#   (e.g. FortyGigE).
#   e.g.  Convert from FGE2/0/50 to FortyGigE2/0/50
# ----------------------------------------------------------------------------


def convert_port(if_str):

    # Convert XGE/XGE/BAGG to FortyGigE/Ten-GigabitEthernet/Bridge-Aggregation
    if_type = re.search(r'[A-Za-z]+', if_str)
    if if_type:
        for k, v in hpe_ifs_conv.items():
            if if_type.group(0) in v:
                break
        if_name = re.sub(hpe_ifs_conv[k], k, if_str)
        return if_name
    else:
        f.write("WARNING: abbreviate interface name %s not found" % if_str)
        return None

# ----------------------------------------------------------------------------
# Create_if_to_vfc
#
# Create interface-to-vfcs dictionary based on the "display interface vfc
#   brief | inc UP" command before starting the test.
#   e.g. FGE1/0/50 = ['Vfc3', 'Vfc4', 'Vfc5', 'Vfc6', 'Vfc11', 'Vfc13',
#                     'Vfc17', 'Vfc19']
# ----------------------------------------------------------------------------


def create_if_to_vfc(outcome):

    vfs_out = filter(None, outcome.splitlines())

    for i in vfs_out:
        # pos0=all, pos1=vfc#, pos2=i/f
        vfcs = re.search(r'(Vfc[0-9]+).*UP +([A-Za-z]+[0-9\/]+)', i)
        if vfcs:
            if vfcs.group(2) in if_to_vfc:
                # Append vfc to the list if it is not in the list
                if vfcs.group(1) not in if_to_vfc[vfcs.group(2)]:
                    if_to_vfc[vfcs.group(2)].append(vfcs.group(1))
            else:
                # Create one
                if_to_vfc[vfcs.group(2)] = [vfcs.group(1)]
            vfs_interface = convert_port(vfcs.group(2))

# ----------------------------------------------------------------------------
# Execute CLIs
#
# Execute the CLI commands
# ----------------------------------------------------------------------------


def execute_clis(cli_list, out_screen=False):

    for cli in cli_list:
        try:
            conn.sendShell(' %s \n' % cli)
            if out_screen:
                print (conn.output)
            f.write(conn.output)
            if cli == vfc_up_brief[0] and not if_to_vfc:
                create_if_to_vfc(conn.output)
        except Exception as e:
            # TODO: handle CLI's unrecognized command properly
            # e.g. [CI-FIT-I5-Top] system-view
            #                      ^
            #       % Unrecognized command found at '^' position.
            print ("\nWARNING: Executing \"{0}\" with following error\n {1} ")\
                .format(cli, e)
            f.write("\nWARNING: Executing \"%s\" with following error\n %s "
                    % (cli, e))
    if not if_to_vfc:
        print (">>> ERROR: if_to_vfc = %s is empty.  No Vfc interface UP.  "
               "Make sure your connections are connected.").format(if_to_vfc)
        f.write(">>> ERROR: if_to_vfc = %s is empty.  No Vfc interface UP. "
                "Make sure your connections are connected." % if_to_vfc)
        exit(1)

# ----------------------------------------------------------------------------
# get_switch_type
#
# Get the switch type and set corresponding CLI commands
# ----------------------------------------------------------------------------


def get_switch_type():

    global switch_type
    global show_word
    global if_disable
    global config_mode
    global login_cli
    global vfc_up_brief
    global vfc_brief
    global if_brief
    global exec_mode

    clis = None
    switch = re.search(r'Hewlett[ -]Packard', conn.output)
    print (switch)
    if switch:
        switch_type = "HPE"
        show_word = "display"
        if_disable = "undo"
        config_mode = ['system-view']
        vfc_up_brief = ['display int vfc brief | inc UP']
        vfc_brief = ['display int vfc brief']
        if_brief = ['display int brief']
        exec_mode = ['quit']
        conn.sendShell('display version | inc "Switch uptime"\n')
        f.write(conn.output)
        switch = re.search(r'([0-9]+)([A-Z]*)-(.*) Switch uptime', conn.output)
        if switch:
            f.write("\n>>> Switch type: %s%s" % (switch.group(1),
                                                 switch.group(2)))
        else:
            print ("WARNING: Unable to get the HPE switch type.")
            f.write("WARNING: Unable to get the HPE switch type.")

        # TODO: May need to handle other FCoE modes in the future
        conn.sendShell('display fcoe-mode\n')
        f.write(conn.output)
        mode = re.search(r' ([A-Z]+)\.', conn.output)
        if mode:
            # For now, expected the FCoE mode is NONE|NPV|FCF
            fcoe_mode = mode.group(1)
            f.write("\n>>> FCoE mode: %s" % fcoe_mode)
            print ("\n>>> FCoE mode: {0}").format(fcoe_mode)
            if fcoe_mode == "FCF":
                login_cli = ['display fc login', ]
            elif fcoe_mode == "NPV":
                login_cli = ['display npv login', ]
            clis = ['display current-configuration', ] + if_brief + vfc_brief \
                + vfc_up_brief + login_cli
        else:
            print ("WARNING: FCoE mode: <empty>")
            f.write("WARNING: FCoE mode: <empty>")
        paging_cmd = "screen-length disable\n"
    elif cisco_switch == re.search(r'cisco', conn.output, re.I):
        # TODO: Handle Cisco switch scenario
        switch_type = "Cisco"
        show_word = "show"
        if_disable = "no"
        config_mode = ['configure terminal']
        if_brief = ['show int brief']
        vfc_brief = ['show int brief | inc vfc']
        login_cli = ['show flogi database']
        exec_mode = ['exit', 'exit']
        f.write("\n>>> Cisco switch type: %s" % switch.group(0))
        conn.sendShell('show version | inc Chassis\n')
        print (conn.output)
        f.write(conn.output)
        switch = re.search(r'(Cisco) ([0-9A-Z]*) Chassis', conn.output, re.I)
        if siwtch:
            # pos1: Cisco, pos2: Nexus5548
            f.write("\n>>> Switch type: %s%s" % (switch.group(1),
                                                 switch.group(2)))
            paging_cmd = "terminal length 0\n"
        else:
            f.write("WARNING: Unable to get the Cisco switch type.")
            print ("WARNING: Unable to get the Cisco switch type.")
        clis = ['show running-config', ] + if_brief + vfc_brief + vfc_up_brief \
            + login_cli

        conn.sendShell('show fcoe\n')
        f.write(conn.output)
        mode = re.search(r'Global ([A-Z]+)\.', conn.output)
        if mode:
            fcoe_mode = mode.group(1)
            f.write("\n>>> FCoE mode: %s" % fcoe_mode)
            print ("\n>>> FCoE mode: {0}").format(fcoe_mode)
        else:
            print ("WARNING: FCoE is not enabled")
            f.write("WARNING: FCoE is not enabled")
            exit(1)

    else:
        print ("ERROR: Unable to get the switch type.")
        exit(1)

    # Turn off paging
    disable_paging(conn, paging_cmd)

    return clis

# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
if __name__ == '__main__':

    # Dictionary definition
    if_to_vfc = dict()
    hpe_ifs_conv = {"FortyGigE": "FGE",
                    "Ten-GigabitEthernet": "XGE",
                    "Bridge-Aggregation": "BAGG",
                    "M-GigabitEthernet": "M-GE",
                    }

    # List definition
    vfc_up_brief = []
    vfc_brief = []
    if_brief = []
    login_cli = []
    config_mode = []
    exec_mode = []

    # Variable definition
    dname = os.path.basename(__file__)
    dname = os.path.splitext(dname)[0]
    test_time = strftime("%F_%T", gmtime())
    mylog = "/tmp/%s/%s/%s.log" % (dname, test_time, dname)
    stop_file = "/root/stop_toggle"
    f = None
    loop_count = 1
    switch_type = ""
    show_word = ""
    if_disable = ""
    wait_interval = 5

    delete_proxy_environment_variables()

    parser = argparse.ArgumentParser()

    parser.add_argument("switch_ip", type=str,
                        help="The IP address of the switch")
    parser.add_argument("switch_user", type=str,
                        help="The admin login username for switch")
    parser.add_argument("switch_password", type=str,
                        help="The admin login password for switch")
    parser.add_argument("interfaces", nargs='+',
                        help="Required at least one interface")

    args = parser.parse_args()
    ifs = args.interfaces

    if os.path.exists(stop_file):
        os.remove(stop_file)

    directory = os.path.dirname(mylog)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Connect to the switch
    conn = ssh(args.switch_ip, args.switch_user, args.switch_password)
    conn.openShell()

    # Open log file
    f = open(mylog, 'a')

    # check switch product name
    clis = get_switch_type()

    # Execute list of CLI commands
    execute_clis(clis)

    while not os.path.exists(stop_file):
        # loop through each provided interfaces each iteration
        print ("\n######################################")
        print ("Iteration {0}:: {1}").format(loop_count, time.ctime())
        print ("Touch the {0} file to stop script").format(stop_file)
        print ("######################################")
        f.write("\n######################################")
        f.write("\nIteration %s:: %s" % (loop_count, time.ctime()))
        f.write("\n######################################")

        # FortyGigE1/0/50 => FGE1/0/50
        # FGE1/0/50  =  ['Vfc3', 'Vfc4', 'Vfc5', 'Vfc6', 'Vfc11', 'Vfc13',
        #                'Vfc15', 'Vfc17', 'Vfc19']
        for i in ifs:
            conn.sendShell('%s interface %s brief\n' % (show_word, i))
            print (conn.output)
            f.write(conn.output)

            print ("\n###### Port toggle down on the interface %s #####")\
                .format(i)
            f.write("\n\n###### Port toggle down the interface %s #####" % i)
            toggle_clis = vfc_up_brief + config_mode + \
                ['interface %s' % i, 'shutdown', ] + vfc_up_brief

            execute_clis(toggle_clis)

            print ("\n###### Verify interface {0} is down #####").format(i)
            f.write("\n\n###### Verify interface %s is down #####" % i)
            conn.sendShell('%s interface %s brief\n' % (show_word, i))
            f.write(conn.output)

            if_shutdown = re.search(r'DOWN|ADM', conn.output)
            if if_shutdown:
                print (">>> The interface {0} is down, it's in {1} state")\
                    .format(i, if_shutdown.group(0))
                f.write("\n>>> The interface %s is down, it's in %s state" %
                        (i, if_shutdown.group(0)))
            else:
                print (">>> FAIL: target interface did not shutdown properly")
                f.write(
                    "\n>>> FAIL: target interface did not shutdown properly")
                exit(1)

            print ("\n###### Port toggle up on the interface {0} #####")\
                .format(i)
            f.write("\n\n###### Port toggle up the interface %s #####" % i)
            toggle_clis = vfc_up_brief + ['%s shutdown' % if_disable, ] \
                + exec_mode

            execute_clis(toggle_clis)

            print ("\n###### Wait for {0}'s attached VFC interfaces are up "
                   "#####").format(i)
            f.write("\n\n###### Wait for %s's attached VFC interfaces are up"
                    " #####" % i)
            inter_ptr = re.search(r'[A-Za-z\-]+', i)
            inter = re.sub(
                inter_ptr.group(0),
                hpe_ifs_conv[
                    inter_ptr.group(0)],
                i)

            if_down = list(if_to_vfc[inter])

            retry = 0
            while if_down and retry <= 5:
                conn.sendShell(' %s \n' % vfc_up_brief[0])
                f.write(conn.output)
                for vfc in if_down:
                    tmp_if = re.search(vfc, conn.output)
                    if tmp_if:
                        print (">>> {0} interface is UP").format(vfc)
                        f.write("\n>>> %s interface is UP" % vfc)
                        if_down.remove(vfc)
                    else:
                        print (">>> {0} interface is still DOWN, sleep for {1}"
                               " seconds").format(vfc, wait_interval)
                        f.write(
                            "\n>>> %s interface is still DOWN, sleep for %s "
                            "seconds" % (vfc, wait_interval))
                        time.sleep(wait_interval)
                retry += 1

            if if_down and retry <= 5:
                print (">>> FAIL: At least one VFC interface {0} is still not "
                       "up after {1} re-try ").format(if_down, retry)
                f.write(
                    "\n>>> FAIL: At least one VFC interface %s is still not "
                    "up after %s re-try " %
                    (if_down, retry))
                exit(1)

            print ("\n###### Verify interface {0} is up #####").format(i)
            f.write("\n\n###### Verify interface %s is up #####" % i)
            inter_convert = convert_port(inter)
            conn.sendShell(
                '%s interface %s brief\n' %
                (show_word, inter_convert))
            f.write(conn.output)
            if_up = re.search(r'UP', conn.output)
            if if_up:
                print (">>> Interface {0} is up").format(inter)
                f.write("\n>>> Interface %s is up" % inter)
            else:
                print (">>> FAIL: Interface {0} is not up").format(inter)
                f.write("\n>>> FAIL: Interface %s is not up" % inter)
                exit(1)

            print (
                "\n###### All VFC interface(s) should be up and login #####")
            f.write("\n\n###### All VFC interface(s) should be up and "
                    "login #####")
            toggle_clis = vfc_up_brief + login_cli + exec_mode
            execute_clis(toggle_clis, True)

            loop_count += 1

    f.close()
    conn.closeConnection()
