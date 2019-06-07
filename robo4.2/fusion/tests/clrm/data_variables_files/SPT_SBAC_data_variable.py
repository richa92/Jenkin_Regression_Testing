# Data variables for FC real hardware
# ServerProfileTemplate_type = 'ServerProfileTemplateV6'
# ServerProfile_type = 'ServerProfileV10'
# FirmwareVersion = '2015.09.0'
# FirmwareVersion2 = '2017.03.27.06'
# Scope1_StoragePool_1 = "SPOOL:orionwpstR0"
# StoragePool1 = "SP:orionwpstR0"
# TemplateUri1 = 'ROOT:orionwpstR0'
# VolumeStorageSystemUri1 = "SSYS:pulsarwpst3par1-srv"
# ServerHardwareType = ['SHT:BL460c Gen8 1', 'SHT:BL460c Gen8 1']
# Enc 2 specific
# ServerHardware = ['pulsarwpst-enc2, bay 2', 'pulsarwpst-enc2, bay 4']
# Scope1_ServerHardware = ['SH:pulsarwpst-enc2, bay 2', 'SH:pulsarwpst-enc2, bay 4']

# Enc 4 specific
# ServerHardware = ['pulsarwpst-enc4, bay 2', 'pulsarwpst-enc4, bay 6']
# Scope1_ServerHardware = ['SH:pulsarwpst-enc4, bay 2', 'SH:pulsarwpst-enc4, bay 6']

# Enc 5 specific
# ServerHardware = ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2']
# Scope1_ServerHardware = ['SH:pulsarwpst-enc5, bay 1', 'SH:pulsarwpst-enc5, bay 2']

# Data variables local real hardware
# TODO

# Data variables for DCS c7000 encl : schematic virtualCenter_1.1
enclgrp = "enclgrp"
ServerProfileTemplate_type = 'ServerProfileTemplateV6'
ServerProfile_type = 'ServerProfileV10'
FirmwareVersion = '2016.04.0'
FirmwareVersion2 = '2017.03.27.06'
Scope1_StoragePool_1 = "SPOOL:cpg-growth-limit-1TiB"
Scope3_StoragePool_1 = Scope1_StoragePool_1
StoragePool1 = "SP:cpg-growth-limit-1TiB"
TemplateUri1 = 'ROOT:cpg-growth-limit-1TiB'
VolumeStorageSystemUri1 = "SSYS:ThreePAR-1"
ServerHardwareType = ['SHT:BL460c Gen8 1', 'SHT:BL660c Gen8 1']
Scope1_ServerHardware = ['SH:Encl1, bay 3', 'SH:Encl1, bay 4']
Scope3_ServerHardware = ['SH:Encl1, bay 4', 'SH:Encl1, bay 5']
ServerHardware = ['Encl1, bay 3', 'Encl1, bay 4', 'Encl1, bay 5']

user_credentials = {"Administrator": {"userName": "Administrator", "password": "admin123", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User1": {"userName": "User1", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User1_NetAdmin": {"userName": "User1_NetAdmin", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User1_SPArch": {"userName": "User1_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User5_SPArch": {"userName": "User5_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User6_InfraAdm": {"userName": "User6_InfraAdm", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User7_SPArch": {"userName": "User7_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User7_SPAdm": {"userName": "User7_SPAdm", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User7_ServAdm": {"userName": "User7_ServAdm", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User8_SPArch": {"userName": "User8_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User9_StorAdm": {"userName": "User9_StorAdm", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User10_SPAdm": {"userName": "User10_SPAdm", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User11_SPArch": {"userName": "User11_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User12_SPArch": {"userName": "User12_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User13_SPArch": {"userName": "User13_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None},
                    "User14_SPArch": {"userName": "User14_SPArch", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None}
                    }

scopes = [{"name": "Scope1",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:icsp", "ETH:corp", "FC:san", "ETH:production", "ETH:tunneled_nw", "ETH:ft_net", Scope1_ServerHardware[0], Scope1_ServerHardware[1],
                                 "ETH:net1", "NS:netset1", "SVOL:svol1", "SVOL:svol2", "SVOL:svol3", "SVOL:svol4", Scope1_StoragePool_1, 'firmware-baselines:Service Pack for ProLiant'],
           "removedResourceUris": []
           },
          {"name": "Scope2",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": [],
           "removedResourceUris": []
           },
          {"name": "Scope3",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:icsp", "ETH:corp", "FC:san", "FC:san_da", "ETH:production", "ETH:untagged_nw", "ETH:ft_net2", Scope3_ServerHardware[0], Scope3_ServerHardware[1],
                                 "ETH:net1", "NS:netset1", "NS:netset2", "SVOL:svol1", "SVOL:svol2", "SVOL:svol5", "SVOL:svol6", Scope3_StoragePool_1, 'firmware-baselines:Service Pack for ProLiant'],
           "removedResourceUris": []
           },
          {"name": "Scope4",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:icsp", "ETH:corp", "FC:san", "FC:san_da", "ETH:production", "ETH:untagged_nw", "ETH:ft_net2", Scope3_ServerHardware[0], Scope3_ServerHardware[1],
                                 "ETH:net1", "NS:netset1", "NS:netset2", "SVOL:svol5", "SVOL:svol6", Scope3_StoragePool_1],
           "removedResourceUris": []
           },
          {"name": "Scope5",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:icsp", "ETH:corp", "FC:san", "FC:san_da", "ETH:production", "ETH:untagged_nw", "ETH:ft_net2", Scope3_ServerHardware[0], Scope3_ServerHardware[1],
                                 "ETH:net1", "NS:netset1", "NS:netset2", "SVOL:svol1", "SVOL:svol2", Scope3_StoragePool_1],
           "removedResourceUris": []
           },
          {"name": "Scope6",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": ["ETH:icsp", "ETH:corp", "FC:san", "FC:san_da", "ETH:untagged_nw", "ETH:ft_net2", Scope3_ServerHardware[1],
                                 "ETH:net1", "SVOL:svol5", "SVOL:svol6", Scope3_StoragePool_1],
           "removedResourceUris": []
           }
          ]

users = [{"type": "UserAndPermissions", "userName": "User1", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User1_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User1_NetAdmin", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Network administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User5_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User7_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User7_SPAdm", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User7_ServAdm", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User8_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User9_StorAdm", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User10_SPAdm", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User11_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User12_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User13_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "User14_SPArch", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]}
         ]

user_scope = {'Administrator': [], "User1": ['Scope1'], "User1_SPArch": ['Scope1'], 'User1_NetAdmin': [], "User5_SPArch": ['Scope1', 'Scope3'], "User6_InfraAdm": ['Scope1', 'Scope3'], "User7_SPArch": ['Scope1', 'Scope2', 'Scope3', 'Scope5'], "User7_SPAdm": ['Scope3'], "User7_ServAdm": ['Scope3'], "User8_SPArch": ['Scope1', 'Scope2', 'Scope3'], "User9_StorAdm": ['Scope2'], "User10_SPAdm": ['Scope1', 'Scope2', 'Scope3', 'Scope4'], "User11_SPArch": ['Scope1', 'Scope4'], "User12_SPArch": ['Scope5'], "User13_SPArch": ['Scope6'], "User14_SPArch": ['Scope5', 'Scope6']}

update_users = [{"type": "UserAndPermissions", "userName": "User1", "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}]},
                {"type": "UserAndPermissions", "userName": "User1_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}]},
                {"type": "UserAndPermissions", "userName": "User5_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Server profile architect", "scopeUri": 'Scope3'}]},
                {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope3'}]},
                {"type": "UserAndPermissions", "userName": "User7_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Server profile architect", "scopeUri": 'Scope3'}, {"roleName": "Server profile architect", "scopeUri": 'Scope5'}, {"roleName": "Server profile architect", "scopeUri": 'Scope2'}]},
                {"type": "UserAndPermissions", "userName": "User7_SPAdm", "permissions": [{"roleName": "Server profile administrator", "scopeUri": 'Scope3'}]},
                {"type": "UserAndPermissions", "userName": "User7_ServAdm", "permissions": [{"roleName": "Server administrator", "scopeUri": 'Scope3'}]},
                {"type": "UserAndPermissions", "userName": "User8_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope3'}, {"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Server profile architect", "scopeUri": 'Scope2'}]},
                {"type": "UserAndPermissions", "userName": "User9_StorAdm", "permissions": [{"roleName": "Storage administrator", "scopeUri": 'Scope2'}]},
                {"type": "UserAndPermissions", "userName": "User10_SPAdm", "permissions": [{"roleName": "Server profile administrator", "scopeUri": 'Scope3'}, {"roleName": "Server profile administrator", "scopeUri": 'Scope2'}, {"roleName": "Server profile administrator", "scopeUri": 'Scope1'}, {"roleName": "Server profile administrator", "scopeUri": 'Scope4'}]},
                {"type": "UserAndPermissions", "userName": "User11_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Server administrator", "scopeUri": 'Scope4'}]},
                {"type": "UserAndPermissions", "userName": "User12_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope5'}]},
                {"type": "UserAndPermissions", "userName": "User13_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope6'}]},
                {"type": "UserAndPermissions", "userName": "User14_SPArch", "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope5'}, {"roleName": "Server administrator", "scopeUri": 'Scope6'}]}]

ServerProfileTemplate_1 = [{'name': 'ServerProfileTemplate_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': False},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }]

ServerProfileTemplate_2 = [{'name': 'ServerProfileTemplate_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]
ServerProfileTemplate_2_SP = [{'name': 'ServerProfileTemplate_2_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                               'connectionSettings': {
                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                   ]},
                               'serverProfileTemplateUri': 'SPT:ServerProfileTemplate_2'
                               }
                              ]
ServerProfileTemplate_3 = [{'name': None, 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

ServerProfileTemplate_4 = [{'name': 'ServerProfileTemplate_4', 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}
                            }
                           ]

ServerProfileTemplate_5 = [{'name': 'ServerProfileTemplate_5', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]
ServerProfileTemplate_7 = [{'name': 'ServerProfileTemplate_7', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

ServerProfileTemplate_8 = [{'name': 'ServerProfileTemplate_8', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                            }
                           ]

ServerProfileTemplate_9 = [{'name': 'ServerProfileTemplate_9', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                            }
                           ]
ServerProfileTemplate_9_update = [{'name': 'ServerProfileTemplate_9', 'new_name': 'ServerProfileTemplate_9_new', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'connectionSettings': {'manageConnections': True,
                                                          'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]
                                                          },
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                                   }]

ServerProfileTemplate_10 = [{'name': 'ServerProfileTemplate_10', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}
                             }
                            ]

ServerProfileTemplate_10_update = [{'name': 'ServerProfileTemplate_10', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[1], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                           ]
                                                           },
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                                    }]

ServerProfileTemplate_11 = [{'name': 'ServerProfileTemplate_11', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]

ServerProfileTemplate_11_update = [{'name': 'ServerProfileTemplate_11', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                           {"id": 6, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:net1'}
                                                                           ]
                                                           },
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                                    }
                                   ]


ServerProfileTemplate_12 = [{'name': 'ServerProfileTemplate_12', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]

ServerProfileTemplate_12_update = [{'name': 'ServerProfileTemplate_12', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                           ]
                                                           },
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                   'volumeAttachments': [{'id': 1,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          'bootVolumePriority': "NotBootable",
                                                                          'lunType': 'Auto',
                                                                          "volumeUri": "v:svol3",
                                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

ServerProfileTemplate_13 = [{'name': 'ServerProfileTemplate_13', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                     'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "san_vol1",
                                                                           "size": 10737418240,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": StoragePool1
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": TemplateUri1
                                                                   },
                                                                   "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                   'bootVolumePriority': "Primary",
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

ServerProfileTemplate_13_update = [{'name': 'ServerProfileTemplate_13', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                            'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                           ]
                                                           },
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                   'volumeAttachments': [{'id': 1,
                                                                          "volume": {
                                                                              "properties": {
                                                                                  "name": "san_vol",
                                                                                  "new_name": "san_vol_new",
                                                                                  "size": 10737418240,
                                                                                  "provisioningType": "Thin",
                                                                                  "isShareable": False,
                                                                                  "storagePool": StoragePool1},
                                                                              "isPermanent": False,
                                                                              "templateUri": TemplateUri1},
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          'bootVolumePriority': "Primary",
                                                                          'lunType': 'Auto',
                                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

ServerProfileTemplate_14 = [{'name': 'ServerProfileTemplate_14', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                     "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:production"}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                   'bootVolumePriority': "NotBootable",
                                                                   'lunType': 'Auto',
                                                                   "volumeUri": "v:svol3",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

ServerProfileTemplate_14_update = [{'name': 'ServerProfileTemplate_14', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}}]

ServerProfileTemplate_15 = [{'name': 'ServerProfileTemplate_15', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]
ServerProfileTemplate_16 = [{'name': 'ServerProfileTemplate_16', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]
ServerProfileTemplate_17 = [{'name': 'ServerProfileTemplate_17', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]
ServerProfileTemplate_18 = [{'name': 'ServerProfileTemplate_18', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]
ServerProfileTemplate_19 = [{'name': 'ServerProfileTemplate_19', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]

ServerProfileTemplate_26 = [{'name': 'ServerProfileTemplate_26', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

ServerProfileTemplate_26_SP = [{'name': 'ServerProfileTemplate_26_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                'connectionSettings': {
                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                    ]},
                                'serverProfileTemplateUri': 'SPT:ServerProfileTemplate_26'
                                }
                               ]

ServerProfileTemplate_21 = [{'name': 'ServerProfileTemplate_21', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

ServerProfileTemplate_21_update = [{'name': 'ServerProfileTemplate_21', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                           ]},
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

SP_Page_1 = [{'name': 'SP_Page_1', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
              'connectionSettings': {
                  'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]}}]

SPT_SP_Page_1 = [{'name': 'SPT_SP_Page_1', 'SP': SP_Page_1}]

SP_Page_12 = [{'name': 'SP_Page_12', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
               'connectionSettings': {
                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]}}]

SPT_SP_Page_12 = [{'name': 'SPT_SP_Page_12', 'SP': SP_Page_12}]

SP_Page_2 = [{'name': 'SP_Page_2', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
              'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]}}]

SPT_SP_Page_2 = [{'name': 'SPT_SP_Page_2', 'SP': SP_Page_2}]

SPT_SP_Page_2_update = [{'name': 'SPT_SP_Page_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[1], 'enclosureGroupUri': 'EG:enclgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'manageConnections': True,
                                                'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]}}]

SP_Page_3 = [{'name': 'SP_Page_3', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
              'connectionSettings': {
                  'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]}}]

SPT_SP_Page_3 = [{'name': 'SPT_SP_Page_3', 'SP': SP_Page_3}]

SPT_SP_Page_3_update = [{'name': 'SPT_SP_Page_3', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'manageConnections': True,
                                                'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn_12", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]}}]

SP_Page_4 = [{'name': 'SP_Page_4', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
              'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                      "networkUri": "ETH:production"},
                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                      "networkUri": "ETH:production"}]},
              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
              'bootMode': None,
              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
              'bios': {'manageBios': False, 'overriddenSettings': []},
              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
              'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
              'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                             'volumeAttachments': []}}]

SPT_SP_Page_4 = [{'name': 'SPT_SP_Page_4', 'SP': SP_Page_4}]

SPT_SP_Page_4_update = [{'name': 'SPT_SP_Page_4', 'type': ServerProfileTemplate_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'manageConnections': True,
                                                'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                 "networkUri": "ETH:production"},
                                                                {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                 "networkUri": "ETH:production"}]},
                         'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                         'bootMode': None,
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'bios': {'manageBios': False, 'overriddenSettings': []},
                         'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                         'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                         'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                        'volumeAttachments': [{'id': 1,
                                                               "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                               'bootVolumePriority': "NotBootable",
                                                               'lunType': 'Auto',
                                                               "volumeUri": "v:svol3",
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

SP_Page_5 = [{'name': 'SP_Page_5', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
              'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
              'bootMode': None,
              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
              'bios': {'manageBios': False, 'overriddenSettings': []},
              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
              'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

SPT_SP_Page_5 = [{'name': 'SPT_SP_Page_5', 'SP': SP_Page_5}]

ServerProfileTemplate_5_SP = [{'name': 'ServerProfileTemplate_5_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                               'connectionSettings': {
                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                               'serverProfileTemplateUri': 'SPT:SPT_SP_Page_5'}]

SP_Page_9 = [{'name': 'SP_Page_9', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
              'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                      "networkUri": "ETH:production"},
                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                      "networkUri": "ETH:production"}]},
              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
              'bootMode': None,
              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
              'bios': {'manageBios': False, 'overriddenSettings': []},
              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
              'localStorage': {'sasLogicalJBODs': [], 'controllers': []}}]

SPT_SP_Page_9 = [{'name': 'SPT_SP_Page_9', 'SP': SP_Page_9}]

SPT_SP_Page_9_update = [{'name': 'SPT_SP_Page_9', 'new_name': 'SPT_SP_Page_9_new', 'type': ServerProfileTemplate_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'manageConnections': True,
                                                'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                 "networkUri": "ETH:production"},
                                                                {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                 "networkUri": "ETH:production"}]},
                         'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                         'bootMode': None,
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'bios': {'manageBios': False, 'overriddenSettings': []},
                         'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                         'localStorage': {'sasLogicalJBODs': [], 'controllers': []}}]

SP_Page_10 = [{'name': 'SP_Page_10', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                       "networkUri": "ETH:production"},
                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                       "networkUri": "ETH:production"}]},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}}]

SPT_SP_Page_10 = [{'name': 'SPT_SP_Page_10', 'SP': SP_Page_10}]

SP_Page_11 = [{'name': 'SP_Page_11', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                       "networkUri": "ETH:production"},
                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                       "networkUri": "ETH:production"}]},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}}]

SPT_SP_Page_11 = [{'name': 'SPT_SP_Page_11', 'SP': SP_Page_11}]

SP_Page_13 = [{'name': 'SP_Page_13', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                       "networkUri": "ETH:production"},
                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                       "networkUri": "ETH:production"}]},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}}]

SPT_SP_Page_13 = [{'name': 'SPT_SP_Page_13', 'SP': SP_Page_13}]

SP_Page_22 = [{'name': 'SP_Page_22', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

SPT_SP_Page_22 = [{'name': 'SPT_SP_Page_22', 'SP': SP_Page_22}]

SP_Page_8 = [{'name': 'SP_Page_8', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
              'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                      "networkUri": "ETH:production"},
                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                      "networkUri": "ETH:production"}]},
              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
              'bootMode': None,
              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
              'bios': {'manageBios': False, 'overriddenSettings': []},
              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
              'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
              'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                             'volumeAttachments': [{'id': 1,
                                                    "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                    'bootVolumePriority': "NotBootable",
                                                    'lunType': 'Auto',
                                                    "volumeUri": "v:svol3",
                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

SPT_SP_Page_8 = [{'name': 'SPT_SP_Page_8', 'SP': SP_Page_8}]

SPT_SP_Page_8_update = [{'name': 'SPT_SP_Page_8', 'type': ServerProfileTemplate_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'manageConnections': True,
                                                'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                 "networkUri": "ETH:production"},
                                                                {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                 "networkUri": "ETH:production"}]},
                         'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                         'bootMode': None,
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'bios': {'manageBios': False, 'overriddenSettings': []},
                         'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                         'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                         'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                        'volumeAttachments': []}}]

UI_ServerProfileTemplate_26 = [{'name': 'UI_ServerProfileTemplate_26', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

UI_ServerProfileTemplate_26_update = [{'name': 'UI_ServerProfileTemplate_26', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'manageConnections': True,
                                                              'connections': [{"id": 1, "name": "ftnet_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:ft_net'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                              {"id": 4, "name": "conn_tunnel", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"},
                                                                              {"id": 5, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"}]},
                                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                       'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1,
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "NotBootable",
                                                                             'lunType': 'Auto',
                                                                             "volumeUri": "v:svol3",
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                            {'id': 2,
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "NotBootable",
                                                                             'lunType': 'Auto',
                                                                             "volumeUri": "v:svol4",
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_26_SP = [{'name': 'UI_ServerProfileTemplate_26_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {
                                       'connections': [{"id": 1, "name": "ftnet_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:ft_net'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_tunnel", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"},
                                                       {"id": 5, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"}]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_26',
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                        {'id': 2,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol4",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_46 = [{'name': 'UI_ServerProfileTemplate_46', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_11 = [{'name': 'UI_ServerProfileTemplate_11', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

UI_ServerProfileTemplate_22 = [{'name': 'UI_ServerProfileTemplate_22', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "ftnet_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:ft_net'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_tunnel", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"},
                                                                       {"id": 5, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfile_22 = [{'name': 'UI_ServerProfile_22', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                        'connectionSettings': {
                                'connections': [{"id": 1, "name": "ftnet_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:ft_net'},
                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                {"id": 4, "name": "conn_tunnel", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"},
                                                {"id": 5, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"}]},
                        'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1,
                                                              "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                              'bootVolumePriority': "NotBootable",
                                                              'lunType': 'Auto',
                                                              "volumeUri": "v:svol3",
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_47 = [{'name': 'UI_ServerProfileTemplate_47', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "ftnet_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:ft_net'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_tunnel", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"},
                                                                       {"id": 5, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                     {'id': 2,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol4",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_47_SP = [{'name': 'UI_ServerProfileTemplate_47_SP', "serverHardwareTypeUri": ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {
                                       'connections': [{"id": 1, "name": "ftnet_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:ft_net'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_tunnel", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"},
                                                       {"id": 5, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"}
                                                       ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_47',
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                        {'id': 2,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol4",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_62 = [{'name': 'UI_ServerProfileTemplate_62', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_62_SP = [{'name': 'UI_ServerProfileTemplate_62_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_62',
                                   'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_62_SP_update = [{'name': 'UI_ServerProfileTemplate_62_SP', 'serverHardwareUri': ServerHardware[1], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                                 ]},
                                          'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_62',
                                          'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                       "firmwareActivationType": "Immediate"},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1,
                                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                                'bootVolumePriority': "NotBootable",
                                                                                'lunType': 'Auto',
                                                                                "volumeUri": "v:svol3",
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]


ServerProfileTemplate_27 = [{'name': 'ServerProfileTemplate_27', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                   'bootVolumePriority': "NotBootable",
                                                                   'lunType': 'Auto',
                                                                   "volumeUri": "v:svol3",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

ServerProfileTemplate_27_SP = [{'name': 'ServerProfileTemplate_27_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'serverProfileTemplateUri': 'SPT:ServerProfileTemplate_27',
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}
                                }
                               ]

ServerProfileTemplate_27_update = [{'name': 'ServerProfileTemplate_27', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                           {"id": 6, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"},
                                                                           {"id": 7, "name": "conn_tunneled_nw", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"}
                                                                           ]},
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                   'volumeAttachments': [{'id': 1,
                                                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                          'bootVolumePriority': "NotBootable",
                                                                          'lunType': 'Auto',
                                                                          "volumeUri": "v:svol3",
                                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]


au1 = 'Create a connection to network {"name":"tunneled_nw", "uri":"/rest/ethernet-networks/b0816739-2a63-49eb-963a-559d41019555"} with id 6 on FlexibleLOM (Flb) 1:1-d.'
au2 = 'Change network of connection on FlexibleLOM (Flb) 1:2-c to {"name":"net1", "uri":"/rest/ethernet-networks/abad3e25-549c-4d9a-9394-cc528c6cc866"}.'
profile_compliance_SP_27 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au1, au2],
        "manualUpdates": []}
}

REST_API_SPT_SP_Page_17 = [{'name': 'REST_API_SPT_SP_Page_17_SPT', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                            'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                           'volumeAttachments': [{'id': 1,
                                                                  "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                  'bootVolumePriority': "NotBootable",
                                                                  'lunType': 'Auto',
                                                                  "volumeUri": "v:svol3",
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

REST_API_SPT_SP_Page_17_SP = [{'name': 'REST_API_SPT_SP_Page_17_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                               'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                               'serverProfileTemplateUri': 'SPT:REST_API_SPT_SP_Page_17_SPT',
                               'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                              'volumeAttachments': [{'id': 1,
                                                                     "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                     'bootVolumePriority': "NotBootable",
                                                                     'lunType': 'Auto',
                                                                     "volumeUri": "v:svol3",
                                                                     'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

REST_API_SPT_SP_Page_17_update = [{'name': 'REST_API_SPT_SP_Page_17_SPT', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'connectionSettings': {'manageConnections': True,
                                                          'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "conn_tunneled_nw", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 6, "name": "conn_net1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"},
                                                                          ]},
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]


au17_1 = 'Create a connection to network {"name":"tunneled_nw", "uri":"/rest/ethernet-networks/b0816739-2a63-49eb-963a-559d41019555"} with id 6 on FlexibleLOM (Flb) 1:1-d.'
au17_2 = 'Change network of connection on FlexibleLOM (Flb) 1:2-c to {"name":"net1", "uri":"/rest/ethernet-networks/abad3e25-549c-4d9a-9394-cc528c6cc866"}.'
profile_compliance_SP_17 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au17_1, au17_2],
        "manualUpdates": []}
}


UI_ServerProfileTemplate_66 = [{'name': 'UI_ServerProfileTemplate_66', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_66_SP = [{'name': 'UI_ServerProfileTemplate_66_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_66',
                                   'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_66_update = [{'name': 'UI_ServerProfileTemplate_66', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'manageConnections': True,
                                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                              ]},
                                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                    "firmwareActivationType": "Immediate"},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                       'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1,
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "NotBootable",
                                                                             'lunType': 'Auto',
                                                                             "volumeUri": "v:svol3",
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                            {'id': 2,
                                                                             "volume": {
                                                                                 "properties": {
                                                                                     "name": "priv_vol",
                                                                                     "size": 11811160064,
                                                                                     "provisioningType": "Thin",
                                                                                     "isShareable": False,
                                                                                     "storagePool": StoragePool1},
                                                                                 "isPermanent": False,
                                                                                 "templateUri": TemplateUri1},
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "Primary",
                                                                             'lunType': 'Auto',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_66_SP_update = [{'name': 'UI_ServerProfileTemplate_66_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                                 ]},
                                          'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_66',
                                          'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                       "firmwareActivationType": "Immediate"},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1,
                                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                                'bootVolumePriority': "NotBootable",
                                                                                'lunType': 'Auto',
                                                                                "volumeUri": "v:svol3",
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                               {'id': 2,
                                                                                "volume": {
                                                                                    "properties": {
                                                                                        "name": "priv_vol",
                                                                                        "size": 11811160064,
                                                                                        "provisioningType": "Thin",
                                                                                        "isShareable": False,
                                                                                        "storagePool": StoragePool1},
                                                                                    "isPermanent": False,
                                                                                    "templateUri": TemplateUri1},
                                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                                'bootVolumePriority': "Primary",
                                                                                'lunType': 'Auto',
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                                }]}}]

au66_1 = 'Change boot for connection on FlexibleLOM (Flb) 1:1-b to FC primary.'
au66_2 = 'Change boot source of connection on FlexibleLOM (Flb) 1:1-b to Managed volume.'
au66_3 = 'Create volume "priv_vol".'
profile_compliance_SP_66 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au66_1, au66_2, au66_2, au66_3],
        "manualUpdates": []}
}

UI_ServerProfileTemplate_56 = [{'name': 'UI_ServerProfileTemplate_56', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': "", 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_56_SP = [{'name': 'UI_ServerProfileTemplate_56_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_56',
                                   'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]


UI_ServerProfileTemplate_56_SP_update = [{'name': 'UI_ServerProfileTemplate_56_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                                 ]},
                                          'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_56',
                                          'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                       "firmwareActivationType": "Immediate"},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1,
                                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                                'bootVolumePriority': "NotBootable",
                                                                                'lunType': 'Auto',
                                                                                "volumeUri": "v:svol3",
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}
                                                                               ]}}]

UI_ServerProfileTemplate_25 = [{'name': 'UI_ServerProfileTemplate_25_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': "", 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False,
                                               'volumeAttachments': []}},
                               {'name': 'UI_ServerProfileTemplate_25_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[1], 'enclosureGroupUri': 'EG:enclgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_net_1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': "", 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False,
                                               'volumeAttachments': []}}]

UI_ServerProfileTemplate_25_SP = [{'name': 'UI_ServerProfileTemplate_25_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_25_1',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': "", 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_25_SP_update = [{'name': 'UI_ServerProfileTemplate_25_SP', 'enclosureGroupUri': 'EG:enclgrp1', "type": ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[1],
                                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                 {"id": 4, "name": "conn_net_1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                                 ]},
                                          'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_25_2',
                                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': "", 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                       "firmwareActivationType": "Immediate"},
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1,
                                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                                'bootVolumePriority': "NotBootable",
                                                                                'lunType': 'Auto',
                                                                                "volumeUri": "v:svol3",
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

profile_compliance_SP_25 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": None,
        "manualUpdates": None}
}

UI_ServerProfileTemplate_40 = [{'name': 'UI_ServerProfileTemplate_40', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                        'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': "", 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                     {'id': 2,
                                                                      "volume": {
                                                                          "properties": {
                                                                              "name": "priv_vol",
                                                                              "size": 11811160064,
                                                                              "provisioningType": "Thin",
                                                                              "isShareable": False,
                                                                              "storagePool": StoragePool1},
                                                                          "isPermanent": False,
                                                                          "templateUri": TemplateUri1},
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "Primary",
                                                                      'lunType': 'Auto',
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                      }]}}]

UI_ServerProfileTemplate_40_SP = [{'name': 'UI_ServerProfileTemplate_40_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                           'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_40',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': "", 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                        {'id': 2,
                                                                         "volume": {
                                                                             "properties": {
                                                                                 "name": "priv_vol",
                                                                                 "size": 11811160064,
                                                                                 "provisioningType": "Thin",
                                                                                 "isShareable": False,
                                                                                 "storagePool": StoragePool1},
                                                                             "isPermanent": False,
                                                                             "templateUri": TemplateUri1},
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "Primary",
                                                                         'lunType': 'Auto',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                         }]}}]

UI_ServerProfileTemplate_40_update = [{'name': 'UI_ServerProfileTemplate_40', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'manageConnections': True,
                                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2400", "networkUri": "ETH:production"}
                                                                              ]},
                                       'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'Floppy', 'HardDisk', 'PXE']},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                    "firmwareActivationType": "Immediate"},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': [{
                                                        "logicalDrives": [{
                                                            "name": "HPSUT-Volume",
                                                            "raidLevel": "RAID1",
                                                            "bootable": False,
                                                            "numPhysicalDrives": 2}],
                                                        "deviceSlot": "Embedded",
                                                        "mode": "RAID",
                                                        "initialize": True
                                                        }]},
                                       'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1,
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "NotBootable",
                                                                             'lunType': 'Auto',
                                                                             "volumeUri": "v:svol3",
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]
au40_1 = "Change boot order to [CD, USB, Floppy, HardDisk, PXE]."
au40_2 = "Delete the connection with id 5 on FlexibleLOM (Flb) 1:2-c.', u'Change boot for connection on FlexibleLOM (Flb) 1:1-b to not bootable."
mu40_1 = "Modify local storage settings to match with the server profile template."
profile_compliance_SP_40 = {
    "name": "",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [au40_1, au40_2],
        "manualUpdates": [mu40_1]}
}

UI_ServerProfileTemplate_70_1 = [{'name': 'UI_ServerProfileTemplate_70_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                         ]
                                                         },
                                  'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                  'bootMode': None,
                                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                  'bios': {'manageBios': False, 'overriddenSettings': []},
                                  'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                  'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                 'volumeAttachments': []}}]


UI_ServerProfileTemplate_70_1_SP = [{'name': 'UI_ServerProfileTemplate_70_1_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                     'serverHardwareUri': ServerHardware[0],
                                     'connectionSettings': {
                                         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                         ]},
                                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                     'bootMode': None,
                                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                     'bios': {'manageBios': False, 'overriddenSettings': []},
                                     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                     'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                    'volumeAttachments': []}}]

UI_ServerProfileTemplate_70_1_SP_update = [{'name': 'UI_ServerProfileTemplate_70_1_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                            'serverHardwareUri': ServerHardware[0],
                                            'connectionSettings': {
                                                'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                ]},
                                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                            'bootMode': None,
                                            'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_70_1',
                                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                            'bios': {'manageBios': False, 'overriddenSettings': []},
                                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                            'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                           'volumeAttachments': []}}]

# Below is for reference. Don't delete
# with OV version 4.00
# UI_ServerProfileTemplate_70_1_SP_compliance = {"name": "UI_ServerProfileTemplate_70_1_SP", "compliance-preview": {
#     "type": "ServerProfileCompliancePreviewV1",
#     "isOnlineUpdate": None,
#     "manualUpdates": None,
#     "automaticUpdates": None,
# }}

# with OV version 4.10
UI_ServerProfileTemplate_70_1_SP_compliance = {"name": "UI_ServerProfileTemplate_70_1_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": [],
}}

UI_ServerProfileTemplate_70_2 = [{'name': 'UI_ServerProfileTemplate_70_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                         ]
                                                         },
                                  'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                  'bootMode': None,
                                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                  'bios': {'manageBios': False, 'overriddenSettings': []},
                                  'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                  'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                 'volumeAttachments': []}}]


UI_ServerProfileTemplate_70_2_SP = [{'name': 'UI_ServerProfileTemplate_70_2_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                     'serverHardwareUri': ServerHardware[1],
                                     'connectionSettings': {
                                         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                         ]},
                                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                     'bootMode': None,
                                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                     'bios': {'manageBios': False, 'overriddenSettings': []},
                                     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                     'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                    'volumeAttachments': []}}]

UI_ServerProfileTemplate_70_2_SP_update = [{'name': 'UI_ServerProfileTemplate_70_2_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                            'serverHardwareUri': ServerHardware[1],
                                            'connectionSettings': {
                                                'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                ]},
                                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                            'bootMode': None,
                                            'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_70_2',
                                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                            'bios': {'manageBios': False, 'overriddenSettings': []},
                                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                            'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                           'volumeAttachments': []}}]


# Below is for reference. Don't delete
# with OV version 4.10, 4.00
UI_ServerProfileTemplate_70_2_SP_compliance = {"name": "UI_ServerProfileTemplate_70_2_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": [],
}}

UI_ServerProfileTemplate_34_1 = [{'name': 'UI_ServerProfileTemplate_34', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                         ]
                                                         },
                                  'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                  'bootMode': None,
                                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                  'bios': {'manageBios': False, 'overriddenSettings': []},
                                  'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                  'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                 'volumeAttachments': []}}]


UI_ServerProfileTemplate_34_1_SP = [{'name': 'UI_ServerProfileTemplate_34_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                     'serverHardwareUri': ServerHardware[0],
                                     'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
    'bootMode': None,
    'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_34',
    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
    'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': []}}]

UI_ServerProfileTemplate_34_1_SPT_update = [{'name': 'UI_ServerProfileTemplate_34', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                             'connectionSettings': {'manageConnections': True,
                                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                                    ]
                                                                    },
                                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                             'bootMode': None,
                                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                             'bios': {'manageBios': False, 'overriddenSettings': []},
                                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                            'volumeAttachments': [
                                                                {'id': 1,
                                                                 "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                 'bootVolumePriority': "NotBootable",
                                                                 'lunType': 'Auto',
                                                                 "volumeUri": "v:svol1",
                                                                 'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}
                                                            ]}}]

UI_ServerProfileTemplate_34_SP_compliance = {"name": "UI_ServerProfileTemplate_34_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*",
                         "REGEX:Create an attachment to volume \{\"name\":\".*\", \"uri\":\"\/rest\/storage-volumes\/.*\"}\.",
                         ]
}}

UI_ServerProfileTemplate_34_1_SP_update = [{'name': 'UI_ServerProfileTemplate_34_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay', 'serverHardwareUri': ServerHardware[0],
                                            'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
    'bootMode': None,
    'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_34',
    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
    'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': [
                       {'id': 1,
                        "associatedTemplateAttachmentId": 'SPTVAID:1',
                        "volumeStorageSystemUri": VolumeStorageSystemUri1,
                        "associatedTemplateAttachmentId": 'SPTVAID:1',
                        'bootVolumePriority': "NotBootable",
                        'lunType': 'Auto',
                        "volumeUri": "v:svol1",
                        'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}
                   ]}}]

UI_ServerProfileTemplate_45 = [{'name': 'UI_ServerProfileTemplate_45', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]
                                                       },
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': []}}]


UI_ServerProfileTemplate_45_SP = [
    {'name': 'UI_ServerProfileTemplate_45_SP1', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
     'serverHardwareUri': ServerHardware[0],
     'connectionSettings': {
         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                         ]},
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
     'bootMode': None,
     'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_45',
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                   'volumeAttachments': []}},
    {'name': 'UI_ServerProfileTemplate_45_SP2', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
     'serverHardwareUri': ServerHardware[1],
     'connectionSettings': {
         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                         ]},
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
     'bootMode': None,
     'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_45',
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                   'volumeAttachments': []}}]

UI_ServerProfileTemplate_45_SPT_update = [{'name': 'UI_ServerProfileTemplate_45', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                                  ]
                                                                  },
                                           'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                           'bootMode': None,
                                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                           'bios': {'manageBios': False, 'overriddenSettings': []},
                                           'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                           'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                          'volumeAttachments': []}}]

UI_ServerProfileTemplate_45_SP_update = [{'name': 'UI_ServerProfileTemplate_45_SP1', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                          'serverHardwareUri': ServerHardware[0],
                                          'connectionSettings': {
                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                              ]},
                                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                          'bootMode': None,
                                          'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_45',
                                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                         'volumeAttachments': []}}]

# Below is for reference. Don't delete
# with OV version 4.00
# UI_ServerProfileTemplate_45_SP1_compliance = {"name": "UI_ServerProfileTemplate_45_SP1", "compliance-preview": {
#     "type": "ServerProfileCompliancePreviewV1",
#     "isOnlineUpdate": None,
#     "manualUpdates": None,
#     "automaticUpdates": None,
# }}

# with OV version 4.10
UI_ServerProfileTemplate_45_SP1_compliance = {"name": "UI_ServerProfileTemplate_45_SP1", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": [],
}}

UI_ServerProfileTemplate_45_SP2_compliance = {"name": "UI_ServerProfileTemplate_45_SP2", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*",
                         ]
}}

UI_ServerProfileTemplate_57 = [{'name': 'UI_ServerProfileTemplate_57', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_netset", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "NS:netset1"},
                                                                       {"id": 5, "name": "conn_net", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"},
                                                                       {"id": 6, "name": "tunnel_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"}
                                                                       ]
                                                       },
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [
                                               ]}}]

# Override SPT settings for boot, BIOS settings , Advanced settings : hideUnusedFlexNics : while creating SP from SPT
UI_ServerProfileTemplate_57_SP = [{'name': 'UI_ServerProfileTemplate_57_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'serverHardwareUri': ServerHardware[0],
                                   'connectionSettings': {
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "NS:netset1"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"},
                                                       {"id": 6, "name": "tunnel_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"}
                                                       ]},
                                   'boot': {'manageBoot': True, 'order': ['Floppy', 'CD', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_57',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': True, 'overriddenSettings': [{'id': '64', 'value': '1'}]},
                                   'hideUnusedFlexNics': False, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [
                                                  ]}}]

UI_ServerProfileTemplate_57_SP_compliance = {"name": "UI_ServerProfileTemplate_57_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change boot order to \[CD, Floppy, USB, HardDisk, PXE\]\.",
                         "REGEX:Change hide unused FlexNICs to Yes\.",
                         ]
}}

UI_ServerProfileTemplate_69 = [{'name': 'UI_ServerProfileTemplate_69', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]
                                                       },
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': []}}]


UI_ServerProfileTemplate_69_SP = [{'name': 'UI_ServerProfileTemplate_69_SP1', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'serverHardwareUri': ServerHardware[0],
                                   'connectionSettings': {
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_69',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': []}},
                                  {'name': 'UI_ServerProfileTemplate_69_SP2', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'serverHardwareUri': ServerHardware[1],
                                   'connectionSettings': {
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_69',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': []}}]

UI_ServerProfileTemplate_69_SPT_update = [{'name': 'UI_ServerProfileTemplate_69', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                  {"id": 6, "name": "tunnel_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"}
                                                                                  ]
                                                                  },
                                           'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                           'bootMode': None,
                                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                           'bios': {'manageBios': False, 'overriddenSettings': []},
                                           'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                           'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                          'volumeAttachments': []}}]


UI_ServerProfileTemplate_69_SP1_compliance = {"name": "UI_ServerProfileTemplate_69_SP1", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Create a connection to network \{\"name\":\".*\", \"uri\":\"\/rest\/ethernet-networks\/.*\"\} with id .*\.",
                         "REGEX:Change requested bandwidth of connection .*b\/s\.",
                         ]
}}

UI_ServerProfileTemplate_69_SP2_compliance = {"name": "UI_ServerProfileTemplate_69_SP2", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Create a connection to network \{\"name\":\".*\", \"uri\":\"\/rest\/ethernet-networks\/.*\"\} with id .*\.",
                         "REGEX:Change requested bandwidth of connection .*b\/s\.",
                         ]
}}

UI_ServerProfileTemplate_43 = [{'name': 'UI_ServerProfileTemplate_43', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_43_SP = [{'name': 'UI_ServerProfileTemplate_43_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_43',
                                   'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

uplink_sets = {'uplink1': {'name': 'upl_corp',
                           'ethernetNetworkType': 'Untagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['corp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]},
               'uplink3': {'name': 'upl_san',
                           'networkType': 'FibreChannel',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkUris': ['san'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'X3', 'speed': 'Auto'}]}}

ligs = {'name': 'lig',
        'type': 'logical-interconnect-groupV500',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'enclosure': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                    {'enclosure': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}],
        'uplinkSets': [uplink_sets['uplink1'].copy(), uplink_sets['uplink3'].copy()],
        'internalNetworkUris': ['ft_net', 'corp1', 'net1', 'untagged_nw', 'tunneled_nw']
        }

update_lig = {'lig': [ligs], 'li': [{'name': 'Encl1-lig'}, {'name': 'Encl2-lig'}], 'networks': ['icsp', 'production']}

ethernet_networks_revert = [{'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '100', 'purpose': 'General'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '70', 'purpose': 'General'}]

uplink_sets_revert = {'uplink1': {'name': 'upl_corp',
                                  'ethernetNetworkType': 'Untagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['corp'],
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]},
                      'uplink2': {'name': 'upl_icsp',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['icsp'],
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'}]},
                      'uplink3': {'name': 'upl_san',
                                  'networkType': 'FibreChannel',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkUris': ['san'],
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'lacpTimer': 'Long',
                                  'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'X3', 'speed': 'Auto'}]}}

ligs_revert = {'name': 'lig',
               'type': 'logical-interconnect-groupV500',
               'enclosureType': 'C7000',
               'interconnectMapTemplate': [{'enclosure': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                           {'enclosure': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}],
               'uplinkSets': [uplink_sets_revert['uplink1'].copy(), uplink_sets_revert['uplink2'].copy(), uplink_sets_revert['uplink3'].copy()],
               'internalNetworkUris': ['production', 'ft_net', 'corp1', 'net1', 'untagged_nw', 'tunneled_nw', 'ft_net2', 'network2']}

revert_scopes_SPT_43 = [{"name": "Scope3",
                         "description": "",
                         "type": "ScopeV3",
                         "addedResourceUris": ["ETH:icsp", "ETH:production"],
                         "removedResourceUris": []},
                        {"name": "Scope1",
                         "description": "",
                         "type": "ScopeV3",
                         "addedResourceUris": ["ETH:icsp", "ETH:production"],
                         "removedResourceUris": []}]

revert_update_lig = {'lig': [ligs_revert], 'li': [{'name': 'Encl1-lig'}, {'name': 'Encl2-lig'}], 'scopes': revert_scopes_SPT_43}
update_lig_name = {'name': 'lig', 'new_name': 'lig_updated'}
revert_lig_name = {'name': 'lig_updated', 'new_name': 'lig'}
profile_compliance_SP_43 = {
    "name": "UI_ServerProfileTemplate_43_SP",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

SPT_SBAC_1 = [{'name': 'SPT_SBAC_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
               'initialScopeUris': ['Scope:Scope1']
               }]

SPT_SBAC_4_1 = [{'name': 'SPT_SBAC_4_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                 'connectionSettings': {'manageConnections': True,
                                        'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                        {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                        {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                        {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                        {"id": 5, "name": "netset1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "NS:netset1"}
                                                        ]},
                 'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                 'bootMode': None,
                 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                 'bios': {'manageBios': False, 'overriddenSettings': []},
                 'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                 'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                 'initialScopeUris': ['Scope:Scope1']
                 }
                ]
SPT_SBAC_4_2 = [{'name': 'SPT_SBAC_4_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                 'connectionSettings': {'manageConnections': True,
                                        'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                        {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                        {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                        {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                        {"id": 5, "name": "netset2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "NS:netset2"}
                                                        ]},
                 'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                 'bootMode': None,
                 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                 'bios': {'manageBios': False, 'overriddenSettings': []},
                 'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                 'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                 'initialScopeUris': ['Scope:Scope1']
                 }
                ]


SPT_SBAC_32 = [{'name': 'SPT_SBAC_32', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': False},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope1', 'Scope:Scope3']
                }
               ]

SPT_SBAC_32_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_32_UserUpdate2 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_32_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Server profile architect", "scopeUri": 'Scope3'}, {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope3'}, {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_35 = [{'name': 'SPT_SBAC_35', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': False},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope1']
                }
               ]

SPT_SBAC_42 = [{'name': 'SPT_SBAC_42', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope1', 'Scope:Scope3']}]

SPT_SBACC_42_EditScope_1 = [{"name": "Scope3",
                             "description": "",
                             "type": "ScopeV3",
                             "addedResourceUris": [],
                             "removedResourceUris": ["NS:netset2"]}]

SPT_SBAC_42_ScopeResetToOldResources = [{"name": "Scope3",
                                         "description": "",
                                         "type": "ScopeV3",
                                         "addedResourceUris": ["NS:netset2"],
                                         "removedResourceUris": []}]

SPT_SBAC_42_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_42_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Server profile architect", "scopeUri": 'Scope3'}, {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope3'}, {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_43 = [{'name': 'SPT_SBAC_43', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                        'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': [{'id': 1,
                                                      "volume": {
                                                          "properties": {
                                                              "name": "san_vol1",
                                                              "size": 10737418240,
                                                              "provisioningType": "Thin",
                                                              "isShareable": False,
                                                              "storagePool": StoragePool1
                                                          },
                                                          "isPermanent": False,
                                                          "templateUri": TemplateUri1
                                                      },
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      'bootVolumePriority': "Primary",
                                                      'lunType': 'Auto',
                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                     {'id': 2,
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      'bootVolumePriority': "NotBootable",
                                                      'lunType': 'Auto',
                                                      "volumeUri": "v:svol3",
                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]},
                'initialScopeUris': ['Scope:Scope1']}]

SPT_SBAC_43_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User1_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User1", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_43_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User1_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User1", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_44 = [{'name': 'SPT_SBAC_44', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                        'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': [{'id': 1,
                                                      "volume": {
                                                          "properties": {
                                                              "name": "san_vol1",
                                                              "size": 10737418240,
                                                              "provisioningType": "Thin",
                                                              "isShareable": False,
                                                              "storagePool": StoragePool1
                                                          },
                                                          "isPermanent": False,
                                                          "templateUri": TemplateUri1
                                                      },
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      'bootVolumePriority': "Primary",
                                                      'lunType': 'Auto',
                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                     {'id': 2,
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      'bootVolumePriority': "NotBootable",
                                                      'lunType': 'Auto',
                                                      "volumeUri": "v:svol6",
                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]},
                'initialScopeUris': ['Scope:Scope1', 'Scope:Scope3']}]

SPT_SBAC_44_UserUpdate1 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}, {"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_44_UserUpdate2 = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]},
                           {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_44_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User5_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope1'}, {"roleName": "Server profile architect", "scopeUri": 'Scope3'}, {"roleName": "Read only", "scopeUri": None}]},
                                    {"type": "UserAndPermissions", "userName": "User6_InfraAdm", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'Scope1'}, {"roleName": "Infrastructure administrator", "scopeUri": 'Scope3'}, {"roleName": "Read only", "scopeUri": None}]}]
ServerProfileTemplate_SBAC_11 = [{'name': 'ServerProfileTemplate_SBAC_11', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                         ]},
                                  'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                  'bootMode': None,
                                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                  'bios': {'manageBios': False, 'overriddenSettings': []},
                                  'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                                  'initialScopeUris': ['Scope:Scope1', 'Scope:Scope3']
                                  }]

ServerProfileTemplate_SBAC_11_SP = [{'name': 'ServerProfileTemplate_SBAC_11_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                     'connectionSettings': {
                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                    ]},
    'serverProfileTemplateUri': 'SPT:ServerProfileTemplate_SBAC_11', 'initialScopeUris': ['Scope:Scope1', 'Scope:Scope3']}
]
ServerProfileTemplate_SBAC_16 = [{'name': 'ServerProfileTemplate_SBAC_16', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                         ]},
                                  'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                  'bootMode': None,
                                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                  'bios': {'manageBios': False, 'overriddenSettings': []},
                                  'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                                  'initialScopeUris': ['Scope:Scope1', 'Scope:Scope2', 'Scope:Scope3']
                                  }]
ServerProfileTemplate_SBAC_16_SP = [{'name': 'ServerProfileTemplate_SBAC_16_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                     'connectionSettings': {
                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                    ]},
    'serverProfileTemplateUri': 'SPT:ServerProfileTemplate_SBAC_16', 'initialScopeUris': ['Scope:Scope1', 'Scope:Scope2', 'Scope:Scope3']}]
SPT_SBAC_OVD15519 = [{'name': 'SPT_SBAC_OVD15519', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'manageConnections': True,
                                             'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                             {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                             {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                             {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                             {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                             ]},
                      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                      'bootMode': None,
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                      'bios': {'manageBios': False, 'overriddenSettings': []},
                      'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                      'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                     'volumeAttachments': []}}]

SPT_SBACC_OVD15519_EditScope_1 = [{"name": "Scope3",
                                   "description": "",
                                   "type": "ScopeV3",
                                   "addedResourceUris": ["SPT:SPT_SBAC_OVD15519"],
                                   "removedResourceUris": []}]

SPT_SBAC_OVD15519_SP1 = [{'name': 'SPT_SBAC_OVD15519_SP1', 'serverHardwareUri': Scope3_ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                 ]},
                          'serverProfileTemplateUri': 'SPT:SPT_SBAC_OVD15519',
                          'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": None},
                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                         'volumeAttachments': []}}]

SPT_SBAC_OVD15519_SP2 = [{'name': 'SPT_SBAC_OVD15519_SP2', 'serverHardwareUri': Scope3_ServerHardware[1], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                 ]},
                          'serverProfileTemplateUri': 'SPT:SPT_SBAC_OVD15519',
                          'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": None},
                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                         'volumeAttachments': []}}]


SPT_SBAC_13 = [{'name': 'SPT_SBAC_13', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': []}}]

SPT_SBAC_13_SP = [{'name': 'SPT_SBAC_13_SP', 'serverHardwareUri': Scope3_ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                          ]},
                   'serverProfileTemplateUri': 'SPT:SPT_SBAC_13',
                   'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": None},
                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                  'volumeAttachments': []}}]

SPT_SBAC_14 = [{'name': 'SPT_SBAC_14', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope3']}]

SPT_SBAC_14_SP = [{'name': 'SPT_SBAC_14_SP', 'serverHardwareUri': Scope3_ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                          ]},
                   'serverProfileTemplateUri': 'SPT:SPT_SBAC_14',
                   'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": None},
                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                  'volumeAttachments': []},
                   'initialScopeUris': ['Scope:Scope3', 'Scope:Scope1', 'Scope:Scope2']}]

SPT_SBAC_15 = [{'name': 'SPT_SBAC_15', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope3']}]

SPT_SBAC_15_SP = [{'name': 'SPT_SBAC_15_SP', 'serverHardwareUri': Scope3_ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                          ]},
                   'serverProfileTemplateUri': 'SPT:SPT_SBAC_15',
                   'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": None},
                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                  'volumeAttachments': []},
                   'initialScopeUris': ['Scope:Scope3', 'Scope:Scope1']}]

SPT_SBAC_OVD13618 = [{'name': 'SPT_SBAC_OVD13618', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]},
                      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                      'bootMode': None,
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                      'bios': {'manageBios': False, 'overriddenSettings': []},
                      'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                      'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                     'volumeAttachments': []},
                      'initialScopeUris': ['Scope:Scope1', 'Scope:Scope2', 'Scope:Scope3']}]

SPT_SBAC_OVD13618_EditScope_1 = [{"name": "Scope4",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": ["SPT:SPT_SBAC_OVD13618"],
                                  "removedResourceUris": []}]

SPT_SBAC_OVD13618_SP = [{'name': 'SPT_SBAC_OVD13618_SP', 'serverHardwareUri': Scope3_ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                         'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                ]},
                         'serverProfileTemplateUri': 'SPT:SPT_SBAC_OVD13618',
                         'initialScopeUris': ['Scope:Scope1', 'Scope:Scope2', 'Scope:Scope3', 'Scope:Scope4']}]

SPT_SBAC_OVD13618_EditScope_2 = [{"name": "Scope4",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:SPT_SBAC_OVD13618"]},
                                 {"name": "Scope3",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:SPT_SBAC_OVD13618"]},
                                 {"name": "Scope2",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:SPT_SBAC_OVD13618"]},
                                 {"name": "Scope1",
                                  "description": "",
                                  "type": "ScopeV3",
                                  "addedResourceUris": [],
                                  "removedResourceUris": ["SPT:SPT_SBAC_OVD13618"]}]

SPT_SBAC_OVD13618_SP_update = [{'name': 'SPT_SBAC_OVD13618_SP', 'serverHardwareUri': Scope3_ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                'initialScopeUris': ['Scope:Scope1', 'Scope:Scope2', 'Scope:Scope3', 'Scope:Scope4']}]

SPT_SBAC_10 = [{'name': 'SPT_SBAC_10', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]
                                       },
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                                                           'volumeAttachments': [{'id': 1,
                                                                                                                  "volume": {
                                                                                                                      "properties": {
                                                                                                                          "name": "svol1",
                                                                                                                          "size": 11000000000,
                                                                                                                          "provisioningType": "Thin",
                                                                                                                          "isShareable": False,
                                                                                                                          "storagePool": "SP:cpg-growth-limit-1TiB"
                                                                                                                      },
                                                                                                                      "isPermanent": False,
                                                                                                                      "templateUri": 'ROOT:cpg-growth-limit-1TiB'
                                                                                                                  },
                                                                                                                  "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                                                                  'bootVolumePriority': "NotBootable",
                                                                                                                  'lunType': 'Auto',
                                                                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                                                                  },
                                                                                                                 {'id': 2,
                                                                                                                  "volume": {
                                                                                                                      "properties": {
                                                                                                                          "name": "svol2",
                                                                                                                          "size": 11000000000,
                                                                                                                          "provisioningType": "Thin",
                                                                                                                          "isShareable": False,
                                                                                                                          "storagePool": "SP:cpg-growth-limit-1TiB"
                                                                                                                      },
                                                                                                                      "isPermanent": False,
                                                                                                                      "templateUri": 'ROOT:cpg-growth-limit-1TiB'
                                                                                                                  },
                                                                                                                  "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                                                                  'bootVolumePriority': "NotBootable",
                                                                                                                  'lunType': 'Auto',
                                                                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                                                                  },
                                                                                                                 {'id': 3,
                                                                                                                  "volume": {
                                                                                                                      "properties": {
                                                                                                                          "name": "svol5",
                                                                                                                          "size": 11000000000,
                                                                                                                          "provisioningType": "Thin",
                                                                                                                          "isShareable": False,
                                                                                                                          "storagePool": "SP:cpg-growth-limit-1TiB"
                                                                                                                      },
                                                                                                                      "isPermanent": False,
                                                                                                                      "templateUri": 'ROOT:cpg-growth-limit-1TiB'
                                                                                                                  },
                                                                                                                  "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                                                                  'bootVolumePriority': "NotBootable",
                                                                                                                  'lunType': 'Auto',
                                                                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                                                                  },
                                                                                                                 {'id': 4,
                                                                                                                  "volume": {
                                                                                                                      "properties": {
                                                                                                                          "name": "svol6",
                                                                                                                          "size": 11000000000,
                                                                                                                          "provisioningType": "Thin",
                                                                                                                          "isShareable": False,
                                                                                                                          "storagePool": "SP:cpg-growth-limit-1TiB"
                                                                                                                      },
                                                                                                                      "isPermanent": False,
                                                                                                                      "templateUri": 'ROOT:cpg-growth-limit-1TiB'
                                                                                                                  },
                                                                                                                  "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                                                                  'bootVolumePriority': "NotBootable",
                                                                                                                  'lunType': 'Auto',
                                                                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                                                                  }]},
                'initialScopeUris': ['Scope:Scope1', 'Scope:Scope4']
                }
               ]

SPT_SBAC_09 = [{'name': 'SPT_SBAC_09', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]
                                       },
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': [{'id': 1,
                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                      'bootVolumePriority': "NotBootable",
                                                      'lunType': 'Auto',
                                                      "volumeUri": "v:svol3",
                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                      }]},
                'initialScopeUris': ['Scope:Scope5']
                }
               ]

SPT_SBAC_17 = [{'name': 'SPT_SBAC_17', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]
                                       },
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope5']
                }
               ]

SPT_SBAC_17_SP = [{'name': 'SPT_SBAC_17_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                   'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
                   'serverProfileTemplateUri': 'SPT:SPT_SBAC_17'
                   }
                  ]

SPT_SBAC_25 = [{'name': 'SPT_SBAC_25', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"}
                                                       ]
                                       },
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope6']
                }
               ]

SPT_SBAC_25_update = [{'name': 'SPT_SBAC_25', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'manageConnections': True,
                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                              {"id": 4, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                              ]
                                              },
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bootMode': None,
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                       'initialScopeUris': ['Scope:Scope6']
                       }
                      ]

SPT_SBAC_27_update = [{'name': 'SPT_SBAC_25', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'manageConnections': True,
                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                              {"id": 4, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                              {"id": 5, "name": "netset1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "NS:netset1"},
                                                              {"id": 6, "name": "netset2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "NS:netset2"}
                                                              ]
                                              },
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bootMode': None,
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                       'initialScopeUris': ['Scope:Scope6']
                       }
                      ]

SPT_SBAC_25_update_scope = [{"name": "Scope6",
                             "description": "",
                             "type": "ScopeV3",
                             "addedResourceUris": ["ETH:production"],
                             "removedResourceUris": []}]

SPT_SBAC_27_update_scope = [{"name": "Scope6",
                             "description": "",
                             "type": "ScopeV3",
                             "addedResourceUris": ["NS:netset1", "NS:netset2"],
                             "removedResourceUris": []}]

SPT_SBAC_27_reverse_scope = [{"name": "Scope6",
                              "description": "",
                              "type": "ScopeV3",
                              "addedResourceUris": [],
                              "removedResourceUris": ["ETH:production", "NS:netset1", "NS:netset2"]}]

SPT_SBAC_36 = [{'name': 'SPT_SBAC_36', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"}
                                                       ]
                                       },
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                'initialScopeUris': ['Scope:Scope5', 'Scope:Scope6']
                }
               ]

SPT_SBAC_36_update = [{'name': 'SPT_SBAC_36', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'manageConnections': True,
                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                              {"id": 4, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]
                                              },
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bootMode': None,
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
                       'initialScopeUris': ['Scope:Scope5', 'Scope:Scope6']
                       }
                      ]

SPT_SBAC_36_UserUpdate = [{"type": "UserAndPermissions", "userName": "User14_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

SPT_SBAC_36_UserResetToOldScopes = [{"type": "UserAndPermissions", "userName": "User14_SPArch", "enabled": True, "replaceRoles": True, "permissions": [{"roleName": "Server profile architect", "scopeUri": 'Scope5'}, {"roleName": "Server administrator", "scopeUri": 'Scope6'}]}]

SPT_OVF1035_02 = [{'name': 'SPT_OVF1035_02', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                   'connectionSettings': {'manageConnections': False},
                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                   'bootMode': None,
                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                   'bios': {'manageBios': False, 'overriddenSettings': []},
                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                   }]

SPT_OVF1035_02_SP = [{'name': 'SPT_OVF1035_02_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                      'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
    'serverProfileTemplateUri': 'SPT:SPT_OVF1035_02'
}
]


profile_compliance_SPT_OVF1035_02_SP = {"name": "SPT_OVF1035_02_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": []
}}

# profile_compliance_SPT_OVF1035_02_SP = {
#     "name": "",
#     "compliance-preview": {
#         "type": "ServerProfileCompliancePreviewV1",
#         "isOnlineUpdate": None,"automaticUpdates": None,
#         "manualUpdates": None}
# }

SPT_OVF1035_03_1 = [{'name': 'SPT_OVF1035_03_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'manageConnections': True,
                                            'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                            {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                            {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                            {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                            {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                            ]
                                            },
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                     'bootMode': None,
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                     'bios': {'manageBios': False, 'overriddenSettings': []},
                     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                     'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                     }
                    ]

SPT_OVF1035_03_1_update = [{'name': 'SPT_OVF1035_03_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': False},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]
SPT_OVF1035_03_2 = [{'name': 'SPT_OVF1035_03_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'manageConnections': True,
                                            'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                            {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                            {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                            {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                            {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                            ]
                                            },
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                     'bootMode': None,
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                     'bios': {'manageBios': False, 'overriddenSettings': []},
                     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                     'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                     }
                    ]

SPT_OVF1035_03_2_SP = [{'name': 'SPT_OVF1035_03_2_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                        'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
    'serverProfileTemplateUri': 'SPT:SPT_OVF1035_03_2'
}
]

SPT_OVF1035_03_2_update = [{'name': 'SPT_OVF1035_03_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': False},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

SPT_OVF1035_04_1 = [{'name': 'SPT_OVF1035_04_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'manageConnections': False},
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                     'bootMode': None,
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                     'bios': {'manageBios': False, 'overriddenSettings': []},
                     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                     'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                     }
                    ]

SPT_OVF1035_04_1_update = [{'name': 'SPT_OVF1035_04_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

SPT_OVF1035_04_2 = [{'name': 'SPT_OVF1035_04_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'manageConnections': False},
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                     'bootMode': None,
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                     'bios': {'manageBios': False, 'overriddenSettings': []},
                     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                     'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                     }
                    ]

SPT_OVF1035_04_2_SP = [{'name': 'SPT_OVF1035_04_2_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                        'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
    'serverProfileTemplateUri': 'SPT:SPT_OVF1035_04_2'
}
]

SPT_OVF1035_04_2_update = [{'name': 'SPT_OVF1035_04_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

SPT_OVF1035_API_1 = [{'name': 'SPT_OVF1035_API_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"}
                                                                   ]
                                             },
                      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                      'bootMode': None,
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                      'bios': {'manageBios': False, 'overriddenSettings': []},
                      'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                      }
                     ]

SPT_OVF1035_API_1_SP = [{'name': 'SPT_OVF1035_API_1_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                         'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
    'serverProfileTemplateUri': 'SPT:SPT_OVF1035_API_1'
}
]

profile_compliance_SPT_OVF1035_API_1_SP_01 = {"name": "SPT_OVF1035_API_1_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*"]
}}

# profile_compliance_SPT_OVF1035_API_1_SP_01 = {
#     "name": "SPT_OVF1035_API_1_SP",
#     "compliance-preview": {
#         "type": "ServerProfileCompliancePreviewV1",
#         "isOnlineUpdate": True,
#         "automaticUpdates": ["REGEX:Change requested bandwidth of connection on .*"]
#         "manualUpdates": None}
# }

SPT_OVF1035_API_1_update = [{'name': 'SPT_OVF1035_API_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': False},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             }
                            ]

profile_compliance_SPT_OVF1035_API_1_SP_02 = {"name": "SPT_OVF1035_API_1_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": []
}}

# profile_compliance_SPT_OVF1035_API_1_SP_02 = {
#     "name": "SPT_OVF1035_API_1_SP",
#     "compliance-preview": {
#         "type": "ServerProfileCompliancePreviewV1",
#         "isOnlineUpdate": None,
#         "automaticUpdates": None
#         "manualUpdates": None}
# }


SPT_OVF1035_API_2 = [{'name': 'SPT_OVF1035_API_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'manageConnections': False},
                      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                      'bootMode': None,
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                      'bios': {'manageBios': False, 'overriddenSettings': []},
                      'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                      }
                     ]

SPT_OVF1035_API_2_SP = [{'name': 'SPT_OVF1035_API_2_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                         'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
    'serverProfileTemplateUri': 'SPT:SPT_OVF1035_API_2'
}
]

SPT_OVF1035_API_2_update = [{'name': 'SPT_OVF1035_API_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             }
                            ]

profile_compliance_SPT_OVF1035_API_2_SP = {"name": "SPT_OVF1035_API_2_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": True,
    "manualUpdates": [],
    "automaticUpdates": ["REGEX:Change requested bandwidth of connection .*"]
}}

UI_SPT_30 = [{'name': 'UI_SPT_30', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
              'connectionSettings': {'manageConnections': True,
                                     'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                      'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                     ]
                                     },
              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
              'bootMode': None,
              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
              'bios': {'manageBios': False, 'overriddenSettings': []},
              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
              #                              'localStorage': {'sasLogicalJBODs': [], 'complianceControl': 'Checked',
              #                                               'controllers': [{
              #                                                   'logicalDrives': [{
              #                                                   'name': 'sas_hdd1',
              #                                                   'raidLevel': 'RAID1',
              #                                                   'bootable': False,
              #                                                   'numPhysicalDrives': 2,
              #                                                   'driveTechnology': 'SasHdd',
              #                                                   'sasLogicalJBODId': None,
              #                                                   'accelerator': 'Unmanaged'
              #                                                   }],
              #                                                   'deviceSlot': 'Embedded',
              #                                                   'mode': 'RAID',
              #                                                   'initialize': True
              #                                                   }]
              #                                               },
              'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
              'sanStorage': {'hostOSType': 'VMware (ESXi)', 'complianceControl': 'Checked', 'manageSanStorage': True,
                             'volumeAttachments': [{'id': 1,
                                                    "volume": {
                                                        "properties": {
                                                            "name": "san_vol1",
                                                            "size": 10737418240,
                                                            "provisioningType": "Thin",
                                                            "isShareable": False,
                                                            "storagePool": StoragePool1
                                                        },
                                                        "isPermanent": False,
                                                        "templateUri": TemplateUri1,
                                                        "associatedTemplateAttachmentId": "SPTVAID:1"
                                                    },
                                                    "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                    'bootVolumePriority': "Primary",
                                                    'lunType': 'Auto',
                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                   {'id': 2,
                                                    "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                    'bootVolumePriority': "NotBootable",
                                                    'lunType': 'Auto',
                                                    "volumeUri": "v:svol1",
                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_SPT_30_SP = [{'name': 'UI_SPT_30_SP', 'serverHardwareUri': ServerHardware[1], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                 'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                     'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]
},
    'serverProfileTemplateUri': 'SPT:UI_SPT_30',
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volume": {
                                                                             "properties": {
                                                                                 "name": "san_vol1",
                                                                                 "size": 10737418240,
                                                                                 "provisioningType": "Thin",
                                                                                 "isShareable": False,
                                                                                 "storagePool": StoragePool1
                                                                             },
                                                                             "isPermanent": False,
                                                                             "templateUri": TemplateUri1,
                                                                             "associatedTemplateAttachmentId": "SPTVAID:1"
                                                                         },
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "Primary",
                                                                         'lunType': 'Auto',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                        {'id': 2,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol1",
                                                                         "associatedTemplateAttachmentId": "SPTVAID:2",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_SPT_30_update_1 = [{'name': 'UI_SPT_30', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'manageConnections': True,
                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                              ]
                                              },
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bootMode': None,
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       #                              'localStorage': {'sasLogicalJBODs': [], 'complianceControl': 'Checked',
                       #                                               'controllers': [{
                       #                                                   'logicalDrives': [{
                       #                                                   'name': 'sas_hdd1',
                       #                                                   'raidLevel': 'RAID1',
                       #                                                   'bootable': True,
                       #                                                   'numPhysicalDrives': 2,
                       #                                                   'driveTechnology': 'SataHdd',
                       #                                                   'sasLogicalJBODId': None,
                       #                                                   'accelerator': 'Unmanaged'
                       #                                                   }],
                       #                                                   'deviceSlot': 'Embedded',
                       #                                                   'mode': 'RAID',
                       #                                                   'initialize': True
                       #                                                   }]
                       #                                               },
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                       'sanStorage': {'hostOSType': 'VMware (ESXi)', 'complianceControl': 'Checked', 'manageSanStorage': True,
                                      'volumeAttachments': [{'id': 2,
                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                             'bootVolumePriority': "NotBootable",
                                                             'lunType': 'Auto',
                                                             "volumeUri": "v:svol1",
                                                             "associatedTemplateAttachmentId": "SPTVAID:2",
                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

mu1 = "REGEX:Change boot for connection 3 on port .* to not bootable."
mu2 = "REGEX:Delete volume attachment for {\"name\":\"san_vol1\", \"uri\":\"/rest/storage-volumes/.*"
# mu3 = "Modify local storage settings to match with the server profile template."

UI_SPT_30_SP_compliance_1 = {"name": "UI_SPT_30_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [mu1, mu2],
    #    "manualUpdates": [mu1, mu2, mu3],
    "automaticUpdates": []
}}

UI_SPT_30_SP_update_1 = [{'name': 'UI_SPT_30_SP', 'serverHardwareUri': ServerHardware[1], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                          'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]
},
    'serverProfileTemplateUri': 'SPT:UI_SPT_30',
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': [{'id': 2,
                                          "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                          'bootVolumePriority': "NotBootable",
                                          'lunType': 'Auto',
                                          "volumeUri": "v:svol1",
                                          "associatedTemplateAttachmentId": "SPTVAID:2",
                                          'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]


UI_SPT_30_SP_compliance_2 = {"name": "UI_SPT_30_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": None,
    "manualUpdates": [],
    "automaticUpdates": [],
}}

UI_SPT_68 = [{'name': 'UI_SPT_68', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
              'connectionSettings': {'manageConnections': True,
                                     'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                     ]
                                     },
              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
              'bootMode': None,
              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
              'bios': {'manageBios': False, 'overriddenSettings': []},
              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
              'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
              'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                             'volumeAttachments': []}}]


UI_SPT_68_SP = [{'name': 'UI_SPT_68_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                 'serverHardwareUri': ServerHardware[1],
                 'connectionSettings': {
    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                    ]},
                 'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                 'bootMode': None,
                 'serverProfileTemplateUri': 'SPT:UI_SPT_68',
                 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                 'bios': {'manageBios': False, 'overriddenSettings': []},
                 'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                 'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                'volumeAttachments': []}}]


UI_SPT_68_SP_compliance_2 = {"name": "UI_SPT_68_SP", "compliance-preview": {
    "type": "ServerProfileCompliancePreviewV1",
    "isOnlineUpdate": False,
    "manualUpdates": [],
    "automaticUpdates": []
}}

REST_API_SPT_SP_Page_15_1 = [{'name': 'REST_API_SPT_SP_Page_16_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connectionSettings': {'manageConnections': True,
                                                     'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                     ]
                                                     },
                              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                              'bootMode': None,
                              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                              'bios': {'manageBios': False, 'overriddenSettings': []},
                              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                              'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                              }]

REST_API_SPT_SP_Page_15_2 = [{'name': 'REST_API_SPT_SP_Page_16_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connectionSettings': {'manageConnections': True,
                                                     'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                     {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                     {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                     {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                     {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                     ]
                                                     },
                              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                              'bootMode': None,
                              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                              'bios': {'manageBios': False, 'overriddenSettings': []},
                              'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                              'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                              }]

REST_API_SPT_SP_Page_16 = [{'name': 'REST_API_SPT_SP_Page_16_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            },
                           {'name': 'REST_API_SPT_SP_Page_16_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }]

REST_API_SPT_SP_Page_16_update = [{'name': 'REST_API_SPT_SP_Page_16_1', 'new_name': 'REST_API_SPT_SP_Page_16_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'connectionSettings': {'manageConnections': True,
                                                          'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]
                                                          },
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                   }]

OVF1035_09 = [{'name': 'OVF1035_09', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': True,
                                      'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                      ]
                                      },
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
               }
              ]

OVF1035_09_update = [{'name': 'OVF1035_09', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'manageConnections': False},
                      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                      'bootMode': None,
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                      'bios': {'manageBios': False, 'overriddenSettings': []},
                      'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                      }
                     ]

REST_API_SPT_SP_Page_14 = [{'name': 'REST_API_SPT_SP_Page_14', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1 Invalid', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': True,
                                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                   ]
                                                   },
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

SP_Page_23 = [{'name': 'SP_Page_23', 'type': ServerProfile_type, 'serverHardwareUri': ServerHardware[0], 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]
SPT_SP_Page_23 = [{'name': 'SPT_SP_Page_23', 'SP': SP_Page_23}]
SPT_SP_Page_23_SP_1 = [{'name': 'SPT_SP_Page_23_SP_1', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type, 'serverHardwareUri': ServerHardware[1],
                        'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                               {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                               {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                               {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                               {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                        'serverProfileTemplateUri': 'SPT:SPT_SP_Page_23',
                        'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                        'bootMode': None,
                        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                        'bios': {'manageBios': False, 'overriddenSettings': []},
                        'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                        'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

OVF1035_08 = [{'name': 'OVF1035_08', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
               }]
OVF1035_08_update = [{'name': 'OVF1035_08', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'manageConnections': True,
                                             'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                             {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                             {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                             {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]
                                             },
                      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                      'bootMode': None,
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                      'bios': {'manageBios': False, 'overriddenSettings': []},
                      'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                      }]

SP_Page_21 = [{'name': 'SP_Page_21', 'type': ServerProfile_type, 'serverHardwareUri': ServerHardware[1], 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                      {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                      {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                      ]
                                      },
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
               'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                              'volumeAttachments': [{'id': 1,
                                                     "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                     'bootVolumePriority': "NotBootable",
                                                     'lunType': 'Auto',
                                                     "volumeUri": "v:svol3",
                                                     'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]
SPT_SP_Page_21 = [{'name': 'SPT_SP_Page_21', 'SP': SP_Page_21}]
SPT_SP_Page_21_update = [{'name': 'SPT_SP_Page_21', 'type': ServerProfileTemplate_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'manageConnections': True,
                                                 'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                 ]
                                                 },
                          'boot': {'manageBoot': True, 'order': ['USB', 'HardDisk', 'PXE', 'CD', 'Floppy']},
                          'bootMode': None,
                          'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareAndOSDrivers', 'firmwareActivationType': 'Immediate'},
                          'bios': {'manageBios': True, 'overriddenSettings': []},
                          'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                         'volumeAttachments': [{'id': 1,
                                                                "associatedTemplateAttachmentId": 'SPTVAID:1',
                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                'bootVolumePriority': "NotBootable",
                                                                'lunType': 'Auto',
                                                                "volumeUri": "v:svol3",
                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_67 = [{'name': 'UI_ServerProfileTemplate_67_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                        "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                        "networkUri": "ETH:production"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}},
                               {'name': 'UI_ServerProfileTemplate_67_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                        "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                        "networkUri": "ETH:production"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol3",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]
UI_ServerProfileTemplate_67_SP = [{'name': 'UI_ServerProfileTemplate_67_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type, 'serverHardwareUri': ServerHardware[1],
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_67_1',
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol3",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]
UI_ServerProfileTemplate_67_SP_update = [{'name': 'UI_ServerProfileTemplate_67_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type, 'serverHardwareUri': ServerHardware[1],
                                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                          'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_67_2',
                                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                          'bootMode': None,
                                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1,
                                                                                "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                                'bootVolumePriority': "NotBootable",
                                                                                'lunType': 'Auto',
                                                                                "volumeUri": "v:svol3",
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]
profile_compliance_SP_67 = {"name": "UI_ServerProfileTemplate_67_SP",
                            "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                   "isOnlineUpdate": None,
                                                   "manualUpdates": [],
                                                   "automaticUpdates": []
                                                   }}
UI_ServerProfileTemplate_67_update = [{'name': 'UI_ServerProfileTemplate_67_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'manageConnections': True,
                                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                               "networkUri": "ETH:production"},
                                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                               "networkUri": "ETH:production"}]},
                                       'boot': {'manageBoot': True, 'order': ['USB', 'HardDisk', 'PXE', 'CD', 'Floppy', ]},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                       'bios': {'manageBios': True, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                       'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1,
                                                                             "associatedTemplateAttachmentId": 'SPTVAID:1',
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "NotBootable",
                                                                             'lunType': 'Auto',
                                                                             "volumeUri": "v:svol3",
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]
profile_compliance_SP_67_updated = {"name": "UI_ServerProfileTemplate_67_SP",
                                    "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                           "isOnlineUpdate": False,
                                                           "manualUpdates": [],
                                                           "automaticUpdates": ["REGEX:Change boot order to .*", "REGEX:Change BIOS settings to managed by profile."]
                                                           }}

REST_API_SPT_SP_Page_18 = [{'name': '', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': False},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

REST_API_SPT_SP_Page_19 = [{'name': 'REST_API_SPT_SP_Page_19', 'type': '', 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': False},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }
                           ]

SPT_SBAC6_1 = [{'name': 'SPT_SBAC6_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                             "firmwareActivationType": "Immediate"},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'initialScopeUris': ['Scope:Scope1', 'Scope:Scope5']
                }
               ]

SPT_SBAC6_2 = [{'name': 'SPT_SBAC6_2', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                'connectionSettings': {'manageConnections': True,
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                       ]},
                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                'bootMode': None,
                'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                             "firmwareActivationType": "Immediate"},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                'initialScopeUris': ['Scope:Scope5']
                }
               ]

SPT_SBAC71 = [{'name': 'ServerProfileTemplate_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
               'initialScopeUris': ['Scope:Scope1']
               }]

SPT_SBAC72 = [{'name': 'ServerProfileTemplate_1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
               'initialScopeUris': ['Scope:Scope1', 'Scope:Scope3']
               }]

storage_volumes = [{"storageSystemUri": VolumeStorageSystemUri1, "name": "svol3"}]

UI_ServerProfileTemplate_48 = {
    "name": "UI_ServerProfileTemplate_56_SP",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}

UI_ServerProfileTemplate_42_SP = [{'name': 'UI_ServerProfileTemplate_42_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'serverHardwareUri': ServerHardware[0],
                                   'connectionSettings': {
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "NS:netset1"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:net1"},
                                                       {"id": 6, "name": "tunnel_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:tunneled_nw"}
                                                       ]},
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_57',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': True, 'overriddenSettings': [{'id': '64', 'value': '1'}]},
                                   'hideUnusedFlexNics': False, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [
                                                  ]}}]

UI_ServerProfileTemplate_42_compliance = {
    "name": "UI_ServerProfileTemplate_42_SP",
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []}
}
network_sets_update_add = [{'name': 'netset1', 'add_networkUris': ['corp1']}]
network_sets_update_delete = [{'name': 'netset1', 'delete_networkUris': ['corp1']}]

UI_ServerProfileTemplate_50 = [{'name': 'UI_ServerProfileTemplate_50', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]
                                                       },
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                }]

UI_ServerProfileTemplate_50_update = [{'name': 'UI_ServerProfileTemplate_50', 'new_name': '!@#$%^&', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'manageConnections': True,
                                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                              ]
                                                              },
                                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                       }]

UI_ServerProfileTemplate_51_SP = [{'name': 'UI_ServerProfileTemplate_51_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'serverHardwareUri': ServerHardware[0],
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_50',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': True, 'overriddenSettings': [{'id': '64', 'value': '1'}]},
                                   'hideUnusedFlexNics': False, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []}
                                   }]

UI_ServerProfileTemplate_51_SP_update = [{'name': 'UI_ServerProfileTemplate_51_SP', 'new_name': '!@', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                          'serverHardwareUri': ServerHardware[0],
                                          'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                                 ]},
                                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                          'bootMode': None,
                                          'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_50',
                                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                          'bios': {'manageBios': True, 'overriddenSettings': [{'id': '64', 'value': '1'}]},
                                          'hideUnusedFlexNics': False, 'iscsiInitiatorNameType': 'AutoGenerated',
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []}
                                          }]

UI_ServerProfileTemplate_12 = [{'name': 'UI_ServerProfileTemplate_12', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': False},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': True, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                }
                               ]

SPT_SBAC_8 = [{'name': 'SPT_SBAC_8', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
               'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []},
               'initialScopeUris':{'Scope:Scope2'}
               }
              ]

REST_API_SPT_SP_Page_20 = [{'name': 'REST_API_SPT_SP_Page_20', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': None, 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': False},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }]
REST_API_SPT_SP_Page_21 = [{'name': 'REST_API_SPT_SP_Page_21', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': None, 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'manageConnections': False},
                            'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                            'bootMode': None,
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                            'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                            }]

SPT_SP_Page_20 = [{'name': 'SPT_SP_Page_20', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                   'connectionSettings': {'manageConnections': True,
                                          'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                           "networkUri": "ETH:production"},
                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                           "networkUri": "ETH:production"}]},
                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                   'bootMode': None,
                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                   'bios': {'manageBios': False, 'overriddenSettings': []},
                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

SPT_SP_Page_20_SP = [{'name': 'SPT_SP_Page_20_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type, 'serverHardwareUri': ServerHardware[1],
                      'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                             {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                             {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                             {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                      'serverProfileTemplateUri': 'SPT:SPT_SP_Page_20',
                      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                      'bootMode': None,
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                      'bios': {'manageBios': False, 'overriddenSettings': []},
                      'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                      'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

SPT_SP_Page_20_update = [{'name': 'SPT_SP_Page_20', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[1], 'enclosureGroupUri': 'EG:enclgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'manageConnections': True,
                                                 'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                  "networkUri": "ETH:production"},
                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                  "networkUri": "ETH:production"}]},
                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                          'bootMode': None,
                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                          'bios': {'manageBios': False, 'overriddenSettings': []},
                          'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

UI_ServerProfileTemplate_34 = [{'name': 'UI_ServerProfileTemplate_34', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                        'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                        "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                        "networkUri": "ETH:production"}]},
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                'sanStorage': {'hostOSType': 'VMware (ESXi)', 'complianceControl': 'Checked', 'manageSanStorage': True,
                                               'volumeAttachments': [{'id': 1,
                                                                      "volume": {
                                                                          "properties": {
                                                                              "name": "san_vol1",
                                                                              "size": 10737418240,
                                                                              "provisioningType": "Thin",
                                                                              "isShareable": False,
                                                                              "storagePool": StoragePool1
                                                                          },
                                                                          "isPermanent": False,
                                                                          "templateUri": TemplateUri1
                                                                      },
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "Primary",
                                                                      'lunType': 'Auto',
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}],
                                                                      "associatedTemplateAttachmentId": "1"},
                                                                     {'id': 2,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      'bootVolumePriority': "NotBootable",
                                                                      'lunType': 'Auto',
                                                                      "volumeUri": "v:svol1",
                                                                      'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}],
                                                                      "associatedTemplateAttachmentId": "2"
                                                                      }]}}]

UI_ServerProfileTemplate_34_SP = [{'name': 'UI_ServerProfileTemplate_34_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type, 'serverHardwareUri': ServerHardware[1],
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                           'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_34',
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1,
                                                                         "volume": {
                                                                             "properties": {
                                                                                 "name": "san_vol1",
                                                                                 "size": 10737418240,
                                                                                 "provisioningType": "Thin",
                                                                                 "isShareable": False,
                                                                                 "storagePool": StoragePool1
                                                                             },
                                                                             "isPermanent": False,
                                                                             "templateUri": TemplateUri1
                                                                         },
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "Primary",
                                                                         'lunType': 'Auto',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}],
                                                                         "associatedTemplateAttachmentId": "1"},
                                                                        {'id': 2,
                                                                         "associatedTemplateAttachmentId": "2",
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         'bootVolumePriority': "NotBootable",
                                                                         'lunType': 'Auto',
                                                                         "volumeUri": "v:svol1",
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]

UI_ServerProfileTemplate_34_update = [{'name': 'UI_ServerProfileTemplate_34', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'manageConnections': True,
                                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                               "networkUri": "ETH:production"},
                                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                               "networkUri": "ETH:production"}]},
                                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                       'sanStorage': {'hostOSType': 'VMware (ESXi)', 'complianceControl': 'Checked', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1,
                                                                             "volume": {
                                                                                 "properties": {
                                                                                     "name": "san_vol1_rename",
                                                                                     "size": 10737418340,
                                                                                     "provisioningType": "Thin",
                                                                                     "isShareable": False,
                                                                                     "storagePool": StoragePool1
                                                                                 },
                                                                                 "isPermanent": False,
                                                                                 "templateUri": TemplateUri1
                                                                             },
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "Primary",
                                                                             'lunType': 'Auto',
                                                                             "associatedTemplateAttachmentId": "1",
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                            {'id': 2,
                                                                             "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                             'bootVolumePriority': "NotBootable",
                                                                             'lunType': 'Auto',
                                                                             "volumeUri": "v:svol1",
                                                                             "associatedTemplateAttachmentId": "2",
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}}]


au34_1 = "REGEX:Change requested bandwidth of connection .*"
mu34_1 = "REGEX:Attachment id 1 for volume .*must be at least the capacity of the volume as defined in the server profile template. The capacity of the volume can be corrected on the volumes page.  Alternatively, the volume's defined capacity can be corrected on the server profile template and volume template .*."
profile_compliance_SP_34_1 = {"name": "UI_ServerProfileTemplate_34_SP",
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": True,
                                                     "manualUpdates": [mu34_1],
                                                     "automaticUpdates": [au34_1]
                                                     }}

profile_compliance_SP_34_2 = {"name": "UI_ServerProfileTemplate_34_SP",
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": None,
                                                     "manualUpdates": [],
                                                     "automaticUpdates": []
                                                     }}

UI_ServerProfileTemplate_OVTC32293_25 = [{'name': 'UI_ServerProfileTemplate_25', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                          'connectionSettings': {'manageConnections': True,
                                                                 'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                                  "networkUri": "ETH:production"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                                  "networkUri": "ETH:production"}]},
                                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                          'bootMode': None,
                                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}},
                                         {'name': 'UI_ServerProfileTemplate_25_different_encgrp', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0],
                                          'enclosureGroupUri': 'EG:enclgrp1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                          'connectionSettings': {'manageConnections': True,
                                                                 'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                 {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                 {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800",
                                                                                  "networkUri": "ETH:production"},
                                                                                 {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                                  "networkUri": "ETH:production"}]},
                                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                          'bootMode': None,
                                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                          'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

UI_ServerProfileTemplate_OVTC32293_25_SP = [{'name': 'UI_ServerProfileTemplate_25_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type, 'serverHardwareUri': ServerHardware[1],
                                             'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                             'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_25',
                                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                             'bootMode': None,
                                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                             'bios': {'manageBios': False, 'overriddenSettings': []},
                                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

UI_ServerProfileTemplate_OVTC32293_25_SP_update = [{'name': 'UI_ServerProfileTemplate_25_SP', 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type, 'serverHardwareUri': ServerHardware[1],
                                                    'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                                    'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_25_different_encgrp',
                                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                                    'bootMode': None,
                                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]


mu25_1 = "REGEX:Change enclosure group to *."
profile_compliance_SP_25_1 = {"name": "UI_ServerProfileTemplate_25_SP",
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": None,
                                                     "manualUpdates": [mu25_1],
                                                     "automaticUpdates": []
                                                     }}

profile_compliance_SP_25_2 = {"name": "UI_ServerProfileTemplate_25_SP",
                              "compliance-preview": {"type": "ServerProfileCompliancePreviewV1",
                                                     "isOnlineUpdate": None,
                                                     "manualUpdates": [],
                                                     "automaticUpdates": []
                                                     }}
SPT_SBAC_28_EditScope = [{"name": "Scope1",
                          "description": "",
                          "type": "ScopeV3",
                          "addedResourceUris": [],
                          "removedResourceUris": ["ETH:production"]}]

UI_ServerProfileTemplate_71_SP = [{'name': 'UI_SPT_68_SP', 'type': ServerProfile_type, 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                   'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                   'bootMode': None,
                                   'serverProfileTemplateUri': 'SPT:UI_SPT_68',
                                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                   'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': []}}]

ServerProfileTemplate_20 = [{'name': 'ServerProfileTemplate_20_spt', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': False},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             }
                            ]
ServerProfileTemplate_20_SPT = [{'name': 'ServerProfileTemplate_20_spt', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                 'connectionSettings': {'manageConnections': True,
                                                        'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                        {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                        {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                        {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                        {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                        ]
                                                        },
                                 'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                 'bootMode': None,
                                 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                 'bios': {'manageBios': False, 'overriddenSettings': []},
                                 'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                 'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                 }
                                ]

UI_ServerProfileTemplate_52_SPT = [{'name': 'UI_ServerProfileTemplate_52_SPT', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"}
                                                                           ]
                                                           },
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                    },
                                   {'name': 'UI_ServerProfileTemplate_52_SPT1', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[1], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'manageConnections': True,
                                                           'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                           {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                           {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                           {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                           {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"}
                                                                           ]
                                                           },
                                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                    'bootMode': None,
                                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                    }
                                   ]

UI_ServerProfileTemplate_49 = [{"name": "UI_ServerProfileTemplate_49_@$", "type": ServerProfileTemplate_type, "serverProfileDescription": "", "serverHardwareTypeUri": ServerHardwareType[0], "enclosureGroupUri": "EG:" + enclgrp, "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                                "connectionSettings": {"manageConnections": True,
                                                       "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:icsp"},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:corp"},
                                                                       {"id": 3, "name": "ft_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:ft_net"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2800", "networkUri": "ETH:production"}
                                                                       ]},
                                "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                                "bootMode": None,
                                "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
                                "bios": {"manageBios": False, "overriddenSettings": []},
                                "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                                "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": False, "volumeAttachments": []}
                                }
                               ]

UI_ServerProfileTemplate_49_SP = [{"name": "UI_ServerProfileTemplate_49_SP_@$", "serverHardwareUri": ServerHardware[0], "enclosureGroupUri": "EG:" + enclgrp, "type": ServerProfile_type,
                                   "connectionSettings": {"connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:icsp"},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:corp"},
                                                                          {"id": 3, "name": "ft_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:ft_net"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   "serverProfileTemplateUri": "SPT:UI_ServerProfileTemplate_49_@$"}]

UI_ServerProfileTemplate_55 = [{"name": "UI_ServerProfileTemplate_55", "type": ServerProfileTemplate_type, "serverProfileDescription": "", "serverHardwareTypeUri": ServerHardwareType[0], "enclosureGroupUri": "EG:" + enclgrp, "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                                "connectionSettings": {"manageConnections": True,
                                                       "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:icsp"},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:corp"},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                       ]},
                                "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                                "bootMode": None,
                                "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                             "firmwareActivationType": "Immediate"},
                                "bios": {"manageBios": False, "overriddenSettings": []},
                                "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                                "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                               "volumeAttachments": [{"id": 1,
                                                                      "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                      "bootVolumePriority": "NotBootable",
                                                                      "lunType": "Auto",
                                                                      "volumeUri": "v:svol3",
                                                                      "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}}]

UI_ServerProfileTemplate_55_SP = [{"name": "UI_ServerProfileTemplate_55_SP", "serverHardwareUri": ServerHardware[1], "enclosureGroupUri": "EG:" + enclgrp, "type": ServerProfile_type,
                                   "connectionSettings": {"connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:icsp"},
                                                                          {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:corp"},
                                                                          {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                          {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                          {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                          ]},
                                   "serverProfileTemplateUri": "SPT:UI_ServerProfileTemplate_55",
                                   "firmware": {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                "firmwareActivationType": "Immediate"},
                                   "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                  "volumeAttachments": [{"id": 1,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         "bootVolumePriority": "NotBootable",
                                                                         "lunType": "Auto",
                                                                         "volumeUri": "v:svol3",
                                                                         "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                        {"id": 2,
                                                                         "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                         "bootVolumePriority": "NotBootable",
                                                                         "lunType": "Auto",
                                                                         "volumeUri": "v:svol4",
                                                                         "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}}]

UI_ServerProfileTemplate_57_1 = [{"name": "UI_ServerProfileTemplate_57", "type": ServerProfileTemplate_type, "serverProfileDescription": "", "serverHardwareTypeUri": ServerHardwareType[0],
                                  "enclosureGroupUri": "EG:" + enclgrp, "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                                  "connectionSettings": {"manageConnections": True,
                                                         "connections": [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:icsp"},
                                                                         {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:corp"},
                                                                         {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                         {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                         {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                         ]},
                                  "boot": {"manageBoot": True, "order": ["CD", "Floppy", "USB", "HardDisk", "PXE"]},
                                  "bootMode": None,
                                  "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                               "firmwareActivationType": "Immediate"},
                                  "bios": {"manageBios": False, "overriddenSettings": []},
                                  "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                                  "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                  "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                 "volumeAttachments": [{"id": 1,
                                                                        "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                        "bootVolumePriority": "NotBootable",
                                                                        "lunType": "Auto",
                                                                        "volumeUri": "v:svol3",
                                                                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                       {"id": 2,
                                                                           "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                           "bootVolumePriority": "NotBootable",
                                                                           "lunType": "Auto",
                                                                           "volumeUri": "v:svol4",
                                                                           "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}}]

UI_ServerProfileTemplate_57_SP_1 = [{"name": "UI_ServerProfileTemplate_57_SP", "serverHardwareUri": ServerHardware[1], "enclosureGroupUri": "EG:" + enclgrp, "type": ServerProfile_type,
                                     "serialNumberType": "Physical", "macType": "Physical", "wwnType": "Physical", "serverHardwareTypeUri": ServerHardwareType[0],
                                     "connectionSettings": {"connections": [{"id": 1, "name": "netset1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "NS:netset1"},
                                                                            {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:corp"},
                                                                            {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                            {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                            {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                            ]},
                                     "serverProfileTemplateUri": "SPT:UI_ServerProfileTemplate_57",
                                     "firmware": {"manageFirmware": True, "firmwareBaselineUri": FirmwareVersion, "forceInstallFirmware": False, "firmwareInstallType": "FirmwareOnlyOfflineMode",
                                                  "firmwareActivationType": "Immediate"},
                                     "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                                    "volumeAttachments": [{"id": 1,
                                                                           "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                           "bootVolumePriority": "NotBootable",
                                                                           "lunType": "Auto",
                                                                           "volumeUri": "v:svol3",
                                                                           "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]},
                                                                          {"id": 2,
                                                                           "volumeStorageSystemUri": VolumeStorageSystemUri1,
                                                                           "bootVolumePriority": "NotBootable",
                                                                           "lunType": "Auto",
                                                                           "volumeUri": "v:svol4",
                                                                           "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []}]}]}}]

UI_ServerProfileTemplate_29 = [{'name': 'UI_ServerProfileTemplate_29', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                'boot': {'manageBoot': False, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]


UI_ServerProfileTemplate_29_SP = [{'name': 'UI_ServerProfileTemplate_29_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {
                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_29',
                                   'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]
UI_ServerProfile_SP_Power_On = ServerHardware[0]
UI_ServerProfileTemplate_29_update = [{'name': 'UI_ServerProfileTemplate_29', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'manageConnections': False,
                                                              'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                       'boot': {'manageBoot': True, 'order': ['HardDisk', 'USB', 'CD', 'PXE', 'Floppy']},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                       'bios': {'manageBios': True, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                       }
                                      ]

profile_compliance_UI_ServerProfile_SP = {"name": "UI_ServerProfileTemplate_29_SP",
                                          "compliance-preview": {
                                              "type": "ServerProfileCompliancePreviewV1",
                                              "automaticUpdates": ["REGEX:Change boot order to .*", "REGEX:Change BIOS settings to managed by profile."],
                                              "manualUpdates": []
                                          }
                                          }

UI_ServerProfile_SP_Power_Off = ServerHardware[0]
UI_ServerProfileTemplate_29_sp_SPT = [{'name': 'UI_ServerProfileTemplate_29_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                       'connectionSettings': {'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                              {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                              {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                              {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                              {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                              ]},
                                       'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_29',
                                       'boot': {'manageBoot': True, 'order': ['HardDisk', 'USB', 'CD', 'PXE', 'Floppy']},
                                       'bootMode': None,
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                       'bios': {'manageBios': True, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                       }
                                      ]
profile_compliance_UI_ServerProfile_SP1 = {"name": "UI_ServerProfileTemplate_29_SP",
                                           "compliance-preview": {
                                               "type": "ServerProfileCompliancePreviewV1",
                                               "automaticUpdates": [],
                                               "manualUpdates": []}
                                           }

UI_ServerProfileTemplate_32 = [{'name': 'UI_ServerProfileTemplate_32', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"}
                                                                       ]
                                                       },
                                'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                'bootMode': None,
                                'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                'bios': {'manageBios': False, 'overriddenSettings': []},
                                'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                }
                               ]
UI_ServerProfileTemplate_32_SP = [{'name': 'UI_ServerProfileTemplate_32_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {
                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"}
                                                   ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_32'
                                   },
                                  {'name': 'UI_ServerProfileTemplate_32_SP1', 'serverHardwareUri': ServerHardware[1], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                                   'connectionSettings': {
                                      'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                      {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                      {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"}
                                                      ]},
                                   'serverProfileTemplateUri': 'SPT:UI_ServerProfileTemplate_32'
                                   }
                                  ]
UI_ServerProfileTemplate_32_SP1_Update = [{'name': 'UI_ServerProfileTemplate_32', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                           'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'HardDisk', 'USB', 'PXE']},
                                           'bootMode': None,
                                           'firmware': {'manageFirmware': True, 'firmwareBaselineUri': FirmwareVersion, 'forceInstallFirmware': False, "firmwareInstallType": "FirmwareOnlyOfflineMode", "firmwareActivationType": "Immediate"},
                                           'bios': {'manageBios': True, 'overriddenSettings': []},
                                           'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                           }]

profile_compliance_UI_ServerProfileTemplate_32_SP = {"name": "UI_ServerProfileTemplate_32_SP",
                                                     "compliance-preview": {
                                                         "type": "ServerProfileCompliancePreviewV1",
                                                         "automaticUpdates": ["REGEX:Create a connection to network .*", "REGEX:Change firmware baseline to .*", "REGEX:Change firmware installation method to Firmware only.", "REGEX:Change firmware activation type to Immediately.", "REGEX:Change boot order to .*", "REGEX:Change BIOS settings to managed by profile."],
                                                         "manualUpdates": []}
                                                     }

profile_compliance_UI_ServerProfileTemplate_32_SP1 = {"name": "UI_ServerProfileTemplate_32_SP1",
                                                      "compliance-preview": {
                                                          "type": "ServerProfileCompliancePreviewV1",
                                                          "automaticUpdates": ["REGEX:Create a connection to network .*", "REGEX:Change firmware baseline to .*", "REGEX:Change firmware installation method to Firmware only.", "REGEX:Change firmware activation type to Immediately.", "REGEX:Change boot order to .*", "REGEX:Change BIOS settings to managed by profile."],
                                                          "manualUpdates": []}
                                                      }
ServerProfileTemplate_12_SPT = [{'name': 'ServerProfileTemplate_12_SPT', 'type': ServerProfileTemplate_type, 'serverProfileDescription': '', 'serverHardwareTypeUri': ServerHardwareType[0], 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connectionSettings': {'manageConnections': True,
                                                       'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                       {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                       {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                       {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                       {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                 'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                                 'bootMode': None,
                                 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                 'bios': {'manageBios': False, 'overriddenSettings': []},
                                 'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                                 'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                                 }]

ServerProfileTemplate_12_SP = [{'name': 'ServerProfileTemplate_12_SP', 'serverHardwareUri': ServerHardware[0], 'enclosureGroupUri': 'EG:enclgrp', "type": ServerProfile_type,
                               'connectionSettings': {
                                   'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                   {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                   {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                   {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                   {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}]},
                                'serverProfileTemplateUri': 'SPT:ServerProfileTemplate_12_SPT'}]
