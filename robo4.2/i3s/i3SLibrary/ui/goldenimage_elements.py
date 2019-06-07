# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''
This file contains all element ID on goldenimages page/screen
'''


class i3sgoldenimagePage(object):
    
    ID_PAGE_LABEL = "xpath=//*[@id='goldenimages-page']"
    ID_ADD_GI = "xpath=//*[@id='goldenimages-page']/div/div[1]/header/h1/div[1]/a"
    ID_ADD_GI_PAGE = "xpath=//*[@id='hp-change-page-container']/section/header/h1"
    ID_INPUT_NAME = "xpath=//*[@id='goldenimages-add-name']"
    ID_INPUT_DESCRIPTION = "xpath=//*[@id='goldenimages-add-desc']"
    ID_INPUT_URL = "xpath=//*[@id='i3s-goldenimages-url-id']"
    ID_ADD_GI_BUTTON = "xpath=//*[@id='goldenimages-add']"
    ID_ADDPLUS_GI_BUTTON = "xpath=//*[@id='goldenimages-addplus']"
    ID_CANCEL_GI_BUTTON = "xpath=//*[@id='goldenimages-add-cancel']"
    ID_CANCEL_CONFIRM_FORM = "xpath=/*[@id='hp-form-navigate-away-dialog']"
    ID_CANCEL_GI_YES_BUTTON = "xpath=//*[@id='hp-form-navigate-away-proceed']"
    ID_STATUS_GI = "xpath=//*[@id='goldenimages-show-status']"
    ID_GI_VISIBLE = "xpath=//*[@id='DataTables_Table_0_wrapper']/div/div[2]"
    ID_GI_VISIBLE_SELECT = "xpath=//*[@id='DataTables_Table_0']/tbody/tr/td[2]"
    ID_BUTTON_ACTION = "xpath=//*[@id='goldenimages-actions']/label"
    ID_BUTTON_EDIT = "xpath=//*[@id='goldenimages-edit-action']"
    ID_INPUT_EDIT_NAME = "xpath=//*[@id='goldenimages-edit-name']"
    ID_INPUT_EDIT_DESCRIPTION = "xpath=//*[@id='goldenimages-edit-desc']"
    ID_EDIT_OK_BUTTON = "xpath=//*[@id='goldenimages-edit-ok']"
    ID_BUTTON_REMOVE = "xpath=//*[@id='goldenimages-remove-action']"
    ID_YES_REMOVE_BUTTON = "xpath=//*[@id='hp-body-div']/div[9]/div/div/div/footer/div/button[1]"
    RADIOBUTTON_SELECT_WEB_SOURCE = "xpath=//*[@id='i3s-goldenimages-download-remote']"
    RADIOBUTTON_SELECT_LOCAL_SOURCE = "xpath=//*[@id='i3s-goldenimages-download-local']"
    CLICK_BROWSE_BUTTON = "//div[@id='goldenimages-filechooser-container']//input[1]"
    CHOOSE_FILE = "//input[@class='hp-button hp-file-chooser-file' and @name='file']"
    TOTAL_GI_AVAILABLE = "xpath=//*[@id='goldenimages-page']/nav/div[2]/span"
    ID_STATUS_GI_ERROR = "xpath=//*[@id='goldenimages-show-status']"
    ID_ADD_GI_STATUS = "xpath=//*[@id='goldenimages-details-status']"
    ID_ELEMENT_FORM_MESSAGE = "xpath=//*[@id='hp-activities']/tbody/tr[8]/td/div/div[2]/div/div[1]/p"
    ID_ELEMENT_GI = "xpath=//td[text()='%s']"
    ID_DELETE_FORM = "xpath=//*[@id='hp-body-div']/div[9]/div/div/div/header"
    ID_CANCEL_DELETE_BUTTON = "xpath=//*[@id='hp-body-div']/div[9]/div/div/div/footer/div/button[2]"
    ID_EDIT_FORM = "xpath=//*[@id='hp-change-page-container']/section/header"
    ID_CANCEL_EDIT_BUTTON = "xpath=//*[@id='goldenimages-edit-cancel']"
    GI_REMOVE_ERROR1 = "xpath=//*[@id='hp-activities']/tbody/tr[3]/td[2]/div"
    ACTIVITY_ERROR_COLLAPSE = "xpath=/*[@id='hp-activities']/tbody/tr[3]/td[1]/div"
    GI_REMOVE_ERROR1_OBJ = "xpath=//*[@id='hp-activities']/tbody/tr[4]/td/div/div[2]/div/div[1]/p/span"
    GI_REMOVE_ERROR2 = "xpath=//*[@id='hp-page-notifications']/div[1]/header"
    GI_PAGE_NOTIFICATION = "xpath=//*[@id='hp-page-notifications']"
    GI_REMOVE_ERROR2_OBJ = "xpath=//*[@id='hp-page-notifications']/div[1]/div/div[2]/div/div[1]/p/span"
    GI_ADD_ERROR_MSG = "xpath=//*[@id='hp-form-message']/div[1]/span"
    GI_ADD_ERROR_MSG_CONTENT = "xpath=//*[@id='hp-form-message']/div[2]"
    GI_ADD_INFOBAR = "xpath=//*[@id='hp-info-bar']"
    GI_ADD_PROGRESSBAR = "xpath=//*[@id='hp-page-notifications']/div[1]/header/div[4]/div/div"
    GI_ADD_COMPLETE = "xpath=//*[@id='hp-page-notifications']/div[1]/header"
    ID_ERROR_FORM = "xpath=//*[@id='hp-form-message']"
    ID_ERROR_LABEL = "xpath=//*[@id='goldenimages-add-panels']"
	

    GI_ADD_SUCCESS = "xpath=//*[@id='hp-page-notifications']//span[text()='Added goldenimages to Database']"
    GV_ADD_SUCCESS = "xpath=//*[@id='hp-page-notifications']//span[text()='Created Golden Volume for Golden Image']"
