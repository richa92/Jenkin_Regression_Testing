"""
This file is used to define different DTO variables used under CDT feature tests
"""

from robot.libraries.BuiltIn import BuiltIn
try:
    API_VERSION = BuiltIn().get_variable_value("${X-API-VERSION}")
except:    # noqa
    API_VERSION = '1200'

# Common Nuvo Types
NUVO_IP = '16.114.220.181'
NUVO_REIMAGE_FILE = 'hub.docker.hpecorp.net/rist/ovreimage:latest'
restore_timeout = '150m'
restore_poll_interval = '5m'
NUVO_SSH_USERNAME = 'root'
NUVO_SSH_PASSWORD = 'hpvse123'
NUVO_PROMPT = 'root'
NUVO_TIMEOUT = 35

# Common Resource Types
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
SERVER_PROFILE_TYPE_200 = 'ServerProfileV5'
SERVER_PROFILE_TYPE_300 = 'ServerProfileV6'
SERVER_PROFILE_TYPE_500 = 'ServerProfileV7'
SERVER_PROFILE_TEMPLATE_TYPE_300 = 'ServerProfileTemplateV2'
SERVER_PROFILE_TEMPLATE_TYPE_500 = 'ServerProfileTemplateV3'
ENCLOSURE_GROUP_TYPE_300 = 'EnclosureGroupV300'
ENCLOSURE_TYPE_400 = 'EnclosureV400'
SERVER_HARDWARE_10 = 'server-hardware-10'

# Frame Types
FRAME_TYPE = 'SY12000'

# Added for effuse tests
POTASH_LI = 'LE1-PotashLIG'
CARBON_LI = 'LE1-CarbonLIG1-1'
NATASHA_LIs = ['LE1-SASLIG1-1']
CL20 = 'Synergy 20Gb Interconnect Link Module'
CL10 = 'Synergy 10Gb Interconnect Link Module'

# ICM Types
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NATASHA = 'Synergy 12Gb SAS Connection Module'
CHLORIDE20 = 'Synergy 20Gb Interconnect Link Module'
CARBON = 'Virtual Connect SE 16Gb FC Module for Synergy'
GRAPHITE16 = 'Brocade 16Gb/24 FC Switch Module for Synergy'

# Server HW Types
BIGBIRD = 'SY D3940'
FIREBIRD4S = 'SY 680 Gen9'
REDBIRD = 'SY 660 Gen9'
BLACKBIRD = 'SY 480 Gen9'
CONDORVP2 = 'SY 660 Gen10'
HARRIERVP2 = 'SY 480 Gen10'

# Mezz Types
BRONCO = 'HP Synergy 3820C 10/20Gb CNA'
QUARTZ = 'HP Synergy 3830C 16G FC HBA'
ELECTRON = 'HP Synergy 3530C 16G HBA'
FISHMAN = 'Smart Array P542D Controller'

# StoreVirtual
STOREVIRTUAL_NAME = 'cdt-cluster'
STOREVIRTUAL_HOSTNAME = '16.114.217.140'

if API_VERSION == '1000':
    # Resource types for X-API-Version=1000
    APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
    ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
    FCOE_NETWORK_TYPE = 'fcoe-networkV4'
    FC_NETWORK_TYPE = 'fc-networkV4'
    NETWORK_SET_TYPE = 'network-setV4'
    STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
    SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
    SERVER_PROFILE_TYPE = 'ServerProfileV10'
    SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-group'
else:
    # Resource types for X-API-Version=1200
    APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
    ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
    FCOE_NETWORK_TYPE = 'fcoe-networkV4'
    FC_NETWORK_TYPE = 'fc-networkV4'
    NETWORK_SET_TYPE = 'network-setV5'
    STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
    SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV7'
    SERVER_PROFILE_TYPE = 'ServerProfileV11'
    SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
