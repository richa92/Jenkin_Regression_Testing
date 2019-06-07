# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion Racks Page
'''


class FusionRacksPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Racks']"
    ID_LINK_ADD_RACK = "link=Add rack"
    ID_LINK_ADD_RACK = "//div[@class='hp-master-add']"
    ID_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ADD = "id=cic-rack-add-action"
    ID_MENU_ACTION_EDIT = "id=cic-rack-edit-action"
    ID_MENU_ACTION_REMOVE = "id=cic-rack-delete-action"
    ID_BTN_ADD_PLUS_RACK = "id=cic-rack-addplus"
    ID_BTN_ADD_RACK = "id=cic-rack-add"
    ID_BTN_CANCEL_RACK = "id=cic-rack-cancel"
    ID_ELEMENT_RACK_NAME_BASE = "xpath=//td[@class='' and text()='%s']"  # replace %s with Rack Name
    # ADD RACK
    ID_INPUT_RACK_NAME = "id=cic-rack-details-name"
    ID_INPUT_THRMAL_LIMIT = "id=cic-rack-details-thermalLimit"
    ID_INPUT_SERIEL_NUMBER = "id=cic-rack-details-serialNumber"
    ID_INPUT_SLOT_HEIGHT = "id=cic-rack-details-uHeight"
    ID_INPUT_RACK_HEIGHT = "id=cic-rack-details-height"
    ID_INPUT_RACK_WIDTH = "id=cic-rack-details-width"
    ID_INPUT_RACK_DEPTH = "id=cic-rack-details-depth"
    ID_INPUT_DEVICE = "css=input[type='text']"
    # Remove
    ID_BTN_YES_RMOVE_CONFIRMATION = "id=cic-confirm-ok"
    ID_BTN_CANCEL_REMOVE_DIALOGUE = "css=button.hp-cancel"
    # View
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_OVERVIEW = "id=cic-rack-overview-selector"
    ID_LINK_GENERAL = "id=cic-rack-general-selector"
    ID_LINK_LAYOUT = "id=cic-rack-layout-selector"
    ID_LINK_ALERT = "id=cic-rack-alerts-selector"
    ID_LINK_RELATED = "link=Related"
    # New Objects Added to edit rack
    ID_ELEMENT_RACK_NAME = "xpath= .//td[text()='%s']"  # %s replaces with rack name
    ID_ELEMENT_RACK_HEADER = "xpath=//h1[text()='%s']"  # %s replace with rack name
    ID_EDIT_RACK_UPDATE = "id=cic-rack-update"
    ID_DROP_DOWN = "css=#cic-rack-edit-panel-selector > div.hp-value"
    ID_LINK_LAYOUT_RACK = "link=Layout"
    ID_SEARCH_TEXT_FIELD = ".//*[@id='cic-additemslist-items-table_filter']/label/input"
    ID_SELECT_PDU = "css=div.hp-device.hp-rack-1u > div.hp-device-name"
    ID_CLICK_ADD = "id=cic-addItemListPanel-add-button"
    ID_ClICK_DROP_DOWN_ALIGNMENT = "xpath = .//li[1]/div/a/span[2]"
    ID_SELECT_ALIGNMENT = "xpath= .//ul/li/a[text()='%s']"  # %s replace with position
    ID_CLICK_DROP_DOWN_ROW = "xpath = .//li[2]/div/a/span[2]"
    ID_SELECT_POSITION_ELEMENT = "xpath= .//ol/li[2]/div/a"
    ID_ADD_RACK_OK = "xpath=(//input[@value='OK'])[2]"
    ID_VALIDATE_PDU = "xpath =.//div[@class='hp-device-name']/a[contains(text(),'%s')]"  # %s will be replace with PDU IP
    ID_VALIDATE_SEARCH_PDU = "xpath =.//div[@class='hp-device-name' and contains(text(),'%s')]"  # %s will be replaced with PDU IP or enclosure name
    ID_REMOVE_PDU = "xpath =.//div[@class='hp-device-name']/a[contains(text(),'%s')]/following::div[@class='hp-close']"  # %s replaces with PDU IP
    ID_EDIT_PDU = "xpath =.//div[@class='hp-device-name']/a[contains(text(),'%s')]/following::div[@class='hp-edit']"  # %s replaces with PDU IP
    ID_EDIT_PDU_VALIDATE = "xpath = .//*[@id='hp-form-message']/div/span[contains(text(),'Moved: %s')]"  # %s will replace with PDU IP
    ID_EDIT_OK_PDU = "xpath =.//*[@id='editDevice-form-dialog']/form/footer/div/input"
    ID_SELECT_HARDWARE = "xpath =.//td/div[@class='hp-device hp-rack-10u']"  # %s replaces with hardware name
    ID_POWERCONNECTION_SELECT_ENCLOSURE = "xpath= .//*[@id='cic-rack-powerConnection-%s']/option[text()='%s']"  # %s replaces with power connections %s will be reaplced with number
    ID_BEST_PRACTISE_CONNECTIONS = "id=cic-rack-bestPractice"
    ID_VALIDATE_POWER_CONNECTIONS = "xpath= .//*[@id='cic-rack-powerConnections-none' and contains(text(),'There are no valid power connection points')]"
    ID_VALIDATE_HARDWARE = "xpath = .//div/div[@class='hp-device-name']/a[contains(text(),'%s')]"  # %s replaces with Hardware name
# ID_VALIDATE_HARDWARE = "xpath = .//*[@id='hp-form-message']/div/span[contains(text(),'Added: %s')]"  # %s replaces with Hardware name
    ID_SELECT_SERVER = "xpath = .//td/div[@class='hp-device hp-rack-1u']"
    ID_POWERCONNECTION_SELECT_SERVER = "xpath= .//*[@id='cic-rack-powerConnection-server-%s']/option[text()='%s']"  # %s replaces with name of the server and server hardware
    ID_VALIDATE_SEARCH_HARDWARE = "xpath= .//div[@class='hp-device-name' and text()='%s']"
    ID_DELETE_SERVER = "xpath= .//div[@class='hp-device-name']/a[text()='%s']"
    ID_DELETE_SERVER_CONFIRM = "xpath= .//div[@class='hp-device-name']/a[text()='%s']/following::div[@class='hp-close']"
    ID_EDIT_SERVER_ENCLOSURE = "xpath= .//div[@class='hp-device-name']/a[text()='%s']/following::div[@class='hp-edit']"
    ID_UPDATE_VALIDATE = "xpath= .//*[@id='hp-activity-notification']/div[@class='hp-active hp-status hp-status-ok']/following::div[contains(text(),'Update')]"
    ID_UPDATE_RACK = "id=cic-rack-update"
    ID_DELETE_RACK_CONFIRM = "id=cic-confirm-ok"
    ID_REMOVE_VALIDATE = "xpath= .//*[@id='hp-activity-notification']/div[@class='hp-active hp-status hp-status-ok']/following::div[contains(text(),'Remove %s')]"  # %s replace with rack name
    ID_ADD_RACK = "xpath= .//div/div/header/h1/div/a[text()='Add rack']"
    ID_ADD_VALIDATE = "xpath= .//*[@id='hp-activity-notification']/div[@class='hp-active hp-status hp-status-ok']/following::div[contains(text(),'Add %s')]"
    ID_DELETE_RACK_CONFIRM = "id=cic-confirm-ok"

    ID_RACK_LIST_TABLE = "xpath=//div[@class='dataTables_scrollBody']/table"
    ID_RACK_ITEM_IN_CONTAINER = "xpath=//div[@id='cic-rack-container']//div[contains(@class, 'hp-device')]//div[@class='hp-device-name'][contains(@title, '%s')]"
    ID_DROPDOWN_RACKSLOT = "xpath=//select[@id='cic-rack-uSlot-select']/../a"
    ID_RACK_ROW = "link=%s"
    ID_ADD_EDIT_SERVER_TO_RACK_CONFIRM = "css=input.hp-ok"
    ID_SERVER_NAME_IN_RACK = "xpath=//div[@id='cic-rack-container']//div[contains(@class, 'hp-device')]//div[@class='hp-device-name'][contains(@title, '%s')]/../..@title"

    ID_ADD_RACK_ITEM_IN_CONTAINER = "xpath=//table[@id='cic-additemslist-items-table']//div[contains(@class, 'hp-device')]//div[@class='hp-device-name'][contains(@title, '%s')]"
    ID_RACK_PDU_ITEM_IN_CONTAINER = "xpath=//div[contains(@class, 'hp-power-device')]//div[@class='hp-device-name'][contains(@title, '%s')]"

    ID_RACK_MOUNT_POS = "xpath=//select[@id='cic-rack-mountLocation-select']/../a"
    ID_ATTR_ID_PDU = "xpath=//div[contains(@class, 'hp-power-device')]//div[@class='hp-device-name'][contains(@title, '%s')]/../..@id"
    ID_ATTR_TITLE_PDU = "xpath=//div[contains(@class, 'hp-power-device')]//div[@class='hp-device-name'][contains(@title, '%s')]/../..@title"

    ID_PUD_IN_RACK = "xpath=//table[@id='cic-additemslist-items-table']//div[@class='hp-device-name'][contains(@title, '%s')]"

    # Applied Solutions
    ID_LABEL_RACK_MODEL = "xpath=//*[@id='cic-rack-details-model']"
    ID_LABEL_RACK_U_HEIGHT = "xpath=//*[@id='cic-rack-details-uHeight']"
    ID_LABEL_ENCL_U_HEIGHT = "xpath=//div[@id='cic-rack-container']/descendant::div[a[text()='%s']]/following-sibling::div[@class='hp-rack-uslot-top']"
    ID_LINK_PANEL_SELECTOR = "id=cic-rack-panel-selector"
    ID_LINK_ENCLOSURE_RACK = "xpath=//a[text()='%s']"
