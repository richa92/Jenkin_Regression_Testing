import sys
from RoboGalaxyLibrary.utilitylib import logging as logger

admin_default_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
storage_system_credentials = [{"hostname": "ovst-3par-7200-01-srv.vse.rdlabs.hpecorp.net", "username": "fusionadm", "password": "hpvse1"},
                              {"hostname": "172.18.11.11", "username": "dcs", "password": "dcs"}]

# Default excluding list for OV resources  (ov-x.json)
licenses = [{'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'},
            {'key': 'YBLG B99A H9PQ 8HVZ U7B5 HWW5 Y9JL KMPL VAWA 8CBE DXAU 2CSM GHTG L762 5NW5 HDV4 KJVT D5KM EFVW DT5J VXP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR JJADJJEDATCA"'}]

enclosures_credentials = {
    "scale-config-sim": {"ov_ip": '15.186.X.X',
                         "oa_credentials": {'oaIpAddress': '192.168.6.0', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                         "vc_credentials": {'vcmIpAddress': '15.178.211.147', 'vcmUsername': 'Administrator', 'vcmPassword': 'Administrator', 'sim': 'True', 'sshUsername': 'root', 'sshPassword': 'jasper'}},
    "scale-config-realAustin4": {"ov_ip": '10.50.3.1',
                                 "oa_credentials": {'oaIpAddress': '15.186.2.223', 'oaUsername': 'Administrator', 'oaPassword': 'compaq'},
                                 "vc_credentials": {'vcmIpAddress': '15.186.20.241', 'vcmUsername': 'Administrator', 'vcmPassword': '6TH2WGZJ'}}}
users_credentials = [{"userName": "appliance", 'password': 'wpsthpvse1'},
                     {"userName": "administrator", 'password': 'wpsthpvse1'},
                     {"userName": "HardwareSetup", 'password': 'wpsthpvse1'},
                     {"userName": "network", 'password': 'wpsthpvse1'},
                     {"userName": "readonly", 'password': 'wpsthpvse1'},
                     {"userName": "server", 'password': 'wpsthpvse1'},
                     {"userName": "storage", 'password': 'wpsthpvse1'}]


san_managers = [{'connectionInfo': [{'name': 'Type', 'value': 'Cisco'},
                                    {'name': 'Host', 'value': '172.18.20.1'},
                                    {'name': 'SnmpPort', 'value': 161},
                                    {'name': 'SnmpUserName', 'value': 'dcs-SHA'},
                                    {'name': 'SnmpAuthString', 'value': 'dcsdcsdcs'},
                                    {'name': 'SnmpAuthLevel', 'value': 'AUTHNOPRIV'},
                                    {'name': 'SnmpAuthProtocol', 'value': 'SHA'}]},
                {'connectionInfo': [{'name': 'Type', 'value': 'Cisco'},
                                    {'name': 'Host', 'value': '172.18.20.2'},
                                    {'name': 'SnmpPort', 'value': 161},
                                    {'name': 'SnmpUserName', 'value': 'dcs-SHA'},
                                    {'name': 'SnmpAuthString', 'value': 'dcsdcsdcs'},
                                    {'name': 'SnmpAuthLevel', 'value': 'AUTHNOPRIV'},
                                    {'name': 'SnmpAuthProtocol', 'value': 'SHA'}]},
                {'connectionInfo': [{'name': 'Type', 'value': 'Brocade Network Advisor'},
                                    {'name': 'Host', 'value': '16.125.71.197'},
                                    {'name': 'Port', 'value': 5989},
                                    {'name': 'Username', 'value': 'Administrator'},
                                    {'name': 'Password', 'value': 'password'},
                                    {'name': 'UseSsl', 'value': True}]}]


def get_variables(enclosure_name=None, OV_IP=None, OV_USERNAME=None, OV_PASSWORD=None):
    """
    Variable files can have a special get_variables method that returns variables as a mapping.
    """
    if enclosure_name is None:
        # logger._log_to_console_and_log_file("WARNING: Enclosure name was not specified {0}".format(__file__))
        admin_credentials = admin_default_credentials
        variables = {
            "ADMIN_CREDENTIALS": admin_credentials,
            "OV_USERNAME": admin_credentials['userName'],
            "OV_PASSWORD": admin_credentials['password'],
            "storage_credentials": storage_system_credentials,
            "san_managers": san_managers,
            "users_credentials": users_credentials
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
            "ALL_ENCLOSURE_CREDENTIALS": enclosures_credentials,
            "storage_credentials": storage_system_credentials,
            "san_managers": san_managers,
            "users_credentials": users_credentials
        }
        return variables
