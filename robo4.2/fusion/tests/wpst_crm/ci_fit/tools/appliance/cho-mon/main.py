#!/usr/local/bin/python

import sys
import commands
import getopt
import time
import re
import os
import datetime
import logging
(index, pwd) = commands.getstatusoutput("pwd")
pwd = pwd + "/lib"

sys.path.append(pwd)
import cicsecuritymodule
import dcuxmlmodule
import logconfigmodule
import metricmodule
import libformatresttext
from libformatresttext import FormatRestText
from metricmodule import GetUuid
from metricmodule import GetMetrics
from logconfigmodule import Logger
from cicsecuritymodule import LoginSession
from cicsecuritymodule import UsersBase
from dcuxmlmodule import DcuXml
from cicconnectivitymodule import ConnTypeBase
from cicconnectivitymodule import NetworkBase
from cicconnectivitymodule import NetworkSetBase
from cicsystemsmodule import EncBase
from cicsystemsmodule import EncPreview
from cicsystemsmodule import EncGrpBase
from cicconnectivitymodule import LogicalSwTempBase
from cicconnectivitymodule import UplinkGrpBase
from cicconnectivitymodule import SwitchesBase
from cicsystemsmodule import ServerHwBase
from cicserverprofiles import ProfileBase
import pdb

consoleLogger = "dcu-term"
fileLogger = "dcu-logger"
libLogger = "api-logger"
xmlFile = "config.xml"
encName = "enc-default"
now = datetime.datetime.now()
logFile = 'dcu-' + now.strftime("%m-%d-%Y_%H:%M") + '.log'
dcuVer = "1.0"


def usage():
    print('Usage:')
    print 'dcu.py -f <config.xml> [[-d [OA enc name]] | [-i [OA enc name]]] [-l <logfile pathname>] [-h]'
    sys.exit(100)


def getCmdLineParam(argv):
    global xmlFile, encName, logFile, consoleLogger
    console = logging.getLogger(consoleLogger)

    try:
        opts, args = getopt.getopt(argv, "hf:d:i:l:")
    except getopt.GetoptError:
        usage()

    if not any('-f' in arg for arg in opts):
        usage()

    if any('-d' in arg for arg in opts) and any('-i' in arg for arg in opts):
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt == '-f':
            if arg.startswith('-'):
                usage()
            else:
                xmlFile = arg
                if os.path.isfile(xmlFile):
                    pass
                else:
                    console.error("The xmlconfig file is not a file")
                    sys.exit(101)
        elif opt == '-d':
            if arg.startswith('-'):
                usage()
            else:
                encName = arg
                console.warning("Sorry Charlie... the '-d' option is not implemented yet")
                sys.exit()
        elif opt == '-i':
            if arg.startswith('-'):
                usage()
            else:
                encName = arg
                console.warning("Sorry Charlie... the '-i' option is not implemented yet")
                sys.exit()
        elif opt == '-l':
            if arg.startswith('-'):
                usage()
            else:
                if os.path.exists(arg):
                    logFile = arg + logFile
                else:
                    console.error("Logfile directory path does not exist")
                    sys.exit(103)


def gUuid(dcuXml, ip, uname, pw, sessionID):
    global xmlFile, fileLogger
    print "in get Uuid method in main.py"
    log = logging.getLogger(fileLogger)

    xmlEnclosures = dcuXml.getEnclosures(xmlFile)
    encs = EncBase(ip=ip, sessionId=sessionID)
    # print "encs = ", encs
    for enclosure in xrange(len(xmlEnclosures)):
        xmlEnclosuresAttr = dict()
        xmlEnclosuresAttr = xmlEnclosures[enclosure]
        print "xmlEnclosuersAttr = ", xmlEnclosuresAttr
        encName = xmlEnclosuresAttr['name']
        print "encName = ", encName
        encHostname = xmlEnclosuresAttr['oahostname']
        print "encHostname = ", encHostname
        encUsername = xmlEnclosuresAttr['oausername']
        print "encUsername = ", encUsername
        encPassword = xmlEnclosuresAttr['oapassword']
        print "enPassword = ", encPassword

        log.info("Previewing enclosure %s" % (xmlEnclosuresAttr['name']))
    print "Call getUuid method in GetUuid class here"
    uuidInstance = GetUuid(ip, uname, pw, sessionID)
    uuid = uuidInstance.getUuid()
    # JRT uuid = uuidInstance.getUuid(ip, uname, pw, sessionID)
    print "Now in gUuid method in main: uuid = ", uuid
    return uuid


def getMetrics(dcuXml, ip, uname, pw, sessionID, uuid, startDate, endDate, metric1):
    global xmlFile, fileLogger
    print "In getMetrics method of main.py."

    log = logging.getLogger(fileLogger)

    xmlEnclosures = dcuXml.getEnclosures(xmlFile)
    encs = EncBase(ip=ip, sessionId=sessionID)
    # print "encs = ", encs
    for enclosure in xrange(len(xmlEnclosures)):
        xmlEnclosuresAttr = dict()
        xmlEnclosuresAttr = xmlEnclosures[enclosure]

        log.info("Previewing enclosure %s" % (xmlEnclosuresAttr['name']))

    metricInstance = GetMetrics(ip, uname, pw, sessionID, uuid, startDate, endDate, metric1)
    metrics = metricInstance.getMetric()
    # JRT print "metrics = ", metrics
    return metrics


def formatText(text):
    newtext = FormatRestText(text)
    ftext = newtext.formatText()
    # JRT print "ftext = ", ftext
    return ftext


def main():

    # TODO:  Parse the entire xml file into data structures and then do
    # data validation on the attributes before calling API to configure

    # #####################################################################
    # Instantiate the logger
    # #####################################################################
    logger = Logger(filename=logFile, loggername=fileLogger,
                    tloggername=consoleLogger, libloggername=libLogger)

    # #####################################################################
    # Get the command line parameters
    # #####################################################################
    getCmdLineParam(argv=sys.argv[1:])

    # #######################################################################
    # Instantiate the DcuXml object and verify that the DCU version matches
    # #######################################################################
    dcuXml = DcuXml()
    dcuXmlVer = dcuXml.getDcuVer(xmlFile)
    if dcuXmlVer != dcuVer:
        logger.log.critical("DCU and xml versions don't match - DCU = %s, XML = %s" % (dcuVer, dcuXmlVer))
        sys.exit(102)

    # #######################################################################
    # Get appliance credentials from the xml file and create a login session
    # #######################################################################
    logger.log.info("Creating login session")
    appliance = dcuXml.getAppliance(xmlFile)  # <- appliance is a dict()
    # <- appliance =  {'ip': '15.178.221.59', 'password': 'hpvse123', 'name': 'Administrator'}
    # <- keys = ip, password, name   values: 15.178.221.59, hpvse123, Administrator
    print "appliance = ", appliance
    curSession = LoginSession(ip=appliance['ip'], uname=appliance['name'], pw=appliance['password'])
    print "curSession = ", curSession
    authToken = curSession.post()
    print "authToken = ", authToken
    ip = appliance['ip']  # <- pull value of 'ip' from appliance dict()
    print "ip = ", ip

    # #######################################################################
    # Get UUID
    # #######################################################################
    print "Setting up uuid call: "
    newUuid = gUuid(dcuXml=dcuXml, ip=appliance['ip'], uname=appliance['name'], pw=appliance['password'], sessionID=authToken)

    print "in main now.  newUuid =", newUuid

    # #######################################################################
    # Get metric(s)
    # #######################################################################
    print "Getting enclosure metrics: "
    # Define missing metrics.  Will be replaced by XML data or command line option
    startdate = "2013-03-10T00:42:34.340Z"
    enddate = "2013-03-10T01:42:34.340Z"
    metric1 = "AveragePower"

    # Get metrics
    myMetrics = getMetrics(dcuXml=dcuXml, ip=appliance['ip'], uname=appliance['name'], pw=appliance['password'], sessionID=authToken, uuid=newUuid, startDate=startdate, endDate=enddate, metric1=metric1)
    # JRT print "myMetrics = ", myMetrics

    # Clean up metrics rest text
    formattedMetrics = formatText(myMetrics)
    print "formattedMetrics = ", formattedMetrics


# Call Main

if __name__ == "__main__":
    main()
