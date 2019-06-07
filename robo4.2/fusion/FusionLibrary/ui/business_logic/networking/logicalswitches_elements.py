# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all elements ID on Fusion Logical Switches sets page/screen
'''
from FusionLibrary.ui.business_logic.base import FusionUIConst


class _BaseGeneralLogicalSwitchesElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Logical Switches']"
    ID_TABLE_LOGICAL_SWITCH = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # Logical Switch name
    ID_TABLE_LOGICAL_SWITCH_LIST = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[1+count(//table[@class='hp-master-table hp-selectable dataTable']//td[text()='Name']//preceding-sibling::*)]"
    ID_TABLE_LOGICAL_SWITCH_SELECTED = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-selected')]/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # Logical Switch name
    ID_TABLE_LOGICAL_SWITCH_NOT_FOUND = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-not-found')]/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # Logical Switch name
    ID_STATUS_LOGICAL_SWITCH_OK = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-ok']"  # Logical Switch name
    ID_STATUS_LOGICAL_SWITCH_WARN = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-warning']"  # Logical Switch name
    ID_STATUS_LOGICAL_SWITCH_ERROR = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-error']"  # Logical Switch name
    ID_BUTTON_ACTIONS = "xpath=//*[text()='Actions']"

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

    # Interconnect settings
    ID_PANEL_INTERCONNECT_SETTINGS = "id=cic-switchtemplate-ethernet-show-switch-settings"
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
    ID_TEXT_SNMP_SYSTEM_CONTACT = "id=cic-snmp-show-system-contact"
    ID_TEXT_SNMP_READ_COMMUNITY = "id=cic-snmp-show-read-community"

    # - Trap Destinations TODO: no plan to support checking 'Severity','VCM','VCM-Enet','VC-FC' options
    ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_DESTINATION = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']"
    ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_COMMUNITY_STRING = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']/../td[2]"
    ID_TEXT_SNMP_TRAP_DESTINATIONS_ROW_FORMAT = "xpath=//table[@id='cic-snmp-trap-forwarding-table']//td[.='%s']/../td[3]"

    # - SNMP Access
    ID_TEXT_SNMP_SNMP_ACCESS_ROW_IP_OR_SUBNET = "xpath=//table[@id='cic-snmp-access-table']//td[.='%s']"

    # Quality of Service
    ID_TEXT_QUALITY_OF_SERVICE_QOS_CONFIGURATION_TYPE = "id=cic-switchtemplate-show-qos"

    ID_DIALOG_LIG_ADD = "id=cic-switchtemplate-add-form"
    ID_OPTION_UPLINK = "xpath=.//*[@id='cic-interconnect-group-qos-edit-container']//*[contains(text(),'Classification for uplinks')]"
    ID_OPTION_DOWNLINK = "xpath =.//*[@id='cic-interconnect-group-qos-edit-container']//*[contains(text(),'Classification for downlinks')]"
    ID_OPTION_RESET = "xpath = .//*[@id='cic-qos-traffic-class-reset-button']"

    # ============
    ID_ELEMENT_SERVER_BASE = "//td[@class='' and text()='%s']"
    ID_WARNING_MSG = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-message']/p/span"
    ID_OVERVIEW_DROPDOWN = "xpath=.//*[@id='cic-torlogicalswitch-panel-selector']/div"
    ID_ILS_OPTION = "link=Internal Link Sets"
    ID_ILS_DATA = "xpath=.//*[@id='cic-torlogicalswitch-general-ils-panel-container']"
    editLSTimeout = 180  # in seconds


class GeneralLogicalSwitchesElements(_BaseGeneralLogicalSwitchesElements):
    pass


class C7000GeneralLogicalSwitchesElements(_BaseGeneralLogicalSwitchesElements):
    pass


class TBirdGeneralLogicalSwitchesElements(_BaseGeneralLogicalSwitchesElements):
    pass


class _BaseCreateLogicalSwitchesElements(object):

    ID_BUTTON_CREATE_LOGICAL_SWITCH = "xpath=//a[text()='Create logical switch']"
    ID_SELECT_ACTIONS_CREATE = "xpath=//*[@id='cic-torlogicalswitch-create-action']/a"
    ID_DIALOG_CREATE_LOGICAL_SWITCH = "xpath=//*[@id='cic-torlogicalswitch-add-form']/ancestor::div[name()='DIV' and position()=1]"
    ID_INPUT_NAME = "xpath=//input[@id='cic-torlogicalswitch-add-name']"
    ID_RADIO_ADD_LOGICAL_SWITCH_AS_MONITORED = "xpath=//input[@id='cic-torlogicalswitch-management-type-monitored']"
    ID_RADIO_ADD_LOGICAL_SWITCH_AS_MANAGED = "xpath=//input[@id='cic-torlogicalswitch-management-type-managed']"
    ID_INPUT_LOGICAL_SWITCH_GROUP = "xpath=//input[@id='cic-torlogicalswitch-add-group-select-input']"
    ID_OPTION_LOGICAL_SWITCH_GROUP = "xpath=//*[@id='cic-torlogicalswitch-add-group-select-input']/following-sibling::*/descendant::span[text()='%s']"  # Logical Switch Group name
    ID_INPUT_SWITCH1_IP_ADDRESS_OR_HOST_NAME = "xpath=//input[@id='cic-torlogicalswitch-add-hostname-switch1']"
    ID_INPUT_SWITCH2_IP_ADDRESS_OR_HOST_NAME = "xpath=//input[@id='cic-torlogicalswitch-add-hostname-switch2']"
    ID_INPUT_SWITCH1_USER_NAME = "xpath=//input[@id='cic-torlogicalswitch-add-username-switch1']"
    ID_INPUT_SWITCH2_USER_NAME = "xpath=//input[@id='cic-torlogicalswitch-add-username-switch2']"
    ID_INPUT_SWITCH1_PASSWORD = "xpath=//input[@id='cic-torlogicalswitch-add-password-switch1']"
    ID_INPUT_SWITCH2_PASSWORD = "xpath=//input[@id='cic-torlogicalswitch-add-password-switch2']"
    ID_INPUT_SWITCH1_SNMP_PORT = "xpath=//input[@id='cic-torlogicalswitch-snmp-port-switch1']"
    ID_INPUT_SWITCH2_SNMP_PORT = "xpath=//input[@id='cic-torlogicalswitch-snmp-port-switch2']"
    ID_SELECT_SWITCH1_SNMP_VERSION = "id=cic-torlogicalswitch-snmp-version-switch1"
    ID_SELECT_SWITCH2_SNMP_VERSION = "id=cic-torlogicalswitch-snmp-version-switch2"
    ID_INPUT_SWITCH1_SNMP_USER_NAME = "xpath=//input[@id='cic-torlogicalswitch-snmp-username-switch1']"
    ID_INPUT_SWITCH2_SNMP_USER_NAME = "xpath=//input[@id='cic-torlogicalswitch-snmp-username-switch2']"
    ID_RADIO_SWITCH1_AUTHORIZATION = "xpath=//input[@id='cic-torlogicalswitch-snmp-authorization-switch1']"
    ID_RADIO_SWITCH2_AUTHORIZATION = "xpath=//input[@id='cic-torlogicalswitch-snmp-authorization-switch2']"
    ID_RADIO_SWITCH1_AUTHORIZATION_AND_PRIVACY = "xpath=//input[@id='cic-torlogicalswitch-snmp-auth_and_priv-switch1']"
    ID_RADIO_SWITCH2_AUTHORIZATION_AND_PRIVACY = "xpath=//input[@id='cic-torlogicalswitch-snmp-auth_and_priv-switch2']"
    ID_SELECT_SWITCH1_AUTHORIZATION_PROTOCOL = "id=cic-torlogicalswitch-snmp-auth_protocol-switch1"
    ID_SELECT_SWITCH2_AUTHORIZATION_PROTOCOL = "id=cic-torlogicalswitch-snmp-auth_protocol-switch2"
    ID_INPUT_SWITCH1_AUTHORIZATION_PASSWORD = "xpath=//input[@id='cic-torlogicalswitch-snmp-auth_pword-switch1']"
    ID_INPUT_SWITCH2_AUTHORIZATION_PASSWORD = "xpath=//input[@id='cic-torlogicalswitch-snmp-auth_pword-switch2']"
    ID_INPUT_SWITCH1_COMMUNITY_STRING = "xpath=//input[@id='cic-torlogicalswitch-snmp-comm_str-switch1']"
    ID_INPUT_SWITCH2_COMMUNITY_STRING = "xpath=//input[@id='cic-torlogicalswitch-snmp-comm_str-switch2']"
    ID_CHECKBOX_SWITCH2_USE_SAME_CREDENTIALS_AS_SWITCH1 = "xpath=//input[@id='cic-torlogicalswitch-switch2-checkbox']"
    # ID_DROPDOWN_TYPE = "xpath=//*[@id='cic-torswitchgroup-add-form']//label[text()='Type']/following-sibling::*//div[contains(@class, 'hp-value')]"
    ID_BUTTON_CREATE = "xpath=//input[@id='cic-torlogicalswitch-add']"
    ID_BUTTON_CREATE_PLUS = "xpath=//input[@id='cic-torlogicalswitch-again']"
    ID_BUTTON_CANCEL = "xpath=//a[@id='cic-torlogicalswitch-add-close']"

    ID_ERROR_CREATE_FAILED = "css=div.hp-details,div.hp-details span"


class CreateLogicalSwitchesElements(_BaseCreateLogicalSwitchesElements):
    pass


class C7000CreateLogicalSwitchesElements(_BaseCreateLogicalSwitchesElements):
    pass


class TBirdCreateLogicalSwitchesElements(_BaseCreateLogicalSwitchesElements):
    pass


class _BaseEditLogicalSwitchesElements(object):
    ID_SELECT_ACTIONS_EDIT = "xpath=//*[@id='cic-torlogicalswitch-edit-action']/a"
    ID_DIALOG_EDIT_LOGICAL_SWITCH = "xpath=//*[@id='cic-torlogicalswitch-edit-form']/../../div[contains(@class, 'dialog')]"
    ID_INPUT_NAME = "xpath=//input[@id='cic-torlogicalswitch-edit-name']"
    ID_RADIO_ADD_LOGICAL_SWITCH_AS_MONITORED = "xpath=//input[@id='cic-torlogicalswitch-management-type-monitored']"
    ID_RADIO_ADD_LOGICAL_SWITCH_AS_MANAGED = "xpath=//input[@id='cic-torlogicalswitch-management-type-managed']"
    ID_ICON_REMOVE_SWITCH = "xpath=//*[@id='cic-torlogicalswitch-switches-table']//td[text()='%s']/following-sibling::td//*[contains(@class, 'hp-close')]"  # switch name
    ID_ICON_EDIT_SWITCH = "xpath=//*[@id='cic-torlogicalswitch-switches-table']//td[text()='%s']/following-sibling::td//*[contains(@class, 'hp-edit')]"  # switch name
    ID_TABLE_EXISTING_SWITCH_LIST = "xpath=//table[@id='cic-torlogicalswitch-switches-table']//td[1+count(//table[@id='cic-torlogicalswitch-switches-table']//th[text()='Host Name']//preceding-sibling::*)]"
    ID_BUTTON_ADD_SWITCH = "xpath=//input[@id='cic-torlogicalswitch-add-switch']"
    ID_DIALOG_EDIT_OR_ADD_SWITCH = "xpath=//div[@id='cic-torlogicalswitch-edit-add-switch-dialog']|//div[@id='cic-torlogicalswitch-edit-switch-dialog']"
    ID_INPUT_SWITCH_IP_ADDRESS_OR_HOST_NAME = "xpath=//input[@id='cic-torlogicalswitch-edit-hostname']|//input[@id='cic-torlogicalswitch-add-hostname']"
    ID_CHECKBOX_USE_SAME_CREDENTIALS_AS_ANOTHER = "xpath=//input[@id='cic-torlogicalswitch-edit-add-use-same-credentials']"
    ID_INPUT_SWITCH_USER_NAME = "xpath=//input[@id='cic-torlogicalswitch-edit-username']|//input[@id='cic-torlogicalswitch-add-username']"
    ID_INPUT_SWITCH_PASSWORD = "xpath=//input[@id='cic-torlogicalswitch-add-password']|//input[@id='cic-torlogicalswitch-edit-password']"
    ID_INPUT_SWITCH_SNMP_PORT = "xpath=//input[@id='cic-torlogicalswitch-snmp-port']"
    ID_SELECT_SWITCH_SNMP_VERSION = "id=cic-torlogicalswitch-snmp-version"
    ID_INPUT_SWITCH_SNMP_USER_NAME = "xpath=//input[@id='cic-torlogicalswitch-snmp-username']"
    ID_RADIO_SWITCH_AUTHORIZATION = "xpath=//input[@id='cic-torlogicalswitch-snmp-authorization']"
    ID_RADIO_SWITCH_AUTHORIZATION_AND_PRIVACY = "xpath=//input[@id='cic-torlogicalswitch-snmp-auth_and_priv']"
    ID_SELECT_SWITCH_AUTHORIZATION_PROTOCOL = "id=cic-torlogicalswitch-snmp-auth_protocol"
    ID_INPUT_SWITCH_AUTHORIZATION_PASSWORD = "xpath=//input[@id='cic-torlogicalswitch-snmp-auth_pword']"
    ID_INPUT_SWITCH_COMMUNITY_STRING = "xpath=//input[@id='cic-torlogicalswitch-snmp-comm_str']"
    ID_BUTTON_OK_FOR_EDIT_OR_ADD_SWITCH = "xpath=//*[@id='cic-torlogicalswitch-edit-switch-dialog-form']//input[@value='OK']|//*[@id='cic-torlogicalswitch-edit-add-switch-form']//input[@value='OK']"
    ID_BUTTON_CANCEL_FOR_EDIT_OR_ADD_SWITCH = "xpath=//*[@id='cic-torlogicalswitch-edit-switch-dialog-form']//input[@value='Cancel']|//*[@id='cic-torlogicalswitch-edit-add-switch-form']//input[@value='Cancel']"
    ID_BUTTON_OK = "xpath=//input[@id='cic-torlogicalswitch-update']"
    ID_BUTTON_CANCEL = "xpath=//input[@id='cic-torlogicalswitch-edit-cancel']"
    ID_ERROR_EDIT_FAILED = "css=div.hp-details,div.hp-details span"


class EditLogicalSwitchesElements(_BaseEditLogicalSwitchesElements):
    pass


class C7000EditLogicalSwitchesElements(_BaseEditLogicalSwitchesElements):
    pass


class TBirdEditLogicalSwitchesElements(_BaseEditLogicalSwitchesElements):
    pass


class _BaseDeleteLogicalSwitchesElements(object):
    ID_SELECT_ACTIONS_DELETE = "xpath=//*[@id='cic-torlogicalswitch-delete-action']/a"
    ID_DIALOG_DELETE_LOGICAL_SWITCH = "xpath=//header//span[contains(text(), 'Delete')]/ancestor::*/div[@class='hp-dialog']"
    ID_LABEL_DELETE = "xpath=//header//span[contains(text(), 'Delete')]"
    ID_LABEL_LOGICAL_SWITCH_NAME = "xpath=//header//span[contains(text(), 'Delete')]/following-sibling::span"
    ID_TEXT_PROMPT_MESSAGE = "xpath=//*[@id='cic-delete-dialog-prompt']"
    ID_BUTTON_YES_DELETE = "xpath=//*[@id='cic-delete-dialog-yes']"
    ID_BUTTON_CANCEL = "xpath=//button[text()='Cancel']"
    ID_LABEL_DELETE_WARNING_MESSAGE = "xpath=//*[@id='cic-delete-warning']"
    ID_LINK_FOR_USED_BY = "xpath=//*[@id='cic-delete-details-tor-switches-label']/span/a"


class DeleteLogicalSwitchesElements(_BaseDeleteLogicalSwitchesElements):
    pass


class C7000DeleteLogicalSwitchesElements(_BaseDeleteLogicalSwitchesElements):
    pass


class TBirdDeleteLogicalSwitchesElements(_BaseDeleteLogicalSwitchesElements):
    pass


class FusionLogicalSwitchPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Logical Switches']"
    CISCO_ID_MENU_LINK_LS = "link=Logical Switches"
    ID_LS_LIST = "xpath=//div[@class='dataTables_scrollBody']/table"
    CISCO_ID_LS_LIST_NAMES = ID_LS_LIST + '/tbody/tr/td[2]'
    CISCO_ID_LINK_CREATE_LS = "link=Create logical switch"
    CISCO_ID_INPUT_LS_NAME = "id=cic-torlogicalswitch-add-name"
    CISCO_LS_ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Logical Switches']"
    CISCO_ID_INPUT_LSG_NAME = "id=cic-torlogicalswitch-add-group-select-input"
    CISCO_ID_LS_SWITCH_IP_1 = "id=cic-torlogicalswitch-add-hostname-switch1"
    CISCO_ID_INPUT_SSH_USER_NAME_1 = "id=cic-torlogicalswitch-add-username-switch1"
    CISCO_ID_INPUT_SSH_PASSWORD_1 = "id=cic-torlogicalswitch-add-password-switch1"
    CISCO_ID_INPUT_SNMP_PORT_1 = "id=cic-torlogicalswitch-snmp-port-switch1"
    CISCO_ID_SNMP_VERSION_DROPDOWN_1 = "//*[@id='cic-torlogicalswitch-add-snmp-section-switch1']/fieldset/ol/li[2]/div/div"
    CISCO_ID_INPUT_SNMP_STRING_1 = "id=cic-torlogicalswitch-snmp-comm_str-switch1"
    CISCO_ID_SNMP_VERSION_DROPDOWN_SELECT_1 = "xpath=//*[@id='cic-torlogicalswitch-add-snmp-section-switch1']/fieldset/ol/li[2]/div/div//span[@class='hp-name' and text()='%s']"
    CISCO_ID_SNMP_SECURITY_NONE_1 = "id=cic-torlogicalswitch-snmp-none-switch1"
    CISCO_ID_SNMP_V3_USER_NAME_1 = "id=cic-torlogicalswitch-snmp-username-switch1"
    CISCO_ID_SNMP_AUTHORIZATION_1 = "id=cic-torlogicalswitch-snmp-authorization-switch1"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_1 = "id=cic-torlogicalswitch-snmp-auth_and_priv-switch1"
    CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_1 = "id=cic-torlogicalswitch-snmp-auth_pword-switch1"
    CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_1 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch1']/ol/li[3]/div/div"
    CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT_1 = "xpath=//*[@id='cic-torlogicalswitch-snmp-v3-section-switch1']/ol/li[3]/div/div//span[@class='hp-name' and text()='%s']"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PASSWORD_1 = "id=cic-torlogicalswitch-snmp-priv_pword-switch1"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_1 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch1']/ol/li[5]/div/div"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_SELECT_1 = "xpath=//*[@id='cic-torlogicalswitch-snmp-v3-section-switch1']/ol/li[5]/div/div//span[@class='hp-name' and text()='%s']"
    CISCO_ID_SNMP_AUTHORIZATION_PROTO_1 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch1']/ol/li[3]/div/div"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_1 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch1']/ol/li[5]/div/div"
    CISCO_ID_LS_SWITCH_IP_SELECT = "id=cic-torlogicalswitch-switch2-checkbox"
    CISCO_ID_LS_SWITCH_IP_2 = "id=cic-torlogicalswitch-add-hostname-switch2"
    CISCO_ID_INPUT_SSH_USER_NAME_2 = "id=cic-torlogicalswitch-add-username-switch2"
    CISCO_ID_INPUT_SSH_PASSWORD_2 = "id=cic-torlogicalswitch-add-password-switch2"
    CISCO_ID_INPUT_SNMP_PORT_2 = "id=cic-torlogicalswitch-snmp-port-switch2"
    CISCO_ID_SNMP_VERSION_DROPDOWN_2 = "//*[@id='cic-torlogicalswitch-add-snmp-section-switch2']/fieldset/ol/li[2]/div/div"
    CISCO_ID_INPUT_SNMP_STRING_2 = "id=cic-torlogicalswitch-snmp-comm_str-switch2"
    CISCO_ID_SNMP_VERSION_DROPDOWN_SELECT_2 = "xpath=//*[@id='cic-torlogicalswitch-add-snmp-section-switch2']//span[@class='hp-name' and text()='%s']"
    CISCO_ID_SNMP_SECURITY_NONE_2 = "id=cic-torlogicalswitch-snmp-none-switch2"
    CISCO_ID_SNMP_V3_USER_NAME_2 = "id=cic-torlogicalswitch-snmp-username-switch2"
    CISCO_ID_SNMP_AUTHORIZATION_2 = "id=cic-torlogicalswitch-snmp-authorization-switch2"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_2 = "id=cic-torlogicalswitch-snmp-auth_and_priv-switch2"
    CISCO_ID_SNMP_AUTHORIZATION_PASSWORD_2 = "id=cic-torlogicalswitch-snmp-auth_pword-switch2"
    CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_2 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch2']/ol/li[3]/div/div"
    CISCO_ID_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT_2 = "xpath=//*[@id='cic-torlogicalswitch-snmp-v3-section-switch2']/ol/li[3]/div/div//span[@class='hp-name' and text()='%s']"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PASSWORD_2 = "id=cic-torlogicalswitch-snmp-priv_pword-switch2"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_2 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch2']/ol/li[5]/div/div"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_SELECT_2 = "xpath=//*[@id='cic-torlogicalswitch-snmp-v3-section-switch2']/ol/li[5]/div/div//span[@class='hp-name' and text()='%s']"
    CISCO_ID_SNMP_AUTHORIZATION_PROTO_2 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch2']/ol/li[3]/div/div"
    CISCO_ID_SNMP_AUTHORIZATION_PRIV_PROTO_2 = "//*[@id='cic-torlogicalswitch-snmp-v3-section-switch2']/ol/li[5]/div/div"
    CISCO_ID_SNMP_V3_NONE_USER = "id=cic-torlogicalswitch-snmp-username"
    CISCO_ID_LSG_DROPDOWN = "//input[@id='cic-torlogicalswitch-add-group-select-input']/following-sibling::div[2]"
    CISCO_ID_LINK_SEARCH_FOR_ANOTHER = "link=Search for another"
    CISCO_ID_ELEMENT_LSG_NAME = "xpath=//span[@class='hp-name' and text()='%s']"  # Replace %s with LSG name
    CISCO_ID_CREATE_LS = "id=cic-torlogicalswitch-add"
    CISCO_ID_CREATE_LS_PLUS = "id=cic-torlogicalswitch-again"
    CISCO_ID_CREATE_LS_CANCEL = "id=cic-torlogicalswitch-add-close"
    CISCO_ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    CISCO_ID_EDIT_LS = "link=Edit"
    CISCO_ID_EDIT_LS_1 = "link=Edit"
    CISCO_ID_EDIT_LS_NAME = "id=cic-torlogicalswitch-edit-name"
    CISCO_ID_EDIT_HOST_NAME = "id=cic-torlogicalswitch-edit-hostname"
    CISCO_ID_EDIT_SSH_USER = "id=cic-torlogicalswitch-edit-username"
    CISCO_ID_EDIT_SSH_PASSWORD = "id=cic-torlogicalswitch-edit-password"
    CISCO_ID_EDIT_SNM_PORT = "id=cic-torlogicalswitch-snmp-port"
    CISCO_ID_EDIT_SNM_STRING = "id=cic-torlogicalswitch-snmp-comm_str"
    CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN = "//*[@id='cic-torlogicalswitch-add-panels']/li[3]/fieldset/ol/li[2]/div/div"
    CISCO_ID_EDIT_SNMP_VERSION_DROPDOWN_SELECT = "xpath=//*[@id='cic-torlogicalswitch-add-panels']//span[@class='hp-name' and text()='%s']"
    CISCO_ID_EDIT_SNMP_SECURITY_NONE = "id=cic-torlogicalswitch-snmp-none"
    CISCO_ID_EDIT_SNMP_V3_USER_NAME = "id=cic-torlogicalswitch-snmp-username"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION = "id=cic-torlogicalswitch-snmp-authorization"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV = "id=cic-torlogicalswitch-snmp-auth_and_priv"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION_PASSWORD = "id=cic-torlogicalswitch-snmp-auth_pword"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PASSWORD = "id=cic-torlogicalswitch-snmp-priv_pword"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN = "//*[@id='cic-torlogicalswitch-snmp-v3-section']/ol/li[3]/div/div"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION_PROTO_DROPDOWN_SELECT = "//*[@id='cic-torlogicalswitch-snmp-v3-section']/ol/li[3]/div/div//span[@class='hp-name' and text()='%s']"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN = "//*[@id='cic-torlogicalswitch-snmp-v3-section']/ol/li[5]/div/div"
    CISCO_ID_EDIT_SNMP_AUTHORIZATION_PRIV_PROTO_DROPDOWN_SELECT = "//*[@id='cic-torlogicalswitch-snmp-v3-section']/ol/li[5]/div/div//span[@class='hp-name' and text()='%s']"
    CISCO_ID_EDIT_OK_MAIN = "id=cic-torlogicalswitch-update"
    CISCO_ID_EDIT_CANCEL_MAIN = "id=cic-torlogicalswitch-edit-cancel"
    CISCO_ID_EDIT_SWITCH_OK = "//*[@id='cic-torlogicalswitch-edit-switch-dialog-form']/div[2]/div[2]/input[1]"
    CISCO_ID_EDIT_SWITCH_CANCEL = "//*[@id='cic-torlogicalswitch-edit-switch-dialog-form']/div[2]/div[2]/input[2]"
    CISCO_ID_EDIT_ADD_SWITCH = "id=cic-torlogicalswitch-add-switch"
    CISCO_ID_EDIT_ADD_SWITCH_OK = "//*[@id='cic-torlogicalswitch-edit-add-switch-form']/div[2]/div[2]/input[1]"
    CISCO_ID_EDIT_ADD_SWITCH_CANCEL = "//*[@id='cic-torlogicalswitch-edit-add-switch-form']/div[2]/div[2]/input[2]"
    CISCO_ID_EDIT_ADD_SWITCH_HOST = "id=cic-torlogicalswitch-add-hostname"
    CISCO_ID_EDIT_USE_SAME_CREDENTIAL = "id=cic-torlogicalswitch-edit-add-use-same-credentials"
    CISCO_ID_EDIT_LS_OK = "id=cic-torlogicalswitch-edit-update"
    CISCO_ID_EDIT_SWITCH_COUNT = "id=cic-torlogicalswitch-edit-switch-number"
    CISCO_ID_EDIT_LS_UPDATE = "link=Update from group"
    CISCO_ID_EDIT_SWITCH_HOST = "id=cic-torlogicalswitch-edit-hostname"
    CISCO_ID_ADD_SSH_USER = "id=cic-torlogicalswitch-add-username"
    CISCO_ID_ADD_SSH_PASSWORD = "id=cic-torlogicalswitch-add-password"
    CISCO_ID_UPDATE_FORM = "id=cic-torlogicalswitch-update-from-group-form"
    CISCO_ID_UPDATE_CONFIRM = "id=cic-torlogicalswitch-update-from-group-confirm"
    CISCO_ID_WARNING_MSG = "xpath =//div[@id='hp-page-notifications']/div/header/div/p/span"
    CISCO_ID_LS_EDIT_COMPLETE = "//header[@class='hp-notification-summary']/div[@class='hp-state' andtext()='Completed']"
    CISCO_ID_LS_EDIT_ERROR = "//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Error']"
    CISCO_ID_LS_EDIT_ERROR_MSG = "xpath = //div[@id='hp-page-notifications']/div[1]/div/div[2]/div/div[1]/p/span"
    CISCO_ID_LS_UPDATE_COMPLETE = "//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Completed']"
    CISCO_ID_LS_EDIT_VERIFY = "id=hp-form-message"
    CISCO_ID_DELETE_LS = "link=Delete"
    CISCO_ID_DELETE_FROM = "id=cic-delete-warning"
    CISCO_ID_DELETE_LS_CONFIRM = "id=cic-delete-dialog-yes"
    CISCO_ID_ELEMENT_SNMP_VERSION = "xpath=//span[@class='hp-name' and text()='%s']"
    CISCO_ID_LS_TYPE = "//*[@id='cic-torlogicalswitch-show-general']/form/fieldset/ol/li[1]/div"
    CISCO_ID_LS_LS_GROUP = "//*[@id='cic-torlogicalswitch-show-general']/form/fieldset/ol/li[2]/div"
    CISCO_ID_LS_STATE = "//*[@id='cic-torlogicalswitch-show-general']/form/fieldset/ol/li[3]/div"
    CISCO_ID_LS_VPC_DMAIN_ID = "//*[@id='cic-torlogicalswitch-show-general']/form/fieldset/ol/li[4]/div"
    CISCO_ID_LS_VPC_PRIMARY_MAC_ID = "//*[@id='cic-torlogicalswitch-show-general']/form/fieldset/ol/li[7]/div"
    CISCO_ID_LS_SWITCH_1 = "//*[@id='cic-torlogicalswitch-show-switches']//tbody/tr[1]"
    CISCO_ID_LS_SWITCH_2 = "//*[@id='cic-torlogicalswitch-show-switches']//tbody/tr[2]"
    CISCO_ID_LS_SWITCH = "//*[@id='cic-torlogicalswitch-show-switches']//tbody/tr[1]"
    CISCO_ID_ELEMENT_SERVER_BASE = "//td[@class='' and text()='%s']"  # Replace %s with LS name
    CISCO_ID_ERROR_POPUP = "//*[@id='hp-form-message']"
    CISCO_ID_ERROR_MSG = "//*[@id='hp-form-message']/div[2]"
    CISCO_ID_TOP_ERROR_MSG = "//div[@id='hp-page-notifications']/div/div"
    CISCO_ID_LS_ADD_MAX_MSG = "//*[@id='cic-torlogicalswitch-add-switch-help']"
    CISCO_ID_ADD_SWITCH_1 = "//*[@id='cic-torlogicalswitch-edit-add-switch-form']/div[2]/div[2]/input[1]"
    CISCO_ID_ADD_SWITCH_2 = "//*[@id='cic-torlogicalswitch-edit-add-switch-form']/div[2]/div[3]/input[1]"
    CISCO_ID_LS_EDIT_WARNING = "//*[@id='hp-page-notifications']/div[1]/header/div[2]/p/span"
    CISCO_ID_LS_EDIT_PAGE_NOTIFICATION = "//*[@id='hp-page-notifications']"
    CISCO_ID_LS_EDIT_PROGRESS_BAR = "//div[@class='hp-progress']"
    CISCO_ID_UPDATE_WRNING = "//*[@id='hp-page-notifications']/div[1]/header/div[2]/p/span"
    CISCO_ID_UPDATE_WRNING_MSG = "//*[@id='hp-page-notifications']/div[1]/div/div[2]/div/div[2]/span"
    CISCO_ID_DELETE_WARNING = "//*[@id='hp-page-notifications']/div[1]/header"
    CISCO_ID_DELETE_WARNING_MSG = "//*[@id='hp-page-notifications']/div[1]/div/div[2]/div"
    CISCO_ID_PROGRESS_BAR = "//div[@class='hp-progress']"
    CISCO_ID_VPC_1 = "//*[@id='cic-torlogicalswitch-stacking-port-data']/tbody/tr[1]"
    CISCO_ID_VPC_2 = "//*[@id='cic-torlogicalswitch-stacking-port-data']/tbody/tr[2]"
    CISCO_ID_NO_LSG_MSG = "//*[@id='hp-dialog-container']"
    CISCO_ID_NO_LSG_CANCEL = "//*[@id='cic-torlogicalswitch-nolsgs-cancel']"
    CISCO_ID_WARNING = "//*[@id='hp-page-notifications']/div[1]/header/div[2]/p/span"
    CISCO_ID_EDIT_SWITCH1_SETTING = "//*[@id='cic-torlogicalswitch-switches-table']/tbody/tr[1]/td[2]/ul/li[1]/div"
    CISCO_ID_EDIT_SWITCH1_REMOVE = "//*[@id='cic-torlogicalswitch-switches-table']/tbody/tr[1]/td[2]/ul/li[2]/div"
    CISCO_ID_EDIT_SWITCH1_SEARCH = "//*[@id='cic-torlogicalswitch-switches-table']/tbody/tr[1]/td[1]"
    CISCO_ID_EDIT_SWITCH2_SETTING = "//*[@id='cic-torlogicalswitch-switches-table']/tbody/tr[2]/td[2]/ul/li[1]/div"
    CISCO_ID_EDIT_SWITCH2_REMOVE = "//*[@id='cic-torlogicalswitch-switches-table']/tbody/tr[2]/td[2]/ul/li[2]/div"
    CISCO_ID_EDIT_SWITCH2_SEARCH = "//*[@id='cic-torlogicalswitch-switches-table']/tbody/tr[2]/td[1]"
    ID_TEXT_LS_STATE = "xpath=.//*[@id='cic-torlogicalswitch-management-type-%s']"
    ID_CHECKBOX_CONFIRM = "xpath=.//*[@id='cic-torlogicalswitch-change-op-state-confirm-checkbox']"
    ID_BUTTON_CONFIRM_OK = "xpath=.//*[@id='cic-torlogicalswitch-change-op-state-confirm-ok']"
