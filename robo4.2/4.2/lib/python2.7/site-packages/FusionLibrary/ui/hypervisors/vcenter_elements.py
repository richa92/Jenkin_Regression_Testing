# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion V center page/screen
'''


class FusionvCenterPage(object):
    ID_PAGE_LABEL = "xpath = //div[@class='hp-page-label']/h1[text()='vCenters']"
    ID_MENU_LINK_VCENTERS = "link=vCenters"
    ID_VCENTER_LIST = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td"
    ID_VCENTER_LIST_NAMES = "xpath=//div[@class='dataTables_scrollBody']/table/tbody/tr/td[2]"
    ID_LINK_VCENTER_NAME = "xpath =//div[@class='dataTables_scrollBody']//table/tbody/tr/td[text()='%s']"
    ID_INPUT_VCENTER_IP_ADDRESS = "id=cic-vcenter-hostname"
    ID_INPUT_USERNAME = "id = cic-vcenter-username"
    ID_INPUT_PASSWORD = "id = cic-vcenter-password"
    ID_BTN_VCENTER_ADD = "id = cic-vcenter-add"
    ID_BTN_VCENTER_ADD_PLUS = "id = cic-vcenter-addplus"
    ID_ADD_VCENTER_NOTIFICATION = "xpath = //div[@id='hp-form-message']/div/div[@class='hp-status hp-status-error']/span[text()='error']"
    ID_BTN_ENCLOSURE_CANCEL = "id=cic-vcenter-add-cancel"
    ID_VCENTER_BUTTON = "xpath =//a[contains(.,'Add vCenter')]"
    ID_BTN_VCENTER_CANCEL = "id = cic-vcenter-add-cancel"
    ID_ADD_VCENTER_ERR_MSG = "xpath = //*[@id='hp-form-message']/div[1]/span[contains(text(),'Unable to add')]"
    ID_ADD_VCENTER_ERR_DETAILS = "xpath = .//*[@id='hp-form-message']/div[@class='hp-form-message-details']"
    ID_ELEMENT_VCENTER = "xpath=//td[text()='%s']"
    ID_MENU_ACTION_MAIN_BTN = "xpath = //label[text()='Actions']"
    ID_CHECK_ACTIVITY = " xpath =//header/h1[text()='Activity']"
    ID_ACTIVITY_VCENTER = "xpath =//div[@id='cic-vcenters-page']/nav/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_ELEMENT_ACTIVITY = "xpath = //ol[@id='hp-flyout-activities']/li/div/div[text()='%s']"  # Replace with vcenter name
    ID_CHECK_ADD_STATUS = "xpath= //span[text()='Add']"
    ID_ACTIVITY_ADD_STATUS_OK = "xpath =//ol[@id='hp-flyout-activities']//p/span[text()='Add']/ancestor::div/following-sibling::div[text()='%s']/preceding-sibling::div[@class='hp-status hp-status-ok']"
    ID_ACTIVITY_STATUS_WARNING = "xpath = //ol[@id='hp-flyout-activities']/li/div/div/span[text()='warning']"

    # Edit vCenter server properties
    ID_MENU_ACTION_EDIT = "link=Edit"
    ID_ELEMENT_EDIT_LABEL = "xpath = //span[@id='cic-vcenter-edit-title' and contains(.,'%s')]"
    ID_VSWITCH_VMOTION_TOGGLE = "xpath = //a[@id='cic-vcenter-enableVMotion-hpToggle']"
    ID_ELEMENT_VSWITCH_VMOTION = "xpath = //*[@id='cic-vcenter-enableVMotion-hpToggle']//li[text()='Disabled']"
    ID_ELEMENT_VSWITCH_TYPE = "xpath =//li[label[@for='cic-vcenter-switchType']]//label/following-sibling::div[@class='hp-value']"
    ID_RESOURCE_SCHEDULER_TOGGLE = "xpath = //a[@id='cic-vcenter-DRS-hpToggle']"
    ID_ELEMENT_RESOURCE_SCHEDULER = "xpath = //a[@id='cic-vcenter-HA-hpToggle']//li[text()='Enabled']"
    ID_ELEMENT_HA_TOGGLE = "xpath = //a[@id='cic-vcenter-HA-hpToggle']"
    ID_ELEMENT_HA = "xpath = //a[@id='cic-vcenter-HA-hpToggle']//li[text()='Disabled']"
    ID_ELEMENT_SELECT_VSWITCH_TYPE = "xpath = //span[text()='%s']"
    ID_ELEMENT_VSWITCH_VERSION = "xpath = //label[@for='cic-vcenter-distributedSwitchVersion']/following-sibling::div//label/following-sibling::div"
    ID_ELEMENT_SELECT_VSWITCH_VERSION = "xpath = //span[text()='%s']"
    ID_ELEMENT_VSWITCH_NETWORK = "xpath = //label[@for='cic-vcenter-distributeSwitchesFor']/following-sibling::div//label/following-sibling::div"
    ID_ELEMENT_SELECT_VSWITCH_NETWORK = "xpath = //span[text()='%s']"
    ID_ELEMENT_OK_BUTTON = "id = cic-vcenter-update"
    ID_ACTIVITY_UPDATE_STATUS_OK = "xpath = //ol[@id='hp-flyout-activities']//p/span[text()='Update']/ancestor::div/following-sibling::div[text()='%s']/preceding-sibling::div[@class='hp-status hp-status-ok']"

    # Delete vCenter
    ID_MENU_ACTION_REMOVE = "link=Remove"
    ID_BTN_DELETE_VCENTER_CONFIRM = "xpath = //button[contains(.,'Yes, Remove')]"
    ID_BTN_VCENTER_REMOVE_NOT_EXIST = "xpath=//*[@id='hp-not-exist']/div[2]"
    ID_DELETE_VCENTER_ERROR = "ERROR-//div[@class='hp-notify']/span"
    ID_RESET_FILTER = "link=Reset"
    ID_ELEMENT_LIST = "xpath = //table[@id='cic-vcenter-master-table']/tbody/tr/td[text()='%s']"
