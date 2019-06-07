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
                "vc_credentials": {'vcmIpAddress': '15.186.19.254', 'vcmUsername': 'Administrator', 'vcmPassword': 'NKTWSQ5S'},
               },
    "Austin2": {"ov_ip": '15.186.8.62',
                "oa_credentials": {'oaIpAddress': '15.186.2.79', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.11.242', 'vcmUsername': 'Administrator', 'vcmPassword': 'DCCNQXF0'},
               },
    "Austin3": {"ov_ip": '15.186.8.63',
                "oa_credentials": {'oaIpAddress': '15.186.2.201', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.20.82', 'vcmUsername': 'Administrator', 'vcmPassword': '0SJ09BHF'}
               },
    "Austin4": {"ov_ip": '15.186.8.64',
                "oa_credentials": {'oaIpAddress': '15.186.2.223', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.11.197', 'vcmUsername': 'Administrator', 'vcmPassword': '6TH2WGZJ'}
               },
    "Austin5": {"ov_ip": '15.186.22.37',
                "oa_credentials": {'oaIpAddress': '15.186.2.220', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.19.68', 'vcmUsername': 'Administrator', 'vcmPassword': '8GB3Z4KW'}
               },
    "Enc181": {"ov_ip": '15.186.22.65',
                "oa_credentials": {'oaIpAddress': '15.186.2.220', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.19.68', 'vcmUsername': 'Administrator', 'vcmPassword': '8GB3Z4KW'}
               },
    "Enc181-1": {"ov_ip": '15.186.22.66',
                "oa_credentials": {'oaIpAddress': '15.186.2.220', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                "vc_credentials": {'vcmIpAddress': '15.186.19.68', 'vcmUsername': 'Administrator', 'vcmPassword': '8GB3Z4KW'}
               },
    "FIT3-el-53": {"ov_ip": '15.186.19.159',
                   "oa_credentials": {'oaIpAddress': '15.178.209.72', 'oaUsername': 'Administrator', 'oaPassword': 'Compaq123'},
                   "vc_credentials": {'vcmIpAddress': '15.178.219.242', 'vcmUsername': 'Administrator', 'vcmPassword': 'YY9RTFZQ'}
                  },
    "FIT3-el-52": {"ov_ip": '15.186.19.159',
                   "oa_credentials": {'oaIpAddress': '15.178.209.73', 'oaUsername': 'Administrator', 'oaPassword': 'Compaq123'},
                   "vc_credentials": {'vcmIpAddress': '15.178.218.156', 'vcmUsername': 'Administrator', 'vcmPassword': 'Q4X02PXF'}
                  },
    "FIT3-el-55": {"ov_ip": '15.186.19.159',
                   "oa_credentials": {'oaIpAddress': '15.178.209.81', 'oaUsername': 'Administrator', 'oaPassword': 'Compaq123'},
                   "vc_credentials": {'vcmIpAddress': '15.178.215.66', 'vcmUsername': 'Administrator', 'vcmPassword': '92XZCR88'}
                  },
    "FIT3-el-56": {"ov_ip": '15.186.19.159',
                   "oa_credentials": {'oaIpAddress': '15.178.209.82', 'oaUsername': 'Administrator', 'oaPassword': 'Compaq123'},
                   "vc_credentials": {'vcmIpAddress': '15.178.214.32', 'vcmUsername': 'Administrator', 'vcmPassword': '03B9NWRV'}
                   }
    }

def get_variables(enclosure_name=None):
    """
    Variable files can have a special get_variables method that returns variables as a mapping.
    """
    if enclosure_name is None:
        logger._log_to_console_and_log_file("ERROR: Please specify an enclosure name from {0}".format( __file__))
    elif enclosure_name not in enclosures_credentials.keys():
        logger._log_to_console_and_log_file("ERROR: Could not find credential data for enclosure {0} in {1}".format(enclosure_name, __file__))
    else:
        logger._log_to_console_and_log_file("Loading credentials data for enclosure '%s'." % enclosure_name)
        cur_enc = enclosures_credentials [enclosure_name]
        if 'ov_credentials' in cur_enc.keys():
            admin_credentials = cur_enc['ov_credentials']
        else:
            admin_credentials = admin_default_credentials
        variables = {
        "OV_IP": cur_enc['ov_ip'],
        "ADMIN_CREDENTIALS": admin_credentials,
        "OV_USERNAME": admin_credentials['userName'],
        "OV_PASSWORD": admin_credentials['password'],
        "OA_CREDENTIAL_DATA": cur_enc['oa_credentials'],
        "VC_CREDENTIAL_DATA": cur_enc['vc_credentials'],
        "OAVC_CREDENTIALS": dict(cur_enc['oa_credentials'].items() + cur_enc['vc_credentials'].items())
        }
        return variables

