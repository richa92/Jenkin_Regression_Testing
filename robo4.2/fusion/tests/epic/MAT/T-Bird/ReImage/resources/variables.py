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
    "hafnium": {
        "ILO_PASSWORD": "AcmeAcme",
        "GATEWAY_IP": "10.49.0.1",
        "NETMASK_IP": "255.255.0.0",
        "PRIMARY_DNS": "10.47.0.11",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.49.1.17",
        "ACTIVE_CIM": "10.49.1.16",
        "FUSION_IP": "10.49.1.15",
        "MAINTANENCE_IP": "10.49.1.17",  # Management IP
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
    "serf": {
        "ILO_PASSWORD": "AcmeAcme",
        "GATEWAY_IP": "10.50.0.1",
        "NETMASK_IP": "255.255.0.0",
        "PRIMARY_DNS": "10.47.0.11",
        "ALTERNATE_DNS": "",
        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.50.3.31",
        "ACTIVE_CIM": "10.50.3.30",
        "FUSION_IP": "10.50.3.1",
        "MAINTANENCE_IP": "10.50.3.31",  # Management IP
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
    "TB2": {
        #        "ILO_PASSWORD": "AcmeAcme",
        #        "GATEWAY_IP": "10.49.0.1",
        #        "NETMASK_IP": "255.255.0.0",
        #        "PRIMARY_DNS": "10.49.0.11",
        #        "ALTERNATE_DNS": "",
        #        "DCS": False,
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "10.49.2.17",
        "ACTIVE_CIM": "10.49.2.16",
        "FUSION_IP": "10.49.2.15",
        "MAINTANENCE_IP": "10.49.2.17",  # Management IP
        #        "FUSION_FQDN": "mustang-cim1.rsn.hp.com",
        #        "FUSION_IPV6": "fe80::9eb6:54ff:fe97:5cc8",
        #        "ILO_IP": "16.114.179.124",
        #        "ILO_PASSWORD": "hpvse123",
        "EM_IP": "fe80::c634:6bff:fec9:c7b8",
        #        "EM1_IP": "fe80::c634:6bff:fec9:c7b8",
        #        "EM2_IP": "fe80::c634:6bff:fec9:b7f0",
        #        "EM_IPV4": "16.114.178.166",
        #        "ENC_SERIAL_NUMBER": "00HPMPC01A"
    }}


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
