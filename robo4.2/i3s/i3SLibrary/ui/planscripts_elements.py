# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on planscripts page/screen
'''
# from _curses import BUTTON1_CLICKED
from Tkconstants import RADIOBUTTON

class i3sPlanScriptPage(object):
    ID_CREATE_PS_TITLE = "xpath=//span[@id='cic-profile-add-details-title' and\
     text()='Create Plan Scripts']"
    ID_ACTION_CREATE_BUTTON = "xpath=//*[@id='planscripts-create-action']"
    ID_ACTION_DELETE_BUTTON = "xpath=//*[@id='planscripts-remove-action']"
    ID_BUTTON_ACTION = "xpath=//*[@id='planscripts-actions']/label"
    ID_BUTTON_COPY = "xpath=//*[@id='planscripts-copy-action']"
    ID_BUTTON_EDIT = "xpath=//*[@id='planscripts-edit-action']"
    ID_CANCEL_BUTTON_YES = "xpath=//button[contains(text(),'Yes, proceed')]"
    ID_CANCEL_CONFIRMATION_FORM = "xpath=//*[@id='hp-form-navigate-away-dialog']"
    ID_CANCEL_PS_BUTTON = "xpath=//*[@id='planscripts-add-cancel']"
    ID_COPY_CANCEL_BUTTON = "xpath=//*[@id='planscripts-copy-cancel']"
    ID_COPY_ERROR_FORM = "xpath=//*[@id='planscripts-copy-form]'"
    ID_COPY_FORM = "xpath=//*[@class='hp-action hp-ellipsised' and text()='Copy']"
    ID_COPY_OK_BUTTON = "xpath=//*[@id='planscripts-copy-ok']"
    ID_CREATE_BUTTON = "xpath=//*[@id='planscripts-create-action']"
    ID_CREATE_PS = "xpath=//*[@id='planscripts-page']//a[text()='Create Plan Script']"
    ID_CREATE_PS_BUTTON = "xpath=//*[@id='planscripts-add']"
    ID_CREATE_PS_PAGE = "xpath=//*[@id='hp-change-page-container']"
    ID_CREATEPLUS_PS_BUTTON = "xpath=//*[@id='planscripts-addplus']"
    ID_CUSTOM_ATTR_VIEW = "xpath=//*[@id='planscripts-show-ca-table_wrapper']"
    ID_CUSTOM_ATTR_KEY = "xpath=//*[@id='planscripts-show-ca-table']/tbody/tr/td[text()='%s']"
    ID_CUSTOM_ATTR_VALUE = "xpath=//*[@id='planscripts-show-ca-table']/tbody/tr/\
    td[text()='%s']/following-sibling::td[2 and text()='%s']"
    ID_DELETE_BUTTON_CANCEL = "//button[contains(text(),'Cancel')]"
    ID_DELETE_BUTTON_YES = "//button[contains(text(),'Yes, Delete')]"
    ID_DELETE_FORM = "xpath= //*[@class='hp-action hp-ellipsised' and text()='Delete']"
    ID_EDIT_CANCEL_BUTTON = "xpath=//*[@id='planscripts-edit-cancel']"
    ID_EDIT_CONTENT = "xpath=//*[@id='planscripts-edit-content']"
    ID_EDIT_CONTENT_CHECK = "xpath=//*[@id='planscripts-show-scripts' and text()='%s']"
    ID_EDIT_COPY_NAME = "xpath=//*[@id='planscripts-copy-name']"
    ID_EDIT_DESC_CHECK = "xpath=//*[@id='planscripts-show-desc' and text()='%s']"
    ID_EDIT_DESCRIPTION = "xpath=//*[@id='planscripts-edit-desc']"
    ID_EDIT_NAME = "xpath=//*[@id='planscripts-edit-name']"
    ID_EDIT_OK_BUTTON = "xpath=//*[@id='planscripts-edit-ok']"
    ID_EDIT_PS_TITLE = "xpath=//*[@id='planscripts-edit-title']"
    ID_ELEMENT_PS = "xpath=//td[text()='%s']"  # Replace %s with planscript
    ID_INPUT_CONTENT = "xpath=//*[@id='planscripts-add-content']"
    ID_INPUT_DESCRIPTION = "xpath=//*[@id='planscripts-add-description']"
    ID_INPUT_NAME = "xpath=//*[@id='planscripts-add-name']"
    ID_OS_TYPE = "xpath=//*[@id='planscripts-add-ostype']"
    ID_OS_TYPE_LIST = "planscripts-add-ostype"
    ID_PLAN_TYPE = "xpath=//*[@id='planscripts-add-plantype']"
    ID_PLAN_TYPE_CAPTURE = "xpath=//*[@id='planscripts-add-plantype']/option[1]"
    ID_PLAN_TYPE_DEPLOYMENT = "xpath=//*[@id='planscripts-add-plantype']/option[2]"
    ID_PLAN_TYPE_LIST = "planscripts-add-plantype"
    ID_PS_CONTENT = "xpath=//*[@id='planscripts-add-content']"
    ID_PS_VISIBLE = "xpath=//*[@class='dataTables_scrollBody']"
    ID_STATUS_PS = "xpath=//*[@id='planscripts-details-status']"
    ID_PAGE_LABEL = "xpath=//*[@id='planscripts-page']/*/*/*[text()='Plan Scripts']"
    # Error messages
    ID_BLANK_CONTENT = "xpath=//label[@for='planscripts-add-content' and \
    text()='This field is required.']"
    ID_BLANK_DESCRIPTION = "xpath=//label[@for='planscripts-add-description' and \
    text()='This field is required.']"
    ID_EDIT_BLANK_DESCRIPTION = "xpath=//label[@for='planscripts-edit-desc' and \
    text()='This field is required.']"
    ID_BLANK_NAME = "xpath=//label[@for='planscripts-add-name' and text()='This field is required.']"
    ID_ERROR_FORM = "xpath=//*[@id='hp-form-message']"
    PS_DUPLICATE_NAME_DETAILS = "xpath=//*[@id='hp-form-message']//"
    "span[text()='Planscript with same name already exists on the appliance.']"
    PS_DUPLICATE_NAME_MESSAGE = "xpath=//*[@id='hp-form-message']//"
    "span[text()='Planscript with same name already exists.']"
    PS_DUPLICATE_NAME_RESOLUTION = "xpath=//*[@id='hp-form-message']//"
    "span[text()='Provide a different name for the new Planscript.']"
    PS_DUPLICATE_NAME_UPDATE_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update \
    planscript.']"
    PS_INVALID_CONTENTTEXT_DETAILS = "xpath=//*[@id='hp-form-message']//span[text()='The value specified \
    for the parameter {0} is not valid or not supported.']"
    PS_INVALID_CONTENTTEXT_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='The value specified \
    for the parameter {0} is not valid or not supported.']"
    PS_INVALID_CONTENTTEXT_RESOLUTION = "xpath=//*[@id='hp-form-message']//span[text()='{0) parameter cannot \
    be null or contain white space/TAB characters. Verify parameters and try again.']"
    PS_INVALID_CONTENTTEXT_UPDATE_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update\
     planscript.']"
    PS_INVALID_DESCRIPTION_DETAILS = "xpath=//*[@id='hp-form-message']//span[text()='The value specified for\
     the parameter {0} is not valid or not supported.']"
    PS_INVALID_DESCRIPTION_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='The value specified for\
     the parameter {0} is not valid or not supported.']"
    PS_INVALID_DESCRIPTION_RESOLUTION = "xpath=//*[@id='hp-form-message']//span[text()='{0} parameter cannot\
     be empty and should be less than 1000 characters. Verify parameters and try again.']"
    PS_INVALID_NAME_DETAILS = "xpath=//*[@id='hp-form-message']//span[text()='The value specified for the\
     parameter {0} is not valid or not supported.']"
    PS_INVALID_NAME_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='The value specified for the\
     parameter {0} is not valid or not supported.']"
    PS_INVALID_NAME_RESOLUTION = "xpath=//*[@id='hp-form-message']//span[text()='={0} parameter cannot be\
     empty and should be unique and less than 255 characters. Verify parameters and try again.']"
    PS_INVALID_UPDATE_DESCRIPTION_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update planscript.']"
    PS_INVALID_UPDATE_NAME_MESSAGE = "xpath=//*[@id='hp-form-message']//span[text()='Unable to update planscript.']"
