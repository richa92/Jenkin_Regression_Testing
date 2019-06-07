FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hponeview'
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks': [{
                 'macAddress': None,
                 'ipv4NameServers': ['16.125.25.82'],
                 "virtIpv4Addr":'16.114.219.35',
                 'interfaceName': 'Appliance',
                 'overrideIpv4DhcpDnsServers': False,
                 'activeNode': '1',
                 'confOneNode': True,
                 'ipv4Type': 'STATIC',
                 'ipv4Subnet': '255.255.240.0',
                 'device': 'eth0',
                 'ipv6Type': 'UNCONFIGURE',
                 'unconfigure': False,
                 'aliasDisabled': False,
                 'ipv4Gateway': '16.114.208.1',
                 'hostname': 'DCSTbird.vse.rdlabs.hpecorp.net',
                 'searchDomains': ['vse.rdlabs.hpecorp.net'],
             }]}
"""
 This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}
