# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''
This file contains all elements ID on Fusion Switches sets page
'''


class GeneralSwitchesElements(object):

    SWITCH_ID_GENERAL_SECTION = "xpath=.//*[@id='cic-switch-moreview-general-selector']/label"
    SWITCH_ID_LINK_OVERVIEW = "xpath=.//*[@id='cic-switch-panel-selector']/div"
    SWITCH_ID_LINK_GENERAL = "xpath=.//*[@id='cic-switch-general-panel-selector']/a"
    SWITCH_ID_LINK_PORTS = "xpath=.//*[@id='cic-switch-ports-panel-selector']/a"
    SWITCH_ID_PORTS_SECTION = "xpath=.//*[@id='cic-switch-moreview-ports-selector']/label"
    ID_TABLE_SWITCHES = "//table[@id='cic-switch-master-table']/tbody/tr/td[last()-1]"
    ID_TABLE_SWITCH = "//table[@id='cic-switch-master-table']/tbody/tr/td[text()='%s']"
    ID_TEXT_SWITCH_TITLE = "//h1[@id='cic-switch-details-title' and text()='%s']"
    ID_SWITCH_CURRENT_STATE = "xpath=.//*[@id='cic-switch-show-state']"
    ID_SWITCH_MODEL_NUMBER = "xpath=.//*[@id='cic-switch-show-model']"
    ID_SWITCH_PORT_TABLE = "xpath=.//*[@id='cic-switch-moreview-ports-table']/tbody"
    ID_SWITCH_EXPAND_TABLE_ROW = "xpath=.//*[@id='cic-switch-moreview-ports-table']/tbody/tr[%s]/td[@class='hp-icon']/div"
    ID_SWITCH_PORT_TABLE_VLAN_LABEL = "xpath=.//*[@id='cic-switch-moreview-ports-table']/tbody/tr[%s]/td/div[@class='hp-collapsible hp-collapsed cic-switch-port-vlanid-collapsible']/label"
    ID_SWITCH_PORT_TABLE_VLAN_DATA = "xpath=.//*[@id='cic-switch-moreview-ports-table']/tbody/tr[%s]/td/div[@class='hp-collapsible cic-switch-port-vlanid-collapsible']/div/div"
    ID_SWITCH_PORT_CHANNEL = "xpath=.//*[@id='cic-switch-moreview-ports-table']/tbody/tr[%s]/td[last()-1]"
    ID_SWITCH_TABLE_ROW_COUNT = "xpath=.//*[@id='cic-switch-moreview-ports-table']/tbody/tr[%s]/td[@class='hp-numeric']"
    ID_SWITCH_ACTION_BTN = "xpath=.//*[@id='cic-switch-actions']/label"
    ID_SWITCH_EDIT_BTN = "xpath=.//*[@id='cic-switch-edit-action']"
    ID_SWITCH_REFRESH_BTN = "xpath=.//*[@id='cic-switch-refresh-action']"
    ID_SWITCH_EDIT_LABEL = "xpath=.//*[@id='hp-change-page-container']/section/div[@class='hp-details-header']"
    ID_SWITCH_CHECKBOX = "xpath=.//*[@id='cic-switch-edit-ports']/..//..//tr[%s]//*[@type='checkbox']"
    ID_SWITCH_PORTSTATUS = "xpath=//tr[%s]/td[@class='hp-numeric']/preceding-sibling::td[text()='Unlinked' or text()='Linked' or text()='Disabled']"
    ID_SWITCH_OK_BTN = "xpath=.//*[@id='cic-switch-update']"
    ID_SWITCH_PROGRESS_BAR = "//div[@class='hp-progress']"
    ID_SWITCH_CONFIGURE_STATE = "//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Completed']"
    ID_PORT_CHANNEL = "xpath=.//*[@id='cic-switch-moreview-ports-table-header']/tr/td[text()='Port Channel']"
    ID_VPC_NUMBER = "xpath=.//*[@id='cic-switch-moreview-ports-table-header']/tr/td[text()='vPC Number']"
