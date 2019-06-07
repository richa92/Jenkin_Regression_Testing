""" planscripts UI """

from i3SLibrary.ui.general.base_elements import i3SBasePage
from i3SLibrary.ui.planscripts_elements import i3sPlanScriptPage
from i3SLibrary.ui.general import base_page
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from i3SLibrary.ui import ps_error_messages
import re

''' Maximum characters allowed'''
MAX_CHAR = 255


def navigate():
    """ Base navigate """
    base_page.navigate_base(
        i3sPlanScriptPage.ID_PAGE_LABEL,
        i3SBasePage.ID_MENU_LINK_PLAN_SCRIPTS,
        "css=span.hp-page-item-count")
    if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to Plan Script page", True)


def str_compare(str1, str2):
    """ Compare 2 strings """
    str1_list = str1.split()
    str2_list = str2.split()
    # logger._warn("The actual error mesage is" +str(str1_list))
    # logger._warn("The expected error message is " +str(str2_list))
    return cmp(str1_list, str2_list)


def return_to_create_pspage():
    """ Return to the create PS page """
    if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_CANCEL_PS_BUTTON):
        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CANCEL_PS_BUTTON)
        if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_CANCEL_CONFIRMATION_FORM):  # Wait for form to visible
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CANCEL_BUTTON_YES)
            if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_PAGE_LABEL):
                ui_lib.fail_test("Failed to navigate to plan script page", True)
    return


def return_to_pspage():
    """ Return to the PS page """
    ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CANCEL_PS_BUTTON)

    if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to plan script page", True)
    return


def create_planscript(*createplanscript_obj):
    """
     Select Create planscripts
     Example:
        | Select create-planscripts     |     |
    """
    s2l = ui_lib.get_s2l()
    # Navigate to Planscript Page
    if not s2l._is_element_present(i3sPlanScriptPage.ID_PAGE_LABEL):
        navigate()
    # Retrieve data from data-sheet

    if type(createplanscript_obj) is test_data.DataObj:
        createplanscript_obj = [createplanscript_obj]

    elif type(createplanscript_obj) is tuple:
        createplanscript_obj = list(createplanscript_obj[0])

    for ps in createplanscript_obj:
        # logger._log_to_console_and_log_file("inside for loop")
        # Below are flags to track invalid inputs
        name_flag = 1
        desc_flag = 1
        content_flag = 1
        dup_name_flag = 0
        special_char_flag = 0
        # logger._log_to_console_and_log_file("ps is " + str(ps.name))
        # In the below code, flags are set/unset based on the validity of the input parameters
        if ps.name == "":
            name_flag = 0

        if ps.description == "":
            desc_flag = 0

        if ps.content == "":
            content_flag = 0

        if re.search('[^a-zA-Z_]', ps.name) and name_flag:
            special_char_flag = 1
        # Before Adding check whether the plan-script exists

        if name_flag:
            # logger._log_to_console_and_log_file("inside name field")
            if s2l._is_element_present(i3sPlanScriptPage.ID_ELEMENT_PS % ps.name):
                # set dup_name_flag to true if name already exists
                dup_name_flag = 1

        if ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CREATE_PS):
            logger._log_to_console_and_log_file("inside create page")

        if not ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_CREATE_PS_PAGE):
            logger._warn("Failed to return to PS Create UI")
            continue

        ui_lib.wait_for_element_and_input_text(i3sPlanScriptPage.ID_INPUT_NAME, ps.name)
        s2l.select_from_list_by_value(i3sPlanScriptPage.ID_PLAN_TYPE_LIST, ps.plantype)
        s2l.select_from_list_by_value(i3sPlanScriptPage.ID_OS_TYPE_LIST, ps.ostype)

        if desc_flag:
            # logger._log_to_console_and_log_file("inside desc field")
            ui_lib.wait_for_element_and_input_text(i3sPlanScriptPage.ID_INPUT_DESCRIPTION, ps.description)

        if content_flag:
            # logger._log_to_console_and_log_file("inside content field")
            ui_lib.wait_for_element_and_input_text(i3sPlanScriptPage.ID_PS_CONTENT, ps.content)

        # logger._log_to_console_and_log_file("button is" + str(ps.button))

        if ps.button != 'cancel':
            if ps.button == 'create':
                # logger._log_to_console_and_log_file("inside create loop")
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CREATE_PS_BUTTON)

            elif ps.button == 'create+':
                # logger._log_to_console_and_log_file("inside create++ loop")
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CREATEPLUS_PS_BUTTON)
            # checking for name, desc blank fields
            if name_flag == 0:
                # logger._log_to_console_and_log_file("inside blank name")
                if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_NAME):
                    logger._warn("ID_BLANK_NAME not found")
            # checking for blank fields or more than allowed chars
            if desc_flag == 0:
                # logger._log_to_console_and_log_file("inside blank desc")
                if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_DESCRIPTION):
                    logger._warn("Invalid description error message not found")

            if content_flag == 0:
                # logger._log_to_console_and_log_file("inside blank content")

                if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_CONTENT):
                    logger._warn("ID_BLANK_CONTENT msg not found")

            if dup_name_flag:
                # logger._log_to_console_and_log_file("inside dup name flag loop")
                try:
                    if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ERROR_FORM):
                        # error message from the UI is uicode text.
                        actual_err_msg = str(ui_lib.get_text(i3sPlanScriptPage.ID_ERROR_FORM))
                        expected_err_msg = ps_error_messages.PS_DUPLICATE_NAME_MESSAGE[0]

                        if len(actual_err_msg.strip()) == 0:
                            logger._warn('no error form found')

                        elif str_compare(actual_err_msg, expected_err_msg):
                            logger._warn("invalid name error message is not as per expectation")
                    else:
                        logger._warn('no error form found')
                except:
                    logger._warn('no error form found')

            if special_char_flag:
                # logger._log_to_console_and_log_file("inside special char flag loop")

                try:
                    if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ERROR_FORM):
                        # error message from the UI is uicode text.
                        actual_err_msg = str(ui_lib.get_text(i3sPlanScriptPage.ID_ERROR_FORM))
                        expected_err_msg = ps_error_messages.PS_INVALID_INPUT_MESSAGE[0]

                        if len(actual_err_msg.strip()) == 0:
                            logger._warn('no error form found')
                        elif str_compare(actual_err_msg, expected_err_msg):
                            logger._warn("invalid name error message is not as per expectation")
                    else:
                        logger._warn('no error form found')
                except:
                    logger._warn('no error form found')

            if ps.button == 'create':

                if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_CREATE_PS_TITLE):
                    # logger._log_to_console_and_log_file("Opened PS UI create")
                    return_to_create_pspage()
                    continue

                elif ui_lib.wait_for_element(i3sPlanScriptPage.ID_ELEMENT_PS % ps.name):
                    logger._log_to_console_and_log_file("planscript '%s' created successfully" % ps.name)
                    continue

                else:
                    logger._warn("Creating planscript %s failed" % ps.name)
                    continue

            if ps.button == 'create+':
                # logger._log_to_console_and_log_file("inside create+ flag loop")
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CREATEPLUS_PS_BUTTON)
                logging._log_to_console_and_log_file("\nCreating planscript please wait ...\n")

                # for create+ the page goes back remains in PS create page after success of PS creation
                if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_CREATE_PS_TITLE):
                    # logger._log_to_console_and_log_file("In PS Create UI")
                    continue

                else:
                    logger._warn("Failed to return to PS Create UI")
                    continue

            continue

        elif ps.button == 'cancel':
            # logger._log_to_console_and_log_file("inside cancel flag loop")
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CANCEL_PS_BUTTON)

            if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_CANCEL_CONFIRMATION_FORM):
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CANCEL_BUTTON_YES)

            if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_PAGE_LABEL):
                logger._warn("Failed to navigate to Planscript page")

            continue

    return


def edit_planscript(*editplanscript_obj):
    """
    Select Edit Planscript
        Example:
        | Edit Planscript     |     |
    """
    s2l = ui_lib.get_s2l()

    """ Navigate to PlanScript Page """
    if not s2l._is_element_present(i3sPlanScriptPage.ID_PAGE_LABEL):
        navigate()

    """ Retrieve data from datasheet """
    if type(editplanscript_obj) is test_data.DataObj:
        editplanscript_obj = [editplanscript_obj]

    elif type(editplanscript_obj) is tuple:
        editplanscript_obj = list(editplanscript_obj[0])
    newName_var = "newName"
    desc_var = "description"
    content_var = "content"

    for ps in editplanscript_obj:

        if s2l._page_contains(ps.name):
            ps_Obj = i3sPlanScriptPage.ID_ELEMENT_PS % ps.name
            s2l.mouse_over(ps_Obj)
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_ELEMENT_PS % ps.name)
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_BUTTON_ACTION)
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_BUTTON_EDIT)
        if not ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_EDIT_PS_TITLE):
            logger._warn("Failed to navigate to Edit page")
            continue

            ''' Below are flags to track invalid inputs'''
            name_flag = 1
            desc_flag = 1
            content_flag = 1
            dup_name_flag = 0
            special_char_flag = 1

            ''' In the below code, flags are set/unset based on the validity of the input parameters'''
            if hasattr(ps, newName_var):
                if re.search('^[a-zA-Z_]', ps.newName):
                    special_char_flag = 0

                if ps.newName == "":
                    name_flag = 0

                """ Before Adding check whether planscript exists """
                if name_flag:

                    if s2l._is_element_present(i3sPlanScriptPage.ID_ELEMENT_PS % ps.newName):
                        ''' set dup_name_flag to true if name already exists'''
                        dup_name_flag = 1
                ui_lib.wait_for_element_and_input_text(i3sPlanScriptPage.ID_EDIT_NAME, ps.newName)

            if hasattr(ps, desc_var):
                if ps.description == "":
                    desc_flag = 0
                ui_lib.wait_for_element_and_input_text(i3sPlanScriptPage.ID_EDIT_DESCRIPTION, ps.description)

            if hasattr(ps, content_var):
                if ps.content == "":
                    content_flag = 0
                ui_lib.wait_for_element_and_input_text(i3sPlanScriptPage.ID_EDIT_CONTENT, ps.content)

            if ps.button == 'edit':
                # logger._log_to_console_and_log_file("inside edit loop")
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_OK_BUTTON)

                if hasattr(ps, "newName"):
                    if name_flag == 0 and desc_flag == 0 and content_flag == 0:
                        ''' If planscript name is NULL then throw error and continue to the next test scenario'''
                        # logger._log_to_console_and_log_file("inside blank name, description and content")

                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_NAME):
                            logger._warn("ID_BLANK_NAME not found")

                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)
                        '''checking for only blank name error message'''

                    elif name_flag == 0 and desc_flag == 1 and content_flag == 1:
                        ''' If planscript name is NULL then throw error and continue to the next test scenario'''
                        # logger._log_to_console_and_log_file("inside blank name")

                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_NAME):
                            logger._warn("ID_BLANK_NAME not found")
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)

                    elif name_flag == 0 and desc_flag == 1 and content_flag == 1 and dup_name_flag == 0 and special_char_flag == 0 and len(ps.name) < MAX_CHAR and len(ps.description) < 1000:
                        # logger._log_to_console_and_log_file("inside check for valid name & description")
                        if not ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ELEMENT_PS % ps.newName, PerfConstants.SUCCESS_TIME):
                            logger._warn("Failed to update with newName: %s" % ps.newName)
                        else:
                            logger._log_to_console_and_log_file("Updated Name to '%s'" % ps.newName)
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_EDIT_DESC_CHECK % ps.description):
                            logger._warn("Failed to update ps %s description: %s" % (ps.name, ps.description))

                        else:
                            logger._log_to_console_and_log_file("Updated Description to '%s'" % ps.description)

                elif hasattr(ps, newName_var):
                    # logger._log_to_console_and_log_file("inside name attribute loop")

                    if dup_name_flag:
                        # logger._log_to_console_and_log_file("inside dup name flag loop")
                        try:
                            if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ERROR_FORM):
                                # error message from the UI is uicode text.
                                actual_err_msg = str(ui_lib.get_text(i3sPlanScriptPage.ID_ERROR_FORM))
                                expected_err_msg = ps_error_messages.PS_INVALID_INPUT_MESSAGE[0]
                                if len(actual_err_msg.strip()) == 0:
                                    logger._warn('no error form found')
                                elif str_compare(actual_err_msg, expected_err_msg):
                                    logger._warn("invalid name error message is not as per expectation")
                            else:
                                logger._warn('no error form found')
                        except:
                            logger._warn('no error form found')

                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)

                    elif special_char_flag:
                        # logger._log_to_console_and_log_file("inside special char loop")
                        try:
                            if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ERROR_FORM):
                                # error message from the UI is unicode text.
                                actual_err_msg = str(ui_lib.get_text(i3sPlanScriptPage.ID_ERROR_FORM))
                                expected_err_msg = ps_error_messages.PS_INVALID_INPUT_EDIT_MESSAGE[0]
                                if len(actual_err_msg.strip()) == 0:
                                    logger._warn('no error form found')
                                elif str_compare(actual_err_msg, expected_err_msg):
                                    logger._warn("invalid name error message is not as per expectation")
                            else:
                                logger._warn('no error form found')
                        except:
                            logger._warn('no error form found')
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)

                    elif len(ps.newName) > MAX_CHAR:
                        # logger._log_to_console_and_log_file("inside name greater than 255 chars")
                        # logger._log_to_console_and_log_file("the content is %s" % (max_char))
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.PS_INVALID_UPDATE_NAME_MESSAGE):
                            logger._warn("PS_INVALID_UPDATE_NAME_MESSAGE not found")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.PS_INVALID_NAME_RESOLUTION):
                            logger._warn("PS_INVALID_NAME_RESOLUTION not found")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.PS_INVALID_NAME_DETAILS):
                            logger._warn("PS_INVALID_NAME_DETAILS not found")
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)

                    elif name_flag == 0:
                        # logger._log_to_console_and_log_file("inside new name update check loop")
                        ''' If planscript name is NULL then throw error and continue to the next test scenario'''
                        # logger._log_to_console_and_log_file("inside blank name")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_NAME):
                            logger._warn("ID_BLANK_NAME not found")
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)

                    else:
                        # logger._log_to_console_and_log_file("inside new name update check loop")
                        if not ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ELEMENT_PS % ps.newName, PerfConstants.SUCCESS_TIME):
                            logger._warn("Failed to update with newName: %s" % ps.newName)
                        else:
                            logger._log_to_console_and_log_file("Updated Name to '%s'" % ps.newName)

                elif hasattr(ps, desc_var):
                    if desc_flag == 0:
                        ''' If planscript desc is NULL then throw error and continue to the next test scenario'''
                        # logger._log_to_console_and_log_file("inside blank desc")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_EDIT_BLANK_DESCRIPTION):
                            logger._warn("ID_BLANK_DESCRIPTION not found")
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)
                    else:
                        # logger._log_to_console_and_log_file("inside new description update check loop")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_EDIT_DESC_CHECK % ps.description):
                            logger._warn("Failed to update ps %s description: %s" % (ps.name, ps.description))
                        else:
                            logger._log_to_console_and_log_file("Updated Description to '%s'" % ps.description)

                elif hasattr(ps, content_var):
                    if content_flag == 0:
                        ''' If goldenimage desc is NULL then throw error and continue to the next test scenario'''
                        # logger._log_to_console_and_log_file("inside blank desc")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_CONTENT):
                            logger._warn("ID_BLANK_DESCRIPTION not found")
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)
                    else:
                        # logger._log_to_console_and_log_file("inside new content update check loop")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_EDIT_CONTENT_CHECK % ps.content):
                            logger._warn("Failed to update ps %s with content: %s" % (ps.name, ps.content))
                        else:
                            logger._log_to_console_and_log_file("Updated content to '%s'" % ps.content)

            elif ps.button == 'cancel':
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)
                if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_PAGE_LABEL):
                    logger._log_to_console_and_log_file("returned successfully to PS UI")
                else:
                    logger._warn("Failed to return to PS UI post clicking cancel in Edit PS UI")
                continue

            if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_EDIT_PS_TITLE):
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_EDIT_CANCEL_BUTTON)
                if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_CANCEL_CONFIRMATION_FORM):
                    ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_CANCEL_BUTTON_YES)
            elif ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_PAGE_LABEL):

                logger._log_to_console_and_log_file("returned successfully to Planscript UI")
            else:
                logger._warn("Failed to return to PS UI post clicking cancel in Edit Planscript UI")

                continue

        else:
            logger._warn("Failed to edit the plan script as the name provided does not exist on the PS UI page")
            continue
    return


def copy_planscript(*copyplanscript_obj):
    """ Copy  PlanScript
     Example:
        | Copy planscript      | ${copyName}    |
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to PlanScript Page """
    if not s2l._is_element_present(i3sPlanScriptPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(i3sPlanScriptPage.ID_PS_VISIBLE)

    """ Retrieve data from datasheet """
    if type(copyplanscript_obj) is test_data.DataObj:
        copyplanscript_obj = [copyplanscript_obj]
    elif type(copyplanscript_obj) is tuple:
        copyplanscript_obj = list(copyplanscript_obj[0])
    copyName_var = "copyName"

    for ps in copyplanscript_obj:
        if s2l._page_contains(ps.name):
            ps_Obj = i3sPlanScriptPage.ID_ELEMENT_PS % ps.name
            s2l.mouse_over(ps_Obj)
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_ELEMENT_PS % ps.name)
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_BUTTON_ACTION)
            if s2l._is_visible(i3sPlanScriptPage.ID_BUTTON_COPY):
                # logger._log_to_console_and_log_file("Copy PlanScript '%s'" % ps.name)
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_BUTTON_COPY)

            ''' Below are flags to track invalid inputs'''
            name_flag = 1
            dup_name_flag = 0
            special_char_flag = 1

            ''' In the below code, flags are set/unset based on the validity of the input parameters'''

            if hasattr(ps, copyName_var):
                if re.search('^[a-zA-Z_]', ps.copyName):
                    special_char_flag = 0
                if ps.copyName == "":
                    name_flag = 0

                """ Before Adding check for the planscript exists """
                if name_flag:
                    if s2l._is_element_present(i3sPlanScriptPage.ID_ELEMENT_PS % ps.copyName):
                        ''' set dup_name_flag to true if name already exists'''
                        dup_name_flag = 1

                if ps.button == "copy":
                    ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_COPY_FORM)
                    ui_lib.wait_for_element_and_input_text(i3sPlanScriptPage.ID_EDIT_COPY_NAME, ps.copyName)
                    ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_COPY_OK_BUTTON)

                    '''checking for only blank name error message'''
                    if name_flag == 0:
                        # logger._log_to_console_and_log_file("inside blank name")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.ID_BLANK_NAME):
                            logger._warn("ID_BLANK_NAME not found")
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_COPY_CANCEL_BUTTON)

                    elif dup_name_flag:
                        # logger._log_to_console_and_log_file("inside dup name flag loop")
                        try:
                            if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ERROR_FORM):
                                # error message from the UI is uicode text.
                                actual_err_msg = str(ui_lib.get_text(i3sPlanScriptPage.ID_COPY_ERROR_FORM))
                                expected_err_msg = ps_error_messages.PS_DUPLICATE_COPY_MESSAGE[0]
                                if len(actual_err_msg.strip()) == 0:
                                    logger._warn('no error form found')
                                elif str_compare(actual_err_msg, expected_err_msg):
                                    logger._warn("invalid name error message is not as per expectation")
                            else:
                                logger._warn('no error form found')
                        except:
                            logger._warn('no error form found')
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_COPY_CANCEL_BUTTON)

                    elif special_char_flag:
                        # logger._log_to_console_and_log_file("inside special char loop")
                        try:
                            if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ERROR_FORM):
                                # error message from the UI is uicode text.
                                logger._warn('no error form found')
                                actual_err_msg = str(ui_lib.get_text(i3sPlanScriptPage.ID_COPY_ERROR_FORM))
                                expected_err_msg = ps_error_messages.PS_INVALID_COPY_MESSAGE[0]
                                if len(actual_err_msg.strip()) == 0:
                                    logger._warn('no error form found')
                                elif str_compare(actual_err_msg, expected_err_msg):
                                    logger._warn("invalid name error message is not as per expectation")
                            else:
                                logger._warn('no error form found')
                        except:
                            logger._warn('no error form found')
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_COPY_CANCEL_BUTTON)

                    elif len(ps.copyName) > MAX_CHAR:
                        # logger._log_to_console_and_log_file("inside name greater than 255 chars")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.PS_INVALID_NAME_COPY_MESSAGE):
                            logger._warn("ps_INVALID_UPDATE_NAME_MESSAGE not found")
                        if not ui_lib.wait_for_element(i3sPlanScriptPage.PS_INVALID_NAME_RESOLUTION):
                            logger._warn("ps_INVALID_NAME_RESOLUTION not found")
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_COPY_CANCEL_BUTTON)

                    else:
                        # logger._log_to_console_and_log_file("inside copy name update check loop")

                        if not ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ELEMENT_PS % ps.copyName, PerfConstants.SUCCESS_TIME):
                            logger._warn("Failed to copy with copyName: %s" % ps.copyName)

                        else:
                            logger._log_to_console_and_log_file("Copy Name to '%s'" % ps.copyName)
                        continue

                elif ps.button == "cancel":
                    ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_COPY_CANCEL_BUTTON)
                    # logger._log_to_console_and_log_file(" PlanScript '%s' not copied as Cancel was chosen" % ps.name)
                    continue
            else:
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_COPY_OK_BUTTON)
                copy_name = ps.name + str('_copy')

                if not ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_ELEMENT_PS % copy_name, PerfConstants.SUCCESS_TIME):
                    logger._warn("Failed to copy with copyName: %s" % copy_name)
                else:
                    logger._log_to_console_and_log_file("Copy Name to '%s'" % copy_name)
                continue

        else:
            logger._warn("'%s' PlanScript not found in planscript page" % ps.name)
            continue
    return


def delete_planscript(*deleteplanscript_obj):
    """ Delete PlanScript
     Example:
        | remove planscript      | ${psName}    |
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to Plan script Page """
    if not s2l._is_element_present(i3sPlanScriptPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(i3sPlanScriptPage.ID_PS_VISIBLE)

    """ Retrieve data from datasheet """
    if type(deleteplanscript_obj) is test_data.DataObj:
        deleteplanscript_obj = [deleteplanscript_obj]
    elif type(deleteplanscript_obj) is tuple:
        deleteplanscript_obj = list(deleteplanscript_obj[0])

    for ps in deleteplanscript_obj:
        if s2l._is_element_present(i3sPlanScriptPage.ID_ELEMENT_PS % ps.name):
            # logger._log_to_console_and_log_file("Remove Planscript '%s'" % ps.name)
            ps_obj = i3sPlanScriptPage.ID_ELEMENT_PS % ps.name
            s2l.mouse_over(ps_obj)
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_ELEMENT_PS % ps.name)
            ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_BUTTON_ACTION)
            if s2l._is_visible(i3sPlanScriptPage.ID_ACTION_DELETE_BUTTON):
                # logger._log_to_console_and_log_file("Remove Planscript '%s'" % ps.name)
                ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_ACTION_DELETE_BUTTON)

                if ui_lib.wait_for_element_visible(i3sPlanScriptPage.ID_DELETE_FORM):  # Wait for form to be visible
                    if ps.button == "delete":
                        ret_status = ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_DELETE_BUTTON_YES)
                        print ret_status
                        # logger._log_to_console_and_log_file(ret_status)
                        if ret_status == "False":
                            logger._log_to_console_and_log_file("Plan script '%s' not deleted " % ps.name)
                    elif ps.button == "cancel":
                        ui_lib.wait_for_element_and_click(i3sPlanScriptPage.ID_DELETE_BUTTON_CANCEL)
                        # logger._log_to_console_and_log_file("Plan script '%s' not deleted as Cancel was chosen" % ps.name)
                        continue
                else:
                    logger._warn("Form is not visible")
                    continue

                # validating Plan script removal
                if ui_lib.wait_for_element_remove(i3sPlanScriptPage.ID_ELEMENT_PS % str(ps.name), PerfConstants.REMOVE_SERVER):
                    logger._log_to_console_and_log_file("Removed Plan script '%s'" % ps.name)
                else:
                    logger._warn("FAILED :: Plan script can't be removed - '%s'" % ps.name)

            else:
                logger._warn("'%s' Plan script can't be deleted, delete option is not visible on page." % ps.name)
        else:
            logger._warn("'%s' Plan script not found in Plan script page" % ps.name)
            continue
    return
