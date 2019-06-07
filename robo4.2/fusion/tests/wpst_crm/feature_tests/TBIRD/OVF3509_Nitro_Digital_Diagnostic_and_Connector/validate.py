'''
This python module contains local keywords for validating the outputs
'''
from data_variables import *
import json
import re


def validate_connector_information(connector, output, sfp=True, lower_api=False):

    flag = True
    out = None
    output = json.loads(output)
    print sfp
    try:
        for i in output:
            if i['portName'] == connector['portName']:
                out = i
                print out
                print out.keys()
        if sfp == 'False':
            print "Validating if connector info is not available when transceiver is not connected"
            for j in out.keys():
                if j == "vendorName" or j == "vendorPartNumber" or j == "vendorRevision" or j == "serialNumber":
                    print j
                    print out[j]
                    if out[j] != '':
                        print ("connector value %s is not as expected %s" % (j, out[j]))
                        flag = False
                        break
                    else:
                        print ("successfully verified that connector info is not available for %s" % j)
        else:
            print "Validating if connector info is available when transceiver is connected"
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
                        print ("out is %s" % out[j])
                        print ("connector is %s" % connector[j])
                        print ("connector information %s is not matching the expected value. Actual value is %s expected value is %s " % (j, out[j], connector[j]))
                        flag = False
                        print flag
                        break
                    else:
                        print ("value of %s is verified successfully as %s" % (j, out[j]))
                        print flag
        if flag:
            return True, "Connector informations are verified successfully"
        else:
            return (False, "Connector values are not matching with expected output")
    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"


def validate_values_of_DDMI_statitics(lane_info, key, DDMI_values):

    if DDMI_values[key] == 'numeric':
        print "value of %s is %s" % (key, lane_info[key])
        pat = re.compile(r"[+-]?\d+(?:\.\d+)")
        out = pat.match(lane_info[key])
        if out is None:
            print "value of %s is not numeric" % key
            return False, "value of %s is not numeric" % key
        else:
            print "Successfully verified value of %s is numeric" % key
            return True, "Successfully verified value of %s is numeric" % key
    elif DDMI_values[key] == 'unsupported' or DDMI_values[key] == 'invalid':
        print "value of %s is %s" % (key, lane_info[key])
        if lane_info[key] == DDMI_values[key]:
            print "Successfully verified value of %s is %s" % (key, lane_info[key])
            return True, "Successfully verified value of %s is %s" % (key, lane_info[key])
        else:
            print "value of %s is not unsupported or invalid as expected" % key
            return False, "value of %s is not unsupported or invalid as expected" % key


def validate_digital_diagnostic_information(connector, output, DDMI_values, lower_api=False):
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
                    return False, "Digital diagnostics values are not found"
                else:
                    print "validate digital diagnostic information"
                    for k in out[j].keys():
                        if k in connector[j].keys():
                            print ("Successfully verified that %s key is present in digital diag" % k)
                            flag = True
                            if k == 'laneInformation':
                                print "validating digital diag info for supported transceiver"
                                lane_info = out[j][k]
                                given_lane_info = connector[j]['laneInformation']
                                for x in range(0, len(out[j][k])):
                                    for m in lane_info[x].keys():
                                        if m in given_lane_info[x].keys():
                                            print "Successfully verfied that all the keys are present in DDMI statistics are available"
                                            if m == 'laneId':
                                                continue
                                            else:
                                                print ("validating the value of %s" % m)
                                                value, msg = validate_values_of_DDMI_statitics(lane_info[x], m, DDMI_values)
                                                if value:
                                                    flag = True
                                                else:
                                                    return False, msg
                                        else:
                                            return False, ("Key %s is not present in lane info" % m)
                        else:
                            return False, ("%s key is not present in digital diag" % k)
                    if flag:
                        return True, "Digital diagnostic info keys and its values are validated successfully"
                    else:
                        return False, "Digital Diagnostic not available"
    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"


def validate_precision_values(output, uplink_ports, DDMI_values, lower_api=False):

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
                            for lane in lane_info:
                                for key in lane:
                                    if key == 'laneId':
                                        continue
                                    elif DDMI_values[key] == 'numeric':
                                        value = _validate_precision(lane[key])
                                        if value:
                                            print ("%s value is precision with 4 decimal points" % key)
                                            flag = True
                if flag:
                    return True, "Successfully validated the values are precision with 4 decimal points"
                else:
                    return False, "the values are not precision with 4 decimal points"
    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"


def validate_digital_diagnostic_info_range(output, uplink_ports, DDMI_values, lower_api=False):

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
                            if -40 < int(temperature) < 125:
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
                            for lane in lane_info:
                                for lane_key in lane:
                                    if lane_key == 'laneId':
                                        continue
                                    elif DDMI_values[lane_key] == 'numeric':
                                        if lane_key == 'txPowerdBm' or lane_key == 'rxPowerdBm' or lane_key == 'rxPowermW' or lane_key == 'txPowermW':
                                            print lane[lane_key]
                                            txPowerdBm = lane[lane_key]
                                            if float(-40) < float(txPowerdBm) < float(8.2):
                                                print ("%s is in correct range" % lane_key)
                                            else:
                                                return False, "%s Not in correct range" % lane_key
                                        if lane_key == 'current':
                                            print lane[lane_key]
                                            current = lane[lane_key]
                                            if 0 < float(current) < float(131):
                                                print "current is in correct range"
                                            else:
                                                return False, "current Not in correct range"
                    if flag:
                        return True, "Ranges validated successfully"
                    else:
                        return False, "Lane info values are not in correct range"
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


def validate_QSFP_lane_information(connector, output, expected_length, DDMI_values, lower_api=False):

    output1 = json.loads(output)
    flag = True
    out = None
    try:
        for i in output1:
            if i['portName'] == connector['portName']:
                print connector['portName']
                out = i
        for j in out.keys():
            if j == 'digitalDiagnostics':
                if None in out[j].values():
                    return False, "Digital diagnostics values are not found if no transceiver is connected"
                for key in out[j]:
                    if key == "laneInformation":
                        print "data is %s" % out[j][key]
                        actual_length = len(out[j][key])
                        print type(expected_length)
                        print type(actual_length)
                        if actual_length != int(expected_length):
                            return False, "DDMI stastics is not displaying %s lane information as expected" % expected_length
                        else:
                            print ("Successfully validated %s lane information as expected") % expected_length
                            value = validate_digital_diagnostic_information(connector, output, DDMI_values)
                            if value:
                                flag = True
                                print "Successfully validated the DDMI statistics"
                            else:
                                print "DDMI statistics values are not displayed as expected"
        if flag:
            return True, "Successfully validated lane count and DDMI statistics for"
        else:
            return False, "lane information count and DDMI statistics are not matching as expected"

    except AttributeError as e:
        return False, "No Content available for Connector and digital diagnostics"
