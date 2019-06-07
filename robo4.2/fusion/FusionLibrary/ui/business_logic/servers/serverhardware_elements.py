class GeneralServerHardwareElements(object):

    ID_TEXT_VIEW_ACTIVITY = "xpath=//tbody/tr/td/div[number(translate(@title,'-:TZ','')) > number('%s')]/../../td/p/span[text()='%s']/../../../td/div[@class='hp-status hp-status-%s']"
    ID_TEXT_SIDEBAR_ACTIVITY_TIME = "xpath=//ol[@id='hp-flyout-activities']/li[div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]][1]/div/header/div[@class='hp-timestamp']/div[@title]"
    ID_TABLE_SERVER_HARDWARE = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[text()='%s']"  # server hardware name
    ID_TABLE_SERVER_HARDWARE_LIST = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[2]"
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-server-panel-selector"
    ID_SELECT_OVERVIEW_PANEL = "xpath=//ol[@class='hp-options']//a[.='Overview']"
    ID_SELECT_HARDWARE_PANEL = "xpath=//ol[@class='hp-options']//a[.='Hardware']"
    ID_SELECT_FIRMWARE_PANEL = "xpath=//ol[@class='hp-options']//a[.='Ports']"
    ID_SELECT_UTILIZATION_PANEL = "xpath=//ol[@class='hp-options']//a[.='Utilization']"
    ID_SELECT_ACTIVITY_PANEL = "xpath=//ol[@class='hp-options']//a[.='Activity']"
    ID_SELECT_MAP_PANEL = "xpath=//ol[@class='hp-options']//a[.='Map']"
    ID_SELECT_LABELS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Labels']"
    ID_STATUS_SERVER_HARDWARE_OK = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # server hardware name
    ID_STATUS_SERVER_HARDWARE_WARN = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"  # server hardware name
    ID_STATUS_SERVER_HARDWARE_ERROR = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"  # server hardware name
    ID_STATUS_SERVER_HARDWARE_UNKNOWN = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-unknown']"  # server hardware name
    ID_TABLE_SERVER_HARDWARE_SELECTED = "//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-selected')]/td[text()='%s']"  # server hardware name
    ID_TABLE_SERVER_HARDWARE_DELETED = "//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # server hardware name
    # ID_DROPDOWN_ACTIONS = "xpath=//label[text()='Actions']"
    ID_DROPDOWN_ACTIONS = "xpath=//*[contains(@class, 'hp-drop-menu')]"
    ID_PAGE_NOTIFICATION_MESSAGE = "//*[@id='hp-page-notifications']/div[@class='hp-controls' and (descendant::span)]/../div[@class='hp-notification']//div[@class='hp-message']/p/span"

    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-servers-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # volume template
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # volume template
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # volume template
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"

    ID_TEXT_HARDWARE_SERVER_POWER = "xpath=//*[@id='cic-server-power-state']"
    ID_TEXT_HARDWARE_STATE = "xpath=//*[@id='cic-server-show-state']"
    ID_TEXT_HARDWARE_SERVER_HARDWARE_TYPE = "xpath=//*[@id='cic-server-type']"
    ID_TEXT_HARDWARE_SERVER_PROFILE = "//*[@id='cic-server-profile-link']/span|//*[@id='cic-server-profile-link']/i/a|//*[@id='cic-server-profile-link']/a"

    ID_TEXT_SCOPE = "//table[@id='hp-scopes-resource-show-table']//td[text()='%s']"

    # UID Light
    ID_BUTTON_UID_LIGHT = "id=cic-server-uid-light-control"
    ID_STATUS_UID_LIGHT_ON = "//div[@id='cic-server-uid-light-control' and contains(@class, 'hp-on')]"
    ID_STATUS_UID_LIGHT_OFF = "//div[@id='cic-server-uid-light-control' and @class='hp-uid-big hp-tooltipped']"

    # activity
    ID_ICON_ACTIVITY_COLLAPSER = "//table[@class='hp-index-table hp-activities dataTable']/tbody/tr//span[text()='%s']/../../../td//div[@class='hp-collapser']"  # activity collapser
    ID_TEXT_ACTIVITY_SUB_TASK = "//tr/td/div[.='%s']/../span[text()='%s']/../..//a[.='%s']"


class AddServerHardwareElements(object):
    ID_BUTTON_ADD_SERVER_HARDWARE = "link=Add server hardware"
    ID_SELECT_ACTION_ADD = "id=cic-server-add-action"

    ID_DIALOG_ADD_SERVER_HARDWARE = "//section[@class='hp-details-add-section']"
    ID_INPUT_ILO_IP = "id=cic-server-hostname"
    ID_ERR_MSG_INPUT_ILO_IP_OR_HOST_NAME = "xpath=//label[@for='cic-server-hostname']"
    ID_RADIO_ADD_SERVER_HARDWARE_AS_MANAGED = "id=cic-server-management-type-managed"
    ID_RADIO_ADD_SERVER_HARDWARE_AS_MONITORED = "id=cic-server-management-type-monitored"
    ID_INPUT_USER_NAME = "id=cic-server-username"
    ID_ERR_MSG_USER_NAME = "xpath=//label[@for='cic-server-username']"
    ID_INPUT_PASSWORD = "id=cic-server-password"
    ID_ERR_MSG_PASSWORD = "xpath=//label[@for='cic-server-password']"
    ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED = "id=cic-server-licensing-oneview"
    ID_RADIO_LICENSING_HP_ONEVIEW_ADVANCED_WO_ILO = "id=cic-server-licensing-oneview-noilo"
    ID_TEXT_VERIFYING_PARAMETERS = "xpath=//div/span[contains(., 'Verifying parameters...')]"
    ID_BUTTON_ADD = "id=cic-server-add"
    ID_BUTTON_ADD_PLUS = "id=cic-server-add-again"
    ID_BUTTON_CANCEL = "id=cic-server-add-cancel"
    ID_CHECKBOX_FORCE_ADD = "xpath=.//*[@id='cic-server-force']"

    ID_ERR_MSG_ALREADY_MONITORED = "xpath=//div[text()='This server is already being monitored by this appliance.']"
    ID_ERR_MSG_MINIMUM_FW_ILO4 = "xpath=//*[contains(text(), 'Supported firmware versions are 1.30 or higher.')]"
    ID_ERR_MSG_MINIMUM_FW_ILO3 = "xpath=//*[contains(text(), 'Supported firmware versions are 1.61 or higher.')]"
    ID_ERR_MSG_MINIMUM_FW_ILO2 = "xpath=//*[contains(text(), 'Supported firmware versions are 2.12 or higher.')]"
    ID_ERR_MSG_MONITOR_ALREADY_MANAGED = "xpath=//*[contains(text(), 'The server is already being managed')]"
    ID_ERR_MSG_MANAGE_ALREADY_MANAGED = "xpath=//*[contains(text(), 'The server hardware has already been added')]"
    # ID_ERR_MSG_MANAGE_SINGLE_BLADE = "xpath=//*[contains(text(), 'The server hardware % is part of a BladeSystem enclosure. Use add enclosure to bring this blade under management')]"
    # use ID_ERR_MSG_MANAGE_SINGLE_BLADE.format('16.125.74.206') to fill in the values of parameter {0}
    # use ID_ERR_MSG_MANAGE_SINGLE_BLADE.format(server.iloIP)
    ID_ERR_MSG_MANAGE_SINGLE_BLADE = "xpath=//*[contains(text()[1], 'The server hardware {0} is part of a BladeSystem enclosure.') and contains(text()[2], 'Use') and contains(./a/text(), 'add enclosure') and contains(text()[3], 'to bring this blade under management')]/../div/*[contains(text(), 'Unable to add server hardware: {0}')]"


class PowerOnHardwareElements(object):
    ID_SELECT_ACTION_POWER_ON = "xpath=//*[@id='cic-server-power-on-action']"
    ID_ERROR_MSG_POWER_ON_DURING_DELETING_PROFILE = "xpath=//*[@id='cic-server-action-error-message']"
    ID_BUTTON_CLOSE_ERROR_DIALOG = "xpath=//*[@id='cic-server-action-error-close']"
    # ID_ERROR_MSG_POWER_ON_DURING_DELETING_PROFILE = "xpath=//*[@id='cic-server-action-error-message']/descendant-or-self::*"


class PowerOffHardwareElements(object):
    ID_SELECT_ACTION_POWER_OFF = "xpath=//*[@id='cic-server-power-off-action']"
    ID_BUTTON_MOMENTARY_PRESS = "xpath=//*[@id='cic-server-momentary-press']"
    ID_BUTTON_PRESS_AND_HOLD = "xpath=//*[@id='cic-server-press-and-hold']"
    ID_BUTTON_CLOSE = "xpath=//*[@id='cic-server-poweroff-cancel']"


class ResetHardwareElements(object):
    ID_TEXT_REST_ILO_WARN_MSG = "xpath=//div[@id='cic-server-action-error-message']"
    ID_DIALOG_RESET_ILO = "xpath=//div[@class='hp-dialog']//span[text()='Reset iLO']"
    ID_SELECT_ACTION_RESET_ILO = "xpath=//a[@id='cic-server-softReset-action']"
    ID_BUTTON_CANCEL_RESET_ILO = "xpath=//a[@id='cic-server-softReset-cancel']"
    ID_BUTTON_CLOSE_RESET_ILO = "xpath=//button[@id='cic-server-action-error-close']"
    ID_BUTTON_YES_RESET = "xpath=//input[@id='cic-server-softReset-confirm-yes']"

    ID_SELECT_ACTION_RESET = "xpath=//*[@id='cic-server-reset-action']"
    ID_BUTTON_RESET = "xpath=//button[@id='cic-server-reset']"
    ID_BUTTON_COLD_BOOT = "xpath=//button[@id='cic-server-cold-boot']"
    ID_BUTTON_CANCEL = "xpath=//button[@id='cic-server-reset-cancel']"


class RefreshHardwareElements(object):
    ID_SELECT_ACTION_REFRESH = "xpath=//*[@id='cic-server-refresh-action']"
    ID_TITLE_FORCE_REFRESH_DIALOG = "xpath=//*[@id='cic-server-refresh-title']"
    ID_INPUT_HOSTNAME_FORCE_REFRESH = "xpath=//*[@id='cic-server-hostname']"
    ID_INPUT_USERNAME_FORCE_REFRESH = "xpath=//*[@id='cic-server-username']"
    ID_INPUT_PASSWORD_FORCE_REFRESH = "xpath=//*[@id='cic-server-password']"
    ID_BUTTON_ADD_FORCE_REFRESH = "xpath=//*[@id='cic-server-refresh-confirm-ok']"


class RemoveHardwareElements(object):
    ID_SELECT_ACTION_REMOVE = "xpath=//*[@id='cic-server-remove-action']"
    ID_BUTTON_YES_REMOVE = "xpath=//*[@id='cic-server-remove-confirm-yes']"
    ID_BUTTON_CANCEL = "xpath=//*[@id='cic-server-remove-cancel']"


class UtilizationElements(object):
    # power meter is collected
    ID_TEXT_UTI_COLLECTED_CPU = "xpath=//*[@id='cpu-meter-container']/div"
    ID_TEXT_UTI_COLLECTED_POWER = "xpath=//*[@id='power-meter-container']/div"
    ID_TEXT_UTI_COLLECTED_TEMPERATURE = "xpath=//*[@id='temperature-meter-container']/div"

    # power meter not supported or power meter has no data in 24 hours
    ID_TEXT_UTI_NOTCOLLECTED_CPU = "xpath=//*[@id='cpu-meter-container']/span[@style='display: inline-block;']"
    ID_TEXT_UTI_NOTCOLLECTED_POWER = "xpath=//*[@id='power-meter-container']/span[@style='display: inline-block;']"
    ID_TEXT_UTI_NOTCOLLECTED_TEMPERATURE = "xpath=//*[@id='temperature-meter-container']/span[@style='display: inline-block;']"


class VerifyHardwareElements(object):

    ID_TEXT_ACTION_NO_AUTHORIZATION = "xpath=.//*[contains(text(),'No authorization')]"


class EditScopeElements(object):
    ID_HEADER_SCOPE = "//li[@id='hp-scopes-resource-show-panel']/label/span[text()='Scopes']"
    ID_TEXT_SCOPE_NOT_LOAD = "//li[@id='hp-scopes-resource-show-panel']/div[@class='hp-unavailable']"
    ID_BUTTON_EDIT = "//li[@id='hp-scopes-resource-show-panel']/label/a[.='Edit']"
    ID_DIALOG_EDIT = "//header[@id='hp-scopes-edit-header']"
    ID_DIALOG_ASSIGN = "//*[@class='hp-ellipsised']//span[contains(text(),'Assign to Scopes')]"
    ID_BUTTON_OK = "id=hp-scopes-edit-ok"
    ID_BUTTON_CANCEL = "id=hp-scopes-edit-cancel"
    ID_BUTTON_CLOSE = "id=hp-scopes-edit-close"
    ID_BUTTON_ASSIGN = "hp-scopes-edit-add"
    ID_BUTTON_ADD = "xpath=//button[.='Add']"
    ID_BUTTON_ADD_PLUS = "xpath=//button[.='Add +']"
    ID_BUTTON_CANCEL_ASSIGN = "xpath=//button[.='Cancel']"
    ID_INPUT_SEARCH_TEXT = "//input[@class='hp-search']"
    ID_TABLE_SCOPE_NAME = "//form[@class='hp-edit-form']//table/tbody/tr/td[text()='%s']"
    ID_TABLE_REMOVE_SCOPE = "//form[@class='hp-edit-form']//table/tbody/tr[td[text()='%s']]//div"
