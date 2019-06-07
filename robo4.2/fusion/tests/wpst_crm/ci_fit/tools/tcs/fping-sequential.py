#!/usr/local/bin/python
# This script runs the fping command in a loop until 'CTRL+C' is hit.
# * It checks if fping is installed.
# * Logs the ping results to the screen and a log file.
# * Allows the user to generate an IP file used by fping from the HA_ipaddr file.
# * Allows the user to change in the fping options.
#     NOTE: Passing in different values may break the script.  You should only change the numeric values.
# * If you are generate the ip file using an HA file you will need to only have entries for the IPs you
#   wish to ping in the HA file.
# USAGE/SYNTAX: ./fping-sequential.py <OPTIONS>
# optional arguments:
#  -h, --help            show this help message and exit
#  -a HAFILE, --HA HAFILE, --a HAFILE
#                        The name of the HA file you want fping to read ip
#                        addresses from. Example: -h HA_ipaddr.conf
#  -c PINGCMD, --command PINGCMD, --c PINGCMD
#                        Name of the ping command to use. Example: -c 'fping'
#  -f IPSFILE, --ipfile IPSFILE, --f IPSFILE
#                        File with list of IPs to ping
#  -g, --genIPFile, --g  Tells script to generate the IP file from an HA file.
#  -o PINGOPTIONS, --options PINGOPTIONS, --o PINGOPTIONS
#                        fping runtime options. Example: -Q 1 -c 1000 -p 50 -u
#                        -r 0 -f
#  -r RUNLOG, --runLog RUNLOG, --r RUNLOG
#                        The name of the log file for the run results.
#  -x, --clearLog, --x   Tells script to clear the ping log
#
# Author:    John Thigpen
# Contact:   john.r.thigpen@hpe.com
# Version:   0.1-06052017
###############################

# ---> Libraries
import argparse
import subprocess
import datetime
import logging
import time
import sys
import re


# ---> Variables
pingcmd = 'fping'
pingOptions = '-Q 1 -c 10 -p 200 -i 1 -T 100 -u -r 0 -f'
# pingOptions = '-Q 1 -c 1000 -p 200 -i 1 -T 100 -u -r 0 -f'
haFile = 'HA_ipaddr.conf'
ipsFile = 'ips2ping.txt'
runLog = 'ping.log'
genIPFile = False
clearLog = False
spIPsDict = {}

logger = logging.getLogger()

# ---> Functions


def initLogs(runLog):
    """
    :py:func:`initLogs` initializes run log file and console handler

    **Parameters**:
          runLog <Name of the run log file. Default: ping.log>

    """
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # Log File handler:
    logFile = logging.FileHandler(runLog)
    logFile.setLevel(logging.DEBUG)
    logFile.setFormatter(formatter)
    logger.addHandler(logFile)
    # Log Console Handler:
    logConsole = logging.StreamHandler()
    logConsole.setLevel(logging.DEBUG)
    logConsole.setFormatter(formatter)
    logger.addHandler(logConsole)


def getCmdLineParam():
    """
    :py:func:`getCmdLineParam` uses the argparse module to parse the command line parameters

    **Parameters**:
         -a <Name of the HA file used to generate IP file>
         -c <Ping Command To run>
         -f <The name of the ipfile to use for fping>
         -g <Tells script to generate the IP file from the HA file>
         -o <Ping Options>
         -r <Run Log Filename>
         -x <Clear run log>

    """
    global haFile, pingOptions, pingcmd, ipsFile, runLog, clearLog, genIPFile

    parser = argparse.ArgumentParser(description="fping-sequential.py is used to ping ips address from and HA file.")
    parser.add_argument("-a", "--HA", "--a", dest="haFile", help="The name of the HA file you want fping to read ip addresses from.  Example: -h HA_ipaddr.conf", default=haFile, required=False)
    parser.add_argument("-c", "--command", "--c", dest="pingcmd", help="Name of the ping command to use. Example: -c 'fping'", default=pingcmd, required=False)
    parser.add_argument("-f", "--ipfile", "--f", dest="ipsFile", help="File with list of IPs to ping", default=ipsFile, required=False)
    parser.add_argument("-g", "--genIPFile", "--g", help="Tells script to generate the IP file from an HA file.", action='store_true', required=False)
    parser.add_argument("-o", "--options", "--o", dest="pingOptions", help="fping runtime options. Example: -Q 1 -c 1000 -p 50 -u -r 0 -f", default=pingOptions, required=False)
    parser.add_argument("-r", "--runLog", "--r", dest="runLog", help="The name of the log file for the run results.", default=runLog, required=False)
    parser.add_argument("-x", "--clearLog", "--x", help="Tells script to clear the ping log", action='store_true', required=False)

    args = parser.parse_args()

    haFile = args.haFile
    pingOptions = args.pingOptions
    pingcmd = args.pingcmd
    ipsFile = args.ipsFile
    runLog = args.runLog
    clearLog = args.clearLog
    genIPFile = args.genIPFile


def checkIfInstalled(pingcmd):

    """
    :py:func:`checkIfInstalled` Verifies a program is installed on the linux server.

    **Parameters**
        checkIfInstalled <command to check for>
    """
    try:
        logger.info("Checking if %s is installed" % (pingcmd))
        isInstalled = subprocess.call("type " + pingcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0
        if not isInstalled:
            logger.error("%s is not installed on this system.  Please install %s and rerun script." % (pingcmd, pingcmd))
            sys.exit(3)
    except Exception as e:
        logger.error("Exception occured while checking for %s. Please verify it is installed." % (pingcmd))
        msg = "Exception occured while checking for %s. Please verify it is installed." % (pingcmd)
        raise Exception(msg, e)


# Get the number of pings from the fping options.  Used to determine ping result summaries:
def getCycles(pingOptions):
    """
    :py:func:`getCycles` parses the fping command options and extracts the ping count.

    **Parameters**
        pingOptions <list of fping options>
    """
    try:
        cycleStr = "r\'-d \d+\'"
        cyclesString = re.search(r'-c \d+', pingOptions)
        cyclesList = cyclesString.group(0).split()
        cycles = cyclesList[1]
        return cycles
    except Exception as e:
        logger.error("Exception occured while attempting to get cycles from the fping command line options")
        msg = "Exception occured while attempting to get cycles from the fping command line options"
        raise Exception(msg, e)


# Clear contents of the log file:
def clearLogFile(runLog):
    """
    :py:func:`clearLogFile` uses FileHandler to open, write and close the ping log file.

    **Parameters**
        runLog <Name of the ping log file to open and clear>
    """
    logger.info("Clearing %s" % (runLog))
    try:
        open(runLog, 'w').close()
    except Exception as e:
        logger.error("Exception occured while attempting to clear %s file." % (runLog))
        msg = "Exception occured while attempting to clear %s file." % (runLog)
        raise Exception(msg, e)


# Read in file and strip off the newline char
def readFileWithStrip(haFile):
    """
    :py:func:`readFileWithStrip` reads the HA file into a list and strips off newlines.

    **Parameters**
        haFile <Name of the HA file to open and read>
    """
    logger.info("Processing %s" % (haFile))
    try:
        with open(haFile) as file:
            lines = [line.rstrip('\n') for line in file]
        file.close()
        return lines
    except Exception as e:
        logger.error("Exception occured while attempting to read %s file." % (haFile))
        msg = "Exception occured while attempting to read %s file." % (haFile)
        raise Exception(msg, e)


# Create Dictionary of SP Names with list of IPs
def getIPs(lines):
    """
    :py:func:`getIPs` reads the lines list, gets the IP addess and writes it to the spIPsList.

    **Parameters**
        lines <List of entries from HA file without newlines>
    """
    spIPsList = []
    try:
        for line in lines:
            lineSplit = line.split()
            lineLen = len(lineSplit)
            if lineLen == 8:
                spIPsList.append(lineSplit[6])
            elif lineLen == 9:
                spIPsList.append(lineSplit[7])
            else:
                logger.error("Unable to parse %s.  Please check that your HA file is correct" % (haFile))
                break
    except Exception as e:
        logger.error("Exception occured while attempting to create Server Profile Dictionary")
        msg = "Exception occured while attempting to create Server Profile Dictionary"
        raise Exception(msg, e)
    finally:
        return spIPsList


def createIpFile(ipsToPing):
    """
    :py:func:`createIpFile` writes the spIPsList to a text file.

    **Parameters**
        ipsToPing <List of IPs that fping will ping>
    """
    try:
        file = open(ipsFile, "w")
        for ip in ipsToPing:
            file.write("%s" % ip),
            file.write("\n")
    except Exception as e:
        msg = "Exception occured while trying to create : %s" % (file)
        raise Exception(msg, e)
    finally:
        logger.info("Created ip file: %s" % (ipsFile))
        file.close()
        sys.exit(0)


def runFping(fpingOptions, ipsFile, pingCycles):
    """
    :py:func:`runFping` runs fping with options defined in variable section or by the user..

    **Parameters**
        fpingOptions <User supplied or default options used by fping>
        ipsFile <Name of the file that contains ips to be pinged by fping>
    """
    loopCount = 1
    pingPassFail = False
    fpingAllOptions = "%s %s" % (fpingOptions, ipsFile)
    logger.info("Using fping options: %s" % (fpingAllOptions))
    fpingcmd = "%s %s" % (pingcmd, fpingAllOptions)
    while True:
        try:
            logger.info("-----------------------------------------------------------")
            logging.info("----  Loop: %d ---- Started at: %s" % (loopCount, datetime.datetime.now()))
            logger.info("-----------------------------------------------------------")
            pingData = subprocess.Popen(fpingcmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            pingData.wait()
            pingResultRC = pingData.returncode
            pingResultsList = pingData.stdout.readlines()
            if pingResultRC == 0:
                for entry in pingResultsList:
                    entryList = entry.split()
                    if len(entryList) == 8:
                        entryIP = entryList[0]
                        entryTimesHeader = entryList[5]
                        entryTimes = entryList[7]
                        entryResultHeader = entryList[2]
                        entryResult = entryList[4]
                        entryResultSplit = entryResult.split("/")
                        pingLoss = entryResultSplit[2].rstrip(',')
                        pingLossInt = int(entryResultSplit[2].rstrip('%,'))
                        if entryResultSplit[0] == pingCycles:
                            if pingLossInt == 0:
                                logger.info("IP/Host: %s, RESULT: PASSED (%s = %s)" % (entryIP, entryResultHeader, entryResult))
                            else:
                                logger.debug("IP/Host: %s, RESULT: FAILED (%s = %s)" % (entryIP, entryResultHeader, entryResult))
            elif pingResultRC == 1:
                for entry in pingResultsList:
                    entryList = entry.split()
                    if len(entryList) == 8:
                        entryIP = entryList[0]
                        entryTimesHeader = entryList[5]
                        entryTimes = entryList[7]
                        entryResultHeader = entryList[2]
                        entryResult = entryList[4]
                        entryResultSplit = entryResult.split("/")
                        pingLoss = entryResultSplit[2].rstrip(',')
                        pingLossInt = int(entryResultSplit[2].rstrip('%,'))
                        if entryResultSplit[0] == pingCycles:
                            if pingLossInt == 0:
                                logger.info("IP/Host: %s, RESULT: PASSED (%s = %s)" % (entryIP, entryResultHeader, entryResult))
                            else:
                                logger.debug("IP/Host: %s, RESULT: FAILED (%s = %s)" % (entryIP, entryResultHeader, entryResult))
                    elif 'xmt/rcv/%loss' in entry:
                        entryIP = entryList[0]
                        entryResult = entryList[4]
                        entryResultHeader = entryList[2]
                        entryResultSplit = entryResult.split("/")
                        pingLoss = entryResultSplit[2]
                        pingLoss = pingLoss.rstrip(',')
                        pingPassFail = True
                        if entryResultSplit[0] == pingCycles:
                            logger.debug("IP/Host: %s, RESULT: FAILED (%s = %s)" % (entryIP, entryResultHeader, entryResult))
            elif pingResultRC == 4:
                logger.error("Invalid IP file: %s!  Please verify IP file and try again!" % (ipsFile))
                break
            loopCount += 1
            logger.info("-----------------------------------------------------------")

        except KeyboardInterrupt:
            logger.info("CTRL-C pressed. Loops completed: %d,  Exiting loop." % (loopCount - 1))
            if pingPassFail:
                logger.error("Ping Failures Detected.  Check log file: %s" % (runLog))
                sys.exit(3)
            else:
                logger.info("No ping failures detected.")
            break


def main():
    """
    This is the main function for fping-sequential.py

    1. Read the cmd line parameters.
    2. Initialize Run Log File.
    3. Verify fping is installed.
    4. Get fping cycle count.  Used to only print out ping summaries.
    5. Check if HA file is passed into the script via command line.
        a. If an HA if passed in Read in HA File.
        b. Create list of IPs.
        c. Write IP list to file.
    6. Run fping.
    """

    # #######################################################################
    # Get the command line parameters
    # #######################################################################
    getCmdLineParam()

    # #######################################################################
    # Initailize Log Files
    # #######################################################################
    initLogs(runLog)

    # #######################################################################
    # Verify fping is installed on the server
    # #######################################################################
    checkIfInstalled(pingcmd)

    # #######################################################################
    # Get the number of ping cycles from the fping options list
    # #######################################################################
    pingCycles = getCycles(pingOptions)

    if clearLog:
        # #######################################################################
        # Clear ping log
        # #######################################################################
        clearLogFile(runLog)

    if genIPFile:
        # #######################################################################
        # Read in HA file
        # #######################################################################
        myLines = readFileWithStrip(haFile)

        # #######################################################################
        # Create a list of sever profiles with a list of IP for each
        # #######################################################################
        ipsToPing = getIPs(myLines)

        # #######################################################################
        # Write ip list to file
        # #######################################################################
        createIpFile(ipsToPing)

    # #######################################################################
    # Run fping
    # #######################################################################
    runFping(pingOptions, ipsFile, pingCycles)


if __name__ == '__main__':
    main()
