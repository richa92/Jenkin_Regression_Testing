# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion enclosures page/screen
'''


class FusionServerHardwarePage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Server Hardware']"
    ID_SERVER_LIST = "xpath=//div[@class='dataTables_scrollBody']/table"
    ID_SERVER_CHANGING = ID_SERVER_LIST + "/tbody/tr//div[@class='hp-status-changing']"
    ID_SERVER_LIST_NAMES = ID_SERVER_LIST + '/tbody/tr/td[2]'
    ID_LINK_ADD_SERVER_HARDWARE = "link=Add server hardware"
    ID_RADIO_MANAGED_OR_MONITOR = "xpath=//input[@name='servermanagementtype'][@value='%s']"
    ID_INPUT_ILO_IPADDRESS = "id=cic-server-hostname"
    ID_INPUT_ILO_USERNAME = "id=cic-server-username"
    ID_INPUT_ILO_PASSWORD = "id=cic-server-password"
    ID_BTN_SERVER_HW_ADD_AGAIN = "id=cic-server-add-again"
    ID_BTN_SERVER_HW_ADD = "link=Add server hardware"
    ID_BTN_SERVER_HW_CANCEL = "id=cic-server-add-cancel"
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ADD = "id=cic-server-add-action"
    ID_MENU_ACTION_POWEROFF = "id=cic-server-power-off-action"
    ID_MENU_ACTION_POWERON = "id=cic-server-power-on-action"
    ID_BTN_POWER_MOMENTERY_PRESS = "id=cic-server-momentary-press"
    ID_BTN_POWER_PRESS_AND_HOLD = "id=cic-server-press-and-hold"
    ID_MENU_ACTION_REFRESH = "id=cic-server-refresh-action"
    ID_MENU_ACTION_REMOVE = "id=cic-server-remove-action"
    ID_MENU_ACTION_LAUNCH_CONSOLE = "id=cic-server-launchconsole-action"
    ID_DLG_BTN_INSTALL_SOFTWARE = "id=cic-dialog-installer-button"
    ID_ELEMENT_SERVER_HARDWARE = "xpath=//td[text()='%s']"  # Replace %s with server Hardware
    ID_ELEMENT_SERVER_BASE = "//td[@class='' and text()='%s']/following-sibling::td[2]"
    ID_ELEMENT_POWER_STATE = "id=cic-server-power-state"
    # View
    ID_COMBO_MENU_VIEW_ = "css=div.hp-value"
    ID_LINK_OVERVIEW = "id=cic-server-overview-selector"
    ID_LINK_HARDWARE = "link=Hardware"
    ID_LINK_PORTS = "link=Ports"
    ID_LINK_UTILIZATION = "id=cic-server-utilization-selector"
    ID_LINK_ALERTS = "id=cic-server-alerts-selector"
    ID_LINK_RELATED = "link=Related"

    # new object
    ID_ELEMENT_SERVER_PROFILE_BASE = "xpath=//*[@id='DataTables_Table_0']/tbody/tr/td[text()='%s']"
    ID_RADIO_LICENSING_ADVANCE = "ID=cic-server-licensing-oneview"
    ID_RADIO_LICENSING_ADVANCE_NOILO = "id=cic-server-licensing-oneview-noilo"
    ID_ADD_SERVER_ERR_MSG = "xpath=.//*[@id='hp-form-message']/div[1]/span[contains(text(),'Unable to add')]"
    ID_BTN_ADD = "xpath=.//*[@id='cic-server-add']"
    ID_ADD_SERVER_HARDWARE_MSG = "xpath=.//*[@id='hp-form-message']/div[1]/span[@class='hp-form-message-text']"
    ID_ADD_SERVER_HARDWARE_ERR_DETAILS = "xpath=.//*[@id='hp-form-message']/div[@class='hp-form-message-details']"
    ID_FORCE_ADD_SERVER_HARDWARE = "xpath=.//*[@id='cic-server-force']"
    ID_ADD_SERVERHARDWARE_PROGRESS = "xpath=.//header/div[@class='hp-state']/div[@class='hp-progress']"
    ID_ACTIVITY_NOTIFY_DETAILS = "xpath=.//*[@id='hp-activities']/tbody/tr[@class='hp-row-details-row hp-selected']//div[@class='hp-details']/p[1]"
    ID_ACTIVITY_NOTIFY_CONTAINER = "xpath=.//*[@id='hp-activities']/tbody/tr[@class='hp-row-details-row hp-selected']/td/div/div[@class='hp-task-notification-container']"
    ID_ACTIVITY_COLLAPSE = "xpath=//td[@date-timestamp and contains(text(),'%s')]//preceding-sibling::td[a[text()='%s']]/preceding-sibling::td[p/span[contains(text(),'Add')]]/preceding-sibling::td/div[@class='hp-collapser']"
    ID_ADDSERVER_STATUS = "xpath=.//*/div/div[@class='dataTables_scrollBody']//tbody//tr/td[text()='%s']/preceding-sibling::td/div/span[@class='hp-value']"
    ID_ADDSERVER_TIMESTAMP = "xpath=.//*/div[1]/header/div[@class='hp-aside']/div[@class='hp-timestamp']"
    ID_SERVER_HARDWARE = "//*[@id='cic-server-type']/a"
    ID_ELEMENT_SERVER_HARDWARE_POWER_STATUS_OFF = "xpath=//div[text()='Off']"
    ID_ELEMENT_SERVER_HARDWARE_POWER_STATUS_ON = "xpath=//div[text()='On']"
    ID_POWER_TIMESTAMP = "xpath=.//*/div[1]/header/div[@class='hp-aside']/div[@class='hp-timestamp']"
    ID_SERVER_ACTIVITY = "xpath=//td[p/span[contains(text(),'%s')]]/following-sibling::td[@date-timestamp and contains(text(),'%s')]"
    ID_PANEL = "xpath=//div[@id='cic-server-panel-selector']"
    ID_SELECT_ACTIVITY = "link=Activity"
    ID_SELECT_OVERVIEW = "link=Overview"
    ID_SERVER_POWER_OFF_VALIDATE = ".//*[@id='cic-server-power-state' and text()='Off']"
    ID_SERVER_POWER_ON_VALIDATE = ".//*[@id='cic-server-power-state' and text()='On']"
    ID_ELEMENT_SERVER_HARDWARE_LABEL = "xpath=//h1[text()='%s']"
    ID_SERVER_ACTIVITY_ACTIVITY_PAGE = "xpath= //td[p/span[contains(text(),'%s')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"

    # Remove Server
    ID_LABEL_REMOVE_ERROR = "xpath=//div[@id='cic-server-action-error-message']"
    ID_BTN_REMOVE_ERROR_CLOSE = "id=cic-server-action-error-close"
    ID_BTN_DELETE_SERVER_CONFIRM = "id=cic-server-remove-confirm-yes"

    # XMAT
    ID_LAUNCH_CONSOLE_ERROR = "xpath=//div[@class='hp-status hp-status-error']/following-sibling::div/p/span[text()='Launch console']"
    ID_BTN_ALLREADY_INSTALLED = "id=cic-dialog-already-installed-button"
    ID_SERVER_COUNT = "//nav/div/span[text()='0']"
    ID_TABLE_SERVER_NAME = "//tbody/tr/td[text()='%s']"
    ID_ELEMENT_SERVER_OVERVIEW = "id=cic-server-panel-selector"
    ID_OVERVIEW_LINK_HARDWARE = "xpath=//*[@id='cic-server-panel-selector']/ol/li/a[text()='Hardware']"
    ID_ELEMENT_SERVER_STATE = "xpath=.//*[@id='cic-server-show-state']"
    ID_ELEMENT_SERVER_PROFILE = "xpath=.//*[@id='cic-server-profile-link']"
    ID_ELEMENT_SERVER_POWER_ON = "xpath=.//*[@id='cic-server-power-state']"
    ID_SERVER_MODEL = "xpath=.//*[@id='cic-server-model']"
    ID_SERVER_HARDWARE_TYPE = "xpath=.//*[@id='cic-server-type']"
    ID_SERVER_PRODUCT_ID = "xpath=.//*[@id='cic-server-part-number']"
    ID_SERVER_SER_NUM = "xpath=.//*[@id='cic-server-serial-number']"
    ID_SERVER_LICENSE = "xpath=.//*[@id='cic-server-license']"
    ID_SER_UID = "xpath=.//*[@id='cic-server-uuid']"
    ID_ILO_HOST_NAME = "xpath = (.//*[@id='cic-server-ilo-address-link'])[1]"
    ID_ILO_IPV4 = "xpath = (.//*[@id='cic-server-ilo-address-link'])[2]"
    ID_LINK_SERVER_LOCATION = "xpath = .//*[@id='cic-server-location']"
    ID_LINK_POWEREDBY = "xpath = .//*[@id='cic-server-power-connection']/span"
    ID_LINK_ASSETTAG = "xpath = .//*[@id='cic-server-asset-tag']"
    ID_LINK_MAX_POWER = "xpath = .//*[@id='cic-server-maximumPower']"
    ID_LINK_POWER_UNIT = "xpath = .//*[@id='cic-server-maximumPower-units']"
    ID_LINK_CPU = "xpath = .//*[@id='cic-server-cpu-sockets']"
    ID_LINK_MEMORY = "xpath = .//*[@id='cic-server-memory']"
    ID_LINK_ROM_VERSION = "xpath = .//*[@id='cic-server-rom-version']"
    ID_LINK_ILO_VERSION = "xpath = .//*[@id='cic-server-ilo-version']"
    ID_TABLE_SERVER_HARDWARE_PORT = "xpath = .//*[@id='cic-server-show-mezz-table-more']/tbody"
    ID_TABLE_SERVER_HARDWARE_PORT_ROW = ID_TABLE_SERVER_HARDWARE_PORT + "/tr[%s]/td[%s]"
    ID_SERVER_TAB_ACTIVITY = "//td[p/span[contains(text(),'%s')]]"
    ID_TABLE_SERVER_NAME_LIST = "xpath=//div[@class='dataTables_scroll']//table//tbody/tr/td[2]"
    ID_DIALOG_ADD_SERVER_HARDWARE = "id=cic-server-add-form"
    ID_SERVER_HARDWARE_ERROR_STATE = "//div[@id='DataTables_Table_0_wrapper']/div/div/table/tbody/tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"

    # Server hardware port ui change
    ID_TABLE_SERVER_HARDWARE_ADDRESS_ROW = ID_TABLE_SERVER_HARDWARE_PORT_ROW + "/ol/li[1]/div/div[1]/span[1]"
    ID_TABLE_SERVER_HARDWARE_INTERCONNECT_DOWNLINK_ROW = ID_TABLE_SERVER_HARDWARE_PORT_ROW + "/ol/li[2]/div/span"

    # Applied Solution
    ID_POWER_METER = "xpath = //span[@id='cic-utilization-power-meter-msg']"
    ID_NO_ILO_LICENSE = "xpath = //div[@id='cic-utilization-noLicense']"
    ID_CPU_METER = "xpath = //li[@id='cpu-meter-container' and @style='display: list-item;']"
    ID_TEMPERATURE_METER = "xpath = //li[@id='temperature-meter-container' and @style='display: list-item;']"
    ID_ELEMENT_TEMPERATURE = "xpath = //td[text()='Temperature']/following-sibling::td[@style='text-align: left;']"
    ID_SERVER_STATUS_OK = "xpath = //div[@id='cic-server-details-status' and @class='hp-status hp-status-ok']"
    ID_ERROR_WARN_MSG = "xpath = //*[@id='hp-page-notifications']/div/header/div/p/span"
    ID_SERVER_STATUS_ERROR = "xpath = //div[@id='cic-server-details-status' and @class='hp-status hp-status-error']"

    # Add labels
    ID_LINK_RESET = "link=Reset"
    ID_DROPDOWN_SELECTION = "link=Labels"
    ID_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/span[text()='Labels']"
    ID_EDIT_LABEL = "xpath = //li[@id='hp-labels-show-panel']/label/a[@class='hp-panel-edit' and text()='Edit']"
    ID_EDIT_LABEL_PANEL = "xpath = //header[@id='hp-labels-edit-header']/h1/span[text()='Edit Labels']"
    ID_LABEL_NAME = "id=hp-labels-edit-search-input"
    ID_ADD_LABEL_BTN = "id=hp-labels-edit-add"
    ID_OK_LABEL_BTN = "id=hp-labels-edit-ok"
    ID_ADDED_LABEL = "xpath = //table[@id='hp-labels-show-table']/descendant::a[text()='%s']"
