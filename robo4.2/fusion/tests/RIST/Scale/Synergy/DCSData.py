from dynamic_data import DynamicData

DD = DynamicData()

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

scaleuser_credentials = {'userName': 'scaleuser', 'password': 'Cosmos123'}

proxy_server = [{'type': 'ProxyServer', 'server': '10.0.0.94', 'port': '1080'}]

ENCLOSURE = [{'serialNumber': '0000A66101', 'scaleName': 'SCALE-01'},
             {'serialNumber': '0000A66102', 'scaleName': 'SCALE-02'},
             {'serialNumber': '0000A66103', 'scaleName': 'SCALE-03'}]

licenses = [{'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

spp_name = 'SPP2016100.2016_0920.172'
ftp_site = 'scalevcenter.vse.rdlabs.hpecorp.net'
ftp_site_path = 'firmware/garfsRC2/'
spp_local_dir = 'C:/SPP/'

users_name = [{'name': 'scaleuser', 'role': 'Infrastructure administrator'},
              {'name': 'backup', 'role': 'Backup administrator'},
              {'name': 'network', 'role': 'Network administrator'},
              {'name': 'server', 'role': 'Server administrator'},
              {'name': 'storage', 'role': 'Storage administrator'},
              {'name': 'software', 'role': 'Software administrator'}]

active_directory = [{'name': 'domain1002.net', 'baseDN': 'dc=dom1002,dc=net', 'user': 'Administrator', 'password': 'Cosmos123', 'directoryServerIpAddress': '10.2.0.11', 'directoryServerSSLPortNumber': '636',
                     'directoryServerCertificateBase64Data': '-----BEGIN CERTIFICATE-----\nMIIF4jCCBMqgAwIBAgIKcwVvUgAAAAAACjANBgkqhkiG9w0BAQUFADBKMRMwEQYKCZImiZPyLGQB\nGRYDbmV0MRcwFQYKCZImiZPyLGQBGRYHZG9tMTAwMjEaMBgGA1UEAxMRZG9tMTAwMi1EQzEwMDIt\nQ0EwHhcNMTYwMjE5MDU1MzIxWhcNMTcwMjE4MDU1MzIxWjAdMRswGQYDVQQDExJEQzEwMDIuZG9t\nMTAwMi5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCfkOLLFVFaiVZMRq28/yIb\nnmeatGpVuFPrG7x7xX2FnW4FQ+xzvK6KhNue0AaKsEFVF3kTedubypoCv5Iaj/HT2R5WcxrquHmy\n0eo3UR1Iph3SdfZpE5aFRIyX0yj9WDqokyK37fG1dFDC9CyD1Y/ZQ/0jyPsA2GZa1paVzuUCJH/B\ndmpNZ7Nqhqa6+fvuLT4xSPKfMeP34u6Q+v/w5JFLVUhalwQWY/hv/he5hzkAJHuySFItr6OkJ1R8\njm3hN0ijEZrwC3orznZRDqawBF2lNsU5U5CAX27JY5TCrjrMeZDGfhcpLd2gEeEOEVsh+se/aDWT\n2MG+7biZnB+mG+ALAgMBAAGjggL1MIIC8TAvBgkrBgEEAYI3FAIEIh4gAEQAbwBtAGEAaQBuAEMA\nbwBuAHQAcgBvAGwAbABlAHIwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMA4GA1UdDwEB\n/wQEAwIFoDB4BgkqhkiG9w0BCQ8EazBpMA4GCCqGSIb3DQMCAgIAgDAOBggqhkiG9w0DBAICAIAw\nCwYJYIZIAWUDBAEqMAsGCWCGSAFlAwQBLTALBglghkgBZQMEAQIwCwYJYIZIAWUDBAEFMAcGBSsO\nAwIHMAoGCCqGSIb3DQMHMD4GA1UdEQQ3MDWgHwYJKwYBBAGCNxkBoBIEEMUoXFY/B/NBkzMacpRZ\nnL2CEkRDMTAwMi5kb20xMDAyLm5ldDAdBgNVHQ4EFgQUKzAO4ED3oJ4zg6FI85l0wUgEkuQwHwYD\nVR0jBBgwFoAU3CtATzpyFss7F2bXDQ0qsVguXj8wgc4GA1UdHwSBxjCBwzCBwKCBvaCBuoaBt2xk\nYXA6Ly8vQ049ZG9tMTAwMi1EQzEwMDItQ0EsQ049REMxMDAyLENOPUNEUCxDTj1QdWJsaWMlMjBL\nZXklMjBTZXJ2aWNlcyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPWRvbTEwMDIsREM9\nbmV0P2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFzcz1jUkxEaXN0cmli\ndXRpb25Qb2ludDCBwwYIKwYBBQUHAQEEgbYwgbMwgbAGCCsGAQUFBzAChoGjbGRhcDovLy9DTj1k\nb20xMDAyLURDMTAwMi1DQSxDTj1BSUEsQ049UHVibGljJTIwS2V5JTIwU2VydmljZXMsQ049U2Vy\ndmljZXMsQ049Q29uZmlndXJhdGlvbixEQz1kb20xMDAyLERDPW5ldD9jQUNlcnRpZmljYXRlP2Jh\nc2U/b2JqZWN0Q2xhc3M9Y2VydGlmaWNhdGlvbkF1dGhvcml0eTANBgkqhkiG9w0BAQUFAAOCAQEA\nGfV6i09sl0pYRU/7r0L8aKT300zj7WTo2F6mM+ZlRSTFPp6AaDqScmbsnTpfUvb6ZrF+J3gF277B\nxbEte8aD5oc2DgcfMAuufjqF+Xc3rwdrHW/lMsVRzZBF+kKela2AT1FdD5KN4Tw58rSer9hXZ2TN\ndEng7R7dOO8nFF26e2f4E+j69aryEMWYKJLTqFVtwzJx/s69vLV3Ps1C2eYUOllEPb/AQUWDc3cP\nsWMwDlOU1UJvABtyRUFGfMHB6hZEBfSIs6W4Y0F7y8r1GEL8nKVsDMvzFkU3LDrmzArl4Xi59QrT\nd5B3m7vD5pDpT3cKAEMToi26CB0whMVtvaG3dQ==\n-----END CERTIFICATE-----'}]

ligs = [{'name': 'POTASH3', 'uplinkSets': [], 'enclosureIndexes': [1, 2, 3], 'interconnectBaySet': 3, 'redundancyType': 'HighlyAvailable',
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                     {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                     {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                     {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                     {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                     {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}]},
        {'name': 'POTASH2', 'uplinkSets': [], 'enclosureIndexes': [1, 2, 3], 'interconnectBaySet': 2, 'redundancyType': 'HighlyAvailable',
         'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                     {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                     {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                     {'bay': 2, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                     {'bay': 5, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}]},
        {'name': 'CARBON2', 'uplinkSets': [], 'enclosureIndexes': [-1], 'interconnectBaySet': 2, 'redundancyType': 'Redundant',
         'interconnectMapTemplate': [{'bay': 2, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 5, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}]}
        ]

sas_ligs = [{'name': 'NATASHA', 'enclosureIndexes': [1], 'interconnectBaySet': 1, 'type': 'sas-logical-interconnect-group', 'enclosureType': 'SY12000',
             'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                                         {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1}]}]

enclosure_groups = [{'name': 'POTASH CARBON NATASHA', 'enclosureCount': 3, 'ipAddressingMode': 'DHCP',
                     'interconnectBayMappings': [{'bay': 1, 'lig': 'SASLIG:NATASHA'},
                                                 {'bay': 2, 'lig': 'LIG:CARBON2'},
                                                 {'bay': 3, 'lig': 'LIG:POTASH3'},
                                                 {'bay': 4, 'lig': 'SASLIG:NATASHA'},
                                                 {'bay': 5, 'lig': 'LIG:CARBON2'},
                                                 {'bay': 6, 'lig': 'LIG:POTASH3'}]},
                    {'name': 'POTASH POTASH NATASHA', 'enclosureCount': 3, 'ipAddressingMode': 'DHCP',
                     'interconnectBayMappings': [{'bay': 1, 'lig': 'SASLIG:NATASHA'},
                                                 {'bay': 2, 'lig': 'LIG:POTASH2'},
                                                 {'bay': 3, 'lig': 'LIG:POTASH3'},
                                                 {'bay': 4, 'lig': 'SASLIG:NATASHA'},
                                                 {'bay': 5, 'lig': 'LIG:POTASH2'},
                                                 {'bay': 6, 'lig': 'LIG:POTASH3'}]}]

logical_enclosure = [{'name': 'LE Scale', 'enclosureUris': ['ENC:SCALE-01', 'ENC:SCALE-02', 'ENC:SCALE-03'], 'enclosureGroupUri': 'EG:POTASH CARBON NATASHA'}]

sans = [{'Type': 'Brocade Network Advisor',
         'Host': '16.125.71.185',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'password', 'UseSsl': True},
        {'Type': 'Cisco',
         'Host': '172.18.20.1',
         'SnmpPort': 161,
         'SnmpUserName': 'dcs-SHA',
         'SnmpAuthLevel': 'AUTHNOPRIV',
         'SnmpAuthProtocol': 'SHA',
         'SnmpAuthString': 'dcsdcsdcs'}]

ethernets = [{"vlanIdStart": 10, "vlanIdEnd": 1009, "purpose": "General", "namePrefix": "Ethernet", "smartLink": False, "privateNetwork": False,
              "bandwidth": {"maximumBandwidth": 10000, "typicalBandwidth": 2000}, "type": "bulk-ethernet-network"}]

fcs = [{'count': 12, 'base_name': 'FC SAN A', 'associatedSAN': 'TbirdR1-Fab1-10:00:50:eb:1a:64:12:09'}]

fcoes = [{'base_name': 'FCoE SAN A', 'vlanId': 1084, 'san': 'VSAN1084', 'count': 2},
         {'base_name': 'FCoE SAN B', 'vlanId': 1085, 'san': 'VSAN1085', 'count': 2}]

net_sets = [{'network_set': 1, 'network_count': 150, 'start_vlan': 10},
            {'network_set': 2, 'network_count': 150, 'start_vlan': 87},
            {'network_set': 3, 'network_count': 90, 'start_vlan': 321},
            {'network_set': 4, 'network_count': 90, 'start_vlan': 548}]

storage_systems = [{'name': 'ThreePAR7200-6704', 'family': 'StoreServ', "hostname": "172.18.11.11",
                    "credentials": {"username": "dcs", "password": "dcs"}, "serialNumber": "TXQ1000307",
                    'deviceSpecificAttributes': {'managedDomain': 'ScaleTestingDomain', 'managedPools': []}}]

storage_pools = [{"storageSystemUri": 'ThreePAR7200-6704', "name": 'ScaleTestingDomain_CPG_1', "isManaged": True},
                 {"storageSystemUri": 'ThreePAR7200-6704', "name": 'ScaleTestingDomain_CPG_2', "isManaged": True},
                 {"storageSystemUri": 'ThreePAR7200-6704', "name": 'ScaleTestingDomain_CPG_3', "isManaged": True}]

storage_volumes = [{"name": "Vol1priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol2priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol3priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol4priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol5priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol6priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol7priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol8priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol9priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol10priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol11priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol12priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol13priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol14priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol15priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol16priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol17priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol18priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol19priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol20priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol21priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol22priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol23priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol24priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol25priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol26priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol27priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol28priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol29priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol30priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol31priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol32priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol33priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol34priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol35priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol36priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol37priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol38priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol39priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True},
                   {"name": "Vol40priv", "StoragePool": "ScaleTestingDomain_CPG_1", "share": True}]

uplinks_data = [{'name': 'usCarbon', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC SAN A1'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]},
                {'name': 'usPotash2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUrisvlanIdStart': 10, 'networkUrisvlanIdEnd': 13, 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'},
                                            {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}]},
                {'name': 'usPotash3', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUrisvlanIdStart': 10, 'networkUrisvlanIdEnd': 13, 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                            {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}]}]

uplink_sets = DD.create_uplink_data(uplinks_data)

update_ligs = [{'name': 'POTASH3', 'uplinkSets': [uplink_sets['usPotash3'].copy()], 'enclosureIndexes': [1, 2, 3], 'interconnectBaySet': 3, 'redundancyType': 'HighlyAvailable',
                'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                            {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                            {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                            {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                            {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                            {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}]},
               {'name': 'POTASH2', 'uplinkSets': [uplink_sets['usPotash2'].copy()], 'enclosureIndexes': [1, 2, 3], 'interconnectBaySet': 2, 'redundancyType': 'HighlyAvailable',
                'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                            {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                            {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                            {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                            {'bay': 2, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                                            {'bay': 5, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}]},
               {'name': 'CARBON2', 'uplinkSets': [uplink_sets['usCarbon'].copy()], 'enclosureIndexes': [-1], 'interconnectBaySet': 2, 'redundancyType': 'Redundant',
                'interconnectMapTemplate': [{'bay': 2, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                            {'bay': 5, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}]}]

server_profile_templates = [{'name': 'Bronco Quartz Fishman', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '',
                             'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:POTASH CARBON NATASHA',
                             'serialNumberType': 'Virtual', 'macType': 'Virtual',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                                                'requestedMbps': '2000', 'networkUri': 'ETH:Ethernet_10'}]},
                             'localStorage': {'sasLogicalJBODs': [{'id': 1, 'deviceSlot': 'Mezz 1', 'name': 'ScaleLD', 'numPhysicalDrives': 3, 'driveMinSizeGB': 1,
                                                                   'driveMaxSizeGB': 900, 'driveTechnology': 'SasHdd'}],
                                              'controllers': [{'logicalDrives': [{'name': None, 'raidLevel': 'RAID5', 'bootable': False,
                                                                                  'numPhysicalDrives': None, 'driveTechnology': None, 'sasLogicalJBODId': 1}],
                                                               'deviceSlot': 'Mezz 1', 'mode': 'RAID', 'initialize': False}]},
                             'sanStorage': {'manageSanStorage': True, 'hostOSType': 'VMware (ESXi)',
                                            'volumeAttachments': [{'id': 1, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1,
                                                                   'storagePaths': [],
                                                                   'volumeName': '1', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 2, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 2,
                                                                   'storagePaths': [],
                                                                   'volumeName': '2', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 3, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 3,
                                                                   'storagePaths': [],
                                                                   'volumeName': '3', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 4, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 4,
                                                                   'storagePaths': [],
                                                                   'volumeName': '4', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 5, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 5,
                                                                   'storagePaths': [],
                                                                   'volumeName': '5', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
#                                                                 {'id': 6, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 6,
#                                                                  'storagePaths': [],
#                                                                  'volumeName': '6', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6955',
#                                                                  'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '107374182400',
#                                                                  'volumeShareable': True, 'permanent': True, 'dataProtectionLevel': None,
#                                                                  'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'}
                                                                  ]}},
                            {'name': 'Bronco Quartz', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '',
                             'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:POTASH CARBON NATASHA',
                             'serialNumberType': 'Virtual', 'macType': 'Virtual',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1',
                                                                     'requestedMbps': 'Auto', 'networkUri': 'FC:FC SAN A1'}]},
                             'localStorage': None,
                             'sanStorage': {'manageSanStorage': True, 'hostOSType': 'VMware (ESXi)',
                                            'volumeAttachments': [{'id': 1, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1,
                                                                   'storagePaths': [],
                                                                   'volumeName': '1', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 2, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 2,
                                                                   'storagePaths': [],
                                                                   'volumeName': '2', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 3, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 3,
                                                                   'storagePaths': [],
                                                                   'volumeName': '3', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 4, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 4,
                                                                   'storagePaths': [],
                                                                   'volumeName': '4', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'},
                                                                  {'id': 5, 'volumeUri': None, 'isBootVolume': False, 'lunType': 'Manual', 'lun': 5,
                                                                   'storagePaths': [],
                                                                   'volumeName': '5', 'volumeDescription': '', 'volumeStorageSystemUri': 'SS:ThreePAR7200-6704',
                                                                   'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes': '10737418240',
                                                                   'volumeShareable': False, 'permanent': False, 'dataProtectionLevel': None,
                                                                   'volumeStoragePoolUri': 'SPOOL:ScaleTestingDomain_CPG_4'}]}},
                            {'name': 'SY 480 Gen9 3', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '',
                             'serverHardwareTypeUri': 'SHT:SY 480 Gen9 3', 'enclosureGroupUri': 'EG:POTASH POTASH NATASHA',
                             'serialNumberType': 'Virtual', 'macType': 'Virtual',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                                     'requestedMbps': '2000', 'networkUri': 'ETH:Ethernet_10'}]}},
                            {'name': 'SY 660 Gen9 1', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '',
                             'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:POTASH CARBON NATASHA',
                             'serialNumberType': 'Virtual', 'macType': 'Virtual',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1',
                                                                     'requestedMbps': 'Auto', 'networkUri': 'FC:FC SAN A1'}]}},
                            {'name': 'SY 660 Gen9 2', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '',
                             'serverHardwareTypeUri': 'SHT:SY 660 Gen9 2', 'enclosureGroupUri': 'EG:POTASH POTASH NATASHA',
                             'serialNumberType': 'Virtual', 'macType': 'Virtual',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                                     'requestedMbps': '2000', 'networkUri': 'ETH:Ethernet_10'}]}}]

server_profiles = [{'name': 'bay 4', 'serverHardwareUri': 'SCALE-01, bay 4', 'serverProfileTemplateUri': 'SPT:Bronco Quartz', 'type': 'ServerProfileV7'},
                   {'name': 'bay 5', 'serverHardwareUri': 'SCALE-01, bay 5', 'serverProfileTemplateUri': 'SPT:Bronco Quartz Fishman', 'type': 'ServerProfileV7'}]

# Enclosure data
encl_update = DD.rename_enclosure(ENCLOSURE)
expected_enclosure = DD.expected_enclosure_data(ENCLOSURE)

# SPP data
spp_ftp_path, spp_local_path = DD.get_spp_path(spp_name, spp_local_dir, ftp_site_path)
expected_spp = DD.expected_spp_data(spp_name)

# Users data
users = DD.users_data(users_name)
expected_users = DD.expected_users_data(users_name)

# Active Directory data
active_directory_server = DD.make_ad_dict(active_directory)

# LIG data
expected_ligs = DD.make_expected_lig_data(ligs)
expected_sasligs = DD.make_expected_saslig_data(sas_ligs)
expected_ligs_updated = DD.make_expected_lig_data(update_ligs)

# Enclosure Group data
enc_groups = DD.make_enc_group_data(enclosure_groups)
expected_encgroup = DD.make_expected_enc_group_data(enclosure_groups)

# LE data
expected_logical_enclosure = DD.make_expected_logical_enclosure_data(logical_enclosure)

# SAN managers data
san_managers = DD.create_san_manager_data(sans)
expected_san_managers = DD.get_expected_san_manager_data(sans)

# Ethernet Networks data
ethernet_networks = DD.create_ebulk_data(ethernets)
expected_ethernet_networks = DD.get_expected_ebulk_data(ethernets)

# Fiber channel Networks data
fc_networks = DD.create_fcnet_data(fcs)
expected_fc_networks = DD.get_expected_fcnet_data(fcs)

# FCoE Networks data
fcoe_networks = DD.create_fcoenet_data(fcoes)
expected_fcoe_networks = DD.get_expected_fcoenet_data(fcoes)

# Network Set data
network_sets = DD.create_network_set_data(net_sets)
expected_network_sets = DD.get_expected_network_set_data(net_sets)

# Storage Systems data
expected_storage_systems = DD.expected_storage_system(storage_systems)

# Storage Volumes data
d_storage_volume = DD.storage_volumes(storage_volumes)
d_expected_storage_volume = DD.expected_storage_volumes(storage_volumes)

# Server Profile data
expected_server_profiles_from_spt = DD.make_expected_server_profile_data(server_profiles)


remotesupport_edit = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                      {'op': 'replace', 'path': '/configuration/companyName', 'value': 'HPE'},
                      {'op': 'replace', 'path': '/configuration/marketingOptIn', 'value': True},
                      {"op": "replace", "path": "/configuration/autoEnableDevices", "value": True},
                      {'op': 'add', 'path': '/sites/default',
                       'value': {'name': 'DEFAULT SITE', 'streetAddress1': 'Compaq Center Dr', 'streetAddress2': '', 'city': 'Houston', 'provinceState': 'TX',
                                 'postalCode': '', 'timeZone': 'US/Central', 'countryCode': 'US', 'type': 'Site', 'default': True}},
                      {'op': 'add', 'path': '/contacts',
                       'value': {'contactKey': 'default', 'firstName': 'FFF', 'lastName': 'LLL', 'email': 'fff.lll@hpe.com', 'primaryPhone': '8884442222',
                                 'alternatePhone': '', 'notes': '', 'language': 'en', 'default': True, 'type': 'Contact'}}]
