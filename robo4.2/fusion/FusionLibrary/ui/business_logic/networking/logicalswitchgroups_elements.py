# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all elements ID on Fusion Logical Switch Groups page/screen
'''
from FusionLibrary.ui.business_logic.base import FusionUIConst


class GeneralLogicalSwitchGroupsElements(object):

    ID_MENU_LINK_LOGICAL_SWITCH_GROUPS = "link=Logical Switch Groups"
    ID_LINK_CREATE_LOGICAL_SWITCH_GROUP = "link=Create logical switch group"
    ID_BTN_CLOSE_LSG = "xpath=//a[@id='cic-torswitchgroup-add-close']"
    ID_TABLE_LOGICAL_SWITCH_GROUP_LIST = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[1+count(//table[@class='hp-master-table hp-selectable dataTable']//td[text()='Name']//preceding-sibling::*)]"
    ID_TABLE_LOGICAL_SWITCH_GROUP = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # Logical Switch Group name
    ID_TABLE_LOGICAL_SWITCH_GROUP_SELECTED = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-selected')]/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # Logical Switch Group name
    ID_TABLE_LOGICAL_SWITCH_GROUP_NOT_FOUND = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-not-found')]/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # Logical Switch Group name
    ID_STATUS_LOGICAL_SWITCH_GROUP_OK = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-ok']"  # Logical Switch Group name
    ID_STATUS_LOGICAL_SWITCH_GROUP_WARN = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-warning']"  # Logical Switch Group name
    ID_STATUS_LOGICAL_SWITCH_GROUP_ERROR = "xpath=//table/tbody//tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']/../td/div[@class='hp-status hp-status-error']"  # Logical Switch Group name
    ID_BUTTON_ACTIONS = "xpath=//*[text()='Actions']"


class CreateLogicalSwitchGroupsElements(object):
    ID_BUTTON_CREATE_LOGICAL_SWITCH_GROUP = "xpath=//a[text()='Create logical switch group']"
    ID_SELECT_ACTIONS_CREATE = "xpath=//*[@id='cic-torswitchgroup-create-action']/a"
    ID_DIALOG_CREATE_LOGICAL_SWITCH_GROUP = "xpath=//*[@id='cic-torswitchgroup-add-form']/../../div[contains(@class, 'dialog')]"
    ID_INPUT_NAME = "xpath=//input[@id='cic-torswitchgroup-add-name']"
    ID_SELECT_TYPE = "cic-torswitchgroup-add-switch-type"
    ID_SELECT_NUMBER_OF_SWITCHES = "cic-torswitchgroup-add-switch-number"
    ID_DROPDOWN_TYPE = "xpath=//*[@id='cic-torswitchgroup-add-form']//label[text()='Type']/following-sibling::*//div[contains(@class, 'hp-value')]"
    ID_BUTTON_CREATE = "xpath=//input[@id='cic-torswitchgroup-add']"
    ID_BUTTON_CREATE_PLUS = "xpath=//input[@id='cic-torswitchgroup-again']"
    ID_BUTTON_CANCEL = "xpath=//a[@id='cic-torswitchgroup-add-close']"

    ID_ERROR_CREATE_FAILED = "css=div.hp-details,div.hp-details span"
    ID_TEXT_TYPE_LIST = "xpath=//*[@id='cic-torswitchgroup-add-form']//label[text()='Type']/following-sibling::*//ol"


class EditLogicalSwitchGroupsElements(object):
    ID_SELECT_ACTIONS_EDIT = "xpath=//*[@id='cic-torswitchgroup-edit-action']/a"
    ID_DIALOG_EDIT_LOGICAL_SWITCH_GROUP = "xpath=//*[@id='cic-torswitchgroup-edit-form']/../../div[contains(@class, 'dialog')]"
    ID_INPUT_NAME = "xpath=//input[@id='cic-torswitchgroup-edit-name']"
    ID_SELECT_NUMBER_OF_SWITCHES = "cic-torswitchgroup-edit-switch-number"
    ID_BUTTON_OK = "xpath=//*[@id='cic-torswitchgroup-update']"
    ID_BUTTON_CANCEL = "xpath=//*[@id='cic-torswitchgroup-edit-cancel']"

    ID_ERROR_EDIT_FAILED = "css=div.hp-details,div.hp-details span"


class DeleteLogicalSwitchGroupsElements(object):
    ID_SELECT_ACTIONS_DELETE = "xpath=//*[@id='cic-torswitchgroup-delete-action']/a"
    ID_DIALOG_DELETE_LOGICAL_SWITCH_GROUP = "xpath=//header//span[contains(text(), 'Delete')]/ancestor::*/div[@class='hp-dialog']"
    ID_LABEL_DELETE = "xpath=//header//span[contains(text(), 'Delete')]"
    ID_LABEL_LOGICAL_SWITCH_GROUP_NAME = "xpath=//header//span[contains(text(), 'Delete')]/following-sibling::span"
    ID_TEXT_PROMPT_MESSAGE = "xpath=//*[@id='cic-delete-dialog-prompt']"
    ID_BUTTON_YES_DELETE = "xpath=//*[@id='cic-delete-dialog-yes']"
    ID_BUTTON_CANCEL = "xpath=//button[text()='Cancel']"
    ID_LABEL_DELETE_ERROR_MESSAGE = "xpath=//*[@id='cic-torswitchgroup-delete-error-msg']"
    ID_LINK_FOR_USED_BY = "xpath=//*[@id='cic-torswitchgroup-delete-error-used-by-single-ls']/a"
    ID_BUTTON_CLOSE = "xpath=//button[text()='Close']"
    ID_LINK_HELP_FOR_DELETE_ERROR = "xpath=//*[@id='cic-torswitchgroup-delete-error-dialog-help']"


class FusionLSGPage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Logical Switch Groups']"
    ID_MASTER_TABLE = "cic-network-master-table"
    ID_LSG_LIST = "xpath=//table[@id='cic-torswitchgroup-master-table']/tbody//tr/td"
    ID_LINK_CREATE_LOGICAL_SWITCH_GROUP = "link=Create logical switch group"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_ACTION_MENU_CREATE_NETWORK = "link=Create network"
    ID_ACTION_MENU_EDIT_LSG = "xpath=//*[@id='cic-torswitchgroup-edit-action']/a"
    ID_ACTION_MENU_DELETE_LSG = "cic-torswitchgroup-delete-action"
    # networks table
    ID_NETWORK_LIST = "xpath=//table[@id='cic-network-master-table']"
    ID_NETWORK_LIST_NAMES = "xpath=//table[@id='cic-network-master-table']/tbody/tr/td[2]"
    # Status pane
    ID_NETWORK_STATUS_TITLE = "cic-network-details-title"
    # Messages
    ID_CREATE_LSG_MESSAGE_DETAILS = "xpath=//div[@class='hp-details']"
    # Create Network
    ID_CREATE_LSG_DIALOG = "xpath=//div[@class='hp-dialog']"
    ID_CREATE_NETWORK_DIALOG_MESSAGE = "xpath=//span[@class='hp-form-message-text']"
    ID_CREATE_NETWORK_DIALOG_FORM_MESSAGE = "hp-form-changes"
    ID_INPUT_LSG_NAME = "cic-torswitchgroup-add-name"
    ID_INPUT_EDIT_LSGNAME = "cic-torswitchgroup-edit-name"
    ID_INPUT_EDIT_LSG_NAME = "cic-torswitchgroup-edit-name"
    ID_RADIO_ETHERNET_TYPE = "cic-network-add-ethernet-type"
    ID_INPUT_NETWORK_VLAND_ID = "id=cic-network-vlan-id"
    ID_INPUT_NETWORK_PREF_BANDWIDTH = "cic-network-pref-bandwidth"
    ID_INPUT_NETWORK_MAXS_BANDWIDTH = "cic-network-max-bandwidth"
    ID_CHKBOX_NETWORK_SMARK_LINK = "cic-network-smart-link"
    ID_CHKBOX_NETWORK_PRIVATE_NETWORK = "cic-network-private-network"
    ID_RADIO_FIBRE_CHANNEL_TYPE = "cic-network-add-fc-type"
    ID_BTN_UPDATE_LSG = "id=cic-torswitchgroup-update"
    ID_BTN_EDIT_CANCEL = "id=cic-torswitchgroup-edit-cancel"
    ID_COMBO_FABRIC_TYPE = "xpath=//label[text()='Fabric type']/following-sibling::div/a"
    ID_COMBO_UPLINK_SPEED = "xpath=//label[text()='Uplink speed']/following-sibling::div/a"
    # ID_COMBO_PURPOSE = "xpath=//*[@id='cic-network-edit-form']/fieldset/ol/li[6]/div/a/span[2]"
    ID_EDIT_PURPOSE_DROPDOWN = "xpath=//*[@id='cic-network-edit-form']/fieldset/ol/li[7]/div/div/div"
    # ID_COMBO_SELECT_PURPOSE = "xpath=.//*[@id='cic-network-edit-form']/fieldset/ol/li[6]/div/a"
    ID_COMBO_FABRIC_ARROW = "xpath=//*[@id='cic-network-data-section']/li[1]/div/a/span[2]"
    ID_PURPOSE_DROPDOWN = "xpath=//div[@id='cic-network-data-section']/li[5]/div/div/div/div"
    SWITCH_TYPE_DROPDOWN = "xpath=//div[@class='hp-dialog-variable-contents']/fieldset/ol/li[2]/div/div/div"
    SWITCH_TYPE_DROPDOWN_SELECT = "xpath=//div[@class='hp-dialog-variable-contents']/fieldset/ol/li[2]/div/div/div/ol/li[text()='%s']"
    SWITCH_COUNT_DROPDOWN = "xpath=//div[@class='hp-dialog-variable-contents']/fieldset/ol/li[3]/div/div/div"
    ID_SELECT_DIRECT_ATTACH = "xpath=//a[@rel='DirectAttach']"
    ID_EDIT_FCNETWORK_LINK_STABILITY = "xpath=.//*[@id='cic-network-edit-link-stability-time']"
    ID_TOGGLE_LOGIN_DISTRIBUTION = "xpath=//a[@id='cic-network-add-auto-login-redistribution-hpToggle']"
    ID_INPUT_FCNETWORK_LINK_STABILITY = "id=cic-network-add-link-stability-time"
    ID_ELEMENT_LSG_NAME_BASE = "xpath=//td[@class='' and text()='%s']"  # replace %s with LSG name
    ID_BTN_CREATE_LSG = "id=cic-torswitchgroup-add"
    ID_BTN_CREATE_LSG_PLUS = "id=cic-torswitchgroup-again"
    ID_BTN_CLOSE_LSG = "xpath=//a[@id='cic-torswitchgroup-add-close']"
    ID_FRAME_NETWORK_ADD_SUMMARY = "css=div.hp-form-message-summary"
    ID_BTN_CONFIRM_DELETE = "id=cic-delete-dialog-yes"
    ID_EDIT_CHKBOX_NETWORK_SMARK_LINK = "cic-network-edit-smart-link"
    ID_EDIT_CHKBOX_NETWORK_PRIVATE_NETWORK = "cic-network-edit-private-network"

    ID_COMBO_EDIT_UPLINK_SPEED = "xpath=.//*[@id='cic-network-edit-form']/fieldset/ol/li[11]/a/span[2]"
    ID_EDIT_FCNETWORK_FABRICTYPE = "xpath=.//*[@id='cic-network-fabricType']"
    # View
    ID_COMBO_MENU_VIEW = "css=#cic-network-panel-selector > div.hp-value"
    ID_LINK_ALERTS = "id=cic-network-alerts-selector"
    ID_LINK_OVERVIEW = "id=cic-network-overview-selector"
    ID_LINK_RELATED = "link=Related"
    # label view
    ID_GENERAL_MENU = "xpath=//*[@id='cic-torswitchgroup-panel-selector']/div"
    ID_LABEL_MENU = "xpath=//*[@id='cic-torswitchgroup-panel-selector']/ol/li[4]/a"
    ID_LABEL_STRING = "xpath=//*[@id='hp-labels-show-panel']/label/span"
    ID_LABEL_EDIT = "xpath=//*[@id='hp-labels-show-panel']/label/a"
    ID_LABEL_INPUT_NAME = "xpath=//*[@id='hp-labels-edit-search-input']"
    ID_LABEL_ADD_BTN = "xpath=//*[@id='hp-labels-edit-add']"
    ID_LABEL_EDIT_OK = "xpath=//*[@id='hp-labels-edit-ok']"
    ID_LABEL_DELETE = "xpath=//*[@id='hp-labels-edit-table']/tbody/tr/td[2]/div"
    ID_FILTER_LABEL = "xpath=//*[@id='cic-torswitchgroup-labels-filter']/div"
    ID_FILTER_RESET = "xpath=//*[@id='cic-torswitchgroup-page']/nav/a"
    # Catagory View
    ID_CATAGORY_MAIN_VIEW = "css=div.hp-value"
    ID_CATAGORY_ALL_TYPE = "xpath=//li[@class='hp-selected' and text()='All types']"
    ID_CATAGORY_ETHERNET = "xpath=//li[@class='hp-selected' and text()='Ethernet']"
    ID_CATAGORY_FIBER_CHANNEL = "xpath=//li[@class='hp-selected' and text()='Fibre channel']"
    # delete dialog text
    ID_DELETE_DIALOG_MESSAGE = "xpath=//div[@id='cic-delete-dialog-prompt']"
    ID_NETWORK_TYPE = "xpath=//div[@class='dataTables_scroll']//table/tbody/tr/td[text()='%s']/following::td[2]"

    # Newly added objects for Fusion 1.10
    ID_PURPOSE_OPTION = "xpath = //span[text()='%s']"  # replace %s with purpose
    ID_COMBO_ASSOCIATE_SAN = "//li[@id='cic-network-add-san-section']/div//div[@class='hp-search-combo-control']"
    ID_ASSOCIATE_SAN = "xpath = //span[text()='%s']"
