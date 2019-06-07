"""Rack server Details:"""
FUSION_ADMIN_LOGIN = ""
FUSION_ADMIN_PASSWORD = ""
FUSION_IP = ""
DATA_FILE = ""

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
server_hardwares = [{"name": 'DL360Gen10', "hostname": "172.18.31.3", "username": "dcs",
                     "password": "dcs", "force": True, "licensingIntent": "OneView", "configurationState": "Managed"}]
Hardware_UriRack = "34343738-3036-584D-5131-303030323131"

APPLIANCE_IP_Rack = "16.83.10.115"
server_hardware = "172.18.31.3"
cred_API = "dcs:dcs"
XAPIversion = "X-API-version:1200"

"""synergy server Details"""
Appliance_IP_Synergy = "16.83.10.142"
Server_IP = "172.18.31.2"


"""C7000 setup details"""

ApplianceC7000 = "16.83.10.115"
server_hardwares_c7000 = [{"name": 'Encl1, bay 3', "hostname": "172.18.31.1", "username": "dcs",
                           "password": "dcs", "force": True, "licensingIntent": "OneView", "configurationState": "Managed"}]
C7000_ip = "172.18.31.1"
ov_device_dict = {}
device_ov_list = []
device_ilo_list = []
device_dict = {}
Final_results_OV = {}
Final_results_ILO = {}
LIG1_NAME = "LIG"
EG1_NAME = "EEST_EnclosureGroup"
ENC1_OA1 = "172.18.1.11"
enclosures = [{'hostname': ENC1_OA1, 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri':
               'EG:' + EG1_NAME, 'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None, }]

ligs = {'name': LIG1_NAME, 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                                                                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}, {'enclosure': 1, 'enclosureIndex': 1,
                                                                                                                                                                                                                           'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}, {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                                                                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'}, {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'}], 'uplinkSets': []}

enc_groups = [{'name': EG1_NAME, 'configurationScript': None, 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 4,
                                                                                                                                                                                                                                                                                                                            'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 6,
                                                                                                                                                                                                                                                                                                                                                                                                                                                            'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 7, 'logicalInterconnectGroupUri': None}, {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}, ]
