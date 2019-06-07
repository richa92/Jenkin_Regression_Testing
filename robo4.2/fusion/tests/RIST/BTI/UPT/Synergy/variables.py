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
    "Ring4ActiveCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.208.115",
        "ACTIVE_CIM": "16.114.208.114",
        "FUSION_IP": "16.114.208.113",
        "MAINTANENCE_IP": "16.114.208.113",
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "",
        "EM_SERIAL": "MXQ831078H"
    },
    "Ring4StandbyCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.208.115",
        "ACTIVE_CIM": "16.114.208.114",
        "FUSION_IP": "16.114.208.113",
        "MAINTANENCE_IP": "16.114.208.113",
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "",
        "EM_SERIAL": "MXQ8320169"
    },
    "Ring5ActiveCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.217.102",
        "ACTIVE_CIM": "16.114.217.101",
        "FUSION_IP": "16.114.217.100",
        "MAINTANENCE_IP": "16.114.217.100",
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "",
        "EM_SERIAL": "MXQ80805DK"
    },
    "Ring5StandbyCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.217.102",
        "ACTIVE_CIM": "16.114.217.101",
        "FUSION_IP": "16.114.217.100",
        "MAINTANENCE_IP": "16.114.217.100",
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "",
        "EM_SERIAL": "MXQ81100P9"
    },
    "Ring6ActiveCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.217.107",
        "ACTIVE_CIM": "16.114.217.106",
        "FUSION_IP": "16.114.217.105",
        "MAINTANENCE_IP": "16.114.217.105",
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "",
        "EM_SERIAL": "MXQ645027K"
    },
    "Ring6StandbyCIM": {
        "FUSION_SSH_USERNAME": "root",
        "FUSION_SSH_PASSWORD": "hpvse1",
        "STANDBY_CIM": "16.114.217.107",
        "ACTIVE_CIM": "16.114.217.106",
        "FUSION_IP": "16.114.217.105",
        "MAINTANENCE_IP": "16.114.217.105",
        "FUSION_FQDN": "",
        "FUSION_IPV6": "",
        "ILO_IP": "",
        "ILO_PASSWORD": "",
        "EM_IP": "",
        "EM_SERIAL": "MXQ6450369"
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
            matches = re.search(
                r'MgmtIP:\s*(\S*:\S*:\S*:\S*:\S*:\S*)',
                output,
                re.MULTILINE)
            if matches:
                print "lldpcli call and regex match succeeded."
                return matches.group(1)
        except paramiko.BadHostKeyException:
            logger._warn(
                "Could not connect to %s because of BadKeyException.  Need to clean up .ssh directory?" %
                variables['FUSION_IP'])
        except Exception as e:
            logger._warn(
                "Could not connect to %s to determine EM_IP address. \n%s" %
                (variables['FUSION_IP'], e))
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
