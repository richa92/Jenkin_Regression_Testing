# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''
This file contains all element ID on Fusion logical Interconnect Group  page/screen
'''


class FusionLogicalInterconnectGroupPage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Logical Interconnect Groups']"
    ID_MASTER_PANE = "xpath=//div[contains(@class, 'hp-master-pane')]"
    ID_LINK_CREATE_LOGICAL_INTERCONNECT_GROUPS = "link=Create logical interconnect group"
    ID_CHK_LIG = "//*[@id='cic-switchtemplate-master-table']//td[text()='%s']"
    # ACTION MENU
    ID_MENU_ACTION_LST_DELETE = "link=Delete"
    ID_MENU_ACTION_LST_CREATE = "link=Create"
    ID_MENU_ACTION_LST_EDIT = "link=Edit"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_LIG_LIST_NAMES = "xpath=//table[@id='cic-switchtemplate-master-table']/tbody/tr/td[1]"
    # LIG Table
    ID_LIG_TABLE = "cic-switchtemplate-master-table"

    # CREATE LST PAGE
    ID_INPUT_NAME_LST = "id=cic-switchtemplate-add-name"
    ID_ENCLOSURE_TYPE = "xpath=.//div[@data-id='C7000']"
    ID_ENCLOSURE_LST = "xpath=//li[@data-id='%s']"
    # ID_BTN_ADD_SWITCH_BASE = "id=cic-switch-template-add-switch-%s"  # replace %s with Bay number
    ID_BTN_ADD_SWITCH_BASE = "xpath=//*[@id='cic-switch-template-add-device-1-%s']//div[@class='hp-value']"  # replace %s with Bay number
    # ID_BTN_ADD_SWITCH_BASE = "id=cic-switch-template-add-switch-type-1-%s"  # replace %s with Bay number
    ID_BTN_ADD_SWITCH_2 = "id=cic-switch-template-add-switch-2"
    ID_COMBO_INPUT_SWITCH_TYPE_1 = "id=cic-switch-template-switch-type-1-input"
    ID_COMBO_INPUT_SWITCH_TYPE_BASE = "id=cic-switch-template-switch-type-%s"  # Replace %s with number
    ID_CHECKBOX_FAST_MAC_CACHE_FAILOVER = "cic-switchtemplate-switch-ethernet-add-failover"
    ID_INPUT_MAC_REFRESH_INTERVAL = "cic-switchtemplate-switch-ethernet-add-mac-interval"
    ID_INPUT_IGMP_INTERVAL = "cic-switchtemplate-switch-ethernet-add-igmp-interval"
    ID_CHECKBOX_LOOP_PROTECTION = "cic-switchtemplate-switch-ethernet-add-loop"
    ID_FIELD_LOOP_PROTECTION_INTERVAL = "cic-switchtemplate-switch-ethernet-add-loop-interval"
    ID_COMBO_SWITCH_BASE = "xpath=.//*[@id='cic-switch-template-add-device-1-%s']/div[2]/fieldset/ol/li/div/div/div/ol/li/span[contains(text(),'%s')]"
    # ID_COMBO_SWITCH_BASE = "xpath=//*[@id='cic-switch-template-switch-type-1-%s']"
    ID_BTN_DELETE_LST_CONFIRM = "id=cic-delete-dialog-yes"
    # ID_ELEMENT_VC_MODULE_BASE = "xpath=//select[@id='cic-switch-template-switch-type-%s']/following-sibling::div[3]/ol/li/span[text()='%s']"  # Replace first %s bay number and second wtih VC Module
    # ID_ELEMENT_VC_MODULE_BASE = "xpath=//*[@id='cic-switch-template-switch-type-1']/option[text()='HP Virtual Connect Flex10/10D Module']"
    ID_ELEMENT_VC_MODULE_BASE = "xpath=//*[@id='cic-switch-template-add-switch-type-1-%s']/option[text()='%s']"  # Replace first %s bay number and second wtih VC Module
    ID_BTN_CREATE_PLUS_LST = "id=cic-switchtemplate-again"
    ID_BTN_CREATE_LST = "id=cic-switchtemplate-add"
    ID_BTN_CANCEL_LST = "id=cic-switchtemplate-add-close"
    ID_ELEMENT_LIG_SELECT_NAME = "xpath=//td[text()='%s']"
    ID_ELEMENT_UPDATE_LIG = "id=cic-switchtemplate-update"

    # added for edit LIG
    # ADD lOGICAL UPLINK SET WHILE EDITING LIG
    ID_BTN_ADD_LOGICAL_UPLINK_SET_EDIT_LIG = "id=cic-switch-template-edit-uplink-button"
    # MODIFIED
    ID_CHKBOX_NATIVE_BASE = "xpath=//tr[descendant::td[contains(.,'%s')]]//input[@type='checkbox']"  # %s replace with native network name
    # #####
    ID_CHKBOX_FAILOVER_PREFERRED_PORT = "xpath=//tr[descendant::td[contains(.,'%s')] and td[contains(.,'%s')]  ] //input[@type='checkbox']"
    ID_BTN_ADD_UPLINK_PORTS = "id=cic-switchtemplate-dialog-uplinks-addUplinks"
    # ID_SELECT_TABLE_ADD_PORT="xpath=//*[@id='hp-add-choices']/tbody/tr/td[text()='1']/following-sibling::td[text()='X5']"
    # FUSION 1.05: ID_SELECT_TABLE_ADD_PORT = "xpath=//*[@id='hp-add-choices']/tbody/tr/td[text()='%s']/following-sibling::td[text()='%s']"
    ID_SELECT_TABLE_ADD_PORT = "xpath=//table/tbody/tr/td[text()='%s']/following-sibling::td[text()='%s']"
    ID_SEARCH_INPUT_UPLINK_PORT = "css=input.hp-search"
    # ADD SWITCH WHILE EDITING LIG
    ID_BTN_ADD_SWITCH_EDIT_LIG_BASE = "id=cic-switch-template-edit-switch-%s"  # replace %s with Bay number
    ID_INPUT_EDIT_NAME_LIG = "id=cic-switchtemplate-edit-name"
    ID_BTN_EDIT_LIG_OK = "cic-switchtemplate-update"
    # ADDED FOR FC UPLINK SET
    ID_FC_INTERCONNECT_LIST = "xpath=//ol[@id='cic-switch-template-dialog-uplinks']//div[@class='hp-search-combo hp-active']"
    ID_FC_INTERCONNECT_LIST_CONTROL = "xpath=//input[@id='cic-switchtemplate-dialog-fc-switch-input']/following-sibling::div[@class='hp-search-combo-control']"
    ID_FC_INTERCONNECT = "xpath=//ol[@id='cic-switch-template-dialog-uplinks']//li/span[text()='%s']"
    ID_INPUT_FC_NETWORK = "id=cic-switchtemplate-dialog-fc-addNetwork-input"
    ID_INPUT_FC_SWITCH = "id=cic-switchtemplate-dialog-fc-switch-input"
    ID_CHKBOX_BASE = "//input[@id='%s']"

    # REMOVE UPLINK SET
    ID_BTN_REMOVE_UPLINK_SET_BASE = "id=cic-switchtemplate-delete-uplink-link-%s"

    # LINK FOR DIV EXAMPLE SNMP,TRAP, INTERCONNECT ETC

    # ID_LINK_SNMP = "css=div.hp-value"
    ID_SELECT_BASE = "link=%s"
    # ADD INTERCONNECT SETTINGS
    ID_CHKBOX_ADD_FAST_MAC_CACHE_FAILOVER = "id=cic-switchtemplate-switch-ethernet-add-failover"
    ID_INPUT_ADD_MAC_REFRESH_INTERVAL = "id=cic-switchtemplate-switch-ethernet-add-mac-interval"
    ID_CHKBOX_ADD_IGMP_SNOOPING = "id=cic-switchtemplate-switch-ethernet-add-snooping"
    ID_INPUT_ADD_IGMP_IDLE_TIMEOUT_INTERVAL = "id=cic-switchtemplate-switch-ethernet-add-igmp-interval"
    ID_CHKBOX_ADD_LOOP_PROTECTION = "id=cic-switchtemplate-switch-ethernet-add-loop"

    # EDIT INTERCONNECT SETTINGS
    ID_CHKBOX_FAST_MAC_CACHE_FAILOVER = "id=cic-switchtemplate-switch-ethernet-edit-failover"
    ID_INPUT_MAC_REFRESH_INTERVAL = "id=cic-switchtemplate-switch-ethernet-edit-mac-interval"
    ID_CHKBOX_IGMP_SNOOPING = "id=cic-switchtemplate-switch-ethernet-edit-snooping"
    ID_INPUT_IGMP_IDLE_TIMEOUT_INTERVAL = "id=cic-switchtemplate-switch-ethernet-edit-igmp-interval"
    ID_CHKBOX_LOOP_PROTECTION = "id=cic-switchtemplate-switch-ethernet-edit-loop"

    # UTILIZATION SAMPLING
    ID_INPUT_INTERVAL_BETWEEN_SAMPLES = "id=cic-switchtemplate-switch-edit-interval"
    ID_INPUT_TOTAL_NO_SAMPLES = "id=cic-switchtemplate-switch-edit-samples"

    # SNMP
    ID_OPTION_SNMP_ENABLE_DISABLE = "css=li.hp-on"  # PASS on for ENABLE and off for DISABLE
    ID_INPUT_SYSTEM_CONTACT = "id=cic-snmp-general-system-contact"
    ID_INPUT_READ_COMMUNITY = "id=cic-snmp-general-read-community"

    # SNMP ACCESS
    ID_INPUT_TEXT_SNMP_ACCESS = "id=cic-snmp-add-access-address"
    ID_OK_SNMP_ADDRESS = "id=cic-snmp-access-ok-button"
    ID_DELETE_SNMP = "css=footer > div.hp-controls > button.hp-ok.hp-primary"
    ID_BTN_ADD_SNMP_ACCESS = "id=cic-snmp-general-add-snmp-access"
    ID_ADD_SNMP_ADDRESS = "id=cic-snmp-access-add-button"
    ID_SNMP_PATH = "xpath=//td[text()='%s']"  # %s replace with snmp ip
    ID_SNMP_DELETE_PATH = "xpath=//tr[descendant::td[contains(.,'%s')]]//td[@class='hp-icon']/div[@class='hp-close']"  # %s will be replace with name of the snamp
    ID_SNMP_EDIT_PATH = "xpath=//tr[descendant::td[contains(.,'%s')]]//td[@class='hp-icon']/div[@class='hp-edit']"

    # Traps
    ID_LINK_SNMP = "css=div.hp-value"
    ID_SELECT_SNMP = "link=SNMP"
    ID_BTN_ADD_TRAPS = "cic-snmp-general-add-trap-destination"
    ID_TXT_INPUT_TRAP = "cic-snmp-trap-destination-trap-destination"
    ID_COMMUNITY_STRING = "cic-snmp-trap-destination-community-string"
    ID_DELETE_TRAP = "xpath=//tr[descendant::td[contains(.,'%s')]]//td[@class='hp-icon']/div[@class='hp-close']"
    ID_SELECT_DROP_DOWN_VCFC = "xpath= .//div[@id='cic-snmp-trap-destination-vcfc-content']//div[@class='hp-collapsible hp-collapsed']//label[@class='hp-unset']"
    ID_SELECT_DROP_DOWN_VCENET = "xpath= .//div[@id='cic-snmp-trap-destination-vcenet-content']//div[@class='hp-collapsible hp-collapsed']//label[@class='hp-unset']"
    ID_SELECT_DROP_DOWN_SEVERITY = "xpath= .//div[@id='cic-snmp-trap-destination-severity-content']//div[@class='hp-collapsible hp-collapsed']//label[@class='hp-unset']"
    ID_SELECT_DROP_DOWN_VCM = "xpath=.//div[@id='cic-snmp-trap-destination-vcmtraps-content']//div[@class='hp-collapsible hp-collapsed']//label[@class='hp-unset']"
    ID_TRAP_PATH = "xpath=//td[text()='%s']"  # %s will be replaced with IP of the trap
    ID_TRAP_FORMAT = "xpath=.//*[@id='cic-snmp-trap-destination-trapformat-content']/input[@value='%s']"
    ID_SELECT_TRAP_SEVERITY = "xpath=.//div[@id='cic-snmp-trap-destination-severity-content']//div[@class='hp-collapsible']/ol//li/input[@value='%s']"  # %s will be replace with the severity
    ID_SELECT_TRAP_VCENET = "xpath=.//div[@id='cic-snmp-trap-destination-vcenet-content']//div[@class='hp-collapsible']/ol//li//input[@value='%s']"  # %s will be repalce with vcenet
    ID_SELECT_TRAP_VCFC = "xpath=.//div[@id='cic-snmp-trap-destination-vcfc-content']//div[@class='hp-collapsible']/ol//li//input[@value='%s']"  # %s will be reaplaced with vcfc
    ID_SELECT_TRAP_VCM = "xpath= .//div[@id='cic-snmp-trap-destination-vcmtraps-content']//div[@class='hp-collapsible']/ol/li/input[@value='%s']"  # %s will be replaced with vcm
    ID_ADD_TRAP = "id=cic-snmp-trap-destination-add-button"
    ID_EDIT_TRAP_BUTTON = "id=cic-snmp-trap-destination-ok-button"
    ID_EDIT_TRAP_SEVERITY_STATUS = "id=cic-snmp-trap-destination-severity-status"
    ID_EDIT_TRAP_VCM_STATUS = "id=cic-snmp-trap-destination-vcmtraps-status"
    ID_EDIT_TRAP_VCNET_STATUS = "id=cic-snmp-trap-destination-vcenet-status"
    ID_EDIT_TRAP_VCFC_STATUS = "id=cic-snmp-trap-destination-vcfc-status"
    ID_LUS_TYPE = "id=cic-switchtemplate-dialog-edit-type"
    # ################
    # ADD LOGICAL UPLINK TEMPLATE
    ID_BTN_ADD_LOGICAL_UPLINK_TEMPLATE = "id=cic-add-uplink-li"
    ID_INPUT_UPLINK_NAME = "id=cic-switchtemplate-dialog-name"
    ID_RADIO_ETHERNET = "id=cic-switchtemplate-dialog-ethernet-type"
    ID_RADIO_AUTO_CONNECTION_MODE = "id=cic-switchtemplate-dialog-auto-conntype"
    ID_RADIO_FAILOVER_CONNECTION_MODE = "id=cic-switchtemplate-dialog-fail-conntype"
    ID_BTN_ADD_NETWORK_UPLINK_PAGE = "id=cic-switchtemplate-dialog-networks-addNetworks"
    ID_BTN_REMOVE_ALL_NETWORK = "id=cic-switchtemplate-dialog-networks-removeAll"
    ID_BTN_ADD_NETWORK_ADD_PLUS = "css=button.hp-add-again"
    ID_RADIO_NETWORK_TYPE = "cic_switchtemplate_dialog_type"
    ID_BTN_ADD_UPLINK_PORTS_PAGE = "cic-switchtemplate-dialog-uplinks-addUplinks"
    ID_NETWORK_CHOICES_LIST = "//table[@id='hp-add-choices']"
    ID_BTN_ADD_NETWORK_ADD = "css=button.hp-add"
    ID_BTN_ADD_NETWORK_CANCEL = "css=button.hp-cancel"
    ID_ELEMENT_NETWORK_NAME_BASE = "//td[@class=' sorting_1' and text()='%s']"

    # EDIT UPLINK SET
    ID_BTN_EDIT_UPLINK_SET_BASE = "id=cic-switchtemplate-edit-link-%s"
    ID_BTN_ADDEDIT_UPLINK_SET_BASE = "id=cic-switchtemplate-add-link-%s"
    ID_ELEMENT_DELETE_NETWORK_LOGICAL_UPLINK = "xpath=//tr[descendant::td[contains(.,'%s')]]//div[@class='hp-close crm-delete-row']"
    ID_ELEMENT_UPLINK_NETWORK_NAME = "xpath=//td[text()='%s']"
    ID_ELEMENT_UPLINK_NETWORK_ADD_CANCEL = "xpath=//button[text()='Cancel']"
    ID_CHECKBOX_NATIVE_NETWORK_UPLINK = "xpath=//tr[descendant::td[contains(.,'%s')]]//input[@type='checkbox']"
    ID_ELEMENT_DELETE_PORT_UPLINK = "xpath=//tr[descendant::td[contains(.,'%s')] and td[contains(.,'%s')]  ] //div[@class='hp-close crm-delete-row']"
    ID_BTN_ADD_NETWORK_EDIT_UPLINK_ADD_NETWORK = "xpath=//button[text()='Add']"
    ID_COMBO_DROPDOWN_UPLINK_SET = "xpath=//input[@id='cic-switchtemplate-dialog-fc-addNetwork-input']//..//div[@class='hp-search-combo-control']"
    ID_ELEMENT_COMBO_DROPDOWN_UPLINK_SET = "xpath=//li/span[text()='%s']"
    ID_ELEMENT_EDIT_EDIT_PAGE_LABEL = "xpath=//label[text()='Logical Interconnect Group']"
    ID_LINK_LIG_EDIT = "xpath=//div[@id='cic-switchtemplate-panel-edit-selector']"
    ID_SELECT_LIG_EDIT = "link=Logical Interconnect Group"
    ID_UPLINK_SET_NAME_BASE = "xpath=//li/div/label/div[text()='%s']"

    # ID_CHKBOX_NATIVE_BASE = "//td[text()='%s']/following-sibling::td/input[@class='cic-uplinkportgroup-native-network']"  # %s replace with Vlan ID
    ID_BTN_CREATE_PLUS_LOGICAL_UPLINK_TEML = "id=cic-switchtemplate-dialog-add-again"
    ID_BTN_CREATE_LOGICAL_UPLINK_TEML = "id=cic-switchtemplate-dialog-add"
    ID_BTN_CANCEL_LOGICAL_UPLINK_TEML = "css=a.hp-button.hp-cancel"
    ID_ELEMENT_UPLINK_PORTS_BASE = "xpath=//td[test()='%s']"  # replace %s with uplink port name
    ID_BTN_ADD_PLUS_UPLINK_PORT = "css=button.hp-add-again"
    ID_BTN_ADD_UPLINK_PORT = "css=button.hp-add"
    ID_BTN_CANCEL_UPLINK_PORT = "css=a.hp-button.hp-cancel"
    # FC add
    ID_RADIO_FIBERCHANNEL = "id=cic-switchtemplate-dialog-storage-type"
    ID_COMBO_FIBER_CHANNEL_NETWORK = "xpath=//select[@id='cic-witchtemplate-dialog-fc-addNetwork']/following-sibling::div[2]"
    ID_COMBO_FIBER_CHANNEL_SWITCH = "xpath=//select[@id='cic-switchtemplate-dialog-fc-switch']/following-sibling::div[2]"
    ID_CHKBOX_X = "//input[@id='%s']"
    ID_CHKBOX_X1 = "//input[@id='X1']"
    ID_CHKBOX_X2 = "//input[@id='X2']"
    ID_CHKBOX_X3 = "//input[@id='X3']"
    ID_CHKBOX_X4 = "//input[@id='X4']"
    # LIST LST
    ID_LST_ELEMENT_BASE = "xpath=//td[@class='' and text()='%s']"  # replace %s with LST Name

    # View
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_LOGICAL_INTERCONNECT_GROUP = "link=Logical Interconnect Group"
    ID_LINK_INTERCONNECT_SETTINGS = "link=Interconnects Settings"

    ID_LINK_GENERAL = "link=General"

    # DELETE LIG VALIDATIONS
    ID_POPUP_DELETE_LIG_ERROR = "xpath=//span[@id='cic-delete-error-message']"
    ID_POPUP_DELETE_LIG_ERR_RESOLUTION = "xpath=//span[@id='cic-delete-error-resolution']"
    ID_POPUP_BTN_CANCEL = "css=button.hp-cancel"

    ID_LUS_SELECT_TO_ADD_EDIT = "xpath=//li[descendant::div/label/div[text()='%s']]/div[@class='hp-controls']/div[@name='cic-switch-template-uplink-edit-add']"
    ID_LUS_SELECT_TO_DELETE = "xpath=//li[descendant::div/label/div[text()='%s']]/div[@class='hp-controls']/div[@name='cic-switch-template-uplink-edit-delete']"
    ID_LUS_SELECT_TO_EDIT_LABEL = "xpath=//li[descendant::div/div[text()='%s']]/div[@class='hp-controls']/div[@name='cic-switch-template-uplink-edit-edit']"
    ID_LUS_SELECT_TO_EDIT_DIV = "xpath=//li[descendant::label[text()='%s']]/div[@class='hp-controls']/div[@name='cic-switch-template-uplink-edit-edit']"
    ID_ELEMENT_COMBO_FC_UPLINK_SET_PORT = "xpath=//li/span[text()='interconnect: %s']"

    ID_BUTTON_REMOVE_UPLINK_SET_NAME_DIV = "xpath=.//li[descendant::div[text()='%s']]/div[@class='hp-controls']/div[@class='hp-close cic-uplink-delete-button']"
    ID_BTN_REMOVE_UPLINK_SET_NAME = "xpath=.//li[descendant::div//label//div[text()='%s']]/div/div[@class='hp-close']"
    ID_LIG_PAGE_TITLE = "xpath=//h1[text()='%s']"
    ID_UPLINK_LIST = "xpath = //label[text()='Type']/following-sibling::div/div/div"
    ID_ETHERNET_UPLINK = "xpath = //li[@data-id='Ethernet']/span[text()='Ethernet']"
    ID_FC_UPLINK = "xpath = //li[@data-id='FibreChannel']/span[text()='Fibre Channel']"
    ID_LACP_SHORT_TIMER = "xpath = //div[text()='Short (1s)']"
    ID_LACP_LONG_TIMER = ID_LACP_SHORT_TIMER + "/following-sibling::ol/li/span[text()='Long (30s)']"
    ID_LIST_FC_UPLINK_NETWORKS = "xpath=//input[@id='cic-switchtemplate-dialog-fc-addNetwork-input']//..//div[@class='hp-search-combo-control']"
    ID_FC_UPLINK_NETWORK = "xpath=//li/span[text()='%s']"
    ID_LIST_FC_UPLINK_PORTS = "xpath=//input[@id='cic-switchtemplate-dialog-fc-switch-input']/following-sibling::div[@class='hp-search-combo-control']"
    ID_FC_UPLINK_PORT = "//li/span[text()='enclosure: 1, interconnect: %s']"
    ID_LINK_RESET = "link=Reset"

    # NEW
    ID_INPUT_NAME_LST = "id=cic-switchtemplate-add-name"
    ID_LIG_ADD_PANEL_SELECTOR = "id=cic-switchtemplate-panel-add-selector"
    ID_LIG_EDIT_PANEL_SELECTOR = "id=cic-switchtemplate-panel-edit-selector"
    ID_LIG_SYSTEM_CONTACT = "id=cic-snmp-general-system-contact"
    ID_LIG_READ_COMMUNITY = "id=cic-snmp-general-read-community"
    ID_LIG_ADD = "cic-switchtemplate-add-form"
    ID_LIG_EDIT = "cic-switchtemplate-edit-form"
    XPATH_LIG_NAME = "//*[@id='cic-switchtemplate-master-table']//*[text()='%s']"
    ID_LIG_EDIT_NAME = "id=cic-switchtemplate-edit-name"
    ID_LIG_EDIT_FORM_OK = "id=cic-switchtemplate-update"
    ID_LIG_EDIT_CANCEL = "id=cic-switchtemplate-edit-cancel"
    XPATH_LIG_EDIT_TRAP = "xpath=//*[@id='cic-snmp-trap-forwarding-table-container']//*[text()='%s']//following-sibling::*/*[@class='hp-edit']"
    XPATH_LIG_REMOVE_TRAP = "xpath=//*[@id='cic-snmp-trap-forwarding-table-container']//*[text()='%s']//following-sibling::*/*[@class='hp-close']"
    XPATH_LIG_REMOVE_TRAP_OK = "xpath=//*[@class='hp-ok hp-primary' and text()='Yes, remove']"
    ID_LIG_TRAP_EDIT_OK = "id=cic-snmp-trap-destination-ok-button"
    XPATH_LIG_TRAP_CANCEL = "xpath=//*[@id='cic-snmp-trap-destination-form']//*[@class='hp-button hp-cancel']"

    # INTERCONNECT SETTINGS
    ID_LIG_INTERCONNECT_SETTINGS = "id=cic-switchtemplate-switch-ethernet-add-switch-settings"
    ID_CHKBOX_IGMPSNOOPING = "id=cic-switchtemplate-switch-ethernet-add-snooping"
    ID_INPUT_IGMP_IDLETTIMEOUTINTERVAL = "id=cic-switchtemplate-switch-ethernet-add-igmp-interval"
    XPATH_LOOPPROTECTION_CHECKBOX = "id=cic-switchtemplate-switch-ethernet-add-loop"
    ID_EDIT_LIG_INTERCONNECT_SETTINGS = "id=cic-switchtemplate-switch-ethernet-edit-switch-settings"
    ID_EDIT_LIG_CHKBOX_IGMPSNOOPING = "id=cic-switchtemplate-switch-ethernet-edit-snooping"
    ID_EDIT_LIG_INPUT_IGMP_IDLETTIMEOUTINTERVAL = "id=cic-switchtemplate-switch-ethernet-edit-igmp-interval"
    XPATH_EDIT_LIG_LOOPPROTECTION_CHECKBOX = "id=cic-switchtemplate-switch-ethernet-edit-loop"
    ID_LIG_PANEL_SELECTOR = "id=cic-switchtemplate-panel-selector"
    LINK_LIG_GENERAL = "link=General"
    LINK_LIG_INTERNAL_NETWORKS = "link=Internal Networks"
    LINK_LIG_UPLINKSETS = "link=Uplink Sets"
    LINK_LIG_INTERCONNECT_SETTINGS = "link=Interconnect settings"
    LINK_LOGICAL_INTERCONNECT_GROUP = "link=Logical Interconnect Group"
    LINK_UTILIZATION_SAMPLING = "link=Utilization Sampling"
    LINK_LIG_SNMP = "link=SNMP"
    ID_LIG_INTERCONNECT_SETTINGS_DATA = "id=cic-switchtemplate-ethernet-show-switch-settings"
    ID_LIG_GENERAL_DATA = "id=cic-switchtemplates-general"
    ID_LIG_INTERNAL_NETWORKS_DATA = "id=cic-switchtemplates-internal-networks"
    ID_LIG_UPLINK_SETS_DATA = "id=cic-switchtemplates-show-uplink-data"
    ID_LIG_SNMP_SETTINGS_DATA = "id=cic-switchtemplate-show-snmp-settings"
    ID_LIG_SWITHC_TEMPLATE_DATA = "id=cic-switchtemplates-show-switch-template-data"
    ID_LIG_UTILIZATION_SAMPLING_DATA = "id=cic-switchtemplates-switch-utilization-sampling-data"
    ID_LIG_SHOW_INTERVAL_BETWEEN_SAMPLES = "id=cic-switchtemplate-show-interval"
    ID_LIG_SHOW_TOTALSAMPLES = "id=cic-switchtemplate-show-samples"
    XPATH_LIG_SHOW_SNMP_ACCESS = "xpath=//*[@id='cic-snmp-access-table']//*[text()='%s']"
    ID_LIG_ENCLOSURE_TYPE = "id=cic-switchtemplate-show-enclosure-type"
    ID_LIG_REDUNDANCY_INFO = "id=cic-switchtemplate-general-redundancy-info-choice"
    XPATH_LIG_TBIR_SHOW_ENCLOSURE_INDEX = "xpath=//*[@id='cic-switch-template-show-switches']//*[text()='Enclosure %s']"
    ID_TBIRD_SHOW_INTERCONNECT_BAY = "xpath=//*[@id='cic-switch-template-show-switches']//*[@id='cic-switch-template-show-device-name-%s-%s']"
    ID_TBIRD_SHOW_DROP_DOWN_OPTIONS = "xpath =//*[@id='cic-switch-template-add-device-%s-%s']//li//li[span[contains(text(), '%s')]]"
    ID_SHOW_IGMP_SNOOPING = "id=cic-switchtemplate-ethernet-show-snooping"
    ID_SHOW_IGMP_INTERVAL = "id=cic-switchtemplate-ethernet-show-igmp-interval"
    ID_SHOW_LOOP_PROTECTION = "id=cic-switchtemplate-ethernet-show-loop"
    ID_SHOW_MAC_CACHE_FAILOVER = "id=cic-switchtemplate-ethernet-show-failover"
    ID_SHOW_MAC_REFRESH_INTERVAL = "id=cic-switchtemplate-ethernet-show-mac-interval"
    ID_SHOW_PAUSE_FLOOD_PROTECTION = "id=cic-switchtemplate-ethernet-show-pause-flood"
    ID_SHOW_READ_COMMUNITY = "id=cic-snmp-show-read-community"
    ID_SHOW_SYSTEM_CONTACT = "id=cic-snmp-show-system-contact"
    XPATH_SHOW_INTERNAL_NETWORK = "xpath=//*[@id='cic-switchtemplates-internal-networks-container']//a[text()='%s']"
    ID_NO_INTERNAL_NETWORKS_MSG = "id=cic-switchtemplates-internal-networks-no-networks-msg"
    XPATH_SHOW_TRAP_DESTINATION = "xpath=//*[@id='cic-snmp-trap-forwarding-table']//*[text()='%s']"
    XPATH_TRAP_FORMAT_COMMUNITY_STRING = "xpath=//*[@id='cic-snmp-trap-forwarding-table']//*[text()='%s']/following-sibling::*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    XPATH_SHOW_UPLINK_SETS = "xpath=//*[@id='cic-switchtemplates-show-uplink-data']//*[@class='cic-uplink-set-panel-name' and text()='%s']"
    ID_LUS_SELECT_TO_ADD_EDIT = "xpath=//li[descendant::div/label/div[text()='%s']]/div[@class='hp-controls']/div[@name='cic-switch-template-uplink-edit-add']"
    ID_LUS_SELECT_TO_DELETE = "xpath=//li[descendant::div/label/div[text()='%s']]/div[@class='hp-controls']/div[@name='cic-switch-template-uplink-edit-delete']"
    ID_LUS_SELECT_TO_EDIT_LABEL = "xpath=//*[@id='cic-switch-template-edit-uplinks']//*[text()='%s']/following-sibling::*/*[@class='hp-edit cic-uplink-edit-button']"
    ID_LUS_SELECT_TO_EDIT_DIV = "xpath=//li[descendant::label[text()='%s']]/div[@class='hp-controls']/div[@name='cic-switch-template-uplink-edit-edit']"
    ID_LIG_SWITCH_TEMPLATE_DIALOG_FORM = "id=cic-switchtemplate-dialog-form"
    ID_LUS_TYPE_VERIFY = "id=cic-switchtemplate-dialog-edit-type"
    XPATH_LACP_TIMER_VERIFY = "xpath=//*[@id='cic-switchtemplate-dialog-lacp-timer']//*[@class='hp-value']"
    XPATH_NETWORK_VERIFY = "xpath=//*[@id='cic-switchtemplate-dialog-network-assigned']//*[text()='%s']"
    XPATH_NATIVE_NETWORK_VERIFY = "xpath=//*[@id='cic-switchtemplate-dialog-network-assigned']//*[text()='%s']//following-sibling::*/*[@class='cic-uplinkportgroup-native-network']"
    XPATH_BAY_PORT_VERIFY = "xpath=//*[@id='cic-switchtemplate-dialog-port-assigned']//*[text()='%s']//following-sibling::*[text()='%s']"
    XPATH_LUS_CANCEL = "xpath=//*[@class='hp-form-controls']/a[@class='hp-button hp-cancel']"

    # VErify xpaths
    XPATH_LIG_C7000_SHOW_INTERCONNECTS = "//*[@id='cic-switch-template-show-device-1-%s']//*[text()='%s']"

    # new xpaths - TBIRD
    LIG_REDUNDANCY = {'REDUNDANT': 'Redundant', 'HA': 'HighlyAvailable', 'NRA': 'NonRedundantASide', 'NRB': 'NonRedundantBSide'}
    IC_TYPE = {'K': 'VC SE 40Gb F8 Module', 'CL-20': 'HP Synergy 20Gb Interconnect Link Module', 'CL-10': 'HP Synergy 10Gb Interconnect Link Module'}  # new name changes
    # IC_TYPE = {'K': 'HP FlexFabric 40GbE Module - EdgeSafe/Virtual Connect version', 'CL-20': 'HP FlexFabric 20GbE Expansion Module', 'CL-10': 'HP FlexFabric 10GbE Expansion Module'} # old values
    TIMEOUT = 10  # in minutes
    UPDATE_WAIT_TIME = 15  # in seconds
    BAY_SET_MEMBER_INCREMENT = 3
    ENCLOSURE_TYPE_TBIRD = "SY12000"
    ENCLOSURE_TYPE_C7000 = "c7000"

    ID_LIG_ADD_FORM = "id=cic-switchtemplate-add-form"
    ID_LIG_EDIT_FORM = "id=cic-switchtemplate-edit-form"
    ID_ENCLOSURE_INDEX = "xpath=//*[@id='cic-switch-template-add-switches']//*[text()='Enclosure %s']"

    ID_INTERCONNECT_BAY = "xpath=//*[@id='cic-switch-template-add-switches']//*[@id='cic-switch-template-add-device-%s-%s']//div[@class='hp-select']"
    ID_DROP_DOWN_OPTIONS = "xpath =//*[@id='cic-switch-template-add-device-%s-%s']//*[@class='hp-options']//*[contains(text(), '%s')]"
    XPATH_ADD_INTERCONNECT_SECOND_BAYSET_MEMBER = "xpath=//*[@id='cic-switch-template-add-switches']//*[@id='row-%s-2']"

    ID_LIG_EDIT_ENCLOSURE_INDEX = "xpath=//*[@id='cic-switch-template-edit-switches']//*[text()='Enclosure %s']"
    ID_LIG_EDIT_INTERCONNECT_BAY = "xpath=//*[@id='cic-switch-template-edit-switches']//*[@id='cic-switch-template-edit-device-%s-%s']//div[@class='hp-select']"
    ID_LIG_EDIT_DROP_DOWN_OPTIONS = "xpath =//*[@id='cic-switch-template-edit-device-%s-%s']//*[@class='hp-options']//*[contains(text(), '%s')]"
    XPATH_EDIT_INTERCONNECT_SECOND_BAYSET_MEMBER = "xpath=//*[@id='cic-switch-template-edit-switches']//*[@id='row-%s-2']"

    XPATH_LIG_TABLE_ELEMENT = "xpath=//*[@id='cic-switchtemplate-master-table']//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    ID_ADD_LIG = "id=cic-switchtemplate-add-lig-tbird"

    ID_ENC_COUNT = "xpath=.//*[@id='cic-switchtemplate-add-enclosure-count']//div[@class='hp-value']"
    ID_ENC_COUNT_SELECT = "xpath=.//*[@id='cic-switchtemplate-add-enclosure-count']//li[@data-id=%s]"
    ID_IBS = "xpath=.//*[@id='cic-switchtemplate-add-interconnect-bay-set']//div[@class='hp-value']"
    ID_IBS_SELECT = "xpath=.//*[@id='cic-switchtemplate-add-interconnect-bay-set']//li[@data-id=%s]"
    ID_REDUNDANCY = "xpath=.//*[@id='cic-switchtemplate-add-redundancy']//div[@class='hp-value']"
    ID_REDUNDANCY_SELECT = "xpath=.//*[@id='cic-switchtemplate-add-redundancy']//li[@data-id='%s']"
    ID_SELECT_INTERCONNECT = "//li[@id='cic-switchtemplate-add-select-interconnects']/div/input[@id='cic-switchtemplate-add-select-interconnects']"
    ID_ADD_SWITCH = "id=cic-switch-template-add-switches"

    # internal network
    XPATH_LIG_INTERNAL_NETWORK_EDIT = "xpath=//*[@id='cic-internal-networks-li']//*[@class='hp-edit cic-internal-networks-edit-button']"
    XPATH_LIG_NO_INTERNAL_NETWORKS = "xpath=//*[@id='cic-internal-nets-network-available-help'  and  contains(text(),'There are no available Ethernet networks to add.')]"
    XPATH_LIG_INTERNAL_NETWORKS_OK = "xpath=//*[@id='cic-internal-nets-dialog-form']//*[@id='cic-internal-nets-dialog-add']"
    XPATH_LIG_INTERNAL_NETWORKS_CANCEL = "xpath=//*[@id='cic-internal-nets-dialog-form']//*[@class='hp-button hp-cancel']"
    ID_LIG_INTERNAL_NETWORK_ADD = "id=cic-internal-nets-dialog-networks-addNetworks"
    XPATH_LIG_INTERNAL_NETWORK = "xpath=//*[@class='dataTables_scrollBody']//*[text()='%s']"
    XPATH_LIG_INTERNAL_NETWORK_ADD = "xpath=//*[@class='hp-add hp-primary']"
    XPATH_LIG_INTERNAL_NETWORK_CANCEL = "xpath=//*[@class='hp-cancel']"
    ID_LIG_INTERNALE_NETWORK_EDIT_OK = "id=cic-internal-nets-dialog-add"
    XPATH_LIG_INTERNALE_NETWORK_EDIT_CANCEL = "xpath=//*[@id='cic-internal-nets-dialog-form']//*[@class='hp-button hp-cancel']"
    XPATH_LIG_INTERNAL_NETWORK_ADDED = "xpath=//table[@id='cic-internal-nets-dialog-network-assigned']//*[text()='%s']"
    XPATH_LIG_REMOVE_INTERNAL_NETWORK = "xpath=//table[@id='cic-internal-nets-dialog-network-assigned']//*[text()='%s']/following-sibling::*/*[@class='hp-close crm-delete-row']"

    # errors
    XPATH_EG_ADD_HP_STATUS_ERROR = "xpath=//*[@id='cic-switchtemplate-add-form']//*[@class='hp-status hp-status-error']"
    XPATH_EG_ADD_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='cic-switchtemplate-add-form']//*[@class='hp-form-message-summary']"
    XPATH_EG_ADD_FORM_MESSAGE_DETAILS = "xpath=//*[@id='cic-switchtemplate-add-form']//*[@class='hp-form-message-details']"
    XPATH_UPDATE_COMPLETE = "xpath=//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Completed']"
    XPATH_UPDATE_STATUS_ERROR = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Error']"
    XPATH_UPDATE_STATUS_WARNING = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Warning']"
    XPATH_LIG_DELETE_WARNING = "xpath=//*[@class='hp-dialog-container hp-wide hp-active']//*[@class='hp-notify hp-notify-warning hp-active']"
    XPATH_LIG_DELETE_WARNING_CANCEL = "xpath=//*[@class='hp-dialog-container hp-wide hp-active']//button[@class='hp-cancel hp-primary']"
    XPATH_EG_EDIT_HP_STATUS_ERROR = "xpath=//*[@id='cic-switchtemplate-edit-form']//*[@class='hp-status hp-status-error']"
    XPATH_EG_EDIT_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='cic-switchtemplate-edit-form']//*[@class='hp-form-message-summary']"
    XPATH_EG_EDIT_FORM_MESSAGE_DETAILS = "xpath=//*[@id='cic-switchtemplate-edit-form']//*[@class='hp-form-message-details']"

    XPATH_EG_TRAP_HP_STATUS_ERROR = "xpath=//*[@id='cic-snmp-trap-destination-form']//*[@class='hp-status hp-status-error']"
    XPATH_EG_TRAP_ERROR_MESSAGE_SUMMARY = "xpath=//*[@id='cic-snmp-trap-destination-form']//*[@class='hp-form-message-summary']"
    XPATH_EG_TRAP_ERROR_MESSAGE_DETAILS = "xpath=//*[@id='cic-snmp-trap-destination-form']//*[@class='hp-form-message-details']"

    XPATH_LUS_SELECT_TYPE = "xpath=//*[@id='cic-switchtemplate-dialog-type-add']//*[@class='hp-select-form']"
    XPATH_LUS_TYPE = "xpath=//*[@id='cic-switchtemplate-dialog-type-add']//*[@class='hp-select-form']//span[text()='%s']"
    XPATH_LUS_LACP_TIMER_SELECT = "xpath=//*[@id='cic-switchtemplate-dialog-lacp-timer']//*[@class='hp-select']"
