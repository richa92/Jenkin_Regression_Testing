import os
import sys
import paramiko
import time
import re


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ENC1 = 'CN754406W6'
LE = 'LE'

uplink_sets = {'us1': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net1'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'},
                                                  ]}
               }
ethnets = {
    "type": "ethernet-networkV4",
    "ethernetNetworkType": "Tagged",
    "name": "Net1",
    "privateNetwork": False,
    "purpose": "General",
    "smartLink": True,
    "connectionTemplateUri": None,
    "vlanId": 401
}

LIGS_TB = {'name': 'LIG2',
           'type': 'logical-interconnect-groupV400',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
                                       ],
           'enclosureIndexes': [1],
           'interconnectBaySet': 3,
           'redundancyType': 'Redundant',
           'uplinkSets': [uplink_sets['us1'].copy()],
           'ethernetSettings': None,
           'state': None,
           'telemetryConfiguration': None,
           'snmpConfiguration': None}

enc_group = [{'name': 'EG2',
              'enclosureCount': 1,
              'powerMode': 'RedundantPowerFeed',
              'ambientTemperatureMode': 'Standard',
              'ipRangeUris': [],
              'ipAddressingMode':'DHCP',
              'enclosureCount': 1,
              'interconnectBayMappings':
              [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG2'},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG2'}]}]

Logical_Enclosure = [{'name': LE,
                      'enclosureUris': ['ENC:' + ENC1],  # REAL
                      'enclosureGroupUri': 'EG:EG2',
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False}]

server_profiles = [{'type': 'ServerProfileV8',
                    'serverHardwareUri': ENC1 + ', bay 6',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC1,
                    'enclosureGroupUri': 'EG:EG2',
                    'serialNumberType': 'Virtual',
                    'macType': 'Virtual',
                    'wwnType': 'Virtual',
                    'name': 'Profile6',
                    'description': '',
                    'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False},
                    'connections': [{'id': 1,
                                     'name': '1',
                                     'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:2',
                                     'requestedMbps': '2500',
                                     'networkUri': 'ETH:Net1'
                                     }]}]

ilo_details = {'ilo_ip': ' 15.245.134.4', 'username': 'Administrator', 'password': 'hpvse123'}

server_details = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse1'}

ic_uri = {'interconnectName': 'CN754406W6, interconnect 6'}

stacking_ports = ['Q7', 'Q8']

port_counters = ['rfc1493Dot1DBasePortDelayExceededDiscards', 'rfc1493Dot1DBasePortMtuExceededDiscards', 'rfc1493Dot1DTpPortInFrames', 'rfc1493Dot1DTpPortOutFrames', 'rfc1493Dot1DPortInDiscards', 'rfc2665Dot3ControlInUnknownOpcodes', 'rfc2665Dot3InPauseFrames', 'rfc2665Dot3OutPauseFrames']
