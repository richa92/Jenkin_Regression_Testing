"""
This is a common data file for C7000 UPT rings
"""
from enum import Enum
import re


class StorageSize(Enum):
    """
        StorageSize: The capacity of the volume in bytes
    """
    OneMB = 1048576
    FourMB = 4194304
    TenMB = 10485760
    OneGB = 1073741824
    TwoGB = 2147483648
    FiveGB = 5368709120
    TenGB = 10737418240
    ThirtyGB = 32212254720
    OneFortyTB = 17592186044416


# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
storage_credentials = {'username': 'fusionadm', 'password': 'hpvse1'}
support_dump = [{"errorCode": "CI", "encrypt": False}]
LE_support_dump = {"errorCode": "LE", "encrypt": True, "excludeApplianceDump": False}

# Resource types for X-API-Version=1000
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
ENCLOSURE_TYPE = 'EnclosureV7'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
INTERCONNECT_TYPE = 'InterconnectV4'
LOGICAL_ENCLOSURE_TYPE = 'LogicalEnclosureV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV6'
NETWORK_SET_TYPE = 'network-setV4'
SAN_MANAGER_TYPE = 'FCDeviceManagerV2'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_SYSTEM_TYPE = 'StorageSystemV5'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageVolumeTemplateV6'
STORAGE_VOLUME_TYPE = 'StorageVolumeV7'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_ROLE_TYPE = 'UserAndPermissions'

# Validation REGEX
REGEX_ENCLOSURE_MODEL = 'REGEX:BladeSystem c7000 Enclosure.*'
REGEX_ISCSI_INITIATOR_NAME = 'REGEX:iqn.*'
REGEX_VSA_STORAGE_PATH_TARGET_NAME = 'REGEX:iqn.2015-11.com.hpe:storevirtual.vsa84-mg'
REGEX_CHAP_SECRET = 'REGEX:.{16}'
REGEX_MCHAP_SECRET = REGEX_CHAP_SECRET

# Cleanup
hponcfg_clear_sso_1 = '''end_marker
<RIBCL VERSION="2.0">
<LOGIN USER_LOGIN="%s" PASSWORD="%s">
<SSO_INFO MODE="write">
<DELETE_SERVER INDEX="1" />
</SSO_INFO>
</LOGIN>
</RIBCL>
end_marker
''' % (ilo_credentials['username'], ilo_credentials['password'])

hponcfg_clear_sso_2 = '''end_marker
<RIBCL VERSION="2.0">
<LOGIN USER_LOGIN="%s" PASSWORD="%s">
<SSO_INFO MODE="write">
<DELETE_SERVER INDEX="2" />
</SSO_INFO>
</LOGIN>
</RIBCL>
end_marker
''' % (ilo_credentials['username'], ilo_credentials['password'])

hponcfg_clear_sso_3 = '''end_marker
<RIBCL VERSION="2.0">
<LOGIN USER_LOGIN="%s" PASSWORD="%s">
<SSO_INFO MODE="write">
<DELETE_SERVER INDEX="3" />
</SSO_INFO>
</LOGIN>
</RIBCL>
end_marker
''' % (ilo_credentials['username'], ilo_credentials['password'])

hponcfg_reset_ilo = '''end_marker
<RIBCL VERSION="2.0">
<LOGIN USER_LOGIN="%s" PASSWORD="%s">
<USER_INFO MODE="write">
<MOD_USER USER_LOGIN="%s">
<PASSWORD value="%s"/>
</MOD_USER>
</USER_INFO>
</LOGIN>
</RIBCL>
end_marker
''' % (ilo_credentials['username'], ilo_credentials['password'], ilo_credentials['username'], ilo_credentials['password'])

# FTS
timeandlocale = {'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'locale': 'en_US.UTF-8', 'timezone': 'UTC'}

# Licenses
licenses = [
    {'key': 'ABAG AQEA H9PQ 8HV2 V7B5 HWWB Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 DMF5 GRRM KJVT D5KM EFVW TSNJ XFU9 4ZSK E828 LFK6 FKA6 DU5N TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8UW BGB5 C324 SFUZ CMSB VNTJ ESB7 KVGR UNPC H4N5 NGHL 97D4 "EG3188881 KEY-E5Y35A#FUSION HP_OV_3yr_24x7_Supp_Phys_Flex_Lic ED4UATGCG2A9"_3JMZZ-RB9CN-DQD7H-CPB8P-M7WW2'},
    {'key': 'QCLG C9MA H9PQ 8HUZ U7B5 HWW5 Y9JL KMPL KRWA NBZY DXAU 2CSM GHTG L762 DNV7 GQFQ KJVT D5KM EFVW DT5J LFM8 76S8 C8SN YGSG Y8JC QUXV XZKH ABB4 NV2C LHXU VLXL HFMP J8TG 2VEB LK4U R6UF S7QS TRRL GX96 CMH4 6MPA M8LC KZU7 WE4X YN9X CDNB NT35 GH9J JGTJ QCV6 3EJF N975 "OV_NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR EY67ATGDTH6C"'},
]


remotesupport_edit = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                      {'op': 'replace', 'path': '/configuration/companyName', 'value': 'HPE'},
                      {'op': 'replace', 'path': '/configuration/marketingOptIn', 'value': True},
                      {"op": "replace", "path": "/configuration/autoEnableDevices", "value": True},
                      {'op': 'add', 'path': '/sites/default',
                       'value': {'name': 'DEFAULT SITE', 'streetAddress1': 'Compaq Center Dr', 'streetAddress2': '', 'city': 'Houston', 'provinceState': 'TX',
                                 'postalCode': '', 'timeZone': 'US/Central', 'countryCode': 'US', 'type': 'Site', 'default': True}},
                      {'op': 'add', 'path': '/contacts',
                       'value': {'contactKey': 'default', 'firstName': 'FFF', 'lastName': 'LLL', 'email': 'fff.ll@hpe.com', 'primaryPhone': '8884442222',
                                 'alternatePhone': '', 'notes': '', 'language': 'en', 'default': True, 'type': 'Contact'}}]


remotesupport_enable = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                        {"op": "replace", "path": "/configuration/autoEnableDevices", "value": True}]


# Users
def build_user(user_attributes):
    """
    :param user_attributes:
    :return:
    """
    return {
        'emailAddress': user_attributes['name'] + '@hpe.com',
        'mobilePhone': '',
        'officePhone': '',
        'password': admin_credentials['password'],
        'permissions': [{'roleName': user_attributes['roleName'], 'scopeUri': None}],
        'type': USER_AND_ROLE_TYPE,
        'userName': user_attributes['name'],
    }


def build_expected_user(user):
    """
    Build expected user
    :param user:
    """
    rtn = user.copy()
    rtn.update({
        'category': 'users',
        'enabled': True,
        'uri': '/rest/users/' + user['userName']})
    return rtn


users_attributes = [
    {'name': 'appliance', 'roleName': 'Infrastructure administrator'},
    {'name': 'network', 'roleName': 'Network administrator'},
    {'name': 'readonly', 'roleName': 'Read only'},
    {'name': 'server', 'roleName': 'Server administrator'},
    {'name': 'storage', 'roleName': 'Storage administrator'},
]
users = map(build_user, users_attributes)
expected_users = map(build_expected_user, users)


# San Managers and FC SANs
def build_san_manager(san_manager_attributes):
    """
    :param user_attributes:
    :return:
    """
    return {
        'connectionInfo': [
            {'name': 'Type', 'value': san_manager_attributes['type']},
            {'name': 'Host', 'value': san_manager_attributes['host']},
            {'name': 'Port', 'value': 5989},
            {'name': 'Username', 'value': 'Administrator'},
            {'name': 'Password', 'value': 'password'},
            {'name': 'UseSsl', 'value': True}]
    }


def build_expected_san_manager(san_manager_attributes):
    """
    Build expected san manager
    :param san_mamager_attributes:
    """
    return {
        'name': san_manager_attributes['host'],
        'category': 'fc-device-managers',
        'deviceManagerVersion': san_manager_attributes['deviceManagerVersion'],
        'providerDisplayName': san_manager_attributes['type'],
        'type': SAN_MANAGER_TYPE,
        'uri': 'SAN:' + san_manager_attributes['host']
    }


san_managers_attributes = [
    {'host': '16.125.66.46', 'deviceManagerVersion': '14.0.2.24', 'type': 'Brocade Network Advisor'}
]
fc_sans_attributes = [
    {'name': 'wpstsan18-FID100-10:00:50:eb:1a:00:21:fe'},
    {'name': 'wpstsan18-FID101-10:00:50:eb:1a:00:21:ff'},
]
san_managers = map(build_san_manager, san_managers_attributes)
expected_san_managers = map(build_expected_san_manager, san_managers_attributes)


# Ethernet networks
def build_ethernet_network(ethernet_network_attributes):
    """
    Build ethernet network
    :param ethernet_network_attributes:
    """
    return {
        'name': ethernet_network_attributes['name'],
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged',
        'privateNetwork': False,
        'purpose': 'General',
        'smartLink': False,
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': ethernet_network_attributes['vlan'],
    }


def build_expected_ethernet_network(ethernet_network):
    """
    Build expected ethernet network
    :param ethernet_network:
    """
    rtn = ethernet_network.copy()
    rtn.pop('connectionTemplateUri', 0)
    rtn.update(
        {'category': 'ethernet-networks',
         'uri': 'ETH:' + ethernet_network['name']})
    return rtn


ethernet_networks_attributes = [
    {'name': 'net293', 'vlan': '293'},
    {'name': 'net300', 'vlan': '300'},
]

ethernet_networks = map(build_ethernet_network, ethernet_networks_attributes)

expected_ethernet_networks = map(build_expected_ethernet_network, ethernet_networks)


# FC networks
def build_fc_network(fc_network_attributes):
    """
    Build fc network
    :param fc_network_attributes:
    """
    return {
        'name': fc_network_attributes['name'],
        'type': FC_NETWORK_TYPE,
        'autoLoginRedistribution': True,
        'connectionTemplateUri': None,
        'fabricType': 'FabricAttach',
        'linkStabilityTime': '30',
        'managedSanUri': 'FCSan:' + fc_network_attributes['fc_san'],
    }


def build_expected_fc_network(fc_network):
    """
    Build expected fc network
    :param fc_network:
    """
    rtn = fc_network.copy()
    rtn.pop('connectionTemplateUri', 0)
    rtn.update(
        {'category': 'fc-networks',
         'uri': 'FC:' + fc_network['name']})
    return rtn


fc_networks_attributes = [
    {'name': 'FC_A', 'fc_san': fc_sans_attributes[0]['name']},
    {'name': 'FC_B', 'fc_san': fc_sans_attributes[1]['name']},
]

fc_networks = map(build_fc_network, fc_networks_attributes)

expected_fc_networks = map(build_expected_fc_network, fc_networks)


# Uplinkset
def build_uplinkset(us_attributes):
    """
    Build uplinkset
    :param us_attributes:
    """
    return {
        'name': us_attributes['name'],
        'ethernetNetworkType': us_attributes['ethernetNetworkType'],
        'mode': 'Auto',
        'logicalPortConfigInfos': us_attributes['logicalPortConfigInfos'],
        'networkType': us_attributes['networkType'],
        'networkUris': us_attributes['networkUris'],
    }


uplinksets_attributes = [
    {'name': 'US_' + fc_networks_attributes[0]['name'],
     'ethernetNetworkType': None,
     'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'}],
     'networkType': 'FibreChannel',
     'networkUris': [fc_networks_attributes[0]['name']]},
    {'name': 'US_' + fc_networks_attributes[1]['name'],
     'ethernetNetworkType': None,
     'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'}],
     'networkType': 'FibreChannel',
     'networkUris': [fc_networks_attributes[1]['name']]},
    {'name': 'US_ETHERNET',
     'ethernetNetworkType': 'Tagged',
     'logicalPortConfigInfos': [{'bay': '1', 'port': 'X6', 'speed': 'Auto'}, {'bay': '2', 'port': 'X6', 'speed': 'Auto'}],
     'networkType': 'Ethernet',
     'networkUris': map(lambda d: d['name'], ethernet_networks_attributes)},
]

uplinksets = map(build_uplinkset, uplinksets_attributes)


# LIG
def build_lig(lig_attributes):
    """
    Build LIG
    :param lig_attributes:
    """
    return {
        'name': lig_attributes['name'],
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'C7000',
        'interconnectMapTemplate': lig_attributes['interconnectMapTemplate'],
        'uplinkSets': uplinksets,
    }


def build_expected_lig(lig):
    """
    Build expected LIG
    :param lig:
    """
    rtn = lig.copy()
    rtn.pop('interconnectMapTemplate', 0)
    rtn.pop('uplinkSets', 0)
    rtn.update({
        "category": "logical-interconnect-groups",
        "uri": "LIG:" + lig['name'],
    })
    return rtn


configuration_script = '''
#Set Login Banner Text Information
CLEAR LOGIN_BANNER_TEXT
DISABLE LOGIN_BANNER
'''


# EG
def build_enclosure_group(eg_attributes):
    """
    Build enclosure group
    :param eg_attributes:
    """
    return {
        'name': eg_attributes['name'],
        'configurationScript': configuration_script,
        'interconnectBayMappings': eg_attributes['interconnectBayMappings'],
    }


def build_expected_enclosure_group(enclosure_group):
    """
    Build expected enclosure group
    :param enclosure_group:
    """
    rtn = enclosure_group.copy()
    rtn.pop('configurationScript', 0)
    rtn.pop('interconnectBayMappings', 0)
    rtn.update(
        {'category': 'enclosure-groups',
         'ipAddressingMode': 'External',
         'portMappingCount': 8,
         'uri': 'EG:' + enclosure_group['name']}
    )
    return rtn


# Enclosure
def build_enclosure(enc_attributes):
    """
    Build enclosure
    :param enc_attributes: enclosure attributes
    """
    return {
        'name': enc_attributes['name'],
        'enclosureGroupUri': 'EG:' + enc_attributes['eg'],
        'force': True,
        'forceInstallFirmware': False,
        'firmwareBaselineUri': None,
        'hostname': enc_attributes['hostname'],
        'licensingIntent': 'OneViewNoiLO',
        'password': oa_credentials['password'],
        'updateFirmwareOn': None,
        'username': oa_credentials['username'],
    }


def build_expected_enclosure(enc_attributes):
    """
    Build expected enclosure
    :param enc_attributes: enclosure attributes
    """
    return {
        'name': enc_attributes['name'],
        'type': ENCLOSURE_TYPE,
        'enclosureGroupUri': 'EG:' + enc_attributes['eg'],
        'enclosureTypeUri': '/rest/enclosure-types/c7000',
        'enclosureModel': REGEX_ENCLOSURE_MODEL,
        'enclosureType': 'C7000',
        'enclosureTypeUri': '/rest/enclosure-types/c7000',
        'deviceBayCount': 16,
        'interconnectBayCount': 8,
        'licensingIntent': 'OneViewNoiLO',
        'logicalEnclosureUri': 'LE:' + enc_attributes['name'],
        'oaBays': 2,
        'uri': 'ENC:' + enc_attributes['name'],
    }


# StRM
def build_storeserv_system(ss_attributes):
    """
    Build StoreServ
    :param ss_attributes:
    """
    return {
        'name': ss_attributes['name'],
        'type': STORAGE_SYSTEM_TYPE,
        'credentials': {'username': 'fusionadm', 'password': 'hpvse1'},
        'family': 'StoreServ',
        'hostname': ss_attributes['hostname'],
        'deviceSpecificAttributes': {
            'managedDomain': ss_attributes['managedDomain'],
            'discoveredDomains': ss_attributes['discoveredDomains'],
        },
    }


def build_storevirtual_system(sv_attributes):
    """
    Build StoreVirtual
    :param sv_attributes:
    """
    return {
        'name': sv_attributes['name'],
        'type': STORAGE_SYSTEM_TYPE,
        'credentials': {'username': 'admin', 'password': 'admin'},
        'family': 'StoreVirtual',
        'hostname': sv_attributes['hostname'],
        'ports': [{
            'name': sv_attributes['vip'],
            'expectedNetworkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
            'expectedNetworkName': ethernet_networks_attributes[0]['name'],
            'mode': 'Managed'}],
    }


def build_expected_storage_system(ss):
    """
    Build expected storage system
    :param ss: storage system
    """
    rtn = ss.copy()
    rtn.update({
        'category': 'storage-systems',
        'uri': 'SSYS' + ss['name']
    })


storeserv_systems_attributes = [
    {
        'name': 'wpst3par-7200-11-srv',
        'hostname': 'wpst3par-7200-11-srv.vse.rdlabs.hpecorp.net',
        'managedDomain': 'UPT',
        'discoveredDomains': ['NODOMAIN', 'lifecycle'],
        'managed_ports':[
            {'name': '0:2:3', 'wwn': '20:23:00:02:AC:00:C4:A5', 'wwn_no_colon': '20:23:00:02:AC:00:C4:A5'.replace(':', '')},
            {'name': '1:2:3', 'wwn': '21:23:00:02:AC:00:C4:A5', 'wwn_no_colon': '21:23:00:02:AC:00:C4:A5'.replace(':', '')},
            {'name': '0:2:4', 'wwn': '20:24:00:02:AC:00:C4:A5', 'wwn_no_colon': '20:24:00:02:AC:00:C4:A5'.replace(':', '')},
            {'name': '1:2:4', 'wwn': '21:24:00:02:AC:00:C4:A5', 'wwn_no_colon': '21:24:00:02:AC:00:C4:A5'.replace(':', '')},
        ],
        'serialNumber': '1650341',
        'storage_pools': [
            'UPT_r1',
            'UPT_r5',
            'UPT_r6'],
    },
]

storevirtual_systems_attributes = [
    {
        'name': 'VSA84_Storage_Pool',
        'hostname': '16.71.151.84',
        'vip': '16.71.151.84',
        'storage_pool': 'VSA84_Storage_Pool',
    },
]


storeserv_systems = map(build_storeserv_system, storeserv_systems_attributes)
storevirtual_systems = map(build_storevirtual_system, storevirtual_systems_attributes)
storage_systems = storeserv_systems + storevirtual_systems
expected_storage_systems = map(build_expected_storage_system, storage_systems)


def build_storeserv_pool(name, ss_name=storeserv_systems_attributes[0]['name']):
    """
    Build StoreServ storage pool
    :param name: storage pool name
    :param ss_name: storage system name
    """
    return {
        'name': name,
        'isManaged': True,
        'storageSystemUri': ss_name,

    }


def build_expected_storage_pool(sp):
    """
    Build expected storage pool
    :param sp: storage pool
    """
    return {
        'name': sp['name'],
        'isManaged': True,
    }


storeserv_pools = map(build_storeserv_pool, storeserv_systems_attributes[0]['storage_pools'])
storage_pools = storeserv_pools
expected_storage_pools = map(build_expected_storage_pool, storage_pools)


def build_storeserv_svt(svt_attributes):
    """
    Build StoreServ SVT
    :param svt_attributes:
    """
    return {
        'name': svt_attributes['name'],
        'description': '',
        'properties': {
            'name': {'title': 'Volume name', 'description': 'A volume name between 1 and 100 characters',
                     'type': 'string', 'minLength': 1, 'maxLength': 100, 'required': True,
                     'meta': {'locked': False}},
            'description': {'title': 'Description', 'description': 'A description for the volume',
                            'type': 'string', 'minLength': 0, 'maxLength': 2000, 'default': '',
                            'meta': {'locked': False}},
            'isShareable': {'title': 'Is Shareable', 'description': 'The shareability of the volume',
                            'type': 'boolean', 'meta': {'locked': False}, 'default': False},
            'provisioningType': {'title': 'Provisioning Type', 'description': 'The provisioning type for the volume',
                                 'type': 'string', 'enum': ['Thin', 'Full'], 'meta': {'locked': True, 'createOnly': True}, 'default': 'Thin'},
            'size': {'title': 'Capacity', 'description': 'The capacity of the volume in bytes',
                     'type': 'integer', 'required': True, 'minimum': StorageSize.OneGB.value, 'maximum': StorageSize.OneFortyTB.value,
                     'meta': {'locked': False, 'semanticType': 'capacity'}, 'default': StorageSize.FiveGB.value},
            'snapshotPool': {'title': 'Snapshot Pool', 'description': 'A URI reference to the common provisioning group used to create snapshots',
                             'type': 'string', 'format': 'x-uri-reference', 'meta': {'locked': True, 'semanticType': 'device-snapshot-storage-pool'},
                             'default': svt_attributes['snapshotPool']},
            'storagePool': {'title': 'Storage Pool', 'description': 'A common provisioning group URI reference',
                            'type': 'string', 'required': True, 'format': 'x-uri-reference',
                            'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'},
                            'default': svt_attributes['storagePool']},
        },
        'rootTemplateUri': svt_attributes['rootTemplateUri']}


def build_storevirtual_svt(svt_attributes):
    """
    Build StoreVirtual SVT
    :param svt_attributes:
    """
    return {
        'name': svt_attributes['name'],
        'description': '',
        'properties': {
            'name': {'title': 'Volume name', 'description': 'A volume name between 1 and 100 characters',
                     'type': 'string', 'minLength': 1, 'maxLength': 100, 'required': True, 'meta': {'locked': False}},
            'description': {'title': 'Description', 'description': 'A description for the volume',
                            'type': 'string', 'minLength': 0, 'maxLength': 2000, 'default': 'VSA RAID0 private', 'meta': {'locked': False}},
            'storagePool': {'title': 'Storage Pool', 'description': 'StoragePoolURI the volume should be added to',
                            'type': 'string', 'format': 'x-uri-reference', 'required': True,
                            'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'}, 'default': svt_attributes['storagePool']},
            'size': {'title': 'Capacity', 'description': 'Capacity of the volume in bytes',
                     'type': 'integer', 'minimum': StorageSize.FourMB.value, 'required': True, 'default': StorageSize.OneGB.value,
                     'meta': {'locked': False, 'semanticType': 'capacity'}},
            'dataProtectionLevel': {'title': 'Data Protection Level', 'description': 'Indicates the number and configuration of data copies in the Storage Pool',
                                    'type': 'string', 'enum': ['NetworkRaid0None', 'NetworkRaid5SingleParity', 'NetworkRaid10Mirror2Way', 'NetworkRaid10Mirror3Way', 'NetworkRaid10Mirror4Way', 'NetworkRaid6DualParity'],
                                    'default': 'NetworkRaid0None', 'required': True, 'meta': {'locked': True, 'semanticType': 'device-dataProtectionLevel'}},
            'provisioningType': {'title': 'Provisioning Type', 'description': 'The provisioning type for the volume',
                                 'type': 'string', 'enum': ['Thin', 'Full'], 'default': 'Thin',
                                 'meta': {'locked': True, 'createOnly': 'True', 'semanticType': 'device-provisioningType'}},
            'isAdaptiveOptimizationEnabled': {'title': 'Adaptive Optimization', 'description': '',
                                              'type': 'boolean', 'default': True, 'meta': {'locked': True}},
            'isShareable': {'title': 'Is Shareable', 'description': 'The shareability of the volume',
                            'type': 'boolean', 'default': False, 'meta': {'locked': False}},
        },
        'rootTemplateUri': svt_attributes['rootTemplateUri'],
    }


def build_expected_svt(svt, family='StoreServ'):
    """
    Build expected SVT
    :param svt:
    """
    rtn = svt.copy()
    rtn.update({
        'isRoot': False,
        'family': family,
    })
    return rtn


storeserv_svts_attributes = [
    {
        'name': 'STORESERV_POOL1_PRIV_THIN',
        'snapshotPool': storeserv_pools[0]['name'],
        'storagePool': storeserv_pools[0]['name'],
        'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
    },
]

storevirtual_svts_attributes = [
    {
        'name': 'STOREVIRTUAL_PRIV_THIN',
        'storagePool': storevirtual_systems_attributes[0]['storage_pool'],
        'rootTemplateUri': 'Volume root template for StoreVirtual 1.2',
    },
]

storeserv_svts = map(build_storeserv_svt, storeserv_svts_attributes)
storevirtual_svts = map(build_storevirtual_svt, storevirtual_svts_attributes)
storage_volume_templates = storeserv_svts + storevirtual_svts
expected_storage_volume_templates = map(build_expected_svt, storage_volume_templates)


def build_storeserv_volume(name,
                           sp_name=storeserv_svts_attributes[0]['storagePool'],
                           templateUri=storeserv_svts_attributes[0]['name']):
    """
    This function builds the storeserv volume with the below parameters:
    [Required Parameters] "name", "size", "snapshotPool", "storagePool", "templateUri"
    """
    return {
        'properties': {
            'name': name,
            'description': '',
            'isShareable': False,
            'provisioningType': 'Thin',
            'size': StorageSize.ThirtyGB.value,
            'snapshotPool': sp_name,
            'storagePool': sp_name},
        'templateUri': templateUri,
        'isPermanent': True,
    }


def build_storevirtual_volume(name,
                              sp_name=storevirtual_svts_attributes[0]['storagePool'],
                              templateUri=storevirtual_svts_attributes[0]['name']):
    """
    This function builds storevirtual volume with the below parameters:
    [Required Parameters] "name", "size", "storagepool", "templateUri"
    """
    return {
        'properties': {
            'name': name,
            'dataProtectionLevel': 'NetworkRaid0None',
            'description': '',
            'isAdaptiveOptimizationEnabled': True,
            'isShareable': False,
            'provisioningType': 'Thin',
            'size': StorageSize.FiveGB.value,
            'storagePool': sp_name},
        'templateUri': templateUri,
        'isPermanent': True,
    }


def build_expected_storage_volume(sv):
    """
    Build expected storage volume
    :param sv: storage volume
    """
    return {'name': sv['properties']['name'],
            'category': 'storage-volumes',
            'isShareable': False,
            'isPermanent': True,
            'provisionedCapacity': sv['properties']['size'],
            'provisioningType': 'Thin',
            'storagePoolUri': 'SPOOL:' + sv['properties']['storagePool'],
            'type': STORAGE_VOLUME_TYPE,
            'volumeTemplateUri': 'SVT:' + sv['templateUri'],
            'uri': 'SVOL:' + sv['properties']['name']}


# Profiles
def build_profile_attributes(server_attributes):
    """
    Build profile attributes
    :param server_attributes:
    """
    label = server_attributes['name'].replace(' ', '').replace(',', '')
    return {
        'name': label + '_profile',
        'eg': server_attributes['eg'],
        'enc': server_attributes['name'].split(',')[0],
        'enc_bay': re.sub(r'.*bay(\d*)', r'\1', label),
        'sh': server_attributes['name'],
        'sht': 'SH:' + server_attributes['name'],
        'volumes': [label + '_priv_vol1', label + '_priv_vol2']
    }


# Group1 Gen8 with bootable FC connection and bootVolumeSource=UserDefined
def build_group1_profile(profile_attributes):
    """
    Build profile
    :param profile_attributes:
    """
    return {
        'name': profile_attributes['name'], 'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + profile_attributes['sh'], 'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:' + profile_attributes['eg'],
        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'affinity': 'Bay',
        'iscsiInitiatorNameType': 'AutoGenerated', 'iscsiInitiatorName': '',
        'hideUnusedFlexNics': True, 'bios': {'manageBios': False, 'overriddenSettings': []},
        'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE']},
        'bootMode': None,
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][0]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][2]['wwn_no_colon'], 'lun': '1'}]}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], "bootVolumePriority": 'NotBootable', 'lunType': 'Manual', 'lun': 1,
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]},
                {'id': 2, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], "bootVolumePriority": 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
            ]
        }
    }


def build_expected_group1_profile(profile_attributes):
    """
    Build expected profile
    :param profile_attributes:
    """
    return {
        'name': profile_attributes['name'], 'type': SERVER_PROFILE_TYPE, 'uri': 'SP:' + profile_attributes['name'],
        'serverHardwareUri': 'SH:' + profile_attributes['sh'], 'serverHardwareTypeUri': 'SHT:' + profile_attributes['sht'],
        'enclosureGroupUri': 'EG:' + profile_attributes['eg'], 'enclosureUri': 'ENC:' + profile_attributes['enc'],
        'enclosureBay': profile_attributes['enc_bay'], 'affinity': 'Bay', 'associatedServer': None,
        'macType': 'Physical', 'wwnType': 'Physical', 'serialNumberType': 'Physical',
        'iscsiInitiatorNameType': 'AutoGenerated', 'iscsiInitiatorName': REGEX_ISCSI_INITIATOR_NAME,
        'hideUnusedFlexNics': True, 'bios': {'overriddenSettings': [], 'manageBios': False},
        'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'Floppy', 'USB', 'PXE']},
        'bootMode': None,
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][0]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][2]['wwn_no_colon'], 'lun': '1'}]}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], "bootVolumePriority": 'NotBootable', 'lunType': 'Manual', 'lun': 1, 'state': 'Attached',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][0]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][1]['wwn']}]},
                     {'targetSelector': 'Auto', 'connectionId': 4, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][2]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][3]['wwn']}]}]
                 },
                {'id': 2, 'state': 'Attached', 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], "bootVolumePriority": 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]},
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]}]
                 },
            ],
            'sanSystemCredentials': [
                {
                    'chapSecret': REGEX_CHAP_SECRET,
                    'chapLevel': 'MutualChap',
                    'chapSource': 'AutoGenerated',
                    'chapName': REGEX_ISCSI_INITIATOR_NAME,
                    'mutualChapName': REGEX_ISCSI_INITIATOR_NAME,
                    'mutualChapSecret': REGEX_MCHAP_SECRET,
                    'storageSystemUri': 'REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}'
                },
            ],
        }
    }


# Group2 Gen9 with bootable FC connection and bootVolumeSource=ManagedVolume
def build_group2_profile(profile_attributes):
    """
    Build profile
    :param profile_attributes:
    """
    return {
        'name': profile_attributes['name'], 'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + profile_attributes['sh'], 'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:' + profile_attributes['eg'],
        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'affinity': 'Bay',
        'iscsiInitiatorNameType': 'AutoGenerated', 'iscsiInitiatorName': '',
        'hideUnusedFlexNics': True, 'bios': {'manageBios': False, 'overriddenSettings': []},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}
             }
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], "bootVolumePriority": "Primary", 'lunType': 'Manual', 'lun': 1, 'state': 'Attached',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True, 'targets': []},
                     {'targetSelector': 'Auto', 'connectionId': 4, 'isEnabled': True, 'targets': []}]
                 },
                {'id': 2, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], "bootVolumePriority": 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
            ]
        }
    }


def build_expected_group2_profile(profile_attributes):
    """
    Build expected profile
    :param profile_attributes:
    """
    return {
        'name': profile_attributes['name'], 'type': SERVER_PROFILE_TYPE, 'uri': 'SP:' + profile_attributes['name'],
        'serverHardwareUri': 'SH:' + profile_attributes['sh'], 'serverHardwareTypeUri': 'SHT:' + profile_attributes['sht'],
        'enclosureGroupUri': 'EG:' + profile_attributes['eg'], 'enclosureUri': 'ENC:' + profile_attributes['enc'],
        'enclosureBay': profile_attributes['enc_bay'], 'affinity': 'Bay', 'associatedServer': None,
        'macType': 'Physical', 'wwnType': 'Physical', 'serialNumberType': 'Physical',
        'iscsiInitiatorNameType': 'AutoGenerated', 'iscsiInitiatorName': REGEX_ISCSI_INITIATOR_NAME,
        'hideUnusedFlexNics': True, 'bios': {'overriddenSettings': [], 'manageBios': False},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}
             }
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], "bootVolumePriority": "Primary", 'lunType': 'Manual', 'lun': 1, 'state': 'Attached', 'lunType': 'Manual',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][0]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][1]['wwn']}]},
                     {'targetSelector': 'Auto', 'connectionId': 4, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][2]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][3]['wwn']}]}]
                 },
                {'id': 2, 'state': 'Attached', 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], "bootVolumePriority": 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]},
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]}]
                 },
            ],
            'sanSystemCredentials': [
                {
                    'chapSecret': REGEX_CHAP_SECRET,
                    'chapLevel': 'MutualChap',
                    'chapSource': 'AutoGenerated',
                    'chapName': REGEX_ISCSI_INITIATOR_NAME,
                    'mutualChapName': REGEX_ISCSI_INITIATOR_NAME,
                    'mutualChapSecret': REGEX_MCHAP_SECRET,
                    'storageSystemUri': 'REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}'
                },
            ],
        }
    }


# Group3 Gen10 Profiles
def build_group3_profile(profile_attributes):
    """
    Build profile
    :param profile_attributes:
    """
    return {
        'name': profile_attributes['name'], 'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + profile_attributes['sh'], 'serverHardwareTypeUri': '',
        'enclosureGroupUri': 'EG:' + profile_attributes['eg'],
        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'affinity': 'Bay',
        'iscsiInitiatorNameType': 'AutoGenerated', 'iscsiInitiatorName': '',
        'hideUnusedFlexNics': True, 'bios': {'manageBios': False, 'overriddenSettings': []},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], "bootVolumePriority": "Primary", 'lunType': 'Manual', 'lun': 1, 'state': 'Attached',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True, 'targets': []},
                     {'targetSelector': 'Auto', 'connectionId': 4, 'isEnabled': True, 'targets': []}]
                 },
                {'id': 2, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], "bootVolumePriority": 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
            ]
        },
    }


def build_expected_group3_profile(profile_attributes):
    """
    Build expected profile
    :param profile_attributes:
    """
    return {
        'name': profile_attributes['name'], 'type': SERVER_PROFILE_TYPE, 'uri': 'SP:' + profile_attributes['name'],
        'serverHardwareUri': 'SH:' + profile_attributes['sh'], 'serverHardwareTypeUri': 'SHT:' + profile_attributes['sht'],
        'enclosureGroupUri': 'EG:' + profile_attributes['eg'], 'enclosureUri': 'ENC:' + profile_attributes['enc'],
        'enclosureBay': profile_attributes['enc_bay'], 'affinity': 'Bay', 'associatedServer': None,
        'macType': 'Physical', 'wwnType': 'Physical', 'serialNumberType': 'Physical',
        'iscsiInitiatorNameType': 'AutoGenerated', 'iscsiInitiatorName': REGEX_ISCSI_INITIATOR_NAME,
        'hideUnusedFlexNics': True, 'bios': {'overriddenSettings': [], 'manageBios': False},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], "bootVolumePriority": "Primary", 'lunType': 'Manual', 'lun': 1, 'state': 'Attached', 'lunType': 'Manual',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][0]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][1]['wwn']}]},
                     {'targetSelector': 'Auto', 'connectionId': 4, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][2]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][3]['wwn']}]}]
                 },
                {'id': 2, 'state': 'Attached', 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], "bootVolumePriority": 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]},
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]}]
                 },
            ],
            'sanSystemCredentials': [
                {
                    'chapSecret': REGEX_CHAP_SECRET,
                    'chapLevel': 'MutualChap',
                    'chapSource': 'AutoGenerated',
                    'chapName': REGEX_ISCSI_INITIATOR_NAME,
                    'mutualChapName': REGEX_ISCSI_INITIATOR_NAME,
                    'mutualChapSecret': REGEX_MCHAP_SECRET,
                    'storageSystemUri': 'REGEX:/rest/storage-systems/\w{8}(-\w{4}){3}-\w{12}'
                },
            ],
        },
    }
