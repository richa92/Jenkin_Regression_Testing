import sys

admin_credentials = {}
admin_default_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
"""
    Store credentials for CI-FIT
        = Usage =
    | *** Settings *** |
    | variables | resources/credentials_cifit.py |
    | variables | resources/credentials_cifit.py | ${ENCLOSURE} |
    | pybot --variablefile resources/credentials_cifit.py |
    | pybot --variablefile resources/credentials_cifit.py:<EnclosureName> |
"""

from RoboGalaxyLibrary.utilitylib import logging as logger

enclosures_credentials = {
    "C15M_Bmark": {"ov_ip": '15.186.x.x',
                   "oa_credentials": {'oaIpAddress': '15.178.212.165', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                   "vc_credentials": {'vcmIpAddress': 'x.x.x.x', 'vcmUsername': 'Administrator', 'vcmPassword': 'P0HHHP00'},
                   },
    "CI-FIT-1": {"ov_ip": '15.186.x.x',
                 "oa_credentials": {'oaIpAddress': '15.186.2.184', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                 "vc_credentials": {'vcmIpAddress': '15.186.x.x', 'vcmUsername': 'Administrator', 'vcmPassword': 'DDDG6Q2T'},
                 },
    "CI-FIT-2": {"ov_ip": '[fdaa:bbbb:cccc:dddd:1111:2222:1234:9440]',
                 "oa_credentials": {'oaIpAddress': 'fdaa:bbbb:cccc:dddd::ef8f', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                 "vc_credentials": {'vcmIpAddress': 'fdaa:bbbb:x:x', 'vcmUsername': 'Administrator', 'vcmPassword': 'P3JVVFCC'},
                 },
    "CI-FIT-3": {"ov_ip": '[fdaa:bbbb:cccc:dddd:x:x:x:x]',
                 "oa_credentials": {'oaIpAddress': 'fdaa:bbbb:cccc:dddd:1111:2222:1234:9903', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                 "vc_credentials": {'vcmIpAddress': 'fdaa:bbbb:x:x', 'vcmUsername': 'Administrator', 'vcmPassword': 'ZBCMZX53'},
                 },
    "CI-FIT-12": {"ov_ip": '[fdaa:bbbb:cccc:dddd:1111:2222:1234:1007]',
                  "oa_credentials": {'oaIpAddress': 'fdaa:bbbb:cccc:dddd:1111:2222:1234:12', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                  "vc_credentials": {'vcmIpAddress': 'x.x.x.x', 'vcmUsername': 'Administrator', 'vcmPassword': 'toe-tag'},
                  },
    "CI-FIT-16": {"ov_ip": '[fdaa:bbbb:cccc:dddd:1111:2222:1234:1007]',
                  "oa_credentials": {'oaIpAddress': 'fdaa:bbbb:cccc:dddd:1111:2222:1234:16', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                  "vc_credentials": {'vcmIpAddress': 'x.x.x.x', 'vcmUsername': 'Administrator', 'vcmPassword': 'toe-tag'},
                  },
    "CI-FIT-17": {"ov_ip": '[fdaa:bbbb:cccc:dddd:1111:2222:1234:1007]',
                  "oa_credentials": {'oaIpAddress': 'fdaa:bbbb:cccc:dddd:1111:2222:1234:17', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                  "vc_credentials": {'vcmIpAddress': 'x.x.x.x', 'vcmUsername': 'Administrator', 'vcmPassword': 'toe-tag'},
                  },
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
