# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion SAN Managers page/screens
Modified by: Connie Johnson
'''


class FusionSANManagersPage(object):

    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='SAN Managers']"
    ID_PAGE_LINK = "link=SAN Managers"
    ID_SAN_MANAGER_LIST = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td"
    ID_ADD_SAN_MANAGER_TITLE = "//div[@id='cic-sanmanagers-page']/x:div[2]/x:div[1]/x:header/x:h1/x:div[1]/x:a"
    ID_ADD_SAN_MANAGER_TITLE3 = "//*[@id='hp-change-page-container']/section/div/h1"
    ID_ADD_SAN_MANAGER_TITLE2 = "xpath=//*[@id='cic-sanmanagers-page']/div[2]/div[1]/header/h1/div[1]/a"

# SAN manager overview screen
    ID_ELEMENT_SAN_MANAGER = "xpath=//td[text()='%s']"  # Replace %s with SAN Manager IP
    ID_ADD_SAN_MANAGER = "link=Add SAN manager"
    ID_INPUT_ADD_SAN_MANAGER = "id=cic-sanmanagers-add-attribute0"
    ID_SELECT_BOX_LABEL = "xpath=//div[@class='hp-select-form']/div"
    ID_SAN_MANAGER_LIST_NAMES = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td[2]"
    ID_ADD_SAN_PROGRESS = "xpath=.//header/div[@class='hp-state']/div[@class='hp-progress']"
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_REMOVE = "link=Remove"
    ID_MENU_ACTION_REFRESH = "link=Refresh"
    ID_MENU_ACTION_ADD = "link=Add"
    ID_MENU_ACTION_EDIT = "link=Edit"

#   SAN manager tabs
    ID_SAN_MANAGER_TABS = "xpath=//*[@id='cic-sanmanagers-panel-selector']/div"
    ID_VIEW_GENERAL = "xpath=.//*[@id='cic-sanmanagers-panel-selector']/ol/li[1]/a"
    ID_VIEW_ACTIVITY = "xpath=.//*[@id='cic-sanmanagers-panel-selector']/ol/li[2]/a"
    ID_VIEW_MAP = "xpath=.//*[@id='cic-sanmanagers-panel-selector']/ol/li[3]/a"

    ID_BTN_DELETE_SAN_CONFIRM = "xpath=//button[text()='Yes, remove']"
    ID_DELETE_SAN_DEPENDENCE = "Xpath = //span[@data-localize='sanmanagers.remove.dependenciesMessage']"
    ID_BTN_SAN_REMOVE = "xpath=//button[text()='Yes, remove']"
    ID_BTN_SAN_REMOVE_NOT_EXIST = "xpath=//*[@id='hp-not-exist']/div[2]"
    ID_DELETE_SAN_ERROR = "ERROR-//div[@class='hp-notify']/span"
    ID_ELEMENT_SAN_MANAGER_DELETED = "xpath=//table/tbody/tr[td[.='%s'] and contains(@class, 'hp-not-found')]"
    ID_SAN_MANAGER_TYPE = "//div[@id='cic-sanmanagers-general-type']"
    ID_SAN_MANAGER_DESCRIPTION = "//div[@id='cic-sanmanagers-hp-description']"
    ID_SAN_MANAGER_STATE = "//div[@id='cic-sanmanagers-general-state']"
    ID_SAN_MANAGER_VERSION = "//div[@id='cic-sanmanagers-general-version']"
    ID_SAN_MANAGER_HP_SSH_USER_NAME = "//div[@id='cic-sanmanagers-User name']"
    ID_SAN_MANAGER_HP_USERNAME = "//div[@id='cic-sanmanagers-dynamic-attribute-0']"
    ID_SAN_MANAGER_HP_SNMP_PORT = "//div[@id='cic-sanmanagers-dynamic-attribute-1']"
    ID_SAN_MANAGER_HP_SNMP_USER_NAME = "//div[@id='cic-sanmanagers-dynamic-attribute-2']"
    ID_SAN_MANAGER_HP_SECURITY_LEVEL = "//div[@id='cic-sanmanagers-dynamic-attribute-3']"
    ID_SAN_MANAGER_HP_AUTHENTICATION_PROTOCOL = "//div[@id='cic-sanmanagers-dynamic-attribute-4']"
    ID_SAN_MANAGER_HP_PRIVACTY_PROTOCOL = "//div[@id='cic-sanmanagers-dynamic-attribute-5']"

# Brocade switch
    ID_SAN_MANAGER_BNA = "xpath=//div[text()='Brocade Network Advisor']"
    ID_SAN_MANAGER_BNA_PORT = "id=cic-sanmanagers-add-attribute1"
    ID_SAN_MANAGER_BNA_USE_SSL = "//div[@id='cic-sanmanagers-dynamic-attribute-2']"
    ID_SAN_MANAGER_BNA_USERNAME = "//div[@id='cic-sanmanagers-dynamic-attribute-1']"
    ID_SAN_BNA_HOST = "id=cic-sanmanagers-add-attribute0"
    ID_SAN_BNA_SSL = "id=cic-sanmanagers-add-attribute1"
    ID_SAN_BNA_USER = "id=cic-sanmanagers-add-attribute2"
    ID_SAN_BNA_PSWD = "id=cic-sanmanagers-add-attribute3"

# HP 5900 switch
    ID_SAN_MANAGER_HP_SWITCH = "xpath=//span[text()='HP']"
    ID_SAN_HP_SWITCH_HOST = "id=cic-sanmanagers-add-attribute5"
    ID_SAN_HP_SWITCH_PORT = "id=cic-sanmanagers-add-attribute6"
    ID_SAN_HP_SWITCH_SNMP_USER = "id=cic-sanmanagers-add-attribute7"
    ID_SAN_HP_SWITCH_SECURITY_LEVEL_NONE = "id=noauthnopriv"
    ID_SAN_HP_SWITCH_SECURITY_LEVEL_AUTHENTICATION = "id=authnopriv"
    ID_SAN_HP_SWITCH_SECURITY_LEVEL_PRIVACY = "id=authpriv"
    ID_SAN_HP_SWITCH_SECURITY_AUTH_PROTOCOL = "xpath=//label[text()='Authentication protocol']/following-sibling::div//div[@class='hp-select']"
    ID_SAN_HP_SWITCH_SECURITY_AUTH_PASSWORD = "id=cic-sanmanagers-add-attribute9"
    ID_SAN_HP_SWITCH_SECURITY_PRIV_PROTOCOL = "xpath=//label[text()='Privacy protocol']/following-sibling::div//div[@class='hp-select']"
    ID_SAN_HP_SWITCH_SECURITY_PRIV_PASSWORD = "id=cic-sanmanagers-add-attribute11"

# CISCO switch
    ID_SAN_MANAGER_CISCO_SWITCH = "xpath=//span[text()='Cisco']"
    ID_SAN_MANAGER_CISCO_SWITCH_HOST = "xpath=//*[@id='cic-sanmanagers-add-general-fieldlist']/li/label"
    ID_SAN_MANAGER_CISCO_SWITCH_HOST_NAME = "id=cic-sanmanagers-add-attribute5"
    ID_SAN_MANAGER_CISCO_SWITCH_PORT = "id=cic-sanmanagers-add-attribute6"
    ID_SAN_MANAGER_CISCO_SWITCH_SNMP_USER = "id=cic-sanmanagers-add-attribute7"
    ID_SAN_MANAGER_CISCO_SWITCH_SECURITY_LEVEL_AUTHENTICATION = "id=authnopriv"
    ID_SAN_MANAGER_CISCO_SWITCH_SECURITY_LEVEL_PRIVACY = "id=authpriv"
    ID_SAN_MANAGER_CISCO_SWITCH_SECURITY_AUTH_PROTOCOL = "xpath=//label[text()='Authentication protocol']/following-sibling::div//div[@class='hp-select']"
    ID_SAN_MANAGER_CISCO_SWITCH_SECURITY_AUTH_PASSWORD = "id=cic-sanmanagers-add-attribute9"
    ID_SAN_MANAGER_CISCO_SWITCH_SECURITY_PRIV_PROTOCOL = "xpath=//label[text()='Privacy protocol']/following-sibling::div//div[@class='hp-select']"
    ID_SAN_MANAGER_CISCO_SWITCH_SECURITY_PRIV_PASSWORD = "id=cic-sanmanagers-add-attribute11"

# Add SAN manager screen
    ID_BTN_SAN_MANAGER_ADD = "id=cic-sanmanagers-add-add-button"
    ID_BTN_SAN_MANAGER_ADD_PLUS = "id=cic-sanmanagers-add-add-again-button"
    ID_BTN_SAN_MANAGER_CANCEL = "id=cic-sanmanagers-add-cancel-button"
    ID_ADD_SAN_PROGRESS = "xpath=.//header/div[@class='hp-state']/div[@class='hp-progress']"
    ID_REMOVE_SAN_MANAGER_VERIFY = "xpath=//button[text()='Yes, remove']"

# Add SAN manager errors
    ID_ADD_SAN_ERR_MSG = "xpath=.//*[@id='hp-form-message']/div[1]/span[contains(text(),'Unable to add')]"
    ID_ADD_SAN_ERR_DETAILS = "xpath=.//*[@id='hp-form-message']/div[@class='hp-form-message-details']"
    ADD_SAN_ERR_MSG = "//*[@id='hp-form-message']//span[text()='Unable to add SAN manager.']"
    ADD_SAN_REQUIRED_ERR_MSG = "//*[@id='cic-sanmanagers-add-general-fieldlist']//label[text()='This field is required.']"
    ADD_SAN_ERR_LINE_DETAILS = "//*[@id='cic-sanmanagers-add-general-fieldlist']//label[text()='Enter valid hostname or IP address.']"
    ADD_SAN_ERR_HOST_REQUIRED = "//*[@id='hp-form-message']/div[2][text()='One or more fields have an invalid value.']"
    ADD_SAN_ERR_PORT_DETAILS = "//*[@id='cic-sanmanagers-add-general-fieldlist']//label[text()='Enter a valid port number (1 - 65535)']"
    ADD_SAN_ERR_CREDENTIALS = "//*[@id='hp-form-message']/div[2][text()='The specified user name and/or password is not valid for the SAN manager.']"
    ADD_SAN_ERR_RESOLUTION = "/b[text() = 'Resolution: ']"

# Edit SAN manager errors
    EDIT_SAN_MANAGER_ERR_MSG = "//*[@id='hp-form-message']//span[text()='Unable to edit SAN manager.']"
    EDIT_SAN_MANAGER_ERR_CREDENTIALS = "//*[@id='hp-form-message']/div[2][text()='The specified user name and/or password is not valid for the SAN manager.']"
    EDIT_SAN_MANAGER_ERR_RESOLUTION = "/b[text() = 'Resolution: ']"
    EDIT_SAN_MANAGER_REQUIRED_ERR_MSG = "//*[@id='cic-sanmanagers-edit-credentials-fieldlist']/li[2]/div//label[text()='This field is required.']"
    ID_BTN_EDIT_SAN_MANAGER_OK = "id=cic-sanmanagers-edit-ok-button"
    ID_BTN_EDIT_SAN_MANAGER_CANCEL = "id=cic-sanmanagers-edit-cancel-button"
    ID_SAN_EDIT_BNA_PSWD = "id=cic-sanmanagers-edit-attribute3"
    ID_SAN_EDIT_BNA_USERNAME = "id=cic-sanmanagers-edit-attribute2"
    ID_SAN_EDIT_BNA_HOSTNAME = "id=cic-sanmanagers-edit-attribute0"
    ID_EDIT_HELP_LINK = "//*[@id='hp-change-page-container']/section/div/div/a/div"

# Selected specific sanmanager action menu
    ID_ACTIONS_ADD_SAN_MANAGER = "id=cic-sanmanagers-add-action"
    ID_ACTIONS_EDIT_SAN_MANAGER = "id=cic-sanmanagers-edit-action"
    ID_ACTIONS_REFRESH_SAN_MANAGER = "id=cic-sanmanagers-refresh-action"
    ID_ACTIONS_REMOVE_SAN_MANAGER = "id=cic-sanmanagers-remove-action"
    ID_MENU_VIEW_MAIN_BTN = "id=cic-sanmanagers-panel-selector"
    ID_VIEW_GENERAL_SAN_MANAGER = "xpath=.//*[@id='cic-sanmanagers-panel-selector']/ol/li[1]/a"
#    ID_VIEW_MANAGEDSANS_SAN_MANAGER = "xpath=.//*[@id='cic-sanmanagers-panel-selector']/ol/li[2]/a"
    ID_VIEW_ACTIVITY_SAN_MANAGER = "xpath=.//*[@id='cic-sanmanagers-panel-selector']/ol/li[2]/a"
    ID_VIEW_MAP_SAN_MANAGER = "xpath=.//*[@id='cic-sanmanagers-panel-selector']/ol/li[3]/a"

# Ids for Links to navigate to san page from san manager page
    ID_LINK_SANSCOUNT = "xpath=.//*[@id='cic-sanmanagers-managedsans-sans-count']/a"
    ID_MANAGEDSAN_LIST = "xpath=//*[@id='cic-sanmanagers-managed-sans-table']/tbody/tr/td/a"

# To Verify San Manager count from dashboard
    ID_SAN_MANAGERS_COUNT = "xpath=//*[@id='cic-sanmanagers-page']/nav/div[2]/span"
    ID_DASHBOARD_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Dashboard']"
    ID_DASHBOARD_SAN_MANAGERS_COUNT = "xpath=//*[@id='hp-dashboard-panels']/div[12]/div/header/h2/a/span[2]"

# Activity tab
    ID_ACTIVITY_LAST_EVENT = "//*[@id='DataTables_Table_4']/tbody/tr/td[3]/p/span"

# Auth
    ID_NO_AUTH = "xpath=//*[@id='cic-sanmanagers-actions']/div/ol[4]/li"

#  MAP tab
    ID_MAP_TOP_LEVEL = "//*[@id='cic-sanmanagers-details-show-view']/div/div/ol/li[1]/ol/li/div[2]"
    ID_MAP_SECOND_LEVEL = "//*[@id='cic-sanmanagers-details-show-view']/div/div/ol/li[2]/ol/li[2]/div[2]"
