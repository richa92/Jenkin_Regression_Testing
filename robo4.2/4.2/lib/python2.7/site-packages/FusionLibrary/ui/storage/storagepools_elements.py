'''
Created on Mar 11, 2014
'''


class FusionStoragePoolsPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Storage Pools']"
    # ID_TABLE_STORAGE_POOL_FIND = "xpath=//table[@id='DataTables_Table_1']/tbody/tr/td[text()='%s']"
    ID_TABLE_STORAGE_POOL_FIND = "xpath=//td[@class='' and text()='%s']"
    ID_ELEMENT_POOL_DELETED = "//table//tr[contains(@class, 'hp-not-found')] and td[text()='%s'] and td[text()='%s']]"
    ID_ELEMENT_POOL_NAME_BASE = "xpath=//td[@class='hp-identifier' and text()='%s']"
    ID_ALL_STORAGE_POOL_LIST = "xpath=//table[@id='DataTables_Table_5']/tbody/tr/td[2]"

    # Action Menu
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_REFRESH = "link=Refresh"
    ID_MENU_ACTION_REMOVE = "link=Remove"

    # Add Storage Pool
    ID_LINK_ADD_STORAGE_POOL = "link=Add storage pool"
    ID_INPUT_STORAGE_SYSTEM = "xpath=//input[@id='cic-storage-pools-add-storagearray-select-input']"
    ID_DROPDOWN_SELECT_STORAGE = "xpath=.//*[@id='cic-storage-pools-add-form']/div/fieldset/ol/li[2]/div/div/div[3]/ol[descendant::span[contains(.,'%s')]]"
    ID_INPUT_STORAGE_POOL = "xpath=//input[@id='cic-storage-pools-add-pool-select-input']"
    ID_DROPDOWN_SELECT_POOL = "xpath=//*[@id='cic-storage-pools-add-form']//div[@class='hp-search-combo-menu']/ol[descendant::span[contains(.,'%s')]]"
    ID_LABEL_ERROR_ADD_CUSTOM = "xpath=//label[@class='hp-error']"
    ID_BTN_ADD = "id=cic-storage-pools-add"
    ID_BTN_ADD_PLUS = "id=cic-storage-pools-addplus"
    ID_BTN_CANCEL = "id=cic-storage-pools-add-cancel"
    ID_LABEL_AFTER_ADD_PLUS = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Adding storage pool')]"

    # Refresh
    ID_PROGRESS = "xpath=//div[@class='hp-progress']"
    ID_STATUSBAR_EDIT = "xpath=//div[@id='hp-activity-notification']/div[@class='hp-message']"
    ID_LABEL_NOTIFICATION = "xpath=//div[@id='hp-page-notifications']//header[@class='hp-notification-summary']"
    ID_LABEL_NOTIFICATION_COMPLETED = "xpath=//div[@id='hp-page-notifications']//header[@class='hp-notification-summary']/div[text()='Completed']"

    # Remove
    ID_REMOVE_POOL_CONFIRM = "xpath=//button[@id='cic-confirm-ok' and text() ='Yes, remove']"
    ID_MESSAGE_WARNING = "xpath=//div[@class='hp-dialog']//div[@class='hp-notify hp-notify-warning hp-active']"
    ID_LABEL_STORAGE_SYSTEM = "xpath=//*[@id='DataTables_Table_0']/tbody/tr/td[preceding-sibling::td[text()='%s']]"
    ID_BTN_WARNING_CLOSE = "xpath=//footer/div/button"
