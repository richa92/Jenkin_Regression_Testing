FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'
admin_credentials = {'userName': 'Administrator', 'password': 'Tbird123'}
appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks': [{
                 'macAddress': None,
                 'ipv4NameServers': ['10.15.10.11'],
                 'interfaceName': 'Appliance',
                 'overrideIpv4DhcpDnsServers': False,
                 'activeNode': '1',
                 'confOneNode': True,
                 'ipv4Type': 'DHCP',
                 'ipv4Subnet': '255.255.0.0',
                 'device': 'eth0',
                 'ipv6Type': 'UNCONFIGURE',
                 'unconfigure': False,
                 'aliasDisabled': False,
                 'ipv4Gateway': '10.16.0.1',
                 'hostname': 'newappliance.deafusion.local',
                 'searchDomains': ['deafusion.local'],
                 'ipv6Subnet': '',
             }], }
"""
 This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}
