"""
OvsLibrary OneView Supportibility Fixme Keywords.

"""

from FusionLibrary.ui.settings.settings_elements import FusionSettingsPage
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.settings.appliance import *
from RoboGalaxyLibrary.keywords.ntnative import *


import os

ROBOT_LIBRARY_VERSION = '0.0'


def navigate():
    """Navigate to settings page"""
    navigate_settings_base(FusionSettingsPage.ID_PAGE_LABEL,
                           FusionUIBaseElements.ID_MENU_LINK_SETTINGS)

    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to Settings page", True)


def navigate_settings_base(currentpage, menulink):
    """ navigate to setting base"""
    logger._log_to_console_and_log_file('\nNavigating to "{0}"'.format(currentpage))
    if not ui_lib.wait_for_element(currentpage):
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL)
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MENU_LINK_USERS_AND_GROUPS, 10)
        ui_lib.wait_for_element_and_click(menulink)
        ui_lib.wait_for_element(currentpage)


def update_appliance(app_obj):
    """ To Update fixmebin file using upgrade framework
        Example:
        <update_appliance>
        <app selectimage="yes" bindirectory="C:\Downloads\" update_option="Upload only"></app>
        </update_appliance>
    """
    navigate()
    for _, app in enumerate(app_obj):
        Updateappliance.click_update_appliance()
        Updateappliance.wait_update_appliance_dialog_shown()
        choose_option = app.update_option
        # choose this option if user prefers to upload the bin file manually
        if app.selectimage == "yes":
            Updateappliance.tick_update_image()
            for files in os.listdir(app.bindirectory):
                filename = files
                logger.info("File Name is %s" % filename)

            if not filename:
                ui_lib.fail_test("Failed to find bin file ", True)
            logger.info("Choose the bin file , " + filename + " from the path specified")
            Updateappliance.click_browse_button()
            # Browsing bin file
            try:
                win32 = NativeOsKeywords()
                logger.debug("Starting choosing bin file to be uploaded %s" % (app.bindirectory + filename))
                win32.activate_window("File Upload")
                logger.debug("Typing bin file path into [ File Name ] text box")
                win32.input_text("File Upload", "Edit1", (app.bindirectory + filename))
                logger.debug("Clicking [ Open ] button")
                win32.click_button("File Upload", "Button1")
                win32.wait_window_close("File Upload", timeout=60)
            except ImportError as e:
                logger.debug("Can't choose file to be uploaded")
                raise e
            logger.info("uploaded bin file")

            if choose_option == "Upload and install":
                Updateappliance.click_upload_and_install()
                Updateappliance.wait_update_dialog_appear(timeout=PerfConstants.UPLOAD_PATCH_FILE * 4, fail_if_false=True)
                Updateappliance.tick_accept_agreement()
                Updateappliance.click_update_button()

            elif choose_option == "Upload only":
                Updateappliance.click_upload_only()
                Updateappliance.click_action_button(timeout=PerfConstants.UPLOAD_PATCH_FILE * 4, fail_if_false=True)
                Updateappliance.select_update_appliance()
                Updateappliance.tick_accept_licence()
                Updateappliance.click_update_option()

            else:
                logger.info("There is no option other than 'upload and install' or 'upload only' to upload the bin file. Hence canceling the operation")
                Updateappliance.click_cancel_button()
                return False

        else:
            logger.info("user has chosen option to upload file available")
            Updateappliance.tick_uploaded_image()
            if Updateappliance.verify_file_added(fail_if_false=False):
                Updateappliance.tick_accept_licence()
                Updateappliance.click_update_option()
            else:
                ui_lib.fail_test("unable to proceed as there is no file uploaded ", True)

        Updateappliance.wait_progress_bar_appear(60, fail_if_false=True)
        Updateappliance.wait_progress_bar_disappear(timeout=PerfConstants.UPGRADE_FUSION_APPLIANCE, fail_if_false=True)
        status = Updateappliance.wait_settings_page_to_appear(100, fail_if_false=True)
        logger.info("status is %s" % status)
    return True
