# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
"""
    Deploymentplan UI
"""

from robot.libraries.BuiltIn import BuiltIn
from i3SLibrary.ui.general.base_elements import i3SBasePage
from i3SLibrary.ui.oedeploymentplan_elements import i3sDeploymentPlanPage
from i3SLibrary.ui.general import base_page
from i3SLibrary.ui.general import base_elements
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from i3SLibrary.ui import error_messages
from time import sleep
import re
import Selenium2Library

def navigate():
    base_page.navigate_base(i3sDeploymentPlanPage.ID_PAGE_LABEL, i3SBasePage.ID_MENU_LINK_DEPLOYMENTPLANS, "css=span.hp-page-item-count")

    if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to OE Deployment page", True)

def return_to_create_dppage():
    '''Return to OEDP UI by clicking Cancel in Create oedp UI'''
    if  ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_CANCEL_DP_BUTTON):
        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CANCEL_DP_BUTTON)
        if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_CANCEL_CONFIRM_FORM):
            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CANCEL_PROCEED_BUTTON)
            if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_PAGE_LABEL):
                ui_lib.fail_test("Failed to navigate to OE Deployment page", True)
    return


def create_oedeploymentplan(self, *createoedeploymentplan_obj):
    """ Select Create OEDeploymentplans - Create OEDP for valid input-data 
    check for error messages for invalid data
        Example:
        | Select Create-OEDeploymentplans     |     |
    """
    MAX_CHAR = 255
    s2l = ui_lib.get_s2l()
    """ Navigate to DeploymentPlan Page """

    if not s2l._is_element_present(i3sDeploymentPlanPage.ID_PAGE_LABEL):
        navigate()

    """ Retrieve data from datasheet """
    if type(createoedeploymentplan_obj) is test_data.DataObj:
        createoedeploymentplan_obj = [createoedeploymentplan_obj]
    elif type(createoedeploymentplan_obj) is tuple:
        createoedeploymentplan_obj = list(createoedeploymentplan_obj[0])
    for oedp in createoedeploymentplan_obj:
        ''' In the below code, flags are set/unset based on the validity of the input parameters'''
        ''' Below are flags to track invalid inputs'''
        name_flag = 1
        desc_flag = 1
        gi_flag = 1
        bp_flag = 1
        new_name_flag = 1
        special_char_flag = 1
        exis_gi_flag = 1
        exis_bp_flag = 1

        if re.search('[^a-zA-Z_]', oedp.name):
            special_char_flag = 0
        if (oedp.name == ""):
            name_flag = 0
            special_char_flag = 1
        if (oedp.description == ""):
            desc_flag = 0
        if (oedp.goldenimageuri == ""):
            gi_flag = 0
        if (oedp.oebuildplanuri == ""):
            bp_flag = 0

        """ Before Adding check for the Deploymentplan exists """
        if name_flag:
            if s2l._is_element_present(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name):
                '''set new_name_flag to false if name already exists'''
                new_name_flag = 0
        if ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CREATE_DP_PAGE):
            ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.CREATE_OEDP_TITLE)
        ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.ID_INPUT_NAME, oedp.name)
        ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.ID_INPUT_DESCRIPTION, oedp.description)
        s2l.select_from_list_by_value(i3sDeploymentPlanPage.ID_INPUT_OSTYPE_LIST, oedp.ostype)

        if (bp_flag == 1):
            if (oedp.oebuildplanuri != 'non-existing-bp'):
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_INPUT_BUILDPLAN_DROPDOWN)
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_INPUT_BUILDPLAN % oedp.oebuildplanuri)
            else:
                '''set exis_bp_flag to false if we provide non-existing BP uri'''
                exis_bp_flag = 0
                ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.OEDP_INPUT_BP_TEXTBOX, oedp.oebuildplanuri)
            sleep(5)

        if (gi_flag == 1):
            if (oedp.goldenimageuri != 'non-existing-gi'):
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_INPUT_GOLDENIMAGE_DROPDOWN)
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_INPUT_GOLDENIMAGE % oedp.goldenimageuri)
            else:
                '''set exis_gi_flag to false if we provide non-existing GI uri'''
                exis_gi_flag = 0
                ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.OEDP_INPUT_GI_TEXTBOX, oedp.goldenimageuri)
            sleep(5)

        if (oedp.button != 'cancel'):
            '''Creating oedeploymentplan clicking create/create plus'''
            if (oedp.button == 'create'):
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CREATE_DP_BUTTON)
            elif (oedp.button == 'create+'):
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CREATEPLUS_DP_BUTTON)
            sleep(5)

            if (gi_flag == 0) :
                if not ui_lib.wait_for_element(i3sDeploymentPlanPage.OEDP_BLANK_GI_URL_MESSAGE):
                    logger._warn("BLANK GI MESSAGE not found")
            if (bp_flag == 0) :
                if not ui_lib.wait_for_element(i3sDeploymentPlanPage.OEDP_BLANK_BP_URL_MESSAGE):
                    logger._warn("BLANK BP MESSAGE not found")

            ''' if we have provided non-existing BP uri and non-existing GI uri or non-existing GI uri and existing BP uri'''
            if ((exis_gi_flag == 0 and exis_bp_flag == 1) or (exis_gi_flag == 0 and exis_bp_flag == 0)) :
                try:
                    if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                        text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                        if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                            logger._warn('Blank error form')
                        elif (text != error_messages.OEDP_INVALID_GI_URL_MESSAGE):
                            logger._warn("Error message displayed  doesn't match the invalid golden image error message")
                            logger._log_to_console_and_log_file("Error message is" + str(text))
                    else:
                        logger._warn('no error form found')
                except:
                    logger._warn('no error form found')

            ''' if we have provided non-existing BP uri and existing GI uri'''
            if (exis_bp_flag == 0 and exis_gi_flag == 1):
                try:
                    if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                        text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                        if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                            logger._warn('Blank error form')
                        elif (text != error_messages.OEDP_INVALID_OEBP_URL_MESSAGE):
                            logger._warn("Error message displayed  doesn't match the invalid build plan error message")
                            logger._log_to_console("Error message is" + str(text))
                    else:
                        logger._warn('no error form found')
                except:
                    logger._warn('no error form found')

            if (name_flag == 0):
                if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_BLANK_NAME):
                    logger._warn("Blank name message not found")

            if (len(oedp.name) > MAX_CHAR):
                new_name_flag = 0

            if (desc_flag == 0):
                if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_BLANK_DESCRIPTION):
                    logger._warn("Blank description message not found")

            if (new_name_flag == 0):
                try:
                    if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                        text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                        if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                            logger._warn('Blank error form found')
                        elif (text != error_messages.OEDP_DUPLICATE_NAME_MESSAGE):
                            logger._warn("duplicate name error message is not displayed")
                            logger._log_to_console_and_log_file("Error message is" + str(text))
                except:
                       logger._warn('no error form found')

            if (special_char_flag == 0):
                try:
                    if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                        text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                        if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                            logger._warn('Blank error form')
                        elif (text != error_messages.OEDP_INVALID_INPUT_MESSAGE):
                           logger._warn("invalid name error message is not displayed")
                           logger._log_to_console_and_log_file("Error message is" + str(text))
                except:
                       logger._warn('no error form found')

            if (oedp.button == 'create'):
                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.CREATE_OEDP_TITLE):
                    return_to_create_dppage()
                    continue
                elif ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name):
                    logger._log_to_console_and_log_file("Created Deploymentplan %s succeedeed" % oedp.name)
                    continue
                else:

                    logger._warn("Creating Deploymentplan %s failed" % oedp.name)
                    continue
            if (oedp.button == 'create+'):
                if not ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.CREATE_OEDP_TITLE):
                    logger._warn("Failed to return to OEDP Create UI, post clicking Create plus")
                continue
                '''Cancelling creation of oedeploymentplan'''
        elif (oedp.button == 'cancel'):
            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CANCEL_DP_BUTTON)
            if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_CANCEL_CONFIRM_FORM):
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CANCEL_PROCEED_BUTTON)
            if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_PAGE_LABEL):
                logger._warn("Failed to navigate to OE Deployment page")
            continue
    return


def edit_oedeploymentplan(self, *editoedeploymentplan_obj):
    """ Select Edit DeploymentPalns - Edit OEDP for valid input-data
    check for error messages for invalid data
        Example:
        | Edit Deploymentplans     |     |
    """
    MAX_CHAR = 255
    s2l = ui_lib.get_s2l()
    """ Navigate to DeploymentPlan Page """
    if not s2l._is_element_present(i3sDeploymentPlanPage.ID_PAGE_LABEL):
        navigate()

    """ Retrieve data from datasheet """
    if type(editoedeploymentplan_obj) is test_data.DataObj:
            editoedeploymentplan_obj = [editoedeploymentplan_obj]
    elif type(editoedeploymentplan_obj) is tuple:
        editoedeploymentplan_obj = list(editoedeploymentplan_obj[0])
	newName_var = "newName"
	desc_var = "description"
	goldenimage_var = "goldenimageuri"
	oebuildplan_var = "oebuildplanuri"
	ostype_var = "ostype"
    for oedp in editoedeploymentplan_obj:
        ''' Below are flags to track invalid inputs'''
        name_flag = 1
        desc_flag = 1
        gi_flag = 1
        bp_flag = 1
        new_name_flag = 1
        special_char_flag = 1
        exis_gi_flag = 1
        exis_bp_flag = 1
        """ Before Editing check if the Deploymentplan exists """
        if s2l._page_contains(oedp.name):
            oedp_Obj = i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name

            ''' In the below code, flags are set/unset based on the validity of the input parameters'''
            if (hasattr(oedp, "newName")):
                if re.search('[^a-zA-Z_]', oedp.newName):
                   special_char_flag = 0
                if (oedp.newName == ""):
                    name_flag = 0
                    special_char_flag = 1

                """ Before Editing check if the Deploymentplan exists by the new name"""
                if s2l._is_element_present(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.newName):
                    ''' set new_name_flag to 0 if name already exists'''
                    new_name_flag = 0
            s2l.mouse_over(oedp_Obj)
            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name)
            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_BUTTON_ACTION)
            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_BUTTON_EDIT)
            ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_EDIT_OEDP_TITLE)

            if (hasattr(oedp, newName_var)):
                if (len(oedp.newName) > MAX_CHAR):
                    new_name_flag = 0
                ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.ID_EDIT_NAME, oedp.newName)
                sleep(5)

            if (hasattr(oedp, desc_var)):
                if (oedp.description == ""):
                    desc_flag = 0
                ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.ID_EDIT_DESCRIPTION, oedp.description)
                sleep(5)

            if (hasattr(oedp, goldenimage_var)):
                if (oedp.goldenimageuri == ""):
                    gi_flag = 0
                if gi_flag:
                    if (oedp.goldenimageuri != 'non-existing-gi'):
                        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_EDIT_GOLDENIMAGE_CLOSE)
                        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_INPUT_GOLDENIMAGE % oedp.goldenimageuri)
                    else:
                        '''set exis_gi_flag to false if we provide non-existing GI uri'''
                        exis_gi_flag = 0
                        ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.OEDP_EDIT_GI_TEXTBOX, oedp.goldenimageuri)
                else:
                    ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.OEDP_EDIT_GI_TEXTBOX, oedp.goldenimageuri)
                sleep(5)

            if (hasattr(oedp, oebuildplan_var)):
                if (oedp.oebuildplanuri == ""):
                    bp_flag = 0
                if bp_flag:
                    if (oedp.oebuildplanuri != 'non-existing-bp'):
                        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_EDIT_BUILDPLAN_CLOSE)
                        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_EDIT_BUILDPLAN % oedp.oebuildplanuri)
                    else:
                        '''set exis_bp_flag to false if we provide non-existing BP uri'''
                        exis_bp_flag = 0
                        ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.OEDP_EDIT_BP_TEXTBOX, oedp.oebuildplanuri)
                else:
                    ui_lib.wait_for_element_and_input_text(i3sDeploymentPlanPage.OEDP_EDIT_BP_TEXTBOX, oedp.oebuildplanuri)
                sleep(5)

            if (hasattr(oedp, ostype_var)):
                s2l.select_from_list_by_value(i3sDeploymentPlanPage.ID_EDIT_OSTYPE_LIST, oedp.ostype)

            if (oedp.button != 'cancel'):
                '''Editing an    oedeploymentplan'''
                if (oedp.button == 'edit'):
                    ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_EDIT_OK_BUTTON)
                    sleep(5)
                    if (hasattr(oedp, goldenimage_var) or hasattr(oedp, oebuildplan_var)):
                        if (gi_flag == 0):
                            if not ui_lib.wait_for_element(i3sDeploymentPlanPage.OEDP_BLANK_GI_URL_MESSAGE_EDIT):
                                logger._warn("Blank Gi edit error message not found")

                        if hasattr(oedp, oebuildplan_var):
                            if (bp_flag == 0):
                                if not ui_lib.wait_for_element(i3sDeploymentPlanPage.OEDP_BLANK_BP_URL_MESSAGE_EDIT):
                                    logger._warn("Blank BP edit error message not found")
                                    ''' if we have provided non-existing BP uri and non-existing GI uri or just non-existing GI uri and existing BP uri'''
                            elif ((exis_gi_flag == 0 and exis_bp_flag == 1) or (exis_gi_flag == 0 and exis_bp_flag == 0)):
                                try:
                                    if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                                        text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                                        if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                                            logger._warn('no error form found')
                                        elif (text != error_messages.OEDP_INVALID_GI_URL_EDIT_MESSAGE):
                                            logger._warn("Error message displayed  doesn't match the invalid golden image error message")
                                            logger._log_to_console_and_log_file("Error message is" + str(text))
                                except:
                                    logger._warn('no invalid golden image error form found')
                                ''' if we have provided non-existing BP uri and existing GI uri'''
                            elif (exis_bp_flag == 0 and exis_gi_flag == 1):
                                try:
                                    if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                                        text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                                        if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                                            logger._warn('your message')
                                        elif (text != error_messages.OEDP_INVALID_OEBP_URL_EDIT_MESSAGE):
                                            logger._warn("Error message displayed  doesn't match the invalid oebuildplan error message")
                                            logger._log_to_console_and_log_file("Error message is" + str(text))
                                except:
                                    logger._warn('no invalid oebuildplan error form found')
                            else:
                                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name)
                                if not ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_EDIT_BPURI_CHECK % oedp.oebuildplanuri, PerfConstants.SUCCESS_TIME):
                                    logger._warn("Failed to update with oebuildplan: %s" % oedp.oebuildplanuri)
                                else:
                                    logger._log_to_console_and_log_file("Updated oebuildplan to '%s'" % oedp.oebuildplanuri)
                        ''' if we have provided non-existing GI uri '''
                        if (exis_gi_flag == 0):
                            try:
                                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                                    text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                                    if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                                        logger._warn('no error form found')
                                    elif (text != error_messages.OEDP_INVALID_GI_URL_EDIT_MESSAGE):
                                        logger._warn("Error message displayed  doesn't match the invalid golden image error message")
                            except:
                                logger._warn('invalid golden image error form found')

                    if hasattr(oedp, goldenimage_var):
                       ''' if we have provided valid GI uri '''
                       if (gi_flag == 1 and exis_gi_flag == 1):
                            ''' Checking if goldenimageuri is updated'''
                            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name)
                            if not ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_EDIT_GIURI_CHECK % oedp.goldenimageuri, PerfConstants.SUCCESS_TIME):
                                logger._warn("Failed to update with goldenimage: %s" % oedp.goldenimageuri)
                            else:
                                logger._log_to_console_and_log_file("Updated goldenimage to '%s'" % oedp.goldenimageuri)

                    if hasattr(oedp, ostype_var):
                        ''' Checking if ostype is updated'''
                        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name)
                        if not ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_EDIT_OSTYPE_CHECK % oedp.ostype, PerfConstants.SUCCESS_TIME):
                            logger._warn("Failed to update with ostype: %s" % oedp.ostype)
                        else:
                            logger._log_to_console_and_log_file("Updated ostype to '%s'" % oedp.ostype)

                    if hasattr(oedp, newName_var):
                        if (name_flag == 0):
                            ''' If goldenimage name is NULL then throw error and continue to the next test scenario'''
                            if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_BLANK_NAME):
                                logger._warn("Blank name error message not found")
                            else:
                                logger._log_to_console_and_log_file("blank name error message found")
                        else:
                            if (special_char_flag == 1 and new_name_flag == 1):
                                if not ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.newName, PerfConstants.SUCCESS_TIME):
                                    logger._warn("Failed to update with newName: %s" % oedp.newName)
                                else:
                                    logger._log_to_console_and_log_file("Updated Name to '%s'" % oedp.newName)
                        if (new_name_flag == 0):
                            try:
                                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                                    text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                                    text1 = text.strip()
                                    logger._log_to_console_and_log_file("text1 is" + str(text1))
                                    if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                                        logger._warn('Duplicate name error form found')
                                    elif (text1 != error_messages.OEDP_DUPLICATE_NAME_EDIT_MESSAGE):
                                        logger._warn("Duplicate name edit error message is not displayed")
                                        logger._log_to_console("Error message is" + str(text))
                                else:
                                    logger._warn('No error form found')
                            except:
                                   logger._warn('no error form found')
                        if (special_char_flag == 0):
                            try:
                                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_ERROR_FORM):
                                    text = ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM)
                                    if len(ui_lib.get_text(i3sDeploymentPlanPage.ID_ERROR_FORM).strip()) == 0:
                                        logger._warn('no error form found')
                                    elif (text != error_messages.OEDP_INVALID_INPUT_EDIT_MESSAGE):
                                       logger._warn("invalid name error message is not displayed")
                                       logger._log_to_console_and_log_file("Error message is" + str(text))
                            except:
                                   logger._warn('invalid name error form found')

                    if hasattr(oedp, desc_var):
                        if (desc_flag == 0):
                            if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_BLANK_DESCRIPTION_EDIT):
                                logger._warn("Blank descriptionedit error message not found")
                        else:
                            ''' Checking if description is updated'''
                            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name)
                            if not ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_EDIT_DESC_CHECK % oedp.description):
                                logger._warn("Failed to update oedp %s description: %s" % (oedp.name, oedp.description))
                            else:
                                logger._log_to_console_and_log_file("Updated Description to '%s'" % oedp.description)

            elif (oedp.button == 'cancel'):
                '''Cancelling an oedeploymentplan edit operation'''
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_EDIT_CANCEL_BUTTON)
                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_CANCEL_CONFIRM_FORM):
                    ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CANCEL_PROCEED_BUTTON)
                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_PAGE_LABEL):
                    logger._log_to_console_and_log_file("returned successfully to OEDP UI")
                else:
                    logger._warn("Failed to return to OEDP UI post clicking cancel in Edit OEDP UI")
                continue

            '''Returning to OEDP UI after successful/failed edit operation'''
            if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_EDIT_OEDP_TITLE):
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_EDIT_CANCEL_BUTTON)
                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_CANCEL_CONFIRM_FORM):
                    ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CANCEL_PROCEED_BUTTON)
            elif ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_PAGE_LABEL):

                logger._log_to_console_and_log_file("returned successfully to OEDP UI")
            else:
                logger._warn("Failed to return to OEDP UI post clicking cancel in Edit OEDP UI")
                continue
        else:
            logger._warn("Failed to edit the deployment plan as the name provided does not exist on the OEDP UI page")
            continue
    return

def delete_oedeploymentplan(self, *deleteoedeploymentplan_obj):
    """ Delete DeploymentPlan
     Example:
        | remove deploymentplan      | ${oedpName}    |
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to DeploymentPlan Page """
    if not s2l._is_element_present(i3sDeploymentPlanPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(i3sDeploymentPlanPage.ID_DP_VISIBLE)

    """ Retrieve data from datasheet """
    if type(deleteoedeploymentplan_obj) is test_data.DataObj:
        deleteoedeploymentplan_obj = [deleteoedeploymentplan_obj]
    elif type(deleteoedeploymentplan_obj) is tuple:
        deleteoedeploymentplan_obj = list(deleteoedeploymentplan_obj[0])

    for oedp in deleteoedeploymentplan_obj:
        if s2l._page_contains(oedp.name):
            oedp_Obj = i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name
            s2l.mouse_over(oedp_Obj)
            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % oedp.name)
            ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_BUTTON_ACTION)
            if s2l._is_visible(i3sDeploymentPlanPage.ID_BUTTON_DELETE):
                logger._log_to_console_and_log_file("Remove DeploymentPlan '%s'" % oedp.name)
                ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_BUTTON_DELETE)
                if ui_lib.wait_for_element_visible(i3sDeploymentPlanPage.ID_DELETE_FORM):
                    if (oedp.button == "delete"):
                        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_YES_DELETE_BUTTON)
                    elif (oedp.button == "cancel"):
                        ui_lib.wait_for_element_and_click(i3sDeploymentPlanPage.ID_CANCEL_DELETE_BUTTON)
                        logger._log_to_console_and_log_file(" Deploymentplan '%s' not deleted as Cancel was chosen" % oedp.name)
                        continue
                else:
                    logger._warn("Form is not visible")
                    continue

                if ui_lib.wait_for_element_remove(i3sDeploymentPlanPage.ID_ELEMENT_DEPLOYMENTPLAN % str(oedp.name), PerfConstants.REMOVE_SERVER):
                    logger._log_to_console_and_log_file("Removed Deploymentplan '%s'" % oedp.name)
                else:
                    logger._warn("FAILED :: Deploymentplan can't be removed - '%s'" % oedp.name)
            else:
                logger._warn("'%s' Deploymentplan can't be deleted, delete option is not visible on page." % oedp.name)
        else:
            logger._warn("'%s' Deploymentplan not found in Deploymentplan page" % oedp.name)
            continue
    return











