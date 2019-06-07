'''
Created on Mar 4, 2014

@author: Administrator
'''


class GeneralVolumeElements(object):
    """
        General Elements found on Volume Page
    """
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Volumes']"
    ID_DROPDOWN_ACTIONS = "xpath=//div[@id='cic-storagevolumes-actions']"
    ID_VOLUMES_TITLE = "xpath=//*[@id='cic-storagevolumes-page']/nav/div[2]/h1]"
    ID_TABLE_VOLUME = "xpath=//table/tbody/tr/td[text()='%s']"  # volume
    ID_TABLE_VOLUMES = "xpath=//table/tbody/tr/td[2]"
    ID_TABLE_VOLUME_SELECTED = "xpath=//table/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"  # volume
    ID_TABLE_SELECTED_VOLUME_NAME = "xpath=//table/tbody/tr[contains(@class, 'hp-selected')]/td[2]"
    ID_TABLE_VOLUME_DELETED = "//table/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # volume
    ID_STATUS_VOLUME_OK = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # volume
    ID_STATUS_VOLUME_WARN = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"  # volume
    ID_STATUS_VOLUME_ERROR = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"  # volume
    UNABLE_TO_LOCATE_ERROR = "xpath=/html/body/div[2]/div[1]/div/div[3]/div[2]/section[2]/div/h1[text()='%s']"

    # ID_STATUS_ADD_NOTIFICATION = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div"
    ID_STATUS_NOTIFICATION_ONGOING = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-unknown']"
    ID_STATUS_NOTIFICATION_OK = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "//*[@id='cic-storagevolumes-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # volume
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # volume
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # volume
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    ID_TEXT_ACTIVITY_SPECIFACTION_OK = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # actionname, volume
    ID_TEXT_ACTIVITY_SPECIFACTION_WARN = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # actionname, volume
    ID_TEXT_ACTIVITY_SPECIFACTION_ERROR = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # actionname, volume
    ID_TEXT_GENERAL_STATE = "id=cic-storagevolumes-details-state"
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-storagevolumes-panel-selector"
    ID_SELECT_SNAPSHOTS_PANEL = "//ol[@class='hp-options']/li/a[text()='Snapshots']"
    ID_TABLE_SNAPSHOTS = "//*[@id='cic-storagevolumes-show-more-snapshots-table']/tbody/tr/td[3]"
    ID_TABLE_SNAPSHOT_NAME = "//*[@id='cic-storagevolumes-show-more-snapshots-table']/tbody/tr/td[contains(text(),'%s')]"  # snapshot name
    ID_TITLE_STORAGE_VOLUME_NAME = "id=cic-storagevolumes-details-title"
    ID_TEXT_TAB_STORAGE_VOLUME_NAVIGATION = "xpath=//*[@id='cic-storagevolumes-more-%s']/label/span"
    ID_LINK_STORAGE_POOLS = "xpath=//*[@id='cic-storagevolumes-details-pool']/a"
    ID_LINK_STORAGE_SYSTEMS = "xpath=//*[@id='cic-storagevolumes-details-array']/a"
    ID_LINK_SNAPSHOT_POOLS = "xpath=//*[@id='cic-storagevolumes-details-snapshotpool']/a"
    ID_LINK_VOLUME_TEMPLATE = "xpath=//*[@id='cic-storagevolumes-details-volume-template']/a"


class CreateVolumeElements(object):
    """
        Elements found on Create Volume Page
    """
    ID_BUTTON_CREATE_VOLUME = "link=Create volume"
    ID_SELECT_ACTION_CREATE = "id=cic-storagevolumes-create-action"
    ID_DIALOG_CREATE_VOLUME = "id=cic-storagevolumes-create-dialog"
    ID_INPUT_NAME = "xpath=//input[@id='cic-storagevolumes-name']"
    ID_INPUT_DESCRIPTION = "xpath=//textarea[@id='cic-storagevolumes-description']"
    ID_INPUT_VOLUME_TEMPLATE = "xpath=//input[@id='cic-storagevolumes-volume-template-input']"
    ID_SELECT_VOLUME_TEMPLATE = ID_INPUT_VOLUME_TEMPLATE + "/..//div[@class='hp-search-combo-menu']/ol[contains(@class,'hp-options')]/li[span[1][text()='%s'] or (span[1][text()='%s'] and span[2][contains(text(),'%s')])]/span[1]"  # volume template, volume template, poolname
    ID_INPUT_STORAGE_POOL = "xpath=//input[@id='cic-storagevolumes-pool-input']"
    ID_SELECT_STORAGE_POOL = ID_INPUT_STORAGE_POOL + "/../div[@class='hp-search-combo-spacer']/div[@class='hp-search-combo-menu']/ol/li[span[1][text()='%s'] or (span[1][text()='%s'] and span[2][contains(text(),'%s')])]/span[1]"  # pool name, pool name, storage name
    ID_INPUT_SNAPSHOT_STORAGE_POOL = "xpath=//input[@id='cic-storagevolumes-snapshotpool-input']"
    ID_SELECT_SNAPSHOT_STORAGE_POOL = ID_INPUT_SNAPSHOT_STORAGE_POOL + "/../div[@class='hp-search-combo-menu']/ol/li[span[1][text()='%s'] or (span[1][text()='%s'] and span[2][contains(text(),'%s')])]/span[1]/.."  # pool name, pool name, storage name
    ID_INPUT_CAPACITY = "xpath=//input[@id='cic-storagevolumes-capacity']"
    ID_DROPDOWN_PROVISIONING = "xpath=//li[@class='hp-form-item cic-storagevolumes-class-provisioning']/div/div/div/div[@class='hp-value']"
    ID_SELECT_PROVISIONING_THIN = "xpath=//li[@class='hp-form-item cic-storagevolumes-class-provisioning']/div/div/div/ol[@class='hp-options']/li/span[text()='Thin']"
    ID_SELECT_PROVISIONING_FULL = "xpath=//li[@class='hp-form-item cic-storagevolumes-class-provisioning']/div/div/div/ol[@class='hp-options']/li/span[text()='Full']"
    ID_RADIO_SHARING_PRIVATE = "xpath=//input[@id='cic-storagevolumes-pool-private']"
    ID_RADIO_SHARING_SHARED = "xpath=//*[@id='cic-storagevolumes-pool-shared']"
    ID_TOGGLE_IOPSLIMIT = "xpath=//*[@id='cic-storagevolumes-isiopslimitenabled-hpToggle']"
    ID_TOGGLE_DATATRANSFERLIMIT = "xpath=//*[@id='cic-storagevolumes-isDataTransferLimitEnabled-hpToggle']"
    ID_INPUT_IOPSLIMIT = "xpath=//*[@id='cic-storagevolumes-iopslimit']"
    ID_LABEL_IOPSLIMIT = "xpath=//*[@id='cic-storagevolumes-iopslimit-unlocked']/label"
    ID_INPUT_DATATRANSFERLIMIT = "xpath=//*[@id='cic-storagevolumes-dataTransferLimit']"
    ID_SELECT_PERFPOLICY = "xpath=//*[@id='cic-storagevolumes-performancePolicy-unlocked']/div[2]/div[3]/div/ol[2]/li/span[1][text()='%s']"
    ID_SELECT_FOLDER = "xpath=//*[@id='cic-storagevolumes-folder-unlocked']/div[2]/div[3]/div/ol[2]/li/span[text()='%s']"
    ID_SELECT_VOLUMESET = "xpath=//*[@id='cic-storagevolumes-volumeSet-unlocked']/div[2]/div[3]/div/ol/li/span[text()='%s']"
    ID_DROPDOWN_PERFPOLICY = "xpath=//*[@id='cic-storagevolumes-performancePolicy-unlocked']/div[2]/div[2]/div"
    ID_DROPDOWN_VOLUMESET = "xpath=//*[@id='cic-storagevolumes-volumeSet-unlocked']/div[2]/div[2]/div"
    ID_DROPDOWN_FOLDER = "xpath=//*[@id='cic-storagevolumes-folder-unlocked']/div[2]/div[2]/div"

    ID_BUTTON_CREATE = "xpath=//input[@id='cic-storagevolumes-create-ok']"
    ID_BUTTON_CREATE_PLUS = "xpath=//*[@id='cic-storagevolumes-create-plus']"
    ID_BUTTON_CANCEL = "//input[@id='cic-storagevolumes-create-cancel']"
    ID_TEXT_CREATING_VOLUME = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Creating volume')]"
    ID_TEXT_CREATE_ERROR_MESSAGE = "xpath=//*[@id='cic-storagevolumes-create-form']/footer/div[1]/div/div[2]/div[1]/span"
    ID_TEXT_IOPSLIMIT_ERROR_MESSAGE = "xpath=//*[@id='cic-storagevolumes-iopslimit-error']"


class AddVolumeElements(object):
    """
        Elements found on Add Volume Page
    """
    ID_BUTTON_ADD_VOLUME = "xpath=//a[text()='Add volume']"
    ID_DIALOG_ADD_VOLUME = "id=cic-storagevolumes-add-dialog"
    ID_INPUT_STORAGE_SYSTEM = "id=cic-storagevolumes-add-storagesystem-input"
    ID_SELECT_STORAGE_SYSTEM = "//*[@id='cic-storagevolumes-add-storagesystem-input']/..//div[@class='hp-search-combo-menu']/ol/li/span[text()='%s']"  # storage system
    ID_INPUT_STORAGE_SYSTEM_VOLUME_NAME = "id=cic-storagevolumes-add-id"
    ID_INPUT_DESCRIPTION = "id=cic-storagevolumes-add-description"
    ID_RADIO_SHARING_PRIVATE = "id=cic-storagevolumes-add-pool-private"
    ID_RADIO_SHARING_SHARED = "id=cic-storagevolumes-add-pool-shared"
    ID_BUTTON_ADD = "id=cic-storagevolumes-add-ok"
    ID_BUTTON_ADD_PLUS = "id=cic-storagevolumes-addplus"
    ID_BUTTON_CANCEL = "id=cic-storagevolumes-add-cancel"
    ID_TEXT_ADDING_VOLUME = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Adding volume')]"
    ID_TEXT_ADD_ERROR_MESSAGE = "xpath=//*[@id='cic-storagevolumes-add-form']/footer/div[1]/div/div[2]/div[1]/span"


class EditVolumeElements(object):
    """
        Elements found on Edit Volume Page
    """
    ID_SELECT_ACTION_EDIT = "id=cic-storagevolumes-edit-action"
    ID_DIALOG_EDIT = "id=cic-storagevolumes-edit-dialog"
    ID_INPUT_NAME = "id=cic-storagevolumes-name"
    ID_INPUT_DESCRIPTION = "id=cic-storagevolumes-description"
    ID_DROPDOWN_VOLUME_TEMPLATE = "xpath=//*[@id='cic-storagevolumes-template-select-container']/div/div[2]/div[2]/div"
    ID_SELECT_VOLUME_TEMPLATE = "//*[@id='cic-storagevolumes-template-select-container']/div/div[2]/div[3]/div/ol[2]/li/span[1][text()='%s']"  # volume template, volume template, poolname
    ID_TEXT_STORAGE_POOL = "xpath=//*[@id='cic-storagevolumes-edit-pool']"
    ID_INPUT_SNAPSHOT_STORAGE_POOL = "id=cic-storagevolumes-snapshotpool-input"
    ID_SELECT_SNAPSHOT_STORAGE_POOL = "xpath=//*[@id='cic-storagevolumes-snapshotpool-input']/../div[@class='hp-search-combo-menu']/ol/li[span[1][text()='%s'] or (span[1][text()='%s'] and span[2][contains(text(),'%s')])]/span[1]"  # pool name, pool name, storage name
    ID_INPUT_CAPACITY = "id=cic-storagevolumes-capacity"
    ID_TEXT_PROVISIONING = "id=cic-storagevolumes-provisioning"
    ID_RADIO_SHARING_PRIVATE = "id=cic-storagevolumes-pool-private"
    ID_RADIO_SHARING_SHARED = "id=cic-storagevolumes-pool-shared"
    ID_TOGGLE_IOPSLIMIT = "xpath=//*[@id='cic-storagevolumes-isiopslimitenabled-hpToggle']"
    ID_TOGGLE_DATATRANSFERLIMIT = "xpath=//*[@id='cic-storagevolumes-isDataTransferLimitEnabled-hpToggle']"
    ID_INPUT_IOPSLIMIT = "xpath=//*[@id='cic-storagevolumes-iopslimiT']"
    ID_INPUT_DATATRANSFERLIMIT = "xpath=//*[@id='cic-storagevolumes-dataTransferLimit']"
    ID_SELECT_PERFPOLICY = "xpath=//*[@id='cic-storagevolumes-performancePolicy-unlocked']/div[2]/div[3]/div/ol[2]/li/span[1][text()='%s']"
    ID_SELECT_FOLDER = "xpath=//*[@id='cic-storagevolumes-folder-unlocked']/div[2]/div[3]/div/ol[2]/li/span[text()='%s']"
    ID_SELECT_VOLUMESET = "xpath=//*[@id='cic-storagevolumes-volumeSet-unlocked']/div[2]/div[3]/div/ol[2]/li/span[1][text()='%s']"
    ID_DROPDOWN_PERFPOLICY = "xpath=//*[@id='cic-storagevolumes-performancePolicy-unlocked']/div[2]/div[2]/div"
    ID_DROPDOWN_VOLUMESET = "xpath=//*[@id='cic-storagevolumes-volumeSet-unlocked']/div[2]/div[2]/div"
    ID_DROPDOWN_FOLDER = "xpath=//*[@id='cic-storagevolumes-folder-unlocked']/div[2]/div[2]/div"

    ID_BUTTON_OK = "id=cic-storagevolumes-edit-ok"
    ID_BUTTON_CANCEL = "id=cic-storagevolumes-edit-cancel"
    ID_TEXT_EDITING_VOLUME_TEMPLATE = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Updating volume')]"
    ID_TEXT_INCONSISTENT_WARNING_MESSAGE = "id=cic-storagevolumes-%s-warning-msg"


class DeleteVolumeElements(object):
    """
        Elements found on Delete Volume Page
    """
    ID_SELECT_ACTION_DELETE = "id=cic-storagevolumes-delete-action"
    ID_DIALOG_DELETE = "id=cic-storagevolumes-delete-confirm-header"
    ID_RADIO_DELETE_VOLUME_FROM_ONEVIEW_AND_THE_STORAGE_SYSTEM = "id=cic-storagevolumes-delete-deletion-option"
    ID_RADIO_DELETE_VOLUME_FROM_ONEVIEW_ONLY = "id=cic-storagevolumes-delete-export-option"
    ID_BUTTON_YES_DELETE = "xpath=//button[text()='Yes, delete']"
    ID_BUTTON_CANCEL = "xpath=//button[text()='Cancel']"


class RefreshVolumeElements(object):
    """
        Elements found on Refresh Volume Page
    """
    ID_SELECT_ACTION_REFRESH = "xpath=//div[@id='cic-storagevolumes-actions']//a[text()='Refresh']"
    ID_TEST_REFRESH_ONGOING = "xpath=//*[@id='cic-storagevolumes-details-state' and text()='Refreshing']"
    ID_TEXT_REFRESH_COMPLETED = "xpath=//*[@id='cic-storagesystems-details-state' and text()='Configured']"


class CreateVolumeSnapshotElements(object):
    """
        Elements found on Create Volume Snapshot Page
    """
    ID_SELECT_ACTION_CREATE_SNAPSHOT = "xpath=//div[@id='cic-storagevolumes-actions']//a[text()='Create snapshot']"
    ID_DIALOG_CREATE_SNAPSHOT = "id=hp-dialog-container"
    ID_INPUT_NAME = "xpath=//*[@id='cic-storagevolumes-create-snapshot-token']/../div[@class='hp-tokens']"
    ID_TEXT_NAME_TOKENS = "xpath=//div[contains(@class, 'hp-token-text')]/div[@class='hp-tokens']"
    ID_INPUT_NAME_CURSOR = "xpath=//div[@class='hp-token-text hp-editable hp-active']/div/span[@class='hp-cursor']"
    ID_SELECT_NAME_VOLUME_NAME = "//div/ul/li/span[text()='Volume name']"
    ID_SELECT_NAME_TIMESTAMP = "//div/ul/li/span[text()='Timestamp']"
    ID_INPUT_DESCRIPTION = "id=cic-storagevolumes-create-snapshot-description"
    ID_BUTTON_CREATE = "id=cic-storagevolumes-create-snapshot-create"
    ID_BUTTON_CANCEL = "id=cic-storagevolumes-create-snapshot-cancel"
    ID_TEXT_CREATE_SNAPSHOT_ERROR_MESSAGE = "xpath=//*[@id='hp-form-message']/div[1]"
    ID_TEXT_SNAPSHOT_NAME_ERROR = "id=cic-storagevolumes-create-snapshot-form"

    ID_TEXT_CREATING_SNAPSHOT = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Creating snapshot')]"


class DeleteVolumeSnapshotElements(object):
    """
        Elements found on Delete Volume Snapshot Page
    """
    ID_ICON_SNAPSHOT_DELETE = "xpath=//*[@id='cic-storagevolumes-show-more-snapshots-table']/tbody/tr/td[6]/a/div"
    ID_DIALOG_DELETE_SNAPSHOT = "id=cic-storagevolumes-delete-snapshots-confirm-header"
    ID_BTN_YES_DELETE_2 = "xpath=//*[@id='hp-body-div']/div[8]/div/div/div/footer/div/button[1]"
    ID_BTN_YES_DELETE = "xpath=//*[@id='hp-body-div']/div[9]/div/div/div/footer/div/button[1]"


class RevertVolumeSnapshotElements(object):
    """
        Elements found on Revert Volume Snapshot Page
    """
    ID_BUTTON_REVERT = "xpath=//td[text()='%s']/ancestor::tr/td/a[text()='Revert']"
    ID_BUTTON_YES_REVERT = "id=cic-storagevolumes-revert-snapshot-yes"


class CreateVolumeUsingSnapshotElements(object):
    """
        Elements found on Create Volume Using Snapshot Page
    """
    ID_BUTTON_CREATE_VOLUME = "xpath=//td[text()='%s']/ancestor::tr/td/a[text()='Create volume']"
    ID_INPUT_VOLUME_NAME = "id=cic-storagevolumes-name"
    ID_INPUT_DESCRIPTION = "id=cic-storagevolumes-description"
    ID_RADIO_PRIVATE_VOLUME = "xpath=//input[@id='cic-storagevolumes-pool-private']"
    ID_RADIO_SHARED_VOLUME = "xpath=//*[@id='cic-storagevolumes-pool-shared']"
    ID_BUTTON_CREATE = "id=cic-storagevolumes-promote-ok"
    ID_BUTTON_CANCEL = "id=cic-storagevolumes-promote-cancel"
    ID_INPUT_STORAGE_POOL = "xpath=//input[@id='cic-storagevolumes-pool-input']"
    ID_INPUT_SNAPSHOT_STORAGE_POOL = "id=cic-storagevolumes-snapshotpool-input"
    ID_SELECT_STORAGE_POOL = ID_INPUT_STORAGE_POOL + "/../div[@class='hp-search-combo-spacer']/div[@class='hp-search-combo-menu']/ol/li[span[1][text()='%s'] or (span[1][text()='%s'] and span[2][contains(text(),'%s')])]/span[1]"  # pool name, pool name, storage name
    ID_SELECT_SNAPSHOT_STORAGE_POOL = "xpath=//input[@id='cic-storagevolumes-snapshotpool-input']/../div[@class='hp-search-combo-menu']/ol/li[span[text()='%s'] or (span[text()='%s'] and span[contains(text(),'%s')])]/span[@class='hp-name']"  # pool name, pool name, storage name
    ID_TEXT_CREATING_VOLUME = "xpath=//*[@id='hp-form-message']/div[1]/span[contains(.,'Creating volume')]"
    ID_TEXT_CREATE_ERROR_MESSAGE = "xpath=//*[@id='cic-storagevolumes-promote-form']/footer/div[1]/div/div[2]/div[1]/span"
