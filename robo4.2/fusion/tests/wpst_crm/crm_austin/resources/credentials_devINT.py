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
    "int1": { "ov_ip": '15.186.8.81',
              "oa_credentials": {'oaIpAddress': '15.186.2.219', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
              "vc_credentials": {'vcmIpAddress': '15.186.10.255', 'vcmUsername': 'Administrator', 'vcmPassword': 'Z448PJ8Z'}
              # ov_credentials :{'ovUsername': 'ovUsername', 'ovPassword': 'ovPassword'}
             },
    "int2": { "ov_ip": '15.186.8.82',
              "oa_credentials": {'oaIpAddress': '15.178.209.147', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
              "vc_credentials": {'vcmIpAddress': '15.178.218.68', 'vcmUsername': 'Administrator', 'vcmPassword': 'FPHRR3BV'}
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

