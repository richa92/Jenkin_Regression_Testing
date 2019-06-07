'''
Created on Apr 2, 2014

@author: Administrator
'''


class FusionStorageVolumesPage(object):

    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Volumes']"
    ID_TABLE_VOLUMES_FIND = "xpath=//*[@class='dataTables_scrollBody']//tbody/tr/td[2][text()='%s']"
    ID_ALL_VOLUMES_LIST = "xpath=//tbody/tr/td[2]"

    # Action Menu
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ADD = "link=Add"
    ID_MENU_ACTION_EDIT = "link=Edit"
    ID_MENU_ACTION_REFRESH = "link=Refresh"
    ID_MENU_ACTION_DELETE = "link=Delete"

    # Create Volume
    ID_LINK_CREATE_VOLUME = "link=Create volume"
    ID_INPUT_VOLUME_NAME = "id=cic-storagevolumes-create-name"
    ID_INPUT_DESCRIPTION = "id=cic-storagevolumes-create-description"
    ID_INPUT_STORAGE_TEMPLATE = "id=cic-storagevolumes-create-volume-template-input"
    ID_DROPDOWN_SELECT_STORAGE_TEMPLATE = "xpath=//form[@id='cic-storagevolumes-create-form']//div[@class='hp-search-combo-menu']/ol[descendant::span[contains(.,'%s')]]"
    ID_SELECT_PROVISIONING_MODEL = "xpath=//form[@id='cic-storagevolumes-create-form']//div[@class='hp-select']/div[@class='hp-value']"
    ID_SELECT_PROVISIONING_THIN = "xpath=//form[@id='cic-storagevolumes-create-form']//ol/li[@data-id='Thin']/span[contains(.,'Thin')]"
    ID_SELECT_PROVISIONING_FULL = "xpath=//form[@id='cic-storagevolumes-create-form']//ol/li[@data-id='Full']/span[contains(.,'Full')]"
    ID_PROVISIONING_MODEL_TABLE = "id=cic-storagevolumes-details-provisioning"
    ID_INPUT_STORAGE_VOLUME_CAPACITY = "id=cic-storagevolumes-create-capacity"
    ID_RADIO_SHARING_PRIVATE = "id=cic-storagevolumes-create-pool-private"
    ID_RADIO_SHARING_SHARED = "id=cic-storagevolumes-create-pool-shared"
    ID_LABEL_ERROR_ADD_CUSTOM = "xpath=//label[@class='hp-error']"
    ID_BTN_CREATE_CANCEL = "id=cic-storagevolumes-create-cancel"
    ID_BTN_CREATE_PLUS = "id=cic-storagevolumes-addplus"
    ID_BTN_CREATE = "id=cic-storagevolumes-create-ok"
    ID_LABEL_AFTER_CREATE_PLUS = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Creating volume')]"
    ID_CREATE_POOL_INPUT = "id=cic-storagevolumes-create-pool-input"
    # edit volume
    ID_INPUT_VOLUME_NAME_EDIT = "id=cic-storagevolumes-edit-name"
    ID_INPUT_DESCRIPTION_EDIT = "id=cic-storagevolumes-edit-description"
    ID_RADIO_SHARING_PRIVATE_EDIT = "id=cic-storagevolumes-edit-pool-private"
    ID_RADIO_SHARING_SHARED_EDIT = "id=cic-storagevolumes-edit-pool-shared"
    ID_BTN_EDIT_OK = "id=cic-storagevolumes-edit-ok"
    ID_BTN_EDIT_CANCEL = "id=cic-storagevolumes-edit-cancel"
    ID_LABEL_AFTER_EDIT = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Editing volume')]"  # Obsolete?
    ID_INPUT_STORAGE_VOLUME_CAPACITY_EDIT = "id=cic-storagevolumes-edit-capacity"
    # ID_LABEL_PAGE_NOTIFICATION = "xpath=//div[@id='hp-page-notifications']/div[@class='hp-notification']/header"
    ID_LABEL_PAGE_NOTIFICATION = "xpath=//div[@id='hp-page-notifications']/div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-state']"
    ID_LABEL_PAGE_OKAY = "//header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_LABEL_PAGE_ERROR = "xpath=.//div[@id='hp-page-notifications']/div[1]/header/div[@class='hp-status hp-status-error']"
    ID_LABEL_PAGE_ERROR_FULL = "xpath=//div[@id='hp-page-notifications']/div[@class='hp-notification']/div"
    # ID_STATUSBAR_EDIT = "xpath=//div[@id='hp-page-notifications']//header//div[@class='hp-progress']"
    ID_STATUSBAR_EDIT = "xpath=//div[@id='hp-activity-notification']/div[@class='hp-message']"
    # delete
    ID_RADIO_DELETE_APPLIANCE_AND_STORAGE = "id=cic-storagevolumes-delete-deletion-option"
    ID_RADIO_DELETE_APPLIANCE_ONLY = "id=cic-storagevolumes-delete-export-option"
    ID_REMOVE_POOL_CONFIRM = "xpath=//button[@class='hp-ok hp-primary' and text() ='Yes, delete']"

    # Add Label to Volume
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-storagevolumes-panel-selector"
    ID_DROPDOWN_LABEL_LINK = "link=Labels"
    ID_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/span[text()='Labels']"
    ID_EDIT_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/a[@class='hp-panel-edit' and text()='Edit']"
    ID_EDIT_LABEL_PANEL = "xpath = //header[@id='hp-labels-edit-header']/h1/span[text()='Edit Labels']"
    ID_LABEL_NAME = "id=hp-labels-edit-search-input"
    ID_ADD_LABEL_BTN = "id=hp-labels-edit-add"
    ID_OK_LABEL_BTN = "id=hp-labels-edit-ok"
    ID_ADDED_LABEL = "xpath = //table[@id='hp-labels-show-table']/descendant::a[text()='%s']"
    ID_RESET_FILTER = "link=Reset"
    ID_ERROR_MESSAGE = "xpath = //label[@class='hp-error']"
    ID_CANCEL_LABEL_BTN = "xpath = //a[@id='hp-labels-edit-cancel']"

    # dropdown
    ID_DROPDOWN = "id=cic-storagevolumes-panel-selector"
    ID_DROPDOWN_SELECTION = "link=Labels"

    # Add storage volume
    ID_LINK_ADD_VOLUME = "link=Add volume"
    ID_INPUT_STORAGE_SYSTEM = "id=cic-storagevolumes-add-storagesystem-input"
    ID_INPUT_STORAGE_VOLUME = "id=cic-storagevolumes-add-id"
    ID_INPUT_ADD_DESCRIPTION = "id=cic-storagevolumes-add-description"
    ID_RADIO_SHARED_POOL = "id=cic-storagevolumes-add-pool-shared"
    ID_BTN_ADD_STORAGE_VOL = "id=cic-storagevolumes-add-ok"
    ID_TXT_ADD_VOLUME = "xpath = //footer[@class='hp-footer']//span[contains(text(), 'Adding volume')]"
    ID_ELEMENT_ADD_VOL_ERR_MSG = "xpath = //footer[@class='hp-footer']//div[div/span[contains(text(), 'Unable to add volume')]]"
