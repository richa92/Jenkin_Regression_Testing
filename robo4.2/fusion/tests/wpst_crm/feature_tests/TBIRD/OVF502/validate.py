'''
This python module contains local keywords for validating the outputs
'''
from data_variables import *
import json
import re


def validate_connector_information(connector, output, lower_api=False):

    flag = True
    out = None
    output = json.loads(output)
    try:
        for i in output:
            if i['portName'] == connector['portName']:
                out = i
                print out
                print out.keys()
        for j in out.keys():
            if j == 'digitalDiagnostics':
                for k in out[j].keys():
                    if k not in connector[j].keys():
                        return False, "Digital diagnostics keys are not same"
                if None in out[j].values():
                    return False, "Digital diagnostics values are not available"
            elif j == "speed" or j == "extIdentifier":
                print "speed and identifier available"
                continue
            else:
                out[j] = out[j].strip()
                if out[j] != connector[j]:
                    flag = False
                    print flag
                    break
                else:
                    print flag
        if flag:
            return True, "Connector infomrations are verified successfully"
        else:
            return (False, "Connector values are not matching with expected output")
    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"


def validate_digital_diagnostic_information(connector, output, lower_api=False):

    output = json.loads(output)
    flag = True
    out = None
    try:
        for i in output:
            if i['portName'] == connector['portName']:
                out = i
                print out
                print out.keys()
        for j in out.keys():
            if j == 'digitalDiagnostics':
                if None in out[j].values():
                    return False, "Digital diagnostics values not found for unsupported transreceiver"
                else:
                    print "validate digital diagnostic informnation for supported transreceiver "
                    for k in out[j].keys():
                        if k in connector[j].keys():
                            print k
                            print "Digital diagnostics keys are  same"
                            flag = True

                            if k == 'laneInformation':
                                print k
                                lane_info = out[j]['laneInformation']
                                given_lane_info = connector[j]['laneInformation']
                                for m in lane_info[0].keys():
                                    if m in given_lane_info[0].keys():
                                        print m
                                        print "digital diagnostic laneInformation keys are same"
                                        flag = True
                                    else:
                                        return False, "digital diagnostic laneInformation not available"
                        else:
                            return False, "digital diagnostic Information not available"
                    if flag:
                        return True, "All digital diagnostic info are verified successfully"
                    else:
                        return False, "Digital Diagnostic not available"
    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"


def validate_precision_values(output, lower_api=False):

    output = json.loads(output)
    flag = True
    out = None
    try:
        for i in output:
            if i['portName'] == uplink_ports:
                out = i
                print out
                print out.keys()
        for j in out.keys():
            if j == 'digitalDiagnostics':
                print j
                if None in out[j].values():
                    return False, "Digital diagnostics values are not available"
                else:
                    for k in out[j].keys():
                        if k == 'laneInformation':
                            lane_info = out[j]['laneInformation']
                            lane_keys = lane_info[0].keys()
                            lane_values = lane_info[0].values()
                            for k in lane_keys:
                                if k == 'txPowerdBm' or k == 'txPowermW':
                                    print lane_info[0][k]
                                    value = _validate_precision(lane_info[0][k])
                                    if value:
                                        print "txPower are correctly with 4 precision values"
                                    else:
                                        return False, "Not in correct precision order"
                                if k == 'rxPowerdBm' or k == 'rxPowermW':
                                    print lane_info[0][k]
                                    value = _validate_precision(lane_info[0][k])
                                    if value:
                                        print "rxPower are correctly with 4 precision values"
                                    else:
                                        return False, "Not in correct precision order"
                            return True, "Precision value validated successfully"
    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"


def validate_digital_diagnostic_info_range(output, lower_api=False):

    output = json.loads(output)
    flag = True
    out = None
    try:
        for i in output:
            if i['portName'] == uplink_ports:
                out = i
                print out
                print out.keys()
        for j in out.keys():
            if j == 'digitalDiagnostics':
                print j
                if None in out[j].values():
                    return False, "Digital diagnostics values are not available"
                else:
                    for k in out[j].keys():
                        if k == 'temperature':
                            temperature = out[j][k]
                            print temperature
                            if -128 < int(temperature) < 128:
                                print "Temperature is in correct range"
                            else:
                                return False, "Temperature Not in correct range"
                        if k == 'voltage':
                            voltage = out[j][k]
                            print voltage
                            if 0 < float(voltage) < float(6550):
                                print "Voltage is in correct range"
                            else:
                                return False, "Voltage Not in correct range"
                        if k == 'laneInformation':
                            print k
                            lane_info = out[j]['laneInformation']
                            lane_keys = lane_info[0].keys()
                            lane_values = lane_info[0].values()
                            for k in lane_keys:
                                if k == 'txPowerdBm':
                                    print lane_info[0][k]
                                    txPowerdBm = lane_info[0][k]
                                    if float(-40) < float(txPowerdBm) < float(8.2):
                                        print "TxPowerdBm is in correct range"
                                    else:
                                        return False, "TxPowerdBm Not in correct range"
                                if k == 'rxPowerdBm':
                                    print lane_info[0][k]
                                    rxPowerdBm = lane_info[0][k]
                                    if float(-40) < float(rxPowerdBm) < float(8.2):
                                        print "RxPowerdBm is in correct range"
                                    else:
                                        return False, "RxPowerdBm Not in correct range"
                                if k == 'current':
                                    print lane_info[0][k]
                                    current = lane_info[0][k]
                                    if 0 < float(current) < float(131):
                                        print "current is in correct range"
                                    else:
                                        return False, "current Not in correct range"
                    return True, "Ranges validated successfully"
    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"


def _validate_precision(value):

    print value
    power_value_list = value.split(".")
    print power_value_list
    print len(power_value_list[1])
    if len(power_value_list[1]) == 4:
        return True
    else:
        return False