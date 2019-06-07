'''
SAT Tbird Ring1 Data File

'''

from dynamicdata import DynamicData
from collections import OrderedDict
import copy

from pysphere import VIServer
import ssl

from robot.libraries.BuiltIn import BuiltIn
fusion_lib = BuiltIn().get_library_instance('FusionLibrary')

# Python 2.7.9+ has issues with unverified certs this is a workaround
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
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


def get_spp_name_version(sppname):
    """
        Get the SPP version and name for the specified spp build name
        [Example]
        ${resp} = get_spp_version(name)
    """
    res = fusion_lib.fusion_api_get_firmware_driver()
    for fw in res['members']:
        if fw['uuid'] == sppname:
            ver = fw['version']
            name = fw['name']
    return ver, name


DD = DynamicData()

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

ilo_credentials = {'username': 'Administrator',
                   'password': 'Cosmos123'
                   }

dhcpservers = [{'ip': '10.120.0.10', 'vlanid': '1151', 'scope': '10.151.0.0',
                'username': 'Administrator', 'password': 'Cosmos123'}]

esxi_os_servers = [{"name": "Enclosure1_FC_Potash_Legacy_Bay1_ESXi_3", 'serverHardwareUri': 'Enclosure1, bay 1'}, {
    "name": "Enclosure3_FC_Potash_uefi_Bay3_ESXi_1", 'serverHardwareUri': 'Enclosure3, bay 3'}]

esxi_os_servers_post_upgrade = [
    {"name": "Enclosure2_FC_Carbon_Legacy_Bay2_ESXi_2", 'serverHardwareUri': 'Enclosure2, bay 2'}]

vi_server_details = {'vcenter': "10.120.12.57", 'username': "administrator@vsphere.local",
                     'password': "Cosmos@123", 'cluster': "sat_tbird", "hostun": "root", "hostpwd": "Cosmos123"}

cluster_vm = {"name": "sat_tb_win_2k12"}

win_os_servers = [{"name": "Enclosure3_FC_Potash_Legacy_Bay1_win2k16", 'serverHardwareUri': 'Enclosure3, bay 1'}, {
    "name": "Enclosure3_FC_Potash_Legacy_Bay2_win2k16", 'serverHardwareUri': 'Enclosure3, bay 2'}]

enclosure = [{'serialNumber': 'MXQ748041Z', 'newName': 'Enclosure1'},
             {'serialNumber': 'MXQ748041Y', 'newName': 'Enclosure2'},
             {'serialNumber': 'MXQ7480423', 'newName': 'Enclosure3'}]

stress_tool = {"username": "Administrator", "password": "Cosmos123", "etdpath": "C:\\Users\\Administrator\\Desktop\\ETD\\etdntmg.exe", "inipath": "C:\\Users\\Administrator\\Desktop\\ETD\\default1.ini",
               "DriverName": "K", "filename": "default1.ini",
               "dest": "\C$\Users\Administrator\Desktop\ETD", "source": "C:\Users\Administrator\Desktop\default1.ini", "target": "K:\default1.ini"}

win_name = [{"shared_folder": "test"}]

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

spp_name = 'bp-2018-06-19-00'
spp_version = 'bp-2018-06-19-00'

server_hardwares = [{'name': 'Enclosure2, bay 2',
                     'old_hostname': 'localhost.dom1151.lab',
                     'new_hostname': 'SATRegression02.dom1151.lab'}]

updated_spp_name = DD.spp_name_withunderscore(spp_name)

spp_local_dir = 'C:/spp/'

spps = [{'name': 'bp-2018-06-19-00', 'localpath': 'C:/spp/'}]

spp_local_paths = DD.get_spp_details(spps)

target_uplinksets_attributes = ['interconnectName', 'portName', 'portStatus',
                                'portStatusReason', 'operationalSpeed', 'uri', 'portHealthStatus', 'neighbor']

# baseline_url = "/rest/firmware-drivers/" + updated_spp_name

# firmware_post_upgrade = {'manageFirmware': True,
#                         'forceInstallFirmware': False, "firmwareBaselineUri": baseline_url}

firmware = {'manageFirmware': False,
            'forceInstallFirmware': False, 'firmwareInstallType': None}

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
         'Host': '10.120.1.85',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'Cosmos123', 'UseSsl': True},
        {'Type': 'HPE',
         'Host': '10.120.1.80',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'},
        {'Type': 'HPE',
         'Host': '10.120.1.86',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'}
        ]

ethernet_networks = [{'name': 'iscsi_1121', 'type': 'ethernet-networkV4', 'vlanId': 1121, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'iscsi_1122', 'type': 'ethernet-networkV4', 'vlanId': 1122, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False}]

ethernet_name_prefix = "eth1"

ethernets = [{"vlanIdStart": 1120, "vlanIdEnd": 2130, "purpose": "General", "namePrefix": ethernet_name_prefix,
              "smartLink": True, "privateNetwork": False,
              "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV1"},
             {"vlanIdStart": 1120, "vlanIdEnd": 2130, "purpose": "General", "namePrefix": "eth2",
              "smartLink": True, "privateNetwork": False,
              "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-networkV1"}]

postbackup_ethernet_networks = [
    {'name': 'postbackup_iscsi_1', 'type': 'ethernet-networkV4', 'vlanId': 1, 'purpose': 'ISCSI', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_iscsi_2', 'type': 'ethernet-networkV4', 'vlanId': 2, 'purpose': 'ISCSI', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_eth1_1146', 'type': 'ethernet-networkV4', 'vlanId': 1146, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_eth1_1147', 'type': 'ethernet-networkV4', 'vlanId': 1147, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False},
    {'name': 'postbackup_eth1_1148', 'type': 'ethernet-networkV4', 'vlanId': 1148, 'purpose': 'General', 'smartLink': True,
     'privateNetwork': False}
]

untagged_tunnel_eth = [{'name': 'untagged', 'ethernetNetworkType': 'Untagged'},
                       {'name': 'tunnel', 'ethernetNetworkType': 'Tunnel'}]

fcs = [
    {'count': 1, 'base_name': 'fc_tb_fab1_',
        'associatedSAN': 'RIST-R1-SN6600B-SW1'},
    {'count': 1, 'base_name': 'fc_tb_fab2_',
        'associatedSAN': 'RIST-R1-SN6600B-SW2'},
]

fcoes = [{'base_name': 'fcoe_3801_', 'vlanId': 3801, 'san': 'VSAN3801', 'count': 1},
         {'base_name': 'fcoe_3802_', 'vlanId': 3802, 'san': 'VSAN3802', 'count': 1}]

network_set = [{'namePrefix': 'nsnomgmt1_', 'count': 3,
                'netNamePrefix': 'eth1_', 'netNameSuffix': 1400, 'netPerNS': 50, 'nativeNetworkUri': None},
               {'namePrefix': 'nsnomgmt2_', 'count': 3,
                'netNamePrefix': 'eth2_', 'netNameSuffix': 1400, 'netPerNS': 50, 'nativeNetworkUri': None},
               {'namePrefix': 'nswithmgmtuntagged1_', 'count': 1,
                'netNamePrefix': 'eth1_', 'netNameSuffix': 1151, 'netPerNS': 150, 'nativeNetworkUri': 'eth1_1151'},
               {'namePrefix': 'nswithmgmtuntagged2_', 'count': 1,
                'netNamePrefix': 'eth2_', 'netNameSuffix': 1151, 'netPerNS': 150, 'nativeNetworkUri': 'eth2_1151'}]

storage_system = [{'name': 'HPE_3PAR_8200_ISCSI_EPIC', 'hostname': '10.134.1.48', 'username': 'cosmos', 'password': 'Insight7',
                   'managedDomain': 'SAT-Synergy', 'managedPools': [], 'serialNumber': '2M271500PZ'},
                  {'name': 'RIST-R1-3PAR', 'hostname': '10.120.1.81', 'username': 'cosmos', 'password': 'Insight7',
                   'managedDomain': "NO DOMAIN", 'managedPools': [], 'serialNumber': '2M273304WT'}]

storage_pools_toedit = [{"storageSystemUri": 'RIST-R1-3PAR', "name": 'FC_r1'},
                        {"storageSystemUri": 'HPE_3PAR_8200_ISCSI_EPIC', "name": 'SAT-SY-R1'}]

storage_system_post = [{'name': 'tbr13par', 'hostname': '10.120.1.7', 'username': 'cosmos', 'password': 'Insight7',
                        'managedDomain': 'TB4', 'managedPools': [], 'serialNumber': '1649938'}]

storage_pools_toedit_manage = [{"storageSystemUri": 'tbr13par', "name": 'TB4-Raid5-FC', "isManaged": True},
                               {"storageSystemUri": 'RIST-R1-3PAR',
                                   "name": 'FC_r5', "isManaged": True},
                               {"storageSystemUri": 'RIST-R1-3PAR', "name": 'FC_r6', "isManaged": True}]

storage_pools_toedit_discover = [{"storageSystemUri": 'RIST-R1-3PAR', "name": 'FC_r5', "isManaged": False},
                                 {"storageSystemUri": 'RIST-R1-3PAR', "name": 'FC_r6', "isManaged": False}]

enc_groups = [{'name': 'EG', 'enclosureCount': 3,
               'interconnectBayMappings': [{'enclosureIndex': 2, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                           {'enclosureIndex': 2, 'interconnectBay': 4,
                                               'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                           {'interconnectBay': 3,
                                               'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                           {'interconnectBay': 6,
                                               'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                           {'enclosureIndex': 3, 'interconnectBay': 1,
                                               'logicalInterconnectGroupUri': 'SASLIG:LIG_SAS'},
                                           {'enclosureIndex': 3, 'interconnectBay': 4,
                                               'logicalInterconnectGroupUri': 'SASLIG:LIG_SAS'},
                                           ],
               'ipAddressingMode': 'DHCP', 'ipRangeUris': [], 'powerMode': 'RedundantPowerFeed'}]

expected_encgroups = [{"type": "EnclosureGroupV7", "uri": "EG:EG", "category": "enclosure-groups", "name": "EG",
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
                       'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                                   {'interconnectBay': 4,
                                                       'logicalInterconnectGroupUri': 'LIG:LIG_Carbon'},
                                                   {'interconnectBay': 3,
                                                       'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                                   {'interconnectBay': 6,
                                                       'logicalInterconnectGroupUri': 'LIG:LIG_Potash'},
                                                   {'interconnectBay': 1,
                                                       'logicalInterconnectGroupUri': 'SASLIG:LIG_SAS'},
                                                   {'interconnectBay': 4,
                                                       'logicalInterconnectGroupUri': 'SASLIG:LIG_SAS'}
                                                   ],
                       "ipAddressingMode": "DHCP", "ipRangeUris": [], "powerMode": "RedundantPowerFeed", "description": None,
                       "associatedLogicalInterconnectGroups": ["LIG:LIG_Carbon", "LIG:LIG_Potash", "LIG:LIG_SAS"], "enclosureCount": 3}]

logical_enclosure = [{'name': 'LE', 'enclosureUris': [
    'ENC:Enclosure3', 'ENC:Enclosure2', 'ENC:Enclosure1'], 'enclosureGroupUri': 'EG:EG'}]

refresh_enclosures = [{"name": "Enclosure2"}, {
    "name": "Enclosure1"}, {"name": "Enclosure3"}]

expected_logical_enclosure = [
    {
        "type": "LogicalEnclosureV4",
        "uri": "LE:LE",
        "status": "OK",
        "name": "LE",
        "enclosureUris": [
            "ENC:Enclosure3",
            "ENC:Enclosure2",
            "ENC:Enclosure1"
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
            "ENC:Enclosure3",
            "ENC:Enclosure2",
            "ENC:Enclosure1"
        ],
        "enclosureGroupUri": "EG:EG"
    }
]

uplink_eth1 = ["eth1_" + str(j) for i in ethernets if i["namePrefix"] == "eth1" for j in range(1123, 2123)]

uplink_sets = {
    "carbon_fc1": {'name': 'fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                   'networkUris': ['fc_tb_fab1_1'], 'mode': 'Auto',
                   'logicalPortConfigInfos': [{
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
                   'networkUris': ['fc_tb_fab2_1'], 'mode': 'Auto',
                   'logicalPortConfigInfos': [{
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
                   'networkUris': uplink_eth1, 'mode': 'Auto',
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
            "fcoe_3801_1"
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
            "fcoe_3802_1"
        ],
        "primaryPort": None
    },
    "potash_fc1": {'name': 'fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                   'networkUris': ['fc_tb_fab1_1'], 'mode': 'Auto',
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
                   'networkUris': ['fc_tb_fab2_1'], 'mode': 'Auto',
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
         'ethernetSettings': None, 'redundancyType': 'Redundant', 'type': 'logical-interconnect-groupV6',
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
         'ethernetSettings': None, 'redundancyType': 'HighlyAvailable', 'type': 'logical-interconnect-groupV6',
         'interconnectBaySet': 3, 'description': None}]

regx_us = "[0-9a-fA-F]"
regex_uuid = "%s{8}(-%s{4}){3}-%s{12}" % (regx_us, regx_us, regx_us)

validate_uplink_eth1 = ["REGEX:/rest/ethernet-networks/%s" %
                        (regex_uuid) for i in ethernets if i["namePrefix"] == "eth1" for j in range(1123, 2123)]

expected_lig = [{'enclosureType': 'SY12000', 'type': 'logical-interconnect-groupV6', 'name': 'LIG_Carbon',
                 'uplinkSets': [{'networkUris': ['FC:fc_tb_fab1_1'], 'name': 'fc1'},
                                {'networkUris': ['FC:fc_tb_fab2_1'], 'name': 'fc2'}]},
                {'enclosureType': 'SY12000', 'type': 'logical-interconnect-groupV6', 'name': 'LIG_Potash',
                 'uplinkSets': [{'networkUris': validate_uplink_eth1, 'name': 'eth'},
                                {'networkUris': [
                                    'ETH:iscsi_1121'], 'name': 'iscsi1'},
                                {'networkUris': [
                                    'ETH:iscsi_1122'], 'name': 'iscsi2'},
                                {'networkUris': [
                                    'ETH:fcoe_3801_1'], 'name': 'fcoe1'},
                                {'networkUris': [
                                    'FC:fc_tb_fab1_1'], 'name': 'fc1'},
                                {'networkUris': [
                                    'ETH:fcoe_3802_1'], 'name': 'fcoe2'},
                                {'networkUris': ['FC:fc_tb_fab2_1'], 'name': 'fc2'}]}]

expected_lig = {"members": expected_lig}

sas_lig = [{"name": "LIG_SAS",
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

expected_sas_lig = [{"name": "LIG_SAS",
                     "type": "sas-logical-interconnect-groupV2",
                     "enclosureType": "SY12000",
                     "description": None,
                     "status": 'OK',
                     "state": 'Active',
                     "uri": 'SASLIG:LIG_SAS',
                     'interconnectBaySet': 1,
                     'enclosureIndexes': [1]}]

sas_li_name = "LE-LIG_SAS-3"

storage_volume_templates = [
    {'name': 'template_thin', "rootTemplateUri": "template_thin", 'default': 'FC_r1'}]

storage_volume_templates_post = [
    {'name': 'template_thin_2', "rootTemplateUri": "template_thin_2", 'default': 'FC_r1'}]

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
                        "default": "FC_r1",
                        "required": True, "description": "A common provisioning group URI reference"},
        "snapshotPool": {"meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                         "type": "string", "title": "Snapshot Pool",
                         "format": "x-uri-reference",
                         "default": "FC_r1",
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
    "storagePoolUri": "FC_r1",
        "name": "template_thin_2",
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
                        "default": "SP:FC_r1",
                        "required": True, "description": "A common provisioning group URI reference"},
        "snapshotPool": {"meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                         "type": "string", "title": "Snapshot Pool",
                         "format": "x-uri-reference",
                         "default": "SP:FC_r1",
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
    "storagePoolUri": "SP:FC_r1",
        "name": "template_thin_2",
        "description": "private non-boot volume template",
        "category": "storage-volume-templates",
        "type": "StorageVolumeTemplateV6"}]

storage_volumes = [
    {'isShareable': False, 'name': 'DND_encl_41z_bay8_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_423_bay2_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_423_bay7_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_423_bay1_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_423_bay3_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_423_bay10_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_41y_bay2_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_41z_bay1_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_41z_bay3_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_41z_bay2_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_423_bay8_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': False, 'name': 'DND_encl_41y_bay1_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': True, 'name': 'encl_41y_share_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': True, 'name': 'encl_41z_share_volume',
        "storageSystemUri": "RIST-R1-3PAR"},
    {'isShareable': True, 'name': 'encl_423_share_volume',
        "storageSystemUri": "RIST-R1-3PAR"}
]

new_storage_volumes = [{"name": "encl_41y_new_volume", "templateUri": "template_thin",
                        "isShareable": False, "storagePool": "FC_r1"},
                       {"name": "encl_41z_new_volume", "templateUri": "template_thin",
                        "isShareable": False, "storagePool": "FC_r1"},
                       {"name": "encl_423_new_volume", "templateUri": "template_thin",
                        "isShareable": False, "storagePool": "FC_r1"}
                       ]

three_par_host_name = [{"name": "Enclosure1_Potash_iscsi_uefi_b5"}, {
    "name": "Enclosure3_Potash_iscsi_uefi_b9"}]

potash_iscsi_shared_volumes = [{"name": "sat3_potash_iscsi_1",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_2",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_3",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_4",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_5",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_6",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_7",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_8",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_9",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_10",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_11",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_12",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_13",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_14",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"},
                               {"name": "sat3_potash_iscsi_15",
                                "templateUri": "ROOT",
                                "isShareable": True,
                                "storagePool": "SAT-SY-R1"}
                               ]

potash_fc_shared_volumes = [{"name": "sat3_potash_fc_cluster_shared_volume_1",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_2",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_3",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_4",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_5",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_6",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_7",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_8",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_9",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_10",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_11",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_12",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_13",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_14",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_potash_fc_cluster_shared_volume_15",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"}
                            ]

carbon_fc_shared_volumes = [{"name": "sat3_carbon_fc_cluster_shared_volume_1",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_2",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_3",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_4",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_5",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_6",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_7",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_8",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_9",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_10",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_11",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_12",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_13",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_14",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"},
                            {"name": "sat3_carbon_fc_cluster_shared_volume_15",
                             "templateUri": "ROOT",
                             "isShareable": True,
                             "storagePool": "FC_r1"}
                            ]

potash_fcoe_shared_volumes = [{"name": "sat3_potash_fcoe_cluster_shared_volume_1",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_2",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_3",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_4",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_5",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_6",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_7",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_8",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_9",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_10",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_11",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_12",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_13",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_14",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"},
                              {"name": "sat3_potash_fcoe_cluster_shared_volume_15",
                               "templateUri": "ROOT",
                               "isShareable": True,
                               "storagePool": "FC_r1"}
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
     'type': 'StorageVolumeV7'},
    {"name": "exec_volume2_toedit", "isShareable": True, 'status': 'OK', 'state': 'Managed', 'type': 'StorageVolumeV7'}]

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
            "mountUri": "ENC:Enclosure2",
            "topUSlot": 20
        },
        {
            "uHeight": 10,
            "mountUri": "ENC:Enclosure1",
            "topUSlot": 30
        },
        {
            "uHeight": 10,
            "mountUri": "ENC:Enclosure3",
            "topUSlot": 10,
        }
    ]
}]

dc = [{'name': 'Datacenter 1', 'width': 7199, 'depth': 2999, 'contents': [
    {'resourceUri': '', 'y': 0, 'x': 0}]}]

server_profile_templates = [{
    "type": "ServerProfileTemplateV6",
    "name": "spt_encl_41y_bay3_bay7",
    "serverHardwareTypeUri": 'SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Virtual",
    "serialNumberType": "Virtual",
    "wwnType": "Virtual",
    'connectionSettings': {"manageConnections": True,
                           'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:nswithmgmtuntagged1_1',
                                            'boot': {'priority': 'Primary'}},
                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:nswithmgmtuntagged1_1',
                                            'boot': {'priority': 'Secondary'}},
                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '2500',
                                            'networkUri': 'FC:fc_tb_fab1_1',
                                            'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                            "requestedMbps": "2500", "networkUri": "FC:fc_tb_fab2_1",
                                            "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
    },
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': True,
             'overriddenSettings': [{'id': 'AdminName', 'value': 'Regression-Tester'},
                                    {'id': 'AdminPhone', 'value': '123-123-4321'}]},
    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    "sanStorage": {"hostOSType": "Windows 2012 / WS2012 R2", "manageSanStorage": True,
                   "volumeAttachments": [{
                       "id": 1,
                       "associatedTemplateAttachmentId": "uniqueid1",
                       'bootVolumePriority': 'Primary',
                       "lun": 1,
                       "lunType": 'Manual',
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
                               "name": "encl_41y_spt_volume",
                               "description": "",
                               "storagePool": "SPOOL:" + "FC_r1",
                               "size": 32213741824,
                               "provisioningType": "Thin",
                               "isShareable": False},
                           "templateUri": "ROOT:" + "FC_r1",
                       },
                       "volumeStorageSystemUri": "SSYS:" + "RIST-R1-3PAR",
                       "volumeUri": None,
                   },
                       {'id': 2, 'volumeUri': 'SVOL:encl_41y_share_volume',
                        "associatedTemplateAttachmentId": "uniqueid2",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 3, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                        "associatedTemplateAttachmentId": "uniqueid3",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 4, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                        "associatedTemplateAttachmentId": "uniqueid4",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 5, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                        "associatedTemplateAttachmentId": "uniqueid5",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 6, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                        "associatedTemplateAttachmentId": "uniqueid6",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                        "associatedTemplateAttachmentId": "uniqueid7",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                        "associatedTemplateAttachmentId": "uniqueid8",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                        "associatedTemplateAttachmentId": "uniqueid9",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                        "associatedTemplateAttachmentId": "uniqueid10",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                        "associatedTemplateAttachmentId": "uniqueid11",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                        "associatedTemplateAttachmentId": "uniqueid12",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                        "associatedTemplateAttachmentId": "uniqueid13",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                        "associatedTemplateAttachmentId": "uniqueid14",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                        "associatedTemplateAttachmentId": "uniqueid15",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                        "associatedTemplateAttachmentId": "uniqueid16",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                        "associatedTemplateAttachmentId": "uniqueid17",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                   ]
                   }
}]

scopes = [{"name": "fc1", "description": "", "type": "ScopeV3",
           "addedResourceUris": ["FC:fc_tb_fab1_1"], "removedResourceUris":[], "initialScopeUris":[]},
          {"name": "fcoe1", "description": "", "type": "ScopeV3", "addedResourceUris": [
              "FCOE:fcoe_3801_1"], "removedResourceUris":[], "initialScopeUris":[]},
          {"name": "eth1", "description": "", "type": "ScopeV3", "addedResourceUris": [
              "ETH:tunnel_8"], "removedResourceUris":[], "initialScopeUris":[]}
          ]

adgroup_scope = [{'userName': 'ad_infra_user', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'infra_group',
                  "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope:eth1'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope:fc1'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope:fcoe1'}
                                  ]}]

expected_adgroup_withscope = [{'category': 'users', 'loginDomain': 'AD', 'type': 'LoginDomainGroupPermission',
                               'egroup': 'infra_group',
                               'permissions': [{"roleName": "Infrastructure administrator", "scopeUri": 'eth1'}, {'roleName': 'Infrastructure administrator', 'scopeUri': 'fc1'}, {'roleName': 'Infrastructure administrator', 'scopeUri': 'fcoe1'}]}]

# end

scopes_postupgrade = [{"name": "fc2", "description": "", "type": "ScopeV3",
                       "addedResourceUris": ["FC:fc_tb_fab2_1"], "removedResourceUris":[], "initialScopeUris":[]},
                      {"name": "fcoe2", "description": "", "type": "ScopeV3", "addedResourceUris": [
                          "FCOE:fcoe_3802_1"], "removedResourceUris":[], "initialScopeUris":[]},
                      {"name": "eth2", "description": "", "type": "ScopeV3", "addedResourceUris": [
                          "ETH:tunnel_9"], "removedResourceUris":[], "initialScopeUris":[]}
                      ]

adgroup_scope_postupgrade = [{'userName': 'ad_infra_user_exec', 'password': 'Cosmos123', 'loginDomain': 'AD', 'egroup': 'exec_infra_group',
                              "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope:eth2'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope:fc2'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope:fcoe2'}]}]

expected_adgroup_withscope_postupgrade = [{'category': 'users', 'loginDomain': 'AD', 'type': 'LoginDomainGroupPermission',
                                           'egroup': 'exec_infra_group',
                                           'permissions': [{"roleName": "Infrastructure administrator", "scopeUri": 'eth2'}, {"roleName": "Infrastructure administrator", "scopeUri": 'fc2'}, {"roleName": "Infrastructure administrator", "scopeUri": 'fcoe2'}]}]

server_profiles_from_spt = [{'name': 'Enclosure2_FC_Potash_uefi_Bay3_SPT', 'serverHardwareUri': 'Enclosure2, bay 3',
                             'serverProfileTemplateUri': 'SPT:spt_encl_41y_bay3_bay7', 'type': 'ServerProfileV10'}
                            ]

server_profiles_from_spt_postupgrade = [{'name': 'Enclosure2_FC_Potash_uefi_Bay7_SPT', 'serverHardwareUri': 'Enclosure2, bay 7',
                                         'serverProfileTemplateUri': 'SPT:spt_encl_41y_bay3_bay7', 'type': 'ServerProfileV10'}
                                        ]

expected_server_profiles_from_spt = [{
    "type": "ServerProfileV10",
    "name": "Enclosure2_FC_Potash_uefi_Bay3_SPT",
    "serverHardwareUri": "SH:Enclosure2, bay 3",
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "firmware": {
        "firmwareScheduleDateTime": None,
        "firmwareActivationType": None,
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
        "firmwareBaselineUri": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "Ethernet",
                "networkUri": "NS:nswithmgmtuntagged1_1",
                "portId": "Mezz 3:1-a",
                "boot": {
                    "priority": "Primary"
                },
            },
            {
                "id": 2,
                "name": "",
                "functionType": "Ethernet",
                "networkUri": "NS:nswithmgmtuntagged1_1",
                "portId": "Mezz 3:2-a",
                "boot": {
                    "priority": "Secondary"
                },
            },
            {
                "id": 3,
                "name": "",
                "functionType": "FibreChannel",
                "networkUri": "FC:fc_tb_fab1_1",
                "portId": "Mezz 3:1-b",
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                },
            },
            {
                "id": 4,
                "name": "",
                "functionType": "FibreChannel",
                "networkUri": "FC:fc_tb_fab2_1",
                "portId": "Mezz 3:2-b",
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                },
            }
        ]
    },
    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    "bios": {
        "overriddenSettings": [{'id': 'AdminName', 'value': 'Regression-Tester'},
                               {'id': 'AdminPhone', 'value': '123-123-4321'}],
        "manageBios": True
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
        "reapplyState": "NotApplying"
    },
    "sanStorage": {
        "volumeAttachments": [
            {
                "storagePaths": [
                    {
                        "targetSelector": "Auto",
                        "isEnabled": True,
                        "connectionId": 3,
                        "status": "OK"
                    },
                    {
                        "targetSelector": "Auto",
                        "isEnabled": True,
                        "connectionId": 4,
                        "status": "OK"
                    }
                ],
                "bootVolumePriority": "Primary",
                "volume": None,
                "state": "Attached",
                "volumeUri": "SVOL:encl_41y_spt_volume",
                "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                "id": 1
            },
            {
                "storagePaths": [{"targetSelector": "Auto", "isEnabled": True, "connectionId": 3},
                                 {"targetSelector": "Auto", "isEnabled": True, "connectionId": 4}],

                "volume": None,
                "state": "Attached",
                "volumeUri": "SVOL:encl_41y_share_volume",
                "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                "id": 2},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_1",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 3},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_2",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 4},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_3",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 5},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_4",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 6},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_5",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 7},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_6",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 8},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_7",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 9},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_8",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 10},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_9",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 11},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_10",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 12},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_11",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 13},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_12",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 14},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_13",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 15},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_14",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 16},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_15",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 17}
        ],
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True
    },
}
]

expected_server_profiles_from_spt_postupgrade = [{
    "type": "ServerProfileV10",
    "name": "Enclosure2_FC_Potash_uefi_Bay7_SPT",
    "serverHardwareUri": "SH:Enclosure2, bay 7",
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "firmware": {
            "firmwareScheduleDateTime": None,
            "firmwareActivationType": None,
            "firmwareInstallType": None,
            "forceInstallFirmware": False,
            "manageFirmware": False,
            "firmwareBaselineUri": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "Ethernet",
                "networkUri": "NS:nswithmgmtuntagged1_1",
                "portId": "Mezz 3:1-a",
                "boot": {
                        "priority": "Primary"
                },
            },
            {
                "id": 2,
                "name": "",
                "functionType": "Ethernet",
                "networkUri": "NS:nswithmgmtuntagged1_1",
                "portId": "Mezz 3:2-a",
                "boot": {
                        "priority": "Secondary"
                },
            },
            {
                "id": 3,
                "name": "",
                "functionType": "FibreChannel",
                "networkUri": "FC:fc_tb_fab1_1",
                "portId": "Mezz 3:1-b",
                "boot": {
                        "priority": "Primary",
                        "bootVolumeSource": "ManagedVolume"
                },
            },
            {
                "id": 4,
                "name": "",
                "functionType": "FibreChannel",
                "networkUri": "FC:fc_tb_fab2_1",
                "portId": "Mezz 3:2-b",
                "boot": {
                        "priority": "Secondary",
                        "bootVolumeSource": "ManagedVolume"
                },
            }
        ]
    },
    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [],
        "reapplyState": "NotApplying"
    },
    "sanStorage": {
        "volumeAttachments": [
            {
                "storagePaths": [
                    {
                        "targetSelector": "Auto",
                        "isEnabled": True,
                        "connectionId": 3,
                        "status": "OK"
                    },
                    {
                        "targetSelector": "Auto",
                        "isEnabled": True,
                        "connectionId": 4,
                        "status": "OK"
                    }
                ],
                "bootVolumePriority": "Primary",
                "volume": None,
                "state": "Attached",
                # "volumeUri": "SVOL:encl_41y_spt_volume",
                "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                "id": 1
            },
            {
                "storagePaths": [{"targetSelector": "Auto", "isEnabled": True, "connectionId": 3},
                                 {"targetSelector": "Auto", "isEnabled": True, "connectionId": 4}],

                "volume": None,
                "state": "Attached",
                "volumeUri": "SVOL:encl_41y_share_volume",
                "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                "id": 2},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_1",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 3},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_2",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 4},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_3",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 5},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_4",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 6},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_5",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 7},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_6",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 8},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_7",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 9},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_8",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 10},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_9",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 11},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_10",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 12},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_11",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 13},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_12",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 14},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_13",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 15},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_14",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 16},
            {"storagePaths": [{"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 3},
                              {"targetSelector": "Auto",
                               "isEnabled": True,
                               "connectionId": 4}],

             "volume": None,
             "state": "Attached",
             "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_15",
             "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
             "id": 17}
        ],
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True
    },
}
]

delete_storage_volumes_ov_only = [
    {'name': 'DND_encl_41z_bay8_volume'},
    {'name': 'DND_encl_423_bay2_volume'},
    {'name': 'DND_encl_423_bay7_volume'},
    {'name': 'DND_encl_423_bay1_volume'},
    {'name': 'DND_encl_423_bay3_volume'},
    {'name': 'DND_encl_423_bay10_volume'},
    {'name': 'DND_encl_41y_bay2_volume'},
    {'name': 'DND_encl_41z_bay1_volume'},
    {'name': 'DND_encl_41z_bay3_volume'},
    {'name': 'DND_encl_41z_bay2_volume'},
    {'name': 'DND_encl_423_bay8_volume'},
    {'name': 'DND_encl_41y_bay1_volume'},
    {'name': 'encl_41y_share_volume'},
    {'name': 'encl_41z_share_volume'},
    {'name': 'encl_423_share_volume'}
]

delete_storage_volume = [{"name": "encl_41y_bay1_nonboot_volume"},
                         {"name": "encl_41z_bay1_nonboot_volume"},
                         {"name": "encl_423_bay1_nonboot_volume"},
                         {"name": "encl_423_bay9_nonboot_volume"},
                         {"name": "encl_41y_new_volume"},
                         {"name": "encl_41z_new_volume"},
                         {"name": "encl_423_new_volume"}
                         ]

# Use "create shared volumes data" to form the body for delete volumes
delete_storage_shared_volumes = [{"name": y['name']} for y in potash_iscsi_shared_volumes +
                                 potash_fcoe_shared_volumes + potash_fc_shared_volumes + carbon_fc_shared_volumes if 'name' in y]

# Merge multiple list of dictionaries to form single list of dictonaries
delete_storage_volumes = list(OrderedDict((frozenset(x.items()), x)
                                          for x in delete_storage_shared_volumes + delete_storage_volume).values())

# Use "create iscsi shared volume data" to form the body to delete volumes
# in 3par hosts
remove_iscsi_exported_volumes = [{"name": y['name']}
                                 for y in potash_iscsi_shared_volumes if 'name' in y]

server_profile_data = [{'type': 'ServerProfileV10', 'name': 'Enclosure3_FC_Potash_Legacy_Bay1_win2k16', 'serverHardwareUri': 'Enclosure3, bay 1',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                             'networkUri': 'FC:fc_tb_fab1_1',
                                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                            {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                                             "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                             "networkUri": "FC:fc_tb_fab2_1",
                                             "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_423_bay1_volume',
                                                              'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {"id": 2,
                                                              "volumeUri": None,
                                                              "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                              "lunType": "Auto",
                                                              "lun": "",
                                                              "storagePaths": [{
                                                                  "isEnabled": True,
                                                                  "connectionId": 3,
                                                                  'targetSelector': 'Auto'
                                                              }, {
                                                                  "isEnabled": True,
                                                                  "connectionId": 4,
                                                                  'targetSelector': 'Auto'
                                                              }
                                                              ],
                                                              "volume": {
                                                                  "isPermanent": True,
                                                                  "properties": {
                                                                      "name": "encl_423_bay1_nonboot_volume",
                                                                      "description": "",
                                                                      "storagePool": "SPOOL:FC_r1",
                                                                      "size": 5073741824,
                                                                      "provisioningType": "Thin",
                                                                      "isShareable": False
                                                                  },
                                                                  "templateUri": "ROOT:FC_r1"
                                                              }
                                                              },
                                                             {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                             ]},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]},
                        'localStorage': {}},

                       {'type': 'ServerProfileV10', 'name': 'Enclosure3_FC_Potash_uefi_Bay3_ESXi_1', 'serverHardwareUri': 'Enclosure3, bay 3',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                             'networkUri': 'FC:fc_tb_fab1_1',
                                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                            {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                                             "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                             "networkUri": "FC:fc_tb_fab2_1",
                                             "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_423_bay3_volume',
                                                              'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {"id": 2,
                                                              "volumeUri": None,
                                                              "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                              "lunType": "Auto",
                                                              "lun": "",
                                                              "storagePaths": [{
                                                                  "isEnabled": True,
                                                                  "connectionId": 3,
                                                                  'targetSelector': 'Auto'
                                                              }, {
                                                                  "isEnabled": True,
                                                                  "connectionId": 4,
                                                                  'targetSelector': 'Auto'
                                                              }
                                                              ],
                                                              "volume": {
                                                                  "isPermanent": True,
                                                                  "properties": {
                                                                      "name": "encl_423_bay3_nonboot_volume",
                                                                      "description": "",
                                                                      "storagePool": "SPOOL:FC_r1",
                                                                      "size": 5073741824,
                                                                      "provisioningType": "Thin",
                                                                      "isShareable": False
                                                                  },
                                                                  "templateUri": "ROOT:FC_r1"
                                                              }
                                                              },
                                                             {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                             ]},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]},
                        'localStorage': {}},

                       {'type': 'ServerProfileV10', 'name': 'Enclosure3_FcOE_Potash_legacy_Bay7', 'serverHardwareUri': 'Enclosure3, bay 7',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': 'fcoe1', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                             'networkUri': 'FCOE:fcoe_3801_1',
                                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                            {"id": 4, "name": "fcoe2", "functionType": "FibreChannel",
                                             "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                             "networkUri": "FCOE:fcoe_3802_1",
                                             "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_423_bay7_volume',
                                                              'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {"id": 2,
                                                              "volumeUri": None,
                                                              "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                              "lunType": "Auto",
                                                              "lun": "",
                                                              "storagePaths": [{
                                                                  "isEnabled": True,
                                                                  "connectionId": 3,
                                                                  'targetSelector': 'Auto'
                                                              }, {
                                                                  "isEnabled": True,
                                                                  "connectionId": 4,
                                                                  'targetSelector': 'Auto'
                                                              }
                                                              ],
                                                              "volume": {
                                                                  "isPermanent": True,
                                                                  "properties": {
                                                                      "name": "encl_423_bay7_nonboot_volume",
                                                                      "description": "",
                                                                      "storagePool": "SPOOL:FC_r1",
                                                                      "size": 5073741824,
                                                                      "provisioningType": "Thin",
                                                                      "isShareable": False
                                                                  },
                                                                  "templateUri": "ROOT:FC_r1"
                                                              }
                                                              },
                                                             {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                             ]},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]},
                        'localStorage': {}},

                       {'type': 'ServerProfileV10', 'name': 'Enclosure3_iscsi_Potash_uefi_Bay9', 'serverHardwareUri': 'Enclosure3, bay 9',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical',
                        "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcgblst00g",
                        "iscsiInitiatorNameType": "UserDefined", 'macType': 'Physical', 'wwnType': 'Physical', 'description': '', 'affinity': 'Bay',
                        "bootMode": {
                            "manageMode": True,
                            "mode": "UEFI",
                            "pxeBootPolicy": "Auto",
                            "secureBoot": "Disabled"
                        },
                        "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
                        "connectionSettings": {
                            "connections": [
                                {'id': 1, 'name': 'eth1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                 'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                 'boot': {'priority': 'Primary'}},
                                {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                 'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                 'boot': {'priority': 'Secondary'}},
                                {
                                    "id": 3,
                                    "name": "iscsi21",
                                    "functionType": "iSCSI",
                                    "networkUri": "ETH:iscsi_1121",
                                    "portId": "Mezz 3:1-b",
                                    "requestedMbps": "2500",
                                    "ipv4": {
                                        "ipAddressSource": "DHCP"
                                    },
                                    "boot": {
                                        "priority": "Primary",
                                        "bootVolumeSource": "UserDefined",
                                        "iscsi": {
                                            "initiatorNameSource": "ProfileInitiatorName",
                                            "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgblst00g",
                                            "bootTargetName": "iqn.2000-05.com.3pardata:20210002ac01d998",
                                            "bootTargetLun": "0",
                                            "firstBootTargetIp": "10.121.0.21",
                                            "firstBootTargetPort": "3260",
                                            "secondBootTargetPort": "",
                                            "chapLevel": "None",
                                            "chapName": "",
                                            "mutualChapName": ""
                                        }
                                    },
                                },
                                {
                                    "id": 4,
                                    "name": "iscsi22",
                                    "functionType": "iSCSI",
                                    "networkUri": "ETH:iscsi_1121",
                                    "portId": "Mezz 3:2-b",
                                    "requestedMbps": "2500",
                                    "ipv4": {
                                        "ipAddressSource": "DHCP"
                                    },
                                    "boot": {
                                        "priority": "Secondary",
                                        "bootVolumeSource": "UserDefined",
                                        "iscsi": {
                                            "initiatorNameSource": "ProfileInitiatorName",
                                            "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgblst00g",
                                            "bootTargetName": "iqn.2000-05.com.3pardata:21210002ac01d998",
                                            "bootTargetLun": "0",
                                            "firstBootTargetIp": "10.122.0.21",
                                            "firstBootTargetPort": "3260",
                                            "secondBootTargetIp": "",
                                            "secondBootTargetPort": "",
                                            "chapLevel": "None",
                                            "chapName": "",
                                            "mutualChapName": ""
                                        }
                                    },
                                }
                            ]
                        },
                        "bootMode": {
                            "manageMode": True,
                            "mode": "UEFI",
                            "pxeBootPolicy": "Auto",
                            "secureBoot": "Disabled"
                        },
                        "boot": {
                            "manageBoot": True,
                            "order": [
                                "HardDisk"
                            ]
                        },
                        "bios": {
                            "manageBios": False,
                        },
                        "localStorage": {
                        },
                        "sanStorage": {
                            "manageSanStorage": False,
                            "volumeAttachments": [],
                        },
                        },

                       {'type': 'ServerProfileV10', 'name': 'Enclosure2_FC_Carbon_uefi_Bay1', 'serverHardwareUri': 'Enclosure2, bay 1',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                             'networkUri': 'FC:fc_tb_fab1_1',
                                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                            {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                                             "portId": 'Mezz 1:2', "requestedMbps": "Auto",
                                             "networkUri": "FC:fc_tb_fab2_1",
                                             "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41y_bay1_volume',
                                                              'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {"id": 2,
                                                              "volumeUri": None,
                                                              "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                              "lunType": "Auto",
                                                              "lun": "",
                                                              "storagePaths": [{
                                                                  "isEnabled": True,
                                                                  "connectionId": 3,
                                                                  'targetSelector': 'Auto'
                                                              }, {
                                                                  "isEnabled": True,
                                                                  "connectionId": 4,
                                                                  'targetSelector': 'Auto'
                                                              }
                                                              ],
                                                              "volume": {
                                                                  "isPermanent": True,
                                                                  "properties": {
                                                                      "name": "encl_41y_bay1_nonboot_volume",
                                                                      "description": "",
                                                                      "storagePool": "SPOOL:FC_r1",
                                                                      "size": 5073741824,
                                                                      "provisioningType": "Thin",
                                                                      "isShareable": False
                                                                  },
                                                                  "templateUri": "ROOT:FC_r1"
                                                              }
                                                              },
                                                             {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 7, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_1',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 8, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_2',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 9, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_3',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 10, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_4',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 11, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_5',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 12, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_6',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 13, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_7',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 14, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_8',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 15, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_9',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 16, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_10',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 17, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_11',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 18, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_12',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 19, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_13',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 20, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_14',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 21, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_15',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                             ]},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]},
                        'localStorage': {}},

                       {'type': 'ServerProfileV10', 'name': 'Enclosure2_Localhdd_uefi_Bay8', 'serverHardwareUri': 'Enclosure2, bay 8',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                             'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}},
                                            {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                             'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}}
                                            ]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': [],
                                       'sanSystemCredentials': []},
                        'localStorage': {'controllers': [
                            {'deviceSlot': 'Embedded', 'initialize': False, 'mode': 'RAID',
                             'importConfiguration': True}], 'sasLogicalJBODs': []},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]}
                        },

                       {'type': 'ServerProfileV10', 'name': 'Enclosure1_FC_Potash_Legacy_Bay1_ESXi_3', 'serverHardwareUri': 'Enclosure1, bay 1',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                             'networkUri': 'FC:fc_tb_fab1_1',
                                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                            {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                                             "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                             "networkUri": "FC:fc_tb_fab2_1",
                                             "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41z_bay1_volume',
                                                              'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {"id": 2,
                                                              "volumeUri": None,
                                                              "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                              "lunType": "Auto",
                                                              "lun": "",
                                                              "storagePaths": [{
                                                                  "isEnabled": True,
                                                                  "connectionId": 3,
                                                                  'targetSelector': 'Auto'
                                                              }, {
                                                                  "isEnabled": True,
                                                                  "connectionId": 4,
                                                                  'targetSelector': 'Auto'
                                                              }
                                                              ],
                                                              "volume": {
                                                                  "isPermanent": True,
                                                                  "properties": {
                                                                      "name": "encl_41z_bay1_nonboot_volume",
                                                                      "description": "",
                                                                      "storagePool": "SPOOL:FC_r1",
                                                                      "size": 5073741824,
                                                                      "provisioningType": "Thin",
                                                                      "isShareable": False
                                                                  },
                                                                  "templateUri": "ROOT:FC_r1"
                                                              }
                                                              },
                                                             {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                             ]},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]},
                        'localStorage': {}},

                       {'type': 'ServerProfileV10', 'name': 'Enclosure1_FCoE_Potash_Legacy_Bay3', 'serverHardwareUri': 'Enclosure1, bay 3',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': 'fcoe1', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                             'networkUri': 'FCOE:fcoe_3801_1',
                                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                            {"id": 4, "name": "fcoe2", "functionType": "FibreChannel",
                                             "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                             "networkUri": "FCOE:fcoe_3802_1",
                                             "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41z_bay3_volume',
                                                              'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {"id": 2,
                                                              "volumeUri": None,
                                                              "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                              "lunType": "Auto",
                                                              "lun": "",
                                                              "storagePaths": [{
                                                                  "isEnabled": True,
                                                                  "connectionId": 3,
                                                                  'targetSelector': 'Auto'
                                                              }, {
                                                                  "isEnabled": True,
                                                                  "connectionId": 4,
                                                                  'targetSelector': 'Auto'
                                                              }
                                                              ],
                                                              "volume": {
                                                                  "isPermanent": True,
                                                                  "properties": {
                                                                      "name": "encl_41z_bay3_nonboot_volume",
                                                                      "description": "",
                                                                      "storagePool": "SPOOL:FC_r1",
                                                                      "size": 5073741824,
                                                                      "provisioningType": "Thin",
                                                                      "isShareable": False
                                                                  },
                                                                  "templateUri": "ROOT:FC_r1"
                                                              }
                                                              },
                                                             {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                             ]},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]},
                        'localStorage': {}},

                       {'type': 'ServerProfileV10', 'name': 'Enclosure3_FC_Potash_Legacy_Bay2_win2k16', 'serverHardwareUri': 'Enclosure3, bay 2',
                        'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                        'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        "connectionSettings": {
                            'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Primary'}},
                                            {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                             'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                             'boot': {'priority': 'Secondary'}},
                                            {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                                             'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                             'networkUri': 'FC:fc_tb_fab1_1',
                                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                            {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                                             "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                             "networkUri": "FC:fc_tb_fab2_1",
                                             "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                        "firmware": {
                            "firmwareInstallType": None,
                            "forceInstallFirmware": False,
                            "manageFirmware": False,
                        },
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_423_bay2_volume',
                                                              'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {"id": 2,
                                                              "volumeUri": None,
                                                              "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                              "lunType": "Auto",
                                                              "lun": "",
                                                              "storagePaths": [{
                                                                  "isEnabled": True,
                                                                  "connectionId": 3,
                                                                  'targetSelector': 'Auto'
                                                              }, {
                                                                  "isEnabled": True,
                                                                  "connectionId": 4,
                                                                  'targetSelector': 'Auto'
                                                              }
                                                              ],
                                                              "volume": {
                                                                  "isPermanent": True,
                                                                  "properties": {
                                                                      "name": "encl_423_bay2_nonboot_volume",
                                                                      "description": "",
                                                                      "storagePool": "SPOOL:FC_r1",
                                                                      "size": 5073741824,
                                                                      "provisioningType": "Thin",
                                                                      "isShareable": False
                                                                  },
                                                                  "templateUri": "ROOT:FC_r1"
                                                              }
                                                              },
                                                             {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                             {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',

                                                              'lunType': 'Auto', 'lun': '',
                                                              'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                               {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                             ]},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                            {'id': 'AdminPhone',
                                                                             'value': '123-123-4321'}]},
                        'localStorage': {}},

                       {
    'type': 'ServerProfileV10',
    'name': 'Enclosure1_BB_logicaldrives_Natsha_legacy_Bay7',
    'description': '',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': 'Enclosure1, bay 7',
    'enclosureGroupUri': 'EG:EG',
    'affinity': 'Bay',
    'hideUnusedFlexNics': True,
    'firmware': {'firmwareInstallType': None,
                 'forceInstallFirmware': False,
                 'manageFirmware': False},
    'macType': 'Physical',
    'wwnType': 'Physical',
    'serialNumberType': 'Physical',
    'connectionSettings': {'connections': [{
        'id': 1,
        'name': 'eth1',
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:eth1_1151',
        'functionType': 'Ethernet',
        'boot': {'priority': 'Primary'},
    }, {
        'id': 2,
        'name': 'eth2',
        'portId': 'Mezz 3:2-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:eth1_1151',
        'functionType': 'Ethernet',
        'boot': {'priority': 'Secondary'},
    },
        {'id': 3, 'name': 'eth3', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
        {'id': 4, 'name': 'eth4', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
        {'id': 5, 'name': 'eth5', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
        {'id': 6, 'name': 'eth6', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
        {'id': 7, 'name': 'eth7', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
        {'id': 8, 'name': 'eth8', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}}]},
    'bootMode': {'manageMode': True, 'mode': 'BIOS',
                 'pxeBootPolicy': None},
    'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'HardDisk',
                                           'PXE']},
    'bios': {'manageBios': False},
    'localStorage': {'sasLogicalJBODs': [{
        'id': 1,
        'deviceSlot': 'Mezz 1',
        'name': 'Data Storage',
        'numPhysicalDrives': 1,
        'driveMinSizeGB': 600,
        'driveMaxSizeGB': 600,
        'driveTechnology': 'SasHdd',
        'sasLogicalJBODUri': None,
        'eraseData': False,
    }], 'controllers': [{
        'deviceSlot': 'Mezz 1',
        'mode': 'Mixed',
        'initialize': False,
        'importConfiguration': False,
        'logicalDrives': [{
                'name': None,
                'raidLevel': 'RAID0',
                'bootable': True,
                'numPhysicalDrives': None,
                'driveTechnology': None,
                'sasLogicalJBODId': 1,
        }],
    }]},
    'sanStorage': {'manageSanStorage': False, 'volumeAttachments': [],
                   'sanSystemCredentials': []},
}
]

server_profile_data_postupgrade = [
    {'type': 'ServerProfileV10', 'name': 'Enclosure1_FC_Potash_Legacy_Bay8_win2k16', 'serverHardwareUri': 'Enclosure1, bay 8',
     'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
     'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     "connectionSettings": {
         'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Primary'}},
                         {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Secondary'}},
                         {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                          'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                          'networkUri': 'FC:fc_tb_fab1_1',
                          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                         {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                          "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                          "networkUri": "FC:fc_tb_fab2_1",
                          "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
     "firmware": {
         "firmwareInstallType": None,
         "forceInstallFirmware": False,
         "manageFirmware": False,
     },
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                    'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41z_bay8_volume',
                                           'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {"id": 2,
                                           "volumeUri": None,
                                           "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                           "lunType": "Auto",
                                           "lun": "",
                                           "storagePaths": [{
                                               "isEnabled": True,
                                               "connectionId": 3,
                                               'targetSelector': 'Auto'
                                           }, {
                                               "isEnabled": True,
                                               "connectionId": 4,
                                               'targetSelector': 'Auto'
                                           }
                                           ],
                                           "volume": {
                                               "isPermanent": True,
                                               "properties": {
                                                   "name": "encl_41z_bay8_nonboot_volume",
                                                   "description": "",
                                                   "storagePool": "SPOOL:FC_r1",
                                                   "size": 5073741824,
                                                   "provisioningType": "Thin",
                                                   "isShareable": False
                                               },
                                               "templateUri": "ROOT:FC_r1"
                                           }
                                           },
                                          {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                          ]},
     'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                         {'id': 'AdminPhone',
                                                          'value': '123-123-4321'}]},
     'localStorage': {}},

    {'type': 'ServerProfileV10', 'name': 'Enclosure3_FcOE_Potash_uefi_Bay8', 'serverHardwareUri': 'Enclosure3, bay 8',
     'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     "connectionSettings": {
         'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Primary'}},
                         {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Secondary'}},
                         {'id': 3, 'name': 'fcoe1', 'functionType': 'FibreChannel',
                          'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                          'networkUri': 'FCOE:fcoe_3801_1',
                          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                         {"id": 4, "name": "fcoe2", "functionType": "FibreChannel",
                          "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                          "networkUri": "FCOE:fcoe_3802_1",
                          "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
     "firmware": {
         "firmwareInstallType": None,
         "forceInstallFirmware": False,
         "manageFirmware": False,
     },
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                    'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_423_bay8_volume',
                                           'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {"id": 2,
                                           "volumeUri": None,
                                           "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                           "lunType": "Auto",
                                           "lun": "",
                                           "storagePaths": [{
                                               "isEnabled": True,
                                               "connectionId": 3,
                                               'targetSelector': 'Auto'
                                           }, {
                                               "isEnabled": True,
                                               "connectionId": 4,
                                               'targetSelector': 'Auto'
                                           }
                                           ],
                                           "volume": {
                                               "isPermanent": True,
                                               "properties": {
                                                   "name": "encl_423_bay8_nonboot_volume",
                                                   "description": "",
                                                   "storagePool": "SPOOL:FC_r1",
                                                   "size": 5073741824,
                                                   "provisioningType": "Thin",
                                                   "isShareable": False
                                               },
                                               "templateUri": "ROOT:FC_r1"
                                           }
                                           },
                                          {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                          ]},
     'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                         {'id': 'AdminPhone',
                                                          'value': '123-123-4321'}]},
     'localStorage': {}},

    {'type': 'ServerProfileV10', 'name': 'Enclosure3_FC_Potash_legacy_Bay10', 'serverHardwareUri': 'Enclosure3, bay 10',
     'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
     'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     "connectionSettings": {
         'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Primary'}},
                         {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Secondary'}},
                         {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                          'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                          'networkUri': 'FC:fc_tb_fab1_1',
                          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                         {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                          "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                          "networkUri": "FC:fc_tb_fab2_1",
                          "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
     "firmware": {
         "firmwareInstallType": None,
         "forceInstallFirmware": False,
         "manageFirmware": False,
     },
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                    'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_423_bay10_volume',
                                           'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {"id": 2,
                                           "volumeUri": None,
                                           "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                           "lunType": "Auto",
                                           "lun": "",
                                           "storagePaths": [{
                                               "isEnabled": True,
                                               "connectionId": 3,
                                               'targetSelector': 'Auto'
                                           }, {
                                               "isEnabled": True,
                                               "connectionId": 4,
                                               'targetSelector': 'Auto'
                                           }
                                           ],
                                           "volume": {
                                               "isPermanent": True,
                                               "properties": {
                                                   "name": "encl_423_bay10_nonboot_volume",
                                                   "description": "",
                                                   "storagePool": "SPOOL:FC_r1",
                                                   "size": 5073741824,
                                                   "provisioningType": "Thin",
                                                   "isShareable": False
                                               },
                                               "templateUri": "ROOT:FC_r1"
                                           }
                                           },
                                          {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                          ]},
     'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                         {'id': 'AdminPhone',
                                                          'value': '123-123-4321'}]},
     'localStorage': {}},

    {'type': 'ServerProfileV10', 'name': 'Enclosure2_FC_Carbon_Legacy_Bay2_ESXi_2', 'serverHardwareUri': 'Enclosure2, bay 2',
     'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
     'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     "connectionSettings": {
         'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Primary'}},
                         {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                          'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                          'boot': {'priority': 'Secondary'}},
                         {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                          'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                          'networkUri': 'FC:fc_tb_fab1_1',
                          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                         {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                          "portId": 'Mezz 1:2', "requestedMbps": "Auto",
                          "networkUri": "FC:fc_tb_fab2_1",
                          "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
     "firmware": {
         "firmwareInstallType": None,
         "forceInstallFirmware": False,
         "manageFirmware": False,
     },
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                    'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41y_bay2_volume',
                                           'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {"id": 2,
                                           "volumeUri": None,
                                           "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                           "lunType": "Auto",
                                           "lun": "",
                                           "storagePaths": [{
                                               "isEnabled": True,
                                               "connectionId": 3,
                                               'targetSelector': 'Auto'
                                           }, {
                                               "isEnabled": True,
                                               "connectionId": 4,
                                               'targetSelector': 'Auto'
                                           }
                                           ],
                                           "volume": {
                                               "isPermanent": True,
                                               "properties": {
                                                   "name": "encl_41y_bay2_nonboot_volume",
                                                   "description": "",
                                                   "storagePool": "SPOOL:FC_r1",
                                                   "size": 5073741824,
                                                   "provisioningType": "Thin",
                                                   "isShareable": False
                                               },
                                               "templateUri": "ROOT:FC_r1"
                                           }
                                           },
                                          {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                            {'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 7, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_1',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 8, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_2',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 9, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_3',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 10, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_4',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 11, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_5',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 12, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_6',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 13, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_7',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 14, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_8',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 15, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_9',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 16, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_10',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 17, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_11',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 18, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_12',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 19, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_13',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 20, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_14',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                          {'id': 21, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_15',

                                           'lunType': 'Auto', 'lun': '',
                                           'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                            {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                          ]},
     'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                         {'id': 'AdminPhone',
                                                          'value': '123-123-4321'}]},
     'localStorage': {}},

    {'type': 'ServerProfileV10', 'name': 'Enclosure2_Localhdd_legacy_Bay9', 'serverHardwareUri': 'Enclosure2, bay 9',
     'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
     'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     "connectionSettings": {
         'connections': [{'id': 1, 'name': 'eth1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                                                         'boot': {'priority': 'Primary'}},
                         {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                                                         'boot': {'priority': 'Secondary'}},
                         {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                          'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}},
                         {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                          'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}}
                         ]},
     "firmware": {
         "firmwareInstallType": None,
         "forceInstallFirmware": False,
         "manageFirmware": False,
     },
     'sanStorage': {'manageSanStorage': False, 'volumeAttachments': [],
                    'sanSystemCredentials': []},
     'localStorage': {'controllers': [
         {'deviceSlot': 'Embedded', 'initialize': False, 'mode': 'RAID',
          'importConfiguration': True}], 'sasLogicalJBODs': []},
     'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                                         {'id': 'AdminPhone',
                                                          'value': '123-123-4321'}]}
     },

    {'type': 'ServerProfileV10', 'name': 'Enclosure1_iscsi_Potash_uefi_Bay5', 'serverHardwareUri': 'Enclosure1, bay 5',
     'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical',
     "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcgblst00r",
     "iscsiInitiatorNameType": "UserDefined", 'macType': 'Physical', 'wwnType': 'Physical', 'description': '', 'affinity': 'Bay',
     "bootMode": {
         "manageMode": True,
         "mode": "UEFI",
         "pxeBootPolicy": "Auto",
         "secureBoot": "Disabled"
     },
     "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "Floppy", "USB", "PXE"]},
     "connectionSettings": {
         "connections": [
             {'id': 1, 'name': 'eth1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
              'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
              'boot': {'priority': 'Primary'}},
             {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
              'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
              'boot': {'priority': 'Secondary'}},
             {
                 "id": 3,
                 "name": "iscsi21",
                 "functionType": "iSCSI",
                 "networkUri": "ETH:iscsi_1121",
                 "portId": "Mezz 3:1-b",
                 "requestedMbps": "2500",
                 "ipv4": {
                     "ipAddressSource": "DHCP"
                 },
                 "boot": {
                     "priority": "Primary",
                     "bootVolumeSource": "UserDefined",
                     "iscsi": {
                         "initiatorNameSource": "ProfileInitiatorName",
                         "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgblst00r",
                         "bootTargetName": "iqn.2000-05.com.3pardata:20210002ac01d998",
                         "bootTargetLun": "0",
                         "firstBootTargetIp": "10.121.0.21",
                         "firstBootTargetPort": "3260",
                         "secondBootTargetPort": "",
                         "chapLevel": "None",
                         "chapName": "",
                         "mutualChapName": ""
                     }
                 },
             },
             {
                 "id": 4,
                 "name": "iscsi22",
                 "functionType": "iSCSI",
                 "networkUri": "ETH:iscsi_1121",
                 "portId": "Mezz 3:2-b",
                 "requestedMbps": "2500",
                 "ipv4": {
                     "ipAddressSource": "DHCP"
                 },
                 "boot": {
                     "priority": "Secondary",
                     "bootVolumeSource": "UserDefined",
                     "iscsi": {
                         "initiatorNameSource": "ProfileInitiatorName",
                         "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgblst00r",
                         "bootTargetName": "iqn.2000-05.com.3pardata:21210002ac01d998",
                         "bootTargetLun": "0",
                         "firstBootTargetIp": "10.122.0.21",
                         "firstBootTargetPort": "3260",
                         "secondBootTargetIp": "",
                         "secondBootTargetPort": "",
                         "chapLevel": "None",
                         "chapName": "",
                         "mutualChapName": ""
                     }
                 },
             }
         ]
     },
     "bootMode": {
         "manageMode": True,
         "mode": "UEFI",
         "pxeBootPolicy": "Auto",
         "secureBoot": "Disabled"
     },
     "boot": {
         "manageBoot": True,
         "order": [
             "HardDisk"
         ]
     },
     "bios": {
         "manageBios": False,
     },
     "localStorage": {
     },
     "sanStorage": {
         "manageSanStorage": False,
         "volumeAttachments": [],
     },
     },

    {
        "name": "Enclosure1_BB_JBODS_Natsha_uefi_Bay6",
        "type": "ServerProfileV10",
        "serverHardwareUri": "Enclosure1, bay 6",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {'id': 1, 'name': 'eth1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                 'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                 'boot': {'priority': 'Primary'}},
                {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                 'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                 'boot': {'priority': 'Secondary'}},
                {'id': 3, 'name': 'eth3', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': 'eth4', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 5, 'name': 'eth5', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 6, 'name': 'eth6', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 7, 'name': 'eth7', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 8, 'name': 'eth8', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}}

            ]
        },
        "boot": {
            "manageBoot": True,
            "order": ['HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": None,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{'deviceSlot': 'Mezz 1', 'driveMinSizeGB': 600, 'name': 'jbod', 'driveMaxSizeGB': 600, 'eraseData': False, 'driveTechnology': 'SasHdd', 'numPhysicalDrives': 1, 'id': 1, "sasLogicalJBODUri": None, }],
            "controllers": [{'deviceSlot': 'Mezz 1', 'importConfiguration': False, 'mode': 'HBA', 'initialize': False, 'logicalDrives': []}]
        },
        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': [],
                       'sanSystemCredentials': []},
    }
]

edit_server_profiles = [{'type': 'ServerProfileV10', 'name': 'Enclosure2_Localhdd_uefi_Bay8',
                         'serverHardwareUri': 'Enclosure2, bay 8',
                         'enclosureGroupUri': 'EG:EG',
                         'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated',
                         'macType': 'Physical', 'wwnType': 'Physical',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         "connectionSettings": {
                             'connections': [{'id': 1, 'name': 'eth1', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                              'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                                              'boot': {'priority': 'Primary'}},
                                             {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                              'networkUri': 'ETH:eth1_1151', 'functionType': 'Ethernet',
                                              'boot': {'priority': 'Secondary'}},
                                             {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                              'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}},
                                             {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                              'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}}
                                             ]},
                         "firmware": {
                             "firmwareInstallType": None,
                             "forceInstallFirmware": False,
                             "manageFirmware": False,
                         },
                         'sanStorage': {'manageSanStorage': False, 'volumeAttachments': [],
                                        'sanSystemCredentials': []},
                         "localStorage":{"controllers": [{"logicalDrives": [], "deviceSlot": "Embedded", "mode": "RAID",
                                                          "initialize": False, "importConfiguration": False}]},
                         'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                                                             {'id': 'AdminPhone',
                                                                              'value': '1800-123-4321'},
                                                                             {"id": "AdminEmail",
                                                                              "value": "sat.regression@hpe.com"}]}
                         }]

expected_edit_server_profiles = [
    {
        "type": "ServerProfileV10",
        "name": "Enclosure2_Localhdd_uefi_Bay8",
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

spt_edit_data = [{
    "type": "ServerProfileTemplateV6",
    "name": "spt_encl_41y_bay3_bay7",
    "serverHardwareTypeUri": 'SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA',
    "enclosureGroupUri": "EG:EG",
    "affinity": "Bay",
    "macType": "Virtual",
    "serialNumberType": "Virtual",
    "wwnType": "Virtual",
    'connectionSettings': {"manageConnections": True,
                           'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:nswithmgmtuntagged1_1',
                                            'boot': {'priority': 'Primary'}},
                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                            'requestedMbps': '2500', 'networkUri': 'NS:nswithmgmtuntagged1_1',
                                            'boot': {'priority': 'Secondary'}},
                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '2500',
                                            'networkUri': 'FC:fc_tb_fab1_1',
                                            'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": 'Mezz 3:2-b',
                                            "requestedMbps": "2500", "networkUri": "FC:fc_tb_fab2_1",
                                            "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
    },
    "hideUnusedFlexNics": True,
    "bios": {'manageBios': True,
             'overriddenSettings': []},
    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    "sanStorage": {"hostOSType": "Windows 2012 / WS2012 R2", "manageSanStorage": True,
                   "volumeAttachments": [{
                       "id": 1,
                       "associatedTemplateAttachmentId": "uniqueid1",
                       "bootVolumePriority": "Primary",
                       "lun": 1,
                       "lunType": 'Manual',
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
                               "name": "encl_41y_spt_volume",
                               "description": "",
                               "storagePool": "SPOOL:" + "FC_r1",
                               "size": 32213741824,
                               "provisioningType": "Thin",
                               "isShareable": False},
                           "templateUri": "ROOT:" + "FC_r1",
                       },
                       "volumeStorageSystemUri": "SSYS:" + "RIST-R1-3PAR",
                       "volumeUri": None,
                   },
                       {'id': 2, 'volumeUri': 'SVOL:encl_41y_share_volume',
                        "associatedTemplateAttachmentId": "uniqueid2",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 3, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                        "associatedTemplateAttachmentId": "uniqueid3",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 4, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                        "associatedTemplateAttachmentId": "uniqueid4",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 5, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                        "associatedTemplateAttachmentId": "uniqueid5",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 6, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                        "associatedTemplateAttachmentId": "uniqueid6",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                        "associatedTemplateAttachmentId": "uniqueid7",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                        "associatedTemplateAttachmentId": "uniqueid8",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                        "associatedTemplateAttachmentId": "uniqueid9",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                        "associatedTemplateAttachmentId": "uniqueid10",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                        "associatedTemplateAttachmentId": "uniqueid11",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                        "associatedTemplateAttachmentId": "uniqueid12",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                        "associatedTemplateAttachmentId": "uniqueid13",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                        "associatedTemplateAttachmentId": "uniqueid14",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                        "associatedTemplateAttachmentId": "uniqueid15",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                        "associatedTemplateAttachmentId": "uniqueid16",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                       {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                        "associatedTemplateAttachmentId": "uniqueid17",
                        'lunType': 'Auto', 'lun': '',
                        'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                         {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                   ]
                   }
}]

re_assign_server_profile = {'type': 'ServerProfileV10', 'name': 'Enclosure3_FC_Potash_legacy_Bay10', 'serverHardwareUri': 'Enclosure3, bay 10',
                                    'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    "connectionSettings": {
                                        'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                         'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                         'boot': {'priority': 'Primary'}},
                                                        {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                         'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                         'boot': {'priority': 'Secondary'}},
                                                        {'id': 3, 'name': 'fc1', 'functionType': 'FibreChannel',
                                                         'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                                         'networkUri': 'FC:fc_tb_fab1_1',
                                                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                        {"id": 4, "name": "fc2", "functionType": "FibreChannel",
                                                         "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                                         "networkUri": "FC:fc_tb_fab2_1",
                                                         "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                    "firmware": {
                                        "firmwareInstallType": None,
                                        "forceInstallFirmware": False,
                                        "manageFirmware": False,
                                    },
                            'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                           'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_423_bay10_volume',
                                                                  'lunType': 'Auto', 'lun': '', "bootVolumePriority": "Primary",
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                   {'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 2, 'volumeUri': 'SVOL:encl_423_bay10_nonboot_volume',
                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                   {'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                   {'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                   {'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                   {'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                 {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',

                                                                  'lunType': 'Auto', 'lun': '',
                                                                  'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                   {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                                 ]},
                            'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                                {'id': 'AdminPhone',
                                                                                 'value': '123-123-4321'}]},
                            'localStorage': {}}

expected_server_profiles_postupgrade = [
    {
        "uri": "SP:Enclosure1_iscsi_Potash_uefi_Bay5",
        'status': 'OK', 'state': 'Normal',
        "name": "Enclosure1_iscsi_Potash_uefi_Bay5",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 5",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "iscsi21",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Primary'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "iscsi22",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Secondary'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:Enclosure2_Localhdd_uefi_Bay8",
        'status': 'OK', 'state': 'Normal',
        "name": "Enclosure2_Localhdd_uefi_Bay8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 8",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Physical",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}}
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                   {'id': 'AdminPhone',
                                    'value': '1800-123-4321'},
                                   {"id": "AdminEmail",
                                    "value": "sat.regression@hpe.com"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{'deviceSlot': 'Embedded', 'importConfiguration': False, 'mode': 'RAID', 'initialize': False}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:Enclosure1_BB_JBODS_Natsha_uefi_Bay6",
        'status': 'OK', 'state': 'Normal',
        "name": "Enclosure1_BB_JBODS_Natsha_uefi_Bay6",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 6",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': 'eth3', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': 'eth4', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 5, 'name': 'eth5', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 6, 'name': 'eth6', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 7, 'name': 'eth7', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 8, 'name': 'eth8', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}}
            ]

        },

        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{'deviceSlot': 'Mezz 1', 'status': 'OK', 'driveMinSizeGB': 600, 'name': 'jbod', 'driveMaxSizeGB': 600, 'eraseData': False, 'driveTechnology': 'SasHdd', 'numPhysicalDrives': 1, 'id': 1}],
            "controllers": [{'deviceSlot': 'Mezz 1', 'importConfiguration': False, 'mode': 'HBA', 'initialize': False, 'logicalDrives': []}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure2_Localhdd_legacy_Bay9",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 9",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}}
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'ME2-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{'deviceSlot': 'Embedded', 'importConfiguration': False, 'mode': 'RAID', 'initialize': False, 'logicalDrives': [{'name': 'Logical Drive 1', 'bootable': False, 'raidLevel': 'RAID0', 'sasLogicalJBODId': None, 'driveTechnology': None, 'numPhysicalDrives': 1}]}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure1_BB_logicaldrives_Natsha_legacy_Bay7",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 7",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': 'eth3', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': 'eth4', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 5, 'name': 'eth5', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 6, 'name': 'eth6', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 7, 'name': 'eth7', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 8, 'name': 'eth8', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}}
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{'deviceSlot': 'Mezz 1', 'driveMinSizeGB': 600, 'name': 'Data Storage', 'driveMaxSizeGB': 600, 'eraseData': False, 'driveTechnology': 'SasHdd', 'numPhysicalDrives': 1, 'id': 1}],
            "controllers": [{'deviceSlot': 'Mezz 1', 'importConfiguration': False, 'mode': 'Mixed', 'initialize': False, 'logicalDrives': [{'name': None, 'bootable': True, 'raidLevel': 'RAID0', 'sasLogicalJBODId': 1}]}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure3_iscsi_Potash_uefi_Bay9",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 9",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                 'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                 'boot': {'priority': 'Secondary'}},
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "iscsi21",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Primary'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "iscsi22",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Secondary'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure2_FC_Potash_uefi_Bay3_SPT",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'Regression-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:encl_41y_spt_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"},
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"},

                    ]
                },
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_1",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 3},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_2",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 4},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_3",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 5},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_4",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 6},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_5",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 7},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_6",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 8},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_7",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 9},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_8",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 10},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_9",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 11},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_10",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 12},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_11",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 13},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_12",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 14},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_13",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 15},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_14",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 16},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_15",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 17}

            ]

        },
    },
    {
        "name": "Enclosure2_FC_Potash_uefi_Bay7_SPT",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 7",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    # "volumeUri": "SVOL:encl_41y_spt_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"},

                    ]
                },
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_1",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 3},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_2",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 4},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_3",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 5},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_4",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 6},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_5",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 7},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_6",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 8},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_7",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 9},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_8",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 10},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_9",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 11},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_10",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 12},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_11",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 13},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_12",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 14},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_13",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 15},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_14",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 16},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_15",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 17}
            ]

        },
    },
    {
        "name": "Enclosure3_FcOE_Potash_uefi_Bay8",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 8",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay8_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay8_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_legacy_Bay10",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 10",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay10_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    # "volumeUri": "SVOL:encl_423_bay10_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_Legacy_Bay2_win2k16",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 2",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay2_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay2_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_uefi_Bay3_ESXi_1",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay3_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay3_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_Legacy_Bay1_win2k16",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 1",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay1_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay1_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FC_Potash_Legacy_Bay8_win2k16",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 8",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay8_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41z_bay8_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FCoE_Potash_Legacy_Bay3",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay3_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41z_bay3_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FCoE_Potash_Legacy_Bay3_copy",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 2",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay2_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FC_Potash_Legacy_Bay1_ESXi_3",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 1",
        "enclosureUri": "ENC:Enclosure1",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay1_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41z_bay1_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FcOE_Potash_legacy_Bay7",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 7",
        "enclosureUri": "ENC:Enclosure3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay7_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay7_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure2_FC_Carbon_uefi_Bay1",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 1",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "fc1",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "fc2",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'}, {'id': 'AdminPhone', 'value': '123-123-4321'}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41y_bay1_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_bay1_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure2_FC_Carbon_Legacy_Bay2_ESXi_2",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 2",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "fc1",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "fc2",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41y_bay2_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_bay2_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    }
]

expected_pre_post_server_profiles = [
    {
        "uri": "SP:Enclosure1_iscsi_Potash_uefi_Bay5",
        'status': 'OK', 'state': 'Normal',
        "name": "Enclosure1_iscsi_Potash_uefi_Bay5",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 5",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "iscsi21",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Primary'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "iscsi22",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Secondary'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:Enclosure2_Localhdd_uefi_Bay8",
        'status': 'OK', 'state': 'Normal',
        "name": "Enclosure2_Localhdd_uefi_Bay8",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 8",
        "enclosureGroupUri": "EG:EG",
        "serialNumberType": "Physical",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}}
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                   {'id': 'AdminPhone',
                                    'value': '1800-123-4321'},
                                   {"id": "AdminEmail",
                                    "value": "sat.regression@hpe.com"}]
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{'deviceSlot': 'Embedded', 'importConfiguration': False, 'mode': 'RAID', 'initialize': False}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "uri": "SP:Enclosure1_BB_JBODS_Natsha_uefi_Bay6",
        'status': 'OK', 'state': 'Normal',
        "name": "Enclosure1_BB_JBODS_Natsha_uefi_Bay6",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 6",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': 'eth3', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': 'eth4', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 5, 'name': 'eth5', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 6, 'name': 'eth6', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 7, 'name': 'eth7', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 8, 'name': 'eth8', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}}
            ]

        },

        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{'deviceSlot': 'Mezz 1', 'status': 'OK', 'driveMinSizeGB': 600, 'name': 'jbod', 'driveMaxSizeGB': 600, 'eraseData': False, 'driveTechnology': 'SasHdd', 'numPhysicalDrives': 1, 'id': 1}],
            "controllers": [{'deviceSlot': 'Mezz 1', 'importConfiguration': False, 'mode': 'HBA', 'initialize': False, 'logicalDrives': []}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure2_Localhdd_legacy_Bay9",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 9",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                 'requestedMbps': '2500', 'networkUri': 'NS:nsnomgmt1_1', 'boot': {'priority': 'NotBootable'}}
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{'deviceSlot': 'Embedded', 'importConfiguration': False, 'mode': 'RAID', 'initialize': False, 'logicalDrives': [{'name': 'Logical Drive 1', 'bootable': False, 'raidLevel': 'RAID0', 'sasLogicalJBODId': None, 'driveTechnology': None, 'numPhysicalDrives': 1}]}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure1_BB_logicaldrives_Natsha_legacy_Bay7",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 7",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:eth1_1151",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {'id': 3, 'name': 'eth3', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 4, 'name': 'eth4', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1123', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 5, 'name': 'eth5', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 6, 'name': 'eth6', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1124', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 7, 'name': 'eth7', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}},
                {'id': 8, 'name': 'eth8', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                          'networkUri': 'ETH:eth1_1125', 'functionType': 'Ethernet',
                          'boot': {'priority': 'NotBootable'}}
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [{'deviceSlot': 'Mezz 1', 'driveMinSizeGB': 600, 'name': 'Data Storage', 'driveMaxSizeGB': 600, 'eraseData': False, 'driveTechnology': 'SasHdd', 'numPhysicalDrives': 1, 'id': 1}],
            "controllers": [{'deviceSlot': 'Mezz 1', 'importConfiguration': False, 'mode': 'Mixed', 'initialize': False, 'logicalDrives': [{'name': None, 'bootable': True, 'raidLevel': 'RAID0', 'sasLogicalJBODId': 1}]}]
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure3_iscsi_Potash_uefi_Bay9",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 9",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {'id': 2, 'name': 'eth2', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                 'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                 'boot': {'priority': 'Secondary'}},
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "iscsi21",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Primary'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "iSCSI",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "iscsi22",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iscsi_1121",
                    "boot": {'priority': 'Secondary'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [
            ]

        },
    },
    {
        "name": "Enclosure2_FC_Potash_uefi_Bay3_SPT",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:encl_41y_spt_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"},
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"},

                    ]
                },
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_1",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 3},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_2",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 4},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_3",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 5},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_4",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 6},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_5",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 7},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_6",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 8},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_7",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 9},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_8",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 10},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_9",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 11},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_10",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 12},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_11",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 13},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_12",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 14},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_13",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 15},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_14",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 16},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_15",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 17}

            ]

        },
    },
    {
        "name": "Enclosure2_FC_Potash_uefi_Bay7_SPT",
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 7",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    # "volumeUri": "SVOL:encl_41y_spt_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"},
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"},

                    ]
                },
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_1",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 3},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_2",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 4},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_3",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 5},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_4",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 6},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_5",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 7},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_6",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 8},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_7",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 9},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_8",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 10},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_9",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 11},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_10",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 12},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_11",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 13},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_12",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 14},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_13",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 15},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_14",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 16},
                {"storagePaths": [{"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 3},
                                  {"targetSelector": "Auto",
                                   "isEnabled": True,
                                   "connectionId": 4}],

                 "volume": None,
                 "state": "Attached",
                 "volumeUri": "SVOL:sat3_potash_fc_cluster_shared_volume_15",
                 "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",
                 "id": 17}
            ]

        },
    },
    {
        "name": "Enclosure3_FcOE_Potash_uefi_Bay8",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 8",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay8_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay8_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto",
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto",
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_legacy_Bay10",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 10",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay10_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    # "volumeUri": "SVOL:encl_423_bay10_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_Legacy_Bay2_win2k16",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 2",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay2_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay2_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_uefi_Bay3_ESXi_1",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay3_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay3_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FC_Potash_Legacy_Bay1_win2k16",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 1",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay1_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay1_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FC_Potash_Legacy_Bay8_win2k16",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 8",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay8_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41z_bay8_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FCoE_Potash_Legacy_Bay3",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay3_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41z_bay3_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FCoE_Potash_Legacy_Bay3_copy",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 2",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay2_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure1_FC_Potash_Legacy_Bay1_ESXi_3",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure1, bay 1",
        "enclosureUri": "ENC:Enclosure1",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fc1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fc2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41z_bay1_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41z_bay1_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure3_FcOE_Potash_legacy_Bay7",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure3, bay 7",
        "enclosureUri": "ENC:Enclosure3",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 10000,
                    "name": "fcoe1",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3801_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 2000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 10000,
                    "name": "fcoe2",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2000",
                    "networkUri": "FCOE:fcoe_3802_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_423_bay7_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_423_bay7_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure2_FC_Carbon_uefi_Bay1",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 1",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "fc1",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "fc2",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },

        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41y_bay1_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_bay1_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    },
    {
        "name": "Enclosure2_FC_Carbon_Legacy_Bay2_ESXi_2",
        'status': 'OK', 'state': 'Normal',
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:Enclosure2, bay 2",
        "enclosureGroupUri": "EG:EG",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 1,
                    "maximumMbps": 10000,
                    "name": "eth1_1151",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Primary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 2500,
                    "functionType": "Ethernet",
                    "id": 2,
                    "maximumMbps": 10000,
                    "name": "eth2_1151",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "NS:nswithmgmtuntagged1_1",
                    "boot": {'priority': 'Secondary', 'ethernetBootType': 'PXE'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 3,
                    "maximumMbps": 16000,
                    "name": "fc1",
                    "portId": "Mezz 1:1",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab1_1",
                    "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'},
                },
                {
                    "allocatedMbps": 16000,
                    "functionType": "FibreChannel",
                    "id": 4,
                    "maximumMbps": 16000,
                    "name": "fc2",
                    "portId": "Mezz 1:2",
                    "requestedMbps": "Auto",
                    "networkUri": "FC:fc_tb_fab2_1",
                    "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'},
                }
            ]

        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "hideUnusedFlexNics": True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "SVOL:DND_encl_41y_bay2_volume",
                    "bootVolumePriority": "Primary",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 2,
                    "volumeUri": "SVOL:encl_41y_bay2_nonboot_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 3,
                    "volumeUri": "SVOL:encl_423_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 5,
                    "volumeUri": "SVOL:encl_41y_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {
                    "id": 6,
                    "volumeUri": "SVOL:encl_41z_share_volume",

                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 4,
                            "targetSelector": "Auto"
                        },
                        {
                            "isEnabled": True,
                            "connectionId": 3,
                            "targetSelector": "Auto"
                        },

                    ]
                },
                {'id': 7, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_1',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 8, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_2',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 9, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_3',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 10, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_4',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 11, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_5',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 12, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_6',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 13, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_7',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 14, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_8',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 15, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_9',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 16, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_10',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 17, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_11',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 18, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_12',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 19, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_13',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 20, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_14',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                {'id': 21, 'volumeUri': 'SVOL:sat3_carbon_fc_cluster_shared_volume_15',
                 'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                  {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
            ]

        },
    }
]

unassign_server_profile = [{'type': 'ServerProfileV10', 'name': 'Enclosure3_FC_Potash_legacy_Bay10', 'serverHardwareUri': None,
                            "serverHardwareTypeUri": 'SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA',
                            'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                            'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                            'boot': {'manageBoot': True, 'order': ['HardDisk']},
                            "connectionSettings": {
                                'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                 'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                 'boot': {'priority': 'Primary'}
                                                 },
                                                {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                 'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                 'boot': {'priority': 'Secondary'}}
                                                ]},
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

serverprofile_name = "Enclosure3_FC_Potash_legacy_Bay10"

profile_data_to_transform = [{'type': 'ServerProfileV10', 'name': 'Enclosure1_FCoE_Potash_Legacy_Bay3', 'serverHardwareUri': 'Enclosure1, bay 3',
                              "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
                              'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                              'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                              'boot': {'manageBoot': True, 'order': ['HardDisk']},
                              "connectionSettings": {
                                  'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                   'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                   'boot': {'priority': 'Primary'}},
                                                  {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                   'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                   'boot': {'priority': 'Secondary'}},
                                                  {'id': 3, 'name': 'fcoe1', 'functionType': 'FibreChannel',
                                                   'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                                   'networkUri': 'FCOE:fcoe_3801_1',
                                                   'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                  {"id": 4, "name": "fcoe2", "functionType": "FibreChannel",
                                                   "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                                   "networkUri": "FCOE:fcoe_3802_1",
                                                   "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                              "firmware": {
                                  "firmwareInstallType": None,
                                  "forceInstallFirmware": False,
                                  "manageFirmware": False,
                              },
                              'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                             'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41z_bay3_volume',
                                                                    'lunType': 'Auto', "bootVolumePriority": "Primary",
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                     {'isEnabled': True, 'connectionId': 4}]},
                                                                   {"id": 2,
                                                                    "volumeUri": "SVOL:encl_41z_bay3_nonboot_volume",
                                                                    "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                                    "lunType": "Auto",
                                                                    "storagePaths": [{
                                                                        "isEnabled": True,
                                                                        "connectionId": 3,
                                                                        'targetSelector': 'Auto'
                                                                    }, {
                                                                        "isEnabled": True,
                                                                        "connectionId": 4,
                                                                        'targetSelector': 'Auto'
                                                                    }
                                                                    ],
                                                                    },
                                                                   {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                                    'lunType': 'Auto',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                     {'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                                    'lunType': 'Auto',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                     {'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                                    'lunType': 'Auto',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                     {'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                   {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',

                                                                    'lunType': 'Auto', 'lun': '',
                                                                    'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                     {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                                   ]},
                              'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                                  {'id': 'AdminPhone',
                                                                                   'value': '123-123-4321'}]},
                              'localStorage': {}}

                             ]
transformed_profile_data = [{'type': 'ServerProfileV10', 'name': 'Enclosure1_FCoE_Potash_Legacy_Bay3_copy', 'serverHardwareUri': 'Enclosure1, bay 2',
                             "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
                             'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                             'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                             'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                             "connectionSettings": {
                                 'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                  'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                  'boot': {'priority': 'Primary'}},
                                                 {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                                  'boot': {'priority': 'Secondary'}},
                                                 {'id': 3, 'name': 'fcoe1', 'functionType': 'FibreChannel',
                                                  'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                                  'networkUri': 'FCOE:fcoe_3801_1',
                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                 {"id": 4, "name": "fcoe2", "functionType": "FibreChannel",
                                                  "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                                  "networkUri": "FCOE:fcoe_3802_1",
                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                             'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41z_bay3_volume',
                                                                   'lunType': 'Auto', "bootVolumePriority": "Primary",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                    {'isEnabled': True, 'connectionId': 4}]},
                                                                  {"id": 2,
                                                                   "volumeUri": "SVOL:encl_41z_bay3_nonboot_volume",
                                                                   "volumeStorageSystemUri": "SYS:RIST-R1-3PAR",

                                                                   "lunType": "Auto",
                                                                   "storagePaths": [{
                                                                       "isEnabled": True,
                                                                       "connectionId": 3,
                                                                       'targetSelector': 'Auto'
                                                                   }, {
                                                                       "isEnabled": True,
                                                                       "connectionId": 4,
                                                                       'targetSelector': 'Auto'
                                                                   }
                                                                   ],
                                                                   },
                                                                  {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                    {'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                    {'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                                    {'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                                  {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',

                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                                    {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                                  ]},
                             'localStorage': {}}

                            ]
copy_profile_data = [{'type': 'ServerProfileV10', 'name': 'Enclosure1_FCoE_Potash_Legacy_Bay3_copy', 'serverHardwareUri': 'SH:Enclosure1, bay 2',
                      "serverHardwareTypeUri": "SHT:SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA",
                      'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical',
                      'bootMode': {'manageMode': True, 'mode': 'BIOS', 'pxeBootPolicy': None},
                      'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                      "connectionSettings": {
                          'connections': [{'id': 1, 'name': 'eth1_1151', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                           'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                           'boot': {'priority': 'Primary'}},
                                          {'id': 2, 'name': 'eth2_1151', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                           'networkUri': 'NS:nswithmgmtuntagged1_1', 'functionType': 'Ethernet',
                                           'boot': {'priority': 'Secondary'}},
                                          {'id': 3, 'name': 'fcoe1', 'functionType': 'FibreChannel',
                                           'portId': 'Mezz 3:1-b', 'requestedMbps': '2000',
                                           'networkUri': 'FCOE:fcoe_3801_1',
                                           'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                          {"id": 4, "name": "fcoe2", "functionType": "FibreChannel",
                                           "portId": 'Mezz 3:2-b', "requestedMbps": "2000",
                                           "networkUri": "FCOE:fcoe_3802_1",
                                           "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                      'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                     'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:DND_encl_41z_bay2_volume',
                                                            'lunType': 'Auto', "bootVolumePriority": "Primary",
                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                             {'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 3, 'volumeUri': 'SVOL:encl_423_share_volume',
                                                            'lunType': 'Auto',
                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                             {'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 5, 'volumeUri': 'SVOL:encl_41y_share_volume',
                                                            'lunType': 'Auto',
                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                             {'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 6, 'volumeUri': 'SVOL:encl_41z_share_volume',
                                                            'lunType': 'Auto',
                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                             {'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 7, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_1',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 8, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_2',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 9, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_3',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 10, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_4',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 11, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_5',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 12, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_6',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 13, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_7',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 14, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_8',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 15, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_9',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 16, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_10',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 17, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_11',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 18, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_12',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 19, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_13',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 20, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_14',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]},
                                                           {'id': 21, 'volumeUri': 'SVOL:sat3_potash_fcoe_cluster_shared_volume_15',

                                                            'lunType': 'Auto',
                                                            'storagePaths': [{"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 3},
                                                                             {"targetSelector": "Auto", 'isEnabled': True, 'connectionId': 4}]}
                                                           ]},
                      'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'SAT-Synergy-Tester'},
                                                                          {'id': 'AdminPhone',
                                                                           'value': '123-123-4321'}]},
                      'localStorage': {}},

                     ]

# LI Firmware Update For Synergy
logical_interconnect_natasha_pa = [{"name": 'LE-LIG_SAS-3', "type": "logical-interconnectV4", "command": "Update", "fwActivationMode": "Parallel",
                                    "validationType": None}]

logical_interconnect_natasha_pp = [{"name": 'LE-LIG_SAS-3', "type": "logical-interconnectV4",
                                    "command": "Update", "fwActivationMode": "Orchestrated"}]

logical_interconnect_carbon_pa = [{"name": 'LE-LIG_Carbon-2', "type": "logical-interconnectV4", "command": "Update", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5",
                                   "fcActivationType": "Parallel", "validationType": "None", "force": "true"}]

logical_interconnect_carbon_pp = [{"name": 'LE-LIG_Carbon-2', "type": "logical-interconnectV4", "command": "Update", "ethernetActivationDelay": "5", "ethernetActivationType": "PairProtect", "fcActivationDelay": "5",
                                   "fcActivationType": "PairProtect", "validationType": "ValidateBestEffort", "force": "true"}]

logical_interconnect_potash_pa = [{"name": 'LE-LIG_Potash', "type": "logical-interconnectV4", "command": "Update", "ethernetActivationDelay": "5", "ethernetActivationType": "Parallel", "fcActivationDelay": "5",
                                   "fcActivationType": "Parallel", "validationType": "None", "force": "true"}]

logical_interconnect_potash_pp = [{"name": 'LE-LIG_Potash', "type": "logical-interconnectV4", "command": "Update", "ethernetActivationDelay": "5", "ethernetActivationType": "PairProtect", "fcActivationDelay": "5",
                                   "fcActivationType": "PairProtect", "validationType": "ValidateBestEffort", "force": "true"}]

binfile_local_path = 'C:/spp'

rhel_os_servers = [{"name": "Enclosure2_FC_Carbon_uefi_Bay1",
                    'serverHardwareUri': 'Enclosure2, bay 1'}]

interconnect_carbon_bay1 = [{'encl_serial': 'MXQ748041Y',
                             'device_type': 'InterconnectBays', 'device_bay': 1, 'name': 'Enclosure2, interconnect 1'}]

interconnect_carbon_bay4 = [{'encl_serial': 'MXQ748041Y',
                             'device_type': 'InterconnectBays', 'device_bay': 4, 'name': 'Enclosure2, interconnect 4'}]

interconnect_potash_bay3 = [{'encl_serial': 'MXQ7480423',
                             'device_type': 'InterconnectBays', 'device_bay': 3, 'name': 'Enclosure3, interconnect 3'}]

interconnect_potash_bay6 = [{'encl_serial': 'MXQ748041Y',
                             'device_type': 'InterconnectBays', 'device_bay': 6, 'name': 'Enclosure2, interconnect 6'}]

windows_os_servers = [{"name": "Enclosure1_FC_Potash_Legacy_Bay8_win2k16",
                       'serverHardwareUri': 'Enclosure1, bay 8'}]

blade_servers = [{'encl_serial': 'Enclosure1', 'device_type': 'BladeBays', 'device_bay': 8, 'name': 'Enclosure1, bay 8'},
                 {'encl_serial': 'Enclosure2', 'device_type': 'BladeBays', 'device_bay': 1, 'name': 'Enclosure2, bay 1'}]

efuse_blade_servers = [{'encl_serial': 'MXQ748041Z', 'device_type': 'BladeBays', 'device_bay': 8, 'name': 'Enclosure1, bay 8'},
                       {'encl_serial': 'MXQ748041Y', 'device_type': 'BladeBays', 'device_bay': 1, 'name': 'Enclosure2, bay 1'}]

blade_hotplug_natasha_bay1 = [{'encl_serial': 'Enclosure1', 'device_type': 'BladeBays',
                               'device_bay': 7, 'serverHardwareUri': 'Enclosure1, bay 7'}]

sp_natasha_bay1 = [{"name": "Enclosure1_BB_logicaldrives_Natsha_legacy_Bay7",
                    'serverHardwareUri': 'Enclosure1, bay 7'}]

efuse_interconnect_natasha_bay1 = [
    {'encl_serial': 'MXQ748041Z', 'device_type': 'InterconnectBays', 'device_bay': 1, 'name': 'Enclosure1, interconnect 1'}]

efuse_interconnect_natasha_bay4 = [
    {'encl_serial': 'MXQ748041Z', 'device_type': 'InterconnectBays', 'device_bay': 4, 'name': 'Enclosure1, interconnect 4'}]

# cleanup data
cleanup_ilo = [{'ilo': '10.151.12.35', 'username': 'Administrator', 'password': 'Cosmos123'},
               {'ilo': '10.151.12.33', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.36', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.37', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.26', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.28', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.15', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.14', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.16', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.6', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.11', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.17', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.9', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.23', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.60', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.40', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.24', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.19', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.18', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               {'ilo': '10.151.12.22', 'username': 'Administrator',
                   'password': 'Cosmos123'},
               ]

cleanup_zone = [{'sanName': 'RIST-R1-SN6600B-SW1'},
                {'sanName': 'RIST-R1-SN6600B-SW2'},
                {'sanName': 'VSAN3801'},
                {'sanName': 'VSAN3802'}
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

# Create volumes
volumes_add = DD.existing_storage_volumes(storage_volumes)
expected_volumes = DD.expected_storage_volumes(storage_volumes)

# Create new volumes
all_new_storage_volumes = list(OrderedDict((frozenset(x.items()), x) for x in new_storage_volumes + potash_iscsi_shared_volumes +
                                           potash_fcoe_shared_volumes + potash_fc_shared_volumes + carbon_fc_shared_volumes).values())
new_volumes_add = DD.storage_volumes(all_new_storage_volumes)
expected_newvolumes = DD.expected_storage_volumes(new_storage_volumes)

exec_volumes_add = DD.storage_volumes(new_storage_volumes_post)
exec_expected_volumes = DD.expected_storage_volumes(new_storage_volumes_post)

# Server Profile Template
server_profile_templates_data = copy.deepcopy(server_profile_templates)
expected_server_profile_templates = DD.make_expected_server_profile_template_data(
    server_profile_templates, firmware)

volume_templates_post_upgrade = DD.make_storage_volume_templates_data(
    storage_volume_templates_post)
expected_volume_templates_post_upgrade = DD.make_expected_storage_volume_template_data(
    storage_volume_templates_post)

# Server Profile Template
spts_edit = copy.deepcopy(spt_edit_data)
expected_spts_edit = DD.make_expected_server_profile_template_data(
    spt_edit_data, firmware)

# Server Profile data
server_profiles = copy.deepcopy(server_profile_data)
expected_server_profiles = DD.make_expected_server_profile_data(
    server_profile_data, updated_spp_name, firmware)

# Server Profile data Post Upgrade
server_profiles_postupgrade = copy.deepcopy(server_profile_data_postupgrade)
expected_server_profiles_postupgrade = DD.make_expected_server_profile_data(
    server_profile_data_postupgrade, updated_spp_name, firmware)

# Scopes
expected_scopes = DD.get_expected_scope_data(scopes)
adgroup_withscope = DD.make_ad_group_data(adgroup_scope)

expected_scopes_post = DD.get_expected_scope_data(scopes_postupgrade)
adgroup_withscope_post = DD.make_ad_group_data(adgroup_scope_postupgrade)

# Transform and copy server profile
server_profile_to_transform = copy.deepcopy(profile_data_to_transform)
transformed_profile = copy.deepcopy(transformed_profile_data)
server_profile_to_copy = copy.deepcopy(copy_profile_data)
