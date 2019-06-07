
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

appliance = {"type": "ApplianceNetworkConfiguration",
             "applianceNetworks": [
                 {"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.213.41", "app1Ipv6Addr": "",
                  "app2Ipv4Addr": "16.114.213.42", "app2Ipv6Addr": "",
                  "virtIpv4Addr": "16.114.213.40", "virtIpv6Addr": None, "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                  "app2Ipv4Alias": None, "app2Ipv6Alias": None,
                  "hostname": "ci-005056b402db-Guthrey-Natasha.vse.rdlabs.hpecorps.net",
                  "confOneNode": True, "interfaceName": "", "macAddress": None,
                  "ipv4Type": "STATIC", "ipv6Type": "UNCONFIGURE", "overrideIpv4DhcpDnsServers": False,
                  "ipv4Subnet": "255.255.240.0", "ipv4Gateway": "16.114.208.1", "ipv6Subnet": None, "ipv6Gateway": None,
                  "domainName": "vse.rdlabs.hpecorp.net", "searchDomains": [],
                  "ipv4NameServers": ["16.125.25.81", "16.125.25.82"],
                  "ipv6NameServers": ["16.125.25.81", "16.125.25.82"], "bondedTo": None, "aliasDisabled": True,
                  "configureRabbitMqSslListener": False, "configurePostgresSslListener": False,
                  "webServerCertificate": None, "webServerCertificateChain": None, "webServerCertificateKey": None}
             ],
             "serverCertificate": {"rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
                                   "rabbitMQCertificateKey": None, "postgresCertificate": None,
                                   "postgresRootCACertificate": None, "postgresCertificateKey": None}
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66102'

enclosures_monitored = [
    {
        "type": "EnclosureV300",
        "name": ENC1,
        "state": "Monitored",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "interconnectBays":
        [
            {"bayNumber": 1, "interconnectModel": "HPE Synergy 12Gb SAS Connection Module"},
            {"bayNumber": 2, "interconnectModel": None},
            {"bayNumber": 3, "interconnectModel": "HP VC SE 40Gb F8 Module"},
            {"bayNumber": 4, "interconnectModel": "HPE Synergy 12Gb SAS Connection Module"},
            {"bayNumber": 5, "interconnectModel": None},
            {"bayNumber": 6, "interconnectModel": "HP VC SE 40Gb F8 Module"}
        ]
    },
    {
        "type": "EnclosureV300",
        "name": ENC2,
        "state": "Monitored",
        "interconnectBays":
        [
            {"bayNumber": 1, "interconnectModel": "HPE Synergy 12Gb SAS Connection Module"},
            {"bayNumber": 2, "interconnectModel": None},
            {"bayNumber": 3, "interconnectModel": "HP VC SE 40Gb F8 Module"},
            {"bayNumber": 4, "interconnectModel": "HPE Synergy 12Gb SAS Connection Module"},
            {"bayNumber": 5, "interconnectModel": None},
            {"bayNumber": 6, "interconnectModel": "HP VC SE 40Gb F8 Module"}
        ]
    },
    {
        "type": "EnclosureV300",
        "name": ENC3,
        "state": "Monitored",
        "interconnectBays":
        [
            {"bayNumber": 1, "interconnectModel": "HPE Synergy 12Gb SAS Connection Module"},
            {"bayNumber": 2, "interconnectModel": None},
            {"bayNumber": 3, "interconnectModel": "HP VC SE 40Gb F8 Module"},
            {"bayNumber": 4, "interconnectModel": "HPE Synergy 12Gb SAS Connection Module"},
            {"bayNumber": 5, "interconnectModel": None},
            {"bayNumber": 6, "interconnectModel": "HP VC SE 40Gb F8 Module"}
        ]
    }
]
