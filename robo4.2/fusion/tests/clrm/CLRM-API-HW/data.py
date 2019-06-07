FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hponeview'
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks': [{'macAddress': None,
                                    'ipv4NameServers': ['10.10.0.22'],
                                    "virtIpv4Addr": '16.114.0.0',
                                    'interfaceName': 'Appliance',
                                    'overrideIpv4DhcpDnsServers': False,
                                    'activeNode': '1',
                                    'confOneNode': True,
                                    'ipv4Type': 'STATIC',
                                    'ipv4Subnet': '255.255.252.0',
                                    'device': 'eth0',
                                    'ipv6Type': 'UNCONFIGURE',
                                    'unconfigure': False,
                                    'aliasDisabled': False,
                                    'ipv4Gateway': '16.114.208.1',
                                    'hostname': 'clrm.cisl.rdlabs.hpecorp.net',
                                    'searchDomains': ['vse.rdlabs.hpecorp.net'],
                                    }]}
"""
 This is the time and locale settings used during FTS.
"""
timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}
FEATURE_TOGGLES = ["OVF206_HypervisorManager_SBAC", "OVF205_ClusterProfileSBAC", "OVF217_CentralizedScope", "OVF2_SBAC_Core", "API_Version_600", "OVF167_Scope_Admin_Roles", "OVF23_ScopeRestrictionsEnabledPerCategory", "OVF218_Server_Profile_Roles", "OVF1160_Server_Profile_Architect_Role", "OVF1563_ClusterProfilesUI", "OVF1040_CLRM_Enable_Public_API"]
