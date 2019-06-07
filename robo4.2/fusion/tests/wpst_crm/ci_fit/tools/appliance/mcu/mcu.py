#!/usr/local/bin/python
"""
.. module:: mcu.py
   :platform: Linux
   :synopsis: This is the MeatGrinder Configuration Utility
              that's used to read the appliance configuration
              and create MeatGrinder ini files based on user
              definition

.. moduleauthor:: Bobby Suber <bobby.suber@hp.com>

(C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
# #######################################################################
#              Import modules and classes                              #
# #######################################################################
import datetime
import commands
import sys
import os
import argparse
import copy
import readline
from tests.wpst_crm.ci_fit.lib.ciccontrollermodule import (NetworkConfig, VersionBase)
from tests.wpst_crm.ci_fit.lib.logconfigmodule import Logger
from tests.wpst_crm.ci_fit.lib.cicsecuritymodule import LoginSession
from tests.wpst_crm.ci_fit.lib.cicserverprofiles import ProfileBase
from tests.wpst_crm.ci_fit.lib.cicsystemsmodule import (EncBase)
from tests.wpst_crm.ci_fit.lib.cicutils import (PingUtils, IpAddrUtils)
from tests.wpst_crm.ci_fit.lib.cicconnectivitymodule import (NetworkBase)
from tests.wpst_crm.ci_fit.lib.logconfigmodule import (Logger)

if os.name == 'nt':
    lib = sys.path[0] + "\\lib"
    sys.path.insert(1, lib)

else:
    (index, pwd) = commands.getstatusoutput("pwd")
    pwd = pwd + "/lib"
    sys.path.append(pwd)

# #######################################################################
#                    Global Constants/Variables                        #
# #######################################################################
CIC_IP = ""
CIC_USER = "Administrator"
CIC_PW = ""
HA_FILE = ""
INI_FILE = "default.ini"

CONSOLE_LOGGER = "mcu-term"
FILE_LOGGER = "robust-logger"
LIB_LOGGER = "api-logger"

NOW = datetime.datetime.now()
LOG_FILE = 'mcu-' + NOW.strftime("%m-%d-%Y_%H-%M") + '.log'
logger = Logger(filename=LOG_FILE, loggername=FILE_LOGGER, tloggername=CONSOLE_LOGGER, libloggername=LIB_LOGGER)

# #######################################################################
#                    Functions                                         #
# #######################################################################


def getCmdLineParam():
    """
    :py:func:`getCmdLineParam` uses the argparse module to parse the command line parameters

    **Parameters**:
         -i <IP address of the HP OneView appliances>
         -u <Administrator username for the appliance>
         -p <Administrator password for the appliance>
         -c <Name of the existing HA file.>
         -l <Logfile directory path>

    """

    global CIC_USER, CIC_IP, CIC_PW, HA_FILE, LOG_FILE, INI_FILE

    parser = argparse.ArgumentParser(description="mcu.py is used to read an HP OneView domain and configure MeatGrinder ini files.")
    parser.add_argument("-i", "--ip", "--i", dest="CIC_IP", help="IP address of the appliance. Example: -i 15.178.221.135'", default=CIC_IP, required=True)
    parser.add_argument("-u", "--user", "--u", dest="CIC_USER", help="Administrator username for appliance", default=CIC_USER, required=True)
    parser.add_argument("-p", "--password", "--p", dest="CIC_PW", help="Administrator password for the appliance", default=CIC_PW, required=True)
    parser.add_argument("-c", "--cfgfile", "--c", dest="HA_FILE", help="Existing HA_ipaddr filename. Required to create MeatGrinder ini files.", default=HA_FILE, required=True)
    parser.add_argument("-l", "--logpath", "--l", dest="LOG_PATH", help="The logfile directory", required=False)
    parser.add_argument("-f", "--inifile", "--f", dest="INI_FILE", help="The default MG ini file", required=True)

    args = parser.parse_args()

    CIC_IP = args.CIC_IP
    CIC_USER = args.CIC_USER
    CIC_PW = args.CIC_PW
    HA_FILE = args.HA_FILE

    if args.LOG_PATH:
        if os.path.exists(args.LOG_PATH):
            LOG_FILE = args.LOG_PATH + LOG_FILE
        else:
            logger.log.error("Logfile directory path does not exist")
            sys.exit(103)

    if args.INI_FILE:
        if os.path.isfile(args.INI_FILE):
            INI_FILE = args.INI_FILE
        else:
            logger.log.error("MG ini file does not exist")
            sys.exit(103)


def groupByPersonalityType(profileList):
    """
    This function evaluates the profiles in the profileList, finds the match profile personalities and returns them in the groupedList
    """
    groupedList = profileList

    numPtype = 1
    for profile in xrange(0, int(len(groupedList['members']))):
        ptype = 'Type' + '-' + str(numPtype)
        if groupedList['members'][profile].get('ptype') is None:
            groupedList['members'][profile]['ptype'] = ptype
            numPtype += 1

        for match in xrange(profile + 1, int(len(groupedList['members']))):
            if groupedList['members'][match].get('ptype') is not None:
                continue
            if len(groupedList['members'][profile]['connectionSettings']['connections']) != (len(groupedList['members'][match]['connectionSettings']['connections'])):
                continue
            else:
                for connection in xrange(0, int(len(groupedList['members'][match]['connectionSettings']['connections']))):
                    if (groupedList['members'][match]['connectionSettings']['connections'][connection]['networkUri'] == groupedList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'] and
                            groupedList['members'][match]['connectionSettings']['connections'][connection]['id'] == groupedList['members'][profile]['connectionSettings']['connections'][connection]['id'] and
                            connection == len(groupedList['members'][match]['connectionSettings']['connections']) - 1):
                        groupedList['members'][match]['ptype'] = ptype
                    elif (groupedList['members'][match]['connectionSettings']['connections'][connection]['networkUri'] == groupedList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'] and
                          groupedList['members'][match]['connectionSettings']['connections'][connection]['id'] == groupedList['members'][profile]['connectionSettings']['connections'][connection]['id']):
                        continue
                    else:
                        break

    return groupedList


def readDefaultMGiniFile(mgfile):
    """
    This function reads in the MeatGrinder ini template file.
    """
    mgfile = mgfile
    parsedFile = []

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
                parsedFile.append(section)
                section = dict()
                keys = []
                section['section'] = line
        else:
            keys.append(line)

    linestring.close()
    return parsedFile


def disableAllMGtests(mgIniFile):
    """
    This function walks the default mg ini tempelate and sets any enabled tests to disabled.
    """
    disableMgIniFile = mgIniFile
    for section in xrange(0, int(len(disableMgIniFile))):
        if 'Tests' in disableMgIniFile[section]['section']:
            for key in xrange(0, int(len(disableMgIniFile[section]['keys']))):
                if 'TestEnabled' in disableMgIniFile[section]['keys'][key]:
                    name = disableMgIniFile[section]['keys'][key].split("=")
                    disableMgIniFile[section]['keys'][key] = name[0] + '=0x0\r\n'

    return disableMgIniFile


def discoverNets(ip, sessionId, profileList):
    """
    This function checks the connections and sorts out the non Ethernet type connections.
    """
    nets = NetworkBase(ip=ip, sessionId=sessionId)
    networkList = nets.getEthNets()
    fcNetworkList = nets.getFcNets()
    for profile in xrange(0, int(len(profileList['members']))):
        if profileList['members'][profile]['serverHardwareUri']:
            for connection in xrange(0, int(len(profileList['members'][profile]['connectionSettings']['connections']))):
                if profileList['members'][profile]['connectionSettings']['connections'][connection]['functionType'] == 'Ethernet':
                    for network in xrange(0, int(len(networkList['members']))):
                        if networkList['members'][network]['uri'] == profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri']:
                            profileList['members'][profile]['connectionSettings']['connections'][connection]['name'] = networkList['members'][network]['name']
                elif profileList['members'][profile]['connectionSettings']['connections'][connection]['functionType'] == 'FibreChannel':
                    for fcnetwork in xrange(0, int(len(fcNetworkList['members']))):
                        if fcNetworkList['members'][fcnetwork]['uri'] == profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri']:
                            profileList['members'][profile]['connectionSettings']['connections'][connection]['name'] = fcNetworkList['members'][fcnetwork]['name']


def discoverEnc(ip, sessionId, profileList):
    """
    This function matches the profile to the correct enclosure.
    """
    encs = EncBase(ip=ip, sessionId=sessionId)
    for profile in xrange(0, int(len(profileList['members']))):
        if profileList['members'][profile]['serverHardwareUri']:
            uuid = profileList['members'][profile]['enclosureUri'].split('/')
            encDto = encs.getEnc(uuid[3])
            profileList['members'][profile]['encname'] = encDto['name']


def createMGFileName(profileList, disabledMGiniFile):
    """
    This function creates the individual MG ini files for each profile/blade.
    """
    for profile in xrange(0, int(len(profileList['members']))):
        if profileList['members'][profile]['serverHardwareUri']:
            profileList['members'][profile]['ininame'] = \
                profileList['members'][profile]['encname'] + \
                '-' + str(profileList['members'][profile]['enclosureBay']) + '.ini'
            profileList['members'][profile]['inifile'] = copy.deepcopy(disabledMGiniFile)


def getProfilePersonalityTypes(groupedList):
    """
    This function collects the server profile personality types and puts them spPersonalityTypes list.
    """
    spPersonalityTypes = []
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')

    # Determine the server profile personality types and add them to the list
    for profile in xrange(0, int(len(groupedList['members']))):
        if profile == 0:
            spPersonalityTypes.append(groupedList['members'][profile]['ptype'])
            continue
        for spptype in xrange(0, int(len(spPersonalityTypes))):
            if spptype == int(len(spPersonalityTypes) - 1) and groupedList['members'][profile]['ptype'] != (spPersonalityTypes[spptype]):
                spPersonalityTypes.append(groupedList['members'][profile]['ptype'])
            elif groupedList['members'][profile]['ptype'] == spPersonalityTypes[spptype]:
                break
            else:
                continue
    return spPersonalityTypes


def printProfileTypes(groupedList, profilePersonalityTypes):
    """
    This function prints the server profile personality types from spPersonalityTypes list.
    """
    # Iterate over the server profile list for each profile type and print the profile name
    for sptype in xrange(0, int(len(profilePersonalityTypes))):
        logger.log.info("Profile type: %s" % (profilePersonalityTypes[sptype]))
        for profile in xrange(0, int(len(groupedList['members']))):
            if ((groupedList['members'][profile]['ptype'] == profilePersonalityTypes[sptype]) and
                    (groupedList['members'][profile].get('serverHardwareUri', None) is not None)):
                logger.log.info(" Profile: %s" % (groupedList['members'][profile]['name']))


def identifyEchoServers(groupedList, sProfilePersonalityTypes):
    """
    This function asks the user which blades will be used as echo servers..
    """
    # Iterate over the server profile list for each profile type and let the user determine the echo server
    for sp_type in xrange(0, int(len(sProfilePersonalityTypes))):
        logger.log.info("Profile type: %s" % (sProfilePersonalityTypes[sp_type]))
        for profile in xrange(0, int(len(groupedList['members']))):
            if ((groupedList['members'][profile]['ptype'] == sProfilePersonalityTypes[sp_type]) and
                    (groupedList['members'][profile].get('echo', None) is None) and
                    (groupedList['members'][profile].get('serverHardwareUri', None) is not None)):

                print '\nType: %s, echo server: %s?\n' % (sProfilePersonalityTypes[sp_type], groupedList['members'][profile]['name'])
                user_input = raw_input('>>> Enter Yes or No: ')
                if user_input == "Yes" or user_input == "YES" or user_input == "yes" or user_input == "Yes" or user_input == "Y" or user_input == "y":
                    groupedList['members'][profile]['echo'] = "Yes"
                    # For all other servers with the same personality type set echo to no
                    # since we only want one echo server
                    logger.log.info(" Profile: %s" % (groupedList['members'][profile]['name']))
                    for server in xrange(0, int(len(groupedList['members']))):
                        if ((groupedList['members'][server]['ptype'] == sProfilePersonalityTypes[sp_type]) and
                                (groupedList['members'][server].get('echo', None) is None)):
                            groupedList['members'][server]['echo'] = "No"
                else:
                    groupedList['members'][profile]['echo'] = "No"
    return groupedList


def printIdentifiedEchoServers(groupedList, sPPersonalityTypes):
    """
    This function displays the echo servers selected by the user.
    """
    # Iterate over the server profile list for each profile type and print the profile name and echo server
    for p_type in xrange(0, int(len(sPPersonalityTypes))):
        logger.log.info("Profile type: %s" % (sPPersonalityTypes[p_type]))
        for profile in xrange(0, int(len(groupedList['members']))):
            if (groupedList['members'][profile]['ptype'] == sPPersonalityTypes[p_type]) and \
               (groupedList['members'][profile].get('serverHardwareUri', None) is not None):
                if groupedList['members'][profile]['echo'] == "Yes":
                    logger.log.info(" Profile: %s -> Echo Server" % (groupedList['members'][profile]['name']))
                else:
                    logger.log.info(" Profile: %s" % (groupedList['members'][profile]['name']))


def configNetSockets(groupedList, fileLineList):
    """
    This function maps profiles to ip addresses and vid.
    """
    # Make call to functions to gather profile and echo server information.
    sProfilePersonalityTypes = getProfilePersonalityTypes(groupedList)
    printProfileTypes(groupedList, sProfilePersonalityTypes)
    updatedGroupedList = identifyEchoServers(groupedList, sProfilePersonalityTypes)
    printIdentifiedEchoServers(updatedGroupedList, sProfilePersonalityTypes)

    # Make a call to the library to get the list of dicts for the IP addressing scheme
    ipUtils = IpAddrUtils()
    ipscheme = ipUtils.init10IpaddrScheme()

    # For each profile that is an echo server create a dict that includes the personality type and the
    # ip mapping that points to a list of dicts that includes each vid and host IP
    echoServerList = []
    echoServer = {}
    for server_type in xrange(0, int(len(sProfilePersonalityTypes))):
        for profile in xrange(0, int(len(groupedList['members']))):
            if ((groupedList['members'][profile]['ptype'] == sProfilePersonalityTypes[server_type]) and
                    (groupedList['members'][profile].get('serverHardwareUri', None) is not None)):
                if groupedList['members'][profile]['echo'] == "Yes":
                    echoServer['ptype'] = groupedList['members'][profile]['ptype']
                    ipmappings = []
                    for sp in xrange(0, int(len(fileLineList))):
                        ipsplit = fileLineList[sp]['ip'].split('.')
                        ipsearch = ipsplit[0] + '.' + ipsplit[1] + '.' + ipsplit[2] + '.' + '0'
                        if groupedList['members'][profile]['name'] == fileLineList[sp]['profile']:
                            mappings = dict()
                            # Search the ipscheme array for the using the ip address and add the vid and ip
                            # and network to the mappings dict
                            for ip in xrange(0, int(len(ipscheme))):
                                if ipscheme[ip]['netip'] == ipsearch:
                                    mappings['vid'] = ipscheme[ip]['vid']
                                    mappings['network'] = ipscheme[ip]['netip']
                                    mappings['ip'] = fileLineList[sp]['ip']
                                    ipmappings.append(mappings)
                    echoServer['ipmappings'] = ipmappings
        echoServerList.append(echoServer)
    createIniFile(groupedList, fileLineList, echoServerList)


def createIniFile(groupedListFinal, iniFileLineList, iniEchoServerList):
    """
    This function generates MG ini files based on user input from previous functions.
    """
    # For each profile that is not an echo server create an ini file and append it to a list
    # Read the HA_ipaddr.conf file and key off the server profile name.  For each IP in the HA_ippaddr.conf
    # file set NicxHost=<IP>, NicxSockets=0x1, NicxRemoteHost=<Remote IP of the echo server>
    for profile in xrange(0, int(len(groupedListFinal['members']))):
        if ((groupedListFinal['members'][profile].get('echo', None) is not None) and
                (groupedListFinal['members'][profile].get('serverHardwareUri', None) is not None)):
            if groupedListFinal['members'][profile]['echo'] == "No":
                # Set NetworkSocketTestEnabled=0x1
                for section in xrange(0, int(len(groupedListFinal['members'][profile]['inifile']))):
                    if 'Tests' in groupedListFinal['members'][profile]['inifile'][section]['section']:
                        for key in xrange(0, int(len(groupedListFinal['members'][profile]['inifile'][section]['keys']))):
                            if 'NetworkSocketTestEnabled' in groupedListFinal['members'][profile]['inifile'][section]['keys'][key]:
                                name = groupedListFinal['members'][profile]['inifile'][section]['keys'][key].split("=")
                                groupedListFinal['members'][profile]['inifile'][section]['keys'][key] = name[0] + '=0x1\r\n'
                # Set AutoAssign=0x0
                for section in xrange(0, int(len(groupedListFinal['members'][profile]['inifile']))):
                    if 'Network Socket Thread' in groupedListFinal['members'][profile]['inifile'][section]['section']:
                        for key in xrange(0, int(len(groupedListFinal['members'][profile]['inifile'][section]['keys']))):
                            if 'AutoAssign' in groupedListFinal['members'][profile]['inifile'][section]['keys'][key]:
                                name = groupedListFinal['members'][profile]['inifile'][section]['keys'][key].split("=")
                                groupedListFinal['members'][profile]['inifile'][section]['keys'][key] = name[0] + '=0x0\r\n'
                nic = 1
                for sp in xrange(0, int(len(iniFileLineList))):
                    if groupedListFinal['members'][profile]['name'] == iniFileLineList[sp]['profile']:
                        ipsplit = iniFileLineList[sp]['ip'].split('.')
                        ipsearch = ipsplit[0] + '.' + ipsplit[1] + '.' + ipsplit[2] + '.' + '0'
                        # Search the iniEchoServerList for a matching personality type
                        for eserv in xrange(0, int(len(iniEchoServerList))):
                            if groupedListFinal['members'][profile]['ptype'] == iniEchoServerList[eserv]['ptype']:
                                # Search the ipmappings for a matching network for NicxRemoteHost
                                for network in xrange(0, int(len(iniEchoServerList[eserv]['ipmappings']))):
                                    if iniEchoServerList[eserv]['ipmappings'][network]['network'] == ipsearch:
                                        # Search the iniFileData and insert NicxHost=<IP>, NicxSockets=0x1, NicxRemoteHost
                                        for section in xrange(0, int(len(groupedListFinal['members'][profile]['inifile']))):
                                            if 'Network Socket Thread' in groupedListFinal['members'][profile]['inifile'][section]['section']:
                                                groupedListFinal['members'][profile]['inifile'][section]['keys'].insert(len(groupedListFinal['members'][profile]['inifile'][section]['keys']) - 1, 'Nic' + str(nic) + 'Host' + '=' + iniFileLineList[sp]['ip'] + '\r\n')
                                                groupedListFinal['members'][profile]['inifile'][section]['keys'].insert(len(groupedListFinal['members'][profile]['inifile'][section]['keys']) - 1, 'Nic' + str(nic) + 'Sockets' + '=' '0x1' + '\r\n')
                                                groupedListFinal['members'][profile]['inifile'][section]['keys'].insert(len(groupedListFinal['members'][profile]['inifile'][section]['keys']) - 1, 'Nic' + str(nic) + 'RemoteHost' + '=' + iniEchoServerList[eserv]['ipmappings'][network]['ip'] + '\r\n')
                                                nic += 1
                # Zero out NicxSockets for all NICs upto and including Nic512
                for section in xrange(0, int(len(groupedListFinal['members'][profile]['inifile']))):
                    if 'Network Socket Thread' in groupedListFinal['members'][profile]['inifile'][section]['section']:
                        for nicx in xrange(nic, 512 + 1):
                            groupedListFinal['members'][profile]['inifile'][section]['keys'].insert(len(groupedListFinal['members'][profile]['inifile'][section]['keys']) - 1, 'Nic' + str(nicx) + 'Host' + '=' + '\r\n')
                            groupedListFinal['members'][profile]['inifile'][section]['keys'].insert(len(groupedListFinal['members'][profile]['inifile'][section]['keys']) - 1, 'Nic' + str(nicx) + 'Sockets' + '=' '0x0' + '\r\n')
                            groupedListFinal['members'][profile]['inifile'][section]['keys'].insert(len(groupedListFinal['members'][profile]['inifile'][section]['keys']) - 1, 'Nic' + str(nicx) + 'RemoteHost' + '=' + '\r\n')


def configRawDisk(groupedList):
    """
    This function lists the profile types and asks the user to identify if the raw disk test will run on the server.
    It also ask the user to verify the raw disk device.
    """
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')

    for profile in xrange(0, int(len(groupedList['members']))):
        if groupedList['members'][profile]['serverHardwareUri']:
            # Read the profile connections and prompt for device name when there is either one FC network
            # assigned to a single connection or two FC networks that are redundantly assigned to a device - FLB1-1-b, FLB1-2-b
            for connection in xrange(0, int(len(groupedList['members'][profile]['connectionSettings']['connections']))):
                if groupedList['members'][profile]['connectionSettings']['connections'][connection]['functionType'] == 'FibreChannel':
                    logger.log.info(" Profile: %s" % (groupedList['members'][profile]['name']))
                    logger.log.info("    Id    Network")
                    # Iterate over the sp connections and print the FC connections
                    for conn in xrange(0, int(len(groupedList['members'][profile]['connectionSettings']['connections']))):
                        if conn == int(len(groupedList['members'][profile]['connectionSettings']['connections'])):
                            connection += 1
                            break
                        if groupedList['members'][profile]['connectionSettings']['connections'][conn]['functionType'] == 'FibreChannel':
                            logger.log.info("    %s     %s" % (groupedList['members'][profile]['connectionSettings']['connections'][conn]['id'], groupedList['members'][profile]['connectionSettings']['connections'][conn]['name']))
                    path = 0
                    # Get the device active path from the user
                    while True:
                        print '\nPlease enter the device active path - /dev/dm-0 or \'c\' to continue\n'
                        uinput = raw_input('>>> ')
                        if uinput == "c":
                            break
                        else:
                            activepath = uinput
                            logger.log.info("ActivePath%s is %s" % (path, activepath))
                            # Set RawDiskTestEnabled=0x1
                            for section in xrange(0, int(len(groupedList['members'][profile]['inifile']))):
                                if 'Tests' in groupedList['members'][profile]['inifile'][section]['section']:
                                    for key in xrange(0, int(len(groupedList['members'][profile]['inifile'][section]['keys']))):
                                        if 'RawDiskTestEnabled' in groupedList['members'][profile]['inifile'][section]['keys'][key]:
                                            name = groupedList['members'][profile]['inifile'][section]['keys'][key].split("=")
                                            groupedList['members'][profile]['inifile'][section]['keys'][key] = name[0] + '=0x1\r\n'
                            # Set ActivePath
                            for section in xrange(0, int(len(groupedList['members'][profile]['inifile']))):
                                if 'Rawdisk Thread' in groupedList['members'][profile]['inifile'][section]['section']:
                                    for key in xrange(0, int(len(groupedList['members'][profile]['inifile'][section]['keys']))):
                                        if 'ActiveCount' in groupedList['members'][profile]['inifile'][section]['keys'][key]:
                                            name = groupedList['members'][profile]['inifile'][section]['keys'][key].split("=")
                                            groupedList['members'][profile]['inifile'][section]['keys'][key] = name[0] + '=0x' + str(path + 1) + '\r\n'
                                    groupedList['members'][profile]['inifile'][section]['keys'].insert(len(groupedList['members'][profile]['inifile'][section]['keys']) - 1, 'ActivePath' + str(path) + '=' + activepath + '\r\n')
                            path += 1
                    break


def writeMGiniFiles(groupedList):
    """
    This function takes the data and information collected from OV and the user to write out the MG ini files.
    """

    for profile in xrange(0, int(len(groupedList['members']))):
        if 'inifile' in groupedList['members'][profile]:
            f = open(groupedList['members'][profile]['ininame'], 'w')
            for section in xrange(0, int(len(groupedList['members'][profile]['inifile']))):
                f.write(groupedList['members'][profile]['inifile'][section]['section'])
                for key in xrange(0, int(len(groupedList['members'][profile]['inifile'][section]['keys']))):
                    f.write(groupedList['members'][profile]['inifile'][section]['keys'][key])
            f.close()


def main():
    """
    This is the main function for mcu.py

    1. Read the cmd line parameters.

    """

    # #######################################################################
    # Get the command line parameters
    # #######################################################################
    getCmdLineParam()

    # #######################################################################
    # Create a login session with the credentials passed-in from the cmd line
    # #######################################################################
    logger.log.info("Creating login session")
    curSession = LoginSession(ip=CIC_IP, uname=CIC_USER, pw=CIC_PW)
    authToken = curSession.post()

    # #######################################################################
    # Get the appliance node version information
    # #######################################################################
    logger.log.info("Getting the appliance node version")
    applianceVer = VersionBase(CIC_IP, authToken)
    nodeVer = applianceVer.getNodeVersion()
    logger.log.debug("Appliance Version: %s, Date: %s" % (nodeVer['softwareVersion'], nodeVer['date']))

    # #######################################################################
    # Get the appliance Name
    # #######################################################################
    applianceName = NetworkConfig(ip=CIC_IP, sessionId=authToken)
    appliancename = applianceName.getNodeName()
    logger.log.info("Appliance name %s" % (appliancename['hostname']))

    # #######################################################################
    # Read the HA_ipaddr.conf file
    # #######################################################################
    if HA_FILE != "":
        logger.log.info("Reading the HA_ipaddr.conf file")
        pingUtils = PingUtils(ip=CIC_IP, sessionId=authToken)
        fileLineList = pingUtils.readFileLineByLine(HA_FILE)

    # #######################################################################
    # Read the default MG ini file
    # #######################################################################
    logger.log.info("Reading the default MG ini file: %s" % (INI_FILE))
    defaultMGiniFile = readDefaultMGiniFile(INI_FILE)

    # #######################################################################
    # Disable all *TestEnabled
    # #######################################################################
    logger.log.info("Disabling all of the MG tests")
    disabledMGiniFile = disableAllMGtests(defaultMGiniFile)

    # #######################################################################
    # Get the server profile list
    # #######################################################################
    logger.log.info("Discovering profiles")
    profileBase = ProfileBase(ip=CIC_IP, sessionId=authToken)
    profileList = profileBase.getProfiles(filter=None)

    # #######################################################################
    # Associate the network name to the profile dto
    # #######################################################################
    logger.log.info("Discovering networks")
    discoverNets(ip=CIC_IP, sessionId=authToken, profileList=profileList)

    # #######################################################################
    # Associate the enclosure name to the profile dto
    # #######################################################################
    logger.log.info("Discovering enclosures")
    discoverEnc(ip=CIC_IP, sessionId=authToken, profileList=profileList)

    # #######################################################################
    # Create the MG ini file names
    # #######################################################################
    logger.log.info("Creating the MG ini file names")
    createMGFileName(profileList, disabledMGiniFile)

    # #######################################################################
    # Group the server profile list by personality type
    # #######################################################################
    logger.log.info("Grouping the profiles by personality type")
    groupedList = groupByPersonalityType(profileList)

    # #######################################################################
    # Configure the network sockets test
    # #######################################################################
    logger.log.info("Configuring the Network Sockets Test")
    configNetSockets(groupedList, fileLineList)

    # #######################################################################
    # Configure the raw disk test
    # #######################################################################
    logger.log.info("Configuring the Raw Disk Test")
    configRawDisk(groupedList)

    # #######################################################################
    # Write the MG ini files
    # #######################################################################
    logger.log.info("Writing the MG ini files")
    writeMGiniFiles(groupedList)


if __name__ == "__main__":
    main()
