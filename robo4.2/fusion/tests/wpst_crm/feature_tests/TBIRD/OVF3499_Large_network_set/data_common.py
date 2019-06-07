ENC_1 = 'CN754404R1'
ENC_2 = 'CN754406W2'
ENC_3 = 'CN754404R5'
ENC_4 = 'CN754404QX'
ENC_5 = 'CN7544044D'

appliance_ip = '15.245.131.152'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

###
# logical enclosure template
###
les = {
    'name': 'Grow-LE',
}

networks = {
    'namePrefix': 'net',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    "bandwidth": {
        "maximumBandwidth": 50000,
        "typicalBandwidth": 2500
    },
    'type': 'bulk-ethernet-networkV1'
}

telemetry = {
    'type': 'telemetry-configuration',
    'enableTelemetry': False,
    'sampleInterval': 200,
    'sampleCount': 20
}

ethernet_setting = {
    'type': 'EthernetInterconnectSettingsV5',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': False,
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 130,
    'macRefreshInterval': 10
}
