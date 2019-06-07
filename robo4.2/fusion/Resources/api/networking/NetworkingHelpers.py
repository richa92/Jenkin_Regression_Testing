from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger

import re

fusion_lib = BuiltIn().get_library_instance('FusionLibrary')

SAS_INTERCONNECT_POWER_ON_TIMEOUT_IN_SECONDS = '300'
SAS_INTERCONNECT_SOFT_RESET_TIMEOUT_IN_SECONDS = '180'
SAS_INTERCONNECT_HARD_RESET_TIMEOUT_IN_SECONDS = '240'


def fusion_api_refresh_sas_interconnect_by_name(name):
    payload = {'refreshState': 'RefreshPending'}
    uri = BuiltIn().run_keyword("Get SAS Interconnect URI", name)
    response = fusion_lib.fusion_api_refresh_sas_interconnect(payload, uri)

    if 'message' in response:
        raise AssertionError(response['message'])

    BuiltIn().run_keyword("Wait for Task2", response)


def fusion_api_hard_reset_sas_interconnect_by_name(name):
    patch_payload = [{'op': 'replace', 'path': '/deviceResetState', 'value': 'Reset'}]
    uri = BuiltIn().run_keyword("Get SAS Interconnect URI", name)
    response = fusion_lib.fusion_api_patch_sas_interconnect(patch_payload, uri)

    if 'message' in response:
        raise AssertionError(response['message'])

    BuiltIn().run_keyword("Wait for Task2", response, SAS_INTERCONNECT_HARD_RESET_TIMEOUT_IN_SECONDS)


def fusion_api_soft_reset_sas_interconnect_by_name(name):
    patch_payload = [{'op': 'replace', 'path': '/cpuResetState', 'value': 'Reset'}]
    uri = BuiltIn().run_keyword("Get SAS Interconnect URI", name)
    response = fusion_lib.fusion_api_patch_sas_interconnect(patch_payload, uri)

    if 'message' in response:
        raise AssertionError(response['message'])

    BuiltIn().run_keyword("Wait for Task2", response, SAS_INTERCONNECT_SOFT_RESET_TIMEOUT_IN_SECONDS)


def fusion_api_power_off_sas_interconnect(uri):
    patch_payload = [{'op': 'replace', 'path': '/powerState', 'value': 'Off'}]
    response = fusion_lib.fusion_api_patch_sas_interconnect(patch_payload, uri)

    if 'message' in response:
        raise AssertionError(response['message'])

    BuiltIn().run_keyword("Wait for Task2", response)
    response = fusion_lib.fusion_api_get_sas_interconnects(uri=uri)
    power_state_after = response['powerState']

    if power_state_after != 'Off':
        raise AssertionError("powerState failed to toggle from On to Off")


def fusion_api_power_on_sas_interconnect(uri):
    patch_payload = [{'op': 'replace', 'path': '/powerState', 'value': 'On'}]
    response = fusion_lib.fusion_api_patch_sas_interconnect(patch_payload, uri)

    if 'message' in response:
        raise AssertionError(response['message'])

    BuiltIn().run_keyword("Wait for Task2", response, SAS_INTERCONNECT_POWER_ON_TIMEOUT_IN_SECONDS)
    response = fusion_lib.fusion_api_get_sas_interconnects(uri=uri)
    power_state_after = response['powerState']

    if power_state_after != 'On':
        raise AssertionError("powerState failed to toggle from Off to On")


def fusion_api_power_sas_interconnect_on_and_off_by_name(name):
    response = fusion_lib.fusion_api_get_sas_interconnects(param="?filter='name'=='{0}'".format(name))
    sas_interconnect = response['members'][0]
    power_state = sas_interconnect['powerState']
    uri = sas_interconnect['uri']

    if power_state == 'On':
        fusion_api_power_off_sas_interconnect(uri)
        fusion_api_power_on_sas_interconnect(uri)
    elif power_state == 'Off':
        fusion_api_power_on_sas_interconnect(uri)
        fusion_api_power_off_sas_interconnect(uri)
    else:
        raise AssertionError("powerState does not equal On or Off")


def get_interconnect_port_status(interconnect):
    """
    param interconnect: interconnect DTO or name
    """
    name = interconnect['name'] if isinstance(interconnect, dict) else interconnect
    param = "?filter=\"'name' = '%s'\"" % name
    response = fusion_lib.fusion_api_get_interconnect(param=param)
    logger._debug("response is %s" % response)
    if response['status_code'] == 200 and response['count'] == 1:
        interconnect = response['members'][0]
        for port in interconnect['ports']:
            logger._debug("Interconnect %s portName %s portType %s portStatus %s" % (name, port['portName'], port['portType'], port['portStatus']))
            BuiltIn().log("Interconnect %s portName %s portType %s portStatus %s" % (name, port['portName'], port['portType'], port['portStatus']), console=True)
    else:
        raise AssertionError("Interconnect DTO not found for %s", name)

def check_interconnect_linked_port_status(interconnect):
    """
    :param: interconnect
    interconnect = {
        "name": ENC1 + ", interconnect 3",
        "linked_ports": [ 'd3', 'd5', 'd7', 'd13', 'd17', 'd19', 'd25', 'Q1:1', 'Q2:1', 'Q3:1', 'Q7', 'Q8', '11', '12', '13', '14']
}
    """
    param = "?filter=\"'name' = '%s'\"" % interconnect['name']
    response = fusion_lib.fusion_api_get_interconnect(param=param)
    if response['status_code'] == 200 and response['count'] == 1:
        ic_uri = response['members'][0]['uri']
        rtn = re.search('[\w\d]{8}-[\w\d]{4}-[\w\d]{4}-[\w\d]{4}-[\w\d]{12}',ic_uri)
        ic_uuid = rtn.group(0)
        check = 'PASS'
        for port in interconnect['linked_ports']:
            port_uri = ic_uri + '/ports/' + ic_uuid +':' + port
            response = fusion_lib.fusion_api_get_resource(uri=port_uri)
            if response['status_code'] == 200:
                logger._debug('Interconnect %s port %s expected portStatus Linked actual portStatus %s' % (interconnect['name'], port, response['portStatus']))
                BuiltIn().log('Interconnect %s port %s expected portStatus Linked actual portStatus %s' % (interconnect['name'], port, response['portStatus']), console=True)
                if response['portStatus'] != 'Linked':
                    check = 'FAIL'
            else:
                raise AssertionError("Interconnect port DTO not found for %s %s", (interconnect['name'],port))

    else:
        raise AssertionError("Interconnect DTO not found for %s", interconnect['name'])

    BuiltIn().should_match(check, 'PASS', msg='check interconnect linked port status should match PASS')
