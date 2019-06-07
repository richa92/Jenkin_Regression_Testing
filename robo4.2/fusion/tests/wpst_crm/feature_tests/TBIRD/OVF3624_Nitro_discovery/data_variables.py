def rlist(start, end, prefix='net_', suffix='', step=1):
    l = []
    for x in xrange(start, end + 1, step):
        l.append('%s%s%s' % (prefix, str(x), suffix))
    return l


feature_toggle = '/ci/bin/set-feature-toggles -e OVF1773_Nitro_ICM_Support -e OVF1776_MethaneDiscovery  \
                 -e OVF2128_NitoMethane_ILT_Support'

SSH_PASS = 'hpvse1'
interface = 'bond0'
FUSION_USERNAME = 'Administrator'  # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'  # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'  # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'  # Fusion SSH Password
FUSION_PROMPT = '#'  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180  # Timeout.  Move this out???
FUSION_NIC = 'bond0'  # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

EG1 = 'EG1'

ENC1 = 'MXQ71902DQ'

LE1 = 'LE1'

LIG1 = 'LIG-IBS1-Aside'
LIG2 = 'LIG-IBS2-Aside'
LIG3 = 'LIG-IBS3-Aside'

NITRO_MODEL = 'Virtual Connect SE 100Gb F32 Module for Synergy'
NITRO_PART = '867796-B21'

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


ligs = {
    LIG1: {'name': LIG1,
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                'enclosureIndex': 1},
           ],
           'enclosureIndexes': [1],
           'interconnectBaySet': 1,
           'redundancyType': 'NonRedundantASide',
           'uplinkSets': []
           },
    LIG2: {'name': LIG2,
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                'enclosureIndex': 1},
           ],
           'enclosureIndexes': [1],
           'interconnectBaySet': 2,
           'redundancyType': 'NonRedundantASide',
           'uplinkSets': []
           },
    LIG3: {'name': LIG3,
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                'enclosureIndex': 1},
           ],
           'enclosureIndexes': [1],
           'interconnectBaySet': 3,
           'redundancyType': 'NonRedundantASide',
           'uplinkSets': []
           },

}

enc_groups = {EG1: {'name': EG1,
                    'enclosureCount': 1,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG3},
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
