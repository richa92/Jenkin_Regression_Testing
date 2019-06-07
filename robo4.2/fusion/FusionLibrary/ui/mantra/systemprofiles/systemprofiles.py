# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.

"""
    System Profiles Page
"""

from collections import Counter
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.mantra.systemprofiles.systemprofile_elements import systemprofilesPage
from FusionLibrary.ui.mantra.utils import mantraUtils
from FusionLibrary.ui.mantra.utils.constants import mantraSyncConstants, mantraConstants
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.api.networking import logical_interconnects


def navigate():
    # Accessing "System Profile" page
    BuiltIn().sleep(1)
    logger._log_to_console_and_log_file("\n- Accessing 'System Profile' Page...")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_ONEVIEW_TAB)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_LINK_SYSTEM_PROFILE)

    # Check if "System Profile" page was correctly displayed
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        logger._log_to_console_and_log_file("\t...Done.")
    else:
        ui_lib.fail_test("\t- Unable to access 'System Profile' page")


def navigateOverview():
    logger._log_to_console_and_log_file("\n\t- Accessing 'Overview' perspective")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_VIEW_SELECTOR)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_OPTION_OVERVIEW)
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_CONTENTS):
        logger._log_to_console_and_log_file("\t- Overview perspective was correctly displayed")
    else:
        ui_lib.fail_test("\t- Unable to change view to Overview perspective")


def navigateGeneral():
    logger._log_to_console_and_log_file("\t- Accessing 'General' View")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_OPTION_OVERVIEW)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_OPTION_GENERAL_VIEW)
    if ui_lib.wait_for_element_text(systemprofilesPage.ID_LABEL_GENERAL, "General"):
        logger._log_to_console_and_log_file("\t- General View was correctly displayed")
        checkGeneralContents()
    else:
        ui_lib.fail_test("\t- Unable to change view to GENERAL perspective")


def navigateActivity():
    logger._log_to_console_and_log_file("\t- Accessing 'Activity' View")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_OPTION_OVERVIEW)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_OPTION_ACTIVITY_VIEW)
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_ACTIVITY_TABLE):
        logger._log_to_console_and_log_file("\t- Activity View was correctly displayed")
    else:
        ui_lib.fail_test("\t- Unable to change access the Activity page")


def navigateMap():
    # Accessing MAP view perspective
    logger._log_to_console_and_log_file("\t- Changing view to MAP perspective")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_MAP)
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_MAP) and ui_lib.wait_for_element_visible(systemprofilesPage.ID_MAP_SYSTEM_PROFILE):
        logger._log_to_console_and_log_file("\t- MAP perspective was correctly displayed")
        checkMapContents()
    else:
        ui_lib.fail_test("- Unable to change view to MAP perspective")


def checkGeneralContents():
    # Using checkElements to verify if the elements were displayed
    if mantraUtils.checkElements([[systemprofilesPage.ID_PRODUCT_NUMBER_LABEL, "'Product Number LABEL'"],
                                  [systemprofilesPage.ID_PRODUCT_NUMBER_CONTENT, "'Product Number CONTENT'"],
                                  [systemprofilesPage.ID_SYSTEM_TYPE_LABEL, "'System Type LABEL'"],
                                  [systemprofilesPage.ID_SYSTEM_TYPE_CONTENT, "'System Type CONTENT'"],
                                  [systemprofilesPage.ID_SYSTEM_TYPE_VERSION_LABEL, "'System Type Version LABEL'"],
                                  [systemprofilesPage.ID_SYSTEM_TYPE_VERSION_CONTENT, "'System Type Version CONTENT'"],
                                  [systemprofilesPage.ID_MODEL_LABEL, "'Model LABEL'"],
                                  [systemprofilesPage.ID_MODEL_CONTENT, "'Model CONTENT'"],
                                  [systemprofilesPage.ID_LAST_REFRESH_LABEL, "'Refresh LABEL'"],
                                  [systemprofilesPage.ID_LAST_REFRESH_CONTENT, "'Refresh CONTENT'"]]):
        ui_lib.fail_test("\t- At least one element was not found. Please check the 'Overview' page")
    else:
        logger._log_to_console_and_log_file("\t- All the elements were found")


def checkMapContents():
    logger._log_to_console_and_log_file("\t- Checking the elements in the tree...")
    # Using checkElements to verify if the elements were displayed, if not, mark failure as true
    if mantraUtils.checkElements([[systemprofilesPage.ID_MAP_SYSTEM_PROFILE, "'System Profile'"],
                                  [systemprofilesPage.ID_MAP_SYSTEMS, "'Systems'"]]):
        ui_lib.fail_test("\t- At least one element was not found. Please check the 'Map' page")
    else:
        logger._log_to_console_and_log_file("\t- All the elements were found")


def checkContents():
    """
       Check that each item on Contents side really exists
    """
    logger._log_to_console_and_log_file("")

    elements = [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.CLUSTERS, systemprofilesPage.HardwareTypesCS700.server_hw), 'Clusters - Server hardware']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.server_profile), 'Server profiles']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.server_profile_templates), 'Server profile template']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.ENCLOSURES, systemprofilesPage.HardwareTypesCS700.enclosure), 'Enclosures - Enclosure']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.logical_enclosure), 'Logical enclosure']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.INTERCONNECTS, systemprofilesPage.HardwareTypesCS700.logical_interconnect), 'Interconnects - Logical interconnect']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.interconnect), 'Interconnects']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.MANAGEMENT_HOSTS, systemprofilesPage.HardwareTypesCS700.server_hw), 'Management Hosts - Server hardware']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.POWER_DEVICES, systemprofilesPage.HardwareTypesCS700.power_devices), 'Power Devices - Power device']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.RACKS, systemprofilesPage.HardwareTypesCS700.rack), 'Racks - Rack']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_STATUS % (systemprofilesPage.ContentItems.STORAGE, systemprofilesPage.HardwareTypesCS700.storage_system), 'Storage - Storage Systems']]

    # Using checkElements to verify if the elements were displayed, if not, mark failure as true
    if mantraUtils.checkElements(elements):
        ui_lib.fail_test("- At least one element was not found. Please check the 'Overview' page")
    else:
        logger._log_to_console_and_log_file("- All the elements were found")


def checkContentsIsGreen():
    """
       Check that each item status on Contents side is green (OK)
    """
    logger._log_to_console_and_log_file("")

    # check green status for each content-item pair
    elements = [[systemprofilesPage.ID_HEALTH_ICON, "'Health GREEN ICON'"]]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.CLUSTERS, systemprofilesPage.HardwareTypesCS700.server_hw), 'Clusters - Server hardware']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.server_profile), 'Server profiles']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.server_profile_templates), 'Server profile template']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.ENCLOSURES, systemprofilesPage.HardwareTypesCS700.enclosure), 'Enclosures - Enclosure']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.logical_enclosure), 'Logical enclosure']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.INTERCONNECTS, systemprofilesPage.HardwareTypesCS700.logical_interconnect), 'Interconnects - Logical interconnect']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.EMPTY, systemprofilesPage.HardwareTypesCS700.interconnect), 'Interconnects']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.MANAGEMENT_HOSTS, systemprofilesPage.HardwareTypesCS700.server_hw), 'Management Hosts - Server hardware']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.POWER_DEVICES, systemprofilesPage.HardwareTypesCS700.power_devices), 'Power Devices - Power device']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.RACKS, systemprofilesPage.HardwareTypesCS700.rack), 'Racks - Rack']]
    elements += [[systemprofilesPage.MAP_CONTENT_ITEM_GREEN_STATUS % (systemprofilesPage.ContentItems.STORAGE, systemprofilesPage.HardwareTypesCS700.storage_system), 'Storage - Storage Systems']]

    # Using checkElements to verify if the elements were displayed, if not, mark failure as true
    if mantraUtils.checkElements(elements):
        ui_lib.fail_test("- At least one element was not in green status (OK). Please check the 'Overview' page")
    else:
        logger._log_to_console_and_log_file("- All the elements were OK")


def refresh():
    """
        Execute System Profiles page refresh action.
    """

    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()

    # Click on "Actions" > "Refresh" button
    logger._log_to_console_and_log_file("\n- Refreshing data")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_ACTIONS)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDONW_OPTION_REFRESH_ACTION)

    # Check if no popup messages were displayed
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_REFRESH_POPUP_ERROR_CLOSE_BUTTON):
        # Importing selenium library to take a screenshot
        selenium2lib = ui_lib.get_s2l()
        selenium2lib.capture_page_screenshot()

        # Click on "Close" button and fail the test
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_REFRESH_POPUP_ERROR_CLOSE_BUTTON)
        ui_lib.fail_test("\t- An unexpected popup message was displayed", captureScreenshot=False)

    # Check the "Refresh" task on "Activity" list
    logger._log_to_console_and_log_file("\t- Checking the 'Refresh' task")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_ICON_ACTIVITY)
    # Was the "Refresh" task created?
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_ACTIVITY_FLYOUT_TASK_BRIEF):
        # Check the task status
        if ui_lib.wait_for_element_visible(systemprofilesPage.ID_ICON_ACTIVITY_FLYOUT_TASK_BRIEF_STATUS_OK):
            logger._log_to_console_and_log_file("\t Refresh task was successfully completed")
        else:
            ui_lib.fail_test("\t- 'Refresh' task has failed")
    else:
        ui_lib.fail_test("\t- 'Refresh' task was not created")


def checkActivity(task_name):
    """
        Check a system profile activity.
    """

    # TODO: validate the check compliance details content
    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("\n- Checking '%s' task..." % task_name)
    if ui_lib.wait_for_element_text(systemprofilesPage.ID_SYSTEM_PROFILE_NOTIFICATION_TASK_NAME, task_name, mantraSyncConstants.COMPLIANCE_SYNC_TIME):
        logger._log_to_console_and_log_file("\t- Task found. Going to System Profiles' Activity page...")
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_SYSTEM_PROFILE_NOTIFICATION)
        # Click on "Details" link
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_TASK_DETAILS)
        # Verify the final state for the selected task
        if ui_lib.wait_for_element_text(systemprofilesPage.ID_EXPANDED_TASK_STATE, "Completed", mantraSyncConstants.COMPLIANCE_SYNC_TIME):
            logger._log_to_console_and_log_file("\t- Task completed!")
        elif ui_lib.wait_for_element_text(systemprofilesPage.ID_EXPANDED_TASK_STATE, "Error", mantraSyncConstants.COMPLIANCE_SYNC_TIME):
            ui_lib.fail_test("\t- Task failed!")
        else:
            ui_lib.fail_test("- Compliance task has failed due timeout. Please check the compliance activity.")
    else:
        ui_lib.fail_test("\t- Task '%s' not found!" % task_name)


def checkSystemProfileStatus(system_profile_name, expected_status):
    """
        Check the status of a specific system profile at System Profiles Page
    """

    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("\n- Checking if system profile status is as expected...")
    SPStatus = systemprofilesPage.Status()
    if (SPStatus.is_valid(expected_status)):
        expected_status = expected_status.lower()
    else:
        ui_lib.fail_test("\tStatus not recognized: %s. Valid status are %s" % (expected_status, systemprofilesPage.Status.status_list))

    # Verify if system profile exists
    actual_status = get_system_profile_status(system_profile_name)
    if actual_status == expected_status:
        logger._log_to_console_and_log_file("\t- System profile is | %s |, as expected." % expected_status)
    else:
        ui_lib.fail_test("\tSystem Profile at wrong status! Expected: %s | Actual: %s" % (expected_status, actual_status))


def get_system_profile_status(system_profile_name):
    """
        Return the status of the system profile previously selected.
    """

    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()
    logger._log_to_console_and_log_file("\n- Getting system profile status...")
    # select the system profile
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_SYSTEM_PROFILE_NAME_IN_TABLE % system_profile_name):
        # select system profile by name on left frame and verify its status
        logger._log_to_console_and_log_file("\t- Selecting system profile %s" % system_profile_name)
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_SYSTEM_PROFILE_NAME_IN_TABLE % system_profile_name)
    else:
        ui_lib.fail_test("\tSystem profile named %s not found. Please, verify the name informed and try again." % system_profile_name)

    # verify the system profile status
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_ICON_SYSTEM_PROFILE_HEALH_STATUS % systemprofilesPage.Status.OK):
        return systemprofilesPage.Status.OK
    elif ui_lib.wait_for_element_visible(systemprofilesPage.ID_ICON_SYSTEM_PROFILE_HEALH_STATUS % systemprofilesPage.Status.WARNING):
        return systemprofilesPage.Status.WARNING
    elif ui_lib.wait_for_element_visible(systemprofilesPage.ID_ICON_SYSTEM_PROFILE_HEALH_STATUS % systemprofilesPage.Status.ERROR):
        return systemprofilesPage.Status.ERROR
    else:
        ui_lib.fail_test("\tNot possible to get the system profile status.", False)


def __open_edit_system_profile_page():
    """
        Open Edit System Profile page through Actions>>Edit.
    """

    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()
    logger._log_to_console_and_log_file("\nGoing to Actions >> Edit...")
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDOWN_ACTIONS)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_DROPDONW_OPTION_EDIT_ACTION)
    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_TITLE_EDIT_SYSTEM_PROFILE):
        ui_lib.fail_test("\nEdit System Profile page was not loaded correctly.", captureScreenshot=True)
    else:
        logger._log_to_console_and_log_file("\t... Done.")


def remove_rack(rack_name):
    """
        Edit a system profile, removing a specific rack.
    """

    __open_edit_system_profile_page()
    if not __is_racks_table_empty():
        logger._log_to_console_and_log_file("\tRack(s) Found")
        logger._log_to_console_and_log_file("\tRemoving rack \"%s\"" % rack_name)
        if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_RACK_NAME % rack_name):
            ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_CANCEL_EDIT_SYSTEM_PROFILE)
            ui_lib.fail_test("\tRack not found. Verify the rack name informed.")

        else:
            ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_REMOVE_RACK % rack_name)
            ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_EDIT_SYSTEM_PROFILE)
            ui_lib.wait_for_element_hidden(systemprofilesPage.ID_BUTTON_EDIT_SYSTEM_PROFILE, mantraSyncConstants.SYSTEM_PROFILE_TASK_TIMEOUT, True)
    else:
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_CANCEL_EDIT_SYSTEM_PROFILE)
        ui_lib.fail_test("\tNo Rack(s) Found. The Rack Table is empty.")


def is_contents_section_empty():
    """
        Verify if the Rack Table in System Profile Edit page is empty
    """

    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()
    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_CONTENTS):
        navigateOverview()
    logger._log_to_console_and_log_file("\n\t- Verifying if contents section is empty,\n\t once there are no racks associated to the System Profile.")
    if not (ui_lib.wait_for_element_text_match(systemprofilesPage.OVERVIEW_CONTENTS, mantraConstants.EMPTY_OVERVIEW_CONTENTS_MESSAGE)):
        ui_lib.fail_test("System Profile Contents was not empty or was not able to retrieve data. Check the screenshot.", captureScreenshot=True)


def __is_racks_table_empty():
    logger._log_to_console_and_log_file("\tVerifying if Racks table is empty or not...")
    if ui_lib.is_visible(systemprofilesPage.ID_TABLE_EDIT_SYSTEM_PROFILE_RACKS):
        logger._log_to_console_and_log_file("\t...Table not empty.")
        return False
    else:
        logger._log_to_console_and_log_file("\t...Table is empty.")
        return True


def rename_system_profile(new_system_profile_name):
    """
        Rename a system profile.
    """

    __open_edit_system_profile_page()
    logger._log_to_console_and_log_file("\n-Renaming system profile to \"%s\"." % new_system_profile_name)
    ui_lib.wait_for_element_and_input_text(systemprofilesPage.ID_INPUT_SYSTEM_PROFILE_NAME, new_system_profile_name)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_EDIT_SYSTEM_PROFILE)
    if not ui_lib.wait_for_element_hidden(systemprofilesPage.ID_BUTTON_EDIT_SYSTEM_PROFILE, mantraSyncConstants.SYSTEM_PROFILE_TASK_TIMEOUT):
        ui_lib.fail_test("Update system profile failed!", captureScreenshot=True)


def validate_system_profile_name(system_profile_name):
    """
        Verify if a System Profile Title is according to the name provided.
    """

    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()
    logger._log_to_console_and_log_file("\nVerifying if system profile name is \"%s\" as expected..." % system_profile_name)
    if ui_lib.element_text_matches(systemprofilesPage.ID_LABEL_SYSTEM_PROFILE_NAME, system_profile_name):
        logger._log_to_console_and_log_file("\tSystem profile correctly checked!")
    else:
            ui_lib.fail_test("\tThe system profile name provided does not match. The System Profile name displayed was \"%s\"." % ui_lib.get_text(systemprofilesPage.ID_LABEL_SYSTEM_PROFILE_NAME))


def add_rack(rack_name):
    """
        Edit a system profile, adding a specific rack.
    """
    logger._log_to_console_and_log_file("\n>>> Add rack \"%s\" to system profile." % rack_name)
    __open_edit_system_profile_page()
    # validating if rack is not already added to the system profile
    if ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_RACK_NAME % rack_name):
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_CANCEL_EDIT_SYSTEM_PROFILE)
        ui_lib.fail_test("Rack \"%s\" cannot be added because it's already listed in rack's table" % rack_name)
    logger._log_to_console_and_log_file("\t-Clicking on \"Add rack\" button.")
    if not ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_ADD_RACK_FROM_EDIT_PAGE):
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_CANCEL_EDIT_SYSTEM_PROFILE)
        ui_lib.fail_test("\"Add rack\" button is not available at Edit System Profile Page.", True)
    if not ui_lib.wait_for_element_and_click(systemprofilesPage.ID_ITEM_RACK_TO_BE_ADDED % rack_name):
        ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_CANCEL_EDIT_SYSTEM_PROFILE)
        ui_lib.fail_test("Rack named \"%s\" not found." % rack_name, True)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_ADD_RACK_AND_CLOSE_PAGE)
    ui_lib.wait_for_element_and_click(systemprofilesPage.ID_BUTTON_EDIT_SYSTEM_PROFILE)
    ui_lib.wait_for_element_hidden(systemprofilesPage.ID_BUTTON_EDIT_SYSTEM_PROFILE, mantraSyncConstants.SYSTEM_PROFILE_TASK_TIMEOUT, True)


def check_content_resource(content_category, content_resource):
    """
        Verify if a resource is displayed on System Profile Contents section.
        This function can also be used to verify the number of a specific resource.

        e.g.: check_content_element("Clusters", "4 Server Profiles")
              check_content_element("Clusters", "Server Profiles")
              check_content_element("Clusters", "4")
    """
    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()
    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_CONTENTS):
        navigateOverview()
    logger._log_to_console_and_log_file("\n -Verifying if category \"%s\" contains \"%s\" in Contents section." % (content_category, content_resource))
    if ui_lib.wait_for_element_visible(systemprofilesPage.MAP_CONTENT_RESOURCE_ITEM % (content_category, content_resource)):
        logger._log_to_console_and_log_file("\t- Found \"%s\" for category \"%s\"!" % (content_resource, content_category))
    else:
        ui_lib.fail_test("Resource and/or category not found in Contents section", captureScreenshot=True)


def go_system_profiles_wait_for_contents_to_load():
    # TO DO: This Function exists due to DE533. Might be enhanced anyway
    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_PAGE_LABEL):
        navigate()
    if not ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_CONTENTS):
        navigateOverview()
    # TO DO - FIX ME: Temporary just to don't have the intermediate state of the loading page as "None" or "Retrieve" text.
    ui_lib.wait_for_element_visible(systemprofilesPage.ID_LABEL_CONTENTS, 10, True)
    ui_lib.wait_for_element_visible(systemprofilesPage.MAP_CONTENT_RESOURCE_ITEM % ("Clusters", "Server hardware"))


class Converged_System:
    def __init__(self, new_racks, ss_dict, spt_dict):
        self.racks = new_racks
        self.storage_system = ss_dict
        self.server_profile_templates = spt_dict

    def get_clusters(self):
        total = Counter({})
        for rack in self.racks:
            total += rack.clusters
        return total

    def get_enclosures(self):
        total = Counter({})
        for rack in self.racks:
            total += rack.enclosures
        return total

    def get_interconnects(self):
        total = Counter({})
        for rack in self.racks:
            total += rack.interconnects
        return total

    def get_mng_hosts(self):
        total = Counter({})
        for rack in self.racks:
            total += rack.mngHosts
        return total

    def get_racks(self):
        total = Counter({})
        for rack in self.racks:
            total += rack.racks
        return total


class Rack:
    def __init__(self):
        self.name = ''
        self.clusters = {}
        self.enclosures = {}
        self.interconnects = {}
        self.mngHosts = {}
        self.racks = {}


def read_rack_from_xml(rack):
    new_rack = Rack()
    new_rack.name = rack.name
    new_rack.clusters = Counter({'Server hardware': int(rack.serverHardware), 'Server profiles': int(rack.serverProfiles)})
    new_rack.enclosures = Counter({'Enclosures': int(rack.enclosures), 'Logical enclosures': int(rack.logicalEnclosures)})
    new_rack.interconnects = Counter({'Logical interconnects': int(rack.logicalInterconnects), 'Interconnects': int(rack.interconnects)})
    new_rack.mngHosts = Counter({'Server hardware': int(rack.mngHostsServer)})
    new_rack.racks = Counter({'Racks': int(rack.racks)})
    return new_rack


def get_contents_from_UI():
    go_system_profiles_wait_for_contents_to_load()

    cData = ui_lib.get_text(systemprofilesPage.OVERVIEW_CONTENTS)
    logger._log_to_console_and_log_file("Creating a Dictionary from the following Text from System profile UI: \n\"%s\"" % cData)

    cData = cData.split()

    logger._log_to_console_and_log_file("Contents from UI after split: \"%s\"\n" % cData)

    ss_count = get_text_from_contents_storage(cData)
    spt_count = get_text_from_server_profile_template(cData)

    rack_total = Rack()
    rack_total.clusters = get_text_from_contents_clusters(cData)
    rack_total.enclosures = get_text_from_contents_enclosures(cData)
    rack_total.interconnects = get_text_from_contents_interconnects(cData)
    rack_total.mngHosts = get_text_from_contents_management_hosts(cData)
    rack_total.racks = get_text_from_contents_racks(cData)
    ui_contents = Converged_System([rack_total], ss_count, spt_count)

    return ui_contents


def get_text_from_contents_clusters(cData):
    # Create a dictionary for this content
    cCluster = {}
    """ Create a Dictionary for Cluster Resources from the System Profile's contents
        cData [2 to 3]  - 'Server hardware'        - cData [1] Quantity
        cData [5 to 6]  - 'Server profiles'        - cData [4] Quantity
    """
    try:
        cCluster = Counter({str(cData[2]) + " " + str(cData[3]): int(cData[1]), str(cData[5]) + " " + str(cData[6]): int(cData[4])})
    except IndexError:
        logger._log_to_console_and_log_file("Dictionary for Cluster not created. The text split does not reach the position expected by the code.")

    logger._log_to_console_and_log_file("Dictionary for the Contents of Cluster from UI created and casted: \"%s\"" % cCluster)
    return cCluster


def get_text_from_contents_enclosures(cData):
    """ Create a Dictionary for Enclosures from System Profiles  Contents UI
        cData [13] = 'Enclosures'               - cData [12] Quantity
        cData [15 to 16] = 'Logical enclosures' - cData [14] Quantity
    """
    cEnc = {}
    try:
        cEnc = Counter({str(cData[13]): int(cData[12]), str(cData[15]) + " " + str(cData[16]): int(cData[14])})
    except IndexError:
        logger._log_to_console_and_log_file("Dictionary for Enclosures not created. The text split does not reach the position expected by the code.")
    logger._log_to_console_and_log_file("Dictionary for the Contents of Enclosures: \"%s\"" % cEnc)
    return cEnc


def get_text_from_contents_interconnects(cData):
    """ Create a Dictionary for Interconnects informations from the System Profiles Contents
        cData[19 to 20] = 'Logical Interconnects'    - cData[18] Quantity
        cData[22] =  'Interconnects'            - cData[21] Quantity
    """
    cInterconnects = {}
    try:
        cInterconnects = Counter({str(cData[19]) + " " + str(cData[20]): int(cData[18]), str(cData[22]): int(cData[21])})
    except IndexError:
        logger._log_to_console_and_log_file("Dictionary for Interconnect was not created. The text split does not reach the position expected by the code.")
    logger._log_to_console_and_log_file("Dictionary for the Contents of Interconnects: \"%s\"" % cInterconnects)
    return cInterconnects


def get_text_from_contents_management_hosts(cData):
    """ Create a Dictionary for Management Hosts from System Profiles Contents table
        cData[26 to 27] = 'Server hardware' -  cData[25] Quantity
    """
    cMhost = {}
    try:
        cMhost = Counter({str(cData[26]) + " " + str(cData[27]): int(cData[25])})
    except IndexError:
        logger._log_to_console_and_log_file("Dictionary for Management hosts was not created. The text split does not reach the position expected by the code.")
    logger._log_to_console_and_log_file("Dictionary for the Contents of Management Hosts: \"%s\"" % cMhost)
    return cMhost


def get_text_from_contents_racks(cData):
    """ Create a Dictionary for Racks from System Profiles Content table
        cData[30] =          'Racks' or 'Rack'          - cData[29] Quantity
    """
    cRacks = {}
    try:
        cRacks = Counter({str(cData[30]): int(cData[29])})
    except IndexError:
        logger._log_to_console_and_log_file("Dictionary for Racks was not created. The text split does not reach the position expected by the code.")
    logger._log_to_console_and_log_file("Dictionary for the Contents of Racks: \"%s\"" % cRacks)
    return cRacks


def get_text_from_contents_storage(cData):
    """ Create a Dictionary for Storage from System Profiles contents table
        cData[33 to 34] = 'Storage system'   -cData[32] Quantity
        1 Rack: [28 to 29] = 'Storage system' -cData[27] Quantity
    """
    cStorage = {}
    try:
        cStorage = Counter({str(cData[33]) + " " + str(cData[34]): int(cData[32])})
    except IndexError:
        logger._log_to_console_and_log_file("Dictionary for Storage was not created. The text split does not reach the position expected by the code.")
    logger._log_to_console_and_log_file("Dictionary for the Contents of Storage: \"%s\"" % cStorage)

    return cStorage


def get_text_from_server_profile_template(cData):
    """ Create a Dictionary for Server profile Template
        cData[8 to 10] = 'Server profile template'   -cData[7] Quantity
    """
    spt = {}
    try:
        spt = Counter({str(cData[8]) + " " + str(cData[9]) + " " + str(cData[10]): int(cData[7])})
    except IndexError:
        logger._log_to_console_and_log_file("Dictionary for server profile template was not created. The text split does not reach the position expected by the code.")
    logger._log_to_console_and_log_file("Dictionary for the Server profile template: \"%s\"" % spt)

    return spt


def compare_UI_with_expected_dics(ui_contents, expected_contents, last_rack_flag):
    if last_rack_flag is True:  # Updating the Expected Dictionary from plural to singular text before comparing
        if ui_contents["Rack"]:
            expected_contents["Rack"] = expected_contents["Racks"]  # The new entry is created with the same value
            del expected_contents["Racks"]
            logger._log_to_console_and_log_file("The Expected Dictionary key: (Racks) is now (Rack)")

        if ui_contents["Enclosure"]:
            expected_contents["Enclosure"] = expected_contents["Enclosures"]
            del expected_contents["Enclosures"]
            logger._log_to_console_and_log_file("The Expected Dictionary key: (Enclosures) is now (Enclosure)")

        if ui_contents["Logical enclosure"]:
            expected_contents["Logical enclosure"] = expected_contents["Logical enclosures"]
            del expected_contents["Logical enclosures"]
            logger._log_to_console_and_log_file("The Expected Dictionary key: (Logical enclosures) is now (Logical enclosure)")

        if ui_contents["Logical interconnect"]:
            expected_contents["Logical interconnect"] = expected_contents["Logical interconnects"]
            del expected_contents["Logical interconnects"]
            logger._log_to_console_and_log_file("The Expected Dictionary key: (Logical interconnects) is now (Logical interconnect)")

    # Perform the compare between GUI and the Converged System (XML)
    checkCompResult = cmp(ui_contents, expected_contents)
    logger._log_to_console_and_log_file("Comparing the UI Contents with the expected result:")

    if (checkCompResult) != (0):
        logger._log_to_console_and_log_file("Contents from UI (GUI): \"%s\"" % ui_contents)
        logger._log_to_console_and_log_file("Content expected  (XML): \"%s\"" % expected_contents)

    if (checkCompResult) == (0):
        logger._log_to_console_and_log_file("Contents from UI  (GUI): \"%s\"" % ui_contents)
        logger._log_to_console_and_log_file("Content expected  (XML): \"%s\"" % expected_contents)

    return checkCompResult


def read_converged_system_from_xml(cs_obj):
    sp = cs_obj.SystemProfile

    # First we'll read the XML file into a Converged_System class
    racks = []
    spt_count = {}
    ss_count = {}
    if sp.has_property("Rack"):
        for rack in sp.Rack:
                new_rack = read_rack_from_xml(rack)
                racks += [new_rack]
    if sp.has_property("profileTemplates"):
        spt_count = Counter({'Server profile template': int(sp.profileTemplates)})
    if sp.has_property("storageSystems"):
        ss_count = Counter({'Storage system': int(sp.storageSystems)})

    return (Converged_System(racks, ss_count, spt_count))


def add_rack_configuration(rack_name, converged_system, full_configuration):
    # Check if a rack exists in a full configuration
    index = None
    for rack in full_configuration.racks:
        if (rack.name == rack_name):
            index = full_configuration.racks.index(rack)
            break

    if (index is None):
        ui_lib.fail_test("Couldn't find rack %s in this configuration" % rack_name)

    # Create a new one passing the multi-rack settings (storage Systems, server profile template)
    if (converged_system is None):
        converged_system = (Converged_System([], full_configuration.storage_system, full_configuration.server_profile_templates))
    # Adding the rack
    converged_system.racks.append(full_configuration.racks[index])

    return converged_system


def subtrack_rack_configuration(rack_name, converged_system):
    index = None
    for rack in converged_system.racks:
        if (rack.name == rack_name):
            index = converged_system.racks.index(rack)
            break
    if (index is None):
        ui_lib.fail_test("Couldn't find rack %s in this configuration" % rack_name)
    # Removing the rack from the list
    converged_system.racks.pop(index)

    if (len(converged_system.racks) == 0):
        converged_system.storage_system = {}
        converged_system.server_profile_templates = {}

    return converged_system


def compare_converged_systems_contents(expected_converged_system, ui_contents):
    res = True

    # set the last_rack_flag variable to check if the expected converged system contains the last Rack to use the value in the compare_UI(...) method
    if (len(expected_converged_system.racks) == 1):
        last_rack_flag = True
        logger._log_to_console_and_log_file("\nConverged System contains the last Rack.\n")
    else:
        last_rack_flag = False
        logger._log_to_console_and_log_file("\nConverged System contain more than one Rack.\n")

    # Cluster
    checkCompResult = compare_UI_with_expected_dics(ui_contents.get_clusters(), expected_converged_system.get_clusters(), last_rack_flag)

    if checkCompResult == 0:
        logger._log_to_console_and_log_file("Test Passed.\n")
    else:
        logger._log_to_console_and_log_file("Test Failed. The contents for (Cluster) does not corresponds to the expected. Exit Code: \"%s\"" % checkCompResult)
        res = False

    # Racks
    checkCompResult = compare_UI_with_expected_dics(ui_contents.get_racks(), expected_converged_system.get_racks(), last_rack_flag)
    if checkCompResult == 0:
        logger._log_to_console_and_log_file("Test Passed.\n")
    else:
        logger._log_to_console_and_log_file("Test Failed, number of (Racks) is not expected. Exit Code:\"%s\"\n" % checkCompResult)
        res = False

    # Enclosures
    checkCompResult = compare_UI_with_expected_dics(ui_contents.get_enclosures(), expected_converged_system.get_enclosures(), last_rack_flag)
    if checkCompResult == 0:
        logger._log_to_console_and_log_file("Test Passed.\n")
    else:
        logger._log_to_console_and_log_file("Test Failed. Number of (Enclosures) is not the expected. Exit Code: \"%s\"\n" % checkCompResult)
        res = False

    # Interconnects
    checkCompResult = compare_UI_with_expected_dics(ui_contents.get_interconnects(), expected_converged_system.get_interconnects(), last_rack_flag)
    if checkCompResult == 0:
        logger._log_to_console_and_log_file("Test Passed.\n")
    else:
        logger._log_to_console_and_log_file("Test Failed. Number of (Interconnects) is not the expected.  Exit Code: \"%s\"\n" % checkCompResult)
        res = False

    # Management Hosts
    checkCompResult = compare_UI_with_expected_dics(ui_contents.get_mng_hosts(), expected_converged_system.get_mng_hosts(), last_rack_flag)
    if checkCompResult == 0:
        logger._log_to_console_and_log_file("Test Passed.\n")
    else:
        logger._log_to_console_and_log_file("Test Failed. Number of (Management Hosts) is not compliant to the expected. Exit Code: \"%s\"\n" % checkCompResult)
        res = False

    # UI Storage
    checkCompResult = compare_UI_with_expected_dics(ui_contents.storage_system, expected_converged_system.storage_system, last_rack_flag)
    if checkCompResult == 0:
        logger._log_to_console_and_log_file("Test Passed.\n")
    else:
        logger._log_to_console_and_log_file("Test Failed. The number of (Storage System) is not compliant to the expected. Exit Code: \"%s\"\n" % checkCompResult)
        res = False

    # Server profile template
    checkCompResult = compare_UI_with_expected_dics(ui_contents.server_profile_templates, expected_converged_system.server_profile_templates, last_rack_flag)
    if checkCompResult == 0:
        logger._log_to_console_and_log_file("Test Passed.\n")
    else:
        logger._log_to_console_and_log_file("Test Failed. The number of (Server profile templates) is not compliant to the expected. Exit Code: \"%s\"\n" % checkCompResult)
        res = False

    return res


def verify_if_ui_contents_matches_configuration(expected_converged_system):
    if (len(expected_converged_system.racks) == 0):
        is_contents_section_empty()
    else:
        # Read UI contents
        ui_contents = get_contents_from_UI()
        if (not compare_converged_systems_contents(expected_converged_system, ui_contents)):
            ui_lib.fail_test("Test has failed. The System Profile Contents does not corresponds to the expected.")

    return expected_converged_system
