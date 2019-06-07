
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

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
         {'name': 'dpWith3Nic_Nic1StaticAndDhcpNic2StaticNic3Dhcp'}]

networks = {'iscsi': 'i3s_deploy_nw',
            'mgmt': 'mgmt_nw',
            'p_nw1': 'private_nw1',
            'p_nw2': 'private_nw2',
            'p_nw3': 'private_nw3',
            'p_nw4': 'private_nw4',
            'p_nw5': 'private_nw5',
            'p_nw6': 'private_nw6'
            }
egs = [{'enclosureGroupUri': 'EG-3enc'}]

servers = [{'serverHardwareUri': 'SGH737XX1T, bay 1', 'serverHardwareTypeUri': 'SY 480 Gen9 1'}]

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
