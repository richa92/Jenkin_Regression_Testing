from datetime import datetime, timedelta
iso = datetime.strftime(datetime.now() + timedelta(minutes=35), '%Y-%m-%dT%H:%M:%S.000Z')
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['172.20.0.25'], 'locale': 'en_US.UTF-8'}

admin_credentials = {
    'userName': 'Administrator',
    'password': 'hpvse123'
}


spp = "SPPGen10Snap4_2018_0628_5"
firmwarebundle1 = "C:\\SPP\\SPP2018060.2018_0618.64.iso"
firmwarebundle1_check = "SPP2018060_2018_0618_64"

gen10_server = 'SH:Encl1, bay 3'
gen10_sp_name = 'SP_Gen10'


gen9_server = 'SH:Encl1, bay 12'
gen9_sp_name = 'SP_Gen9'
profile_type = 'ServerProfileV10'
new_name = 'new_sp'


web_url = 'http://webdav.vse.rdlabs.hpecorp.net/webdav/Internal/'
web_url_hotfix = 'http://webdav.vse.rdlabs.hpecorp.net/webdav/Internal/Hotfix'
webdav_username = 'tester'
webdav_password = 'tester'

http_repo_with_password = {
    'repositoryName': 'external',
    'repositoryURI': 'http://webdav.vse.rdlabs.hpecorp.net/webdav/',
    'userName': 'tester',
    'password': 'tester',
    'base64Data': ""
}


server_profiles_force = [
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR  ENCL1, BAY4',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnlyOfflineMode',
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_online',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareActivationType': 'Immediate'
            #    'manageFirmware': True,
            #    'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            #    'forceInstallFirmware': True,
            #    'firmwareInstallType': 'FirmwareAndOSDrivers',
            #    'firmwareScheduleDateTime': iso,
            #    'firmwareActivationType': 'Scheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'Scheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'NotScheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'Scheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'NotScheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },

]

server_profiles_edit_force = [
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR  ENCL1, BAY3',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnlyOfflineMode',
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_online_edit',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'Scheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'NotScheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'Immediate'
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'Scheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'NotScheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },

]


server_profiles_no_force = [
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR  ENCL1, BAY3',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': False,
            'firmwareInstallType': 'FirmwareOnlyOfflineMode',
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': False,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen10_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen10_sp_name,
        'description': 'SP FOR ENC1-BAY3',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': False,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },


]


server_profiles_gen9_force = [
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR  ENCL1, BAY1',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnlyOfflineMode',
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'Scheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'NotScheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareScheduleDateTime': iso,
            'firmwareActivationType': 'Scheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1_fw_only-using_sut',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': True,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'NotScheduled'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },

]


server_profiles_gen9_no_force = [
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR  ENCL1, BAY1',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': False,
            'firmwareInstallType': 'FirmwareOnlyOfflineMode',
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1',
        'affinity': 'Bay',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': False,
            'firmwareInstallType': 'FirmwareAndOSDrivers',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },
    {
        'type': profile_type,
        'serverHardwareUri': gen9_server,
        'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': gen9_sp_name,
        'description': 'SP FOR ENC1-BAY1',
        "eTag": "",
        'firmware': {
            'manageFirmware': True,
            'firmwareBaselineUri': "/rest/firmware-drivers/{}".format(spp),
            'forceInstallFirmware': False,
            'firmwareInstallType': 'FirmwareOnly',
            'firmwareActivationType': 'Immediate'
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
    },


]

ligHA = {"type": "logical-interconnect-groupV6",
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
         "description": None,
         "name": "lig_1_Encl_2_potash",
         "interconnectMapTemplate":
         {"interconnectMapEntryTemplates": [
             {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
             {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1}]},
         "enclosureType": "SY12000",
         "enclosureIndexes": [1],
         "interconnectBaySet": "3",
         "redundancyType": "Redundant",
         "internalNetworkUris": [],
         "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
         "qosConfiguration": None,
         "uplinkSets": []
         }


sas_ligs = [{'name': 'LIG_Natasha',
             'type': 'sas-logical-interconnect-groupV2',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': [
                 {'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                 {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1}],
             'interconnectBaySet': 1,
             'enclosureIndexes': [1]}]


lig_new = [{'name': 'LIG',
            'type': 'logical-interconnect-groupV4',
            'enclosureType': 'C7000',
            'interconnectMapTemplate': [  # {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
            ],
            'uplinkSets': [
                # uplinkSetBs3['us1_netset1'].copy(),
                # uplinkSetBs3['us2_fc1'].copy(),
                # uplinkSetBs3['us3_fc2'].copy(),
                # uplinkSetBs3['us4_fcoe1'].copy(),
                # uplinkSetBs3['us5_fcoe2'].copy(),
            ],
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess':[], 'enabled':True, 'description':None, 'name':None, 'state':None, 'status':None, 'eTag':None, 'category':'snmp-configuration', 'uri':None},
            'qosConfiguration':None}, ]


enclosure_group = {'name': 'EG1', 'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
                    ],
                   "ipRangeUris": [],
                   "enclosureCount": 1,
                   "osDeploymentSettings": None,
                   "configurationScript": None,
                   "powerMode": None,
                   "ambientTemperatureMode": "Standard"}

encss = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:EG1', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}]
logical_enclosure = {
    'name': 'LE1',
    'enclosureUris': ['ENC:Enc1'],
    'enclosureGroupUri': 'EG:EG1',
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}

expected_logical_enclosure = {
    'type': 'LogicalEnclosureV5',
    'name': 'LE1',
    'status': 'OK',
    'enclosureUris': ['ENC:Enc1'],
    'enclosureGroupUri': 'EG:EG1'
}
