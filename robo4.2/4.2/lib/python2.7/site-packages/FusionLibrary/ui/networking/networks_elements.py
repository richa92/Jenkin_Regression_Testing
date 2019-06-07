# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion Networks page/screen
'''


class FusionNetworksPage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Networks']"
    ID_MASTER_TABLE = "cic-network-master-table"
    ID_NETWORK_LIST = "xpath=//table[@id='cic-network-master-table']/tbody//tr/td[2]"
    ID_LINK_CREATE_NETWORK = "link=Create network"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_ACTION_MENU_CREATE_NETWORK = "link=Create network"
    ID_ACTION_MENU_EDIT_NETWORK = "cic-network-edit-action"
    ID_ACTION_MENU_DELETE_NETWORK = "cic-network-delete-action"
    # networks table
    ID_NETWORK_LIST = "xpath=//table[@id='cic-network-master-table']"
    ID_NETWORK_LIST_NAMES = "xpath=//table[@id='cic-network-master-table']/tbody/tr/td[2]"
    # Status pane
    ID_NETWORK_STATUS_TITLE = "cic-network-details-title"
    # Messages
    ID_CREATE_NETWORK_MESSAGE_DETAILS = "xpath=//div[@class='hp-form-message-details']"
    # Create Network #
    ID_CREATE_NETWORK_DIALOG = "xpath=//section[@class='hp-details-add-section']"
    ID_CREATE_NETWORK_DIALOG_MESSAGE = "xpath=//span[@class='hp-form-message-text']"
    ID_CREATE_NETWORK_DIALOG_FORM_MESSAGE = "hp-form-changes"
    ID_INPUT_NETWORK_NAME = "cic-network-name"
    ID_RADIO_ETHERNET_TYPE = "cic-network-add-ethernet-type"
    ID_RADIO_FCOE_TYPE = "id=cic-network-add-fcoe-type"
    ID_INPUT_NETWORK_VLAND_ID = "id=cic-network-vlan-id"
    ID_INPUT_NETWORK_PREF_BANDWIDTH = "cic-network-pref-bandwidth"
    ID_INPUT_NETWORK_MAXS_BANDWIDTH = "cic-network-max-bandwidth"
    ID_CHKBOX_NETWORK_SMARK_LINK = "cic-network-smart-link"
    ID_CHKBOX_NETWORK_PRIVATE_NETWORK = "cic-network-private-network"
    ID_RADIO_FIBRE_CHANNEL_TYPE = "cic-network-add-fc-type"
    ID_BTN_UPDATE_NETWORK = "id=cic-network-update"
    ID_COMBO_FABRIC_TYPE = "xpath=//label[text()='Fabric type']/following-sibling::div/a"
    ID_COMBO_UPLINK_SPEED = "xpath=//label[text()='Uplink speed']/following-sibling::div/a"
    # ID_COMBO_PURPOSE = "xpath=//*[@id='cic-network-edit-form']/fieldset/ol/li[6]/div/a/span[2]"
    ID_EDIT_PURPOSE_DROPDOWN = "xpath=//*[@id='cic-network-edit-form']/fieldset/ol/li[7]/div/div/div"
    # ID_COMBO_SELECT_PURPOSE = "xpath=.//*[@id='cic-network-edit-form']/fieldset/ol/li[6]/div/a"
    ID_COMBO_FABRIC_ARROW = "xpath=//*[@id='cic-network-data-section']/li[1]/div/a/span[2]"
    ID_PURPOSE_DROPDOWN = "xpath=//div[@id='cic-network-data-section']/li[5]/div/div/div/div"
    ID_VLAN_DROPDOWN = "xpath=//div[@id='cic-network-data-section']/li[3]/div/div/div"
    ID_SELECT_DIRECT_ATTACH = "xpath=//a[@rel='DirectAttach']"
    ID_EDIT_FCNETWORK_LINK_STABILITY = "xpath=.//*[@id='cic-network-edit-link-stability-time']"
    ID_TOGGLE_LOGIN_DISTRIBUTION = "xpath=//a[@id='cic-network-add-auto-login-redistribution-hpToggle']"
    ID_INPUT_FCNETWORK_LINK_STABILITY = "id=cic-network-add-link-stability-time"
    ID_ELEMENT_NETWORK_NAME_BASE = "xpath=//td[@class='hp-identifier' and text()='%s']"  # replace %s with network/fc name
    ID_ELEMENT_NETWORK_DELETED = "xpath=//table[@id='cic-network-master-table']//td[.='%s' and parent::tr[contains(@class, 'hp-not-found')]]"
    ID_BTN_CREATE_NETWORK = "id=cic-network-add"
    ID_BTN_CREATE_NETWORK_PLUS = "id=cic-network-add-again"
    ID_BTN_CLOSE_NETWORK = "id=cic-network-add-close"
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
    ID_NETWORK_VLAN = "xpath=//div[@class='dataTables_scroll']//table/tbody/tr/td[text()='%s']/following::td[1]"

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
    ID_ASSOCIATE_SAN = "xpath = //td[text()='%s']"
    ID_INPUT_ASSOC_SAN = "id=cic-network-add-san-select-input"

    # Modified objects for Fusion 1.10
    ID_RADIO_FIBRE_CHANNEL_TYPE = "id=cic-network-add-fc-type"
    ID_PURPOSE_DROPDOWN = "xpath=//label[text()='Purpose']/following-sibling::div/div/div/div"
    ID_LINK_RESET = "link=Reset"

    # To add label
    ID_LINK_VIEW = "xpath = .//*[@id='cic-network-panel-selector']"
    ID_DROPDOWN_SELECTION = "link=Labels"
    ID_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/span[text()='Labels']"
    ID_EDIT_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/a[@class='hp-panel-edit' and text()='Edit']"
    ID_EDIT_LABEL_PANEL = "xpath = //header[@id='hp-labels-edit-header']/h1/span[text()='Edit Labels']"
    ID_LABEL_NAME = "id=hp-labels-edit-search-input"
    ID_ADD_LABEL_BTN = "id=hp-labels-edit-add"
    ID_OK_LABEL_BTN = "id=hp-labels-edit-ok"
    ID_ADDED_LABEL = "xpath = //table[@id='hp-labels-show-table']/descendant::a[text()='%s']"
