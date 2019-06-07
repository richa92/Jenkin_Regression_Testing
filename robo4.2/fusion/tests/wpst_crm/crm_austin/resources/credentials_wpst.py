import sys

admin_credentials = {}
admin_default_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
"""
    Store credentials for WPST
        = Usage =
    | *** Settings *** |
    | variables | resources/credentials_wpst.py |
    | variables | resources/credentials_wpst.py | ${ENCLOSURE} |
    | pybot --variablefile resources/credentials_wpst.py |
    | pybot --variablefile resources/credentials_wpst.py:<EnclosureName> |
"""

from RoboGalaxyLibrary.utilitylib import logging as logger

enclosures_credentials = {
    "Austin1": {"ov_ip": '15.186.8.61',
                "oa_credentials": {'oaIpAddress': '15.186.2.214', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.18.82', 'vcmUsername': 'Administrator', 'vcmPassword': '9WWX4H07'},
                },
    "Austin2": {"ov_ip": '15.186.8.62',
                "oa_credentials": {'oaIpAddress': '15.186.2.79', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.20.255', 'vcmUsername': 'Administrator', 'vcmPassword': 'DCCNQXF0'},
                },
    "Austin3": {"ov_ip": '15.186.8.63',
                "oa_credentials": {'oaIpAddress': '15.186.2.201', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.20.82', 'vcmUsername': 'Administrator', 'vcmPassword': '0SJ09BHF'}
                },
    "Austin4": {"ov_ip": '15.186.8.64',
                "oa_credentials": {'oaIpAddress': '15.186.2.223', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.20.241', 'vcmUsername': 'Administrator', 'vcmPassword': '6TH2WGZJ'}
                },
    "Austin5": {"ov_ip": '15.186.8.65',
                "oa_credentials": {'oaIpAddress': '15.186.2.220', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.19.68', 'vcmUsername': 'Administrator', 'vcmPassword': '8GB3Z4KW'}
                },
    # The above enclosures are reserved with static IP and should not get modified!
    "DualHop": {"ov_ip": '15.186.X.X',
                "oa_credentials": {'oaIpAddress': '15.186.2.227', 'oaUsername': 'Administrator', 'oaPassword': 'Compaq123'},
                "vc_credentials": {'vcmIpAddress': '15.186.16.247', 'vcmUsername': 'Administrator', 'vcmPassword': '7Q04WX09'},
                }
}


def get_variables(enclosure_name=None, OV_IP=None, OV_USERNAME=None, OV_PASSWORD=None):
    """
    Variable files can have a special get_variables method that returns variables as a mapping.
    """

    if enclosure_name is None:
        logger._log_to_console_and_log_file("WARNING: Enclosure name was not specified {0}".format(__file__))
        if OV_IP is None:
            logger._log_to_console_and_log_file("ERROR: OneView IP/FQDN was not specified but required in the absence of enclosure name argument in {1}".format(__file__))
            sys.exit("ERROR: OneView IP/FQDN was not specified but required in the absence of enclosure name argument in {1}".format(__file__))

        variables = {
            "ADMIN_CREDENTIALS": admin_default_credentials,
            "OV_IP": OV_IP,
            "OV_USERNAME": OV_USERNAME if OV_USERNAME else admin_credentials['userName'],
            "OV_PASSWORD": OV_PASSWORD if OV_PASSWORD else admin_credentials['password']
        }
        return variables
    elif enclosure_name not in enclosures_credentials.keys():
        logger._log_to_console_and_log_file("ERROR: Could not find credential data for enclosure \"{0}\" in {1}".format(enclosure_name, __file__))
        sys.exit("ERROR: Could not find credential data for enclosure \"{0}\" in {1}".format(enclosure_name, __file__))
    else:
        logger._log_to_console_and_log_file("Loading credentials data for enclosure '%s'." % enclosure_name)

        cur_enc = enclosures_credentials[enclosure_name]
        if 'ov_credentials' in cur_enc.keys():
            admin_credentials = cur_enc['ov_credentials']
        else:
            admin_credentials = admin_default_credentials

        if OV_USERNAME:
            admin_credentials['userName'] = OV_USERNAME
        if OV_PASSWORD:
            admin_credentials['password'] = OV_PASSWORD

        variables = {
            "OV_IP": OV_IP if OV_IP else cur_enc['ov_ip'],
            "ADMIN_CREDENTIALS": admin_credentials,
            "OV_USERNAME": admin_credentials['userName'],
            "OV_PASSWORD": admin_credentials['password'],
            "OA_CREDENTIAL_DATA": cur_enc['oa_credentials'],
            "VC_CREDENTIAL_DATA": cur_enc['vc_credentials'],
            "OAVC_CREDENTIALS": dict(cur_enc['oa_credentials'].items() + cur_enc['vc_credentials'].items()),
        }

        return variables
