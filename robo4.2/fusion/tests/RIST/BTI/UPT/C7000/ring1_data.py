from common_data import *

# FTS
APPLIANCE_HOSTNAME = 'wpst35-ov.vse.rdlabs.hpecorp.net'
appliance = {
    'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
    'applianceNetworks': [
        {'device': 'eth0',
         'macAddress': None,
         'interfaceName': 'Appliance',
         'activeNode': '1',
         'unconfigure': False,
         'ipv4Type': 'STATIC',
         'app1Ipv4Addr': '',
         'ipv6Type': 'UNCONFIGURE',
         'ipv4Subnet': '255.255.240.0',
         'ipv4Gateway': '16.114.208.1',
         'hostname': APPLIANCE_HOSTNAME,
         'confOneNode': True,
         'domainName': 'vse.rdlabs.hpecorp.net',
         'ipv4NameServers': ['16.125.25.81', '16.125.25.82', '16.125.24.20'],
         'aliasDisabled': False}
    ]
}

# LIG
ligs_attributes = [
    {'name': 'LIG35',
     'interconnectMapTemplate': [
         {'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
         {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 1, 'type': 'HP VC Flex-10 Enet Module', 'enclosureIndex': 1},
         {'bay': 4, 'enclosure': 1, 'type': 'HP VC Flex-10 Enet Module', 'enclosureIndex': 1},
         {'bay': 5, 'enclosure': 1, 'type': 'HP VC 8Gb 20-Port FC Module', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'HP VC 8Gb 20-Port FC Module', 'enclosureIndex': 1}]},
]

ligs = map(build_lig, ligs_attributes)

expected_ligs = map(build_expected_lig, ligs)

# EG
enclosure_groups_attributes = [
    {
        'name': 'EG35',
        'interconnectBayMappings': [
            {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + ligs[0]['name']}],
        'interconnectBayMappingCount': 6,
    }
]

enclosure_groups = map(build_enclosure_group, enclosure_groups_attributes)

expected_enclosure_groups = map(build_expected_enclosure_group, enclosure_groups)

# Enclosure
enclosures_attributes = [
    {
        'name': 'wpst35',
        'hostname': 'wpst35-oa1.vse.rdlabs.hpecorp.net',
        'oa': 'wpst35-oa1.vse.rdlabs.hpecorp.net',
        'eg': enclosure_groups[0]['name'],
        'servers': [
            {'name': 'wpst35, bay 1'},  # Gen8
            {'name': 'wpst35, bay 2'},  # Gen8
            {'name': 'wpst35, bay 8'},  # Gen8
            {'name': 'wpst35, bay 3'},  # Gen9
            {'name': 'wpst35, bay 7'},  # Gen9
            {'name': 'wpst35, bay 10'},  # Gen9
            {'name': 'wpst35, bay 11'},  # Gen9
        ],
        'interconnects': [{'name': 'wpst35, interconnect 1', 'linked_ports': ['d1', 'd2', 'd3', 'd7', 'd8', 'd9', 'd10', 'd11', 'd15', 'd16', 'X6', 'X7', 'X8']},
                          {'name': 'wpst35, interconnect 2', 'linked_ports': ['d1', 'd2', 'd3', 'd7', 'd8', 'd9', 'd10', 'd11', 'd15', 'd16', 'X6', 'X7', 'X8']},
                          {'name': 'wpst35, interconnect 3', 'linked_ports': ['d1', 'd2', 'd3', 'd7', 'd8', 'd11', 'X7', 'X8']},
                          {'name': 'wpst35, interconnect 4', 'linked_ports': ['d1', 'd2', 'd3', 'd7', 'd8', 'd11', 'X7', 'X8']},
                          {'name': 'wpst35, interconnect 5', 'linked_ports': ['1']},
                          {'name': 'wpst35, interconnect 6', 'linked_ports': ['1']},
                          ]
    }
]

enclosures = map(build_enclosure, enclosures_attributes)

expected_enclosures = map(build_expected_enclosure, enclosures_attributes)

# Group2 Gen8
group1_servers_attributes = [
    {'name': enclosures_attributes[0]['servers'][0]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][1]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][2]['name'], 'eg': enclosures_attributes[0]['eg']},
]

# Group2 Gen9
group2_servers_attributes = [
    {'name': enclosures_attributes[0]['servers'][3]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][4]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][5]['name'], 'eg': enclosures_attributes[0]['eg']},
    {'name': enclosures_attributes[0]['servers'][6]['name'], 'eg': enclosures_attributes[0]['eg']},
]

group1_profiles_attributes = map(build_profile_attributes, group1_servers_attributes)

group2_profiles_attributes = map(build_profile_attributes, group2_servers_attributes)

profiles_attributes = group1_profiles_attributes + group2_profiles_attributes

storeserv_volumes = map(build_storeserv_volume, map(lambda d: d['volumes'][0], profiles_attributes))

storevirtual_volumes = map(build_storevirtual_volume, map(lambda d: d['volumes'][1], profiles_attributes))

storage_volumes = storeserv_volumes + storevirtual_volumes

expected_storage_volumes = map(build_expected_storage_volume, storage_volumes)

group1_profiles = map(build_group1_profile, group1_profiles_attributes)

group2_profiles = map(build_group2_profile, group2_profiles_attributes)

all_profiles = group1_profiles + group2_profiles

expected_group1_profiles = map(build_expected_group1_profile, group1_profiles_attributes)

expected_group2_profiles = map(build_expected_group2_profile, group2_profiles_attributes)

expected_all_profiles = expected_group1_profiles + expected_group2_profiles

preupdate_profiles = [group1_profiles[0].copy(), group2_profiles[0].copy()]

expected_preupdate_profiles = [expected_group1_profiles[0], expected_group2_profiles[0]]

# Cleaup
cleanup_storeserv_volumes = map(lambda d: d['properties']['name'], storage_volumes)

cleanup_storeserv_hosts = map(lambda d: d['name'], profiles_attributes)

cleanup_oas = map(lambda d: d['oa'], enclosures_attributes)

# Upgrade loop
upt_hops_profiles = [
    {'pre_existing_profiles': expected_preupdate_profiles,
     'new_profiles': [group1_profiles[1].copy()]},
    {'pre_existing_profiles': expected_preupdate_profiles + [expected_group1_profiles[1]],
     'new_profiles': [group2_profiles[1].copy()]},
    {'pre_existing_profiles': expected_preupdate_profiles + [expected_group1_profiles[1], expected_group2_profiles[1]],
     'new_profiles': [group1_profiles[2].copy()]},
    {'pre_existing_profiles': expected_preupdate_profiles + [expected_group1_profiles[1], expected_group2_profiles[1], expected_group1_profiles[2]],
     'new_profiles': [group2_profiles[2].copy()]},
    {'pre_existing_profiles': expected_preupdate_profiles + [expected_group1_profiles[1], expected_group2_profiles[1], expected_group1_profiles[2], expected_group2_profiles[2]],
     'new_profiles':[group2_profiles[3].copy()]},
]
