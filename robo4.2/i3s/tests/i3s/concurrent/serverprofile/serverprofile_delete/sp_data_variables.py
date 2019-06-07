from winnt import NULL
from requests.api import patch


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

subnet = [{'type': 'Subnet',
           'gateway': '192.168.0.1',
           'networkId': '192.168.0.0',
           'subnetmask': '255.255.0.0',
           'dnsServers': [                          
                    ],
            'domain': 'vse.rdlabs.hpecorp.net'},   
          
          {'type': 'Subnet',
           'gateway': '15.212.168.1',
           'networkId': '15.212.168.0',
           'subnetmask': '255.255.252.0',
           'dnsServers': [
                    '16.110.135.51'
                        ],
            'domain': 'vse.rdlabs.hpecorp.net'}     
]
range_enable = [{'type': 'Range',
                 'enabled': 'true'}
                ]
range_disable = [{'type': 'Range',
                  'enabled': 'false'}
                 ]

ipv4ranges = [{'type': 'Range',
               'startAddress': '192.168.20.10',
               'endAddress': '192.168.20.50',
               'name': 'iscsi_nw',
               'subnetUri': ' '},              
              {'type': 'Range',
               'startAddress': '15.212.170.61',
               'endAddress': '15.212.170.63',
               'name': 'mgmt_nw',
               'subnetUri': ' '}
              ]

Ethernet_network_1 = [
    {'vlanId': '149',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose':'ISCSI',
     'name':'iscsi_nw',
     'smartLink': False,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '0',
     'ethernetNetworkType': 'Untagged',
     'subnetUri': '',
     'purpose': 'Management',
     'name': 'mgmt_nw',
     'smartLink': False,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'}
]

lig_tbird_1enc = {'type':'logical-interconnect-groupV300',
'ethernetSettings':{'type':'EthernetInterconnectSettingsV201','enableIgmpSnooping':False,'igmpIdleTimeoutInterval':260,'enableFastMacCacheFailover':True,'macRefreshInterval':5,'enableNetworkLoopProtection':True,'enablePauseFloodProtection':True,'enableRichTLV':False,'interconnectType':'Ethernet','dependentResourceUri':None,'name':'defaultEthernetSwitchSettings','category':None,'uri':'/ethernetSettings'},
'description':None,
'name':'LIG-1enc',
'interconnectMapTemplate':
{'interconnectMapEntryTemplates':[
{'logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Enclosure','relativeValue':1}]},'permittedInterconnectTypeUri':'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23','enclosureIndex':1}]},
'enclosureType':'SY12000',
'enclosureIndexes':[1],
'interconnectBaySet':'3',
'redundancyType':'NonRedundantASide',
'internalNetworkUris':[],
'snmpConfiguration':{'type':'snmp-configuration','readCommunity':'public','systemContact':'','trapDestinations':None,'snmpAccess':None,'enabled':True,'description':None,'name':None,'state':None,'category':'snmp-configuration'},
'qosConfiguration':None,
'uplinkSets':[
{'networkUris':['iscsi_nw'],'mode':'Auto','lacpTimer':'Short','primaryPort':None,
'logicalPortConfigInfos':[{'desiredSpeed':'Auto','logicalLocation':{'locationEntries':[{'type':'Bay','relativeValue':3},{'type':'Port','relativeValue':62},{'type':'Enclosure','relativeValue':1}]}}],
'networkType':'Ethernet','ethernetNetworkType':'Tagged','name':'iscsi_nw'}
]
}

enc_groups_tbird_1enc = [{'name': 'EG-1enc',
'type': 'EnclosureGroupV300',
'enclosureTypeUri': '/rest/enclosure-types/SY12000',
'stackingMode': 'Enclosure',
'ipAddressingMode': 'External',
'ipRangeUris': [],
'interconnectBayMappingCount': 1,
'enclosureCount': 1,
'configurationScript': None,
'osDeploymentSettings':{'manageOSDeployment':True,'deploymentModeSettings':{'deploymentMode':'Unmanaged','deploymentNetworkUri': ['iscsi_nw']}},
'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-1enc'},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
                             ]},
{'name': 'enc_groups_2enc',
'type': 'EnclosureGroupV300',
'enclosureTypeUri': '/rest/enclosure-types/SY12000',
'stackingMode': 'Enclosure',
'ipAddressingMode': 'External',
'ipRangeUris': [],
'interconnectBayMappingCount': 1,
'enclosureCount': 1,
'configurationScript': None,
'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-1enc'},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
                             ]}]


les_1enc = {'name': 'LE-1enc',
            'enclosureUris': ['ENC:7U86XMVH6T'],  # 1 ENCL
            'enclosureGroupUri': 'EG:EG-1enc',
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }

osdeploymentserver = { 'name' : 'OSDS-1enc',
'description': 'os deployment server',
'applianceUri':'7U86XMVH6T,CIM bay2',
'mgmtNetworkUri':['mgmt_nw'],
'deplManagersType':'Image Streamer'
}

serverprofile_1enc = [{'type':'ServerProfileV6',
'name':'i3s_serverprofile_1',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : '7U86XMVH6T, bay 1',
'serverHardwareTypeUri' : 'SY 480 Gen9 1',
'enclosureGroupUri': 'EG-2potash',
'enclosureUri':'7U86XMVH6T',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_for_e2e_test',
'osCustomAttributes':[{'name': 'DomainName', 'value': 'vse.rdlabs.hpecorp.net'},{'name': 'hostname', 'value': 'bay1'}],
                      'osVolumeUri':None},              
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:1-a','requestedVFs':'Auto','allocatedVFs':24,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'boot':{'priority':'Primary','initiatorNameSource':'ProfileInitiatorName','bootVolumeSource':'ManagedVolume','chapLevel':'None'}
}],
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':[]},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False}
},
{'type':'ServerProfileV6',
'name':'i3s_serverprofile_2',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : '7U86XMVH6T, bay 3',
'serverHardwareTypeUri' : 'SY 480 Gen9 1',
'enclosureGroupUri': 'EG-2potash',
'enclosureUri':'7U86XMVH6T',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_for_e2e_test',
'osCustomAttributes':[{'name': 'DomainName', 'value': 'vse.rdlabs.hpecorp.net'},{'name': 'hostname', 'value': 'bay3'}],
                      'osVolumeUri':None},              
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:1-a','requestedVFs':'Auto','allocatedVFs':24,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'boot':{'priority':'Primary','initiatorNameSource':'ProfileInitiatorName','bootVolumeSource':'ManagedVolume','chapLevel':'None'}
}],
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':[]},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False}
},
{'type':'ServerProfileV6',
'name':'i3s_serverprofile_3',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : '7U86XMVH6T, bay 6',
'serverHardwareTypeUri' : 'SY 660 Gen9 1',
'enclosureGroupUri': 'EG-2potash',
'enclosureUri':'7U86XMVH6T',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_for_e2e_test',
'osCustomAttributes':[{'name': 'DomainName', 'value': 'vse.rdlabs.hpecorp.net'},{'name': 'hostname', 'value': 'bay6'}],
                      'osVolumeUri':None},              
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:1-a','requestedVFs':'Auto','allocatedVFs':24,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'boot':{'priority':'Primary','initiatorNameSource':'ProfileInitiatorName','bootVolumeSource':'ManagedVolume','chapLevel':'None'}
}],
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':[]},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False}
},
{'type':'ServerProfileV6',
'name':'i3s_serverprofile_4',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : '7U86XMVH6T, bay 7',
'serverHardwareTypeUri' : 'SY 480 Gen9 1',
'enclosureGroupUri': 'EG-2potash',
'enclosureUri':'7U86XMVH6T',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_for_e2e_test',
'osCustomAttributes':[{'name': 'DomainName', 'value': 'vse.rdlabs.hpecorp.net'},{'name': 'hostname', 'value': 'bay7'}],
                      'osVolumeUri':None},              
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:1-a','requestedVFs':'Auto','allocatedVFs':24,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'boot':{'priority':'Primary','initiatorNameSource':'ProfileInitiatorName','bootVolumeSource':'ManagedVolume','chapLevel':'None'}
}],
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':[]},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False}
}]

serverprofile_1enc_old = {'type':'ServerProfileV6',
'name':'i3s_serverprofile_for_SE',
'iscsiInitiatorNameType':'AutoGenerated',
'serverHardwareUri' : '7U86XMVH6T, bay 7',
'serverHardwareTypeUri' : 'SY 480 Gen9 1',
'enclosureGroupUri': 'EG-2potash',
'enclosureUri':'7U86XMVH6T',
'affinity':'Bay',
'hideUnusedFlexNics':True,
'firmware':{'firmwareInstallType': None,'forceInstallFirmware':False,'manageFirmware':False,'firmwareBaselineUri':None},
'macType':'Virtual',
'wwnType':'Virtual',
'osDeploymentSettings':{'osDeploymentPlanUri':'oedp_deploy_for_e2e_test',
'osCustomAttributes':[{'name': 'DomainName', 'value': 'vse.rdlabs.hpecorp.net'},{'name': 'hostname', 'value': 'bay7'}],
                      'osVolumeUri':None},              
'connections':[
{'id':1,'name':'Deployment Network A','functionType':'Ethernet','networkUri':['iscsi_nw'],
'portId':'Mezz 3:1-a','requestedVFs':'Auto','allocatedVFs':24,'macType':'Virtual','wwpnType':'Virtual','mac':'','requestedMbps':'2500',
'allocatedMbps':2500,'maximumMbps':20000,
'boot':{'priority':'Primary','initiatorNameSource':'ProfileInitiatorName','bootVolumeSource':'ManagedVolume','chapLevel':'None'}
}],
'bootMode':{'manageMode':True,'pxeBootPolicy':'Auto','mode':'UEFIOptimized'},
'boot':{'manageBoot':True,'order':[]},
'bios':{'manageBios':False,'overriddenSettings':[]},
'localStorage':{},
'sanStorage':{'volumeAttachments':[],'manageSanStorage':False}
}


BLADES = {'Blade1'    :    '7U86XMVH6T, bay 7'}