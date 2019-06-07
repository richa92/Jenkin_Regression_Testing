import json
import paramiko
import time
import re
import os
import threading
import Queue
import Queue
import time
from robot.libraries.BuiltIn import BuiltIn

IGNORE_ATTR = (['rfc1213IfInDiscards', 'rfc1213IfInNUcastPkts', 'rfc1213IfInOctets', 'rfc1213IfInUcastPkts',
                'rfc1213IfOutDiscards', 'rfc1213IfOutOctets', 'rfc1493Dot1DPortInDiscards', 'rfc1493Dot1DTpPortInFrames',
                'rfc1493Dot1DTpPortOutFrames', 'rfc2233IfHCInBroadcastPkts', 'rfc2233IfHCInMulticastPkts',
                'rfc2233IfHCInOctets', 'rfc2233IfHCInUcastPkts', 'rfc2233IfHCOutMulticastPkts', 'rfc2233IfHCOutOctets',
                'rfc2665Dot3StatsSQETTestErrors', 'rfc1493Dot1DBasePortDelayExceededDiscards', 'rfc1213IpInHdrErrors',
                'rfc2665Dot3OutPauseFrames', 'rfc2665Dot3StatsFCSErrors', 'rfc2233IfHCOutBroadcastPckts',
                'stormControlBCASTDropCounters', 'rfc1213IfInUnknownProtos', 'rfc2665Dot3StatsExcessiveCollisions',
                'rfc2665Dot3StatsAlignmentErrors', 'rfc1213IpInDiscards', 'rfc2665Dot3StatsInternalMacReceiveErrors',
                'rfc1757StatsRXNoErrors', 'rfc2665Dot3StatsDeferredTransmissions', 'rfc2665Dot3StatsInternalMacTransmitErrors',
                'rfc2665Dot3StatsCarrierSenseErrors', 'rfc1213IfInErrors', 'rfc2665Dot3ControlInUnknownOpcodes',
                'rfc1213IfOutUcastPkts', 'rfc2665Dot3StatsLateCollisions', 'rfc1493Dot1DBasePortMtuExceededDiscards',
                'rfc1213IpForwDatagrams', 'rfc1213IfOutQLen', 'rfc1213IfOutErrors', 'rfc1213IfOutNUcastPkts',
                'rfc2665Dot3StatsSymbolErrors', 'rfc1757StatsTXNoErrors', 'rfc2665Dot3StatsMultipleCollisionFrames',
                'rfc2665Dot3InPauseFrames', 'stormControlMCASTDropCounters', 'stormControlDLFDropCounters', 'rfc1213IpInReceives',
                'rfc2233IfHCOutUcastPkts', 'rfc2665Dot3StatsSingleCollisionFrames', 'rfc2665Dot3StatsFrameTooLongs', 'portNumber', 'resetTimeEpoch', 'type', 'linkChanges', 'subportNumber', 'resetTime'])


def fetch_statistics(ic_uri, ic_port, counter_keys=None, counters_to_validate=None, stats_flag=None, subport_no=None, stat=None):
    try:
        flag = True
        counter_values = []
        counters_value_dic = {}
        statistics = {}
        exp_stat = {}
        value, output = get_interconnect_statistics(ic_uri, ic_port)
        if value:
            if stats_flag == 'fc_stats':
                statistics = output['fcStatistics']['extendedStatistics']
            if stats_flag == 'uplink_lag':
                if stat == 'common':
                    statistics = output['lagStatistics']['commonStatistics']
                elif stat == 'advanced':
                    statistics = output['lagStatistics']['advancedStatistics']
                if statistics:
                    for k, v in statistics.iteritems():
                        if k not in IGNORE_ATTR:
                            exp_stat[k] = v
                        else:
                            continue
                else:
                    return False, "Step Failed"
                return exp_stat, ("Successfully retrieved the port statistics of the port %s") % (ic_port)
            if stats_flag == 'uplink':
                if stat == 'common':
                    statistics = output['commonStatistics']
                elif stat == 'advanced':
                    statistics = output['advancedStatistics']
                if statistics:
                    for k, v in statistics.iteritems():
                        if k not in IGNORE_ATTR:
                            exp_stat[k] = v
                        else:
                            continue
                else:
                    return False, "Step Failed"
                return exp_stat, ("Successfully retrieved the port statistics of the port %s") % (ic_port)
            if stats_flag == 's_channel':
                sub_port_len = len(output['subportStatistics'])
                if stat == 'common':
                    for x in range(0, sub_port_len):
                        if int(output['subportStatistics'][x]['subportNumber']) == int(subport_no):
                            statistics = output['subportStatistics'][x]['subportCommonStatistics']
                elif stat == 'advanced':
                    for x in range(0, sub_port_len):
                        if int(output['subportStatistics'][x]['subportNumber']) == int(subport_no):
                            statistics = output['subportStatistics'][x]['subportAdvancedStatistics']
                if statistics:
                    for k, v in statistics.iteritems():
                        if k not in IGNORE_ATTR:
                            exp_stat[k] = v
                        else:
                            continue
                else:
                    return False, "Step Failed"
                return exp_stat, ("Successfully retrieved the port statistics of the port %s") % (ic_port)
            if stats_flag == 's_channel_lag':
                sub_port_len = len(output['subportStatistics'])
                if stat == 'common':
                    for x in range(0, sub_port_len):
                        if int(output['subportStatistics'][x]['subportNumber']) == int(subport_no):
                            statistics = output['subportStatistics'][x]['subportLagStatistics']['subportCommonStatistics']
                elif stat == 'advanced':
                    for x in range(0, sub_port_len):
                        if int(output['subportStatistics'][x]['subportNumber']) == int(subport_no):
                            statistics = output['subportStatistics'][x]['subportLagStatistics']['subportAdvancedStatistics']
                        else:
                            continue
                if statistics:
                    for k, v in statistics.iteritems():
                        if k not in IGNORE_ATTR:
                            exp_stat[k] = v
                        else:
                            continue
                else:
                    return False, "Step Failed"
                return exp_stat, ("Successfully retrieved the port statistics of the port %s") % (ic_port)
        else:
            return False, "Failed to fetch stats %s" % output
    except Exception as e:
        return False, "unable to fetch statistics counter values. failed with exception"


def get_interconnect_statistics(ic_uri, ic_port):
    try:
        uri = ic_uri + '/statistics/' + ic_port
        fz = BuiltIn().get_library_instance('FusionLibrary')
        output = fz.fusion_api_get_interconnect(uri)
        if output:
            print 'out is %s' % output
            return True, output
        else:
            return False, 'statistics is not available'
    except Exception as e:
        print 'e is %s' % e
        return False, 'Failed with exception %s' % e


def Kill_traffic(server_details, kill_cmd):
    win_server = []
    linux_server = []
    esxi_server = []
    print server_details
    for server in server_details:
        print server
        if server['OS'] == 'windows':
            win_server.append(server)
        if server['OS'] == 'linux':
            linux_server.append(server)
        if server['OS'] == 'esxi':
            esxi_server.append(server)
    if len(win_server) != 0:
        threads_win = [
            threading.Thread(target=execute_windows_commands, args=(i['ip'], i['username'], i['password'], kill_cmd))
            for i in server_details
        ]
        for thread in threads_win:
            thread.start()
            thread.join()
    if len(linux_server) != 0:
        threads_linux = [
            threading.Thread(target=execute_linux_commands, args=(i['ip'], i['username'], i['password'], i['kill_cmd']))
            for i in server_details
        ]
        for thread in threads_linux:
            thread.start()
            thread.join()
    if len(esxi_server) != 0:
        threads_esxi = [
            threading.Thread(target=execute_linux_commands, args=(i['ip'], i['username'], i['password'], i['kill_cmd']))
            for i in server_details
        ]
        for thread in threads_esxi:
            thread.start()
            thread.join()


def execute_windows_commands(ip, username, passwd, cmd):
    '''
    Execute any windows commands
    '''
    try:
        build_cmd = "paexec \\\\" + ip + " -u " + username + " -p " + passwd + " " + cmd
        print build_cmd
        output = os.system(build_cmd)
        print output
        return output
    except Exception as e:
        return e


def aggregate_stat(stat1_dict, stat2_dict, stat):
    try:
        if stat == 'common':
            exp_aggregate_stat = {}
            for k, v in stat1_dict.iteritems():
                if v is None and stat2_dict[k] is None:
                    exp_aggregate_stat[k] = None
                elif v is None:
                    exp_aggregate_stat[k] = stat2_dict[k]
                elif stat2_dict[k] is None:
                    exp_aggregate_stat[k] = v
                else:
                    exp_aggregate_stat[k] = v + stat2_dict[k]
            return exp_aggregate_stat, "Success"
        if stat == 'advanced':
            exp_aggregate_stat = {}
            for k, v in stat1_dict.iteritems():
                adv_1 = str(v).split(':')
                adv_2 = stat2_dict[k].split(':')
                agg = []
                for i in range(len(adv_1)):
                    if (adv_1[i] == "NA" and adv_2[i] == "NA"):
                        Flag = False
                        break
                    else:
                        sum = int(adv_1[i]) + int(adv_2[i])
                        agg.append(str(sum))
                        Flag = True
                if not Flag:
                    exp_aggregate_stat[k] = v
                else:
                    exp_aggregate_stat[k] = ':'.join([one_val for one_val in agg])
            return exp_aggregate_stat, "Success"
    except Exception as e:
        return e


def validate_aggregate_stat(stat1_dict, stat2_dict, stat):
    try:
        flag = True
        if stat == 'common':
            for k, v in stat1_dict.iteritems():
                if v == stat2_dict[k]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                return True, "Validation of Aggregate Common Statistics is successful"
            else:
                return False, "Failed to validate aggregate common statistics"
        if stat == 'advanced':
            for k, v in stat1_dict.iteritems():
                adv_1 = str(v).split(':')
                adv_2 = stat2_dict[k].split(':')
                for i in range(len(adv_1)):
                    if(adv_1[i] == "NA" and adv_2[i] == "NA"):
                        flag = True
                    elif (adv_1[i].isdigit() and adv_2[i].isdigit()):
                        buffer = int(adv_1[i]) + (int(adv_1[i]) * (0.10))
                        if(int(adv_1[i]) == int(adv_2[i]) or (int(adv_1[i]) < int(adv_2[i]) and int(adv_2[i]) < buffer)):
                            flag = True
                    else:
                        flag = False
                        return flag, "Failed to validate aggregate advanced statistics"
            return flag, "Validation of Aggregate Advanced Statistics is successful"
    except Exception as e:
        return e


def validate_decrease_statistics(initial_output, final_output, stat):
    try:
        flag = True
        if initial_output:
            if final_output:
                if stat == 'common':
                    for k, v in final_output.iteritems():
                        if final_output[k] is None or int(final_output[k]) == int(initial_output[k]):
                            print "The counter value is constant for the key %s" % (k)
                            continue
                        else:
                            buffer = (int(initial_output[k])) * (0.10)
                            if int(initial_output[k]) - buffer <= int(v) <= int(initial_output[k]) + buffer:
                                print "The counter value for the key %s is decreasing" % (k)
                            else:
                                print "The counter value for the key %s is not decreasing" % (k)
                                flag = False
                if stat == 'advanced':
                    for k, v in initial_output.iteritems():
                        if final_output[k] is None:
                            print "Statistics not available to calculate"
                            continue
                        else:
                            adv_1 = str(v).split(':')
                            adv_2 = final_output[k].split(':')
                            for i in range(len(adv_1)):
                                if((adv_1[i] == "NA" and adv_2[i] == "NA") or (adv_1[i] == "0" and adv_2[i] == "0") or (adv_1[i] == adv_2[i])):
                                    flag = True
                                    continue
                                else:
                                    buffer = int(adv_1[i]) * (0.10)
                                    if int(adv_1[i]) - buffer <= int(adv_2[i]) <= int(adv_1[i]) + buffer:
                                        flag = True
                                    else:
                                        flag = False
                if flag:
                    return True, "Successfully verified the decrease in counter value"
                else:
                    return False, "Failed to verify the decrease in counter value"
    except Exception as e:
        return e


def execute_command_in_tcs(cmd):
    try:
        output = os.system(cmd)
        print output
        return output
    except Exception as e:
        return e
