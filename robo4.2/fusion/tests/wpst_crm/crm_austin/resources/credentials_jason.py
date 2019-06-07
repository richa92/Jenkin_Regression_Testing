import sys
from RoboGalaxyLibrary.utilitylib import logging as logger
"""
    Store credentials for Dev INT
        = Usage =
    | *** Settings *** |
    | variables | resources/credentials_devINT.py |
    | variables | resources/credentials_devINT.py | ${ENCLOSURE} |
    | pybot --variablefile resources/credentials_devINT.py |
    | pybot --variablefile resources/credentials_devINT.py:<EnclosureName> |
"""


admin_default_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

enclosures_credentials = {
    "vc-bvt-backup": {"ov_ip": '15.186.21.158',
                      "oa_credentials": {'oaIpAddress': '15.178.222.237', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                      "vc_credentials": {'vcmIpAddress': '15.178.217.98', 'vcmUsername': 'Administrator', 'vcmPassword': 'NG5Z8HWZ'}
                      },
    "scale-config-431-sim": {"ov_ip": '15.186.X.X',
                             "oa_credentials": {'oaIpAddress': '192.168.6.0', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                             "vc_credentials": {'vcmIpAddress': '15.178.216.19', 'vcmUsername': 'Administrator', 'vcmPassword': 'Administrator', 'sim': 'True', 'sshUsername': 'root', 'sshPassword': 'somerootpassword'}
                             },
    "scale-config-431-realAustin4": {"ov_ip": '15.186.X.X',
                                     "oa_credentials": {'oaIpAddress': '15.186.2.223', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                                     "vc_credentials": {'vcmIpAddress': '15.186.20.69', 'vcmUsername': 'Administrator', 'vcmPassword': '6TH2WGZJ'}
                                     },
    "scale-config-sim": {"ov_ip": '15.186.X.X',
                             "oa_credentials": {'oaIpAddress': '192.168.6.0', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                             "vc_credentials": {'vcmIpAddress': '15.178.211.147', 'vcmUsername': 'Administrator', 'vcmPassword': 'Administrator', 'sim': 'True', 'sshUsername': 'root', 'sshPassword': 'jasper'}
                             },
    "scale-config-realAustin4": {"ov_ip": '15.186.X.X',
                                     "oa_credentials": {'oaIpAddress': '15.186.2.223', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                                     "vc_credentials": {'vcmIpAddress': '15.186.20.241', 'vcmUsername': 'Administrator', 'vcmPassword': '6TH2WGZJ'}
                                     }
}


def get_variables(enclosure_name=None, OV_IP=None, OV_USERNAME=None, OV_PASSWORD=None):
    """
    Variable files can have a special get_variables method that returns variables as a mapping.
    """
    if enclosure_name is None:
        logger._log_to_console_and_log_file("WARNING: Enclosure name was not specified {0}".format(__file__))
        admin_credentials = admin_default_credentials
        variables = {
            "ADMIN_CREDENTIALS": admin_credentials,
            "OV_USERNAME": admin_credentials['userName'],
            "OV_PASSWORD": admin_credentials['password']
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
        logger._log_to_console_and_log_file("DEBUG: %s" % OV_IP)
        variables = {
            "OV_IP": OV_IP if OV_IP else cur_enc['ov_ip'],
            "ADMIN_CREDENTIALS": admin_credentials,
            "OV_USERNAME": admin_credentials['userName'],
            "OV_PASSWORD": admin_credentials['password'],
            "OA_CREDENTIAL_DATA": cur_enc['oa_credentials'],
            "VC_CREDENTIAL_DATA": cur_enc['vc_credentials'],
            "OAVC_CREDENTIALS": dict(cur_enc['oa_credentials'].items() + cur_enc['vc_credentials'].items()),
            "ALL_ENCLOSURE_CREDENTIALS": enclosures_credentials
        }
        return variables
