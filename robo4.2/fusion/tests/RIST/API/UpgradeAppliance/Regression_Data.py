from RoboGalaxyLibrary import BuiltIn
from RoboGalaxyLibrary import VsphereKeywords
import re
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.libs.utils.common import get_firmware_bundle

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
Issuer_IP = '15.114.112.61'

ENC = ['CN75440444', ]

SH_NAME = '%s, bay 4' % ENC[0]
EG_NAME = 'EG_SYNERGY'
FC1 = 'FA1'
FC2 = 'FA2'

# Enclosures
ENC1 = 'CN75440444'
# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
# Server Hardware
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1

# Firmware bundle
spp_folder = r'Z:\firmware\hotfix'
spp_prefix = 'cp030892'
fw_bundle = get_firmware_bundle(spp_folder, spp_prefix)

# -- Begin - Upgrade data
repo_400 = "http://ci-nexus.vse.rdlabs.hpecorp.net/Fusion/rel"
repo_latest = "http://ci-artifacts02.vse.rdlabs.hpecorp.net/Fusion/rel"
release = BuiltIn().get_variable_value("${RELEASE}")
repo = repo_400 if release == "4.00" else repo_latest
repo = repo + "/" + release
update_bin_repo = "%s/UpdateBin/ue-fullupdate/" % repo

pb_number = BuiltIn().get_variable_value("${PASS_BUILD}")

dd_image_repo = '%s/DDImage/SSH/' % repo


def embedded_numbers(str_with_num):
    """    @Author:  John"""
    re_digits = re.compile(r'(\d+)')
    # Split to digit and non-digit
    pieces = re_digits.split(str_with_num)
    # Convert digit to int
    pieces[1:: 2] = map(int, pieces[1:: 2])
    return pieces[1:: 2]


def get_update_bin_filename(
        filename_filter,
        image_repo=dd_image_repo,
        bin_repo=update_bin_repo):
    image_filename = VsphereKeywords().get_LatestBuild_name(
        image_repo,
        '',
        'zip',
        r"HPE?OneView.*{0}.*.%s.*".format(filename_filter))
    build_number = embedded_numbers(image_filename)[3]
    bin_filename = VsphereKeywords().get_LatestBuild_name(
        bin_repo,
        '',
        'bin',
        r"HPE?OneView.*{0}.%s$".format(build_number))
    return bin_filename, str(build_number)

update_bin_filename, target_build_number = get_update_bin_filename(
    filename_filter=pb_number)

update_bin_file_url = "{0}{1}".format(update_bin_repo, update_bin_filename)
# -- End


# --Begin - OV3.0 Base resources data before upgrade
class OneView_300(object):
    USER_AND_PERMISSION_TYPE = 'UserAndRoles'
    ETHERNET_NETWORK_TYPE = 'ethernet-networkV300'
    NETWORK_SET_TYPE = 'network-setV300'
    FCOE_NETWORK_TYPE = 'fcoe-networkV300'
    FC_NETWORK_TYPE = 'fc-networkV300'
    LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV300'
    SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-group'
    ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV300'
    STORAGE_SYSTEM_TYPE = 'StorageSystemV3'
    SERVER_PROFILE_TYPE = 'ServerProfileV6'

    users = [{'userName': 'FullAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'FullAdmin',
              'roles': ['Infrastructure administrator'],
              'emailAddress': 'InfraUser@hp.com',
              'officePhone': '970-555-0003',
              'mobilePhone': '970-555-0004',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'ServerAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'ServerAdmin',
              'roles': ['Server administrator'],
              'emailAddress': 'ServerUser@hp.com',
              'officePhone': '970-555-0005',
              'mobilePhone': '970-555-0005',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'Networkadmin',
              'password': 'wpsthpvse1',
              'fullName': 'Networkadmin',
              'roles': ['Network administrator'],
              'emailAddress': 'NetworkUser@hp.com',
              'officePhone': '970-555-0006',
              'mobilePhone': '970-555-0006',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'BackupAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'BackupAdmin',
              'roles': ['Backup administrator'],
              'emailAddress': 'BackupUser@hp.com',
              'officePhone': '970-555-0007',
              'mobilePhone': '970-555-0007',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'ReadOnly',
              'password': 'wpsthpvse1',
              'fullName': 'ReadOnly',
              'roles': ['Read only'],
              'emailAddress': 'ReadOnlyUser@hp.com',
              'officePhone': '970-555-0008',
              'mobilePhone': '970-555-0008',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'StorageAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'StorageAdmin',
              'roles': ['Storage administrator'],
              'emailAddress': 'StorageUser@hp.com',
              'officePhone': '970-555-0009',
              'mobilePhone': '970-555-0009',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'IA',
              'password': 'wpsthpvse1',
              'fullName': 'IA',
              'roles': ['Infrastructure administrator'],
              'emailAddress': 'InfraUser@hpe.com',
              'officePhone': '970-555-0004',
              'mobilePhone': '970-555-0004',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'SA',
              'password': 'wpsthpvse1',
              'fullName': 'SA',
              'roles': ['Server administrator'],
              'emailAddress': 'ServerUser@hpe.com',
              'officePhone': '970-555-0005',
              'mobilePhone': '970-555-0005',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'NA',
              'password': 'wpsthpvse1',
              'fullName': 'NA',
              'roles': ['Network administrator'],
              'emailAddress': 'NetworkUser@hpe.com',
              'officePhone': '970-555-0006',
              'mobilePhone': '970-555-0006',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'BA',
              'password': 'wpsthpvse1',
              'fullName': 'BA',
              'roles': ['Backup administrator'],
              'emailAddress': 'BackupUser@hpe.com',
              'officePhone': '970-555-0007',
              'mobilePhone': '970-555-0007',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'Full',
              'password': 'wpsthpvse1',
              'fullName': 'Full',
              'roles': ['Infrastructure administrator'],
              'emailAddress': 'FullUser@hpe.com',
              'officePhone': '970-555-0008',
              'mobilePhone': '970-555-0008',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'RO',
              'password': 'wpsthpvse1',
              'fullName': 'RO',
              'roles': ['Read only'],
              'emailAddress': 'ReadOnlyUser@hpe.com',
              'officePhone': '970-555-0009',
              'mobilePhone': '970-555-0009',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'StA',
              'password': 'wpsthpvse1',
              'fullName': 'StA',
              'roles': ['Storage administrator'],
              'emailAddress': 'StorageUser@hpe.com',
              'officePhone': '970-555-0003',
              'mobilePhone': '970-555-0003',
              'type': USER_AND_PERMISSION_TYPE},
             ]
    licenses = [{'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
                {'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
                {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
                {'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}
                ]
    SAN_Managers = [{"connectionInfo": [{'name': 'Type',
                                         'value': 'Brocade Network Advisor'},
                                        {"name": "Host",
                                         "displayName": "Host",
                                         "required": True,
                                         "value": "16.125.65.9",
                                         "valueFormat": "IPAddressOrHostname",
                                         "valueType": "String"},
                                        {"name": "Port",
                                         "displayName": "Port",
                                         "required": True,
                                         "value": 5989,
                                         "valueFormat": "None",
                                         "valueType": "Integer"},
                                        {"name": "Username",
                                         "displayName": "Username",
                                         "required": True,
                                         "value": "Administrator",
                                         "valueFormat": "None",
                                         "valueType": "String"},
                                        {"name": "Password",
                                         "displayName": "Password",
                                         "required": True,
                                         "value": "password",
                                         "valueFormat": "SecuritySensitive",
                                         "valueType": "String"},
                                        {"name": "UseSsl",
                                         "displayName": "UseSsl",
                                         "required": True,
                                         "value": True,
                                         "valueFormat": "None",
                                         "valueType": "Boolean"},
                                        ],
                     },
                    {"connectionInfo": [{'name': 'Type',
                                         'value': 'HPE'},
                                        {"name": "Host",
                                         "value": "16.125.25.45"},
                                        {"name": "SnmpPort",
                                         "value": 161},
                                        {"name": "SnmpUserName",
                                         "value": "UNoAuthNoPriv"},
                                        {"name": "SnmpAuthLevel",
                                         "value": "NOAUTHNOPRIV"},
                                        ],
                     },
                    ]
    ethernet_networks = [{'name': 'dev100',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 100,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev101-management',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 101,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev102-vmmigration',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 102,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev103-ft-a',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 103,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev104',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 104,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev300-pxeboot',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 300,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'ut-net1',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Untagged'},
                         {'name': 'ut-net2',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': True,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Untagged'},
                         {'name': 'ut-net3',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'Management',
                          'smartLink': True,
                          'privateNetwork': True,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Untagged'},
                         {'name': 'tu-net1',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'Management',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tunnel'},
                         {'name': 'tu-net2',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'Management',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tunnel'},
                         {'name': 'tu-net3',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': True,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tunnel'}]
    fc_networks = [{'name': 'FA1',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'},
                   {'name': 'FA2',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'},
                   {'name': 'FA3',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': None},
                   {'name': 'FA4',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True},
                   {'name': 'FA5',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'},
                   {'name': 'FA6',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'},
                   {'name': 'DA1',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'DirectAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': None},
                   {'name': 'DA2',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'DirectAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True}]
    fcoe_networks = [{'name': 'fcoe_103',
                      'type': FCOE_NETWORK_TYPE,
                      'vlanId': 103},
                     {'name': 'FCoE1',
                      'type': FCOE_NETWORK_TYPE,
                      'vlanId': 350,
                      'managedSanUri': 'FCSan:VSAN350'},
                     {'name': 'FCoE2',
                      'type': FCOE_NETWORK_TYPE,
                      'vlanId': 450,
                      'managedSanUri': 'FCSan:VSAN450'}]
    network_sets = [{'name': 'Net-Set1',
                     'type': NETWORK_SET_TYPE,
                     'networkUris': ['dev100',
                                     'dev300-pxeboot'],
                     'nativeNetworkUri': None},
                    {'name': 'Net-Set2',
                     'type': NETWORK_SET_TYPE,
                     'networkUris': ['dev101-management',
                                     'dev103-ft-a'],
                     'nativeNetworkUri': None},
                    {'name': 'Net-Set3',
                     'type': NETWORK_SET_TYPE,
                     'networkUris': ['dev100',
                                     'dev101-management',
                                     'dev102-vmmigration',
                                     'dev103-ft-a',
                                     'dev104'],
                     'nativeNetworkUri': None},
                    ]

    enc_names = ENC
    enc_list = ["ENC:%s" % enc for enc in enc_names]
    fc_domain = "Tbird_Regression_Domain"
    fcoe_domain = "NO DOMAIN"

    uplink_sets = {}

    icmap = {'LIG_POTASH': [{'bay': 3,
                             'enclosure': 1,
                             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                             'enclosureIndex': 1},
                            {'bay': 6,
                             'enclosure': 1,
                             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                             'enclosureIndex': 1},
                            ],
             'LIG_SAS': [{'bay': 1,
                          'enclosure': 1,
                          'type': 'Synergy 12Gb SAS Connection Module',
                          'enclosureIndex': 1},
                         ],
             }

    LIG = [
        {
            'name': 'LIG_POTASH',
            'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': icmap['LIG_POTASH'],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'fcoeSettings': {'fcoeMode': 'FcfNpv'},
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None,
            'uplinkSets': [],
        }
    ]

    SAS_LIG = [
        {
            "name": "LIG_SAS",
            "state": "Active",
            "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
            "enclosureType": "SY12000",
            "interconnectMapTemplate": icmap["LIG_SAS"],
            "enclosureIndexes": [1],
            "interconnectBaySet": 1,
        }
    ]

    EG = [{'name': EG_NAME,
           'type': ENCLOSURE_GROUP_TYPE,
           'enclosureCount': 1,
           'enclosureTypeUri': '/rest/enclosure-types/SY12000',
           'stackingMode': 'Enclosure',
           'interconnectBayMappingCount': 3,
           'configurationScript': None,
           'interconnectBayMappings': [{"interconnectBay": 3,
                                        "logicalInterconnectGroupUri": "LIG:" + LIG[0]["name"]},
                                       {"interconnectBay": 6,
                                        "logicalInterconnectGroupUri": "LIG:" + LIG[0]["name"]},
                                       {"interconnectBay": 1,
                                        "enclosureIndex": 1,
                                        "logicalInterconnectGroupUri": "SASLIG:" + SAS_LIG[0]["name"]},
                                       ],
           'ipAddressingMode': "External",
           'ipRangeUris': [],
           'powerMode': "RedundantPowerFeed"}]

    LE = {"name": "LE_SYNERGY",
          "enclosureUris": enc_list,
          "enclosureGroupUri": "EG:" + EG_NAME,
          "firmwareBaselineUri": None,
          "forceInstallFirmware": False}

    StorageSystems_Put = [{"type": STORAGE_SYSTEM_TYPE,
                           "hostname": "wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net",
                           "credentials": {"username": "fusionadm", "password": "hpvse1"},
                           "family": "StoreServ",
                           "name": "wpst3par-7200-7-srv",
                           "managedDomain": fc_domain,
                           "serialNumber": "1645767",
                           "uri": "wpst3par-7200-7-srv",
                           "unmanagedPorts": [],
                           "refreshState": "NotRefreshing",
                           "managedPools": [
                               {"type": "StoragePool", "domain": fc_domain, "name": "FVT_Tbird_reg1_r1",
                                "deviceType": "FC"},
                               {"type": "StoragePool", "domain": fc_domain, "name": "FVT_Tbird_reg1_r5",
                                "deviceType": "FC"},
                               {"type": "StoragePool", "domain": fc_domain, "name": "FVT_Tbird_reg1_r6",
                                "deviceType": "FC"}],
                           "managedPorts": [{"type": "StorageTargetPortV3",
                                             "portWwn": "20230002AC00B2C7",
                                             "portName": "0:2:3",
                                             "name": "0:2:3",
                                             "expectedNetworkUri": "FC:FA1",
                                             "actualNetworkUri": "FA1",
                                             "actualNetworkSanUri": "wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55",
                                             "groupName": "Auto"},
                                            {"type": "StorageTargetPortV3",
                                             "portWwn": "21230002AC00B2C7",
                                             "portName": "1:2:3",
                                             "name": "1:2:3",
                                             "expectedNetworkUri": "FC:FA1",
                                             "actualNetworkUri": "FA1",
                                             "actualNetworkSanUri": "wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55",
                                             "groupName": "Auto"},
                                            {"type": "StorageTargetPortV3",
                                             "portWwn": "20240002AC00B2C7",
                                             "portName": "0:2:4",
                                             "name": "0:2:4",
                                             "expectedNetworkUri": "FC:FA2",
                                             "actualNetworkUri": "FA2",
                                             "actualNetworkSanUri": "wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56",
                                             "groupName": "Auto"},
                                            {"type": "StorageTargetPortV3",
                                             "portWwn": "21240002AC00B2C7",
                                             "portName": "1:2:4",
                                             "name": "1:2:4",
                                             "expectedNetworkUri": "FC:FA2",
                                             "actualNetworkUri": "FA2",
                                             "actualNetworkSanUri": "wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56",
                                             "groupName": "Auto"},
                                            ]
                           },
                          {"type": STORAGE_SYSTEM_TYPE,
                           "hostname": "fvt3par-8400-1-srv.vse.rdlabs.hpecorp.net",
                           "credentials": {"username": "3paradm", "password": "3pardata"},
                           "family": "StoreServ",
                           "name": "fvt3par-8400-1-srv",
                           "managedDomain": fcoe_domain,
                           "serialNumber": "MXN6262MRY",
                           "uri": "fvt3par-8400-1-srv",
                           "unmanagedPorts": [],
                           "refreshState": "NotRefreshing",
                           "managedPools": [
                               {"type": "StoragePool", "domain": fcoe_domain, "name": "FC_r1",
                                "deviceType": "FC"},
                               {"type": "StoragePool", "domain": fcoe_domain, "name": "FC_r5",
                                "deviceType": "FC"}],
                           "managedPorts": [{"type": "StorageTargetPortV3",
                                             "portWwn": "22:21:00:02:AC:01:AF:55",
                                             "portName": "2:2:1",
                                             "name": "2:2:1",
                                             "expectedNetworkUri": "FCOE:FCoE1",
                                             "actualNetworkUri": "FCoE1",
                                             "actualNetworkSanUri": "VSAN350",
                                             "groupName": "Auto"},
                                            {"type": "StorageTargetPortV3",
                                             "portWwn": "23:21:00:02:AC:01:AF:55",
                                             "portName": "3:2:1",
                                             "name": "3:2:1",
                                             "expectedNetworkUri": "FCOE:FCoE1",
                                             "actualNetworkUri": "FCoE1",
                                             "actualNetworkSanUri": "VSAN350",
                                             "groupName": "Auto"},
                                            {"type": "StorageTargetPortV3",
                                             "portWwn": "22:22:00:02:AC:01:AF:55",
                                             "portName": "2:2:2",
                                             "name": "2:2:2",
                                             "expectedNetworkUri": "FCOE:FCoE2",
                                             "actualNetworkUri": "FCoE2",
                                             "actualNetworkSanUri": "VSAN450",
                                             "groupName": "Auto"},
                                            {"type": "StorageTargetPortV3",
                                             "portWwn": "23:22:00:02:AC:01:AF:55",
                                             "portName": "3:2:2",
                                             "name": "3:2:2",
                                             "expectedNetworkUri": "FCOE:FCoE2",
                                             "actualNetworkUri": "FCoE2",
                                             "actualNetworkSanUri": "VSAN450",
                                             "groupName": "Auto"},
                                            ]
                           }
                          ]

    Volumes = [
        {
            'name': '%s-FA-Vol1-Thin-20GB-R5-Private' %
            enc_names[0].upper(), 'storageSystemUri': 'wpst3par-7200-7-srv', 'snapshotPoolUri': 'FVT_Tbird_reg1_r6', 'templateUri': None, 'description': '%s-FA-Vol1-Thin-20GB-R5-Private' %
            enc_names[0].upper(), 'provisioningParameters': {
                'storagePoolUri': 'FVT_Tbird_reg1_r5', 'requestedCapacity': '21474836480', 'provisionType': 'Thin', 'shareable': False}}, {
            'name': '%s-FA-Vol2-Full-20GB-R5-Private' %
            enc_names[0].upper(), 'storageSystemUri': 'wpst3par-7200-7-srv', 'snapshotPoolUri': 'FVT_Tbird_reg1_r6', 'templateUri': None, 'description': '%s-FA-Vol2-Full-20GB-R5-Private' %
            enc_names[0].upper(), 'provisioningParameters': {
                    'storagePoolUri': 'FVT_Tbird_reg1_r5', 'requestedCapacity': '21474836480', 'provisionType': 'Full', 'shareable': False}}, {
                        'name': '%s-FA-Vol3-Thin-30GB-R5-Shared' %
                        enc_names[0].upper(), 'storageSystemUri': 'wpst3par-7200-7-srv', 'snapshotPoolUri': 'FVT_Tbird_reg1_r6', 'templateUri': None, 'description': '%s-FA-Vol1-Thin-20GB-R5-Private' %
                        enc_names[0].upper(), 'provisioningParameters': {
                            'storagePoolUri': 'FVT_Tbird_reg1_r5', 'requestedCapacity': '32212254720', 'provisionType': 'Thin', 'shareable': True}}, {
                                'name': '%s-FCoE-Vol1-Thin-20GB-R5-Private' %
                                enc_names[0].upper(), 'storageSystemUri': 'fvt3par-8400-1-srv', 'snapshotPoolUri': 'FC_r1', 'templateUri': None, 'description': '%s-FA-Vol1-Thin-20GB-R5-Private' %
                                enc_names[0].upper(), 'provisioningParameters': {
                                    'storagePoolUri': 'FC_r1', 'requestedCapacity': '21474836480', 'provisionType': 'Thin', 'shareable': False}}, {
                                        'name': '%s-FCoE-Vol2-Full-20GB-R5-Private' %
                                        enc_names[0].upper(), 'storageSystemUri': 'fvt3par-8400-1-srv', 'snapshotPoolUri': 'FC_r1', 'templateUri': None, 'description': '%s-FA-Vol2-Full-20GB-R5-Private' %
                                        enc_names[0].upper(), 'provisioningParameters': {
                                            'storagePoolUri': 'FC_r1', 'requestedCapacity': '21474836480', 'provisionType': 'Full', 'shareable': False}}, {
                                                'name': '%s-FCoE-Vol3-Thin-30GB-R5-Shared' %
                                                enc_names[0].upper(), 'storageSystemUri': 'fvt3par-8400-1-srv', 'snapshotPoolUri': 'FC_r1', 'templateUri': None, 'description': '%s-FA-Vol1-Thin-20GB-R5-Private' %
                                                enc_names[0].upper(), 'provisioningParameters': {
                                                    'storagePoolUri': 'FC_r1', 'requestedCapacity': '32212254720', 'provisionType': 'Thin', 'shareable': True}}]

    resources_names = ["LE:%s" % LE["name"],
                       "LI:%s-%s" % (LE["name"], LIG[0]["name"]),
                       "SASLI:%s-%s-1" % (LE["name"], SAS_LIG[0]["name"]),
                       "IC:%s" % ENC1ICBAY3,
                       "IC:%s" % ENC1ICBAY6,
                       # "ENC:%s" % ENC1,
                       "SH:%s" % ENC1SHBAY4,
                       "SH:%s" % ENC1SHBAY6,
                       "SH:%s" % ENC1SHBAY7,
                       "SH:%s" % ENC1SHBAY8,
                       "SH:%s" % ENC1SHBAY9,
                       # "SP:%s" % server_profile[0]["name"],
                       "SSYS:%s" % StorageSystems_Put[0]["name"],
                       "SSYS:%s" % StorageSystems_Put[1]["name"],
                       ]
# -- End


# --Begin - OV3.1 Base resources data before upgrade
class OneView_310(object):
    USER_AND_PERMISSION_TYPE = 'UserAndRoles'
    ETHERNET_NETWORK_TYPE = 'ethernet-networkV300'
    NETWORK_SET_TYPE = 'network-setV300'
    FCOE_NETWORK_TYPE = 'fcoe-networkV300'
    FC_NETWORK_TYPE = 'fc-networkV300'
    LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV300'
    SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-group'
    ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV400'
    STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
    SERVER_PROFILE_TYPE = 'ServerProfileV7'

    users = [{'userName': 'FullAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'FullAdmin',
              'roles': ['Infrastructure administrator'],
              'emailAddress': 'InfraUser@hp.com',
              'officePhone': '970-555-0003',
              'mobilePhone': '970-555-0004',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'ServerAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'ServerAdmin',
              'roles': ['Server administrator'],
              'emailAddress': 'ServerUser@hp.com',
              'officePhone': '970-555-0005',
              'mobilePhone': '970-555-0005',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'Networkadmin',
              'password': 'wpsthpvse1',
              'fullName': 'Networkadmin',
              'roles': ['Network administrator'],
              'emailAddress': 'NetworkUser@hp.com',
              'officePhone': '970-555-0006',
              'mobilePhone': '970-555-0006',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'BackupAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'BackupAdmin',
              'roles': ['Backup administrator'],
              'emailAddress': 'BackupUser@hp.com',
              'officePhone': '970-555-0007',
              'mobilePhone': '970-555-0007',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'ReadOnly',
              'password': 'wpsthpvse1',
              'fullName': 'ReadOnly',
              'roles': ['Read only'],
              'emailAddress': 'ReadOnlyUser@hp.com',
              'officePhone': '970-555-0008',
              'mobilePhone': '970-555-0008',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'StorageAdmin',
              'password': 'wpsthpvse1',
              'fullName': 'StorageAdmin',
              'roles': ['Storage administrator'],
              'emailAddress': 'StorageUser@hp.com',
              'officePhone': '970-555-0009',
              'mobilePhone': '970-555-0009',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'IA',
              'password': 'wpsthpvse1',
              'fullName': 'IA',
              'roles': ['Infrastructure administrator'],
              'emailAddress': 'InfraUser@hpe.com',
              'officePhone': '970-555-0004',
              'mobilePhone': '970-555-0004',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'SA',
              'password': 'wpsthpvse1',
              'fullName': 'SA',
              'roles': ['Server administrator'],
              'emailAddress': 'ServerUser@hpe.com',
              'officePhone': '970-555-0005',
              'mobilePhone': '970-555-0005',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'NA',
              'password': 'wpsthpvse1',
              'fullName': 'NA',
              'roles': ['Network administrator'],
              'emailAddress': 'NetworkUser@hpe.com',
              'officePhone': '970-555-0006',
              'mobilePhone': '970-555-0006',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'BA',
              'password': 'wpsthpvse1',
              'fullName': 'BA',
              'roles': ['Backup administrator'],
              'emailAddress': 'BackupUser@hpe.com',
              'officePhone': '970-555-0007',
              'mobilePhone': '970-555-0007',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'Full',
              'password': 'wpsthpvse1',
              'fullName': 'Full',
              'roles': ['Infrastructure administrator'],
              'emailAddress': 'FullUser@hpe.com',
              'officePhone': '970-555-0008',
              'mobilePhone': '970-555-0008',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'RO',
              'password': 'wpsthpvse1',
              'fullName': 'RO',
              'roles': ['Read only'],
              'emailAddress': 'ReadOnlyUser@hpe.com',
              'officePhone': '970-555-0009',
              'mobilePhone': '970-555-0009',
              'type': USER_AND_PERMISSION_TYPE},
             {'userName': 'StA',
              'password': 'wpsthpvse1',
              'fullName': 'StA',
              'roles': ['Storage administrator'],
              'emailAddress': 'StorageUser@hpe.com',
              'officePhone': '970-555-0003',
              'mobilePhone': '970-555-0003',
              'type': USER_AND_PERMISSION_TYPE},
             ]
    licenses = [{'key': 'QCLA A9MA H9PA KHW3 V7B5 HWWB Y9JL KMPL BRKD 8FBM DXAU 2CSM GHTG L762 XKJ3 VBF4 KJVT D5KM EFRW DS5R A9E9 52KG 9K2P 3E22 UKYU 3UFZ TZZ7 MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863966 HPOV-NFR1 HP_OneView_16_Seat_NFR 7EA7ADTYED49"_3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'},
                {'key': 'YCLC C9MA H9P9 8HW3 U7B5 HWW5 Y9JL KMPL LRGB 7ABQ DXAU 2CSM GHTG L762 QGFZ EEZM KJVT D5KM EFRW DS5R M94M N5KG 9K2P 3E22 AKYU LUV5 TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424864041 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR HY95ADTYTCHT"'},
                {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
                {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]
    SAN_Managers = [{"connectionInfo": [{'name': 'Type',
                                         'value': 'Brocade Network Advisor'},
                                        {"name": "Host",
                                         "displayName": "Host",
                                         "required": True,
                                         "value": "16.125.65.9",
                                         "valueFormat": "IPAddressOrHostname",
                                         "valueType": "String"},
                                        {"name": "Port",
                                         "displayName": "Port",
                                         "required": True,
                                         "value": 5989,
                                         "valueFormat": "None",
                                         "valueType": "Integer"},
                                        {"name": "Username",
                                         "displayName": "Username",
                                         "required": True,
                                         "value": "Administrator",
                                         "valueFormat": "None",
                                         "valueType": "String"},
                                        {"name": "Password",
                                         "displayName": "Password",
                                         "required": True,
                                         "value": "password",
                                         "valueFormat": "SecuritySensitive",
                                         "valueType": "String"},
                                        {"name": "UseSsl",
                                         "displayName": "UseSsl",
                                         "required": True,
                                         "value": True,
                                         "valueFormat": "None",
                                         "valueType": "Boolean"},
                                        ],
                     },
                    {"connectionInfo": [{'name': 'Type',
                                         'value': 'HPE'},
                                        {"name": "Host",
                                         "value": "16.125.25.45"},
                                        {"name": "SnmpPort",
                                         "value": 161},
                                        {"name": "SnmpUserName",
                                         "value": "UNoAuthNoPriv"},
                                        {"name": "SnmpAuthLevel",
                                         "value": "NOAUTHNOPRIV"},
                                        ],
                     },
                    ]
    ethernet_networks = [{'name': 'dev100',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 100,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev101-management',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 101,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev102-vmmigration',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 102,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev103-ft-a',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 103,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev104',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 104,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'dev300-pxeboot',
                          'type': ETHERNET_NETWORK_TYPE,
                          'vlanId': 300,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tagged',
                          'bandwidth': {'maximumBandwidth': 20000,
                                        'typicalBandwidth': 2000}},
                         {'name': 'ut-net1',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Untagged'},
                         {'name': 'ut-net2',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'General',
                          'smartLink': False,
                          'privateNetwork': True,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Untagged'},
                         {'name': 'ut-net3',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'Management',
                          'smartLink': True,
                          'privateNetwork': True,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Untagged'},
                         {'name': 'tu-net1',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'Management',
                          'smartLink': True,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tunnel'},
                         {'name': 'tu-net2',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'Management',
                          'smartLink': False,
                          'privateNetwork': False,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tunnel'},
                         {'name': 'tu-net3',
                          'type': ETHERNET_NETWORK_TYPE,
                          'purpose': 'General',
                          'smartLink': True,
                          'privateNetwork': True,
                          'connectionTemplateUri': None,
                          'ethernetNetworkType': 'Tunnel'}]
    fc_networks = [{'name': 'FA1',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'},
                   {'name': 'FA2',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'},
                   {'name': 'FA3',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': None},
                   {'name': 'FA4',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True},
                   {'name': 'FA5',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'},
                   {'name': 'FA6',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'FabricAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'},
                   {'name': 'DA1',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'DirectAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True,
                    'managedSanUri': None},
                   {'name': 'DA2',
                    'type': FC_NETWORK_TYPE,
                    'fabricType': 'DirectAttach',
                    'linkStabilityTime': 30,
                    'autoLoginRedistribution': True}]
    fcoe_networks = [{'name': 'fcoe_103',
                      'type': FCOE_NETWORK_TYPE,
                      'vlanId': 103},
                     {'name': 'FCoE1',
                      'type': FCOE_NETWORK_TYPE,
                      'vlanId': 350,
                      'managedSanUri': 'FCSan:VSAN350'},
                     {'name': 'FCoE2',
                      'type': FCOE_NETWORK_TYPE,
                      'vlanId': 450,
                      'managedSanUri': 'FCSan:VSAN450'}]
    network_sets = [{'name': 'Net-Set1',
                     'type': NETWORK_SET_TYPE,
                     'networkUris': ['dev100',
                                     'dev300-pxeboot'],
                     'nativeNetworkUri': None},
                    {'name': 'Net-Set2',
                     'type': NETWORK_SET_TYPE,
                     'networkUris': ['dev101-management',
                                     'dev103-ft-a'],
                     'nativeNetworkUri': None},
                    {'name': 'Net-Set3',
                     'type': NETWORK_SET_TYPE,
                     'networkUris': ['dev100',
                                     'dev101-management',
                                     'dev102-vmmigration',
                                     'dev103-ft-a',
                                     'dev104'],
                     'nativeNetworkUri': None},
                    ]

    enc_names = ENC
    enc_list = ["ENC:%s" % enc for enc in enc_names]
    fc_domain = "Tbird_Regression_Domain"
    fcoe_domain = "NO DOMAIN"

    uplink_sets = {}

    icmap = {'LIG_POTASH': [{'bay': 3,
                             'enclosure': 1,
                             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                             'enclosureIndex': 1},
                            {'bay': 6,
                             'enclosure': 1,
                             'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                             'enclosureIndex': 1},
                            ],
             'LIG_SAS': [{'bay': 1,
                          'enclosure': 1,
                          'type': 'Synergy 12Gb SAS Connection Module',
                          'enclosureIndex': 1},
                         ],
             }

    LIG = [
        {
            'name': 'LIG_POTASH',
            'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': icmap['LIG_POTASH'],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'fcoeSettings': {'fcoeMode': 'FcfNpv'},
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None,
            'uplinkSets': [],
        }
    ]

    SAS_LIG = [
        {
            "name": "LIG_SAS",
            "state": "Active",
            "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
            "enclosureType": "SY12000",
            "interconnectMapTemplate": icmap["LIG_SAS"],
            "enclosureIndexes": [1],
            "interconnectBaySet": 1,
        }
    ]

    EG = [{'name': EG_NAME,
           'type': ENCLOSURE_GROUP_TYPE,
           'enclosureCount': 1,
           'enclosureTypeUri': '/rest/enclosure-types/SY12000',
           'stackingMode': 'Enclosure',
           'interconnectBayMappingCount': 3,
           'configurationScript': None,
           'interconnectBayMappings': [{"interconnectBay": 3,
                                        "logicalInterconnectGroupUri": "LIG:" + LIG[0]["name"]},
                                       {"interconnectBay": 6,
                                        "logicalInterconnectGroupUri": "LIG:" + LIG[0]["name"]},
                                       {"interconnectBay": 1,
                                        "enclosureIndex": 1,
                                        "logicalInterconnectGroupUri": "SASLIG:" + SAS_LIG[0]["name"]},
                                       ],
           'ipAddressingMode': "External",
           'ipRangeUris': [],
           'powerMode': "RedundantPowerFeed"}]

    LE = {"name": "LE_SYNERGY",
          "enclosureUris": enc_list,
          "enclosureGroupUri": "EG:" + EG_NAME,
          "firmwareBaselineUri": None,
          "forceInstallFirmware": False}

    StorageSystems_Put = [{"type": STORAGE_SYSTEM_TYPE,
                           "hostname": "wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net",
                           "credentials": {"username": "fusionadm", "password": "hpvse1"},
                           "family": "StoreServ",
                           "name": "wpst3par-7200-7-srv",
                           "serialNumber": "1645767",
                           "category": "storage-systems",
                           "ports": [
                               {"type": "StorageTargetPortV4",
                                "name": "1:2:4",
                                "address": "21:24:00:02:AC:00:B2:C7",
                                "expectedNetworkUri": "FC:FA2",
                                "expectedSanName": "wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56",
                                "expectedSanUri": None
                                },
                               {"type": "StorageTargetPortV4",
                                "name": "1:2:3",
                                "address": "21:23:00:02:AC:00:B2:C7",
                                "expectedNetworkUri": "FC:FA1",
                                "expectedSanName": "wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55",
                                "expectedSanUri": None
                                },
                               {"type": "StorageTargetPortV4",
                                "name": "0:2:4",
                                "address": "20:24:00:02:AC:00:B2:C7",
                                "expectedNetworkUri": "FC:FA2",
                                "expectedSanName": "wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56",
                                "expectedSanUri": None
                                },
                               {"type": "StorageTargetPortV4",
                                "name": "0:2:3",
                                "address": "20:23:00:02:AC:00:B2:C7",
                                "expectedNetworkUri": "FC:FA1",
                                "expectedSanName": "wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55",
                                "expectedSanUri": None
                                },
                           ],
                           "deviceSpecificAttributes": {
                               "wwn": "28:11:00:02:AC:00:B2:C7",
                               "model": "HP_3PAR 7200",
                               "managedDomain": fc_domain,
                               "managedPools": [
                                   {"name": "FVT_Tbird_reg1_r1",
                                    "uuid": "409d9e7c-a99d-4e00-b9d5-f5fbf861a9e5",
                                    "domain": fc_domain,
                                    "deviceType": "FC",
                                    },
                                   {"name": "FVT_Tbird_reg1_r5",
                                    "uuid": "7d456b95-d2b7-4ef5-8f91-345d5a62476d",
                                    "domain": fc_domain,
                                    "deviceType": "FC",
                                    },
                                   {"name": "FVT_Tbird_reg1_r6",
                                    "uuid": "56c20b40-14b0-4694-a055-5f19f745cbe8",
                                    "domain": fc_domain,
                                    "deviceType": "FC",
                                    },
                               ],
                               "discoveredPools": [],
                               "discoveredDomains": [
                                   "NO DOMAIN",
                                   "wpst8",
                                   "wpst9",
                                   "wpst22",
                                   "wpst23",
                                   "wpst26",
                                   "wpst30",
                                   "wpst31",
                                   "wpst32",
                                   "wpst33",
                                   "wpst34",
                                   "wpst20",
                                   "FVT_C7000_reg1",
                                   fc_domain
                               ],
                           },
                           },
                          {"type": STORAGE_SYSTEM_TYPE,
                           "hostname": "fvt3par-8400-1-srv.vse.rdlabs.hpecorp.net",
                           "credentials": {"username": "3paradm", "password": "3pardata"},
                           "family": "StoreServ",
                           "name": "fvt3par-8400-1-srv",
                           "managedDomain": fcoe_domain,
                           "serialNumber": "MXN6262MRY",
                           "uri": "fvt3par-8400-1-srv",
                           "ports": [
                               {"type": "StorageTargetPortV4",
                                "address": "22:21:00:02:AC:01:AF:55",
                                "name": "2:2:1",
                                "expectedNetworkUri": "FCOE:FCoE1",
                                "expectedSanUri": None
                                },
                               {"type": "StorageTargetPortV4",
                                "address": "23:21:00:02:AC:01:AF:55",
                                "name": "3:2:1",
                                "expectedNetworkUri": "FCOE:FCoE1",
                                "expectedSanUri": None
                                },
                               {"type": "StorageTargetPortV4",
                                "address": "22:22:00:02:AC:01:AF:55",
                                "name": "2:2:2",
                                "expectedNetworkUri": "FCOE:FCoE2",
                                "expectedSanUri": None
                                },
                               {"type": "StorageTargetPortV4",
                                "address": "23:22:00:02:AC:01:AF:55",
                                "name": "3:2:2",
                                "expectedNetworkUri": "FCOE:FCoE2",
                                "expectedSanUri": None
                                },
                           ],
                           "deviceSpecificAttributes": {
                               "managedDomain": fcoe_domain,
                               "managedPools": [
                                   {"domain": fcoe_domain,
                                    "name": "FC_r1",
                                    "deviceType": "FC",
                                    "uuid": "895362b2-d2b7-4660-b3c5-ee241d704cd1"
                                    },
                                   {"domain": fcoe_domain,
                                    "name": "FC_r5",
                                    "deviceType": "FC",
                                    "uuid": "c95f7da6-7803-4183-bbe9-08d78120b191"
                                    }
                               ],
                               "discoveredPools": [],
                               "discoveredDomains": []
                           }
                           }
                          ]

    VolumeTemplates = [
        {
            'name': '%s-FA-VT1-Thin-1GB-R5-Private' %
            enc_names[0].upper(),
            'description': '',
            'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
            'properties': {
                'storageSystem': 'wpst3par-7200-7-srv',
                'name': {
                    'title': 'Volume name',
                    'description': 'A volume name between 1 and 100 characters',
                    'type': 'string',
                    'minLength': 1,
                    'maxLength': 100,
                    'required': True,
                    'meta': {
                        'locked': False}},
                'description': {
                    'title': 'Description',
                    'description': 'A description for the volume',
                    'type': 'string',
                    'minLength': 0,
                    'maxLength': 2000,
                    'default': '3Par1 pool1 private',
                    'meta': {
                            'locked': False}},
                'storagePool': {
                    'title': 'Storage Pool',
                    'description': 'A common provisioning group URI reference',
                    'type': 'string',
                    'required': True,
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': False,
                        'createOnly': True,
                        'semanticType': 'device-storage-pool'},
                    'default': 'FVT_Tbird_reg1_r6'},
                'size': {
                    'title': 'Capacity',
                    'description': 'The capacity of the volume in bytes',
                    'type': 'integer',
                    'required': True,
                    'minimum': 1073741824,
                    'maximum': 17592186044416,
                    'meta': {
                        'locked': False,
                        'semanticType': 'capacity'},
                    'default': 1073741824,
                },
                'isShareable': {
                    'title': 'Is Shareable',
                    'description': 'The shareability of the volume',
                    'type': 'boolean',
                    'meta': {
                        'locked': False},
                    'default': False,
                },
                'provisioningType': {
                    'title': 'Provisioning Type',
                    'description': 'The provisioning type for the volume',
                    'type': 'string',
                    'enum': [
                        'Thin',
                        'Full'],
                    'meta': {
                        'locked': True,
                        'createOnly': True},
                    'default': 'Thin'},
                'snapshotPool': {
                    'title': 'Snapshot Pool',
                    'description': 'A URI referenceto the common provisioning group used to create snapshots',
                    'type': 'string',
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': True,
                        'semanticType': 'device-snapshot-storage-pool'},
                    'default': 'FVT_Tbird_reg1_r5'}},
        },
        {
            'name': '%s-FA-VT2-Full-1GB-R5-Private' %
            enc_names[0].upper(),
            'description': '',
            'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
            'properties': {
                'storageSystem': 'wpst3par-7200-7-srv',
                'name': {
                    'title': 'Volume name',
                    'description': 'A volume name between 1 and 100 characters',
                    'type': 'string',
                    'minLength': 1,
                    'maxLength': 100,
                    'required': True,
                    'meta': {
                        'locked': False}},
                'description': {
                    'title': 'Description',
                    'description': 'A description for the volume',
                    'type': 'string',
                    'minLength': 0,
                    'maxLength': 2000,
                    'default': '3Par1 pool1 private',
                    'meta': {
                        'locked': False}},
                'storagePool': {
                    'title': 'Storage Pool',
                    'description': 'A common provisioning group URI reference',
                    'type': 'string',
                    'required': True,
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': False,
                        'createOnly': True,
                        'semanticType': 'device-storage-pool'},
                    'default': 'FVT_Tbird_reg1_r6'},
                'size': {
                    'title': 'Capacity',
                    'description': 'The capacity of the volume in bytes',
                    'type': 'integer',
                    'required': True,
                    'minimum': 1073741824,
                    'maximum': 17592186044416,
                    'meta': {
                        'locked': False,
                        'semanticType': 'capacity'},
                    'default': 1073741824,
                },
                'isShareable': {
                    'title': 'Is Shareable',
                    'description': 'The shareability of the volume',
                    'type': 'boolean',
                    'meta': {
                        'locked': False},
                    'default': False,
                },
                'provisioningType': {
                    'title': 'Provisioning Type',
                    'description': 'The provisioning type for the volume',
                    'type': 'string',
                    'enum': [
                        'Thin',
                        'Full'],
                    'meta': {
                        'locked': True,
                        'createOnly': True},
                    'default': 'Full'},
                'snapshotPool': {
                    'title': 'Snapshot Pool',
                    'description': 'A URI referenceto the common provisioning group used to create snapshots',
                    'type': 'string',
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': True,
                        'semanticType': 'device-snapshot-storage-pool'},
                    'default': 'FVT_Tbird_reg1_r5'}},
        },
        {
            'name': '%s-FA-VT3-Thin-1GB-R5-Shared' %
            enc_names[0].upper(),
            'description': '',
            'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
            'properties': {
                'storageSystem': 'wpst3par-7200-7-srv',
                'name': {
                    'title': 'Volume name',
                    'description': 'A volume name between 1 and 100 characters',
                    'type': 'string',
                    'minLength': 1,
                    'maxLength': 100,
                    'required': True,
                    'meta': {
                        'locked': False}},
                'description': {
                    'title': 'Description',
                    'description': 'A description for the volume',
                    'type': 'string',
                    'minLength': 0,
                    'maxLength': 2000,
                    'default': '3Par1 pool1 private',
                    'meta': {
                        'locked': False}},
                'storagePool': {
                    'title': 'Storage Pool',
                    'description': 'A common provisioning group URI reference',
                    'type': 'string',
                    'required': True,
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': False,
                        'createOnly': True,
                        'semanticType': 'device-storage-pool'},
                    'default': 'FVT_Tbird_reg1_r6'},
                'size': {
                    'title': 'Capacity',
                    'description': 'The capacity of the volume in bytes',
                    'type': 'integer',
                    'required': True,
                    'minimum': 1073741824,
                    'maximum': 17592186044416,
                    'meta': {
                        'locked': False,
                        'semanticType': 'capacity'},
                    'default': 1073741824,
                },
                'isShareable': {
                    'title': 'Is Shareable',
                    'description': 'The shareability of the volume',
                    'type': 'boolean',
                    'meta': {
                        'locked': False},
                    'default': False,
                },
                'provisioningType': {
                    'title': 'Provisioning Type',
                    'description': 'The provisioning type for the volume',
                    'type': 'string',
                    'enum': [
                        'Thin',
                        'Full'],
                    'meta': {
                        'locked': True,
                        'createOnly': True},
                    'default': 'Thin'},
                'snapshotPool': {
                    'title': 'Snapshot Pool',
                    'description': 'A URI referenceto the common provisioning group used to create snapshots',
                    'type': 'string',
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': True,
                        'semanticType': 'device-snapshot-storage-pool'},
                    'default': 'FVT_Tbird_reg1_r5'}},
        },
        {
            'name': '%s-FCoE-VT1-Thin-1GB-R5-Private' %
            enc_names[0].upper(),
            'description': '',
            'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
            'properties': {
                'storageSystem': 'fvt3par-8400-1-srv',
                'name': {
                    'title': 'Volume name',
                    'description': 'A volume name between 1 and 100 characters',
                    'type': 'string',
                    'minLength': 1,
                    'maxLength': 100,
                    'required': True,
                    'meta': {
                        'locked': False}},
                'description': {
                    'title': 'Description',
                    'description': 'A description for the volume',
                    'type': 'string',
                    'minLength': 0,
                    'maxLength': 2000,
                    'default': '3Par1 pool1 private',
                    'meta': {
                        'locked': False}},
                'storagePool': {
                    'title': 'Storage Pool',
                    'description': 'A common provisioning group URI reference',
                    'type': 'string',
                    'required': True,
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': False,
                        'createOnly': True,
                        'semanticType': 'device-storage-pool'},
                    'default': 'FC_r1'},
                'size': {
                    'title': 'Capacity',
                    'description': 'The capacity of the volume in bytes',
                    'type': 'integer',
                    'required': True,
                    'minimum': 1073741824,
                    'maximum': 17592186044416,
                    'meta': {
                        'locked': False,
                        'semanticType': 'capacity'},
                    'default': 1073741824,
                },
                'isShareable': {
                    'title': 'Is Shareable',
                    'description': 'The shareability of the volume',
                    'type': 'boolean',
                    'meta': {
                        'locked': False},
                    'default': False,
                },
                'provisioningType': {
                    'title': 'Provisioning Type',
                    'description': 'The provisioning type for the volume',
                    'type': 'string',
                    'enum': [
                        'Thin',
                        'Full'],
                    'meta': {
                        'locked': True,
                        'createOnly': True},
                    'default': 'Thin'},
                'snapshotPool': {
                    'title': 'Snapshot Pool',
                    'description': 'A URI referenceto the common provisioning group used to create snapshots',
                    'type': 'string',
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': True,
                        'semanticType': 'device-snapshot-storage-pool'},
                    'default': 'FC_r1',
                }},
        },
        {
            'name': '%s-FCoE-VT2-Full-1GB-R5-Private' %
            enc_names[0].upper(),
            'description': '',
            'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
            'properties': {
                'storageSystem': 'fvt3par-8400-1-srv',
                'name': {
                    'title': 'Volume name',
                    'description': 'A volume name between 1 and 100 characters',
                    'type': 'string',
                    'minLength': 1,
                    'maxLength': 100,
                    'required': True,
                    'meta': {
                        'locked': False}},
                'description': {
                    'title': 'Description',
                    'description': 'A description for the volume',
                    'type': 'string',
                    'minLength': 0,
                    'maxLength': 2000,
                    'default': '3Par1 pool1 private',
                    'meta': {
                        'locked': False}},
                'storagePool': {
                    'title': 'Storage Pool',
                    'description': 'A common provisioning group URI reference',
                    'type': 'string',
                    'required': True,
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': False,
                        'createOnly': True,
                        'semanticType': 'device-storage-pool'},
                    'default': 'FC_r1',
                },
                'size': {
                    'title': 'Capacity',
                    'description': 'The capacity of the volume in bytes',
                    'type': 'integer',
                    'required': True,
                    'minimum': 1073741824,
                    'maximum': 17592186044416,
                    'meta': {
                        'locked': False,
                        'semanticType': 'capacity'},
                    'default': 1073741824,
                },
                'isShareable': {
                    'title': 'Is Shareable',
                    'description': 'The shareability of the volume',
                    'type': 'boolean',
                    'meta': {
                        'locked': False},
                    'default': False,
                },
                'provisioningType': {
                    'title': 'Provisioning Type',
                    'description': 'The provisioning type for the volume',
                    'type': 'string',
                    'enum': [
                        'Thin',
                        'Full'],
                    'meta': {
                        'locked': True,
                        'createOnly': True},
                    'default': 'Full'},
                'snapshotPool': {
                    'title': 'Snapshot Pool',
                    'description': 'A URI referenceto the common provisioning group used to create snapshots',
                    'type': 'string',
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': True,
                        'semanticType': 'device-snapshot-storage-pool'},
                    'default': 'FC_r1',
                }},
        },
        {
            'name': '%s-FCoE-VT3-Thin-1GB-R5-Shared' %
            enc_names[0].upper(),
            'description': '',
            'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
            'properties': {
                'storageSystem': 'fvt3par-8400-1-srv',
                'name': {
                    'title': 'Volume name',
                    'description': 'A volume name between 1 and 100 characters',
                    'type': 'string',
                    'minLength': 1,
                    'maxLength': 100,
                    'required': True,
                    'meta': {
                        'locked': False}},
                'description': {
                    'title': 'Description',
                    'description': 'A description for the volume',
                    'type': 'string',
                    'minLength': 0,
                    'maxLength': 2000,
                    'default': '3Par1 pool1 private',
                    'meta': {
                        'locked': False}},
                'storagePool': {
                    'title': 'Storage Pool',
                    'description': 'A common provisioning group URI reference',
                    'type': 'string',
                    'required': True,
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': False,
                        'createOnly': True,
                        'semanticType': 'device-storage-pool'},
                    'default': 'FC_r1',
                },
                'size': {
                    'title': 'Capacity',
                    'description': 'The capacity of the volume in bytes',
                    'type': 'integer',
                    'required': True,
                    'minimum': 1073741824,
                    'maximum': 17592186044416,
                    'meta': {
                        'locked': False,
                        'semanticType': 'capacity'},
                    'default': 1073741824,
                },
                'isShareable': {
                    'title': 'Is Shareable',
                    'description': 'The shareability of the volume',
                    'type': 'boolean',
                    'meta': {
                        'locked': False},
                    'default': False,
                },
                'provisioningType': {
                    'title': 'Provisioning Type',
                    'description': 'The provisioning type for the volume',
                    'type': 'string',
                    'enum': [
                        'Thin',
                        'Full'],
                    'meta': {
                        'locked': True,
                        'createOnly': True},
                    'default': 'Thin'},
                'snapshotPool': {
                    'title': 'Snapshot Pool',
                    'description': 'A URI referenceto the common provisioning group used to create snapshots',
                    'type': 'string',
                    'format': 'x-uri-reference',
                    'meta': {
                        'locked': True,
                        'semanticType': 'device-snapshot-storage-pool'},
                    'default': 'FC_r1',
                }},
        },
    ]

    Volumes = [{'properties': {'name': '%s-FA-Vol1-Thin-1GB-R5-Private' % enc_names[0].upper(),
                               'storagePool': 'FVT_Tbird_reg1_r6',
                               'storageSystem': 'wpst3par-7200-7-srv',
                               'size': 1073741824,
                               'provisioningType': 'Thin',
                               'isShareable': True,
                               'snapshotPool': 'FVT_Tbird_reg1_r5'},
                'templateUri': '%s-FA-VT1-Thin-1GB-R5-Private' % enc_names[0].upper(),
                'isPermanent': True},
               {'properties': {'name': '%s-FA-Vol2-Full-1GB-R5-Private' % enc_names[0].upper(),
                               'storagePool': 'FVT_Tbird_reg1_r6',
                               'storageSystem': 'wpst3par-7200-7-srv',
                               'size': 1073741824,
                               'provisioningType': 'Full',
                               'isShareable': False,
                               'snapshotPool': 'FVT_Tbird_reg1_r5', },
                'templateUri': '%s-FA-VT2-Full-1GB-R5-Private' % enc_names[0].upper(),
                'isPermanent': True},
               {'properties': {'name': '%s-FA-Vol3-Thin-1GB-R5-Shared' % enc_names[0].upper(),
                               'storagePool': 'FVT_Tbird_reg1_r6',
                               'storageSystem': 'wpst3par-7200-7-srv',
                               'size': 1073741824,
                               'provisioningType': 'Thin',
                               'isShareable': True,
                               'snapshotPool': 'FVT_Tbird_reg1_r5', },
                'templateUri': '%s-FA-VT3-Thin-1GB-R5-Shared' % enc_names[0].upper(),
                'isPermanent': True},
               {'properties': {'name': '%s-FCoE-Vol1-Thin-1GB-R5-Private' % enc_names[0].upper(),
                               'storagePool': 'FC_r1',
                               'storageSystem': 'fvt3par-8400-1-srv',
                               'size': 1073741824,
                               'provisioningType': 'Thin',
                               'isShareable': True,
                               'snapshotPool': 'FC_r1'},
                'templateUri': '%s-FCoE-VT1-Thin-1GB-R5-Private' % enc_names[0].upper(),
                'isPermanent': True},
               {'properties': {'name': '%s-FCoE-Vol2-Full-1GB-R5-Private' % enc_names[0].upper(),
                               'storagePool': 'FC_r1',
                               'storageSystem': 'fvt3par-8400-1-srv',
                               'size': 1073741824,
                               'provisioningType': 'Full',
                               'isShareable': False,
                               'snapshotPool': 'FC_r1', },
                'templateUri': '%s-FCoE-VT2-Full-1GB-R5-Private' % enc_names[0].upper(),
                'isPermanent': True},
               {'properties': {'name': '%s-FCoE-Vol3-Thin-1GB-R5-Shared' % enc_names[0].upper(),
                               'storagePool': 'FC_r1',
                               'storageSystem': 'fvt3par-8400-1-srv',
                               'size': 1073741824,
                               'provisioningType': 'Thin',
                               'isShareable': True,
                               'snapshotPool': 'FC_r1', },
                'templateUri': '%s-FCoE-VT3-Thin-1GB-R5-Shared' % enc_names[0].upper(),
                'isPermanent': True},
               ]

    server_profile = [{
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": 'SH:{}'.format(SH_NAME),
        "enclosureGroupUri": EG_NAME,
        "enclosureUri": ENC[0],
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "SP1",
        "description": "",
        "affinity": "Bay",
        "connections": [],
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
    }]

    resources_names = ["LE:%s" % LE["name"],
                       "LI:%s-%s" % (LE["name"], LIG[0]["name"]),
                       "SASLI:%s-%s-1" % (LE["name"], SAS_LIG[0]["name"]),
                       "IC:%s" % ENC1ICBAY3,
                       "IC:%s" % ENC1ICBAY6,
                       # "ENC:%s" % ENC1,
                       "SH:%s" % ENC1SHBAY4,
                       "SH:%s" % ENC1SHBAY6,
                       "SH:%s" % ENC1SHBAY7,
                       "SH:%s" % ENC1SHBAY8,
                       "SH:%s" % ENC1SHBAY9,
                       "SP:%s" % server_profile[0]["name"],
                       "SSYS:%s" % StorageSystems_Put[0]["name"],
                       "SSYS:%s" % StorageSystems_Put[1]["name"],
                       ]
# -- End

CSRinfo = {
    "type": "CertificateDtoV2",
    "country": "US",
    "state": "California",
    "locality": "Palo Alto",
    "organization": "Hewlett Packard Enterprise",
    "commonName": "",
    "organizationalUnit": "",
    "alternativeName": "",
    "contactPerson": "",
    "email": "",
    "surname": "",
    "givenName": "",
    "initials": "",
    "dnQualifier": "",
    "unstructuredName": "",
    "challengePassword": "",
}

appliance_cert = {
    "base64Data": '',
    "type": "CertificateDataV2"
}


# -- Shan
Directory_Type = "LoginDomainConfigVersion200"
DirectoryGroup_Type = "Group2RolesMappingPerGroupValidationDto"
AD_IP = "15.114.113.178"
LDAP_IP = "15.114.114.1"
REPO_IP = "16.114.218.204"
IPDU182_IP = "16.125.33.182"
ok_status = "OK"

addldaprequestbody_3_10 = {
    "type": Directory_Type,
    "name": "TestLdap",
    "credential": {
        "userName": "admin",
        "password": "admin"},
    "authProtocol": "LDAP",
    "orgUnits": [
        "ou=users",
        "ou=People",
        "ou=Groups"],
    "userNamingAttribute": "UID",
    "baseDN": "dc=ov,dc=cn",
    "directoryServers": [
        {
            "type": "LoginDomainDirectoryServerInfoDto",
                    "directoryServerSSLPortNumber": "636",
                    "directoryServerIpAddress": LDAP_IP,
                    "directoryServerCertificateStatus": "",
                    "serverStatus": "",
                    "directoryServerCertificateBase64Data": ""}]}

createldapgrouprequestbody_3_10 = {
    "type": DirectoryGroup_Type,
    "group2rolesPerGroup": {
        "type": "Group2RolesMappingPerGroupDto",
        "loginDomain": "TestLdap",
        "egroup": "cn=FUSION_SVR_ADMIN,ou=Groups,dc=ov,dc=cn",
        "roles": ["Server administrator"]},
    "credentials": {
        "userName": "admin",
        "password": "admin"}}

addadrequestbody_3_10 = {
    "type": Directory_Type,
    "name": "TestAD",
    "credential": {
        "userName": "administrator",
        "password": "#EDC2wsx!QAZ"},
    "authProtocol": "AD",
    "orgUnits": [],
    "userNamingAttribute": "UID",
    "baseDN": "dc=adserver,dc=com",
    "directoryServers": [
        {
            "type": "LoginDomainDirectoryServerInfoDto",
            "directoryServerSSLPortNumber": "636",
            "directoryServerIpAddress": AD_IP,
            "directoryServerCertificateStatus": "",
            "serverStatus": "",
            "directoryServerCertificateBase64Data": ""}]}

createadgrouprequestbody_3_10 = {
    "type": DirectoryGroup_Type,
    "group2rolesPerGroup": {
        "type": "Group2RolesMappingPerGroupDto",
        "loginDomain": "TestAD",
        "egroup": "CN=Administrators,CN=Builtin,DC=adserver,DC=com",
        "roles": ["Server administrator"]},
    "credentials": {
        "userName": "Administrator",
        "password": "#EDC2wsx!QAZ"}}

ad_user = {
    'userName': 'testuser2',
    'password': '!QAZ2wsx#EDC',
    'authLoginDomain': 'TestAD'}

ldap_user = {
    'userName': 'test',
    'password': 'test',
    'authLoginDomain': 'TestLdap'}

addselfsignedreporequestbody = {
    "repositoryName": "TestRepo",
    "repositoryURI": "https://%s/webdav" % REPO_IP,
    "userName": "joanna",
    "password": "joanna",
    "base64Data": ""}

addipducertificate = {
    "aliasName": IPDU182_IP,
    "type": "SSLCertificateDTO",
    "base64SSLCertData": "",
    "status": None,
    "verifyRevocationStatus": False,
    "verifyTrustChainAndRevocation": False}

addipdurequestbody = {
    "hostname": IPDU182_IP,
    "username": "admin",
    "password": "admin",
    "force": True}

ValidateFirmwares = [
    "1.7.0.0",
    "1.0.1.0",
    "10.7.221.0",
    "2016.10.0",
    "2017.07.0",
    "4.99",
    "HPG6"]

FirmwareVersions = [
    "1.7.0.0",
    "1.0.1.0",
    "10.7.221.0",
    "2016.10.0",
    "2017.07.0",
    "4.99",
    "HPG6"]
