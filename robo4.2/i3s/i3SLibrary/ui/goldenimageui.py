# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    goldenimage UI
"""

from robot.libraries.BuiltIn import BuiltIn, _Verify
from i3SLibrary.ui.general.base_elements import i3SBasePage
from i3SLibrary.ui.goldenimage_elements import i3sgoldenimagePage
from i3SLibrary.ui import error_messages
from i3SLibrary.ui.general import base_page
from i3SLibrary.ui.general import base_elements
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def navigate():
    base_page.navigate_base(i3sgoldenimagePage.ID_PAGE_LABEL, i3SBasePage.ID_MENU_LINK_GOLDEN_IMAGES, "css=span.hp-page-item-count")

    if not ui_lib.wait_for_element(i3sgoldenimagePage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to Golden Image page", True)

def return_to_add_goldenimage():
    
    if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_CANCEL_GI_BUTTON):
        ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_CANCEL_GI_BUTTON)
        if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_CANCEL_CONFIRM_FORM):
            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_CANCEL_CONFIRM_FORM)
            
            if not ui_lib.wait_for_element(i3sgoldenimagePage.ID_PAGE_LABEL):
                ui_lib.fail_test("Failed to navigate to GI page", True)
            if ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI):
                ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_PAGE)
    
    else:
        if not ui_lib.wait_for_element(i3sgoldenimagePage.ID_PAGE_LABEL):
            ui_lib.fail_test("Failed to navigate to Golden Image page", True)
        if ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI):
            ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_PAGE)
    return


def add_goldenimage(self, *addgoldenimageui_obj):
    """ Select Add-Golden-Image
        Example:
        | `Select Add-Golden-Image`      |     |
    """
    s2l = ui_lib.get_s2l()
    error = 0
    return_data = ""
    """ Navigate to Golden Image Page """
    if not s2l._is_element_present(i3sgoldenimagePage.ID_PAGE_LABEL):
        navigate()
    if ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI):
        ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_PAGE)
    logging._log_to_console_and_log_file("Successfully opened Add-golden-image page")

    """ Retrieve data from datasheet """
    if type(addgoldenimageui_obj) is test_data.DataObj:
        addgoldenimageui_obj = [addgoldenimageui_obj]
    elif type(addgoldenimageui_obj) is tuple:
        addgoldenimageui_obj = list(addgoldenimageui_obj[0])
        logging._log_to_console_and_log_file(type(addgoldenimageui_obj))
    for gi in addgoldenimageui_obj:
        logger._log_to_console_and_log_file("inside for loop")

        ''' Below are flags to track invalid inputs'''
        name_flag = 1
        desc_flag = 1
        url_flag = 1
        dup_name_flag = 0
        special_char_flag = 0
        non_exis_gi_flag = 0

        logger._log_to_console_and_log_file("gi is " + str(gi))

        ''' In the below code, flags are set/unset based on the validity of the input parameters'''
        if (gi.name == "" or len(gi.name) > 255):
            name_flag = 0
        if (gi.description == "" or len(gi.description) > 1024):
            desc_flag = 0
        if (gi.URL == ""):
            url_flag = 0

        """ Before Adding check for the Golden Image exists """
        logger._log_to_console_and_log_file(" name_flag is" + str(name_flag))
        if name_flag:
            logger._log_to_console_and_log_file("inside name flag")
            if s2l._is_element_present(i3sgoldenimagePage.ID_ELEMENT_GI % gi.name):
                ''' set dup_name_flag to true if name already exists'''
                dup_name_flag = 1
                logger._log_to_console_and_log_file(" dup name")
            logger._log_to_console_and_log_file(" name_flag is" + str(name_flag))
            ui_lib.wait_for_element_and_input_text(i3sgoldenimagePage.ID_INPUT_NAME, gi.name)

        if desc_flag:
            ui_lib.wait_for_element_and_input_text(i3sgoldenimagePage.ID_INPUT_DESCRIPTION, gi.description)
            logger._log_to_console_and_log_file("inside desc flag")

        ui_lib.wait_for_element_and_click(i3sgoldenimagePage.RADIOBUTTON_SELECT_WEB_SOURCE)

        if url_flag:
            ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_INPUT_URL)
            logging._log_to_console_and_log_file("Able to find field to enter url")
            logger._log_to_console_and_log_file(" url_flag is" + str(url_flag))
            ui_lib.wait_for_element_and_input_text(i3sgoldenimagePage.ID_INPUT_URL, gi.URL)
            logger._log_to_console_and_log_file("button is" + str(gi.button))

        if (gi.button != "cancel"):
            if (gi.button == "Add"):
                logger._log_to_console_and_log_file("inside Add loop")
                ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_BUTTON)
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI_BUTTON)
            elif (gi.button == "Add+"):
                logger._log_to_console_and_log_file("inside Add+ loop")
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADDPLUS_GI_BUTTON)


            '''checking for blank name and description field messages'''
            if (name_flag == 0 and len(gi.name) > 255 and desc_flag == 0 and len(gi.description) > 1024 and url_flag == 0 and len(gi.URL) > 128):
                logger._log_to_console_and_log_file("inside blank name")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_FORM):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM).strip()) == 0:
                        logger._warn('Blank error form')
                    elif (text != error_messages.GI_ADD_INVALID_NAME_MESSAGE):
                        logger._warn("Error message displayed  doesn't match the invalid golden image error message")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
                if not ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_LABEL):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL).strip()) == 0:
                        logger._warn('Blank label in the panel')
                    elif (text != error_messages.GI_ADD_EMPTY_NAME_MESSAGE):
                        logger._warn("Label displayed  doesn't match the invalid golden image label")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
                   
                logger._log_to_console_and_log_file("inside blank desc")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_LABEL):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL).strip()) == 0:
                        logger._warn('Blank label in the panel')
                    elif (text != error_messages.GI_ADD_EMPTY_DESCRIPTION_MESSAGE):
                        logger._warn("Label displayed  doesn't match the invalid golden image description label")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
                        
                logger._log_to_console_and_log_file("inside blank URL")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_LABEL):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL).strip()) == 0:
                        logger._warn('Blank label in the panel')
                    elif (text != error_messages.GI_ADD_EMPTY_URL_MESSAGE):
                        logger._warn("Label displayed  doesn't match the invalid golden image description label")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
                
                return_to_add_goldenimage()
                continue

            
            '''checking for Duplicate Name'''
            if (dup_name_flag == 0):
                logger._log_to_console_and_log_file("inside dup name flag loop")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_FORM):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM).strip()) == 0:
                        logger._warn('Blank error form')
                    elif (text != error_messages.GI_ADD_DUPLICATE_NAME_MESSAGE):
                        logger._warn("Error message displayed  doesn't match the duplicate golden image error message")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
            
                return_to_add_goldenimage()
                continue
                   

            '''Changed GI_INVALID_INPUT_* to GI_INVALID_NAME_*'''
            if (special_char_flag == 0):
                logger._log_to_console_and_log_file("inside Invalid Characters name flag loop")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_FORM):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM).strip()) == 0:
                        logger._warn('Blank error form')
                    elif (text != error_messages.GI_ADD_INVALID_NAME_MESSAGE):
                        logger._warn("Error message displayed  doesn't match the duplicate golden image error message")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
            
                return_to_add_goldenimage()
                continue

            logging._log_to_console_and_log_file("\n Adding Golden Image please wait ...\n")

            if ui_lib.wait_for_element_visible(i3sgoldenimagePage.GI_ADD_INFOBAR):
                addinfo = s2l._get_text(i3sgoldenimagePage.GI_ADD_INFOBAR)
                logging._log_to_console_and_log_file("Info bar Message: '%s'" % addinfo)
                s2l._is_element_present(i3sgoldenimagePage.GI_ADD_PROGRESSBAR)
                ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_STATUS)
                if s2l._is_element_present(i3sgoldenimagePage):
                    ui_lib.wait_for_element_and_click(i3sgoldenimagePage.GI_ADD_COMPLETE)
                    ui_lib.wait_for_element(i3sgoldenimagePage.GI_ADD_SUCCESS)
                    addsuccess1 = s2l._get_text(i3sgoldenimagePage.GI_ADD_SUCCESS)
                    logging._log_to_console_and_log_file("Info bar Message: '%s'" % addsuccess1)
                    ui_lib.wait_for_element(i3sgoldenimagePage.GV_ADD_SUCCESS)
                    addsuccess2 = s2l._get_text(i3sgoldenimagePage.GV_ADD_SUCCESS)
                    logging._log_to_console_and_log_file("Info bar Message: '%s'" % addsuccess2)
                    logger._log_to_console_and_log_file("golden image '%s' Added successfully" % gi.name)
                    continue

            else:
                logger._warn("Creating golden image %s failed" % gi.name)
                continue

            ''' To continue to next scenario, we need to have the Add page displayed '''
            if (gi.button == 'Add'):
                if ui_lib.wait_for_element(i3sgoldenimagePage.ID_ELEMENT_GI % gi.name):
                    logger._log_to_console_and_log_file("Golden Image '%s' created successfully" % gi.name)
                    logger._log_to_console_and_log_file("inside Add button loop")
                    ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI)
                    if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_PAGE):
                        logger._log_to_console_and_log_file("ON Golden Image Add Page")
                    continue
                else:
                    logger._warn("Creating golden image %s failed" % gi.name)
                    continue

            if (gi.button == 'Add+'):
                logger._log_to_console_and_log_file("inside Add+ flag loop")
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADDPLUS_GI_BUTTON)
                logging._log_to_console_and_log_file("\n Adding Golden Image please wait ...\n")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_PAGE):
                    logger._log_to_console_and_log_file("In GI UI")
                    continue
                else:
                    logger._log_to_console_and_log_file("Failed to return to GI UI")
                    continue
            logger._log_to_console_and_log_file("before continue in outer loop")
            continue
        elif (gi.button == 'cancel'):
                logger._log_to_console_and_log_file("inside cancel flag loop")
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_CANCEL_GI_BUTTON)
                if not ui_lib.wait_for_element(i3sgoldenimagePage.ID_PAGE_LABEL):
                    logger._warn("Failed to navigate to Golden Image page")
                else:
                    if not ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ELEMENT_GI):
                        logger._log_to_console_and_log_file("Golden Image '%s' not created " % gi.name)
                    else:
                        logger._warn("Golden Image '%s' created " % gi.name)
                    if ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI):
                        ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_PAGE)
                        logger._log_to_console_and_log_file("Clicked on Add GI button")

                return_to_add_goldenimage()
                continue
    return


def return_to_edit_goldenimage():
    ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_CANCEL_EDIT_BUTTON)
    if not ui_lib.wait_for_element(i3sgoldenimagePage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to Edit GI page", True)
    if ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_ACTION):
        ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_EDIT)
        ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_EDIT_FORM)
    logging._log_to_console_and_log_file("Edit Golden Image Clicked")
    return


def edit_goldenimage(self, *editgoldenimage_obj):

    """ Select Edit Golden Image 
        Example:
        | Edit GoldenImage     |     |
    """
    s2l = ui_lib.get_s2l()
    error = 0
    return_data = ""
    """ Navigate to Golden Image Page """
    if not s2l._is_element_present(i3sgoldenimagePage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(i3sgoldenimagePage.ID_GI_VISIBLE_SELECT)

    """ Retrieve data from datasheet """
    if type(editgoldenimage_obj) is test_data.DataObj:
        editgoldenimage_obj = [editgoldenimage_obj]
    elif type(editgoldenimage_obj) is tuple:
        editgoldenimage_obj = list(editgoldenimage_obj[0])
    logging._log_to_console_and_log_file(type(editgoldenimage_obj))

    for gi in editgoldenimage_obj:
        if s2l._page_contains(gi.nameedit):
            gi_obj = i3sgoldenimagePage.ID_ELEMENT_GI % gi.nameedit
            s2l.mouse_over(gi_obj)
            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ELEMENT_GI % gi.nameedit)
            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_ACTION)
            if s2l._is_visible(i3sgoldenimagePage.ID_BUTTON_EDIT):
                logger._log_to_console_and_log_file("Edit Golden Image '%s'" % gi.name)
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_EDIT)


        ''' Below are flags to track invalid inputs'''
        name_flag = 1
        desc_flag = 1
        dup_name_flag = 0
        special_char_flag = 0
        non_exis_gi_flag = 0

        logger._log_to_console_and_log_file("gi is " + str(gi))

        ''' In the below code, flags are set/unset based on the validity of the input parameters'''
        if (gi.name == "" or len(gi.name) > 255):
            name_flag = 0
        if (gi.description == "" or len(gi.description) > 1024):
            desc_flag = 0

        """ Before Adding check for the Golden Image exists """
        logger._log_to_console_and_log_file(" name_flag is" + str(name_flag))
        if name_flag:
            logger._log_to_console_and_log_file("inside name flag")
            if s2l._is_element_present(i3sgoldenimagePage.ID_ELEMENT_GI % gi.nameedit):
                ''' set dup_name_flag to true if name already exists'''
                dup_name_flag = 1
                logger._log_to_console_and_log_file(" dup name")
            logger._log_to_console_and_log_file(" name_flag is" + str(name_flag))
            ui_lib.wait_for_element_and_input_text(i3sgoldenimagePage.ID_INPUT_EDIT_NAME, gi.name)

        if desc_flag:
            ui_lib.wait_for_element_and_input_text(i3sgoldenimagePage.ID_INPUT_EDIT_DESCRIPTION, gi.description)
            logger._log_to_console_and_log_file("inside desc flag")

        if (gi.button != "cancel"):
            if (gi.button == "OK"):
                logger._log_to_console_and_log_file("inside Edit loop")
                ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_EDIT_OK_BUTTON)
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_EDIT_OK_BUTTON)


            '''checking for blank name error message'''
            if (name_flag == 0 and len(gi.name) > 255 and desc_flag == 0 and len(gi.description)):
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_FORM):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM).strip()) == 0:
                        logger._warn('Blank error form')
                    elif (text != error_messages.GI_EDIT_INVALID_NAME_MESSAGE):
                        logger._warn("Error message displayed  doesn't match the invalid golden image error message")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
                if not ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_LABEL):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL).strip()) == 0:
                        logger._warn('Blank label in the panel')
                    elif (text != error_messages.GI_EDIT_DUPLICATE_NAME_MESSAGE):
                        logger._warn("Label displayed  doesn't match the invalid golden image label")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
                  
                logger._log_to_console_and_log_file("inside blank desc")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_LABEL):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_LABEL).strip()) == 0:
                        logger._warn('Blank label in the panel')
                    elif (text != error_messages.GI_ADD_EMPTY_DESCRIPTION_MESSAGE):
                        logger._warn("Label displayed  doesn't match the invalid golden image description label")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
  
                return_to_edit_goldenimage()
                continue


            '''Duplicate Name'''
            if (dup_name_flag == 0):
                logger._log_to_console_and_log_file("inside dup name flag loop")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_FORM):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM).strip()) == 0:
                        logger._warn('Blank error form')
                    elif (text != error_messages.GI_EDIT_DUPLICATE_NAME_MESSAGE):
                        logger._warn("Error message displayed  doesn't match the duplicate golden image error message")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
            
                return_to_edit_goldenimage()
                continue

            '''Changed GI_INVALID_INPUT_* to GI_INVALID_NAME_*'''
            if (special_char_flag == 0):
                logger._log_to_console_and_log_file("inside Invalid Characters name flag loop")
                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ERROR_FORM):
                    text = ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM)
                    if len(ui_lib.get_text(i3sgoldenimagePage.ID_ERROR_FORM).strip()) == 0:
                        logger._warn('Blank error form')
                    elif (text != error_messages.GI_EDIT_INVALID_NAME_MESSAGE):
                        logger._warn("Error message displayed  doesn't match the duplicate golden image error message")
                        logger._log_to_console_and_log_file("Error message is" + str(text))
            
                return_to_edit_goldenimage()
                continue

            logging._log_to_console_and_log_file("\n Editing Golden Image please wait ...\n")

            if ui_lib.wait_for_element_remove(i3sgoldenimagePage.ID_ELEMENT_GI % str(gi.nameedit), PerfConstants.REMOVE_SERVER):
                    logger._log_to_console_and_log_file("Edited Golden Image '%s'" % gi.nameedit)
            else:
                logger._warn("FAILED :: Golden Image can't be edited - '%s'" % gi.name)

            ''' To continue to next scenario, we need to have the Add page displayed '''
            if (gi.button == 'OK'):
                if ui_lib.wait_for_element(i3sgoldenimagePage.ID_ELEMENT_GI % gi.nameedit):
                    logger._log_to_console_and_log_file("Golden Image '%s' Edited successfully" % gi.name)
                    logger._log_to_console_and_log_file("inside Edit button loop")
                    ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_ACTION)
                    if s2l._is_visible(i3sgoldenimagePage.ID_BUTTON_EDIT):
                        logger._log_to_console_and_log_file("Edit Golden Image '%s'" % gi.name)
                        ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_EDIT)
                        continue
                else:
                    logger._warn("Editing golden image %s failed" % gi.name)
                    continue
            elif (gi.button == 'cancel'):
                logger._log_to_console_and_log_file("inside cancel flag loop")
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_CANCEL_EDIT_BUTTON)
                if not ui_lib.wait_for_element(i3sgoldenimagePage.ID_PAGE_LABEL):
                    logger._warn("Failed to navigate to Edit Golden Image page")
                else:
                    if not ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ELEMENT_GI):
                        logger._log_to_console_and_log_file("Golden Image '%s' not Edited " % gi.nameedit)
                    else:
                        logger._warn("Golden Image '%s' Edited " % gi.name)
                    if ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_ACTION):
                        ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_EDIT)
                        ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_EDIT_FORM)
                        logger._log_to_console_and_log_file("Clicked on Edit GI button")

                return_to_edit_goldenimage()
                continue
    return



def delete_goldenimage(self, *removegoldenimage_obj):

    """ Select Delete Golden Image 
        Example:
        | Edit GoldenImage     |     |
    """
    s2l = ui_lib.get_s2l()
    s2l = ui_lib.get_s2l()
    error = 0
    return_data = ""
    """ Navigate to Golden Image Page """
    if not s2l._is_element_present(i3sgoldenimagePage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(i3sgoldenimagePage.ID_GI_VISIBLE_SELECT)

    """ Retrieve data from datasheet """
    if type(removegoldenimage_obj) is test_data.DataObj:
        removegoldenimage_obj = [removegoldenimage_obj]
    elif type(removegoldenimage_obj) is tuple:
        removegoldenimage_obj = list(removegoldenimage_obj[0])
    logging._log_to_console_and_log_file(type(removegoldenimage_obj))

    for gi in removegoldenimage_obj:
        if s2l._page_contains(gi.name):
            gi_Obj = i3sgoldenimagePage.ID_ELEMENT_GI % gi.name
            s2l.mouse_over(gi_Obj)
            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ELEMENT_GI % gi.name)
            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_ACTION)
            if s2l._is_visible(i3sgoldenimagePage.ID_BUTTON_REMOVE):
                logger._log_to_console_and_log_file("Remove Golden Image '%s'" % gi.name)
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_BUTTON_REMOVE)

                if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_DELETE_FORM):  # Wait for GI form to visible
                    if (gi.button == "Remove"):
                        ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_YES_REMOVE_BUTTON)
                        if ui_lib.wait_for_element_visible(i3sgoldenimagePage.GI_PAGE_NOTIFICATION):
                            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.GI_REMOVE_ERROR2)
                            error2 = s2l._get_text(i3sgoldenimagePage.GI_REMOVE_ERROR2_OBJ)
                            logger._log_to_console_and_log_file("Failure Error: '%s'" % error2)
                            logger._warn("Failed to remove Golden Image")
                            continue
                        elif (gi.button == "Cancel"):
                            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_CANCEL_DELETE_BUTTON)
                            logger._log_to_console_and_log_file(" Golden Image '%s' not deleted as Cancel was chosen" % gi.name)
                            continue
                else:
                    logger._warn("Golden Image is not visible")
                    continue
                # validating Golden Image removal
                if ui_lib.wait_for_element_remove(i3sgoldenimagePage.ID_ELEMENT_GI % str(gi.name), PerfConstants.REMOVE_SERVER):
                    logger._log_to_console_and_log_file("Removed Golden Image '%s'" % gi.name)
                else:
                    logger._warn("FAILED :: Golden Image can't be removed - '%s'" % gi.name)

            else:
                logger._warn("'%s' Golden Image can't be deleted, Remove option is not visible on page." % gi.name)
        else:
            logger._warn("'%s' Golden Image not found in Golden Image page" % gi.name)
            continue
    return



################################################
'''
Selecting Golden Image from Local Source
'''
################################################

def add_localgoldenimage(self, *testdata):
    """ Select Add-Golden-Image
        Example:
        | `Select Add-Golden-Image`      |     |
    """
    navigate()
    if ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI):
        ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_PAGE)
        logging._log_to_console_and_log_file("Successfully opened Add-golden-image page")

        s2l = ui_lib.get_s2l()
        error = 0
        return_data = ""

        if not s2l._is_element_present(i3sgoldenimagePage.ID_ADD_GI_PAGE):
            navigate()

        testdata = list(testdata[0])
        logging._log_to_console_and_log_file(type(testdata))

        for gi in testdata:
            # if gi.name not in testdata:
                # logger._warn("LS '%s' does not exist" % gi.name)
                # error += 1
            # continue

            ui_lib.wait_for_element_and_input_text(
                i3sgoldenimagePage.ID_INPUT_NAME,
                gi.name)

            ui_lib.wait_for_element_and_input_text(
                i3sgoldenimagePage.ID_INPUT_DESCRIPTION,
                gi.description)

            ui_lib.wait_for_element_and_click(i3sgoldenimagePage.RADIOBUTTON_SELECT_LOCAL_SOURCE)
            sleep(3)

            # if  ui_lib.wait_for_element_visible(i3sgoldenimagePage.CLICK_BROWSE_BUTTON, PerfConstants.FIRMWARE_ADD_BUTTON_TIME):
            ui_lib.wait_for_element_visible(i3sgoldenimagePage.CLICK_BROWSE_BUTTON, PerfConstants.FIRMWARE_ADD_BUTTON_TIME)
            s2l.click_element(i3sgoldenimagePage.CHOOSE_FILE)
            ui_lib.wait_for_element_visible(i3SImageBundlePage.ID_BTN_CHOOSE_FILE, PerfConstants.FIRMWARE_CHOOSE_BUTTON_TIME)
            s2l.choose_file(i3sgoldenimagePage.CHOOSE_FILE, "C:\Users\sasankot\Downloads\hpesxi.zip")
            if ntnative.NativeOsKeywords.send_keys_to_native_window("{TAB}{TAB}{TAB}{ENTER}"):
                logging._log_to_console_and_log_file("Able to close the window...")
            else:
                logging._log_to_console_and_log_file("Not Able to close the window ...")
                return False

            if ui_lib.wait_for_element_visible(i3sgoldenimagePage.ID_ADD_GI_BUTTON):
                logging._log_to_console_and_log_file("Able to find Add Button")
                ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_ADD_GI_BUTTON)
            else:
                logging._log_to_console_and_log_file("Not able to find Add Button")
                return False

            logging._log_to_console_and_log_file("Adding GI in to the DB please wait ...")
            # sleep(180)

            if ui_lib.wait_for_element_text_match(i3sgoldenimagePage.ID_STATUS_GI_ERROR, "Unknown"):
                    logging._log_to_console_and_log_file("Failed to Add-golden-image")
                    return False

                # ui_lib.wait_for_element_and_click(i3sgoldenimagePage.ID_CANCEL_GI_BUTTON)
            elif ui_lib.wait_for_element_text_match(i3sgoldenimagePage.ID_STATUS_GI, "ok"):
                    logging._log_to_console_and_log_file("Golden Image Added successfully.")
                    return True
            else:
                logging._log_to_console_and_log_file("unknown reason")
                return False
        return

