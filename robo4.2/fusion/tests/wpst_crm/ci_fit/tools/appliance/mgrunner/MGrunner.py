#!/usr/local/bin/python
"""
.. module:: runmg.py
   :platform: Linux
   :synopsis: This is utility that reads an ini file and
              then starts the echo servers on the target.
              After the echo servers have started it
              then starts the MG-console on the targets.

.. moduleauthor:: Bobby Suber <bobby.suber@hp.com>

(C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""

# #######################################################################
#              Import modules and classes                              #
# #######################################################################
import sys
import os
import argparse
import tempfile
import string
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import paramiko
from os import write
from scp import SCPClient
# from RoboGalaxyLibrary.api.wpst_crm.lib.cicsecuritymodule import LoginSession
import pdb

# #######################################################################
#                    Global Constants/Variables                        #
# #######################################################################
IC_USER = "Administrator"
IC_IP = ""
IC_PW = "hpvse123"
SERVER_NAME = ""

UNAME = "root"
PW = "rootpwd"

SSH_ECHO_OPTS = "DISPLAY=:0 nohup screen -S \'Echo Server\' -d -m"
SSH_MG_OPTS = "DISPLAY=:0 nohup screen -S \'MG-Console\' -d -m"
ECHO_SERVER = "/root/tools/LinuxMG_2.610_x86-64/EtdNetworkEchoServer"
INI_DIR = ""
MG_DIR = "/root/tools/LinuxMG_2.610_x86-64"
MG_CONSOLE = "MG-console"
MG_LOG_DIR = MG_DIR + "/logs/"
MG_OPTS = "-ascii -nologo -nodrivers -logfrequency=1 -ini="
flowOption = None
MGIniFile = []


# #######################################################################
#                    Functions                                         #
# #######################################################################


def getCmdLineParam():
    """
    :py:func:`getCmdLineParam` uses the argparse module to parse the command line parameters

    **Parameters**:
         -f <Meatgrinder master configuration ini file>

    """

    global INI_FILE, IC_USER, IC_IP, IC_PW, SERVER_NAME, INI_DIR, flowOption

    parser = argparse.ArgumentParser(description="runmg.py is used to deploy MG ini files and run echo servers as well as MG.")
    parser.add_argument("-f", "--inifile", "--f", dest="INI_FILE", help="The master MG ini file", required=True)
    parser.add_argument("-i", "--ip", "--i", dest="IC_IP", help="IP address of the IC appliance. Example: -i 15.186.7.148'", default=IC_IP, required=False)
    parser.add_argument("-u", "--user", "--u", dest="IC_USER", help="Administrator IC username", default=IC_USER, required=False)
    parser.add_argument("-p", "--password", "--p", dest="IC_PW", help="Administrator IC password", default=IC_PW, required=False)
    parser.add_argument("-o", "--option", "--o", dest="flowOption", help="The flow option to use for this run",
                        choices=['runAll', 'runAllEcho', 'runAllMG', 'runEcho', 'runMG', 'killMG', 'killEcho', 'killAllEcho', 'killAllMG', 'getMGStatus', 'cleanAllLogs'], required=True)
    parser.add_argument("-s", "--server", "--s", dest="SERVER_NAME", help="The server name - i.e. CI-FIT-7-1", default=SERVER_NAME, required=False)
    parser.add_argument("-d", "--dir", "--d", dest="INI_DIR", help="The directory where the mg ini files are located", default=INI_DIR, required=False)

    args = parser.parse_args()

    if args.INI_FILE:
        if os.path.isfile(args.INI_FILE):
            INI_FILE = args.INI_FILE
        else:
            print ("MG ini file does not exist")
            sys.exit(103)

    if args.flowOption == 'runMG' or args.flowOption == 'runEcho':
        if args.SERVER_NAME == "":
            parser.print_help()

    if args.flowOption == 'runAll' or args.flowOption == 'runAllMG' or args.flowOption == 'runMG':
        if args.INI_DIR == "":
            parser.print_help()

    IC_USER = args.IC_USER
    IC_IP = args.IC_IP
    IC_PW = args.IC_PW
    SERVER_NAME = args.SERVER_NAME
    INI_DIR = args.INI_DIR
    flowOption = args.flowOption

def readMasterMGIniFile(file):
    mgfile = file

    global MGIniFile

    try:
        linestring = open(mgfile)
    except Exception as e:
        msg = "Failed to open file %s" % (mgfile)
        logger.log.error(msg)
        raise Exception(msg, e)

    section = dict()
    keys = []
    for line in linestring:
        if '[' in line:
            if section.get('section') is None:
                section = dict()
                section['section'] = line
            else:
                section['keys'] = keys
                MGIniFile.append(section)
                section = dict()
                keys = []
                section['section'] = line
        else:
            keys.append(line)

    section['keys'] = keys
    MGIniFile.append(section)

    linestring.close()
    return


def runEchoServers(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'Echo Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    host = data[0]

                    try:
                        command = string.Template("$opt $echo")
                        command = command.substitute(opt=SSH_ECHO_OPTS, echo=ECHO_SERVER)
                        print('  %s, %s, %s' % (host, ip, command))

                        client = paramiko.SSHClient()
                        client.load_system_host_keys()
                        # client.set_missing_host_key_policy(paramiko.WarningPolicy())
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        hostname = ip
                        port = 22
                        client.connect(hostname, port=port, username=UNAME, password=PW)

                        stdin, stdout, stderr = client.exec_command(command)

                    except Exception as e:
                        msg = "Exception occured while attempting to send ssh command %s" \
                              % (command)
                        raise Exception(msg, e)
                    finally:
                        client.close()


def runAllMG(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'MeatGrinder Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    mgfile = data[0] + '.ini'

                    try:
                        scpfrom = string.Template("$dir/$mgfile")
                        scpfrom = scpfrom.substitute(dir=INI_DIR, mgfile=mgfile)
                        scpto = string.Template("$dir/$mgfile")
                        scpto = scpto.substitute(dir=MG_DIR, mgfile=mgfile)

                        client = paramiko.SSHClient()
                        client.load_system_host_keys()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        hostname = ip
                        port = 22
                        client.connect(hostname, port=port, username=UNAME, password=PW)

                        scp = SCPClient(client.get_transport())
                        print('  %s, %s, scp.put(%s, %s)' % (data[0], ip, scpfrom, scpto))
                        scp.put(scpfrom, scpto)

                        command = string.Template("$opt $mgdir/$mg $mg_opt$mgdir/$mgfile -start")
                        command = command.substitute(opt=SSH_MG_OPTS, mgdir=MG_DIR, mg=MG_CONSOLE,
                                                     mg_opt=MG_OPTS, mgfile=mgfile)
                        print('  %s, %s, %s' % (data[0], ip, command))
                        stdin, stdout, stderr = client.exec_command(command)

                    except Exception as e:
                        msg = "Exception occured while attempting to send scp.put command %s" \
                              % (scpfrom)
                        raise Exception(msg, e)
                    finally:
                        client.close()


def runMG(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'MeatGrinder Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    mgfile = data[0] + '.ini'

                    if SERVER_NAME == data[0]:

                        try:
                            scpfrom = string.Template("$dir/$mgfile")
                            scpfrom = scpfrom.substitute(dir=INI_DIR, mgfile=mgfile)
                            scpto = string.Template("$dir/$mgfile")
                            scpto = scpto.substitute(dir=MG_DIR, mgfile=mgfile)

                            client = paramiko.SSHClient()
                            client.load_system_host_keys()
                            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            hostname = ip
                            port = 22
                            client.connect(hostname, port=port, username=UNAME, password=PW)

                            scp = SCPClient(client.get_transport())
                            print('  %s, %s, scp.put(%s, %s)' % (data[0], ip, scpfrom, scpto))
                            scp.put(scpfrom, scpto)

                            command = string.Template("$opt $mgdir/$mg $mg_opt$mgdir/$mgfile -start")
                            command = command.substitute(opt=SSH_MG_OPTS, mgdir=MG_DIR, mg=MG_CONSOLE,
                                                         mg_opt=MG_OPTS, mgfile=mgfile)
                            print('  %s, %s, %s' % (data[0], ip, command))
                            stdin, stdout, stderr = client.exec_command(command)

                        except Exception as e:
                            msg = "Exception occured while attempting to send scp.put command %s" \
                                  % (scpfrom)
                            raise Exception(msg, e)
                        finally:
                            client.close()


def runEcho(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'Echo Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    mgfile = data[0] + '.ini'
                    host = data[0]

                    if SERVER_NAME == data[0]:

                        try:
                            command = string.Template("$opt $echo")
                            command = command.substitute(opt=SSH_ECHO_OPTS, echo=ECHO_SERVER)
                            print('  %s, %s, %s' % (host, ip, command))

                            client = paramiko.SSHClient()
                            client.load_system_host_keys()
                            # client.set_missing_host_key_policy(paramiko.WarningPolicy())
                            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            hostname = ip
                            port = 22
                            client.connect(hostname, port=port, username=UNAME, password=PW)

                            stdin, stdout, stderr = client.exec_command(command)

                        except Exception as e:
                            msg = "Exception occured while attempting to send ssh command %s" \
                                  % (command)
                            raise Exception(msg, e)
                        finally:
                            client.close()


def killMG(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'MeatGrinder Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')

                    if SERVER_NAME == data[0]:

                        try:
                            client = paramiko.SSHClient()
                            client.load_system_host_keys()
                            # client.set_missing_host_key_policy(paramiko.WarningPolicy())
                            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            hostname = ip
                            port = 22
                            client.connect(hostname, port=port, username=UNAME, password=PW)
                            stdin, stdout, stderr = client.exec_command("pkill -f \'MG-Console\'")

                        except Exception as e:
                            msg = "Exception occured while attempting to send ssh command %s" \
                                % (command)
                            raise Exception(msg, e)
                        finally:
                            client.close()


def killMGServers(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'MeatGrinder Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')

                    try:
                        client = paramiko.SSHClient()
                        client.load_system_host_keys()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        hostname = ip
                        port = 22
                        client.connect(hostname, port=port, username=UNAME, password=PW)
                        stdin, stdout, stderr = client.exec_command("pkill -f \'MG-Console\'")

                    except Exception as e:
                        msg = "Exception occured while attempting to send ssh command %s" \
                            % (command)
                        raise Exception(msg, e)
                    finally:
                        client.close()


def killEchoServers(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'Echo Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')

                    try:
                        client = paramiko.SSHClient()
                        client.load_system_host_keys()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        hostname = ip
                        port = 22
                        client.connect(hostname, port=port, username=UNAME, password=PW)
                        stdin, stdout, stderr = client.exec_command("pkill -f \'EtdNetworkEchoServer\'")

                    except Exception as e:
                        msg = "Exception occured while attempting to send ssh command %s" \
                            % (command)
                        raise Exception(msg, e)
                    finally:
                        client.close()


def killEcho(MGIniFile):

    for section in xrange(0, int(len(MGIniFile))):
        if 'Echo Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')

                    if SERVER_NAME == data[0]:
                        try:
                            client = paramiko.SSHClient()
                            client.load_system_host_keys()
                            # client.set_missing_host_key_policy(paramiko.WarningPolicy())
                            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            hostname = ip
                            port = 22
                            client.connect(hostname, port=port, username=UNAME, password=PW)
                            stdin, stdout, stderr = client.exec_command("pkill -f \'EtdNetworkEchoServer\'")

                        except Exception as e:
                            msg = "Exception occured while attempting to send ssh command %s" \
                                % (command)
                            raise Exception(msg, e)
                        finally:
                            client.close()


def deleteLogs(ip, process):

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = ip
        port = 22
        client.connect(hostname, port=port, username=UNAME, password=PW)
        #command = string.Template("rm -rf $MG_LOG_DIR*.jrt")
        command = string.Template("rm -rf $MG_LOG_DIR*")
        command = command.substitute(MG_LOG_DIR=MG_LOG_DIR)
        stdin, stdout, stderr = client.exec_command(command)

    except Exception as e:
        msg = "Exception occured while attempting to delete the MG log files %s" \
            % (command)
        raise Exception(msg, e)
    finally:
        client.close()

def getStatus(ip, process):

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        # client.set_missing_host_key_policy(paramiko.WarningPolicy())
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = ip
        port = 22
        client.connect(hostname, port=port, username=UNAME, password=PW)
        command = string.Template("ps -aef | grep \"$process\" | grep -v \"grep\"")
        command = command.substitute(process=process)

        stdin, stdout, stderr = client.exec_command(command)
        if len(stdout.read()) > 0:
            status = "Running"
        else:
            status = "Not Running"

    except Exception as e:
        msg = "Exception occured while attempting to send ssh command %s" \
            % (command)
        raise Exception(msg, e)
    finally:
        client.close()

    return status


def getMgStatus(ip, process):

    mgprogDict = {'ctime': '00:00', 'rtime': '00:00', 'stime': '00:00',
                  'ttests': '0', 'terrors': '0', 'twarns': '0'
                  }

    statusDict = {'status': 'Unknown', 'runtime': 'Unknown',
                  'mgprogfile': 'Unknown', 'mgprog': mgprogDict
                  }

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        # client.set_missing_host_key_policy(paramiko.WarningPolicy())
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = ip
        port = 22
        client.connect(hostname, port=port, username=UNAME, password=PW)
        command = string.Template("ps -aef | grep \"$process\" | grep -v \"grep\"")
        command = command.substitute(process=process)
        stdin, stdout, stderr = client.exec_command(command)

        if len(stdout.read()) > 0:
            statusDict['status'] = "Running"
        else:
            statusDict['status'] = "Not Running"

        if statusDict['status'] == "Running" and process == "MG-Console":
            command = "find . -name \"mgprogress*\" -type f -printf \'%T+ %p\n\' | sort | tail -n 1 | awk \'BEGIN{FS=\"/\"} {print $NF}\'"
            stdin, stdout, stderr = client.exec_command(command)
            statusDict['mgprogfile'] = stdout.read()

            if len(statusDict['mgprogfile']) > 0:
                statusDict['mgprogfile'] = MG_LOG_DIR + statusDict['mgprogfile'].strip('\n')

                # Get test start time
                command = string.Template("cat $log | grep \"Test Summary\" -A 6 | grep \"Start Time\" | awk \'BEGIN{FS=\"=\"} {print $NF}\'")
                command = command.safe_substitute(log=statusDict['mgprogfile'])
                stdin, stdout, stderr = client.exec_command(command)
                statusDict['mgprog']['stime'] = stdout.read()
                statusDict['mgprog']['stime'] = statusDict['mgprog']['stime'].strip('\n\r')
                statusDict['mgprog']['stime'] = statusDict['mgprog']['stime'].lstrip()

                # Get current time
                command = string.Template("cat $log | grep \"Test Summary\" -A 6 | grep \"Current Time\" | awk \'BEGIN{FS=\"=\"} {print $NF}\'")
                command = command.safe_substitute(log=statusDict['mgprogfile'])
                stdin, stdout, stderr = client.exec_command(command)
                statusDict['mgprog']['ctime'] = stdout.read()
                statusDict['mgprog']['ctime'] = statusDict['mgprog']['ctime'].strip('\n\r')
                statusDict['mgprog']['ctime'] = statusDict['mgprog']['ctime'].lstrip()

                # Get running time
                command = string.Template("cat $log | grep \"Test Summary\" -A 6 | grep \"Running Time\" | awk \'BEGIN{FS=\"=\"} {print $NF}\'")
                command = command.safe_substitute(log=statusDict['mgprogfile'])
                stdin, stdout, stderr = client.exec_command(command)
                statusDict['mgprog']['rtime'] = stdout.read()
                statusDict['mgprog']['rtime'] = statusDict['mgprog']['rtime'].strip('\n\r')
                statusDict['mgprog']['rtime'] = statusDict['mgprog']['rtime'].lstrip()

                # Get the total number of tests
                command = string.Template("cat $log | grep \"Test Summary\" -A 6 | grep \"Total Tests\" | awk \'BEGIN{FS=\"=\"} {print $NF}\'")
                command = command.safe_substitute(log=statusDict['mgprogfile'])
                stdin, stdout, stderr = client.exec_command(command)
                statusDict['mgprog']['ttests'] = stdout.read()
                statusDict['mgprog']['ttests'] = statusDict['mgprog']['ttests'].strip('\n\r')
                statusDict['mgprog']['ttests'] = statusDict['mgprog']['ttests'].lstrip()

                # Get the total number of errors
                command = string.Template("cat $log | grep \"Test Summary\" -A 6 | grep \"Total Errors\" | awk \'BEGIN{FS=\"=\"} {print $NF}\'")
                command = command.safe_substitute(log=statusDict['mgprogfile'])
                stdin, stdout, stderr = client.exec_command(command)
                statusDict['mgprog']['terrors'] = stdout.read()
                statusDict['mgprog']['terrors'] = statusDict['mgprog']['terrors'].strip('\n\r')
                statusDict['mgprog']['terrors'] = statusDict['mgprog']['terrors'].lstrip()

                # Get the total number of warnings
                command = string.Template("cat $log | grep \"Test Summary\" -A 6 | grep \"Total Warnings\" | awk \'BEGIN{FS=\"=\"} {print $NF}\'")
                command = command.safe_substitute(log=statusDict['mgprogfile'])
                stdin, stdout, stderr = client.exec_command(command)
                statusDict['mgprog']['twarns'] = stdout.read()
                statusDict['mgprog']['twarns'] = statusDict['mgprog']['twarns'].strip('\n\r')
                statusDict['mgprog']['twarns'] = statusDict['mgprog']['twarns'].lstrip()

    except Exception as e:
        msg = "Exception occured while attempting to send ssh command %s" \
            % (command)
        raise Exception(msg, e)
    finally:
        client.close()

    return statusDict


def printBanner(process):

    command = string.Template("\n$process Server Status")
    command = command.substitute(process=process)
    print command
    if process == "Echo":
        print '{0:20} {1:20} {2:20}.'.format("Host", "IP", "Status")
    else:
        print '{0:20} {1:30} {2:20}.'.format("Host", "IP", "Status")


def deleteAllOldLogFiles(MGIniFile):
    print "Deleting old MG log files"
    for section in xrange(0, int(len(MGIniFile))):
        if 'Echo Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    host = data[0]
                    print "Deleting logs on ECHO Server: %s" % (host)
                    status = deleteLogs(ip, "EtdNetworkEchoServer")

    for section in xrange(0, int(len(MGIniFile))):
        if 'MeatGrinder Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    print "IP: %s" % (ip)
                    host = data[0]
                    print "Deleting logs on MG Server: %s" % (host)
                    status = deleteLogs(ip, "MG-Console")
    
        
def getAllEchoAndMGStatus(MGIniFile):

    printBanner("Echo")
    for section in xrange(0, int(len(MGIniFile))):
        if 'Echo Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    host = data[0]
                    status = getStatus(ip, "EtdNetworkEchoServer")
                    print data[0].ljust(20), ip.ljust(20), status.ljust(20)

    printBanner("MG")
    for section in xrange(0, int(len(MGIniFile))):
        if 'MeatGrinder Servers' in MGIniFile[section]['section']:
            for key in xrange(0, int(len(MGIniFile[section]['keys']))):
                if '=' in MGIniFile[section]['keys'][key]:
                    data = MGIniFile[section]['keys'][key].split("=")
                    ip = data[1].strip('\n')
                    host = data[0]
                    # status = getStatus(ip, "MG-Console")
                    status = getMgStatus(ip, "MG-Console")
                    # if status == "Running":
                    #    progressDict = getmgprogress(ip)
                    # else:
                    if status['status'] == "Running":
                        print data[0].ljust(20), ip.ljust(30), status['status'].ljust(20)
                        print "Running Time".ljust(20), status['mgprog']['rtime'].ljust(30), "Total Tests".ljust(20), status['mgprog']['ttests'].ljust(20)
                        print "Start Time".ljust(20), status['mgprog']['stime'].ljust(30), "Total Errors".ljust(20), status['mgprog']['terrors'].ljust(20)
                        print "Current Time".ljust(20), status['mgprog']['ctime'].ljust(30), "Total Warnings".ljust(20), status['mgprog']['twarns'].ljust(20), "\n"
                    else:
                        print data[0].ljust(20), ip.ljust(30), status['status'].ljust(20)


def runAllEchoAndMGServers():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, runEchoServers(MGIniFile),
            2, runAllMG(MGIniFile)
            }


def runAllEchoServers():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, runEchoServers(MGIniFile),
            }


def runSingleEchoServer():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, runEcho(MGIniFile)
            }


def runAllMGServers():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, runAllMG(MGIniFile)
            }


def runSingleMGServer():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, runMG(MGIniFile)
            }


def killSingleMGServer():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, killMG(MGIniFile)
            }


def killSingleEchoServer():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, killEcho(MGIniFile)
            }


def killAllMGServers():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, killMGServers(MGIniFile)
            }


def killAllEchoServers():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, killEchoServers(MGIniFile)
            }


def getMGStatus():

    flow = {0, readMasterMGIniFile(INI_FILE),
            1, getAllEchoAndMGStatus(MGIniFile),
            }

def cleanAllLogs():
    flow = {0, readMasterMGIniFile(INI_FILE),
            1, deleteAllOldLogFiles(MGIniFile),
            }

def main():
    # #######################################################################
    # Associate the flowOption with the function
    # #######################################################################
    flowOrder = {'runAll': runAllEchoAndMGServers,
                 'runAllEcho': runAllEchoServers,
                 'runEcho': runSingleEchoServer,
                 'runAllMG': runAllMGServers,
                 'runMG': runSingleMGServer,
                 'killMG': killSingleMGServer,
                 'killEcho': killSingleEchoServer,
                 'killAllMG': killAllMGServers,
                 'killAllEcho': killAllEchoServers,
                 'getMGStatus': getMGStatus,
                 'cleanAllLogs': cleanAllLogs}

    # #######################################################################
    # Get the command line parameters
    # #######################################################################
    getCmdLineParam()

    # #######################################################################
    # Execute the flow order function
    # #######################################################################
    try:
        flowOrder[flowOption]()

    except Exception as e:
        msg = "An unhandled exception occurred."
        raise Exception(msg, e)

if __name__ == "__main__":
    main()
