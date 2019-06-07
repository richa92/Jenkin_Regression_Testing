# (C) Copyright 2016 Hewlett-Packard Development Company, L.P.
'''

This File contains all element ID on Fusion Scopes page/screen
'''


class GeneralScopesElements(object):
    ID_TABLE_MASTER = "id=fs-scope-table"
    ID_TABLE_SCOPE = "xpath=//table[@id='fs-scope-table']"
    ID_RESOURCE_TABLE = "xpath=//*[@id='fs-scope-resources-container']"
    ID_TABLE_SCOPE_NAME_LIST = "//table[@id='fs-scope-table']/tbody//tr/td"
    ID_TABLE_SCOPE_NAME = "xpath=//table[@id='fs-scope-table']/tbody//tr/td[text()='%s']"  # scope_name
    ID_NETWORK_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Networks']"
    ID_TABLE_NO_SCOPE_MESSAGE = "xpath=//div[text()='No scopes']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_TABLE_ENETS_LIST = "xpath=.//*[@class='hp-selectable hp-association-selector-table dataTable']/tbody"
    ID_MOUSE_OVER = "xpath=//*[contains(text(),'Load more')]"
    ID_APPLIANCE_STATE = "xpath=.//*[@id='hp-error-page']"
    ID_MAIN_MENU = "xpath=.//*[@id='hp-main-menu-label']"
    ID_ACTIVITY_LABEL = "xpath=.//*[@id='hp-activity-page']/nav/div[2]/h1"
    ID_SCOPES_LABEL = "xpath=.//*[@id='fs-scope-page']/nav/div[1]/h1/span"
    ID_SELECT_SCOPE_PANEL = "id=fs-scope-panel-selector"
    ID_SELECT_SCOPE_VIEWS = "//*[@id='fs-scope-panel-selector']/ol/li/a[text()='Overview']"  # % Overview, Activity, Map, Labels
    ID_VERIFY_SCOPE_TITLE = "//h1[@id='fs-scope-details-title' and text()='%s']"
    ID_PAGE_LABEL = "//h1[@class='hp-parent-page-label']//span[text()='Scopes']"
    ID_PAGE_OVERVIEW = "id=fs-scope-overview"
    ID_LINK_SCOPES = "//div[@id='fs-settings-scope-panel']//a"
    ID_LINK_SCOPE_RESOURCE = "//table[@id='fs-scope-resource-table']//a[contains(text(),'%s')]"
    ID_BTN_SETTING_SCOPE = "xpath=//*[@id='fs-scope-page']/nav/div[@class='hp-page-label hp-preserve']/h1/a"
    ID_SCOPE_NAME = "xpath=//h1[@id='fs-scope-details-title']"
    ID_SCOPE_DESCRIPTION = "xpath=//div[@id='fs-scope-description']"
    ID_SCOPE_COUNT = "xpath=//span[@id='fs-settings-scope-overview-count']"
    ID_SCOPE_ERROR_TEXT = "xpath=//div[@id='hp-form-message']"
    ID_BUTTON_ACTION_MENU = "xpath=//div[@id='hp-form-message']"
    ID_SCOPE_NAME_VALIDATE_MSG = "css=label.hp-error"
    ID_SETTINGS_LINK = "xpath=//a[contains(text(),'Settings')]"
    ID_SCOPE_HELP_ICON = "xpath=//*[@id='hp-help-control']/div"
    ID_SCOPE_ACTIVITY_ICON = "xpath=//*[@id='hp-activity-control']"
    ID_SCOPE_MESSAGE = "xpath=//*[@id='hp-scopes-resource-show-empty']"
    ID_LIG_TABLE = "xpath=//*[@id='cic-switchtemplate-master-table']//*[contains(text(),'%s')]"
    ID_NETWORK_TABLE = "xpath=//*[@id='cic-network-master-table_wrapper']//*[contains(text(),'%s')]"
    ID_ENCLOSURE_TABLE = "xpath=//*[@id='DataTables_Table_0_wrapper']//*[contains(text(),'%s')]"
    ID_NETWORKSETS_TABLE = "xpath=//*[@id='cic-networkset-master-table_wrapper']//*[contains(text(),'%s')]"
    ID_INTERCONNECTS_TABLE = "xpath=//*[@id='cic-interconnects-master-table_wrapper']//*[contains(text(),'%s')]"
    ID_LI_TABLE = "xpath=.//*[@id='cic-logicalswitch-master-table_wrapper']//*[contains(text(),'%s')]"
    ID_SERVERHW_TABLE = "xpath=.//*[@class='dataTables_scrollBody']//*[contains(text(),'%s')]"
    ID_SCOPEASSIGN_ACTVITY = "xpath=.//*[@id='hp-activities']/tbody/tr[position()=1]//*[contains(text(),'Completed')]"


class CreateScopesElements(object):
    ID_BUTTON_CREATE_SCOPE = "//a[text()='Create scope']"
    ID_ACTION_MENU_CREATE_SCOPE = "id=fs-scope-create-action"
    ID_DIALOG_CREATE_SCOPE = "xpath=//section[@id='fs-scope-edit-section']"
    ID_DIALOG_CREATE_SCOPE_MESSAGE = "xpath=//span[@class='hp-form-message-text']"
    ID_DIALOG_CREATE_SCOPE_FORM_MESSAGE = "hp-form-changes"
    ID_INPUT_SCOPE_NAME = "id=fs-scope-create-name"
    ID_INPUT_SCOPE_DESCRIPTION = "id=fs-scope-create-description"
    ID_BUTTON_ADD_RESOURCE = "id=fs-scope-create-add-resources-button"
    ID_BUTTON_REMOVE_RESOURCE = "id=fs-scope-create-remove-resources-button"

    ID_DIALOG_ADD_RESOURCE = "id=fs-scope-add-resources-dialog"
    ID_COMBO_RESOURCE_CATEGORY = "id=fs-scope-add-resources-category-select-input"
    ID_INPUT_SEARCH_TEXT = "//input[@class='hp-search']"
    ID_TABLE_RESOURCE_NAME = "//form[@class='hp-add-form']//table/tbody/tr/td[text()='%s']"
    ID_ICON_REMOVE_RESOURCE = "//div[@id='fs-scope-create-resources-container']//tr[td[text()='%s']]/td/ol/li"
    ID_BUTTON_ADD = "id=fs-scope-add-resources-add-button"
    ID_BUTTON_ADD_AGAIN = "id=fs-scope-add-resources-add-again-button"
    ID_BUTTON_ADD_RESOURCE_CANCEL = "id=fs-scope-add-resources-cancel-button"

    ID_BUTTON_CREATE = "//input[@id='fs-scope-create-ok']"
    ID_BUTTON_CREATE_SCOPE_PLUS = "//input[@id='fs-scope-create-again']"
    ID_BUTTON_CREATE_SCOPE_CANCEL = "//*[@id='fs-scope-create-cancel']"


class EditScopesElements(object):
    ID_BUTTON_ACTIONS_EDIT_SCOPE = "//li[@id='fs-scope-edit-scope']/a"
    ID_BUTTON_ACTIONS = "xpath=//label[text()='Actions']"
    ID_DIALOG_EDIT_SCOPE = "id=fs-scope-edit-section"
    ID_INPUT_SCOPE_NAME = "id=fs-scope-create-name"
    ID_INPUT_SCOPE_DESCRIPTION = "id=fs-scope-create-description"
    ID_BUTTON_ADD_RESOURCE = "id=fs-scope-create-add-resources-button"
    ID_BUTTON_REMOVE_RESOURCE = "id=fs-scope-create-remove-resources-button"

    ID_DIALOG_ADD_RESOURCE = "id=fs-scope-add-resources-dialog"
    ID_COMBO_RESOURCE_CATEGORY = "id=fs-scope-add-resources-category-select-input"
    ID_COMBO_REMOVE_RESOURCE_CATEGORY = "id=fs-scope-remove-resources-category-select"
    ID_INPUT_SEARCH_TEXT = "//input[@class='hp-search']"
    ID_TABLE_RESOURCE_NAME = "//form[@class='hp-add-form']//table/tbody/tr/td[text()='%s']"
    ID_ICON_REMOVE_RESOURCE = "//div[@id='fs-scope-create-resources-container']//tr[td[text()='%s']]/td/ol/li"

    ID_SELECT_RESOURCE_NAME = "xpath=.//*[@id='fs-scope-remove-resources-selector']//tbody/tr/td[text()='%s']"
    ID_BUTTON_ADD = "id=fs-scope-add-resources-add-button"
    ID_BUTTON_ADD_AGAIN = "id=fs-scope-add-resources-add-again-button"
    ID_BUTTON_ADD_RESOURCE_CANCEL = "id=fs-scope-add-resources-cancel-button"

    ID_BUTTON_OK = "id=fs-scope-create-ok"
    ID_BUTTON_EDIT_SCOPE_CANCEL = "id=fs-scope-create-cancel"
    ID_BUTTON_REMOVE_RESOURCE_FROM_SCOPE = "id=fs-scope-remove-resources-remove-button"
    ID_BUTTON_ACTION_MENU = "xpath=//*[@id='fs-scope-actions']/label"
    ID_BUTTON_AUTH = "xpath=//*[@id='fs-scope-actions']/div/ol/li"


class DeleteScopesElements(object):
    ID_ACTION_MENU_DELETE_SCOPE = "//li[@id='fs-scope-delete-scope']/a"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_DIALOG_DELETE_SCOPE = "id=delete-scope-confirm-prompt"
    ID_BTN_DELETE_SCOPE = "id=delete-scope-confirm-ok"
    ID_BTN_CANCEL = "id=delete-scope-confirm-cancel"
    ID_BUTTON_CANCEL = "xpath=.//*[@id='fs-scope-remove-resources-cancel-button']"


class VerifyScopesElements(object):
    ID_VERIFY_DELETED_SCOPE_TITLE = "//h1[@id='hp-not-exist-title' and text()='%s']"
    ID_VERIFY_SCOPE_TITLE = "//h1[@id='fs-scope-details-title' and text()='%s']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_TABLE_SCOPE_DELETED = "//table/tbody//td[parent::tr[contains(@class, 'hp-not-found')] and text()='%s']"  # scope_name

    ID_LINK_SCOPE_RESOURCE_NAME = "//table[@id='fs-scope-resource-table']//a[text()='%s']"
    ID_ADD_RESOURCES_TABLE = "id=fs-scope-create-resources-container"
    ID_ADD_RESOURCES_TABLE_ITEM = "//div[@id='fs-scope-create-resources-container']//td[text()='%s']"
    ID_EDIT_RESOURCES_TABLE = "id=fs-scope-create-resources-container"
    ID_EDIT_RESOURCES_TABLE_ITEM = "//div[@id='fs-scope-create-resources-container']//td[text()='%s']"
    ID_CREATE_SCOPE_FORM_MESSAGE = "id=hp-form-changes"
    ID_INPUT_SCOPE_NAME = "id=fs-scope-create-name"
    ID_ICON_REMOVE_RESOURCE = "//div[@id='fs-scope-create-resources-container']//tr[td[text()='%s']]/td/ol/li"
    ID_SCOPE_TABLE = "xpath=//*[@id='cic-%s-filter']/div"
    ID_ALL_SCOPE = "xpath=.//*[@id='cic-%s-filter']/ol/li[text()='All scopes']"
    ID_FILTER_BY_TABLE_ITEM = "xpath=//*[@id='cic-%s-filter']/ol/li[text()='%s']"
    ID_PAGE_SELECT = "xpath=//*[@id='cic-%s-filter']"
    ID_ANY_RESOURCE = "xpath=.//*[@class='hp-options hp-select-all-or-any-options']/li[text()='Any']"
    ID_ALL_RESOURCE = "xpath=.//*[@class='hp-options hp-select-all-or-any-options']/li[text()='All']"
    ID_NETWORK_TABLE = "xpath=//*[@id='cic-network-master-table_wrapper']/div/div[1]/div/table/thead/tr/td[text()='Name']"
