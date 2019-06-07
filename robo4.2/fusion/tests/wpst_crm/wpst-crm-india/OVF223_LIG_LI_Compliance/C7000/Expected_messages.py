AND = "and"
MORE = "more"
NULL = "null"
ENABLED = "enabled"
DISABLED = "disabled"
NO_NETWORKS = "No networks"
PASSTHROUGH = '"Passthrough"'
CUSTOM_WITH_FCOE = '"Custom(with FCoE lossless)"'
CUSTOM_WITHOUT_FCOE = '"Custom(without FCoE lossless)"'
ACTIVE_QOS_CONFIGURATION = "active qos configuration"
INACTIVE_WITH_FCOE_QOS_CONFIGURATION = "inactive custom with FCOE qos configuration"
INACTIVE_WITHOUT_FCOE_QOS_CONFIGURATION = "inactive custom without FCOE qos configuration"
TRAFFIC_CLASS_ADDED = "Queue XXX will be added in YYY."
TRAFFIC_CLASS_REMOVED = "Queue XXX will be removed from YYY."
QOS_CONFIG_TYPE_MODIFIED = "Configuration type will be changed from XXX to YYY in ZZZ."
UPLINK_CLASSIFICATION_MODIFIED = "Classification type for uplink ports will be updated from XXX to YYY in ZZZ."
DOWNLINK_CLASSIFICATION_MODIFIED = "Classification type for downlink ports will be updated from XXX to YYY in ZZZ."
TRAFFIC_CLASS_ENABLED_DISABLED = "Queue XXX will be YYY in ZZZ."
TRAFFIC_CLASS_REAL_TIME = "Queue ZZZ will become real time in AAA."
TRAFFIC_CLASS_NOT_REAL_TIME = "Queue ZZZ will be removed from real time in AAA."
TRAFFIC_CLASS_SHARE_MODIFIED = "Bandwidth will be updated from XXX% to YYY% for queue ZZZ in AAA."
TRAFFIC_CLASS_MAXSHARE_MODIFIED = "Maximum share will be updated from XXX% to YYY% for queue ZZZ in AAA."
TRAFFIC_CLASS_EGRESSDOT1P_MODIFIED = "Egress dot1p priority will be updated from XXX to YYY for queue ZZZ in AAA."
INGRESS_DOT1P_MAPPING_MODIFIED = "Ingress dot1p values XXX will be classified for queue YYY in ZZZ."
INGRESS_DSCP_MAPPING_MODIFIED = "Ingress dscp XXX will be classified for queue YYY in ZZZ."
QOS_GENERAL_COMPLIANCE_MESSAGE = "QoS settings do not match the template."
INTERNAL_NETWORK_GENERAL_COMPLIANCE_MESSAGE = "Internal network settings do not match the template."
TELEMETRY_GENERAL_COMPLIANCE_MESSAGE = " Utilization sampling settings do not match the template."
ETHERNET_GENERAL_COMPLIANCE_MESSAGE = "Interconnect settings do not match the template."
UPLINK_GENERAL_COMPLIANCE_MESSAGE = "Uplinkset settings do not match the template."
SWITCHMAP_GENERAL_COMPLIANCE_MESSAGE = " Switch map settings do not match the template."
SFLOW_GENERAL_COMPLIANCE_MESSAGE = "sFlow settings do not match the template."
SNMP_GENERAL_COMPLIANCE_MESSAGE = "SNMP settings do not match the template."
PORT_MONITORING_GENERAL_COMPLIANCE_MESSAGE = "Port Monitoring settings do not match the template."
PORT_MONITORING_NON_COMPLIANT_DESCRPTION = "Port Monitoring is enabled on LI making it non compliant with LIG."
INTENRAL_NETWORK_TO_BE_ADDED_COUNT = "XXX network(s) will be added."
INTENRAL_NETWORK_TO_BE_REMOVED_COUNT = "XXX network(s) will be removed."


TELEMETRY_SAMPLE_INTERVAL_COLLECTION_COMPLIANCE_MESSAGE = "Interval between samples will be changed from XXX to YYY seconds."
TELEMETRY_SAMPLE_COUNT_COMPLIANCE_MESSAGE = "Total number of samples will be changed from XXX to YYY."
TELEMETRY_SAMPLE_COLLECTION_ENABLED_COMPLIANCE_MESSAGE = "Sample Collection will be enabled with XXX samples at an interval for every YYY seconds."
TELEMETRY_SAMPLE_COLLECTION_DISABLED_COMPLIANCE_MESSAGE = "Sample Collection will be disabled."
TELEMETRY_SAMPLE_COLLECTION_ADD_COMPLIANCE_MESSAGE = "Utilization Sampling will be added."

# logical uplink
LOGICAL_UPLINK_ADDED = "Uplink set(s) XXX will be added."
LOGICAL_UPLINK_REMOVED = "Uplink set(s) XXX will be removed."
LOGICAL_UPLINK_LACP_TIMER_MODIFIED = "For uplink set XXX, lacp time will be updated from YYY to ZZZ."
LOGICAL_UPLINK_FC_MODE_MODIFIED = "For uplink set XXX, fc mode will be updated from YYY to ZZZ"
UPLINK_PORT_ADDED = "Uplink port(s) XXX will be added to uplink set YYY."
UPLINK_PORT_REMOVED = "Uplink port(s) XXX will be removed from uplink set YYY."
UPLINK_PORT_SPEED_MODIFIED = "For uplink port XXX, desired speed will be updated from YYY to ZZZ."
NETWORK_ADDED = "Network(s) XXX will be added to uplink set YYY."
NETWORK_REMOVED = "Network(s) XXX will be removed from uplink set YYY."
NATIVE_NETWORK = "For uplink set XXX, network YYY will be updated as native network."
NON_NATIVE_NETWORK = "For uplink set XXX, network YYY will be updated as non-native network."

# interconnect setting
IPV4_ONLY = '"IPv4 only"'
IPV6_ONLY = '"IPv6 only"'
IPV4_AND_IPV6 = "IPv4 and IPv6"
IGMP_SNOOPING_DISABLED = "IGMP Snooping will be disabled."
IGMP_SNOOPING_ENABLED_WITH_INTERVAL = "IGMP Snooping will be enabled with timeout interval XXX seconds."
IGMP_SNOOPING_ENABLED_WITH_VLAN_INTERVAL = "IGMP Snooping will be enabled for vlan tagged network(s) XXX with timeout interval YYY seconds."
IGMP_SNOOPING_TIMEOUT_INTRERVAL_MOD = "IGMP Snooping idle timeout interval value will be updated from XXX to YYY seconds."
IGMP_SNOOPING_ENABLED_VLAN_IDS = "IGMP snooping will be enabled for vlan ids XXX."
IGMP_SNOOPING_DISABLED_VLAN_IDS = "IGMP snooping will be disabled for vlan ids XXX."
FAST_MAC_FAILOVER_ENABLED = "Fast MAC cache failover will be enabled with refresh interval XXX seconds."
FAST_MAC_FAILOVER_DISABLED = "Fast MAC cache failover will be disabled."
FAST_MAC_REFRESH_INTERVAL_MOD = "Fast MAC cache failover refresh interval will be updated from XXX to YYY."
STROM_CONTROL_ENABLED = "Strom control will be enabled with threshold value XXX per second and with polling interval YYY seconds."
STROM_CONTROL_DISABLED = "Strom control will be disabled."
STROM_CONTROL_THRESHHOLD_MOD = "Strom control threshold value will be updated from XXX to YYY per seconds."
STROM_CONTROL_TIME_INTREVAL_MOD = "Strom control poling interval will be updated from XXX to YYY seconds."
NETWORK_LOOP_PROTECTION_ENABLED = "Network loop protection will be enabled with Tx interval XXX."
NETWORK_LOOP_PROTECTION_DISABLED = "Network loop protection will be disabled."
PAUSE_FLOOD_PROTECTION_ENABLED = "Pause flood protection will be enabled."
PAUSE_FLOOD_PROTECTION_DISABLED = "Pause flood protection will be disabled."
RICH_TLV_ENABLED = "Rich TLV will be enabled."
RICH_TLV_DISABLED = "Rich TLV will be disabled."
TAGGED_LLDP_ENABLED = "LLDP tagging will be enabled."
TAGGED_LLDP_DISABLED = "LLDP tagging will be disabled."
LLDP_IPADDRESS_MODE_MOD = "LLDP tagging ip address mode will be updated from XXX to YYY."
ETHERNET_SETTING_ADDED = "Interconnect setting will added."
ETHERNET_SETTING_REMOVED = "Interconnect setting will be removed."

# SNMP Messages
SNMP_CONFIGURATION_ADD = "SNMP configuration will be added."
SNMP_V1_V2_ENABLE_WITH_READ_COMMUNITY = "SNMPv1, v2 will be enabled with Read community String XXX"
SNMP_V1_V2_DISABLE = "SNMPv1, v2 will be disabled"
SNMP_V1_V2_ENABLE_WITH_READ_COMMUNITY_CHANGE = "Read community name will be changed from XXX to YYY"
SNMP_SYSTEM_CONTACT = "System contact will be changed from XXX to YYY"
SNMP_SYSTEM_CONTACT_NONE = "System contact will be changed to none"
SNMP_SYSTEM_CONTACT_CHANGED = "System contact will be changed to XXX"
SNMP_V3_ENABLE = "SNMPv3 will be enabled"
SNMP_V3_DISABLE = "SNMPv3 will be disabled"
SNMP_V3_USERS_ADDED = "SNMPv3 user(s) XXX will be added"
SNMP_V3_USERS_REMOVED = "SNMPv3 user(s) XXX will be removed"
SNMP_V3_USERS_AUTH_PROTOCOL_CHANGED = "Authentication protocol will be changed from XXX to YYY for SNMPv3 user ZZZ"
SNMP_V3_USERS_PRIVACY_PROTOCOL_CHANGED = "Privacy protocol will be changed from XXX to YYY for SNMPv3 user ZZZ"
SNMP_V3_USERS_AUTH_PROTOCOL_CRED_CHANGED = "Authentication protocol password will be changed for SNMPv3 user XXX"
SNMP_V3_USERS_PRIVACY_PROTOCOL_CRED_CHANGED = "Privacy protocol password will be changed for SNMPv3 user XXX"
SNMP_ACCESS_LIST_REMOVED = "SNMP Access XXX will be removed"
SNMP_ACCESS_LIST_ADDED = "SNMP Access XXX will be added"
SNMP_TRAP_DESTINATIONS_ADDED = "SNMP Trap destination(s) XXX will be added"
SNMP_TRAP_DESTINATIONS_REMOVED = "SNMP Trap destination(s) XXX will be removed"
SNMP_TRAP_DESTINATION_PORT_CHANGE = "Port will be changed from XXX to YYY for trap destination ZZZ"
SNMP_TRAP_DESTINATION_V3_WITH_INFORM_NOTIFICATION_DEFAULTS = "SNMPv3 Inform will be set as Notification Type for trap destination XXX"
SNMP_TRAP_DESTINATION_V3_WITH_TRAP_NOTIFICATION_DEFAULTS = "SNMPv3 Trap will be set as Notification Type for trap destination XXX"
SNMP_SEVERITIES_ADDED = "The Severities XXX will be added for trap destination YYY"
SNMP_SEVERITIES_REMOVED = "The Severities XXX will be removed for trap destination YYY"
SNMP_VCM_TRAPS_ADDED = "The VCM Trap(s) XXX will be added for trap destination YYY"
SNMP_VCM_TRAPS_REMOVED = "The VCM Trap(s) XXX will be removed for trap destination YYY"
SNMP_VC_ENET_TRAPS_ADDED = "The VC-Enet Trap(s) XXX will be added for trap destination YYY"
SNMP_VC_ENET_TRAPS_REMOVED = "The VC-Enet Trap(s) XXX will be removed for trap destination YYY"
SNMP_VC_FC_TRAPS_ADDED = "The VC-FC Trap(s) XXX will be added for trap destination YYY"
SNMP_VC_FC_TRAPS_REMOVED = "The VC-FC Trap(s) XXX will be removed for trap destination YYY"
SNMP_TRAP_DESTINATION_TRAP_FORMAT_CHANGE = "Trap format will be changed from XXX to YYY for trap destination ZZZ"
SNMP_TRP_DEST_V3_USER_CHANGES_FOR_TRAP_TYPE = "SNMPv3 Trap user name will be changed from XXX to YYY for trap destination ZZZ"
SNMP_TRP_DEST_V3_USER_CHANGES_FOR_INFROM_TYPE = "SNMPv3 Inform user name will be changed from XXX to YYY for trap destination ZZZ"
SNMP_TRP_DEST_V3_CHNGD_ENGN_ID = "SNMPv3 Inform engine id will be changed from XXX to YYY for trap destination ZZZ"
# Switc Map
SWITCH_TYPES_ADDED = "Switch types XXX will be added in bay YYY for enclosure at index ZZZ."
SWITCH_TYPES_REMOVED = "Switch types XXX will be removed in bay YYY for enclosure at index ZZZ."
SWITCH_TYPES_UPDATED = "Switch type will be updated from XXX type to YYY in bay ZZZ for enclosure at index AAA."

# Sflow
INGRESS = "Ingress"
EGRESS = "Egress"
BOTH = "Both"
SFLOW_DHCP = "dhcp"
SFLOW_IP_POOL = "IP Pool"
SFLOW_STATIC = "static"
SFLOW_CONFIGURATION_ENABLED = "sFlow configuration will be enabled."
SFLOW_CONFIGURATION_DISABLED = "sFlow configuration will be disabled."
SFLOW_CONFIG_NETWORK_MOD = "Network XXX will be used for sFlow configuration."
SFLOW_COLLECTOR_REMOVED = "For sFlow configuration,  collector(s) XXX will be removed."
SFLOW_COLLECTOR_ADDED = "For sFlow configuration, collector(s) XXX will be added."
SFLOW_COLLECTOR_NAME_MOD = "sFlow collector name will be updated from YYY to ZZZ."
SFLOW_COLLECTOR_IP_MOD = "For sFlow collector XXX, IP address will be updated from YYY to ZZZ."
SFLOW_COLLECTOR_PORT_MOD = "For sFlow collector XXX, port number will be updated from YYY to ZZZ."
SFLOW_COLLECTOR_DATAGRAM_MOD = "For sFlow collector XXX, max datagram size will be updated from YYY to ZZZ."
SFLOW_COLLECTOR_HEADER_MOD = "For sFlow collector XXX, max header size will be updated from YYY to ZZZ."
SFLOW_COLLECTOR_COLLECTION_ENABLED = "For sFlow collector XXX, collection will be enabled."
SFLOW_COLLECTOR_COLLECTION_DISABLED = "For sFlow collector XXX, collection will be disabled."
SFLOW_PORT_COLLECTOR_MOD = "For port XXX, collector YYY will be added."
SFLOW_PORT_SAMPLING_DIRECTION_MOD = "Sampling direction will be updated from XXX to YYY for port ZZZ."
SFLOW_PORT_SAMPLING_RATE_MOD = "Sampling rate will be updated with sample one out of every XXX packets for port YYY."
SFLOW_PORT_POLLING_INTERVAL_MOD = "Polling interval will be updated from XXX to YYY seconds for port ZZZ."
SFLOW_CONFIGURATION_PORT_ADDED = "For sFlow configuration, port(s) XXX will be added."
SFLOW_CONFIGURATION_PORT_REMOVED = "For sFlow configuration, port(s) XXX will be removed."
SFLOW_AGENT_CONFIG_IP_MODE = "sFlow agent IP address configuration mode will be updated from XXX to YYY."
SFLOW_CONFIGURATION_ADDED = "sFlow configuration will be added."
SFLOW_CONFIGURATION_REMOVED = "sFlow configuration will be removed."

MORE_DETAILS_ON_COMPLIANCE = "For more detail refer to details section below."
