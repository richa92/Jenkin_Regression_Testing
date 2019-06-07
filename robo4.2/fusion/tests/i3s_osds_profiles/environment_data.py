
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

server_admin = {'userName': 'server', 'password': 'admin123'}

spp_local_path = {'file_path': 'C:/Users/komerao/Downloads/bp-2018-01-29-02.iso'}

FirmwareVersion = '2018.01.29.02'

goldenimage = [{'name': 'GoldenImage_e2e', 'description': 'valid_goldenimage', 'file': 'valid_file'},
               {'name': 'GoldenImage_e2e_1', 'description': 'valid_goldenimage', 'file': 'valid_file'}]

artifactbundle_add = {'name': 'c:/Goldenimage/HPE-ESXi-2018-03-02-v3.1.zip'}

artifactbundle_extract = {'name': 'HPE-ESXi-2018-03-02-v3.1'}

osdps = [{'name': 'dpWith1Nic_StaticNic'},
         {'name': 'dpWith1Nic_DhcpNic'},
         {'name': 'dp1With1Nic_StaticAndDhcpNic'},
         {'name': 'dpWith1Nic_DisabledNWConfig'},
         {'name': 'dpWith1Nic_StaticNicAndDisableNWConfig'},
         {'name': 'dp2With1Nic_StaticAndDhcpNic'},
         {'name': 'dpWith2Nic_Nic1StaticAndDhcpNic2Static'},
         {'name': 'dpWith2Nic_Nic1StaticNic2StaticAndDhcp'},
         {'name': 'dpWith2Nic_Nic1StaticNic2DhcpAndDisabledNWConfig'},
         {'name': 'dpWith2Nic_Nic1StaticAndDhcpNic2DisableNWConfig'},
         {'name': 'dpWith2Nic_Nic1StaticAndDhcpNic2Dhcp'},
         {'name': 'dpWith3Nic_Nic1StaticNic2StaticNic3Static'},
         {'name': 'dpWith3Nic_Nic1StaticAndDisableNWConfigNic2DhcpAndDisableNWConfigNic3DisableNWConfig'},
         {'name': 'dpWith3Nic_Nic1StaticDHCPNic2StaticDhcpDisableNWConfigNic3DisableNWConfig'},
         {'name': 'dpWith3Nic_Nic1StaticAndDhcpNic2StaticNic3Dhcp'},
         {'name': 'dpNicTeaming'},
         {'name': 'dpNicTeam_AllowNoNWTeaming'},
         {'name': 'dpNicTeam_NoNWTeamingAndNoNWConn'},
         {'name': 'dpNicTeaming_StaticAndDhcp'},
         {'name': 'dpNicTeaming_1NicDhcp'}]

# ------------------- SE Setup details--------------------
# networks = {'iscsi': 'deploy', 'mgmt': 'deploy'}
# egs = [{'enclosureGroupUri': 'EG'}]
# servers = [{'serverHardwareUri': 'SGH537YCES, bay 1', 'serverHardwareTypeUri': 'SY 660 Gen9 1'},
#            {'serverHardwareUri': 'SGH537YCES, bay 3', 'serverHardwareTypeUri': 'SY 480 Gen9 2'}]

# ------------------- ME Setup details--------------------
networks = {'iscsi': 'iscsi_nw', 'mgmt': 'mgmt_nw'}
egs = [{'enclosureGroupUri': 'EG-3enc'}]

# 1st and 2nd are different server hardware of same SHT from same enclosure
# 3rd server hardware of same SHT from different enclosure in same LE
# Last server hardware is of different SHT in same LE
servers = [{'serverHardwareUri': 'MXQ64306Q3, bay 5', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'MXQ64306Q3, bay 8', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'MXQ64805PH, bay 8', 'serverHardwareTypeUri': 'SY 480 Gen9 1'},
           {'serverHardwareUri': 'MXQ64805PH, bay 5', 'serverHardwareTypeUri': 'SY 660 Gen9 3'}]

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
