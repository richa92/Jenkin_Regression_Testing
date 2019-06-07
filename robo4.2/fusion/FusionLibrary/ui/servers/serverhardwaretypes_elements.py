# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion server hardware page/screen
'''


class FusionServerHardwareTypePage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Server Hardware Types']"
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_EDIT = "id=cic-servertypes-launchedit-action"
    ID_INPUT_SERVER_TYPE_NAME = "id=cic-servertypes-name"
    ID_INPUT_SERVER_TYPE_DESCRIPTION = "id=cic-servertypes-description"
    ID_MENU_ACTION_DELETE = "id=cic-servertypes-launchdelete-action"
    # VIEW
    ID_COMBO_MENU_VIEW_ = "css=div.hp-value"
    ID_LINK_OVERVIEW = "id=cic-servertypes-overview-selector"
    ID_LINK_RELATED = "link=Related"
    # Server Hardware Type Select
    ID_HARDWARE_LIST = "xpath=//*[@id='cic-servertypes-page']//ol[@class='hp-master-grid hp-active']"
    ID_HARDWARE_LIST_NAME = "xpath=//*[@id='cic-servertypes-page']//header/div[contains(text(),'%s')]"
    ID_HARDWARE_LIST_STATUS_OK = "xpath=//*[@id='cic-servertypes-details-status' and @class='hp-status hp-status-ok']"
    ID_HARDWARE_LIST_STATUS_ERROR = "xpath=//*[@id='cic-servertypes-details-status' and @class='hp-status hp-status-error']"
    ID_NO_SERVER_HARDWARE_TYPES = "//*[@id='cic-servertypes-page']/div/div[2]/div[contains(text(),'No server hardware types')]"
    # Server Hardware Type Edit
    ID_HARDWARE_BASE = "xpath=//header/div[@class='hp-master-item-name']"
    ID_INPUT_HARDWARE_TYPE_NAME = "xpath=//input[@id='cic-servertypes-name']"
    ID_INPUT_HARDWARE_TYPE_DESCRIPTION = "xpath=//textarea[@id='cic-servertypes-description']"
    ID_BTN_CONFIRM_EDIT = "xpath=//input[@id='cic-servertypes-edit-ok']"
    ID_BTN_CANCEL_EDIT = "xpath=//input[@id='cic-servertypes-edit-cancel']"
    ID_HARDWARE_DESCRIPTION = "xpath=//div[text()='%s']"
    ID_EDIT_HARDWARE_ERROR = "xpath=//div[@id='hp-form-message']"
    IE_EDIT_PAGE_CONTAINER = "id=hp-change-page-container"
    # Server Hardware Type Delete
    ID_DELETE_HARDWARE_TYPE_DIALOG = "xpath=//div[@id='cic-servertypes-delete-dialog']"
    ID_DELETE_ERROR_MSG = "xpath=//span[@id='cic-servertypes-delete-attention-warning-msg']"
    ID_DELETE_OK = "xpath=//button[@class='hp-ok hp-primary']"
    ID_DELETE_CLOSE = "xpath=//button[@class='hp-cancel hp-primary']"

    ID_ADAPTER_INFO = "xpath=//span[text()='%s']"
    ID_USEDBY_INFO = "xpath=//div[@id='cic-servertype-usedby' and text()='%s']"
    ID_USEDBY_LINK = "xpath=//div[@id='cic-servertype-usedby']/ol/li[1]/a"
    ID_SERVER_LOCATION_LINK = "xpath=//div[@id='cic-server-location']/a[2]"
    ID_SERVER_LOCATION = "xpath=//div[@id='cic-server-location']"
    ID_ENCLOSURE_SELECTOR = "xpath=//div[@id='cic-enclosure-panel-selector']"
    ID_ENCLOSURE_IP = "xpath=//td[@id='cic-enclosure-more-oa-active-ipv4']/a"
    ID_MODEL_TEXT = "xpath=//div[@id='cic-servertype-model']"
    ID_FORMFACTOR_TEXT = "xpath=//div[@id='cic-servertype-form-factor']"
    ID_ADAPTER_INFO_TABLE_ROW = "xpath=//*[@id='cic-servertypes-adapters-table']/tbody/tr"
    ID_ADAPTER_INFO_TABLE_SPECIFIC_ROW = "xpath=//table[@id='cic-servertypes-adapters-table']/tbody/tr[%s]/td"
    ID_ADAPTER_INFO_TABLE_SPECIFIC_CELL = "xpath=//table[@id='cic-servertypes-adapters-table']/tbody/tr[%s]/td[%s]"

    ID_HARDWARE_TYPE_NAME_HEADER = "xpath=//ol[@class='hp-master-grid hp-active']/li"
    ID_HARDWARE_TYPE_NAME_HEADER_VALUE = "xpath=//ol[@class='hp-master-grid hp-active']/li[%s]/header/div"
