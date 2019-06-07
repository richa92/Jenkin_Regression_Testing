'''
SAT SYNERGY RING2 GEN1 Data File

'''

from dynamicdata import DynamicData
from collections import OrderedDict
import copy

from pysphere import VIServer
import ssl

# Python 2.7.9+ has issues with unverified certs this is a workaround
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by  default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
# end workaround


def get_status_of_vm(host, user, password, vm_name):
    """
        Takes VI server details, VM name and returns the status of the VM
        [Example]
        ${resp} = get status of vm  | <host> | <user> | <password> | <vm_name>
    """
    vi_obj = VIServer()
    vi_obj.connect(host, user, password)
    get_vm_obj = vi_obj.get_vm_by_name(vm_name)
    return get_vm_obj.get_status()


DD = DynamicData()

spp_version_li = '2018.05.08.00'

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

ilo_credentials = {'username': 'Administrator',
                   'password': 'Cosmos123'
                   }

dhcpservers = [{'ip': '10.146.0.11', 'vlanid': '1167', 'scope': '10.167.0.0',
                'username': 'Administrator', 'password': 'Cosmos123'}]

esxi_os_servers = [{"name": "frame1_fc_bay3", 'serverHardwareUri': 'frame1, bay 3'},
                   {"name": "frame1_fc_bay4", 'serverHardwareUri': 'frame1, bay 4'},
                   {"name": "frame1_fc_bay9", 'serverHardwareUri': 'frame1, bay 9'}]

enclosure = [{'serialNumber': 'MXQ8190017', 'newName': 'frame1'},
             {'serialNumber': 'MXQ82104X2', 'newName': 'frame2'},
             {'serialNumber': 'MXQ82104X6', 'newName': 'frame3'}]

support_dump = [{"errorCode": "CI", "encrypt": True,
                 "userName": "Administrator", "password": "Cosmos123"}]

le_support_dump_prebuildup = [{"name": "LE",
                               "errorCode": "LESD1",
                               "encrypt": False,
                               "excludeApplianceDump": False}]

le_support_dump_postexec = [{"name": "LE",
                             "errorCode": "LESD1",
                             "encrypt": False,
                             "excludeApplianceDump": False}]

licenses = [{'key': 'YBYE CQEA H9PA CHXZ V2B4 HWWV Y9JL KMPL LJ2A PGVQ DXAU 2CSM GHTG L762 2ET7 FQV9 KJVT D5KM EFVW TSNJ K4UP 536G SMT9 YGS6 SMQQ MUCF 4WCN MYN7 N2QS LHJQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TX83 T45F NGG3 EHM4 "EVAL-N3R43A_NFR N3R43A_NFR Synergy_8Gb_FC_Upgrade_License_NFR EVAL-N3R43A_NFR"'},
            {'key': 'QB9A DQEA H9PY 8HXY V2B4 HWWV Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 6S74 ERB4 KJVT D5KM EFVW TSNJ YF4J 86CS SMT9 YGS6 SMQQ MUCF UW2L MYN7 N2QC DHKQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TVPT 74UF NGGT EHM4 "EVAL-N3R43A_ILR N3R43A_ILR Synergy_8Gb_FC_Upgrade_License EVAL-N3R43A_ILR"'},
            {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

ad_directory = [{'name': 'AD', 'baseDN': 'DC=dom1120,DC=lab', 'userName': 'Administrator', 'password': 'Cosmos123',
                 'directoryServerSSLPortNumber': '636', 'directoryServerIpAddress': '10.120.0.10',
                 'directoryServerCertificateBase64Data': "-----BEGIN CERTIFICATE-----\nMIIFizCCA3OgAwIBAgIQX683Rjb/mZJL5I5psfyIPTANBgkqhkiG9w0BAQ0FADBMMRMwEQYKCZImiZPyLGQBGRYDbGFiMRcwFQYKCZImiZPyLGQBGRYHZG9tMTEyMDEcMBoGA1UEAxMTZG9tMTEyMC1SSVNULUFEUy1DQTAeFw0xODAxMDkxNzMyMTRaFw0yMzAxMDkxNzQyMTJaMEwxEzARBgoJkiaJk/IsZAEZFgNsYWIxFzAVBgoJkiaJk/IsZAEZFgdkb20xMTIwMRwwGgYDVQQDExNkb20xMTIwLVJJU1QtQURTLUNBMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvIBRmndaN5Mdsl0PuOmjRATEqbU3Y40e10OPXZmjdoiqJNIDqvEXUCOCfAnK7Hfcx8/qcoWojlL+ah9GaaounGAloCss3C1kmWW6LYPgzhqB/o6y6uHUrt3vjD2rOZ6sGdYKjzJRXqCjb+lTTOlZ9t1vsH6l+HQ65wHHMYMBmiAik6aZLULA1jp+nstpVs7DS+lrSTbR6cGoRCR/BjfD2aOWluoHBVxf9Ub8CQXiuNQV2ow3Nax7rxjox+GB32JsxsnTm7ICU0XT5bTp0werTVD96WMs+CmBqZoXjBVbkQ+roDzhCi8OtJJBdqqpnAntZaj9zR/g1zEgvNzoNt7lUbrwDfHIKdT2JZxG35cXzIOwZl4wIhDxgv6dUGQh4emxV+bhfitcDm9YEaSXaJrAFDYfIV7KeFLCRO3KGLoXKssIz5jjr0D+rLLEyrDYcNkzKzxF6NA2ESbDN0J4a7kitdI9aqDgUeEhSK/S1jK2tr+ji7zK5Q1YU3QE2eh7IVg5ug0bvr7eZv5xYGmQrRWiP6KD1mROCV6/RLezgNLsqICYeDeDIjf70mXQibXUQxCOzwlF8zleXxXfm6ptkRkiXPA4pDLeC+NYDyO9xqwygNYdpfhrbxhzp0GoMhISF1pwGjVMW9zFftiKBN6lrKoP5DtJpIXW3rlBhmi6Vn8YcDUCAwEAAaNpMGcwEwYJKwYBBAGCNxQCBAYeBABDAEEwDgYDVR0PAQH/BAQDAgGGMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFEy4YjctbqgWfnV7/qfpqzGE5w3sMBAGCSsGAQQBgjcVAQQDAgEAMA0GCSqGSIb3DQEBDQUAA4ICAQCTw3tVAyVtN/lrJN8OHEhjh2SmRjeRh6SksTMEWfKhDKQKu8fROr8fkniXDXX0xxBddcGANVcn0aNZU43mlhI7MMHKE7ixCzJ+jrjKFldVQPZypchh83gaa6A4KegioUeCa9QVhwGSZqeQPn9V6A3h0Ts9YzvNCl9YGOJ/TcMEwVMeSMYqx/mBS/2KVCK5TZSV7L2VquEOwFAUH2FJ8nlHSOMfWW50aipMrwSthWffINasrFFhc5jE49YKoim4r20oPbSiEkpYKqQ3PB1ID7r6tWljxbgg8JEA6IaNIZQj+PszL5zLnJndAj0+mKncLKxJxqJIbyet3o2q3S7DZ/h1GYr9JGKMzLG4yGPc39jlfKtqGRShM0BkK+9p+3veomd5PB2rNK3fsCAz2lH2mp+UB2OobxLV4GzEV2YLzhVKjSvGeqoVdWGObK+Lgyp+KEhm9OE9W8Y0s6xEmXyYfyJS5zpQkk04vhBJRL0LMotCgSf/eJEbMFH0xuPkWhILO90I9C66WeF6vlwxqpwx3yWlfyGEsGeFYSPUp1bBAsF6DrIEC3fn9mT88GphHHR9Nd6xitV5RZZM7VCg10Ellw54fT0jpGZfn/ypxsIIj+z0PQ+7b1uHMGkXwghNJZLgLJRFv5hIlrqKhSTKhU/XHXil6ZplmUP+fac2Ty8JDpsZZA==\n-----END CERTIFICATE-----"}]

ad_backup_credentials = {'userName': 'ad_backup_user', 'password': 'Cosmos123', 'authLoginDomain': 'AD',
                         'loginMsgAck': 'True'}

ad_infra_credentials = {'userName': 'ad_infra_user', 'password': 'Cosmos123', 'authLoginDomain': 'AD',
                        'loginMsgAck': 'True'}

ad_network_credentials = {'userName': 'ad_network_user', 'password': 'Cosmos123', 'authLoginDomain': 'AD',
                          'loginMsgAck': 'True'}

ad_readonly_credentials = {'userName': 'ad_readonly_user', 'password': 'Cosmos123', 'authLoginDomain': 'AD',
                           'loginMsgAck': 'True'}

ad_server_credentials = {'userName': 'ad_server_user', 'password': 'Cosmos123', 'authLoginDomain': 'AD',
                         'loginMsgAck': 'True'}

ad_storage_credentials = {'userName': 'ad_storage_user', 'password': 'Cosmos123', 'authLoginDomain': 'AD',
                          'loginMsgAck': 'True'}

adgroup = [{'userName': 'ad_backup_user', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'backup_group',
            "permissions": [{"roleName": "Backup administrator", "scopeUri": None}]},
           {'userName': 'ad_network_user', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'network_group',
            "permissions": [{"roleName": "Network administrator", "scopeUri": None}]},
           {'userName': 'ad_readonly_user', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'readonly_group',
            "permissions": [{"roleName": "Read only", "scopeUri": None}]},
           {'userName': 'ad_server_user', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'server_group',
            "permissions": [{"roleName": "Server administrator", "scopeUri": None}]},
           {'userName': 'ad_storage_user', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'storage_group',
            "permissions": [{"roleName": "Storage administrator", "scopeUri": None}]}]

spp_name = 'bp-2018-11-14'
spp_version = '2018.11.14.00'

forceinstallfirmware = 'True'
firmwareupdateOn = 'EnclosureOnly'
li_updatemode = 'Parallel'
firmwarebaseline = '2018.11.14.00'

updated_spp_name = DD.spp_name_withunderscore(spp_name)

buildup_spp_name = 'bp-2018-11-14'
buildup_spp_version = '2018.11.14.00'

spp_local_dir = 'C:/spp/'

spps = [{'name': 'bp-2018-01-14-01', 'localpath': 'C:/spp/'}]

firmware = {'manageFirmware': False,
            'forceInstallFirmware': False, 'firmwareInstallType': None}

spp_local_paths = DD.get_spp_details(spps)
buildup_spp_local_paths = [DD.get_spp_path(buildup_spp_name, spp_local_dir)]

number_of_session = 100

remotesupport_edit = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                      {'op': 'replace', 'path': '/configuration/companyName',
                       'value': 'HPE'},
                      {'op': 'replace',
                       'path': '/configuration/marketingOptIn', 'value': True},
                      {"op": "replace",
                       "path": "/configuration/autoEnableDevices", "value": True},
                      {'op': 'add', 'path': '/sites/default1',
                       'value': {'name': 'DEFAULT SITE', 'streetAddress1': 'Compaq Center Dr', 'streetAddress2': '',
                                 'city': 'Houston', 'provinceState': 'TX',
                                 'postalCode': '', 'timeZone': 'US/Central', 'countryCode': 'US', 'type': 'Site',
                                 'default': True}},
                      {'op': 'add', 'path': '/contacts',
                       'value': {'contactKey': 'default', 'firstName': 'FFFa', 'lastName': 'LLL',
                                 'email': 'ffff.lll19@hpe.com', 'primaryPhone': '8884442222',
                                 'alternatePhone': '', 'notes': '', 'language': 'en', 'default': True,
                                 'type': 'Contact'}}]

sans = [{'Type': 'Brocade Network Advisor',
         'Host': '10.120.1.160',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'Cosmos123', 'UseSsl': True},
        {'Type': 'HPE',
         'Host': '10.120.1.155',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'}
        ]

ethernet_networks = [
    {'name': 'iscsi_1121', 'type': 'ethernet-networkV4', 'vlanId': 1121, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'iscsi_1122', 'type': 'ethernet-networkV4', 'vlanId': 1122, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False}
]

ethernet_name_prefix = "eth"

ethernets = [{"vlanIdStart": 1123, "vlanIdEnd": 1872, "purpose": "General", "namePrefix": ethernet_name_prefix,
              "smartLink": True, "privateNetwork": False,
              "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV1"}]

postbackup_ethernet_networks = [
    {'name': 'postbackup_iscsi_1', 'type': 'ethernet-networkV4', 'vlanId': 1, 'purpose': 'ISCSI', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_iscsi_2', 'type': 'ethernet-networkV4', 'vlanId': 2, 'purpose': 'ISCSI', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_eth_1146', 'type': 'ethernet-networkV4', 'vlanId': 1146, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_eth_1147', 'type': 'ethernet-networkV4', 'vlanId': 1147, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_eth_1148', 'type': 'ethernet-networkV4', 'vlanId': 1148, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False}
]

untagged_tunnel_eth = [{'name': 'untagged', 'ethernetNetworkType': 'Untagged'},
                       {'name': 'tunnel', 'ethernetNetworkType': 'Tunnel'}]

fcs = [
    {'count': 1, 'base_name': 'fc_a',
     'associatedSAN': 'FC-SAN-Fabric-A'},
    {'count': 1, 'base_name': 'fc_b',
     'associatedSAN': 'FC-SAN-Fabric-B'},
]

fcoes = [{'base_name': 'fcoe_a', 'vlanId': 3405, 'san': 'VSAN3405', 'count': 1},
         {'base_name': 'fcoe_b', 'vlanId': 3406, 'san': 'VSAN3406', 'count': 1}]

network_set = [{'namePrefix': 'ns_15', 'count': 1, 'netNamePrefix': 'eth_', 'netNameSuffix': 1123, 'netPerNS': 150, 'nativeNetworkUri': 'eth_1167'},
               {'namePrefix': 'ns_30', 'count': 1, 'netNamePrefix': 'eth_',
                   'netNameSuffix': 1273, 'netPerNS': 150, 'nativeNetworkUri': None},
               {'namePrefix': 'ns_45', 'count': 1, 'netNamePrefix': 'eth_',
                   'netNameSuffix': 1423, 'netPerNS': 150, 'nativeNetworkUri': None},
               {'namePrefix': 'ns_60', 'count': 1, 'netNamePrefix': 'eth_',
                   'netNameSuffix': 1573, 'netPerNS': 150, 'nativeNetworkUri': None},
               {'namePrefix': 'ns_75', 'count': 1, 'netNamePrefix': 'eth_', 'netNameSuffix': 1723, 'netPerNS': 150, 'nativeNetworkUri': None}]

storage_system = [{'name': 'HPE_3PAR_8200_ISCSI_EPIC', 'hostname': '10.120.1.48', 'username': 'cosmos', 'password': 'Insight7',
                   'managedDomain': 'SAT-Synergy', 'managedPools': [], 'serialNumber': '2M271500PZ'},
                  {'name': 'cosmosp7200', 'hostname': '10.120.1.158', 'username': 'cosmos', 'password': 'Insight7',
                   'managedDomain': "SAT_SY_GEN1_R2", 'managedPools': [], 'serialNumber': '1675719'}]

storage_pools_toedit = [{"storageSystemUri": 'cosmosp7200', "name": 'SAT_SY_GEN1_R2_FC_FCoE'},
                        {"storageSystemUri": 'HPE_3PAR_8200_ISCSI_EPIC', "name": 'SAT-SY-R1'}]

storage_system_post = [{'name': 'tbr13par', 'hostname': '10.120.1.7', 'username': 'cosmos', 'password': 'Insight7',
                        'managedDomain': 'TB4', 'managedPools': [], 'serialNumber': '1649938'}]

storage_pools_toedit_manage = [
    {"storageSystemUri": 'tbr13par', "name": 'TB4-Raid5-FC', "isManaged": True}]

storage_pools_toedit_discover = [
    {"storageSystemUri": 'tbr13par', "name": 'TB4-Raid5-FC', "isManaged": False}]

enc_groups = [{'name': 'EG', 'enclosureCount': 3,
               'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                           {'interconnectBay': 6,
                                               'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                           {'enclosureIndex': 2, 'interconnectBay': 1,
                                               'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                           {'enclosureIndex': 2, 'interconnectBay': 4,
                                               'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                           {'enclosureIndex': 3, 'interconnectBay': 1,
                                               'logicalInterconnectGroupUri': 'SASLIG:LIG_Natasha'},
                                           {'enclosureIndex': 3, 'interconnectBay': 4,
                                               'logicalInterconnectGroupUri': 'SASLIG:LIG_Natasha'},
                                           ],
               'ipAddressingMode': 'DHCP', 'ipRangeUris': [], 'powerMode': 'RedundantPowerFeed'}]

expected_encgroups = [{"type": "EnclosureGroupV8", "uri": "EG:EG", "category": "enclosure-groups", "name": "EG",
                       "status": "REGEX:OK|Unknown", "state": "Normal", "enclosureTypeUri": "/rest/enclosure-types/SY12000",
                       "stackingMode": "Enclosure", "portMappingCount": 8, "portMappings": [{"midplanePort": 1, "interconnectBay": 1},
                                                                                            {"midplanePort": 2, "interconnectBay": 2},
                                                                                            {"midplanePort": 3, "interconnectBay": 3},
                                                                                            {"midplanePort": 4, "interconnectBay": 4},
                                                                                            {"midplanePort": 5, "interconnectBay": 5},
                                                                                            {"midplanePort": 6, "interconnectBay": 6},
                                                                                            {"midplanePort": 7, "interconnectBay": 7},
                                                                                            {"midplanePort": 8, "interconnectBay": 8}],
                       "interconnectBayMappingCount": 6,
                       'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                                   {'interconnectBay': 6,
                                                       'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                                   {'enclosureIndex': 2, 'interconnectBay': 1,
                                                       'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                                   {'enclosureIndex': 2, 'interconnectBay': 4,
                                                    'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                                   {'enclosureIndex': 3, 'interconnectBay': 1,
                                                    'logicalInterconnectGroupUri': 'SASLIG:LIG_Natasha'},
                                                   {'enclosureIndex': 3, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:LIG_Natasha'}],
                       "ipAddressingMode": "DHCP", "ipRangeUris": [], "powerMode": "RedundantPowerFeed", "description": None,
                       "associatedLogicalInterconnectGroups": ["LIG:LIG_Potash", "LIG:LIG_Natasha"], "enclosureCount": 3}]


logical_enclosure = [{'name': 'LE', 'enclosureUris': [
    'ENC:frame1', 'ENC:frame2', 'ENC:frame3'], 'enclosureGroupUri': 'EG:EG'}]

refresh_enclosures = [{"name": "frame1"}, {
    "name": "frame2"}, {"name": "frame3"}]

expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "LE:LE",
        "status": "OK",
        "name": "LE",
        "enclosureUris": [
            "ENC:frame1",
            "ENC:frame2",
            "ENC:frame3"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]

le_firmware_update = [
    {
        "type": "LogicalEnclosureV4",
        "status": "OK",
        "name": "LE",
        "enclosureUris": [
            "ENC:frame3",
            "ENC:frame1",
            "ENC:frame2"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]

potash_eth_1167 = [
    "eth_" + str(j) for i in ethernets if i["namePrefix"] == "eth" for j in range(1123, 1872)]

uplink_sets = {
    "carbon_fc1": {'name': 'fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                   'networkUris': ['fc_a1'], 'mode': 'Auto',
                   'logicalPortConfigInfos': [{
                       "speed": "Auto",
                       "bay": "1",
                       "enclosure": "-1",
                       "port": "6"
                   }, {
                       "speed": "Auto",
                       "bay": "1",
                       "enclosure": "-1",
                       "port": "5"
                   }, {
                       "speed": "Auto",
                       "bay": "1",
                       "enclosure": "-1",
                       "port": "4"
                   }, {
                       "speed": "Auto",
                       "bay": "1",
                       "enclosure": "-1",
                       "port": "3"
                   }, {
                       "speed": "Auto",
                       "bay": "1",
                       "enclosure": "-1",
                       "port": "2"
                   }, {
                       "speed": "Auto",
                       "bay": "1",
                       "enclosure": "-1",
                       "port": "1"
                   }]},
    "carbon_fc2": {'name': 'fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                   'networkUris': ['fc_b1'], 'mode': 'Auto',
                   'logicalPortConfigInfos': [{
                       "speed": "Auto",
                       "bay": "4",
                       "enclosure": "-1",
                       "port": "6"
                   }, {
                       "speed": "Auto",
                       "bay": "4",
                       "enclosure": "-1",
                       "port": "5"
                   }, {
                       "speed": "Auto",
                       "bay": "4",
                       "enclosure": "-1",
                       "port": "4"
                   }, {
                       "speed": "Auto",
                       "bay": "4",
                       "enclosure": "-1",
                       "port": "3"
                   }, {
                       "speed": "Auto",
                       "bay": "4",
                       "enclosure": "-1",
                       "port": "2"
                   }, {
                       "speed": "Auto",
                       "bay": "4",
                       "enclosure": "-1",
                       "port": "1"
                   }]},
    "potash_eth": {'name': 'eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                   'networkUris': potash_eth_1167, 'mode': 'Auto',
                   'logicalPortConfigInfos': [
                       {
                           "speed": "Auto",
                           "enclosure": "1",
                           "port": "Q1",
                           "bay": "3"
                       },
                       {
                           "speed": "Auto",
                           "enclosure": "2",
                           "port": "Q1",
                           "bay": "6"
                       }
                   ]},
    "potash_iscsi1": {
        "ethernetNetworkType": "Tagged",
        "lacpTimer": "Short",
        "logicalPortConfigInfos": [
            {
                "speed": "Auto",
                "port": "Q2",
                "enclosure": "1",
                "bay": "3"
            }
        ],
        "mode": "Auto",
        "name": "iscsi1",
        "nativeNetworkUri": None,
        "networkType": "Ethernet",
        "networkUris": [
            "iscsi_1121"
        ],
        "primaryPort": None
    },
    "potash_iscsi2": {
        "ethernetNetworkType": "Tagged",
        "lacpTimer": "Short",
        "logicalPortConfigInfos": [
            {
                "speed": "Auto",
                "port": "Q2",
                "enclosure": "2",
                "bay": "6"
            }
        ],
        "mode": "Auto",
        "name": "iscsi2",
        "nativeNetworkUri": None,
        "networkType": "Ethernet",
        "networkUris": [
            "iscsi_1122"
        ],
        "primaryPort": None
    },
    "potash_fcoe1": {
        "ethernetNetworkType": "Tagged",
        "lacpTimer": "Short",
        "logicalPortConfigInfos": [
            {
                "speed": "Auto",
                "port": "Q3",
                "enclosure": "1",
                "bay": "3"
            },
            {
                "speed": "Auto",
                "enclosure": "1",
                "port": "Q4",
                "bay": "3"
            }
        ],
        "mode": "Auto",
        "name": "fcoe1",
        "nativeNetworkUri": None,
        "networkType": "Ethernet",
        "networkUris": [
            "fcoe_a1"
        ],
        "primaryPort": None
    },
    "potash_fcoe2": {
        "ethernetNetworkType": "Tagged",
        "lacpTimer": "Short",
        "logicalPortConfigInfos": [
            {
                "speed": "Auto",
                "port": "Q3",
                "enclosure": "2",
                "bay": "6"
            },
            {
                "speed": "Auto",
                "enclosure": "2",
                "port": "Q4",
                "bay": "6"
            }
        ],
        "mode": "Auto",
        "name": "fcoe2",
        "nativeNetworkUri": None,
        "networkType": "Ethernet",
        "networkUris": [
            "fcoe_b1"
        ],
        "primaryPort": None
    },
    "potash_fc1": {'name': 'fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                   'networkUris': ['fc_a1'], 'mode': 'Auto',
                   'logicalPortConfigInfos': [{
                       "speed": "Auto",
                       "enclosure": "1",
                       "port": "Q5:1",
                       "bay": "3"
                   }, {
                       "speed": "Auto",
                       "enclosure": "1",
                       "port": "Q6:1",
                       "bay": "3"
                   }]},
    "potash_fc2": {'name': 'fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                   'networkUris': ['fc_b1'], 'mode': 'Auto',
                   'logicalPortConfigInfos': [{
                       "speed": "Auto",
                       "enclosure": "2",
                       "port": "Q5:1",
                       "bay": "6"
                   }, {
                       "speed": "Auto",
                       "enclosure": "2",
                       "port": "Q6:1",
                       "bay": "6"
                   }]},
}

ligs = [{'status': None, 'category': None, 'enclosureIndexes': [-1], 'name': 'LIG_Carbon', 'created': None,
         'internalNetworkUris': [], 'qosConfiguration': {'status': None, 'modified': None, 'eTag': None,
                                                         'activeQosConfig': {'status': None, 'description': None,
                                                                             'uri': None, 'eTag': None,
                                                                             'qosTrafficClassifiers': None,
                                                                             'category': 'qos-aggregated-configuration',
                                                                             'name': None, 'created': None,
                                                                             'modified': None,
                                                                             'configType': 'Passthrough', 'state': None,
                                                                             'downlinkClassificationType': None,
                                                                             'uplinkClassificationType': None,
                                                                             'type': 'QosConfiguration'},
                                                         'category': 'qos-aggregated-configuration', 'name': None,
                                                         'created': None, 'uri': None, 'state': None,
                                                         'inactiveFCoEQosConfig': None,
                                                         'inactiveNonFCoEQosConfig': None,
                                                         'type': 'qos-aggregated-configuration'}, 'modified': None,
         'uplinkSets': [uplink_sets["carbon_fc1"].copy(), uplink_sets["carbon_fc2"].copy()],
         'uri': None, 'enclosureType': 'SY12000', 'state': None, 'eTag': None,
         'interconnectMapTemplate': [
             {'type': 'Virtual Connect SE 16Gb FC Module for Synergy',
                 'enclosure': -1, 'enclosureIndex': -1, 'bay': 4},
             {'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosure': -1, 'enclosureIndex': -1,
              'bay': 1}],
         'ethernetSettings': None, 'redundancyType': 'Redundant', 'type': 'logical-interconnect-groupV7',
         'interconnectBaySet': 1, 'description': None},
        {'status': None, 'category': None, 'enclosureIndexes': [1, 2, 3], 'name': 'LIG_Potash', 'created': None,
         'internalNetworkUris': [], 'qosConfiguration': {'status': None, 'modified': None, 'eTag': None,
                                                         'activeQosConfig': {'status': None, 'description': None,
                                                                             'uri': None, 'eTag': None,
                                                                             'qosTrafficClassifiers': None,
                                                                             'category': 'qos-aggregated-configuration',
                                                                             'name': None, 'created': None,
                                                                             'modified': None,
                                                                             'configType': 'Passthrough', 'state': None,
                                                                             'downlinkClassificationType': None,
                                                                             'uplinkClassificationType': None,
                                                                             'type': 'QosConfiguration'},
                                                         'category': 'qos-aggregated-configuration', 'name': None,
                                                         'created': None, 'uri': None, 'state': None,
                                                         'inactiveFCoEQosConfig': None,
                                                         'inactiveNonFCoEQosConfig': None,
                                                         'type': 'qos-aggregated-configuration'}, 'modified': None,
         'uplinkSets': [uplink_sets["potash_eth"].copy(), uplink_sets["potash_fcoe1"].copy(),
                        uplink_sets["potash_fc1"].copy(
         ), uplink_sets["potash_fcoe2"].copy(),
            uplink_sets["potash_fc2"].copy(), uplink_sets["potash_iscsi1"].copy(), uplink_sets["potash_iscsi2"].copy()], 'uri': None, 'enclosureType': 'SY12000', 'state': None,
         'eTag': None,
         'interconnectMapTemplate': [
            {'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosure': 1, 'enclosureIndex': 1, 'bay': 3},
            {'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosure': 1, 'enclosureIndex': 1, 'bay': 6},
            {'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosure': 3, 'enclosureIndex': 3, 'bay': 3},
            {'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
             'enclosure': 2, 'enclosureIndex': 2, 'bay': 6},
            {'type': 'Synergy 20Gb Interconnect Link Module',
             'enclosure': 3, 'enclosureIndex': 3, 'bay': 6},
            {'type': 'Synergy 20Gb Interconnect Link Module', 'enclosure': 2, 'enclosureIndex': 2, 'bay': 3}],
         'ethernetSettings': None, 'redundancyType': 'HighlyAvailable', 'type': 'logical-interconnect-groupV7',
         'interconnectBaySet': 3, 'description': None}]

regx_us = "[0-9a-fA-F]"
regex_uuid = "%s{8}(-%s{4}){3}-%s{12}" % (regx_us, regx_us, regx_us)

validate_uplink_eth1 = ["REGEX:/rest/ethernet-networks/%s" %
                        (regex_uuid) for i in ethernets if i["namePrefix"] == "eth1" for j in range(1123, 1872)]

expected_lig = [{'enclosureType': 'SY12000', 'type': 'logical-interconnect-groupV7', 'name': 'LIG_Potash',
                 'uplinkSets': [{'networkUris': validate_uplink_eth1, 'name': 'eth'},
                                {'networkUris': [
                                    'ETH:iscsi_1121'], 'name': 'iscsi1'},
                                {'networkUris': [
                                    'ETH:iscsi_1122'], 'name': 'iscsi2'},
                                {'networkUris': [
                                    'ETH:fcoe_a1'], 'name': 'fcoe1'},
                                {'networkUris': [
                                    'FC:fc_a1'], 'name': 'fc1'},
                                {'networkUris': [
                                    'ETH:fcoe_b1'], 'name': 'fcoe2'},
                                {'networkUris': ['FC:fc_b1'], 'name': 'fc2'}]},
                {'enclosureType': 'SY12000', 'type': 'logical-interconnect-groupV7', 'name': 'LIG_Carbon',
                 'uplinkSets': [{'networkUris': ['FC:fc_a1'], 'name': 'fc1'},
                                {'networkUris': ['FC:fc_b1'], 'name': 'fc2'}]}]

expected_lig = {"members": expected_lig}

sas_lig = [{"name": "LIG_Natasha",
            "type": "sas-logical-interconnect-groupV2",
            "enclosureType": "SY12000",
            "description": None,
            "status": None,
            "state": None,
            "category": None,
            "created": None,
            "modified": None,
            "eTag": None,
            "uri": None,
            'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                                        {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1}],
            'interconnectBaySet': 1,
            'enclosureIndexes': [1]}
           ]

expected_sas_lig = [{"name": "LIG_Natasha",
                     "type": "sas-logical-interconnect-groupV2",
                     "enclosureType": "SY12000",
                     "description": None,
                     "status": 'OK',
                     "state": 'Active',
                     "uri": 'SASLIG:LIG_Natasha',
                     'interconnectBaySet': 1,
                     'enclosureIndexes': [1]}]

sas_li_name = "LE-LIG_Natasha-3"

potash_li_name = "LE-LIG_Potash"
carbon_li_name = "LE-LIG_Carbon"

expected_lig = {"members": expected_lig}

storage_volume_templates = [
    {'name': 'frame1_priv_vol', "rootTemplateUri": "frame1_priv_vol",
        'default': 'SAT_SY_GEN1_R2_FC_FCoE'},
    {'name': 'frame2_priv_vol', "rootTemplateUri": "frame2_priv_vol",
        'default': 'SAT_SY_GEN1_R2_FC_FCoE'},
    {'name': 'frame3_priv_vol', "rootTemplateUri": "frame3_priv_vol", 'default': 'SAT-SY-R1'}]

storage_volume_templates_post = [
    {'name': 'frame1_priv_vol_2', "rootTemplateUri": "frame1_priv_vol_2", 'default': 'SAT_SY_GEN1_R2_FC_FCoE'}]

edit_storage_volume_templates = [{
    "isRoot": False, "properties":
    {"name": {"meta": {"locked": False},
              "type": "string",
              "title": "Volume name",
              "required": True,
              "maxLength": 100,
              "minLength": 1,
              "description": "A volume name between 1 and 100 characters"},
        "size": {"meta": {"locked": False, "semanticType": "capacity"},
                 "type": "integer",
                 "title": "Capacity",
                 "default": 10737418240,
                 "maximum": 17592186044416, "minimum": 1073741824,
                 "required": True, "description": "The capacity of the volume in bytes"},
        "description": {"meta": {"locked": False},
                        "type": "string",
                        "title": "Description",
                        "default": "",
                        "maxLength": 2000, "minLength": 0,
                        "description": "A description for the volume"},
        "isShareable": {"meta": {"locked": False},
                        "type": "boolean", "title": "Is Shareable", "default": False, "description": "The shareability of the volume"},
        "storagePool": {"meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                        "type": "string", "title": "Storage Pool",
                        "format": "x-uri-reference",
                        "default": "SAT_SY_GEN1_R2_FC_FCoE",
                        "required": True, "description": "A common provisioning group URI reference"},
        "snapshotPool": {"meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                         "type": "string", "title": "Snapshot Pool",
                         "format": "x-uri-reference",
                         "default": "SAT_SY_GEN1_R2_FC_FCoE",
                         "description": "A URI reference to the common provisioning group used to create snapshots"},
        "isDeduplicated": {"meta": {"locked": False},
                           "type": "boolean",
                           "title": "Is Deduplicated",
                           "default": False, "description": "Enables or disables deduplication of the volume"},
        "templateVersion": {"meta": {"locked": True},
                            "type": "string",
                            "title": "Template version", "default": "1.1",
                            "required": True, "description": "Version of the template"},
        "provisioningType": {"enum": ["Thin", "Full"],
                             "meta":{"locked": True, "createOnly": True},
                             "type": "string", "title": "Provisioning Type",
                             "default": "Full", "description": "The provisioning type for the volume"}},
    "family": "StoreServ",
    "storagePoolUri": "SAT_SY_GEN1_R2_FC_FCoE",
        "name": "frame1_priv_vol_2",
        "description": "private non-boot volume template",
        "category": "storage-volume-templates",
        "type": "StorageVolumeTemplateV6"}]

expected_edit_storage_volume_templates = [{
    "isRoot": False, "properties":
    {"name": {"meta": {"locked": False},
              "type": "string",
              "title": "Volume name",
              "required": True,
              "maxLength": 100,
              "minLength": 1,
              "description": "A volume name between 1 and 100 characters"},
        "size": {"meta": {"locked": False, "semanticType": "capacity"},
                 "type": "integer",
                 "title": "Capacity",
                 "default": 10737418240,
                 "maximum": 17592186044416, "minimum": 1073741824,
                 "required": True, "description": "The capacity of the volume in bytes"},
        "description": {"meta": {"locked": False},
                        "type": "string",
                        "title": "Description",
                        "default": "",
                        "maxLength": 2000, "minLength": 0,
                        "description": "A description for the volume"},
        "isShareable": {"meta": {"locked": False},
                        "type": "boolean", "title": "Is Shareable", "default": False, "description": "The shareability of the volume"},
        "storagePool": {"meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                        "type": "string", "title": "Storage Pool",
                        "format": "x-uri-reference",
                        "default": "SP:SAT_SY_GEN1_R2_FC_FCoE",
                        "required": True, "description": "A common provisioning group URI reference"},
        "snapshotPool": {"meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                         "type": "string", "title": "Snapshot Pool",
                         "format": "x-uri-reference",
                         "default": "SP:SAT_SY_GEN1_R2_FC_FCoE",
                         "description": "A URI reference to the common provisioning group used to create snapshots"},
        "isDeduplicated": {"meta": {"locked": False},
                           "type": "boolean",
                           "title": "Is Deduplicated",
                           "default": False, "description": "Enables or disables deduplication of the volume"},
        "templateVersion": {"meta": {"locked": True},
                            "type": "string",
                            "title": "Template version", "default": "1.1",
                            "required": True, "description": "Version of the template"},
        "provisioningType": {"enum": ["Thin", "Full"],
                             "meta":{"locked": True, "createOnly": True},
                             "type": "string", "title": "Provisioning Type",
                             "default": "Full", "description": "The provisioning type for the volume"}},
    "family": "StoreServ",
    "storagePoolUri": "SP:SAT_SY_GEN1_R2_FC_FCoE",
        "name": "frame1_priv_vol_2",
        "description": "private non-boot volume template",
        "category": "storage-volume-templates",
        "type": "StorageVolumeTemplateV6"}]

new_storage_volumes = [{"name": "frame1_bay3_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame1_bay4_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame1_bay5_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame1_bay6_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame1_bay9_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame1_bay10_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame1_bay11_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame1_bay12_fc_pri_vol", "templateUri": "frame1_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame2_bay1_fc_pri_vol", "templateUri": "frame2_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame2_bay2_fc_pri_vol", "templateUri": "frame2_priv_vol",
                        "isShareable": False, "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                       {"name": "frame3_bay3_iscsi_pri_vol", "templateUri": "frame3_priv_vol",
                        "isShareable": False, "storagePool": "SAT-SY-R1"},
                       {"name": "frame3_bay4_iscsi_pri_vol", "templateUri": "frame3_priv_vol",
                        "isShareable": False, "storagePool": "SAT-SY-R1"},
                       {"name": "frame3_bay5_iscsi_pri_vol", "templateUri": "frame3_priv_vol",
                        "isShareable": False, "storagePool": "SAT-SY-R1"},
                       {"name": "frame3_bay6_iscsi_pri_vol", "templateUri": "frame3_priv_vol",
                        "isShareable": False, "storagePool": "SAT-SY-R1"}
                       ]

three_par_host_name = [{"name": "frame3_iscsi_bay3"}, {"name": "frame3_iscsi_bay4"}, {
    "name": "frame3_iscsi_bay5"}, {"name": "frame3_iscsi_bay6"}]

potash_iscsi_shared_volumes = [{"name": "frame3_iscsi_share_vol1",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol2",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol3",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol4",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol5",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol6",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol7",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol8",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol9",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol10",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol11",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol12",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol13",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol14",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol15",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "frame3_iscsi_share_vol16",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"}
                               ]

potash_fc_shared_volumes = [{"name": "frame1_fc_share_vol1",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol2",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol3",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol4",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol5",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol6",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol7",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol8",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol9",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol10",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol11",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol12",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol13",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol14",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol15",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                            {"name": "frame1_fc_share_vol16",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"}
                            ]

potash_fcoe_shared_volumes = [{"name": "frame2_fcoe_share_vol1",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol2",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol3",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol4",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol5",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol6",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol7",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol8",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol9",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol10",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol11",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol12",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol13",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol14",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol15",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                              {"name": "frame2_fcoe_share_vol16",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"}
                              ]


exec_storage_volume_name = 'exec_volume1_toedit'

new_storage_volumes_post = [{"name": exec_storage_volume_name, "storagePool": "TB4-Raid5-FC",
                             "templateUri": "ROOT", "isShareable": False, "snapshotPool": "TB4-Raid5-FC"},
                            {"name": "exec_volume2_toedit", "templateUri": "ROOT",
                             "isShareable": False, "storagePool": "TB4-Raid5-FC"},
                            {"name": "exec_volume3_toedit", "templateUri": "ROOT",
                             "isShareable": False, "storagePool": "TB4-Raid5-FC"}
                            ]

exec_edit_storage_volumes = [{"name": exec_storage_volume_name, "provisionedCapacity": "37212254720"},
                             {"name": "exec_volume2_toedit", "isShareable": True}]

exec_expected_edit_storage_volumes = [
    {"name": exec_storage_volume_name, "provisionedCapacity": "37212254720", 'status': 'OK', 'state': 'Managed',
     'type': 'StorageVolumeV6'},
    {"name": "exec_volume2_toedit", "isShareable": True, 'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'}]

exec_storage_volumes_snapshot_name = "snapshot1"

exec_storage_volumes_snapshot = [{"storage_volume_name": "exec_volume1_toedit", "name": exec_storage_volumes_snapshot_name,
                                  "description": ""}]

exec_expected_storage_vol_snapshot_dto = [{"storage_volume_name": "exec_volume1_toedit",
                                           "members": [{"type": "SnapshotV2", "status": "OK",
                                                        "name": exec_storage_volumes_snapshot_name}]}]

exec_delete_storage_volumes_snapshots = [{"storage_volume_name": "exec_volume1_toedit",
                                          "snapshot_name": exec_storage_volumes_snapshot_name}]

exec_delete_storage_volumes = [
    {"name": exec_storage_volume_name}, {"name": "exec_volume2_toedit"}, {"name": "exec_volume3_toedit"}]

exec_storage_system_to_remove = ['tbr13par']

rack_name = 'MyRack'

racks = [{
    "name": rack_name,
    "depth": 710,
    "height": 2150,
    "width": 1344,
    "rackMounts": [
        {
            "uHeight": 10,
            "mountUri": "ENC:frame1",
            "topUSlot": 20
        },
        {
            "uHeight": 10,
            "mountUri": "ENC:frame2",
            "topUSlot": 30
        },
        {
            "uHeight": 10,
            "mountUri": "ENC:frame3",
            "topUSlot": 10,
        }
    ]
}]

dc = [{'name': 'Datacenter 1', 'width': 7199, 'depth': 2999, 'contents': [
    {'resourceUri': '', 'y': 0, 'x': 0}]}]


scopes = [{"name": "fc1", "description": "", "type": "ScopeV3",
           "addedResourceUris": ["FC:fc_a1"], "removedResourceUris":[], "initialScopeUris":[]},
          {"name": "fcoe1", "description": "", "type": "ScopeV3", "addedResourceUris": [
              "FCOE:fcoe_a1"], "removedResourceUris":[], "initialScopeUris":[]},
          {"name": "eth", "description": "", "type": "ScopeV3", "addedResourceUris": [
              "ETH:tunnel_8"], "removedResourceUris":[], "initialScopeUris":[]}
          ]

adgroup_scope = [{'userName': 'ad_infra_user', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'infra_group',
                  "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope:eth'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope:fc1'},
                                  {"roleName": "Infrastructure administrator",
                                      "scopeUri": 'Scope:fcoe1'}
                                  ]}]

expected_adgroup_withscope = [{'category': 'users', 'loginDomain': 'AD', 'type': 'LoginDomainGroupPermission',
                               'egroup': 'infra_group',
                               'permissions': [{"roleName": "Infrastructure administrator", "scopeUri": 'eth'}, {'roleName': 'Infrastructure administrator', 'scopeUri': 'fc1'},
                                               {'roleName': 'Infrastructure administrator', 'scopeUri': 'fcoe1'}]}]

# end

scopes_postupgrade = [{"name": "fc2", "description": "", "type": "ScopeV3",
                       "addedResourceUris": ["FC:fc_b1"], "removedResourceUris":[], "initialScopeUris":[]},
                      {"name": "fcoe2", "description": "", "type": "ScopeV3", "addedResourceUris": [
                          "FCOE:fcoe_b1"], "removedResourceUris":[], "initialScopeUris":[]},
                      {"name": "eth2", "description": "", "type": "ScopeV3", "addedResourceUris": [
                          "ETH:tunnel_9"], "removedResourceUris":[], "initialScopeUris":[]}
                      ]


adgroup_scope_postupgrade = [{'userName': 'ad_infra_user_exec', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'exec_infra_group',
                              "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope:eth2'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope:fc2'},
                                              {"roleName": "Infrastructure administrator", "scopeUri": 'Scope:fcoe2'}]}]

expected_adgroup_withscope_postupgrade = [{'category': 'users', 'loginDomain': 'AD', 'type': 'LoginDomainGroupPermission',
                                           'egroup': 'exec_infra_group',
                                           'permissions': [{"roleName": "Infrastructure administrator", "scopeUri": 'eth2'}, {"roleName": "Infrastructure administrator", "scopeUri": 'fc2'},
                                                           {"roleName": "Infrastructure administrator", "scopeUri": 'fcoe2'}]}]

server_profile_templates = [{
    "type": "ServerProfileTemplateV5",
    "name": "frame1_spt",
    "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Physical",
    "serialNumberType": "Physical",
    "wwnType": "Physical",
    'connectionSettings': {"manageConnections": True,
                           'connections': [{'id': 1, 'name': 'ns_1123_1272_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 2, 'name': 'ns_1123_1272_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 3, 'name': 'fc_a', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '2500', 'networkUri': 'FC:fc_a1',
                                            'boot': {'priority': 'NotBootable'}},
                                           {"id": 4, "name": "fc_b", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                            "requestedMbps": "2500", "networkUri": "FC:fc_b1",
                                            "boot": {'priority': 'NotBootable'}},
                                           {'id': 5, 'name': 'ns_1273_1422_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 6, 'name': 'ns_1273_1422_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 7, 'name': 'eth_1423_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 8, 'name': 'eth_1423_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}}]},
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
    },
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': False, 'overriddenSettings': []},
    'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
    "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                   "volumeAttachments": [{
                       "id": 1,
                       "associatedTemplateAttachmentId": "uniqueid1",
                       "isBootVolume": False,
                       'lunType': 'Auto', 'lun': '',
                       "storagePaths": [{"isEnabled": True,
                                         "connectionId": 3,
                                         "targetSelector": "Auto",
                                         "targets": []},
                                        {"isEnabled": True,
                                         "connectionId": 4,
                                         "targetSelector": "Auto",
                                         "targets": []}],
                       "volume": {
                           "isPermanent": False,
                           "properties": {
                               "name": "frame1_priv_vol",
                               "description": "",
                               "storagePool": "SPOOL:" + "SAT_SY_GEN1_R2_FC_FCoE",
                               "size": 32213303296,
                               "provisioningType": "Thin",
                               "isShareable": False},
                           "templateUri": "ROOT:" + "SAT_SY_GEN1_R2_FC_FCoE",
                       },
                       "volumeStorageSystemUri": "SSYS:" + "cosmosp7200",
                       "volumeUri": None,
                   },
                       {'id': 2, 'volumeUri': 'SVOL:frame1_fc_share_vol1',
                        "associatedTemplateAttachmentId": "uniqueid2",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 3, 'volumeUri': 'SVOL:frame1_fc_share_vol2',
                        "associatedTemplateAttachmentId": "uniqueid3",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 4, 'volumeUri': 'SVOL:frame1_fc_share_vol3',
                        "associatedTemplateAttachmentId": "uniqueid4",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 5, 'volumeUri': 'SVOL:frame1_fc_share_vol4',
                        "associatedTemplateAttachmentId": "uniqueid5",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 6, 'volumeUri': 'SVOL:frame1_fc_share_vol5',
                        "associatedTemplateAttachmentId": "uniqueid6",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 7, 'volumeUri': 'SVOL:frame1_fc_share_vol6',
                        "associatedTemplateAttachmentId": "uniqueid7",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 8, 'volumeUri': 'SVOL:frame1_fc_share_vol7',
                        "associatedTemplateAttachmentId": "uniqueid8",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 9, 'volumeUri': 'SVOL:frame1_fc_share_vol8',
                        "associatedTemplateAttachmentId": "uniqueid9",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 10, 'volumeUri': 'SVOL:frame1_fc_share_vol9',
                        "associatedTemplateAttachmentId": "uniqueid10",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 11, 'volumeUri': 'SVOL:frame1_fc_share_vol10',
                        "associatedTemplateAttachmentId": "uniqueid11",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 12, 'volumeUri': 'SVOL:frame1_fc_share_vol11',
                        "associatedTemplateAttachmentId": "uniqueid12",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 13, 'volumeUri': 'SVOL:frame1_fc_share_vol12',
                        "associatedTemplateAttachmentId": "uniqueid13",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 14, 'volumeUri': 'SVOL:frame1_fc_share_vol13',
                        "associatedTemplateAttachmentId": "uniqueid14",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 15, 'volumeUri': 'SVOL:frame1_fc_share_vol14',
                        "associatedTemplateAttachmentId": "uniqueid15",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 16, 'volumeUri': 'SVOL:frame1_fc_share_vol15',
                        "associatedTemplateAttachmentId": "uniqueid16",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 17, 'volumeUri': 'SVOL:frame1_fc_share_vol16',
                        "associatedTemplateAttachmentId": "uniqueid17",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                   ]
                   }
}]

server_profiles_from_spt = [{
    'name': 'frame1_fc_bay3', 'serverHardwareUri': 'frame1, bay 3',
    'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay4', 'serverHardwareUri': 'frame1, bay 4',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay9', 'serverHardwareUri': 'frame1, bay 9',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay10', 'serverHardwareUri': 'frame1, bay 10',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'}]

spt_edit_data = [{
    "type": "ServerProfileTemplateV5",
    "name": "frame1_spt",
    "serverHardwareTypeUri": 'SHT:SY 480 Gen9 2:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Physical",
    "serialNumberType": "Physical",
    "wwnType": "Physical",
    'connectionSettings': {"manageConnections": True,
                           'connections': [{'id': 1, 'name': 'ns_1123_1272_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 2, 'name': 'ns_1123_1272_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 3, 'name': 'fc_a', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '2500', 'networkUri': 'FC:fc_a1',
                                            'boot': {'priority': 'NotBootable'}},
                                           {"id": 4, "name": "fc_b", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                            "requestedMbps": "2500", "networkUri": "FC:fc_b1",
                                            "boot": {'priority': 'NotBootable'}},
                                           {'id': 5, 'name': 'ns_1273_1422_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 6, 'name': 'ns_1273_1422_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 7, 'name': 'eth_1423_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 8, 'name': 'eth_1423_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}}]},
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
    },
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': False, 'overriddenSettings': []},
    'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
    "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                   "volumeAttachments": [{
                       "id": 1,
                       "associatedTemplateAttachmentId": "uniqueid1",
                       "isBootVolume": False,
                       'lunType': 'Auto', 'lun': '',
                       "storagePaths": [{"isEnabled": True,
                                         "connectionId": 3,
                                         "targetSelector": "Auto",
                                         "targets": []},
                                        {"isEnabled": True,
                                         "connectionId": 4,
                                         "targetSelector": "Auto",
                                         "targets": []}],
                       "volume": {
                           "isPermanent": False,
                           "properties": {
                               "name": "frame1_priv_vol",
                               "description": "",
                               "storagePool": "SPOOL:" + "SAT_SY_GEN1_R2_FC_FCoE",
                               "size": 32213303296,
                               "provisioningType": "Thin",
                               "isShareable": False},
                           "templateUri": "ROOT:" + "SAT_SY_GEN1_R2_FC_FCoE",
                       },
                       "volumeStorageSystemUri": "SSYS:" + "cosmosp7200",
                       "volumeUri": None,
                   },
                       {'id': 2, 'volumeUri': 'SVOL:frame1_fc_share_vol1',
                        "associatedTemplateAttachmentId": "uniqueid2",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 3, 'volumeUri': 'SVOL:frame1_fc_share_vol2',
                        "associatedTemplateAttachmentId": "uniqueid3",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 4, 'volumeUri': 'SVOL:frame1_fc_share_vol3',
                        "associatedTemplateAttachmentId": "uniqueid4",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 5, 'volumeUri': 'SVOL:frame1_fc_share_vol4',
                        "associatedTemplateAttachmentId": "uniqueid5",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 6, 'volumeUri': 'SVOL:frame1_fc_share_vol5',
                        "associatedTemplateAttachmentId": "uniqueid6",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 7, 'volumeUri': 'SVOL:frame1_fc_share_vol6',
                        "associatedTemplateAttachmentId": "uniqueid7",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 8, 'volumeUri': 'SVOL:frame1_fc_share_vol7',
                        "associatedTemplateAttachmentId": "uniqueid8",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 9, 'volumeUri': 'SVOL:frame1_fc_share_vol8',
                        "associatedTemplateAttachmentId": "uniqueid9",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 10, 'volumeUri': 'SVOL:frame1_fc_share_vol9',
                        "associatedTemplateAttachmentId": "uniqueid10",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 11, 'volumeUri': 'SVOL:frame1_fc_share_vol10',
                        "associatedTemplateAttachmentId": "uniqueid11",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 12, 'volumeUri': 'SVOL:frame1_fc_share_vol11',
                        "associatedTemplateAttachmentId": "uniqueid12",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 13, 'volumeUri': 'SVOL:frame1_fc_share_vol12',
                        "associatedTemplateAttachmentId": "uniqueid13",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 14, 'volumeUri': 'SVOL:frame1_fc_share_vol13',
                        "associatedTemplateAttachmentId": "uniqueid14",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 15, 'volumeUri': 'SVOL:frame1_fc_share_vol14',
                        "associatedTemplateAttachmentId": "uniqueid15",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 16, 'volumeUri': 'SVOL:frame1_fc_share_vol15',
                        "associatedTemplateAttachmentId": "uniqueid16",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 17, 'volumeUri': 'SVOL:frame1_fc_share_vol16',
                        "associatedTemplateAttachmentId": "uniqueid17",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                   ]
                   }
}]

server_profiles_from_spt_postupgrade = [{
    'name': 'frame1_fc_bay5', 'serverHardwareUri': 'frame1, bay 5',
    'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay6', 'serverHardwareUri': 'frame1, bay 6',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay11', 'serverHardwareUri': 'frame1, bay 11',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay12', 'serverHardwareUri': 'frame1, bay 12',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'}]

ethernet_name_prefix_system_validation = "net"

ethernetssystem_validation = [{"vlanIdStart": 1873, "vlanIdEnd": 2322, "purpose": "General", "namePrefix": ethernet_name_prefix_system_validation,
                               "smartLink": True, "privateNetwork": False,
                               "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV1"}]

network_set_system_validation = [{'namePrefix': 'ns_90', 'count': 1, 'netNamePrefix': 'net_', 'netNameSuffix': 1873, 'netPerNS': 150, 'nativeNetworkUri': None},
                                 {'namePrefix': 'ns_105', 'count': 1, 'netNamePrefix': 'net_', 'netNameSuffix': 2023, 'netPerNS': 150, 'nativeNetworkUri': None}]

update_network_sets_system_validation = [{"name": 'ns_750', "networkUris": [], "add_networkUris": [
    'net_2173'], "type": 'network-setV4', "nativeNetworkUri": None, "uri": ''}]

edit_network_set_system_validation = ['net_2173']

update_network_sets_rollback = [{"name": 'ns_750', "networkUris": [], "delete_networkUris": [
    'net_2173'], "type": 'network-setV4', "nativeNetworkUri": None, "uri": ''}]

potash_iscsi_shared_volumes_system_validation = [{"name": "frame3_iscsi_share_vol17",
                                                  "templateUri": "ROOT",
                                                  "isShareable": True,
                                                  "storagePool": "SAT-SY-R1"},
                                                 {"name": "frame3_iscsi_share_vol18",
                                                  "templateUri": "ROOT",
                                                  "isShareable": True,
                                                  "storagePool": "SAT-SY-R1"},
                                                 {"name": "frame3_iscsi_share_vol19",
                                                  "templateUri": "ROOT",
                                                  "isShareable": True,
                                                  "storagePool": "SAT-SY-R1"},
                                                 {"name": "frame3_iscsi_share_vol20",
                                                  "templateUri": "ROOT",
                                                  "isShareable": True,
                                                  "storagePool": "SAT-SY-R1"},
                                                 {"name": "frame3_iscsi_share_vol21",
                                                  "templateUri": "ROOT",
                                                  "isShareable": True,
                                                  "storagePool": "SAT-SY-R1"}]

potash_fc_shared_volumes_system_validation = [{"name": "frame1_fc_share_vol17",
                                               "templateUri": "ROOT",
                                               "isShareable": True,
                                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                              {"name": "frame1_fc_share_vol18",
                                               "templateUri": "ROOT",
                                               "isShareable": True,
                                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                              {"name": "frame1_fc_share_vol19",
                                               "templateUri": "ROOT",
                                               "isShareable": True,
                                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                              {"name": "frame1_fc_share_vol20",
                                               "templateUri": "ROOT",
                                               "isShareable": True,
                                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                              {"name": "frame1_fc_share_vol21",
                                               "templateUri": "ROOT",
                                               "isShareable": True,
                                               "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"}]

potash_fcoe_shared_volumes_system_validation = [{"name": "frame2_fcoe_share_vol17",
                                                 "templateUri": "ROOT",
                                                 "isShareable": True,
                                                 "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                                {"name": "frame2_fcoe_share_vol18",
                                                 "templateUri": "ROOT",
                                                 "isShareable": True,
                                                 "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                                {"name": "frame2_fcoe_share_vol19",
                                                 "templateUri": "ROOT",
                                                 "isShareable": True,
                                                 "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                                {"name": "frame2_fcoe_share_vol20",
                                                 "templateUri": "ROOT",
                                                 "isShareable": True,
                                                 "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"},
                                                {"name": "frame2_fcoe_share_vol21",
                                                 "templateUri": "ROOT",
                                                 "isShareable": True,
                                                 "storagePool": "SAT_SY_GEN1_R2_FC_FCoE"}]

edit_storage_volume_system_validations = [{"name": "frame1_bay3_fc_pri_vol", "provisionedCapacity": "37212254720"},
                                          {"name": "frame1_bay4_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame1_bay5_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame1_bay6_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame1_bay9_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame1_bay10_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame1_bay11_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame1_bay12_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame2_bay1_fc_pri_vol",
                                              "provisionedCapacity": "37212254720"},
                                          {"name": "frame2_bay2_fc_pri_vol", "provisionedCapacity": "37212254720"}]

expected_edit_storage_volumes_system_validation = [{"name": "frame1_bay3_fc_pri_vol", "provisionedCapacity": "37212254720", 'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame1_bay4_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame1_bay5_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame1_bay6_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame1_bay9_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame1_bay10_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame1_bay11_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame1_bay12_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame2_bay1_fc_pri_vol", "provisionedCapacity": "37212254720",
                                                       'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'},
                                                   {"name": "frame2_bay2_fc_pri_vol", "provisionedCapacity": "37212254720", 'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV6'}]

edit_server_profiles = [{'type': 'ServerProfileV9', 'name': 'frame1_fc_bay3',
                         'serverHardwareUri': 'frame1, bay 3',
                         'enclosureGroupUri': 'EG:EG',
                         'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                                                             {'id': 'AdminPhone',
                                                                              'value': '1800-123-4321'},
                                                                             {"id": "AdminEmail",
                                                                              "value": "sat.regression@hpe.com"}]}
                         }]

expected_edit_server_profiles = [
    {
        "type": "ServerProfileV9",
        "name": "frame1_fc_bay3",
        "status": "OK",
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                   {'id': 'AdminPhone',
                                    'value': '1800-123-4321'},
                                   {"id": "AdminEmail",
                                    "value": "sat.regression@hpe.com"}]
        }
    }
]

edit_server_profiles_template_data = [{
    "type": "ServerProfileTemplateV5",
    "name": "frame1_spt",
    "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Physical",
    "serialNumberType": "Physical",
    "wwnType": "Physical",
    'connectionSettings': {"manageConnections": True,
                           'connections': [{'id': 1, 'name': 'ns_1123_1272_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 2, 'name': 'ns_1123_1272_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 3, 'name': 'fc_a', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '2500', 'networkUri': 'FC:fc_a1',
                                            'boot': {'priority': 'NotBootable'}},
                                           {"id": 4, "name": "fc_b", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                            "requestedMbps": "2500", "networkUri": "FC:fc_b1",
                                            "boot": {'priority': 'NotBootable'}},
                                           {'id': 5, 'name': 'ns_1273_1422_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 6, 'name': 'ns_1273_1422_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 7, 'name': 'eth_1423_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1424',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 8, 'name': 'eth_1423_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1424',
                                            'boot': {'priority': 'NotBootable'}}]},
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
    },
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': False, 'overriddenSettings': []},
    'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
    "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                   "volumeAttachments": [{
                       "id": 1,
                       "associatedTemplateAttachmentId": "uniqueid1",
                       "isBootVolume": False,
                       'lunType': 'Auto', 'lun': '',
                       "storagePaths": [{"isEnabled": True,
                                         "connectionId": 3,
                                         "targetSelector": "Auto",
                                         "targets": []},
                                        {"isEnabled": True,
                                         "connectionId": 4,
                                         "targetSelector": "Auto",
                                         "targets": []}],
                       "volume": {
                           "isPermanent": False,
                           "properties": {
                               "name": "frame1_priv_vol",
                               "description": "",
                               "storagePool": "SPOOL:" + "SAT_SY_GEN1_R2_FC_FCoE",
                               "size": 32213303296,
                               "provisioningType": "Thin",
                               "isShareable": False},
                           "templateUri": "ROOT:" + "SAT_SY_GEN1_R2_FC_FCoE",
                       },
                       "volumeStorageSystemUri": "SSYS:" + "cosmosp7200",
                       "volumeUri": None,
                   },
                       {'id': 2, 'volumeUri': 'SVOL:frame1_fc_share_vol1',
                        "associatedTemplateAttachmentId": "uniqueid2",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 3, 'volumeUri': 'SVOL:frame1_fc_share_vol2',
                        "associatedTemplateAttachmentId": "uniqueid3",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 4, 'volumeUri': 'SVOL:frame1_fc_share_vol3',
                        "associatedTemplateAttachmentId": "uniqueid4",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 5, 'volumeUri': 'SVOL:frame1_fc_share_vol4',
                        "associatedTemplateAttachmentId": "uniqueid5",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 6, 'volumeUri': 'SVOL:frame1_fc_share_vol5',
                        "associatedTemplateAttachmentId": "uniqueid6",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 7, 'volumeUri': 'SVOL:frame1_fc_share_vol6',
                        "associatedTemplateAttachmentId": "uniqueid7",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 8, 'volumeUri': 'SVOL:frame1_fc_share_vol7',
                        "associatedTemplateAttachmentId": "uniqueid8",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 9, 'volumeUri': 'SVOL:frame1_fc_share_vol8',
                        "associatedTemplateAttachmentId": "uniqueid9",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 10, 'volumeUri': 'SVOL:frame1_fc_share_vol9',
                        "associatedTemplateAttachmentId": "uniqueid10",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 11, 'volumeUri': 'SVOL:frame1_fc_share_vol10',
                        "associatedTemplateAttachmentId": "uniqueid11",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 12, 'volumeUri': 'SVOL:frame1_fc_share_vol11',
                        "associatedTemplateAttachmentId": "uniqueid12",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 13, 'volumeUri': 'SVOL:frame1_fc_share_vol12',
                        "associatedTemplateAttachmentId": "uniqueid13",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 14, 'volumeUri': 'SVOL:frame1_fc_share_vol13',
                        "associatedTemplateAttachmentId": "uniqueid14",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 15, 'volumeUri': 'SVOL:frame1_fc_share_vol14',
                        "associatedTemplateAttachmentId": "uniqueid15",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 16, 'volumeUri': 'SVOL:frame1_fc_share_vol15',
                        "associatedTemplateAttachmentId": "uniqueid16",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 17, 'volumeUri': 'SVOL:frame1_fc_share_vol16',
                        "associatedTemplateAttachmentId": "uniqueid17",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 18, 'volumeUri': 'SVOL:frame1_fc_share_vol17',
                        "associatedTemplateAttachmentId": "uniqueid18",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 19, 'volumeUri': 'SVOL:frame1_fc_share_vol18',
                        "associatedTemplateAttachmentId": "uniqueid19",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 20, 'volumeUri': 'SVOL:frame1_fc_share_vol19',
                        "associatedTemplateAttachmentId": "uniqueid20",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 21, 'volumeUri': 'SVOL:frame1_fc_share_vol20',
                        "associatedTemplateAttachmentId": "uniqueid21",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 22, 'volumeUri': 'SVOL:frame1_fc_share_vol21',
                        "associatedTemplateAttachmentId": "uniqueid22",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                   ]
                   }
}]

update_server_profiles_from_spt = [
    {'name': 'frame1_fc_bay4', 'serverHardwareUri': 'frame1, bay 4',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay9', 'serverHardwareUri': 'frame1, bay 9',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay10', 'serverHardwareUri': 'frame1, bay 10',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'}]

server_profiles_from_spt_system_validation = [
    {'name': 'frame1_fc_bay5', 'serverHardwareUri': 'frame1, bay 5',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay6', 'serverHardwareUri': 'frame1, bay 6',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay11', 'serverHardwareUri': 'frame1, bay 11',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'},
    {'name': 'frame1_fc_bay12', 'serverHardwareUri': 'frame1, bay 12',
     'serverProfileTemplateUri': 'SPT:frame1_spt', 'type': 'ServerProfileV9'}]

unassign_server_profile = [{'type': 'ServerProfileV9',
                            'serverHardwareUri': None,
                            "name": "frame1_fc_bay10",
                            "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
                            "enclosureGroupUri": "EG:EG",
                            "affinity": "Bay",
                            "macType": "Physical",
                            "serialNumberType": "Physical",
                            "wwnType": "Physical",
                            "bios": {'manageBios': False, 'overriddenSettings': []},
                            'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None}, "connectionSettings": {
                                'connections': [{'id': 1, 'name': 'ns_1123_1272_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 2, 'name': 'ns_1123_1272_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 3, 'name': 'fc_a', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                                 'requestedMbps': '2500', 'networkUri': 'FC:fc_a1',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {"id": 4, "name": "fc_b", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                                 "requestedMbps": "2500", "networkUri": "FC:fc_b1",
                                                 "boot": {'priority': 'NotBootable'}},
                                                {'id': 5, 'name': 'ns_1273_1422_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 6, 'name': 'ns_1273_1422_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 7, 'name': 'eth_1423_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_1424',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 8, 'name': 'eth_1423_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_1424',
                                                 'boot': {'priority': 'NotBootable'}}]},
                            "firmware": {
                                "firmwareInstallType": None,
                                "forceInstallFirmware": False,
                                "manageFirmware": False,
                            },
                            'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                           'volumeAttachments': [
                                           ]},
                            'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                                {'id': 'AdminPhone',
                                                                                 'value': '123-123-4321'}]},
                            'localStorage': {}}]

reassign_server_profile = [{'type': 'ServerProfileV9',
                            'serverHardwareUri': 'SH:frame1, bay 10',
                            "name": "frame1_fc_bay10",
                            'serverProfileTemplateUri': 'SPT:frame1_spt',
                            "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
                            "enclosureGroupUri": "EG:EG",
                            "affinity": "Bay",
                            "macType": "Physical",
                            "serialNumberType": "Physical",
                            "wwnType": "Physical",
                            "bios": {'manageBios': False, 'overriddenSettings': []},
                            'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None}, "connectionSettings": {
                                'connections': [{'id': 1, 'name': 'ns_1123_1272_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 2, 'name': 'ns_1123_1272_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 3, 'name': 'fc_a', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                                 'requestedMbps': '2500', 'networkUri': 'FC:fc_a1',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {"id": 4, "name": "fc_b", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                                 "requestedMbps": "2500", "networkUri": "FC:fc_b1",
                                                 "boot": {'priority': 'NotBootable'}},
                                                {'id': 5, 'name': 'ns_1273_1422_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 6, 'name': 'ns_1273_1422_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                                 'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 7, 'name': 'eth_1423_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_1424',
                                                 'boot': {'priority': 'NotBootable'}},
                                                {'id': 8, 'name': 'eth_1423_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_1424',
                                                 'boot': {'priority': 'NotBootable'}}]},
                            "firmware": {
                                "firmwareInstallType": None,
                                "forceInstallFirmware": False,
                                "manageFirmware": False,
                            },
                            'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                           'volumeAttachments': [{
                                               "id": 1,
                                               "associatedTemplateAttachmentId": "uniqueid1",
                                               "isBootVolume": False,
                                               'lunType': 'Auto', 'lun': '',
                                               "storagePaths": [{"isEnabled": True,
                                                                 "connectionId": 3,
                                                                 "targetSelector": "Auto",
                                                                 "targets": []},
                                                                {"isEnabled": True,
                                                                 "connectionId": 4,
                                                                 "targetSelector": "Auto",
                                                                 "targets": []}],
                                               "volume": {
                                                   "isPermanent": False,
                                                   "properties": {
                                                       "name": "frame1_priv_vol",
                                                       "description": "",
                                                       "storagePool": "SPOOL:" + "SAT_SY_GEN1_R2_FC_FCoE",
                                                       "size": 32213303296,
                                                       "provisioningType": "Thin",
                                                       "isShareable": False},
                                                   "templateUri": "ROOT:" + "SAT_SY_GEN1_R2_FC_FCoE",
                                               },
                                               "volumeStorageSystemUri": "SSYS:" + "cosmosp7200",
                                               "volumeUri": None,
                                           },
                                               {'id': 2, 'volumeUri': 'SVOL:frame1_fc_share_vol1',
                                                "associatedTemplateAttachmentId": "uniqueid2",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 3, 'volumeUri': 'SVOL:frame1_fc_share_vol2',
                                                "associatedTemplateAttachmentId": "uniqueid3",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 4, 'volumeUri': 'SVOL:frame1_fc_share_vol3',
                                                "associatedTemplateAttachmentId": "uniqueid4",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 5, 'volumeUri': 'SVOL:frame1_fc_share_vol4',
                                                "associatedTemplateAttachmentId": "uniqueid5",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 6, 'volumeUri': 'SVOL:frame1_fc_share_vol5',
                                                "associatedTemplateAttachmentId": "uniqueid6",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 7, 'volumeUri': 'SVOL:frame1_fc_share_vol6',
                                                "associatedTemplateAttachmentId": "uniqueid7",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 8, 'volumeUri': 'SVOL:frame1_fc_share_vol7',
                                                "associatedTemplateAttachmentId": "uniqueid8",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 9, 'volumeUri': 'SVOL:frame1_fc_share_vol8',
                                                "associatedTemplateAttachmentId": "uniqueid9",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 10, 'volumeUri': 'SVOL:frame1_fc_share_vol9',
                                                "associatedTemplateAttachmentId": "uniqueid10",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 11, 'volumeUri': 'SVOL:frame1_fc_share_vol10',
                                                "associatedTemplateAttachmentId": "uniqueid11",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 12, 'volumeUri': 'SVOL:frame1_fc_share_vol11',
                                                "associatedTemplateAttachmentId": "uniqueid12",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 13, 'volumeUri': 'SVOL:frame1_fc_share_vol12',
                                                "associatedTemplateAttachmentId": "uniqueid13",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 14, 'volumeUri': 'SVOL:frame1_fc_share_vol13',
                                                "associatedTemplateAttachmentId": "uniqueid14",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 15, 'volumeUri': 'SVOL:frame1_fc_share_vol14',
                                                "associatedTemplateAttachmentId": "uniqueid15",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 16, 'volumeUri': 'SVOL:frame1_fc_share_vol15',
                                                "associatedTemplateAttachmentId": "uniqueid16",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 17, 'volumeUri': 'SVOL:frame1_fc_share_vol16',
                                                "associatedTemplateAttachmentId": "uniqueid17",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 18, 'volumeUri': 'SVOL:frame1_fc_share_vol17',
                                                "associatedTemplateAttachmentId": "uniqueid18",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 19, 'volumeUri': 'SVOL:frame1_fc_share_vol18',
                                                "associatedTemplateAttachmentId": "uniqueid19",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 20, 'volumeUri': 'SVOL:frame1_fc_share_vol19',
                                                "associatedTemplateAttachmentId": "uniqueid20",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 21, 'volumeUri': 'SVOL:frame1_fc_share_vol20',
                                                "associatedTemplateAttachmentId": "uniqueid21",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                               {'id': 22, 'volumeUri': 'SVOL:frame1_fc_share_vol21',
                                                "associatedTemplateAttachmentId": "uniqueid22",
                                                'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                                                'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                 {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                           ]},
                            'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                                {'id': 'AdminPhone',
                                                                                 'value': '123-123-4321'}]},
                            'localStorage': {}}]
spt_edit_data_rollback = [{
    "type": "ServerProfileTemplateV5",
    "name": "frame1_spt",
    "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Physical",
    "serialNumberType": "Physical",
    "wwnType": "Physical",
    'connectionSettings': {"manageConnections": True,
                           'connections': [{'id': 1, 'name': 'ns_1123_1272_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 2, 'name': 'ns_1123_1272_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 3, 'name': 'fc_a', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '2500', 'networkUri': 'FC:fc_a1',
                                            'boot': {'priority': 'NotBootable'}},
                                           {"id": 4, "name": "fc_b", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                            "requestedMbps": "2500", "networkUri": "FC:fc_b1",
                                            "boot": {'priority': 'NotBootable'}},
                                           {'id': 5, 'name': 'ns_1273_1422_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 6, 'name': 'ns_1273_1422_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 7, 'name': 'eth_1423_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 8, 'name': 'eth_1423_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}}]},
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
    },
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': False, 'overriddenSettings': []},
    'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
    "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                   "volumeAttachments": [{
                       "id": 1,
                       "associatedTemplateAttachmentId": "uniqueid1",
                       "isBootVolume": False,
                       'lunType': 'Auto', 'lun': '',
                       "storagePaths": [{"isEnabled": True,
                                         "connectionId": 3,
                                         "targetSelector": "Auto",
                                         "targets": []},
                                        {"isEnabled": True,
                                         "connectionId": 4,
                                         "targetSelector": "Auto",
                                         "targets": []}],
                       "volume": {
                           "isPermanent": False,
                           "properties": {
                               "name": "frame1_priv_vol",
                               "description": "",
                               "storagePool": "SPOOL:" + "SAT_SY_GEN1_R2_FC_FCoE",
                               "size": 32213303296,
                               "provisioningType": "Thin",
                               "isShareable": False},
                           "templateUri": "ROOT:" + "SAT_SY_GEN1_R2_FC_FCoE",
                       },
                       "volumeStorageSystemUri": "SSYS:" + "cosmosp7200",
                       "volumeUri": None,
                   },
                       {'id': 2, 'volumeUri': 'SVOL:frame1_fc_share_vol1',
                        "associatedTemplateAttachmentId": "uniqueid2",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 3, 'volumeUri': 'SVOL:frame1_fc_share_vol2',
                        "associatedTemplateAttachmentId": "uniqueid3",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 4, 'volumeUri': 'SVOL:frame1_fc_share_vol3',
                        "associatedTemplateAttachmentId": "uniqueid4",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 5, 'volumeUri': 'SVOL:frame1_fc_share_vol4',
                        "associatedTemplateAttachmentId": "uniqueid5",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 6, 'volumeUri': 'SVOL:frame1_fc_share_vol5',
                        "associatedTemplateAttachmentId": "uniqueid6",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 7, 'volumeUri': 'SVOL:frame1_fc_share_vol6',
                        "associatedTemplateAttachmentId": "uniqueid7",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 8, 'volumeUri': 'SVOL:frame1_fc_share_vol7',
                        "associatedTemplateAttachmentId": "uniqueid8",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 9, 'volumeUri': 'SVOL:frame1_fc_share_vol8',
                        "associatedTemplateAttachmentId": "uniqueid9",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 10, 'volumeUri': 'SVOL:frame1_fc_share_vol9',
                        "associatedTemplateAttachmentId": "uniqueid10",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 11, 'volumeUri': 'SVOL:frame1_fc_share_vol10',
                        "associatedTemplateAttachmentId": "uniqueid11",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 12, 'volumeUri': 'SVOL:frame1_fc_share_vol11',
                        "associatedTemplateAttachmentId": "uniqueid12",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 13, 'volumeUri': 'SVOL:frame1_fc_share_vol12',
                        "associatedTemplateAttachmentId": "uniqueid13",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 14, 'volumeUri': 'SVOL:frame1_fc_share_vol13',
                        "associatedTemplateAttachmentId": "uniqueid14",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 15, 'volumeUri': 'SVOL:frame1_fc_share_vol14',
                        "associatedTemplateAttachmentId": "uniqueid15",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 16, 'volumeUri': 'SVOL:frame1_fc_share_vol15',
                        "associatedTemplateAttachmentId": "uniqueid16",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 17, 'volumeUri': 'SVOL:frame1_fc_share_vol16',
                        "associatedTemplateAttachmentId": "uniqueid17",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                   ]
                   }
}]

spt_edit_data_storage_vol_rollback = [{
    "type": "ServerProfileTemplateV5",
    "name": "frame1_spt",
    "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Physical",
    "serialNumberType": "Physical",
    "wwnType": "Physical",
    'connectionSettings': {'connections': [{'id': 1, 'name': 'ns_1123_1272_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 2, 'name': 'ns_1123_1272_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_150',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 3, 'name': 'fc_a', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '2500', 'networkUri': 'FC:fc_a1',
                                            'boot': {'priority': 'NotBootable'}},
                                           {"id": 4, "name": "fc_b", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                            "requestedMbps": "2500", "networkUri": "FC:fc_b1",
                                            "boot": {'priority': 'NotBootable'}},
                                           {'id': 5, 'name': 'ns_1273_1422_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 6, 'name': 'ns_1273_1422_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                            'requestedMbps': '2500', 'networkUri': 'NS:ns_300',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 7, 'name': 'eth_1423_a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}},
                                           {'id': 8, 'name': 'eth_1423_b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_1423',
                                            'boot': {'priority': 'NotBootable'}}]},
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
    },
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': False, 'overriddenSettings': []},
    'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
    "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {'id': 2, 'volumeUri': 'SVOL:frame1_fc_share_vol1',
                        "associatedTemplateAttachmentId": "uniqueid2",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 3, 'volumeUri': 'SVOL:frame1_fc_share_vol2',
                        "associatedTemplateAttachmentId": "uniqueid3",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 4, 'volumeUri': 'SVOL:frame1_fc_share_vol3',
                        "associatedTemplateAttachmentId": "uniqueid4",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 5, 'volumeUri': 'SVOL:frame1_fc_share_vol4',
                        "associatedTemplateAttachmentId": "uniqueid5",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 6, 'volumeUri': 'SVOL:frame1_fc_share_vol5',
                        "associatedTemplateAttachmentId": "uniqueid6",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 7, 'volumeUri': 'SVOL:frame1_fc_share_vol6',
                        "associatedTemplateAttachmentId": "uniqueid7",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 8, 'volumeUri': 'SVOL:frame1_fc_share_vol7',
                        "associatedTemplateAttachmentId": "uniqueid8",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 9, 'volumeUri': 'SVOL:frame1_fc_share_vol8',
                        "associatedTemplateAttachmentId": "uniqueid9",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 10, 'volumeUri': 'SVOL:frame1_fc_share_vol9',
                        "associatedTemplateAttachmentId": "uniqueid10",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 11, 'volumeUri': 'SVOL:frame1_fc_share_vol10',
                        "associatedTemplateAttachmentId": "uniqueid11",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 12, 'volumeUri': 'SVOL:frame1_fc_share_vol11',
                        "associatedTemplateAttachmentId": "uniqueid12",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 13, 'volumeUri': 'SVOL:frame1_fc_share_vol12',
                        "associatedTemplateAttachmentId": "uniqueid13",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 14, 'volumeUri': 'SVOL:frame1_fc_share_vol13',
                        "associatedTemplateAttachmentId": "uniqueid14",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 15, 'volumeUri': 'SVOL:frame1_fc_share_vol14',
                        "associatedTemplateAttachmentId": "uniqueid15",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 16, 'volumeUri': 'SVOL:frame1_fc_share_vol15',
                        "associatedTemplateAttachmentId": "uniqueid16",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 17, 'volumeUri': 'SVOL:frame1_fc_share_vol16',
                        "associatedTemplateAttachmentId": "uniqueid17",
                        'lunType': 'Auto', 'lun': '', "isBootVolume": False,
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                   ]
                   }
}]

edit_server_profiles_storage_rollback = [{
    'type': 'ServerProfileV9',
    'serverHardwareUri': 'SH:frame1, bay 4',
    "name": "frame1_fc_bay4",
    'serverProfileTemplateUri': 'SPT:frame1_spt',
    "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Physical",
    "serialNumberType": "Physical",
    "wwnType": "Physical",
    'connectionSettings': spt_edit_data_storage_vol_rollback[0]["connectionSettings"],
    "firmware": spt_edit_data_storage_vol_rollback[0]["firmware"],
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': False, 'overriddenSettings': []},
    'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
    "sanStorage": spt_edit_data_storage_vol_rollback[0]["sanStorage"]
},

    {'type': 'ServerProfileV9',
     'serverHardwareUri': 'SH:frame1, bay 9',
     "name": "frame1_fc_bay9",
     'serverProfileTemplateUri': 'SPT:frame1_spt',
     "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
     "enclosureGroupUri": "EG:EG",
     "affinity": "Bay",
     "macType": "Physical",
     "serialNumberType": "Physical",
     "wwnType": "Physical",
     'connectionSettings': spt_edit_data_storage_vol_rollback[0]["connectionSettings"],
     "firmware": spt_edit_data_storage_vol_rollback[0]["firmware"],
     "hideUnusedFlexNics": True,
     "bios": {'manageBios': False, 'overriddenSettings': []},
     'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
     "sanStorage": spt_edit_data_storage_vol_rollback[0]["sanStorage"]
     },

    {'type': 'ServerProfileV9',
     'serverHardwareUri': 'SH:frame1, bay 10',
     "name": "frame1_fc_bay10",
     'serverProfileTemplateUri': 'SPT:frame1_spt',
     "serverHardwareTypeUri": 'SHT:frame1_sht:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
     "enclosureGroupUri": "EG:EG",
     "affinity": "Bay",
     "macType": "Physical",
     "serialNumberType": "Physical",
     "wwnType": "Physical",
     'connectionSettings': spt_edit_data_storage_vol_rollback[0]["connectionSettings"],
     "firmware": spt_edit_data_storage_vol_rollback[0]["firmware"],
     "hideUnusedFlexNics": True,
     "bios": {'manageBios': False, 'overriddenSettings': []},
     'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
     "sanStorage": spt_edit_data_storage_vol_rollback[0]["sanStorage"]
     }]

delete_storage_shared_volumes_rollback = [{"name": y['name']} for y in potash_iscsi_shared_volumes_system_validation +
                                          potash_fcoe_shared_volumes_system_validation + potash_fc_shared_volumes_system_validation if 'name' in y]

le_firmware_update = [
    {
        "type": "LogicalEnclosureV4",
        "status": "OK",
        "name": "LE",
        "enclosureUris": [
            "ENC:frame1",
            "ENC:frame2",
            "ENC:frame3"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]

target_uplinksets_attributes = ['interconnectName', 'portName', 'portStatus',
                                'portStatusReason', 'operationalSpeed', 'uri', 'portHealthStatus', 'neighbor']

interconnect_potash_bay3 = [{'encl_serial': 'MXQ8190017',
                             'device_type': 'InterconnectBays', 'device_bay': 3, 'name': 'frame1, interconnect 3'}]

interconnect_potash_bay6 = [{'encl_serial': 'MXQ8190017',
                             'device_type': 'InterconnectBays', 'device_bay': 6, 'name': 'frame1, interconnect 6'}]

efuse_interconnect_natasha_bay1 = [
    {'encl_serial': 'MXQ82104X6', 'device_type': 'InterconnectBays', 'device_bay': 1, 'name': 'frame3, interconnect 1'}]

efuse_interconnect_natasha_bay4 = [
    {'encl_serial': 'MXQ82104X6', 'device_type': 'InterconnectBays', 'device_bay': 4, 'name': 'frame3, interconnect 4'}]

efuse_blade_servers = [{'encl_serial': 'MXQ8190017', 'device_type': 'BladeBays', 'device_bay': 10, 'name': 'frame1, bay 10'},
                       {'encl_serial': 'MXQ8190017', 'device_type': 'BladeBays', 'device_bay': 11, 'name': 'frame1, bay 11'}]

reset_flm_frames_bay1 = [
    {'encl_serial': 'MXQ82104X6', 'name': 'frame3', 'bay': '1'}]

reset_flm_frames_bay2 = [
    {'encl_serial': 'MXQ82104X6', 'name': 'frame3', 'bay': '2'}]

logical_interconnect_natasha_pa = [{"name": 'LE-LIG_Natasha-3', "type": "logical-interconnectV4", "command": "Update", "fwActivationMode": "Parallel",
                                    "validationType": None, "sppName": "Custom Gen10 NOV MSB SPP b38 OVF RC1 2018 11 14"}]

logical_interconnect_natasha_pp = [{"name": 'LE-LIG_Natasha-3', "type": "logical-interconnectV4",
                                    "command": "Update", "sppName": "Custom Gen10 NOV MSB SPP b38 OVF RC1 2018 11 14", "fwActivationMode": "Orchestrated"}]

logical_interconnect_potash_pa = [{"name": 'LE-LIG_Potash', "type": "logical-interconnectV4", "command": "Update", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel",
                                   "fcActivationDelay": "5", "fcActivationType": "Parallel", "validationType": "None", "force": "true", "sppUri": "2018.11.14.00"}]

logical_interconnect_potash_pp = [{"name": 'LE-LIG_Potash', "type": "logical-interconnectV4", "command": "Update", "ethernetActivationDelay": "5", "ethernetActivationType": "PairProtect",
                                   "fcActivationDelay": "5", "fcActivationType": "PairProtect", "validationType": "ValidateBestEffort", "force": "true", "sppUri": "2018.11.14.00"}]


# Use "create shared volumes data" to form the body for delete volumes
delete_storage_shared_volumes = [{"name": y['name']} for y in potash_iscsi_shared_volumes +
                                 potash_fcoe_shared_volumes + potash_fc_shared_volumes + new_storage_volumes if 'name' in y]

# Merge multiple list of dictionaries to form single list of dictonaries
delete_storage_volumes = list(OrderedDict(
    (frozenset(x.items()), x) for x in delete_storage_shared_volumes).values())

# Use "create iscsi shared volume data" to form the body to delete volumes
# in 3par hosts
remove_iscsi_exported_volumes = [{"name": y['name']}
                                 for y in potash_iscsi_shared_volumes if 'name' in y]

binfile_local_path = 'C:/spp'

# cleanup data
cleanup_ilo = [{'ilo': '10.167.12.10', 'username': 'Administrator', 'password': 'Cosmos123'},
               {'ilo': '10.167.12.2', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.5', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.3', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.14', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.13', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.11', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.8', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.6', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.9', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.12', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.4', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.1', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.167.12.7', 'username': 'Administrator',
                   'password': 'Cosmos123'}
               ]

cleanup_zone = [{'sanName': 'FC-SAN-Fabric-A'},
                {'sanName': 'FC-SAN-Fabric-B'},
                {'sanName': 'VSAN3405'},
                {'sanName': 'VSAN3406'}
                ]

# Enclosure data
encl_update = DD.rename_enclosure(enclosure)
expected_enclosure = DD.expected_enclosure_data(enclosure)

# Add AD
ad = DD.make_ad_dict(ad_directory)
expected_ad = DD.make_expected_ad_dict(ad_directory)

# Add AD Groups
adgrp = DD.make_ad_group_data(adgroup)
expected_adgrp = DD.make_expected_ad_group_data(adgroup)

# SAN managers data
san_managers = DD.create_san_manager_data(sans)
expected_san_managers = DD.get_expected_san_manager_data(sans)

# Add FC Networks
fc_networks = DD.create_fcnet_data(fcs)
expected_fc_networks = DD.get_expected_fcnet_data(fc_networks)

# Add Ethernet Networks
ethernet_networks_bulk = DD.create_ebulk_data(ethernets)
expected_ethernet_networks_bulk = DD.get_expected_ebulk_data(ethernets)
expected_ethernet_networks = DD.get_expected_ethernet_data(ethernet_networks)
postbackup_expected_ethernet_networks = DD.get_expected_ethernet_data(
    postbackup_ethernet_networks)

ethernet_networks_system_validation = DD.create_ebulk_data(
    ethernetssystem_validation)
expected_ethernet_networks_system_validation = DD.get_expected_ebulk_data(
    ethernetssystem_validation)

# Add Tagged and Tunnel Networks
untagged_tunnel_eth_networks = DD.make_untagged_tunnel_data(
    untagged_tunnel_eth)
expected_untagged_tunnel_eth_networks = DD.make_expected_untagged_tunnel_data(
    untagged_tunnel_eth)

# Add FCoE networks
fcoe_networks = DD.create_fcoenet_data(fcoes)
expected_fcoe_networks = DD.get_expected_fcoenet_data(fcoe_networks)

# Add Network sets
network_sets = DD.create_bulk_network_set_data(network_set)
expected_network_sets = DD.get_expected_network_set_data(network_sets)

network_sets_system_validation = DD.create_bulk_network_set_data(
    network_set_system_validation)
expected_network_sets_system_validation = DD.get_expected_network_set_data(
    network_sets_system_validation)

# Add Storage system
storagesystems = DD.make_storage_system_with_pools_data(storage_system)
expected_storagesystem = DD.make_expected_storage_system_with_pools_data(
    storage_system)

exec_storage_systems = DD.make_storage_system_with_pools_data(
    storage_system_post)
exec_expected_storage_systems = DD.make_expected_storage_system_with_pools_data(
    storage_system_post)

# Edit storage pools
storage_pools = DD.make_storage_pools_toedit_data(storage_pools_toedit)

# Create volume template
volume_templates = DD.make_storage_volume_templates_data(
    storage_volume_templates)
expected_volume_templates = DD.make_expected_storage_volume_template_data(
    storage_volume_templates)

volume_templates_post_upgrade = DD.make_storage_volume_templates_data(
    storage_volume_templates_post)
expected_volume_templates_post_upgrade = DD.make_expected_storage_volume_template_data(
    storage_volume_templates_post)

new_volumes_system_validation = list(OrderedDict((frozenset(x.items()), x) for x in potash_iscsi_shared_volumes_system_validation + potash_fcoe_shared_volumes_system_validation +
                                                 potash_fc_shared_volumes_system_validation).values())
new_volumes_add_system_validation = DD.storage_volumes(
    new_volumes_system_validation)
expected_new_volumes_add_system_validation = DD.expected_storage_volumes(
    new_volumes_system_validation)

# Create new volumes
all_new_storage_volumes = list(OrderedDict((frozenset(x.items()), x) for x in new_storage_volumes +
                                           potash_iscsi_shared_volumes + potash_fcoe_shared_volumes + potash_fc_shared_volumes).values())
new_volumes_add = DD.storage_volumes(all_new_storage_volumes)
expected_newvolumes = DD.expected_storage_volumes(new_storage_volumes)

exec_volumes_add = DD.storage_volumes(new_storage_volumes_post)
exec_expected_volumes = DD.expected_storage_volumes(new_storage_volumes_post)

# Scopes
expected_scopes = DD.get_expected_scope_data(scopes)
adgroup_withscope = DD.make_ad_group_data(adgroup_scope)

expected_scopes_post = DD.get_expected_scope_data(scopes_postupgrade)
adgroup_withscope_post = DD.make_ad_group_data(adgroup_scope_postupgrade)

# Server Profile Template
server_profile_templates_data = copy.deepcopy(server_profile_templates)
expected_server_profile_templates = DD.make_expected_server_profile_template_data(
    server_profile_templates, firmware)

spts_edit = copy.deepcopy(spt_edit_data)
expected_spts_edit = DD.make_expected_server_profile_template_data(
    spt_edit_data, firmware)

# System Validation
ethernet_networks_system_validation = DD.create_ebulk_data(
    ethernetssystem_validation)
expected_ethernet_networks_system_validation = DD.get_expected_ebulk_data(
    ethernetssystem_validation)

network_sets_system_validation = DD.create_bulk_network_set_data(
    network_set_system_validation)
expected_network_sets_system_validation = DD.get_expected_network_set_data(
    network_sets_system_validation)

edit_server_profiles_template = copy.deepcopy(
    edit_server_profiles_template_data)
expected_edit_server_profiles_template = DD.make_expected_server_profile_template_data(
    edit_server_profiles_template_data, firmware)

edit_server_profiles_template_rollback = copy.deepcopy(spt_edit_data_rollback)
expected_edit_server_profile_templates_rollback = DD.make_expected_server_profile_template_data(
    spt_edit_data_rollback, firmware)

ethernet_networks_delete_rollback = DD.get_ethernet_name_data(
    ethernetssystem_validation)
