# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion Data Center Page
'''


class FusionDataCenterPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Data Centers']"
    ID_MAIN_MENU = "xpath=//div[@id='hp-main-menu-labels']"
    ID_LINK_ADD_DATA_CENTER = "link=Add data center"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ADD = "link=Add"
    ID_MENU_ACTION_EDIT = "link=Edit"
    ID_MENU_ACTION_REMOVE = "link=Remove"
    ID_BTN_YES_REMOVE_CONFIRMATION = "id=cic-confirm-ok"
    ID_BTN_CLOSE_REMOVE_DIALOGUE = "css=button.hp-cancel"
    # Add Data Center
    ID_INPUT_DATACENTER_NAME = "id=cic-datacenter-name"
    ID_INPUT_WIDTH_DATACENTER = "id=cic-datacenter-width"
    ID_INPUT_DEPTH_DATACENTER = "id=cic-datacenter-depth"
    ID_COMBO_ELECTRICAL_DERATING = "//label[text()='Electrical derating']/following-sibling::div/div/div"
    ID_INPUT_DEFAULT_VOLTAGE = "id=cic-datacenter-defaultPowerLineVoltage"
    ID_INPUT_CURRENCY = "id=cic-datacenter-currency"
    ID_INPUT_POWER_COST = "id=cic-datacenter-costPerKilowattHour"
    ID_INPUT_COOLING_CAPACITY = "id=cic-datacenter-coolingCapacity"
    ID_INPUT_COOLING_MULTIPLIER = "id=cic-datacenter-coolingMultiplier"
    ID_INPUT_UNPOSITIONED_RACK = "css=input[type='text']"
    ID_BTN_ADD_UNPOSITIONED_RACK = "id=cic-addItemListPanel-add-button"
    ID_BTN_ADD_PLUS_DATACENTER = "id=cic-datacenter-addplus"
    ID_BTN_ADD_DATACENTER = "id=cic-datacenter-add"
    ID_BTN_CANCEL_PLUS_DATACENTER = "id=cic-datacenter-add-cancel"
    # View
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_OVERVIEW = "id=cic-datacenter-overview-selector"
    ID_LINK_GENERAL = "id=cic-datacenter-general-selector"
    ID_LINK_LAYOUT = "id=cic-datacenter-layout-selector"
    ID_LINK_ALERT = "id=cic-datacenter-alerts-selector"
    ID_LINK_RELATED = "link=Related"
    ID_SELECT_DATACENTER = "xpath =//td[@class='' and text()='%s']"
    ID_LIST_DATACENTERS = "id=DataTables_Table_0_wrapper"
    ID_DROP_DOWN = "xpath = //*[@id='cic-datacenter-panel-selector']"
    ID_GENERAL = "id=cic-datacenter-add-general"
    ID_LINK_LAYOUT_RACK = "link=Layout"
    ID_VALIDATE_DATACENTER = "xpath=//td[text()='%s']"     # %s will ask for name of datacenter
    ID_ADD_DATACENTER = "id=cic-datacenter-page"
    ID_UNPOSIOTIONED_RACK = "xpath=//*[@id='cic-datacenter-itemList-Column']"
    ID_SELECT_RACK = "xpath=//*[@id='cic-additemslist-items-table']/tbody/tr/td"
    ID_OVERVIEW_PAGE = "xpath=.//*[@id='cic-datacenter-panel-selector']/div"
    ID_MAP_PAGE = "xpath=.//*[@id='cic-datacenter-panel-selector']/ol/li[4]/a"
    ID_VAL_RACK_IN_DC = "xpath = //ol[@class='hp-bucket-items']/li/div[text()='%s']"
    ID_VAL_DC_IN_MAP = "xpath = .//*[@id='cic-datacenter-show']//li/div[text()='%s']"

    ID_Datacenter_LIST = "xpath = //*[@class='dataTables_scrollBody']//table"
    ID_Datacenter_LIST_NAMES = ID_Datacenter_LIST + '/tbody/tr/td[2]'
