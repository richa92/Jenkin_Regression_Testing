"""resources/variables.py - Default variables used for Comet RoboGalaxyLibrary testing

    = Usage =
        | *** Settings ***      |
        | variables | resources/variables.py |
        | variables | resources/variables.py | ${FUSION IP} | ${SWTICH} |

        | pybot --variablefile resources/variables.py |
        | pybot --variablefile resources/variables.py:<Fusion_IP>:<SWITCH> |
"""

default_variables = {
    # Fusion Details and Credentials
    "FUSION_IP": 'unknown',          # Fusion Appliance IP Address
    "FUSION_USERNAME": 'Administrator',    # Fusion Appliance Username
    "FUSION_PASSWORD": 'hpvse123',         # Fusion Appliance Password
    "FUSION_SSH_USERNAME": 'root',             # Fusion SSH Username
    "FUSION_SSH_PASSWORD": 'hpvse1',           # Fusion SSH Password
    "FUSION_FACTORY_PASSWORD": "admin",        # Fusion Factory Default Password
    "FUSION_PROMPT": '#',
    "FUSION_TIMEOUT": 300,

    # Second Fusion VM Details and Credentials
    "2ND_FUSION_IP": 'unknown',          # Fusion Appliance IP Address
    "2ND_FUSION_USERNAME": 'Administrator',    # Fusion Appliance Username
    "2ND_FUSION_PASSWORD": 'hpvse123',         # Fusion Appliance Password
    "2ND_FUSION_SSH_USERNAME": 'root',             # Fusion SSH Username
    "2ND_FUSION_SSH_PASSWORD": 'hpvse1',           # Fusion SSH Password

    # Switch Credentials
    "SWITCH_IP": 'unknown',          # Switch IP address
    "SWITCH_USERNAME": 'Administrator',    # Switch Username
    "SWITCH_PASSWORD": 'hpvse123',         # Switch Password
    "SWITCH_GATEWAY_IP": '16.119.96.1',      # LC switch gateway IP
    "SWITCH_PROMPT": '>',
    "SWITCH_TIMEOUT": 300,

    # Serial DL Server Details and Credentials
    "SERIAL_DL_OS": 'unknown',
    "SERIAL_DL_MODEL": 'unknown',
    "SERIAL_DL_IP": 'unknown',          # Serial DL Server Primary NIC IP Address (server access to switch serial port)
    "SERIAL_DL_HOSTNAME": 'unknown',          # Serial DL Server Primary NIC Hostname (server access to switch serial port)
    "SERIAL_DL_USERNAME": 'root',             # Serial DL Server Primary NIC Username (server access to switch serial port)
    "SERIAL_DL_PASSWORD": 'hpinvent1',        # Serial DL Server Primary NIC Password (server access to switch serial port)
    "SERIAL_DL_ILO_IP": 'unknown',
    "SERIAL_DL_ILO_USERNAME": 'Administrator',
    "SERIAL_DL_ILO_PASSWORD": 'hpvse123',

    # Default Logical Interconnect group name, Logical Interconnect name and Interconnect type
    "LIG_NAME": 'LIG',
    "LI_NAME": 'LI',
    "I_NAME": 'HP 5900AF-48XG-4QSFP+ Switch',

    # Gui/Selenium defaults
    "BROWSER": 'firefox',
    "FUSION_GUI_DELAY": 5,
}

switch_configurations = {
    "hou-sw1": {
        "SWITCH_HOSTNAME": 'hou-sw1',
        "SWITCH_IP": '10.51.0.28',
        "SERIAL_DL_HOSTNAME": '10.51.0.25',
    },
    "hyd-sw1": {
        "SWITCH_HOSTNAME": 'hyd-sw1',
        "SWITCH_IP": '16.119.102.220',
        "SERIAL_DL_HOSTNAME": 'udrogono.rsn.hp.com',
    },
    "hyd-sw2": {
        "SWITCH_HOSTNAME": 'hyd-sw2',
        "SWITCH_IP": '16.119.102.221',
        "SERIAL_DL_HOSTNAME": 'wodor.rsn.hp.com'
    },
    "hyd-sw3": {
        "SWITCH_HOSTNAME": 'hyd-sw3',
        "SWITCH_IP": '16.119.98.152',
        "SERIAL_DL_HOSTNAME": 'vety.rsn.hp.com',
    },
    "hyd-sw4": {
        "SWITCH_HOSTNAME": 'hyd-sw4',
        "SWITCH_IP": '16.119.98.155',
        "SERIAL_DL_HOSTNAME": 'brint.rsn.hp.com',
    },
    "hyd-sw5": {
        "SWITCH_HOSTNAME": 'hyd-sw5',
        "SWITCH_IP": '16.119.98.156',
        "SERIAL_DL_HOSTNAME": 'vate.rsn.hp.com',
    },
    "hyd-sw6": {
        "SWITCH_HOSTNAME": 'hyd-sw6',
        "SWITCH_IP": '16.119.98.158',
        "SERIAL_DL_HOSTNAME": 'vesinik.rsn.hp.com',
    },
}

serial_dl_configurations = {
    "vate.rsn.hp.com": {
        "SERIAL_DL_OS": 'SLES11',
        "SERIAL_DL_MODEL": 'dl560',
        "SERIAL_DL_IP": '16.119.102.228',
        "SERIAL_DL_PASSWORD": 'hpvse123',
        "SERIAL_DL_ILO_IP": '16.119.102.234',
    },
    "vety.rsn.hp.com": {
        "SERIAL_DL_OS": 'SLES11',
        "SERIAL_DL_MODEL": 'dl385p',
        "SERIAL_DL_IP": '16.119.102.225',
        "SERIAL_DL_PASSWORD": 'hpvse123',
        "SERIAL_DL_ILO_IP": '16.119.102.231',
    },
    "brint.rsn.hp.com": {
        "SERIAL_DL_OS": 'SLES11',
        "SERIAL_DL_MODEL": 'dl385p',
        "SERIAL_DL_IP": '16.119.102.224',
        "SERIAL_DL_PASSWORD": 'hpvse123',
        "SERIAL_DL_ILO_IP": '16.119.102.230',
    },
    "wodor.rsn.hp.com": {
        "SERIAL_DL_OS": 'SLES11',
        "SERIAL_DL_MODEL": 'dl380p',
        "SERIAL_DL_IP": '16.119.102.227',
        "SERIAL_DL_PASSWORD": 'hpvse123',
        "SERIAL_DL_ILO_IP": '16.119.102.233',
    },
    "udrogono.rsn.hp.com": {
        "SERIAL_DL_OS": 'SLES11',
        "SERIAL_DL_MODEL": 'dl380p',
        "SERIAL_DL_IP": '16.119.102.226',
        "SERIAL_DL_PASSWORD": 'hpvse123',
        "SERIAL_DL_ILO_IP": '16.119.102.232',
    },
    "vesinik.rsn.hp.com": {
        "SERIAL_DL_OS": 'SLES11',
        "SERIAL_DL_MODEL": 'dl360p',
        "SERIAL_DL_IP": '16.119.102.229',
        "SERIAL_DL_PASSWORD": 'hpvse123',
        "SERIAL_DL_ILO_IP": '16.119.102.235',
    },
    "10.51.0.25": {                                         # DL serving Houston 5900 switch
        "SERIAL_DL_IP": '10.51.0.25',
        "SERIAL_DL_PASSWORD": 'Hpinvent1',
        "SERIAL_DL_ILO_IP": '10.51.0.25',
        "SWITCH_GATEWAY_IP": '10.51.0.1',  # HOU switch gateway IP
    },
}


def get_variables(fusion_ip=None, switch=None):
    """Variable files can have a special get_variables method that returns variables as a mapping.
    """
    variables = default_variables

    # Set Fusion IP
    if fusion_ip is not None:
        print "Fusion IP: %s" % fusion_ip
        variables["FUSION_IP"] = fusion_ip

    # Get Switch and Serial DL Configurations
    if switch is not None:
        # Find out if Switch is a known configuration
        print "Switch: %s" % switch
        switch_configuration = get_switch_configuration(switch)
        if switch_configuration is not None:
            for key in switch_configuration:
                variables[key] = switch_configuration[key]
            # Find out if Serial DL is a known configuration
            print "Switch IP: %s" % variables["SWITCH_IP"]
            serial_dl_configuration = get_serial_dl_configuration(variables["SERIAL_DL_HOSTNAME"])
            if serial_dl_configuration is not None:
                for key in serial_dl_configuration:
                    variables[key] = serial_dl_configuration[key]
            else:
                print "WARNING: Serial DL '%s' is not a known configuration." % switch_configuration[key]
        else:
            print "WARNING: Switch '%s' is not a known configuration." % switch

    return variables


def get_switch_configuration(switch):
    """ Returns stored switch configuration information from specified switch name or IP address.

    Example:
        get_switch_configuration("hyd-sw1")
        get_switch_configuration("16.119.102.221")
    """

    for switch_name in switch_configurations:
        if switch_name == switch or switch_configurations[switch_name]["SWITCH_IP"] == switch:
            return switch_configurations[switch_name]
    return None


def get_serial_dl_configuration(hostname):
    """ Returns stored serial dl server configuration information from specified hostname.
        Full name specification is required.

    Example:
        get_serial_dl_configuration("wordor.rsn.hp.com")
    """

    for dl_hostname in serial_dl_configurations:
        if hostname == dl_hostname:
            return serial_dl_configurations[dl_hostname]
    return None


def print_variables(fusion_ip=None, switch=None):
    variables = get_variables(fusion_ip, switch)
    print "\nVariables: %s\n" % pprint.pformat(variables)


if __name__ == '__main__':
    """ Test Program
    """
    import pprint
    import sys

    fusion_ip = None
    if len(sys.argv) > 1:
        fusion_ip = sys.argv[1]

    switch = None
    if len(sys.argv) > 2:
        switch = sys.argv[2]

    print_variables(fusion_ip, switch)
