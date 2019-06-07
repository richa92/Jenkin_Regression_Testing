#!/usr/local/bin/python
"""
Description: The script read the fping logs and parse all the continuous fping loss and print them.
             It supports parsing NDFU Case C Stages in ciDebug log and attach them to a particular fping loss.
             It supports mapping server to a bonding mode via a data variable file.

Author: Jason Mascarinas Pernito <jason.mas.pernito@hpe.com>

(c) Copyright 2017. Hewlett-Packard Enterprise
"""
import glob
import argparse
import re
import paramiko
import os
from datetime import datetime
from datetime import timedelta

SUMMARY_PACKETS = 10000
MIN_LOSS = 0
HA_FILE = ""
FPING_LOGS = ""
SORT_BY1 = "loss"
SORT_BY2 = "ipAddr"
SORT_BY3 = "startTime"
NDFU_CASE = None
OV_IP = None
BONDING_MODES = None
NDFU_HIGHEST_LOSS = None


def is_valid_file(parser, arg):
    """
    Test that data file specified in arg exists. Fail if not else load source.
    Arguments:
        parser: argparse.ArgumentParser() object
        arg: data file
    """
    if not arg:
        return arg
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        import imp
        variableFileData = imp.load_source('variableFileData', arg)
        return variableFileData


def parseArguments():
    """
    Parse command line arguments and set global variables for it.
    **Parameters**:
         -s <number of packets indicating a summary report>
         -m <minimum loss in ms to print>
         -c <your HA file>
         -l <path to your fping log>
         -a <sorting options: [loss|ipAddr|startTime|ndfuStage|bondingMode]. Defaul: loss>
         -a2 <sorting options: [loss|ipAddr|startTime|ndfuStage|bondingMode]. Default: ipAddr>
         -a3 <sorting options: [loss|ipAddr|startTime|ndfuStage|bondingMode]. Default: startTime>
         -r <NDFU Cases but only needed for Case C for now>
         -o <OneView IP to search for NDFU Case stages>
         -b <bonding modes variable file>
         -t <print only NDFU's highest fping loss per unique stage in ms>
    """
    global SUMMARY_PACKETS, MIN_LOSS, HA_FILE, FPING_LOGS, SORT_BY1, SORT_BY2, SORT_BY3, NDFU_CASE, OV_IP, BONDING_MODES, NDFU_HIGHEST_LOSS

    parser = argparse.ArgumentParser(description="The script read the fping logs and parse all the continuous fping loss and print them.")
    parser.add_argument("-s", "--summaryPackets", "--s", dest="SUMMARY_PACKETS", help="[Required] The maximum number of packets reported in summary. Default: 10000", default=SUMMARY_PACKETS, required=False)
    parser.add_argument("-m", "--minAcceptable", "--m", dest="MIN_LOSS", help="[Required] Mimimum loss in ms to print. Default: 0", default=MIN_LOSS, required=False)
    parser.add_argument("-c", "--haFile", "--c", dest="HA_FILE", help="[Required] HA file for your CI-FIT system. Default: /root/ci-fit/config_files/HA_ipaddr.conf", default=HA_FILE, required=False)
    parser.add_argument("-l", "--fpingLog", "--l", dest="FPING_LOGS", help="[Required] Path to you fping log. You can specify a wildcard here but it has to escaped (\). Example: /root/tools/logs/\*.log", default=FPING_LOGS, required=True)
    parser.add_argument("-a", "--sortBy", "--a", dest="SORT_BY1", help="[Optional] Sort the parsed data by loss or ip address (loss|ipAddr). Default: loss", default=SORT_BY1, required=False)
    parser.add_argument("-a2", "--sortBy2", "--a2", dest="SORT_BY2", help="[Optional] Primary sort name of the parsed fping loss data (loss|ipAddr|startTime|ndfuStage|bondingMode). Default: ipAddr", default=SORT_BY2, required=False)
    parser.add_argument("-a3", "--sortBy3", "--a3", dest="SORT_BY3", help="[Optional] Primary sort name of the parsed fping loss data (loss|ipAddr|startTime|ndfuStage|bondingMode). Default: startTime", default=SORT_BY3, required=False)
    parser.add_argument("-r", "--ndfuCase", "--r", dest="NDFU_CASE", help="[Optional] NDFU Cases but only needed for Case C for now.", default=NDFU_CASE, required=False)
    parser.add_argument("-o", "--ovIp", "--o", dest="OV_IP", help="[Optional] OneView IP to search for NDFU Case stages. This is required when -r option is specified.", default=OV_IP, required=False)
    parser.add_argument("-b", "--bondingModes", "--b", dest="BONDING_MODES", help="[Optional] Bonding modes variable file. Dictionary of bonding mode(key) to list of servers(value).", default=BONDING_MODES, required=False)
    parser.add_argument("-t", "--highestNdfuLoss", "--t", dest="NDFU_HIGHEST_LOSS", help="[Optional] Print only NDFU's highest fping loss per unique stage in ms.", default=NDFU_HIGHEST_LOSS, required=False, action="store_true")

    args = parser.parse_args()

    SUMMARY_PACKETS = args.SUMMARY_PACKETS
    MIN_LOSS = int(args.MIN_LOSS)
    HA_FILE = args.HA_FILE
    FPING_LOGS = args.FPING_LOGS
    SORT_BY1 = args.SORT_BY1
    SORT_BY2 = args.SORT_BY2
    SORT_BY3 = args.SORT_BY3
    NDFU_CASE = args.NDFU_CASE.lower() if args.NDFU_CASE else None
    OV_IP = args.OV_IP
    BONDING_MODES = is_valid_file(parser, args.BONDING_MODES)
    NDFU_HIGHEST_LOSS = args.NDFU_HIGHEST_LOSS


def getipAddrHAData(ip):
    """
    Parses server profile name and vlan id of a specific IP Address from HA File.
    Argument:
        ip: IP Address to search for in HA File
    """
    try:
        with open(HA_FILE, "r") as read_h:
            for ha_line in read_h:
                if re.search(r'\b' + re.escape(ip) + r'\b', ha_line) is None:
                    continue
                else:
                    # ip found, parse profile and vlan id
                    ha_line_split = ha_line.split()
                    return [ha_line_split[0], ha_line_split[6]]
    except IOError:
        print "WARNING: Failed to open %s! You will get ping loss HA File Data" % HA_FILE
        return ['Unable to retrieve data', 'Unable to retrieve data']


def get_ndfu_stages_time(host, stages, username='root', password='hpvse1'):
    """
    Parses NDFU Stages in OneView ciDebug log. Returns list of dictionary of stage:timestamp (key-value pair).
    Arguments:
        host: OneView IP Address (or FQDN)
        stages: List of NDFU Stages as logged in ciDebug
        username: OneView login name
        password: OneView login name password
    """
    if not stages:
        return []
    ovCaseStages = []
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        for stage in stages:
            stdin, stdout, stderr = ssh.exec_command('grep \'' + stage + '\' /ci/logs/ciDebug.*')
            output = stdout.read()
            if output == "":
                raise AssertionError("Failed to find \"%s\" from ciDebug log of %s! STDIN: %s, STDOUT: %s, STDERR: %s" % (stage, host, stdin, stdout, stderr))
            # in case of multiple stages in the log found
            log = output.split('\n')
            i = 0
            for L in log:
                if L == "":
                    continue
                # strip the filename
                strpFile = re.sub('^/ci/logs/ciDebug.log(\.\d+)?:', '', L)
                plog = strpFile.split(',')
                pstageNumber = re.search('Stage(.):Start:', plog[-1].strip())
                if len(ovCaseStages) < i + 1:
                    ovCaseStages.append({})
                ovCaseStages[i][pstageNumber.group(1)] = plog[0]
                i += 1
    except Exception as e:
        msg = "Exception occured while attempting to send ssh command to %s" % host
        raise Exception(msg, e)
    finally:
        ssh.close()
    return ovCaseStages[::-1]


if __name__ == "__main__":
    parseArguments()

    sortingOptions = {'loss': 6, 'ipAddr': 0, 'startTime': 4, 'ndfuStage': 8, 'bondingMode': 9}
    ndfuStages = {'c': ['Stage1:Start: CASE-C Firmware Update', 'Stage2:Start: CASE-C Firmware Update', 'Stage3:Start: CASE-C Firmware Update'], None: []}
    qualLoss = MIN_LOSS + 1
    files = glob.glob(FPING_LOGS)
    if not files:
        raise AssertionError("Failed to find fping log from %s!" % FPING_LOGS)
    losses = {}
    # iterate over the list getting each file to build a list of IP with loss
    for filename in files:
        with open(filename, "r") as f:
            for line in f:
                m = re.match(".* (\d+)/(\d+)/\d+%.*", line)
                if m:
                    if m.group(1) == m.group(2) or m.group(1) == SUMMARY_PACKETS:
                        continue
                    # split the loss/return log entry
                    lossLine = line.split()
                    if lossLine[2] in losses:
                        # known IP with pre-existing loss
                        # get the open loss timestamp
                        openLoss = losses[lossLine[2]].get('last')
                        if openLoss is None:
                            # get the current length of IP's dictionary
                            length = len(losses[lossLine[2]].items())
                            # create new open entry in loss dictionary
                            loss = re.match("(\d+)/(\d+)/\d+%.*", lossLine[6])
                            loss = (1000 / int(loss.group(1))) * (int(loss.group(1)) - int(loss.group(2)))
                            losses[lossLine[2]]['last'] = {'start': lossLine[0] + ' ' + lossLine[1], 'end': lossLine[0] + ' ' + lossLine[1], 'loss': loss}
                        else:
                            startLoss = datetime.strptime(losses[lossLine[2]]['last']['end'], "%Y-%m-%d %H:%M:%S:%f")
                            # check to see if it is continuous loss
                            endLoss = datetime.strptime(lossLine[0] + ' ' + lossLine[1], "%Y-%m-%d %H:%M:%S:%f")
                            diffLoss = endLoss - startLoss
                            loss = re.match("(\d+)/(\d+)/\d+%.*", lossLine[6])
                            loss = (1000 / int(loss.group(1))) * (int(loss.group(1)) - int(loss.group(2)))
                            if diffLoss.seconds > 1:
                                # get the current length of IP's dictionary
                                length = len(losses[lossLine[2]].items())
                                # close previous opening
                                losses[lossLine[2]][length] = losses[lossLine[2]].pop('last')
                                # create new open entry in loss dictionary
                                losses[lossLine[2]]['last'] = {'start': lossLine[0] + ' ' + lossLine[1], 'end': lossLine[0] + ' ' + lossLine[1], 'loss': loss}
                            else:
                                # create temporary end loss
                                netLoss = losses[lossLine[2]]['last']['loss'] + loss
                                if netLoss > 0:
                                    losses[lossLine[2]]['last']['loss'] = netLoss
                                    losses[lossLine[2]]['last']['end'] = lossLine[0] + ' ' + lossLine[1]
                                else:
                                    del losses[lossLine[2]]['last']
                    elif re.match(r'.*%loss', lossLine[4]):
                        # add IP to losses dictionary unless the first one is a return
                        # we ignore return being first as it come from previous fping run
                        loss = re.match("(\d+)/(\d+)/\d+%.*", lossLine[6])
                        loss = (1000 / int(loss.group(1))) * (int(loss.group(1)) - int(loss.group(2)))
                        losses[lossLine[2]] = {'last': {'start': lossLine[0] + ' ' + lossLine[1], 'end': lossLine[0] + ' ' + lossLine[1], 'loss': loss}}

    # iterate over the list of IP with fping loss and convert into CSV
    lossList = []
    for k, v in losses.iteritems():
        for count, data in v.iteritems():
            if data['loss'] < MIN_LOSS:
                continue
            ha = getipAddrHAData(k)
            if ha is None:
                lossList.append([k, 'Unable to retrieve data', 'Unable to retrieve data', count, data['start'], data['end'], data['loss']])
            else:
                lossList.append([k, ha[0], ha[1], count, data['start'], data['end'], data['loss']])
    if NDFU_CASE:
        # sort loss list by startTime for ease of stage mapping
        sortedLossList = sorted(lossList, key=lambda row: row[sortingOptions['startTime']])
        # initialize new list for final printing
        newLossList = []
    else:
        sortedLossList = sorted(lossList, key=lambda row: (row[sortingOptions[SORT_BY1]], row[sortingOptions[SORT_BY2]], row[sortingOptions[SORT_BY3]]))
    # parse ndfu stages from ciDebug log into list of dict
    parsedStages = get_ndfu_stages_time(OV_IP, ndfuStages[NDFU_CASE])
    for loss in sortedLossList:
        currLossTime = datetime.strptime(loss[4], "%Y-%m-%d %H:%M:%S:%f")
        stageFound = 0
        stageCounter = 0
        for pStage in parsedStages:
            # iterate over list of dictionary
            stageCounter += 1
            nextTime = 0
            for k in sorted(pStage.keys()):
                # iterate over dictionary keys
                # keys are ndfu case stages
                strpStageTime = datetime.strptime(pStage[k], "%Y-%m-%d %H:%M:%S.%f %Z")
                stageLossTimeDiff = currLossTime - strpStageTime
                diffTotalSec = stageLossTimeDiff.total_seconds()
                if k == '1':
                    tolerance = 30
                    strpStageTimeNext = datetime.strptime(pStage[str(int(k) + 1)], "%Y-%m-%d %H:%M:%S.%f %Z")
                    if currLossTime < strpStageTimeNext:
                        nextTime = 1
                elif k == '2':
                    tolerance = 0
                    # forward tolerance should match with stage 3 tolerance
                    fwdTolerance = 120
                    strpStageTimeNext = datetime.strptime(pStage[str(int(k) + 1)], "%Y-%m-%d %H:%M:%S.%f %Z")
                    if currLossTime < (strpStageTimeNext - timedelta(0, fwdTolerance)):
                        nextTime = 1
                elif k == '3':
                    # giving tolerance of 120s for stage3
                    tolerance = 120
                    # forward tolerance should match with stage 1 tolerance
                    fwdTolerance = 30
                    if len(parsedStages) > stageCounter:
                        # get the next set of stages if any
                        nextStages = sorted(parsedStages[stageCounter].keys())
                        strpStageTimeNext = datetime.strptime(parsedStages[stageCounter]['1'], "%Y-%m-%d %H:%M:%S.%f %Z")
                        if currLossTime < (strpStageTimeNext - timedelta(0, fwdTolerance)):
                            nextTime = 1
                    else:
                        nextTime = 1
                else:
                    raise AssertionError("Invalid stage number \"%s\" from ciDebug log of %s!" % (k, OV_IP))
                if diffTotalSec >= -tolerance and nextTime:
                    loss.append('Stage' + k)
                    loss.append(pStage[k])
                    stageFound = 1
                    break
            if stageFound:
                break
        if not stageFound:
            loss.append('N/A')
            loss.append('N/A')
        if BONDING_MODES:
            for b, profile in BONDING_MODES.bondingModes.iteritems():
                if loss[1] in profile:
                    loss.append(b)
        if NDFU_CASE:
            # append data to newLossList for final printing
            newLossList.append(loss)
        else:
            print loss
    if NDFU_CASE:
        # do final sort for printing ndfu case due to added column/list data we now support
        sortedNewLossList = sorted(newLossList, key=lambda row: (row[sortingOptions[SORT_BY1]], row[sortingOptions[SORT_BY2]], row[sortingOptions[SORT_BY3]]))
        if NDFU_HIGHEST_LOSS:
            # only print NDFU's highest loss per unique stage
            prevH = ['', '', '', '', '', '', 0, '', '', '']
            highs = []
            for h in sortedNewLossList:
                if h[8] == 'N/A':
                    print h
                    continue
                if h[8] == prevH[8]:
                    if h[9] != prevH[9]:
                        highs.append(prevH)
                elif prevH[0] != "":
                    highs.append(prevH)
                prevH = h
            highs.append(prevH)
            print '\n'.join(str(l) for l in highs)
        else:
            print '\n'.join(str(l) for l in sortedNewLossList)
