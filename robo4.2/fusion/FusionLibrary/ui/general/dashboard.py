# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Dashboard
"""


from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType


def navigate():
    FusionUIBase.navigate_to_section(SectionType.DASHBOARD)


def create_dashboard(*dashboard_obj):
    """ Create Server Profile    """
    selenium2lib = ui_lib.get_s2l()
    resources = {"alerts": 'activity', "fc-device-managers": "san managers", "firmware-drivers": "firmware Bundles",
                 "grouprolemappings": "users and groups", "tasks": "activity", "ethernet-networks": "networks", "fc-networks": "networks",
                 "power-devices": "power delivery devices", "users": "users and groups"}
    if not selenium2lib._is_element_present(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    if type(dashboard_obj) is test_data.DataObj:
        dashboard_obj = [dashboard_obj]
    elif type(dashboard_obj) is tuple:
        dashboard_obj = list(dashboard_obj[0])

    for dashboard in dashboard_obj:
        if len(dashboard.title.strip()) > 0:
            logger._log_to_console_and_log_file("\nCreating Dashboard %s..." % dashboard.name)
            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_LINK_ADD_DASHBOARD)
            if dashboard.panel != "Custom":
                logger._log_to_console_and_log_file("\nSeleting  %s Panel..." % dashboard.panel)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_PANEL_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_PANEL_SELECT % dashboard.panel)
            else:
                logger._log_to_console_and_log_file("\nSelecting Custom Panel %s..." % dashboard.name)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_PANEL_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_PANEL_SELECT % dashboard.panel)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_RESOURCES_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_RESOURCES_SELECT % dashboard.resource)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_TITLE)
                ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_TITLE, dashboard.title)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_QUERY)
                ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_QUERY, dashboard.query)
                if dashboard.type.lower() == "custom":
                    logger._log_to_console_and_log_file("\nSelecting Type Custom")
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_DROPDOWN)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_SELECT % dashboard.type)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_CAPTION)
                    ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_CAPTION, dashboard.caption)
                    if dashboard.addslice.lower() == "true":
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_ADD_SLICE)
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_SLICE_LABEL)
                        ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_SLICE_LABEL, dashboard.slicelabel)
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_SLICE_QUERY)
                        ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_SLICE_QUERY, dashboard.slicequery)
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_ADD_SLICE_OK)
                elif dashboard.type.lower() == "status":
                    # Select Type Status
                    logger._log_to_console_and_log_file("\nSelecting Status Type")
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_DROPDOWN)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_SELECT % dashboard.type)
                ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_OTHER_LABEL, dashboard.otherlabel)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_ADD_DASHBOARD_ADD)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title)
                # Verify Dashboard reource and Dashboard Page Label
                pagelabel = ui_lib.get_text(FusionDashboardPage.ID_PAGE_LABEL_TEXT)
                for key in resources:
                    if key == dashboard.title:
                        dashboardlabel = resources[key]
                    else:
                        dashboardlabel = dashboard.title.replace('-', ' ')
                if pagelabel.lower() == dashboardlabel.lower():
                    logger._log_to_console_and_log_file("%s Dashboard was created and  page verified" % dashboard.title)
                    return True
                else:
                    locator = FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title
                    raise AssertionError("\n Dashboard was not created with element %s or not found" % locator)
        else:
            raise AssertionError("\nDashboard's Title cannot be empty")


def verify_dashboard_exist(*dashboard_obj):
    """ Verify Dashboard Should Exist """
    selenium2lib = ui_lib.get_s2l()
    # resources that does not match with Dashboard page label
    resources = {"alerts": 'activity', "fc-device-managers": "san managers", "firmware-drivers": "firmware Bundles",
                 "grouprolemappings": "users and groups", "tasks": "activity", "ethernet-networks": "networks", "fc-networks": "networks",
                 "power-devices": "power delivery devices", "users": "users and groups"}
    if not selenium2lib._is_element_present(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    if type(dashboard_obj) is test_data.DataObj:
        dashboard_obj = [dashboard_obj]
    elif type(dashboard_obj) is tuple:
        dashboard_obj = list(dashboard_obj[0])
    for dashboard in dashboard_obj:
        if len(dashboard.title.strip()) > 0:
            logger._log_to_console_and_log_file("\nVerifying Dashboard %s exist..." % dashboard.title)
            if selenium2lib._is_visible(FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title):
                logger._log_to_console_and_log_file("Dashboard exist, verifying Dashboard link...")
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title)
                ui_lib.wait_for_element_visible(FusionDashboardPage.ID_LINK_ADD_DASHBOARD)
                pagelabel = ui_lib.get_text(FusionDashboardPage.ID_PAGE_LABEL_TEXT)
                for key in resources:
                    if key == dashboard.title:
                        dashboardlabel = resources[key]
                    else:
                        dashboardlabel = dashboard.title.replace('-', ' ')
                    if pagelabel.lower() == dashboardlabel.lower():
                        logger._log_to_console_and_log_file("Verified Dashboard link accessible")
                        return True
                    else:
                        message = "Dashboard -- %s link is not accessible" % dashboard.title
                        raise AssertionError(message)
            else:
                locator = FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title
                message = "Dashboard is not visible in the Dashboards Page with element %s" % locator
                raise AssertionError(message)
        else:
            message = "\n%s has Dashboard title name is empty" % dashboard.name
            raise AssertionError(message)


def edit_dashboard(*edit_dashboard_obj):
    """ Edit Dashboard """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    if type(edit_dashboard_obj) is test_data.DataObj:
        edit_dashboard_obj = [edit_dashboard_obj]
    elif type(edit_dashboard_obj) is tuple:
        edit_dashboard_obj = list(edit_dashboard_obj[0])
    for dashboard in edit_dashboard_obj:
        if len(dashboard.title.strip()) > 0:
            logger._log_to_console_and_log_file("\nEditing Dashboard %s ..." % dashboard.name)
            ui_lib.wait_for_element_visible(FusionDashboardPage.ID_LINK_ADD_DASHBOARD)
            # Check if Dashboard exist and click on Edit
            if selenium2lib._is_visible(FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title):
                logger._log_to_console_and_log_file("Dashboard exist, Editing Dashboard %s..." % dashboard.title)
                ui_lib.move_to_element_and_click(FusionDashboardPage.ID_LINK_DASHBOARD_EDIT % dashboard.title, FusionDashboardPage.ID_LINK_DASHBOARD_EDIT % dashboard.title)
                if selenium2lib._is_visible(FusionDashboardPage.ID_EDIT_DASHBOARD_PANEL_LABEL):
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_PANEL_DROPDOWN)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_PANEL_SELECT % dashboard.panel)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_RESOURCES_DROPDOWN)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_RESOURCES_SELECT % dashboard.resource)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_TITLE)
                    ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_TITLE, dashboard.title)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_QUERY)
                    ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_QUERY, dashboard.query)
                    if dashboard.type.lower() == "custom":
                        # Select Type Custom and input caption
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_DROPDOWN)
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_SELECT % dashboard.type)
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_CAPTION)
                        ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_CAPTION, dashboard.caption)
                        if dashboard.editslice.lower() == "add":
                            # add new slice
                            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_ADD_SLICE)
                            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_SLICE_LABEL)
                            ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_SLICE_LABEL, dashboard.slicelabel)
                            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_SLICE_QUERY)
                            ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_SLICE_QUERY, dashboard.slicequery)
                            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_ADD_SLICE_OK)
                        elif dashboard.editslice.lower() == "edit":
                            # Edit current slice
                            ui_lib.move_to_element_and_click(FusionDashboardPage.ID_LINK_ADD_SLICE_EDIT % dashboard.editslicelabel, FusionDashboardPage.ID_LINK_ADD_SLICE_EDIT % dashboard.editslicelabel)
                            ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_SLICE_LABEL, dashboard.slicelabel)
                            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_TXT_ADD_SLICE_QUERY)
                            ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_SLICE_QUERY, dashboard.slicequery)
                            ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_ADD_SLICE_OK)
                    elif dashboard.type.lower() == "status":
                        # Select Type Status
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_DROPDOWN)
                        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_COMBO_ADD_DASHBOARD_TYPE_SELECT % dashboard.type)
                        # Input other Label and click add
                    ui_lib.wait_for_element_and_input_text(FusionDashboardPage.ID_TXT_ADD_DASHBOARD_OTHER_LABEL, dashboard.otherlabel)
                    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_EDIT_DASHBOARD_OK)
                    return True
                else:
                    message = "\n Dashboard %s is not editable" % dashboard.title
                    raise AssertionError(message)
            else:
                message = "\n Dashboard %s does not exist or not visible" % dashboard.title
                raise AssertionError(message)
        else:
            message = "\n%s Dashboard title is empty" % dashboard.name
            raise AssertionError(message)


def delete_dashboard(*dashboard_obj):
    """ Delete Dashboard """
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    if type(dashboard_obj) is test_data.DataObj:
        dashboard_obj = [dashboard_obj]
    elif type(dashboard_obj) is tuple:
        dashboard_obj = list(dashboard_obj[0])
    for dashboard in dashboard_obj:
        if len(dashboard.title.strip()) > 0:
            logger._log_to_console_and_log_file("\nVerifying Dashboard %s exist..." % dashboard.title)
            ui_lib.wait_for_element_visible(FusionDashboardPage.ID_LINK_ADD_DASHBOARD)
            if selenium2lib._is_visible(FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title):
                logger._log_to_console_and_log_file("Dashboard exist, Deleting Dashboard %s..." % dashboard.title)
                ui_lib.move_to_element_and_click(FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title, FusionDashboardPage.ID_LINK_DASHBOARD_DELETE % dashboard.title)
                ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_BTN_DASHBOARD_DELETE_CONFIRM)
                ui_lib.wait_for_element_notvisible(FusionDashboardPage.ID_LINK_DASHBOARD_NAME % dashboard.title)
                logger._log_to_console_and_log_file("Dashboard %s deleted" % dashboard.title)
                return True
            else:
                message = "Dashboard -- %s is not available or not visible in the Dashboards Page" % dashboard.title
                raise AssertionError(message)
        else:
            message = "\n%s has Dashboard title name is empty" % dashboard.name
            raise AssertionError(message)


def validate_dashboard_graphs(*component_obj):
    """
    This function is to Validate Dash board Graphs which includes component hyper link
    as well as component objects (critical,warning and error) hyper links
    Example:
        validate_dashboard_graphs(*component)
    """
    s2l = ui_lib.get_s2l()

    if isinstance(component_obj, test_data.DataObj):
        component_obj = [component_obj]
    elif isinstance(component_obj, tuple):
        component_obj = list(component_obj[0])

    bln_var = True
    if not ui_lib.wait_for_element(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    for component in component_obj:
        logger._log_to_console_and_log_file("Verifying the dash board components list for existence of component '{0}".format(component.name))
        component_list = [ui_lib.get_text(s).lower() for s in s2l._element_find(FusionDashboardPage.ID_COMPONENT_LIST, False, False)]
        if component.name.lower() not in component_list:
            logger._warn("Component '{0}' does not exists".format(component.name))
            return False

        logger._log_to_console_and_log_file("Validating Component hyper link")
        ui_lib.wait_for_element(FusionDashboardPage.ID_COMPONENT_SUMMARY % component.name)
        obj_count = ui_lib.get_text(FusionDashboardPage.ID_NUMBER_OF_OBJECT % component.name)
        ui_lib.wait_for_element_visible(FusionDashboardPage.ID_ELEMENT_COMPONENT % component.name)
        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_ELEMENT_COMPONENT % component.name)

        if not _validate_dashboard_component_hyper_link(component.name, obj_count):
            return False

        if int(obj_count) == 0:
            logger._log_to_console_and_log_file("Dashboard component {0} doesn't have objects".format(component.name))
            return True

        logger._log_to_console_and_log_file("Validating component objects status")
        if not ui_lib.wait_for_element(FusionDashboardPage.ID_PAGE_LABEL):
            navigate()

        ui_lib.wait_for_element(FusionDashboardPage.ID_COMPONENT_SUMMARY % component.name)
        if ui_lib.wait_for_element(FusionDashboardPage.ID_NO_SUMMARY_STATUS % component.name, PerfConstants.DEFAULT_SYNC_TIME):
            logger._log_to_console_and_log_file("Dashboard component '{0}' doen't have Status summary".format(component.name))
            return True

        logger._log_to_console_and_log_file("Validating critical object hyper link")
        if not _validate_critical_object_hyper_link(component.name):
            return False

        logger._log_to_console_and_log_file("Validating warning object hyper link")
        if not _validate_warning_object_hyper_link(component.name):
            return False

        logger._log_to_console_and_log_file("Validating OK object hyper link")
        if not _validate_error_object_hyper_link(component.name):
            return False

    return bln_var


def _validate_dashboard_component_hyper_link(component, obj_count):
    """
        validating dash board component hyper link
    """

    s2l = ui_lib.get_s2l()
    comp_without_table = ['Enclosure Groups', 'Server Hardware Types']
    obj_list = []
    # giving wait time for loading page objects
    BuiltIn().sleep(2)

    if component not in comp_without_table:
        ui_lib.wait_for_element(FusionDashboardPage.ID_ELEMENT_LIST, PerfConstants.DEFAULT_SYNC_TIME)
        obj_list = [ui_lib.get_text(s) for s in s2l._element_find(FusionDashboardPage.ID_ELEMENT_LIST, False, False)]
    else:
        ui_lib.wait_for_element(FusionDashboardPage.ID_COMPONENT_TABLE_COUNT)
        obj_list = [ui_lib.get_text(s) for s in s2l._element_find(FusionDashboardPage.ID_COMPONENT_TABLE_COUNT, False, False)]

    if int(obj_count) == len(obj_list):
        logger._log_to_console_and_log_file("No.of objects in component hyper link is valid")
        return True
    elif len(obj_list) == 1 and obj_list[0].lower() == ("No " + component).lower():
        logger._log_to_console_and_log_file("No.of objects in component hyper link is valid")
        return True
    else:
        logger._warn("No.of objects in component hyper link is not valid")
        return False


def _validate_critical_object_hyper_link(component):
    """
        validating dash board component's critical object hyper link
    """
    if not ui_lib.wait_for_element(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element(FusionDashboardPage.ID_CRITICAL_OBJECTS_COUNT % component, PerfConstants.DEFAULT_SYNC_TIME)
    critical_obj_count = ui_lib.get_text(FusionDashboardPage.ID_CRITICAL_OBJECTS_COUNT % component)
    logger._log_to_console_and_log_file("number of objects with critical status :{0}".format(critical_obj_count))
    ui_lib.wait_for_element(FusionDashboardPage.ID_CRITICAL_OBJECTS_COUNT % component)
    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_CRITICAL_OBJECTS_COUNT % component)

    if int(critical_obj_count) == 0:
        logger._log_to_console_and_log_file("'{0}' Component does not have any critical status".format(component))
        return True
    else:
        if not _validate_dashboard_component_hyper_link(component, critical_obj_count):
            return False


def _validate_warning_object_hyper_link(component):
    """
        validating dash board component's warning object hyper link
    """
    if not ui_lib.wait_for_element(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element(FusionDashboardPage.ID_WARNING_COUNT_SUMMARY % component, PerfConstants.DEFAULT_SYNC_TIME)
    warning_obj_count = int(ui_lib.get_text(FusionDashboardPage.ID_WARNING_COUNT_SUMMARY % component))
    logger._log_to_console_and_log_file("number of objects with warning status :{0}".format(warning_obj_count))
    ui_lib.wait_for_element(FusionDashboardPage.ID_WARNING_COUNT_SUMMARY % component)
    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_WARNING_COUNT_SUMMARY % component)

    if int(warning_obj_count) == 0:
        logger._log_to_console_and_log_file("'{0}' Component does not have any warning status".format(component))
        return True
    else:
        if not _validate_dashboard_component_hyper_link(component, warning_obj_count):
            return False


def _validate_error_object_hyper_link(component):
    """
        validating dash board component's error object hyper link
    """
    if not ui_lib.wait_for_element(FusionDashboardPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element(FusionDashboardPage.ID_OK_COUNT_SUMMARY % component, PerfConstants.DEFAULT_SYNC_TIME)
    ok_obj_count = int(ui_lib.get_text(FusionDashboardPage.ID_OK_COUNT_SUMMARY % component))
    logger._log_to_console_and_log_file("number of ok status are:{0}".format(ok_obj_count))
    ui_lib.wait_for_element(FusionDashboardPage.ID_OK_COUNT_SUMMARY % component)
    ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_OK_COUNT_SUMMARY % component)

    if int(ok_obj_count) == 0:
        logger._log_to_console_and_log_file("'{0}' Component does not have any ok status".format(component))
        return True
    else:
        if not _validate_dashboard_component_hyper_link(component, ok_obj_count):
            return False


def verify_dashboard_component_status(*component_obj):
    """ This function is verify whether component status is as per expected
        Example:
            verify_dashboard_component_status(*component_obj)
    """
    if not ui_lib.wait_for_element(FusionDashboardPage.ID_PAGE_LABEL):
        if not navigate():
            return False

    if isinstance(component_obj, test_data.DataObj):
        component_obj = [component_obj]
    elif isinstance(component_obj, tuple):
        component_obj = list(component_obj[0])

    for component in component_obj:
        if ui_lib.wait_for_element(FusionDashboardPage.ID_ELEMENT_COMPONENT % component.name):
            logger._log_to_console_and_log_file("Component '{0}' is present".format(component.name))
            ui_lib.wait_for_element(FusionDashboardPage.ID_COMPONENT_STATUS % component.name)
            storage_status = ui_lib.get_text(FusionDashboardPage.ID_COMPONENT_STATUS % component.name)
        else:
            logger._warn("Component '{0}' is not present".format(component.name))
            return False

        if storage_status.lower() == component.status.lower():
            logger._log_to_console_and_log_file("Storage pool status is '{0}' same as expected '{1}'".format(storage_status, component.status))
            return True
        else:
            logger._warn("Storage pool status is '{0}' not same as expected '{1}'".format(storage_status, component.status))
            return False
