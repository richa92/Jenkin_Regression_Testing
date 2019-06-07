from robot.libraries.BuiltIn import BuiltIn

# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV4'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
STORAGE_VOLUME_TYPE = 'StorageVolumeV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV5'
SERVER_PROFILE_TYPE = 'ServerProfileV9'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'

# OA
OVF91_ENC = 'wpst11'
OVF91_ENC_OA1 = "wpst11-oa1.vse.rdlabs.hpecorp.net"
# LIG and EG
OVF91_LIG = 'OVF91_LIG'
OVF91_EG = 'OVF91_EG'

ligs = [
    {'name': OVF91_LIG,
     'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
     'enclosureType': 'C7000',
     'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                 {'enclosure': 1,
                                  'enclosureIndex': 1,
                                  'bay': 2,
                                  'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                 {'enclosure': 1,
                                  'enclosureIndex': 1,
                                  'bay': 3,
                                  'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                 {'enclosure': 1,
                                  'enclosureIndex': 1,
                                  'bay': 4,
                                  'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                 {'enclosure': 1,
                                  'enclosureIndex': 1,
                                  'bay': 5,
                                  'type': 'HP VC 8Gb 24-Port FC Module'},
                                 {'enclosure': 1,
                                  'enclosureIndex': 1,
                                  'bay': 6,
                                  'type': 'HP VC 8Gb 24-Port FC Module'},
                                 ],
     'uplinkSets': [],
     'stackingMode': 'Enclosure',
     'ethernetSettings': None,
     'state': 'Active',
     'telemetryConfiguration': None,
     'snmpConfiguration': None},
]

enc_groups = [
    {'name': OVF91_EG,
     'configurationScript': None,
     'interconnectBayMappings':
        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + OVF91_LIG},
            {'interconnectBay': 2,
             'logicalInterconnectGroupUri': 'LIG:' + OVF91_LIG},
            {'interconnectBay': 3,
             'logicalInterconnectGroupUri': 'LIG:' + OVF91_LIG},
            {'interconnectBay': 4,
             'logicalInterconnectGroupUri': 'LIG:' + OVF91_LIG},
            {'interconnectBay': 5,
             'logicalInterconnectGroupUri': 'LIG:' + OVF91_LIG},
            {'interconnectBay': 6,
             'logicalInterconnectGroupUri': 'LIG:' + OVF91_LIG},
            {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 8, 'logicalInterconnectGroupUri': None},
         ]
     },
]

enclosures = [
    {'hostname': OVF91_ENC_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + OVF91_EG,
     'force': True, 'licensingIntent': 'OneViewNoiLO', "firmwareBaselineUri": None, },
]

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": OVF91_ENC, },
]

OVF91_ENC_OA1_CONCATENATED_CERTIFICATES = '''
-----BEGIN CERTIFICATE-----
MIID/zCCAuegAwIBAgICfe4wDQYJKoZIhvcNAQELBQAwazELMAkGA1UEBhMCVVMx
EzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVBhbG8gQWx0bzEYMBYGA1UE
ChMPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDExBIUCBUZXN0SGVhZCBSb290MCAX
DTE3MDgyNDIxMTYwNVoYDzIxMTcwNzMxMjExNjA1WjCBizEYMBYGA1UEAwwPT0Et
ODBDMTZFNkEwRjhGMQswCQYDVQQGEwJVUzERMA8GA1UECAwIQ29sb3JhZG8xFTAT
BgNVBAcMDEZvcnQgQ29sbGluczEYMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMR4w
HAYDVQQLDBVPbmJvYXJkIEFkbWluaXN0cmF0b3IwggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDCzQOPANmcpKCeWTPyY/X5hD/nqqI+MAsEHq6lEDU6LFva
TmnET6JP66Tks4o6mpX7TlyiqTHhMb6ntMyON7JWYSatx54AQeNXZUHLZXqavBUk
rvQAIwZZsEyq29hZoZ+aBxLVNfETk91ZZ8Qm4y7uPxhVEXbkAAIIyfa6qCqBIByQ
Ma6mxxTYlYu9cia8zRMEbbRk3NrJIH4IZhsJVzqBOEiEMouV4OIGZSim2SlqYJHK
wpZRiMUwdz2WiQg2A0qCnsEiH4qgUH+UTFc8An+56ELcLwvw3n+rKMxCNdpRZRbx
nt+JgOq5qyQcmnmZrGB1+CYhkgLMGPAtDM1brDdBAgMBAAGjgYkwgYYwCQYDVR0T
BAIwADALBgNVHQ8EBAMCBLAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwEQYJYIZIAYb4
QgEBBAQDAgZAMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3QvY2Eu
Y3JsMBoGA1UdEQQTMBGCD09BLTgwQzE2RTZBMEY4RjANBgkqhkiG9w0BAQsFAAOC
AQEAnpOO3A/x9bg8q4ScH/3rQNypj5uZt6z8KHmzO6bHLrKnTbHyzi3qdNhNzL2x
tAIZ9tStT5y+mD3OQisRZ2hCLrXjGUf5DWpvaboWvUO4PlPQMwh9attT5jvZbiPo
puONWFjvP+yzbzBCcNs4O67vPkhuJhGR+5cQ46f8AZjILrcl8Nl90akpOsSQuF1F
VJgXOWnIBXUKqC+N/4zYeoCMyfeApJKocI6E6IA6Qss/3WW8vsV410BMardexQtZ
PfpcFqH6O1oFzZy7AXeu9AlhDPTVtsNLv7KBfpUV1IBRM2rHP/yjFAthk6qyBLxY
hZIQ302pgbgaR02a+SRZS5Xrig==
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIEOTCCAyGgAwIBAgIJANNmdKPRkJXPMA0GCSqGSIb3DQEBCwUAMGsxCzAJBgNV
BAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRIwEAYDVQQHEwlQYWxvIEFsdG8x
GDAWBgNVBAoTD0hld2xldHQtUGFja2FyZDEZMBcGA1UEAxMQSFAgVGVzdEhlYWQg
Um9vdDAgFw0xNzA4MjQyMTE2MDVaGA8yMTE3MDczMTIxMTYwNVowazELMAkGA1UE
BhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVBhbG8gQWx0bzEY
MBYGA1UEChMPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDExBIUCBUZXN0SGVhZCBS
b290MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvPzxUxy/w4+k0njL
+dVx+Dpl8omdJmC7x41/zG9ewz3Cpc8uYxvUZq7iC6MczvItN5L2toNhhzjruFYE
CEphky9bfBspTBjPERp6lkToB61nmMuovevW5CxgPxFtN1gm2S7WsLLWk6WPsN/q
N1l2+hb2MYQv3gV6SRa9PZZR6PFH7X2wkKerZDIXQfKYdwpEX4kNbl47p4v8A1vM
8pf7S7oT10ITx9c/V/E0TCk8A7/jGvRrjr44Q3CVp8oRMO8pVQrei579AAH3JNUy
4gcxRctoNDRX2JkCbmLe6tqIxO/VWB4SxO/h5osy6JjIEkKvnPRXVzTh8W6V1UFY
wo3XEwIDAQABo4HdMIHaMB0GA1UdDgQWBBRzC7/pexb8koLeFR2DAja1u6QNazCB
nQYDVR0jBIGVMIGSgBRzC7/pexb8koLeFR2DAja1u6QNa6FvpG0wazELMAkGA1UE
BhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVBhbG8gQWx0bzEY
MBYGA1UEChMPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDExBIUCBUZXN0SGVhZCBS
b290ggkA02Z0o9GQlc8wCwYDVR0PBAQDAgG2MAwGA1UdEwQFMAMBAf8wDQYJKoZI
hvcNAQELBQADggEBAEOWAQcdPS6eQpbBnux0y3JEaaZGZXbhtsaTlI0i3FiPkC9g
SwmF36t6597airU7JV0iIqsG/lo/MMsQUR7pQQWv0M5FJ/jOJt0wFaGvLl9dAJv+
TmfsRsJho4kY/cx+kjf0jd301ylop/0ArAWrKpIU3f3uNnYcJZFR9NWqcj7+FeCh
2QujfUWp4FA200gtwHd2NBTamowjrjhGVtJmCd97cBpnYHlt75viCc2fsUhR3Mn+
DNcNUj2iWepnVYEyVwplHbXs8QGzYJiKD9Iwz2siV8R3MSnI3qdLOgTVYe/gx+mT
SDbpLp/EzcV62bjj2NMyH1up2i+X/E+Q9mf5cEo=
-----END CERTIFICATE-----
'''

OVF91_ENC_OA1_CA_ROOT_CERTIFICATE = '''
-----BEGIN CERTIFICATE-----
MIIEOTCCAyGgAwIBAgIJANNmdKPRkJXPMA0GCSqGSIb3DQEBCwUAMGsxCzAJBgNV
BAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRIwEAYDVQQHEwlQYWxvIEFsdG8x
GDAWBgNVBAoTD0hld2xldHQtUGFja2FyZDEZMBcGA1UEAxMQSFAgVGVzdEhlYWQg
Um9vdDAgFw0xNzA4MjQyMTE2MDVaGA8yMTE3MDczMTIxMTYwNVowazELMAkGA1UE
BhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVBhbG8gQWx0bzEY
MBYGA1UEChMPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDExBIUCBUZXN0SGVhZCBS
b290MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvPzxUxy/w4+k0njL
+dVx+Dpl8omdJmC7x41/zG9ewz3Cpc8uYxvUZq7iC6MczvItN5L2toNhhzjruFYE
CEphky9bfBspTBjPERp6lkToB61nmMuovevW5CxgPxFtN1gm2S7WsLLWk6WPsN/q
N1l2+hb2MYQv3gV6SRa9PZZR6PFH7X2wkKerZDIXQfKYdwpEX4kNbl47p4v8A1vM
8pf7S7oT10ITx9c/V/E0TCk8A7/jGvRrjr44Q3CVp8oRMO8pVQrei579AAH3JNUy
4gcxRctoNDRX2JkCbmLe6tqIxO/VWB4SxO/h5osy6JjIEkKvnPRXVzTh8W6V1UFY
wo3XEwIDAQABo4HdMIHaMB0GA1UdDgQWBBRzC7/pexb8koLeFR2DAja1u6QNazCB
nQYDVR0jBIGVMIGSgBRzC7/pexb8koLeFR2DAja1u6QNa6FvpG0wazELMAkGA1UE
BhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVBhbG8gQWx0bzEY
MBYGA1UEChMPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDExBIUCBUZXN0SGVhZCBS
b290ggkA02Z0o9GQlc8wCwYDVR0PBAQDAgG2MAwGA1UdEwQFMAMBAf8wDQYJKoZI
hvcNAQELBQADggEBAEOWAQcdPS6eQpbBnux0y3JEaaZGZXbhtsaTlI0i3FiPkC9g
SwmF36t6597airU7JV0iIqsG/lo/MMsQUR7pQQWv0M5FJ/jOJt0wFaGvLl9dAJv+
TmfsRsJho4kY/cx+kjf0jd301ylop/0ArAWrKpIU3f3uNnYcJZFR9NWqcj7+FeCh
2QujfUWp4FA200gtwHd2NBTamowjrjhGVtJmCd97cBpnYHlt75viCc2fsUhR3Mn+
DNcNUj2iWepnVYEyVwplHbXs8QGzYJiKD9Iwz2siV8R3MSnI3qdLOgTVYe/gx+mT
SDbpLp/EzcV62bjj2NMyH1up2i+X/E+Q9mf5cEo=
-----END CERTIFICATE-----
'''

OVF91_ENC_OA1_CA_ROOT_CERTIFICATE_NAME = 'HP TestHead Root'

OVF91_ADD_CA_CERTIFICATES = {
    "type": "CertificateAuthorityInfoCollection",
    "members": [{"certificateDetails": {"aliasName": None, "base64Data": OVF91_ENC_OA1_CA_ROOT_CERTIFICATE, "type": "CertificateDetailV2"}, "type": "CertificateAuthorityInfo"}],
}
