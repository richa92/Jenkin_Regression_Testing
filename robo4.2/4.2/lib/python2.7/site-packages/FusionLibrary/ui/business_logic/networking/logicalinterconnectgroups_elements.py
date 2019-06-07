class _BaseGeneralLogicalInterconnectGroupsElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Logical Interconnect Groups']"

    # Action button
    ID_BUTTON_ACTIONS = "xpath=//label[text()='Actions']"
    ID_SAS_BUTTON_ACTIONS = "xpath=.//*[@id='cic-switchtemplate-actions-dfrm']/label[text()='Actions']"

    # for verify
    ID_TABLE_LIG = "xpath=//table/tbody/tr/td[text()='%s']"
    ID_TABLE_LIGS = "xpath=//table[@id='cic-switchtemplate-master-table']/tbody/tr/td[@class != 'dataTables_empty']"
    ID_TABLE_LIG_SELECTED = "xpath=//table/tbody/tr[contains(@class, hp-selected)]/td[text()='%s']"
    ID_PANEL_NOTIFICATION = "id=hp-page-notifications"

    ID_STATUS_NOTIFICATION_OK = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "xpath=//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-switchtemplate-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"
    ID_TEXT_ACTIVITY_ACTION_OK = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]/../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_ACTION_WARN = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]/../div[@class='hp-status hp-status-warning']"
    ID_TEXT_ACTIVITY_ACTION_ERROR = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]/../div[@class='hp-status hp-status-error']"
    ID_TEXT_ACTIVITY_MESSAGE = "xpath=//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"

    # option panel
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-switchtemplate-panel-selector"
    ID_SELECT_LOGICAL_INTERCONNECT_GROUP_PANEL = "xpath=//ol[@class='hp-options']//a[.='Logical Interconnect Group']"
    ID_SELECT_GENERAL_PANEL = "xpath=//ol[@class='hp-options']//a[.='General']"
    ID_SELECT_INTERNAL_NETWORKS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Internal Networks']"
    ID_SELECT_UPLINK_SETS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Uplink Sets']"
    ID_SELECT_INTERCONNECT_SETTINGS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Interconnect settings']"
    ID_SELECT_UTILIZATION_SAMPLING_PANEL = "xpath=//ol[@class='hp-options']//a[.='Utilization Sampling']"
    ID_SELECT_SNMP_PANEL = "xpath=//ol[@class='hp-options']//a[.='SNMP']"
    ID_SELECT_QUALITY_OF_SERVICE_PANEL = "xpath=//ol[@class='hp-options']//a[.='Quality of Service']"
    ID_SELECT_ACTIVITY_PANEL = "xpath=//ol[@class='hp-options']//a[.='Activity']"
    ID_SELECT_MAP_PANEL = "xpath=//ol[@class='hp-options']//a[.='Map']"
    ID_SELECT_LABELS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Labels']"

    ID_LINK_USED_BY_EG = "xpath=//div[@id='cic-switchtemplate-show-used-by']/div[@class='cic-used-by-category-enclosure-groups']/span/a"
    ID_LINK_USED_BY_LI = "xpath=//div[@id='cic-switchtemplate-show-used-by']/div[@class='cic-used-by-category-logical-interconnects']/span/a"
    ID_TEXT_USED_BY = "xpath=.//*[@id='cic-switchtemplate-show-used-by']"

    # General
    ID_TEXT_GENERAL_TYPE = "id=cic-switchtemplate-show-enclosure-type"
    ID_TEXT_GENERAL_USED_BY_EG = "xpath=//div[@id='cic-switchtemplate-show-used-by-enclosure-template']//a|//div[@id='cic-switchtemplate-show-used-by-enclosure-template']//span"
    ID_TEXT_GENERAL_USED_BY_LI = "xpath=//div[@id='cic-switchtemplate-show-used-by-logical-switches']//a|//div[@id='cic-switchtemplate-show-used-by-logical-switches']//span"

    # Internal Networks
    ID_TEXT_INTERNAL_NETWORKS_COUNT = "id=cic-switchtemplates-internal-networks-count"
    ID_TEXT_INTERNAL_NETWORKS_ITEM_NAME = "xpath=//div[@id='cic-switchtemplates-internal-networks-container']/table//td[a[.='%s']]"
    ID_TEXT_INTERNAL_NETWORKS_VLAN = "xpath=//div[@id='cic-switchtemplates-internal-networks-container']/table//td[a[.='%s']]/../td[2]"  # ID or Type

    # Uplink Sets
    ID_TEXT_UPLINK_SETS_ITEM = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']"
    ID_BTN_FOLDING_UPLINK_SET = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/.."
    ID_UPLINK_SET_PANEL = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../following-sibling::div"

    # - FC
    ID_TEXT_UPLINK_SETS_FC_NETWORK_NAME = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../../div//div[@class='cic-uplink-set-panel-fc-network-section']//span/a"
    ID_TEXT_UPLINK_SETS_FC_NETWORK_TYPE = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../../div//div[@class='cic-uplink-set-panel-fc-network-section']//span[contains(@class, 'cic-uplink-set-panel-fc-fabric-type')]"
    ID_TEXT_UPLINK_SETS_FC_NETWORK_SPEED = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../../div//div[@class='cic-uplink-set-panel-fc-speed']"
    ID_TEXT_UPLINK_SETS_FC_PORT = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div/table[contains(@class, 'cic-uplink-set-panel-fc-uplinks-table')]//td[.='%s']"

    # - Ethernet
    ID_TEXT_UPLINK_SETS_ETHERNET_CONNECTION_MODE = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../../div//div[@class='cic-uplink-set-panel-connection-mode']"
    ID_TEXT_UPLINK_SETS_ETHERNET_LACP_TIMER = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../../div//div[@class='cic-uplink-set-panel-lacp-timer']"
    ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_NAME = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div[contains(@class, 'cic-uplink-set-panel-ethernet-networks-table')]/table//td[.='%s']"
    ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_VLAN_ID = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div[contains(@class, 'cic-uplink-set-panel-ethernet-networks-table')]/table//td[.='%s']/../td[2]"
    ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_TYPE = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div[contains(@class, 'cic-uplink-set-panel-ethernet-networks-table')]/table//td[.='%s']/../td[3]"
    # ID_TEXT_UPLINK_SETS_ETHERNET_NO_NETWORK = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div[@class='cic-uplink-set-panel-ethernet-networks-other-section']/div[.='No networks']"
    ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_PORT = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//table[contains(@class, 'cic-uplink-set-panel-ethernet-uplinks-table')]//td[.='%s']"
    # ID_TEXT_UPLINK_SETS_ETHERNET_NO_PORT = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div[contains(@class, 'cic-uplink-set-panel-ethernet-uplinks-none')]/div[.='No uplinks']"

    ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_SPEED = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div//td[.='%s']/following-sibling::td[count(//table/thead/tr/th[.='Speed']/preceding-sibling::td)+1]"
    ID_TEXT_UPLINK_SETS_ETHERNET_NETWORK_AUTO_NEGOTIATION = "xpath=//span[@class='cic-uplink-set-panel-name' and .='%s']/../..//div//td[.='%s']/following-sibling::td[count(//table/thead/tr/th[.='Auto-negotiation']/preceding-sibling::td)+2]"

    # Interconnect settings
    ID_PANEL_INTERCONNECT_SETTINGS = "id=cic-switchtemplate-show-ethernet-switch-settings"  # changed xpath
    ID_TEXT_INTERCONNECT_SETTINGS_FAST_MAC_CACHE_FAILOVER = "id=cic-switchtemplate-ethernet-show-failover"
    ID_TEXT_INTERCONNECT_SETTINGS_MAC_REFRESH_INTERVAL = "id=cic-switchtemplate-ethernet-show-mac-interval"
    ID_TEXT_INTERCONNECT_SETTINGS_IGMP_SNOOPING = "id=cic-switchtemplate-ethernet-show-snooping"
    ID_TEXT_INTERCONNECT_SETTINGS_IGMP_IDLE_TIMEOUT_INTERVAL = "id=cic-switchtemplate-ethernet-show-igmp-interval"
    ID_TEXT_INTERCONNECT_SETTINGS_LOOP_PROTECTION = "id=cic-switchtemplate-ethernet-show-loop"
    ID_TEXT_INTERCONNECT_SETTINGS_PAUSE_FLOOD_PROTECTION = "id=cic-switchtemplate-ethernet-show-pause-flood"
    ID_TEXT_INTERCONNECT_SETTINGS_REDUNDANCY = "id=cic-switchtemplate-general-redundancy-info-choice"

    # Utilization Sampling
    ID_TEXT_UTILIZATION_SAMPLING_INTERVAL_BETWEEN_SAMPLES = "id=cic-switchtemplate-show-interval"
    ID_TEXT_UTILIZATION_SAMPLING_TOTAL_NUMBER_OF_SAMPLES = "id=cic-switchtemplate-show-samples"
    ID_TEXT_UTILIZATION_SAMPLING_SAMPLE_COLLECTION_RATE = "id=cic-switchtemplate-show-collection-rate"
    ID_TEXT_UTILIZATION_SAMPLING_TOTAL_SAMPLING_HISTORY = "id=cic-switchtemplate-show-sampling-history"

    # SNMP
    ID_TEXT_SNMP_ENABLED = "id=cic-snmp-show-snmp"
    ID_TEXT_SNMPV3_ENABLED = ".//*[@id='cic-snmp-show-snmpv3']"
    ID_TEXT_SNMPV1V2_ENABLED = ".//*[@id='cic-snmp-show-snmpv1v2']"
    ID_TEXT_SNMP_SYSTEM_CONTACT = "id=cic-snmp-show-system-contact"
    ID_TEXT_SNMP_READ_COMMUNITY = "id=cic-snmp-show-read-community"
    ID_DIALOG_ADD_SNMP_USER = "xpath=.//*[@id='cic-snmp-user-add-dialog']/header"
    ID_TEXT_ADD_SNMP_USER_INVALID_AUTH_PASSWORD_ERROR = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item auth-protocol-fields']/div/label"
    ID_TEXT_ADD_SNMP_USER_INVALID_PRIV_PASSWORD_ERROR = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item privacy-protocol-fields']/div/label"
    ID_TEXT_ADD_SNMP_USER_OR_TRAP_ERROR = "xpath=.//*[@id='hp-form-message']/..//div/div[@class='hp-details']"
    ID_TEXT_ADD_SNMP_INVALID_USER_USERNAME_ERROR = "xpath=.//*[@id='cic-snmp-snmpv3-user-username-li']/div/label"
    ID_TEXT_ADD_SNMP_DUPLICATE_USER_USERNAME_ERROR = "xpath=.//*[@id='hp-form-message']/..//div[@class='hp-details']/p/span"
    ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY = "xpath=.//*[@id='cic-snmp-snmpv3-user-security-level-authpriv']"
    ID_DIALOG_REMOVE_SNMP_USER = "xpath=.//*[@id='hp-body-div']/div[@class='hp-dialog-overlay hp-active']/div/div/div/header"
    ID_TEXT_SNMP_USER = "xpath=//table[@id='cic-snmp-user-table']//td[.='%s']"
    ID_TEXT_SNMPV3_USERS_PRIVACY_PROTOCOL = "xpath=//table[@id='cic-snmp-user-table']//td[.='%s']/../td[last()]"
    ID_TEXT_SNMPV3_USERS_AUTHENTICATION_PROTOCOL = "xpath=//table[@id='cic-snmp-user-table']//td[.='%s']/../td[last()-1]"
    ID_TEXT_SNMPV3_USERS_SECURITY_LEVEL = "xpath=//table[@id='cic-snmp-user-table']//td[.='%s']/../td[last()-2]"
    ID_DIALOG_EDIT_SNMP_USER = "xpath=.//*[@id='cic-snmp-user-dialog-title']"
    ID_LABEL_SNMPV3_ENABLED = "xpath=.//*[@id='cic-snmp-general-snmp-v3-label']"
    # - Trap Destinations TODO: no plan to support checking 'Severity','VCM','VCM-Enet','VC-FC' options
    ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_DESTINATION = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']"
    ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_COMMUNITY_STRING = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']/../td[2]"
    ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_FORMAT = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']/../td[3]"
    ID_TEXT_ADD_TRAP_ERROR_INVALID_PORT = "xpath=.//*[@id='cic-snmp-trap-destination-port-li']/div/label"
    ID_TEXT_ADD_TRAP_ERROR_INVALID_ENGINEID = "xpath=.//*[@id='cic-snmp-trap-destination-engine-id-li']/div/label"
    ID_TEXT_ADD_TRAP_NO_USER_ERROR_MSG = "xpath=.//*[@id='cic-snmp-trap-destination-snmp-user-div']/label"
    ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV2 = "id=cic-snmp-trap-destination-snmpv2"
    ID_TEXT_SNMP_USER_REMOVE_ERROR = "xpath=.//*[@id='cic-snmp-snmpv3-user-delete-error-dialog-msg']"
    ID_TEXT_SNMP_USER_ASSOCITED_TRAPS = "xpath=.//*[@id='cic-snmp-snmpv3-user-delete-error-details-table']/tbody/tr/td[contains (text(),'%s')]"
    ID_DIALOG_REMOVE_SNMPV3_TRAP_DESTINATION = "xpath=.//*[@id='cic-snmp-remove-trap-dialog-title-destination']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ROW_COMMUNITY_STRING = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-community-string']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ROW_FORMAT = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']/../td[.='%s']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_SEVERITY = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-severity']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_PORT = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']/../td[.='%s']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_USERNAME = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-user-name']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ENGINEID = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-engine-id']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_NOTIFICATION_TYPE = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-notification-type']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_VCM_TRAPS = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-vcm']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_ENET_TRAPS = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-vc-enet']"
    ID_TEXT_SNMPV3_TRAP_DESTINATIONS_FC_TRAPS = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/..//div/label[@class='cic-snmp-trap-destination-more-vc-fc']"
    ID_DROPDOWN_SNMPV3_TRAP_DESTINATION_VALUES = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/tr[contains(.,'%s')]/td[div[@class='hp-collapser']]"
    ID_COLLAPSE_SNMPV3_TRAP_DESTINATION_VALUES = "xpath=.//*[@id='cic-snmp-trap-forwarding-table']/tbody/tr[contains(.,'%s')]/td[div[@class='hp-collapser hp-active']]"

    # - SNMP Access
    ID_TEXT_SNMP_SNMP_ACCESS_ROW_IP_OR_SUBNET = "xpath=//table[@id='cic-snmp-access-table']//td[.='%s']"

    # Quality of Service
    ID_TEXT_QUALITY_OF_SERVICE_QOS_CONFIGURATION_TYPE = "id=cic-switchtemplate-show-qos"

    ID_DIALOG_LIG_ADD = "id=cic-switchtemplate-add-form"
    ID_OPTION_UPLINK = "xpath=.//*[@id='cic-interconnect-group-qos-edit-container']//*[contains(text(),'Classification for uplinks')]"
    ID_OPTION_DOWNLINK = "xpath =.//*[@id='cic-interconnect-group-qos-edit-container']//*[contains(text(),'Classification for downlinks')]"
    ID_OPTION_RESET = "xpath = .//*[@id='cic-qos-traffic-class-reset-button']"


class GeneralLogicalInterconnectGroupsElements(_BaseGeneralLogicalInterconnectGroupsElements):
    pass


class C7000GeneralLogicalInterconnectGroupsElements(_BaseGeneralLogicalInterconnectGroupsElements):
    pass


class TBirdGeneralLogicalInterconnectGroupsElements(_BaseGeneralLogicalInterconnectGroupsElements):
    ID_TEXT_WARNING_MESSAGE = "id=hp-form-message"


class _BaseCreateLogicalInterconnectGroupsElements(object):
    ID_CHECKBOX_FAILOVER_PREFERRED_PORT = "xpath=//tr[descendant::td[contains(.,'%s')] and td[contains(.,'%s')]]//input[@type='checkbox']"
    ID_BUTTON_CREATE_LIG = "link=Create logical interconnect group"
    ID_SELECT_ACTION_CREATE = "id=cic-switchtemplate-create-action"

    # dialog
    ID_DIALOG_CREATE_LIG = "id=cic-switchtemplate-add-form"
    # panel selector
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-switchtemplate-panel-add-selector"
    ID_DROPDOWN_PANEL_LAYER = "xpath=//div[@id='cic-switchtemplate-panel-add-selector']//ol[@class='hp-options']"
    ID_SELECT_GENERAL = "xpath=//a[.='General']"
    ID_SELECT_LOGICAL_INTERCONNECT_GROUP = "xpath=//a[.='Logical Interconnect Group']"
    ID_SELECT_INTERCONNECT_SETTINGS = "xpath=//a[.='Interconnect Settings']"
    ID_SELECT_SNMP = "xpath=//a[.='SNMP']"
    ID_SELECT_QUALITY_OF_SERVICE = "xpath=//a[.='Quality of Service']"

    # dialog element
    ID_INPUT_NAME = "id=cic-switchtemplate-add-name"

    ID_BUTTON_ADD_UPLINK_SET = "id=cic-add-uplink-li"
    ID_BUTTON_SELECT_INTERCONNECTS = "xpath=//*[@id='cic-switchtemplate-add-select-c7000-interconnects-button']"

    # - { internal network
    ID_BUTTON_EDIT_INTERNAL_NETWORKS = "xpath=//div[contains(@class, 'cic-internal-networks-edit-button')]"
    ID_DIALOG_EDIT_INTERNAL_NETWORKS = "xpath=//h1[.='Edit Internal Networks']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "id=cic-internal-nets-dialog-networks-addNetworks"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_REMOVE_ALL = "xpath=//*[@id='cic-internal-nets-dialog-networks-removeAll']"
    ID_DIALOG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "xpath=//h1/span[text()='Add Networks']"
    ID_INPUT_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_SEARCH_NETWORK = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "xpath=//table//tr[td[.='%s']]"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_CANCEL = "xpath=//form[@id='cic-internal-nets-dialog-form']//button[.='Cancel']"
    ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS = "xpath=//table[@id='cic-internal-nets-dialog-network-assigned']//td[.='%s']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_OK = "id=cic-internal-nets-dialog-add-ok"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_CANCEL = "id=cic-internal-nets-dialog-add-cancel"
    # - }

    # - { add uplink set
    ID_DIALOG_CREATE_UPLINK_SET = "id=cic-switchtemplate-dialog-add"  # dialog
    ID_INPUT_CREATE_UPLINK_SET_NAME = "id=cic-switchtemplate-dialog-name"
    ID_SELECT_CREATE_UPLINK_SET_TYPE = "id=cic-switchtemplate-dialog-type"
    ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_AUTOMATIC = "id=cic-switchtemplate-dialog-auto-conntype"  # for ethernet
    ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_FAILOVER = "id=cic-switchtemplate-dialog-fail-conntype"  # for ethernet
    ID_SELECT_CREATE_UPLINK_SET_LACP_TIMER = "id=cic-switchtemplate-dialog-lacp-timer-select"  # for ethernet
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS = "id=cic-switchtemplate-dialog-networks-addNetworks"  # for ethernet
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_NETWORKS = "id=cic-switchtemplate-dialog-networks-removeAll"  # for ethernet
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_PORTS = "id=cic-switchtemplate-dialog-ports-removeAll"  # for ethernet, tunnel, untagged
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS = "id=cic-switchtemplate-dialog-uplinks-addUplinks"  # port of ethernet, tunnel, untagged
    ID_COMBO_CREATE_UPLINK_SET_IMAGE_STREAMER_NETWORK = "id=cic-switchtemplate-dialog-image-streamer-addNetwork-input"  # image streamer network
    ID_COMBO_CREATE_UPLINK_SET_IMAGE_STREAMER_PORTS = "id=cic-switchtemplate-dialog-img-streamer-port-select-%s-input"  # image streamer ports
    ID_COMBO_CREATE_UPLINK_SET_FC_NETWORK = "id=cic-switchtemplate-dialog-fc-addNetwork-input"  # fc network
    ID_SEARCH_CREATE_UPLINK_SET_FC_NETWORK = "xpath=//input[@id='cic-switchtemplate-dialog-fc-addNetwork-input']/..//div[@class='hp-search-combo-control']"  # fc network
    ID_OPTION_CREATE_UPLINK_SET_FC_NETWORK = "xpath=//input[@id='cic-switchtemplate-dialog-fc-addNetwork-input']/..//ol/li/span[.='%s']"
    ID_COMBO_CREATE_UPLINK_SET_FC_INTERCONNECT = "id=cic-switchtemplate-dialog-fc-switch-input"  # fc interconnect
    ID_COMBO_CREATE_UPLINK_SET_TUNNEL_NETWORK = "id=cic-switchtemplate-dialog-tunnel-addNetwork-input"  # tunnel
    ID_COMBO_CREATE_UPLINK_SET_UNTAGGED_NETWORK = "id=cic-switchtemplate-dialog-untagged-addNetwork-input"  # untagged
    ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_NATIVE = "xpath=//table//tr[td[.='%s']]//input"  # ethernet native network
    ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_PREFERRED_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s']]//input"  # ethernet preferred port
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ETHERNET_NETWORK = "xpath=//table//tr[td[.='%s']]//div"  # ethernet - remove network
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ETHERNET_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s']]//div"  # ethernet, tunnel, untagged - remove port
    ID_CHECKBOX_CREATE_UPLINK_SET_FC_PORT = "xpath=//tr[@id='cic-switchtemplate-uplink-port-row-%s']//input"  # fc port
    # ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[3][.='%s'] and td[4][.='%s']]/td[5]/div/div"  # fc port speed
    # ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[3][.='%s'] and td[4][.='%s']]/td[5]/div//ol/li[span[.='%s']]"  # fc port speed
    ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.='%s'] and td[.='%s'] and td[@class='hp-select-control']]//div/div[@class='hp-select']"  # bay,port
    ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.='%s'] and td[.='%s'] and td[@class='hp-select-control']]//div/ol/li[.='%s']"

    ID_TEXT_UPLINK_NOTIFICATION_RESOLUTION = "xpath=.//*[@class='hp-form-message-details']//div[@class='hp-notification-details']//div[@class='hp-resolution-container']/span[@class='hp-resolution']/p/span"
    ID_TEXT_UPLINK_NOTIFICATION_ERROR = "xpath=.//*[@class='hp-form-message-details']//div[@class='hp-notification-details']//div[@class='hp-details']/p/span"
    # -- { add networks to (ethernet)
    ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO = "xpath=//h1[contains(., 'Add Networks to')]"  # dialog
    ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_NETWORKS_TO = "xpath=//table//tr[td[.='%s']]"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_CANCEL = "xpath=//button[.='Cancel']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_NETWORK = "xpath=//table[@id='cic-switchtemplate-dialog-network-assigned']//td[.='%s']"
    # -- }
    # -- { add uplink port (ethernet)
    ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO = "xpath=//h1[contains(., 'Add Uplink Ports to')]"  # dialog
    ID_INPUT_CREATE_UPLINK_SET_ADD_UPLINK_PORT_SEARCH_PORT = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT = "xpath=//table//tr[(td[2][.='{0}'] and td[3][.='{1}']) or (td[3][.='{0}'] and td[4][.='{1}'])]"
    ID_TBIRD_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s'] and td[4][.='%s']]"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_CANCEL = "xpath=//button[.='Cancel']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_PORT = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[(td[2][.='{0}'] and td[3][.='{1}']) or (td[3][.='{0}'] and td[4][.='{1}'])]"
    ID_TBIRD_TABLE_ROW_CREATE_UPLINK_SET_PORT = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[2][.='%s'] and td[3][.='%s'] and td[4][.='%s']]"
    # -- }
    ID_TBIRD_TABLE_ROW_CREATE_UPLINK_SET_PORT_CARBON = "xpath=//table[@class='hp-selectable hp-association-selector-table dataTable']/tbody/tr/td[text()='%s']/following-sibling::td[text()='%s']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD = "id=cic-switchtemplate-dialog-add"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_PLUS = "id=cic-switchtemplate-dialog-add-again"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_CANCEL = "xpath=//form[@id='cic-switchtemplate-dialog-form']//a[.='Cancel']"
    # - }

    # - { Interconnect Settings
    ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER = "id=cic-interconnect-settings-edit-failover"
    ID_INPUT_MAC_REFRESH_INTERVAL = "id=cic-interconnect-settings-edit-mac-interval"
    ID_CHECKBOX_IGMP_SNOOPING = "id=cic-interconnect-settings-edit-snooping-enable"
    ID_INPUT_IGMP_IDLE_TIMEOUT_INTERVAL = "id=cic-interconnect-settings-edit-igmp-interval"
    ID_CHECKBOX_LOOP_PROTECTION = "id=cic-interconnect-settings-edit-loop"
    ID_CHECKBOX_PAUSE_FLOOD_PROTECTION = "id=cic-interconnect-settings-edit-pause-flood"
    ID_CHECKBOX_LLDP_TAGGING = "id=cic-interconnect-settings-edit-vlan-tagging"
    ID_CHECKBOX_LLDP_ENHANCED_TLV = "id=cic-interconnect-settings-edit-rich-tlv"
    # - }

    # - { Utilization Sampling
    ID_INPUT_INTERVAL_BETWEEN_SAMPLES = "id=cic-utilization-sampling-edit-interval"
    ID_INPUT_TOTAL_NUMBER_OF_SAMPLES = "id=cic-utilization-sampling-edit-samples"
    ID_LABEL_SAMPLE_COLLECTION_RATE = "id=cic-utilization-sampling-edit-collection-rate"
    ID_LABEL_TOTAL_SAMPLING_HISTORY = "id=cic-utilization-sampling-edit-sampling-history"
    # - }

    # - { SNMP
    ID_TOGGLE_SNMP = "id=cic-snmp-general-snmp-hpToggle"
    ID_TOGGLE_SNMPV1V2 = "id=cic-snmp-general-snmp-v1v2-hpToggle"
    ID_TOGGLE_SNMPv3 = "id=cic-snmp-general-snmp-v3-hpToggle"
    ID_INPUT_SYSTEM_CONTACT = "id=cic-snmp-general-system-contact"
    ID_INPUT_READ_COMMUNITY = "id=cic-snmp-general-read-community"
    # The Below elements are applicable only for feature toggle in OVF292/293 feature.
    # -- { Add SNMP user
    ID_BUTTON_ADD_SNMP_USER = "xpath=.//*[@id='cic-snmp-general-add-snmp-user']"
    ID_BUTTON_ADD_SNMPV3_USER_CANCEL = "xpath=//form[@id='cic-snmp-snmpv3-user-form']//a[.='Cancel']"
    ID_INPUT_ADD_SNMP_USER_NAME = "xpath=.//*[@id='cic-snmp-snmpv3-user-username']"
    ID_RADIO_SECURITY_LEVEL_NONE = "xpath=.//*[@id='cic-snmp-snmpv3-user-security-level-none']"
    ID_RADIO_SECURITY_LEVEL_AUTHENTICATION = "xpath=.//*[@id='cic-snmp-snmpv3-user-security-level-auth']"
    ID_COLLAPSE_AUTHENTICATION_AND_PRIVACY_PROTOCOL = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item privacy-protocol-fields']/div/..//div[@class='hp-value']"
    ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY = "xpath=.//*[@id='cic-snmp-snmpv3-user-security-level-authpriv']"
    ID_COLLAPSE_AUTHENTICATION_PROTOCOL = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item auth-protocol-fields']/div/..//div[@class='hp-value']"
    ID_SELECT_AUTHENTICATION_PROTOCOL = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item auth-protocol-fields']/div/..//li[@data-id='%s']"
    ID_TEXT_AUTHENTICATION_PROTOCOL = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item auth-protocol-fields']/div/..//ol[@class='hp-options']"
    ID_TEXT_PRIVACY_PROTOCOL = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item privacy-protocol-fields']/div/..//ol[@class='hp-options']"
    ID_INPUT_AUTHENTICATION_PASSWORD = "xpath=.//*[@id='cic-snmp-snmpv3-user-auth-password']"
    ID_INPUT_CONFIRM_AUTHENTICATION_PASSWORD = "xpath=.//*[@id='cic-snmp-snmpv3-user-auth-password-confirm']"
    ID_SELECT_AUTHENTICATION_AND_PRIVACY_PROTOCOL = "xpath=.//*[@id='cic-snmp-snmpv3-user-form']/..//fieldset/ol/li[@class='hp-form-item privacy-protocol-fields']/div/..//ol/li[span[.='%s']]/span"
    ID_INPUT_PRIVACY_PASSWORD = "xpath=.//*[@id='cic-snmp-snmpv3-user-priv-password']"
    ID_INPUT_CONFIRM_PRIVACY_PASSWORD = "xpath=.//*[@id='cic-snmp-snmpv3-user-priv-password-confirm']"
    ID_BUTTON_ADD_SNMP_USER_ADD = "xpath=.//*[@id='cic-snmp-snmpv3-user-add-button']"
    ID_BUTTON_ADD_SNMP_USER_ADD_PLUS = "xpath=.//*[@id='cic-snmp-snmpv3-user-add-again']"
    ID_BUTTON_ADD_SNMP_USER_CANCEL = "xpath=//form[@id='cic-snmp-snmpv3-user-form']//a[.='Cancel']"
    ID_BUTTON_SNMP_ERROR_DIALOG_CLOSE = "xpath=//button[.='Close']"
    ID_COLLAPSE_SNMP_ERROR_DIALOG_TRAPS = "xpath=.//*[@id='cic-snmp-snmpv3-user-delete-error-details-label']"
    ID_TEXT_SNMP_ERROR_DIALOG_TRAPS = "xpath=.//*[@id='cic-snmp-snmpv3-user-delete-error-details-table_wrapper']"
    # -- { Add Trap Destination
    ID_BUTTON_ADD_TRAP_DESTINATION = "id=cic-snmp-general-add-trap-destination"
    ID_DIALOG_ADD_TRAP_DESTINATION = "id=cic-snmp-trap-destination-form"
    ID_INPUT_ADD_TRAP_DESTINATION_TRAP_DESTINATION = "id=cic-snmp-trap-destination-trap-destination"
    ID_INPUT_ADD_TRAP_DESTINATION_COMMUNITY_STRING = "id=cic-snmp-trap-destination-community-string"
    ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV1 = "id=cic-snmp-trap-destination-snmpv1"
    ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV2 = "id=cic-snmp-trap-destination-snmpv2"
    ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV3 = "id=cic-snmp-trap-destination-snmpv3"
    ID_TOGGLE_TRAP_DESTINATION_NOTIFICATION = "id=cic-snmp-trap-destination-notification-type-hpToggle"
    ID_INPUT_TRAP_DESTINATION_ENGINE_ID = "xpath=.//*[@id='cic-snmp-trap-destination-engine-id']"
    ID_COLLAPSE_USER_TRAP_DESTINATION = "xpath=.//*[@id='cic-snmp-trap-destination-snmp-user-div']/div/div[@class='hp-search-combo-control-region']/div"
    ID_TEXT_SNMPV3_TRAP_DESTINATION_SNMP_USERS = "xpath=.//*[@id='cic-snmp-trap-destination-snmp-user-div']/..//ol[@class='hp-search-combo-scroller hp-options']"
    ID_SELECT_SNMPV3_TRAP_DESTINATION_SNMP_USER = "xpath=.//*[@id='cic-snmp-trap-destination-snmp-user-div']/..//ol[@class='hp-search-combo-scroller hp-options']/li[@data-id='%s']"
    ID_INPUT_ADD_TRAP_DESTINATION_PORT = "xpath=.//*[@id='cic-snmp-trap-destination-port']"

    # -- }
    # --- { Severity
    ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_SEVERITY = "xpath=.//*[@id='cic-snmp-trap-destination-severity-%s']"
    ID_COLLAPSE_ADD_TRAP_DESTINATION_SEVERITY = "id=cic-snmp-trap-destination-severity-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_CRITICAL = "id=cic-snmp-trap-destination-severity-critical"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_MAJOR = "id=cic-snmp-trap-destination-severity-major"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_MINOR = "id=cic-snmp-trap-destination-severity-minor"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_WARNING = "id=cic-snmp-trap-destination-severity-warning"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_NORMAL = "id=cic-snmp-trap-destination-severity-normal"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_INFO = "id=cic-snmp-trap-destination-severity-info"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_UNKNOWN = "id=cic-snmp-trap-destination-severity-unknown"
    # --- }
    # --- { VCM traps
    ID_COLLAPSE_ADD_TRAP_DESTINATION_VCM_TRAPS = "id=cic-snmp-trap-destination-vcmtraps-status"
    ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_VCM_TRAP = "xpath=.//*[@id='cic-snmp-trap-destination-vcmtraps-%s']"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VCM_TRAPS_LEGACY = "id=cic-snmp-trap-destination-vcmtraps-legacy"
    # --- }
    # --- { VC-Enet traps
    ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_ENET_TRAPS = "id=cic-snmp-trap-destination-vcenet-status"
    ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_ENET_TRAP = "xpath=.//*[@id='cic-snmp-trap-destination-vcenet-%s']"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_ENET_TRAPS_PORT_STATUS = "id=cic-snmp-trap-destination-vcenet-port-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_ENET_TRAPS_PORT_THRESHOLDS = "id=cic-snmp-trap-destination-vcenet-port-threshold"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_ENET_TRAPS_OTHER = "id=cic-snmp-trap-destination-vcenet-other"
    # --- }
    # --- { VC-FC traps
    ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_FC_TRAPS = "id=cic-snmp-trap-destination-vcfc-status"
    ID_BUTTON_ADD_TRAP_DESTINATION_SELECT_FC_TRAP = "xpath=.//*[@id='cic-snmp-trap-destination-vcfc-%s']"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_FC_TRAPS_PORT_STATUS = "id=cic-snmp-trap-destination-vcfc-port-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_FC_TRAPS_OTHER = "id=cic-snmp-trap-destination-vcfc-other"
    # --- }
    ID_BUTTON_ADD_TRAP_DESTINATION_ADD = "id=cic-snmp-trap-destination-add-button"
    ID_BUTTON_ADD_TRAP_DESTINATION_ADD_PLUS = "id=cic-snmp-trap-destination-add-again"
    ID_BUTTON_ADD_TRAP_DESTINATION_CANCEL = "xpath=//form[@id='cic-snmp-trap-destination-form']//a[.='Cancel']"
    # -- }

    # -- { Add SNMP Access
    ID_BUTTON_ADD_SNMP_ACCESS = "id=cic-snmp-general-add-snmp-access"
    ID_DIALOG_ADD_SNMP_ACCESS = "id=cic-snmp-access-form"
    ID_INPUT_ADD_SNMP_ACCESS_IP_OR_SUBNET = "id=cic-snmp-add-access-address"
    ID_BUTTON_ADD_SNMP_ADD = "id=cic-snmp-access-add-button"
    ID_BUTTON_ADD_SNMP_ADD_PLUS = "id=cic-snmp-access-add-again-button"
    ID_BUTTON_ADD_SNMP_CANCEL = "xpath=//form[@id='cic-snmp-access-form']//a[.='Cancel']"
    # -- }
    # - }

    # - { QOS
    ID_SELECT_QOS_CONFIGURATION_TYPE = "id=cic-qos-select-configtype-content"
    # - }
    ID_OPTION_UPLINK = "id=cic-qos-set-classify-uplinks"
    ID_OPTION_DOWNLINK = "id=cic-qos-set-classify-downlinks"

    ID_TEXT_VERIFYING_PARAMETERS = "xpath=//div/span[contains(., 'Verifying parameters')]"
    ID_ICON_STATUS_CHANGING = "xpath=//div[@id='hp-form-message']//div[@class='hp-status-changing']"

    ID_BUTTON_CREATE = "id=cic-switchtemplate-add"
    ID_BUTTON_CREATE_PLUS = "id=cic-switchtemplate-again"
    ID_BUTTON_CANCEL = "id=cic-switchtemplate-add-close"


class CreateLogicalInterconnectGroupsElements(_BaseCreateLogicalInterconnectGroupsElements):
    pass


class C7000CreateLogicalInterconnectGroupsElements(_BaseCreateLogicalInterconnectGroupsElements):
    # replace %s with 'Virtual Connect' or 'Fabric Extender' in below xpath
    ID_SELECT_INTERCONNECT_TYPE = "cic-switchtemplate-add-module-type-c7000-value"
    ID_BUTTON_SELECT_INTERCONNECTS = "xpath=//input[@id='cic-switchtemplate-add-select-c7000-interconnects-button']"
    ID_SELECT_BAY_TYPE = "id=cic-switch-template-add-device-%s"
    ID_SELECTED_BAY_TYPE = "xpath=//li[@id='cic-switch-template-add-device-1-%s']/..//div[@class='hp-value'][.='%s']"
    ID_JAVASCRIPT_BAY_TYPE = "$('#cic-switch-template-add-device-1-%s').find('div[class=\"hp-select\"]').trigger('click');"
    ID_JAVASCRIPT_SELECT_BAY_TYPE = "$('#cic-switch-template-add-device-1-%s').parent().find('span').filter(function(idx, elt){return $(elt).text()=='%s';}).trigger('click');"
    ID_DROPDOWN_BAY_TYPE_OPTION_LAYER = "xpath=//li[@id='cic-switch-template-add-device-1-%s']//ol[@class='hp-options']"
    ID_COMBO_UPLINK_ETHERNET_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.=%s] and td[.='%s'] and td[@class='hp-select-control']]//div/div[@class='hp-select']//*[text()='Auto']"  # bay,port
    ID_SELECT_UPLINK_ETHERNET_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.=%s] and td[.='%s'] and td[@class='hp-select-control']]//div/ol/li[.='%s']"
    ID_TEXT_AUTONEGOTIATION = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.='%s'] and td[.='%s']]/td[(text()='Enabled') or (text()='Disabled')]"   # enclosure,Bay,portname


class TBirdCreateLogicalInterconnectGroupsElements(_BaseCreateLogicalInterconnectGroupsElements):
    ID_SELECT_INTERCONNECT_TYPE = "cic-switchtemplate-add-module-type-synergy-value"
    ID_SELECT_BAY_TYPE = "xpath=//*[@id='cic-switch-template-add-device-%s-%s']//div[@class='hp-value']"
    ID_SELECT_BAY_TYPE_FC = "xpath=//*[@id='cic-switch-template-add-device--%s-%s']//div[@class='hp-value']"
    ID_DROPDOWN_BAY_TYPE_VALUE = "xpath=//*[@id='cic-switch-template-add-device-%s-%s']//span[@class='hp-name' and text()='%s']"
    ID_DROPDOWN_BAY_TYPE_VALUE_FC = "xpath=//*[@id='cic-switch-template-add-device--%s-%s']//span[@class='hp-name' and text()='%s']"

    ID_JAVASCRIPT_BAY_TYPE = "$('#cic-switch-template-add-device-%s-%s').find('div[class=\"hp-select\"]').trigger('click');"
    ID_JAVASCRIPT_SELECT_BAY_TYPE = "$('#cic-switch-template-add-device-%s-%s').parent().find('span').filter(function(idx, elt){return $(elt).text()=='%s';}).trigger('click');"
    ID_DROPDOWN_BAY_TYPE_OPTION_LAYER = "xpath=//li[@id='cic-switch-template-add-device-%s-%s']//ol[@class='hp-options']"
    ID_SELECTED_BAY_TYPE = "xpath=//li[@id='cic-switch-template-add-device-%s-%s']/..//div[@class='hp-value'][.='%s']"

    # tbird dialog element
    ID_SELECT_ENCLOSURE_COUNT = "id=cic-switchtemplate-add-enclosure-count-value"
    ID_SELECT_INTERCONNECT_BAY_SET = "id=cic-switchtemplate-add-interconnect-bay-value"
    ID_SELECT_REDUNDANCY = "id=cic-switchtemplate-add-redundancy-choice"
    ID_BUTTON_SELECT_INTERCONNECTS = "xpath=//*[@id='cic-switchtemplate-add-select-synergy-interconnects-button']"
    ID_SELECT_INTERCONNECT_TEXT = "xpath=//*[@id='cic-switchtemplate-add-module-type-value-container']//span[@class='hp-name' and text()='%s']"

    ID_INTERCONNECT_TYPE = "xpath=//li[@id='cic-switchtemplate-add-module-type-synergy']//div[@class='hp-select']/div[@class='hp-value']"
    ID_INTERCONNECT_TYPE_OPTION = "xpath=//*[@id='cic-switchtemplate-add-module-type-synergy']//ol[@class='hp-options']//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    ID_ENCLOSURE_STATIC_COUNT = "xpath=//*[@id='cic-switchtemplate-add-enclosure-count-static-value']"
    ID_DROPDOWN_TBIRD_ENCLOSURE_COUNT = "id=cic-switchtemplate-add-enclosure-count"
    ID_DROPDOWN_TBIRD_INTERCONNECT_BAY_SET = "id=cic-switchtemplate-add-interconnect-bay-set"
    ID_DROPDOWN_TBIRD_REDUNDANCY = "id=cic-switchtemplate-add-redundancy"
    ID_ENCLOSURE_CONTAINER = "xpath=//*[@id='cic-switch-template-add-switches']//*[text()='Enclosure %s']"
    ID_TOGGLE_SAMPLE_COLLECTION = 'id=cic-switchtemplate-switch-add-sample-collection-hpToggle'
    ID_INPUT_INTERVAL_SAMPLES = 'id=cic-switchtemplate-switch-add-interval'
    ID_INPUT_TOTAL_SAMPLES = 'id=cic-switchtemplate-switch-add-samples'
    ID_COMBO_UPLINK_ETHERNET_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.=%s] and td[.='%s'] and td[.='%s'] and td[@class='hp-select-control']]//div/div[@class='hp-select']"  # bay,port
    ID_SELECT_UPLINK_ETHERNET_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.=%s] and td[.='%s'] and td[.='%s'] and td[@class='hp-select-control']]//div/ol/li[.='%s']"  # enclosure,bay,port,speed
    ID_TEXT_AUTONEGOTIATION = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[.='%s'] and td[.='%s'] and td[.='s']]/td[(text()='Enabled') or (text()='Disabled')]"   # enclosure,Bay,port


class _BaseEditLogicalInterconnectGroupsElements(object):
    ID_SELECT_ACTION_EDIT = "//li[@id='cic-switchtemplate-edit-action']/a"

    # dialog
    ID_DIALOG_EDIT_LIG = "id=cic-switchtemplate-edit-form"

    # panel selector
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-switchtemplate-panel-edit-selector"
    ID_DROPDOWN_PANEL_LAYER = "xpath=//div[@id='cic-switchtemplate-panel-edit-selector']//ol[@class='hp-options']"
    ID_SELECT_GENERAL = "xpath=//a[.='General']"
    ID_SELECT_LOGICAL_INTERCONNECT_GROUP = "xpath=//a[.='Logical Interconnect Group']"
    ID_SELECT_INTERCONNECT_SETTINGS = "xpath=//a[.='Interconnect Settings']"
    ID_SELECT_UTILIZATION_SAMPLING = "xpath=//a[.='Utilization Sampling']"
    ID_SELECT_SNMP = "xpath=//a[.='SNMP']"
    ID_SELECT_QUALITY_OF_SERVICE = "xpath=//a[.='Quality of Service']"

    # dialog elements
    ID_INPUT_NAME = "id=cic-switchtemplate-edit-name"
    ID_JAVASCRIPT_BAY_TYPE = "$('#cic-switch-template-edit-switch-type-1-%s').parent().find('div[class=\"hp-select\"]').trigger('click');"
    ID_JAVASCRIPT_SELECT_BAY_TYPE = "$('#cic-switch-template-edit-switch-type-1-%s').parent().find('span').filter(function(idx, elt){return $(elt).text()=='%s';}).trigger('click');"
    ID_DROPDOWN_BAY_TYPE_OPTION_LAYER = "xpath=//select[@id='cic-switch-template-edit-switch-type-1-%s']/..//ol[@class='hp-options']"
    ID_SELECTED_BAY_TYPE = "xpath=//select[@id='cic-switch-template-edit-switch-type-1-%s']/..//div[@class='hp-value'][.='%s']"
    ID_BUTTON_ADD_UPLINK_SET = "id=cic-add-uplink-li"
    ID_TITLE_UPLINK_SET_BOX = "//ol[@id='cic-switch-template-edit-uplinks']//div[.='%s']"
    ID_BUTTON_EDIT_UPLINK_SET = "xpath=//ol[@id='cic-switch-template-edit-uplinks']//div[.='%s']/../div[@class='hp-controls']/div[contains(@class, 'cic-uplink-edit-button')]"
    ID_BUTTON_REMOVE_UPLINK_SET = "xpath=//ol[@id='cic-switch-template-edit-uplinks']//div[.='%s']/../div[@class='hp-controls']/div[contains(@class, 'cic-uplink-delete-button')]"

    # - { internal network
    ID_BUTTON_EDIT_INTERNAL_NETWORKS = "xpath=//div[contains(@class, 'cic-internal-networks-edit-button')]"
    ID_DIALOG_EDIT_INTERNAL_NETWORKS = "xpath=//h1[.='Edit Internal Networks']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "id=cic-internal-nets-dialog-networks-addNetworks"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_REMOVE_ALL = CreateLogicalInterconnectGroupsElements.ID_BUTTON_EDIT_INTERNAL_NETWORKS_REMOVE_ALL
    ID_DIALOG_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "xpath=//h1[.='Add Networks']"
    ID_INPUT_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_SEARCH_NETWORK = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS = "xpath=//table//tr[td[.='%s']]"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_ADD_NETWORKS_CANCEL = "xpath=//form[@id='cic-internal-nets-dialog-form']//button[.='Cancel']"
    ID_TABLE_ROW_EDIT_INTERNAL_NETWORKS = "xpath=//table[@id='cic-internal-nets-dialog-network-assigned']//td[.='%s']"
    ID_TABLE_ROW_TH_EDIT_INTERNAL_NETWORKS = "xpath=//div[@id='cic-internal-nets-dialog-network-assigned_wrapper']//th[.='%s']"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_OK = "cic-internal-nets-dialog-add-ok"
    ID_BUTTON_EDIT_INTERNAL_NETWORKS_CANCEL = "xpath=//form[@id='cic-internal-nets-dialog-form']//a[.='Cancel']"
    # - }

    # - { Utilization Sampling
    ID_INPUT_INTERVAL_BETWEEN_SAMPLES = _BaseCreateLogicalInterconnectGroupsElements.ID_INPUT_INTERVAL_BETWEEN_SAMPLES
    ID_INPUT_TOTAL_NUMBER_OF_SAMPLES = _BaseCreateLogicalInterconnectGroupsElements.ID_INPUT_TOTAL_NUMBER_OF_SAMPLES
    ID_LABEL_SAMPLE_COLLECTION_RATE = _BaseCreateLogicalInterconnectGroupsElements.ID_LABEL_SAMPLE_COLLECTION_RATE
    ID_LABEL_TOTAL_SAMPLING_HISTORY = _BaseCreateLogicalInterconnectGroupsElements.ID_LABEL_TOTAL_SAMPLING_HISTORY
    # - }

    # - { add uplink set
    ID_DIALOG_CREATE_UPLINK_SET = "xpath=//h1[.='Create uplink set']"  # dialog
    ID_DIALOG_EDIT_UPLINK_SET = "xpath//h1[@id='cic-switchtemplate-dialog-title'][.='Edit %s']"  # edit dialog
    ID_INPUT_CREATE_UPLINK_SET_NAME = "id=cic-switchtemplate-dialog-name"
    ID_SELECT_CREATE_UPLINK_SET_TYPE = "id=cic-switchtemplate-dialog-type"
    ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_AUTOMATIC = "id=cic-switchtemplate-dialog-auto-conntype"  # for ethernet
    ID_RADIO_CREATE_UPLINK_SET_CONNECTION_MODE_FAILOVER = "id=cic-switchtemplate-dialog-fail-conntype"  # for ethernet
    ID_SELECT_CREATE_UPLINK_SET_LACP_TIMER = "id=cic-switchtemplate-dialog-lacp-timer-select"  # for ethernet
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS = "id=cic-switchtemplate-dialog-networks-addNetworks"  # for ethernet
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_NETWORKS = "id=cic-switchtemplate-dialog-networks-removeAll"  # for ethernet
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ALL_ETHERNET_PORTS = "id=cic-switchtemplate-dialog-ports-removeAll"  # for ethernet, tunnel, untagged
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS = "id=cic-switchtemplate-dialog-uplinks-addUplinks"  # port of ethernet, tunnel, untagged
    ID_COMBO_CREATE_UPLINK_SET_FC_NETWORK = "id=cic-switchtemplate-dialog-fc-addNetwork-input"  # fc network
    ID_COMBO_CREATE_UPLINK_SET_FC_INTERCONNECT = "id=cic-switchtemplate-dialog-fc-switch-input"  # fc interconnect
    ID_COMBO_CREATE_UPLINK_SET_TUNNEL_NETWORK = "id=cic-switchtemplate-dialog-tunnel-addNetwork-input"  # tunnel
    ID_COMBO_CREATE_UPLINK_SET_UNTAGGED_NETWORK = "id=cic-switchtemplate-dialog-untagged-addNetwork-input"  # untagged
    ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_NATIVE = "xpath=//table//tr[td[.='%s']]//input"  # ethernet native network
    ID_CHECKBOX_CREATE_UPLINK_SET_ETHERNET_PREFERRED_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s']]//input"  # ethernet preferred port
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ETHERNET_NETWORK = "xpath=//table//tr[td[.='%s']]//div"  # ethernet - remove network
    ID_BUTTON_CREATE_UPLINK_SET_REMOVE_ETHERNET_PORT = "xpath=//table//tr[td[2][.='%s'] and td[3][.='%s']]//div"  # ethernet, tunnel, untagged - remove port
    ID_CHECKBOX_CREATE_UPLINK_SET_FC_PORT = "xpath=//tr[@id='cic-switchtemplate-uplink-port-row-%s']//input"  # fc port
    ID_SELECT_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[2][.='{0}'] and td[3][.='{1}']]/td[4]/div/div/div | //table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[3][.='{0}'] and td[4][.='{1}']]/td[5]/div/div/div"  # fc port speed
    ID_DROPDOWN_CREATE_UPLINK_SET_FC_PORT_SPEED = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[2][.='{0}'] and td[3][.='{1}']]/td[4]/div//ol/li[span[.='{2}']] | //table[@id='cic-switchtemplate-dialog-port-assigned']//tr[td[3][.='{0}'] and td[4][.='{1}']]/td[5]/div//ol/li[span[.='{2}']]"  # fc port speed
    # -- { add networks to (ethernet)
    ID_DIALOG_CREATE_UPLINK_SET_ADD_NETWORKS_TO = "xpath=//h1[contains(., 'Add Networks to')]"  # dialog
    ID_INPUT_CREATE_UPLINK_SET_ADD_NETWORKS_TO_SEARCH_NETWORK = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_NETWORKS_TO = "xpath=//table//tr[td[.='%s']]"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_NETWORKS_TO_CANCEL = "xpath=//button[.='Cancel']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_NETWORK = "xpath=//table[@id='cic-switchtemplate-dialog-network-assigned']//td[.='%s']"
    # -- }
    # -- { add uplink port (ethernet)
    ID_DIALOG_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_TO = "xpath=//h1[contains(., 'Add Uplink Ports to')]"  # dialog
    ID_INPUT_CREATE_UPLINK_SET_ADD_UPLINK_PORT_SEARCH_PORT = "xpath=//div[@class='hp-association-selector']//input[@class='hp-search']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_ADD_UPLINK_PORT = "xpath=//table//tr[(td[2][.='{0}'] and td[3][.='{1}']) or (td[3][.='{0}'] and td[4][.='{1}'])]"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_UPLINK_PORTS_CANCEL = "xpath=//button[.='Cancel']"
    ID_TABLE_ROW_CREATE_UPLINK_SET_PORT = "xpath=//table[@id='cic-switchtemplate-dialog-port-assigned']//tr[(td[2][.='{0}'] and td[3][.='{1}']) or (td[3][.='{0}'] and td[4][.='{1}'])]"
    # -- }
    ID_BUTTON_CREATE_UPLINK_SET_ADD = "id=cic-switchtemplate-dialog-add"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_PLUS = "id=cic-switchtemplate-dialog-add-again"
    ID_BUTTON_CREATE_UPLINK_SET_ADD_CANCEL = "xpath=//form[@id='cic-switchtemplate-dialog-form']//a[.='Cancel']"
    # - }

    # - { Interconnect Settings
    ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER = _BaseCreateLogicalInterconnectGroupsElements.ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER
    ID_INPUT_MAC_REFRESH_INTERVAL = _BaseCreateLogicalInterconnectGroupsElements.ID_INPUT_MAC_REFRESH_INTERVAL
    ID_CHECKBOX_IGMP_SNOOPING = _BaseCreateLogicalInterconnectGroupsElements.ID_CHECKBOX_IGMP_SNOOPING
    ID_INPUT_IGMP_IDLE_TIMEOUT_INTERVAL = _BaseCreateLogicalInterconnectGroupsElements.ID_INPUT_IGMP_IDLE_TIMEOUT_INTERVAL
    ID_CHECKBOX_LOOP_PROTECTION = _BaseCreateLogicalInterconnectGroupsElements.ID_CHECKBOX_LOOP_PROTECTION
    ID_CHECKBOX_PAUSE_FLOOD_PROTECTION = _BaseCreateLogicalInterconnectGroupsElements.ID_CHECKBOX_PAUSE_FLOOD_PROTECTION
    ID_CHECKBOX_LLDP_TAGGING = _BaseCreateLogicalInterconnectGroupsElements.ID_CHECKBOX_LLDP_TAGGING
    ID_CHECKBOX_LLDP_ENHANCED_TLV = _BaseCreateLogicalInterconnectGroupsElements.ID_CHECKBOX_LLDP_ENHANCED_TLV
    # - }

    # - { SNMP
    ID_TOGGLE_SNMP = "id=cic-snmp-general-snmp-hpToggle"
    ID_INPUT_SYSTEM_CONTACT = "id=cic-snmp-general-system-contact"
    ID_INPUT_READ_COMMUNITY = "id=cic-snmp-general-read-community"
    ID_BUTTON_EDIT_TRAP_DESTINATION = "xpath=//div[@id='cic-snmp-trap-forwarding-table-container']//tr[td[.='%s']]//td[div[@class='hp-edit']]/div"
    ID_BUTTON_DELETE_TRAP_DESTINATION = "xpath=//div[@id='cic-snmp-trap-forwarding-table-container']//tr[td[1][.='%s']]/td[9]/div"
    ID_BUTTON_DELETE_SNMPV3_TRAP_DESTINATION = "xpath=//div[@id='cic-snmp-trap-forwarding-table-container']//tr[td[.='%s']]/td[div[@class='hp-close']]/div"
    ID_BUTTON_TBIRD_DELETE_TRAP_DESTINATION = "xpath=//div[@id='cic-snmp-trap-forwarding-table-container']//tr[td[1][.='%s']]/td[5]/div"
    ID_BUTTON_REMOVE_TRAP_DESTINATION_YES_REMOVE = "xpath=//button[.='Yes, remove']"
    ID_DIALOG_REMOVE_TRAP_DESTINATION = "id=cic-snmp-remove-trap-dialog-title"
    ID_BUTTON_EDIT_SNMP_ACCESS = "xpath=//div[@id='cic-snmp-access-table-container']//tr[td[1][.='%s']]/td[2]/div"
    ID_BUTTON_DELETE_SNMP_ACCESS = "xpath=//div[@id='cic-snmp-access-table-container']//tr[td[1][.='%s']]/td[3]/div"
    ID_BUTTON_REMOVE_SNMP_ACCESS_YES_REMOVE = "xpath=//button[.='Yes, remove']"
    ID_DIALOG_REMOVE_SNMP_ACCESS = "id=cic-snmp-remove-access-dialog-title"

    # - {SNMP USERS
    ID_BUTTON_REMOVE_SNMP_USER = "xpath=.//*[@id='cic-snmp-user-table']/tbody/tr[td[.='%s']]/td[div[@class='hp-close']]/div"
    ID_BUTTON_REMOVE_SNMP_USER_CONFIRM = "xpath=//button[.='Yes, remove']"
    ID_BUTTON_EDIT_SNMP_USER = "xpath=.//*[@id='cic-snmp-user-table']/.//tr[td[.='%s']]/td[div[@class='hp-edit']]/div"
    ID_BUTTON_OK_EDIT_SNMP_USER = "xpath=.//*[@id='cic-snmp-snmpv3-user-ok-button']"
    # }

    # -- { Add Trap Destination
    ID_BUTTON_ADD_TRAP_DESTINATION = "id=cic-snmp-general-add-trap-destination"
    ID_DIALOG_ADD_TRAP_DESTINATION = "id=cic-snmp-trap-destination-form"
    ID_INPUT_ADD_TRAP_DESTINATION_TRAP_DESTINATION = "id=cic-snmp-trap-destination-trap-destination"
    ID_INPUT_ADD_TRAP_DESTINATION_COMMUNITY_STRING = "id=cic-snmp-trap-destination-community-string"
    ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV1 = "id=cic-snmp-trap-destination-snmpv1"
    ID_RADIO_ADD_TRAP_DESTINATION_TRAP_FORMAT_SNMPV2 = "id=cic-snmp-trap-destination-snmpv2"
    ID_DIALOG_EDIT_TRAP_DESTINATION = "xpath=.//*[@id='cic-snmp-trap-destination-dialog-title']"
    ID_BUTTON_EDIT_TRAP_DESTINATION_OK = "xpath=.//*[@id='cic-snmp-trap-destination-ok-button']"
    # --- { Severity
    ID_COLLAPSE_ADD_TRAP_DESTINATION_SEVERITY = "id=cic-snmp-trap-destination-severity-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_CRITICAL = "id=cic-snmp-trap-destination-severity-critical"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_MAJOR = "id=cic-snmp-trap-destination-severity-major"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_MINOR = "id=cic-snmp-trap-destination-severity-minor"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_WARNING = "id=cic-snmp-trap-destination-severity-warning"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_NORMAL = "id=cic-snmp-trap-destination-severity-normal"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_INFO = "id=cic-snmp-trap-destination-severity-info"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_SEVERITY_UNKNOWN = "id=cic-snmp-trap-destination-severity-unknown"

    # --- }
    # --- { VCM traps
    ID_COLLAPSE_ADD_TRAP_DESTINATION_VCM_TRAPS = "id=cic-snmp-trap-destination-vcenet-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VCM_TRAPS_LEGACY = "id=cic-snmp-trap-destination-vcmtraps-legacy"
    # --- }
    # --- { VC-Enet traps
    ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_ENET_TRAPS = "id=cic-snmp-trap-destination-vcenet-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_ENET_TRAPS_PORT_STATUS = "id=cic-snmp-trap-destination-vcenet-port-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_ENET_TRAPS_PORT_THRESHOLDS = "id=cic-snmp-trap-destination-vcenet-port-threshold"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_ENET_TRAPS_OTHER = "id=cic-snmp-trap-destination-vcenet-other"
    # --- }
    # --- { VC-FC traps
    ID_COLLAPSE_ADD_TRAP_DESTINATION_VC_FC_TRAPS = "id=cic-snmp-trap-destination-vcfc-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_FC_TRAPS_PORT_STATUS = "id=cic-snmp-trap-destination-vcfc-port-status"
    ID_CHECKBOX_ADD_TRAP_DESTINATION_VC_FC_TRAPS_OTHER = "id=cic-snmp-trap-destination-vcfc-other"
    # --- }
    ID_BUTTON_ADD_TRAP_DESTINATION_ADD = "id=cic-snmp-trap-destination-add-button"
    ID_BUTTON_ADD_TRAP_DESTINATION_ADD_PLUS = "id=cic-snmp-trap-destination-add-again"
    ID_BUTTON_ADD_TRAP_DESTINATION_CANCEL = "xpath=//form[@id='cic-snmp-trap-destination-form']//a[.='Cancel']"
    # -- }

    # -- { Add SNMP Access
    ID_BUTTON_ADD_SNMP_ACCESS = "id=cic-snmp-general-add-snmp-access"
    ID_DIALOG_ADD_SNMP_ACCESS = "id=cic-snmp-access-form"
    ID_INPUT_ADD_SNMP_ACCESS_IP_OR_SUBNET = "id=cic-snmp-add-access-address"
    ID_BUTTON_ADD_SNMP_ADD = "id=cic-snmp-access-add-button"
    ID_BUTTON_ADD_SNMP_ADD_PLUS = "id=cic-snmp-access-add-again-button"
    ID_BUTTON_ADD_SNMP_CANCEL = "xpath=//form[@id='cic-snmp-access-form']//a[.='Cancel']"
    # -- }
    # - }

    # - { QOS
    ID_SELECT_QOS_CONFIGURATION_TYPE = "id=cic-qos-select-configtype-content"
    # - }

    ID_TEXT_VERIFYING_PARAMETERS = "xpath=//div/span[contains(., 'Verifying parameters')]"
    ID_ICON_STATUS_CHANGING = "xpath=//div[@id='hp-form-message']//div[@class='hp-status-changing']"

    ID_BUTTON_OK = "id=cic-switchtemplate-update"
    ID_BUTTON_CANCEL = "id=cic-switchtemplate-edit-cancel"
    ID_TEXT_QUALITY_OF_SERVICE_QOS_CONFIGURATION_TYPE = "xpath=.//*[@id='cic-interconnect-group-qos-edit-container']//*[@class='hp-value']"
    ID_OPTION_EDITCLASS = "xpath=.//*[@id='traffic-classes-table']//*[contains(text(),'%s')]"
    ID_OPTION_EDIT = "xpath =//*[contains(text(),'%s')]/../..//*[@class='hp-edit']"
    ID_TEXT_SHARE = "xpath=//*[contains (text(),'FCoE lossless')]/../..//*[contains (text(),'Share is')]"
    ID_TEXT_MAXSHARE = "xpath=//*[contains (text(),'FCoE lossless')]/../..//*[contains (text(),'Max share')]"
    ID_CHECKBOX_DSCP_VALUES = "xpath=.//*[@id='chkbx_%s']"
    ID_CHECKBOX_DOT1P_VALUES = "xpath=.//*[@id='chkbx_%s'] "
    ID_TEXT_MAPPINGS = "xpath=//*[contains(text(),'%s')]"
    ID_OPTION_EDITCLASS = "xpath=.//*[@id='traffic-classes-table']//*[contains(text(),'%s')]"
    ID_BUTTON_CLASS_OK = "xpath = //*[@id='cic-qos-traffic-class-ok-button']"
    ID_INPUT_SHAREVALUES = "xpath =.//*[@id='cic-qos-traffic-class-share']"
    ID_BUTTON_CLASS_ENABLE = "xpath=//*[@id='cic-qos-traffic-class-enable-hpToggle']/ol/li[text()='Disabled']"
    ID_TEXT_DISABLED = "xpath=.//*[@id='cic-qos-traffic-class-enable-hpToggle']/../*[@class='hp-toggle hp-checked']"
    ID_TABLE_DOTIP = "xpath = //table/tbody/tr/td[text()='%s']"
    ID_TEXT_MAPPINGS = "xpath=//*[contains(text(),'%s')]"
    ID_TABLE_DOTIP = "xpath = //table/tbody/tr/td[text()='%s']"
    ID_TEXT_INPUT_NAME = "xpath=//*[@id='cic-qos-traffic-class-name']"
    ID_TEXT_VALIDATE_MSG = "css=label.hp-error"
    ID_TEXT_QOS_ERROR = "xpath = //*[@class='hp-details']/p/span"
    ID_TABLE_CLASS_LIST = "xpath =//*[@id='traffic-classes-table']//*[@class='className']"
    ID_TEXT_TRAFFIC = "xpath =//*[contains(text(),'%s')]"
    ID_OPTION_MAX = "xpath = //*[@for='cic-qos-traffic-class-max-share']"
    ID_BUTTON_CLASS_CANCEL = "xpath=.//*[@id='cic-qos-traffic-class-form']//..[@class='hp-button hp-cancel']"
    ID_TEXT_SHAREVALUE = "xpath=//*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='%s']/following-sibling::th)]"
    ID_DROPDOWN_EGRESS_PRIORITY = "id=cic-qos-traffic-class-form"
    ID_INPUT_SHAREORMAX = "xpath=//*[@id='cic-qos-traffic-class-%s']"
    ID_TEXT_CLASS_NAME = "xpath=//*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='Max Share']/following-sibling::th)]"
    ID_TEXT_EGRESS_MAPPINGS = "xpath =.//*[@id='cic-qos-traffic-class-form']//*[@class ='hp-select hp-disabled']"
    ID_TABLE_EGRESS_FIELDS = "xpath =//table/tbody/tr/td[count(//table/thead/tr/th[.='Egress DOT1P Priority']/preceding-sibling::th)+1]"
    ID_DROPDOWN_DOT1P_LIST = "xpath = .//*[@id='cic-qos-traffic-class-form']//div[@class='hp-value']"
    ID_TEXT_DOT1P_PRIORITY = "xpath = .//*[@id='cic-qos-traffic-class-form']//li[@data-id=%s]"
    ID_FCOE_LOSELESS_PRIORITY = "xpath = //*[contains(text(),'FCoE lossless')]/../../td[count(//table/thead/tr/th[.='Egress DOT1P Priority']/preceding-sibling::th)+1]"
    ID_BEST_EFFORT_PRIORITY = "xpath = //*[contains(text(),'Best effort')]/../../td[count(//table/thead/tr/th[.='Egress DOT1P Priority']/preceding-sibling::th)+1]"
    ID_OPTION_CLASS_DISABLE = "xpath=.//*[@id='cic-qos-traffic-class-enable-hpToggle']/ol/li[text()='Enabled']"
    ID_TABLE_DOT1P_AVAILABILITY = "xpath=.//*[@id='cic-qos-traffic-class-form']/div/ol/li/label[@data-localize='qos.trafficClass.dialog.egressDot1p']"
    ID_BUTTON_CLASS_CANCEL = "xpath= //a[@class='hp-button hp-cancel']"
    ID_TABLE_DOT1P_CURRENT = "xpath=.//*[@id='cic-qos-dot1p_table']/tbody/tr[%s]/td[last()]"
    ID_TABLE_DOT1P_VALUE = "xpath=.//*[@id='cic-qos-dot1p_table']/tbody/tr[%s]/td[last()-1]"
    ID_TEXT_DSCP_CURRENT = "xpath=.//*[@id='cic-qos-dscp_table']/tbody/tr[%s]/td[last()]"
    ID_TEXT_DSCP_VALUE = "xpath=.//*[@id='cic-qos-dscp_table']/tbody/tr[%s]/td[last()-1]"
    ID_REAL_TIME_VALUE = "xpath=//*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='Traffic Class']/following-sibling::th)]"
    ID_TABLE_DOT1P_MAPPING = "xpath=.//*[@id='cic-qos-dot1p_mappings_wrapper']/ol/li/label"
    ID_TABLE_DSCP_MAPPING = "xpath=.//*[@id='cic-qos-dscp-mapping-table-title']"
    ID_DOT1P_DROPDOWN_LIST = "xpath=.//*[@id='cic-qos-traffic-class-form']//div[@class='hp-value']"
    ID_REAL_TIME_COL = "xpath = //*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='Traffic Class']/following-sibling::th)]"
    ID_REAL_TIME_SHAREVALUE = "xpath=. //*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='%s']/following-sibling::th)]"
    ID_TEXT_ENABLED_BESTEFFORT = "xpath = //*[@id='cic-qos-traffic-class-enable-hpToggle']/../*[@class='hp-toggle hp-checked hp-disabled']"
    ID_INPUT_MAXSHARE_VALUES = "//*[@id='cic-qos-traffic-class-max-share']"
    ID_TABLE_EGRESS_PRIORITY_VALUES = "xpath=//*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='Egress DOT1P Priority']/preceding-sibling::th)+1]"
    ID_TRAFFIC_CLASS_CANCEL = "xpath= //a[@class='hp-button hp-cancel']"
    ID_TEXT_DSCP_VALUE = "xpath=.//*[@id='cic-qos-dscp_table']/tbody/tr[%s]/td[last()-1]"
    ID_REAL_TIME_VALUE = "xpath=//*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='Traffic Class']/following-sibling::th)]"
    ID_TABLE_DOT1P_MAPPING = "xpath=.//*[@id='cic-qos-dot1p_mappings_wrapper']/ol/li/label"
    ID_TABLE_DSCP_MAPPING = "xpath=.//*[@id='cic-qos-dscp-mapping-table-title']"
    ID_DOT1P_DROPDOWN_LIST = "xpath=.//*[@id='cic-qos-traffic-class-form']//div[@class='hp-value']"
    ID_REAL_TIME_COL = "xpath = //*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='Traffic Class']/following-sibling::th)]"
    ID_BUTTON_REALCLASS_ENABLE = "xpath = .//*[@id='cic-qos-traffic-class-real-time-hpToggle']/ol/li[text()='Disabled']"
    ID_TEXT_MAXSHAREVALUE = "xpath=//*[contains(text(),'%s')]/../../td[count(//table/thead/tr/th[.='Enabled']/following-sibling::th)]"
    ID_TEXT_DOT1P_DSCP_MAPPINGS = "xpath=//*[@id='traffic-classes-table']/tbody/tr[%s]/td"
    ID_BUTTON_RESET = "xpath = .//*[@id='cic-qos-traffic-class-reset-button']"


class EditScopeElements(object):
    ID_HEADER_SCOPE = "//li[@id='hp-scopes-resource-show-panel']/label/span[text()='Scopes']"
    ID_TEXT_SCOPE_NOT_LOAD = "//li[@id='hp-scopes-resource-show-panel']/div[@class='hp-unavailable']"
    ID_BUTTON_EDIT = "//li[@id='hp-scopes-resource-show-panel']/label/a[.='Edit']"
    ID_DIALOG_EDIT = "//header[@id='hp-scopes-edit-header']"
    ID_DIALOG_ASSIGN = "//*[@class='hp-ellipsised']//span[contains(text(),'Assign to Scopes')]"
    ID_BUTTON_OK = "id=hp-scopes-edit-ok"
    ID_BUTTON_CANCEL = "id=hp-scopes-edit-cancel"
    ID_BUTTON_CLOSE = "id=hp-scopes-edit-close"
    ID_BUTTON_ASSIGN = "hp-scopes-edit-add"
    ID_BUTTON_ADD = "xpath=//button[text()='Add']"
    ID_BUTTON_ADD_PLUS = "xpath=//button[text()='Add +']"
    ID_BUTTON_CANCEL_ASSIGN = "xpath=//button[text()='Cancel']"
    ID_INPUT_SEARCH_TEXT = "//input[@class='hp-search']"
    ID_TABLE_SCOPE_NAME = "//form[@class='hp-edit-form']//table/tbody/tr/td[text()='%s']"
    ID_TABLE_REMOVE_SCOPE = "//form[@class='hp-edit-form']//table/tbody/tr[td[text()='%s']]//div"


class EditLogicalInterconnectGroupsElements(_BaseEditLogicalInterconnectGroupsElements):
    pass


class C7000EditLogicalInterconnectGroupsElements(_BaseEditLogicalInterconnectGroupsElements):
    ID_SELECT_BAY_TYPE = "id=cic-switch-template-edit-switch-type-1-%s"  # for C7000


class TBirdEditLogicalInterconnectGroupsElements(_BaseEditLogicalInterconnectGroupsElements):
    ID_SELECT_BAY_TYPE = "xpath=//*[@id='cic-switch-template-edit-device-%s-%s']//div[@class='hp-value']"
    ID_SELECT_BAY_TYPE_FC = "xpath=//*[@id='cic-switch-template-edit-device--%s-%s']//div[@class='hp-value']"
    ID_DROPDOWN_BAY_TYPE_VALUE = "xpath=//*[@id='cic-switch-template-edit-device-%s-%s']//span[@class='hp-name' and text()='%s']"
    ID_DROPDOWN_BAY_TYPE_VALUE_FC = "xpath=//*[@id='cic-switch-template-edit-device--%s-%s']//span[@class='hp-name' and text()='%s']"
    ID_BUTTON_ACTIONS_DFRM = "xpath=//*[@id='cic-switchtemplate-actions-dfrm']"
    ID_SELECT_ACTION_EDIT_DFRM = "//li[@id='cic-switchtemplate-edit-action-dfrm']/a"


class _BaseDeleteLogicalInterconnectGroupsElements(object):
    ID_SELECT_ACTION_DELETE = "link=Delete"
    ID_SAS_SELECT_ACTION_DELETE = "//*[@id='cic-switchtemplate-delete-action-dfrm']/a[text()='Delete']"
    ID_DIALOG_DELETE = "id=cic-delete-dialog-prompt"  # dialog
    ID_BUTTON_YES_DELETE = "xpath=//button[.='Yes, delete']"
    ID_BUTTON_CANCEL = "xpath=//button[.='Cancel']"
    ID_TABLE_LIG_DELETED = "xpath=//table/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # lig table list

    # can't be removed, being referenced
    ID_DIALOG_DELETE_ERROR = "id=cic-switch-template-delete-error-dialog"
    ID_TEXT_DELETE_ERROR = "id=cic-switchtemplate-remove-error-msg"
    ID_BUTTON_CLOSE = "xpath=//div[@id='cic-switch-template-delete-error-dialog']//button[.='Close']"

    ID_DIALOG_DELETE_LIG_ERROR = "xpath=//span[@id='cic-delete-error-message']"
    ID_DIALOG_DELETE_LIG_ERROR_RESOLUTION = "xpath=//span[@id='cic-delete-error-resolution']"
    ID_DIALOG_BUTTON_CANCEL = "css=button.hp-cancel"


class DeleteLogicalInterconnectGroupsElements(_BaseDeleteLogicalInterconnectGroupsElements):
    pass


class C7000DeleteLogicalInterconnectGroupsElements(_BaseDeleteLogicalInterconnectGroupsElements):
    pass


class TBirdDeleteLogicalInterconnectGroupsElements(_BaseDeleteLogicalInterconnectGroupsElements):
    pass
