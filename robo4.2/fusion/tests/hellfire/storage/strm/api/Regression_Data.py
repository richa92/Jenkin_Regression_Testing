from robot.libraries.BuiltIn import BuiltIn

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

svmc_credentials = {"username": "dan", "password": "hpinvent"}

oa_credentials = {'username': 'dcs', 'password': 'dcs'}

APP1_IPV4_ADDRESS = BuiltIn().get_variable_value("${APPLIANCE_IP}")
HOSTNAME = "Hellfire-SVMC-Regression"

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'Appliance',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'app1Ipv4Addr': APP1_IPV4_ADDRESS,
                   'ipv6Type': 'UNCONFIGURE',
                   'ipv4Subnet':'255.255.240.0',
                   'ipv4Gateway':'16.114.208.1',
                   'hostname': HOSTNAME,
                   'confOneNode': True,
                   'domainName': 'vse.rdlabs.hpecorp.net',
                   'ipv4NameServers':['16.125.25.81','16.125.25.82','16.125.24.20'],
                   'aliasDisabled': True}]}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

licenses = [
    {'key': 'QCLE C9MA H9PA 8HV3 V7B5 HWWB Y9JL KMPL D4KG MEZA DXAU 2CSM GHTG L762 B57Z GLJM KJVT D5KM EFRW DS5R DQEM 7ZS2 9K2P 3E22 LKAG LUVR TZZP MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424669494 HPOV-NFR1 HP_OneView_16_Seat_NFR ADEJAYTJC7YC"_3JJKW-KM6WK-KZ45Y-V6789-9Q5J6'},
    {'key': 'YC3G A9MA H9P9 KHW3 U7B5 HWW5 Y9JL KMPL F42C PEJA DXAU 2CSM GHTG L762 AB36 XJZU KJVT D5KM EFRW DS5R FQU9 6ZC2 9K2P 3E22 LKAG LUVR TZZX MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424669495 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 3GJ9AYTJ275U"'},
]


# StoreVirtual
STOREVIRTUAL1_NAME = 'VSA160_Storage_Pool'
STOREVIRTUAL1_HOSTNAME = '15.116.1.163'
STOREVIRTUAL1_VIP = '15.116.1.163'
STOREVIRTUAL1_POOL = 'VSA160_Storage_Pool'
STOREVIRTUAL_SVMC1_IP = '15.116.0.220'
STOREVIRTUAL1_MGMT_GRP_ID = '' 
VSA1_STORAGE_PATH_TARGET_NAME_REGEX = 'REGEX:iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:\d*:'     

HELLFIRE_API = 400
NAME_PREFIX = 'hellfire-reg1-'
# Storage volumes
VOLUME_NAME_PREFIX = NAME_PREFIX
# Pre-existing volumes in storage systems
VOLUME_EXIST_VSA1_SHARED = VOLUME_NAME_PREFIX+'vsa1-exist-shared'
VOLUME_EXIST_VSA1_PRIV = VOLUME_NAME_PREFIX+'vsa1-exist-priv'

VOLUME_VSA1_SHARED = VOLUME_NAME_PREFIX+'vsa1-shared'
VOLUME_PRIVATE_VSA2 = VOLUME_NAME_PREFIX+'vsa2-private'
VOLUME_VSA1_NAME_CHANGE = VOLUME_VSA1_SHARED + "-CHG" 
VOLUME_VSA2_NAME_CHANGE = VOLUME_PRIVATE_VSA2 + "-CHG"

storage_system = {'family':'StoreVirtual', 'hostname':STOREVIRTUAL1_HOSTNAME,
    'username':'dan','password':'hpinvent',
      'deviceSpecificSettings': {'svmcIP': 'NONE', 'managementGroupId': 'NONE'} 
       }

storage_system_put = {'type':'StorageSystemV4','name': STOREVIRTUAL1_NAME , "family":"StoreVirtual",
                     "hostname":STOREVIRTUAL1_HOSTNAME,"credentials":{"username":"admin","password":'admin'},
                     "ports":[{
                       "name": STOREVIRTUAL1_HOSTNAME,
                       "expectedNetworkUri": "ETH:networke",
                        "expectedNetworkName": "networke",
                        "mode": "Managed",},],
                      }
                 

volume = {"name":VOLUME_VSA1_NAME_CHANGE}

#vsa to be attached to svmc
svmc_vsa = {'address': STOREVIRTUAL1_HOSTNAME,'administratorUserName':'admin','administratorPassword':'admin'}
svmc_auth = {"Authorization": "Basic ZGFuOmhwaW52ZW50", "Content-Type":"application/json", "Accept":"application/json"}
svmcdevice = {}

storage_volumes = [

    {"properties":{"name":VOLUME_VSA1_SHARED,"description":"","storagePool":STOREVIRTUAL1_POOL,
                   "size":1073741824,"dataProtectionLevel":"NetworkRaid5SingleParity","provisioningType":"Thin",
                   "isShareable":True,"isAdaptiveOptimizationEnabled":True},
     "templateUri":"ROOT","isPermanent":True,
    },
    {"properties":{"name":VOLUME_PRIVATE_VSA2,"description":"","storagePool":STOREVIRTUAL1_POOL,
                   "size":1073741824,"dataProtectionLevel":"NetworkRaid5SingleParity","provisioningType":"Thin",
                   "isShareable":False,"isAdaptiveOptimizationEnabled":True},
     "templateUri":"ROOT","isPermanent":True,
    },


]

existing_storage_volumes = [
    {"name":VOLUME_EXIST_VSA1_SHARED, 'description':'', 'storageSystemUri':STOREVIRTUAL1_NAME, 'deviceVolumeName':VOLUME_EXIST_VSA1_SHARED, 'isShareable':True},
    {"name":VOLUME_EXIST_VSA1_PRIV, 'description':'', 'storageSystemUri':STOREVIRTUAL1_NAME, 'deviceVolumeName':VOLUME_EXIST_VSA1_PRIV, 'isShareable':False},
]


#### SAN Manager and Managed SANs
san_managers = [{'connectionInfo': [{'name': 'Type', 'value': 'Brocade Network Advisor'},
                                    {'name': 'Host', 'value': '172.18.15.1'},
                                    {'name': 'Port', 'value': 5989},
                                    {'name': 'Username', 'value': 'dcs'},
                                    {'name': 'Password', 'value': 'dcs'},
                                    {'name': 'UseSsl', 'value': True}]    }

                ]

FA_SAN_A = 'SAN1_0'
FA_SAN_B = 'SAN1_1'
FA_A = '/rest/fc-networks/' + FA_SAN_A
FA_B = '/rest/fc-networks/' + FA_SAN_B
DA_A = '/rest/fc-networks/NetworkDA1'
DA_B = '/rest/fc-networks/NetworkDA2'
ETH_A = '/rest/ethernet-networks/networke'

#### Enclosures, Interconnects, Server Hardware, Networks, ULS, LIG, and EG
## Enclosures
ENC2 = 'Encl2'
ENC2_OA1 = "172.18.1.13"

## Interconnects
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

## Server Hardware

ENC2SHBAY1  = '%s, bay 1' % ENC2
ENC2SHBAY2  = '%s, bay 2' % ENC2
ENC2SHBAY3  = '%s, bay 3' % ENC2
ENC2SHBAY4  = '%s, bay 4' % ENC2
ENC2SHBAY5  = '%s, bay 5' % ENC2
ENC2SHBAY6  = '%s, bay 6' % ENC2
ENC2SHBAY7  = '%s, bay 7' % ENC2

## LIGs and EGs
LIG1_NAME = 'LIG22'
EG2_NAME = 'EG22'

## Server profiles
PROFILE_NAME_PREFIX = "c7000-reg1-"
PROFILE1_NAME = PROFILE_NAME_PREFIX + "profile1"
PROFILE1_IQN = "iqn.2015-02.com.hpe:oneview-" + PROFILE1_NAME
PROFILE1_IQN_EDIT = "iqn.2015-02.com.hpe:oneview-" + PROFILE1_NAME + '-new'
VOLUME_VSA1_SHARED = VOLUME_NAME_PREFIX+'vsa1-shared'
VOLUME_PRIVATE_VSA2 = VOLUME_NAME_PREFIX+'vsa2-private'

## profiles server, EG, and ENC
PROFILE1_SERVER = ENC2SHBAY1
PROFILE1_EG = EG2_NAME
PROFILE1_ENC = ENC2
PROFILE1_HARDWARE_TYPE = "BL660c Gen9 1"
NEW_RHE = "Windows 2012 / WS2012 R2"


ethernet_networks = [

                    {'name': 'networke',
                      'type': 'ethernet-networkV300',
                      'vlanId': 0,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'}
                     
                     ]


network_sets = [{'name': 'NS1', 'type': 'network-setV300', 'networkUris': ['net100','net300'], 'nativeNetworkUri': 'net100'},]

fc_networks = [
   {'name': 'networksan0', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + FA_SAN_A},
   {'name': 'networksan1', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + FA_SAN_B},
   {'name': 'networkDA1', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None,'managedSanUri': None},
   {'name': 'networkDA2', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'DirectAttach', 'connectionTemplateUri': None,'managedSanUri': None}
]

ligs = [{'name': LIG1_NAME,
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                                     
                                     ],
         'uplinkSets': [{'name': 'uplinke',
                         'ethernetNetworkType': 'Untagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['networke'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'},{'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]},

                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        
    ]

enc_groups = [{'name': EG2_NAME,
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' +LIG1_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' +LIG1_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               }
              
]

enclosures = [
    {'hostname': ENC2_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:'+EG2_NAME,
         'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri' : None } 

   
]


profile1_create = {
    "type":"ServerProfileV400","name":PROFILE1_NAME,"description":"",  
    "serverHardwareUri":'SH:'+PROFILE1_SERVER,
    "serverHardwareTypeUri":'SHT:'+PROFILE1_HARDWARE_TYPE,  
    "enclosureGroupUri":'EG:'+PROFILE1_EG,"enclosureUri":'ENC:'+PROFILE1_ENC,
    "iscsiInitiatorNameType":"AutoGenerated","iscsiInitiatorName":PROFILE1_IQN,
    "serialNumberType":"Virtual","macType":"Virtual","wwnType":"Virtual","affinity":"Bay",
    "hideUnusedFlexNics":True,"osDeploymentSettings":None,
    "connections":[
         {"id":1,"name":"","state": "Deployed","functionType":"Ethernet","portId":"Flb 1:1-a","requestedMbps":"2500","networkUri":"ETH:networke",}
     ],
    "boot":{"manageBoot":False},"bootMode":None,   
    "firmware":{"manageFirmware":False,"firmwareBaselineUri":None,"forceInstallFirmware":False,"firmwareInstallType":None},
    "bios":{"manageBios":False,"overriddenSettings":[]},
    "localStorage":{"sasLogicalJBODs":[],"controllers":[]},
    "sanStorage":{"manageSanStorage":True, "hostOSType":NEW_RHE,
        "volumeAttachments":[
            {"id":1,"state": "VolumeCreating","volumeUri":"SVOL:"+VOLUME_VSA1_SHARED,"isBootVolume":False,"lunType":"Auto",   
             "storagePaths":[
                 {"isEnabled":True,"connectionId":1,"targetSelector":"Auto",
                  "targets":[]},
                    
                 ]
             },
            {"id":2,"state": "VolumeCreating","volumeUri":"SVOL:"+VOLUME_PRIVATE_VSA2,"isBootVolume":False,"lunType":"Auto",   
             "storagePaths":[
                 {"isEnabled":True,"connectionId":1,"targetSelector":"Auto",
                  "targets":[]},
                    
                 ]
             }
            
        ],
        "sanSystemCredentials":
            [ ],
          
    }
}   
                     