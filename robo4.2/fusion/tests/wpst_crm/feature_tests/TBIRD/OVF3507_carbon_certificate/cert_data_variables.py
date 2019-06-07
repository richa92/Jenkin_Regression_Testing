import os


def Change_Directory(dir):
    os.chdir(dir)

APPLIANCE_IP = "15.186.9.136"
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ENC1 = "MXQ80503HJ"
ENC2 = "MXQ734024N"
FUSION_IP = "15.186.9.136"
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.
IC_SSH_USERNAME = 'root'
IC_PROMPT = '>'
IC_TIMEOUT = 100
snmp_host = '15.186.21.149'
snmp_user = 'root'
snmp_pass = 'password'
INTERCONNECTS1 = ['MXQ80503HJ, interconnect 1', 'MXQ80503HJ, interconnect 4']
INTERCONNECTS2 = ['MXQ734024N, interconnect 1', 'MXQ734024N, interconnect 4']
Interconnect_dto_all = [{"name": INTERCONNECTS1[0]}, {"name": INTERCONNECTS1[1]}, {"name": INTERCONNECTS2[0]}, {"name": INTERCONNECTS2[1]}]
# Interconnect_dto_all = [{"name" : INTERCONNECTS1[0]},{"name" : INTERCONNECTS1[1]}]
Interconnect_dto = [{"name": INTERCONNECTS1[0]}, {"name": INTERCONNECTS1[1]}]
Interconnect_dto_1 = [{"name": INTERCONNECTS2[0]}]
# Interconnect_dto_1 = [{"name" : INTERCONNECTS1[0]}]
Interconnect_dto_2enc = [{"name": INTERCONNECTS1[1]}, {"name": INTERCONNECTS2[0]}]
# Interconnect_dto_2enc = [{"name" : INTERCONNECTS1[1]}]
Enc_bay_type = {'enc1': 'Redundant', 'enc2': 'Redundant'}
# LIG1 = 'LIG1'
# LI2 = 'LE-LIG1-1'
# LE1 = 'LE'
EG = 'EG'
bay = ['1', '4']
IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3
enclosureCount = 2
Enclosure_Name = ['MXQ80503HJ', 'MXQ734024N']
ICM_MODEL = 'Virtual Connect SE 32Gb FC Module for Synergy'
server_bay = ['MXQ80503HJ, bay 1']
ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'hpvse123'}
diskspd_cmd_720s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-720s.ps1"
server_details = {'username': 'Administrator', 'password': 'password@123'}
linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}
icmap_Redundant = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1},
                                                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantASide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantBSide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}
LIG_ME = ['LIG1', 'LIG2']
interconnectBayMappings = [{"interconnectBay": IC_bay_set, "enclosureIndex": 1, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 1, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 2, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 2, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 3, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 3, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 4, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 4, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 5, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 5, "logicalInterconnectGroupUri": ""}]

EG_body = {"name": "",
           "interconnectBayMappings": interconnectBayMappings,
           "ipAddressingMode": "DHCP",
           "ipRangeUris": [],
                   "enclosureCount": enclosureCount}
Fc_body = {"name": "",
           "connectionTemplateUri": None,
           "linkStabilityTime": "30",
           "autoLoginRedistribution": True,
           "fabricType": "",
           "type": "fc-networkV4"}
FC_Network_Names = ['FC_1', 'FC_2', 'FC_3', 'FC_4']
les = [{'name': 'LE',
        'enclosureUris': [],
        'enclosureGroupUri': '',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]
le_body = {'name': 'LE',
           'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
           'enclosureGroupUri': 'EG:' + EG,
           'firmwareBaselineUri': None,
           'forceInstallFirmware': False
           }
# le_body = {'name': 'LE',
# 'enclosureUris': ['ENC:' + ENC1],
# 'enclosureGroupUri': 'EG:' + EG,
# 'firmwareBaselineUri': None,
# 'forceInstallFirmware': False
# }
LI_dto = [{'name': 'LE-LIG1-1'}, {'name': 'LE-LIG2-2'}]
LIG_body = {"type": "logical-interconnect-groupV6",
            "ethernetSettings": None,
            "name": "",
            "telemetryConfiguration": None,
            "interconnectMapTemplate": "",
            "uplinkSets": [],
            "enclosureType": "SY12000",
            "enclosureIndexes": [-1],
            "enclosureIndexes": [-1],
            "interconnectBaySet": IC_bay_set,
            "redundancyType": "",
            "internalNetworkUris": [],
            "snmpConfiguration": None,
            "qosConfiguration": None}
uplinkset = {'UplinkSet_1': {"fcMode": "TRUNK", 'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                             'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                        {'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                        ]},
             'UplinkSet_2': {"fcMode": "TRUNK", 'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                             'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                        {'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                        ]},
             'UplinkSet_3': {"fcMode": "TRUNK", 'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                             'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                        {'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                        ]},
             'UplinkSet_4': {"fcMode": "TRUNK", 'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                             'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                        {'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'}
                                                        ]}
             }
ligs_me = [{'name': 'LIG1',
            'type': 'logical-interconnect-groupV5',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                        ],
            'enclosureIndexes': [-1],
            'interconnectBaySet': 1,
            'redundancyType': 'Redundant',
            'uplinkSets': [uplinkset['UplinkSet_1'].copy(), uplinkset['UplinkSet_2'].copy()],
            'internalNetworkUris': [],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None
            },
           {'name': 'LIG2',
            'type': 'logical-interconnect-groupV5',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                        ],
            'enclosureIndexes': [-1],
            'interconnectBaySet': 1,
            'redundancyType': 'Redundant',
            'uplinkSets': [uplinkset['UplinkSet_3'].copy(), uplinkset['UplinkSet_4'].copy()],
            'internalNetworkUris': [],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None
            }]
File_Names = ['writeMECanmic.sh', 'readMECanmic.sh']
server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:94:f1:28:9b:d3:04', 'wwnn': '20:00:94:f1:28:9b:d3:04'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:94:f1:28:9b:d3:05', 'wwnn': '20:00:94:f1:28:9b:d3:05'},
                                        ]}},
                   # {'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 3',
                   # 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG,
                   # 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   # 'name': ENC2 + '_Bay3', 'description': '', 'affinity': 'Bay',
                   # 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                   # 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                   # 'connectionSettings': {
                   # 'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                   # 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_3',
                   # 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:32', 'wwnn': '20:00:00:00:c9:71:7b:32'},
                   # {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                   # 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_4',
                   # 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:33', 'wwnn': '20:00:00:00:c9:71:7b:33'},
                   # ]}},
                   ]
port_no = ['1']
No_request_get_error = 'CRM_NO_CERTIFICATE_SIGNING_REQUEST_IN_PROGRESS'
Invalid_certificate_error = 'CRM_INVALID_LOAD_CERTIFICATE_REQUEST'
Parallel_Post_Error = 'CRM_DUPLICATE_CERTIFICATE_SIGNING_REQUEST'
Missing_Required_Field = 'CRM_MISSING_REQUIRED_FIELD_FOR_HTTPS_CERTIFICATES'
Monitored_Error = 'Interconnect ICNAME must be in a configured state for this https certificate management operation.'
Invalid_message = 'The certificate does not pass the validation checks being performed. This nested error may provide more details about the specific validation that failed:\nCertificate is malformed.'
Expired_message = 'The certificate does not pass the validation checks being performed. This nested error may provide more details about the specific validation that failed:\nOne or more certificates have expired.'
ocsp_sign_pattern = 'OCSP Signing'
revoke_output = 'Revoking Certificate'
generate_self_signed_cert_message = 'Generated self-signed https certificate successfully.'
Invalid_Request_Body = {
    "type": "CertificateDtoV3",
    "organization": "Acme Corp.",
    "organizationalUnit": "IT",
    "locality": "Grenoble",
    "state": "Mississippi",
    # "country" : "US",
    "commonName": "192.168.10.10"
}
Certificate_Request_Body = {
    "type": "CertificateDtoV3",
    "organization": "Alte.",
    "organizationalUnit": "RND",
    "locality": "Alaska",
    "state": "Alaska",
    "country": "US",
    "commonName": "http://15.186.15.149"
}
OCSP_Request_Body = {
    "type": "CertificateDtoV3",
    "organization": "Acme Corp.",
    "organizationalUnit": "IT5",
    "locality": "Aquafina",
    "state": "San Jose com",
    "country": "Uk",
    "commonName": "192.168.02.42"
}
Invalid_Upload_Body = {
    "type": "CertificateDataV2",
}
Certificate_Upload_Body = {
    "type": "CertificateDataV2",
    "base64Data": ""
}
Path_for_unsigned_cert = '/root/ca/intermediate/csr'
Path_for_signed_cert = '/root/ca/intermediate/certs'
Path_for_linux_exec = '/root/ca'
Linux_command = 'openssl ca -config intermediate/openssl.cnf -extensions server_cert -days 375 -notext -md sha256 -in intermediate/csr/input_file -out intermediate/certs/output_file'
Expire_command = 'openssl ca -config intermediate/openssl.cnf -extensions server_cert -days -1 -notext -md sha256 -in intermediate/csr/input_file -out intermediate/certs/output_file'
Expire10_command = 'openssl ca -config intermediate/openssl.cnf -extensions server_cert -startdate starttimeZ -enddate endtimeZ -notext -in intermediate/csr/input_file -out intermediate/certs/output_file'
OCSP_command = 'openssl ca -config intermediate/openssl.cnf -extensions ocsp -days 375 -notext -md sha256 -in intermediate/csr/input_file -out intermediate/certs/output_file'
ocsp_verify_command = 'openssl x509 -noout -text -in intermediate/certs/output_file'
revoke_cmd = 'openssl ca -config intermediate/openssl.cnf -revoke intermediate/certs/output_file'
Permission_file_command = 'chmod 444 intermediate/certs/output_file'
date_cmd = 'date +%F+%T'
