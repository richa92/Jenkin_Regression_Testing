class DriveEnclosuresElements(object):
    # Drive Bay
    ID_EMPTY_DRIVE_BAY = "xpath=//li[@class='hp-bay hp-empty']"
    ID_EMPTY_DRIVE_BAY_NUMBER = ID_EMPTY_DRIVE_BAY + "/label[text()='%s']"
    ID_EMPTY_DRIVE_BAY_BY_NUMBER = ID_EMPTY_DRIVE_BAY_NUMBER + "/.."
    ID_EMPTY_DRIVE_BAY_BY_NUMBER_AND_CAPACITY = ID_EMPTY_DRIVE_BAY_BY_NUMBER + "//div[text()='empty']"
    ID_DRIVE_BAY = "xpath=//li[@class='hp-bay']"
    ID_DRIVE_BAY_NUMBER = ID_DRIVE_BAY + "/label[text()='%s']"
    ID_DRIVE_BAY_BY_NUMBER = ID_DRIVE_BAY_NUMBER + "/.."
    ID_DRIVE_BAY_BY_NUMBER_AND_CAPACITY = ID_DRIVE_BAY_BY_NUMBER + "//div[@id='cic-dfrm-jbod-bay-drive-capacity'][text()='%s']"
    ID_DRIVE_BAY_STATUS_BY_BAY_NUMBER = ID_DRIVE_BAY_BY_NUMBER + "//span[@class='hp-value'][text()='%s']"
    ID_DRIVE_BAY_UID_OFF_BY_BAY_NUMBER = ID_DRIVE_BAY_BY_NUMBER + "//div[@class='hp-uid']"
    ID_DRIVE_BAY_UID_ON_BY_BAY_NUMBER = ID_DRIVE_BAY_BY_NUMBER + "//div[@class='hp-uid' 'hp-on']"
    # Drive Bay Hover Over
    ID_DRIVE_BAY_HOVER_OVER = "//div[@class='hp-flyout-content']"
    ID_DRIVE_BAY_NUMBER_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//div[@id='cic-dfrm-jbod-bay-number'][text()='Bay %s']"
    ID_DRIVE_STATUS_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//span[@class='hp-value'][text()='%s']"
    ID_DRIVE_CAPACITY_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//div[@id='cic-dfrm-jbod-drive-capacity'][text()='%s']"
    ID_DRIVE_TYPE_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//div[@id='cic-dfrm-jbod-drive-type'][text()='%s']"
    ID_DRIVE_LOGICAL_JBOD_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//div[@id='cic-dfrm-jbod-logical-jbod']/div[text()='%s']"
    ID_DRIVE_SERVER_PROFILE_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//div[@class='hp-fields']//div[@id='cic-dfrm-jbod-server-profile']/div[text()='%s']"
    ID_DRIVE_UID_OFF_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//div[@class='hp-uid']"
    ID_DRIVE_UID_ON_IN_HOVER_OVER = ID_DRIVE_BAY_HOVER_OVER + "//div[@class='hp-uid hp-on']"
    # 'Drives' View
    ID_DRIVES_VIEW_DRIVES_TABLE = "//table[@id='cic-drive-enclosures-drives-table']"
    ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER = ID_DRIVES_VIEW_DRIVES_TABLE + "/tbody/tr/td[@class=' sorting_1'][text()='%s']/.."
    ID_DRIVES_VIEW_PANEL = "//li[@id='cic-drive-enclosures-show-drives-panel']"
    ID_ROW_DRIVES_VIEW_TABLE_HEAD = ID_DRIVES_VIEW_DRIVES_TABLE + "/thead/tr"
    ID_DRIVES_VIEW_MODEL_COLUMN_HEAD = "//td[text()='Model']"
    ID_DRIVES_VIEW_TYPE_COLUMN_HEAD = "//td[text()='Type']"
    ID_DRIVES_VIEW_CAPACITY_COLUMN_HEAD = "//td[text()='Capacity']"
    ID_DRIVES_VIEW_LOGICAL_JBOD_COLUMN_HEAD = "//td[text()='Logical JBOD']"
    ID_DRIVES_VIEW_SERVER_PROFILE_COLUMN_HEAD = "//td[text()='Server Profile']"
    ID_DRIVES_VIEW_STATUS_BY_BAY_NUMBER = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + "//div[@class='hp-status hp-status-%s']"
    ID_DRIVES_VIEW_UID_OFF_BY_BAY_NUMBER = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + "//div[@class='hp-uid-big hp-status hp-tooltipped']"
    ID_DRIVES_VIEW_UID_ON_BY_BAY_NUMBER = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + "//div[@class='hp-uid-big hp-status hp-tooltipped hp-on']"
    ID_DRIVES_VIEW_DETAILS_BY_BAY_NUMBER = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + "/../tr[@class='hp-row-details-row']"
    ID_DRIVES_VIEW_SERIAL_NUMBER_BY_BAY_NUMBER = ID_DRIVES_VIEW_DETAILS_BY_BAY_NUMBER + "//div[@id='cic-drive-enclosures-drive-details-serial-number'][text()='%s']"
    ID_DRIVES_VIEW_AUTHENTIC_BY_BAY_NUMBER = ID_DRIVES_VIEW_DETAILS_BY_BAY_NUMBER + "//div[@id='cic-drive-enclosures-drive-details-authentic'][text()='%s']"
    ID_DRIVES_VIEW_FIRMWARE_BY_BAY_NUMBER = ID_DRIVES_VIEW_DETAILS_BY_BAY_NUMBER + "//div[@id='cic-drive-enclosures-drive-details-firmware'][text()='%s']"
    ID_DRIVES_VIEW_LINK_RATE_BY_BAY_NUMBER = ID_DRIVES_VIEW_DETAILS_BY_BAY_NUMBER + "//div[@id='cic-drive-enclosures-drive-details-link-rate'][text()='%s']"
    ID_DRIVES_VIEW_RPM_BY_BAY_NUMBER = ID_DRIVES_VIEW_DETAILS_BY_BAY_NUMBER + "//div[@id='cic-drive-enclosures-drive-details-rpm'][text()='%s']"
    ID_DRIVES_VIEW_TEMPERATURE_BY_BAY_NUMBER = ID_DRIVES_VIEW_DETAILS_BY_BAY_NUMBER + "//div[@id='cic-drive-enclosures-drive-details-temperature']/div[text()='%s']"
    # There is no unique attribute for a table cell so this is necessary. Index is found dynamically within code.
    ID_GENERAL_CELL_BY_INDEX = "/td[%s]"
    ID_GENERAL_CELL_VALUE_BY_INDEX = ID_GENERAL_CELL_BY_INDEX + "/div"
    ID_TABLE_VALUE_BY_BAY_NUMBER_AND_COLUMN_NUMBER = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + ID_GENERAL_CELL_VALUE_BY_INDEX
    ID_DRIVES_VIEW_COLLAPSER_BY_DRIVE_BAY_NUMBER = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + "//div[@class='hp-collapser hp-collapsed cic-drive-enclosures-more-dr-collapser']"
    ID_DRIVES_VIEW_EXPANDED_COLLAPSER_BY_DRIVE_BAY_NUMBER = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + "//div[@class='hp-collapser hp-collapsed cic-drive-enclosures-more-dr-collapser hp-active']"
    ID_DRIVES_VIEW_TABLE_CELL = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + ID_GENERAL_CELL_VALUE_BY_INDEX
    ID_DRIVES_VIEW_TABLE_CELL_TYPE_AND_CAPACITY = ID_DRIVES_VIEW_ROW_BY_BAY_NUMBER + ID_GENERAL_CELL_BY_INDEX
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Drive Enclosures']"

    ID_DROPDOWN_ACTIONS = "//label[text()='Actions']"
    ID_SELECT_ACTION_EDIT = "id=cic-drive-enclosure-edit-action"
    ID_SELECT_ACTION_POWER_ON = "id=cic-drive-enclosure-power-on-action"
    ID_SELECT_ACTION_POWER_OFF = "id=cic-drive-enclsosure-power-off-action"
    ID_SELECT_ACTION_RESET = "id=cic-drive-enclosure-reset"

    ID_BUTTON_UID_LIGHT = "id=cic-drive-enclosures-uid-light-control"
    ID_STATUS_UID_LIGHT_ON = "xpath=//div[@id='cic-drive-enclosures-uid-light-control' and contains(@tooltip, 'UID light On.')]"
    ID_STATUS_UID_LIGHT_OFF = "//div[@id='cic-drive-enclosures-uid-light-control' and contains(@tooltip, 'UID light Off.')]"

    ID_TABLE_DRIVE_ENCLOSURES = "xpath=//table/tbody/tr[not(contains(@class, 'hp-not-found'))]/td[text()='%s']"

    ID_TEXT_STATE = "xpath=//*[@id='cic-drive-enclosure-details-module-state']"
    ID_TEXT_POWER = "xpath=//*[@id='cic-drive-enclosure-details-module-power']"
    ID_TEXT_LOGICAL_INTERCONNECT = "xpath=//div[contains(@id, 'cic-drive-enclosure-details-logical-interconnect')]"
    ID_NUMBER_OF_DRIVES = "xpath=//*[@id='cic-drive-enclosure-details-number-of-drives']"
    ID_TEMPERATURE = "xpath=//*[@id='cic-drive-enclosure-details-temperature']"
    ID_DRIVE_ENCLOSURE_MODEL = "xpath=//*[@id='cic-drive-enclosure-details-model']"
    ID_INTERCONNECT_BAY_SET = "xpath=//*[@id='cic-drive-enclosure-details-bay-set']"
    ID_SERIAL_NUMBER = "xpath=//*[@id='cic-drive-enclosure-details-serial-number']"
    ID_PART_NUMBER = "xpath=//*[@id='cic-drive-enclosure-details-part-number']"
    ID_FIRMWARE_1 = "xpath=//*[@id='cic-drive-enclosure-details-firmware-iom1']"
    ID_FIRMWARE_2 = "xpath=//*[@id='cic-drive-enclosure-details-firmware-iom2']"
    ID_IO_ADAPTER_1_BAY = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[1]/td[2]"
    ID_IO_ADAPTER_1_STATUS = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[1]/td[3]/div"
    ID_IO_ADAPTER_1_MODEL = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[1]/td[4]/div"
    ID_IO_ADAPTER_1_STATE = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[1]/td[5]/div"
    ID_IO_ADAPTER_1_SERIAL_NUMBER = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[1]/td[6]/div"
    ID_IO_ADAPTER_1_PART_NUMBER = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[1]/td[7]/div"
    ID_IO_ADAPTER_2_BAY = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[3]/td[2]"
    ID_IO_ADAPTER_2_STATUS = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[3]/td[3]/div"
    ID_IO_ADAPTER_2_MODEL = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[3]/td[4]/div"
    ID_IO_ADAPTER_2_STATE = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[3]/td[5]/div"
    ID_IO_ADAPTER_2_SERIAL_NUMBER = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[3]/td[6]/div"
    ID_IO_ADAPTER_2_PART_NUMBER = "xpath=//*[@id='cic-drive-enclosure-more-iomodules-table']/tbody/tr[3]/td[7]/div"
    ID_STATUS_DRIVE_ENCLOSURE_OK = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"
    ID_STATUS_DRIVE_ENCLOSURE_WARN = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"
    ID_STATUS_DRIVE_ENCLOSURE_ERROR = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"
    ID_STATUS_DRIVE_ENCLOSURE_UNKNOWN = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-unknown']"
    ID_DRIVE_ENCLOSURE_TITLE = "xpath=//*[@id='cic-drive-enclosures-show-title' and text()='%s']"
    ID_ENCLOSURE_SERVER_BAY_LINK = "xpath=//*[@id='cic-enclosure-show-bladebays']//a[text()='%s']"
    ID_PROGRESS_BAR = "xpath=//*[@id='hp-page-notifications']//div[@class='hp-progress']"
    ID_PROGRESS_BAR_COMPLETE = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Completed']"  # "xpath=//*[@id='hp-page-notifications']//div[@class='hp-state' and text()='Completed']"
    ID_PROGRESS_BAR_ERROR = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Error']"
    ID_PROGRESS_BAR_WARNING = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Warning']"
    ID_PAGE_NOTIFICATION_MESSAGE = "//*[@id='hp-page-notifications']/div[@class='hp-controls' and (descendant::span)]/../div[@class='hp-notification']//div[@class='hp-message']/p/span"


class PowerOnDriveEnclosureElements(object):
    ID_SELECT_ACTION_POWER_ON = "xpath=//*[@id='cic-drive-enclosure-power-on-action']"


class PowerOffDriveEnclosureElements(object):
    ID_SELECT_ACTION_POWER_OFF = "xpath=//*[@id='cic-drive-enclosure-power-off-action']"
    ID_BUTTON_POWEROFF_CONFIRM_YES = "xpath=//*[@class='hp-ok hp-primary' and text() ='Yes, power off']"
    ID_BUTTON_POWEROFF_CONFIRM_CANCEL = "xpath=//*[@class='hp-cancel' and text() ='Cancel']"


class ResetDriveEnclosureElements(object):
    ID_SELECT_ACTION_RESET = "xpath=//*[@id='cic-drive-enclosure-reset']"
    ID_BUTTON_RESET = "xpath=//button[@id='cic-server-reset']"
    ID_BUTTON_RESET_CONFIRM_YES = "xpath=//*[@class='hp-ok hp-primary' and text() ='Yes, reset']"
    ID_BUTTON_RESET_CONFIRM_CANCEL = "xpath=//*[@class='hp-cancel' and text() ='Cancel']"


class RefreshDriveEnclosureElements(object):
    ID_SELECT_ACTION_REFRESH = "xpath=//*[@id='cic-drive-enclosure-refresh']"
