FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hponeview'
admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}
appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks': [{
                 'macAddress': None,
                 'interfaceName': 'Appliance',
                 'overrideIpv4DhcpDnsServers': False,
                 'activeNode': '1',
                 'confOneNode': True,
                 'ipv4Type': 'STATIC',
                 'ipv4Subnet': '255.255.0.0',
                 'device': 'eth0',
                 'ipv6Type': 'UNCONFIGURE',
                 'unconfigure': False,
                 'aliasDisabled': False,
                 'ipv4Gateway': '10.34.0.1',
                 'hostname': 'bfs1034.dom1034.net',
                 'searchDomains': ['dom1034.net'],
             }], }
"""
 This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}
