
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

osdps = [{'name': 'dpWith1Nic_StaticNic'},
         {'name': 'dpWith1Nic_StaticAndDhcpNic_noPswd'},
         {'name': 'dp1With1Nic_StaticAndDhcpNic'},
         {'name': 'dp2With1Nic_StaticAndDhcpNic'},
         {'name': 'dpWithUserName'}]

networks = {'iscsi': 'i3s_deploy_nw',
            'mgmt': 'mgmt_nw',
            'p_nw1': 'private_nw1'}

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
