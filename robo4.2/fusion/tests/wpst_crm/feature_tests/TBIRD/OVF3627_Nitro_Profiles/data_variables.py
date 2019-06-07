def rlist(start, end, prefix='net_', suffix='', step=1):
    return ['%s%s%s' % (prefix, str(x), suffix)
            for x in xrange(start, end + 1, step)]


feature_toggle = "echo 'hafnium.tempWorkarounds.skipProcessingBlock162=true' > /tmp/hafnium-simulation.properties;" \
                 "chmod 755 /tmp/hafnium-simulation.properties;" \
                 "/ci/bin/set-feature-toggles -e OVF1773_Nitro_ICM_Support -e OVF1776_MethaneDiscovery " \
                 "-e OVF2128_NitoMethane_ILT_Support"

SSH_PASS = 'hpvse1'
interface = 'bond0'

EG1 = 'EG1'

ENC1 = 'MXQ71902DQ'

LE1 = 'LE1'

NITRO_MODEL = 'Virtual Connect SE 100Gb F32 Module for Synergy'
NITRO_PART = '867796-B21'
CL50_MODEL = 'Synergy 50Gb Interconnect Link Module'

ENC1_BAY1_IPS = ['172.16.1.3', '172.16.3.3', '172.16.5.3', '172.16.60.3', '172.16.90.3']
ENC1_BAY2_IPS = ['172.16.1.4', '172.16.3.4', '172.16.5.4', '172.16.60.4', '172.16.90.4']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

users = [
    {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin',
     'permissions': [{'roleName': 'Server administrator'}],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
     'permissions': [{'roleName': 'Network administrator'}], 'emailAddress': 'nat@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin',
     'permissions': [{'roleName': 'Backup administrator'}],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge',
     'permissions': [{'roleName': 'Read only'}],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'}
]

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM',
           'startAddress': '00:BC:56:00:00:00', 'endAddress': '00:BC:56:00:00:7F', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM',
           'startAddress': '21:11:BC:56:00:00:00:00', 'endAddress': '21:11:BC:56:00:00:00:7F', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM',
           'startAddress': 'VCUAAAAAAA', 'endAddress': 'VCUAAAAADT', 'enabled': True}]

e1 = [{'name': n,
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'} for n in rlist(1, 256, 'tunnel_')]

e2 = [{'name': 'untagged_1',
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Untagged'}]

e3 = [{'name': n,
       'type': 'ethernet-networkV4',
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(1, 3966)]

ethernet_networks = e1 + e2 + e3

network_sets = [{'name': 'NetSet1', 'type': 'network-setV4', 'networkUris': rlist(1, 500),
                 'nativeNetworkUri': None},
                {'name': 'NetSet2', 'type': 'network-setV4', 'networkUris': rlist(501, 998),
                 'nativeNetworkUri': None}
                ]


def us(**kwargs):
    return {'name': kwargs.get('name', None),
            'ethernetNetworkType': kwargs.get('ethernetNetworkType', 'Tagged'),
            'networkType': 'Ethernet',
            'networkUris': kwargs.get('networkUris', None),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': kwargs.get('logicalPortConfigInfos', None)}


def lig(**kwargs):
    return {'name': kwargs.get('name', None),
            'type': kwargs.get('type', 'logical-interconnect-groupV5'),
            'enclosureType': kwargs.get('enclosureType', 'SY12000'),
            'interconnectMapTemplate': kwargs.get('interconnectMapTemplate', [
                {'bay': 3, 'enclosure': 1, 'type': NITRO_MODEL,
                 'enclosureIndex': 1}]),
            'enclosureIndexes': kwargs.get('enclosureIndexes', [1]),
            'interconnectBaySet': kwargs.get('interconnectBaySet', 3),
            'redundancyType': kwargs.get('redundancyType', 'NonRedundantASide'),
            'uplinkSets': kwargs.get('uplinkSets', []),
            'internalNetworkUris': kwargs.get('internalNetworkUris', None),
            }


uplink_sets = {'Q6': us(name='Tagged 1-100',
                        networkUris=rlist(1, 100),
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q6', 'speed': 'Auto'}]),

               'Q4': us(name='Tunnel',
                        networkUris=['tunnel_1'],
                        ethernetNetworkType='Tunnel',
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q4', 'speed': 'Auto'}]),
               'Q1': us(name='Untagged',
                        networkUris=['untagged_1'],
                        ethernetNetworkType='Untagged',
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q1', 'speed': 'Auto'}]),
               'BigPipe': us(name='BigPipe',
                             networkUris=rlist(101, 3966),
                             logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                      'port': p,
                                                      'speed': 'Auto'}
                                                     for p in sorted(['Q%i.%i' % (n, i)
                                                                      for i in range(1, 5)
                                                                      for n in (3, 5)])])
               }

LIG1 = 'LIG1'

ligs = {LIG1: lig(name=LIG1,
                  internalNetworkUris=[n for n in rlist(2, 126, 'tunnel_')],
                  uplinkSets=[v for v in uplink_sets.itervalues()])}

enc_groups = {EG1: {'name': EG1,
                    'enclosureCount': 1,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
                    'ipAddressingMode': "External"
                    }
              }

les = {LE1: {'name': LE1,
             'enclosureUris': ['ENC:%s' % ENC1],
             'enclosureGroupUri': 'EG:%s' % EG1,
             'firmwareBaselineUri': None,
             'forceInstallFirmware': False
             }
       }

connections = [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                'requestedMbps': '2500', 'networkUri': 'ETH:untagged_1',
                'boot': {'priority': 'NotBootable'}},
               {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                'requestedMbps': '2500', 'networkUri': 'ETH:tunnel_1',
                'boot': {'priority': 'NotBootable'}},
               {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                'requestedMbps': '2500', 'networkUri': 'NS:NetSet1',
                'boot': {'priority': 'NotBootable'}},
               {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                'requestedMbps': '2500', 'networkUri': 'NS:NetSet2',
                'boot': {'priority': 'NotBootable'}}
               ]

server_profiles = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG1,
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': ENC1 + '_Bay1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {'connections': connections}},

                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG1,
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': ENC1 + '_Bay2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {'connections': connections}}
                   ]
