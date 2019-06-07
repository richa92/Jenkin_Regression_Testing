'''
Created on Mar 4, 2014

@author: Administrator
'''


class FusionStorageSystemsPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Storage Systems']"
    ID_STORAGE_SYSTEMS_LIST = "xpath=//*[@class='dataTables_scrollBody']//tbody/tr/td[2]"

    ID_LINK_ADD_STORAGE_SYSTEM = "link=Add storage system"
    # Action Menu
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ADD = "link=Add"
    ID_MENU_ACTION_EDIT = "link=Edit"
    ID_MENU_ACTION_EDIT_CREDENTIALS = "link=Edit Credentials"
    ID_MENU_ACTION_REMOVE = "link=Remove"

    # Storage system details
    ID_INPUT_STORAGE_SYSTEM_IP_OR_HOSTNAME = "id=cic-storagesystems-hostname"
    ID_INPUT_STORAGE_SYSTEM_USERID = "id=cic-storagesystems-username"
    ID_INPUT_STORAGE_SYSTEM_PASSWORD = "id=cic-storagesystems-password"
    ID_BTN_CONNECT = "id=cic-storagesystems-connect"
    ID_MESSAGE_WHILE_CONNECT = "xpath=//div[@class='hp-form-message-summary']/span[text()='Connecting to the storage system...']"
    ID_MESSAGE_CONNECT_STORAGE_SUMMARY = "xpath=//div[@class='hp-form-message-summary']"
    ID_MESSAGE_CONNECT_STORAGE_DETAILS = "xpath=//div[@class='hp-form-message-details']"
    ID_INPUT_SEARCH_DOMAIN = "xpath=//input[@id='cic-storagesystems-add-domain-input']"
    ID_DROPDOWN_SEARCH_DOMAIN = "xpath=//div[@id='cic-storagesystems-add-domain-section']//div[@class='hp-search-combo-menu']/ol[@class='hp-options']"
    ID_BTN_ADD_STORAGE_POOL = "id=cic-storagesystems-add-addpools"
    ID_INPUT_SEARCH_STORAGE_POOL = "xpath=//div[@id='hp-association-edit']/div/input"
    ID_TABLE_STORAGE_POOL_MATCH = "xpath=//table[@id='hp-edit-choices']/tbody/tr/td[1]"
    ID_BTN_STORAGE_POOLS_ADD = "xpath=//div[@id='hp-association-edit']/footer//button[text()='Add']"
    ID_BTN_STORAGE_POOLS_CANCEL = "xpath=//div[@id='hp-association-edit']/footer//button[text()='Cancel']"
    ID_BTN_STORAGE_POOL_EDIT_OK = "xpath=//input[@id='cic-storagesystems-edit']"

    # tabs
    ID_LINK_NAVIGATE = "xpath=//*[@id='cic-storagesystems-panel-add-selector']/div"
    ID_LINK_STORAGE_POOLS = "link=Storage Pools"
    ID_LINK_STORAGE_PORTS = "link=Storage System Ports"

    # system ports
    ID_TABLE_SYSTEM_PORTS_BASE = "xpath=//table[@id='cic-storagesystems-add-ports-assigned']"
    ID_COMBO_INPUT_EXPECTED_NETWORK = "xpath=//table[@id='cic-storagesystems-add-ports-assigned']/tbody/tr[descendant::td[contains(.,'%s')] and td[contains(.,'%s')]]/td[3]//input"
    ID_COMBO_INPUT_PORT_GROUP = "xpath=//table[@id='cic-storagesystems-add-ports-assigned']/tbody/tr[descendant::td[contains(.,'%s')] and td[contains(.,'%s')]]/td[5]//input[@class='hp-search-combo-input']"

    # edit storage system
    ID_COMBO_INPUT_EXPECTED_NETWORK_EDIT = "xpath=//table[@id='cic-storagesystems-edit-ports-assigned']/tbody/tr[descendant::td[contains(.,'%s')] and td[contains(.,'%s')]]/td[3]//input"
    ID_COMBO_INPUT_PORT_GROUP_EDIT = "xpath=//table[@id='cic-storagesystems-edit-ports-assigned']/tbody/tr[descendant::td[contains(.,'%s')] and td[contains(.,'%s')]]/td[5]//input[@class='hp-search-combo-input']"

    # ADD,ADD+ and CANCEL BUTTONS
    ID_BTN_CANCEL_STORAGE_SYSTEMS = "id=cic-storagesystems-add-cancel"
    ID_BTN_ADD_PLUS_STORAGE_SYSTEMS = "cic-storagesystems-add-plus"
    ID_BTN_ADD_STORAGE_SYSTEMS = "id=cic-storagesystems-add"

    # Message
    ID_MESSAGE_STORAGE_ADD = "xpath=//div[@class='hp-form-message-summary']/span[text()='Adding storage systems']"
    ID_TABLE_STORAGE_SYS_FIND = "xpath=//td[@class='' and text()='%s']"
    ID_STATUS_STORAGE_SYSTEM = "xpath=//tbody/tr[descendant::td[contains(.,'%s')]]//span[text()='ok']"

    # Refresh
    ID_REFRESH_STORAGE_SYSTEM = "cic-storagesystems-refresh-action"
    ID_LABEL_PAGE_NOTIFICATION = "xpath=//div[@id='hp-page-notifications']/div[@class='hp-notification']/header[@class='hp-notification-summary']/div[@class='hp-state']"

    # edit credentials page
    ID_INPUT_EDIT_CREDENTIALS_HOSTNAME = "id=cic-storagesystems-editcredentials-hostname"
    ID_INPUT_EDIT_CREDENTIALS_USERNAME = "id=cic-storagesystems-editcredentials-username"
    ID_INPUT_EDIT_CREDENTIALS_PASSWORD = "id=cic-storagesystems-editcredentials-password"
    ID_BTN_EDIT_CREDENTIALS_OK = "id=cic-storagesystems-editcredentials-ok"
    ID_LABEL_PAGE_NOTIFICATION = "xpath=//div[@id='hp-page-notifications']/div[@class='hp-notification']/header"
    ID_LABEL_PAGE_ERROR = "xpath=.//div[@id='hp-page-notifications']/div[1]/header/div[@class='hp-status hp-status-error']"
    ID_LABEL_PAGE_ERROR_FULL = "xpath=//div[@id='hp-page-notifications']/div[@class='hp-notification']/div"
    ID_STATUSBAR_EDIT = "xpath=//div[@id='hp-page-notifications']//header//div[@class='hp-progress']"

    # Remove Storage System
    ID_MESSAGE_WARNING = "xpath=//div[@class='hp-dialog']//div[@class='hp-notify hp-notify-warning hp-active']"
    ID_BTN_WARNING_CLOSE = "xpath=//footer/div/button"
    ID_BTN_STORAGE_STSTEM_REMOVE = "xpath=//button[text()='Yes, Remove']"
    ID_LINK_RESET = "link=Reset"
