# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion network sets page/screen
'''


class FusionNetworkSetsPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Network Sets']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_CREATE_NETWORK_SET = "link=Create network set"
    # ID_MENU_ACTION_EDIT_NETWORK_SET = "cic-networkset-edit-action" #modified
    ID_NETWORK_SET_TABLE = "cic-networkset-master-table"
    ID_CREATE_NETWORK_SET_DIALOG = "hp-change-page-container"
    ID_CREATE_NETWORK_SET_FORM_MESSAGE = "hp-form-message"
    ID_MENU_ACTION_DELETE_NETWORK_SET = "id=cic-networkset-delete-action"
    ID_INPUT_NETWORK_SET_NAME = "id=cic-networkset-add-name"
    ID_INPUT_PREFERRED_BANDWIDTH = "id=cic-networkset-pref-bandwidth"
    ID_INPUT_MAX_BANDWIDTH = "id=cic-networkset-max-bandwidth"
    ID_BTN_ADD_NETWORKS = "id=cic-networkset-add-add-networks"
    ID_BTN_ADD_NETWORK_SET = "cic-networkset-add"
    ID_BTN_CREATE_NETWORK_SET = "cic-networkset-add"
    ID_BTN_CREATE_NETWORK_SET_PLUS = "cic-networkset-add-again"
    ID_BTN_EDIT_NETWORKS_NAME = "id=cic-networkset-edit-name"
    ID_BTN_CREATE_NETWORK_SET_CANCEL = "id=cic-networkset-add-close"
    ID_BTN_EDIT_ADD_NETWORKS = "cic-networkset-edit-add-networks"
    ID_ELEMENT_NETWORK_NAME_BASE = "xpath=//td[@class=' sorting_1' and text()='%s']"
    ID_BTN_ADD_NETWORKS_TO_NETWORK_SET = "id=cic-networkset-add"
    ID_BTN_ADD_PLUS_NETWORKS_TO_NETWORK_SET = "css=button.hp-add-again"
    ID_BTN_CANCEL_ADD_NETWORKS_TO_NETWORK_SET = "css=button.hp-cancel"
    ID_BTN_REMOVE_ALL_NETWORKS_FROM_NETWORK_SET = "cic-networkset-add-remove-all-networks"
    ID_DLG_DELETE_CONFIRM = "id=cic-delete-dialog-yes"
    ID_ELEMENT_NETWORK_SET_NAME_BASE = "xpath=//td[@class='' and text()='%s']"  # Replace with network set name
    ID_ADD_NETWORKS_TABLE = "cic-networkset-add-networks-table"

    # View
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_OVERVIEW = "id=cic-networkset-overview-selector"
    ID_LINK_RELATED = "link=Related"
    # modified
    ID_MENU_ACTION_EDIT_NETWORK_SET = "link=Edit"
    # newly added
    ID_BTN_ADD_NETWORK_TO_NETWORK_SET = "css=button.hp-add"
    ID_INPUT_NETWORK_NAME_SEARCH = "css=input.hp-search"
    ID_ELEMENT_NETWORKSET_NETWORK_NAME = "xpath=//tbody/tr/td[text()='%s']"
    ID_ELEMENT_NETWORKSET_EDIT_NAME_TABLE = "xpath=//table[@id='cic-networkset-edit-networks-table']/tbody//td[text()='%s']"
    ID_ELEMENT_DELETE_NETWORK_NETWORKSET = "xpath=//tr[descendant::td[contains(.,'%s')]]//div[@class='hp-close crm-networkset-close']"
    ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET = "xpath=//tr[descendant::td[contains(.,'%s')]]//input[@type='checkbox']"
    ID_ELEMENT_NETWORKSET_HEADER = "xpath=//h1[text()='%s']"
    ID_BTN_UPDATE_CONFORM = "id=cic-networkset-update"
    ID_BTN_UPDATE_CANCEL = "id=cic-networkset-edit-cancel"
    ID_BTN_ADD_NETWORKS_TO_NETWORKSET_CANCEL_BUTTON = "css=button.hp-cancel"
    ID_ELEMENT_ERROR_MESSAGE = "xpath=//label[text()='%s']"
    ID_ERROR_MESSAGE_FOR_EMPTY_VALUE = "This field is required."
    ID_ERROR_MESSAGE_FOR_INVALID_VALUE = "Enter a value less than or equal to 10."
    ID_ERROR_MESSAGE_FOR_LESS_VALUE = "Value must be less than or equal to Maximum bandwidth."
    ID_ERROR_MESSAGE_FOR_ZERO_VALUE = "Enter a value greater than or equal to 0.1."
    ID_INPUT_NETWORKSET_NEXTPATH_NAME = "xpath=//td[text()='%s']"
    ID_NETWORK_NETWORKSET_TABLE_NAME_COLUMN = "xpath=//table[@id='cic-networkset-edit-networks-table']/tbody/tr[%s]/td[1]"
    ID_NETWORK_NETWORKSET_TABLE_ROW = "xpath=//table[@id='cic-networkset-edit-networks-table']/tbody/tr"
    ID_BTN_REMOVE_ALL_NETWORKS = "id=cic-networkset-edit-remove-all-networks"

    # To add label
    ID_LINK_RESET = "link=Reset"
    ID_NETWORK_SET_LIST_NAMES = "xpath = .//*[@id='cic-networkset-master-table']/tbody/tr/td"
    ID_LINK_VIEW = "xpath = .//*[@id='cic-networkset-panel-selector']"
    ID_DROPDOWN_SELECTION = "link=Labels"
    ID_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/span[text()='Labels']"
    ID_EDIT_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/a[@class='hp-panel-edit' and text()='Edit']"
    ID_EDIT_LABEL_PANEL = "xpath = //header[@id='hp-labels-edit-header']/h1/span[text()='Edit Labels']"
    ID_LABEL_NAME = "id=hp-labels-edit-search-input"
    ID_ADD_LABEL_BTN = "id=hp-labels-edit-add"
    ID_OK_LABEL_BTN = "id=hp-labels-edit-ok"
    ID_ADDED_LABEL = "xpath = //table[@id='hp-labels-show-table']/descendant::a[text()='%s']"
