import os
import sys


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ENC1 = 'CN754406W6'
ENC2 = 'CN754406W5'

fc_networks = [{'name': '502_FC_1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': '502_FC_2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]

uplink_sets1 = {'us1': {'name': 'up1',
                        'ethernetNetworkType': None,
                        'networkType': 'FibreChannel',
                        'networkUris': ['502_FC_1'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'lacpTimer': 'Short',
                        'primaryPort': None,
                        'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q6:1', 'speed': 'Auto'}]},
                'us2': {'name': 'up2',
                        'ethernetNetworkType': None,
                        'networkType': 'FibreChannel',
                        'networkUris': ['502_FC_2'],
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'lacpTimer': 'Short',
                        'primaryPort': None,
                        'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': 'Q4:1', 'speed': 'Auto'}]}
                }

LIGS_TB = {'name': 'LIG_502',
           'type': 'logical-interconnect-groupV400',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
                                       ],
           'enclosureIndexes': [1],
           'interconnectBaySet': 3,
           'redundancyType': 'Redundant',
           'uplinkSets': [uplink_sets1['us1'].copy(), uplink_sets1['us2'].copy()],
           'ethernetSettings': None,
           'state': None,
           'telemetryConfiguration': None,
           'snmpConfiguration': None}

enc_group = [{'name': 'EG_502',
              'enclosureCount': 1,
              'powerMode': 'RedundantPowerFeed',
              'ambientTemperatureMode': 'Standard',
              'ipAddressingMode': 'DHCP',
              'enclosureCount': 1,
              'interconnectBayMappings':
              [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG_502'},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG_502'}]}]


LE = 'LE'

Logical_Enclosure = [{'name': LE,
                      'enclosureUris': ['ENC:' + ENC1],
                      'enclosureGroupUri': 'EG:EG_502',
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False}]

INTERCONNECTS = ['CN754406W6, interconnect 3', 'CN754406W6, interconnect 6']

GET_INTERCONNECTS_URI = [{'interconnectName': 'CN754406W6, interconnect 3'}, {'interconnectName': 'CN754406W6, interconnect 6'}]

interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]

Supported_transreceiver_SFP = {"portName": "Q4:1",
                               "speed": "null",
                               "vendorName": "HPE",
                               "vendorPartNumber": "455883-B21",
                               "vendorRevision": "C1",
                               "vendorOui": "00:0a:0d",
                               "extIdentifier": "null",
                               "digitalDiagnostics":
                               {
                                   "temperature": "30",
                                   "voltage": "3.3083",
                                   "laneInformation":
                                        [
                                            {
                                                "laneId": "1",
                                                "rxPowermW": "0.5778",
                                                "txPowermW": "0.5960",
                                                "rxPowerdBm": "-2.3822",
                                                "txPowerdBm": "-2.2475",
                                                "current": "5.2100"
                                            }
                                        ]
                               },
                               "serialNumber": "EN1443-00814",
                               "identifier": "SFP",
                               "connector": "UNKNOWN_OR_UNSPECIFIED"
                               }

unsupported_transreceiver = {"portName": "d3",
                             "speed": "null",
                             "vendorName": "null",
                             "vendorPartNumber": "null",
                             "vendorRevision": "null",
                             "vendorOui": "null",
                             "extIdentifier": "null",
                             "digitalDiagnostics":
                             {
                                 "temperature": "null",
                                 "voltage": "null",
                                 "laneInformation":
                                 [
                                 ]
                             },
                             "serialNumber": "null",
                             "identifier": "UNKNOWN",
                             "connector": "UNKNOWN_OR_UNSPECIFIED"
                             }

uplink_ports = 'Q4:1'

Disable_Port = {"interconnectName": "CN754406W6, interconnect 6", "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["EnetFcoe", "Ethernet"], "enabled": False, "portName": "Q4:1", "portStatus": "Unknown", "type": "port"}

Enable_port = {"interconnectName": "CN754406W6, interconnect 6", "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["EnetFcoe", "Ethernet"], "enabled": True, "portName": "Q4:1", "portStatus": "Unknown", "type": "port"}
