'''
Created on Mar 20, 2014
'''


class FusionStorageTemplatesPage(object):

    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Volume Templates']"
    ID_TABLE_STORAGE_TEMPLATE_FIND = "xpath=//td[@class='' and text()='%s']"
    ID_ALL_STORAGE_TEMPLATE_LIST = "xpath=//*[@class='dataTables_scrollBody']//tbody/tr/td[2]"

    # Action Menu
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_EDIT = "link=Edit"
    ID_MENU_ACTION_EDIT_SETTINGS = "link=Edit Settings"
    ID_MENU_ACTION_DELETE = "link=Delete"

    # create storage volume template
    ID_LINK_CREATE_STORAGE_TEMPLATE = "link=Create volume template"
    ID_INPUT_STORAGE_TEMPLATE_NAME = "id=cic-storagetemplates-add-name"
    ID_INPUT_STORAGE_TEMPLATE_DESCRIPTION = "id=cic-storagetemplates-add-description"
    ID_INPUT_STORAGE_POOL = "xpath=//input[@id='cic-storagetemplates-add-pool-input']"
    ID_DROPDOWN_STORAGE_POOL = "xpath=//*[@id='cic-storagetemplates-add-form']//div[@class='hp-search-combo-menu']/ol[descendant::span[contains(.,'%s')]]"
    ID_INPUT_STORAGE_CAPACITY = "id=cic-storagetemplates-add-capacity"
    ID_SELECT_PROVISIONING = "xpath=//li[@id='cic-storagetemplates-add-volume-properties']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//div[@class='hp-value']"
    ID_DROPDOWN_PROVISIONING = "xpath=//li[@id='cic-storagetemplates-add-volume-properties']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//ol[@class='hp-options']//span[text()='%s']"
    ID_CHECKBOX_SHARED = "id=cic-storagetemplates-add-pool-shared"
    ID_CHECKBOX_PRIVATE = "id=cic-storagetemplates-add-pool-private"
    ID_LABEL_ERROR_ADD_CUSTOM = "xpath=//label[@class='hp-error']"
    ID_BTN_CREATE = "id=cic-storagetemplates-add-ok"
    ID_BTN_CREATE_PLUS = "id=cic-storagetemplates-addplus"
    ID_BTN_ADD_CANCEL = "//input[@id='cic-storagetemplates-add-cancel']"
    ID_LABEL_AFTER_CREATE_PLUS = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Creating volume template')]"

    # Edit Storage Volume Template
    ID_INPUT_EDIT_STORAGE_VOLUME_TEMPLATE = "id=cic-storagetemplates-edit-name"
    ID_INPUT_EDIT_STORAGE_TEMPLATE_DESCRIPTION = "id=cic-storagetemplates-edit-description"
    ID_INPUT_EDIT_STORAGE_POOL = "xpath=//input[@id='cic-storagetemplates-edit-pool-input']"
    ID_DROPDOWN_EDIT_STORAGE_POOL = "xpath=//*[@id='cic-storagetemplates-edit-form']//div[@class='hp-search-combo-menu']/ol[descendant::span[contains(.,'%s')]]"
    ID_INPUT_EDIT_STORAGE_CAPACITY = "id=cic-storagetemplates-edit-capacity"
    ID_SELECT_EDIT_PROVISIONING = "xpath=//li[@id='cic-storagetemplates-edit-volume-properties']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//div[@class='hp-value']"
    ID_DROPDOWN_EDIT_PROVISIONING = "xpath=//li[@id='cic-storagetemplates-edit-volume-properties']/fieldset/ol/li[descendant::label[contains(.,'Provisioning')]]//ol[@class='hp-options']//span[text()='%s']"
    ID_CHECKBOX_EDIT_SHARED = "id=cic-storagetemplates-edit-pool-shared"
    ID_CHECKBOX_EDIT_PRIVATE = "id=cic-storagetemplates-edit-pool-private"
    ID_LABEL_ERROR_EDIT_CUSTOM = "xpath=//label[@class='hp-error']"
    ID_BTN_EDIT_OK = "id=cic-storagetemplates-edit-ok"
    ID_BTN_EDIT_CANCEL = "id=cic-storagetemplates-edit-cancel"
    ID_LABEL_AFTER_EDIT = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Editing volume template')]"

    # Edit Settings
    ID_CHECKBOX_REQUIRED_FOR_STORAGE = "id=cic-storagetemplates-edit-settings-require-template"
    ID_BTN_OK = "xpath=//input[@id='cic-storagetemplates-edit-settings-ok']"
    ID_BTN_CANCEL = "xpath=.//input[@id='cic-storagetemplates-edit-settings-cancel']"

    # Delete Storage Volume template
    ID_BTN_YES_DELETE = "id=cic-confirm-ok"
    ID_POPUP_DELETE_VT_ERROR = "xpath=//span[@id='cic-delete-error-message']"
    ID_POPUP_DELETE_VT_ERR_RESOLUTION = "xpath=//span[@id='cic-delete-error-resolution']"
    ID_POPUP_BTN_CANCEL = "css=button.hp-cancel"
    ID_RESET_FILTER = "link=Reset"
