# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on oedeploymentplan page/screen
'''

class i3sDeploymentPlanPage(object):
    ID_PAGE_LABEL = "xpath=//*[@id='deploymentplans-page']//h1[text()='Deployment Plans']"
    ID_DP_VISIBLE = "xpath=//*[@class='dataTables_scrollBody']"
    # Xpaths for create OEDP
    CREATE_OEDP_TITLE = "xpath=//span[@id='cic-profile-add-details-title' and text()='Create deployment plan']"
    ID_CREATE_DP_PAGE = "xpath=//*[@id='deploymentplans-page']//a[text()='Create deployment plan']"
    ID_INPUT_NAME = "xpath=//*[@id='deploymentplans-create-name']"
    ID_INPUT_DESCRIPTION = "xpath=//*[@id='deploymentplans-create-desc']"
    ID_INPUT_GOLDENIMAGE_DROPDOWN = "xpath=//label[text()='Golden Image']/following-sibling::div//div[@class='hp-search-combo-control']"
    ID_INPUT_GOLDENIMAGE = "//span[@class='hp-name' and text()='%s']"
    ID_INPUT_BUILDPLAN_DROPDOWN = "xpath=//label[text()='Oe Build Plan']/following-sibling::div//div[@class='hp-search-combo-control']"
    ID_INPUT_BUILDPLAN = "xpath=//span[@class='hp-name' and text()='%s']"
    ID_CREATE_DP_BUTTON = "xpath=//*[@id='deploymentplans-create']"
    ID_CREATEPLUS_DP_BUTTON = "xpath=//*[@id='deploymentplans-createplus']"
    ID_CANCEL_DP_BUTTON = "xpath=//*[@id='deploymentplans-create-cancel']"
    ID_BUTTON_ACTION = "xpath=//*[@id='deploymentplans-actions']//label[text()='Actions']"
    ID_BUTTON_DELETE = "xpath=//*[@id='deploymentplans-remove-action']"
    ID_BUTTON_EDIT = "xpath=//*[@id='deploymentplans-edit-action']"
    ID_CANCEL_CONFIRM_FORM = "xpath=//*[@id='hp-form-navigate-away-dialog']"
    ID_CANCEL_PROCEED_BUTTON = "xpath=//*[@id='hp-form-navigate-away-proceed']"
    ID_ERROR_FORM = "xpath=//*[@id='hp-form-message']"
    OEDP_INPUT_GI_TEXTBOX = "xpath=//*[@id='deploymentplans-create-goldenimageuri-input']"
    OEDP_INPUT_BP_TEXTBOX = "xpath=//*[@id='deploymentplans-create-oebuildplanuri-input']"
    ID_INPUT_OSTYPE_LIST = "deploymentplans-create-ostype"
    # Xpaths for Edit
    ID_EDIT_OEDP_TITLE = "xpath=//span[@data-localize='deploymentplans.edit.title' and text()='Edit Deployment Plan']"
    ID_EDIT_NAME = "xpath=//*[@id='deploymentplans-edit-name']"
    ID_EDIT_DESCRIPTION = "xpath=//*[@id='deploymentplans-edit-desc']"
    ID_EDIT_GOLDENIMAGE_CLOSE = "xpath=//label[text()='Golden Image']/following-sibling::div//div[@class='hp-close']"
    ID_EDIT_BUILDPLAN_CLOSE = "xpath=//label[text()='Oe Build Plan']/following-sibling::div//div[@class='hp-close']"
    ID_EDIT_BUILDPLAN = "//span[@class='hp-name' and text()='%s']"
    ID_EDIT_OK_BUTTON = "xpath=//*[@id='deploymentplans-edit-ok']"
    ID_EDIT_CANCEL_BUTTON = "xpath=//*[@id='deploymentplans-edit-cancel']"
    ID_EDIT_DESC_CHECK = "xpath=//*[@id='deploymentplans-show-desc' and text()='%s']"
    ID_EDIT_OSTYPE_CHECK = "xpath=//*[@id='deploymentplans-show-ostype' and text()='%s']"
    ID_EDIT_GIURI_CHECK = "xpath=//*[@id='deploymentplans-show-goldenimageuri' and text()='%s']"
    ID_EDIT_BPURI_CHECK = "xpath=//*[@id='deploymentplans-show-oebuildplanuri' and text()='%s']"
    ID_EDIT_OSTYPE_LIST = "deploymentplans-edit-ostype"
    OEDP_EDIT_GI_TEXTBOX = "xpath=//*[@id='deploymentplans-edit-goldenimageuri-input']"
    OEDP_INVALID_BP_MSSG = "xpath=//div[@class='hp-header' and text()='No matches']"
    OEDP_EDIT_BP_TEXTBOX = "xpath=//*[@id='deploymentplans-edit-oebuildplanuri-input']"
    # Xpaths for delete
    ID_DELETE_FORM = "//div[@class='hp-dialog']"
    ID_YES_DELETE_BUTTON = "//button[contains(text(),'Yes, delete')]"
    ID_CANCEL_DELETE_BUTTON = "//button[contains(text(),'Cancel')]"
    ID_ELEMENT_DEPLOYMENTPLAN = "xpath=//td[text()='%s']"
    # Xpaths for blank name error messages
    ID_BLANK_NAME = "xpath=//label[@for='deploymentplans-create-name' and text()='This field is required.']"
    ID_BLANK_DESCRIPTION = "xpath=//label[@for='deploymentplans-create-desc' and text()='This field is required.']"
    OEDP_BLANK_GI_URL_MESSAGE = "xpath=//label[@for='deploymentplans-create-goldenimageuri' and text()='This field is required.']"
    OEDP_BLANK_BP_URL_MESSAGE = "xpath=//label[@for='deploymentplans-create-oebuildplanuri' and text()='This field is required.']"
    ID_BLANK_NAME_EDIT = "xpath=//label[@for='deploymentplans-edit-name' and text()='This field is required.']"
    ID_BLANK_DESCRIPTION_EDIT = "xpath=//label[@for='deploymentplans-edit-desc' and text()='This field is required.']"
    OEDP_BLANK_GI_URL_MESSAGE_EDIT = "xpath=//label[@for='deploymentplans-edit-goldenimageuri' and text()='This field is required.']"
    OEDP_BLANK_BP_URL_MESSAGE_EDIT = "xpath=//label[@for='deploymentplans-edit-oebuildplanuri' and text()='This field is required.']"
















