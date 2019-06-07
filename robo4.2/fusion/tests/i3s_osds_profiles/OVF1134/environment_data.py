
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

spp_local_path = {"file_path": "Y:/spp/synergy/4.10/bp-2018-05-14-02.iso"}

FirmwareVersion = '2018.05.14.02'

osdps = [{'name': 'dp1With1Nic_StaticAndDhcpNic'},
         {'name': 'dp2With1Nic_StaticAndDhcpNic'}]

networks = {'iscsi': 'i3s_deploy_nw',
            'mgmt': 'mgmt_nw',
            'private_nw': 'private_nw1'}

egs = [{'enclosureGroupUri': 'EG-3enc'}]
le = {'name': 'LE-3enc'}

# 1st and 2nd are different server hardware of same SHT from same enclosure
# 3rd server hardware of same SHT from different enclosure in same LE
# Last server hardware is of different SHT in same LE
servers = [{'serverHardwareUri': 'SGH737XX1T, bay 1', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'SGH737XX1T, bay 6', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'SGH736WS9C, bay 10', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'SGH736WS9C, bay 8', 'serverHardwareTypeUri': 'SY 480 Gen9 3'}]

se_connSettings = {
    'reapplyState': 'NotApplying',
    'connections': [{'id': 1, 'name': 'Deployment Network A',
                     'functionType': 'Ethernet', 'networkUri': 'ETH:' + networks['iscsi'],
                     'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'allocatedVFs': 64,
                     'macType': 'Virtual', 'wwpnType': 'Virtual', 'mac': '', 'requestedMbps': '2500',
                     'allocatedMbps': 2500, 'maximumMbps': 20000,
                     'boot': {'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                              'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                    {'id': 2, 'name': 'Blade_boot_mgmt',
                     'functionType': 'Ethernet', 'networkUri': 'ETH:' + networks['mgmt'],
                     'portId': 'Mezz 3:1-b', 'requestedVFs': 0, 'allocatedVFs': 24, 'macType': 'Virtual',
                     'wwpnType': 'Virtual', 'mac': '', 'requestedMbps': '2500',
                     'allocatedMbps': 2500, 'maximumMbps': 10000,
                     'boot': {'priority': 'NotBootable', 'iscsi': {}}}]}

me_connSettings = {"connections": [
    {"id": 1,
     "name": "Deployment Network A", "functionType": "Ethernet",
     "portId": "Mezz 3:1-a", "requestedMbps": "2500",
     "networkUri": 'ETH:' + networks['iscsi'],
     "mac": None, "wwpn": "",
     "wwnn": "", "requestedVFs": "Auto",
     "ipv4": {"ipAddress": None},
     "boot": {"priority": "Primary",
              "ethernetBootType": "iSCSI",
              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                        "firstBootTargetIp": None, "secondBootTargetIp": "",
                        "secondBootTargetPort": "", "initiatorName": None,
                        "bootTargetName": None, "bootTargetLun": None}}},
    {"id": 2,
     "name": "Deployment Network B", "functionType": "Ethernet",
     "portId": "Mezz 3:2-a", "requestedMbps": "2500",
     "networkUri": 'ETH:' + networks['iscsi'],
     "mac": None, "wwpn": "",
     "wwnn": "", "requestedVFs": "Auto",
     "ipv4": {"ipAddress": None},
     "boot": {"priority": "Secondary",
              "ethernetBootType": "iSCSI",
              "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                        "firstBootTargetIp": None, "secondBootTargetIp": "",
                        "secondBootTargetPort": "", "initiatorName": None,
                        "bootTargetName": None, "bootTargetLun": None}}},
    {"id": 3,
     "name": "", "functionType": "Ethernet",
     "portId": "Auto", "requestedMbps": "2500",
     "networkUri": 'ETH:' + networks['mgmt'],
     "lagName": None, "mac": None,
     "wwpn": None, "wwnn": None,
     "requestedVFs": "0", "ipv4": {},
     "boot": {"priority": "NotBootable", "iscsi": {}}}]}
