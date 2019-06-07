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
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
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
REGEX_ENCLOSURE_MODEL = 'REGEX:Synergy 12000 Frame.*'
REGEX_ISCSI_INITIATOR_NAME = 'REGEX:iqn.*'
REGEX_VSA_STORAGE_PATH_TARGET_NAME = 'REGEX:iqn.2015-11.com.hpe:storevirtual.vsa84-mg'
REGEX_CHAP_SECRET = 'REGEX:.{16}'
REGEX_MCHAP_SECRET = REGEX_CHAP_SECRET


# FTS
timeandlocale = {'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}


# Licenses
licenses = [
    {'key': 'ABAG AQEA H9PQ 8HV2 V7B5 HWWB Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 DMF5 GRRM KJVT D5KM EFVW TSNJ XFU9 4ZSK E828 LFK6 FKA6 DU5N TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8UW BGB5 C324 SFUZ CMSB VNTJ ESB7 KVGR UNPC H4N5 NGHL 97D4 "EG3188881 KEY-E5Y35A#FUSION HP_OV_3yr_24x7_Supp_Phys_Flex_Lic ED4UATGCG2A9"_3JMZZ-RB9CN-DQD7H-CPB8P-M7WW2'},
    {'key': 'QCLG C9MA H9PQ 8HUZ U7B5 HWW5 Y9JL KMPL KRWA NBZY DXAU 2CSM GHTG L762 DNV7 GQFQ KJVT D5KM EFVW DT5J LFM8 76S8 C8SN YGSG Y8JC QUXV XZKH ABB4 NV2C LHXU VLXL HFMP J8TG 2VEB LK4U R6UF S7QS TRRL GX96 CMH4 6MPA M8LC KZU7 WE4X YN9X CDNB NT35 GH9J JGTJ QCV6 3EJF N975 "OV_NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR EY67ATGDTH6C"'},
    {'key': 'QB9A DQEA H9PY 8HXY V2B4 HWWV Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 6S74 ERB4 KJVT D5KM EFVW TSNJ YF4J 86CS SMT9 YGS6 SMQQ MUCF UW2L MYN7 N2QC DHKQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TVPT 74UF NGGT EHM4 "EVAL-N3R43A_ILR N3R43A_ILR Synergy_8Gb_FC_Upgrade_License EVAL-N3R43A_ILR"'},
    {'key': 'YBYE CQEA H9PA CHXZ V2B4 HWWV Y9JL KMPL LJ2A PGVQ DXAU 2CSM GHTG L762 2ET7 FQV9 KJVT D5KM EFVW TSNJ K4UP 536G SMT9 YGS6 SMQQ MUCF 4WCN MYN7 N2QS LHJQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TX83 T45F NGG3 EHM4 "EVAL-N3R43A_NFR N3R43A_NFR Synergy_8Gb_FC_Upgrade_License_NFR EVAL-N3R43A_NFR"'}
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
    {'host': '16.114.217.129', 'deviceManagerVersion': '14.4.1.7', 'type': 'Brocade Network Advisor'}
]
fc_sans_attributes = [
    {'name': 'merlin-10:00:88:94:71:19:ea:27'},  # Side A
    {'name': 'merlin-10:00:88:94:71:19:ea:26'},  # Side B
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
    {'name': 'net283', 'vlan': '283'},
    {'name': 'net100', 'vlan': '100'},
    {'name': 'net101', 'vlan': '101'},
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
    {'name': 'FC_POTASH_A', 'fc_san': fc_sans_attributes[0]['name']},
    {'name': 'FC_POTASH_B', 'fc_san': fc_sans_attributes[1]['name']},
    {'name': 'FC_CARBON_A', 'fc_san': fc_sans_attributes[0]['name']},
    {'name': 'FC_CARBON_B', 'fc_san': fc_sans_attributes[1]['name']},
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
    {'name': 'US_' + fc_networks_attributes[0]['name'],  # Potash FC side A
     'ethernetNetworkType': None,
     'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'}],
     'networkType': 'FibreChannel',
     'networkUris': [fc_networks_attributes[0]['name']]},
    {'name': 'US_' + fc_networks_attributes[1]['name'],  # Potash FC side B
     'ethernetNetworkType': None,
     'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q4:1', 'speed': 'Auto'}],
     'networkType': 'FibreChannel',
     'networkUris': [fc_networks_attributes[1]['name']]},
    {'name': 'US_ETHERNET',  # Potash Tagged Ethernet
     'ethernetNetworkType': 'Tagged',
     'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'},
                                {'enclosure': '2', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'}],
     'networkType': 'Ethernet',
     'networkUris': map(lambda d: d['name'], ethernet_networks_attributes)},
    {'name': 'US_' + fc_networks_attributes[2]['name'],  # Carbon FC side A
     'ethernetNetworkType': None,
     'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '1', 'port': '1', 'speed': 'Auto'}],
     'networkType': 'FibreChannel',
     'networkUris': [fc_networks_attributes[2]['name']]},
    {'name': 'US_' + fc_networks_attributes[3]['name'],  # Carbon FC side B
     'ethernetNetworkType': None,
     'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '4', 'port': '1', 'speed': 'Auto'}],
     'networkType': 'FibreChannel',
     'networkUris': [fc_networks_attributes[3]['name']]},
]


uplinksets = map(build_uplinkset, uplinksets_attributes)


# LIG
def build_lig(lig_attributes):
    """
    Build expected LIG
    :param lig_attributes:
    """
    return {
        'name': lig_attributes['name'],
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureIndexes': lig_attributes['enclosureIndexes'],
        'enclosureType': 'SY12000',
        'interconnectBaySet': lig_attributes['interconnectBaySet'],
        'interconnectMapTemplate': lig_attributes['interconnectMapTemplate'],
        'redundancyType': lig_attributes['redundancyType'],
        'uplinkSets': lig_attributes['uplinkSets'],
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
        'category': 'logical-interconnect-groups',
        'uri': 'LIG:' + lig['name'],
    })
    return rtn


# SAS LIG
def build_sas_lig(sas_lig_attributes):
    """
    Build expected LIG
    :param sas_lig_attributes:
    """
    return {
        'name': sas_lig_attributes['name'],
        'type': SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureIndexes': sas_lig_attributes['enclosureIndexes'],
        'enclosureType': 'SY12000',
        'interconnectBaySet': sas_lig_attributes['interconnectBaySet'],
        'interconnectMapTemplate': sas_lig_attributes['interconnectMapTemplate'],
    }


def build_expected_sas_lig(sas_lig):
    """
    Build expected SAS LIG
    :param sas_lig:
    """
    rtn = sas_lig.copy()
    rtn.pop('interconnectMapTemplate', 0)
    rtn.update({
        'category': 'logical-interconnect-groups',
        'uri': 'SASLIG:' + sas_lig['name'],
    })
    return rtn


# EG
def build_enclosure_group(eg_attributes):
    """
    Build enclosure group
    :param eg_attributes:
    """
    return {
        'name': eg_attributes['name'],
        # 'type': ENCLOSURE_GROUP_TYPE,
        'configurationScript': '',
        'enclosureCount': eg_attributes['enclosureCount'],
        # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'ipAddressingMode': 'External',
        'interconnectBayMappings': eg_attributes['interconnectBayMappings'],
        # 'interconnectBayMappingCount': eg_attributes['interconnectBayMappingCount'],
        # 'stackingMode': 'Enclosure',
    }


def build_expected_enclosure_group(eg):
    """
    Build expected enclosure group
    :param eg:
    """
    rtn = eg.copy()
    rtn.pop('configurationScript', 0)
    rtn.pop('interconnectBayMappings', 0)
    rtn.update(
        {'category': 'enclosure-groups',
         'ipAddressingMode': 'External',
         'portMappingCount': 8,
         'uri': 'EG:' + eg['name']}
    )
    return rtn


# EG
def build_logical_enclosure(le_attributes):
    """
    Build logical enclosure
    :param le_attributes:
    """
    return {'name': le_attributes['name'],
            'enclosureUris': le_attributes['enclosureUris'],
            'enclosureGroupUri': le_attributes['enclosureGroupUri']}


def build_expected_logical_enclosure(le):
    """
    Build logical enclosure
    :param le_attributes:
    """
    rtn = le.copy()
    rtn.update({
        'type': LOGICAL_ENCLOSURE_TYPE
    })
    return rtn


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
        'name': 'ovst-3par-8400-01-srv',
        'hostname': 'ovst-3par-8400-01-srv.vse.rdlabs.hpecorp.net',
        'managedDomain': 'UPT',
        'discoveredDomains': ['NODOMAIN'],
        'managed_ports': [
            {'name': '0:0:1', 'wwn': '20:01:00:02:AC:01:AB:80', 'wwn_no_colon': '20:01:00:02:AC:01:AB:80'.replace(':', '')},
            {'name': '1:0:1', 'wwn': '21:01:00:02:AC:01:AB:80', 'wwn_no_colon': '21:01:00:02:AC:01:AB:80'.replace(':', '')},
            {'name': '0:0:2', 'wwn': '20:02:00:02:AC:01:AB:80', 'wwn_no_colon': '20:02:00:02:AC:01:AB:80'.replace(':', '')},
            {'name': '1:0:2', 'wwn': '21:02:00:02:AC:01:AB:80', 'wwn_no_colon': '21:02:00:02:AC:01:AB:80'.replace(':', '')},
        ],
        'serialNumber': 'MXN6222KXP',
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
    Build storeserv volume
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
    Build storevirtual volume
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


# Group1 enc1 Potash FC connections
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
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][0]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][2]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {
            'sasLogicalJBODs': [
                {'id': 1, 'deviceSlot': 'Mezz 1', 'name': profile_attributes['name'] + '_LJBOD1', 'numPhysicalDrives': 1, 'driveMinSizeGB': 146,
                 'driveMaxSizeGB': 300, 'driveTechnology': 'SasHdd', }],
            'controllers': [
                {'deviceSlot': 'Mezz 1', 'mode': 'RAID', 'initialize': False, 'importConfiguration': False,
                 'logicalDrives': [
                     {'name': None, 'raidLevel': 'RAID0', 'bootable': False, 'numPhysicalDrives': None, 'driveTechnology': None, 'sasLogicalJBODId': 1}]
                 }]
        },
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], 'bootVolumePriority': 'NotBootable', 'lunType': 'Manual', 'lun': 1,
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}]},
                {'id': 2, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], 'bootVolumePriority': 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]},
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
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        "connectionSettings": {"reapplyState": "NotApplying", 'connections': [
            {'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][0]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][2]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {
            'sasLogicalJBODs': [
                {'id': 1, 'deviceSlot': 'Mezz 1', 'name': profile_attributes['name'] + '_LJBOD1', 'numPhysicalDrives': 1, 'driveMinSizeGB': 146,
                 'driveMaxSizeGB': 300, 'driveTechnology': 'SasHdd', }],
            'controllers': [
                {'deviceSlot': 'Mezz 1', 'mode': 'RAID', 'initialize': False, 'importConfiguration': False,
                 'logicalDrives': [
                     {'name': None, 'raidLevel': 'RAID0', 'bootable': False, 'numPhysicalDrives': None, 'driveTechnology': None, 'sasLogicalJBODId': 1}]
                 }]
        },
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], 'bootVolumePriority': 'NotBootable', 'lunType': 'Manual', 'lun': 1, 'state': 'Attached', 'lunType': 'Manual',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 1, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][0]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][1]['wwn']}]},
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][2]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][3]['wwn']}]}]
                 },
                {'id': 2, 'state': 'Attached', 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], 'bootVolumePriority': 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]},
                     {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto',
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


# Group2 enc2 Carbon FC connections
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
            {'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '16000',
             'networkUri': 'FC:' + fc_networks_attributes[2]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '16000',
             'networkUri': 'FC:' + fc_networks_attributes[3]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], 'bootVolumePriority': 'Primary', 'lunType': 'Manual', 'lun': 1, 'state': 'Attached', 'lunType': 'Manual',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}]},
                {'id': 2, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], 'bootVolumePriority': 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]},
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
            {'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': '16000',
             'networkUri': 'FC:' + fc_networks_attributes[2]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': '16000',
             'networkUri': 'FC:' + fc_networks_attributes[3]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], 'bootVolumePriority': 'Primary', 'lunType': 'Manual', 'lun': 1, 'state': 'Attached', 'lunType': 'Manual',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 1, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][0]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][1]['wwn']}]},
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][2]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][3]['wwn']}]}]
                 },
                {'id': 2, 'state': 'Attached', 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], 'bootVolumePriority': 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]},
                     {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto',
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


# Group3 enc1 Potash FC connections
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
            {'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][0]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][2]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
        "localStorage": {
            "sasLogicalJBODs": [{'id': 1, "deviceSlot": "Mezz 1", "name": profile_attributes['name'] + '_LJBOD1', "numPhysicalDrives": 1,
                                 "driveMinSizeGB": 146, "driveMaxSizeGB": 300, "driveTechnology": "SasHdd", "sasLogicalJBODUri": None, }],

            "controllers": [{"logicalDrives": [{"name": None, "raidLevel": "RAID0", "bootable": False, "numPhysicalDrives": None, "driveTechnology": None, "sasLogicalJBODId": 1, }], "deviceSlot": "Mezz 1", "mode": "Mixed", "initialize": False, "importConfiguration": False}]
        },
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], 'bootVolumePriority': 'NotBootable', 'lunType': 'Manual', 'lun': 1,
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}]},
                {'id': 2, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], 'bootVolumePriority': 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []},
                     {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]},
            ]
        }
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
            {'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[0]['name'],
             'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][0]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '8000',
             'networkUri': 'FC:' + fc_networks_attributes[1]['name'],
             'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                      'targets': [{'arrayWwpn': storeserv_systems_attributes[0]['managed_ports'][2]['wwn_no_colon'], 'lun': '1'}]}
             },
            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
            {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
             'networkUri': 'ETH:' + ethernet_networks_attributes[0]['name'],
             'boot': {'priority': 'NotBootable'}
             },
        ]},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
        "localStorage": {
            "sasLogicalJBODs": [{'id': 1, "deviceSlot": "Mezz 1", "name": profile_attributes['name'] + '_LJBOD1', "numPhysicalDrives": 1,
                                 "driveMinSizeGB": 146, "driveMaxSizeGB": 300, "driveTechnology": "SasHdd", }],

            "controllers": [{"logicalDrives": [{"name": None, "raidLevel": "RAID0", "bootable": False, "numPhysicalDrives": None, "driveTechnology": None, "sasLogicalJBODId": 1, }],
                             "deviceSlot": "Mezz 1", "mode": "Mixed", "initialize": False, "importConfiguration": False}]
        },
        'sanStorage': {
            'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
            'volumeAttachments': [
                {'id': 1, 'volumeUri': 'SVOL:' + profile_attributes['volumes'][0], 'bootVolumePriority': 'NotBootable', 'lunType': 'Manual', 'lun': 1, 'state': 'Attached', 'lunType': 'Manual',
                 'storagePaths': [
                     {'targetSelector': 'Auto', 'connectionId': 1, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][0]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][1]['wwn']}]},
                     {'targetSelector': 'Auto', 'connectionId': 2, 'isEnabled': True,
                      'targets': [{'name': storeserv_systems_attributes[0]['managed_ports'][2]['wwn']}, {'name': storeserv_systems_attributes[0]['managed_ports'][3]['wwn']}]}]
                 },
                {'id': 2, 'state': 'Attached', 'volumeUri': 'SVOL:' + profile_attributes['volumes'][1], 'bootVolumePriority': 'NotBootable', 'lunType': 'Auto',
                 'storagePaths': [
                     {'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto',
                      'targets': [{'ipAddress': storevirtual_systems_attributes[0]['vip'], 'tcpPort': '3260', 'name': REGEX_VSA_STORAGE_PATH_TARGET_NAME}]},
                     {'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto',
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
