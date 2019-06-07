"""
This file is used to define different DTO variables used under API feature tests
"""

from robot.libraries.BuiltIn import BuiltIn

try:
    API_VERSION = BuiltIn().get_variable_value("${X-API-VERSION}")
except:  # noqa
    API_VERSION = '1200'

if API_VERSION == '1000':
    # Resource types for X-API-Version=1000
    APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
    ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
    FCOE_NETWORK_TYPE = 'fcoe-networkV4'
    FC_NETWORK_TYPE = 'fc-networkV4'
    NETWORK_SET_TYPE = 'network-setV4'
    LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV6'
    SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-group'
    ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
    INTERCONNECT_TYPE = 'InterconnectV4'
    ENCLOSURE_TYPE = 'EnclosureV7'
    STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
    SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
    SERVER_PROFILE_TYPE = 'ServerProfileV10'
    SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
    STORAGE_VOLUME_TYPE = 'StorageVolumeV7'
    ALERT_RESOURCE_TYPE = 'AlertResourceV3'
    SAS_LOGICAL_JBOD_TYPE = 'sas-logical-jbodV4'
    SAS_LOGICAL_JBOD_ATTACHMENT_TYPE = 'sas-logical-jbod-attachment'
    LOGIN_DOMAIN_GROUP_CRED_TYPE = 'LoginDomainGroupCredentials'
    LOGIN_DOMAIN_GROUP_PERMISSION_TYPE = 'LoginDomainGroupPermission'
    ROLE_NAME_TYPE = 'RoleNameDtoV2'
    SERVER_HARDWARE_TYPE = 'server-hardware-8'
    STORAGE_POOL_TYPE = 'StoragePoolV4'
    STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
    SCOPE_TYPE = 'ScopeV3'
    DOMAIN_TYPE = 'LoginDomainConfigV600'
    SUB_RESOURCES_TYPE = 'SubResourceV1'
    LOGICAL_ENCLOSURE_TYPE = 'LogicalEnclosureV4'
    UPLINK_SET_TYPE = 'uplink-setV5'
    CRL_DUPLICATE_ERROR_STATUS_CODE = 400
    TASK_URI = "['uri']"  # OVF2422_OVS18190
    APPLIANCE_CSR_TYPE = 'CertificateSigningRequest'
    INTERCONNECT_PORT_TYPE = 'portV5'
    BULK_ETHERNET_NETWORK_TYPE = 'bulk-ethernet-networkV1'
    ETHERNET_INTERCONNECT_SETTINGS_TYPE = 'EthernetInterconnectSettingsV4'
else:
    # Resource types for X-API-Version=1200
    APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
    ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
    FCOE_NETWORK_TYPE = 'fcoe-networkV4'
    FC_NETWORK_TYPE = 'fc-networkV4'
    NETWORK_SET_TYPE = 'network-setV5'
    LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV7'
    SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
    ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV8'
    INTERCONNECT_TYPE = 'InterconnectV6'
    ENCLOSURE_TYPE = 'EnclosureV8'
    STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
    SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV7'
    SERVER_PROFILE_TYPE = 'ServerProfileV11'
    SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
    STORAGE_VOLUME_TYPE = 'StorageVolumeV8'
    ALERT_RESOURCE_TYPE = 'AlertResourceV3'
    SAS_LOGICAL_JBOD_TYPE = 'sas-logical-jbodV4'
    SAS_LOGICAL_JBOD_ATTACHMENT_TYPE = 'sas-logical-jbod-attachment'
    LOGIN_DOMAIN_GROUP_CRED_TYPE = 'LoginDomainGroupCredentials'
    LOGIN_DOMAIN_GROUP_PERMISSION_TYPE = 'LoginDomainGroupPermission'
    ROLE_NAME_TYPE = 'RoleNameDtoV2'
    SERVER_HARDWARE_TYPE = 'ServerHardwareTypeV10'
    STORAGE_POOL_TYPE = 'StoragePoolV4'
    STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageVolumeTemplateV6'
    SCOPE_TYPE = 'ScopeV3'
    DOMAIN_TYPE = 'LoginDomainConfigV600'
    SUB_RESOURCES_TYPE = 'SubResourceV1'
    LOGICAL_ENCLOSURE_TYPE = 'LogicalEnclosureV5'
    UPLINK_SET_TYPE = 'uplink-setV6'
    CRL_DUPLICATE_ERROR_STATUS_CODE = 409
    TASK_URI = "['headers']['Location']"  # OVF2422_OVS18190
    APPLIANCE_CSR_TYPE = 'CertificateSigningRequestV2'
    INTERCONNECT_PORT_TYPE = 'portV6'
    BULK_ETHERNET_NETWORK_TYPE = 'bulk-ethernet-networkV2'
    ETHERNET_INTERCONNECT_SETTINGS_TYPE = 'EthernetInterconnectSettingsV6'

# Common Resource Types
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
SERVER_PROFILE_TYPE_200 = 'ServerProfileV5'
SERVER_PROFILE_TYPE_300 = 'ServerProfileV6'
SERVER_PROFILE_TYPE_500 = 'ServerProfileV7'
SERVER_PROFILE_TEMPLATE_TYPE_300 = "ServerProfileTemplateV2"
SERVER_PROFILE_TEMPLATE_TYPE_500 = 'ServerProfileTemplateV3'
ENCLOSURE_GROUP_TYPE_300 = 'EnclosureGroupV300'
ENCLOSURE_TYPE_400 = 'EnclosureV400'
SERVER_HARDWARE_10 = 'server-hardware-10'

# Frame Types
FRAME_TYPE = 'SY12000'
FRAME_TYPE2 = 'C7000'

# ICM Types
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NATASHA = 'Synergy 12Gb SAS Connection Module'
CHLORIDE20 = 'Synergy 20Gb Interconnect Link Module'
CARBON16 = 'Virtual Connect SE 16Gb FC Module for Synergy'
GRAPHITE16 = 'Brocade 16Gb/24 FC Switch Module for Synergy'
# C7000
SHEPPARD = 'HP VC FlexFabric 10Gb/24-Port Module'
OCHO = 'HP VC 8Gb 20-Port FC Module'
SUPERSHAW = "HP VC FlexFabric-20/40 F8 Module"
UTAH = 'HP VC 8Gb 24-Port FC Module'

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
