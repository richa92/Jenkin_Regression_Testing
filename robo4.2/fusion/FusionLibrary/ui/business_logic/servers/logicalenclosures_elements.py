class GeneralLogicalEnclosureElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Logical Enclosures']"
    ID_TEXT_LOGICAL_INTERCONNECT_DETAILS = "xpath=.//*[@id='cic-logicalenclosure-details-lis']//a"
    # action button
    ID_BUTTON_ACTIONS = "//label[text()='Actions']"
    ID_SELECT_ACTION_DELETE = "id=cic-logicalenclosure-delete-action"
    ID_SELECT_ACTION_UPDATE_FIRMWARE = "id=cic-logicalenclosure-updatefw-action"

    # for verify
    ID_TABLE_LOGICAL_ENCLOSURE = "xpath=//table/tbody/tr/td[text()='%s']"
    ID_TABLE_ITEM_SELECTED = "//table[contains(@id, 'DataTables_Table')]//td[.='%s' and parent::tr[contains(@class, 'hp-selected')]]"
    ID_TABLE_LOGICAL_ENCLOSURES = "xpath=//table/tbody/tr/td[2]"
    ID_TABLE_LOGICAL_ENCLOSURE_SELECTED = "xpath=//table/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"
    ID_STATUS_LOGICAL_ENCLOSURE_OK = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"
    ID_STATUS_LOGICAL_ENCLOSURE_WARN = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"
    ID_STATUS_LOGICAL_ENCLOSURE_ERROR = "xpath=//table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"
    ID_STATUS_LOGICAL_ENCLOSURE = "xpath=//table[contains(@class, 'hp-master-table')]//td[text()='%s']/../td/div[contains(@class, 'hp-status')]//span"
    ID_ELEMENT_LOGICAL_ENCLOSURE_DELETED = "xpath=//table//td[.='%s' and parent::tr[contains(@class, 'hp-not-found')]]"
    ID_BUTTON_EXPAND_ALL = "//a[@id='cic-logicalenclosure-more-firmware-expand-all']"
    ID_LINK_SERVER_HARDWARE = "//table[@id='cic-logicalenclosure-more-fw-table']//tr/td/div/following-sibling::a[text()='%s']"
    ID_TEXT_SERVER_FIRMWARE_INSTALLED = "//table[@id='cic-logicalenclosure-more-fw-table']//tr[contains(@class, '%s')]/td[contains(text(), '%s')]/../td[1+count(//thead[@id='cic-logicalenclosure-more-fw-table-header']//td[.='Installed']/preceding-sibling::td)][contains(text(), '%s')]"
    ID_TEXT_SERVER_FIRMWARE_BASELINE = "//table[@id='cic-logicalenclosure-more-fw-table']//tr[contains(@class, '%s')]/td[contains(text(), '%s')]/../td[1+count(//thead[@id='cic-logicalenclosure-more-fw-table-header']//td[.='Baseline']/preceding-sibling::td)][.='%s']"
    ID_TEXT_COMMON_FIRMWARE_INSTALLED = "//table[@id='cic-logicalenclosure-more-fw-table']//td[.='%s']/../td[1+count(//thead[@id='cic-logicalenclosure-more-fw-table-header']//td[.='Installed']/preceding-sibling::td)][.='%s']"
    ID_TEXT_COMMON_FIRMWARE_BASELINE = "//table[@id='cic-logicalenclosure-more-fw-table']//td[.='%s']/../td[1+count(//thead[@id='cic-logicalenclosure-more-fw-table-header']//td[.='Baseline']/preceding-sibling::td)][.='%s']"

    ID_STATUS_NOTIFICATION_ONGOING = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-unknown']"
    ID_STATUS_NOTIFICATION_OK = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "//*[@id='cic-logicalenclosure-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    ID_TEXT_GENERAL_STATE = "id=cic-logicalenclosure-details-status"
    ID_TEXT_ACTIVITY_TITLE = "//div[@id='hp-page-notifications']/div/header/div/p/span"
    ID_TEXT_ACTIVITY_OK = "//div[@id='hp-page-notifications']/div/header/div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_WARN = "//div[@id='hp-page-notifications']/div/header/div[@class='hp-status hp-status-warning']"
    ID_TEXT_ACTIVITY_WARN_MESSAGE = "//div[@id='hp-page-notifications']/div/header/div[@class='hp-message']/p/span"
    ID_TEXT_LE_CONSISTENCY_STATE = "id=cic-logicalenclosure-state"
    ID_TEXT_ACTIVITY_ERROR = "//div[@id='hp-page-notifications']/div/header/div[@class='hp-status hp-status-error']"
    ID_TEXT_ACTIVITY_DETAILS_OK = "//div[@id='hp-page-notifications']/div/header/div[@class='hp-status hp-status-ok']"
    # option panel
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-logicalenclosure-panel-selector"
    ID_SELECT_ICBAYCFG_PANEL = "xpath=//ol[@class='hp-options']//a[.='Interconnect Bay Configuration']"
    ID_SELECT_GENERAL_PANEL = "xpath=//ol[@class='hp-options']//a[.='General']"
    ID_SELECT_CFGSCRIPT_PANEL = "xpath=//ol[@class='hp-options']//a[.='Configuration Script']"
    ID_SELECT_LABEL_PANEL = "xpath=//ol[@class='hp-options']//a[.='Labels']"
    ID_SELECT_ACTIVITY_PANEL = "xpath=//ol[@class='hp-options']//a[.='Activity']"
    ID_SELECT_MAP_PANEL = "xpath=//ol[@class='hp-options']//a[.='Map']"

    # Used For Interconnect Bay Licensing under ID_SELECT_ICBAYLICENSING_PANEL.
    ID_SELECT_ICBAYLICENSING_PANEL = "xpath=//ol[@class='hp-options']//a[.='Interconnect Bay Licensing']"

    ID_INTERCONNECT_BAY_LICENSING_INTENT = "xpath=//*[@id='cic-logicalenclosure-more-baylicense']//td[.='%s']/../td[1+count(//*[@id='cic-logicalenclosure-more-baylicense']//a[.='%s']/../../../../following-sibling::*//td[.='Use Synergy 8Gb FC Upgrade']/preceding-sibling::td)]"  # interconnectname,enclosure
    ID_INTERCONNECT_BAY_LICENSING_ICM_BAY = "xpath=//*[@id='cic-logicalenclosure-more-baylicense']//td[.='%s']/../td[1+count(//*[@id='cic-logicalenclosure-more-baylicense']//a[.='%s']/../../../../following-sibling::*//td[.='Bay']/preceding-sibling::td)]"  # interconnectname,enclosure
    ID_INTERCONNECT_BAY_LICENSING_LI = "xpath=//*[@id='cic-logicalenclosure-more-baylicense']//td[.='%s']/../td[1+count(//*[@id='cic-logicalenclosure-more-baylicense']//a[.='%s']/../../../../following-sibling::*//td[.='Licensing defined by']/preceding-sibling::td)]"  # interconnectname,enclosure
    ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_INTENT_TOGGLE = "//*[@id='cic-logicalenclosures-panel-edit-iclicense']/p[fieldset//*[text()='%s']]//tbody/tr[%s]/td//a[@id='undefined-hpToggle']"
    ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_CANCEL = "//*[@id='cic-logical-enclosure-edit-cancel']"
    ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_OK = "//*[@id='cic-logical-enclosure-update']"
    ID_INTERCONNECT_BAY_LICENSING_EDITPANEL_BAYDATA = "xpath=//*[@id='cic-logicalenclosures-panel-edit-iclicense']//p[fieldset//*[text()='%s']]//tbody//tr[%s]"
    ID_LE_TABLE = "xpath=//div[@class='dataTables_scrollBody']//table"

    # ip verification if in range
    ID_ENCLOSURES_DETAILS = "id=cic-logicalenclosure-details-enclosure"
    ID_TEXT_ENCLOSURES_IN_LE = "//*[@id='cic-logicalenclosure-details-enclosure']//a"


class CreateLogicalEnclosuresElements(object):

    ID_BUTTON_CREATE_LOGICAL_ENCLOSURE = "xpath=//a[.='Create logical enclosure']"
    ID_DIALOG_CREATE_LOGICAL_ENCLOSURE = "id=cic-logical-enclosure-add-form"
    ID_INPUT_NAME = "id=cic-logical-enclosure-name"
    ID_COMBO_ENCLOSURES = "id=cic-logical-enclosure-enclosure-select-input"
    ID_COMBO_ENCLOSURES_SEARCH_BUTTON = "xpath=//*[@id='logicalenclosures-add-enclosure-block']//div[@class='hp-search-combo-control']"
    ID_COMBO_ENCLOSURES_SELECT = "xpath=//*[@id='logicalenclosures-add-enclosure-block']//span[@class='hp-name' and text()='%s']"
    ID_COMBO_ENCLOSURE_GROUP = "id=cic-logical-enclosure-enclosure-group-select-input"
    ID_SELECT_FIRMWARE_BASELINE = "id=cic-logicalenclosure-firmware-baseline"
    ID_BUTTON_CREATE = "id=cic-logical-enclosure-add"
    ID_BUTTON_CREATE_PLUS = "id=cic-logical-enclosure-addplus"
    ID_BUTTON_CREATE_CANCEL = "id=cic-logical-enclosure-add-cancel"

    ID_COMBO_FIRMWARE_BASELINE = "id=cic-logicalenclosure-firmware-baseline"
    ID_CHECKBOX_FIRMWARE_FORCE_INSTALL = "id=cic-logicalenclosure-firmware-force"


class UpdateFirmwareElements(object):

    ID_DIALOG_UPDATE_FIRMWARE = "id=cic-logicalenclosure-edit-form"
    ID_SELECT_FIRMWARE_BASELINE = "id=cic-logicalenclosure-firmware-baseline"
    ID_BUTTON_OK = "id=cic-logicalenclosure-fw-edit-ok"
    ID_BUTTON_CANCEL = "id=cic-logicalenclosure-fw-edit-cancel"
    ID_LINK_EXPAND_ALL = "id=cic-logicalenclosure-edit-expand-all"
    ID_LINK_COLLAPSE_ALL = "id=cic-logicalenclosure-edit-collapse-all"

    ID_OPTION_FIRMWARE_BASELINE = "id=cic-logicalenclosure-edit-firmwareBaseline"
    ID_OPTION_UPDATE_FIRMWARE_FOR = "id=cic-logicalenclosure-edit-updateFirmware-for"
    ID_CHECKBOX_FIRMWARE_FORCE_INSTALL = "id=cic-logicalenclosure-edit-firmware-force"

    ID_RADIO_ORCHESTRATED = "id=cic-logicalenclosures-activation-orchestrated-type"
    ID_RADIO_PARALLEL = "id=cic-logicalenclosures-activation-parallel-type"

    ID_LINK_SERVER_HARDWARE = "//table[@id='cic-logicalenclosure-edit-fwtable']//tr/td/div/following-sibling::a[text()='%s']"
    ID_TEXT_SERVER_FIRMWARE_INSTALLED = "//table[@id='cic-logicalenclosure-edit-fwtable']//tr[contains(@class, '%s')]/td[text()='%s']/../td[1+count(//thead[@id='cic-logicalenclosure-edit-fwtable-header']//td[.='Installed']/preceding-sibling::td)][contains(text(), '%s')]"
    ID_TEXT_SERVER_FIRMWARE_BASELINE = "//table[@id='cic-logicalenclosure-edit-fwtable']//tr[contains(@class, '%s')]/td[text()='%s']/../td[1+count(//thead[@id='cic-logicalenclosure-edit-fwtable-header']//td[.='Selected']/preceding-sibling::td)][.='%s']"
    ID_TEXT_COMMON_FIRMWARE_INSTALLED = "//table[@id='cic-logicalenclosure-edit-fwtable']//td[.='%s']/../td[1+count(//thead[@id='cic-logicalenclosure-edit-fwtable-header']//td[.='Installed']/preceding-sibling::td)][.='%s']"
    ID_TEXT_COMMON_FIRMWARE_BASELINE = "//table[@id='cic-logicalenclosure-edit-fwtable']//td[.='%s']/../td[1+count(//thead[@id='cic-logicalenclosure-edit-fwtable-header']//td[.='Selected']/preceding-sibling::td)][.='%s']"


class EditLogicalEnclosureElements(object):
    ID_ACTION_EDIT_LOGICAL_ENCLOSURE = "//div[@id='cic-logicalenclosure-actions']//a[text()='Edit']"  # Action->Create

    ID_DIALOG_EDIT_LOGICAL_ENCLOSURE = "id=hp-change-page-container"

    ID_INPUT_LOGICAL_ENCLOSURE_NAME = "//input[@id='cic-logical-enclosure-name']"  # Logical Enclosure name input box    t
    ID_INPUT_CONFIG_SCRIPT = "//textarea[@id='cic-logical-enclosure-config-script']"

    ID_BUTTON_LOGICAL_ENCLOSURE_OK = "id=cic-logical-enclosure-update"
    ID_BUTTON_LOGICAL_ENCLOSURE_CANCEL = "id=cic-logical-enclosure-edit-cancel"
    ID_INTERCONNECT_BAY_LICENSING_EDITPANEL = "//*[@id='cic-logicalenclosure-more-baylicense']//*[text()='Edit']"


class DeleteLogicalEnclosuresElements(object):

    ID_DIALOG_DELETE = "id=hp-logicalenclosure-remove-dialog"
    ID_BUTTON_YES_DELETE = "id=cic-logicalenclosure-delete-confirm-button"
    ID_TABLE_LE_DELETED = "xpath=//table/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # le table list

    # can't be removed
    ID_CHECKBOX_FORCE_REMOVE_LOGICAL_ENCLOSURE = "id=cic-logicalenclosure-force-remove"
    ID_DIALOG_DELETE_ERROR = "id=cic-logicalenclosure-delete-error-dialog"
    ID_TEXT_DELETE_ERROR = "id=cic-logicalenclosure-remove-error-msg"
    ID_BUTTON_CLOSE = "xpath=//div[@id='cic-logical-enclosure-delete-error-dialog']//button[.='Close']"


class LogicalEnclosuresReapplyConfiguration(object):
    ID_ACTION_REAPPLY_CONFIGURATION = "id=cic-logicalenclosure-reconfigure-action"

    ID_DIALOG_REAPPLY_CONFIGURATION_LOGICAL_ENCLOSURE = "id=cic-logicalenclosure-reapplyconf-show-dialog"

    ID_BUTTON_REAPPLY_LOGICAL_ENCLOSURE_CONFIRM = "xpath=//button[@class='hp-ok hp-primary' and text()='Yes, reapply']"
    ID_BUTTON_REAPPLY_LOGICAL_ENCLOSURE_CANCEL = "xpath=//button[@class='hp-cancel' and text()='Cancel']"
    ID_BUTTON_REAPPLY_LOGICAL_ENCLOSURE_CLOSE = "xpath=//button[@class='hp-cancel hp-primary' and text()='Close']"


class LogicalEnclosuresUpdateFromGroup(object):
    ID_ACTION_UPDATE_FROM_GROUP = "id=cic-logicalenclosure-update-from-group-action"

    ID_DIALOG_UPDATE_FROM_GROUP = "id=cic-logicalenclosure-updateFromGroup-show-dialog"

    ID_BUTTON_UPDATE_FROM_GROUP_CONFIRM = "xpath=//button[@class='hp-ok hp-primary' and text()='Yes, update']"
    ID_CHECKBOX_UPDATE_FROM_GROUP_CONFIRM = "id=cic-logicalenclosure-updateFromGroup-confirm-checkbox"
    ID_BUTTON_UPDATE_FROM_GROUP_CONFIRM_AGAIN = "id=cic-logicalenclosure-updateFromGroup-confirm-update"

    ID_BUTTON_UPDATE_FROM_GROUP_CANCEL = "xpath=//button[@class='hp-cancel' and text()='Cancel']"
    ID_BUTTON_UPDATE_FROM_GROUP_CLOSE = "xpath=//button[@class='hp-cancel hp-primary' and text()='Close']"


class CreateLogicalEnclosuresSupportDump(object):
    ID_ACTION_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP = "//div[@id='cic-logicalenclosure-actions']//a[text()='Create logical enclosure support dump']"

    ID_DIALOG_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP = "id=cic-logical-enclosure-support-dump-dialog"

    ID_BUTTON_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP_CONFIRM = "xpath=//button[@class='hp-ok hp-primary' and text()='Yes, create']"
    ID_BUTTON_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP_CANCEL = "xpath=//button[@class='hp-cancel' and text()='Cancel']"
    ID_BUTTON_CREATE_LOGICAL_ENCLOSURE_SUPPORT_DUMP_CLOSE = "xpath=//button[@class='hp-cancel hp-primary' and text()='Close']"

    ID_CHECKBOX_ENABLE_ENCRYPTION = "id=cic-logical-enclosure-support-dump-encryption-checkbox"


class LogicalEnclosuresUpdateFirmware(object):
    ID_BUTTON_UPDATE_FIRMWARE = "cic-logicalenclosure-updatefw-action"
    ID_BUTTON_FIRMWARE_BASELINE = "xpath=//div[@id='cic-logicalenclosure-edit-form-contents']//li[label[contains(text(), 'Firmware baseline')]]//div[@class='hp-value']"
    ID_DROPDOWN_FIRMWARE_BASELINE = "xpath=//*[@id='cic-logicalenclosure-edit-form-contents']//li[@class='hp-form-item']//li[span[text()='%s']]"
    ID_BUTTON_UPDATE_FOR = "xpath=//*[@id='cic-logicalenclosure-edit-form-contents']//li[@class='hp-form-item']//li[span[contains(text(), '%s')]]"
    ID_DROPDOWN_UPDATE_OPTION = "xpath=//*[@id='cic-logicalenclosure-edit-form-contents']//li[label[contains(text(), 'Update firmware for')]]/div"
    ID_CHECKBOX_UNMANAGED_INTERCONNECT = "xpath=//*[@id='cic-logicalenclosure-edit-firmware-update-unmanaged']"
    ID_BUTTON_FORCE_INSTALL = "xpath=//*[@id='cic-logicalenclosure-edit-firmware-force']"
    ID_TEXT_ACTIVATION_CONTENT = "id=cic-logicalenclosure-enclosures-activation-content"
    ID_BUTTON_ACTIVATION_TYPE = "xpath=//*[@id='cic-logicalenclosures-activation-%s-type']"
    ID_BUTTON_CANCEL = "id=cic-logicalenclosure-fw-edit-cancel"
    ID_TEXT_WARNING_FORCE_INSTALL = "xpath=//*[@id='cic-logicalenclosure-edit-firmware-force-warning']/label/span"
    ID_TEXT_FW_DOWNGRADE_WARNING_MSG = "Downgrading the firmware can result in the installation of unsupported firmware and cause hardware to cease operation."
    ID_TEXT_WARNING_ORCHESTRATED = "id=cic-logicalenclosure-edit-firmware-orchestrated-type-message"
    ID_TEXT_WARNING_PARALLEL = "id=cic-logicalenclosure-edit-firmware-parallel-type-warning"
    ID_TEXT_PARALLEL_ACTIVATION_WARNING_MSG = "Warning: Parallel activation is optimized for faster updates and will cause service outages. Firmware updates using parallel activation should be performed within a maintenance window."
    ID_TEXT_ORCHESTRATED_ACTIVATION_WARNING_MSG = "Orchestrated activation will minimize service outages. Determining the extent of outages will be tested before activation begins"
    ID_BUTTON_FIRMWARE_UPDATE_OK = "id=cic-logicalenclosure-fw-edit-ok"
    ID_DIALOG_FW_UPDATE_FORM = "id=cic-logicalenclosure-edit-form"
    ID_TEXT_FW_UPDATE_HP_STATUS_ERROR = "xpath=//*[@id='cic-logicalenclosure-edit-form']//*[@class='hp-status hp-status-error']"
    ID_TEXT_FW_UPDATE_FORM_MESSAGE_SUMMARY = "xpath=//*[@id='cic-logicalenclosure-edit-form']//*[@class='hp-form-message-summary']"
    ID_TEXT_FW_UPDATE_FORM_MESSAGE_DETAILS = "xpath=//*[@id='cic-logicalenclosure-edit-form']//*[@class='hp-form-message-details']"
    ID_TEXT_UPDATE_STATUS_COMPLETE = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Completed']"
    ID_TEXT_UPDATE_STEP = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-step']"
    ID_TEXT_UPDATE_STATUS_ERROR = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Error']"
    ID_TEXT_UPDATE_STATUS_WARNING = "xpath=//*[@id='hp-page-notifications']/div[@class='hp-notification']/header/div[@class='hp-state' and text()='Warning']"
    ID_TEXT_LE_SERVER_HARDWARE = "//*[@id='cic-logicalenclosure-more-fw-table']//td[.='Server hardware']/../td[1+count(//*[@id='cic-logicalenclosure-more-fw-table']//a[.='%s']/../../../../following-sibling::*//td[.='Component']/preceding-sibling::td)]"
    ID_TEXT_LE_UPDATE_ACTIVITY = "xpath=//tbody/tr[td[@class='hp-name']/p/span[text()='%s']]"
    ID_TEXT_LE_UPDATE_ACTIVITY_STATE = "xpath=//tbody/tr[td[@class='hp-name']/p/span[text()='%s']]/td[@class='hp-date']/following-sibling::node()"
    ID_TEXT_LE_ACTIVITY_DETAILS = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]//following::*[@class='hp-notification-details']/*[@class='hp-details']"
    ID_TEXT_LE_ACTIVITY_ISSUE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::*[@class='hp-task-details hp-full']/*[@class='hp-task-notification-container']//*[@class='hp-details-correlations-container']//*[@class='hp-details-container']/span/p"
    ID_TEXT_LE_ACTIVITY_RESOLUTION = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::*[@class='hp-task-details hp-full']/*[@class='hp-task-notification-container']//*[@class='hp-details-correlations-container']//*[@class='hp-resolution-container']/span/p"
    ID_TEXT_EM_ACTIVITY_DETAILS = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]//following::node()[position()=1]//*[@class='hp-task-notification-container']//*[@class='hp-details']/p"
    ID_TEXT_EM_ACTIVITY_ISSUE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]/following::node()[position()=1]//*[@class='hp-details-correlations-container']//*[@class='hp-details']"
    ID_TEXT_EM_ACTIVITY_RESOLUTION = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]/following::node()[position()=1]//*[@class='hp-details-correlations-container']//*[@class='hp-resolution']"
    ID_TEXT_UNMANAGED_FW_ACTIVITY_STATE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-status-name']//span[text()='Firmware update for unmanaged interconnects']]//td[@class='hp-state']"
    ID_TEXT_ACTIVITY_COLLAPSER = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]//div[@class='hp-collapser']"
    ID_TEXT_UNMANAGED_ACTIVITY_DESC = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]//following::node()[position()=1]//div[@class='hp-details']/p"
    ID_TEXT_LI_SH_ACTIVITY = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]"
    ID_TEXT_LI_SH_ACTIVITY_DESC = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]//following::node()[position()=1]//div[@class='hp-details']/p"
    ID_TEXT_LI_SH_ISSUE = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]//following::node()[position()=1]//span[@class='hp-details']"
    ID_TEXT_LI_SH_RESOLUTION = "xpath=//tbody/tr[td[@class='hp-name']//span[text()='Logical enclosure firmware update']]/following::tr[td[@class='hp-source']/a[text()='%s']]//following::node()[position()=1]//span[@class='hp-resolution']//span"
