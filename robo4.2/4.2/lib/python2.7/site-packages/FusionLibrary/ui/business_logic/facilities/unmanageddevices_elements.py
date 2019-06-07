# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion Unmanaged Device Page
'''


class FusionUnmanagedDevicePage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Unmanaged Devices']"
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ADD = "link=Add"
    ID_MENU_ACTION_EDIT = "link=Edit"
    ID_INPUT_NAME_UNMANAGED_DEVICE = "id=cic-unmanaged-name"
    ID_INPUT_MODEL = "id=cic-unmanaged-model"
    ID_COMBO_HEIGHT = "xpath=//label[text()='Height']/following-sibling::div/div/div"
    ID_COMBO_OPTION = "xpath=//label[text()='Height']/following-sibling::div/div/div//span[.='%s']"
    ID_INPUT_MAXIMUM_POWER = "id=cic-unmanaged-maximumPower"
    ID_BTN_ADD_PLUS_UNMANAGED_DEVICE = "id=cic-unmanaged-addplus"
    ID_BTN_ADD_UNMANAGED_DEVICE = "id=cic-unmanaged-add"
#     ID_BTN_ADD_PLUS_UNMANAGED_DEVICE = "id=cic-unmanaged-add-cancel"
    ID_BTN_CANCLE_PLUS_UNMANAGED_DEVICE = "id=cic-unmanaged-add-cancel"
    ID_ELEMENT_UNAMANGED_DEVICE_BASE = "xpath=//td[@class='' and text()='%s']"
    # VIEW
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_OVERVIEW = "id=cic-unmanaged-overview-selector"
    ID_LINK_GENERAL = "id=cic-unmanaged-general-selector"
    ID_LINK_ALERTS = "id=cic-unmanaged-alerts-selector"
    ID_LINK_RELATED = "link=Related"
    ID_BTN_UPDATE = "id=cic-unmanaged-update"
    ID_MENU_ACTION_REMOVE = "id=cic-unmanaged-delete-action"
    ID_BTN_REMOVE_UD_CONFIRM = "id=cic-confirm-ok"
    ID_UDS_LIST = "xpath=//div[@class='dataTables_scrollBody']/table"
    ID_UDS_LIST_NAMES = ID_UDS_LIST + '/tbody/tr/td[2]'
    ID_LINK_CREATE_UD = "link=Add unmanaged device"
    ID_UDS_UPDATE_SUCESS = "xpath=//header[@class='hp-notification-summary']/div[@class='hp-status hp-status-ok']/following-sibling::div/p/span[text()='Update']"
