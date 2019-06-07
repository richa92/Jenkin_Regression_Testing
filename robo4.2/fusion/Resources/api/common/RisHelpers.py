from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
import re
import subprocess
import sys
import json

fusion_lib = BuiltIn().get_library_instance('FusionLibrary')


def transform_ris_to_oneview(ris_data, type):
    """
    transform ris data to OneView format
    :param ris_data:
    :param type: arrayController, logicalDrive, physicalDrive, storageEnclosure, userPrivilege
    :return ov_data:
    """
    ov_data = {}
    decoder = {}
    if type == 'arrayController':
        decoder = {
            "AdapterType": "adapterType",
            "BackupPowerSourceStatus": "backupPowerSourceStatus",
            "CacheMemorySizeMiB": "cacheMemorySizeMiB",
            "CacheModuleSerialNumber": "cacheModuleSerialNumber",
            "CurrentOperatingMode": "controllerMode",
            "DriveWriteCache": "driveWriteCache",
            "EncryptionCryptoOfficerPasswordSet": "encryptionCryptoOfficerPasswordSet",
            "EncryptionCspTestPassed": "encryptionCspTestPassed",
            "EncryptionEnabled": "encryptionEnabled",
            "EncryptionFwLocked": "encryptionFwLocked",
            "EncryptionHasLockedVolumesMissingBootPassword": "encryptionHasLockedVolumesMissingBootPassword",
            "EncryptionMixedVolumesEnabled": "encryptionMixedVolumesEnabled",
            "EncryptionSelfTestPassed": "encryptionSelfTestPassed",
            "EncryptionStandaloneModeEnabled": "encryptionStandaloneModeEnabled",
            "ExternalPortCount": "externalPortCount",
            "InternalPortCount": "internalPortCount",
            "LocationFormat": "locationFormat",
            "Model": "model",
            "SerialNumber": "serialNumber",
        }
    elif type == 'localUserAccounts':
        decoder = {
            'HostBIOSConfigPriv': 'hostBIOSConfigPriv',
            'HostNICConfigPriv': 'hostNICConfigPriv',
            'HostStorageConfigPriv': 'hostStorageConfigPriv',
            'LoginPriv': 'loginPriv',
            'RemoteConsolePriv': 'remoteConsolePriv',
            'SystemRecoveryConfigPriv': 'systemRecoveryConfigPriv',
            'UserConfigPriv': 'userConfigPriv',
            'VirtualMediaPriv': 'virtualMediaPriv',
            'VirtualPowerAndResetPriv': 'virtualPowerAndResetPriv',
            'iLOConfigPriv': 'iLOConfigPriv',
        }
    elif type == 'logicalDrive':
        decoder = {
            "AccelerationMethod": "accelerator",
            "CapacityMiB": "capacityMiB",
            "LegacyBootPriority": "legacyBootPriority",
            "LogicalDriveEncryption": "logicalDriveEncryption",
            "LogicalDriveName": "logicalDriveName",
            "LogicalDriveNumber": "logicalDriveNumber",
            "LogicalDriveType": "logicalDriveType",
            "MediaType": "mediaType",
            "Model": "model",
            "SerialNumber": "serialNumber",
            "StripeSizeBytes": "stripeSizeBytes",
        }
    elif type == 'physicalDrive':
        decoder = {
            "BlockSizeBytes": "blockSizeBytes",
            "CapacityMiB": "capacityMiB",
            "DiskDriveUse": "diskDriveUse",
            "EncryptedDrive": "encryptedDrive",
            "InterfaceSpeedMbps": "interfaceSpeedMbps",
            "InterfaceType": "interfaceType",
            "LegacyBootPriority": "LegacyBootPriority",
            "Location": "location",
            "LocationFormat": "locationFormat",
            "MediaType": "mediaType",
            "Model": "model",
            "SerialNumber": "serialNumber",
        }
    elif type == 'storageEnclosure':
        decoder = {
            "Id": "id",
            "DriveBayCount": "DriveBayCount",
            "Location": "location",
            "LocationFormat": "locationFormat",
            "Model": "model",
            "SerialNumber": "serialNumber",
        }
    elif type == 'userPrivilege':
        decoder = {
            'HostBIOSConfigPriv': 'hostBIOSConfigPriv',
            'HostNICConfigPriv': 'hostNICConfigPriv',
            'HostStorageConfigPriv': 'hostStorageConfigPriv',
            'LoginPriv': 'loginPriv',
            'RemoteConsolePriv': 'remoteConsolePriv',
            'SystemRecoveryConfigPriv': 'systemRecoveryConfigPriv',
            'UserConfigPriv': 'userConfigPriv',
            'VirtualMediaPriv': 'virtualMediaPriv',
            'VirtualPowerAndResetPriv': 'virtualPowerAndResetPriv',
            'iLOConfigPriv': 'iLOConfigPriv',
        }

    for k in decoder.keys():
        v = decoder[k]
        if k in ris_data.keys():
            ov_data[v] = ris_data[k]
        else:
            ov_data[v] = None

    return ov_data


def get_ris_resource(ilo, username, password, path):
    """
    Get the ris resource
    :param ilo:
    :param username:
    :param password:
    :param path:
    :return: output: dictionary
    """
    output = ''
    try:
        command = "curl -ksL --user %s:%s -X GET https://%s%s" % (username, password, ilo, path)
        logger._debug("The curl command is %s " % command)
        output = subprocess.check_output(command)
        if output != '' and 'error' not in output:
            logger._debug("The RIS resource %s for iLO %s output is %s" % (path, ilo, output))
            return json.loads(output)
        else:
            raise AssertionError("Get RIS resource %s for iLO %s had error" % (path, ilo))
    except subprocess.CalledProcessError as e:
        raise AssertionError("Get RIS resource %s for iLO %s had exception" % (path, ilo))


def put_ris_resource(ilo, username, password, path, payload):
    """
    put the ris resource
    :param ilo:
    :param username:
    :param password:
    :param path: /redfish/v1/Systems/1/smartstorageconfig/settings
    :param payload: JSON
    :return: True or False
    """
    output = ''
    try:
        command = "curl -ksL --user %s:%s -H 'content-type:application/json' -X PUT --data '%s' https://%s%s" % (username, password, payload, ilo, path)
        logger._debug("The curl command is %s " % command)
        output = subprocess.check_output(command)
        logger._debug("PUT RIS resource %s for iLO %s output is %s" % (path, ilo, output))
        if output != '' and 'Success' in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        raise AssertionError("Delete RIS resource %s for iLO %s had exceptions" % (path, ilo))


def delete_ris_resource(ilo, username, password, path):
    """
    delete the ris resource
    :param ilo:
    :param username:
    :param password:
    :param path: /redfish/v1/AccountService/Accounts/37/
    :return: True or False
    """
    output = ''
    try:
        command = "curl -ksL --user %s:%s -X DELETE https://%s%s" % (username, password, ilo, path)
        logger._debug("The curl command is %s " % command)
        output = subprocess.check_output(command)
        logger._debug("Delete RIS resource %s for iLO %s output is %s" % (path, ilo, output))
        if output != '' and 'Removed' in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        raise AssertionError("Delete RIS resource %s for iLO %s had exceptions" % (path, ilo))


def get_ris_array_controller_component(ilo, username, password, path, component_type):
    """
    Get the array controller component in OneView format
    :param ilo:
    :param username:
    :param password:
    :param path: /redfish/v1/Systems/1/SmartStorage/ArrayControllers/0/<type>/0/
    :param component_type: logicalDrive, physicalDrive, storageEnclosure
    :return component: dictionary
    """
    component = {}
    if component_type == 'logicalDrive':
        component['physicalDrives'] = []
    d = get_ris_resource(ilo, username, password, path)
    component = d  # transform_ris_to_oneview(d, component_type)
    if component_type == 'logicalDrive':
        component['physicalDrives'] = get_ris_array_controller_components(ilo, username, password, d['Links']['DataDrives']['@odata.id'], 'physicalDrive')
    elif component_type == 'physicalDrive' or component_type == 'storageEnclosure':
        component['firmwareVersion'] = d['FirmwareVersion']['Current']['VersionString']
        component['status'] = d['Status']['Health']

    return component


def get_ris_array_controller_components(ilo, username, password, path, component_type):
    """
    Get the array controller components in OneView format
    :param ilo:
    :param username:
    :param password:
    :param path: /redfish/v1/Systems/1/SmartStorage/ArrayControllers/0/<type>
    :param component_type: logicalDrive, physicalDrive, storageEnclosure
    :return component_list:
    """
    component_list = []
    d = get_ris_resource(ilo, username, password, path)
    if 'Members@odata.count' in d.keys() and d['Members@odata.count'] != 0:
        for member in d['Members']:
            path = member['@odata.id']
            component_list.append(get_ris_array_controller_component(ilo, username, password, path, component_type))

    return component_list


def get_ris_array_controller(ilo, username, password, path):
    """
    Get the array controller in OneView format
    :param ilo:
    :param username:
    :param password:
    :param path: /redfish/v1/Systems/1/SmartStorage/ArrayControllers/0/
    :return controller:
    """
    controller = {}
    controller['LogicalDrives'] = []
    controller['PhysicalDrives'] = []
    controller['StorageEnclosures'] = []
    controller['UnconfiguredDrives'] = []
    d = get_ris_resource(ilo, username, password, path)
    controller = d  # transform_ris_to_oneview(d, 'arrayController')
    j, controller['slotNumber'] = d['Location'].split()
    # controller['firmwareVersion'] = d['FirmwareVersion']['Current']['VersionString']
    # controller['status'] = d['Status']['Health']
    if 'Links' in d.keys() and isinstance(d['Links'], dict) and d['Links']:
        if 'LogicalDrives' in d['Links']:
            controller['LogicalDrives'] = get_ris_array_controller_components(ilo, username, password, d['Links']['LogicalDrives']['@odata.id'], 'logicalDrive')
        if 'PhysicalDrives' in d['Links']:
            controller['PhysicalDrives'] = get_ris_array_controller_components(ilo, username, password, d['Links']['PhysicalDrives']['@odata.id'], 'physicalDrive')
        if 'StorageEnclosures' in d['Links']:
            controller['StorageEnclosures'] = get_ris_array_controller_components(ilo, username, password, d['Links']['StorageEnclosures']['@odata.id'], 'storageEnclosure')
        if 'UnconfiguredDrives' in d['Links']:
            controller['UnconfiguredDrives'] = get_ris_array_controller_components(ilo, username, password, d['Links']['UnconfiguredDrives']['@odata.id'], 'physicalDrive')
    return controller


def get_ris_array_controllers(ilo, username, password):
    """
    Get the array controllers in OneView format
    :param ilo:
    :param username:
    :param password:
    :return rtn: controller list in OneView format
    """
    rtn = {}
    controller_list = []
    d = get_ris_resource(ilo, username, password, '/redfish/v1/Systems/1/smartstorage/ArrayControllers')
    if 'Members' in d.keys() and isinstance(d['Members'], list):
        if len(d['Members']) != 0:
            for item in d["Members"]:
                path = item['@odata.id']
                controller = get_ris_array_controller(ilo, username, password, path)
                controller_list.append(controller)
    rtn['data'] = controller_list
    return rtn


def get_ris_local_user_account(ilo, username, password, path):
    """
    get the local user account in OneView format
    :param ilo:
    :param username:
    :param password:
    :param path: /redfish/v1/AccountService/Accounts/1/
    :return: user_account = {u'@odata.type': u'#ManagerAccount.v1_0_0.ManagerAccount',
                            u'UserName': u'Administrator', u'Description': u'iLO User Account',
                            u'@odata.id': u'/redfish/v1/AccountService/Accounts/1/', u'@odata.context':
                            u'/redfish/v1/$metadata#ManagerAccount.ManagerAccount',
                            u'Oem': {u'Hpe': {u'@odata.type': u'#HpeiLOAccount.v2_1_0.HpeiLOAccount',
                            u'Privileges': {u'HostNICConfigPriv': True, u'HostStorageConfigPriv': True,
                                            u'RemoteConsolePriv': True, u'iLOConfigPriv': True,
                                            u'VirtualMediaPriv': True, u'UserConfigPriv': True,
                                            u'HostBIOSConfigPriv': True, u'VirtualPowerAndResetPriv': True,
                                            u'LoginPriv': True, u'SystemRecoveryConfigPriv': True},
                            u'LoginName': u'Administrator',
                            u'ServiceAccount': False,
                            u'@odata.context': u'/redfish/v1/$metadata#HpeiLOAccount.HpeiLOAccount'}},
                            u'Name': u'User Account',
                            u'Password': None, u'Id': u'1', u'@odata.etag': u'W/"FA68B14A"'}
    """
    user = {}
    d = get_ris_resource(ilo, username, password, path)
    # get the OEM path
    if 'Oem' in d.keys() and 'Hpe' in d['Oem'].keys():
        oem_path = 'Hpe'
    elif 'Oem' in d.keys() and 'Hp' in d['Oem'].keys():
        oem_path = 'Hp'
    else:
        raise AssertionError("iLO user account OEM path not defined")
    # get the user priv
    if 'Privileges' in d['Oem'][oem_path]:
        user = transform_ris_to_oneview(d['Oem'][oem_path]['Privileges'], 'userPrivilege')
    user['userName'] = d['UserName']
    user['displayName'] = d['Oem'][oem_path]['LoginName']
    return user


def get_ris_local_user_names(ilo, username, password):
    """
    get the local user names
    :param ilo:
    :param username:
    :param password:
    :return" user_names = [u'Administrator', u'_HPOneViewAdmin']
    """
    user_names = []
    d = get_ris_resource(ilo, username, password, '/redfish/v1/AccountService/Accounts')
    if 'Members' in d.keys():
        if isinstance(d['Members'], list) and len(d['Members']) != 0:
            for item in d["Members"]:
                path = item['@odata.id']
                user = get_ris_local_user_account(ilo, username, password, path)
                user_names.append(user['userName'])
    else:
        raise AssertionError("No user accounts for iLO %s defined" % ilo)
    return user_names


def get_ris_local_user_accounts(ilo, username, password):
    """
    get the local user accounts except in OneView format except Administrator and __HPOneViewAdmin
    :param ilo:
    :param username:
    :param password:
    :return: user_accounts = {  'localAccounts': [{'userName': u'test',
                                'hostNICConfigPriv': False,
                                'displayName': u'test',
                                'hostStorageConfigPriv': False,
                                'remoteConsolePriv': True,
                                'iLOConfigPriv': False,
                                'virtualMediaPriv': True,
                                'userConfigPriv': False,
                                'hostBIOSConfigPriv': False,
                                'virtualPowerAndResetPriv': True,
                                'loginPriv': True,
                                'systemRecoveryConfigPriv': False}]}
    """
    user_list = []
    rtn = {}
    d = get_ris_resource(ilo, username, password, '/redfish/v1/AccountService/Accounts')
    if 'Members' in d.keys():
        if isinstance(d['Members'], list) and len(d['Members']) != 0:
            for item in d["Members"]:
                path = item['@odata.id']
                user = get_ris_local_user_account(ilo, username, password, path)
                if user['userName'] == 'Administrator' or user['userName'] == '_HPOneViewAdmin':
                    continue
                else:
                    user_list.append(user)
    else:
        raise AssertionError("No user accounts for iLO %s defined" % ilo)

    rtn['localAccounts'] = user_list
    return rtn


def delete_ris_local_user_accounts(ilo, username, password):
    """
    delete the local user accounts except Administrator and __HPOneViewAdmin
    :param ilo:
    :param username:
    :param password:
    :return: True or False
    """
    rtn = True
    d = get_ris_resource(ilo, username, password, '/redfish/v1/AccountService/Accounts')
    if 'Members' in d.keys():
        if isinstance(d['Members'], list) and len(d['Members']) != 0:
            for item in d["Members"]:
                path = item['@odata.id']
                user = get_ris_local_user_account(ilo, username, password, path)
                if user['userName'] == 'Administrator' or user['userName'] == '_HPOneViewAdmin':
                    continue
                else:
                    r = delete_ris_resource(ilo, username, password, path)
                    if r:
                        logger._debug("Deleted user account %s for iLO %s" % (user['userName'], ilo))
                    else:
                        rtn = False
                        logger._debug("Delete user account %s for iLO %s failed" % (user['userName'], ilo))
    else:
        raise AssertionError("No user accounts for iLO %s defined" % ilo)

    return rtn


def server_profile_mpsettings_local_accounts_should_match_ris(profile, ilo, username, password):
    """
    :param profile = {
        "type": SERVER_PROFILE_TYPE,
        "name": "TEST",
        "description": None,
        "serverHardwareUri": 'SH:'+ENC1SHBAY1,
        "enclosureGroupUri": 'EG:'+EG_NAME,
        "enclosureUri": 'ENC:'+ ENC1,
        "serverProfileTemplateUri": "SPT:",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "osDeploymentSettings": None,
        "connectionSettings": {"connections":[]},
        "boot":{"manageBoot": False, "order": []}, "bootMode":None,
        "firmware":{"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False,"firmwareInstallType": None},
        "bios": {"manageBios": False, "overriddenSettings": []},
        "localStorage": {"sasLogicalJBODs": [], "controllers": []},
        "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": False,"volumeAttachments": []},
        "managementProcessor": { "reapplyState": None, "manageMp": True,
                                 "mpSettings": [
                                     {"settingType": "LocalAccounts",
                                      "args": {"localAccounts" : [
                                                   {
                                                        "userName": "test",
                                                        "displayName": "test",
                                                        "password": "MySecurePassword7",
                                                        "hostBIOSConfigPriv": False,
                                                        "hostNICConfigPriv": False,
                                                        "hostStorageConfigPriv": False,
                                                        "loginPriv": True,
                                                        "remoteConsolePriv": True,
                                                        "systemRecoveryConfigPriv": False,
                                                        "userConfigPriv": False,
                                                        "virtualMediaPriv": True,
                                                        "virtualPowerAndResetPriv": True,
                                                        "iLOConfigPriv": False,
                                                    },
                                                ]},
                                     },
                                 ]},
        }
    :param ilo:
    :param username:
    :param password:
    """
    if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
        BuiltIn().log('Checking mpsettings local accounts for profile %s' % profile['name'], console=True)
        if 'managementProcessor' in profile.keys():
            if 'mpSettings' in profile['managementProcessor'].keys():
                if isinstance(profile['managementProcessor']['mpSettings'], list) and len(profile['managementProcessor']['mpSettings']) != 0:
                    for item in profile['managementProcessor']['mpSettings']:
                        if item['settingType'] == 'LocalAccounts':
                            profile_user_accounts = item['args']
                            # remove the password in the profile user since Redfish doesn't return it
                            for profile_user in profile_user_accounts['localAccounts']:
                                profile_user.pop('password', 0)
                            ris_user_accounts = get_ris_local_user_accounts(ilo, username, password)
                            logger._debug("The profile user accounts: %s" % (profile_user_accounts))
                            logger._debug("The iLO user accounts: %s" % (ris_user_accounts))
                            verify = fusion_lib.fusion_api_validate_response_follow(profile_user_accounts, ris_user_accounts, wordy=True)
                            BuiltIn().should_be_equal(verify, True, msg=('Server profile mpsettings local accounts should match RIS for profile %s') % profile['name'])
                            BuiltIn().log('PASS: Server profile mpsettings local accounts should match RIS for profile %s' % profile['name'], console=True)
                else:
                    raise AssertionError("mpSettings in profile %s is an empty list" % profile['name'])
            else:
                raise AssertionError("mpSettings not defined in profile %s" % profile['name'])
        else:
            raise AssertionError("managementProcessor not defined in profile %s" % profile['name'])
    else:
        raise AssertionError("The argument profile %s is not profile DTO" % profile['name'])


def Massage_REST_For_RIS_Compare(rest):
    # used by "Server Hardware Local Storage Should Match RIS"
    # RIS used to be the Expected and REST the actual for Fusion Api Validate Response Follow
    # a 4.20 REST is a ~subset of the RIS thus easier to make REST the Expecte.
    #
    # Some data massage is still required
    #
    # These are "top" level items that won't be in the RIS
    remove = ["uri", "collectionState", "modified", "etag", "count", "name", "status_code", "headers"]
    for rm in remove:
        rest.pop(rm)

    # this is a simple key rename.  In REST it exists as 'DataDrives' but in RIS it is 'physicalDrives'
    for data in rest['data']:
        if 'LogicalDrives' in data:
            for LD in data['LogicalDrives']:
                LD['physicalDrives'] = LD.pop('DataDrives')

    return rest
