import os
import sys
sys.path.append(os.path.dirname(__file__))

ENC_1  = 'CN7544044G'
ENC_2  = 'CN7545084V'
ENC_3  = 'CN7545084B'

ENC_4  = 'CN7545061R'
ENC_5  = 'CN7544044D'
		
# Interconnect bays configurations for valid CL10 configurations
# Maximum configuration of 5 enclosures possible.
# CL10 are in fabric 3
###

###
# 1 Enclosure
###
Enc1Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
        ]

###
# 2 Enclosures
###
Enc2Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
        ]
				
###
# 3 Enclosures
###
Enc3Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
        ]
		
###
# 4 Enclosures
###
Enc4Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
         {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
        ]
		
###
# 5 Enclosures
###
Enc5Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
         {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
         {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
         {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
        ]
		
###
# 2 Enclosures for unmanaged state putting bay 6 in Unmanaged state
###
UnmanagedEnc2Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
        ]
				
###
# 3 Enclosures for unmanaged state putting bay 6 in Unmanaged state
###
UnmanagedEnc3Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
        ]
		
###
# 4 Enclosures for unmanaged state putting bay 6 in Unmanaged state
###
UnmanagedEnc4Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
         {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
        ]
		
###
# 5 Enclosures for unmanaged state putting bay 6 in Unmanaged state
###
UnmanagedEnc5Map = \
        [
		 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
         {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
         {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
         {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
        ]
		
lig_uplink_set = {
		'name': 'US1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork1','wpstnetwork2','wpstnetwork3', 'wpstnetwork4','wpstnetwork5'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
        ]
    }
	
###
# LIGs for all 1, 2, 3, 4 and 5 enclosure set ups in one or two fabric mode using CL10 and CL20
###	   
ligs = {
      'Enc1-LIG':
            {'name': 'Enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc1Map,
             'enclosureIndexes': [1],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },
        'Enc2-LIG':
            {'name': 'Enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [1, 2],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },			
        'Enc3-LIG':
            {'name': 'Enc3-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc3Map,
             'enclosureIndexes': [1, 2, 3],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },
        'Enc4-LIG':
            {'name': 'Enc4-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc4Map,
             'enclosureIndexes': [1, 2, 3, 4],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
           },
        'Enc5-LIG':
            {'name': 'Enc5-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc5Map,
             'enclosureIndexes': [1, 2, 3, 4, 5],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },
	   }
	   
unmanaged_ligs = {
        'Enc2-LIG':
            {'name': 'Enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2MapUnmanaged,
             'enclosureIndexes': [1, 2],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },
        'Enc3-LIG':
            {'name': 'Enc3-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc3MapUnmanaged,
             'enclosureIndexes': [1, 2, 3],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },
		'Enc4-LIG':
            {'name': 'Enc4-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc4MapUnmanaged,
             'enclosureIndexes': [1, 2, 3, 4],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
           },
        'Enc5-LIG':
            {'name': 'Enc5-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc5MapUnmanaged,
             'enclosureIndexes': [1, 2, 3, 4, 5],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },
	   }
	   }
	   
enc_groups = {
            'Enc2-EG':
                {'name': 'Enc2-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 2,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
            'Enc3-EG':
                {'name': 'Enc3-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 3,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
            'Enc4-EG':
                {'name': 'Enc4-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 4,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
            'Enc5-EG':
                {'name': 'Enc5-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 5,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
			}
###
# All logical enclosures
###
les = { 
		'Enc1-LE':
			{'name': 'Enc1-LE',
			 'enclosureUris': [ENC_1],
			 'enclosureGroupUri': 'Enc1-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc2-LE':
			{'name': 'Enc2-LE',
			 'enclosureUris': [ENC_1, ENC_2],
			 'enclosureGroupUri': 'Enc2-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc3-LE':
			{'name': 'Enc3-LE',
			 'enclosureUris': [ENC_1, ENC_2, ENC_3],
			 'enclosureGroupUri': 'Enc3-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc4-LE':
			{'name': 'Enc4-LE',
			 'enclosureUris': [ENC_1, ENC_2, ENC_3, ENC_4],
			 'enclosureGroupUri': 'Enc4-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc5-LE':
			{'name': 'Enc5-LE',
			 'enclosureUris': [ENC_1, ENC_2, ENC_3, ENC_4, ENC_5],
			 'enclosureGroupUri': 'Enc5-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			}
	  } 
	
	
lig_add_uplinkset = {
		'name': 'add_uplinkset',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork6','wpstnetwork7','wpstnetwork8'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}
        ]
    }

lig_edit_uplinkset = {
		'name': 'US1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork1','wpstnetwork2','wpstnetwork3'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}
        ]
    }
	
li_add_uplinkset = {
		'name': 'add_uplinkset',
		'type': 'uplink-setV300',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork6','wpstnetwork7','wpstnetwork8'],
		'manualLoginRedistributionState': 'NotSupported',
        'connectionMode': 'Auto',
		'portConfigInfos': [
			{'desiredSpeed': 'Auto',
				'location': {
					'locationEntries': [
						{
							'value': 'Q1',
							'type': 'Port'
						},
						{
							'value': '3',
							'type': 'Bay'
						},
						{
							'value': ENC_1,
							'type': 'Enclosure'
						}
					]
				}
			},
			{'desiredSpeed': 'Auto',
				'location': {
					'locationEntries': [
						{
							'value': 'Q1',
							'type': 'Port'
						},
						{
							'value': '6',
							'type': 'Bay'
						},
						{
							'value': ENC_2,
							'type': 'Enclosure'
						}
					]
				}
			}
		],
		'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
    }
	
li_edit_uplinkset = {
		'name': 'US1',
		'type': 'uplink-setV300',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork1','wpstnetwork2','wpstnetwork3'],
		'manualLoginRedistributionState': 'NotSupported',
        'lacpTimer': 'Long',
        'connectionMode': 'Auto',
		'portConfigInfos': [
			{'desiredSpeed': 'Auto',
				'location': {
					'locationEntries': [
						{
							'value': 'Q1',
							'type': 'Port'
						},
						{
							'value': '3',
							'type': 'Bay'
						},
						{
							'value': ENC_1,
							'type': 'Enclosure'
						}
					]
				}
			},
			{'desiredSpeed': 'Auto',
				'location': {
					'locationEntries': [
						{
							'value': 'Q1',
							'type': 'Port'
						},
						{
							'value': '6',
							'type': 'Bay'
						},
						{
							'value': ENC_2,
							'type': 'Enclosure'
						}
					]
				}
			}
		],
		'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
    }


		
###
# LIGs for all 1, 2, 3, 4 and 5 enclosure setups in one or two fabric mode using CL10 and CL20
###
ligs = {
        'Enc2-LIG':
            {'name': 'Enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [1, 2],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },			
        'Enc3-LIG':
            {'name': 'Enc3-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc3Map,
             'enclosureIndexes': [1, 2, 3],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },
        'Enc4-LIG':
            {'name': 'Enc4-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc4Map,
             'enclosureIndexes': [1, 2, 3, 4],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
           },
        'Enc5-LIG':
            {'name': 'Enc5-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc5Map,
             'enclosureIndexes': [1, 2, 3, 4, 5],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [lig_uplink_set],
            },

	   }
	
telemetry = { 
			 'type': 'telemetry-configuration',
			 'enableTelemetry': False,
			 'sampleInterval': 200,
			 'sampleCount': 20
			}
			
ethernet_setting = { 
			 'type': 'EthernetInterconnectSettingsV201',
			 'enableFastMacCacheFailover': False,
			 'enableIgmpSnooping': False,
			 'enableNetworkLoopProtection': False,
			 'igmpIdleTimeoutInterval': 130,
			 'macRefreshInterval': 10
		}
	
editligs = {
        'Enc2-LIG': {
			'telemetry' : 
						{	'name': 'Enc2-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc2Map,
							'enclosureIndexes': [1, 2],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set],
							'telemetryConfiguration': telemetry,
						},
			'ethernetSettings' :
						{	'name': 'Enc2-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc2Map,
							'enclosureIndexes': [1, 2],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set],
							'ethernetSettings': ethernet_setting,
						},
			'add_uplinkset' :
						{	'name': 'Enc2-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc2Map,
							'enclosureIndexes': [1, 2],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set, lig_add_uplinkset],
						},
			'delete_uplinkset' :
						{	'name': 'Enc2-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc2Map,
							'enclosureIndexes': [1, 2],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set],
						},
			'edit_uplinkset' :
						{	'name': 'Enc2-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc2Map,
							'enclosureIndexes': [1, 2],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_edit_uplinkset],
						}
		},
        'Enc3-LIG': {
			'telemetry' : 
						{	'name': 'Enc3-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc3Map,
							'enclosureIndexes': [1, 2, 3],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set],
							'telemetryConfiguration': telemetry,
						},
			'ethernetSettings' :
						{	'name': 'Enc3-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc3Map,
							'enclosureIndexes': [1, 2, 3],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set],
							'ethernetSettings': ethernet_setting,
						},
			'add_uplinkset' :
						{	'name': 'Enc3-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc3Map,
							'enclosureIndexes': [1, 2, 3],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set, lig_add_uplinkset],
						},
			'delete_uplinkset' :
						{	'name': 'Enc3-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc3Map,
							'enclosureIndexes': [1, 2, 3],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_uplink_set],
						},
			'edit_uplinkset' :
						{	'name': 'Enc3-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc3Map,
							'enclosureIndexes': [1, 2, 3],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [lig_edit_uplinkset],
						}
		}
	}

enc_group = {
            'Enc2-EG':
                {'name': 'Enc2-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 2,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
            'Enc3-EG':
                {'name': 'Enc3-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 3,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
            'Enc4-EG':
                {'name': 'Enc4-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 4,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
            'Enc5-EG':
                {'name': 'Enc5-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 5,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
			}
	
###
# All logical enclosures
###
les = { 
		'Enc2-LE':
			{'name': 'Enc2-LE',
			 'enclosureUris': [ENC_1, ENC_2],
			 'enclosureGroupUri': 'Enc2-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc3-LE':
			{'name': 'Enc3-LE',
			 'enclosureUris': [ENC_1, ENC_2, ENC_3],
			 'enclosureGroupUri': 'Enc3-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc4-LE':
			{'name': 'Enc4-LE',
			 'enclosureUris': [ENC_1, ENC_2, ENC_3, ENC_4],
			 'enclosureGroupUri': 'Enc4-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc5-LE':
			{'name': 'Enc5-LE',
			 'enclosureUris': [ENC_1, ENC_2, ENC_3, ENC_4, ENC_5],
			 'enclosureGroupUri': 'Enc5-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			}
	  } 

###
# Server profiles
###
profiles = {
	'Profile1': {
		'payload' : {
			'name': 'Profile1', 
			'type': 'ServerProfileV6', 
			'serverHardwareUri': ENC_1 + ', bay 1',
			'enclosureUri': ENC_1, 
			'enclosureGroupUri': None, 
			'connections':[ 
						{	'name': 'conn',
							'functionType': 'Ethernet', 
							'portId': 'Auto', 
							'networkUri': 'wpstnetwork1', 
						}
            ]
		},
		'IP':'15.245.132.49',
		'handle':None
	},
	'Profile2': {
		'payload' : {
			'name': 'Profile2', 
			'type': 'ServerProfileV6', 
			'serverHardwareUri': ENC_2 + ', bay 1',
			'enclosureUri': ENC_2, 
			'enclosureGroupUri': None, 
			'connections':[ 
						{	'name': 'conn',
							'functionType': 'Ethernet', 
							'portId': 'Auto', 
							'networkUri': 'wpstnetwork3', 
						}
            ]
		},
		'IP':'15.199.234.43',
		'handle':None
	},
	'Profile3': {
		'payload' : {
			'name': 'Profile3', 
			'type': 'ServerProfileV6', 
			'serverHardwareUri': ENC_3 + ', bay 1',
			'enclosureUri': ENC_3, 
			'enclosureGroupUri': None, 
			'connections':[ 
						{	'name': 'conn',
							'functionType': 'Ethernet', 
							'portId': 'Auto', 
							'networkUri': 'wpstnetwork2', 
						}
            ]
		},
		'IP':'15.199.234.43',
		'handle':None
	},
	'Profile4': {
		'payload' : {
			'name': 'Profile4', 
			'type': 'ServerProfileV6', 
			'serverHardwareUri': ENC_1 + ', bay 2',
			'enclosureUri': ENC_1, 
			'enclosureGroupUri': None, 
			'connections':[ 
						{	'name': 'conn',
							'functionType': 'Ethernet', 
							'portId': 'Auto', 
							'networkUri': 'wpstnetwork4', 
						}
            ]
		},
		'IP':'15.199.234.43',
		'handle':None
	}
}