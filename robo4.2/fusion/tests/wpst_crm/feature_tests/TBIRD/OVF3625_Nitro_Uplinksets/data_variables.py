from copy import deepcopy


def rlist(start, end, prefix='net_', suffix='', step=1):
    ls = []
    for x in xrange(start, end + 1, step):
        ls.append('%s%s%s' % (prefix, str(x), suffix))
    return ls


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

e1 = [{'name': 'tunnelnetwork1',
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'},
      {'name': 'untaggednetwork1',
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Untagged'},
      ]

e2 = [{'name': n,
       'type': 'ethernet-networkV4',
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(1, 3966)]

ethernet_networks = e1 + e2


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
    return deepcopy({'name': kwargs.get('name', None),
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
                     })


def li_us(**kwargs):
    # noinspection PyUnboundLocalVariable
    return deepcopy({'name': kwargs.get('name', None),
                     'ethernetNetworkType': kwargs.get('ethernetNetworkType', 'Tagged'),
                     'networkType': kwargs.get('networkType', 'Ethernet'),
                     'networkUris': kwargs.get('networkUris', []),
                     'fcNetworkUris': kwargs.get('fcNetworkUris', []),
                     'fcoeNetworkUris': kwargs.get('fcoeNetworkUris', []),
                     'lacpTimer': kwargs.get('lacpTimer', 'Short'),
                     'logicalInterconnectUri': kwargs.get('logicalInterconnectUri', None),
                     'primaryPortLocation': kwargs.get('primaryPortLocation', None),
                     'manualLoginRedistributionState': kwargs.get('manualLoginRedistributionState', 'NotSupported'),
                     'connectionMode': kwargs.get('connectionMode', 'Auto'),
                     'nativeNetworkUri': kwargs.get('nativeNetworkUri', None),
                     'portConfigInfos': kwargs.get('portConfigInfos', None)})


uplink_sets = {'All-Q': us(name='All-Q',
                           networkUris=rlist(1, 3966),
                           logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                    'port': 'Q%i' % n,
                                                    'speed': 'Auto'}
                                                   for n in range(1, 7)]),
               'All-Q-neg': us(name='All-Q',
                               networkUris=rlist(1, 3967),
                               logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                        'port': 'Q%i' % n,
                                                        'speed': 'Auto'}
                                                       for n in range(1, 7)]),
               '12ports': us(name='12ports - Q1.1 - Q3.4',
                             networkUris=rlist(1, 3966),
                             logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                      'port': p,
                                                      'speed': 'Auto'}
                                                     for p in sorted(['Q%i.%i' % (n, i)
                                                                      for i in range(1, 5)
                                                                      for n in range(1, 4)])]
                             ),
               '12ports2': us(name='12ports - Q1.1 - Q3.4',
                              networkUris=rlist(1, 3965),
                              logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                       'port': p,
                                                       'speed': 'Auto'}
                                                      for p in sorted(['Q%i.%i' % (n, i)
                                                                       for i in range(1, 5)
                                                                       for n in range(1, 4)])]
                              ),
               'mixed-ports': us(name='13ports - Q1.1 - Q3.4, Q4',
                                 networkUris=rlist(1, 3966),
                                 logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                          'port': p,
                                                          'speed': 'Auto'}
                                                         for p in sorted(['Q%i.%i' % (n, i)
                                                                          for i in range(1, 5)
                                                                          for n in range(1, 4)])] +
                                                        [{'enclosure': '1', 'bay': '3',
                                                          'port': 'Q4', 'speed': 'Auto'}]
                                 ),
               '16ports': us(name='16ports - Q1.1 - Q4.4',
                             networkUris=rlist(1, 3966),
                             logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                      'port': p,
                                                      'speed': 'Auto'}
                                                     for p in sorted(['Q%i.%i' % (n, i)
                                                                      for i in range(1, 5)
                                                                      for n in range(1, 5)])]
                             ),
               '16ports2': us(name='16ports - Q1.1 - Q4.4, 1 net',
                              networkUris=['net_200'],
                              logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                       'port': p,
                                                       'speed': 'Auto'}
                                                      for p in sorted(['Q%i.%i' % (n, i)
                                                                       for i in range(1, 5)
                                                                       for n in range(1, 5)])]
                              ),
               '16ports3': us(name='16ports - Q1.1 - Q4.4, 1 net',
                              networkUris=rlist(1, 3967),
                              logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                       'port': p,
                                                       'speed': 'Auto'}
                                                      for p in sorted(['Q%i.%i' % (n, i)
                                                                       for i in range(1, 5)
                                                                       for n in range(1, 5)])]
                              ),
               'Q4subs': us(name='4ports - Q4.1 - Q4.4, 1 net',
                            networkUris=['net_3966'],
                            logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                     'port': p,
                                                     'speed': 'Auto'}
                                                    for p in sorted(['Q%i.%i' % (n, i)
                                                                     for i in range(1, 5)
                                                                     for n in range(4, 5)])]
                            ),

               'Q4': us(name='Q4 3965 nets',
                        networkUris=rlist(1, 3966),
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q4', 'speed': 'Auto'}]),

               'Q5': us(name='Q5 1 net',
                        networkUris=['net_3967'],
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q5', 'speed': 'Auto'}]),
               'Q7': us(name='Q7 not allowed',
                        networkUris=['net_3967'],
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q7', 'speed': 'Auto'}]),
               'Q8': us(name='Q8 not allowed',
                        networkUris=['net_3967'],
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q8', 'speed': 'Auto'}]),
               'X1': us(name='X1 not allowed',
                        networkUris=['net_3967'],
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'X1', 'speed': 'Auto'}]),
               'X2': us(name='X2 not allowed',
                        networkUris=['net_3967'],
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'X2', 'speed': 'Auto'}]),
               '24ports': us(name='24ports - Q1.1 - Q6.4',
                             networkUris=['net_3967'],
                             logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                      'port': p,
                                                      'speed': 'Auto'}
                                                     for p in sorted(['Q%i.%i' % (n, i)
                                                                      for i in range(1, 5)
                                                                      for n in range(1, 7)])]),
               '3967vlans': us(name='Exceeds max 3966 vlans',
                               networkUris=rlist(1, 3967),
                               logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                        'port': 'Q6', 'speed': 'Auto'}]),
               'i3s1': us(name='Valid I3S',
                          networkUris=['net_2'],
                          ethernetNetworkType='ImageStreamer',
                          logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                   'port': 'X1', 'speed': 'Auto'},
                                                  {'enclosure': '1', 'bay': '3',
                                                   'port': 'X2', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6',
                                                   'port': 'X1', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6',
                                                   'port': 'X2', 'speed': 'Auto'}
                                                  ]),
               'i3s2': us(name='Invalid I3S',
                          networkUris=['net_2'],
                          ethernetNetworkType='ImageStreamer',
                          logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                   'port': 'Q1', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6',
                                                   'port': 'Q1', 'speed': 'Auto'},
                                                  {'enclosure': '1', 'bay': '3',
                                                   'port': 'Q2', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6',
                                                   'port': 'Q2', 'speed': 'Auto'}
                                                  ]),
               }

i3s_icmap = [{'bay': 3, 'enclosure': 1, 'type': NITRO_MODEL, 'enclosureIndex': 1},
             {'bay': 6, 'enclosure': 1, 'type': CL50_MODEL, 'enclosureIndex': 1},
             {'bay': 3, 'enclosure': 2, 'type': CL50_MODEL, 'enclosureIndex': 2},
             {'bay': 6, 'enclosure': 2, 'type': NITRO_MODEL, 'enclosureIndex': 2}]

# Negative LIGS
NLIG1 = 'NLIG1-24 Uplink Ports 1 US'
NLIG3 = 'NLIG3-3967 Vlans 1 US'
NLIG4 = 'NLIG4-3967 Vlans 2 US'
NLIG5 = 'NLIG5-Q7 not allowed'
NLIG6 = 'NLIG6-Q8 not allowed'
NLIG7 = 'NLIG7-X1 not allowed'
NLIG8 = 'NLIG8-X2 not allowed'
NLIG9 = 'NLIG9-I3S Q1 - Q8 not allowed'
NLIG10 = 'NLIG10-exceeds-max-internal-nets'
NLIG11 = 'NLIG11-edit-exceeds-max-ports'
NLIG12 = 'NLIG12-edit-exceeds-max-nets'
NLIG13 = 'NLIG13-edit-exceeds-max-internal-nets'
NLIG14 = 'NLIG14-mixed-port uplinkset not allowed'

neg_ligs = {NLIG1: lig(name=NLIG1, uplinkSets=[deepcopy(uplink_sets['24ports'])]),
            NLIG3: lig(name=NLIG3, uplinkSets=[deepcopy(uplink_sets['3967vlans'])]),
            NLIG4: lig(name=NLIG4, uplinkSets=[deepcopy(uplink_sets['Q4'])] + [deepcopy(uplink_sets['Q5'])]),
            NLIG5: lig(name=NLIG5, uplinkSets=[deepcopy(uplink_sets['Q7'])]),
            NLIG6: lig(name=NLIG6, uplinkSets=[deepcopy(uplink_sets['Q8'])]),
            NLIG7: lig(name=NLIG7, uplinkSets=[deepcopy(uplink_sets['X1'])]),
            NLIG8: lig(name=NLIG8, uplinkSets=[deepcopy(uplink_sets['X2'])]),
            NLIG9: lig(name=NLIG9,
                       interconnectMapTemplate=i3s_icmap,
                       enclosureIndexes=[1, 2],
                       redundancyType='HighlyAvailable',
                       uplinkSets=[deepcopy(uplink_sets['i3s2'])]),
            NLIG10: lig(name=NLIG10, internalNetworkUris=rlist(1, 3967)),
            NLIG11: lig(name=NLIG11, uplinkSets=[deepcopy(uplink_sets['24ports'])]),
            NLIG12: lig(name=NLIG12, uplinkSets=[deepcopy(uplink_sets['16ports3'])]),
            NLIG13: lig(name=NLIG13, internalNetworkUris=rlist(1, 3967)),
            NLIG14: lig(name=NLIG14, uplinkSets=[uplink_sets['mixed-ports']])
            }

# Positive LIGS
LIG1 = 'LIG1'
LIG2 = 'LIG2'
LIG3 = 'LIG3'
LIG4 = 'LIG4'
LIG5 = 'LIG5'
LIG6 = 'LIG6'
LIG7 = 'LIG7'
LIG8 = 'LIG8'
LIG9 = 'LIG9'

pos_ligs = {LIG1: lig(name=LIG1, uplinkSets=[deepcopy(uplink_sets['All-Q'])]),
            LIG2: lig(name=LIG2, uplinkSets=[deepcopy(uplink_sets['16ports'])]),
            LIG3: lig(name=LIG3, internalNetworkUris=rlist(1, 3966)),
            LIG4: lig(name=LIG4,
                      interconnectMapTemplate=i3s_icmap,
                      enclosureIndexes=[1, 2],
                      redundancyType='HighlyAvailable',
                      uplinkSets=[deepcopy(uplink_sets['i3s1'])]),
            LIG5: lig(name=LIG5, uplinkSets=[deepcopy(uplink_sets['12ports'])]),
            LIG6: lig(name=LIG6, uplinkSets=[deepcopy(uplink_sets['12ports2'])],
                      internalNetworkUris=['net_3966']),
            LIG7: lig(name=LIG7, uplinkSets=[deepcopy(uplink_sets['12ports2']),
                                             deepcopy(uplink_sets['Q4subs'])],
                      internalNetworkUris=None),
            LIG8: lig(name=LIG8, uplinkSets=[deepcopy(uplink_sets['16ports2'])]),
            LIG9: lig(name=LIG9, uplinkSets=[deepcopy(uplink_sets['16ports2'])] + [deepcopy(uplink_sets['Q5'])]),

            }

neg_li_us = {
    '24ports': li_us(name='24ports - Q1.1 - Q6.4',
                     networkUris=rlist(1, 3966),
                     portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': p, 'desiredSpeed': 'Auto'}
                                      for p in sorted(['Q%i:%i' % (n, i)
                                                       for i in range(1, 5)
                                                       for n in range(1, 7)])]),
    'Q5_3967nets': li_us(name='Q5_3967nets',
                         networkUris=rlist(1, 3967),
                         portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': 'Q5', 'desiredSpeed': 'Auto'}]),
    'mixed-ports': li_us(name='13ports - Q1.1 - Q3.4, Q4',
                         networkUris=rlist(1, 3966),
                         portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': p, 'desiredSpeed': 'Auto'}
                                          for p in sorted(['Q%i:%i' % (n, i)
                                                           for i in range(1, 5)
                                                           for n in range(1, 4)])] +
                                         [{'enclosure': ENC1, 'bay': '3', 'port': 'Q4', 'desiredSpeed': 'Auto'}])
}

pos_li_us = {
    'Q4subs': li_us(name='4ports - Q4.1 - Q4.4, 1 net',
                    networkUris=['net_3966'],
                    portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': p, 'desiredSpeed': 'Auto'}
                                     for p in sorted(['Q%i:%i' % (n, i)
                                                      for i in range(1, 5)
                                                      for n in range(4, 5)])]),

    'Q5': li_us(name='Q5',
                portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': 'Q5', 'desiredSpeed': 'Auto'}]),
    'Q6': li_us(name='Q6',
                networkUris=['net_3967'],
                portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': 'Q5', 'desiredSpeed': 'Auto'}]),

    '12ports': li_us(name='12ports - Q1.1 - Q3.4',
                     networkUris=rlist(1, 3966),
                     portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': p, 'desiredSpeed': 'Auto'}
                                      for p in sorted(['Q%i:%i' % (n, i)
                                                       for i in range(1, 5)
                                                       for n in range(1, 4)])]),
    '12ports2': li_us(name='12ports - Q1.1 - Q3.4',
                      networkUris=rlist(1, 3965),
                      portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': p, 'desiredSpeed': 'Auto'}
                                       for p in sorted(['Q%i:%i' % (n, i)
                                                        for i in range(1, 5)
                                                        for n in range(1, 4)])]),

    '16ports': li_us(name='16ports - Q1.1 - Q4.4',
                     networkUris=rlist(1, 3966),
                     portConfigInfos=[{'enclosure': ENC1, 'bay': '3', 'port': p, 'desiredSpeed': 'Auto'}
                                      for p in sorted(['Q%i:%i' % (n, i)
                                                       for i in range(1, 5)
                                                       for n in range(1, 5)])]),
}

enc_groups = {EG1: {'name': EG1,
                    'enclosureCount': 1,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG2},
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
