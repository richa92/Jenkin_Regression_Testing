# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on Fusion Firmware Bundle  Page
'''


class FusionFirmwareBundlePage(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Firmware Bundles']"
    ID_LINKE_ADD_FW_BUNDLE = "link=Add Firmware Bundle"
    ID_BTN_CHOOSE_FILE = "xpath=//*[@id='hp-file-chooser-file']"
    ID_BTN_CLOSE_FILE_DIALOGUE = "link=Close"
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ITEM_ADD = "id=cic-fwdriver-add-action"
    ID_MENU_ACTION_ITEM_DELETE = "xpath=//*[@id='cic-fwdriver-delete-action']"
    ID_BTN_CLOSE_DELETE_DIALOGUE = "css=button.hp-cancel"
    ID_BTN_START_UPLOAD = "xpath=//input[@class='hp-button hp-upload-send' and @value='Start upload']"
    ID_BTN_DELETE_BUNDLE_CONFIRM = "xpath=//*[@id='hp-body-div']//div/button[text()='Remove bundle']"
    ID_ELEMENT_UPLOAD_PROGRESS = "css=label.hp-upload-progress-message"
    ID_BIN_OK = "xpath=//*[@id='cic-fwdriver-add-ok']"
    ID_ICON_ACTIVITY_COLLAPSER = "//table[@class='hp-index-table hp-activities dataTable']/tbody/tr//span[text()='%s']/../../../td//div[@class='hp-collapser']"  # activity collapser
    ID_TEXT_ACTIVITY_CONTENT = "//table[@class='hp-index-table hp-activities dataTable']/tbody/tr//li[contains(text(), '%s')]"
    ID_TEXT_FIRMWARE_COMPONENT = "//div[@id='cic-fwdriver-contents']/table//tr[td[contains(text(), '%s')]]/td[contains(text(), '%s')]"

    # Add Firmware Validation
    ID_ELEMENT_FORM_MESSAGE = "xpath=//*[@id='hp-form-message']/div[1]/span"
    ID_NEW_ACTIVITY_PROGRESS = "xpath= //tr/td[@class='hp-icon' and div[@class='hp-status hp-status-changing']]/following-sibling::td[@class='hp-name' and p/span[contains(text(),'Add')]]/following-sibling::td/a[text()='%s']"  # %s replaces spp name
    ID_NEW_ACTIVITY_TIMESTAMP = "xpath= //td[div[@class='hp-status hp-status-changing']]/following-sibling::td[p/span[contains(text(),'Add')]]/following-sibling::td[a[text()='%s']] /following-sibling::td[@date-timestamp]"  # %s replaces with spp name
    ID_NEW_ACTIVITY_SUCCESS = "xpath=  //td[div[@class='hp-status hp-status-ok']]/following-sibling::td[p/span[contains(text(),'Add')]]/following-sibling::td[span[text()='Firmware Bundles']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_NEW_ACTIVITY_ERROR = "xpath=  //td[div[@class='hp-status hp-status-error']]/following-sibling::td[p/span[contains(text(),'Add')]]/following-sibling::td[span[text()='Firmware Bundles']] /following-sibling::td[@date-timestamp and contains(text(),'%s')]"  # %s replace with enclosure namd and time stamp
    ID_MAIN_PAGE = "id= hp-main-menu-control"

    # New Objects
    ID_FIRMWARE_BUNDLE = "xpath=.//div/div/ol/li[header/div[text()='%s'] and div/ol/li[contains(text(),'%s')]]"
    ID_TABLE_FIRMWARE_BUNDLE = "//table[@class='hp-master-table hp-selectable dataTable']//tr/td[text()='%s']/following-sibling::td[text()='%s']"
    ID_FWDRIVER_TITLE = "xpath=//*[@id='cic-fwdriver-title']"
    ID_UPLOAD_STATUS = "xpath=//div[@id='fwdrivers-fileupload']//div[@class='hp-upload-progress-meter hp-progress']"
    # Objects for Activity Page
    ID_SELECTOR_FW_ACTIVITY = "xpath=//table[@id='hp-activities']/tbody/tr/td[following-sibling::td/a[text()='%s'] and following-sibling::td/p[contains(.,'Add')]]/div[@class='hp-collapser']"
    ID_ACTIVITY_FW_SUMMARY = "xpath=//table[@id='hp-activities']/tbody/tr[td[following-sibling::td/span[text()='Firmware Bundles']]]/following-sibling::tr//p[contains(.,'%s')]"


class RemoveFirmwareBundleElements(object):
    ID_BUTTON_REMOVE_BUNDLE = "//div[@id='hp-body-div']//div/button[text()='Remove bundle']"
    ID_BUTTON_YES_REMOVE = "//div[@id='hp-body-div']//div/button[text()='Yes, remove']"
    ID_BUTTON_CANCEL = "//div[@id='hp-body-div']//div/button[text()='Cancel']"
    ID_DIALOG_REMOVE = "//div[@id='cic-fwdrivers-remove-dialog']"
    ID_TITLE_FIRMWARE_BUNDLE = "xpath=.//div/div/ol/li[header/div[text()='%s'] and div/ol/li[contains(text(),'%s')]]"
    ID_PANEL_REMOVE_ERROR = "//div[@id='hp-page-notifications']//div[text()='Error']"
    ID_TEXT_REMOVE_ERROR = "//div[@id='hp-page-notifications']//span[contains(text(),'This Service Pack for ProLiant (SPP) is being used for firmware installation and/or BIOS/Local storage provisioning')]"


class AddFirmwareBundleElements(object):
    ID_BUTTON_REMOVE_BUNDLE = "//div[@id='hp-body-div']//div/button[text()='Remove bundle']"
    ID_BUTTON_OK = "//a[@id='cic-fwdriver-add-ok']"
    ID_BUTTON_SELECT_FILE = "//input[@id='hp-file-chooser-file']"
    ID_BUTTON_CLOSE = "//a[text()='Close']"
    ID_BUTTON_CANCEL = "//a[text()='Cancel']"
    ID_DIALOG_ADD = "//form[@id='cic-fwdriver-add-form']"
    ID_TEXT_FORM_MESSAGE = "//div[@id='hp-form-message']/div[@class='hp-form-message-summary']/span"
    ID_TITLE_FIRMWARE_BUNDLE = "xpath=.//div/div/ol/li[header/div[text()='%s'] and div/ol/li[contains(text(),'%s')]]"
    ID_PANEL_REMOVE_ERROR = "//div[@id='hp-page-notifications']//div[text()='Error']"
    ID_TEXT_REMOVE_ERROR = "//div[@id='hp-page-notifications']//span[contains(text(),'This Service Pack for ProLiant (SPP) is being used for firmware installation and/or BIOS/Local storage provisioning')]"
