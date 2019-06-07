def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist

SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password


FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

SWITCH_USERNAME = 'admin'
SWITCH_PASSWORD = 'wpsthpvse1'
SWITCH_PROMPT = '>'
SWITCH_TIMEOUT = 300

IC_SSH_USERNAME = 'root'
IC_TIMEOUT = 100
IC_PROMPT = '>'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
APPLIANCE_IP = '15.186.9.136'
FUSION_IP = '15.186.9.136'
Host = '15.186.9.136'

valDict = {'status_code': 200, 'taskState': 'Completed'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN 106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'portmon.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

ICM_MODEL = 'Virtual Connect SE 32Gb FC Module for Synergy'

INTERCONNECTS = ['MXQ734024N, interconnect 1', 'MXQ734024N, interconnect 4']

partNumber = ['876259-B21']
serialNumber = ['1CG7280012', '1CG728001C']
firmwareVersion = ['4.03.02']
hostName = ['VCFC5-0000010']
sparePartNumber = ['881769-001']
type = ['InterconnectV4']
enclosureType = ['SY12000']
interconnectMAC = ['C4:F5:7C:E8:DA:D4', 'C4:F5:7C:E7:94:E5']
baseWWN = ['10:00:C4:F5:7C:E8:DA:D4', '10:00:C4:F5:7C:E7:94:E5']

ENC1 = 'MXQ734024N'
ICBay = ['1', '4']
Action = ['EFuseOn', 'EFuseOff']
UID_Light_State = ['On', 'Off']
subnet = {'type': 'Subnet',
          'name': 'snet',
          'gateway': '10.233.45.1',
          'networkId': '10.233.45.0',
          'subnetmask': '255.255.255.0',
          'dnsServers': [],
          'domain': 'testdom.com'}

ipv4range = {'type': 'Range',
             'startAddress': '10.233.45.11',
             'endAddress': '10.233.45.20',
             'name': 'test',
             'subnetUri': ' '}

EG1 = 'EG_1'
ip_pool_static = ['10.233.45.11', '10.233.45.12', '10.233.45.13', '10.233.45.14', '10.233.45.15',
                                  '10.233.45.16', '10.233.45.17', '10.233.45.18', '10.233.45.19', '10.233.45.20'
                  ]

enc_group_static = [{'name': 'EG_1',
                     'enclosureCount': 1,
                     'ipAddressingMode': 'IpPool',
                     'ipRangeUris': [],
                     'interconnectBayMappings':[],
                     'ambientTemperatureMode':'Standard',
                     'powerMode': 'RedundantPowerFeed'
                     }]
LE1 = 'LE_1'

LE = {'le1':
      {'name': 'LE_1',
       'enclosureUris': ['ENC:' + ENC1],
       'enclosureGroupUri': 'EG:EG_1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False
       }
      }

enc_groups = {'enc_group_dhcp':
              {'name': 'EG_1',
               'type': 'EnclosureGroupV7',
               'stackingMode': 'Enclosure',
               'enclosureCount': 1,
               'interconnectBayMappings': [],
               'ipAddressingMode': 'DHCP',
               'ipRangeUris': [],
               'ambientTemperatureMode': 'Standard',
               'powerMode': 'RedundantPowerFeed'
               }
              }
