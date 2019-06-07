#!/usr/local/bin/python

import logging
import sys
import re
import tempfile
import os
import datetime
import time
import copy
import json
import string
import subprocess
import pprint
from os import write
from logconfigmodule import Logger
from cicserverprofiles import ProfileBase
from cicsystemsmodule import (EncBase, ServerHwBase)
from cicconnectivitymodule import (InterconnectBase, LogicalInterconnectBase)
libLogger = "api-logger"
consoleLogger = "robust-term"


class PingUtils(object):

    def __init__(self, ip=None, sessionId=None):
        self.applip = ip
        self.sessionId = sessionId
        self.log = logging.getLogger(consoleLogger)
        self.file = logging.getLogger(libLogger)

    def pingSequential(self, ip, count, interval, retries):
        self.ip = ip
        self.count = count
        self.interval = interval
        self.retries = retries

        try:
            ping = subprocess.Popen(["ping", "-c", self.count, "-i", self.interval, self.ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, error = ping.communicate(input)

            if ping.returncode == 0:
                self.log.info("IP %s is reachable" % self.ip)
            elif ping.returncode != 0 and self.retries > 0:
                for retry in xrange(self.retries + 1):
                    time.sleep(1)
                    self.log.info("IP %s is NOT reachable retry %d" % (self.ip, retry + 1))
                    ping = subprocess.Popen(["ping", "-c", "1", "-i", self.interval, self.ip],
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)

                    out, error = ping.communicate(input)
                    if ping.returncode == 0:
                        self.log.info("IP %s is reachable" % self.ip)
                        break
                    if retry == self.retries:
                        self.file.info("IP %s is NOT reachable and failed all retries" % self.ip)
                        return 1
            else:
                self.file.info("IP %s is NOT reachable" % self.ip)
                return 1

        except Exception as e:
            msg = "Exception occured while attempting to ping"
            raise Exception(msg, e)

        return 0

    def pingParallel(self, ip, count, interval):
        self.ip = ip
        self.count = count
        self.interval = interval

        try:
            ping = subprocess.Popen(["ping", "-c", self.count, "-i", self.interval, self.ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, error = ping.communicate(input)

            if error:
                self.file.warn("Error pinging %s, Returned: %s " % (ip, error))
                return out, error
            else:
                return out

        except Exception as e:
            msg = "Exception occured while attempting to ping"
            raise Exception(msg, e)

    def getIps(self, ipaddrFile):
        self.ipaddrFile = ipaddrFile
        self.ipList = []

        try:
            ipstring = open(self.ipaddrFile)
        except Exception as e:
            msg = "Failed to open file %s" % (self.ipaddrFile)
            file.info(msg)
            raise Exception(msg, e)

        ippattern = '(\d+){1,3}\.(\d+){1,3}\.(\d+){1,3}\.(\d+){1,3}'
        for line in ipstring:
            matches = re.search(ippattern, line)
            if matches:
                ip = matches.group(0)
                self.ipList.append(ip)
            else:
                continue

        ipstring.close()
        return self.ipList

    def getIpsFromFile(self, ipaddrFile, serverList):
        self.ipaddrFile = ipaddrFile
        self.serverList = serverList
        self.ipList = []

        try:
            ipstring = open(self.ipaddrFile)
        except Exception as e:
            msg = "Failed to open file %s" % (self.ipaddrFile)
            self.file.info(msg)
            raise Exception(msg, e)

        profileBase = ProfileBase(ip=self.applip, sessionId=self.sessionId)

        self.profilePwrStates = []
        ippattern = '(\d+){1,3}\.(\d+){1,3}\.(\d+){1,3}\.(\d+){1,3}'

        for line in ipstring:
            matches = re.search(ippattern, line)
            if matches:
                ip = matches.group(0)
                profilename = line.split(" ", 1)[0]
                FOUND = False

                for profile in xrange(len(self.profilePwrStates)):
                    if profilename in self.profilePwrStates[profile]['name']:
                        FOUND = True

                if not FOUND:
                    for server in serverList['members']:
                        if server['serverProfileUri'] is None:
                            continue
                        profileDto = profileBase.getProfile(uri=server['serverProfileUri'])
                        if profileDto['name'] == profilename:
                            self.powerstate = dict()
                            self.powerstate['name'] = profileDto['name']
                            self.powerstate['power'] = server['powerState']
                            self.profilePwrStates.append(self.powerstate)
                            if self.powerstate['power'] == "On":
                                self.ipList.append(ip)
                            else:
                                self.log.warn("Server %s is powered off" % (server['name']))
                            break
                        else:
                            continue
                else:
                    for profile in xrange(len(self.profilePwrStates)):
                        if profilename == self.profilePwrStates[profile]['name'] and self.profilePwrStates[profile]['power'] == "On":
                            self.ipList.append(ip)
        ipstring.close()
        return self.ipList

    def getIpsFromFileTrimmed(self, ipaddrFile, serverList, maxips):
        self.ipaddrFile = ipaddrFile
        self.serverList = serverList
        self.maxips = maxips
        self.ipList = []
        self.ipListTrimmed = []

        self.ipList = self.readFileLineByLine(self.ipaddrFile)
        if (len(self.ipList) < int(maxips)):
            self.log.warn("The IP list total is %d which is less than the requested max of %s" % (len(self.ipList), maxips))
            self.log.warn("IP list trimming is not required")
            return self.ipList

        profileBase = ProfileBase(ip=self.applip, sessionId=self.sessionId)
        self.profilePwrStates = []

        # Iterate over the ipList and filter the servers that are powered off
        for line in xrange(0, int(len(self.ipList))):
            FOUND = False
            for profile in xrange(len(self.profilePwrStates)):
                if self.ipList[line]['profile'] in self.profilePwrStates[profile]['name']:
                    FOUND = True

            if not FOUND:
                for server in serverList['members']:
                    if server['serverProfileUri'] is None:
                        continue
                    profileDto = profileBase.getProfile(uri=server['serverProfileUri'])
                    if profileDto['name'] == self.ipList[line]['profile']:
                        self.powerstate = dict()
                        self.powerstate['name'] = profileDto['name']
                        self.powerstate['power'] = server['powerState']
                        self.profilePwrStates.append(self.powerstate)
                        if self.powerstate['power'] == "On":
                            self.ipListTrimmed.append(self.ipList[line])
                            break
                        else:
                            self.log.warn("Server %s is powered off" % (server['name']))
                            break
                    else:
                        continue

            else:
                for profile in xrange(len(self.profilePwrStates)):
                    if self.ipList[line]['profile'] == self.profilePwrStates[profile]['name'] and self.profilePwrStates[profile]['power'] == "On":
                        self.ipListTrimmed.append(self.ipList[line])

        # Move the the data to the ipList list so that it can be iterated over when we need to trim it further later
        self.ipList = []
        self.ipList = copy.deepcopy(self.ipListTrimmed)
        self.ipListTrimmed = []

        # Iterate over the ipList and create a list of dicts that describe the complete list of vids
        # that need to be covered in the trimmed list
        self.vidslist = []
        for line in xrange(0, int(len(self.ipList))):
            if len(self.ipList[line]) == 8:
                # This line does not contain a vid so continue
                continue
            if len(self.vidslist) == 0:
                self.vid = dict()
                self.vid['vid'] = self.ipList[line]['vid']
                self.vid['ip'] = None
                self.vidslist.append(self.vid)
            for vid in xrange(0, int(len(self.vidslist))):
                if self.vidslist[vid]['vid'] == self.ipList[line]['vid']:
                    # The vid is already in the list so break
                    break
                if vid == len(self.vidslist) - 1:
                    # The vid is not in the list so add it
                    self.vid = dict()
                    self.vid['vid'] = self.ipList[line]['vid']
                    self.vid['ip'] = None
                    self.vidslist.append(self.vid)

        # Iterate over the ipList and add all the untagged networks to the ipListTrimmed.  Since there can
        # only be one untagged network on a downlink we will include all of these networks.
        for line in xrange(0, int(len(self.ipList))):
            if len(self.ipList[line]) == 8:
                self.ipListTrimmed.append(self.ipList[line]['ip'])
                self.vid = dict()
                self.vid['vid'] = "Untagged"
                self.vid['ip'] = self.ipList[line]['ip']
                self.vidslist.append(self.vid)

        # Iterate over the ipList and add a single IP for each LF that has more than one IP assigned. In other
        # words, filter the networks sets and add only one IP per network set
        lastAddedProfile = None
        lastAddedPortId = None
        lastAddedBay = None

        # TODO: Remove the added variable once the algorithm is cleaned up so we don't need the
        # check below to ensure that we don't get caught in an infinite loop
        added = 0
        Adding = True
        while Adding:
            for line in xrange(0, int(len(self.ipList))):
                if (len(self.ipList[line]) == 8):
                    # Untagged networks have already been added so continue
                    continue
                elif ((line == 0) and (lastAddedProfile is None)):
                    # Add the first IP
                    self.ipListTrimmed.append(self.ipList[line]['ip'])
                    # Update the vidslist to show that this IP was added to the network
                    for vid in xrange(0, int(len(self.vidslist))):
                        if self.ipList[line]['vid'] == self.vidslist[vid]['vid']:
                            ips = []
                            ips.append(self.ipList[line]['ip'])
                            self.vidslist[vid]['ip'] = ips
                            self.vidslist[vid]['portId'] = self.ipList[line]['portId']
                            self.vidslist[vid]['bay'] = self.ipList[line]['bay']
                            self.vidslist[vid]['profile'] = self.ipList[line]['profile']
                            lastAddedProfile = self.ipList[line]['profile']
                            lastAddedPortId = self.ipList[line]['portId']
                            lastAddedBay = self.ipList[line]['bay']
                            break
                elif ((self.ipList[line]['portId'] == self.ipList[line - 1]['portId']) and
                      (self.ipList[line]['profile'] == self.ipList[line - 1]['profile']) and
                      (self.ipList[line]['bay'] == self.ipList[line - 1]['bay'])):
                    if ((lastAddedProfile == self.ipList[line]['profile']) and
                            (lastAddedPortId == self.ipList[line]['portId']) and
                            (lastAddedBay == self.ipList[line]['bay'])):
                        # Only add one IP from the network sets each time you iterate over the ipList
                        continue

                    for portmap in xrange(line, int(len(self.ipList))):
                        if ((self.ipList[portmap]['profile'] != self.ipList[line]['profile']) or
                                (self.ipList[portmap]['portId'] != self.ipList[line]['portId']) or
                                (self.ipList[portmap]['bay'] != self.ipList[line]['bay'])):
                            break
                        for vid in xrange(0, int(len(self.vidslist))):
                            if ((self.ipList[portmap]['vid'] == self.vidslist[vid]['vid']) and
                                    (self.vidslist[vid]['ip'] is None)):
                                self.ipListTrimmed.append(self.ipList[portmap]['ip'])
                                ips = []
                                ips.append(self.ipList[portmap]['ip'])
                                self.vidslist[vid]['ip'] = ips
                                self.vidslist[vid]['portId'] = self.ipList[portmap]['portId']
                                self.vidslist[vid]['bay'] = self.ipList[portmap]['bay']
                                self.vidslist[vid]['profile'] = self.ipList[portmap]['profile']
                                lastAddedProfile = self.ipList[portmap]['profile']
                                lastAddedPortId = self.ipList[portmap]['portId']
                                lastAddedBay = self.ipList[portmap]['bay']
                                break
                        break
                else:
                    continue

            # Iterate over the vidslist to ensure that networks have been covered
            # and change Adding to False once they have been covered

            # TODO Remove the count variable and the logic that detects when the IP is equal to None
            # and then verifies if the count and added are equal.  This is the condition where we
            # are caught in an infinite loop where we probably got most the IPs included but the
            # alogrithm failed to get all of them.
            count = 0
            for vid in xrange(0, int(len(self.vidslist))):
                if (self.vidslist[vid].get('ip', None) is None):
                    for net in xrange(0, int(len(self.vidslist))):
                        if (self.vidslist[net].get('ip', None) is None):
                            count += 1
                    if count != added:
                        added = count
                        Adding = True
                        break
                    else:
                        Adding = False
                        break
                elif (vid == (len(self.vidslist) - 1)):
                    Adding = False
                else:
                    continue

        if (len(self.ipListTrimmed) > int(maxips)):
            self.log.warn("The IP list can only be trimmed to %d where the requested max was %s" % (len(self.ipListTrimmed), maxips))
            # TODO Print the contents of the self.vidslist to the log file.
            return self.ipListTrimmed

        Adding = True
        while Adding:
            for line in xrange(0, int(len(self.ipList))):
                if not Adding:
                    break
                if (line == 0):
                    # The first line was already added so continue
                    continue
                elif (len(self.ipList[line]) == 8):
                    # Untagged networks have already been added so continue
                    continue
                elif ((self.ipList[line]['portId'] == self.ipList[line - 1]['portId']) and
                      (self.ipList[line]['profile'] == self.ipList[line - 1]['profile']) and
                      (self.ipList[line]['bay'] == self.ipList[line - 1]['bay'])):
                    if ((lastAddedProfile == self.ipList[line]['profile']) and
                            (lastAddedPortId == self.ipList[line]['portId']) and
                            (lastAddedBay == self.ipList[line]['bay'])):
                        # Only add one IP from the network sets each time you iterate over the ipList
                        continue

                    for portmap in xrange(line, int(len(self.ipList))):
                        if ((self.ipList[portmap]['profile'] != self.ipList[line]['profile']) or
                                (self.ipList[portmap]['portId'] != self.ipList[line]['portId']) or
                                (self.ipList[portmap]['bay'] != self.ipList[line]['bay'])):
                            break
                        for vid in xrange(0, int(len(self.vidslist))):
                            if (self.ipList[portmap]['vid'] == self.vidslist[vid]['vid']):
                                self.ipListTrimmed.append(self.ipList[portmap]['ip'])
                                self.vidslist[vid]['ip'].append(self.ipList[portmap]['ip'])
                                self.vidslist[vid]['portId'] = self.ipList[portmap]['portId']
                                self.vidslist[vid]['bay'] = self.ipList[portmap]['bay']
                                self.vidslist[vid]['profile'] = self.ipList[portmap]['profile']
                                lastAddedProfile = self.ipList[portmap]['profile']
                                lastAddedPortId = self.ipList[portmap]['portId']
                                lastAddedBay = self.ipList[portmap]['bay']
                                if (len(self.ipListTrimmed) >= int(maxips)):
                                    Adding = False
                                break
                        break
                else:
                    continue

        self.log.warn("The IP list was trimmed to %d" % (len(self.ipListTrimmed)))
        # TODO Print the contents of the self.vidslist to the log file.
        return self.ipListTrimmed

    def readFileLineByLine(self, ipaddrFile):
        self.ipaddrFile = ipaddrFile
        self.ipList = []

        try:
            ipstring = open(self.ipaddrFile)
        except Exception as e:
            msg = "Failed to open file %s" % (self.ipaddrFile)
            self.file.error(msg)
            raise Exception(msg, e)

        for line in ipstring:
            self.line = dict()
            tokens = line.split(" ")

            if len(tokens) != 8 and len(tokens) != 9:
                self.file.warn("Warning:  The number of tokens on the line is not 8 or 9 num=%d" % (len(tokens)))
                break

            self.line['profile'] = tokens[0]
            self.line['bay'] = tokens[1]
            self.line['portId'] = tokens[2]
            self.line['mac'] = tokens[3]
            self.line['bindPortId'] = tokens[4]
            self.line['bindmac'] = tokens[5]
            if len(tokens) == 8:
                self.line['ip'] = tokens[6]
                self.line['serialNumber'] = tokens[7].strip('\n')
            if len(tokens) == 9:
                self.line['vid'] = tokens[6]
                self.line['ip'] = tokens[7]
                self.line['serialNumber'] = tokens[8].strip('\n')

            self.ipList.append(self.line)

        ipstring.close()
        return self.ipList

    def waitDeviceReachable(self, name, ip, duration, interval=5):
        self.name = name
        self.ip = ip

        abortTime = duration
        startTime = time.time()

        if os.name == 'nt':
            rc = 1
        else:
            rc = 0

        while True:
            ping = subprocess.Popen(["ping", "-c", "1", ip],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            out, error = ping.communicate(input)

            if ping.returncode == rc:
                self.log.info("%s: %s is reachable" % (self.name, self.ip))
                break
            else:
                self.log.info("%s: %s is NOT reachable" % (self.name, self.ip))
                deltaTime = time.time() - startTime
                if deltaTime >= abortTime:
                    return 1
                else:
                    time.sleep(interval)
        return

    def checkPingResults(self, ipList, baseLogDir):
        self.ipList = ipList
        self.baseLogDir = baseLogDir

        self.file.info("Checking IP log files for packet loss.")
        noErrorsFound = True
        for ip in ipList:
            # Setup log file directory vars
            logDir = self.baseLogDir + "/" + ip
            ipFile = logDir + "/" + ip + ".log"

            # Call function to read in the file:
            val2check = "packet loss"
            lines = self.checkFileLineByLine(val2check, ipFile)
            valuesList = []
            splitter = ","
            for line in lines:
                block = self.splitLine(line, splitter)
                for nextItem in block:
                    values = self.checkValue(nextItem, val2check)
                    if values is not None:
                        valuesList.append(values)

            splitter = "%"
            for val in valuesList:
                results = self.splitLine(val, splitter)
                result = int(results[0])
                if result != 0:
                    self.file.error("ERROR: %s" % (val))
                    noErrorsFound = False
                else:
                    continue
        if noErrorsFound:
            self.file.info("No packet loss found.")
            return "PASS"
        else:
            return "FAIL"

    def checkPingResultsNew(self, ipList, baseLogDir, maxPkt):
        self.ipList = ipList
        self.baseLogDir = baseLogDir

        self.file.info("Checking IP log files for packet loss.")
        noErrorsFound = True
        for ip in ipList:
            # Setup log file directory vars
            logDir = self.baseLogDir + "/" + ip
            ipFile = logDir + "/" + ip + ".log"

            # Call function to read in the file:
            lines = self.checkFileLineByLine("packet loss", ipFile)
            valuesList = []
            for line in lines:
                block = self.splitLine(line, ",")
                pktXmitted = []
                pktRecvd = []
                for nextItem in block:
                    values = self.checkValue(nextItem, "packets transmitted")
                    if values is not None:
                        pktXmitted = values.split(" ")
                    values = self.checkValue(nextItem, "received")
                    if values is not None:
                        pktRecvd = values.split(" ")

                    if ((len(pktXmitted) > 0) and (len(pktRecvd) > 0)):
                        if (int(pktXmitted[0]) - int(pktRecvd[1]) >= int(maxPkt)):
                            self.file.error("IP: %s, packet loss count: %d" % (ip, (int(pktXmitted[0]) - int(pktRecvd[1]))))
                            noErrorsFound = False
                        else:
                            self.file.debug("IP: %s, packet loss count: %d" % (ip, (int(pktXmitted[0]) - int(pktRecvd[1]))))

        if noErrorsFound:
            return "PASS"
        else:
            return "FAIL"

    def checkFileLineByLine(self, val2check, fileName):

        linesFound = 0
        self.file.debug("Checking for %s in %s" % (val2check, fileName))

        try:
            lineList = []
            # Read in file line by line
            for line in open(fileName, 'r'):
                # Check line for 'packet loss' string
                if val2check in line:
                    linesFound += 1
                    lineList.append(line)
                else:
                    continue

        except Exception as e:
            msg = "Failed to open file %s" % (fileName)
            raise Exception(msg, e)

        return lineList

    def checkValue(self, list, val2check):
        if val2check in list:
            return list

    def splitLine(self, line, splitter):
        newLine = line.split(splitter)
        return newLine


class DirUtils(object):

    def __init__(self):
        self.file = logging.getLogger(libLogger)

    def createDir(self, dirName):

        try:
            if not os.path.isdir(dirName):
                os.makedirs(dirName)
            else:
                self.file.debug("%s found directory. Not creating." % (dirName))

        except Exception as e:
            msg = "Failed to create directory %s" % (dirName)
            self.file.debug(msg)

            raise Exception(msg, e)


class IpAddrUtils(object):

    def __init__(self):
        self.file = logging.getLogger(libLogger)

    def init10IpaddrScheme(self):
        first_octet = 172
        second_octet = 16
        third_octet = 0
        fourth_octet = 0
        ipscheme = []

        for vlan in xrange(0, 4096 + 1):
            xlation = dict()
            # NOTE: vid = 0 correlates to a tunnel network
            mod = vlan % 128
            if mod == 0 and vlan != 0:
                xlation['netip'] = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(fourth_octet)
                third_octet = 1
                second_octet += 1
            else:
                xlation['netip'] = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(fourth_octet)
                third_octet += 1
            xlation['vid'] = vlan
            ipscheme.append(xlation)

        return ipscheme


class ResourceBase(object):

    def __init__(self, ip=None, sessionId=None):
        self.ip = ip
        self.sessionId = sessionId
        self.file = logging.getLogger(libLogger)

    def discoverResources(self):
        resource = dict()

        resource['encs'] = self.getEncList()
        resource['servers'] = self.getServerList()
        resource['profiles'] = self.getProfileList()
        resource['ics'] = self.getIcList()
        resource['lis'] = self.getLiList()

        return resource

    def getEncList(self):

        encBase = EncBase(ip=self.ip, sessionId=self.sessionId)
        self.file.info("Getting enclosure list.")
        encList = encBase.listEnc(filter='start=-1&count=-1')

        return encList

    def getServerList(self):

        serverBase = ServerHwBase(ip=self.ip, sessionId=self.sessionId)
        self.file.info("Getting server hardware list.")
        serverList = serverBase.listServerHw(filter=None)

        return serverList

    def getProfileList(self):

        profileBase = ProfileBase(ip=self.ip, sessionId=self.sessionId)
        self.file.info("Getting profile list.")
        profileList = profileBase.getProfiles(filter=None)

        return profileList

    def getIcList(self):

        icBase = InterconnectBase(ip=self.ip, sessionId=self.sessionId)
        self.file.info("Getting interconnect list.")
        icList = icBase.getInterconnects()

        return icList

    def getLiList(self):

        liBase = LogicalInterconnectBase(ip=self.ip, sessionId=self.sessionId)
        self.file.info("Getting logical interconnect list.")
        liList = liBase.getLogicalInterconnects

        return liList
