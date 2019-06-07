admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# portStatus
LINKED = 'Linked'
UNLINKED = 'Unlinked'

# portStatusReason
MODULEINCOMPATIBE = 'ModuleIncompatible'
LOGGEDIN = 'LoggedIn'
NOTLOGGEDIN = 'NotLoggedIn'
FABRICMISMATCH = 'FabricTypeMismatch'
UNKNOWN = 'Unknown'

# Wait time for reaching stable state
SERVER_BOOT_WAIT = '8min'
BFS_SERVER_BOOT_WAIT = '15min'
UPLINK_STATUS_WAIT = '2min'
UPLINK_SHORT_WAIT = '60s'

UPLINK_SPEED_WAIT = '3min'
# UPLINK_SPEED_WAIT = '60s'

# 0 sec is not enough for nameServer to be updated after enable back downlink
SUBPORT_STATUS_WAIT = '240s'
CONN_DEPLOY_WAIT = '300s'

# FA environment
REMOVE_IC_WAIT = '90s'
POWEROFF_IC_WAIT = '120s'
ADD_PORT_WAIT = '240s'

OPSPEED8 = 'Speed8G'
OPSPEED4 = 'Speed4G'

# Resource not available (status 503). remove ICM scenario. HA sync and nameServers, 300s not enough
# OVD5732
REMOVE_IC_NS_WAIT = '12min'

CHLORIDE10 = 'CL10'
CHLORIDE20 = 'CL20'

# Server Profile total requested BW of all connections cannot exceed the Chloride bandwidth,
# otherwise SP creation will fail with BW_TOTAL_LINKRATE_OVERFLOW_ERROR
# In F118 and F117 tests, all server profiles has max of 1 enet connection and 2 FC connections


def getEnetRBW(cl_type):
    rbw = '2500'
    if cl_type == CHLORIDE10:
        rbw = '1000'
    return rbw


def getFcRBW(cl_type):
    rbw = '8000'
    if cl_type == CHLORIDE10:
        rbw = '4000'
    return rbw


ethernet_networks = [{'name': 'wpstnetwork1',
                      'type': 'ethernet-networkV4',
                      'vlanId': '401',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'wpstnetwork2',
                      'type': 'ethernet-networkV4',
                      'vlanId': '402',
                      'purpose': 'Management',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}
                     ]

fc_networks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': False,
                'name': 'FA2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA3',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA4',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA5',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA101',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA102',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'FAM1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA3',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA4',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA5',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'}
               ]
