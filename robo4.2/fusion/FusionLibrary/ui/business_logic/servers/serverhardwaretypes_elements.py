class GeneralServerHardwareTypeElements(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Server Hardware Types']"

    # action button
    ID_BUTTON_ACTIONS = "xpath=//label[text()='Actions']"

    # for verify
    ID_TABLE_SHT = "xpath=//ol[contains(@class, 'hp-master-grid')]/li//div[.='%s']"
    ID_TABLE_SHTS = "xpath=//ol[contains(@class, 'hp-master-grid')]/li/header/div"
    ID_TABLE_SHT_SELECTED = "xpath=//ol[contains(@class, 'hp-master-grid')]/li[header/div[.='%s'] and contains(@class, 'hp-selected')]"
    ID_TEXT_SHT_TITLE = "xpath=//h1[@id='cic-servertypes-details-title']"
    ID_TABLE_SHT_DELETED = "xpath=//ol[contains(@class, 'hp-master-grid')]/li[header/div[.='%s'] and contains(@class, 'hp-not-found')]"

    ID_STATUS_NOTIFICATION_OK = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']"
    ID_STATUS_NOTIFICATION_WARN = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-warning']"
    ID_STATUS_NOTIFICATION_ERROR = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-status hp-status-error']"
    ID_TEXT_NOTIFICATION_MESSAGE = "xpath=//div[@class='hp-notification']/header[@class='hp-notification-summary']/div/p/span"
    ID_TEXT_NOTIFICATION_RESOLUTION = "xpath=//div[@class='hp-notification']/div/div/div[@class='hp-notification-details']/div[@class='hp-resolution-container']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-servertypes-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"
    ID_TEXT_ACTIVITY_ACTION_OK = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]/../div[@class='hp-status hp-status-ok']"
    ID_TEXT_ACTIVITY_ACTION_WARN = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]/../div[@class='hp-status hp-status-warning']"
    ID_TEXT_ACTIVITY_ACTION_ERROR = "xpath=//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-source' and text()='%s' and ../div[@class='hp-activity-message'][starts-with(., '%s')]]/../div[@class='hp-status hp-status-error']"
    ID_TEXT_ACTIVITY_MESSAGE = "xpath=//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"

    ID_TEXT_DETAILS_STATUS_OK = "xpath=//div[@id='cic-servertypes-details-status' and @class='hp-status hp-status-ok']"
    ID_TEXT_GENERAL_SERVER_MODEL = "id=cic-servertype-model"
    ID_TEXT_GENERAL_FORM_FACTOR = "id=cic-servertype-form-factor"
    ID_TEXT_GENERAL_DESCRIPTION = "id=cic-servertype-description"
    ID_TEXT_GENERAL_USED_BY = "xpath=//div[@id='cic-servertype-usedby']|//div[@id='cic-servertype-usedby']/a"
    ID_TEXT_GENERAL_USED_BY_SH = "xpath=//div[@id='cic-servertype-usedby']/ol/li[1]/a"
    ID_TEXT_GENERAL_USED_BY_SP = "xpath=//div[@id='cic-servertype-usedby']/ol/li[2]/a"
    ID_TEXT_ADAPTERS_ROW_LOCATION = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Location']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_MODEL = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Model']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_DEVICE_TYPE = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Device Type']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_MAX_PORT_SPEED = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Max Port Speed']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_PHYSICAL_PORTS = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Physical Ports']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_VIRTUAL_PORTS = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Virtual Ports']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_AVAILABLE_VIRTUAL_FUNCTIONS = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Available Virtual Functions']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_VIRTUAL_FUNCTION_ALLOCATION_INCREMENT = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Virtual Function Allocation Increment']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_ETHERNET = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='Ethernet']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_FC = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='FC']/preceding-sibling::td)]"
    ID_TEXT_ADAPTERS_ROW_ISCSI = "xpath=//table[@id='cic-servertypes-adapters-table']//tr[td[.='%s']]/td[1+count(//table[@id='cic-servertypes-adapters-table']/thead/tr/td[text()='iSCSI']/preceding-sibling::td)]"

    # option panel
    ID_DROPDOWN_PANEL_SELECTOR = "id=cic-servertypes-panel-selector"
    ID_SELECT_GENERAL_PANEL = "xpath=//ol[@class='hp-options']//a[.='General']"
    ID_SELECT_ADAPTERS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Adapters']"
    ID_SELECT_LABELS_PANEL = "xpath=//ol[@class='hp-options']//a[.='Labels']"


class EditServerHardwareTypeElements(object):
    ID_SELECT_ACTION_EDIT = "id=cic-servertypes-launchedit-action"

    ID_DIALOG_EDIT_SHT = "id=cic-servertypes-edit-form"
    ID_INPUT_NAME = "id=cic-servertypes-name"
    ID_INPUT_DESCRIPTION = "id=cic-servertypes-description"
    ID_BUTTON_OK = "id=cic-servertypes-edit-ok"
    ID_BUTTON_CANCEL = "id=cic-servertypes-edit-cancel"


class DeleteServerHardwareTypeElements(object):
    ID_SELECT_ACTION_DELETE = "id=cic-servertypes-launchdelete-action"

    ID_DIALOG_DELETE_SHT = "xpath=//button[.='Yes, delete']"  # should verify if confirm button show in dialog since delete error dialog has same id attribute as normal delete dialog
    ID_BUTTON_YES_DELETE = "xpath=//button[.='Yes, delete']"
    ID_BUTTON_CANCEL = "xpath=//button[.='Cancel']"

    # can't be removed, being referenced
    ID_DIALOG_DELETE_ERROR = "id=cic-servertypes-delete-inuse-content"
    ID_TEXT_DELETE_ERROR = "id=cic-servertypes-delete-attention-warning-msg"
    ID_BUTTON_CLOSE = "xpath=//div[@id='cic-servertypes-delete-dialog']//button[.='Close']"
