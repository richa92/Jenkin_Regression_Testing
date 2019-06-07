#!/usr/local/bin/python


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
from ciccontrollermodule import RestoreAppliance
from ciccontrollermodule import UploadBackup
from taskstatusmodule import CheckTaskStatus

# Variables
sampleDelay = False
applianceIP = "15.178.0.0"
now = datetime.now()

# JRT xmlFile = "/root/ci-fit/trunk/ci-fit/tools/appliance/example.xml"
xmlFile = "example.xml"
cifitVer = "1.0"
backupFile = "latest.pbk"
# log variables
libLogger = "api-logger"
consoleLogger = "restore-term"
fileLogger = "restore-logger"
logFile = 'restore-' + now.strftime("%m-%d-%Y_%H:%M") + '.log'


# JRT    pdb.set_trace() #<-- set a break point in the code

# Methods
# - Command Line Parsing.
def getCmdLineParam():
    global xmlFile, ip, backupFile

    # Instantiate the parser
    parser = argparse.ArgumentParser(description="backup.py executes and monitors a backup of the appliance.  Defaults: XML file: example.xml. Requires: XML file and backup file name.")

    # Setup/Define command-line arguments:
    parser.add_argument("-b", "--backupFile", "--b", dest="backupFile", help="Enter the name of the backup file you wish to user for the restore.", default=backupFile)
    parser.add_argument("-i", "--IP", "--i", dest="applianceIP", help="IP address of the appliance. Example: -i 10.10.10.10'", default=applianceIP)
    parser.add_argument("-f", "--xmlFile", "--f", dest="xmlFile", help="Enter the name of the XML file you wish to use.", default=xmlFile)

    args = parser.parse_args()

    # Assign values to global variables
    backupFile = args.backupFile
    xmlFile = args.xmlFile
    ip = args.applianceIP


# - Check if task finnished:
def checkTaskState(ip, sessionID, taskURI):
    statusURL = CheckTaskStatus(ip, sessionID, taskURI)
    taskData = statusURL.getTaskStatus(ip, sessionID, taskURI)
    print "taskData = ", taskData
    taskName = taskData['type']
    taskStatus = taskData['status']
    progress = taskData['restorePhase']
    startTime = taskData['restoreStartTime']

    print "Task Name: %s, Task Status: %s, Task Progress: %s" % (taskName, taskStatus, progress)
    print "Restore Started: ", startTime
    # JRT pdb.set_trace()

    while taskStatus == "IN_PROGRESS":
        os.system('clear')
        print "Task Name: %s, Task Status: %s, Task Progress: %s" % (taskName, taskStatus, progress)
        print "Restore Started: ", startTime
        time.sleep(1)
        os.system('clear')
        print "Task Name: %s, Task Status: %s, Task Progress: %s." % (taskName, taskStatus, progress)
        print "Restore Started: ", startTime
        time.sleep(1)
        os.system('clear')
        print "Task Name: %s, Task Status: %s, Task Progress: %s.." % (taskName, taskStatus, progress)
        print "Restore Started: ", startTime
        time.sleep(1)
        os.system('clear')
        print "Task Name: %s, Task Status: %s, Task Progress: %s..." % (taskName, taskStatus, progress)
        print "Restore Started: ", startTime
        time.sleep(1)
        statusURL = CheckTaskStatus(ip, sessionID, taskURI)
        taskData = statusURL.getTaskStatus(ip, sessionID, taskURI)
        taskName = taskData['type']
        taskStatus = taskData['status']
        progress = taskData['restorePhase']
        startTime = taskData['restoreStartTime']
        backupName = taskData['id'] + ".bkp"
    os.system('clear')
    print "Task Name: %s, Task Status: %s, Task Progress: %s" % (taskName, taskStatus, progress)
    print "Restore Started: ", startTime
    time.sleep(1)
    # JRT endTime = datetime.now()
    endTime = taskData['modified']
    print "Restore Completed: ", endTime
    print "Restored appliance to %s backup" % (backupName)
    # JRT print "taskData = ", taskData


# ####
# - MAIN
def main():
    os.system('clear')

    # #####################################################################
    # Instantiate the logger
    # #####################################################################
    logger = Logger(filename=logFile, loggername=fileLogger,
                    tloggername=consoleLogger, libloggername=libLogger)

    # #####################################################################
    # Get the command line parameters
    # #####################################################################
    getCmdLineParam()
    logger.log.info("xmlFile: %s" % (xmlFile))
    logger.log.info("Appliance ip: %s" % (applianceIP))
    logger.log.info("backupFile: %s" % (backupFile))

    # #######################################################################
    # Instantiate the Xml object and verify that the version is correct
    # #######################################################################
    logger.log.info("Instantiating the Xml parser.")
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
    # Copy backup file (*.bpk) to appliance
    # #######################################################################
    logger.log.info("Calling uploadFileData")
    uploadFileData = UploadBackup(ip=appliance['ip'], sessionID=authToken, backupfile=backupFile)
    restoreURI = uploadFileData.uploadBackupFile(ip=appliance['ip'], sessionID=authToken, backupfile=backupFile)
    logger.log.info("restoreURI: %s " % (restoreURI))

    # #######################################################################
    # Send request to start the restore process.  Returns URI to access the task manager.
    # #######################################################################
    logger.log.info("Calling restoreAppliance to start restore process and to get task URI.")
    restoreInst = RestoreAppliance(ip=appliance['ip'], sessionID=authToken, restoreURI=restoreURI)
    restoreJsonData = restoreInst.restoreAppliance(ip=appliance['ip'], sessionID=authToken, restoreURI=restoreURI)
    # JRT print  "restore JSON Data = ", restoreJsonData
    restoreTaskURI = restoreJsonData['uri']
    # JRT print "Restore Task URI = ", restoreTaskURI

    # #######################################################################
    # Call method to check restore task status
    # #######################################################################
    # Call method to check task status
    logger.log.info("Calling restoreTaskState to check the task status.")
    checkTaskState(ip=appliance['ip'], sessionID=authToken, taskURI=restoreTaskURI)

    # JRT pdb.set_trace() #<-- set a break point in the code
    # JRT exit (1)


# Call Main

if __name__ == "__main__":
    main()
