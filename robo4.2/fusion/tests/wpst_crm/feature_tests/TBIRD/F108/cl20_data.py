import os
import sys
sys.path.append(os.path.dirname(__file__))

enc1  = 'CN7544044G'
enc2  = 'CN7545084V'
enc3  = 'CN7545084B'

###
# Interconnect bays configurations for valid CL20 configurations
# Maximum configuration of 3 enclosures possible.
# CL20 are in fabric 2
###

###
# 1 Enclosure
###

Enc1Map = \
        [
		 {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
        ]

###
# 2 Enclosures
###
Enc2Map = \
        [
		 {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
        ]
				
###
# 3 Enclosures
###
Enc3Map = \
        [
		 {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 2, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 5, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
        ]
		
###
# 2 Enclosures which will put bay 5 CL to Unmanaged state
###
UnmanagedEnc2Map = \
        [
		 {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 5, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
        ]
				
###
# 3 Enclosures which will put bay 5 CL to Unmanaged state
###
UnmanagedEnc3Map = \
        [
		 {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 5, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
        ]

default_lig_uplink_set = {
		'name': 'US1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['wpstnetwork1','wpstnetwork2','wpstnetwork3', 'wpstnetwork4','wpstnetwork5'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '5', 'port': 'Q6', 'speed': 'Auto'}
        ]
    }
	
###
# LIGs for all 1, 2 and 3
###
ligs = {
       'enc1-LIG':
            {'name': 'enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc1Map,
             'enclosureIndexes': [1],
             'interconnectBaySet': 2,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [default_lig_uplink_set],
            },
        'enc2-LIG':
            {'name': 'enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc2Map,
             'enclosureIndexes': [1, 2],
             'interconnectBaySet': 2,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [default_lig_uplink_set],
            },
        'enc3-LIG':
            {'name': 'enc3-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': Enc3Map,
             'enclosureIndexes': [1, 2, 3],
             'interconnectBaySet': 2,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [default_lig_uplink_set],
            },
	   }
	   
unmanaged_ligs = {
        'enc2-LIG':
            {'name': 'enc2-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': UnmanagedEnc2Map,
             'enclosureIndexes': [1, 2],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [default_lig_uplink_set],
            },
        'enc3-LIG':
            {'name': 'enc3-LIG',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': UnmanagedEnc3Map,
             'enclosureIndexes': [1, 2, 3],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'uplinkSets': [default_lig_uplink_set],
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
	
enc_group = {
           'Enc1-EG':
                {'name': 'Enc2-EG',
                   'type': 'EnclosureGroupV300',
                   'enclosureCount': 1,
                   'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                   'stackingMode': 'Enclosure',
                   'interconnectBayMappingCount': 6,
                   'configurationScript': None,
                   'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
                   'ipAddressingMode': "External",
                   'ipRangeUris': [],
                   'powerMode': "RedundantPowerFeed"
                },
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
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
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
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
                        {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
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
			 'enclosureUris': [enc1],
			 'enclosureGroupUri': 'Enc1-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc2-LE':
			{'name': 'Enc2-LE',
			 'enclosureUris': [enc1, enc2],
			 'enclosureGroupUri': 'Enc2-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
		'Enc3-LE':
			{'name': 'Enc3-LE',
			 'enclosureUris': [enc1, enc2, enc3],
			 'enclosureGroupUri': 'Enc3-EG',
			 'firmwareBaselineUri': None,
			 'forceInstallFirmware': False
			},
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
							'value': enc1,
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
							'value': enc2,
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
							'value': enc1,
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
							'value':  enc2,
							'type': 'Enclosure'
						}
					]
				}
			}
		],
		'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
    }


		
#

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
							'uplinkSets': [default_lig_uplink_set],
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
							'uplinkSets': [default_lig_uplink_set],
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
							'uplinkSets': [default_lig_uplink_set, lig_add_uplinkset],
						},
			'delete_uplinkset' :
						{	'name': 'Enc2-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc2Map,
							'enclosureIndexes': [1, 2],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [default_lig_uplink_set],
						},
			'edit_uplinkset' :
						{	'name': 'Enc2-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc2Map,
							'enclosureIndexes': [1, 2],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [default_lig_uplink_set],
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
							'uplinkSets': [default_lig_uplink_set],
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
							'uplinkSets': [default_lig_uplink_set],
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
							'uplinkSets': [default_lig_uplink_set, lig_add_uplinkset],
						},
			'delete_uplinkset' :
						{	'name': 'Enc3-LIG',
							'type': 'logical-interconnect-groupV3',
							'enclosureType': 'SY12000',
							'interconnectMapTemplate': Enc3Map,
							'enclosureIndexes': [1, 2, 3],
							'interconnectBaySet': 3,
							'redundancyType': 'HighlyAvailable',
							'uplinkSets': [default_lig_uplink_set],
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

###
# Server profiles
###
profiles = {
	'Profile1': {
		'payload' : {
			'name': 'Profile1', 
			'type': 'ServerProfileV6', 
			'serverHardwareUri': enc1 + ', bay 1',
			'enclosureUri': enc1, 
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
			'serverHardwareUri':  enc2 + ', bay 1',
			'enclosureUri':  enc2, 
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
			'serverHardwareUri':  enc3 + ', bay 1',
			'enclosureUri':  enc3, 
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
			'serverHardwareUri': enc1 + ', bay 2',
			'enclosureUri': enc1, 
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