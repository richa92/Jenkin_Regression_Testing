#!/usr/local/bin/python
# ##################################################################
# Script: backup.py
# Summary:
#      This script triggers a backup of an appliance.  Once
# the backup has been created it is downloaded to the local server.
# Requires:
# You must have a XML with the appliance IP and login credentials.
#
# ##################################################################

# ############# TODO ######################
# Add command line user/password arguments
#

# Imports
import sys
import commands
import time
import re
import os
import datetime
import logging
import argparse
(index, pwd) = commands.getstatusoutput("pwd")
pwd = pwd + "/lib"

sys.path.append(pwd)

import pdb
import logconfigmodule
from logconfigmodule import Logger
from datetime import datetime
from cifitxmlmodule import CiFitXml
from cicsecuritymodule import LoginSession
from ciccontrollermodule import BackupAppliance
from ciccontrollermodule import DownloadBackup
from taskstatusmodule import CheckTaskStatus

# Variables
sampleDelay = False
applianceIP = "15.178.0.0"
now = datetime.now()

# JRT xmlFile = "/root/ci-fit/trunk/ci-fit/tools/appliance/example.xml"
xmlFile = "example.xml"
cifitVer = "1.0"

# log variables
libLogger = "api-logger"
consoleLogger = "backup-term"
fileLogger = "backup-logger"
logFile = 'backup-' + now.strftime("%m-%d-%Y_%H:%M") + '.log'


# JRT    pdb.set_trace() #<-- set a break point in the code

# Methods
# - Command Line Parsing.
def getCmdLineParam():
    global xmlFile, ip

    # Instantiate the parser
    parser = argparse.ArgumentParser(description="backup.py executes and monitors a backup of the appliance.  Defaults: XML file: example.xml. Requires XML file.")

    # Setup/Define command-line arguments:
    parser.add_argument("-i", "--IP", "--i", dest="applianceIP", help="IP address of the appliance. Example: -i 10.10.10.10'", default=applianceIP)
    parser.add_argument("-f", "--xmlFile", "--f", dest="xmlFile", help="Enter the name of the XML file you wish to use.", default=xmlFile)

    args = parser.parse_args()

    # Assign values to global variables
    xmlFile = args.xmlFile
    ip = args.applianceIP


# - Check if task finnished:
def checkTaskState(ip, sessionID, taskURI):

    statusURL = CheckTaskStatus(ip, sessionID, taskURI)
    taskData = statusURL.getTaskStatus(ip, sessionID, taskURI)
    print "taskData = ", taskData
    taskName = taskData['name']
    taskStatus = taskData['taskState']

    while taskStatus == "Running":
        os.system('clear')
        print "Task: '%s' is %s." % (taskName, taskStatus)
        time.sleep(1)
        os.system('clear')
        print "Task: '%s' is %s.." % (taskName, taskStatus)
        time.sleep(1)
        os.system('clear')
        print "Task: '%s' is %s..." % (taskName, taskStatus)
        time.sleep(1)
        statusURL = CheckTaskStatus(ip, sessionID, taskURI)
        taskData = statusURL.getTaskStatus(ip, sessionID, taskURI)
        taskName = taskData['name']
        taskStatus = taskData['taskState']
    os.system('clear')
    print "Task: '%s' has %s" % (taskName, taskStatus)
    time.sleep(1)


# ####
# - MAIN
def main():
    os.system('clear')

    # #####################################################################
    # Get the command line parameters
    # #####################################################################
    getCmdLineParam()
    print "------------------------------------------------------------"
    print "xmlFile = ", xmlFile
    print "------------------------------------------------------------"

    # #####################################################################
    # Instantiate the logger
    # #####################################################################
    logger = Logger(filename=logFile, loggername=fileLogger,
                    tloggername=consoleLogger, libloggername=libLogger)

    # #######################################################################
    # Instantiate the Xml object and verify that the version is correct
    # #######################################################################
    # JRT chomonXml = ChoMonXml()
    cifitXml = CiFitXml()
    cifitXmlVer = cifitXml.getCiFitVer(xmlFile)
    if cifitXmlVer != cifitVer:
        logger.log.critical("CiFit and xml versions don't match - CiFit = %s, XML = %s" % (cifitVer, cifitXmlVer))
        sys.exit(102)

    # #######################################################################
    # Get appliance credentials from the xml file and create a login session
    # #######################################################################
    logger.log.info("Creating login session.")
    appliance = cifitXml.getAppliance(xmlFile)  # <- appliance is a dict()
    curSession = LoginSession(ip=appliance['ip'], uname=appliance['name'], pw=appliance['password'])
    authToken = curSession.post()
    ip = appliance['ip']  # <- pull value of 'ip' from appliance dict()
    logger.log.info("Appliance IP: %s" % (ip))
    logger.log.info("Current authorization token: %s" % (authToken))

    # #######################################################################
    # Send request to start the backup process.  Returns URI to access the task manager.
    # #######################################################################
    # JRT print "Calling backupAppliance to start backup process and to get task URI"
    logger.log.info("Calling backupAppliance to start backup process and to get task URI.")
    # Instantiate a backup instance:
    backup = BackupAppliance(ip=appliance['ip'], sessionID=authToken)
    backupJsonData = backup.backAppliance(ip=appliance['ip'], sessionID=authToken)
    # Get task URI:
    backupTaskURI = backupJsonData['uri']
    backupFileName = backupJsonData['associatedResourceUri'] + ".bkp"
    logger.log.info("Backup Task URI is: %s" % (backupTaskURI))
    logger.log.info("Backup File Name is: %s" % (backupFileName))

    # #######################################################################
    # Call method to check backup task status
    # #######################################################################
    # Call method to check task status
    logger.log.info("Calling backupTaskState to check the task status.")
    checkTaskState(ip=appliance['ip'], sessionID=authToken, taskURI=backupTaskURI)

    # #######################################################################
    # Call method to get download URI
    # #######################################################################
    logger.log.info("Calling backupPathURL to get the appliance download URI.")
    backupPathURL = DownloadBackup(ip=appliance['ip'], sessionID=authToken, backupURI=backupFileName)
    backupDirURL = backupPathURL.getBackupDownloadURI(ip=appliance['ip'], sessionID=authToken, backupURI=backupFileName)
    logger.log.info("The backup directoty URL: %s" % (backupDirURL))

    # #######################################################################
    # Call to get the URI/URL path to the backup file
    # #######################################################################
    logger.log.info("Calling backupFileData to get the path to the appliance download.")
    print "Calling method to get download URI/URL."
    backupFileData = DownloadBackup(ip=appliance['ip'], sessionID=authToken, backupURI=backupFileName)
    backupData = backupFileData.getBackupData(ip=appliance['ip'], sessionID=authToken, backupURI=backupFileName)
    logger.log.info("Sucessfully gathered the backup data dicts")

    # #######################################################################
    # Call method to download appliance backup file
    # #######################################################################
    logger.log.info("Calling downloadAppBackup to download the appliance backup file.")
    downloadAppBackup = DownloadBackup(ip=appliance['ip'], sessionID=authToken, backupURI=backupData)
    downloadAppBackup = downloadAppBackup.downloadBackupFile(ip=appliance['ip'], sessionID=authToken, backupURI=backupData)
    if downloadAppBackup == 200:
        logger.log.info("Downloaded %s successfully" % (backupFileName))
    else:
        logger.log.info("return code: ", downloadAppBackup)


# Call Main

if __name__ == "__main__":
    main()
