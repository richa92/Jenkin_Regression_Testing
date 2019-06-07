def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM',
           'startAddress': 'AA:AA:AA:00:00:00', 'endAddress': 'AA:AA:AA:00:00:80', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM',
           'startAddress': '2A:AA:AA:AA:AA:AA:AA:AA', 'endAddress': '2A:AA:AA:AA:AA:AA:AB:29', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM',
           'startAddress': 'VCUAAAAAAA', 'endAddress': 'VCUAAAAADT', 'enabled': True}]

ENC1 = 'WPST-PABA58-EN3'
LE = 'WPST-PABA58-EN3'
LIG1 = 'FEX-LIG1'
LIG2 = 'VC-LIG1'
LSG1 = 'LSG1'
LS1 = 'LS1'
IC1 = ENC1 + ', interconnect 1'
IC2 = ENC1 + ', interconnect 2'
IC3 = ENC1 + ', interconnect 3'
IC4 = ENC1 + ', interconnect 4'
OA_HOST = '15.245.129.78'
OA_USER = 'Administrator'
OA_PASS = 'hpvse1'
SWITCH1 = '15.245.128.170'
SWITCH1_USER = 'admin'
SWITCH1_PASS = 'Wpst@hpvse1#'

PORTS_VAL = {'ports': [
    {'name': '1.1', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 1', 'remotePortId': '1'},
     'portStatus': 'Linked'},
    {'name': '1.2', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 1', 'remotePortId': '2'},
     'portStatus': 'Linked'},
    {'name': '1.3', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.4', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.5', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 4', 'remotePortId': 'X1'},
     'portStatus': 'Linked'},
    {'name': '1.6', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.7', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 4', 'remotePortId': 'X2'},
     'portStatus': 'Linked'},
    {'name': '1.8', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.9', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.10', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.11', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 3', 'remotePortId': 'X4'},
     'portStatus': 'Linked'},
    {'name': '1.12', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.13', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 2', 'remotePortId': '2'},
     'portStatus': 'Linked'},
    {'name': '1.14', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 2', 'remotePortId': '1'},
     'portStatus': 'Linked'},
    {'name': '1.15', 'neighbor': {}, 'portStatus': 'Linked'},
    {'name': '1.16', 'neighbor': {}, 'portStatus': 'Linked'},
    {'name': '1.17', 'neighbor': {}, 'portStatus': 'Linked'},
    {'name': '1.18', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.19', 'neighbor': {'linkLabel': None, 'remotePortId': 'X2'}, 'portStatus': 'Linked'},
    {'name': '1.20', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.21', 'neighbor': {}, 'portStatus': 'Linked'},
    {'name': '1.22', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.23', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.24', 'neighbor': {'linkLabel': 'WPST-PABA58-EN3, interconnect 3', 'remotePortId': 'X3'},
     'portStatus': 'Linked'},
    {'name': '1.25', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.26', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.27', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.28', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.29', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.30', 'neighbor': {}, 'portStatus': 'Unlinked'},
    {'name': '1.31', 'neighbor': {}, 'portStatus': 'Linked'},
    {'name': '1.32', 'neighbor': {}, 'portStatus': 'Linked'}]}

"""
IP 15.199.230.78
User- Administrator
Password- hpvse1

Nexus 5548 (Nexus-1)
IP- 15.199.230.70
DNS- nexus-1.usa.hp.com
User- admin
Password- Wpst@hpvse1#

FEX 1: port 1 -> Nexus port 1
FEX 1: port 2 -> Nexus port 2

FEX2: port 1 -> Nexus port 14
FEX2: port 2 -> Nexus port 13


"""
appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'LIT',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'f748-f750.rdlabs.hpecorp.net',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True,
                   }],
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

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

licenses = [{
    'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
    {
        'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
]

enc_groups = [{'name': 'EG',
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:FEX-LIG1'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:FEX-LIG1'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:VC-LIG1'},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:VC-LIG1'},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}
              ]

encs = [{'hostname': OA_HOST, 'username': OA_USER, 'password': OA_PASS, 'enclosureGroupUri': 'EG:EG', 'force': False,
         'licensingIntent': 'OneViewNoiLO'}]

lsgs = [{'name': LSG1,
         'type': 'logical-switch-groupV4',
         'switchMapTemplate': {'switchMapEntryTemplates': [
             {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
              'permittedSwitchTypeUri': 'SWT:Cisco Nexus 55xx'}]}}
        ]

lss = [{"logicalSwitch": {"name": LS1, "state": "Active", "type": "logical-switchV4", "managementLevel": "MONITORED",
                          "logicalSwitchGroupUri": "LSG:" + LSG1,
                          "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "public"},
                                                             "snmpV3Configuration": {"authorizationProtocol": None,
                                                                                     "privacyProtocol": None,
                                                                                     "securityLevel": None},
                                                             "logicalSwitchManagementHost": SWITCH1,
                                                             "snmpVersion": "SNMPv1", "snmpPort": 161}]},
        "logicalSwitchCredentials": [{"connectionProperties": [
            {"propertyName": "SshBasicAuthCredentialUser", "value": SWITCH1_USER, "valueFormat": "Unknown",
             "valueType": "String"}, {"propertyName": "SshBasicAuthCredentialPassword", "value": SWITCH1_PASS,
                                      "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ligs = [{'name': 'FEX-LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Cisco Fabric Extender for HP BladeSystem'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'Cisco Fabric Extender for HP BladeSystem'}],
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': 'VC-LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}],
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}]
