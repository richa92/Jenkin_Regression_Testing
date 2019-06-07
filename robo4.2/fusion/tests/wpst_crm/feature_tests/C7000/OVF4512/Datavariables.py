

# Appliance IP to be changed for different appliance
APPLIANCE_IP = '15.186.26.190'

# Appliance Credentials to be changed
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# EG Name
EG = 'config1-group'

# LIG Name
LIG = 'LIG-COMP-OU'

# LI Name
LI_NAME = {'name': 'enc2-LIG-COMP-OU'}

LI = 'enc2-LIG-COMP-OU'


# Enclosure details to be changed for different hardware
ENCs = ['enc2']
ENC1 = 'enc2'
Enclosure_IP = '15.186.23.18'
Enc_Username = 'Administrator'
Enc_Password = 'compaq'
enc_body1 = [{'hostname': Enclosure_IP, 'username': Enc_Username, 'password': Enc_Password, 'enclosureGroupUri': 'EG:' + EG, 'licensingIntent': 'OneViewNoiLO'}]

# Interconnect Details need to be changed for different Enclosure

IC_Hill = [ENC1 + ', interconnect 5', ENC1 + ', interconnect 6']
IC_Utah = [ENC1 + ', interconnect 3', ENC1 + ', interconnect 4']
Utah_bays = ['3', '4']
Hill_bays = ['5', '6']

# Uplinkset Names
US_Names_Hill = ['us_hill1', 'us_hill2']
US_Names_Utah = ['us_1', 'us_2']

# Uplink port details to be changed for different hardware
uplinkport_Hill = [['1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3']]
uplinkport_Utah = [['1', '2'], ['1', '2']]

# downlink port details to be changed for different hardware
downlink_ports_hill = [['d1', 'd2'], ['d1', 'd2']]  # hill bay 5, 6
downlink_ports_utah = [['d1', 'd2'], ['d1', 'd2']]  # utah bay 3, 4

# Removed uplinkports from Hill & Utah in LIG
removedports_Hill = [['6', '7'], ['1', '2', '3']]
removedports_Utah = [['2'], ['1', '2']]

# Removed uplinkports from Hill & Utah in LI
LI_removedports_Hill = [['1', '2', '3', '4', '5', '6', '7', '8'], ['1']]
LI_removedports_Utah = [['1', '2'], ['2']]

# FC Modes
fcmodes = ['TRUNK', 'NONE']

# checking the attributes with older Xapi versions
older_xapi_versions = ['600', '800']

# FC Switch Details
Switch_IP = '15.186.24.60'
Switch_UserName = 'admin'
Switch_Password = 'password'
FC_switch_details = {'ip': Switch_IP, 'userName': Switch_UserName, 'password': Switch_Password}
FC_switch_ports = {'segment1': [0, 1, 2, 3, 4, 5, 6, 7], 'segment2': [8, 9, 10]}

# Bay for which trunk group is to be created
Trunking_Bays = ['5', '6']

US_details = [{'bay': Trunking_Bays[0], 'Act_ports': ['1', '2', '3', '4', '5', '6', '7', '8'], 'rel_ports':['17', '18', '19', '20', '21', '22', '23', '24'], 'name':'us_hill1'}, {'bay': Trunking_Bays[1], 'Act_ports': ['1', '2', '3'], 'rel_ports':['17', '18', '19'], 'name':'us_hill2'}]

# Trunking commands
Trunk_Commands = ['porttrunkarea --show enabled', 'portdisable', 'porttrunkarea --disable', 'portcfgtrunkport', 'portenable', 'porttrunkarea --enable', 'portCfgPersistentenable']
no_trunk_message = 'No ports have Trunk Area enabled'

# Trunking Modes
fcmodes = ['TRUNK', 'NONE', 'NA']

FUSION_PROMPT = '#'

fc = [{'type': 'fc-networkV4',
       'linkStabilityTime': 30,
       'autoLoginRedistribution': False,
       'name': 'FA_1',
       'connectionTemplateUri': None,
       'managedSanUri': None,
       'fabricType': 'FabricAttach'},

      {'type': 'fc-networkV4',
       'linkStabilityTime': 30,
       'autoLoginRedistribution': False,
       'name': 'FA_2',
       'connectionTemplateUri': None,
       'managedSanUri': None,
       'fabricType': 'FabricAttach'},
      {'type': 'fc-networkV4',
       'linkStabilityTime': 30,
       'autoLoginRedistribution': False,
       'name': 'FA_3',
       'connectionTemplateUri': None,
       'managedSanUri': None,
       'fabricType': 'FabricAttach'},
      {'type': 'fc-networkV4',
       'linkStabilityTime': 30,
       'autoLoginRedistribution': False,
       'name': 'FA_4',
       'connectionTemplateUri': None,
       'managedSanUri': None,
       'fabricType': 'FabricAttach'}
      ]

edit_lig_uplink_server = {
    'UplinkSet_1': {'name': 'us_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},

    'UplinkSet_2': {'name': 'us_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '4', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},

    'UplinkSet_3': {'name': 'us_hill1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_3'], 'fcMode': 'TRUNK', 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '3', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '4', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '5', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '6', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '7', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '8', 'speed': 'Auto'}]
                    },
    'UplinkSet_4': {'name': 'us_hill2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_4'], 'fcMode': 'TRUNK', 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                               {'bay': '6', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]},

    'UplinkSet_5': {'name': 'us_hill1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_3'], 'fcMode': 'NONE', 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None, 'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                                                                                                                                                                                                     {'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                                                                                                                                                                                                     {'bay': '5', 'enclosure': '1', 'port': '3', 'speed': 'Auto'},
                                                                                                                                                                                                                                     {'bay': '5', 'enclosure': '1', 'port': '4', 'speed': 'Auto'},
                                                                                                                                                                                                                                     {'bay': '5', 'enclosure': '1', 'port': '5', 'speed': 'Auto'},
                                                                                                                                                                                                                                     {'bay': '5', 'enclosure': '1', 'port': '8', 'speed': 'Auto'}]},

    'UplinkSet_6': {'name': 'us_hill2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_4'], 'fcMode': 'NA', 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': []},

    'UplinkSet_7': {'name': 'us_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}
                                               ]},

    'UplinkSet_8': {'name': 'us_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': []}
}


lig_uplink_server = {
    'UplinkSet_1': {'name': 'us_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},

    'UplinkSet_2': {'name': 'us_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '4', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},

    'UplinkSet_3': {'name': 'us_hill1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_3'], 'fcMode': 'NONE', 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '3', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '4', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '5', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '6', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '7', 'speed': 'Auto'},
                                               {'bay': '5', 'enclosure': '1', 'port': '8', 'speed': 'Auto'}]
                    },

    'UplinkSet_4': {'name': 'us_hill2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FA_4'], 'fcMode': 'NONE', 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                    'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                               {'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                               {'bay': '6', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]}

}


ligs = {'lig1':
        {'name': 'LIG-COMP-OU',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                                     ],
         'internalNetworkUris': [],
            'uplinkSets': [lig_uplink_server['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_2'].copy(), lig_uplink_server['UplinkSet_3'].copy(), lig_uplink_server['UplinkSet_4'].copy()],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None,
            'qosConfiguration': None}}


eg_body1 = {'name': 'config1-group',
            'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
            'ipRangeUris': [],
            'enclosureCount': 1,
            'osDeploymentSettings': None,
            'configurationScript': None,
            'powerMode': None,
            'ambientTemperatureMode': 'Standard'}


edit_lig = {'lig_trunking_enable':
            {
                'name': 'LIG-COMP-OU',
                'type': 'logical-interconnect-groupV6',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
                'internalNetworkUris': [],
                'uplinkSets': [edit_lig_uplink_server['UplinkSet_1'].copy(), edit_lig_uplink_server['UplinkSet_2'].copy(), edit_lig_uplink_server['UplinkSet_3'].copy(), edit_lig_uplink_server['UplinkSet_4'].copy()],
                'stackingMode': 'Enclosure',
                'ethernetSettings': None,
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None,
                'qosConfiguration': None,

            },
            'lig_remove_uplinkport_hill':
            {'name': 'LIG-COMP-OU',
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                                         ],
             'internalNetworkUris': [],
             'uplinkSets': [edit_lig_uplink_server['UplinkSet_1'].copy(), edit_lig_uplink_server['UplinkSet_2'].copy(), edit_lig_uplink_server['UplinkSet_5'].copy(), edit_lig_uplink_server['UplinkSet_6'].copy()],
             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None,
             'qosConfiguration': None},

            'lig_remove_uplinkport_utah':
            {
                'name': 'LIG-COMP-OU',
                'type': 'logical-interconnect-groupV6',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 8, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
                'internalNetworkUris': [],
                'uplinkSets': [edit_lig_uplink_server['UplinkSet_7'].copy(), edit_lig_uplink_server['UplinkSet_8'].copy(), lig_uplink_server['UplinkSet_3'].copy(), lig_uplink_server['UplinkSet_4'].copy()],
                'stackingMode': 'Enclosure',
                'ethernetSettings': None,
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None,
                'qosConfiguration': None

            }

            }


server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'config1-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:51', 'wwnn': '20:00:a0:b9:cc:1c:08:51'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:52', 'wwnn': '20:00:a0:b9:cc:1c:08:52'},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': None, 'wwnn': None},
                                        {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': None, 'wwnn': None},
                                        ]}},
                   {'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'config1-group',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile_server2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:53', 'wwnn': '20:00:a0:b9:cc:1c:08:53'},
                                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:54', 'wwnn': '20:00:a0:b9:cc:1c:08:54'},
                                                           {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_3', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '208000C0FF25B079', 'lun': '0'}]}, 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_4', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '237000C0FF25B079', 'lun': '0'}]}, 'mac': None, 'wwpn': None, 'wwnn': None}]
                                           }}]

multiple_server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'config1-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'connectionSettings': {
                                 'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:51', 'wwnn': '20:00:a0:b9:cc:1c:08:51'},
                                                 {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': None, 'wwnn': None}
                                                 ]}},
                            {'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 2',
                             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'config1-group',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'Profile_server2', 'description': '', 'affinity': 'Bay',
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': '10:00:a0:b9:cc:1c:08:53', 'wwnn': '20:00:a0:b9:cc:1c:08:53'},
                                                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:FA_3', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '208000C0FF25B079', 'lun': '0'}]}, 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                    ]
                                                    }}]

Disable_uplinkPort = {'associatedUplinkSetUri': ' ',
                      'interconnectName': ' ',
                      'portType': 'Uplink',
                      'portId': ' ',
                      'portHealthStatus': 'Warning',
                      'capability': ['FibreChannel'],
                      'configPortTypes': ['FibreChannel'],
                      'enabled': '',
                      'portName': ' ',
                                 'portStatus': 'Unknown',
                      'type': 'portV5'}


li_uplinkports_hill = ['Remove_uplink_ports_hill1', 'Remove_uplink_ports_hill2']
li_uplinkports_utah = ['Remove_uplink_ports_utah1', 'Remove_uplink_ports_utah2']

li_uplinksets = {
    'Remove_uplink_ports_hill1':
        {'name': 'us_hill1',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA_3'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
                 'fcMode': 'NA',
         'portConfigInfos': [],
         'logicalInterconnectUri': None},

    'Remove_uplink_ports_hill2':
        {'name': 'us_hill2',
         'ethernetNetworkType': 'NotApplicable',
         'networkType': 'FibreChannel',
         'networkUris': [],
         'fcNetworkUris': ['FA_4'],
         'fcoeNetworkUris': [],
         'manualLoginRedistributionState': 'Supported',
         'connectionMode': 'Auto',
                 'fcMode': 'NONE',
         'portConfigInfos': [{'bay': '6', 'enclosure': ENC1, 'port': '2', 'desiredSpeed': 'Auto'},
                             {'bay': '6', 'enclosure': ENC1, 'port': '3', 'desiredSpeed': 'Auto'}],
         'logicalInterconnectUri': None},

        'Remove_uplink_ports_utah1':
    {'name': 'us_1',
            'ethernetNetworkType': 'NotApplicable',
            'networkType': 'FibreChannel',
            'networkUris': [],
            'fcNetworkUris': ['FA_1'],
            'fcoeNetworkUris': [],
            'manualLoginRedistributionState': 'Supported',
            'connectionMode': 'Auto',
            'portConfigInfos': [],
            'logicalInterconnectUri': None},

    'Remove_uplink_ports_utah2':
    {'name': 'us_2',
            'ethernetNetworkType': 'NotApplicable',
            'networkType': 'FibreChannel',
            'networkUris': [],
            'fcNetworkUris': ['FA_2'],
            'fcoeNetworkUris': [],
            'manualLoginRedistributionState': 'Supported',
            'connectionMode': 'Auto',
            'portConfigInfos': [{'bay': '4', 'enclosure': ENC1, 'port': '1', 'desiredSpeed': 'Auto'}],
            'logicalInterconnectUri': None}
}


# suite 2 data variables #
DEVICE = 'IOM'
# interconnect power off & on
power_state_value = ['poweroff', 'poweron']
# Firmware upgrade and downgrade to 4.10 uri
fw_uri_410 = '/rest/firmware-drivers/bp-2018-03-29-01'
# Firmware upgrade and downgrade to 4.00 uri
fw_uri_400 = '/rest/firmware-drivers/Custom_4x'
# Firmware upgrade and downgrade to 3.08 uri
fw_uri_308 = '/rest/firmware-drivers/SPP2017070_2017_0608_153'
# Firmware upgrade and downgrade to 3.05 uri
fw_uri_305 = '/rest/firmware-drivers/SPPgen9snap6_2016_0825_153'
# Firmware upgrade to 5.00 uri
fw_uri_500 = '/rest/firmware-drivers/Custom_5x'
Uplink_ports_hill = [['1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3']]  # Suite 2###
liupdate_body = {"sppUri": ' ', "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel", "ethernetActivationDelay": "0", "fcActivationType": "Parallel", "fcActivationDelay": "0", "validationType": "None"}
# Efuse off/on hill and utah bays
ACTION = ['OFF', 'ON']

trunkmaster_value = ['True', 'False']
downlink_value = ['None', '0']
# To check version hill and utah bays in 3.08
firmwareVersion_308 = '3.08'
# To check version hill and utah bays in 3.05
firmwareVersion_305 = '3.05'
# To check version hill and utah bays in 4.10
firmwareVersion_410 = ['4.10', '3.09']
# To check version hill and utah bays in 4.00
firmwareVersion_400 = ['4.00', '3.08']
# To check version hill and utah bays in 5.00
firmwareVersion_500 = ['5.00', '3.09']
# OA credential for efuse Hill and utah bays
OA_USER = 'Administrator'
OA_PASS = 'compaq'
# oa_details = {'oa_ip': ENCLOSURE_IP, 'username': 'Administrator', 'password': 'compaq'}
