"""OVF487_OVF488_OVF2394 for C7000"""
# pylint: disable=E0401,E0602

from dto import *

# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin'
}

# Enclosures, Interconnects, Server Hardware, Networks, ULS, LIG, and EG
# Enclosures
ENC1 = 'wpst22'
ENC1_OA1 = "16.125.77.71"
ENC2 = 'wpst23'
ENC2_OA1 = "16.125.77.80"
ENC3 = 'wpst26'
ENC3_OA1 = "16.125.79.45"
# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY1 = '%s, interconnect 1' % ENC3
ENC3ICBAY2 = '%s, interconnect 2' % ENC3
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY4 = '%s, interconnect 4' % ENC3
ENC3ICBAY5 = '%s, interconnect 5' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1  # BL465c Gen8
ENC1SHBAY2 = '%s, bay 2' % ENC1  # BL465c Gen8
ENC1SHBAY3 = '%s, bay 3' % ENC1  # BL465c Gen8
ENC1SHBAY4 = '%s, bay 4' % ENC1  # BL420c Gen8
ENC1SHBAY5 = '%s, bay 5' % ENC1  # BL460c Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1  # BL460c G6
ENC1SHBAY8 = '%s, bay 7' % ENC1  # BL495c G5
ENC1SHBAY14 = '%s, bay 14' % ENC1  # BL460c Gen10
ENC1SHBAY16 = '%s, bay 16' % ENC1  # BL460c Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2  # BL465c Gen8
ENC2SHBAY2 = '%s, bay 2' % ENC2  # BL465c Gen8
ENC2SHBAY3 = '%s, bay 3' % ENC2  # BL465c Gen8
ENC2SHBAY4 = '%s, bay 4' % ENC2  # BL420c Gen8
ENC2SHBAY5 = '%s, bay 5' % ENC2  # BL460c Gen9
ENC2SHBAY6 = '%s, bay 6' % ENC2  # BL460c G6
ENC2SHBAY7 = '%s, bay 7' % ENC2  # BL2x220c G5
ENC2SHBAY10 = '%s, bay 10' % ENC2  # BL460c Gen10
ENC2SHBAY16 = '%s, bay 16' % ENC2  # BL460c Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3  # BL465c Gen8
ENC3SHBAY2 = '%s, bay 2' % ENC3  # BL465c Gen8
ENC3SHBAY3 = '%s, bay 3' % ENC3  # BL465c Gen8
ENC3SHBAY4 = '%s, bay 4' % ENC3  # BL420c Gen8
ENC3SHBAY5 = '%s, bay 5' % ENC3  # BL460c Gen9
ENC3SHBAY7 = '%s, bay 7' % ENC3  # BL660c Gen9
ENC3SHBAY8 = '%s, bay 8' % ENC3  # BL660c Gen8
ENC3SHBAY9 = '%s, bay 9' % ENC3  # BL460c G7
ENC3SHBAY10 = '%s, bay 10' % ENC3  # BL465c G7
# LIGs and EGs
LIG1_NAME = 'LIG22'
EG1_NAME = 'EG22'
LIG2_NAME = 'LIG23'
EG2_NAME = 'EG23'
LIG3_NAME = 'LIG26'
EG3_NAME = 'EG26'

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
]

# OVF487
snmpv3_user1 = 'fvttest1'
snmpv3_user2 = 'fvttest2'
snmpv3_user3 = 'fvttest3'
snmpv3_passphrase = 'wpsthpvse1'
rocommunity1 = 'public'
rocommunity2 = 'abcabc'
rocommunity3 = 'xyzxyz'
ovf487_testhead = 'ENC1'
ovf487_oa = ENC1_OA1
ovf487_oa_username = oa_credentials['username']
ovf487_oa_password = oa_credentials['password']
ovf487_oa_user1 = [
    snmpv3_user1,
    'SHA1',
    snmpv3_passphrase,
    'AES128',
    snmpv3_passphrase]
ovf487_oa_trapreceiver1 = [ovf487_testhead, rocommunity2]
ovf487_oa_trapreceiver2 = [ovf487_testhead, snmpv3_user1]
ovf487_server1 = ENC1SHBAY3
ovf487_ilo1 = '16.125.69.240'
ovf487_server2 = ENC3SHBAY5
ovf487_ilo2 = '16.125.74.164'
ovf487_server3 = ENC1SHBAY14
ovf487_ilo3 = '16.125.73.236'

# Trap Listner
trap_listener = 'TrapListener.py'

# OVF488 SNMPv3 trap destination
ovf488_testhead = 'fvt_linux_testhead.vse.rdlabs.hpecorp.net'
ovf488_testhead_username = 'root'
ovf488_testhead_password = 'hpvse1'
ovf488_trap_forwarding_user = {
    "type": "Users", "userName": snmpv3_user2,
    "securityLevel": "Authentication and privacy",
    "authenticationProtocol": "SHA1",
    "authenticationPassphrase": snmpv3_passphrase,
    "privacyProtocol": "AES-256", "privacyPassphrase": snmpv3_passphrase
}
ovf488_edit_trap_forwarding_user = {
    "type": "Users", "userName": snmpv3_user2,
    "securityLevel": "Authentication and privacy",
    "authenticationProtocol": "SHA256",
    "authenticationPassphrase": snmpv3_passphrase,
    "privacyProtocol": "AES-256", "privacyPassphrase": snmpv3_passphrase
}
ovf488_trap_destination = {
    "type": "Destination", "destinationAddress": ovf488_testhead, "port": 2161,
    "userId": "", "userUri": ""
}
ovf488_edit_trap_destination = {
    "type": "Destination", "destinationAddress": ovf488_testhead, "port": 2162,
    "userId": "", "userUri": ""
}
ovf488_data_size = 300
ovf488_status_file = '/root/trap_forwarding/C7000_OVF488_status_file'
ovf488_log_file = '/root/trap_forwarding/C7000_OVF488_log_file'
ovf488_fw_required = "ACCEPT\\s+udp\\s+--\\s+fvt-ring1.vse.rdlabs.hpecorp.net\\s+fvtlinuxtesthead.vse.rdlabs.hpecorp.net\\sudp\\sdpt:navisphere"

# OVF2394 SNMPv1 trap destination
ovf2394_testhead = 'fvt_linux_testhead.vse.rdlabs.hpecorp.net'
ovf2394_testhead_username = 'root'
ovf2394_testhead_password = 'hpvse1'
ovf2394_trap_destination = {
    "destination": ovf2394_testhead,
    "communityString": "public",
    "uri": "/rest/appliance/trap-destinations/1",
    "port": 2161
}
ovf2394_edit_trap_destination = {
    "destination": ovf2394_testhead,
    "communityString": "public",
    "uri": "/rest/appliance/trap-destinations/1",
    "port": 2162
}
ovf2394_data_size = 150
ovf2394_status_file = '/root/trap_forwarding/C7000_OVF2394_status_file'
ovf2394_log_file = '/root/trap_forwarding/C7000_OVF2394_log_file'
