"""Rack server Details:"""

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
server_hardwares = [{"name": 'ILOCN77120KF7', "hostname": "16.83.14.77", "username": "Administrator", "password": "password", "force": True, "licensingIntent": "OneView", "configurationState": "Managed"}]
AuthRack = "LTQyMDQ4MTY3NzU3XIvqJIfqvIPaOwSNA0uCQTWrGtrkzxN"
Hardware_UriRack = "38314357-3237-4E43-3737-3132304B4637"
ApplianceRack = "16.83.13.61"
server_hardware = "16.83.14.77"
cred_API = "Administrator:password"
XAPIversion = "X-API-version:1000"

"""synergy server Details"""

Appliance_IP_Synergy = "16.83.10.14"
Server_IP = "16.83.10.69"
AuthSynergy = "NDM4Mzg1Nzg5NjQ5AM4ZEKo2j0RvWyZdLrAKbFs2pNMlK_Aa"
Hardware_UriSynergy = "39314357-3730-4E43-3737-303930335033"

"""C7000 setup details"""

ApplianceC7000 = "16.83.13.61"
Hardware_Uri_C7000 = "38314357-3237-4E43-3737-3132304B4637"
ov_device_dict = {}
device_ov_list = []
device_ilo_list = []
device_dict = {}
LIG1_NAME = "LIG"
EG1_NAME = "EEST_EnclosureGroup"
ENC1_OA1 = "16.83.10.26"
server_hardwareC = "16.83.13.32"
Hardware_UriC = "30373438-3231-4337-4537-303350313432"
enc_groups = [{'name': EG1_NAME, 'configurationScript': None, 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}]}]
enclosures = [{'hostname': ENC1_OA1, 'username': 'Administrator', 'password': 'HPHPHPHP', 'enclosureGroupUri': 'EG:' + EG1_NAME, 'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None, }]
