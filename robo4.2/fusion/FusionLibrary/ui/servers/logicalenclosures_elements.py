# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This  file contains all  element ID on Fusion Logical enclosure page/screen
'''


class FusionLogicalEnclosuresPage(object):

    CREATE_LE_TIME = 30  # in  seconds
    DELETE_LE_TIME = 30  # in seconds
    WAIT_TIME = 30  # in seconds
    TIMEOUT = 40  # in minutes

    FW_UPGRADE_TIMEOUT = 90  # in minutes
    FW_UPGRADE_TIME = 15  # in  seconds

    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Logical Enclosures']"
    ID_LE_TABLE = "xpath=//div[@class='dataTables_scrollBody']//table"
    ID_LINK_CREATE_LOGICAL_ENCLOSURES = "link=Create logical enclosure"
    ID_INPUT_LE_NAME = "cic-logical-enclosure-name"
    ID_ENCLOSURE_SELECT_DROPDOWN = "xpath=//*[@class='hp-search-combo-control']"
    ID_INPUT_LE_ENCLOSURE_SELECT = "xpath=//span[contains(.,'%s')]"
    ID_INPUT_EG_SELECT_DROPDOWN = "xpath=//*[@id='logicalenclosures-add-enclosure-group-block']//*[@class='hp-search-combo-control']"
    ID_INPUT_EG_SELECT = "xpath=//span[contains(.,'%s')]"

    ID_LE_CREATE_BTN = "id=cic-logical-enclosure-add"

    ID_LINK_LE_NAME = "xpath=//div[@class='dataTables_scrollBody']//table/tbody/tr/td[text()='%s']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"

    ID_REAPPLY_CONFIG = "id=cic-logicalenclosure-reconfigure-action"
    ID_REAPPLY_CONFIRMATION = "id=cic-logicalenclosure-reapplyconf-reapply"

    ID_DELETE_BTN = "id=cic-logicalenclosure-delete-action"
    ID_DELETE_CONFIRMATION = "id=cic-logicalenclosure-delete-confirm-button"

    XPATH_LE_NAME = "xpath=//div[@class='dataTables_scrollBody']/table/tbody//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    XPATH_FIRMWARE_BASELINE_DROPDOWN = "xpath=//*[@id='cic-logicalenclosure-firmware-content']//*[@class='hp-value']"
    XPATH_FIRMWARE_BASELINE_OPTIONS = "xpath=//*[@id='cic-logicalenclosure-firmware-content']//*[@class='hp-options']//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]"
    ID_FIRMWARE_FORCE_INSTALL = "id=cic-logicalenclosure-firmware-force"

    XPATH_UPDATE_STATUS_COMPLETE = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Completed']"
    XPATH_UPDATE_STEP = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-step']"
    XPATH_UPDATE_STATUS_ERROR = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Error']"
    XPATH_UPDATE_STATUS_WARNING = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Warning']"

    ID_LE_ADD_FORM = "id=cic-logical-enclosure-add-form"
    ID_LE_EDIT_FORM = "id=cic-logical-enclosure-edit-form"
    ID_BTN_LE_ADD_CANCEL = "id=cic-logical-enclosure-add-cancel"

    XPATH_LE_ADD_HP_STATUS_ERROR = "xpath=//*[@id='cic-logical-enclosure-add-form']//*[@class='hp-status hp-status-error']"
    XPATH_LE_EDIT_HP_STATUS_ERROR = "xpath=//*[@id='cic-logical-enclosure-edit-form']//*[@class='hp-status hp-status-error']"
    XPATH_LE_DELETE_HP_STATUS_ERROR = "xpath=//*[@id='hp-logicalenclosure-remove-dialog']//*[@class='hp-status hp-status-error']"

    XPATH_LE_ADD_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='cic-logical-enclosure-add-form']//*[@class='hp-form-message-summary']"
    XPATH_LE_EDIT_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='cic-logical-enclosure-edit-form']//*[@class='hp-form-message-summary']"
    XPATH_LE_DELETE_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='hp-logicalenclosure-remove-dialog']//*[@class='hp-form-message-summary']"
    XPATH_LE_ADD_FORM_MESSAGE_DETAILS = "xpath=//*[@id='cic-logical-enclosure-add-form']//*[@class='hp-form-message-details']"
    XPATH_LE_EDIT_FORM_MESSAGE_DETAILS = "xpath=//*[@id='cic-logical-enclosure-edit-form']//*[@class='hp-form-message-details']"
    XPATH_LE_DELETE_FORM_MESSAGE_DETAILS = "xpath=//*[@id='hp-logicalenclosure-remove-dialog']//*[@class='hp-form-message-details']"
    ID_LE_FORCE_DELETE = "id=cic-logicalenclosure-force-remove"

    ID_LE_DELETE_CANCEL = "id=cic-logicalenclosure-delete-close-cancel-button"
    LE_ADD_FORM = "cic-logical-enclosure-add-form"
    LE_EDIT_FORM = "cic-logical-enclosure-edit-form"
    XPATH_LE_DELETE_ERROR = "//*[@class='cic-logicalenclosure-delete-error']"
    XPATH_LE_DELETE_WARNING = "//*[@class='cic-logicalenclosure-delete-error']//*[@id='cic-logicalenclosure-delete-error-warning']"

    XPATH_LE_CREATE_ACTIVITY = "xpath=//*[@id='hp-activity-resource-view']//tr[*  [@class='hp-name']//*[text()='Create']]"
    XPATH_LE_CREATE_ACTIVITY_STATE = "xpath=//*[@id='hp-activity-resource-view']//tr[*[@class='hp-name']//*[text()='Create']]/*[@class='hp-date']/following-sibling::node()[position()=1]"

    ID_LE_PANEL_SELECTOR = "id=cic-logicalenclosure-panel-selector"
    LINK_LE_ACTIVITY = "link=Activity"
    ID_LE_ACTIVITY_RESOURCE_VIEW = "id=hp-activity-resource-view"

    ID_SELECT_LOGICAL_ENCLOSURE = "xpath=//td[text()='%s']"  # replace with Logical enclosure name
    ID_LOGICAL_ENCLOSURE_TITLE = "xpath=//*[@id='cic-logicalenclosure-details-title' and text()='%s']"   # %s will be replace with name of the Logical enclosure
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_UPDATE_FIRMWARE = "link=Update firmware"
    ID_UPDATE_FIRMWARE = "xpath=//span[text()='Update firmware']"
    ID_FIRMWARE_BASELINE = "xpath=//div[@id='cic-logicalenclosure-edit-form-contents']//div[@class='hp-value']"
    ID_SELECT_FIRMWARE_BASELINE = "xpath=//span[@class='hp-name' and text()='%s']"  # %s replace with Firmware Bundle name
    ID_UPDATE_FIRMWARE_OK_BUTTON = "xpath=//input[@id='cic-logicalenclosure-fw-edit-ok']"
    ID_UPDATE_FIRMWARE_CANCEL_BUTTON = "xpath=//input[@id='cic-logicalenclosure-fw-edit-cancel']"
    ID_FIRMWARE_BASELINE_CHECKBOX = "xpath=//input[@id='cic-logicalenclosure-edit-firmware-force']"
    ID_LE_UPDATE_FIRMWARE = "xpath=//span[text()='Logical enclosure firmware update']"
    ID_UPDATE_FIRMWARE_STATUS = "xpath=//header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_BAR = "xpath=//div[@id='hp-page-notifications']/div[1]/header"
    ID_ALL_LE_LIST = "xpath=//tbody/tr/td[2]"

    ''' For firmware upgrade from LE '''
    LI_MESSAGE_LIST = ["Activation success for the interconnect %s with firmware version %s from baseline",
                       "Activation started for the interconnect %s with firmware version %s from baseline",
                       "Staging success for the interconnect %s with firmware version %s from baseline",
                       "Staging started for the interconnect %s with firmware version %s from baseline"]

    ID_LE_FW_UPDATE_FORM = "id=cic-logicalenclosure-edit-form"
    XPATH_LE_FW_UPDATE_HP_STATUS_ERROR = "xpath=//*[@id='cic-logicalenclosure-edit-form']//*[@class='hp-status hp-status-error']"
    XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='cic-logicalenclosure-edit-form']//*[@class='hp-form-message-summary']"
    XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS = "xpath=//*[@id='cic-logicalenclosure-edit-form']//*[@class='hp-form-message-details']"

    FW_DOWNGRADE_WARNING_MSG = "Downgrading the firmware can result in the installation of unsupported firmware and cause hardware to cease operation."
    PARALLEL_ACTIVATION_WARNING_MSG = "Warning: Parallel activation is optimized for faster updates and will cause service outages. Firmware updates using parallel activation should be performed within a maintenance window."
    ORCHASTRATED_ACTIVATION_WARNING_MSG = "Orchestrated activation will minimize service outages. Determining the extent of outages will be tested before activation begins"
    XPATH_LI_DETAILS = "xpath=//*[@id='cic-logicalenclosure-details-lis']"
    XPATH_LI_ELEMENT = "//*[@id='cic-logicalenclosure-details-lis']//a"
    ID_LE_DETAILS = "id=cic-logicalenclosure-details"
    ID_FIRMWARE_UPGRADE = "cic-logicalenclosure-updatefw-action"
    ID_FIRMWARE_DROPDOWN = "xpath=//div[@id='cic-logicalenclosure-edit-form-contents']//li[label[contains(text(), 'Firmware baseline')]]//div[@class='hp-value']"
    ID_SELECT_FROM_DROPDOWN = "xpath=//*[@id='cic-logicalenclosure-edit-form-contents']//li[@class='hp-form-item']//li[span[text()='%s']]"
    ID_UPGRADE_FOR_DROPDOWN = "xpath=//*[@id='cic-logicalenclosure-edit-form-contents']//li[label[contains(text(), 'Update firmware for')]]/div"
    ID_UNMANAGED_INTERCONNECT_CHECKBOX = "xpath=//*[@id='cic-logicalenclosure-edit-firmware-update-unmanaged']"

    ID_ACTIVATION_CONTENT = "id=cic-logicalenclosure-enclosures-activation-content"
    ID_ACTIVATION_TYPE = "xpath=//*[@id='cic-logicalenclosures-activation-%s-type']"

    ID_FORCE_INSTALL = "xpath=//*[@id='cic-logicalenclosure-edit-firmware-force']"
    ID_FORCE_INSTALL_WARNING = "xpath=//*[@id='cic-logicalenclosure-edit-firmware-force-warning']/label/span"

    ID_ORCHESTRATED_WARNING = "id=cic-logicalenclosure-edit-firmware-orchestrated-type-message"
    ID_PARALLEL_WARNING = "id=cic-logicalenclosure-edit-firmware-parallel-type-warning"
    ID_FIRMWARE_UPDATE_OK = "id=cic-logicalenclosure-fw-edit-ok"

    ID_LE_NAME = "xpath=//td[text()='%s']"
    ID_LE_UPDATE_PROGRESS = "xpath = //*[@id='hp-page-notifications']//div[@class='hp-message']//span[text()='Logical enclosure firmware update']/following::div[@class='hp-state']/div[@class='hp-progress']"

    ID_FW_CANCEL = "id=cic-logicalenclosure-fw-edit-cancel"
    ID_ACTIVITY_BAR = "xpath = .//*[@id='hp-flyout-activities']/li/div[@class='hp-brief']/div[@class='hp-status hp-status-changing']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Update firmware']/following::div[text()='%s']"
    ID_UPDATE_PROGRESS = "xpath = .//header[@class='hp-active']/div[@class='hp-status hp-status-changing']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Update firmware']//following::a[text()='%s']"
    ID_UPDATE_SUCCESS = "xpath = .//header[@class='hp-active']/div[@class='hp-status hp-status-ok']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Update firmware']//following::a[text()='%s']"
    ID_UPDATE_WARNING = "xpath = .//header[@class='hp-active']/div[@class='hp-status hp-status-warning']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Update firmware']//following::a[text()='%s']"
    ID_UPDATE_FAILED = "xpath = .//header[@class='hp-active']/div[@class='hp-status hp-status-error']/following-sibling::div[@class='hp-activity-message']/p/span[text()='Update firmware']//following::a[text()='%s']"
    ID_MENU_SELECTOR = "xpath = //*[@id='cic-logicalenclosure-panel-selector']"
    ID_ACTIVITY = "link=Activity"
    LINK_OVERVIEW = "link=Overview"
    ID_FW_STATE = "xpath = .//*[@id='hp-page-notifications']/div[1]/header/div[@class='hp-message']/p/span[text()='Logical enclosure firmware update']/following::div[@class='hp-state']"
    ID_ACTIVITY_COLLAPSER = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]//div[@class='hp-collapser']"

    ID_ACTIVITY_COLLAPSER_ACTIVE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]//div[@class='hp-collapser hp-active']"

    ID_FORM_LI_SP_ACTIVITY = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::tr[td[@class='hp-source']/a[text()='%s']][1]"
    ID_FORM_LI_SP_ACTIVITY_DESC = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::tr[td[@class='hp-source']/a[text()='%s']][1]//following::node()[position()=1]//div[@class='hp-details']/p"
    ID_FORM_LI_SP_ISSUE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::tr[td[@class='hp-source']/a[text()='%s']][1]//following::node()[position()=1]//span[@class='hp-details']"
    ID_FORM_LI_SP_RESOLUTION = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::tr[td[@class='hp-source']/a[text()='%s']][1]//following::node()[position()=1]//span[@class='hp-resolution']//span"

    ID_FIRM_UPGRADE_LE_ERROR = "xpath=//*[@id='hp-form-message']//span[text()='error']"
    ID_FORM_ERROR = "xpath=//*[@id='hp-form-message']"

    XPATH_EM_ACTIVITY_DETAILS = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::tr[td[@class='hp-source']/a[text()='%s']]//following::node()[position()=1]//*[@class='hp-task-notification-container']//*[@class='hp-details']/p"
    XPATH_EM_ACTIVITY_ISSUE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::tr[td[@class='hp-source']/a[text()='%s']]/following::node()[position()=1]//*[@class='hp-details-correlations-container']//*[@class='hp-details']"
    XPATH_EM_ACTIVITY_RESOULTION = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::tr[td[@class='hp-source']/a[text()='%s']]/following::node()[position()=1]//*[@class='hp-details-correlations-container']//*[@class='hp-resolution']"

    ID_LE_FIRMWARE_TABLE_WRPAAPER = "id=cic-logicalenclosure-more-fw-table"
    LINK_FIRMWARE = "link=Firmware"
    XPATH_LE_SERVER_PROFILES = "//*[@id='cic-logicalenclosure-more-fw-table']/tbody//td[text()='Server profile']/parent::tr/*[1]"

    XPATH_LE_UPDAtE_ACTIVITY = "xpath=//tbody/tr[td[@class='hp-name']/p/span[text()='%s']][1]"
    XPATH_LE_UPDATE_ACTIVITY_STATE = "xpath=//tbody/tr[td[@class='hp-name']/p/span[text()='%s']][1]/td[@class='hp-date']/following-sibling::node()[position()=1]"
    ID_LE_ACTIVITY_RESOURCE_VIEW = "id=hp-activity-resource-view"

    XPATH_LE_OVERALL_ACTIVITY_DETAILS = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]//following::*[@class='hp-notification-details']/*[@class='hp-details']"
    XPATH_LE_OVERALL_ACTIVITY_ISSUE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::*[@class='hp-task-details hp-full']/*[@class='hp-task-notification-container']//*[@class='hp-details-correlations-container']//*[@class='hp-details-container']/span/p"
    XPATH_LE_OVERALL_ACTIVITY_RESOLUTION = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']][1]/following::*[@class='hp-task-details hp-full']/*[@class='hp-task-notification-container']//*[@class='hp-details-correlations-container']//*[@class='hp-resolution-container']/span/p"
    ID_LE_CONSISTENCY_STATE = "id=cic-logicalenclosure-state"
    ID_CONSISTENCY_STATE = "xpath=//*[@id='cic-logicalenclosure-state' and text()='%s']"

    # update from group
    ID_MENU_ACTION_UPDATE_FROM_GROUP = "xpath=.//*[@id='cic-logicalenclosure-update-from-group-action']"
    ID_CONFIRM_UPDATE_FROM_GROUP = "xpath=.//*[@id='cic-logicalenclosure-updateFromGroup-update']"
    ID_STATUS = "xpath=.//*[@id='hp-page-notifications']/div/header/div[@class='hp-state']"

    # update firmwarefor
    ID_UPDATE_FIRMWARE_FOR = "xpath=.//div[@class='hp-select']/div[text()='Shared infrastructure']"
    ID_SELECT_UPDATE_FIRMWARE_FOR = "xpath=//span[text()='%s']"  # %s will be the update firmware option
    ID_UNMANAGED_FW_ACTIVITY_STATE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-status-name']//span[text()='Firmware update for unmanaged interconnects']]//td[@class='hp-state']"
    ID_PROGRESS_BAR = "xpath=//*[@class='hp-progress']"
    ID_CMPLETE_XPATH = "xpath=//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Completed']"
    ID_WARNING_XPATH = "xpath=//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Warning']"
    ID_ERROR_XPATH = "xpath=//header[@class='hp-notification-summary']/div[@class='hp-state' and text()='Error']"
    UPDATE_WAIT_TIME = 15  # in seconds
    ID_UNMANAGED_INTERCONNECT_CHECKBOX = "xpath=//*[@id='cic-logicalenclosure-edit-firmware-update-unmanaged']"

    FW_UPDATE_TIME = 3600  # in seconds this is LE firmware update time out
    ID_LE_UPDATE_WAIT_TIME = 30  # in seconds

    ''' For firmware upgrade from LE '''

    LI_MESSAGE_LIST_C7K = ["Activation success for the interconnect %s with firmware version %s from baseline",
                           "Activation started for the interconnect %s with firmware version %s from baseline",
                           "Staging success for the interconnect %s with firmware version %s from baseline",
                           "Staging started for the interconnect %s with firmware version %s from baseline"]
