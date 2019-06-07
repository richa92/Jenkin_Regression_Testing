# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
'''

This File contains all Element ID on Fusion NetworkSets page/screen
'''


class GeneralNetworkSetsElements(object):
    ID_TABLE_MASTER = "id=cic-networkset-master-table"
    ID_TABLE_NETWORK_SET = "xpath=//table[@id='cic-networkset-master-table']"
    ID_TABLE_NETWORK_SET_NAME_LIST = "xpath=//table[@id='cic-networkset-master-table']/tbody//tr/td[2]"
    ID_TABLE_NETWORK_SET_NAME = "xpath=//table[@id='cic-networkset-master-table']/tbody//tr/td[text()='%s']"  # %Network_name
    ID_TABLE_NO_NETWORK_SET_MESSAGE = "xpath=//div[text()='No network sets']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_VERIFY_NETWORK_SET_STATUS_TITLE = "id=cic-network-details-title"
    ID_SELECT_NETWORK_SET_PANEL = "id=cic-networkset-panel-selector"
    ID_SELECT_NETWORK_SET_VIEWS = "//*[@id='cic-networkset-panel-selector']/ol/li/a[text()='Overview']"  # % Overview, Activity, Map, Labels
    ID_VERIFY_NETWORK_SET_TITLE = "//h1[@id='cic-networkset-details-title' and text()='%s']"
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Network Sets']"
    ID_PAGE_OVERVIEW = "id=cic-networkset-show-overview"
    ID_TABLE_NETWORKSET_NAME_LIST = "xpath=//table[@id='cic-networkset-master-table']/tbody//tr/td"


class CreateNetworkSetsElements(object):
    ID_BUTTON_CREATE_NETWORK_SET = "//a[text()='Create network set']"
    ID_ACTION_MENU_CREATE_NETWORK_SET = "id=cic-networkset-create-action"
    ID_DIALOG_CREATE_NETWORK_SET = "xpath=//section[@class='hp-details-add-section']"
    ID_DIALOG_CREATE_NETWORK_SET_MESSAGE = "xpath=//span[@class='hp-form-message-text']"
    ID_DIALOG_CREATE_NETWORK_SET_FORM_MESSAGE = "hp-form-changes"
    ID_INPUT_NETWORK_SET_NAME = "id=cic-networkset-add-name"
    ID_INPUT_NETWORK_SET_PREF_BANDWIDTH = "id=cic-networkset-pref-bandwidth"
    ID_INPUT_NETWORK_SET_MAXS_BANDWIDTH = "id=cic-networkset-max-bandwidth"
    ID_BUTTON_ADD_NETWORK = "id=cic-networkset-add-add-networks"
    ID_BUTTON_REMOVEALL_NETWORK = "id=cic-networkset-add-remove-all-networks"

    ID_DIALOG_ADD_NETWORK = "//h1[contains(.,'Add Networks to')]"
    ID_INPUT_SEARCH_TEXT = "//input[@class='hp-search']"
    ID_TABLE_NETWORK_NAME = "//form[@class='hp-edit-form']//table/tbody/tr/td[text()='%s']"
    ID_BUTTON_REMOVE_NETWORK = "//tr[td[text()='%s']]/td/div"
    ID_BUTTON_ADD = "//button[text()='Add']"
    ID_BUTTON_ADD_AGAIN = "//button[text()='Add +']"
    ID_BUTTON_CANCEL = "//form[@class='hp-edit-form']//button[text()='Cancel']"
    ID_CHECKBOX_NETWORK_UNTAGGED = "//tr[td[text()='%s']]/td[@class='hp-single']/input"

    ID_BTN_CREATE_NETWORK_SET = "//input[@id='cic-networkset-add']"
    ID_BTN_CREATE_NETWORK_SET_PLUS = "//input[@id='cic-networkset-add-again']"
    ID_BTN_CLOSE_NETWORK_SET = "//a[@id='cic-networkset-add-close']"


class EditNetworkSetsElements(object):
    ID_ACTION_MENU_EDIT_NETWORK_SET = "id=cic-networkset-edit-action"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_DIALOG_EDIT_NETWORK_SET = "id=cic-networkset-edit-form"
    ID_INPUT_NETWORK_SET_NAME = "id=cic-networkset-edit-name"
    ID_INPUT_NETWORK_SET_PREF_BANDWIDTH = "id=cic-networkset-pref-bandwidth"
    ID_INPUT_NETWORK_SET_MAXS_BANDWIDTH = "id=cic-networkset-max-bandwidth"
    ID_BUTTON_ADD_NETWORK = "id=cic-networkset-edit-add-networks"
    ID_BUTTON_REMOVEALL_NETWORK = "id=cic-networkset-edit-remove-all-networks"

    ID_INPUT_SEARCH_TEXT = "//input[@class='hp-search']"
    ID_TABLE_NETWORK_NAME = "//form[@class='hp-edit-form']//table/tbody/tr/td[text()='%s']"
    ID_BUTTON_REMOVE_NETWORK = "//tr[td[text()='%s']]/td/div"
    ID_BUTTON_ADD = "//button[text()='Add']"
    ID_BUTTON_ADD_AGAIN = "//button[text()='Add +']"
    ID_BUTTON_CANCEL = "//form[@class='hp-edit-form']//button[text()='Cancel']"
    ID_CHECKBOX_NETWORK_UNTAGGED = "//tr[td[text()='%s']]/td[@class='hp-single']/input"

    ID_BTN_UPDATE_NETWORK_SET = "id=cic-networkset-update"
    ID_BTN_CANCEL = "id=cic-networkset-edit-cancel"


class DeleteNetworkSetsElements(object):
    ID_ACTION_MENU_DELETE_NETWORK_SET = "id=cic-networkset-delete-action"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_DIALOG_DELETE_NETWORK_SET = "id=cic-delete-dialog-prompt"
    ID_BTN_DELETE_NETWORK_SET = "id=cic-delete-dialog-yes"
    ID_BTN_CANCEL = "//button[text()='Cancel']"


class VerifyNetworkSetsElements(object):
    ID_VERIFY_DELETED_NETWORK_SET_TITLE = "//h1[@id='hp-not-exist-title' and text()='%s']"
    ID_VERIFY_NETWORK_SET_TITLE = "//h1[@id='cic-networkset-details-title' and text()='%s']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_DIALOG_DELETE_NETWORK_SET = "id=cic-delete-dialog-prompt"
    ID_BTN_DELETE_NETWORK_SET = "id=cic-delete-dialog-yes"
    ID_BTN_CANCEL = "//button[text()='Cancel']"
    ID_TABLE_NETWORK_SET_DELETED = "//table/tbody//td[parent::tr[contains(@class, 'hp-not-found')] and text()='%s']"  # network_name
    ID_TABLE_NETWORK_SETS_NOT_FOUND = "xpath=//td[@class='dataTables_empty' and text()='No network sets']"

    ID_VERIFY_NETWORK_SET_PREF_BANDWIDTH = "//span[@id='cic-networkset-pref-bandwidth' and text()='%s']"
    ID_VERIFY_NETWORK_SET_MAX_BANDWIDTH = "//span[@id='cic-networkset-max-bandwidth' and text()='%s']"
    ID_VERIFY_NETWORK_SET_NETWORK_NAME = "//a[text()='%s']"
    ID_VERIFY_NETWORK_SET_NETWORK_VLAN = "//tr[td[a[text()='%s']]]/td[text()='%s']"
    ID_VERIFY_NETWORK_SET_NETWORK_UNTAGGED = "//tr[td[a[text()='%s']]]/td[text()='Untagged']"
    ID_ADD_NETWORKS_TABLE = "id=cic-networkset-add-networks-table"
    ID_ADD_NETWORKS_TABLE_ITEM = "//table[@id='cic-networkset-add-networks-table']//td[text()='%s']"
    ID_EDIT_NETWORKS_TABLE = "id=cic-networkset-edit-networks-table"
    ID_EDIT_NETWORKS_TABLE_ITEM = "//table[@id='cic-networkset-edit-networks-table']//td[text()='%s']"
    ID_CREATE_NETWORK_SET_FORM_MESSAGE = "id=hp-form-changes"
    ID_INPUT_NETWORK_SET_NAME = "id=cic-networkset-add-name"
    ID_BUTTON_REMOVE_NETWORK = "//tr[td[text()='%s']]/td/div"


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
