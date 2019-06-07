#  (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion SANMangers page/screen
'''


class GeneralSANMangersElements(object):
    ID_TABLE_MASTER = "id=cic-network-master-table"
    ID_TABLE_SAN_MANAGERS = "xpath=//table/tbody//tr/td[2]"
    ID_TABLE_SAN_MANAGER = "xpath=//table/tbody//tr/td[text()='%s']"  # network_name
    ID_STATUS_SAN_MANAGER_OK = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-ok']"  # network_name
    ID_STATUS_SAN_MANAGER_WARN = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-warning']"  # network_name
    ID_STATUS_SAN_MANAGER_ERROR = "xpath=//table/tbody//tr/td[text()='%s']/../td/div[@class='hp-status hp-status-error']"  # network_name
    ID_TABLE_SAN_MANAGER_SELECTED = "//table/tbody//tr[contains(@class, 'hp-selected')]/td[text()='%s']"  # network_name
    ID_TABLE_SAN_MANAGER_REMOVED = "//table/tbody//tr[contains(@class, 'hp-not-found')]/td[text()='%s']"  # network_name
    ID_DROPDOWN_ACTIONS = "xpath=//label[text()='Actions']"
    ID_TEXT_SAN_MANAGER_STATUS_TITLE = "id=cic-sanmanagers-details-title"
    ID_TEXT_SAN_MANAGER_STATUS = "id=cic-sanmanagers-details-status"
    ID_DROPDOWN_PANEL_SELECTOR = "//*[@id='cic-sanmanagers-panel-selector']/div"
    ID_SELECT_GENERAL_PANEL = "//*[@id='cic-sanmanagers-panel-selector']/ol/li/a[text()='General']"
    ID_SELECT_ACTIVITY_PANEL = "//*[@id='cic-sanmanagers-panel-selector']/ol/li/a[text()='Activity']"
    ID_SELECT_MAP_PANEL = "//*[@id='cic-sanmanagers-panel-selector']/ol/li/a[text()='Map']"
    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-sanmanagers-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_TEXT_ACTIVITY_ACTION_TITLE = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-activity-message']/p/span"  # network_name
    ID_TEXT_ACTIVITY_ACTION_OK = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # network_name
    ID_TEXT_ACTIVITY_ACTION_WARN = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # network_name
    ID_TEXT_ACTIVITY_ACTION_ERROR = "//ol[@id='hp-flyout-activities']/li[1]/div/div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # network_name
    ID_TEXT_ACTIVITY_ACTION_DETAILS_OK = "//header[@class='hp-active']/a[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # network_name
    ID_TEXT_ACTIVITY_SPECIFACTION_OK = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-ok']"  # actionname, network_name
    ID_TEXT_ACTIVITY_SPECIFACTION_WARN = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-warning']"  # actionname, network_name
    ID_TEXT_ACTIVITY_SPECIFACTION_ERROR = "//ol[@id='hp-flyout-activities']/li/div/div[@class='hp-activity-message']/p/span[text()='%s']/../../../div[@class='hp-activity-source' and text()='%s']/../div[@class='hp-status hp-status-error']"  # actionname, network_name
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    ID_TEXT_GENERAL_SAN_MANAGER_TYPE = "id=cic-sanmanagers-general-type"
    ID_TEXT_GENERAL_STATE = "id=cic-sanmanagers-general-state"
    ID_TEXT_GENERAL_VERSION = "id=cic-sanmanagers-general-version"
    ID_TEXT_GENERAL_PORT = "id=cic-sanmanagers-dynamic-attribute-0"
    ID_TEXT_GENERAL_USER_NAME = "id=cic-sanmanagers-dynamic-attribute-1"
    ID_TEXT_GENERAL_USE_SSL = "id=cic-sanmanagers-dynamic-attribute-2"
    ID_TEXT_GENERAL_USED_BY = "xpath=//*[@id='cic-sanmanagers-managedsans-sans-count']/a"


class AddSANMangersElements(object):
    ID_BUTTON_ADD_SAN_MANAGER = "link=Add SAN manager"
    ID_SELECT_ACTION_ADD = "id=cic-sanmanagers-add-action"
    ID_DIALOG_ADD_SAN_MANAGER = "id=cic-sanmanagers-add-form"
    ID_SELECT_SAN_MANAGER_TYPE = "id=cic-sanmanagers-add-type-select"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME = "xpath=//label[text()='IP address or host name']/../div/input[@id='cic-sanmanagers-add-attribute0']"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME2 = "xpath=//label[text()='IP address or host name']/../div/input[@id='cic-sanmanagers-add-attribute4']"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME_CISCO = "xpath=//label[text()='IP address or host name']/../div/input[@id='cic-sanmanagers-add-attribute12']"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME_HPE = "xpath=//label[text()='IP address or host name']/../div/input[@id='cic-sanmanagers-add-attribute5']"

    ID_INPUT_PORT = "xpath=//label[text()='Port']/../div/input"
    ID_CHECKBOX_USE_SSL = "xpath=//label[text()='Use SSL']/../input"
    ID_CHECKBOX_USE_SSL2 = "xpath=//label[text()='Use secure connection (HTTPS)']/../input"

    ID_INPUT_USER_NAME = "xpath=//*[@id='cic-sanmanagers-panel-add-credentials']//label[text()='User name']/../div/input[@id='cic-sanmanagers-add-attribute2']"
    ID_INPUT_USER_NAME2 = "xpath=//*[@id='cic-sanmanagers-panel-add-credentials']//label[text()='User name']/../div/input[@id='cic-sanmanagers-add-attribute6']"
    ID_INPUT_PASSWORD = "xpath=//*[@id='cic-sanmanagers-add-credentials-fieldlist']/li[2]/label[text()='Password']/../div/input"
    ID_INPUT_PASSWORD2 = "xpath=//*[@id='cic-sanmanagers-add-credentials-fieldlist']/li[4]/label[text()='Password']/../div/input"

    ID_INPUT_SNMP_USER_NAME = "xpath=//*[@id='cic-sanmanagers-panel-snmp']//label[text()='User name']/../div/input[@class='required']"
    ID_INPUT_SNMP_PORT = "xpath=//label[text()='SNMP port']/../div/input"
    ID_RADIO_SECURITY_LEVEL_NONE = "xpath=//label[text()='None']"
    ID_RADIO_SECURITY_LEVEL_AUTHENTICATION = "xpath=//label[text()='Authentication']"
    ID_RADIO_SECURITY_LEVEL_AUTHENTICATION_AND_PRIVACY = "xpath=//label[text()='Authentication and privacy']"
    ID_DROPDOWN_AUTHENTICATION_PROTOCOL = "xpath=//*[@id='cic-sanmanagers-add-snmp-fieldlist']/li[4]/div/div/div/div"
    ID_SELECT_AUTHENTICATION_PROTOCOL_SHA = "xpath=//label[text()='Authentication protocol']/../div/div[@class='hp-select-form']/div/ol/li/span[text()='SHA']"
    ID_SELECT_AUTHENTICATION_PROTOCOL_MD5 = "xpath=//label[text()='Authentication protocol']/../div/div[@class='hp-select-form']/div/ol/li/span[text()='MD5']"
    ID_INPUT_AUTHENTICATION_PASSWORD = "xpath=//*[@id='cic-sanmanagers-panel-snmp']//label[text()='Authentication password']/../div/input[@class='required']"
    ID_DROPDOWN_PRIVACY_PROTOCOL = "xpath=//label[text()='Privacy protocol']/../div/div"
    ID_SELECT_PRIVACY_PROTOCOL_DES56 = "xpath=//label[text()='Privacy protocol']/../div/div[@class='hp-select-form']/div/ol/li/span[text()='DES-56']"
    ID_SELECT_PRIVACY_PROTOCOL_AES128 = "xpath=//label[text()='Privacy protocol']/../div/div[@class='hp-select-form']/div/ol/li/span[text()='AES-128']"
    ID_INPUT_PRIVACY_PASSWORD = "xpath=//label[text()='Privacy password']/../div/input"
    ID_TEXT_ADDED_SAN_MANAGER = "xpath=//*[@id='hp-form-message']/div/span[contains(text(), 'Added SAN manager')]/../div[@class='hp-status hp-status-ok']"
    ID_BUTTON_ADD = "id=cic-sanmanagers-add-add-button"
    ID_BUTTON_ADD_PLUS = "id=cic-sanmanagers-add-add-again-button"
    ID_BUTTON_CANCEL = "id=cic-sanmanagers-add-cancel-button"


class EditSANMangersElements(object):
    ID_SELECT_ACTION_EDIT = "id=cic-sanmanagers-edit-action"
    ID_DIALOG_EDIT_SAN_MANAGER = "id=cic-sanmanagers-edit-form"
    ID_INPUT_IP_ADDRESS_OR_HOST_NAME = "xpath=//label[text()='IP address or host name']/../div/input[@class='hostAddress']"
    ID_INPUT_PORT = "xpath=//label[text()='Port']/../div/input"
    ID_CHECKBOX_USE_SSL = "xpath=//label[text()='Use SSL']/../input"
    ID_INPUT_USER_NAME = "xpath=//label[text()='User name']/../div/input"
    ID_INPUT_PASSWORD = "xpath=//label[text()='Password']/../div/input"
    ID_BUTTON_OK = "id=cic-sanmanagers-edit-ok-button"
    ID_BUTTON_CANCEL = "id=cic-sanmanagers-edit-cancel-button"


class RemoveSANMangersElements(object):
    ID_SELECT_ACTION_REMOVE = "id=cic-sanmanagers-remove-action"
    ID_DIALOG_REMOVE = "id=cic-sanmanagers-remove-title-details"
    ID_BUTTON_YES_REMOVE = "xpath=//button[text()='Yes, remove']"
    ID_BUTTON_CANCEL = "xpath=//button[text()='Cancel']"


class RefreshSANMangersElements(object):
    ID_SELECT_ACTION_REFRESH = "id=cic-sanmanagers-refresh-action"
