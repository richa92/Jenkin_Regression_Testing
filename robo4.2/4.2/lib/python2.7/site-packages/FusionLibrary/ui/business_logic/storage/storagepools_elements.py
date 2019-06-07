'''
Created on Mar 4, 2014

@author: Administrator
'''


class GeneralStoragePoolElements(object):
    '''
        Storage Pool Elements
    '''
    ID_BUTTON_ACTIONS = "xpath=//label[text()='Actions']"
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Storage Pools']"
    ID_TABLE_STORAGE_POOL = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]"  # storage-pools
    ID_TABLE_STORAGE_POOL_SELECTED = "xpath=//table/tbody/tr[contains(@class, hp-selected) and td[text()='%s'] and td[text()='%s']]"  # storage-pools
    ID_STATUS_STORAGE_POOL_OK = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-ok']"  # storage-pools
    ID_STATUS_STORAGE_POOL_WARN = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-warning']"  # storage-pools
    ID_STATUS_STORAGE_POOL_ERROR = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-error']"  # storage-pools
    ID_STATUS_STORAGE_POOL_DISABLED = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-disabled']"  # storage-pools
    ID_STATUS_STORAGE_POOL = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div/span"

    ID_STATUS_ADD_NOTIFICATION = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div"
    ID_STATUS_NOTIFICATION_ONGOING = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-unknown']"
    ID_STATUS_NOTIFICATION_OK = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "//*[@id='cic-storage-pools-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # storagesystem
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # storagesystem
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    ID_TEXT_GENERAL_STATE = "//*[@id='cic-storage-pools-details-state']"
    ID_LINK_STORAGE_SYSTEMS = "xpath=//*[@id='cic-storage-pools-details-array']/a"
    ID_LINK_USED_BY_VOLUMES = "xpath=//*[@id='cic-storage-pools-details-array-volumes']/a"
    ID_LINK_USED_BY_TEMPLATES = "xpath=//*[@id='cic-storage-pools-details-array-templates']/a"


class EditStoragePoolElements(object):
    '''
        Elements used on the Edit Storage Pool Page
    '''
    ID_SELECT_ACTION_EDIT = "//li[@id='cic-storage-pools-edit-action']/a"
    ID_DIALOG_EDIT_STORAGE_POOL = "//div[@id='cic-storage-pools-edit-dialog']"
    ID_RADIO_STATE_MANAGED = "//input[@id='cic-storage-pools-state-managed']"
    ID_RADIO_STATE_DISCOVERED = "//input[@id='cic-storage-pools-state-discovered']"
    ID_BUTTON_OK = "//input[@id='cic-storage-pools-edit']"
    ID_BUTTON_CANCEL = "//input[@id='cic-storage-pools-edit-cancel']"


class RefreshStoragePoolElements(object):
    '''
        Elements used on the Refresh Storage Pool Page
    '''
    ID_SELECT_ACTION_REFRESH = "id=cic-storage-pools-refresh-action"
    # ID_TEXT_GENERAL_STATE = "id=cic-storage-pools-details-state"
    ID_TEST_REFRESH_ONGOING = "xpath=//*[@id='cic-storage-pools-details-state' and text()='Refreshing']"
    ID_TEXT_REFRESH_COMPLETED = "xpath=//*[@id='cic-storage-pools-details-state' and text()='Configured']"
