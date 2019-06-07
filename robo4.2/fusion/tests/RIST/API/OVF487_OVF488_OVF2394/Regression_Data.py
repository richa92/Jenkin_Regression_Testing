# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {
    'mgmt_ip': '16.71.149.173',
    'username': 'admin',
    'password': 'admin'}

# Resource types for X-API-Version=600
ENCLOSURE_TYPE = 'EnclosureV400'

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'
# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1    # SY680 Gen9
ENC1SHBAY5 = '%s, bay 5' % ENC1    # SY660 Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1    # SY480 Gen10
ENC1SHBAY7 = '%s, bay 7' % ENC1    # SY480 Gen9
ENC1SHBAY8 = '%s, bay 8' % ENC1    # SY480 Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2    # SY480 Gen9
ENC2SHBAY5 = '%s, bay 5' % ENC2    # SY660 Gen9
ENC2SHBAY7 = '%s, bay 7' % ENC2    # SY480 Gen10
ENC2SHBAY8 = '%s, bay 8' % ENC2    # SY480 Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3    # SY480 Gen9
ENC3SHBAY5 = '%s, bay 5' % ENC3    # SY680 Gen9

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": ENC1, },
    {"type": ENCLOSURE_TYPE, "name": ENC2, },
    {"type": ENCLOSURE_TYPE, "name": ENC3, },
]

# OVF487
snmpv3_user1 = 'fvttest1'
snmpv3_user2 = 'fvttest2'
snmpv3_user3 = 'fvttest3'
snmpv3_passphrase = 'wpsthpvse1'
rocommunity1 = 'public'
rocommunity2 = 'abcabc'
rocommunity3 = 'xyzxyz'
ovf487_enc = ENC1
ovf487_server1 = ENC2SHBAY1
ovf487_server2 = ENC2SHBAY8

# Trap Listner
trap_listener = 'TrapListener.py'

# OVF488 SNMPv3 trap destination
ovf488_testhead = 'fvt_linux_testhead.vse.rdlabs.hpecorp.net'
ovf488_testhead_username = 'root'
ovf488_testhead_password = 'hpvse1'
ovf488_trap_forwarding_user = {"type": "Users", "userName": snmpv3_user2, "securityLevel": "Authentication and privacy",
                               "authenticationProtocol": "SHA1", "authenticationPassphrase": snmpv3_passphrase,
                               "privacyProtocol": "AES-256", "privacyPassphrase": snmpv3_passphrase}
ovf488_edit_trap_forwarding_user = {"type": "Users", "userName": snmpv3_user2, "securityLevel": "Authentication and privacy",
                                    "authenticationProtocol": "SHA256", "authenticationPassphrase": snmpv3_passphrase,
                                    "privacyProtocol": "AES-256", "privacyPassphrase": snmpv3_passphrase}
ovf488_trap_destination = {"type": "Destination", "destinationAddress": ovf488_testhead, "port": 2161,
                           "userId": "", "userUri": ""}
ovf488_edit_trap_destination = {"type": "Destination", "destinationAddress": ovf488_testhead, "port": 2162,
                                "userId": "", "userUri": ""}
ovf488_data_size = 300
ovf488_status_file = '/root/trap_forwarding/Synergy_OVF488_status_file'
ovf488_log_file = '/root/trap_forwarding/Synergy_OVF488_log_file'
ovf488_fw_required = "ACCEPT\\s+udp\\s+--\\s+fvt-ring1.vse.rdlabs.hpecorp.net\\s+fvtlinuxtesthead.vse.rdlabs.hpecorp.net\\sudp\\sdpt:navisphere"

# OVF2394 SNMPv1 trap destination
ovf2394_testhead = 'fvt_linux_testhead.vse.rdlabs.hpecorp.net'
ovf2394_testhead_username = 'root'
ovf2394_testhead_password = 'hpvse1'
ovf2394_trap_destination = {
    "destination": ovf2394_testhead,
    "communityString": "public",
    "uri": "/rest/appliance/trap-destinations/1",
    "port": 2161}
ovf2394_edit_trap_destination = {
    "destination": ovf2394_testhead,
    "communityString": "public",
    "uri": "/rest/appliance/trap-destinations/1",
    "port": 2162}
ovf2394_data_size = 150
ovf2394_status_file = '/root/trap_forwarding/Synergy_OVF2394_status_file'
ovf2394_log_file = '/root/trap_forwarding/Synergy_OVF2394_log_file'
