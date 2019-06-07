""" resources/variables.py - Enclosure variables used for AM-DVT Fusion testing
    = Usage =
    | *** Settings *** |
    | variables | resources/variables.py |
    | variables | resources/variables.py | ${ENCLOSURE} |
    | pybot --variablefile resources/variables.py |
    | pybot --variablefile resources/variables.py:<EnclosureName> |
"""

import paramiko
import re
import copy
from RoboGalaxyLibrary.utilitylib import logging as logger

enclosure_defaults = {
    "ILO_PASSWORD"  : "AcmeAcme",
    "GATEWAY_IP"    : "16.114.176.1",
    "NETMASK_IP"    : "255.255.240.0",
    "PRIMARY_DNS"   : "16.114.180.180",
    "ALTERNATE_DNS" : "16.114.180.181",
    "DCS"           : False,
    "FUSION_SSH_USERNAME" : "root",
    "FUSION_SSH_PASSWORD" : "hpvse1"
    #
    # See resources\defaults.txt for additional variables.
    #
}

enclosure_configurations = {
    "dcs" : {
        "EM_IP"             : "172.18.8.101",
        "EM_IPV4"           : "172.18.8.101",
        "ENC_SERIAL_NUMBER" : "0000A66101",
        "ENC_UUID"          : "8c031050-4b30-40b5-8ddd-e55d7a093f2e",
        "BLADE_DATA" : { "1" : {  "SerialNumber":"2M220101SL", "Model":"" },
                         "2" : {  "SerialNumber":"2M220101SL", "Model":"" },
                         "4" : {  "SerialNumber":"2M201100GR", "Model":"" },
                         "5" : {  "SerialNumber":"2M220103SL", "Model":"" },
                         "6" : {  "SerialNumber":"2M220103SL", "Model":"" },
                        },
        "INTERCONNECT_DATA" : { "1" : {  "SerialNumber":"100010010100a", "Model":"Natasha SAS 12Gb Switch" },
                                "3" : {  "SerialNumber":"100010010100a", "Model":"HP FlexFabric 40/40Gb Module" },
                                "4" : {  "SerialNumber":"100010010101a", "Model":"Natasha SAS 12Gb Switch" },
                                "6" : {  "SerialNumber":"100010010100a", "Model":"HP FlexFabric 10GbE Expansion Module" }
                        },
        "FUSION_NIC_SUFFIX"   : "",
        "DCS"                 : True,
        "HW_DESCRIPTION_FILE" : "hw_tbird_demo.js",
        "DISCOVER_TRUTH_FILE" : "discover_tbird_demo.js"
        },

    "alias" : {
        "ENC_SERIAL_NUMBER"  : "00HPMP93B8",
        "FUSION_IP"          : "16.114.180.58",
        "FUSION_FQDN"        : "alias-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::9eb6:54ff:fe97:8d78",
        "ILO_IP"             : "alias-cim1-ilo.rsn.hp.com",
        "ILO_PASSWORD"       : "compaq",
        "EM_IP"              : "fe80::3a63:bbff:fe2b:93b8",
        "EM1_IP"             : "fe80::3a63:bbff:fe2b:93b8",
        "EM2_IP"             : "fe80::3a63:bbff:fe2b:6368",
        "EM_IPV4"            : "",
        "BLADE_DATA" : { "1" : {
                             "SerialNumber":"", 
                             "Model":"",
                             "BLADE_ILO_IP6"  : "FE80::1658:D0FF:FE5D:FE8C",
                             "BLADE_ILO_IP4"  : "16.114.178.65",
                             "BLADE_ILO_FQDN" : "alias01-ilo.rsn.hp.com",
                             "BLADE_ILO_USER" : "Administrator",
                             "BLADE_ILO_PW"   : "compaq",
                             "BLADE_TYPE"     : "BL460t Gen9"
                             },
                         "2" : {
                             "SerialNumber":"", 
                             "Model":"",
                             "BLADE_ILO_IP6"  : "FE80::1658:D0FF:FE5D:F2A",
                             "BLADE_ILO_IP4"  : "16.114.178.71",
                             "BLADE_ILO_FQDN" : "alias02-ilo.rsn.hp.com",
                             "BLADE_ILO_USER" : "Administrator",
                             "BLADE_ILO_PW"   : "compaq",
                             "BLADE_TYPE"     : "BL460t Gen9"
                             },
                         "3" : {
                             "SerialNumber":"", 
                             "Model":"",
                             "BLADE_ILO_IP6"  : "FE80::1658:D0FF:FE46:5CE5",
                             "BLADE_ILO_IP4"  : "16.114.178.236",
                             "BLADE_ILO_FQDN" : "alias03-ilo.rsn.hp.com",
                             "BLADE_ILO_USER" : "Administrator",
                             "BLADE_ILO_PW"   : "compaq",
                             "BLADE_TYPE"     : "BL460t Gen9"
                             },
                        }
        },

    "csitb1" : {
        "ENC_SERIAL_NUMBER"  : "0000A66101",
        "FUSION_IP"          : "16.114.178.132",
        "FUSION_FQDN"        : "csi-cimanager1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::46ae:7ebd:1a08:16a0",
        "ILO_IP"             : "16.114.189.10",
        "ILO_PASSWORD"       : "hpvse123",
        "EM_IP"              : "fe80::60eb:781e:575f:b04e",
        "EM_IPV4"            : "",
        "INTERCONNECT_DATA" : { 
                                "3" : {  "SerialNumber":"000A66101", "Model":"HP FlexFabric 40/40Gb Module" },
                                "6" : {  "SerialNumber":"000A66101", "Model":"HP FlexFabric 10GbE Expansion Module" }
                        },
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hponeview",
        "CLI_USERNAME"    : "Administrator",
        "CLI_PASSWORD" : "svtAcme1234",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_PASSWORD" : "svtAcme1234",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },

    "csitb2" : {
        "ENC_SERIAL_NUMBER"  : "00HPMP7D38",
        "EM_IP"              : "fe80::f71f:a026:da48:d4df",
        "FUSION_IP"          : "16.114.180.112",
        "FUSION_FQDN"        : "csitb2-ov.rsn.hp.com",
        "INTERCONNECT_DATA" : { 

                                "2" : {  "SerialNumber":"2TV4510276", "Model":"HP FlexFabric 40/40Gb Module" },
                        },
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "CLI_USERNAME"    : "Administrator",
        "CLI_PASSWORD" : "svtAcme1234",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_PASSWORD" : "svtAcme1234",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },

    "csitb3" : {
        "ENC_SERIAL_NUMBER"  : "WCYO6HFVSO",
        "EM_IP"              : "fe80::a4a8:ee8a:a54e:a756",
        "FUSION_IP"          : "16.114.180.113",
        "FUSION_FQDN"        : "csitb3-ov.rsn.hp.com",
        "INTERCONNECT_DATA" : { 

                                "3" : {  "SerialNumber":"PTASH4FB82", "Model":"HP FlexFabric 40/40Gb Module" },
                                "4" : {  "SerialNumber":"NTASHA4FB84", "Model":"HP FlexFabric 40/40Gb Module" },
                                "6" : {  "SerialNumber":"0CL204FB85", "Model":"HP FlexFabric 10GbE Expansion Module" }
                        },
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "CLI_USERNAME"    : "Administrator",
        "CLI_PASSWORD" : "svtAcme1234",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_PASSWORD" : "svtAcme1234",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },

    "csitb6" : {
        "ENC_SERIAL_NUMBER"  : "00HPMP2348",
        "FUSION_IP"          : "16.114.180.9",
        "FUSION_FQDN"        : "csitb6-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::46ae:7ebd:1a08:16a0",
        "ILO_IP"             : "16.114.189.10",
        "ILO_PASSWORD"       : "hpvse123",
        "EM_IP"              : "fe80::60eb:781e:575f:b04e",
        "EM_IPV4"            : "",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },

    "csitb7" : {
        "ENC_SERIAL_NUMBER"  : "QWJ8N32XYR",
        "FUSION_IP"          : "16.114.180.117",
        "FUSION_FQDN"        : "csitb7-ov.rsn.hp.com",
        "PRIMARY_DNS"        : "16.110.135.51",
        "ALTERNATE_DNS"      : "16.110.135.52",
        "ILO_PASSWORD"       : "hpvse123",
        "EM_IP"              : "fe80::60eb:781e:575f:b04e",
        "EM_IPV4"            : "",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },

    "csitb12" : {
        "ENC_SERIAL_NUMBER"  : "0000000010",
        "EM_IP"              : "fe80::eeb1:d7ff:fe8b:fcf0",
        "FUSION_IP"          : "16.114.180.216",
        "FUSION_FQDN"        : "csitb12-ov.rsn.hp.com",
        "INTERCONNECT_DATA" : { 
                                "2" : {  "SerialNumber":"GRAPH23103", "Model":"Brocade 16Gb/12 FC Switch Module" },
                                "3" : {  "SerialNumber":"2TV5181117", "Model":"VC SE 40Gb F8 Module" },
                                "6" : {  "SerialNumber":"2TV5181122", "Model":"VC SE 40Gb F8 Module" }
                        },
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "CLI_USERNAME"    : "Administrator",
        "CLI_PASSWORD" : "svtAcme1234",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_PASSWORD" : "svtAcme1234",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },
        
    "csitb_auto" : {
        "ENC_SERIAL_NUMBER"  : "CN75120D6Z",
        "EM_IP"              : "fe80::eeb1:d7ff:fe8b:2d90",
        "FUSION_IP"          : "16.114.181.220",
        "FUSION_FQDN"        : "csitbauto-ov.rsn.rdlabs.hpecorp.net",
        "INTERCONNECT_DATA" : { 
                                "3" : {  "SerialNumber":"2TV4510379", "Model":"VC SE 40Gb F8 Module" },
                                "6" : {  "SerialNumber":"2TV4510276", "Model":"VC SE 40Gb F8 Module" }
                        },
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "CLI_USERNAME"    : "Administrator",
        "CLI_PASSWORD" : "svtAcme1234",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_PASSWORD" : "svtAcme1234",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },
        
    "csitb_dcs" : {
        "ENC_SERIAL_NUMBER"  : "0000A66101",
        "EM_IP"              : "fe80::eeb1:d7ff:fe8b:fcf0",
        "FUSION_IP"          : "16.114.178.135",
        "FUSION_FQDN"        : "csi-cimanager4.rsn.hp.com",
        "INTERCONNECT_DATA" : { 
                                "3" : {  "SerialNumber":"0000A44100", "Model":"VC SE 40Gb F8 Module" },
                                "6" : {  "SerialNumber":"0000A55100", "Model":"VC SE 40Gb F8 Module" }
                        },
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hponeview",
        "CLI_USERNAME"    : "Administrator",
        "CLI_PASSWORD" : "svtAcme1234",
        "FUSION_USERNAME"    : "Administrator",
        "FUSION_PASSWORD" : "svtAcme1234",
        "FUSION_FACTORY_PASSWORD" : "svtAcme1234"
        },

    "aptera" : {
        "ENC_SERIAL_NUMBER"  : "00HPMP57A2",
        "FUSION_IP"          : "16.114.180.57",
        "FUSION_FQDN"        : "aptera-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::9eb6:54ff:fe97:1ea8",
        "ILO_IP"             : "16.114.180.63",
        "ILO_PASSWORD"       : "compaq",
        "EM_IP"              : "fe80::3a63:bbff:fe2b:3c0",
        "EM1_IP"             : "fe80::3a63:bbff:fe2b:3c0",
        "EM2_IP"             : "",
        "EM_IPV4"            : "",
        "BLADE_DATA" : { "1" : {
                             "SerialNumber":"", 
                             "Model":"",
                             "BLADE_ILO_IP6"  : "FE80::1658:D0FF:FE5D:1F93",
                             "BLADE_ILO_IP4"  : "16.114.178.73",
                             "BLADE_ILO_FQDN" : "aptera01-ilo.rsn.hp.com",
                             "BLADE_ILO_USER" : "Administrator",
                             "BLADE_ILO_PW"   : "compaq",
                             "BLADE_TYPE"     : "BL460t Gen9"
                             },
                         "2" : {
                             "SerialNumber":"", 
                             "Model":"",
                             "BLADE_ILO_IP6"  : "FE80::1658:D0FF:FE5D:FF3",
                             "BLADE_ILO_IP4"  : "16.114.178.75",
                             "BLADE_ILO_FQDN" : "aptera02-ilo.rsn.hp.com",
                             "BLADE_ILO_USER" : "Administrator",
                             "BLADE_ILO_PW"   : "compaq",
                             "BLADE_TYPE"     : "BL460t Gen9"
                             },
                        }
        },

    "csitb4" : {
        "FUSION_IP"             : "16.114.180.7",
        "FUSION_FQDN"           : "csitb4-cim1.rsn.hp.com",
        "FUSION_PASSWORD"       : "svtAcme1234",
        "ILO_IP"                : "16.114.186.101",
        "ILO_PASSWORD"          : "compaq",
        "EM_IP"                 : "fe80::1658:d0ff:fe41:e240",
        "EM1_IP"                : "fe80::1658:d0ff:fe41:e240",
        "EM2_IP"                : "fe80::c634:6bff:fec9:b7f0",
        "EM_IPV4"               : "16.114.178.166",

        "ENC_SERIAL_NUMBER"     : "00HPMPE240",
        "BLADE_DATA" : { "3" :
                         {  "SerialNumber":"", "Model":"",
                            "BLADE_TYPE"     : "Synergy 480 Gen9"
                          },
                         "4" :
                         {  "SerialNumber":"", "Model":"",
                            "BLADE_TYPE"     : "Synergy 480 Gen9"
                          },
                         "6" :
                         {  "SerialNumber":"", "Model":"",
                            "BLADE_TYPE"     : "Synergy 480 Gen9"
                          },
                         "9" :
                         {  "SerialNumber":"", "Model":"",
                            "BLADE_TYPE"     : "Synergy 480 Gen9"
                          },
                         "10" :
                         {  "SerialNumber":"", "Model":"",
                            "BLADE_TYPE"     : "Synergy 480 Gen9"
                          },
                         "11" :
                         {  "SerialNumber":"", "Model":"",
                            "BLADE_TYPE"     : "Synergy 480 Gen9"
                          },
                         "12" :
                         {  "SerialNumber":"", "Model":"",
                            "BLADE_TYPE"     : "Synergy 480 Gen9"
                          },
                        },
        "INTERCONNECT_DATA" :
                        { "2" : {  "SerialNumber":"00HPMPE240", "Model":"HP Virtual Connect 40Gb F8 Interconnect" },
                          "5" : {  "SerialNumber":"00HPMPE240", "Model":"HP HP FlexFabric 20GbE Expansion Module" }
                }
    },

    "mustang" : {
        "FUSION_IP"             : "16.114.179.125",
        "FUSION_FQDN"           : "mustang-cim1.rsn.hp.com",
        "FUSION_IPV6"           : "fe80::9eb6:54ff:fe97:5cc8",
        "ILO_IP"                : "16.114.179.124",
        "ILO_PASSWORD"          : "compaq",
        "EM_IP"                : "fe80::c634:6bff:fec9:c7b8",
        "EM1_IP"               : "fe80::c634:6bff:fec9:c7b8",
        "EM2_IP"               : "fe80::c634:6bff:fec9:b7f0",
        "EM_IPV4"              : "16.114.178.166",

        "ENC_SERIAL_NUMBER" : "00HPMPC01A",
        "BLADE_DATA" : { "1" : 
                          {  "SerialNumber"   : "CN74250H94", 
                             "Model"          : "ProLiant BL460t Gen9",
                             "BLADE_ILO_IP6"  : "fe80::fe15:b4ff:fe12:adfe",
                             "BLADE_ILO_IP4"  : "16.114.179.64",
                             "BLADE_ILO_FQDN" : "mustang01-ilo.rsn.hp.com",
                             "BLADE_ILO_USER" : "Administrator",
                             "BLADE_ILO_PW"   : "compaq",
                             "BLADE_TYPE"     : "BL460t Gen9"
                          },
                         "2" : 
                          {  "SerialNumber"   : "CN74250HCH", 
                             "Model"          : "ProLiant BL460t Gen9",
                             "BLADE_ILO_IP6"  : "fe80:0:0:0:fe15:b4ff:fe12:ad21",
                             "BLADE_ILO_IP4"  : "16.114.179.65",
                             "BLADE_ILO_FQDN" : "mustang02-ilo.rsn.hp.com",
                             "BLADE_ILO_USER" : "Administrator",
                             "BLADE_ILO_PW"   : "compaq",
                             "BLADE_TYPE"     : "BL460t Gen9"
                          }, 
                        # "5" : 
                        #   {  "SerialNumber"   : "", 
                        #      "Model"          : "",
                        #      "BLADE_ILO_IP6"  : "fe80::fe15:b4ff:fe12:bd49",
                        #      "BLADE_ILO_IP4"  : "16.114.179.132",
                        #      "BLADE_ILO_FQDN" : "mustang05-ilo.rsn.hp.com",
                        #      "BLADE_ILO_USER" : "Administrator",
                        #      "BLADE_ILO_PW"   : "compaq",
                        #      "BLADE_TYPE"     : "BL460t Gen9"
                        #   },
                        },
        "INTERCONNECT_DATA" : { "1" : { "SerialNumber": "PTASHC01A1",
                                        "Model" : " HP FlexFabric 40GbE Module - EdgeSafe/Virtual Connect version",
                                    },
                        },
        },

    "tesla" : {
        "FUSION_IP"             : "16.114.179.117",
        "FUSION_FQDN"           : "tesla-cim1.rsn.hp.com",
        "FUSION_IPV6"           : "fe80::9eb6:54ff:fe97:bc98",
        "ILO_IP"                : "tesla-cim1-ilo.rsn.hp.com",
        "ILO_PASSWORD"          : "compaq",
        "EM_IP"                 : "fe80::c634:6bff:feb0:3f70",
        "EM1_IP"                : "fe80::c634:6bff:feb0:3f70",
        "EM2_IP"                : "",
        "EM_IPV4"               : "16.114.179.116",
        "HW_DESCRIPTION_FILE"   : "hw_tesla.js",

        "ENC_SERIAL_NUMBER" : "00HPMP3F70",
        "ENC_UUID"          : "00000000HPMP3F70",
        "BLADE_DATA" : { "1" :
                         {  "SerialNumber":"", "Model":"Synergy 480 Gen9",
                            "BLADE_ILO_IP6"  : "FE80::FE15:B4FF:FE12:BD30",
                            "BLADE_ILO_IP4"  : "16.114.179.176",
                            "BLADE_ILO_FQDN" : "tesla01-ilo.rsn.hp.com",
                            "BLADE_ILO_USER" : "Administrator",
                            "BLADE_ILO_PW"   : "compaq",
                            "BLADE_TYPE"     : "BL460t Gen9"
                          },
                         # "2" :
                         # {  "SerialNumber":"", "Model":"",
                         #    "BLADE_ILO_IP6"  : "FE80::FE15:B4FF:FE12:AD52",
                         #    "BLADE_ILO_IP4"  : "16.114.179.66",
                         #    "BLADE_ILO_FQDN" : "tesla02-ilo.rsn.hp.com",
                         #    "BLADE_ILO_USER" : "Administrator",
                         #    "BLADE_ILO_PW"   : "compaq",
                         #    "BLADE_TYPE"     : "BL460t Gen9"
                         #  },
                        },
        "INTERCONNECT_DATA" : { "1" : {  "SerialNumber":"PTASH3F701", "Model":"HP Virtual Connect 40Gb F8 Interconnect" },
                        },
        "DISCOVER_TRUTH_FILE" : "discover_tesla.js"
        },

    "amstel" : {
        "FUSION_IP"          : "16.114.179.32",
        "FUSION_FQDN"        : "amstel-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::9eb6:54ff:fe97:3cb8",
        "ILO_IP"             : "amstel-cim1-ilo.rsn.hp.com",
        "EM_IP"              : "fe80::c634:6bff:feb0:8ff8",
        "EM1_IP"             : "fe80::c634:6bff:feb0:8ff8",
        "EM2_IP"             : "",
        "EM_IPV4"            : "16.114.179.30",
        },

    "innis" : {
        "FUSION_IP"          : "16.114.179.139",
        "FUSION_FQDN"        : "innis-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::9eb6:54ff:fe97:bec0",
        "ILO_IP"             : "innis-cim1-ilo.rsn.hp.com",
        "EM_IP"              : "fe80::c634:6bff:feb0:8f48",
        "EM1_IP"             : "fe80::c634:6bff:feb0:8f48",
        "EM2_IP"             : "",
        "EM_IPV4"            : "16.114.179.137",
        },

    "ipa" : {
        "FUSION_IP"          : "16.114.179.143",
        "FUSION_FQDN"        : "ipa-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::9eb6:54ff:fe97:5c40",
        "ILO_IP"             : "ipa-cim1-ilo.rsn.hp.com",
        "EM_IP"              : "fe80::c634:6bff:feb0:8f28",
        "EM1_IP"             : "fe80::c634:6bff:feb0:8f28",
        "EM2_IP"             : "",
        "EM_IPV4"            : "16.114.179.141",
        },

    "duvel" : {
        "FUSION_IP"          : "16.114.179.146",
        "FUSION_FQDN"        : "duvel-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::9eb6:54ff:fe97:8c30",
        "ILO_IP"             : "duvel-cim1-ilo.rsn.hp.com",
        "EM_IP"              : "fe80::c634:6bff:feb0:af78",
        "EM1_IP"             : "fe80::c634:6bff:feb0:af78",
        "EM2_IP"             : "",
        "EM_IPV4"            : "16.114.179.144",
        "ENC_SERIAL_NUMBER"  : "EM1AF78101",
        "DISCOVER_TRUTH_FILE" : "discover_duvel.js"
        },

    "corona" : {
        "FUSION_IP"          : "16.114.179.136",
        "FUSION_FQDN"        : "corona-cim1.rsn.hp.com",
        "FUSION_IPV6"        : "fe80::9eb6:54ff:fe97:6c78",
        "ILO_IP"             : "corona-cim1-ilo.rsn.hp.com",
        "EM_IP"              : "fe80::c634:6bff:feb0:2f10",
        "EM1_IP"             : "fe80::c634:6bff:feb0:2f10",
        "EM2_IP"             : "",
        "EM_IPV4"            : "16.114.179.134",
        },

    "firebird" : {
        "FUSION_IP"    : '16.114.179.127',
        "FUSION_FQDN"  : 'firebird-cim1.rsn.hp.com',
        "ILO_IP"       : '16.114.179.126',
        "ILO_PASSWORD" : "compaq",
        "EM_IP"        : 'fe80::c634:6bff:feb0:af18',
        "EM1_IP"       : 'fe80::c634:6bff:feb0:af18',
        "EM2_IP"       : '',
        "EM_IPV4"      : 'firebird-em1.rsn.hp.com'
        },

    "kirin" : {              
        "FUSION_IP"    : '16.114.179.42', 
        "FUSION_IPV6"  : "fe80::9eb6:54ff:fe97:bc38",
        "FUSION_FQDN"  : 'dp2proto1-cim1.rsn.hp.com', 
        "ILO_IP"       : '16.114.179.41',
        "EM_IP"        : 'fe80::c634:6bff:feb0:af10',
        "EM1_IP"       : 'fe80::c634:6bff:feb0:af10',
        "EM2_IP"       : '',
        "EM_IPv4"      : 'dp2proto1-em1.rsn.hp.com',

        "ENC_SERIAL_NUMBER"   : "EM1AF10101",
        "BLADE_DATA" : {  "6" : {
                              "BLADE_ILO_IP6"  : "fe80:0:0:0:fe15:b4ff:fe12:bd34",
                              "BLADE_ILO_IP4"  : "16.114.179.14",
                              "BLADE_ILO_USER" : "Administrator",
                              "BLADE_ILO_PW"   : "compaq",
                              "BLADE_TYPE"     : "BL460t Gen9"
                              },
                        },
    },

    "orion" : {
        "FUSION_IP"    : '16.114.179.42', 
        "FUSION_IPV6"  : 'fe80::9eb6:54ff:fe97:8ce0',
        "FUSION_FQDN"  : 'dp2proto2-cim1.rsn.hp.com', 
        "ILO_IP"       : '16.114.179.41',
        "EM_IP"        : 'fe80::c634:6bff:feb0:4ff8',
        "EM1_IP"       : 'fe80::c634:6bff:feb0:4ff8',
        "EM2_IP"       : '',
        "EM_IPv4"      : '16.114.178.163',

        "ENC_SERIAL_NUMBER"   : "EM14FF8101",
        "HW_DESCRIPTION_FILE" : "hw_dp2proto2.js",
        "DISCOVER_TRUTH_FILE" : "discover_dp2proto2.js",
        "BLADE_DATA" : {  "5" : {
                              "BLADE_ILO_IP6"  : "fe80:0:0:0:fe15:b4ff:fe12:bd34",
                              "BLADE_ILO_IP4"  : "16.114.179.14",
                              "BLADE_ILO_USER" : "Administrator",
                              "BLADE_ILO_PW"   : "AcmeAcme",
                              "BLADE_TYPE"     : "BL460t Gen9"
                              },
                          "8" : {
                              "BLADE_ILO_IP6"  : "fe80:0:0:0:fe15:b4ff:fe12:bd34",
                              "BLADE_ILO_IP4"  : "16.114.179.14",
                              "BLADE_ILO_USER" : "Administrator",
                              "BLADE_ILO_PW"   : "AcmeAcme",
                              "BLADE_TYPE"     : "BL460t Gen9"
                              },
                        },
        },

    "stella" : {
        "FUSION_IP"    : '16.114.179.34',
        "FUSION_IPV6"  : 'fe80::9eb6:54ff:fe97:5c60',
        "FUSION_FQDN"  : 'stella-cim1.rsn.hp.com',
        "ILO_IP"       : '16.114.179.33',
        # Using Fosters EM addresses
        "EM_IP"        : 'fe80::c634:6bff:feb0:5f50',
        "EM1_IP"        : 'fe80::c634:6bff:feb0:5f50',
        "EM2_IP"        : '',
        "EM_IPV4"      : "16.114.178.164",

        "ENC_SERIAL_NUMBER"   : "EM15F50101",
        "HW_DESCRIPTION_FILE" : "hw_stella.js",
        "DISCOVER_TRUTH_FILE" : "discover_stella.js",
        "ENC_UUID"            : "000000EM15F50101",
        "ENC_INTERCONNECTS"   : "0",
        }
}

def get_variables(enc_args):
    """
    Variable files can have a special get_variables method that returns variables as a mapping.
    """
    enclosure_names = enc_args.split(',')
    all_variables = {}

    # Get enclosure configuration
    if enclosure_names is not []:
        for enclosure_name in enclosure_names:
            variables = copy.deepcopy(enclosure_defaults)
            print "enclosure name: %s" % enclosure_name
            enclosure_configuration = get_enclosure_configuration(enclosure_name)
            if enclosure_configuration is not None:
                for key in enclosure_configuration:
                    variables[key] = enclosure_configuration[key]
                origIP = variables['EM_IP']
                print "EM_IP is Static:  %s." % variables['EM_IP']
                variables['EM_IP'] = get_enclosure_manager_ip(variables)
                if variables['EM_IP'] == None:
                    variables['EM_IP'] = origIP
                print "EM_IP is FloatingIp:  %s." % variables['EM_IP']
            else:
                print "WARNING: Enclosure '%s' is not known configuration." % enclosure_name
            if(enclosure_names.index(enclosure_name) == 0): 
                all_variables = copy.deepcopy(variables)
                all_variables['ENCLOSURE_COUNT'] = len(enclosure_names)
                all_variables['ENCLOSURES'] = {}
            all_variables['ENCLOSURES'][enclosure_name] = copy.deepcopy(variables)
    else: all_variables[''] = enclosure_defaults
    return all_variables

def get_enclosure_configuration(enclosure_name):
    """
    Returns Enclosure Manager configuration information from specified enclosure name.
    Example:
        get_serial_dl_configuration("tesla-em.rsn.hp.com")
    """
    for name in enclosure_configurations:
        if enclosure_name == name:
            return enclosure_configurations[name]
    return None

def get_enclosure_manager_ip(variables):
    """
    Get the floating IPv6 address of the active EM by logging into the CI and
    extracting the lldp data.
    """
    if 'FUSION_IP' in variables:
        try:
            # Connect to the CI Manager.
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(variables['FUSION_IP'],
                        username=variables['FUSION_SSH_USERNAME'],
                        password=variables['FUSION_SSH_PASSWORD'])
            # We're connected. Let's run the command and get the output.
            print "SSH to CiMgr succeeded."
            stdin, stdout, stderr = ssh.exec_command("lldpcli show neighbor")
            output = stdout.read()
            # Find 'MgmtIP' followed by the IPv6 address.
            matches = re.search(r'MgmtIP:\s*(\S*:\S*:\S*:\S*:\S*:\S*)', output, re.MULTILINE)
            if matches:
                print "lldpcli call and regex match succeeded."
                return matches.group(1)
        except paramiko.BadHostKeyException:
            logger._warn("Could not connect to %s because of BadKeyException.  Need to clean up .ssh directory?" % variables['FUSION_IP'])
        except Exception as e:
            logger._warn ("Could not connect to %s to determine EM_IP address. \n%s" % (variables['FUSION_IP'], e))
    return None

if __name__ == "__main__":
    """
    Test Program
    """
    import pprint
    import sys

    enclosure_name = []  # Default to no name
    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            enclosure_names += sys.argv[i]
    variables = get_variables(enclosure_names)
    print "\nVariables: %s\n" % pprint.pformat(variables)
