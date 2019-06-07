from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import re

fusion_lib = BuiltIn().get_library_instance('FusionLibrary')


def fusion_api_power_off_drive_enclosure(uri):
    patch_payload = [{'op': 'replace', 'path': '/powerState', 'value': 'Off'}]
    response = fusion_lib.fusion_api_patch_drive_enclosure(patch_payload, uri)

    if 'message' in response:
        raise AssertionError(response['message'])

    BuiltIn().run_keyword("Wait for Task2", response, "240", "10")
    response = fusion_lib.fusion_api_get_drive_enclosure(uri=uri)
    power_state_after = response['powerState']

    if power_state_after != 'Off':
        raise AssertionError("powerState failed to get toggle from On to Off")


def fusion_api_power_on_drive_enclosure(uri):
    patch_payload = [{'op': 'replace', 'path': '/powerState', 'value': 'On'}]
    response = fusion_lib.fusion_api_patch_drive_enclosure(patch_payload, uri)

    if 'message' in response:
        raise AssertionError(response['message'])

    BuiltIn().run_keyword("Wait for Task2", response, "240", "10")
    response = fusion_lib.fusion_api_get_drive_enclosure(uri=uri)
    power_state_after = response['powerState']

    if power_state_after != 'On':
        raise AssertionError("powerState failed to get toggle from Off to On")


def fusion_api_power_drive_enclosure_on_and_off_by_name(name):
    response = fusion_lib.fusion_api_get_drive_enclosure(param="?filter='name'=='{0}'".format(name))
    drive_enclosure = response['members'][0]
    power_state = drive_enclosure['powerState']
    uri = drive_enclosure['uri']

    if power_state == 'On':
        fusion_api_power_off_drive_enclosure(uri)
        fusion_api_power_on_drive_enclosure(uri)
    elif power_state == 'Off':
        fusion_api_power_on_drive_enclosure(uri)
        fusion_api_power_off_drive_enclosure(uri)
    else:
        raise AssertionError("powerState does not equal on or off")


def fusion_api_turn_on_uid_drive_enclosure(uri):
    patch_payload = [{'op': 'replace', 'path': '/uidState', 'value': 'On'}]
    response = fusion_lib.fusion_api_patch_drive_enclosure(patch_payload, uri)
    BuiltIn().run_keyword("Wait for Task2", response)
    response = fusion_lib.fusion_api_get_drive_enclosure(uri=uri)
    uid_state_after = response['uidState']

    if uid_state_after != 'On':
        raise AssertionError("uidState failed to get toggle from Off to On")


def fusion_api_turn_off_uid_drive_enclosure(uri):
    patch_payload = [{'op': 'replace', 'path': '/uidState', 'value': 'Off'}]
    response = fusion_lib.fusion_api_patch_drive_enclosure(patch_payload, uri)
    BuiltIn().run_keyword("Wait for Task2", response)
    response = fusion_lib.fusion_api_get_drive_enclosure(uri=uri)
    uid_state_after = response['uidState']

    if uid_state_after != 'Off':
        raise AssertionError("uidState failed to get toggle from On to Off")


def fusion_api_toggle_drive_enclosure_UID_on_and_off_by_name(name):
    response = fusion_lib.fusion_api_get_drive_enclosure(param="?filter='name'=='{0}'".format(name))
    drive_enclosure = response['members'][0]
    uid_state = drive_enclosure['uidState']
    uri = drive_enclosure['uri']

    if uid_state == 'On':
        fusion_api_turn_off_uid_drive_enclosure(uri)
        fusion_api_turn_on_uid_drive_enclosure(uri)
    elif uid_state == 'Off':
        fusion_api_turn_on_uid_drive_enclosure(uri)
        fusion_api_turn_off_uid_drive_enclosure(uri)
    else:
        raise AssertionError("uidState does not equal on or off")


def fusion_api_delete_storage_volume_attachments(svas, api=None, param=''):
    """
    :param svas:  storage volume attachment DTO or a list of SVA DTO
    :param param: ex. ?force=true
    :return: http response
    """
    if isinstance(svas, dict) and re.search('StorageVolumeAttachment', svas['type']):
        logger._log_to_console_and_log_file("The argument svas is SVA DTO.  Convert to list.")
        svas = [svas]
    elif isinstance(svas, list) and len(svas) == 0:
        raise AssertionError("The argument svas %s is an empty list" % svas)
    elif isinstance(svas, list) and isinstance(svas[0], dict) and re.search('StorageVolumeAttachment', svas[0]['type']):
        logger._log_to_console_and_log_file("The argument svas is a list of SVA DTO")
    else:
        raise AssertionError("The argument svas %s is not SVA DTO or a list of SVA DTO" % svas)

    payload = []
    for sva in svas:
        payload.append({"resourceUri": "%s" % sva['uri'],
                        "eTag": "%s" % sva['eTag'],
                        "patchData": [{"op": "remove", "path": "/", "value": None}]})
    if not api:
        if BuiltIn().get_variable_value("${X-API-VERSION}"):
            api = str(BuiltIn().get_variable_value("${X-API-VERSION}"))
        else:
            api = fusion_lib._currentVersion()
    logger._log_to_console_and_log_file("the api version is %s" % api)
    headers = {'Content-Type': 'application/json-patch-array+json', 'Accept-language': 'en_US', 'Accept': 'application/json, */*', 'X-Api-Version': api}
    response = fusion_lib.fusion_api_patch_storage_volume_attachments(body=payload, param=param, headers=headers)
    return response


def check_storage_system_port_status(storage_system):
    """
    param storage_system: storage system DTO or name
    """
    name = storage_system['name']
    param = "?filter=\"'name' = '%s'\"" % name
    response = fusion_lib.fusion_api_get_storage_system(param=param)
    logger._debug("response is %s" % response)
    check = "PASS"
    if response['status_code'] == 200 and response['count'] == 1:
        for port in storage_system['managed_ports']:
            for resp_port in response['members'][0]['ports']:
                if port['name'] == resp_port['name']:
                    logger._debug("port is %s" % port)
                    logger._debug("Storage System port %s has mode %s, connectionState %s, and status %s" % (resp_port['name'], resp_port['mode'], resp_port['connectionState'], resp_port['status']))
                    BuiltIn().log("Storage System port %s has mode %s, connectionState %s, and status %s" % (resp_port['name'], resp_port['mode'], resp_port['connectionState'], resp_port['status']), console=True)
                    if (resp_port['mode'] != 'Managed') or (resp_port['connectionState'] != 'Connected') or (not re.search('OK|WARNING', resp_port['status'])):
                        check = 'FAIL'
    else:
        raise AssertionError("storage system not found %s", name)

    BuiltIn().should_match(check, 'PASS', msg='check storage system port status should match PASS')
