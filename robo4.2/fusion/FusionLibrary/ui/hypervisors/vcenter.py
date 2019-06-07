# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
""" Fusion  vCenter UI page."""


from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.hypervisors.vcenter_elements import FusionvCenterPage


def navigate():
    base_page.navigate_base(FusionvCenterPage.ID_PAGE_LABEL,
                            FusionvCenterPage.ID_MENU_LINK_VCENTERS,
                            "css=span.hp-page-item-count")


def add_vcenter(*vcen_obj):
    """ add_vCenter function to add vCenter to the appliance

    Example:
        | `Add vCenter`      |     @{vcen_obj}    |

    """

    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionvCenterPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(vcen_obj, test_data.DataObj):
        vcen_obj = [vcen_obj]
    elif isinstance(vcen_obj, tuple):
        vcen_obj = list(vcen_obj[0])

    # variable to hold the no of vCenters
    count = 0
    vcenterpools = []
    vcenterpool_list = [ui_lib.get_webelement_attribute("text", s) for s in s2l._element_find(FusionvCenterPage.ID_VCENTER_LIST_NAMES, False, False)]

    for pool in vcen_obj:
        logger._log_to_console_and_log_file("Verifying vCenters if already exists...")
        if pool in vcenterpool_list:
            logger._warn("vcenter'{0}' already exists".format(pool.name))
        else:
            vcenterpools.append(pool)

    if len(vcenterpools) == 0:
        logger._warn("All vcenters passed from data sheet are already existing..")
        return True
    else:
        logger._log_to_console_and_log_file("vcenters are in a list to be added")

    """ Loop to add vCenter """
    for vcenter in vcenterpools:
        logger._log_to_console_and_log_file("Adding vcenter: '%s'" % vcenter.name)
        if s2l._is_element_present(FusionvCenterPage.ID_VCENTER_BUTTON):
            ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_VCENTER_BUTTON)

            # Check whether mandatory fields are empty or not
            if (vcenter.hostname == "" or vcenter.username == "" or vcenter.password == ""):
                logger._warn("Mandatory fields for adding vcenter can't be empty")
                continue
            else:
                logger._log_to_console_and_log_file("Typing vcenter ip address..")
                ui_lib.wait_for_element_and_input_text(FusionvCenterPage.ID_INPUT_VCENTER_IP_ADDRESS, vcenter.hostname)
                logger._log_to_console_and_log_file("Typing user name..")
                ui_lib.wait_for_element_and_input_text(FusionvCenterPage.ID_INPUT_USERNAME, vcenter.username)
                logger._log_to_console_and_log_file("Typing password..")
                ui_lib.wait_for_element_and_input_text(FusionvCenterPage.ID_INPUT_PASSWORD, vcenter.password)

            ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_BTN_VCENTER_ADD)
            # if add vCenter fails,below script will capture the error msg and display to console
            if(ui_lib.wait_for_element(FusionvCenterPage.ID_ADD_VCENTER_ERR_MSG, PerfConstants.DEFAULT_SYNC_TIME * 2)):
                logger._warn("Unable to add vcenter: '%s'" % vcenter.name)
                msgText2 = ui_lib.get_text(FusionvCenterPage.ID_ADD_VCENTER_ERR_DETAILS)
                logger._warn(msgText2)
                continue

            # verifying vCenter is added and displayed in UI
            ui_lib.wait_for_element(FusionvCenterPage.ID_VCENTER_LIST, PerfConstants.DEFAULT_SYNC_TIME * 2)
            s2l.wait_until_page_contains_element(FusionvCenterPage.ID_ELEMENT_VCENTER % vcenter.name, PerfConstants.ADD_VCENTER_TIME)
            logger._log_to_console_and_log_file("vcenter  %s is added Successfully and it is available in vCenter List" % vcenter.name)

            # validating vCenter is added or not
            logger._log_to_console_and_log_file("Validating vCenter %s" % vcenter.name)
            logger._log_to_console_and_log_file("Clicking on Activity button")
            ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ACTIVITY_VCENTER)
            if ui_lib.wait_for_element(FusionvCenterPage.ID_ELEMENT_ACTIVITY % vcenter.name):
                if ui_lib.wait_for_element(FusionvCenterPage.ID_ACTIVITY_ADD_STATUS_OK % vcenter.name, PerfConstants.DEFAULT_SYNC_TIME * 2):
                    logger._log_to_console_and_log_file("vCenter  %s added successfully" % vcenter.name)
                    count = count + 1
                elif ui_lib.wait_for_element(FusionvCenterPage.ID_ACTIVITY_STATUS_WARNING, PerfConstants.DEFAULT_SYNC_TIME * 2):
                    logger._warn("vCenter %s is added with warning" % vcenter.name)
                else:
                    logger._warn("Failed to add vcenter %s" % vcenter.name)
            ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ACTIVITY_VCENTER)

        else:
            logger._warn("Failed to open add vcenter page")

    """ once all the vCenters are added , matching the count with the vCenters length """
    if len(vcenterpools) == count:
        logger._log_to_console_and_log_file("SUCCESS : Added all the vCenters to the Fusion Appliance")
        return True
    else:
        logger._warn("FAILURE : Not able to add all vCenters as mentioned in the data file. ")
        return False


def edit_vcenter_server_properties(*vcen_obj):
    """ edit vcenter

        Example:
        | `edit vCenter Server Property`      | @{vcen_obj}    |
    """

    """ Navigate to vCenter Page """
    if not ui_lib.wait_for_element(FusionvCenterPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(vcen_obj, test_data.DataObj):
        vcen_obj = [vcen_obj]
    elif isinstance(vcen_obj, tuple):
        vcen_obj = list(vcen_obj[0])

    """ Function call to Edit the vCenter server properties"""
    for vcenter in vcen_obj:
        logger._log_to_console_and_log_file("Selecting Vcenter: '{0}".format(vcenter.name))
        if ui_lib.wait_for_element_visible(FusionvCenterPage.ID_ELEMENT_VCENTER % vcenter.name):
            ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_VCENTER % vcenter.name)
        else:
            ui_lib.fail_test("Fail: Vcenter {0} is not present in Vcenter list".format(vcenter.name))

        logger._log_to_console_and_log_file("Editing Vcenter: '{0}".format(vcenter.name))
        ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_MENU_ACTION_EDIT)
        if not ui_lib.wait_for_element_visible(FusionvCenterPage.ID_ELEMENT_EDIT_LABEL % vcenter.name, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.fail_test("Unable to navigate to Edit page")

        if vcenter.has_property("password") and vcenter.password != '':
            ui_lib.wait_for_element_and_input_text(FusionvCenterPage.ID_INPUT_PASSWORD, vcenter.password)

        """ depending on type, edit values to screen fields from data file """

        if vcenter.has_property('type') and vcenter.type != "":
            if vcenter.type.lower() == "distributed":
                logger._log_to_console_and_log_file("Selecting vSwitch type...")
                ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_VSWITCH_TYPE)
                ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_SELECT_VSWITCH_TYPE % vcenter.type)
                ui_lib.wait_for_element_visible(FusionvCenterPage.ID_ELEMENT_VSWITCH_VERSION)
                if vcenter.has_property("vswitch_version") and vcenter.type != '':
                    logger._log_to_console_and_log_file("Selecting vswitch version...")
                    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_VSWITCH_VERSION)
                    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_SELECT_VSWITCH_VERSION % vcenter.vswitch_version)

                if(vcenter.has_property("vswitch_network")):
                    logger._log_to_console_and_log_file("Selecting vswitch network...")
                    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_VSWITCH_NETWORK)
                    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_SELECT_VSWITCH_NETWORK % vcenter.vswitch_network)
            else:
                logger._log_to_console_and_log_file("By default Standard switch is selected...")
                ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_VSWITCH_TYPE)
                ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_SELECT_VSWITCH_TYPE % vcenter.type)

        """ Example: default UI value is taken for writing xpath and the script is validating with input data and exist value in script"""

        if (vcenter.has_property('vmotion') and vcenter.vmotion != ""):
            logger._log_to_console_and_log_file("Selecting vSwitch vMotion...")
            status = ui_lib.wait_for_element_visible(FusionvCenterPage.ID_ELEMENT_VSWITCH_VMOTION)
            if vcenter.vmotion.lower() == "disabled" and status:
                ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_VSWITCH_VMOTION_TOGGLE)
        if (vcenter.has_property('resource_scheduler') and vcenter.resource_scheduler != ""):
            logger._log_to_console_and_log_file("Selecting vSwitch resource scheduler...")
            status = ui_lib.wait_for_element_visible(FusionvCenterPage.ID_ELEMENT_RESOURCE_SCHEDULER)
            if vcenter.resource_scheduler.lower() == "disabled" and status:
                ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_RESOURCE_SCHEDULER_TOGGLE)
        if(vcenter.has_property('availability') and vcenter.availability != ""):
            logger._log_to_console_and_log_file("Selecting vSwitch high availability...")
            status = ui_lib.wait_for_element_visible(FusionvCenterPage.ID_ELEMENT_HA)
            if vcenter.availability.lower() == "enabled" and status:
                ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_HA_TOGGLE)
    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ELEMENT_OK_BUTTON)

    # validating vCenter is added or not
    logger._log_to_console_and_log_file("Validating vCenter %s" % vcenter.name)
    logger._log_to_console_and_log_file("Clicking on Activity button")
    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ACTIVITY_VCENTER)
    if ui_lib.wait_for_element(FusionvCenterPage.ID_ELEMENT_ACTIVITY % vcenter.name):
        if ui_lib.wait_for_element(FusionvCenterPage.ID_ACTIVITY_UPDATE_STATUS_OK % vcenter.name, PerfConstants.DEFAULT_SYNC_TIME * 2):
            logger._log_to_console_and_log_file("vCenter  %s edited successfully" % vcenter.name)
        else:
            logger._warn("Failed to Edit vcenter %s" % vcenter.name)
    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_ACTIVITY_VCENTER)
    return True


def delete_all_vcenters():
    """ Delete all vCenters from appliance """

    """Example:
        | `delete vCenter `    """

    s2l = ui_lib.get_s2l()

    """ Navigate to vCenter Page """
    if not ui_lib.wait_for_element(FusionvCenterPage.ID_PAGE_LABEL):
        navigate()

    count = 0
    ui_lib.wait_for_element(FusionvCenterPage.ID_VCENTER_LIST)
    vCenter_list = [ui_lib.get_webelement_attribute("text", el) for el in s2l._element_find(FusionvCenterPage.ID_VCENTER_LIST_NAMES, False, False)]

    for vcenter in vCenter_list:
        logger._log_to_console_and_log_file("Deleting vCenter %s" % vcenter)
        if delete_vCenter(vcenter):
            count = count + 1

    if len(vCenter_list) == count:
        logger._log_to_console_and_log_file("SUCCESS: All vCenters are removed successfully")
        return True
    else:
        logger._log_to_console_and_log_file("FAIL: Failed to remove few or all vCenters")
        return False


def delete_vCenter(vcen_name):
    """ delete vcenter

        Example:
        | `delete vCenter `      | ${vcen_name}    |
    """

    """ Navigate to vcenter Page """

    if not ui_lib.wait_for_element(FusionvCenterPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Function call to remove selected vcenter")
    if not ui_lib.wait_for_element(FusionvCenterPage.ID_ELEMENT_VCENTER % vcen_name):
        logger.warn("vCenter %s not found in GUI" % vcen_name)
        return False

    logger._log_to_console_and_log_file("Deleting vCenter  %s" % vcen_name)
    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_MENU_ACTION_REMOVE)
    ui_lib.wait_for_element_visible(FusionvCenterPage.ID_BTN_DELETE_VCENTER_CONFIRM, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_BTN_DELETE_VCENTER_CONFIRM)

    "validating presence of vCenter in UI "
    logger._log_to_console_and_log_file("Waiting for the element disappear from the UI")
    ui_lib.wait_for_element_remove(FusionvCenterPage.ID_ELEMENT_LIST % vcen_name, PerfConstants.REMOVE_VCENTER)
    ui_lib.wait_for_element_and_click(FusionvCenterPage.ID_RESET_FILTER, PerfConstants.DEFAULT_SYNC_TIME)
    if ui_lib.wait_for_element_notvisible(FusionvCenterPage.ID_ELEMENT_LIST % vcen_name, PerfConstants.REMOVE_VCENTER):
        logger._log_to_console_and_log_file("Success: vCenter '{0}' is deleted".format(vcen_name))
        return True
    else:
        logger.warn("Fail: Failed to delete vCenter: '{0}".format(vcen_name))
        return False
