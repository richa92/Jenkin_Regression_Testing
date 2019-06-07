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
from RoboGalaxyLibrary.utilitylib import logging as logger

enclosure_defaults = {
    "ILO_PASSWORD": "",
    "GATEWAY_IP": "",
    "NETMASK_IP": "",
    "PRIMARY_DNS": "",
    "ALTERNATE_DNS": "",
    "DCS": False,
    "FUSION_SSH_USERNAME": "",
    "FUSION_SSH_PASSWORD": "",
    "STANDBY_CIM": "",
    "ACTIVE_CIM": "",
    "FUSION_IP": ""
    #
    # See resources\defaults.txt for additional variables.
    #
}

enclosure_configurations = {
    "dcs": {
        "EM_IP": "172.18.8.101",
        "EM_IPV4": "172.18.8.101",
        "ENC_SERIAL_NUMBER": "0000A66101",
        "ENC_UUID": "8c031050-4b30-40b5-8ddd-e55d7a093f2e",
        "BLADE_DATA": {"1": {"SerialNumber": "2M220101SL", "Model": ""},
                       "2": {"SerialNumber": "2M220101SL", "Model": ""},
                       "4": {"SerialNumber": "2M201100GR", "Model": ""},
                       "5": {"SerialNumber": "2M220103SL", "Model": ""},
                       "6": {"SerialNumber": "2M220103SL", "Model": ""},
                       },
        "INTERCONNECT_DATA": {"1": {"SerialNumber": "100010010100a", "Model": "Natasha SAS 12Gb Switch"},
                              "3": {"SerialNumber": "100010010100a", "Model": "HP FlexFabric 40/40Gb Module"},
                              "4": {"SerialNumber": "100010010101a", "Model": "Natasha SAS 12Gb Switch"},
                              "6": {"SerialNumber": "100010010100a", "Model": "HP FlexFabric 10GbE Expansion Module"}
                              },
        "FUSION_NIC_SUFFIX": "",
        "DCS": True,
        "HW_DESCRIPTION_FILE": "hw_tbird_demo.js",
        "DISCOVER_TRUTH_FILE": "discover_tbird_demo.js"
    },
    "Ring1ActiveCIM": {
        "ILO_PASSWORD": "",
        "GATEWAY_IP": "",
        "NETMASK_IP": "",
        "PRIMARY_DNS": "",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.210.202",
        "ACTIVE_CIM": "16.114.210.201",
        "FUSION_IP": "16.114.211.32",
        "MAINTANENCE_IP": "16.114.210.201",  # Management IP
        "FUSION_FQDN": "wpst-tbird-1-oneview.vse.rdlabs.hpecorp.net",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "fe80::2347:92b:e77:d65b",
        "EM1_IP": "fe80::3a63:bbff:fe2b:7348",
        "EM2_IP": "fe80::3a63:bbff:fe2b:f2c0",
        "EM_IPV4": "16.114.178.166",

        "ENC_SERIAL_NUMBER": "00HPMPC01A",
        "BLADE_DATA": {"1":
                        {"SerialNumber": "CN74250H94",
                             "Model": "ProLiant BL460t Gen9",
                             "BLADE_ILO_IP6": "fe80::fe15:b4ff:fe12:adfe",
                             "BLADE_ILO_IP4": "16.114.179.64",
                             "BLADE_ILO_FQDN": "mustang01-ilo.rsn.hp.com",
                             "BLADE_ILO_USER": "Administrator",
                             "BLADE_ILO_PW": "hpvse123",
                             "BLADE_TYPE": "BL460t Gen9",
                             "MEZZ_1": "HP FlexFabric Bronco Gen3 2p 20GbE CNA BCM57840",
                             "MEZZ_2": "",
                             "MEZZ_3": "",
                         },
                       },
    },
    "Houston": {
        "ILO_PASSWORD": "Tbird123",
        "GATEWAY_IP": "10.15.0.1",
        "NETMASK_IP": "255.255.0.0",
        "PRIMARY_DNS": "10.15.10.11",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.15.3.252",
        "ACTIVE_CIM": "10.15.3.254",
        "FUSION_IP": "10.15.3.254",
        "MAINTANENCE_IP": "10.15.3.252",  # Management IP
        "FUSION_FQDN": "Houston.deafusion.local",
        "FUSION_IPV6": "fe80::9eb6:54ff:fe98:e410",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "fe80::8653:110c:c063:4857",
        "EM1_IP": "fe80::1602:ecff:fe44:4d40",
        "EM2_IP": "fe80::9657:a5ff:fe65:da30",
        "EM_IPV4": "16.114.178.166",

        "ENC_SERIAL_NUMBER": "MXQ645026W",
        "BLADE_DATA": {"1":
                        {"SerialNumber": "MXQ64504KB",
                             "Model": "Synergy 480 Gen9",
                             "BLADE_ILO_IP6": "fe80::fe15:b4ff:fe12:adfe",
                             "BLADE_ILO_IP4": "10.15.53.112",
                             "BLADE_ILO_FQDN": "WIN-VHISNPBKS9D",
                             "BLADE_ILO_USER": "Administrator",
                             "BLADE_ILO_PW": "Tbird123",
                             "BLADE_TYPE": "BL480 Gen9",
                             "MEZZ_1": "",
                             "MEZZ_2": "",
                             "MEZZ_3": "Synergy 3820C 10/20Gb CNA",
                         },
                       },
    },
    "Woodlands": {
        "ILO_PASSWORD": "Tbird123",
        "GATEWAY_IP": "10.16.0.1",
        "NETMASK_IP": "255.255.0.0",
        "PRIMARY_DNS": "10.15.10.11",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.16.26.252",
        "ACTIVE_CIM": "10.16.26.254",
        "FUSION_IP": "10.16.26.254",
        "MAINTANENCE_IP": "10.16.26.252",  # Management IP
        "FUSION_FQDN": "Woodlands.deafusion.local",
        "FUSION_IPV6": "fe80::9eb6:54ff:fe98:e410",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "fe80::8653:110c:c063:4857",
        "EM1_IP": "fe80::1602:ecff:fe44:4d40",
        "EM2_IP": "fe80::9657:a5ff:fe65:da30",
        "EM_IPV4": "16.114.178.166",

        "ENC_SERIAL_NUMBER": "CN75120D70",
        "BLADE_DATA": {"1":
                        {"SerialNumber": "CN75120D70",
                             "Model": "Synergy 480 Gen9",
                             "BLADE_ILO_IP6": "fe80::fe15:b4ff:fe12:adfe",
                             "BLADE_ILO_IP4": "10.15.53.112",
                             "BLADE_ILO_FQDN": "WIN-VHISNPBKS9D",
                             "BLADE_ILO_USER": "Administrator",
                             "BLADE_ILO_PW": "Tbird123",
                             "BLADE_TYPE": "BL480 Gen9",
                             "MEZZ_1": "",
                             "MEZZ_2": "",
                             "MEZZ_3": "Synergy 3820C 10/20Gb CNA",
                         },
                       },
    },
    "Waco": {
        "ILO_PASSWORD": "",
        "GATEWAY_IP": "",
        "NETMASK_IP": "",
        "PRIMARY_DNS": "",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "",
        "ACTIVE_CIM": "10.16.23.254",
        "FUSION_IP": "10.16.23.254",
        "MAINTANENCE_IP": "10.16.23.253",  # Management IP
        "FUSION_FQDN": "Waco.deafusion.local",
        "FUSION_IPV6": "fe80::9eb6:54ff:fe97:2eb0",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "fe80::8653:110c:c063:4857",
        "EM1_IP": "fe80::1602:ecff:fe44:4d40",
        "EM2_IP": "fe80::9657:a5ff:fe65:da30",
        "EM_IPV4": "",

        "ENC_SERIAL_NUMBER": "MXQ706000V",
        "BLADE_DATA": {"1":
                        {"SerialNumber": "MXQ64504KB",
                             "Model": "Synergy 480 Gen9",
                             "BLADE_ILO_IP6": "fe80::fe15:b4ff:fe12:adfe",
                             "BLADE_ILO_IP4": "10.15.53.112",
                             "BLADE_ILO_FQDN": "WIN-VHISNPBKS9D",
                             "BLADE_ILO_USER": "Administrator",
                             "BLADE_ILO_PW": "Tbird123",
                             "BLADE_TYPE": "BL480 Gen9",
                             "MEZZ_1": "",
                             "MEZZ_2": "",
                             "MEZZ_3": "Synergy 3820C 10/20Gb CNA",
                         },
                       },
    },
    "Sugarland": {
        "ILO_PASSWORD": "",
        "GATEWAY_IP": "",
        "NETMASK_IP": "",
        "PRIMARY_DNS": "",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.16.27.252",
        "ACTIVE_CIM": "10.16.27.254",
        "FUSION_IP": "10.16.27.254",
        "MAINTANENCE_IP": "10.16.27.252",  # Management IP
        "FUSION_FQDN": "Houston.deafusion.local",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "fe80::daef:fde6:6685:4f28",
        "EM1_IP": "fe80::daef:fde6:6685:4f28",
        "EM2_IP": "fe80::daef:fde6:6685:6000",
        "EM_IPV4": "16.114.178.166",

        "ENC_SERIAL_NUMBER": "CN754408RZ",
        "BLADE_DATA": {"1":
                        {"SerialNumber": "CN74250H94",
                             "Model": "ProLiant BL460t Gen9",
                             "BLADE_ILO_IP6": "fe80::fe15:b4ff:fe12:adfe",
                             "BLADE_ILO_IP4": "16.114.179.64",
                             "BLADE_ILO_FQDN": "mustang01-ilo.rsn.hp.com",
                             "BLADE_ILO_USER": "Administrator",
                             "BLADE_ILO_PW": "hpvse123",
                             "BLADE_TYPE": "BL460t Gen9",
                             "MEZZ_1": "HP FlexFabric Bronco Gen3 2p 20GbE CNA BCM57840",
                             "MEZZ_2": "",
                             "MEZZ_3": "",
                         },
                       },
    },
    "Ring2ActiveCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.210.206",
        "ACTIVE_CIM": "16.114.210.205",
        "FUSION_IP": "16.114.211.46",
        "MAINTANENCE_IP": "16.114.210.205",  # Management IP
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "fe80::ced3:589c:ae89:ebcd"
    },
    "Ring2StandbyCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.210.206",
        "ACTIVE_CIM": "16.114.210.205",
        "FUSION_IP": "16.114.211.46",
        "MAINTANENCE_IP": "16.114.210.206",  # Management IP
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "fe80::e40a:1958:dd12:3b79"
    },

    "mustang": {
        "ILO_PASSWORD": "AcmeAcme",
        "GATEWAY_IP": "10.87.0.1",
        "NETMASK_IP": "255.255.0.0",
        "PRIMARY_DNS": "10.87.0.11",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.87.1.19",
        "ACTIVE_CIM": "10.87.1.18",
        "FUSION_IP": "10.87.1.17",
        "MAINTANENCE_IP": "10.87.1.19",  # Management IP
        "FUSION_FQDN": "mustang-cim1.rsn.hp.com",
        "FUSION_IPV6": "fe80::9eb6:54ff:fe97:5cc8",
        "ILO_IP": "16.114.179.124",
        "ILO_PASSWORD": "hpvse123",
        "EM_IP": "fe80::c634:6bff:fec9:c7b8",
        "EM1_IP": "fe80::c634:6bff:fec9:c7b8",
        "EM2_IP": "fe80::c634:6bff:fec9:b7f0",
        "EM_IPV4": "16.114.178.166",

        "ENC_SERIAL_NUMBER": "00HPMPC01A",
        "BLADE_DATA": {"1":
                        {"SerialNumber": "CN74250H94",
                             "Model": "ProLiant BL460t Gen9",
                             "BLADE_ILO_IP6": "fe80::fe15:b4ff:fe12:adfe",
                             "BLADE_ILO_IP4": "16.114.179.64",
                             "BLADE_ILO_FQDN": "mustang01-ilo.rsn.hp.com",
                             "BLADE_ILO_USER": "Administrator",
                             "BLADE_ILO_PW": "hpvse123",
                             "BLADE_TYPE": "BL460t Gen9",
                             "MEZZ_1": "HP FlexFabric Bronco Gen3 2p 20GbE CNA BCM57840",
                             "MEZZ_2": "",
                             "MEZZ_3": "",
                         },
                       },
    },

    "tesla": {
        "ILO_PASSWORD": "AcmeAcme",
        "GATEWAY_IP": "10.87.0.1",
        "NETMASK_IP": "255.255.0.0",
        "PRIMARY_DNS": "10.87.0.11",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.87.1.19",
        "ACTIVE_CIM": "10.87.1.18",
        "FUSION_IP": "10.87.1.17",
        "MAINTANENCE_IP": "10.87.1.18",
        "FUSION_FQDN": "tesla-cim1.rsn.hp.com",
        "FUSION_IPV6": "fe80::9eb6:54ff:fe97:bc98",
        "ILO_IP": "tesla-cim1-ilo.rsn.hp.com",
        "ILO_PASSWORD": "hpvse123",
        "EM_IP": "fe80::23a9:c127:ede6:7258",
        "EM1_IP": "fe80::c634:6bff:feb0:3f70",
        "EM2_IP": "",
        "EM_IPV4": "16.114.179.116",
        "HW_DESCRIPTION_FILE": "hw_tesla.js",

        "ENC_SERIAL_NUMBER": "CN75450625",
        "ENC_UUID": "00000000HPMP0E7E",
        "BLADE_DATA": {"1":
                         {"SerialNumber": "CN74250H66",
                          "Model": "Synergy 480 Gen9",
                          "BLADE_ILO_IP6": "FE80::FE15:B4FF:FE12:BD30",
                          "BLADE_ILO_IP4": "16.114.179.176",
                          "BLADE_ILO_FQDN": "tesla01-ilo.rsn.hp.com",
                          "BLADE_ILO_USER": "Administrator",
                          "BLADE_ILO_PW": "hpvse123",
                          "BLADE_TYPE": "BL460t Gen9",
                          "MEZZ_1": "HP FlexFabric Bronco Gen3 2p 20GbE CNA BCM57840",
                          "MEZZ_2": "",
                          "MEZZ_3": "",
                          },
                       },
        "INTERCONNECT_DATA": {"1": {"SerialNumber": "TWA4280042", "Model": "HP VC SE 40Gb F8 Module"},
                              },
        "DISCOVER_TRUTH_FILE": "discover_tesla.js"
    },
}


def get_variables(enclosure_name=None):
    """
    Variable files can have a special get_variables method that returns variables as a mapping.
    """
    variables = enclosure_defaults

    # Get enclosure configuration
    if enclosure_name is not None:
        print "enclosure name: %s" % enclosure_name
        enclosure_configuration = get_enclosure_configuration(enclosure_name)
        if enclosure_configuration is not None:
            for key in enclosure_configuration:
                variables[key] = enclosure_configuration[key]
            origIP = variables['EM_IP']
            print "EM_IP is Static:  %s." % variables['EM_IP']
            variables['EM_IP'] = get_enclosure_manager_ip(variables)
            if variables['EM_IP'] is None:
                variables['EM_IP'] = origIP
            print "EM_IP is FloatingIp:  %s." % variables['EM_IP']
        else:
            print "WARNING: Enclosure '%s' is not known configuration." % enclosure_name
    return variables


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
            logger._warn("Could not connect to %s to determine EM_IP address. \n%s" % (variables['FUSION_IP'], e))
    return None

if __name__ == "__main__":
    """
    Test Program
    """
    import pprint
    import sys

    enclosure_name = ""  # Default to no name
    if len(sys.argv) > 1:
        enclosure_name = sys.argv[1]
    variables = get_variables(enclosure_name)
    print "\nVariables: %s\n" % pprint.pformat(variables)
