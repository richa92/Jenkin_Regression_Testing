#!/usr/local/bin/python
"""
.. module:: D-NCT
   :platform: Linux
   :synopsis: The script reads the HP OneView appliance configuration and creates the HA file (default: HA_ipaddr.conf)
              that is used to configure the network interfaces for bonding, ip, and vlans.

.. moduleauthor::  John Thigpen <john.r.thigpen@hp.com>, Bobby Suber <bobby.suber@hp.com>

(C) Copyright 2013 Hewlett-Packard Development Company, L.P.

"""


# #######################################################################
#              Import modules and classes                              #
# #######################################################################
import datetime
import commands
import sys
import time
import os
import shutil
import re
import argparse
import tempfile
import operator
import pdb
import logging
import pdb
from tests.wpst_crm.ci_fit.lib.logconfigmodule import Logger
from tests.wpst_crm.ci_fit.lib.cicsecuritymodule import LoginSession
from tests.wpst_crm.ci_fit.lib.ciccontrollermodule import (NetworkConfig, VersionBase)
from tests.wpst_crm.ci_fit.lib.cicserverprofiles import ProfileBase
from tests.wpst_crm.ci_fit.lib.cicconnectivitymodule import (NetworkBase, NetworkSetBase)
from tests.wpst_crm.ci_fit.lib.cicutils import (PingUtils, IpAddrUtils)
import pprint

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
CIC_USER = "Administrator"
CIC_IP = ""
CIC_PW = "hpvse123"
OA_ENC = ""
HA_FILE = ""
HA_FILE_NAME = "HA_ipaddr.conf"
NAME = "D-NCT"
IP_RANGE = "R1"

FILE_LOGGER = "D-NCT-logger"
LIB_LOGGER = "api-logger"
CONSOLE_LOGGER = "D-NCT-term"

NOW = datetime.datetime.now()
LOG_FILE = NAME + '-' + NOW.strftime("%m-%d-%Y_%H-%M") + '.log'
logger = Logger(filename=LOG_FILE, loggername=FILE_LOGGER, tloggername=CONSOLE_LOGGER, libloggername=LIB_LOGGER)
# Default Tunnel VLANs: 3000 - 3010


# #######################################################################
#                    Functions                                         #
# #######################################################################


def getCmdLineParam():
    """
    :py:func:`getCmdLineParam` uses the argparse module to parse the command line parameters

    **Parameters**:
         -c <name of the existing HA file for build new HA_ipaddr.conf file for 2 enclosures>
         -i <IP address of the fusion appliances>
         -o <the name of the enclosure>
         -p <Administrator password for the appliance>
         -u <Administrator username for the appliance>

    .. todo::
       Add -l <logfile>
       Add -k  <keep the D-NCT logs. *italics*NOT Implemented Yet>

    """
    logger.log.info("Parsing command line parameters")
    global CIC_USER, CIC_IP, CIC_PW, HA_FILE, HA_FILE_NAME, OA_ENC, IP_RANGE, START_TUNNEL_ID

    os.system('clear')

    parser = argparse.ArgumentParser(description="D-NCT gets the existing Server Profiles from the Fusion appliance and creates a HA_ippadr.conf file based on the configuration.")

    parser.add_argument("-c", "--cfgfile", "--c", dest="HA_FILE", help="[Optional] Existing HA_ipaddr filename for existing enclosure. Used to create new HA_ipddr.conf file for mulitple enclosures.", default=HA_FILE, required=False)
    parser.add_argument("-n", "--newcfgfile", "--n", dest="HA_FILE_NAME", help="[Optional. Default: HA_ipaddr.conf] New HA_ipaddr file to be generated.", default=HA_FILE_NAME, required=False)
    parser.add_argument("-s", "--startTunnelId", "--l", dest="START_TUNNEL_ID", help="[Optional. Default: 3000] Start tunnel vlan id.", default=3000, required=False)
    parser.add_argument("-i", "--ip", "--i", dest="CIC_IP", help="[Required] IP address of the appliance. Example: -i 15.178.221.135'", default=CIC_IP, required=True)
    parser.add_argument("-o", "--enc_name", "--o", dest="OA_ENC", help="[Optional] Enclosure name. Example: CI-FIT-1.", default=OA_ENC, required=False)
    parser.add_argument("-p", "--password", "--p", dest="CIC_PW", help="[Required] Administrator password for the appliance", default=CIC_PW, required=True)
    parser.add_argument("-u", "--user", "--u", dest="CIC_USER", help="[Required] Administrator username for appliance", default=CIC_USER, required=True)
    parser.add_argument("-r", "--range", "--r", dest="IP_RANGE", help="[Optional] Host IP range where R1 starts at 2, R2 starts at 86, and R3 starts at 170", choices=['R1', 'R2', 'R3'], default=IP_RANGE, required=False)

    args = parser.parse_args()

    CIC_USER = args.CIC_USER
    CIC_IP = args.CIC_IP
    CIC_PW = args.CIC_PW
    HA_FILE = args.HA_FILE
    HA_FILE_NAME = args.HA_FILE_NAME
    OA_ENC = args.OA_ENC
    IP_RANGE = args.IP_RANGE
    START_TUNNEL_ID = int(args.START_TUNNEL_ID)


def getTunnelsUri(ethNetList):
    """
    :py:func:`getTunnelsUri` parses the ethernet network list and pulls out the uri for tunnel
    networks.

    **Args**:
         *ethNetList* (dict) : Ethernet network dict tthat points to a list of members \n

    """
    tunnelList = []
    for ethNet in xrange(0, int(len(ethNetList['members']))):
        if ethNetList['members'][ethNet]['ethernetNetworkType'] == 'Tunnel':
            # JRT tunnelList.append(ethNetList['members'][ethNet]['uri'])
            tunnelList.append(ethNetList['members'][ethNet])

    return tunnelList


def addVidToNetworkSet(nwSetList, ethNetList):
    """
    :py:func:`addVidToNetworkSet` associates the vid to each network in the network set.  By default the
    network set dto does not have a vlan attribute for each network that is assigned to the network set.  This
    function iterates over the list of network sets and adds the attribute 'networks' which points to a list
    of dicts that includes the uri, name, and vlanId of each network assigned to the set.  The primary reason
    for this function is to make this association once so that it can be used by the program when determining
    which networks in a network set can be bound together because networks can be bound iff they have the same vid.

    **Args**:
        *nwSetList* (dict)  : Network set dict that points to a list of members \n
        *ethNetList* (dict) : Ethernet network dict that points to a list of members \n

    """

    for nwset in xrange(0, int(len(nwSetList['members']))):
        networks = []
        for network in xrange(0, int(len(nwSetList['members'][nwset]['networkUris']))):
            for ethnet in xrange(0, int(len(ethNetList['members']))):
                if nwSetList['members'][nwset]['networkUris'][network] == ethNetList['members'][ethnet]['uri']:
                    network = dict()
                    network['name'] = ethNetList['members'][ethnet]['name']
                    network['uri'] = ethNetList['members'][ethnet]['uri']
                    network['vlanId'] = ethNetList['members'][ethnet]['vlanId']
                    networks.append(network)
                    break
        nwSetList['members'][nwset]['networks'] = networks


def checkForFile(file2Check):
    """
    :py:func:`checkForFile` verifies if a file exists on the system and if it does then it renames
     it to <name>.tmp.

    **Args**:
        *file2Check* (str)        : name of the file to verify.
    """

    logger.log.info("Checking for %s." % (file2Check))
    if os.path.exists(file2Check):
        tstamp = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
        newFile = file2Check + tstamp
        logger.log.info("Moving file to %s." % (newFile))
        shutil.move(file2Check, newFile)


def initIpAddrScheme(haFile):

    ipUtils = IpAddrUtils()
    ipscheme = ipUtils.init10IpaddrScheme()

    """
    :py:func:`initIpAddrScheme` uses the :py:class:`cicutils.IpAddrUtils` class to initialize the IP addressing
    scheme.  If the HA_ipaddr file is passed in then it reads the file to determine the host IP for each network
    otherwise the IP is set to 2.

    **Args**:
        *haFile* (list)  : List of dicts that includes each line of the HA_FILE content\n

    """

    if haFile != "":
        pingUtil = PingUtils()
        fileList = pingUtil.readFileLineByLine(haFile)
        for vlan in xrange(0, int(len(ipscheme))):
            host = 1
            for line in xrange(0, int(len(fileList))):
                ipsplit = fileList[line]['ip'].split('.')
                ipsearch = ipsplit[0] + '.' + ipsplit[1] + '.' + ipsplit[2] + '.' + '0'
                for ip in xrange(0, int(len(ipscheme))):
                    if ipscheme[ip]['netip'] == ipsearch:
                        vlanId = ipscheme[ip]['vid']
                        break
                if vlanId != ipscheme[vlan]['vid']:
                    continue
                else:
                    if int(ipsplit[3]) > host:
                        host = int(ipsplit[3])
            host += 1
            # Changing to max out at 245 to reserve 10 set of IPs for iSCSI static.
            # OLD: if host == 254:
            if host == 245:
                logger.log.error("Exhausted host IP addresses for vlan %s." % (vlan))
                exit(1)
            else:
                ipscheme[vlan]['hostip'] = str(host)
    else:
        for vid in xrange(0, int(len(ipscheme))):
            if IP_RANGE == "R1":
                ipscheme[vid]['hostip'] = "2"
            elif IP_RANGE == "R2":
                ipscheme[vid]['hostip'] = "86"
            elif IP_RANGE == "R3":
                ipscheme[vid]['hostip'] = "170"
            else:
                logger.log.error("Invalid IP range: %s." % (IP_RANGE))
                exit(1)

    return ipscheme


def bindDevices(profileList, ipScheme, ethNetList, nwSetList, tunnelUriList, startTunnelId=3000):
    """
    :py:func:`bindDevices` iterates over each profile and then each profile connection and attempts to
     find a matching connection to bind.  The connection portId is used for the match where we only bind
     odd ports to even ports and only bind to corresponding ports on a device - ie. Flb1:1-c -> Flb1:2-c.

    **Args**:
        *profileList* (dict)  : Profile dict that points to a list of members\n
        *ipScheme*    (list)  : List of dicts that includes the netip, vid, and hostip for each vlan\n
        *ethNetList*  (dict)  : Ethernet network dict that points to a list of members\n
        *nwSetList*   (dict)  : Network set dict that points to a list of members\n
        *tunnelUriList*   (dict)  : Tunnel Network set dict that points to a list of tunnel URIs\n

    """
    # Walk Profile List to get connections for each member
    for profile in xrange(0, int(len(profileList['members']))):
        haFile = []
        # Walk each connection in the profile
        for connection in xrange(0, int(len(profileList['members'][profile]['connectionSettings']['connections']))):
            # Check if the connection an 'Ethernet' connection
            if profileList['members'][profile]['connectionSettings']['connections'][connection]['functionType'] == 'Ethernet':
                portId = splitPortId(profileList['members'][profile]['connectionSettings']['connections'][connection]['portId'])

                # Determine if the phy port is odd or even.
                port = int(portId['phyPort']) % 2
                logger.log.debug("Physical port: %s, remainder: %d" % (portId['phyPort'], port))
                print("Phy port: %s, remainder: %d" % (portId['phyPort'], port))
                print("Checking if port is even.")
                # Check if the port is even - If even get next connection/port
                if port == 0:
                    # Only bind odd ports to even ports - LOM1:a->LOM2:a or LOM3:a->LOM4:a
                    # Don't bind LOM2:c->LOM3:c
                    logger.log.debug("Port is even so continuing: Port ID %s %s:%s-%s"
                                     % (portId['portType'], portId['devSlot'], portId['phyPort'], portId['virtPort']))
                    continue
                # The connection port is odd.  Create the bind port
                logger.log.debug("Creating bind port Id")
                if portId['virtPort'] is None:
                    bindPortId = portId['portType'] + " " + portId['devSlot'] + ":" + str((int(portId['phyPort']) + 1))
                else:
                    bindPortId = portId['portType'] + " " + portId['devSlot'] + ":" + str((int(portId['phyPort']) + 1)) + "-" + portId['virtPort']
                print("Created bindPortId: %s" % (bindPortId))

                # Walk the connections of the profile again to find the matching bindconnection based on the bindPortId
                for bindconnection in xrange(0, int(len(profileList['members'][profile]['connectionSettings']['connections']))):
                    # bindconnection portId and bindPortId do not match.  Get next bindconnection.
                    if profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['portId'] != bindPortId:
                        continue
                    # Found matching bind connection portID.
                    else:
                        # Found a portId match now find a match for the vlan ids for each network
                        print("Checking if the bindconnection and connection networkUri match")

                        logger.log.debug("Checking if the bindconnection and connection networkUri match")
                        logger.log.debug("Bind connection URI: %s" % (profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['networkUri']))
                        logger.log.debug("Connection URI: %s" % (profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri']))
                        # Check if the bindconnection and connection URI match -- i.e. they are ethernet networks are are using the same network
                        if (('ethernet-networks' in profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['networkUri']) and
                                ('ethernet-networks' in profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'])):
                            print("connection and bindconnection Uri match!")
                            print(">>> JRT >>> Profile:         %s" % (profileList['members'][profile]['name']))
                            print(">>> JRT >>> bindPortId: %s" % (bindPortId))
                            print("Checking if vid is in ethNetwList")
                            # Check ethNetList for matching URI
                            # Walk the ethNetList members to find the vid uri that match the bindconnection and connection URIs
                            for vid in xrange(0, int(len(ethNetList['members']))):
                                if profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'] == ethNetList['members'][vid]['uri'] and \
                                   profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['networkUri'] == ethNetList['members'][vid]['uri']:
                                    # This is the scenario where the connection and the bindconnection is using the same network
                                    connectionVid = ethNetList['members'][vid]['vlanId']
                                    bindConnectionVid = ethNetList['members'][vid]['vlanId']
                                    networkName = ethNetList['members'][vid]['name']
                                    print("SAME NETWORK: connectionVid: %s, bindConnectionVid: %s" % (connectionVid, bindConnectionVid))
                                    print(">>> JRT >>> bindPortId: %s Calling BREAK" % (bindPortId))
                                    break

                                # Set the connectionVid based on the ethNetList uri.
                                elif profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'] == ethNetList['members'][vid]['uri']:
                                    connectionVid = ethNetList['members'][vid]['vlanId']
                                    networkName = ethNetList['members'][vid]['name']
                                    print("Connection: connectionVid: %s" % (connectionVid))
                                # Set the bindConnectionVid based on the ethNetList uri
                                elif profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['networkUri'] == ethNetList['members'][vid]['uri']:
                                    bindConnectionVid = ethNetList['members'][vid]['vlanId']
                                    print("Bindconnection: bindConnectionVid: %s" % (bindConnectionVid))
                                else:
                                    continue

                            ##########################################################
                            # Check if the connectionVid and bindConnectionVid match:
                            if (connectionVid == bindConnectionVid):
                                # Walk the tunnelUriList and check if the connnection is part of a tunnel
                                print ("JRT: Checking if network uri is a tunnel uri")
                                for tun in xrange(0, int(len(tunnelUriList))):
                                    if profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'] == tunnelUriList[tun]['uri']:
                                        print ("FOUND:           matching tunnel! Need to add HA entry for the network.")
                                        print("Profile:         %s" % (profileList['members'][profile]['name']))
                                        # Fail on tunnel network name without number suffix
                                        if not re.search('(\d+)$', networkName):
                                            logger.log.error("ethernetNetworkType is Tunnel but the name does not conform with CI-FIT naming requirement. Please add number suffix to %s. Example Tunnel1, Tunnel2, etc. accordingly" % (networkName))
                                            exit(1)
                                        # Get tunnel number
                                        tunnel_number = int(re.search('(\d+)$', networkName).group(0)) - 1
                                        # Set the appropriate tunnel ids
                                        newStartTunnelId = tunnel_number * 10 + startTunnelId + tunnel_number
                                        # Check vlans and create the HA entry
                                        for vlan in xrange(newStartTunnelId, newStartTunnelId + 11):
                                            for vip in xrange(0, int(len(ipScheme))):
                                                if vlan == ipScheme[vip]['vid']:
                                                    haFileData = dict()
                                                    haFileData['profile'] = profileList['members'][profile]['name']
                                                    haFileData['bay'] = profileList['members'][profile]['enclosureBay']
                                                    haFileData['portId'] = profileList['members'][profile]['connectionSettings']['connections'][connection]['portId'].replace(" ", "")
                                                    haFileData['mac'] = profileList['members'][profile]['connectionSettings']['connections'][connection]['mac']
                                                    haFileData['bindPortId'] = profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['portId'].replace(" ", "")
                                                    haFileData['bindmac'] = profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['mac']
                                                    haFileData['serialNumber'] = profileList['members'][profile]['serialNumber']
                                                    ipsplit = ipScheme[vip]['netip'].rsplit(".", 1)
                                                    haFileData['ip'] = ipsplit[0] + '.' + ipScheme[vip]['hostip']
                                                    ipScheme[vip]['hostip'] = str(int(ipScheme[vip]['hostip']) + 1)
                                                    haFileData['vid'] = ipScheme[vip]['vid']
                                                    print("TUNNEL HA Entry: %s" % (haFileData))
                                                    haFile.append(haFileData)
                                                    break

                                # Not a tunnel
                                print ("JRT: NOT a tunnel, but VIDs match! Writing to HA File")
                                haFileData = dict()
                                haFileData['profile'] = profileList['members'][profile]['name']
                                haFileData['bay'] = profileList['members'][profile]['enclosureBay']
                                haFileData['portId'] = profileList['members'][profile]['connectionSettings']['connections'][connection]['portId'].replace(" ", "")
                                haFileData['mac'] = profileList['members'][profile]['connectionSettings']['connections'][connection]['mac']
                                haFileData['bindPortId'] = profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['portId'].replace(" ", "")
                                haFileData['bindmac'] = profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['mac']
                                haFileData['serialNumber'] = profileList['members'][profile]['serialNumber']
                                print("JRT: Not a Tunnel: HA Entry: %s" % (haFileData))
                                for vlan in xrange(0, int(len(ipScheme))):
                                    print("vlan: %s" % (vlan))
                                    if (ipScheme[vlan]['vid'] == connectionVid):
                                        print ("JRT: FOUND match VID")
                                        ipsplit = ipScheme[vlan]['netip'].rsplit(".", 1)
                                        haFileData['ip'] = ipsplit[0] + '.' + ipScheme[vlan]['hostip']
                                        ipScheme[vlan]['hostip'] = str(int(ipScheme[vlan]['hostip']) + 1)
                                        if re.match(r'ISCSI[-_].*|FCOE[-_].*|PXE([-_].*)?|IC([-_].*)?|.*Tunnel.*', networkName, re.I) or profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['boot']['priority'] != 'NotBootable':
                                            break
                                        else:
                                            haFileData['vid'] = 'X'
                                        print("HA Entry: %s" % (haFileData))
                                        haFile.append(haFileData)
                                        break

                            ##########################################################

                        elif (('network-sets' in profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['networkUri']) and
                              ('network-sets' in profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'])):
                            for nwset in xrange(0, int(len(nwSetList['members']))):
                                if profileList['members'][profile]['connectionSettings']['connections'][connection]['networkUri'] == nwSetList['members'][nwset]['uri']:
                                    for network in xrange(0, int(len(nwSetList['members'][nwset]['networks']))):
                                        for bindNwset in xrange(0, int(len(nwSetList['members']))):
                                            if profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['networkUri'] == nwSetList['members'][bindNwset]['uri']:
                                                for bindnetwork in xrange(0, int(len(nwSetList['members'][bindNwset]['networks']))):
                                                    if (nwSetList['members'][nwset]['networks'][network]['vlanId'] == nwSetList['members'][bindNwset]['networks'][bindnetwork]['vlanId']):
                                                        haFileData = dict()
                                                        haFileData['profile'] = profileList['members'][profile]['name']
                                                        haFileData['bay'] = profileList['members'][profile]['enclosureBay']
                                                        haFileData['portId'] = profileList['members'][profile]['connectionSettings']['connections'][connection]['portId'].replace(" ", "")
                                                        haFileData['mac'] = profileList['members'][profile]['connectionSettings']['connections'][connection]['mac']
                                                        haFileData['bindPortId'] = profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['portId'].replace(" ", "")
                                                        haFileData['bindmac'] = profileList['members'][profile]['connectionSettings']['connections'][bindconnection]['mac']
                                                        haFileData['serialNumber'] = profileList['members'][profile]['serialNumber']
                                                        for vlan in xrange(0, int(len(ipScheme))):
                                                            if (ipScheme[vlan]['vid'] == nwSetList['members'][nwset]['networks'][network]['vlanId']):
                                                                ipsplit = ipScheme[vlan]['netip'].rsplit(".", 1)
                                                                haFileData['ip'] = ipsplit[0] + '.' + ipScheme[vlan]['hostip']
                                                                ipScheme[vlan]['hostip'] = str(int(ipScheme[vlan]['hostip']) + 1)
                                                                if (nwSetList['members'][nwset]['networks'][network]['uri'] != nwSetList['members'][nwset]['nativeNetworkUri']):
                                                                    # Only add the vid for the non-native/untagged network in the network set
                                                                    haFileData['vid'] = ipScheme[vlan]['vid']
                                                                else:
                                                                    haFileData['vid'] = 'X'
                                                                print("HA Entry: %s" % (haFileData))
                                                                haFile.append(haFileData)
                                                                break
                        else:
                            logger.log.warn("Profile is not configured for high availability.")

        if (len(haFile) > 0):
            profileList['members'][profile]['hafile'] = haFile


def splitPortId(connPortId):
    """
    :py:func:`splitPortId` splits the connection portId to determine the port type, device slot,
     physical port and virtual port.

    **Args**:
        *connPortId* (string)  : Port ID string that looks like Lom 1:1-a, Flb 2:2-d, or Mezz 3:1-b\n

    **Returns**:
        *portId*       (dict)  : Port ID dict that includes port type, device slot, physical port
                                 and virtual port\n
    """

    portId = dict()

    # Split the connection port id to get the port type (Flb, Lom, Mezz) and port map (1:1-a)
    connPortIdData = connPortId.split(" ", 2)
    if (len(connPortIdData) != 2):
        logger.log.error("Connection port id is not what's expected: portId %s." % (connPortId))
        exit(1)
    else:
        portId['portType'] = connPortIdData[0]
        connPortMap = connPortIdData[1]

    # Split the connection port map (1:1-a) to get the device slot (1,2,3) and the Flex10/20 map (1-a)
    connPortMapData = connPortMap.split(":", 2)
    if (len(connPortMapData) != 2):
        logger.log.error("Connection port map is not what's expected: Port map %s." % (connPortMapData))
        exit(1)
    else:
        portId['devSlot'] = connPortMapData[0]
        flexMap = connPortMapData[1]

    # Split the flexMap (1-a) to get phy and virt port
    flexMapData = flexMap.split("-", 2)
    if (len(flexMapData) == 1):
        portId['phyPort'] = flexMapData[0]
        portId['virtPort'] = None
    elif (len(flexMapData) != 2):
        logger.log.error("Flex10/20 map is not what's expected: Flex10/20 map %s." % (flexMap))
        exit(1)
    else:
        portId['phyPort'] = flexMapData[0]
        portId['virtPort'] = flexMapData[1]

    return portId


def writeHAfile(HA_List):
    """
    :py:func:`writeHAfile` iterates over the HAList list and writes the contents of
     the dicts to the HA_ipaddr.conf file.

    **Args**:
        *HA_List* (list)  : A list of dicts that points to the contents of the HA file.\n

    """

    f = open(HA_FILE_NAME, 'w')
    for line in xrange(0, int(len(HA_List))):
        if 'vid' in HA_List[line]:
            f.write(str(HA_List[line]['profile']) + ' ' +
                    str(HA_List[line]['bay']) + ' ' +
                    str(HA_List[line]['portId']) + ' ' +
                    str(HA_List[line]['mac']) + ' ' +
                    str(HA_List[line]['bindPortId']) + ' ' +
                    str(HA_List[line]['bindmac']) + ' ' +
                    str(HA_List[line]['vid']) + ' ' +
                    str(HA_List[line]['ip']) + ' ' +
                    str(HA_List[line]['serialNumber']) + '\n')
        else:
            f.write(str(HA_List[line]['profile']) + ' ' +
                    str(HA_List[line]['bay']) + ' ' +
                    str(HA_List[line]['portId']) + ' ' +
                    str(HA_List[line]['mac']) + ' ' +
                    str(HA_List[line]['bindPortId']) + ' ' +
                    str(HA_List[line]['bindmac']) + ' ' +
                    str(HA_List[line]['ip']) + ' ' +
                    str(HA_List[line]['serialNumber']) + '\n')
            continue
    f.close


def sortHAList(profileList, fileLineList=None):
    """
    :py:func:`sortHAList` iterates over the profile list and appends the contents of
     each profiles hafile list of dicts to a single list.  Once this list is combined
     then it is sorted so that it's human readable.

    **Args**:
        *profileList* (dict)  : Profile dict that points to a list of members\n

    """
    hafile = []
    for profile in xrange(0, int(len(profileList['members']))):
        if (profileList['members'][profile].get('hafile', None) is not None):
            for line in xrange(0, int(len(profileList['members'][profile]['hafile']))):
                hafile.append(profileList['members'][profile]['hafile'][line])

    if fileLineList is not None:
        hafile.extend(fileLineList)

    sortedHA = sorted(hafile, key=lambda k: (k['serialNumber'], k['portId'], k['ip']))

    return sortedHA


def checkForDups(HA_List):
    """
    :py:func:`checkForDups` iterates over the HAList and searches for duplicate IPs.

    **Args**
        *HA_List* (list)        : The sorted HA data list of dicts
    """

    for line in xrange(0, int(len(HA_List))):
        for searchline in xrange(line + 1, int(len(HA_List))):
            if (HA_List[line]['ip'] != HA_List[searchline]['ip']):
                continue
            else:
                logger.log.warn("ERROR: Found duplicate IP: %s" % (HA_List[line]['ip']))
                exit(1)

    logger.log.info("No duplicate IP addresses found.")


def main():
    """
    """

    # #######################################################################
    # Get the command line parameters
    # #######################################################################
    getCmdLineParam()

    # #######################################################################
    # Create a login session
    # #######################################################################
    logger.log.info("Creating login session.")
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
        logger.log.info("Reading the %s file" % HA_FILE)
        pingUtils = PingUtils(ip=CIC_IP, sessionId=authToken)
        fileLineList = pingUtils.readFileLineByLine(HA_FILE)

    # #######################################################################
    # Get the ethernet networks list
    # #######################################################################
    logger.log.info("Creating Ethernet networks.")
    ethBase = NetworkBase(ip=CIC_IP, sessionId=authToken)
    ethNetList = ethBase.getEthNets()

    # #######################################################################
    # Get the network set list and associate the vid to the network uris
    # #######################################################################
    logger.log.info("Getting network sets.")
    nwSetBase = NetworkSetBase(ip=CIC_IP, sessionId=authToken)
    nwSetList = nwSetBase.getNetworkSet(CIC_IP)
    addVidToNetworkSet(nwSetList, ethNetList)

    # #######################################################################
    # Get the server profile list
    # #######################################################################
    logger.log.info("Getting server profiles.")
    profileBase = ProfileBase(ip=CIC_IP, sessionId=authToken)
    profileList = profileBase.getProfiles(filter="count=100")

    # #######################################################################
    # Get the tunnel uri list
    # #######################################################################
    logger.log.info("Getting tunnel uris.")
    tunnelUriList = getTunnelsUri(ethNetList)

    # #######################################################################
    # Initialize IP Addressing scheme
    # #######################################################################
    logger.log.info("Initializing IP scheme. This may take a minute or two.")
    ipScheme = initIpAddrScheme(HA_FILE)
    checkForFile(HA_FILE_NAME)

    # #######################################################################
    # Iterate over the profile list and bind the devices
    # #######################################################################
    logger.log.info("Binding the connections within the profile")
    bindDevices(profileList, ipScheme, ethNetList, nwSetList, tunnelUriList, startTunnelId=START_TUNNEL_ID)
    # JRT bindDevices(profileList, ipScheme, ethNetList, nwSetList)

    # #######################################################################
    # Combine the HA_file contents and sort it so that it's human readable
    # #######################################################################
    logger.log.info("Sorting the contents of the %s file" % HA_FILE)
    if HA_FILE != "":
        HA_List = sortHAList(profileList, fileLineList)
    else:
        HA_List = sortHAList(profileList)

    # JRT pdb.set_trace()
    # #######################################################################
    # Check for duplicate IPs
    # #######################################################################
    logger.log.info("Checking for duplicate IPs")
    checkForDups(HA_List)

    # #######################################################################
    # Write the HA file
    # #######################################################################
    logger.log.info("Writing %s file." % HA_FILE)
    writeHAfile(HA_List)


if __name__ == "__main__":
    main()
