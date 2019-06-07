##############################################################

# These conditions are based on resource manager and are predefined by the users.
# Example below: name- would be the name of OneView's resource, then followed by
# the conditions. For server profile resource, it has a few conditions such as
# applying a profile with no connections(connectionless) takes about 30000 milliseconds(30 seconds)
# to complete, while a profile with firmware takes 400000 milliseconds. Listener will use
# these predefined conditions to determine the asynchronous performance results.

# {name: <resource>, <conditions>: <time_to_complete_async_task>}
##############################################################


conditions = [{'name': 'server profiles', 'connectionless': 30000, 'gen8_connections_only': 30000, 'connections_only': 30000, 'local_storage': 400000, 'firmware': 1200000, 'everything': 1200000, 'BIOS': 1200000, '2eth': 60000, '4eth': 65000, 'isci': 65000, 'jbods': 240000, 'hw_iscsi': 120000, 'iscsi_managed_volume': 120000, 'gen8_firmware': 2700000, 'gen9_firmware': 2700000, 'gen10_firmware': 2700000, 'firmware_ls': 4000000, 'local_storage': 1800000},
              {'name': 'enclosure', 'single': 24000},
              {'name': 'server hardware', 'single': 6000},
              {'name': 'lig', 'SE_SLI_3US_ETH_FC_FCOE ': 60000, 'dual': 120000},
              {'name': 'ethernet network', 'multi': 14000},
              {'name': 'logical enclosures', '1K_1Kum_1Serv': 108000000, '3encl': 2640000},
              {'name': 'license', 'add': 10000, 'remove': 10000, 'get': 1000},
              {'name': 'fc Network', 'multi': 14000},
              {'name': 'refresh enclosure', '1K_1Kum_1Serv': 54000000},
              {'name': 'fcoe Network', 'single': 14000},
              {'name': 'networks', 'multi': 40000},
              {'name': 'li', 'single': 400000},
              {'name': 'logical interconnect', 'single': 400000},
              {'name': 'enclosure group', '1K_1Kum_1Serv': 60000},
              {'name': 'update from group', 'single': 400000},
              {'name': 'sas_interconnects', 'reset': 400000, 'power': 400000},
              {'name': 'drive_enclosures', 'reset': 400000, 'power': 400000},
              {'name': 'gen10', 'BIOS': 900000}
              ]
