from common_data import *

APPLIANCE_HOSTNAME = 'ovst06-ov.vse.rdlabs.hpecorp.net'
APPLIANCE_IPV4_ADDRESS = '16.114.217.105'

appliance = {
    'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
    'applianceNetworks': [
        {'device': 'eth0',
         'macAddress': None,
         'interfaceName': 'SynergyUPT',
         'activeNode': '1',
         'unconfigure': False,
         'ipv4Type': 'STATIC',
         'ipv4Subnet': '255.255.240.0',
         'ipv4Gateway': '16.114.208.1',
         'ipv4NameServers': ['16.114.208.11'],
         'app1Ipv4Addr': APPLIANCE_IPV4_ADDRESS,
         'ipv6Type': 'UNCONFIGURE',
         'hostname': APPLIANCE_HOSTNAME,
         'confOneNode': True,
         'domainName': 'vse.rdlabs.hpecorp.net',
         'aliasDisabled': True, }]
}

ligs_attributes = [
    {'name': 'LIG_POTASH',
     'enclosureIndexes': [1, 2],
     'interconnectBaySet': 3,
     'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                 {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                 {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                 {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
                                 ],
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [uplinksets[0].copy(), uplinksets[1].copy(), uplinksets[2].copy()]
     },
    {'name': 'LIG_CARBON',
     'enclosureIndexes': [-1],
     'interconnectBaySet': 1,
     'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                 {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
     'redundancyType': 'Redundant',
     'uplinkSets': [uplinksets[3].copy(), uplinksets[4].copy()]
     },
]

ligs = map(build_lig, ligs_attributes)

expected_ligs = map(build_expected_lig, ligs)

sas_ligs_attributes = [
    {'name': 'SASLIG',
     'enclosureIndexes': [1],
     'interconnectBaySet': 1,
     'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                                 {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1}]}
]

sas_ligs = map(build_sas_lig, sas_ligs_attributes)

expected_sas_ligs = map(build_expected_sas_lig, sas_ligs)

enclosure_groups_attributes = [
    {'name': 'EG_RING6',
     'configurationScript': '',
     'enclosureCount': 2,
     'interconnectBayMappings': [
         {'enclosureIndex': 1, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:' + sas_ligs[0]['name']},
         {'enclosureIndex': 1, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:' + sas_ligs[0]['name']},
         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']},
         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']},
         {'enclosureIndex': 2, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + ligs[1]['name']},
         {'enclosureIndex': 2, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + ligs[1]['name']}],
     'interconnectBayMappingCount': 6}
]

enclosure_groups = map(build_enclosure_group, enclosure_groups_attributes)

expected_enclosure_groups = map(build_expected_enclosure_group, enclosure_groups)

enclosures_attributes = [
    {
        'name': 'MXQ645027K',
        'eg': enclosure_groups[0]['name'],
        'servers': [
            {'name': 'MXQ645027K, bay 1'},
            {'name': 'MXQ645027K, bay 2'},
            {'name': 'MXQ645027K, bay 5'},
            {'name': 'MXQ645027K, bay 7'},
            {'name': 'MXQ645027K, bay 8'},  # Gen10
            {'name': 'MXQ645027K, bay 9'},  # Gen10
            {'name': 'MXQ645027K, bay 10'},  # Gen10
        ],
        'interconnects': [{'name': 'MXQ645027K, interconnect 3', 'linked_ports': ['d1', 'd2', 'd5', 'd7', 'd8', 'd9', 'd10', 'd13', 'd14', 'd17', 'd18', 'd19', 'd20', 'd21', 'd23', 'Q1:1', 'Q4:1', 'Q7', 'Q8', 'l1', 'l4']},
                          {'name': 'MXQ645027K, interconnect 6', 'linked_ports': ['d1', 'd2', 'd5', 'd7', 'd8', 'd9', 'd10', 'l1', 'l2']},
                          ]
    },
    {
        'name': 'MXQ6450369',
        'eg': enclosure_groups[0]['name'],
        'servers': [
            {'name': 'MXQ6450369, bay 1'},
            {'name': 'MXQ6450369, bay 2'},
            #  {'name': 'MXQ6450369, bay 3'},  Missing 1 more proc and Mezz1/3
            {'name': 'MXQ6450369, bay 5'},
            {'name': 'MXQ6450369, bay 6'},
            {'name': 'MXQ6450369, bay 7'},  # Gen10
            {'name': 'MXQ6450369, bay 8'},  # Gen10
        ],
        'interconnects': [{'name': 'MXQ6450369, interconnect 3', "linked_ports": ['d1', 'd2', 'd5', 'd6', 'd7', 'd8', 'd9', 'd11', 'l1', 'l2']},
                          {'name': 'MXQ6450369, interconnect 6', "linked_ports": ['d1', 'd2', 'd5', 'd6', 'd7', 'd8', 'd9', 'd11', 'd13', 'd14', 'd17', 'd19', 'd20', 'd21', 'd22', 'Q1:1', 'Q4:1', 'Q7', 'Q8', 'l1', 'l4']},
                          ]
    }
]

logical_enclosures_attributes = [
    {'name': 'LE_RING6',
     'enclosureUris': ['ENC:' + enclosures_attributes[0]['name'], 'ENC:' + enclosures_attributes[1]['name']],
     'enclosureGroupUri': 'EG:' + enclosure_groups_attributes[0]['name']}
]

logical_enclosures = map(build_logical_enclosure, logical_enclosures_attributes)

expected_logical_enclosures = map(build_expected_logical_enclosure, logical_enclosures)

# Group1 top enclosure
group1_servers_attributes = [
    {'name': enclosures_attributes[0]['servers'][0]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][1]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][2]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][3]['name'], 'eg': enclosures_attributes[0]['eg']},
]

# Group2 bottom enclosure
group2_servers_attributes = [
    {'name': enclosures_attributes[1]['servers'][0]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[1]['servers'][1]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[1]['servers'][2]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[1]['servers'][3]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[1]['servers'][4]['name'], 'eg': enclosures_attributes[0]['eg']},
    # {'name': enclosures_attributes[1]['servers'][5]['name'], 'eg': enclosures_attributes[0]['eg']},
    # {'name': enclosures_attributes[1]['servers'][6]['name'], 'eg': enclosures_attributes[0]['eg']},
]

# Group3 top enclosure Gen10 Blades
group3_servers_attributes = [
    {'name': enclosures_attributes[0]['servers'][4]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][5]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][6]['name'], 'eg': enclosures_attributes[0]['eg']},
]

group1_profiles_attributes = map(build_profile_attributes, group1_servers_attributes)

group2_profiles_attributes = map(build_profile_attributes, group2_servers_attributes)

group3_profiles_attributes = map(build_profile_attributes, group3_servers_attributes)

profiles_attributes = group1_profiles_attributes + group2_profiles_attributes + group3_profiles_attributes

storeserv_volumes = map(build_storeserv_volume, map(lambda d: d['volumes'][0], profiles_attributes))

storevirtual_volumes = map(build_storevirtual_volume, map(lambda d: d['volumes'][1], profiles_attributes))

storage_volumes = storeserv_volumes + storevirtual_volumes

expected_storage_volumes = map(build_expected_storage_volume, storage_volumes)

group1_profiles = map(build_group1_profile, group1_profiles_attributes)

group2_profiles = map(build_group2_profile, group2_profiles_attributes)

group3_profiles = map(build_group3_profile, group3_profiles_attributes)

all_profiles = group1_profiles + group2_profiles + group3_profiles

expected_group1_profiles = map(build_expected_group1_profile, group1_profiles_attributes)

expected_group2_profiles = map(build_expected_group2_profile, group2_profiles_attributes)

expected_group3_profiles = map(build_expected_group3_profile, group3_profiles_attributes)

expected_all_profiles = expected_group1_profiles + expected_group2_profiles + expected_group3_profiles

preupdate_profiles = [group1_profiles[0].copy(), group2_profiles[0].copy(), group3_profiles[0].copy()]

expected_preupdate_profiles = [expected_group1_profiles[0], expected_group2_profiles[0], expected_group3_profiles[0]]

# Cleaup
cleanup_storeserv_volumes = map(lambda d: d['properties']['name'], storage_volumes)

cleanup_storeserv_hosts = map(lambda d: d['name'], profiles_attributes)


# Upgrade loop
upt_hops_profiles = [
    {'pre_existing_profiles': expected_preupdate_profiles,
     'new_profiles': [group1_profiles[1].copy(), group2_profiles[1].copy(), group3_profiles[1].copy()]},
    {'pre_existing_profiles': expected_preupdate_profiles + [expected_group1_profiles[1], expected_group2_profiles[1], expected_group3_profiles[1]],
     'new_profiles': [group1_profiles[2].copy(), group2_profiles[2].copy(), group3_profiles[2].copy()]},
    {'pre_existing_profiles': expected_preupdate_profiles + [expected_group1_profiles[1], expected_group2_profiles[1], expected_group3_profiles[1], expected_group1_profiles[2], expected_group2_profiles[2], expected_group3_profiles[2]],
     'new_profiles': [group1_profiles[3].copy(), group2_profiles[3].copy()]},
]
