"""
This  module supports SPT new feature implemented in Frankfurt (4.10) release : OVF1053 and OVF3651.
The modules in this file is used  as support function in resource and test case file.
In order to support new feature SPT automated regression test in rg, certain variables need to be
assigned in resource.txt or SPT test case file accordingly

For setting scope for prereq resources used in testing OVF1053 and  OVF3651

Only OVF1053        | @{consistency_check_scope}=    Checked    Unchecked    CheckedMinimumChecked    CheckedMinimumUnchecked
-------------------------------------------------------------------------------------------------------------------------------------
OVF1053 and OVF3651 | @{EG_optional_scope}=    single EG    shared EGs    single EG 2
   or               | @{consistency_check_scope}=    Checked    Unchecked    CheckedMinimumChecked    CheckedMinimumUnchecked
OVF 3651 only       |


Before running SPT regression test suite, please follow instruction to set variables as mentioned below:

isDataVariableFile  |   condition
----------------------------------------------------------------------------------
    True            |   * SPT regression test without any new feature
                    |   * can run in OV 4.0 and 4.10 (Edinburgh or Frankfurt but no feature enabled)
                    |   * when using data variable file : SPT_SBAC_data_variable.py
-----------------------------------------------------------------------------------
    False           |   * SPT regression test with new feature: OVF1053/OVF3651 or both
                    |   * can run in OV 4.10 (Frankfurt)
                    |   * when using data variable file : SPT_SBAC_data_variable_template.py

If using combination of 0VF1053 and OVF3651

OVF1053   | OVF3651              | variables value
------------------------------------------------------------------------------------------------------------------------
No        |single EG/ shared    | OVF1053: NoCheck
          |                     |  OVF3651: single EG or shared EG
-------------------------------------------------------------------------------------------------------------------------
Yes       |single EG/ shared    | OVF1053: Checked or Unchecked or CheckedMinimumChecked or CheckedMinimumUnchecked
          |                     |  OVF3651: single EG or shared EG
-------------------------------------------------------------------------------------------------------------------------
yes       |No                   | OVF1053: Checked or Unchecked or CheckedMinimumChecked or CheckedMinimumUnchecked
          |                     |
--------------------------------------------------------------------------------------------------------------------------
"""
from copy import deepcopy
import re
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.libraries.BuiltIn import BuiltIn
CHECK_FIELD = 'complianceControl'
CHECK_VALUE = 'Checked'
UNCHECK_VALUE = 'Unchecked'
MIN_CHECK_VALUE = 'CheckedMinimum'
feature3651_num = {'NoOVF3651': '',
                   'single EG': '1',
                   'shared EGs': '',
                   'single EG 2': '2'}

# ===============================================================================
# OVF 3651 feature support
# ===============================================================================


def make_EG_option_scope_data(argv):
    """
    Generate required scope payload for OVF3651
    """
    scopes = argv[0]
    out = []
    eg_optional_scope_list = argv[2]
    for scope in scopes:
        if "addedResourceUris" in scope:
            addresource = []
            for i in range(len(scope["addedResourceUris"])):
                if re.match("^((ETH)|(FC)|(NS)).*", scope["addedResourceUris"][i]):
                    for i1 in eg_optional_scope_list:
                        if feature3651_num[i1] == "":
                            addresource.append(scope["addedResourceUris"][i])
                        else:
                            addresource.append(scope["addedResourceUris"][i] + "_" + feature3651_num[i1])
                else:
                    addresource.append(scope["addedResourceUris"][i])
            scope["addedResourceUris"] = addresource
        if "removedResourceUris" in scope:
            remove_Resource = []
            for i in range(len(scope["removedResourceUris"])):
                if re.match("^((ETH)|(FC)|(NS)).*", scope["addedResourceUris"][i]):
                    for i1 in eg_optional_scope_list:
                        if feature3651_num[i1] == "":
                            remove_Resource.append(scope["addedResourceUris"][i])
                        else:
                            remove_Resource.append(scope["addedResourceUris"][i] + "_" + feature3651_num[i1])
                else:
                    remove_Resource.append(scope["removedResourceUris"])
            scope["removedResourceUris"] = remove_Resource
        out.append(scope)
    logger._log_to_console_and_log_file("modified scope payload for OVF3651 : {0}".format(out))
    return out


def make_EG_optional_payload(data_payload, feature, SERVER_PROFILE_TEMPLATE_TYPE='ServerProfileTemplateV*'):
    """
    Modify the EG section in SPT payload based on OVF3651 feature
    """

    if 'NoChange' in feature.keys() and feature['NoChange'] == 'True':
        return data_payload
    elif 'NoChange' in feature.keys() and feature['NoChange'] == 'False':
        if 'OVF3651' in feature.keys():
            if feature['OVF3651'] == 'NoOVF3651':
                return data_payload
            for opn in data_payload.keys():
                if isinstance(data_payload[opn]['payload'], list):
                    for pd_num in range(len(data_payload[opn]['payload'])):
                        if 'type' in data_payload[opn]['payload'][pd_num] and re.match(SERVER_PROFILE_TEMPLATE_TYPE, data_payload[opn]['payload'][pd_num]['type']):
                            if 'enclosureGroupUri' in data_payload[opn]['payload'][pd_num]:
                                del data_payload[opn]['payload'][pd_num]['enclosureGroupUri']
                                logger._log_to_console_and_log_file("modified payload EG")
                        if 'connectionSettings' in data_payload[opn]['payload'][pd_num].keys():
                            if 'connections' in data_payload[opn]['payload'][pd_num]['connectionSettings']:
                                conn = data_payload[opn]['payload'][pd_num]['connectionSettings']['connections']
                                for net_num in range(len(conn)):
                                    if feature3651_num[feature['OVF3651']] != "":
                                        conn[net_num]["networkUri"] = conn[net_num]["networkUri"] + "_" + feature3651_num[feature['OVF3651']]
                        if 'type' in data_payload[opn]['payload'][pd_num] and re.match("network-setV*", data_payload[opn]['payload'][pd_num]['type']):
                            if feature3651_num[feature['OVF3651']] != "":
                                if 'name' in data_payload[opn]['payload'][pd_num]:
                                    data_payload[opn]['payload'][pd_num]["name"] = data_payload[opn]['payload'][pd_num]["name"] + "_" + feature3651_num[feature['OVF3651']]
                                if "add_networkUris" in data_payload[opn]['payload'][pd_num]:
                                    addnet = [i + "_" + feature3651_num[feature['OVF3651']] for i in data_payload[opn]['payload'][pd_num]["add_networkUris"]]
                                    data_payload[opn]['payload'][pd_num]["add_networkUris"] = addnet
                                if "delete_networkUris" in data_payload[opn]['payload'][pd_num]:
                                    delnet = [i + "_" + feature3651_num[feature['OVF3651']] for i in data_payload[opn]['payload'][pd_num]["delete_networkUris"]]
                                    data_payload[opn]['payload'][pd_num]["delete_networkUris"] = delnet
            logger._log_to_console_and_log_file("modified payload {0}".format(data_payload))
            return data_payload
        else:
            return data_payload
    elif 'NoChange' not in feature.keys():
        if 'OVF3651' in feature.keys():
            if feature['OVF3651'] == 'NoOVF3651':
                return data_payload
            for opn in data_payload.keys():
                if isinstance(data_payload[opn]['payload'], list):
                    for pd_num in range(len(data_payload[opn]['payload'])):
                        if 'type' in data_payload[opn]['payload'][pd_num] and re.match(SERVER_PROFILE_TEMPLATE_TYPE, data_payload[opn]['payload'][pd_num]['type']):
                            if 'enclosureGroupUri' in data_payload[opn]['payload'][pd_num]:
                                del data_payload[opn]['payload'][pd_num]['enclosureGroupUri']
                                # logger._log_to_console_and_log_file("modified payload EG: ")
                        if 'connectionSettings' in data_payload[opn]['payload'][pd_num]:
                            if 'connections' in data_payload[opn]['payload'][pd_num]['connectionSettings']:
                                conn = data_payload[opn]['payload'][pd_num]['connectionSettings']['connections']
                                for net_num in range(len(conn)):
                                    if feature3651_num[feature['OVF3651']] != "":
                                        conn[net_num]["networkUri"] = conn[net_num]["networkUri"] + "_" + feature3651_num[feature['OVF3651']]
                        if 'type' in data_payload[opn]['payload'][pd_num] and re.match("network-setV*", data_payload[opn]['payload'][pd_num]['type']):
                            if feature3651_num[feature['OVF3651']] != "":
                                if 'name' in data_payload[opn]['payload'][pd_num]:
                                    data_payload[opn]['payload'][pd_num]["name"] = data_payload[opn]['payload'][pd_num]["name"] + "_" + feature3651_num[feature['OVF3651']]
                                if "add_networkUris" in data_payload[opn]['payload'][pd_num]:
                                    addnet = [i + "_" + feature3651_num[feature['OVF3651']] for i in data_payload[opn]['payload'][pd_num]["add_networkUris"]]
                                    data_payload[opn]['payload'][pd_num]["add_networkUris"] = addnet
                                if "delete_networkUris" in data_payload[opn]['payload'][pd_num]:
                                    delnet = [i + "_" + feature3651_num[feature['OVF3651']] for i in data_payload[opn]['payload'][pd_num]["delete_networkUris"]]
                                    data_payload[opn]['payload'][pd_num]["delete_networkUris"] = delnet
            logger._log_to_console_and_log_file("modified payload {0}".format(data_payload))
            return data_payload
        else:
            return data_payload


def enable_OVF3651(fun):
    """
    layer to enable OVF3651 based SPT payload modification
    """
    def dynamic_data(self, *argv, **kwargs):
        """
        Generate payload for OVF1053
        """
        opns, data_payload = fun(self, *argv, **kwargs)
        data_payload = make_EG_optional_payload(data_payload, kwargs)
        return opns, data_payload
    return dynamic_data


def scope_for_OVF3651_resources(funct):
    """
    layer to enable OVF3651 based scope payload modification
    """
    def dynamic_data(self, *argv, **kwargs):
        """
        Generate payload for OVF1053
        """
        data_payload = funct(self, *argv, **kwargs)
        data_payload = make_EG_option_scope_data(argv)
        return data_payload
    return dynamic_data


class new_feature_support(object):
    """
    This class is the interface to SPT robogalaxy resource file
    """
    def __init__(self, data_variable=[]):
        self.fusionlib = BuiltIn().get_library_instance('FusionLibrary')
        self.data_variable = data_variable
        self.test_data = []
        self.check_field = ['connectionSettings', 'localStorage', 'sanStorage', 'bootMode', 'bios', 'firmware', 'boot']
        self.uncheck_field = ['connectionSettings', 'localStorage', 'sanStorage', 'bootMode', 'bios', 'firmware', 'boot']
        self.checkMinimum_field = ['connectionSettings', 'localStorage', 'sanStorage']
        self.field = ['connectionSettings', 'localStorage', 'sanStorage', 'boot', 'bootMode', 'bios', 'firmware']
        self.spt_from_sp_manage_check_field = ['bootMode', 'bios', 'firmware', 'boot']
        self.spt_from_sp_manage_checkMinimum_field = ['sanStorage', 'localStorage', 'connectionSettings']

    def combination(self, tc_data, fields):
        """
        custom made payload  with combination of check, uncheck and check minimum
        """
        tc_data = self.add_check_uncheck(tc_data, UNCHECK_VALUE)
        custom_data = []
        for tc1 in tc_data:
            for field in fields:
                tc = deepcopy(tc1)

                for key in field:
                    if key == 'checked':
                        for f in field[key]:
                            if f in tc:
                                if tc[f] is not None:
                                    tc[f][CHECK_FIELD] = CHECK_VALUE
                    elif key == 'unchecked':
                        for f in field[key]:
                            if f in tc:
                                if tc[f] is not None:
                                    tc[f][CHECK_FIELD] = UNCHECK_VALUE
                    elif key == 'minChecked':
                        for f in field[key]:
                            if f in tc:
                                if tc[f] is not None:
                                    tc[f][CHECK_FIELD] = MIN_CHECK_VALUE
                custom_data.append(tc)
        return custom_data

    def add_check_uncheck(self, tc_data, checkCondition):
        """
        Generate  payload for Check\ uncheck  payload for SPT
        """
        data = []
        if checkCondition == 'Checked':
            checkC = CHECK_VALUE
            checkFeilds = self.check_field
            num = "_1"
        elif checkCondition == 'Unchecked':
            checkC = UNCHECK_VALUE
            checkFeilds = self.uncheck_field
            num = "_2"

        if checkCondition == checkC:
            for tc in tc_data:
                tc1 = deepcopy(tc)
                if 'name' in tc1:
                    if tc1['name'] is not None:
                        tc1['name'] = tc1['name'] + num
                if 'new_name' in tc1:
                    if tc1['new_name'] is not None:
                        tc1['new_name'] = tc1['new_name'] + num
                if 'SP' in tc1:
                    tc1['SP'] = self.generate_test_data(tc1['SP'], checkCondition)
                if 'type' in tc1:
                    if tc1['type'] == self.SERVER_PROFILE_TEMPLATE_TYPE:
                        for field in checkFeilds:
                            if field in tc1:
                                if tc1[field] is not None:
                                    tc1[field][CHECK_FIELD] = checkC
                    else:
                        if 'serverProfileTemplateUri' in tc1:
                            tc1['serverProfileTemplateUri'] = tc1['serverProfileTemplateUri'] + num
                data.append(tc1)
        return data

    def checkedMinimum(self, tc_data, checkCondition):
        """
        Generate payload for SPT minimumcheck
        """
        if checkCondition == 'CheckedMinimumChecked':
            min1 = self.add_check_uncheck(tc_data, CHECK_VALUE)
            num = "_3"
        elif checkCondition == 'CheckedMinimumUnchecked':
            min1 = self.add_check_uncheck(tc_data, UNCHECK_VALUE)
            num = "_4"
        checkC = MIN_CHECK_VALUE
        checkFeilds = self.checkMinimum_field
        minm = []
        for tc in min1:
            tc1 = deepcopy(tc)
            if 'name' in tc1:
                if tc['name'] is not None:
                    tc1['name'] = tc1['name'][:-2] + num
            if 'new_name' in tc1:
                if tc1['new_name'] is not None:
                    tc1['new_name'] = tc1['new_name'][:-2] + num
            if 'SP' in tc1:
                sps = self.generate_test_data(tc1['SP'], checkCondition)
                for sp in sps:
                    if 'name' in sp:
                        sp['name'] = sp['name'][:-4] + num
                tc1['SP'] = sps
            if 'type' in tc1:
                if tc1['type'] == self.SERVER_PROFILE_TEMPLATE_TYPE:
                    for field in checkFeilds:
                        if field in tc1:
                            if tc1[field] is not None:
                                tc1[field][CHECK_FIELD] = checkC
                    if 'SP' in tc1:
                        tc1['SP'] = self.generate_test_data(tc1['SP'], checkCondition)
                else:
                    if 'serverProfileTemplateUri' in tc1:
                        tc1['serverProfileTemplateUri'] = tc1['serverProfileTemplateUri'][:-2] + num
            minm.append(tc1)
        return minm

    @scope_for_OVF3651_resources
    def generate_scope_data(self, scopes, checkConsistency_list, EG_optional_scope, CONSISTENCY_CHECK_HW):
        """
        Generate scope payload based on OVF3651
        """
        out = []
        if not EG_optional_scope:
            logger._log_to_console_and_log_file("EG optional scope not available")
        self.hardware = CONSISTENCY_CHECK_HW
        for scope in scopes:
            if "addedResourceUris" in scope:
                addresource = []
                for i in range(len(scope["addedResourceUris"])):
                    if re.match("^SH", scope["addedResourceUris"][i]):
                        dat = scope["addedResourceUris"][i].split(":")
                        for checkConsistency in checkConsistency_list:
                            if dat[1] == 'SH1':
                                addresource.append(dat[0] + ":" + self.hardware[checkConsistency]['SH'][0])
                            if dat[1] == 'SH2':
                                addresource.append(dat[0] + ":" + self.hardware[checkConsistency]['SH'][1])
                            if dat[1] == 'SH3':
                                addresource.append(dat[0] + ":" + self.hardware[checkConsistency]['SH'][2])
                    else:
                        addresource.append(scope["addedResourceUris"][i])
                scope["addedResourceUris"] = addresource
            if "removedResourceUris" in scope:
                remove_Resource = []
                for i in range(len(scope["removedResourceUris"])):
                    if re.match("^SH", scope["removedResourceUris"][i]):
                        dat = scope["removedResourceUris"][i].split(":")
                        for checkConsistency in checkConsistency_list:
                            if dat[1] == 'SH1':
                                remove_Resource.append(dat[0] + ":" + self.hardware[checkConsistency]['SH'][0])
                            if dat[1] == 'SH2':
                                remove_Resource.append(dat[0] + ":" + self.hardware[checkConsistency]['SH'][1])
                            if dat[1] == 'SH3':
                                remove_Resource.append(dat[0] + ":" + self.hardware[checkConsistency]['SH'][2])
                    else:
                        remove_Resource.append(scope["removedResourceUris"])
                scope["removedResourceUris"] = remove_Resource
            out.append(scope)
        return out

    def resourcesinScopeOVF1053(self, payload, checkConsistency):
        """
        scope payload change based on OVF1053
        """
        if checkConsistency == 'Checked':
            num = "_1"
        elif checkConsistency == 'Unchecked':
            num = "_2"
        elif checkConsistency == 'CheckedMinimumChecked':
            num = "_3"
        elif checkConsistency == 'CheckedMinimumUnchecked':
            num = "_4"
        elif checkConsistency == 'NoCheck':
            return payload
        if checkConsistency != 'NoCheck':
            if "removedResourceUris" in payload:
                for rv in range(len(payload["removedResourceUris"])):
                    if re.match("^(SP|SPT)\:*", payload["removedResourceUris"][rv]):
                        payload["removedResourceUris"][rv] = payload["removedResourceUris"][rv] + num
            if "addedResourceUris" in payload:
                for ad in range(len(payload["addedResourceUris"])):
                    if re.match("^(SP|SPT)\:*", payload["addedResourceUris"][ad]):
                        payload["addedResourceUris"][ad] = payload["addedResourceUris"][ad] + num
        return payload

    def generate_test_data(self, tc_data, checkConsistency):
        """
        Modify SPT payload based on OVF1053
        """
        if isinstance(tc_data, dict):
            if checkConsistency == 'Checked':
                num = "_1"
            elif checkConsistency == 'Unchecked':
                num = "_2"
            elif checkConsistency == 'CheckedMinimumChecked':
                num = "_3"
            elif checkConsistency == 'CheckedMinimumUnchecked':
                num = "_4"
            elif checkConsistency == 'NoCheck':
                num = ""
            if 'name' in tc_data:
                if 'type' in tc_data and re.match("ScopeV*", tc_data["type"]):
                    return self.resourcesinScopeOVF1053(tc_data, checkConsistency)
                else:
                    if not re.match("lig*", tc_data["name"]):
                        tc_data['name'] = tc_data['name'] + num
                    return tc_data
            else:
                return tc_data
        else:
            isScopePayload = [True if 'type' in pld and re.match("ScopeV*", pld["type"]) else False for pld in tc_data]
            if False not in isScopePayload:
                tc = []
                for scopePayload in tc_data:
                    tc.append(self.resourcesinScopeOVF1053(scopePayload, checkConsistency))
                return tc
            isNSPayload = [True if 'type' in pld and re.match("network-setV*", pld["type"]) else False for pld in tc_data]
            if False not in isNSPayload:
                return tc_data
            payload = self.assign_SHT_SH(tc_data, checkConsistency)
            if isinstance(payload, str):
                return payload
            if checkConsistency == 'Checked' or checkConsistency == 'Unchecked':
                payload = self.add_check_uncheck(payload, checkConsistency)
            elif checkConsistency == 'CheckedMinimumChecked' or checkConsistency == 'CheckedMinimumUnchecked':
                payload = self.checkedMinimum(payload, checkConsistency)
            return payload

    def assign_SHT_SH(self, tc_data, checkConsistency):
        """
        Based on consistency check chosen assign required hardware and its type
        """
        payload = []
        if isinstance(tc_data, str):
            if re.match("^SH", tc_data):
                dat = tc_data
                if dat == 'SH1':
                    tc_data = self.hardware[checkConsistency]['SH'][0]
                elif dat == 'SH2':
                    tc_data = self.hardware[checkConsistency]['SH'][1]
                elif dat == 'SH3':
                    tc_data = self.hardware[checkConsistency]['SH'][2]
            return tc_data
        else:
            for tc in tc_data:
                if 'type' in tc:
                    if tc['type'] == self.SERVER_PROFILE_TEMPLATE_TYPE:
                        if 'serverHardwareTypeUri' in tc:
                            dat = tc['serverHardwareTypeUri'].split(":")
                            if dat[1] == 'SHT1':
                                tc['serverHardwareTypeUri'] = dat[0] + ":" + self.hardware[checkConsistency]['SHT'][0]
                            elif dat[1] == 'SHT2':
                                tc['serverHardwareTypeUri'] = dat[0] + ":" + self.hardware[checkConsistency]['SHT'][1]
                    elif tc['type'] == self.SERVER_PROFILE_TYPE:
                        if 'serverHardwareTypeUri' in tc:
                            dat = tc['serverHardwareTypeUri'].split(":")
                            if dat[1] == 'SHT1':
                                tc['serverHardwareTypeUri'] = dat[0] + ":" + self.hardware[checkConsistency]['SHT'][0]
                            elif dat[1] == 'SHT2':
                                tc['serverHardwareTypeUri'] = dat[0] + ":" + self.hardware[checkConsistency]['SHT'][1]
                        if 'serverHardwareUri' in tc:
                            dat = tc['serverHardwareUri']
                            if dat == 'SH1':
                                tc['serverHardwareUri'] = self.hardware[checkConsistency]['SH'][0]
                            elif dat == 'SH2':
                                tc['serverHardwareUri'] = self.hardware[checkConsistency]['SH'][1]
                            elif dat == 'SH3':
                                tc['serverHardwareUri'] = self.hardware[checkConsistency]['SH'][2]
                payload.append(tc)
            return payload

    def validate_spt_created_from_sp(self, payload):
        """
        validate the Check consistency check in each section in payload generated after SPT is created from SP.
        following condition is checked in each section in SPT
            1. if unmanage : then consistency Check : Unchecked
            2. if managed : consistency check of sanstorage, local storage and connection : Checked Minimum
                    rest of the  section will be  Checked
        return True/False
        """
        parameter = '?filter=name=\'%s\''
        error_msg = "Validation Failed: {0} Consistency Check is not matching with expected value: {1}"
        for SPT in payload:
            spt_param = parameter % SPT['name']
            get_spt = self.fusionlib.fusion_api_get_server_profile_templates(uri=None, api=None, headers=None, param=spt_param)
            if 'members' in get_spt:
                if get_spt['members']:
                    for get_spt1 in get_spt['members']:
                        for key in self.field:
                            if key in get_spt1.keys():
                                section = get_spt1[key]
                                if section:
                                    for sec_key in section.keys():
                                        s = re.search("(manage).*", sec_key)
                                        if s:
                                            if not section[s.group(0)]:
                                                if section[CHECK_FIELD] != UNCHECK_VALUE:
                                                    logger._log_to_console_and_log_file(section)
                                                    logger._warn(error_msg.format(key, UNCHECK_VALUE))
                                                    return False
                                            else:
                                                if key in self.spt_from_sp_manage_check_field:
                                                    if section[CHECK_FIELD] != CHECK_VALUE:
                                                        logger._log_to_console_and_log_file(section)
                                                        logger._warn(error_msg.format(key, CHECK_VALUE))
                                                        return False
                                                elif key in self.spt_from_sp_manage_checkMinimum_field:
                                                    if section[CHECK_FIELD] != MIN_CHECK_VALUE:
                                                        logger._log_to_console_and_log_file(section)
                                                        logger._warn(error_msg.format(key, MIN_CHECK_VALUE))
                                                        return False
        logger._log_to_console_and_log_file("Consistency Check Validation Successful : SPT created from SP")
        return True

    def __validate_connectionSettings(self, spt, sp):
        """
        Validate SPT and SP Connection settings based on consistency check
        """
        sp_index = {}
        flagcc = 0
        for i in range(len(sp['connections'])):
            net_uri = sp['connections'][i]['networkUri']
            if net_uri not in sp_index.keys():
                sp_index[net_uri] = [i]
            else:
                sp_index[net_uri].append(i)
        if not spt['manageConnections']:
            return True
        else:
            if 'connections' in spt and 'connections' in sp:
                if len(spt['connections']) != len(sp['connections']):
                    if spt[CHECK_FIELD] == CHECK_VALUE:
                        logger._log_to_console_and_log_file("Validation: Number of connection in SPT doesn't match with SP")
                        flagcc = 1
                    elif spt[CHECK_FIELD] == MIN_CHECK_VALUE:
                        if len(spt['connections']) > len(sp['connections']):
                            logger._log_to_console_and_log_file("Validation: Number of connection in SPT doesn't match with SP")
                            flagcc = 1
                else:
                    for spt_conn in spt['connections']:
                        net_uri = spt_conn['networkUri']
                        if net_uri in sp_index.keys():
                            sp_conn = sp['connections']
                            flag = 0
                            for i in range(len(sp_index[net_uri])):
                                conn = sp_conn[sp_index[net_uri][i]]
                                if spt_conn['requestedMbps'] == conn['requestedMbps'] and spt_conn['portId'] == conn['portId']:
                                    if spt_conn['boot']['priority'] == conn['boot']['priority']:
                                        del sp_index[net_uri][i]
                                        flag = 1
                                        break
                            if flag == 0:
                                if spt[CHECK_FIELD] == CHECK_VALUE or spt[CHECK_FIELD] == MIN_CHECK_VALUE:
                                    net = self.fusionlib.fusion_api_get_connections(uri=spt_conn['networkUri'])
                                    logger._log_to_console_and_log_file("Validation: Network connection properties of :{0} is not matching with SP".format(net))
                                    flagcc = 1
                        else:
                            if spt[CHECK_FIELD] == CHECK_VALUE or spt[CHECK_FIELD] == MIN_CHECK_VALUE:
                                net = self.fusionlib.fusion_api_get_connections(uri=spt_conn['networkUri'])
                                logger._log_to_console_and_log_file("Validation: Network Connection :{0} in SPT is not in SP".format(net['name']))
                                flagcc = 1
            sp_dict = {net: sp_index[net] for net in sp_index.keys() if sp_index[net]}
            if len(sp_dict) == 0:
                return True
            else:
                if spt[CHECK_FIELD] == CHECK_VALUE:
                    sp_nets = [self.fusionlib.fusion_api_get_connections(uri=a)['name'] for a in sp_dict.keys()]
                    spt_nets = [self.fusionlib.fusion_api_get_connections(uri=a['networkUri'])['name'] for a in spt['connections']]
                    logger._log_to_console_and_log_file("Validation: List of Network connection mismatch found between SP{0} and SPT{1}".format(sp_nets, spt_nets))
                    flagcc = 1
        if flagcc == 1:
            logger._log_to_console_and_log_file("**** SPT connection settings {0} ".format(spt))
            logger._log_to_console_and_log_file("**** SP connection settings {0} ".format(sp))
            return False
        else:
            return True

    def __validate_sanStorage(self, spt, sp):
        """
        Validate SP and SPT san Storage based on Consistency Check
        """
        parameter = '?filter=name=\'%s\''
        flagcc = 0
        if not spt['manageSanStorage']:
            return True
        else:
            if 'volumeAttachments' in spt and 'volumeAttachments' in sp:
                if len(spt['volumeAttachments']) > len(sp['volumeAttachments']):
                    logger._log_to_console_and_log_file("Extra volume(s) in SPT than SP")
                    flagcc = 1
                elif len(spt['volumeAttachments']) <= len(sp['volumeAttachments']):
                    if len(spt['volumeAttachments']) == 0 and len(sp['volumeAttachments']) == 0:
                        return True
                    spt_vol_lst = spt['volumeAttachments']
                    sp_vol_lst = sp['volumeAttachments']
                    for spt_vol in spt_vol_lst:
                        flag = 0
                        for sp_vol in sp_vol_lst:
                            if spt_vol['volumeUri'] is not None:
                                if spt_vol['volumeUri'] == sp_vol['volumeUri']:
                                    if spt_vol["associatedTemplateAttachmentId"] != sp_vol["associatedTemplateAttachmentId"]:
                                        logger._log_to_console_and_log_file("Validation: spt shared vol attachmentId not matching with sp")
                                        flagcc = 1
                                    if spt_vol["lun"] is not None and spt_vol["lun"] != sp_vol["lun"]:
                                        logger._log_to_console_and_log_file("Validation: spt shared vol lun not matching with sp")
                                        flagcc = 1
                                    if spt_vol["lunType"] != sp_vol["lunType"]:
                                        logger._log_to_console_and_log_file("Validation: spt shared vol lunType not matching with sp")
                                        flagcc = 1
                                    if "isBootVolume" in spt_vol and "isBootVolume" in sp_vol:
                                        if spt_vol["isBootVolume"] != sp_vol["isBootVolume"]:
                                            logger._log_to_console_and_log_file("Validation: spt shared vol isbootvolume {0} not matching with sp{1}".format(spt_vol["isBootVolume"], sp_vol["isBootVolume"]))
                                            flagcc = 1
                                    if spt_vol["volumeStorageSystemUri"] != sp_vol["volumeStorageSystemUri"]:
                                        logger._log_to_console_and_log_file("Validation: spt shared vol storage system {0} not matching with sp{1}".format(spt_vol["volumeStorageSystemUri"], sp_vol["volumeStorageSystemUri"]))
                                        flagcc = 1
                                    spt_str_path = spt_vol["storagePaths"]
                                    sp_str_path = sp_vol["storagePaths"]
                                    for spt_str_p in spt_str_path:
                                        for sp_str_p in sp_str_path:
                                            if spt_str_p["connectionId"] == sp_str_p["connectionId"]:
                                                if spt_str_p["isEnabled"] != sp_str_p["isEnabled"]:
                                                    logger._log_to_console_and_log_file("Validation: volume: isEnable is not matching with spt{0} sp{1}".format(spt_vol, sp_vol))
                                                    flagcc = 1
                                                if spt_str_p["targetSelector"] != sp_str_p["targetSelector"]:
                                                    logger._log_to_console_and_log_file("Validation: spt's volume : target selector is not matching with sp")
                                                    flagcc = 1
                                    break
                            else:
                                if 'volume' in spt_vol and 'name' in spt_vol['volume']:
                                    param_vol = parameter % spt_vol['volume']['name']
                                    get_vol = self.fusionlib.fusion_api_get_storage_volumes(param=param_vol)
                                    if 'count' in get_vol:
                                        if get_vol['count'] >= 1:
                                            if 'members' in get_vol:
                                                for i in get_vol['members']:
                                                    vol_uri = i['uri']
                                                    if vol_uri == sp_vol['volumeUri']:
                                                        logger._log_to_console_and_log_file("****Matched priv volume {0}".format(spt_vol['volume']['name']))
                                                        if spt_vol["associatedTemplateAttachmentId"] != sp_vol["associatedTemplateAttachmentId"]:
                                                            logger._log_to_console_and_log_file("Validation: spt priv vol attachmentId not matching with sp")
                                                            flagcc = 1
                                                        if spt_vol["lun"] is not None and spt_vol["lun"] != sp_vol["lun"]:
                                                            logger._log_to_console_and_log_file("Validation: spt priv vol lun {0} not matching with sp{1}".format(spt_vol["lun"], sp_vol["lun"]))
                                                            flagcc = 1
                                                        if spt_vol["lunType"] != sp_vol["lunType"]:
                                                            logger._log_to_console_and_log_file("Validation: spt priv vol lunType {0} not matching with sp{1}".format(spt_vol["lunType"], sp_vol["lunType"]))
                                                            flagcc = 1
                                                        if spt_vol["isBootVolume"] != sp_vol["isBootVolume"]:
                                                            logger._log_to_console_and_log_file("Validation: spt priv vol isbootvolume {0} not matching with sp{1}".format(spt_vol["isBootVolume"], sp_vol["isBootVolume"]))
                                                            flagcc = 1
                                                        if spt_vol["volumeStorageSystemUri"] != sp_vol["volumeStorageSystemUri"]:
                                                            logger._log_to_console_and_log_file("Validation: spt priv vol storage system {0} not matching with sp{1}".format(spt_vol["volumeStorageSystemUri"], sp_vol["volumeStorageSystemUri"]))
                                                            flagcc = 1
                                                        spt_str_path = spt_vol["storagePaths"]
                                                        sp_str_path = sp_vol["storagePaths"]
                                                        for spt_str_p in spt_str_path:
                                                            for sp_str_p in sp_str_path:
                                                                if spt_str_p["connectionId"] == sp_str_p["connectionId"]:
                                                                    if spt_str_p["isEnabled"] != sp_str_p["isEnabled"]:
                                                                        logger._log_to_console_and_log_file("Validation: isEnabled not matching for {0}".format(spt_vol))
                                                                        flagcc = 1
                                                                    if spt_str_p["targetSelector"] != sp_str_p["targetSelector"]:
                                                                        logger._log_to_console_and_log_file("Validation: targetSelector not matching {0}".format(spt_vol))
                                                                        flagcc = 1
                                                        flag = 1
                                                        break
                                    if flag == 1:
                                        break
                        if flagcc == 1:
                            logger._log_to_console_and_log_file("**** SPT san storage {0} ".format(spt))
                            logger._log_to_console_and_log_file("**** SP sanstorage {0} ".format(sp))
                            return False
                        else:
                            return True

    def __validate_firmware(self, spt, sp):
        """
        Validate SP and SPT firmware based on Consistency Check
        """
        flagcc = 0
        if 'manageFirmware' in spt and 'manageFirmware' in sp:
            if spt['manageFirmware'] == sp['manageFirmware']:
                if not spt['manageFirmware']:
                    return True
                else:
                    for field in spt.keys():
                        if field == 'manageFirmware' or field == 'complianceControl':
                            continue
                        else:
                            if field in sp.keys():
                                if spt[field] != sp[field]:
                                    if spt[CHECK_FIELD] == CHECK_VALUE:
                                        logger._log_to_console_and_log_file("Validation: spt firmware {0} is not matching with sp".format(field))
                                        flagcc = 1
            else:
                if spt[CHECK_FIELD] == CHECK_VALUE:
                    logger._log_to_console_and_log_file("Validation: spt {0} manage firmware not matching with sp {1}".format(spt['manageFirmware'], sp['manageFirmware']))
                    flagcc = 1
        if flagcc == 1:
            logger._log_to_console_and_log_file("**** SPT firmware {0} ".format(spt))
            logger._log_to_console_and_log_file("**** SP firmware {0} ".format(sp))
            return False
        else:
            return True

    def __validate_bios(self, spt, sp):
        """
        Validate SP and SPT bios based on Consistency Check
        """
        flagcc = 0
        if 'manageBios' is spt:
            if spt['manageBios']:
                if 'manageBios' in sp:
                    if spt['manageBios'] == sp['manageBios']:
                        if spt[CHECK_FIELD] == CHECK_VALUE:
                            for key in spt.keys():
                                if key == 'manageBios' or key == 'manageBios':
                                    continue
                                else:
                                    if spt[key] != sp[key]:
                                        logger._log_to_console_and_log_file("Validation: Bios setting Failed to match {0} between SP and SPT".format(key))
                                        flagcc = 1
                            return True
                    else:
                        if spt[CHECK_FIELD] == CHECK_VALUE:
                            logger._log_to_console_and_log_file("Validation: BIOS manageBios is not matching spt:{0} sp:{1}".format(spt['manageBios'], sp['manageBios']))
                            flagcc = 1
        if flagcc == 1:
            logger._log_to_console_and_log_file("**** SPT bios {0} ".format(spt))
            logger._log_to_console_and_log_file("**** SP bios {0} ".format(sp))
            return False
        else:
            return True

    def __validate_local_storage(self, spt, sp):
        """
        Validate local storage between SP and SPT
        """
        flagcc = 0
        if spt is not None and sp is not None:
            if 'controllers' in spt and 'controllers' in sp:
                if spt[CHECK_FIELD] == CHECK_VALUE:
                    if len(spt['controllers']) != len(sp['controllers']):
                        logger._log_to_console_and_log_file("Validation: SPT local storage controller Failed to match with SP")
                        flagcc = 1
                    else:
                        spt_contr = spt['controllers']
                        sp_contr = sp['controllers']
                        if "logicalDrives" in spt_contr and "logicalDrives" in sp_contr:
                            if len(spt_contr["logicalDrives"]) != len(sp_contr["logicalDrives"]):
                                logger._log_to_console_and_log_file("Validation: SPT local storage controller Failed to match with SP")
                                flagcc = 1
                            else:
                                spt_drive = [log_dr['name'] for log_dr in spt_contr["logicalDrives"]]
                                sp_drive = [log_dr['name'] for log_dr in sp_contr["logicalDrives"]]
                                dif = set(spt_drive).symmetric_difference(set(sp_drive))
                                if dif:
                                    logger._log_to_console_and_log_file("Validation: local storage controller logical drive: {0} SPT failed to match with SP".format(dif))
                                    flagcc = 1
                elif spt[CHECK_FIELD] == MIN_CHECK_VALUE:
                    if len(spt['controllers']) < len(sp['controllers']):
                        logger._log_to_console_and_log_file("Validation: SPT local storage controller Failed to match with SP")
                        flagcc = 1
                    else:
                        spt_contr = spt['controllers']
                        sp_contr = sp['controllers']
                        if "logicalDrives" in spt_contr and "logicalDrives" in sp_contr:
                            if len(spt_contr["logicalDrives"]) != len(sp_contr["logicalDrives"]):
                                logger._log_to_console_and_log_file("Validation: SPT local storage controller Failed to match with SP")
                                flagcc = 1
                            else:
                                spt_drive = [log_dr['name'] for log_dr in spt_contr["logicalDrives"]]
                                sp_drive = [log_dr['name'] for log_dr in sp_contr["logicalDrives"]]
                                dif = set(spt_drive).difference(set(sp_drive))
                                if dif:
                                    logger._log_to_console_and_log_file("Validation: local storage logical drives: {0} SPT failed to match with SP".format(dif))
                                    flagcc = 1
            if 'sasLogicalJBODs' in spt and 'sasLogicalJBODs' in sp:
                if spt[CHECK_FIELD] == CHECK_FIELD:
                    if len(spt["sasLogicalJBODs"]) != len(sp["sasLogicalJBODs"]):
                        logger._log_to_console_and_log_file("Validation: SPT local storage sasLogicalJBODs Failed to match with SP")
                        flagcc = 1
                    else:
                        spt_sas = [log_dr['name'] for log_dr in spt["logicalDrives"]]
                        sp_sas = [log_dr['name'] for log_dr in sp["logicalDrives"]]
                        dif = set(spt_sas).symmetric_difference(set(sp_sas))
                        if dif:
                            logger._log_to_console_and_log_file("Validation: local storage saslogical : {0} SPT failed to match with SP".format(dif))
                            flagcc = 1
                elif spt[CHECK_FIELD] == MIN_CHECK_VALUE:
                    if len(spt["sasLogicalJBODs"]) < len(sp["sasLogicalJBODs"]):
                        logger._log_to_console_and_log_file("Validation: SPT local storage sasLogicalJBODs Failed to match with SP")
                        flagcc = 1
                    else:
                        spt_sas = [log_dr['name'] for log_dr in spt["sasLogicalJBODs"]]
                        sp_sas = [log_dr['name'] for log_dr in sp["sasLogicalJBODs"]]
                        dif = set(spt_sas).difference(set(sp_sas))
                        if dif:
                            logger._log_to_console_and_log_file("Validation: local storage saslogical : {0} SPT failed to match with SP".format(dif))
                            flagcc = 1
        if flagcc == 1:
            logger._log_to_console_and_log_file("**** SPT local storage {0} ".format(spt))
            logger._log_to_console_and_log_file("**** SP local storage {0} ".format(sp))
            return False
        else:
            return True

    def missing_key(self, l, r):
        """
        compare two set of resource
        """
        return list(set(l).symmetric_difference(r))

    def __validate_boot(self, spt_boot, sp_boot, spt_bootMode, sp_bootMode):
        """
        Validate boot section between SP and SPT
        """
        flagcc = 0
        if sp_bootMode is not None and spt_bootMode is not None:
            if spt_boot[CHECK_FIELD] != sp_bootMode[CHECK_FIELD]:
                logger._log_to_console_and_log_file("Validation: Consistency check in Boot Mode is not matching with Moot in SPT ")
                flagcc = 1
            else:
                for key in spt_bootMode.keys():
                    if key != CHECK_FIELD or key != 'manageBoot':
                        if spt_bootMode[key] != sp_bootMode[key]:
                            logger._log_to_console_and_log_file("Validation: Boot setting in SPT :{0} is not matching with SP".format(key))
                            flagcc = 1
        if spt_boot['manageBoot']:
            for key in spt_boot.keys():
                if key != 'manageBoot' and key != CHECK_FIELD:
                    if spt_boot[key] != sp_boot[key]:
                        logger._log_to_console_and_log_file("Validation: Boot setting in SPT :{0} is not matching with SP".format(key))
                        flagcc = 1
                    else:
                        if isinstance(sp_boot[key], list):
                            if self.missing_key(spt_boot[key], sp_boot[key]):
                                logger._log_to_console_and_log_file("Validation: boot setting : missing element in {0}: {1}".format(key, self.missing_key(spt_boot[key], sp_boot[key])))
                                flagcc = 1
                            order_mismatch = [spt_boot[key][i] for i in range(len(spt_boot[key])) if spt_boot[key][i] != sp_boot[key][i]]
                            if order_mismatch:
                                logger._log_to_console_and_log_file("Validation: boot setting : mismatch in boot {0}: {1}".format(key, order_mismatch))
                                flagcc = 1

        if flagcc == 1:
            logger._log_to_console_and_log_file("**** SPT boot {0} ".format(spt_boot))
            logger._log_to_console_and_log_file("**** SP boot {0} ".format(sp_boot))
            logger._log_to_console_and_log_file("**** SPT boot {0} ".format(spt_bootMode))
            logger._log_to_console_and_log_file("**** SP boot {0} ".format(sp_bootMode))
            return False
        else:
            return True

    def validate_profile_compliance(self, payload, compliance_status):
        """
        Validate required compliance preview is been generated based on new feature and difference
        in setting between SP and SPT
        """
        parameter = '?filter=name=\'%s\''
        logger._log_to_console_and_log_file("compliance_status {0}".format(compliance_status))
        flagcc = 0
        if payload:
            if 'name' in payload:
                sp_param = parameter % payload['name']
                get_sp = self.fusionlib.fusion_api_get_server_profiles(uri=None, api=None, headers=None, param=sp_param)
                if get_sp:
                    if 'count' in get_sp:
                        if get_sp['count'] > 0:
                            for sp in get_sp['members']:
                                if 'serverProfileTemplateUri' in sp and sp['serverProfileTemplateUri'] is not None:
                                    get_spt = self.fusionlib.fusion_api_get_server_profile_templates(uri=sp['serverProfileTemplateUri'])
                                    get_sp1 = self.fusionlib.fusion_api_get_server_profiles(uri=sp['uri'])
                                    for spt_f in self.field:
                                        if spt_f in get_spt and spt_f in get_sp1:
                                            if spt_f != 'bootMode':
                                                if spt_f == 'connectionSettings':
                                                    connection_status = self.__validate_connectionSettings(get_spt[spt_f], get_sp1[spt_f])
                                                    if not connection_status:
                                                        logger._log_to_console_and_log_file("Validation Failed : connection : SP is not consistent with SPT")
                                                        flagcc = 1
                                                if spt_f == 'sanStorage':
                                                    sanStorage_status = self.__validate_sanStorage(get_spt[spt_f], get_sp1[spt_f])
                                                    if not sanStorage_status:
                                                        logger._log_to_console_and_log_file("Validation Failed : san storage : SP is not consistent with SPT")
                                                        flagcc = 1
                                                if spt_f == 'firmware':
                                                    firmware_status = self.__validate_firmware(get_spt[spt_f], get_sp1[spt_f])
                                                    if not firmware_status:
                                                        logger._log_to_console_and_log_file("Validation Failed : firmware : SP is not consistent with SPT")
                                                        flagcc = 1
                                                if spt_f == 'bios':
                                                    bios_status = self.__validate_bios(get_spt[spt_f], get_sp1[spt_f])
                                                    if not bios_status:
                                                        logger._log_to_console_and_log_file("Validation Failed : bios : SP is not consistent with SPT")
                                                        flagcc = 1
                                                if spt_f == 'boot':
                                                    boot_status = self.__validate_boot(get_spt[spt_f], get_sp1[spt_f], get_spt['bootMode'], get_sp1['bootMode'])
                                                    if not boot_status:
                                                        logger._log_to_console_and_log_file("Validation Failed: boot : SP is not consistent with SPT")
                                                        flagcc = 1
                                                if spt_f == 'localStorage':
                                                    localStr_status = self.__validate_local_storage(get_spt[spt_f], get_sp1[spt_f])
                                                    if not localStr_status:
                                                        logger._log_to_console_and_log_file("Validation Failed: local storage : SP is not consistent with SPT")
                                                        flagcc = 1
        if flagcc == 1:
            logger._log_to_console_and_log_file("Consistency Check validation Failed: Profile is not consistent with template")
            return False
        else:
            logger._log_to_console_and_log_file("Consistency Check validation Passed: Profile is consistent with template")
            return True

    @enable_OVF3651
    def dynamic_arguments(self, argument, **feature):
        '''
        This module supports  new feature and backward compactible with older release(4.0| Ediburgh release)

        This will ensures to perform required data manipulation based on the feature toggle enabled (OVF1053) and
        data are grouped together into list of operation with its payload and required condition.

        In addition to it, based on the data variable template the server hardware and hardware type will be  dynamically assigned.
         we can disable it by adding argument  "NoChange" , thus user does can directly use the payload from data varible file without manipulation

        For feature toggle  OVF1053 enabled in 4.10/Frankfurt use (x-api-version:800):
            dynamic arguments    ${<list of arguments>}    OVF1053=${OVF1053}

        If no feature toggle enabled but dynamically genarate payload with hardware and hardware type, where payload is from data variable template file
            (can be used in 4.10/4.0) : x-api-version:600
            dynamic arguments    ${argument}

        If no feature toggle is enabled and use payload directly from data variable file
            (can be used in 4.10/4.0) : x-api-version:600
            dynamic arguments    ${argument}    NoChange=False
        '''
        keys = [k for k in argument.keys() if re.match("opn\d+\s*$", k)]
        opn_lst = {}
        if 'SERVER_PROFILE_TEMPLATE_TYPE' in argument.keys():
            self.SERVER_PROFILE_TEMPLATE_TYPE = argument['SERVER_PROFILE_TEMPLATE_TYPE']
        if 'SERVER_PROFILE_TYPE' in argument.keys():
            self.SERVER_PROFILE_TYPE = argument['SERVER_PROFILE_TYPE']
        if 'CONSISTENCY_CHECK_HW' in argument.keys():
            self.hardware = argument['CONSISTENCY_CHECK_HW']
        if 'OVF1053' in argument.keys():
            consistency_check_feature = argument['OVF1053']
        elif 'OVF1053' in feature.keys():
            consistency_check_feature = feature['OVF1053']
        else:
            consistency_check_feature = None
        for opern in keys:
            opn = re.match("opn(\d+)", opern)
            opn_lst[opern] = {}
            opn_lst[opern]["opn"] = argument[opern]
            if opn:
                opn_num = opn.group(1)
                opn_lst[opern]["num"] = int(opn_num)
                if opern + "_payload" in argument.keys():
                    if "NoChange" in feature.keys() and feature["NoChange"] == 'True':
                        opn_lst[opern]["payload"] = argument[opern + "_payload"]
                    elif "NoChange" in feature.keys() and feature["NoChange"] == 'False':
                        if consistency_check_feature is not None:
                            opn_lst[opern]["payload"] = self.generate_test_data(argument[opern + "_payload"], consistency_check_feature)
                        else:
                            opn_lst[opern]["payload"] = self.generate_test_data(argument[opern + "_payload"], 'NoCheck')
                    elif "NoChange" not in feature.keys():
                        if consistency_check_feature is not None:
                            opn_lst[opern]["payload"] = self.generate_test_data(argument[opern + "_payload"], consistency_check_feature)
                        else:
                            opn_lst[opern]["payload"] = self.generate_test_data(argument[opern + "_payload"], 'NoCheck')
                else:
                    opn_lst[opn]["payload"] = None
                if opn_num == str(1):
                    if "isPositive" in argument:
                        opn_lst[opern]["isPositive"] = argument["isPositive"]
                    else:
                        opn_lst[opern]["isPositive"] = True
                else:
                    if "isPositive" + opn_num in argument.keys():
                        opn_lst[opern]["isPositive"] = argument["isPositive" + opn_num]
                    else:
                        opn_lst[opern]["isPositive"] = True
                if opn_num == str(2):
                    if "errorMessage" in argument:
                        opn_lst[opern]["errorMessage"] = argument["errorMessage"]
                    else:
                        opn_lst[opern]["errorMessage"] = None
                else:
                    if "errorMessage" + opn_num in argument.keys():
                        opn_lst[opern]["errorMessage"] = argument["errorMessage" + opn_num]
                    else:
                        opn_lst[opern]["errorMessage"] = None
                if opn_num == str(4):
                    if 'compliancePreview' in argument.keys():
                        opn_lst[opern]["compliancePreview"] = argument["compliancePreview"]
                    else:
                        opn_lst[opern]["compliancePreview"] = None
                else:
                    if 'compliancePreview' + opn_num in argument.keys():
                        opn_lst[opern]["compliancePreview"] = argument["compliancePreview" + opn_num]
                    else:
                        opn_lst[opern]["compliancePreview"] = None
        opn_keys = sorted(opn_lst.keys(), key=lambda x: opn_lst[x]["num"])
        logger._log_to_console_and_log_file("operation {0}".format(opn_keys))
        logger._log_to_console_and_log_file(opn_lst)
        return opn_keys, opn_lst

    def modify_profile_compliance_payload(self, payload, **feature):
        """
        Modify compliance preview payload based on OVF3651 and OVF1053
        """
        logger._log_to_console_and_log_file("original compliance preview payload :{0}".format(payload))
        pattern_Uncheck = ".*((FlexNICs)|(Change enclosure group)).*"
        pattern_checkMin = ".*((Delete the connection .)|(Delete volume attachment)).*"
        patternUncheck_checkminimum = [".*Change boot order", ".*Change enclosure group.*", ".*Change BIOS settings.*", ".*Change firmware.*"]
        off_Check_checkmin = [".*Create a connection to network.*", ".*FlexNICs.*", ".*Change boot order.*", ".*Change boot for connection.*", ".*Change boot source of connection.*", ".*Change enclosure group*"]
        on_Check_checkmin = [".*Change requested bandwidth.*", ".*Create volume.*"]
        pattern_egOptional = ".*Change enclosure group.*"
        if 'compliance-preview' in payload:
            if 'OVF3651' in feature and feature['OVF3651'] != "NoOVF3651":
                if payload["compliance-preview"]["automaticUpdates"] is not None:
                    for cp in payload["compliance-preview"]["manualUpdates"]:
                        if not payload["compliance-preview"]["manualUpdates"]:
                            break
                        if re.match(pattern_egOptional, str(cp)):
                            payload["compliance-preview"]["manualUpdates"].remove(cp)
            if 'OVF1053' in feature:
                if feature['OVF1053'] == CHECK_VALUE:
                    return payload
                elif feature['OVF1053'] == UNCHECK_VALUE:
                    if payload["compliance-preview"]["automaticUpdates"] is not None:
                        if payload["compliance-preview"]["automaticUpdates"]:
                            payload["compliance-preview"]["automaticUpdates"] = [i for i in payload["compliance-preview"]["automaticUpdates"] if re.match(pattern_Uncheck, str(i))]
                    if payload["compliance-preview"]["manualUpdates"] is not None:
                        if payload["compliance-preview"]["manualUpdates"]:
                            payload["compliance-preview"]["manualUpdates"] = [i for i in payload["compliance-preview"]["manualUpdates"] if re.match(pattern_Uncheck, str(i))]
                    if "isOnlineUpdate" in payload["compliance-preview"] and payload["compliance-preview"]["isOnlineUpdate"] is not None:
                        if not payload["compliance-preview"]["automaticUpdates"]:
                            payload["compliance-preview"]["isOnlineUpdate"] = None
                    logger._log_to_console_and_log_file("modified compliance preview payload :{0}".format(payload))
                    return payload
                elif feature['OVF1053'] == 'CheckedMinimumChecked' or feature['OVF1053'] == 'CheckedMinimumUnchecked':
                    if payload["compliance-preview"]["automaticUpdates"] is not None:
                        for cp in payload["compliance-preview"]["automaticUpdates"]:
                            if not payload["compliance-preview"]["automaticUpdates"]:
                                break
                            if re.match(pattern_checkMin, str(cp)):
                                payload["compliance-preview"]["automaticUpdates"].remove(cp)
                        if feature['OVF1053'] == 'CheckedMinimumUnchecked':
                            au_lst = [i for i in payload["compliance-preview"]["automaticUpdates"] for pat in patternUncheck_checkminimum if re.match(pat, i)]
                            payload["compliance-preview"]["automaticUpdates"] = [i for i in payload["compliance-preview"]["automaticUpdates"] if i not in au_lst]
                    if payload["compliance-preview"]["manualUpdates"] is not None:
                        for cp in payload["compliance-preview"]["manualUpdates"]:
                            if not payload["compliance-preview"]["manualUpdates"]:
                                break
                            if re.match(pattern_checkMin, str(cp)):
                                payload["compliance-preview"]["manualUpdates"].remove(cp)
                        if feature['OVF1053'] == 'CheckedMinimumUnchecked':
                            mu_lst = [i for i in payload["compliance-preview"]["manualUpdates"] for pat in patternUncheck_checkminimum if re.match(pat, i)]
                            payload["compliance-preview"]["manualUpdates"] = [i for i in payload["compliance-preview"]["manualUpdates"] if i not in mu_lst]
                    if "isOnlineUpdate" in payload["compliance-preview"] and payload["compliance-preview"]["isOnlineUpdate"] is not None:
                        au = [i for i in payload["compliance-preview"]["automaticUpdates"] for pat in off_Check_checkmin if re.match(pat, i)]
                        if au:
                            payload["compliance-preview"]["isOnlineUpdate"] = False
                        else:
                            online_au = [i for i in payload["compliance-preview"]["automaticUpdates"] for pat in on_Check_checkmin if re.match(pat, i)]
                            if online_au:
                                payload["compliance-preview"]["isOnlineUpdate"] = True
                            else:
                                payload["compliance-preview"]["isOnlineUpdate"] = None
                    logger._log_to_console_and_log_file("modified compliance preview payload :{0}".format(payload))
                    return payload
            else:
                return payload

    def validation_for_EG_optional(self, payloads):
        """
        Validate the expected  result based on OVF3651 behavior
        """
        parameter = '?filter=name=\'%s\''
        spt_type_pattern = '^(ServerProfileTemplateV).\d*'
        sp_type_pattern = '^(ServerProfileV).\d*'
        if isinstance(payloads, list):
            for payload in payloads:
                if 'type' in payload:
                    if re.match(spt_type_pattern, payload['type']):
                        spt_param = parameter % payload['name']
                        get_spt = self.fusionlib.fusion_api_get_server_profile_templates(uri=None, api=None, headers=None, param=spt_param)
                        return self.__network_target_validation_for_EG('SPT', get_spt)
                    elif re.match(sp_type_pattern, payload['type']):
                        sp_param = parameter % payload['name']
                        get_sp = self.fusionlib.fusion_api_get_server_profiles(uri=None, api=None, headers=None, param=sp_param)
                        return self.__network_target_validation_for_EG('SP', get_sp)
                elif 'SP' in payload:
                    spt_param = parameter % payload['name']
                    get_spt = self.fusionlib.fusion_api_get_server_profile_templates(uri=None, api=None, headers=None, param=spt_param)
                    return self.__network_target_validation_for_EG('SPT', get_spt)

    def intersect(self, a, b):
        """
        difference between  two list of specific resource
        """
        return set(a).intersection(set(b))

    def __network_target_validation_for_EG(self, rtype, payload):
        """
        Validate network section for OVF3651 SPT payload
        """
        if rtype:
            logger._log_to_console_and_log_file("payload :{0}".format(payload))
            eg_data = self.__avail_networks_and_servers_in_EG()
            eg_network_table = {}
            if 'count' in payload:
                if payload['count'] > 0 and 'members' in payload:
                    for pd in payload['members']:
                        if 'connectionSettings' in pd and 'connections' in pd['connectionSettings']:
                            networks = [conn['networkUri'] for conn in pd['connectionSettings']['connections']]
                            for net in networks:
                                eg_list = []
                                for eg in eg_data:
                                    if net in eg_data[eg]['networks']:
                                        eg_list.append(eg)
                                if tuple(eg_list) not in eg_network_table.keys():
                                    eg_network_table[tuple(eg_list)] = [net]
                                else:
                                    eg_network_table[tuple(eg_list)].append(net)
                        if eg_network_table:
                            if len(eg_network_table) == 1:
                                iscommonEG = eg_network_table.keys()
                            elif len(eg_network_table) > 1:
                                iscommonEG = reduce(self.intersect, eg_network_table.keys())
                                if iscommonEG:
                                    logger._log_to_console_and_log_file(" iscommonEG {0}".format(iscommonEG))
                                else:
                                    logger._log_to_console_and_log_file(" No common EG for connections in {0}".format(rtype))
                                    logger._log_to_console_and_log_file(" eg table{0}".format(eg_network_table))
                                    return False
                    if rtype == 'SP':
                        if 'serverHardwareUri' in pd and pd['serverHardwareUri'] is not None:
                            for eg in eg_data.keys():
                                if 'servers' in eg_data[eg] and pd['serverHardwareUri'] in eg_data[eg]['servers']:
                                    logger._log_to_console_and_log_file(iscommonEG[0])
                                    logger._log_to_console_and_log_file(eg)
                                    if eg in iscommonEG[0]:
                                        return True
                                    else:
                                        return False
                            logger._log_to_console_and_log_file("server hardware{0} not found in egs".format(pd['serverHardwareUri']))
                            return False
                    return True
                elif payload['count'] == 0:
                    logger._log_to_console_and_log_file("No {0} found".format(rtype))
                    return True
            else:
                return True

    def isTrue(self, a, b):
        """
        check isTrue
        """
        return a and b

    def __avail_networks_and_servers_in_EG(self):
        '''
        Get available network and hardware for list of EGs
        '''
        get_enc = self.fusionlib.fusion_api_get_enclosures()
        enc_data = {}
        if 'members' in get_enc:
            for enc in get_enc['members']:
                if 'name' in enc:
                    name = enc['name']
                    enc_data[name] = {}
                    if 'enclosureGroupUri' in enc:
                        enc_data[name]['EG'] = enc['enclosureGroupUri']
                    if 'deviceBays' in enc:
                        hw = []
                        for bay in enc['deviceBays']:
                            if 'deviceUri' in bay and bay['deviceUri'] is not None and re.match("/rest/server-hardware/*", bay['deviceUri']):
                                hw.append(bay['deviceUri'])
                        enc_data[name]['servers'] = hw
        get_lig = self.fusionlib.fusion_api_get_lig()
        lig_data = {}
        if 'members' in get_lig:
            for lig in get_lig['members']:
                if 'uri' in lig:
                    uri = lig['uri']
                    lig_data[uri] = {}
                    if 'name' in lig:
                        lig_data[uri]['name'] = lig['name']
                    if 'internalNetworkUris' in lig:
                        lig_data[uri]['networks'] = lig['internalNetworkUris']
                    if 'uplinkSets' in lig:
                        for uplink in lig['uplinkSets']:
                            if 'networkUris' in uplink:
                                lig_data[uri]['networks'] = lig_data[uri]['networks'] + uplink['networkUris']

        get_eg = self.fusionlib.fusion_api_get_enclosure_groups()
        eg_data = {}
        if 'members' in get_eg:
            for eg in get_eg['members']:
                if 'uri' in eg:
                    uri = eg['uri']
                    eg_data[uri] = {}
                    if 'name' in eg:
                        eg_data[uri]['name'] = eg['name']
                    if 'associatedLogicalInterconnectGroups' in eg:
                        eg_data[uri]['lig'] = eg['associatedLogicalInterconnectGroups']

        for eg in eg_data.keys():
            networks = []
            for lig in eg_data[eg]['lig']:
                if lig in lig_data.keys():
                    if not networks:
                        networks = lig_data[lig]['networks']
                    else:
                        networks.append(lig_data[lig]['networks'])
            eg_data[eg]['networks'] = networks
        for enc in enc_data.keys():
            for eg in eg_data.keys():
                if eg == enc_data[enc]['EG']:
                    if 'servers' not in eg_data[eg]:
                        eg_data[eg]['servers'] = enc_data[enc]['servers']
                    elif eg_data[eg]['servers']:
                        eg_data[eg]['servers'] = eg_data[eg]['servers'] + enc_data[enc]['servers']
        get_ns = self.fusionlib.fusion_api_get_network_set()
        if 'members' in get_ns:
            for ns in get_ns['members']:
                uri = ns['uri']
                net_uris = ns['networkUris']
                for eg in eg_data.keys():
                    isNSinEG = reduce(self.isTrue, [True if net in eg_data[eg]['networks'] else False for net in net_uris])
                    if isNSinEG:
                        eg_data[eg]['networks'].append(uri)
        logger._log_to_console_and_log_file(" eg data {0}".format(eg_data))
        return eg_data
