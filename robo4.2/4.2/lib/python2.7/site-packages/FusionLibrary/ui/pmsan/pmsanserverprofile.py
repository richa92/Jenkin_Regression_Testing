# (C) Copyright 2015 Hewlett-Packard Development Company, L.P.
# Code For the Keywords that will be used for the PM SAN tests
# Fusion Server Profile - San Storage UI page.

import Selenium2Library
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.general.activity_elements import FusionActivityPage
from FusionLibrary.ui.servers.serverprofiles_elements import FusionServerProfilesPage
from FusionLibrary.ui.servers import serverhardware
from FusionLibrary.ui.servers.serverhardware_elements import FusionServerHardwarePage
from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.pmsan.pmsanserverprofile_elements import ProfileSanStorageElements
from FusionLibrary.ui.servers import serverprofiles
from FusionLibrary.ui.storage.volumes_elements import FusionStorageVolumesPage
from FusionLibrary.ui.storage import volumes
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import uuid
import time
from FusionLibrary.ui.servers.serverprofiles import __get_time_from_timestamp,\
    is_element_present_in_activity_page, __validate_requested_bandwidth,\
    __select_value_from_a_profile_combo_box, PROFILE_BOOT_MODE_LIST
from FusionLibrary.ui.servers.serverprofiletemplates import _select_value_from_a_profile_combo_box
import cmd

selenium2lib = Selenium2Library.Selenium2Library()


def navigate():
    # Navigate to Server Profile Page
    base_page.navigate_base(FusionServerProfilesPage.ID_PAGE_LABEL,
                            FusionUIBaseElements.ID_MENU_LINK_SERVER_PROFILE,
                            ProfileSanStorageElements.ID_CSS_PATH)
    # Verify
    if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_LINK_CREATE_SERVER_PROFILES):
        logger._log_to_console_and_log_file("Unable to Navigate To Server Profiles Page")
        return False
    return True


# ==================================================================================
# This keyword will set up a server profile by filling in the necessary sections
# of the server profile. This includes the General and Connections sections. Once
# These Sections have been filled out, the keyword will fill in the San Storage
# Section. All sections will be filled in according to the profile object passed in
# ==================================================================================
def create_san_storage_profile(*profile_obj):
    selenium2lib = ui_lib.get_s2l()

    # Get to the server profile page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    # Create The Profiles From the profile_obj
    for profile in profile_obj:
        # Check for required fields
        if (profile.name == "" or profile.server == ""):
            logger._warn("Mandatory fields missing for profile %s. Skipping profile." % profile.name)
            continue

        logger._log_to_console_and_log_file("Creating Profile %s" % profile.name)

        # Check to see if this profile already exists
        profile_list = [pname.text for pname in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if profile.name in profile_list:
            # If this profile has already been created, fail the test
            ui_lib.fail_test("This Profile, %s, already exists. Cannot proceed with creation" % profile.name)

        # Check the server hardware power status
        serverhardwarelist = []
        if(profile.server != "unassigned"):
            if not selenium2lib._is_element_present(FusionServerHardwarePage.ID_PAGE_LABEL):
                base_page.navigate_base(FusionServerHardwarePage.ID_PAGE_LABEL,
                                        FusionUIBaseElements.ID_MENU_LINK_SERVER_HARDWARE, ProfileSanStorageElements.ID_CSS_PATH)
                serverhardwarelist = [sh.text for sh in selenium2lib._element_find(ProfileSanStorageElements.ID_SERVER_HARDWARE_TABLE,
                                                                                   False, False)]
                if profile.server in serverhardwarelist:
                    if not(serverhardware.power_off_server(profile.server)):
                        logger._warn("Can't proceed with server profile creation on server %s" % profile.server)
                        ui_lib.fail_test("Failing test")
                navigate()

        # Fill in the General section
        if not _fill_profile_general_info(profile):
            logger._warn("Unable to fill general section for profile %s" % profile.name)
            ui_lib.fail_test("Failing test")

        # Fill in the Connections section
        if not _fill_profile_connections_info(profile):
            logger._warn("Unable to fill connections section for profile %s" % profile.name)
            ui_lib.fail_test("Failing test")

        # Fill in the San Storage section
        if not _fill_profile_san_storage_info(profile):
            logger._warn("Unable to fill san storage section for profile %s" % profile.name)
            ui_lib.fail_test("Failing test")

        # Create server profile
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE)
        if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_VERIFY_MESS_CREATE_PROFILE, 5):
            logger._warn("Unable to create server profile %s" % profile.name)
            ui_lib.fail_test("Failing test")
        # Possibly get a warning about storage paths and volumes
        validationmsgs = []
        if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_STORAGE_PATHS_PROFILE, 15):
            logger._log_to_console_and_log_file("At least one volume created a warning related to storage paths")
            validationmsgs = ui_lib.get_text(ProfileSanStorageElements.ID_WARNING_STORAGE_PATHS_PROFILE)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE)
        elif ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_STORAGE_PATHS_PROFILE + "//span", 15):
            logger._log_to_console_and_log_file("At least one volume created a warning related to storage paths")
            validationmsgs = ui_lib.get_text(ProfileSanStorageElements.ID_WARNING_STORAGE_PATHS_PROFILE + "//span")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE)
        else:
            logger._log_to_console_and_log_file("No warning")
        done = False
        while not done:
            if ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_COMPLETED, 10):
                logger._log_to_console_and_log_file("Profile created")
                done = True
            elif ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_WARNING, 10):
                logger._warn("Profile updated in warning state")
                done = True
    logger._log_to_console_and_log_file("All profiles created")
    return validationmsgs


# ====================================================================================
# This keyword will be used to edit an already existing profile's san storage section
# The profile object only needs to have a volume section, and for each volume, it
# will either be added, modified, or deleted. A profile must have already been made
# Other sections will be edited if the profile object calls for it
# ====================================================================================
def edit_san_storage_profile(*profile_obj):
    selenium2lib = ui_lib.get_s2l()
    # Get to the server profile page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    # List of all the created profiles
    profile_names = [pname.text for pname in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
    for editprofile in profile_obj:
        if not (editprofile.name in profile_names):
            logger._warn("Cannot edit profile %s since it does not exist" % editprofile.name)
            ui_lib.fail_test("Failing test")

        # Assure Server Profile is powered as requested
        if(editprofile.has_property("power")):
            ui_lib.wait_for_element(FusionServerProfilesPage.ID_SERVER_POWER_STATUS)
            power_state = ui_lib.ignore_staleElementRefException("get_text", FusionServerProfilesPage.ID_SERVER_POWER_STATUS)
            if (power_state != editprofile.power):
                logger._warn("Server Profile must be powered %s before editing" % editprofile.power)
                status = False
                continue

        logger._log_to_console_and_log_file("Editing profile %s" % editprofile.name)
        # Select the profile from the sidebar
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % editprofile.name)

        # Edit General
        if (editprofile.has_property("newname") or editprofile.has_property("newdescription") or editprofile.has_property("newServerHardware")):
            # Select 'General'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_GENERAL_VIEW_MENU_OPEN)
            logger._log_to_console_and_log_file("Edit General...")
            # Select 'Overview' then 'General'  (make sure we're at the top of the page).
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_OVERVIEW)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_GENERAL_VIEW_MENU_OPEN)
            # Edit the 'Name' field
            if (editprofile.has_property("newname")):
                logger._log_to_console_and_log_file("Setting name to %s" % editprofile.newname)
                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_EDIT_SERVER_PROFILE_NAME, editprofile.newname)

            # Edit the 'Description' field
            if (editprofile.has_property("newdescription")):
                logger._log_to_console_and_log_file("Setting description to %s" % editprofile.newdescription)
                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_EDIT_SERVER_PROFILE_DESCRIPTION, editprofile.newdescription)

            if ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_PROFILE_POWER_OFF_LINK):

                # This function will power off the server hardware without navigate to Server Hardware page.
                if not (serverprofiles.__power_off_server_hardware()):
                    logger._warn("Unable to verify or power off the selected server hardware")

            if (editprofile.has_property("newServerHardware")):
                logger._log_to_console_and_log_file("Setting Server Hardware to %s" % editprofile.newServerHardware)
                # ui_lib.wait_for_element_and_click("css=div.hp-close")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_EDIT_DROPDOWN_SEARCH_SERVER_HARDWARE)
                if(selenium2lib._is_element_present(FusionServerProfilesPage.ID_LINK_SEARCH_FOR_ANOTHER)):
                    ui_lib.wait_for_element_and_click("//a[contains(text(),'Search for another')]")
                ui_lib.wait_for_element_and_input_text("//input[@id='cic-profile-edit-server-input']", editprofile.newServerHardware[-6:])
                if ui_lib.wait_for_element_and_click("//span[contains(text(),'%s')]/.." % editprofile.newServerHardware):
                    logger._log_to_console_and_log_file("Selected valid server hardware")
                else:
                    logger._log_to_console_and_log_file("Please pass valid server hardware (%s)" % editprofile.newServerHardware)
            # Don't hit OK just yet! There may be other things to edit

        # Manage network connections
        if not _edit_profile_connetions(editprofile):
            logger._warn("Unable to edit the connections for the profile")
            ui_lib.fail_test("Failing Test")

        # Get the number of connections this profile has
        num_connections = 0
        if ui_lib.is_visible(ProfileSanStorageElements.ID_NUMBER_OF_CONNECTIONS):
            num_connections = int(str(ui_lib.get_text(ProfileSanStorageElements.ID_NUMBER_OF_CONNECTIONS)))

        # Edit San Storage
        if not _edit_profile_san_storage_section(editprofile, num_connections):
            logger._warn("Unable to edit san storage section")
            ui_lib.fail_test("Failing test")

        # Save the profile
        validationmsgs = []
        logger._log_to_console_and_log_file("Updating profile and clicking OK")
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_OK_EDIT_PROFILE)
        if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_VERIFY_MESS_CREATE_PROFILE, 5):
            logger._warn("Unable to create server profile %s" % editprofile.name)
            ui_lib.fail_test("Failing test")
        # Possibly get a warning about storage paths and volumes
        if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_UPDATE_PROFILE, 7):
            logger._warn("One of the volumes has a warning with its connections")
            validationmsgs = ui_lib.get_text(ProfileSanStorageElements.ID_WARNING_UPDATE_PROFILE)
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_OK_EDIT_PROFILE)
        done = False
        while not done:
            if ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_COMPLETED, 10):
                logger._log_to_console_and_log_file("Profile updated")
                done = True
            elif ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_WARNING, 10):
                logger._warn("Profile updated in warning state")
                done = True
    return validationmsgs


# ====================================================================================
# This keyword will delete the profiles passed in. It will do some checking regarding
# san storage in that if the profile has non-permanent volumes associated with it,
# a warning should be displayed. The profile must already be set up. If a complex
# profile is being used, it may be useful to use the keyword "Fusion UI Delete Server
# Profiles" as that provides much more comprehensive validation for other areas of
# a server profile
# ====================================================================================
def delete_pmsan_server_profile(*profile_obj):
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    # Go through each profile and delete it
    for deleteprofile in profile_obj:
        # Check to make sure this profile exists
        profile_list = [pname.text for pname in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
        if not (deleteprofile.name in profile_list):
            # If this profile has already been created, fail the test
            ui_lib.fail_test("This Profile, %s, does not exist. Cannot proceed with deletion" % deleteprofile.name)

        # Now it can be deleted, so select it from the sidebar
        logger._log_to_console_and_log_file("Deleting profile %s" % deleteprofile.name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % deleteprofile.name)
        # Click on delete from the action menu
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
        if selenium2lib._is_visible(FusionServerProfilesPage.ID_MENU_ACTION_DELETE):
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_DELETE)
            # Now if the profile has non-permanent volumes, a warning message should appear
            if deleteprofile.has_property("nonpermanentvolume"):
                if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_DELETE_PROFILE_LOSE_SAN):
                    logger._warn("No warning about losing san storage when deleting profile")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("no_warning_delete_profile_nonpermanent_volume.png")
                    ui_lib.fail_test("Failing test")
                else:
                    # Warning should have been displayed
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_DELETE_PROFILE_YES)
            # Otherwise don't expect a warning, there shouldn't be one
            else:
                if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_DELETE_PROFILE_LOSE_SAN):
                    logger._warn("Warning about losing san for profile with no non-permanent volumes")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("warning_when_deleting_profile_unexpected.png")
                    ui_lib.fail_test("Failing Test")
                else:
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_DELETE_PROFILE_YES)
        else:
            logger._warn("The delete button is not appearing")
            selenium2lib.capture_page_screenshot("no_delete_button.png")
            ui_lib.fail_test("Failing test")
        # Now wait for the confirmation that the profile has been deleted
        done = False
        while not done:
            if ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_COMPLETED, 10):
                logger._log_to_console_and_log_file("Profile deleted")
                done = True
            elif ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_WARNING, 10):
                logger._warn("Profile deleted in warning state")
                done = True
    return True


# ====================================================================================
# This keyword will check to see that the right messages are displayed when incorrect
# values are input to the various sections in san storage. A profile will be configured
# such that the general and connections sections are set up correctly, and then the
# input checking will happen in the san storage section
# ====================================================================================
def validate_invalid_san_elements_in_profile(*profile_obj):
    selenium2lib = ui_lib.get_s2l()
    # Get to the server profile page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    for profile in profile_obj:
        # Fill in the general section
        if not _fill_profile_general_info(profile):
            logger._warn("Unable to fill general section for profile %s" % profile.name)
            ui_lib.fail_test("Failing test")
        # Fill in the connections section
        if not _fill_profile_connections_info(profile):
            logger._warn("Unable to fill connections section for profile %s" % profile.name)
            ui_lib.fail_test("Failing test")
        # Check invalid input for san storage
        if not _validate_invalid_san_input(profile):
            logger._warn("Some invalid input was accedpted as valid")
            ui_lib.fail_test("Failing test")

        logger._log_to_console_and_log_file("Invalid input was correctly refused")
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
    return True


# ====================================================================================
# This keyword will be used to verify that the volume configurations for a profile
# are consistent between the san storage area of the server profile page, the edit
# profile dialogue, and that both of these areas have information that matches
# the configuration of the volumes in the volumes object. The volume object passed in
# must have all the volumes for a profile, with the correct configuration based on
# operations that have happened to the profile already
# ====================================================================================
def verify_volume_configuration_for_profile(profile_name, *volumes_obj):
    selenium2lib = ui_lib.get_s2l()
    # Get to the server profile page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()
    if isinstance(volumes_obj, test_data.DataObj):
        volumes_obj = [volumes_obj]
    elif isinstance(volumes_obj, tuple):
        volumes_obj = list(volumes_obj[0])

    logger._log_to_console_and_log_file("Attempting to verify volume configurations for profile: %s" % profile_name)
    # First check that the profile exists
    profile_names = [pname.text for pname in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]
    if not (profile_name in profile_names):
        logger._warn("This profile has not been created yet")
        ui_lib.fail_test("Failing test")
    # Select the profile from the sidebar
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile_name)

    # Verify the configuration in the edit profile section first
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_OVERVIEW)
    if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_EDIT_ICON):
        logger._warn("Unable to access edit profile dialogue")
        ui_lib.fail_test("Failing test")
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_EDIT_MENU_DROP_DOWN, 10)
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_LINK_EDIT)
    # Run the verification on the table
    if not _verify_volume_table(volumes_obj, ProfileSanStorageElements.ID_STORAGE_VOLUMES_TABLE):
        logger._warn("The edit profile configuration did not match the actual configuration")
        ui_lib.fail_test("Failing test")
    logger._log_to_console_and_log_file("All volumes' information is correct in edit profile section")
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL_EDIT_PROFILE)

    # Verify the configuration in the san storage section now
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_PROFILE_LINK)
    if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_SAN_STORAGE_TITLE):
        logger._warn("Unable to access san storage section of server profile")
        ui_lib.fail_test("Failing test")
    # Run the verification on the table
    if not _verify_volume_table(volumes_obj, ProfileSanStorageElements.ID_VOLUME_ATTACHMENTS_TABLE):
        logger._warn("The san storage configuration did not match the actual configuration")
        ui_lib.fail_test("Failing test")
    logger._log_to_console_and_log_file("All volumes' information is correct in san storage section")
    return True


# ====================================================================================
# This keyword will be used to check that the correct volumes are shown in the volume
# section. Requires that the profile has already been deleted
# ====================================================================================
def verify_volume_section_of_fusion(*volume_obj):
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionStorageVolumesPage.ID_PAGE_LABEL):
        volumes.navigate()
    # Now we're on the volumes page, so get a list of the volume names on the side bar
    storagevolumes = []
    storagevolume_list = [str(s.text.lower()) for s in selenium2lib._element_find(FusionStorageVolumesPage.ID_ALL_VOLUMES_LIST, False, False)]
    # Now check the list to make sure the correct volumes are listed
    if isinstance(volume_obj, test_data.DataObj):
        volume_obj = [volume_obj]
    elif isinstance(volume_obj, tuple):
        volume_obj = list(volume_obj[0])
    logger._log_to_console_and_log_file("Checking the status of the volumes")
    for volume in volume_obj:
        if volume.has_property("remain"):
            # this volume should still be present
            if volume.name.lower() not in storagevolume_list:
                logger._warn("The volume %s should be in the list, but isn't" % volume.name)
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("No_volume_name.png")
                ui_lib.fail_test("Failing Test", False)
            else:
                logger._log_to_console_and_log_file("The volume %s correctly remains" % volume.name)
        else:
            # this volume should not be here
            if volume.name in storagevolume_list:
                logger._warn("The volume %s should have been deleted, but still remains" % volume.name)
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("volume_still_present.png")
                ui_lib.fail_test("Failing Test", False)
            else:
                logger._log_to_console_and_log_file("The volume %s was correctly deleted" % volume.name)
    logger._log_to_console_and_log_file("The volumes were handled correctly after profile deletion")
    return True


# ====================================================================================
# This keyword will be used to check whether the san storage page, and the edit
# profile section of the server profile render in the given time. This should be used
# to verify that certain fusion time requirements are met. It will return true if the
# pages render in the given time, and false if it takes too long. The time to render
# will be output to the console. The render time should be passed in as ms
# ====================================================================================
def verify_render_time_for_san_storage(render_time, *profile_obj):
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    # First place we'll check is in the san storage section
    render_time = int(render_time)
    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])
    profile_list = [el.text for el in selenium2lib._element_find(FusionServerProfilesPage.ID_PROFILE_LIST_NAMES, False, False)]

    pass_test = True

    # go through all the profiles
    for profile in profile_obj:
        if not (profile.name in profile_list):
            logger._warn("This profile has not been created yet, so cannot view")
            ui_lib.fail_test("Failing test")
        logger._log_to_console_and_log_file("Selecting profile %s to view both san storage sections" % profile.name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % profile.name)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_OVERVIEW)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_EDIT_ICON)

        # Get the start time before going to the san storage section
        start_time = int(round(time.time() * 1000))
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_EDIT_MENU_DROP_DOWN)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_LINK_EDIT)
        # Now wait for the table to become visible (wait a max of 2 minutes)
        ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_STORAGE_VOLUMES_TABLE, 120)
        end_time = int(round(time.time() * 1000))
        total_time = end_time - start_time
        logger._log_to_console_and_log_file("The san storage table took %d ms to load (edit profile)" % total_time)
        if render_time < total_time:
            logger._warn("The edit profile san storage table took too long to load")
            pass_test = False

        # Now go to the san storage section of profile view
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL_EDIT_PROFILE)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_OVERVIEW)
        # Get the start time before going to the san storage section
        start_time = int(round(time.time() * 1000))
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_PROFILE_LINK)
        # Now wait for the table to become visible (wait a max of 2 minutes)
        ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_VOLUME_ATTACHMENTS_TABLE, 120)
        end_time = int(round(time.time() * 1000))
        total_time = end_time - start_time
        logger._log_to_console_and_log_file("The san storage table took %d ms to load (sanstorage overview)" % total_time)
        # check to see if the profile passed
        if render_time < total_time:
            logger._warn("The san storage table took too long to load")
            pass_test = False

        if not pass_test:
            logger._warn("At least one of the sections took too long to render in under %d ms" % render_time)
            ui_lib.fail_test("Failing test")
        logger._log_to_console_and_log_file("Both sections rendered in under %d ms" % render_time)
        return True


# ====================================================================================
# This keyword can be used to easily uncheck manage san storage from a profile
# It will go through the list of profiles passed in and uncheck the manage san
# storage checkbox, and save the profile update
# ====================================================================================
def uncheck_manage_san_storage_of_profile(*profile_obj):
    selenium2lib = ui_lib.get_s2l()
    # Get to the server profile page
    if not selenium2lib._is_element_present(FusionServerProfilesPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(profile_obj, test_data.DataObj):
        profile_obj = [profile_obj]
    elif isinstance(profile_obj, tuple):
        profile_obj = list(profile_obj[0])

    logger._log_to_console_and_log_file("About to unmanage san storage for the profiles")
    # Go through all the profiles
    for editprofile in profile_obj:
        logger._log_to_console_and_log_file("Unmanaging san storage for %s" % editprofile.name)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_PROFILE_NAME_BASE % editprofile.name)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_OVERVIEW)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_EDIT_ICON)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_EDIT_MENU_DROP_DOWN)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_LINK_EDIT)
        # Click on the checkbox if its visible
        if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_CHKBOX_SAN_STORAGE_EDIT):
            logger._warn("Unable to see the san storage checkbox")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("no_manage_san_storage_checkbox.png")
            ui_lib.fail_test("Failing test")
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_CHKBOX_SAN_STORAGE_EDIT)
        logger._log_to_console_and_log_file("Updating %s" % editprofile.name)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_OK_EDIT_PROFILE)
        # Should get a warning if the profile has nonpermanentvolumes
        if editprofile.has_property("nonpermanentvolume"):
            if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_UNMANAGE_SAN_STORAGE):
                logger._warn("No warning for unmanaging san storage")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("no_warning_for_deleting_san_storage.png")
                ui_lib.fail_test("Failing Test")
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_DELETE_NON_PERMANENT_VOLUME)
        else:
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_OK_EDIT_PROFILE)
        if not ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_VERIFY_MESS_CREATE_PROFILE, 5):
            logger._warn("Unable to create server profile %s" % editprofile.name)
            ui_lib.fail_test("Failing test")
        done = False
        while not done:
            if ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_COMPLETED, 10):
                done = True
            elif ui_lib.is_visible(ProfileSanStorageElements.ID_PROFILE_CREATION_WARNING, 10):
                logger._warn("Profile updated in warning state")
                done = True
    return True

# ====================================================================================
# Private helper functions for keywords above
# ====================================================================================


# Method for filling in the general section when creating a profile
def _fill_profile_general_info(profile):
    selenium2lib = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Filling in general section for profile %s" % profile.name)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CREATE_SERVER_PROFILES)
    # Fill in profile name
    ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME)
    selenium2lib.input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_NAME, profile.name)

    # Fill in the description if applicable
    if (profile.has_property("profile")):
        logger._log_to_console_and_log_file("Filling in profile description")
        ui_lib.wait_for_element_visible(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION)
        selenium2lib.input_text(FusionServerProfilesPage.ID_INPUT_SERVER_PROFILE_DESCRIPTION, profile.profile)

    # Select hardware
    logger._log_to_console_and_log_file("Selecting hardware")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN)
    logger._log_to_console_and_log_file("Creating profile for server %s" % profile.server)
    if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.server, 10):
        logger._log_to_console_and_log_file("Selected valid hardware")
    else:
        logger._warn("Please pass valid server hardware")
        _cancel_profile_creation()
        return False

    # If hardware is unassigned, select the other mandatory fields
    if (profile.server.lower() == "unassigned"):
        if (not hasattr(profile, "hardwaretype") or profile.hardwaretype == "" or profile.enclgroup == ""):
            logger._warn("Mandatory fields (hardwaretype or enclgroup) cannot be left emtpy for unassigned server hardware")
            _cancel_profile_creation()
            return False
        else:
            # Select hardware type
            logger._log_to_console_and_log_file("Selecting hardware for profile")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_SERVER_HARDWARE_DROPDOWN)
            if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.hardwaretype):
                logger._log_to_console_and_log_file("Selected valid hardware type")
            else:
                logger._warn("Please provide valid hardware")
                _cancel_profile_creation()
                return False
            # Select enclosure group
            logger._log_to_console_and_log_file("Selecting enclosure group for unassigned profile")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_COMBO_ENCLOSURE_GROUP_DROPDOWN)
            if ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_ELEMENT_NETWORK_NAME_BASE % profile.enclgroup):
                logger._log_to_console_and_log_file("Selected valid enclosure group")
            else:
                logger._warn("Did not select valid enclosure group")
                _cancel_profile_creation()
                return False
    # Otherwise, verify the auto-filled sections
    else:
        # Verify Server hardware type
        if (hasattr(profile, 'hardwaretype') and profile.hardwaretype != ""):
            logger._log_to_console_and_log_file("Verify server hardware type: %s" % profile.hardwaretype)
            if not ui_lib.wait_for_element_text("//label[@id='cic-profile-add-server-type']", profile.hardwaretype):
                logger._warn("Failed to verify Server Hardware Type.")
                _cancel_profile_creation()
                return False
        else:
            logger._log_to_console_and_log_file("No hardware type, not verifying")

        if "DL" not in profile.hardwaretype:
            # Verify Enclosure Group
            logger._log_to_console_and_log_file("Verify enclosure group: %s" % profile.enclgroup)
            if not ui_lib.wait_for_element_text("//label[@id='cic-profile-add-enclosure-group']", profile.enclgroup):
                logger._warn("Failed to verify Enclosure Group.")
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)
                return False

    if "DL" not in profile.hardwaretype:
        # Selecting the Affinity
        if(profile.has_property("affinity") and profile.affinity != ""):
            logger._log_to_console_and_log_file("Selecting affinity..")
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN)
            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN_SELECT % profile.affinity)
            if (selenium2lib.get_text(FusionServerProfilesPage.ID_AFFINITY_DROP_DOWN) != profile.affinity):
                logger._warn("Failed to select affinity..")
                _cancel_profile_creation()
                return False
    return True


# helper function to cancel profile creation
def _cancel_profile_creation():
    logger._warn("Canceling profile")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)


# method to fill out connections section
def _fill_profile_connections_info(profile):
    selenium2lib = ui_lib.get_s2l()

    # Navigate to the connections area
    if (profile.has_property("connection") and len(profile.connection) > 0):
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_ADD_MENU_DROP_DOWN)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_CONNECTIONS)
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION)

        if type(profile.connection) is test_data.DataObj:
            profile.connection = [profile.connection]
        elif type(profile.connection) is tuple:
            profile.connection = list(profile.connection[0])

        for connection in profile.connection:
            # Selecting connection type
            if (connection.type.upper() in ["FIBRE CHANNEL", "ETHERNET"]):
                # Validating mandatory fields
                if ((not connection.has_property("network")) or (not connection.has_property("type"))):
                    logger._warn("Network name and type are mandatory fields for connections")
                    _cancel_connection()
                    return False
                logger._log_to_console_and_log_file("Selecting connection type")
                __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_CONNECTION_FUNCTION_TYPE,
                                                        FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (connection.type, connection.type))
            else:
                logger._warn("Invalid connection type")
                _cancel_connection()
                return False
            # Add connection name
            if (connection.has_property("name") and connection.name != ""):
                logger._log_to_console_and_log_file("Adding connection %s" % connection.name)
                selenium2lib.input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.name)
            # Add connection network
            logger._log_to_console_and_log_file("Selecting Network")
            __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_NETWORK_ADD_CONNECTION,
                                                    FusionServerProfilesPage.ID_ELEMENT_NETWORK_ADD_CONNECTION % connection.network)

            # Selecting Port Name
            if connection.has_property("portName") and connection.portName != "":
                logger._log_to_console_and_log_file("Selecting port")
                __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_FLEXNIC_ADD_CONNECTION,
                                                        FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT % connection.portName)

            # Fill in bandwith
            if connection.has_property("band") and connection.band != "":
                selenium2lib.input_text(ProfileSanStorageElements.ID_CONNECTION_BANDWITH, connection.band)
                if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_INCORRECT_BANDWITH):
                    logger._warn("Incorrect bandwith")
                    _cancel_connection()
                    return False

            # Selecting Boot
            if (connection.has_property("boot") and (connection.boot.upper() == "PRIMARY" or connection.boot.upper() == "SECONDARY")):
                logger._log_to_console_and_log_file("Selecting Boot")
                __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_BOOT_ADD_CONNECTION,
                                                        FusionServerProfilesPage.ID_ELEMENT_BOOT_ADD_CONNECTION % connection.boot)

                if connection.type.upper() == "FIBRE CHANNEL":
                    if (connection.has_property("targetwwpn") and connection.targetwwpn != "" and connection.has_property("targetlun") and connection.targetlun != ""):
                        logger._log_to_console_and_log_file("Specifying Boot Order")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_SPECIFIY_BOOT_TARGET)
                        logger._log_to_console_and_log_file("Typing target WWPN")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET, connection.targetwwpn)
                        logger._log_to_console_and_log_file('typing target LUN')
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET, connection.targetlun)
                    else:
                        logger._log_to_console_and_log_file("Not bootable connection")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USE_BIOS)

                    if (connection.has_property("wwpn") and connection.wwpn != "" and connection.has_property("wwnn") and connection.wwnn != ""):
                        logger._log_to_console_and_log_file("Selecting use user specified IDs checkbox.")
                        selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                        logger._log_to_console_and_log_file("Typing WWPN")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN, connection.wwpn)
                        logger._log_to_console_and_log_file("Typing WWNN")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN, connection.wwnn)
                        if connection.has_property("macaddress") and connection.macaddress != "":
                            logger._log_to_console_and_log_file("Typing Mac address")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macaddress)
                # otherwise must be ethernet since it was already checked prior
                else:
                    if connection.has_property("macaddress") and connection.macaddress != "":
                        logger._log_to_console_and_log_file("Selecting use user specified IDs checkbox.")
                        selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                        logger._log_to_console_and_log_file("Typing Mac Address")
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                        ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macadress)
                    if (profile.connection.index(connection) < (len(profile.connection) - 1)):
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON)
                        logger._log_to_console_and_log_file("Adding the next connection")
                    else:
                        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON)
                        logger._log_to_console_and_log_file("Adding last connection")
            if (profile.connection.index(connection) < (len(profile.connection) - 1)):
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_PLUS_CONNECTON)
                logger._log_to_console_and_log_file("Adding the next connection")
            else:
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON)
                logger._log_to_console_and_log_file("Adding last connection")

        # Validate the connections
        logger._log_to_console_and_log_file("Verifying that the connections are correctly displayed (by name)")
        for connection in profile.connection:
            if connection.has_property("name"):
                if ui_lib.is_visible(FusionServerProfilesPage.ID_PROFILE_CONNECTION_ELEMENT_BY_NAME % connection.name):
                    logger._log_to_console_and_log_file("Connection %s was successfully created" % connection.name)
                else:
                    logger._warn("Connection %s was not found in the connection table" % connection.name)
                    return False
    return True


# helper function to cancel connection
def _cancel_connection():
    logger._warn("Canceling connections")
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_ADD_CONNECTION)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CANCEL_SERVER_PROFILE)


# method for filling in the san storage section
def _fill_profile_san_storage_info(profile):
    selenium2lib = ui_lib.get_s2l()
    if profile.has_property("sanstorage"):
        logger._log_to_console_and_log_file("Adding San Storage")
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_ADD_MENU_DROP_DOWN)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_LINK_ADD)

        # Click manage san storage
        if not ui_lib.wait_for_checkbox_and_select(ProfileSanStorageElements.ID_CHKBOX_SAN_STORAGE_ADD):
            logger._warn("Unable to Select Manage San Storage")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("cannot_manage_san.png")
            _cancel_profile_creation()
            return False

        if type(profile.sanstorage) is test_data.DataObj:
            profile.sanstorage = [profile.sanstorage]
        elif type(profile.sanstorage) is tuple:
            profile.sanstorage = list(profile.sanstorage[0])

        # Add each storage volume
        lun_list = []
        for sanstorage in profile.sanstorage:
            if sanstorage.san.lower() == "true":
                logger._log_to_console_and_log_file("Adding sanstorage volume %s" % sanstorage.sanvolume)

                # Fill in OS Type
                if sanstorage.has_property("ostype") and sanstorage.ostype != "":
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_OS_TYPE_DROP_DOWN)
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_OS_TYPE_SELECT % sanstorage.ostype)
                    if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_NO_STORAGE_VOLUMES):
                        logger._warn("No storage volumes are available for assigning to the servers")
                        logger._log_to_console_and_log_file("Capturing screenshot")
                        selenium2lib.capture_page_screenshot("no_storage_volumes_available.png")
                        _cancel_profile_creation()
                        return False
                if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_ADD_STORAGE):
                    logger._warn("Unable to click add storage volume")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_click_add_storage_volume.png")
                    _cancel_profile_creation()
                    return False
                # duplicate lun test. check to see if the lun already exists
                if sanstorage.sanlun in lun_list and sanstorage.sanlun != "":
                    if not _add_volume_with_duplicate_lun(sanstorage):
                        return False
                else:
                    if sanstorage.sanlun != "":
                        lun_list.append(sanstorage.sanlun)
                    if profile.has_property("connection"):
                        length = len(profile.connection)
                    else:
                        length = 0
                    if not _add_a_volume(sanstorage, length):
                        return False
        return True
    else:
        logger._log_to_console_and_log_file("No San Storage to add")
        return True


# method to fill the general form for sanstorage
def _fill_sanstorage_general_form(sanstorage):
    logger._log_to_console_and_log_file("Creating new sanstorage volume %s" % sanstorage.sanvolume)
    # Add name
    if sanstorage.has_property("sanvolume") and sanstorage.sanvolume != "":
        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_NAME, sanstorage.sanvolume)
    else:
        logger._warn("No name given for volume")
        return False
    # Add description
    if sanstorage.has_property("description") and sanstorage.description != "":
        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_DESCRIPTION, sanstorage.description)
    if sanstorage.has_property("sanlun") and sanstorage.sanlun != "":
        # set lun to manual
        ui_lib.wait_for_checkbox_and_select(ProfileSanStorageElements.ID_LUN_BTN_MANUAL)
        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_TEXT_LUN, sanstorage.sanlun)
    else:
        # keep lun as auto
        ui_lib.wait_for_checkbox_and_select(ProfileSanStorageElements.ID_LUN_BTN_AUTO)
    return True


# method to fill the volume properties for sanstorage
def _fill_sanstorage_properties(sanstorage):
    logger._log_to_console_and_log_file("Filling in volume properties")
    # Select storage pool
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_NEW_VOLUME_STORAGE_POOL_DROP_DOWN)
    if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_NEW_VOLUME_STORAGE_POOL_SELECT % sanstorage.storagepool):
        selenium2lib.capture_page_screenshot("cannot_select_storage_pool.png")
        logger._warn("Unable to select a valid storage pool")
        logger._log_to_console_and_log_file("Capturing screenshot")
        return False
    # Fill in capacity
    if sanstorage.has_property("capacity") and sanstorage.capacity != "":
        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_CAPACITY, sanstorage.capacity)
        logger._log_to_console_and_log_file("Inputing the capacity of %s as %s" % (sanstorage.sanvolume, sanstorage.capacity))
        if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_CAPACITY_ERROR):
            selenium2lib.capture_page_screenshot("invalid_capacity_input.png")
            logger._warn("Not a valid capacity")
            logger._log_to_console_and_log_file("Capturing screenshot")
            return False
    else:
        logger._log_to_console_and_log_file("Keeping capacity as default 10 GiB")
    # Select provisioning
    if sanstorage.has_property("provisioning") and sanstorage.provisioning != "":
        logger._log_to_console_and_log_file("Selecting provisioning")
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROVISIONING_DROP_DOWN)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROVISIONING_SELECT % sanstorage.provisioning)
    else:
        logger._log_to_console_and_log_file("Keeping provisioning as default Thin")
    if sanstorage.has_property("permanent") and sanstorage.permanent.upper() == "FALSE":
        logger._log_to_console_and_log_file("Making the volume non-permanent")
        ui_lib.wait_for_checkbox_and_unselect(ProfileSanStorageElements.ID_CHKBOX_PERMANENT)
    else:
        logger._log_to_console_and_log_file("Leaving volume as default permanent")
    return True


# method to add storage paths to a sanstorage volume
def _add_storage_paths(sanstorage):
    if sanstorage.has_property("connection"):
        if isinstance(sanstorage.connection, test_data.DataObj):
            sanstorage.connection = [sanstorage.connection]
        elif isinstance(sanstorage.connection, tuple):
            sanstorage.connection = list(sanstorage.connection[0])
        # Add the storage paths defined in the sanstorage object
        # Click on remove all to start from scratch
        if ui_lib.is_visible(ProfileSanStorageElements.ID_BTN_STORAGE_PATHS_REMOVE_ALL):
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_PATHS_REMOVE_ALL)
        if not ui_lib.is_visible(ProfileSanStorageElements.ID_WARNING_NO_STORAGE_PATHS):
            logger._warn("No message about no storage paths associate with volume")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("no_storage_paths_missing_warning.png")
            return False
        num_cons = 0
        for connection in sanstorage.connection:
            # Check the zero connection case first (1 connection with no name)
            if (not connection.has_property("name")) and (len(sanstorage.connection) == 1):
                continue
            # check to see if it is already in the table
            if not ui_lib.wait_for_element_text(ProfileSanStorageElements.ID_STORAGE_PATHS_TABLE, connection.name):
                logger._log_to_console_and_log_file("Adding storage path")
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_ADD_STORAGE_PATH)
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_ADD_SPECIFIC_STORAGE_PATHS % connection.name)
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CONFIRM_ADD_STORAGE_PATH)
                # check to see it has been added to the table
                if not ui_lib.wait_for_element_text(ProfileSanStorageElements.ID_STORAGE_PATHS_TABLE, connection.name, 10):
                    logger._warn("Unable to add the storage path")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("cannot_select_storage_path.png")
                    return False
            # target ports configuration
            if not _edit_storage_target_ports(connection):
                logger._warn("Unable to configure storage target ports")
                return False
            num_cons += 1
        # Now add the volume, expecting warnings in some cases
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
        if num_cons == 1:
            if not ui_lib.is_visible(ProfileSanStorageElements.ID_WARNING_STORAGE_PATHS_VOLUME):
                logger._warn("No warning for redundant paths shown")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("no_redundant_path_warning.png")
                return False
            else:
                logger._log_to_console_and_log_file("Warning correctly shown")
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
    return True


# method to edit storage target port
def _edit_storage_target_ports(connection):
    if connection.has_property("port"):
        if isinstance(connection.port, test_data.DataObj):
            connection.port = [connection.port]
        elif isinstance(connection.port, tuple):
            connection.port = list(connection.port[0])
        logger._log_to_console_and_log_file("Editing storage target ports")
        if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_EDIT_STORAGE_TARGETS % connection.name):
            logger._warn("Unable to click on gear icon for %s" % connection.name)
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("cannot_click_gear_icon_storage_targets.png")
            return False
        # Click on storage ports to edit
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_STORAGE_EDIT_TARGETS_MANUAL)
        num_ports = 0
        for port in connection.port:
            if ui_lib.wait_for_element_text(ProfileSanStorageElements.ID_STORAGE_TARGETPORTS_TABLE, port.target):
                # There are various checks to go through depending on if this is coming from and edit request
                if port.has_property("enabled"):
                    num_ports += 1
                    # check to see if the checkbox is enabled already
                    if ui_lib.is_visible((ProfileSanStorageElements.ID_STORAGE_TARGETPORTS_ENABLE_CHKBOX + "[@checked]") % port.target):
                        logger._log_to_console_and_log_file("This storage target is already enabled")
                    else:
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_STORAGE_TARGETPORTS_ENABLE_CHKBOX % port.target)
                elif port.has_property("disabled"):
                    if ui_lib.is_visible((ProfileSanStorageElements.ID_STORAGE_TARGETPORTS_ENABLE_CHKBOX + "[@checked]") % port.target):
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_STORAGE_TARGETPORTS_ENABLE_CHKBOX % port.target)
                    else:
                        logger._log_to_console_and_log_file("This storage target is already disabled")
                # otherwise this must be coming from an add profile request, so all are initialized to unchecked
                else:
                    ui_lib.wait_for_checkbox_and_select(ProfileSanStorageElements.ID_STORAGE_TARGETPORTS_ENABLE_CHKBOX % port.target)
                    num_ports += 1
            else:
                logger._warn("Unable to select the given port %s" % port.target)
                selenium2lib.capture_page_screenshot("unable_to_select_given_port.png")
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL_STORAGE_TARGETS)
                return False
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_OK_STORAGE_TARGETS)
        # If all ports have been disabled, expect a message
        if num_ports == 0:
            if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_NO_STORAGE_TARGETS):
                logger._warn("Expected an error message but got none")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("no_error_meesage_for_storage_paths")
                return False
            else:
                logger._log_to_console_and_log_file("Got the error message that was expected. Clicking cancel")
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL_2)
        elif ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_NO_STORAGE_TARGETS) and num_ports != 0:
            selenium2lib.capture_page_screenshot("unexpected_no_storage_targets_error.png")
            logger._warn("Warning for no storage targets when some were selected")
            logger._log_to_console_and_log_file("Capturing screenshot")
            return False
    return True


# method to test invalid san storage input (does not include duplicate lun)
def _validate_invalid_san_input(profile):
    if profile.has_property("sanstorage"):
        logger._log_to_console_and_log_file("Adding San Storage")
        ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_LINK_SANSTORAGE)

        # Click manage san storage
        if not ui_lib.wait_for_checkbox_and_select(ProfileSanStorageElements.ID_CHKBOX_SAN_STORAGE_ADD):
            logger._warn("Unable to Select Manage San Storage")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("unable_to_manage_san_storage.png")
            _cancel_profile_creation()
            return False

        if type(profile.sanstorage) is test_data.DataObj:
            profile.sanstorage = [profile.sanstorage]
        elif type(profile.sanstorage) is tuple:
            profile.sanstorage = list(profile.sanstorage[0])

        # Add each storage volume
        for sanstorage in profile.sanstorage:
            if sanstorage.san.lower() == "true":
                logger._log_to_console_and_log_file("Adding sanstorage volume %s" % sanstorage.sanvolume)

                # Fill in OS Type
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_OS_TYPE_DROP_DOWN)
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_OS_TYPE_SELECT % sanstorage.ostype)
                if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_NO_STORAGE_VOLUMES):
                    logger._warn("No storage volumes are available for assigning to the servers")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("no_available_volumes.png")
                    _cancel_profile_creation()
                    return False
                if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_ADD_STORAGE):
                    logger._warn("Unable to click add storage volume")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_click_add_storage.png")
                    _cancel_profile_creation()
                    return False

                # Now validate invalid input if a new volume
                if (sanstorage.has_property("volumetype") and sanstorage.volumetype.upper() == "NEW VOLUME"):
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_TYPE_DROP_DOWN)
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_TYPE_NEW)

                    # Since this volume should have all incorrect values, make sure the correct errors pop up
                    # check empty inputs first
                    ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
                    if not (ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_NO_VOLUME_NAME_INPUT) and
                            ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_INVALID_STORAGE_POOL)):
                        logger._warn("Failed to catch empty input for name or storage pool")
                        logger._log_to_console_and_log_file("Capturing screenshot")
                        selenium2lib.capture_page_screenshot("no_error_for_empty_input_in_san.png")
                        return False
                    ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_NAME, sanstorage.sanvolume)
                    # check for too long a description
                    if sanstorage.has_property("description") and sanstorage.description != "":
                        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_DESCRIPTION, sanstorage.description)
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
                        if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_DESCRIPTION_TOO_LONG):
                            logger._warn("Failed to catch an oversize description")
                            logger._log_to_console_and_log_file("Capturing screenshot")
                            selenium2lib.capture_page_screenshot("no_error_for_long_description.png")
                            return False

                    # check for incorrect lun
                    if sanstorage.has_property("sanlun") and sanstorage.sanlun != "":
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_LUN_BTN_MANUAL)
                        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_TEXT_LUN, sanstorage.sanlun)
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
                        if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_INCORRECT_LUN):
                            logger._warn("Failed to catch incorrect lun")
                            logger._log_to_console_and_log_file("Capturing screenshot")
                            selenium2lib.capture_page_screenshot("no_error_for_incorrect_lun.png")
                            return False

                    # check for incorrect storage pool
                    if sanstorage.has_property("storagepool") and sanstorage.storagepool != "":
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_NEW_VOLUME_STORAGE_POOL_DROP_DOWN)
                        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_STORAGE_POOL_INPUT,
                                                               sanstorage.storagepool)
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
                        if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_INCORRECT_STORAGE_POOL_NAME):
                            logger._warn("Failed to catch incorrect storage pool")
                            logger._log_to_console_and_log_file("Capturing screenshot")
                            selenium2lib.capture_page_screenshot("no_error_for_incorrect_storage_pool.png")
                            return False

                    # check for incorrect capacity
                    if sanstorage.has_property("capacity") and sanstorage.capacity != "":
                        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_CAPACITY, sanstorage.capacity)
                        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
                        if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_INVALID_CAPACITY):
                            logger._warn("Failed to catch incorrect capacity")
                            logger._log_to_console_and_log_file("Capturing screenshot")
                            selenium2lib.capture_page_screenshot("no_error_for_invalid_capacity.png")
                            return False
                    logger._log_to_console_and_log_file("Successfully caught all invalid input errors")
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL)
        return True
    return True


# method to add a volume
def _add_a_volume(sanstorage, num_connections):
    selenium2lib = ui_lib.get_s2l()
    # Fill in New Volume Form
    if sanstorage.has_property("volumetype") and sanstorage.volumetype.upper() == "NEW VOLUME":
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_TYPE_DROP_DOWN)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_TYPE_NEW)

        # Fill general form
        if not _fill_sanstorage_general_form(sanstorage):
            logger._warn("Unable to fill general section for sanstorage")
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL)
            _cancel_profile_creation()
            return False

        # Fill properties form
        if not _fill_sanstorage_properties(sanstorage):
            logger._warn("Unable to fill sanstorage volume properties")
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL)
            _cancel_profile_creation()
            return False

    # Fill in Existing Volume Form
    else:
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_SELECT_DROPDOWN)
        if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_SELECT % sanstorage.sanvolume):
            logger._warn("The specified existing volume %s does not exist" % sanstorage.sanvolume)
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("volume_does_not_exist.png")
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL)
            _cancel_profile_creation()
            return False
        if sanstorage.has_property("sanlun") and sanstorage.sanlun != "":
            logger._log_to_console_and_log_file("Setting Lun to Manual")
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_LUN_BTN_MANUAL)
            ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_TEXT_LUN, sanstorage.sanlun)
        else:
            logger._log_to_console_and_log_file("Keeping Lun as Auto")

    # Check to see that add storage path and remove all buttons are active/not active in certain cases
    # If there are more than 2 connections, both buttons should be active since 2 connections
    # are automatically filled, and there are more to add
    table = selenium2lib._table_element_finder.find(selenium2lib._current_browser(),
                                                    ProfileSanStorageElements.ID_STORAGE_PATHS_TABLE)
    if table is not None:
        rows = table.find_elements_by_xpath("./tbody/tr")
        num_paths = len(rows)
    else:
        logger._warn("Not finding table")
        num_paths = 0
    if num_connections > 2:
        logger._log_to_console_and_log_file("Making sure both Add Storage Path and Remove All are enabled")
        if (ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_BTN_ADD_STORAGE_PATH_DISABLED) or ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_BTN_STORAGE_PATHS_REMOVE_ALL_DISABLED)):
            logger._warn("A button is disabled when it should be enabled")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("incorrect_button_status.png")
            _cancel_profile_creation()
            return False
        # num_paths should also 2
        if num_paths != 2:
            logger._warn("Expected 2 connections auto-added. Got %d" % num_paths)
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("wrong_number_of_connections_auto_added.png")
            return False
    # If there are 1 or 2 connections, only the remove all button should be enabled
    elif num_connections > 0:
        logger._log_to_console_and_log_file("Making sure Add Storage Path is Disabled, Remove All is enabled")
        if (not ui_lib.is_visible(ProfileSanStorageElements.ID_BTN_ADD_STORAGE_PATH_DISABLED) or ui_lib.is_visible(ProfileSanStorageElements.ID_BTN_STORAGE_PATHS_REMOVE_ALL_DISABLED)):
            logger._warn("A button is in an incorrect state")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("incorrect_button_status.png")
            _cancel_profile_creation()
            return False
        # determine correct number of auto added paths
        # if 2 connections for profile, expect 2 auto added
        if num_connections == 2:
            if num_paths != 2:
                logger._warn("Expected 2 connections auto-added. Got %d" % num_paths)
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("wrong_number_of_connections_auto_added.png")
                return False
        # otherwise there should only be 1 auto added
        elif num_paths != 1:
            logger._warn("Expected 1 connection auto-added. Got %d" % num_paths)
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("wrong_number_of_connections_auto_added.png")
            return False
        # Also make sure there is a message about no more storage paths to add
        if not ui_lib.is_visible(ProfileSanStorageElements.ID_MESSAGE_NO_MORE_STORAGE_PATHS):
            logger._warn("No message about no more storage paths is being displayed")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("missing_warning_about_no_more_storage_paths.png")
            return False
    # Otherwise there must be 0 connections, so go ahead and add the volume expecting the warnings
    else:
        logger._log_to_console_and_log_file("Making sure both buttons are disabled")
        if not ui_lib.is_visible(ProfileSanStorageElements.ID_WARNING_NO_STORAGE_PATHS):
            logger._warn("No warning shown for no storage paths")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("no_warning_for_no_storage_paths.png")
            _cancel_profile_creation()
            return False
        # Check both buttons are disabled
        if not (ui_lib.is_visible(ProfileSanStorageElements.ID_BTN_ADD_STORAGE_PATH_DISABLED) and
                ui_lib.is_visible(ProfileSanStorageElements.ID_BTN_STORAGE_PATHS_REMOVE_ALL_DISABLED)):
            logger._warn("A button is enabled when it should be disabled")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("inccorect_button_status.png")
            return False
        # If the warning and buttons are as expected, add the volume
        logger._log_to_console_and_log_file("Adding a volume with no storage paths")
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
        return True

    # Only need to do this for volumes with connections
    if not _add_storage_paths(sanstorage):
        logger._warn("Unable to add storage paths")
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CANCEL)
        _cancel_profile_creation()
        return False

    return True


# method to edit the san storage section of a profile
def _edit_profile_san_storage_section(editprofile, num_connections):
    selenium2lib = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Editing san storage for %s" % editprofile.name)
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_EDIT_MENU_DROP_DOWN, 10)
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_SAN_STORAGE_LINK_EDIT)
    if not editprofile.has_property("sanstorage"):
        logger._log_to_console_and_log_file("Skipping the san storage section")
        return True
    if isinstance(editprofile.sanstorage, test_data.DataObj):
        editprofile.sanstorage = [editprofile.sanstorage]
    elif isinstance(editprofile.sanstorage, tuple):
        editprofile.sanstorage = list(editprofile.sanstorage[0])

    table = selenium2lib._table_element_finder.find(selenium2lib._current_browser(), ProfileSanStorageElements.ID_STORAGE_VOLUMES_TABLE)
    # Make sure sanstorage is checked
    ui_lib.wait_for_checkbox_and_select(ProfileSanStorageElements.ID_CHKBOX_SAN_STORAGE_EDIT)
    for sanstorage in editprofile.sanstorage:
        # Get a list of the lun numbers already in use
        lun_cells = table.find_elements_by_xpath("./tbody/tr/td[3]")
        lun_cells = [ui_lib.get_text(cell) for cell in lun_cells]
        luns = [str(i) for i in lun_cells]
        # Adding a new volume
        if sanstorage.modification.lower() == "add":
            logger._log_to_console_and_log_file("Adding volume %s" % sanstorage.sanvolume)
            ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_BTN_ADD_VOLUME_EDIT_PROFILE)
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_ADD_VOLUME_EDIT_PROFILE)
            # duplicate lun check
            if sanstorage.sanlun in luns:
                if not _add_volume_with_duplicate_lun(sanstorage):
                    logger._warn("Unable to add volume with duplicate lun")
                    return False
            elif not _add_a_volume(sanstorage, num_connections):
                logger._warn("Unable to add the volume %s" % sanstorage.sanvolume)
                return False

        # Editing an already made volume
        elif sanstorage.modification.lower() == "edit":
            logger._log_to_console_and_log_file("Editing volume %s" % sanstorage.sanvolume)
            if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_VOLUME_IN_STORAGE_VOLUMES_TABLE
                                                   % sanstorage.sanvolume):
                logger._warn("Unable to find the volume in the table")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("no_volume_name_in_table.png")
                return False
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_EDIT_IN_STOR_VOL_TABLE % sanstorage.sanvolume)
            if not _edit_a_volume(sanstorage, *luns):
                logger._warn("Unable to edit the volume %s" % sanstorage.sanvolume)
                return False

        # Deleting an already made volume
        elif sanstorage.modification.lower() == "delete":
            logger._log_to_console_and_log_file("Deleting volume %s" % sanstorage.sanvolume)
            if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_VOLUME_IN_STORAGE_VOLUMES_TABLE
                                                   % sanstorage.sanvolume):
                logger._warn("Unable to find the volume in the table")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("no_volume_name_in_table.png")
                return False
            # based on whether this volume is permanent or not, a warning should be displayed
            permanence = str(ui_lib.get_text(ProfileSanStorageElements.ID_VOLUME_PERMANENCE_STOR_VOL_TABLE % sanstorage.sanvolume))
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_REMOVE_FROM_STOR_VOL_TABLE % sanstorage.sanvolume)
            # No warning should be displayed if its permanent
            if sanstorage.has_property("permanent"):
                if ui_lib.is_visible(ProfileSanStorageElements.ID_BTN_DELETE_NON_PERMANENT_VOLUME):
                    logger._warn("Getting a warning for deleting a non permanent volume for a permanent volume")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("warning_for_deleting_permanent_volume.png")
                    return False
            # A warning should be displayed
            else:
                if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_BTN_DELETE_NON_PERMANENT_VOLUME):
                    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_DELETE_NON_PERMANENT_VOLUME)
                else:
                    logger._warn("A warning for deleting a non permanent volume was not displayed")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("non_warning_for_deleting_non_permanent_volume.png")
                    return False
            # Check to make sure it was removed from the table
            if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_VOLUME_IN_STORAGE_VOLUMES_TABLE % sanstorage.sanvolume):
                logger._warn("Unable to delete the volume %s" % sanstorage.sanvolume)
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("volume_still_present_after_deletion.png")
                return False
            else:
                logger._log_to_console_and_log_file("Successfully deleted the volume")
        # specific case for lunswap test
        elif sanstorage.modification.lower() == "lunswap":
            logger._log_to_console_and_log_file("Lunswap test")
            if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_VOLUME_IN_STORAGE_VOLUMES_TABLE
                                                   % sanstorage.sanvolume):
                logger._warn("Unable to find the volume in the table")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("no_volume_name_in_table.png")
                return False
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_EDIT_IN_STOR_VOL_TABLE % sanstorage.sanvolume)
            if not _run_lunswap_test(sanstorage):
                logger._warn("lunswap test failed")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("lunswap_test_error.png")
                return False
    return True


# method to edit a sanstorage volume
def _edit_a_volume(sanstorage, *luns):
    selenium2lib = ui_lib.get_s2l()
    # Edit the lun. If already present run the duplun test
    if sanstorage.has_property("sanlun"):
        if sanstorage.sanlun in luns:
            if not _edit_volume_to_have_duplun(sanstorage):
                logger._warn("Unable to edit volume to have duplun")
                return False
            return True
    if sanstorage.has_property("sanlun") and sanstorage.sanlun != "":
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_LUN_BTN_MANUAL)
        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_TEXT_LUN, sanstorage.sanlun)
    else:
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_LUN_BTN_AUTO)
    # Edit the storage paths
    if not _edit_storage_paths(sanstorage):
        return False
    # Determine how many connections there are
    ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_STORAGE_PATHS_TABLE)
    storage_paths_table = selenium2lib._table_element_finder.find(selenium2lib._current_browser(),
                                                                  ProfileSanStorageElements.ID_STORAGE_PATHS_TABLE)
    if storage_paths_table is None:
        logger._warn("Not finding table")

    rows = storage_paths_table.find_elements_by_xpath("./tbody/tr")
    num_cons = len(rows)
    # expect a warning if only 1 connection
    if num_cons == 1:
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
        if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_STORAGE_PATHS_VOLUME):
            logger._warn("Not seeing warning message about no redundant paths")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("no_redundant_storage_path_warning.png")
            return False
        else:
            logger._log_to_console_and_log_file("Warning correctly shown")
            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
    else:
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
    return True


# method to edit storage paths when editing san storage in a profile
def _edit_storage_paths(sanstorage):
    if sanstorage.has_property("connection"):
        if isinstance(sanstorage.connection, test_data.DataObj):
            sanstorage.connection = [sanstorage.connection]
        elif isinstance(sanstorage.connection, tuple):
            sanstorage.connection = list(sanstorage.connection[0])
        for connection in sanstorage.connection:
            # Add a connection
            if connection.edit.lower() == "add":
                logger._log_to_console_and_log_file("Adding a new storage path %s" % connection.name)
                if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_ADD_STORAGE_PATH):
                    logger._warn("No storage paths to add")
                    logger._log_to_console_and_log_file("Capturing screenshto")
                    selenium2lib.capture_page_screenshot("no_storage_paths_to_add.png")
                if not ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_ADD_SPECIFIC_STORAGE_PATHS
                                                         % connection.name):
                    logger._warn("Could not find the specified storage path")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_find_the_indicated_storage_path.png")
                    return False
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CONFIRM_ADD_STORAGE_PATH)
                if not _edit_storage_target_ports(connection):
                    return False
            # Remove a connection
            elif connection.edit.lower() == "remove":
                logger._log_to_console_and_log_file("Removing the storage path %s" % connection.name)
                if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_NETWORK_IN_STORAGE_PATH_TABLE % connection.name):
                    logger._warn("Unable to find the specified storage path")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_find_the_indicated_storage_path.png")
                    return False
                ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_REMOVE_STORAGE_PATH % connection.name)
                if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_NETWORK_IN_STORAGE_PATH_TABLE % connection.name):
                    logger._warn("Unable to remove the specified storage path")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_remove_the_indicated_storage_path.png")
                    return False
            # Disable a connection
            elif connection.edit.lower() == "disable":
                logger._log_to_console_and_log_file("Disabling the storage path %s" % connection.name)
                if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_NETWORK_IN_STORAGE_PATH_TABLE % connection.name):
                    logger._warn("Unable to find the specified storage path")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_find_the_indicated_storage_path.png")
                    return False
                if not ui_lib.wait_for_checkbox_and_unselect(ProfileSanStorageElements.ID_CHKBOX_ENABLE_STORAGE_PATH % connection.name):
                    logger._warn("Unable to disable the specified connection")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_disable_the_indicated_storage_path.png")
                    return False
            # Enable a connection
            elif connection.edit.lower() == "enable":
                if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_NETWORK_IN_STORAGE_PATH_TABLE % connection.name):
                    logger._warn("Unable to find the specified storage path")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("unable_to_find_the_indicated_storage_path.png")
                    return False
                ui_lib.wait_for_checkbox_and_select(ProfileSanStorageElements.ID_CHKBOX_ENABLE_STORAGE_PATH % connection.name)
                logger._log_to_console_and_log_file("Enabling the storage path %s" % connection.name)
                if not _edit_storage_target_ports(connection):
                    return False
            # Modify an existing connection
            elif connection.edit == "":
                if not _edit_storage_target_ports(connection):
                    return False
            else:
                logger._warn("Unrecognized edit command")
                return False
    return True


# method to verify the volume table in the edit profile dialogue
def _verify_volume_table(volumes_obj, page_location):
    selenium2lib = ui_lib.get_s2l()
    # get the table from the page
    ui_lib.wait_for_element_visible(page_location, 10)
    table = selenium2lib._table_element_finder.find(selenium2lib._current_browser(),
                                                    page_location)
    if table is None:
        logger._warn("Not finding table")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("no_volume_table_present.png")
        return False
    logger._log_to_console_and_log_file("Verifying the volume attachments table")
    # Check the case where there should be no volumes
    if not volumes_obj[0].has_property("name"):
        logger._log_to_console_and_log_file("No volumes should be associated with this profile")
        # If we're on the edit profile page, make sure the table is not displayed
        if page_location == ProfileSanStorageElements.ID_STORAGE_VOLUMES_TABLE:
            if ui_lib.is_visible(page_location):
                logger._warn("The table is being shown when it should not be")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("table_present_when_should_be_hidden.png")
                return False
            else:
                logger._log_to_console_and_log_file("There is no table showing as expected!")
                return True
        # Otherwise we're on the san storage page
        else:
            if not ui_lib.is_visible(ProfileSanStorageElements.ID_MESSAGE_NO_ADDED_VOLUMES):
                logger._warn("There is no message saying there are no volumes for this profile")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("no_message_for_no_volumes_with_profile.png")
                return False
            else:
                logger._log_to_console_and_log_file("There is no table showing as expected!")
                return True
    # Gather table headings
    table_headings = []
    headers = table.find_elements_by_xpath("./thead/tr/th")
    for heading in headers:
        if heading.text:
            table_headings.append(str(heading.text))
    # Go through and check each volume
    for volume in volumes_obj:
        row_count = 1
        found = False
        volume_data = []
        # find the row with this volumes information
        rows = table.find_elements_by_xpath("./tbody/tr")
        for row in rows:
            if not found:
                # Check to see if this row contains the volume information
                if volume.name in str(row.text):
                    found = True
                    data = table.find_elements_by_xpath("./tbody/tr[" + str(row_count) + "]/td")
                    for td in data:
                        if td.text:
                            volume_data.append(str(td.text))
                    # Now volume data and table headers are full, so create a dictionary
                    volume_dictionary = dict(zip(table_headings, volume_data))
                    logger._log_to_console_and_log_file("Volume information: %s" % volume_dictionary)
                    if not _validate_vol_data_table(volume, volume_dictionary):
                        return False
                    logger._log_to_console_and_log_file("Information for %s is correct!" % volume.name)
                    logger._log_to_console_and_log_file("Checking the storage paths table for %s" % volume.name)
                    if not _verify_storage_paths_table(row_count, table, volume, selenium2lib, page_location):
                        return False
                row_count += 1
        if not found:
            logger._warn("Unable to find the volume in the table")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("no_volume_name_in_table.png")
            return False
    return True


def _verify_storage_paths_table(row_num, vol_table, volume, selenium2lib, page_location):
    # Get the storage paths table
    if page_location == ProfileSanStorageElements.ID_VOLUME_ATTACHMENTS_TABLE:
        location = ProfileSanStorageElements.ID_NETWORKS_TABLE_FOR_VOLUME % volume.name
    else:
        location = ProfileSanStorageElements.ID_CONNECTIONS_FOR_VOLUME_TABLE % volume.name
    paths_table = selenium2lib._table_element_finder.find(selenium2lib._current_browser(), location)
    ui_lib.wait_for_element_visible(paths_table, 10)
    # First Case is if the volume has no storage paths
    if not volume.has_property("connection"):
        # Should see "No storage paths"
        if not ui_lib.is_visible(ProfileSanStorageElements.ID_NO_STORAGE_PATHS_FOR_VOLUME % volume.name):
            logger._warn("Not seeing 'No storage paths' message for volume")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("no_no_storage_paths_message_for_volume.png")
            return False
        else:
            logger._log_to_console_and_log_file("Correctly displaying 'No storage paths' message")
            return True
    # Go through each of the volume's connections
    if paths_table is None:
        logger._warn("Not finding table")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.caption("no_table_when_expected.png")
        return False

    if isinstance(volume.connection, test_data.DataObj):
        volume.connection = [volume.connection]
    elif isinstance(volume.connection, tuple):
        volume.connection = list(volume.connection[0])

    for connection in volume.connection:
        con_dictionary = {}
        found = False
        row_count = 1
        rows = paths_table.find_elements_by_xpath("./tbody/tr")
        # find the row with this connections information
        for row in rows:
            if not found:
                # check to see if this row has the connection
                if connection.name in str(row.text):
                    found = True
                    if page_location == ProfileSanStorageElements.ID_STORAGE_VOLUMES_TABLE:
                        # Add the name to the dictionary
                        con_name = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[2]/div/a"))
                        con_dictionary["Name"] = con_name
                        # Add the type to the dictionary
                        con_type = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[2]/div/span"))
                        con_dictionary["Type"] = con_type
                        # Add the server initiator
                        con_serv_init = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[3]/div"))
                        con_dictionary["Server Initiator"] = con_serv_init
                        # Add the storage targets
                        line = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[4]"))
                        line = line.split()
                        con_stor_targets = [line[i] for i in range(len(line)) if i % 2 == 0]
                        con_stor_target_group = [line[i] for i in range(len(line)) if i % 2 == 1]
                        con_dictionary["Storage Targets"] = con_stor_targets
                        con_dictionary["Storage Targets Group"] = con_stor_target_group
                    else:
                        # Add the name to the dictionary
                        con_name = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[3]/div/a"))
                        con_dictionary["Name"] = con_name
                        # Add the type to the dictionary
                        con_type = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[3]/div/span"))
                        con_dictionary["Type"] = con_type
                        # Add the server initiator
                        con_serv_init = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[4]/div"))
                        con_dictionary["Server Initiator"] = con_serv_init
                        # Add the storage targets
                        line = str(ui_lib.get_text(location + "//tbody/tr[" + str(row_count) + "]/td[5]"))
                        line = line.split()
                        con_stor_targets = [line[i] for i in range(len(line)) if i % 2 == 0]
                        con_stor_target_group = [line[i] for i in range(len(line)) if i % 2 == 1]
                        con_dictionary["Storage Targets"] = con_stor_targets
                        con_dictionary["Storage Targets Group"] = con_stor_target_group
                    logger._log_to_console_and_log_file("Storage paths information %s" % con_dictionary)
                    if not _validate_storage_paths_data_table(con_dictionary, connection, location, row_count, volume.name, page_location):
                        return False
                row_count += 1
    return True


# helper function to validate a volumes attributes
def _validate_vol_data_table(volume, volume_dictionary):
    # change some of the volumes fields to ensure proper compatibility
    if volume.lun == "":
        volume.lun = "Auto"
    # Need different volume size methods for GiB and TiB
    vol_size = float(volume.size)
    if vol_size < 1024:
        vol_size = "{0:.2f}".format(vol_size)
        vol_size += " GiB"
    else:
        vol_size /= 1024
        vol_size = "{0:.2f}".format(vol_size)
        vol_size += " TiB"
    error_count = 0
    # Now verify each part
    # name
    if volume.name.lower() != volume_dictionary["Volume Name"].lower():
        logger._warn("The Table shows the wrong volume name")
        logger._warn("Got: %s. Expected: %s" % (volume_dictionary["Volume Name"], volume.name))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_volume_name.png")
        error_count += 1
    # permanence
    if volume.permanent.lower() != volume_dictionary["Permanent"].lower():
        logger._warn("The Table shows the wrong volume permanence")
        logger._warn("Got: %s. Expected: %s" % (volume_dictionary["Permanent"], volume.permanent))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_volume_permanence.png")
        error_count += 1
    # lun
    if volume.lun == "Auto":
        # Nothing to check since the initial config was for auto lun
        logger._log_to_console_and_log_file("Not checking lun since it was assigned automatically")
    elif volume.lun.lower() != volume_dictionary["LUN"].lower():
        logger._warn("The Table shows the wrong volume LUN")
        logger._warn("Got: %s. Expected: %s" % (volume_dictionary["LUN"], volume.lun))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_volume_lun.png")
        error_count += 1
    # storagepool
    if volume.storagepool.lower() != volume_dictionary["Pool"].lower():
        logger._warn("The Table shows the wrong volume storage pool")
        logger._warn("Got: %s. Expected: %s" % (volume_dictionary["Pool"], volume.storagepool))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_volume_storage_pool.png")
        error_count += 1
    # size
    if vol_size.lower() != volume_dictionary["Size"].lower():
        logger._warn("The Table shows the wrong volume size")
        logger._warn("Got: %s. Expected: %s" % (volume_dictionary["Size"], vol_size))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_volume_size.png")
        error_count += 1
    # provisioning
    if volume.provisioning.lower() != volume_dictionary["Provisioning"].lower():
        logger._warn("The Table shows the wrong volume provisioning")
        logger._warn("Got: %s. Expected: %s" % (volume_dictionary["Provisioning"], volume.provisioning))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_volume_provisioning.png")
        error_count += 1
    # sharing
    if volume.sharing.lower() != volume_dictionary["Sharing"].lower():
        logger._warn("The Table shows the wrong volume sharing")
        logger._warn("Got: %s. Expected: %s" % (volume_dictionary["Sharing"], volume.sharing))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_volume_sharing.png")
        error_count += 1
    # if we got an error, fail test
    if error_count > 0:
        logger._warn("There were %d errors with this volume" % error_count)
        return False
    return True


# helper function to check validate connections attributes
def _validate_storage_paths_data_table(con_dictionary, connection, location, row_num, volume_name, page_location):
    error_count = 0
    # Check connection name
    if connection.name.lower() != con_dictionary["Name"].lower():
        logger._warn("The Table shows the wrong connection name")
        logger._warn("Got :%s. Expected: %s" % (con_dictionary["Name"], connection.name))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_connection_name.png")
        error_count += 1
    # Check connection type
    if connection.type.lower() != con_dictionary["Type"].lower():
        logger._warn("The Table shows the wrong connection type")
        logger._warn("Got: %s. Expected: %s" % (con_dictionary["Type"], connection.type))
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("incorrect_connection_type.png")
        error_count += 1

    # Check server initiator if provided
    if connection.has_property("serverinitiator") and connection.serverinitiator != "":
        if connection.serverinitiator.lower() != con_dictionary["Server Initiator"].lower():
            logger._warn("The Table shows the wrong server initiator")
            logger._warn("Got: %s. Expected: %s" % (con_dictionary["Server Initiator"], connection.serverinitiator))
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("incorrect_connection_server_initiator.png")
            error_count += 1

    # Check the target ports and groups only if the connection type if FC or FCOE
    if connection.type.lower() != "direct attach":
        # Convert storage targets to upper case for consistency
        con_dictionary["Storage Targets"] = [x.upper() for x in con_dictionary["Storage Targets"]]
        # Convert storage target groups to lower case for consistency
        con_dictionary["Storage Targets Group"] = [x.lower() for x in con_dictionary["Storage Targets Group"]]
        target_num = 0
        # check to see if ports have been auto-assigned
        if not connection.has_property("port"):
            logger._log_to_console_and_log_file("Not checking storage targets since they were auto assigned")
        else:
            if type(connection.port) is test_data.DataObj:
                connection.port = [connection.port]
            elif type(connection.port) is tuple:
                connection.port = list(connection.port[0])
            for port in connection.port:
                ind = -1
                # pending assignment case
                if port.target.lower() == "pending assignment":
                    if not ((con_dictionary["Storage Targets"][0].lower() == "pending") and
                            (con_dictionary["Storage Targets Group"][0].lower() == "assignment")):
                        logger._warn("The Table shows the wrong Storage Target")
                        logger._warn("Got %s. Expected: %s" % (con_dictionary["Storage Target"][0], port.target))
                        logger._log_to_console_and_log_file("Capturing screenshot")
                        selenium2lib.capture_page_screenshot("incorrect_connection_storage_target.png")
                        error_count += 1
                        continue
                    else:
                        target_num += 1
                        continue
                if port.target.upper() not in con_dictionary["Storage Targets"]:
                    logger._warn("The Table shows the wrong Storage Target")
                    logger._log_to_console_and_log_file("Capturing screenshot")
                    selenium2lib.capture_page_screenshot("incorrect_connection_storage_target.png")
                    error_count += 1
                # indexes of storage targets and group correspond with each other
                else:
                    ind = con_dictionary["Storage Targets"].index(port.target.upper())
                # check storage targets group based on index of storage target
                if ind != -1:
                    if port.group.lower() != con_dictionary["Storage Targets Group"][ind]:
                        logger._warn("The Table shows the wrong Storage Target Group")
                        logger._warn("Got: %s. Expected: %s" % (con_dictionary["Storage Targets Group"][ind], port.group))
                        logger._log_to_console_and_log_file("Capturing screenshot")
                        selenium2lib.capture_page_screenshot("incorrect_connection_storage_target_group.png")
                        error_count += 1
                else:
                    logger._warn("Not checking group since target was not found")
                # keep count of the ports we need
                target_num += 1
            if target_num != len(con_dictionary["Storage Targets"]):
                logger._warn("Error in the number of storage targets that should be present")
                logger._warn("Got: %d. Expected: %d" % (len(con_dictionary["Storage Targets"]), target_num))
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("incorrect_number_of_connections.png")
                error_count += 1
    else:
        logger._log_to_console_and_log_file("Not checking storage targets since connection is direct attach")
    # Check to see if its enabled or not
    # San Storage Section
    if page_location == ProfileSanStorageElements.ID_VOLUME_ATTACHMENTS_TABLE:
        if connection.enabled.lower() == "no port":
            if str(ui_lib.get_text(location + "//tbody/tr[" + str(row_num) + "]/td[6]")).lower() != "no":
                logger._warn("The Table shows the wrong Enable")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("incorrect_connection_enable.png")
                error_count += 1
        elif connection.enabled.lower() != str(ui_lib.get_text(location + "//tbody/tr[" + str(row_num) + "]/td[6]")).lower():
            logger._warn("The Table shows the wrong Enable")
            logger._log_to_console_and_log_file("Capturing screenshot")
            selenium2lib.capture_page_screenshot("incorrect_connection_enable.png")
            error_count += 1
    # Edit profile Section
    else:
        if connection.enabled.lower() == "yes":
            # The checkbox should have an attribute called checked
            if not ui_lib.is_visible(ProfileSanStorageElements.ID_NETWORK_ENABLED_IN_STOR_VOL_TABLE
                                     % (volume_name, connection.name)):
                logger._warn("The connection is not enabled when it should be")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("incorrect_connection_enable.png")
                error_count += 1
        # otherwise the connection should not be enabled
        elif connection.enabled.lower() == "no":
            if ui_lib.is_visible(ProfileSanStorageElements.ID_NETWORK_ENABLED_IN_STOR_VOL_TABLE
                                 % (volume_name, connection.name)):
                logger._warn("The connection is enabled when it should not be")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("incorrect_connection_enable.png")
                error_count += 1
        # check the case of no port
        elif connection.enabled.lower() == "no port":
            if str(ui_lib.get_text((ProfileSanStorageElements.ID_NETWORK_FOR_VOL_IN_STOR_VOL_TABLE + "/../../../td[5]")
                                   % (volume_name, connection.name))) != "No port":
                logger._warn("Missing text about No port for this connection")
                logger._log_to_console_and_log_file("Capturing screenshot")
                selenium2lib.capture_page_screenshot("missing_no_port_text.png")
                error_count += 1
    if error_count > 0:
        logger._warn("There were %d errors with this connection" % error_count)
        return False
    logger._log_to_console_and_log_file("Storage path table is correct for %s" % connection.name)
    return True


# Method to edit profile connections
def _edit_profile_connetions(editprofile):
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_MAIN_ACTION)
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_MENU_ACTION_EDIT)
    ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_PROFILE_EDIT_MENU_DROP_DOWN)
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_PROFILE_EDIT_MENU_DROP_DOWN)
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_CONNECTIONS_LINK_EDIT)
    if editprofile.has_property("connection"):
        logger._log_to_console_and_log_file("Modifying connections")
        if isinstance(editprofile.connection, test_data.DataObj):
            editprofile.connection = [editprofile.connection]
        elif isinstance(editprofile.connection, tuple):
            editprofile.connection = list(editprofile.connection[0])
        for connection in editprofile.connection:
            # First add any connections
            if connection.modification.lower() == "add":
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION)
                # Selecting connection type
                if (connection.type.upper() in ["FIBRE CHANNEL", "ETHERNET"]):
                    # Validating mandatory fields
                    if ((not connection.has_property("network")) or (not connection.has_property("type"))):
                        logger._warn("Network name and type are mandatory fields for connections")
                        _cancel_connection()
                        return False
                    logger._log_to_console_and_log_file("Selecting connection type")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_CONNECTION_FUNCTION_TYPE,
                                                            FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (connection.type, connection.type))
                else:
                    logger._warn("Invalid connection type")
                    _cancel_connection()
                    return False

                if (connection.has_property("name") and connection.name != ""):
                    logger._log_to_console_and_log_file("Adding connection %s" % connection.name)
                    selenium2lib.input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.name)

                logger._log_to_console_and_log_file("Selecting Network")
                __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_NETWORK_ADD_CONNECTION,
                                                        FusionServerProfilesPage.ID_ELEMENT_NETWORK_ADD_CONNECTION % connection.network)

                # Selecting Port Name
                if connection.has_property("portname") and connection.portname != "":
                    logger._log_to_console_and_log_file("Selecting port")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_FLEXNIC_ADD_CONNECTION,
                                                            FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT % connection.portName)

                # Fill in bandwith
                if connection.has_property("band") and connection.band != "":
                    selenium2lib.input_text(ProfileSanStorageElements.ID_CONNECTION_BANDWITH, connection.band)
                    if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_INCORRECT_BANDWITH):
                        logger._warn("Incorrect bandwith")
                        _cancel_connection()
                        return False

                # Selecting Boot
                if (connection.has_property("boot") and (connection.boot.upper() == "PRIMARY" or connection.boot.upper() == "SECONDARY")):
                    logger._log_to_console_and_log_file("Selecting Boot")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_BOOT_ADD_CONNECTION,
                                                            FusionServerProfilesPage.ID_ELEMENT_BOOT_ADD_CONNECTION % connection.boot)

                    if connection.type.upper() == "FIBRE CHANNEL":
                        if (connection.has_property("targetwwpn") and connection.targetwwpn != "" and connection.has_property("targetlun") and connection.targetlun != ""):
                            logger._log_to_console_and_log_file("Specifying Boot Order")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_SPECIFIY_BOOT_TARGET)
                            logger._log_to_console_and_log_file("Typing target WWPN")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET, connection.targetwwpn)
                            logger._log_to_console_and_log_file('typing target LUN')
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET, connection.targetlun)
                        else:
                            logger._log_to_console_and_log_file("Not bootable connection")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USE_BIOS)

                        if (connection.has_property("wwpn") and connection.wwpn != "" and connection.has_property("wwnn") and connection.wwnn != ""):
                            logger._log_to_console_and_log_file("Selecting use user specified IDs checkbox.")
                            selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                            logger._log_to_console_and_log_file("Typing WWPN")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN, connection.wwpn)
                            logger._log_to_console_and_log_file("Typing WWNN")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN, connection.wwnn)
                            if connection.has_property("macaddress") and connection.macaddress != "":
                                logger._log_to_console_and_log_file("Typing Mac address")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macaddress)
                    # otherwise must be ethernet since it was already checked prior
                    else:
                        if connection.has_property("macaddress") and connection.macaddress != "":
                            logger._log_to_console_and_log_file("Selecting use user specified IDs checkbox.")
                            selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                            logger._log_to_console_and_log_file("Typing Mac Address")
                            ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                            ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macadress)
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON)
            # Now edit any connections
            if connection.modification.lower() == "edit":
                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_CONNECTION)
                if not (connection.has_property("name")):
                    logger._warn("Please inform the name of the connection that will be updated.")
                    return False
                else:
                    logger._log_to_console_and_log_file("Changing profile connection %s" % connection.name)
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_EDIT_CONNECTION % connection.name)

                if (connection.has_property("newname") and len(connection.newname) > 0):
                    logger._log_to_console_and_log_file("Changing connection name from '%s' to '%s'." % (connection.name, connection.newname))
                    ui_lib.wait_for_element_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.name)
                    ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_NAME, connection.newname)

                if (connection.has_property("network")):
                    logger._log_to_console_and_log_file("   - Changing network selection.")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_NETWORK_ADD_CONNECTION,
                                                            FusionServerProfilesPage.ID_ELEMENT_NETWORK_ADD_CONNECTION % connection.network)
                    # check to see if we get a warning about san storage if we expect it
                    if connection.has_property("warning"):
                        if ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_EDIT_CONNECTION_REMOVE_FROM_SAN):
                            logger._log_to_console_and_log_file("Modifying connection will affect SAN volume storage paths")
                            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_CLOSE_EDIT_CONNECTION_WARNING)
                        else:
                            logger._warn("Not seeing a warning when expecting it")
                            logger._log_to_console_and_log_file("Capturing screenshot")
                            selenium2lib.capture_page_screenshot("no_network_change_affect_san_warning.png")
                            return False

                if connection.has_property('band'):
                    if not serverprofiles.__validate_requested_bandwidth(ui_lib.get_text(FusionServerProfilesPage.ID_COMBO_CONNECTION_FUNCTION_TYPE),
                                                                         connection.band):
                        _cancel_connection()
                        return False

                if connection.has_property('portName'):
                    logger._log_to_console_and_log_file("Selecting port.")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_FLEXNIC_ADD_CONNECTION,
                                                            FusionServerProfilesPage.XP_CREATE_SP_ADD_CONN_NIC_DD_SELECT % connection.portName)

                if (connection.has_property('boot')):
                    logger._log_to_console_and_log_file("Selecting boot.")
                    __select_value_from_a_profile_combo_box(FusionServerProfilesPage.ID_COMBO_BOOT_ADD_CONNECTION,
                                                            FusionServerProfilesPage.ID_SELECT_BOX_GENERIC_ELEMENT % (connection.boot, connection.boot))
                    if (connection.boot == 'Primary' or connection.boot == 'Secondary'):
                        if (ui_lib.get_text(FusionServerProfilesPage.ID_COMBO_CONNECTION_FUNCTION_TYPE) == "Fibre Channel"):
                            if (connection.has_property('targetwwpn') and connection.has_property('targetlun') and connection.targetwwpn != "" and connection.targetlun != ""):
                                logger._log_to_console_and_log_file("Specifying boot target.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_SPECIFIY_BOOT_TARGET)
                                logger._log_to_console_and_log_file("Typing target WWPN.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET)
                                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWN_TARGET, connection.targetwwpn)
                                logger._log_to_console_and_log_file("Typing target LUN.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET)
                                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_LUN_TARGET, connection.targetlun)
                            else:
                                logger._log_to_console_and_log_file("Not bootable connection.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_RADIO_USE_BIOS)

                            if connection.has_property('wwpn') and connection.has_property('wwnn') and connection.wwpn != "" and connection.wwnn != "":
                                logger._log_to_console_and_log_file("Selecting use user specified IDs checkbox.")
                                selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                                logger._log_to_console_and_log_file("Typing WWPN.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN)
                                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWPN, connection.wwpn)
                                logger._log_to_console_and_log_file("Typing WWNN.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN)
                                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_FIBERCHANNEL_WWNN, connection.wwnn)
                                if connection.has_property('macaddress') and connection.macaddress != "":
                                    logger._log_to_console_and_log_file("Typing MAC address.")
                                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                                    ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macaddress)
                        elif connection.type.upper() == "ETHERNET":
                            if connection.has_property('macaddress') and connection.macaddress != "":
                                logger._log_to_console_and_log_file("Selecting use user specified IDs checkbox.")
                                selenium2lib.select_checkbox(FusionServerProfilesPage.ID_CHKBOX_USER_SPECIFIED_IDS)
                                logger._log_to_console_and_log_file("Typing MAC address.")
                                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC)
                                ui_lib.wait_for_element_and_input_text(FusionServerProfilesPage.ID_INPUT_CONNECTION_MAC, connection.macaddress)

                ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_ADD_NETWORK_ADD_CONNECTON)
                logger._log_to_console_and_log_file("Clicking on OK button.")

            if connection.modification.lower() == "delete":
                # Now delete any connections
                if ui_lib.is_visible(FusionServerProfilesPage.ID_PROFILE_CONNECTION_ELEMENT_BY_NAME % connection.name):
                    logger._log_to_console_and_log_file("Deleting connection %s." % connection.name)
                    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_DELETE_CONNECTION % connection.name)
                    # Check to see we get a warning if we expect it
                    if connection.has_property("warning"):
                        if ui_lib.is_visible(ProfileSanStorageElements.ID_WARNING_REMOVE_CONNECTION_REMOVE_FROM_SAN):
                            logger._log_to_console_and_log_file("Deleting this connection will affect san volumes")
                            ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_OK_REMOVE_CONNECTION)
                        else:
                            logger._warn("Not seeing warning message about deleting connection affecting san voluems")
                            logger._log_to_console_and_log_file("Capturing screenshot")
                            selenium2lib.capture_page_screenshot("no_warning_for_deleting_connection_from_san.png")
                            return False
                else:
                    logger.warn("Connection %s not found." % connection.name)
                    return False
    return True


# method to add volume with duplicate lun, should be a new volume
def _add_volume_with_duplicate_lun(sanstorage):
    logger._log_to_console_and_log_file("Attempting to add volume with duplicate lun")
    selenium2lib = ui_lib.get_s2l()
    # Fill in New Volume Form
    if sanstorage.has_property("volumetype") and sanstorage.volumetype.upper() == "NEW VOLUME":
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_TYPE_DROP_DOWN)
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_TYPE_NEW)
    else:
        logger._warn("Please make it a new volume")
        return False

    # Fill in the name, and description if necessary
    ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_NAME, sanstorage.sanvolume)
    if sanstorage.has_property("description"):
        ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_NEW_VOLUME_DESCRIPTION, sanstorage.description)

    # Now fill in the duplicate lun
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_LUN_BTN_MANUAL)
    ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_TEXT_LUN, sanstorage.sanlun)

    # Fill in remaining things
    if not _fill_sanstorage_properties(sanstorage):
        logger._warn("Unable to fill sanstorage properties")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("unable_to_fill_sanstorage_properties.png")
        return False

    # Now click add volume, and expect a warning
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
    if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_DUPLICATE_LUNS):
        logger._warn("Failed to see error about duplicate LUNs")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("no_duplicate_lun_warning_present.png")
        return False
    else:
        logger._log_to_console_and_log_file("Correctly saw warning about duplicate LUN")
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)

    # Click on the create profile button and expect to be blocked
    ui_lib.wait_for_element_and_click(FusionServerProfilesPage.ID_BTN_CREATE_SERVER_PROFILE)
    if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_DUPLICATE_LUN % sanstorage.sanlun, 7):
        logger._warn("Not seeing error about the duplicate lun")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("no_duplicate_lun_error.png")
        return False
    else:
        logger._log_to_console_and_log_file("Profile creation is correctly blocked")
    # Now remove the volume and proceed with profile creation
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_NEW_VOLUME_REMOVE_FROM_VOLUME_ATTACHMENTS_TABLE % sanstorage.sanvolume)
    return True


# method to edit a volume to have duplicate lun
def _edit_volume_to_have_duplun(sanstorage):
    logger._log_to_console_and_log_file("Attempting to edit volume to have duplicate lun")
    # Edit the lun to be a duplicate
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_LUN_BTN_MANUAL)
    ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_TEXT_LUN, sanstorage.sanlun)

    # Click on OK and verify a warning message is shown
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
    if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_DUPLICATE_LUNS):
        logger._warn("Failed to see error about duplicate LUNs")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("no_duplicate_lun_warning_present.png")
        return False
    else:
        logger._log_to_console_and_log_file("Correctly saw warning about duplicate LUN")
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)

    # Now OK the profile edit and verify it is blocked
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_OK_EDIT_PROFILE)
    if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_ERROR_DUPLICATE_LUN % sanstorage.sanlun, 7):
        logger._warn("Not seeing error about the duplicate lun")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("no_duplicate_lun_error.png")
        return False
    else:
        logger._log_to_console_and_log_file("Profile updation correctly blocked")
    # Now remove the volume and proceed with profile creation
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_VOLUME_REMOVE_FROM_STOR_VOL_TABLE % sanstorage.sanvolume)
    return True


# method to run a lunswap test
def _run_lunswap_test(sanstorage):
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_LUN_BTN_MANUAL)
    ui_lib.wait_for_element_and_input_text(ProfileSanStorageElements.ID_TEXT_LUN, sanstorage.sanlun)
    ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
    if not ui_lib.wait_for_element_visible(ProfileSanStorageElements.ID_WARNING_DUPLICATE_LUNS):
        logger._warn("Failed to see error about duplicate LUNs")
        logger._log_to_console_and_log_file("Capturing screenshot")
        selenium2lib.capture_page_screenshot("no_duplicate_lun_warning_present.png")
        return False
    else:
        logger._log_to_console_and_log_file("Correctly saw warning about duplicate LUN")
        ui_lib.wait_for_element_and_click(ProfileSanStorageElements.ID_BTN_STORAGE_ADD)
    return True
