'''
Created on Mar 4, 2019

@author: Administrator
'''


class GeneralVolumeSetElements(object):
    """
        General Elements used on the Volume Sets Page
    """
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Volume Sets']"
    ID_VOLUMESET_TITLE = "xpath=//*[@id='cic-storagevolumesets-page']/nav/div[2]/h1/text()='%s']"
    ID_TABLE_VOLUMESET = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]"  # storage-pools
    ID_TABLE_VOLUMESET_SELECTED = "xpath=//table/tbody/tr[contains(@class, hp-selected) and td[text()='%s'] and td[text()='%s']]"  # storage-pools
    ID_STATUS_VOLUMESET_OK = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-ok']"  # storage-pools
    ID_STATUS_VOLUMESET_WARN = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-warning']"  # storage-pools
    ID_STATUS_VOLUMESET_ERROR = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-error']"  # storage-pools
    ID_STATUS_VOLUMESET_DISABLED = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div[@class='hp-status hp-status-disabled']"  # storage-pools
    ID_STATUS_VOLUMESET = "xpath=//table/tbody/tr[td[text()='%s'] and td[text()='%s']]/td/div/span"
    ID_LINK_USED_BY_VOLUMES = "xpath=//*[@id='cic-storagevolumesets-overview-usedby-volumecount']/a[text()='%s']"

    # action button should not exist
    ID_ACTION_BUTTON = "xpath=//*[@id='cic-storagesystems-actions']"

    ID_INPUT_APP_SYNC = "xpath=//*[@id='cic-storagevolumesets-overview-applicationsync']"
    ID_INPUT_REPL_PARTNER = "xpath=//*[@id='ic-storagevolumesets-overview-replicationpartner']"
    ID_INPUT_LAST_SNAPSHOT = "xpath=//*[@id='cic-storagevolumesets-overview-lastsnapshot']"
    ID_INPUT_SNAPSHOT_COLLECTION = "xpath=//*[@id='cic-storagevolumesets-overview-snapshotcollections'"
    ID_LINK_USED_BY_STORAGE_SYSTEM = "xpath=//*[@id='cic-storagevolumesets-overview-storagesystem']/a"

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
    ID_LINK_STORAGE_SYSTEMS = "xpath=//*[@id='cic-storagevolumesets-overview-storagesystem']/a"
    ID_LINK_USED_BY_VOLUMES = "xpath=//*[@id='cic-storagevolumesets-overview-usedby-volumecount']/a"
    ID_LINK_USED_BY_TEMPLATES = "xpath=//*[@id='cic-storagevolumesets-overview-usedby-templatecount']/a"
