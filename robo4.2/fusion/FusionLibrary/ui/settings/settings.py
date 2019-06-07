"""Library for Fusion Settings UI page.

    = Table of contents =

    - `Revision Notes`
    - `Usage`
    - `Valid log levels`
    - `Examples`
    - `Importing`
    - `Shortcuts`
    - `Keywords`

    = Revision Notes =

    | Rev      | Date         |   Originator              |  Comments                      |
    | 0.0     |   07/10/2013  |   Andy Tran               |  skeleton code               |

    NOT YET IMPLEMENTED

    = Usage =

    This library has keywords for UI interaction with Fusion Settings page.

    = Valid log levels =

    None

    = Examples =

    Notice how keywords are linked from examples.

    | `Create Support Dump`      |  NOT YET IMPLEMENTED  |                |               |
    | `Download Audit Logs`      |  NOT YET IMPLEMENTED  |                |               |
    | `Create Certificate Signing Request`      |  NOT YET IMPLEMENTED  |                |               |
    | `Create Self Signed Certificate`      |  NOT YET IMPLEMENTED  |                |               |
    | `Import Certificate`      |  NOT YET IMPLEMENTED  |                |                |
    | `Update Appliance`      |  NOT YET IMPLEMENTED  |                |                |
    | `Edit Support Access`      |  NOT YET IMPLEMENTED  |                |                |
    | `Create Backup`      |    |                |                |
    | `Download Backup`      |    |                |                |
    | `Restore From Backup`      |    |                |                |
    | `Shut Down`      |  NOT YET IMPLEMENTED  |                |                |
    | `Restart`      |  NOT YET IMPLEMENTED  |                |                |
    | `Edit Appliance Details`      |  NOT YET IMPLEMENTED  |                |                |

"""

from FusionLibrary.ui.settings.settings_elements import FusionSettingsPage
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.general.login_elements import FusionLoginPage
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType, SubSectionType
from FusionLibrary.ui.business_logic.settings.supportdump import CreateSupportDump
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.settings.appliance import *
from RoboGalaxyLibrary.keywords.ntnative import *

from FusionLibrary.ui.business_logic.settings.addressandidentifiers import GeneralAddressesAndIdentifiers, CreateSubnetsAndAddressRange, VerifySubnetsAndAddressRange, \
    EditSubnetsAndAddressRange, DeleteSubnetsAndAddressRange, VerifySubnetsAndRangeAddressIdentifiersPage, VerifySubnetsAndRangeEditDialog, GetSubnetsAndAddressRangeAttributes

from datetime import datetime
import time
import os

ROBOT_LIBRARY_VERSION = '0.0'


def navigate():
    """Nvaigate to settings page"""
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)


def navigate_settings_base(currentpage, menulink):
    """ Navigate to settings base"""
    logger._log_to_console_and_log_file('\nNavigating to "{0}"'.format(currentpage))
    if not ui_lib.wait_for_element(currentpage):
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL)
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MENU_LINK_USERS_AND_GROUPS, 10)
        ui_lib.wait_for_element_and_click(menulink)
        ui_lib.wait_for_element(currentpage)


def create_support_dump(backupdirectory):
    """ Create and Download support dump for fusion appliance, the download will happen at 'C:\\DownloadFolder'
        NOTE :
        > As downloading fusion appliance back-up involves windows object,
        > and to handle the download window, we need to add below mentioned lines of code
        > in 'C:\Python27\Lib\site-packages\robotframework_selenium2library-1.2.0-py2.7.egg\Selenium2Library\resources\firefoxprofile\prefs.js'
        >
                user_pref("browser.download.folderList",2);
                user_pref("browser.download.dir",'C:\\DownloadFolder');
                user_pref("browser.helperApps.neverAsk.saveToDisk","application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
                user_pref("browser.download.manager.scanWhenDone", false);
                user_pref("browser.download.manager.showAlertOnComplete", true);
                user_pref("browser.download.manager.useWindow", false);
                user_pref("browser.helperApps.alwaysAsk.force", false);

        > This will make sure the download happens silently at the directory specified
    """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Create and download Support Dump")
    # CODE TO CREATE DOWNLOAD DIRECTORY AND DELETE FILES INSIDE, IF DIRECTORY EXISTS
    if not os.path.exists(backupdirectory):
        os.makedirs(backupdirectory)
    for root, dirs, files in os.walk(backupdirectory, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    # TO create the support dump for the given fusion appliance
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_CREATE_SUPPORT_DUMP)
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_CREATE_SUPPORTDUMP, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_YES_CREATE_SUPPORT_DUMP)
    else:
        ui_lib.fail_test("Failed to Create support dump", True)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_ACTVITY_SUPPORT_DUMP)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_CLICK_ACTIVITY)
    if ui_lib.wait_for_element(FusionSettingsPage.ID_TIMESTAMP_SUPPORT_DUMP):
        logging._log_to_console_and_log_file("Creation of support dump started")
        if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_VALIDATE_SUCCESS, 120):
            logging._log_to_console_and_log_file("Support dump created successfully")
        else:
            ui_lib.fail_test("Failed to Create Support Dump", True)
    else:
        logging._log_to_console_and_log_file("Support dump not yet started")

    while os.listdir(backupdirectory) == []:
        BuiltIn().sleep(2)
    # CODE TO WAIT TILL THE DOWNLOAD IS IN PROGRESS
    for files in os.listdir(backupdirectory):
        filesize = os.path.getsize(os.path.join(backupdirectory))
        logger._log_to_console_and_log_file("initial file size %s" % filesize)
        finalfilesize = 0
        while filesize != finalfilesize:
            BuiltIn().sleep(2)
            finalfilesize = os.path.getsize(os.path.join(backupdirectory))
            # logger._log_to_console_and_log_file("size %s" % finalfilesize)
            start = datetime.now()
            if(datetime.now() - start).total_seconds() > PerfConstants.DOWNLOAD_BACKUP_TIMEOUT:
                break


def download_audit_logs(folder=None):
    """ Download Audit Logs
        Download the Audit logs from Fusion
        Arguments:
            folder - the destination folder
    """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_SECURITY_LINK, fail_if_false=True)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_SECURITY_LINK)

    # Get the URL for the audit log file and download the file
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_AUDIT_LOGS, fail_if_false=True)
    ui_lib.download_file(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_AUDIT_LOGS, folder)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_SETTINGS_LINK, fail_if_false=True)

    logger.info('Audit log downloaded successfully in path "{0}"'.format(folder))
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_SETTINGS_LINK)


def create_self_signed_certificate(*props):  # pylint: disable=unused-argument
    """ Create Self Signed Certificate

        Not Yet Implemented


        Example:
        | `Create Self Signed Certificate`      |     |
    """
    pass


def create_certificate_signing_request(*props):  # pylint: disable=unused-argument
    """ Create Certificate Signing Request

        Not Yet Implemented


        Example:
        | `Create Certificate Signing Request`      |     |
    """
    pass


def import_certificate(cert):  # pylint: disable=unused-argument
    """ Import Certificate

        Not Yet Implemented


        Example:
        | `Import Certificate`      |     |
    """
    pass


def update_appliance(app_obj):
    """ Update Appliance

        Update the appliance

        Example:
        <update_appliance>
        <app selectimage="yes" bindirectory="C:\Downloads\" update_option="Upload only" version ="0266939"></app>
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
        if status:
            validate_appliance_version(app.version)
    return True


def edit_services_access(isEnabled):
    """
    Edit Support Access: function to enable or disable support access

    """
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Edit services access")
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_EDIT_SUPPORT_ACCESS)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_EDIT_SUPPORT_ACCESS)
    ui_lib.wait_for_element(FusionSettingsPage.ID_TOGGLE_BTN_SERVICE_ACCESS_ON)
    option_on = s2l.get_text(FusionSettingsPage.ID_TOGGLE_BTN_SERVICE_ACCESS_ON)
    option_off = s2l.get_text(FusionSettingsPage.ID_TOGGLE_BTN_SERVICE_ACCESS_OFF)
    current_status = "hp-checked" in s2l.get_element_attribute(FusionSettingsPage.ID_TOGGLE_BTN_SERVICE_ACCESS + "@class")

    if current_status is True and isEnabled.lower() == option_on.lower():
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_TOGGLE_OFF)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK_SUPPORT_ACCESS)
    elif current_status is False and isEnabled.lower() == option_off.lower():
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_TOGGLE_OFF)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK_SUPPORT_ACCESS)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK_SUPPORT_ACCESS)
    ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_STATUS)
    lablestatus = s2l.get_text(FusionSettingsPage.ID_LABEL_STATUS)
    if lablestatus.lower() == isEnabled.lower():
        logger._log_to_console_and_log_file("Services access is successfully updated from '%s' to '%s'" % ("Enabled" if current_status is True else "Disabled", isEnabled))
        return True
    else:
        logger._warn("Failed to edit Services access ")
        s2l.capture_page_screenshot()
        return False


def create_backup():
    """
    Create Backup : function to create fusion appliance backup
    """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Create Backup")
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_CREATE_BACKUP)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_BACKUP_NOTIFICATION)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LABEL_BACKUP_NOTIFICATION)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LABEL_CREATE_BACKUP)
    # waiting for the backup to be completed
    if ui_lib.wait_for_element_text(FusionSettingsPage.ID_LABEL_BACKUP_DETAILS, "Backup completed", PerfConstants.CREATE_BACKUP_TIMEOUT):
        logger._log_to_console_and_log_file("Create Backup Completed")
    else:
        ui_lib.fail_test("Failed to Create Backup", True)


def download_backup(backupdirectory):
    """ Download Backup for fusion appliance, the download will happen at 'C:\\BackupDownloadFolder'
        NOTE :
        > As downloading fusion appliance back-up involves windows object,
        > and to handle the download window, we need to add below mentioned lines of code
        > in 'C:\Python27\Lib\site-packages\robotframework_selenium2library-1.2.0-py2.7.egg\Selenium2Library\resources\firefoxprofile\prefs.js'
        >
                user_pref("browser.download.folderList",2);
                user_pref("browser.download.dir",'C:\\BackupDownloadFolder');
                user_pref("browser.helperApps.neverAsk.saveToDisk","application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
                user_pref("browser.download.manager.scanWhenDone", false);
                user_pref("browser.download.manager.showAlertOnComplete", true);
                user_pref("browser.download.manager.useWindow", false);
                user_pref("browser.helperApps.alwaysAsk.force", false);

        > This will make sure the download happens silently at the directory specified
    """

    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Download Backup")
    # CODE TO CREATE DOWNLOAD DIRECTORY AND DELETE FILES INSIDE, IF DIRECTORY EXISTS
    if not os.path.exists(backupdirectory):
        os.makedirs(backupdirectory)
    for root, dirs, files in os.walk(backupdirectory, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BACKUP_LINK)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_BACKUP)
    ui_lib.wait_for_element_text(FusionSettingsPage.ID_LABEL_BACKUP_DETAILS, "Download backup completed", PerfConstants.DOWNLOAD_BACKUP_TIMEOUT)

    while os.listdir(backupdirectory) == []:
        BuiltIn().sleep(2)
    # CODE TO WAIT TILL THE DOWNLOAD IS IN PROGRESS
    for files in os.listdir(backupdirectory):
        filesize = os.path.getsize(os.path.join(backupdirectory, files))
        logger._log_to_console_and_log_file("initial file size %s" % filesize)
        finalfilesize = 0
        while filesize != finalfilesize:
            BuiltIn().sleep(1)
            finalfilesize = os.path.getsize(os.path.join(backupdirectory, files))
            logger._log_to_console_and_log_file("size %s" % finalfilesize)
            start = datetime.now()
            if(datetime.now() - start).total_seconds() > PerfConstants.DOWNLOAD_BACKUP_TIMEOUT:
                break


def restore_from_backup(backupdirectory=None):
    """ Restore From Backup : restore backup for fusion appliance,
    "[LEGACY]"
    NOTE : This code is dependent on download_backup function, execute download_backup then go for restore_from_backup

    PRE-REQUISITES :
        > AutoIT used to upload back-up file to the appliance.
          Steps to configure AUTOIT,
            1. Download autoit-v3-setup and pywin32-218.win-amd64-py2.7 (or pywin32-214.win32-py2.7) to your system
            2. register AUTOITX3 , type on cmd prompt:
                C:\Program Files (x86)\AutoIt3\AutoItX>regsvr32 AutoItX3_x64.dll
                OR
                C:\Program Files (x86)\AutoIt3\AutoItX>regsvr32 AutoItX3.dll
            3. Download and install AUTOIT module from robot framework website.

    """
    logger._log_to_console_and_log_file(backupdirectory)
    if backupdirectory is not None:
        s2l = ui_lib.get_s2l()
        if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
            navigate()

        logger._log_to_console_and_log_file("Restore Backup")
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_RESTORE_FROM_BACKUP)
        ui_lib.wait_for_element_visible(FusionSettingsPage.ID_BTN_BROWSE_FILE, PerfConstants.RESTORE_BACKUP_CHOOSE_FILE)
        logger._log_to_console_and_log_file("Choose the restore backup file , " + backupdirectory + " from the path specified")
        # chooses the specific file
        for files in os.listdir(backupdirectory):
            filenamewithpath = os.path.join(backupdirectory, files)
            logger._log_to_console_and_log_file("File Name, along with the path  %s" % filenamewithpath)

        if not filenamewithpath:
            ui_lib.fail_test("Failed to find backup file ", True)

        s2l.choose_file(FusionSettingsPage.ID_BTN_BROWSE_FILE, filenamewithpath)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_BROWSE_FILE)

        # AutoIT code to click on open button
        # if os.name == "nt":
        # autoit = win32com.client.Dispatch("AutoItX3.Control")
        # autoit.ControlClick("File Upload", "", "Button1")

        s2l.wait_until_page_contains("This file is compatible", PerfConstants.FILE_COMPATIBILITY_CHECK)
        logger._log_to_console_and_log_file("uploaded backup file")
        s2l.select_checkbox(FusionSettingsPage.ID_CHECKBOX_RESTORE_CONFIRMATION)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_RESTORE_FROM_BACKUP)
        # need to confirm, by clicking the restore from backup button again
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_RESTORE_FROM_BACKUP)

        # waiting for restore to finish
        ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_RESTORING_FROM_BACKUP, PerfConstants.RESTORING_LABEL_VISIBLE)
        ui_lib.wait_for_element_notvisible(FusionSettingsPage.ID_LABEL_RESTORING_FROM_BACKUP, PerfConstants.RESTORING_LABEL_VISIBLE)
        ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_RESTORING, PerfConstants.RESTORING_LABEL_VISIBLE)
        ui_lib.wait_for_element_notvisible(FusionSettingsPage.ID_LABEL_RESTORING, PerfConstants.RESTORE_DATA_FROM_BACKUP_TIME)
        logger._log_to_console_and_log_file("Restore Completed, checking if the login page is visible.")

        # final check for login page existence
        ui_lib.wait_for_element(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
        logger._log_to_console_and_log_file("Restore Successful for Fusion Appliance")

    else:

        logger.info("WITHOUT BACKUPDIRECTORY")
        if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
            navigate()

        logger._log_to_console_and_log_file("Restore Backup")
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BACKUP_LINK)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_RESTORE_BACKUP)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_RESTORE_LABEL)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_CHECKBOX_RESTORE)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_RESTORE_CONFIRM)
        logger.info("Restore in Progress")

        # waiting for restore to finish
        ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_RESTORING_FROM_BACKUP, PerfConstants.RESTORING_LABEL_VISIBLE)
        ui_lib.wait_for_element_notvisible(FusionSettingsPage.ID_LABEL_RESTORING_FROM_BACKUP, PerfConstants.RESTORING_LABEL_VISIBLE)
        ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_RESTORING, PerfConstants.RESTORING_LABEL_VISIBLE)
        ui_lib.wait_for_element_notvisible(FusionSettingsPage.ID_LABEL_RESTORING, PerfConstants.RESTORE_DATA_FROM_BACKUP_TIME)
        logger._log_to_console_and_log_file("Restore Completed, checking if the login page is visible.")

        # final check for login page existence
        ui_lib.wait_for_element(FusionLoginPage.ID_BTN_LOGIN_BUTTON)
        logger._log_to_console_and_log_file("Restore Successful for Fusion Appliance")


def shut_down():
    """ Shut Down

        Shutdown the fusion appliance

        Example:
        | `Shut Down`      |     |
    """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()
    logger._log_to_console_and_log_file("Shutdown Appliance")
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_SHUTDOWN)
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_TEXT_SHUTDOWN):
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_YES_CONFIRM_SHUTDOWN)
    else:
        ui_lib.fail_test('Failed: The message while shutting down the appliance is not displayed')
    # Checking whether the fusion appliance started shutting down or not
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_WAITING, PerfConstants.RESTART_LABEL_VISIBLE):
        logger._log_to_console_and_log_file("The fusion appliance is getting shutdown")
    else:
        ui_lib.fail_test('Failed: The fusion appliance failed to shutdown')
    # Checking whether the fusion appliance is shut down or not
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_UNAVAILABLE, PerfConstants.STARTING_PROGRESS_VISIBLE):
        logger._log_to_console_and_log_file("The fusion appliance is shutdown successfully ")
    else:
        ui_lib.fail_test('Failed: The fusion appliance failed to shutdown the appliance in the restart procedure')


def restart():
    """ Restart

        Restarts the given fusion appliance

        Example:
        | `Restart`      |     |
    """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_APPLIANCE_LINK)

    logger._log_to_console_and_log_file("Restart Appliance")
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_RESTART)
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_RESTART):
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_YES_CONFIRM_SHUTDOWN)
    else:
        ui_lib.fail_test('Failed: The message while restarting the appliance is not displayed')
    # Check whether the fusion appliance is restarting
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_TEXT_RESTARTING, PerfConstants.RESTART_LABEL_VISIBLE):
        logger._log_to_console_and_log_file("The fusion appliance is restarting ")
    else:
        ui_lib.fail_test('Failed: The fusion appliance failed to display restarting label')
    # Checking whether the fusion appliance started to coming up
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_PROGRESS, PerfConstants.STARTING_PROGRESS_VISIBLE):
        logger._log_to_console_and_log_file("The fusion appliance is powered on successfully and waiting for the appliance")
    else:
        ui_lib.fail_test('Failed: The fusion appliance dint get powered on successfully and appliance couldnot start')
    # Checking whether the fusion appliance home page
    if ui_lib.wait_for_element_notvisible(FusionSettingsPage.ID_LABEL_PROGRESS, PerfConstants.STARTING_PROGRESS_VISIBLE):
        if ui_lib.wait_for_element_visible(FusionDashboardPage.ID_PAGE_LABEL, PerfConstants.FUSION_LOGIN_TIME):
            logger._log_to_console_and_log_file("The fusion appliance is restarted successfully")
    else:
        ui_lib.fail_test('Failed: The fusion appliance did not come up after restart')


def edit_appliance_details(*props):  # pylint: disable=unused-argument
    """ Edit Appliance Details

        Not Yet Implemented


        Example:
        | `Edit Appliance Details`      |     |
    """
    pass


def edit_address_and_identifier(*edit_add_iden):
    """ edit_address_and_identifier

        Example:
        | `edit_address_and_identifier`      | edit_add_iden    |
    """
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_ADDRESS_AND_IDENTIFIER)
    # s2l.mouse_over(FusionSettingsPage.ID_LINK_ADDRESS_AND_IDENTIFIER)
    # s2l.mouse_up("//div[@id='cic-settings-guid-panel']/header/a[text()='Edit']")
    s2l.click_element(FusionSettingsPage.ID_LINK_EDIT_ADDRESS_AND_IDENTIFIER)

    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_DIALOG_EDIT_ADDRESS_AND_IDENTIFIER) is False:
        ui_lib.fail_test("Edit Address and Identifier dialog not show up.", True)

    # Check for the edit link, if now highlighted by mouse over then the fn will exit.
    # if not ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_EDIT_ADDRESS_AND_IDENTIFIER):
    #    ui_lib.fail_test("Not able to edit Address and Identifier", True)

    logger._log_to_console_and_log_file("Editing Address and Identifier.")
    edit_obj = list(edit_add_iden[0])

    # ======================== MAC ADDRESS=======================================
    # select MAC ADDRESS from dropdown
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DROPDOWN_EDIT_SELECTOR)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_MAC_ADDRESS)

    # Enable Virtual for MAC Address
    ui_lib.wait_for_element(FusionSettingsPage.ID_CHKBOX_MAC_ENABLE_VIRTUAL)
    if edit_obj[0].mac.enablevirtual.lower() == "true":
        s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_MAC_ENABLE_VIRTUAL)
    else:
        s2l.unselect_checkbox(FusionSettingsPage.ID_CHKBOX_MAC_ENABLE_VIRTUAL)

    # CODE TO ADD CUSTOM RANGE FOR MAC Address
    addcustomranges = None
    if edit_obj[0].mac.has_property('addcustomrange'):
        addcustomranges = edit_obj[0].mac.addcustomrange

    if addcustomranges is None:
        logger._warn("There is no MAC ADDRESS Custom range to be added")

    if isinstance(addcustomranges, (list)) and edit_obj[0].mac.enablevirtual.lower() == "true":
        for addrange in addcustomranges:
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_MAC_ADD_CUSTOM_RANGE)
            ret_custom_mac = _add_custom_range(addrange, FusionSettingsPage.ID_TABLE_MAC_BASE)
            # ENABLE CUSTOM RANGE ADDED
            if ret_custom_mac:
                macrange = addrange.rangefrom.replace(':', '--')
                if addrange.enabled.lower() == "true":
                    s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_MAC_ENABLE % macrange)
                else:
                    s2l.unselect_checkbox(FusionSettingsPage.ID_CHKBOX_MAC_ENABLE % macrange)

    # Add Auto Generated MAC Address
    if edit_obj[0].mac.autoflag[0].addautogenerated.lower() == "true" and edit_obj[0].mac.enablevirtual.lower() == "true":
        for _ in xrange(0, int(edit_obj[0].mac.autoflag[0].addautogenratedcount)):  # pylint: disable=unused-variable
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_AUTO_GENERATED_MAC)
            return_auto_from = _add_auto_generated_range(FusionSettingsPage.ID_TABLE_MAC_BASE)
            # Enable Auto Generated MAC Address
            if not isinstance(return_auto_from, (bool)):
                macautorange = return_auto_from.replace(':', '--')
                s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_MAC_ENABLE % macautorange)
                logger._log_to_console_and_log_file("Successfully Added AUTO GENERATED MAC Address. Starts from %s" % return_auto_from)

    # ============================WORLD WIDE NAMES===========================
    # select World Wide Names from dropdown
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DROPDOWN_EDIT_SELECTOR)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_WWN)

    # Enable Virtual for WWN
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_CHKBOX_WWN_ENABLE_VIRTUAL)
    if edit_obj[0].wwn.enablevirtual.lower() == "true":
        s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_WWN_ENABLE_VIRTUAL)
    else:
        s2l.unselect_checkbox(FusionSettingsPage.ID_CHKBOX_WWN_ENABLE_VIRTUAL)

    # CODE TO ADD CUSTOM RANGE FOR WWN
    addwwncustomranges = None
    if edit_obj[0].wwn.has_property('addcustomrange'):
        addwwncustomranges = edit_obj[0].wwn.addcustomrange

    if addwwncustomranges is None:
        logger._warn("There is no WWN Custom range to be added")

    if isinstance(addwwncustomranges, (list)) and edit_obj[0].wwn.enablevirtual.lower() == "true":
        for addrange in addwwncustomranges:
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_WWN_ADD_CUSTOM_RANGE)
            ret_custom_wwn = _add_custom_range(addrange, FusionSettingsPage.ID_TABLE_WWN_BASE)
            # ENABLE CUSTOM RANGE ADDED
            if ret_custom_wwn:
                macrange = addrange.rangefrom.replace(':', '--')
                if addrange.enabled.lower() == "true":
                    s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_WWN_ENABLE % macrange)
                else:
                    s2l.unselect_checkbox(FusionSettingsPage.ID_CHKBOX_WWN_ENABLE % macrange)

    # Add Auto Generated WWN Address
    if edit_obj[0].wwn.autoflag[0].addautogenerated.lower() == "true" and edit_obj[0].wwn.enablevirtual.lower() == "true":
        for x in xrange(0, int(edit_obj[0].wwn.autoflag[0].addautogenratedcount)):     # pylint: disable=unused-variable
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_AUTO_GENERATED_WWN)
            return_auto_from = _add_auto_generated_range(FusionSettingsPage.ID_TABLE_WWN_BASE)
            # Enable Auto Generated MAC Address
            if not isinstance(return_auto_from, (bool)):
                macautorange = return_auto_from.replace(':', '--')
                s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_WWN_ENABLE % macautorange)
                logger._log_to_console_and_log_file("Successfully Added AUTO GENERATED WWN. Starts from %s" % return_auto_from)

    # ============================SERIAL NUMBERS===========================
    # select SERIAL NUMBER from dropdown
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DROPDOWN_EDIT_SELECTOR)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_SERIAL_NO)

    # Enable Virtual for SERIAL NO.
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_CHKBOX_SERIAL_NO_ENABLE_VIRTUAL)
    if edit_obj[0].serialno.enablevirtual.lower() == "true":
        s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_SERIAL_NO_ENABLE_VIRTUAL)
    else:
        s2l.unselect_checkbox(FusionSettingsPage.ID_CHKBOX_SERIAL_NO_ENABLE_VIRTUAL)

    # CODE TO ADD CUSTOM RANGE FOR SERIAL NUMBER
    addserialcustomranges = None
    if edit_obj[0].serialno.has_property('addcustomrange'):
        addserialcustomranges = edit_obj[0].serialno.addcustomrange

    if addserialcustomranges is None:
        logger._warn("There is no SERIAL NUMBER Custom range to be added")

    if isinstance(addserialcustomranges, (list)) and edit_obj[0].serialno.enablevirtual.lower() == "true":
        for addrange in addserialcustomranges:
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_SERIAL_NO_ADD_CUSTOM_RANGE)
            ret_custom_sn = _add_custom_range(addrange, FusionSettingsPage.ID_TABLE_SERIAL_NO_BASE)
            # ENABLE CUSTOM RANGE ADDED
            if ret_custom_sn:
                serialno_val = "VCU" + addrange.rangefrom
                if addrange.enabled.lower() == "true":
                    s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_SERIAL_NO_ENABLE % serialno_val)
                else:
                    s2l.unselect_checkbox(FusionSettingsPage.ID_CHKBOX_SERIAL_NO_ENABLE % serialno_val)

    # Add Auto Generated SERIAL NUMBER
    if edit_obj[0].serialno.autoflag[0].addautogenerated.lower() == "true" and edit_obj[0].serialno.enablevirtual.lower() == "true":
        for x in xrange(0, int(edit_obj[0].serialno.autoflag[0].addautogenratedcount)):
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_AUTO_GENERATED_SERIAL_NO)
            return_auto_from = _add_auto_generated_range(FusionSettingsPage.ID_TABLE_SERIAL_NO_BASE)
            # Enable Auto Generated MAC Address
            if not isinstance(return_auto_from, (bool)):
                s2l.select_checkbox(FusionSettingsPage.ID_CHKBOX_SERIAL_NO_ENABLE % return_auto_from)
                logger._log_to_console_and_log_file("Successfully Added AUTO GENERATED SERIAL NUMBER starting from %s" % return_auto_from)

    # =======================================================================
    # DONE with EDITS related to ADDRESS and IDENTIFIER LINK, now click on OK, to save changes
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK)
    ui_lib.wait_for_element_notvisible(FusionSettingsPage.ID_EDIT_MESSAGE_SUMMARY)

    return True


def verify_address_and_identifier_used_number(*address_obj):
    """ verify_address_and_identifier_used_number

        Example:
        | `verify_address_and_identifier_used_number`      | add_iden    |
    """
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_ADDRESS_AND_IDENTIFIER)
    s2l.click_element(FusionSettingsPage.ID_LINK_CLICK_ADDRESS_AND_IDENTIFIER)

    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_PAGE_ADDRESS_AND_IDENTIFIER) is False:
        ui_lib.fail_test("Edit Address and Identifier dialog not show up.", True)

    if isinstance(address_obj, test_data.DataObj):
        address_obj = [address_obj]
    elif isinstance(address_obj, tuple):
        address_obj = list(address_obj[0])

    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_TEXT_MAC_COUNT)
    mac_count = int(s2l.get_text(FusionSettingsPage.ID_TEXT_MAC_COUNT))
    mac_allocated = int(s2l.get_text(FusionSettingsPage.ID_TEXT_MAC_ALLOCATED))
    mac_remaining = int(s2l.get_text(FusionSettingsPage.ID_TEXT_MAC_REMAINING))
    wwn_count = int(s2l.get_text(FusionSettingsPage.ID_TEXT_WWN_COUNT))
    wwn_allocated = int(s2l.get_text(FusionSettingsPage.ID_TEXT_WWN_ALLOCATED))
    wwn_remaining = int(s2l.get_text(FusionSettingsPage.ID_TEXT_WWN_REMAINING))
    sn_count = int(s2l.get_text(FusionSettingsPage.ID_TEXT_SN_COUNT))
    sn_allocated = int(s2l.get_text(FusionSettingsPage.ID_TEXT_SN_ALLOCATED))
    sn_remaining = int(s2l.get_text(FusionSettingsPage.ID_TEXT_SN_REMAINING))

    for _, address in enumerate(address_obj):
        expect_mac_allocated = int(address.MAC_count)
        expect_wwn_allocated = int(address.WWN_count)
        expect_sn_allocated = int(address.SN_count)

        if mac_allocated != expect_mac_allocated:
            ui_lib.fail_test("Allocated MAC addresses number are not equal with expected", True)

        if wwn_allocated != expect_wwn_allocated:
            ui_lib.fail_test("Allocated World Wide Names number are not equal with expected", True)

        if sn_allocated != expect_sn_allocated:
            ui_lib.fail_test("Allocated Serial Numbers number are not equal with expected", True)

    if mac_remaining == mac_count - mac_allocated \
            and wwn_remaining == wwn_count - wwn_allocated \
            and sn_remaining == sn_count - sn_allocated:
        logger.info("The remaining number of MAC,WWN and SN is correctly")
    else:
        ui_lib.fail_test("The remaining number are not correctly, please check.", True)

    logger.info("The number of MAC,WWN,SN allocated number do not increase due to unused by server profile or not set to physical")

    return True


def _add_custom_range(addrange, table_locator):
    """
        _add_custom_range(addrange)
        function called when adding custom range while editing address and identifier on settings page
    """
    s2l = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_ADD_CUSTOM_RANGE_FROM, addrange.rangefrom)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_ADD_CUSTOM_RANGE_TO, addrange.to)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_ADD_CUSTOM_RANGE_COUNT, addrange.count)

    # check for errors, if any !! click cancel and proceed for the next add custom WWN
    actual_xpath_count = len(s2l._element_find(FusionSettingsPage.ID_LABEL_ERROR_ADD_CUSTOM, False, False))
    if int(actual_xpath_count) != 0:
        logger._warn(" custom range add failed as there is error while filling info, Custom range from : '%s'" % addrange.rangefrom)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_CANCEL_MAC_CUSTOM_ADD)
        s2l.capture_page_screenshot()
        return False
    else:
        # No Error, Clicking on add
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ADD_CUSTOM_RANGE)
        if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_CUSTOM_ADD_OVERLAPPING_ERROR):
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_CANCEL_MAC_CUSTOM_ADD)
            logger._warn(" Cannot create overlapping pool. Please select a different range, CURRENT RANGE PASSED - '%s'" % addrange.rangefrom)
            s2l.capture_page_screenshot()
            return False
        else:
            # check for custom range in table after addition.
            from_element = s2l._table_element_finder.find_by_content(s2l._current_browser(), table_locator, addrange.rangefrom)
            to_element = s2l._table_element_finder.find_by_content(s2l._current_browser(), table_locator, addrange.to)

            if from_element is None or to_element is None:
                logger._warn(" Custom Range not reflecting in table, range starting from %s" % addrange.rangefrom)
                s2l.capture_page_screenshot()
                return False
            else:
                logger._log_to_console_and_log_file("Added CUSTOM RANGE starting from %s" % addrange.rangefrom)
                return True


def _add_auto_generated_range(table_locator):
    """
       _add_auto_generated_range(table_locator)
       function called when adding auto generated range to edit address and identifiers
    """
    s2l = ui_lib.get_s2l()
    ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_AUTO_GENERATED_FROM)
    auto_from = s2l.get_text(FusionSettingsPage.ID_LABEL_AUTO_GENERATED_FROM)
    auto_to = s2l.get_text(FusionSettingsPage.ID_LABEL_AUTO_GENERATED_TO)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_AUTO_GENERATE_ADD)
    from_element = s2l._table_element_finder.find_by_content(s2l._current_browser(), table_locator, str(auto_from))
    to_element = s2l._table_element_finder.find_by_content(s2l._current_browser(), table_locator, str(auto_to))

    if from_element is None or to_element is None:
        logger._warn(" Auto Generated MAC Address not reflecting in MAC table,MAC address starts from %s" % auto_from)
        s2l.capture_page_screenshot()
        return False
    else:
        logger._log_to_console_and_log_file("Added AUTO GENERATED RANGE")
        return auto_from


def editDevelopmentSettings(*props):    # pylint: disable=unused-argument
    """ Create Support Dump

        Not Yet Implemented


        Example:
        | `Create Support Dump`      |     |
    """
    pass


def editSecurity(*props):   # pylint: disable=unused-argument
    """ Create Support Dump

        Not Yet Implemented


        Example:
        | `Create Support Dump`      |     |
    """
    pass


def add_license(*license_obj):
    """ Add License
        add license to the fusion appliance
        Prerequisite: license dat file should be placed "C:\robogalaxy\dev\robogalaxy\tools\licenses\fusion"
        Example:
        | `Add License`      | ${license_obj}    |
    """

    logger._log_to_console_and_log_file("Add License to appliance")
    s2l = ui_lib.get_s2l()

    """ Call function to navigate to licenses """
    _Navigate_To_Licenses()

    """ Retrieve data from datasheet """
    if isinstance(license_obj, test_data.DataObj):
        license_obj = [license_obj]
    elif isinstance(license_obj, tuple):
        license_obj = list(license_obj[0])

    fail = 0
    for lic in license_obj:

        """ Get the License name strlicense"""
        strlicense = getattr(lic, 'type', '')
        if strlicense not in ['HP OneView w/o iLO', 'HP OneView']:
            logger._warn("Given license type is not supported by fusion. Expected type is 'HP OneView w/o iLO' or 'HP OneView'")
            s2l.capture_page_screenshot()
            fail += 1
            continue

#         if getattr(lic, 'licensepath', '') != '':
#             if re.search(r'noiLO_\d+\.dat$', lic.licensepath):
#                 logger._log_to_console_and_log_file("check for the existence of HP OneView w/o iLO license")
#                 strlicense = "HP OneView w/o iLO"
#             elif re.search(r'\d+\.dat$', lic.licensepath):
#                 logger._log_to_console_and_log_file("check for the existence of HP OneView license ")
#                 strlicense = "HP OneView"
#             else:
#                 logger._warn("Given license is not supported by fusion")
#                 fail += 1
#                 continue

        """ Call function to check the availability of license """
        strVal = check_availability_licenses(strlicense)
        if not strVal:
            logger._log_to_console_and_log_file("License %s does not exists,Add the license now" % strlicense)
            if getattr(lic, 'licensepath', '') != '':
                fopen = open(lic.licensepath)
                strLincenseKey = fopen.read()
            else:
                strLincenseKey = getattr(lic, 'content', '')
                if strLincenseKey == '':
                    BuiltIn().fail("Please specify content attribute for holding license key")
            """ Read the license key from the given path"""
            # with open(lic.licensepath, 'r') as f:
            # f.next()
            # line = f
            # logger._log_to_console_and_log_file("HP OneView license1 = ")
            # for line in f:
            # strLincenseKey = line
            # logger._log_to_console_and_log_file("HP OneView license = " % line)
            # f.closed
            """ Entering inputs in ADD License Page """
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
            ui_lib.wait_for_element_visible(FusionSettingsPage.ID_MENU_ACTION_ADDLICENSE)
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_ADDLICENSE)
            ui_lib.wait_for_element_visible(FusionSettingsPage.ID_DLG_ADDLICENSE, fail_if_false=True)
            # s2l.input_text(FusionSettingsPage.ID_INPUT_LICENSEKEY, strLincenseKey)
            s2l.execute_javascript("$('#fs-license-licenseKeyValue').val('%s');return true;" % strLincenseKey)
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DLG_BTN_ADD)

            """ Check for Error messages """
            if not ui_lib.wait_for_element(FusionSettingsPage.ID_ADDLICENSE_ERR_MSG):

                if not check_availability_licenses(strlicense):
                    logger._warn("Fail in Adding License %s" % strlicense)
                    s2l.capture_page_screenshot()
                    fail += 1
                else:
                    logger._log_to_console_and_log_file("License %s is added successfully" % strlicense)

            else:
                strErr = s2l._get_text(FusionSettingsPage.ID_ADDLICENSE_ERR_MSG)
                logger._warn("Unable to Add License %s,and the Err Msg is %s" % (strlicense, strErr))
                ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DLG_BTN_CANCEL)
                s2l.capture_page_screenshot()
                fail += 1
        else:
            logger._log_to_console_and_log_file("License %s available with licenses,Check the other License" % strlicense)
    if fail > 0:
        return False
    else:
        return True


def check_availability_licenses(strlicense):
    """ check_availability_licenses

        Example:
        | check_availability_licenses("HP OneView")
    """

    s2l = ui_lib.get_s2l()

    """ Call function to navigate to licenses """
    _Navigate_To_Licenses()

    """ Check the availability of license in Licenses Page and get the License Number """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_LICENSE_AVAILABILITY % strlicense):
        if strlicense == 'HP OneView':
            strlicense = 'HP OneView Advanced'
        elif strlicense == 'HP OneView w/o iLO':
            strlicense = 'HP OneView Advanced w/o iLO'
    if ui_lib.wait_for_element(FusionSettingsPage.ID_LICENSE_AVAILABILITY % strlicense):
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_AVAILABLE_LICENSE % strlicense)
        intAvailableLicense = s2l._get_text(FusionSettingsPage.ID_AVAILABLE_LICENSE % strlicense)
        intAvlLicense = intAvailableLicense.split()

        if int(intAvlLicense[0].strip()) > 0:
            logger._log_to_console_and_log_file("License %s available with %s licenses" % (strlicense, str(intAvlLicense[0])))
            return True
        else:
            logger._log_to_console_and_log_file("License %s available with %s licenses" % (strlicense, str(intAvlLicense[0])))
            s2l.capture_page_screenshot()
            return False
    else:
        logger._log_to_console_and_log_file("License %s not available " % strlicense)
        s2l.capture_page_screenshot()
        return False


def _Navigate_To_Licenses():
    """ _Navigate_To_Licenses

        Example:
        | _Navigate_To_Licenses()
    """

    """ Navigate to Settings Page """
    selenium2lib = ui_lib.get_s2l()
    if ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_LICENSES_TITLE):
        return True

    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, fail_if_false=True)
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MENU_LINK_SETTINGS, fail_if_false=True)
        ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL, timeout=10, fail_if_false=True)

    if ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        logger._log_to_console_and_log_file("Navigated successfully to Settings Page")
        ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_LICENSE, fail_if_false=True)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_LICENSE, fail_if_false=True)

        if ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_LICENSES_TITLE):
            logger._log_to_console_and_log_file("Navigated successfully to Licenses")
            return True
        else:
            ui_lib.fail_test("Fail to Navigate Licenses")
            selenium2lib.capture_page_screenshot()
            return False


def del_directory_server(dServer, fail_on_err):
    """ del directory server from the appliance
        Example:
        settings.del_directory_users_and_groups(dServer, fail_on_err)
    """

    # Navigate to the 'Settings' page
    navigate()
    selenium2lib = ui_lib.get_s2l()
    # Find the 'Security' Frame
    ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SECURYTY_HEADER)

    # Does the server exist in 'Directories' field (list of existing directories).
    directories = selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_DIRECTORIES)
    logger._log_to_console(directories)
    if dServer.domainName in directories:
        logging._log_to_console_and_log_file("Removing directory server '%s'" % dServer.domainName)
        # Press the Edit Icon (next to Security).
        selenium2lib.click_element(FusionSettingsPage.ID_SECURITY_EDIT)
        # ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_SECURITY_EDIT)
        # wait until table is visible
        ui_lib.wait_for_element_visible(FusionSettingsPage.ID_BTN_ADD_DIRECTORY_SETTINGS)
        # click X to delete the server
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DIRECTORY_DEL % dServer.domainName)
        # confirm yes
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_REMOVE_SERVER_YES_BUTTON)

        # Click on OK Button
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_SECURITY_OK_BUTTON)
        # Navigate to Setting page
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_PAGE_LABEL)
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MENU_LINK_SETTINGS)

        # validate server is deleted
        if ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SERVER_ALREADY_ADDED):
            logging._warn("ERROR deleting the directory server '%s' was not deleted" % dServer.domainName)
            selenium2lib.capture_page_screenshot()
            return False
    else:
        if fail_on_err:
            logging._warn("Cannot delete - directory server did not exist in the list: '%s'" % dServer.domainName)
            ui_lib.fail_test("Cannot delete - directory server did not exist: '%s'" % dServer.domainName)
        selenium2lib.capture_page_screenshot()
        return False
    directories = selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_DIRECTORIES)
    if dServer.domainName in directories:
        logger._warn("Directory server %s is still in the list" % dServer.domainName)
        selenium2lib.capture_page_screenshot()
        return False
    return True


def add_directory_server(dServer):
    """ add directory server to the appliance
        called by function usersandgroups.add_directory_users_and_groups
        Example:
        settings.add_directory_users_and_groups(dServer)
    """
    # Navigate to the 'Settings' page
    navigate()
    selenium2lib = ui_lib.get_s2l()

    # Find the 'Security' Frame
    ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SECURYTY_HEADER)
    # Get text from 'Directories' field (list of existing directories).
    directories = selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_DIRECTORIES)
    if dServer.domainName in directories:
        logging._log_to_console_and_log_file("directory is already added with name '%s'" % dServer.domainName)
        return True

    logging._log_to_console_and_log_file("adding directory server")
    # Press the Edit Icon (next to Security).
    # NOTE: This command fails when using the ui_lib.wait_for_element_and_click() function.
    selenium2lib.click_element(FusionSettingsPage.ID_SECURITY_EDIT)

    # Wait for and click on the 'Add Directory' button
    ui_lib.wait_for_element(FusionSettingsPage.ID_BTN_ADD_DIRECTORY_SETTINGS)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ADD_DIRECTORY_SETTINGS)

    # Directory name
    ui_lib.wait_for_element(FusionSettingsPage.ID_INPUT_DIR_NAME)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_DIR_NAME, dServer.domainName)
    # Directory type - Chose 'Active Directory' or 'OpenLDAP'
    ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_AD_OR_LDAP_SELECTION, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_ELEMENT_AD_OR_LDAP_SELECTION)
    # Find out how many items are in the list
    # itemCount = len(selenium2lib.get_list_items("xpath=//*[@id='fs-settings-authn-dir-type-select']"))

    desiredText = ""
    if dServer.has_property("ldapServer") and dServer.ldapServer == "True":
        # Select OpenLDAP Directory type
        desiredText = "OpenLDAP"
    else:
        # Default to Active Directory type
        desiredText = "Active Directory"

    # For the record, we were supposed to be able to simulate a PgUp press to select the 1st element
    # then simulate hitting the Down arrow until we see the desired text in the HTML element
    # But here we're hitting the 1st letter of the desired text so as to try & select it

    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_ELEMENT_SELECT_OPTION % desiredText)

    # Fail if we didn't find it
    if ui_lib.wait_for_element_text(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT, desiredText) is False:
        ui_lib.fail_test("Desired text " + desiredText + " not found.")
        selenium2lib.capture_page_screenshot()
        return False
    # Log that we do indeed have the desired text
    logger._log_to_console_and_log_file("Finally got text: '" + selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT) + "'")
    # NOTE: If the UI seems to be going haywire & preventing Selenium from hitting "Add Directory", insert an Enter key-press here
    # selenium2lib.press_key(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT, '\\13')

    # Search context
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_BASE_DN, dServer.top)
    if desiredText == "OpenLDAP" and dServer.has_property("org"):
        # org values in data sheet - org= "OU=People;OU=Groups "
        orgval = dServer.org.split(";")
        orgxpath = FusionSettingsPage.ID_ORGANIZATIONAL_UNIT
        ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_ORGANIZATIONAL_UNIT, orgval[0])

        for i in range(1, len(orgval)):
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_ADD_ORG_UNIT)
            val = "text" + str(i)
            additionalOrgXpath = orgxpath.replace("text", val)
            ui_lib.wait_for_element_and_input_text(additionalOrgXpath, orgval[i])

    # Credentials (Username & Password)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_AUTHN_USERNAME, dServer.userName)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_AUTHN_PASSWORD, dServer.userPswd)
    # Add Directory Server button
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LABEL_DIRECTORY_SERVERS)
    BuiltIn().sleep(2)
    counter = 0
    while counter < 3:
        logger._log_to_console_and_log_file("====Click add directory button.")
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ADD_DIRECTORY)
        # Wait for dialog appear
        if ui_lib.wait_for_element_visible("id=fs-authn-add-dir-server-dlg") is False:
            counter = counter + 1
        else:
            break

        if counter >= 3:
            ui_lib.fail_test("Failed to wait add dir server dialog displayed")
    # IP address or host name
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_IPADDRESS, dServer.server)
    # Directory server port
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_SERVER_PORT, dServer.port)

    if not dServer.certificate == "True":
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_DIRECTORY_SERVER_ADD)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_TRUST_BUTTON)
    else:
        selenium2lib.click_element(FusionSettingsPage.ID_CERT_CHECKBOX)

        # get certificate content according to certificate type
        # cert_obj = get_data_by_xpath("//directorycerts/directorycert[@type='%s']" % dServer.certType)

        test_data_file = BuiltIn().get_variable_value("${DataFile}")
        import xml.etree.cElementTree as ET
        tree = ET.ElementTree(file=test_data_file)
        cert_content = ""
        for elt in tree.iterfind(".//directorycerts/directorycert[@type='%s']" % dServer.certType):
            cert_content = elt.text
            break
        else:
            ui_lib.fail_test("not found certificate content in test data (.//directorycerts/directorycert[@type='%s'])" % dServer.certType)

            browser = selenium2lib._current_browser()
            cert_content = cert_content.replace("\n", "\\n")
            browser.execute_script("document.getElementById('%s').value = '%s';" % (FusionSettingsPage.JS_ID_INPUT_CERTIFICATE, cert_content))
    # Click on Add button
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_DIRECTORY_SERVER_ADD)

    # validate server is added
    ui_lib.wait_for_element(FusionSettingsPage.ID_BTN_ADD_DIR)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ADD_DIR)

    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_AD_OK_BUTTON)
    if not ui_lib.wait_for_element_visible(FusionSettingsPage.ID_DISABLE_ACCESS_SUPPORT_ERROR):
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_TOGGLE_BTN_SERVICE_ACCESS)

    selenium2lib.wait_until_page_contains_element(FusionSettingsPage.ID_SECURITY_OK_BUTTON, 30)
    selenium2lib.click_element(FusionSettingsPage.ID_SECURITY_OK_BUTTON)

    if ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SERVER_ALREADY_ADDED):
        logging._log_to_console_and_log_file("Directory server '%s' is added in the appliance" % dServer.domainName)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_DIR_SERVER_CANCEL)
        return True

    ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SECURYTY_HEADER)
    # ui_lib.wait_for_element(FusionSettingsPage.ID_SECURITY_EDIT)
    directories = selenium2lib.get_text(FusionSettingsPage.ID_SERVER % dServer.domainName)
    if dServer.domainName in directories:
        logging._log_to_console_and_log_file("Directory server '%s' is added in the appliance" % dServer.domainName)
        return True

    ui_lib.fail_test("failed to add directory server '%s'  in the appliance" % dServer.domainName)
    selenium2lib.capture_page_screenshot()
    return False


def add_alert_notifications(*notifications_obj):
    """ Add alert notification """

    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    """ Retrieve data from datasheet """
    if isinstance(notifications_obj, test_data.DataObj):
        notifications_obj = [notifications_obj]
    elif isinstance(notifications_obj, tuple):
        notifications_obj = list(notifications_obj[0])

    notifications = notifications_obj[0].notification
    alertfilters = notifications_obj[0].filter

    for notification in notifications:
        if len(notification.senderemail.strip()) > 0:
            logger._log_to_console_and_log_file("\nAdding Notifications %s..." % notification.name)
            ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_NOTIFICATIONS)
            ui_lib.move_to_element_and_click(FusionSettingsPage.ID_LINK_EDIT_NOTIFICATIONS, FusionSettingsPage.ID_LINK_EDIT_NOTIFICATIONS)
            ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_EDIT_NOTIFICATIONS)
            if selenium2lib._is_element_present(FusionSettingsPage.ID_LABEL_EDIT_NOTIFICATIONS):
                ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_TXT_EDIT_NOTIFICATIONS_SENDER_EMAIL, notification.senderemail)
                if len(notification.senderpassword.strip()) > 0:
                    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_TXT_EDIT_NOTIFICATIONS_SENDER_PASSWORD, notification.senderemail)
                if len(notification.smtpserver.strip()) > 0:
                    selenium2lib.select_checkbox(FusionSettingsPage.ID_CHCKBOX_SMTP_OPTIONS)
                    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_TXT_EDIT_NOTIFICATIONS_SENDER_SMTP_SERVER, notification.smtpserver)
                    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_TXT_EDIT_NOTIFICATIONS_SENDER_SMTP_PORT, notification.smtpport)
                else:
                    selenium2lib.unselect_checkbox(FusionSettingsPage.ID_CHCKBOX_SMTP_OPTIONS)
                if notification.alertemail.lower() == "enabled":
                    if not ui_lib.wait_for_element_visible(FusionSettingsPage.ID_ENABLE_ALTER_EMAIL):
                        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ALERTS_ENABLED)
                for alertfilter in alertfilters:
                    add_email_alert_filter(alertfilter)
                ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK_EDIT_NOTIFICATIONS)
                if not ui_lib.wait_for_element_visible(FusionSettingsPage.ID_PAGE_LABEL):
                    return False
                else:
                    return True
            else:
                raise AssertionError("\n Unable to open Edit notifications page")
        else:
            raise AssertionError("\n Sender's email cannot be empty")


def add_email_alert_filter(alertfilter):
    """ add email alert and filter """

    selenium2lib = ui_lib.get_s2l()
    if selenium2lib._is_element_present(FusionSettingsPage.ID_LABEL_EDIT_NOTIFICATIONS):
        if len(alertfilter.filter.strip()) > 0:
            selenium2lib.click_element(FusionSettingsPage.ID_BTN_ADD_ALERT_EMAIL_FILTER)
            ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_ADD_EMAIL_FILTER)
            ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_ADD_ALERT_EMAIL_NAME, alertfilter.name)
            if alertfilter.filteremail.lower() == "enabled":
                if not ui_lib.is_visible(FusionSettingsPage.ID_BTN_EMAIL_FILTER):
                    selenium2lib.click_element(FusionSettingsPage.ID_BTN_EMAIL_FILTER_ENABLED)
            elif alertfilter.filteremail.lower() == "disabled":
                if ui_lib.is_visible(FusionSettingsPage.ID_BTN_EMAIL_FILTER):
                    selenium2lib.click_element(FusionSettingsPage.ID_BTN_EMAIL_FILTER_DISABLED)
            ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_TXT_FILTER, alertfilter.filter)
            emails = alertfilter.emailsaddresses.replace(' ', '\n').split(',')
            for email in emails:
                ui_lib.send_keys(FusionSettingsPage.ID_TXT_FILTER_EMAILADDRESSES, email)
            selenium2lib.click_element(FusionSettingsPage.ID_BTN_ADD_EMAIL_FILTER)
        else:
            raise AssertionError("Filter Email not specify")
    else:
        raise AssertionError("\nEdit Notifications Page not present or visible")

# ##########################################################################################
#                IP POOLS Functions     ########
# ##########################################################################################


def is_ip_in_subnet(ip_to_verify, range_list):
    '''
    Function to check if the IP specified is from the ip ranges passed as input
    Returns true if found else returns false and logs appropriate error message

    parameters :
        ip_to_verify   - IP to verify is the ranges specified in range list
        range_list     - List of ranges to check the IP in

    Input Example:
        <addressrange name = "test12" rangestart = "1.1.160.231" rangeend = "1.1.160.240"/>
    '''
    ipInt = 0
    minVal = 0
    maxVal = 0

    for addressrange in range_list:
        # convert the IP passed to integer form (base 10)
        ipInt = iptoint(ip_to_verify)
        # get the integer values of the start and end IP of the range
        minVal = iptoint(addressrange.rangestart)
        maxVal = iptoint(addressrange.rangeend)
        logger.info("Checking If the IP {} is from range [{},{}]".format(ip_to_verify, addressrange.rangestart, addressrange.rangeend))
        # if any of the ips specified is invalid exit
        if ipInt == 0 or maxVal == 0 or minVal == 0:
            logger.info("One or more of the IPs specified [{},{},{}] are invalid".format(ip_to_verify, addressrange.rangestart, addressrange.rangeend))
            return False
        # check if the ip specified is withn the range specified
        if minVal <= ipInt and ipInt <= maxVal and addressrange.enable.lower() == "true":
            logger.debug("\nThe IP - {} is from the Range pool - {} and within range ({},{})".format(ip_to_verify, addressrange.name, addressrange.rangestart, addressrange.rangeend))
            return True
        elif minVal <= ipInt and ipInt <= maxVal and addressrange.enable.lower() == "false":
            logger.info("The IP [{}] is allocated from range [{}] which is DISABLED!! ".format(ip_to_verify, addressrange.name))
            return False
    logger.info("IP {} not found in any of the ranges specified".format(ip_to_verify))
    return False


def iptoint(ip):
    '''
    Function to ge integer value of and ip passed
    ip = x1.x2.x3.x4
    intValueIP = (x1 * 256**3) + (x2 * 256**2) + (x3 * 256) + x4
    '''
    res = 0
    temp = map(int, ip.split('.'))
    if len(temp) < 4:
        logging._warn("Invalid IP address - {}".format(ip))
        return 0
    res = (16777216 * temp[0]) + (65536 * temp[1]) + (256 * temp[2]) + temp[3]
    return res


def navigate_to_addresses_and_identifiers_page():
    '''
    Function to navigate to address and identifiers page.

    Returns boolean True on success else Raises Exception of type AssertionError
    '''
    logger.info("-- Navigating to Address and Identifiers page")
    if not GeneralAddressesAndIdentifiers.wait_for_addresses_and_identifiers_page_visible(fail_if_false=False):
        navigate()
        sub_section = SubSectionType.Settings.ADDRESSES_AND_IDENTIFIERS
        FusionUIBase.navigate_to_section_by_link(link=sub_section[0], title=sub_section[1], sub_section=True)
        GeneralAddressesAndIdentifiers.wait_for_addresses_and_identifiers_page_visible(timeout=8, fail_if_false=True)
    return True


def _open_edit_addressesidentifiers_dialog_from_settings_page():
    '''
    Function to click on edit address and identifiers Gear , by hovering over address and identifiers link in settings page
    on open Edit addresses and identifiers Dialog
    Returns boolean True on success else Raises Exception of type AssertionError
    '''

    logger.info("-- Opening Edit Addresses And Identifiers Dialog by Clicking on Edit Link from Settings page")
    if not GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_dialog_visible(fail_if_false=False):
        navigate()
        GeneralAddressesAndIdentifiers.wait_for_addresses_and_identifiers_link_visible(fail_if_false=False)
        GeneralAddressesAndIdentifiers.click_addresses_and_identifiers_edit_link()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_dialog_visible(fail_if_false=True)
        GeneralAddressesAndIdentifiers.wait_for_edit_dialog_ipv4subnet_table_nodata_disappear(fail_if_false=False)
    return True


def _open_edit_addressesidentifiers_dialog_from_actions_menu():
    """
    Function to click edit from the actions dropdown in Address and Identifiers page and Open Edit Addresses and identifiers Dialog

    Returns boolean True on success else Raises Exception of type AssertionError
    """
    logger.info("-- Opening Edit Addresses and identifiers by clicking Edit from Actions Menu")
    if not GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_dialog_visible(fail_if_false=False):
        navigate()
        sub_section = SubSectionType.Settings.ADDRESSES_AND_IDENTIFIERS
        FusionUIBase.navigate_to_section_by_link(link=sub_section[0], title=sub_section[1], sub_section=True)
        GeneralAddressesAndIdentifiers.wait_for_addresses_and_identifiers_page_visible(fail_if_false=True)

        GeneralAddressesAndIdentifiers.click_addresses_and_identifiers_page_actions_menu(fail_if_false=False)
        GeneralAddressesAndIdentifiers.click_actions_edit()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_dialog_visible()
        GeneralAddressesAndIdentifiers.wait_for_edit_dialog_ipv4subnet_table_nodata_disappear(fail_if_false=False)
    return True


def validate_settings_page_addressesidentifiers_edit_link_for_user():
    '''
    Function to velidate if  edit address and identifiers icon is visible , by hovering over address and identifiers link in settings page

    Returns boolean True on success else Raises Exception of type AssertionError
    '''

    logger.info("-- Validating on Address And Identifiers Edit Link from Settings page")
    navigate()
    GeneralAddressesAndIdentifiers.wait_for_addresses_and_identifiers_link_visible(fail_if_false=False)
    try:
        GeneralAddressesAndIdentifiers.click_addresses_and_identifiers_edit_link()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_dialog_visible(timeout=8, fail_if_false=True)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        raise AssertionError("Edit Icon visible clicking which opens the Edit Addresses and Identifiers Dialog")
    except AssertionError as Ex:
        logger.debug(Ex.message)
        logger.debug("Edit Icon not clickable as expected")
    return True


def validate_addressesidentifiers_actions_menu_edit_option_for_user():
    """
    Function to validate edit option from the actions dropdown in Address and Identifiers page

    Returns boolean True on success else Raises Exception of type AssertionError
    """
    logger.info("-- Validating Edit option in Actions Menu of Address And Identifiers Page")
    navigate_to_addresses_and_identifiers_page()
    if GeneralAddressesAndIdentifiers.wait_for_addresses_and_identifiers_page_actions_menu(fail_if_false=False):
        GeneralAddressesAndIdentifiers.click_addresses_and_identifiers_page_actions_menu(fail_if_false=False)
        if GeneralAddressesAndIdentifiers.wait_for_actions_menu_option("Edit", timeout=8, fail_if_false=False):
            GeneralAddressesAndIdentifiers.click_actions_edit()
            GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_dialog_visible()
            GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
            raise AssertionError("Edit option seen in Actions dropdown clicking which opens the Edit Addresses and Identifiers Dialog")
        logger.debug("Edit option not visible in the Actions Dropdown as expected")
    else:
        logger.debug("Actions dropdown in Address and identifiers page not visible in UI")
    return True


def _add_ipv4_addressrange_to_subnet(addressrange_list):
    '''
    Function to add address ranges to create/edit subnet form

    Arguments :
        addressrange_list     - list of address ranges containing the follwonig attributes :
                                    - name*           - range name
                                    - rangestart*     - starting IP address of range
                                    - rangeend*       - end ip address of range

        * required attributes

    Input Example:
        <addressrange name = "test12" rangestart = "1.1.160.231" rangeend = "1.1.160.240"/>

    Return Value :
        Returns a boolean True on success ELSE Raises an  Exception of type AssertionError

    '''
    total_length = len(addressrange_list)
    error_msg_list = []
    for n, address_range in enumerate(addressrange_list):
        errors_on_form = []
        logger.info("--Adding address range : {}".format(address_range.name))
        if not CreateSubnetsAndAddressRange.wait_for_add_range_dialog_visible(fail_if_false=False):
            if CreateSubnetsAndAddressRange.wait_for_add_addressrange_button(fail_if_false=False):
                CreateSubnetsAndAddressRange.click_add_subnet_add_addressrange_button()
            elif EditSubnetsAndAddressRange.wait_for_update_subnet_add_range_button(fail_if_false=False):
                EditSubnetsAndAddressRange.click_update_subnet_add_range_button()
            else:
                raise AssertionError("Add address range button is not visible!!")
            if CreateSubnetsAndAddressRange.wait_for_add_range_warning_dialog(fail_if_false=False):
                warning_text = CreateSubnetsAndAddressRange.get_add_range_warning_text()
                logger.debug("Warning seen during range [{}] addition. - \n{}".format(address_range.name, warning_text))
                error_msg_list.append(warning_text)
                CreateSubnetsAndAddressRange.click_add_range_warning_dialog_close()
                continue
            CreateSubnetsAndAddressRange.wait_for_add_range_dialog_visible(timeout=8)
        CreateSubnetsAndAddressRange.input_rangename(address_range.name)
        CreateSubnetsAndAddressRange.input_range_startip(address_range.rangestart)
        CreateSubnetsAndAddressRange.input_range_endip(address_range.rangeend)

        if n < total_length - 1:
            CreateSubnetsAndAddressRange.click_range_add_plus_button()
        else:
            CreateSubnetsAndAddressRange.click_range_add_button()

        errors_on_form = CreateSubnetsAndAddressRange.get_all_errors_on_addrange_dialog()
        if errors_on_form:
            error_msg_list += errors_on_form
            CreateSubnetsAndAddressRange.click_range_cancel_button()
            CreateSubnetsAndAddressRange.wait_for_add_range_dialog_disappear(timeout=10)
            continue
        else:
            logger.info("No Errors seen in Add Address Range Form")

    CreateSubnetsAndAddressRange.wait_for_add_range_dialog_disappear(timeout=10)
    if error_msg_list:
        raise AssertionError(error_msg_list)
    logger.debug("Return Value - True")
    return True


def create_ipv4_subnet_and_addressrange(subnet_obj):
    '''
    Arguments:
        subnet_obj      -- list of subnet objects with following attributes --
                            <ipv4subnet>
                                subnetid*                        --   subnet id for the subnet as x.x.x.x
                                subnetmask*                      --   subnet mask for the subnet as x.x.x.x
                                gateway(optional for Hellfire)   --   gateway for the suvnet as x.x.x.x
                                domain(optional for Hellfire)    --   domain name of the subnet
                                dns1(optional)                   --   1st dns IP
                                dns2(optional)                   --   2nd dns IP
                                dns3(optional)                   --   3rd dns IP
                                <addressrange>(optional)         --    Ranges to add to the subnet
                                    name*                        --   Address range name
                                    rangestart*                  --   range start IP
                                    rangeend*                    --   range end IP

        *Required attributes

    Return Value :
        Returns True on success else Raises an  Exception of type AssertionError

    INPUT Example :

    <ipv4subnet subnetid = "1.1.1.0" subnetmask="255.55.255.0" gateway = "1.1.1.1" domain="hpe.com" dns1="1.1.1.2" dns2="1.1.1.3" dns3 = 1.1.1.4" >
        <addressrange rangename = "Test1" rangestart="1.1.1.10" rangeend="1.1.1.20" />
        <addressrange rangename = "Test2" rangestart="1.1.1.10" rangeend="1.1.1.20" />
        <addressrange rangename = "Test3" rangestart="1.1.1.10" rangeend="1.1.1.20" />
    </ipv4subnet>

    <ipv4subnet subnetid = "1.1.1.0" subnetmask="255.55.255.0" gateway = "1.1.1.1" domain="hpe.com" dns3 = 1.1.1.4">
    </ipv4subnet>

    <ipv4subnet subnetid = "1.1.1.0" subnetmask="255.55.255.0" gateway = "" domain="" dns3 = "" hellfire="yes">  Only for Hellfire Data
    </ipv4subnet>

    '''
    total_length = len(subnet_obj)
    errors_on_form = []
    error_msg_list = []
    logger.info("---- Creating IPV4 Subnet and Address Ranges ----")
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    for n, subnet in enumerate(subnet_obj):
        addressrange_list = []
        errors_on_form = []
        logger.info("--Creating Subnet ID : {}".format(subnet.subnetid))
        if VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnet.subnetid, fail_if_false=False):
            logger.warn("Subnet [{}] already present.Creation may lead to error".format(subnet.subnetid))
            error_msg_list.append("Subnet [{}] already present.Creation may lead to error".format(subnet.subnetid))
        if not CreateSubnetsAndAddressRange.wait_for_add_subnet_addressrange_dialog_visible(fail_if_false=False):
            if not CreateSubnetsAndAddressRange.wait_for_add_ipv4_subnet_and_range_button(fail_if_false=False):
                GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
                GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
                raise AssertionError("'Add ipv4 Subnet and Address Range' button not visible!!")
            CreateSubnetsAndAddressRange.click_add_ipv4_subnet_and_range_button()
            CreateSubnetsAndAddressRange.wait_for_add_subnet_addressrange_dialog_visible(timeout=10)

        CreateSubnetsAndAddressRange.input_subnetid(subnet.subnetid)
        CreateSubnetsAndAddressRange.input_subnetmask(subnet.subnetmask)
        CreateSubnetsAndAddressRange.input_gateway(subnet.gateway)
        CreateSubnetsAndAddressRange.input_domain(subnet.domain)
        if subnet.has_property('dns1'):
            CreateSubnetsAndAddressRange.input_dns1(subnet.dns1)
        if subnet.has_property('dns2'):
            CreateSubnetsAndAddressRange.input_dns2(subnet.dns2)
        if subnet.has_property('dns3'):
            CreateSubnetsAndAddressRange.input_dns3(subnet.dns3)

        addressrange_list = getattr(subnet, "addressrange", [])
        if addressrange_list:
            try:
                _add_ipv4_addressrange_to_subnet(addressrange_list)
                # basic check - check if ranges are visible in table
                for add_range in addressrange_list:
                    if not VerifySubnetsAndAddressRange.verify_range_exists_in_add_subnet_table(add_range.name, fail_if_false=False):
                        logger.warn("Range [{}] is not visible in subnet table.Not created.".format(add_range.name))
                        error_msg_list.append("Range [{}] is not visible in subnet table.Not created.".format(add_range.name))
                    else:
                        logger.debug("Range [{}] is visible in subnet table".format(add_range.name))
            except AssertionError as Ex:
                logger.warn("Following Exception during Range addition - \n{}".format(Ex.message))
                error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

        if n < total_length - 1:
            CreateSubnetsAndAddressRange.click_subnet_add_plus_button()
        else:
            CreateSubnetsAndAddressRange.click_subnet_add_button()

        # check for errors on form - if any capture and continue with next subnet creation
        errors_on_form = CreateSubnetsAndAddressRange.get_all_errors_on_addsubnet_dialog()
        if errors_on_form:
            error_msg_list += errors_on_form
            CreateSubnetsAndAddressRange.click_add_subnet_cancel_button()
            CreateSubnetsAndAddressRange.wait_for_add_subnet_addressrange_dialog_disappear(timeout=10)
            continue
        else:
            logger.info("No Errors Seen in Subnet Creation form")

    CreateSubnetsAndAddressRange.wait_for_add_subnet_addressrange_dialog_disappear(timeout=10)
    # basic check - check if the Subnets are visible in table
    for subnet in subnet_obj:
        if not VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnet.subnetid, fail_if_false=False):
            logger.warn("Subnet [{}] not visible in subnet table.Not created.".format(subnet.subnetid))
            error_msg_list.append("Subnet [{}] not visible in subnet table.Not created.".format(subnet.subnetid))
        else:
            logger.debug("Subnet [{}] is visible in subnet table.".format(subnet.subnetid))

            if getattr(subnet, "addressrange", []):
                try:
                    VerifySubnetsAndAddressRange.verify_range_unavailable_for_operation_on_addition(subnet.subnetid, getattr(subnet, "addressrange", []))
                except AssertionError as Ex:
                    logger.warn("Exception seen  : \n{}".format(Ex.message))
                    error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Error Seen During Subnet Creation - \n{}".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)
    if error_msg_list:
        raise AssertionError(error_msg_list)
    logger.debug("return Value -True")
    return True


def _edit_ipv4_addressrange_in_edit_subnet(addressrange_list):
    '''
    Function to Edit the ipv4 address ranges of a subnet

    Arguments:
        address_range_obj    - list of address range objects / single address range object

        <addressrange>
            name*                       --  current range name
            newname(optional)           --  New range name
            rangestart(optional)        --  new range start IP
            rangeend(optional)          --  new range end IP
            enable(optional)            --  Enable/disable range
         * required attributes

    Input Example :
        <addressrange name = "test10" newname = "testNew" rangestart = "1.1.160.200" rangeend = "1.1.160.210"/>

    Return Value :
        Returns a boolean True on successfull edit of all address ranges ELSE raises an AssertionError Exception with appropriate error message

    '''

    error_msg_list = []
    name_to_verify = None
    for addressrange in addressrange_list:
        logger.info("-- Editing Address range [{}]".format(addressrange.name))
        errors_on_form = []
        if VerifySubnetsAndAddressRange.verify_range_exists_in_edit_subnet_table(addressrange.name, fail_if_false=False) is False:
            logger.warn("address range [{}] is not present in the address ranges table".format(addressrange.name))
            error_msg_list.append("address range [{}] is not present in the address ranges table".format(addressrange.name))
            continue

        if EditSubnetsAndAddressRange.wait_for_update_subnet_edit_range_icon(addressrange.name, fail_if_false=False) is False:
            raise AssertionError("Edit range Gear not visible for range [{}]!!".addressrange.name)
        EditSubnetsAndAddressRange.click_update_subnet_edit_range_icon(addressrange.name)
        EditSubnetsAndAddressRange.wait_for_update_range_dialog()

        if addressrange.has_property("newname"):
            name_to_verify = addressrange.newname
            EditSubnetsAndAddressRange.update_range_name(addressrange.newname)
        else:
            name_to_verify = addressrange.name

        if addressrange.has_property("rangestart"):
            if EditSubnetsAndAddressRange.wait_for_input_range_startip(fail_if_false=False):
                EditSubnetsAndAddressRange.update_range_startip(addressrange.rangestart)
            else:
                logger.warn("Start IP field is not Editable for range {}".format(addressrange.name))
                error_msg_list.append("Start IP field is not Editable for range {}".format(addressrange.name))

        if addressrange.has_property("rangeend"):
            EditSubnetsAndAddressRange.update_range_endip(addressrange.rangeend)

        EditSubnetsAndAddressRange.click_update_range_ok_button()

        errors_on_form = EditSubnetsAndAddressRange.get_all_errors_on_editrange_dialog()
        if errors_on_form:
            error_msg_list += errors_on_form
            EditSubnetsAndAddressRange.click_update_range_cancel_button()
            EditSubnetsAndAddressRange.wait_for_update_range_dialog_disappear()
            continue
        else:
            logger.info("No Errors seen in Edit Address Range Form")

        EditSubnetsAndAddressRange.wait_for_update_range_dialog_disappear()

        # basic verification-check that the new range is seen in table
        if VerifySubnetsAndAddressRange.verify_range_exists_in_edit_subnet_table(name_to_verify, fail_if_false=False):
            logger.debug("New Range [{}] is visible in table".format(name_to_verify))
        else:
            logger.warn("Address range [{}] is not visible in range table".format(name_to_verify))
            error_msg_list.append("Address range [{}] is not visible in range table".format(name_to_verify))

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def _delete_ipv4_addressrange_from_edit_subnet(address_range_obj):
    '''
    Function to delete the ipv4 address ranges of a subnet

    Arguments:
        address_range_obj    - list of address range objects / single address range object

        <addressrange>
            names*                      --  multiple range names as a comma(,) seperated string

        * required attributes

    Input Example :
        <addressrange names = "test10,test11,test12" />

    Return Value :
        Returns a boolean True on successfull deletion of all address ranges ELSE raises an AssertionError Exception with appropriate error message
    '''
    error_msg_list = []
    delete_count = 0
    addressrange_list = []
    for address_range in address_range_obj:
        addressrange_list += address_range.names.split(",")

    total_length = len(addressrange_list)

    for addressrange in addressrange_list:
        logger.info("-- Deleting Address range [{}]".format(addressrange))
        if VerifySubnetsAndAddressRange.verify_range_exists_in_edit_subnet_table(addressrange, fail_if_false=False) is False:
            logger.warn("address range [{}] is not present in the address ranges table".format(addressrange))
            error_msg_list.append("address range [{}] is not present in the address ranges table".format(addressrange))
            continue

        if DeleteSubnetsAndAddressRange.wait_for_update_subnet_delete_range_button(addressrange, fail_if_false=False) is False:
            raise AssertionError("Delete range button not visible!!")

        DeleteSubnetsAndAddressRange.click_update_subnet_delete_range_button(addressrange)

        if DeleteSubnetsAndAddressRange.wait_for_range_delete_warning_dialog(fail_if_false=False):
            delete_warning = DeleteSubnetsAndAddressRange.get_range_delete_warning_dialog_message()
            logger.warn("Warning seen on trying to delete range [{}] - \n {}".format(addressrange, delete_warning))
            error_msg_list.append(delete_warning)
            DeleteSubnetsAndAddressRange.click_delete_warning_dialog_close()
            DeleteSubnetsAndAddressRange.wait_for_range_delete_warning_dialog_disappear()
            continue
        if not VerifySubnetsAndAddressRange.verify_range_exists_in_edit_subnet_table(addressrange, fail_if_false=False):
            logger.debug("address range [{}] deleted successfully".format(addressrange))
            delete_count += 1
        else:
            logger.warn("address range [{}] is still visible in table".format(addressrange))
            error_msg_list.append("address range [{}] is still visible in table".format(addressrange))
    if delete_count != total_length:
        logger.warn("Not all address ranges deleted successfully")
        error_msg_list.append("Not all address ranges deleted successfully")

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def edit_ipv4_subnet_and_addressrange(subnet_obj):
    '''
    Function to Edit a subnet and address range

    Arguments:
        subnet_obj  -- list of subnet objects with the following attributes --
                        <ipv4subnet>
                            subnetid*                            -- subnet IF of the subnet
                            newsubnetid(optional)                -- new subnet ID of the subnet
                            subnetmask(optional)                 -- new subnet mask of the subnet
                            gateway(optional)                    -- new gateway of the subnet
                            domain(optional)                     -- new domain name of the subnet
                            dns1(optional)                       -- new dns1 IP
                            dns2(optional)                       -- new dns2 IP
                            dns3(optional)                       -- new dns3 IP
                            <remove_addressrange> (optional)     -- address ranges to delete from the subnet
                                names*                           -- multiple/single range name/names as a comma(,) seperated string
                            <add_addressrange>( optional)        -- address ranges to add
                                name*                            -- range name
                                rangestart*                      -- range start IP
                                rangeend*                        -- range end IP
                            <edit_addressrange> (optional)       -- address ranges to edit
                                name*                            -- current range name
                                newrangename(optional)           -- new range name
                                rangestart(optional)             -- new range start IP
                                rangeend(optional)               -- new range end IP
                                enable(optional)                 --Enable/Disable range (True/False)

        *Required attributes

    Return Value :
        Returns a Boolean True on success ELSE Raises an  Exception of type AssertionError

    INPUT Example :

        <ipv4subnet subnetid = "1.1.1.0" newsubnetid = "" subnetmask="255.255.255.0" gateway = "1.1.1.1" domain="hpe.com" >
                <remove_addressrange names = "Test2" />
                <add_addressrange name = "Test3" rangestart="1.1.1.100" rangeend="1.1.1.110"  />
                <edit_addressrange name = "Test1" rangestart="1.1.1.25" rangeend="1.1.1.30" enable="False"/>
        </ipv4subnet>

        <ipv4subnet subnetid = "1.1.1.0" newsubnetid = "" subnetmask="255.255.255.0" gateway = "1.1.1.1" domain="hpe.com" >
                <remove_addressrange names = "Test2,Test3,Test4" />
                <edit_addressrange name = "Test1" rangestart="1.1.1.25" rangeend="1.1.1.30" />
        </ipv4subnet>

    '''
    error_msg_list = []
    logger.info("-- Editing IPV4 Subnet and Address Ranges --")
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()
    if not VerifySubnetsAndAddressRange.verify_edit_addressesidentifiers_ipv4_subnet_table_is_not_empty(fail_if_false=False):
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)
        raise AssertionError("No subnets have been defined")

    for _, subnet in enumerate(subnet_obj):
        errors_on_form = []
        if VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnet.subnetid, fail_if_false=False) is False:
            logger.warn("Subnet [{}] does not exist".format(subnet.subnetid))
            error_msg_list.append("Subnet [{}] does not exist".format(subnet.subnetid))
            continue

        if not VerifySubnetsAndAddressRange.verify_edit_subnet_form_visible_for_subnetid(subnet.subnetid, fail_if_false=False):
            EditSubnetsAndAddressRange.click_edit_subnet_icon(subnet.subnetid)
            EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_visible(fail_if_false=True)

        logger.info("-- Editing Subnet : {}".format(subnet.subnetid))
        subnetid_to_verify = subnet.subnetid

        if VerifySubnetsAndAddressRange.verify_update_subnet_and_addressrange_table_is_not_empty(fail_if_false=False):
            if VerifySubnetsAndAddressRange.verify_subnetid_is_not_editable(fail_if_false=False) is False:
                logger.warn("Subnet ID is editable, though address ranges are present")
                error_msg_list.append("Subnet ID is editable, though address ranges are present")
            else:
                logger.debug("Subnet ID field is not editable as expected")
            if VerifySubnetsAndAddressRange.verify_subnet_mask_is_not_editable(fail_if_false=False) is False:
                logger.warn("Subnet Mask is editable, though address ranges are present")
                error_msg_list.append("Subnet Mask is editable, though address ranges are present")
            else:
                logger.debug("Subnet Mask field is not editable as expected")
        else:
            if subnet.has_property("newsubnetid"):
                subnetid_to_verify = subnet.newsubnetid
                EditSubnetsAndAddressRange.update_subnetid(subnet.newsubnetid)
            if subnet.has_property("subnetmask"):
                EditSubnetsAndAddressRange.update_subnetmask(subnet.subnetmask)

        if subnet.has_property("gateway"):
            EditSubnetsAndAddressRange.update_gateway(subnet.gateway)
        if subnet.has_property("domain"):
            EditSubnetsAndAddressRange.update_domain(subnet.domain)
        if subnet.has_property("dns1"):
            EditSubnetsAndAddressRange.update_dns1(subnet.dns1)
        if subnet.has_property("dns2"):
            EditSubnetsAndAddressRange.update_dns2(subnet.dns2)
        if subnet.has_property("dns3"):
            EditSubnetsAndAddressRange.update_dns3(subnet.dns3)

        remove_addressrange_list = getattr(subnet, "remove_addressrange", [])
        add_addressrange_list = getattr(subnet, "add_addressrange", [])
        edit_addressrange_list = getattr(subnet, "edit_addressrange", [])

        if remove_addressrange_list:
            try:
                logger.debug("Deleting Address ranges from subnet [{}]".format(subnetid_to_verify))
                _delete_ipv4_addressrange_from_edit_subnet(remove_addressrange_list)
            except AssertionError as Ex:
                logger.warn("Following Exception seen during Range deletion of subnet [{}] : \n {} \n".format(subnetid_to_verify, Ex.message))
                error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]
        if add_addressrange_list:
            try:
                logger.debug("Adding Address ranges to subnet [{}]".format(subnetid_to_verify))
                _add_ipv4_addressrange_to_subnet(add_addressrange_list)
                # basic check - check if ranges are visible in table
                for add_range in add_addressrange_list:
                    if not VerifySubnetsAndAddressRange.verify_range_exists_in_edit_subnet_table(add_range.name, fail_if_false=False):
                        logger.warn("Range [{}] is not visible in subnet table.Not created.".format(add_range.name))
                        error_msg_list.append("Range [{}] is not visible in subnet table.Not created.".format(add_range.name))
                    else:
                        logger.debug("Range [{}] is visible in subnet table".format(add_range.name))
            except AssertionError as Ex:
                logger.warn("Following Exception seen during Range addition to subnet [{}] : \n {} \n".format(subnetid_to_verify, Ex.message))
                error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]
        if edit_addressrange_list:
            try:
                logger.debug("Editing Address ranges of subnet [{}]".format(subnetid_to_verify))
                _edit_ipv4_addressrange_in_edit_subnet(edit_addressrange_list)
            except AssertionError as Ex:
                logger.warn("Following Exception seen during Range edit if subnet [{}] : \n {} \n".format(subnetid_to_verify, Ex.message))
                error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

        EditSubnetsAndAddressRange.click_subnet_update_button()

        errors_on_form = EditSubnetsAndAddressRange.get_all_errors_on_editsubnet_dialog()
        if errors_on_form:
            error_msg_list += errors_on_form
            EditSubnetsAndAddressRange.click_update_subnet_cancel_button()
        else:
            logger.info("No Errors Seen in Edit subnet form")

        EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_disappear()

        if not VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnetid_to_verify, fail_if_false=False):
            logger.warn("Subnet [{}] not visible in subnet table after update".format(subnetid_to_verify))
            error_msg_list.append("Subnet [{}] not visible in subnet table after update".format(subnetid_to_verify))
        else:
            logger.debug("Subnet [{}] is visible in subnet table after update".format(subnetid_to_verify))
            try:
                if edit_addressrange_list:
                    VerifySubnetsAndAddressRange.verify_range_unavailable_for_operation_on_addition(subnetid_to_verify, add_addressrange_list)
                    GeneralAddressesAndIdentifiers.enable_disable_addressrange(subnetid_to_verify, edit_addressrange_list)
            except AssertionError as Ex:
                logger.warn("Exception : \n {} ".format(Ex.message))
                error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Errors Seen During Subnet Edit - \n {}".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)
    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def delete_ipv4_subnet_and_addressrange(subnet_obj):
    '''
    Arguments:
    <ipv4subnet>
        subnetid*       -- subnet ID of the subnet.Acts as the identifier of the subnet
                -- Rest of the attributes are optional

    * required attributes

    Return Value :
        Returns True on success else Raises an  Exception of type AssertionError

    EXAMPLE :

        <ipv4subnet subnetid = "23.23.23.0" subnetmask="255.255.255.0" gateway = "23.23.23.1" domain="hpe.com" />

    '''
    logger.info("---- Deleting Subnet And Address Ranges ----")
    error_msg_list = []
    delete_count = 0
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    total_length = len(subnet_obj)

    if VerifySubnetsAndAddressRange.verify_edit_addressesidentifiers_ipv4_subnet_table_is_not_empty(timeout=10, fail_if_false=False) is False:
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
        raise AssertionError("No subnets have been defined")

    for subnet in subnet_obj:
        logger.info("---- Deleting Subnet {} ----".format(subnet.subnetid))
        if VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnet.subnetid, fail_if_false=False) is False:
            logger.warn("Subnet [{}] does not exist".format(subnet.subnetid))
            continue

        if not DeleteSubnetsAndAddressRange.wait_for_delete_subnet_button(subnet.subnetid, fail_if_false=False):
            GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
            GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
            raise AssertionError("Delete subnet button not visible!!")

        DeleteSubnetsAndAddressRange.click_delete_subnet_button(subnet.subnetid)
        if DeleteSubnetsAndAddressRange.wait_for_subnet_delete_warning_dialog(fail_if_false=False):
            warning_msg = DeleteSubnetsAndAddressRange.get_subnet_delete_warning_dialog_message()
            logger.warn("Warning Seen on trying to delete subnet [{}] - \n{}".format(subnet.subnetid, warning_msg))
            error_msg_list.append(warning_msg)
            DeleteSubnetsAndAddressRange.click_delete_warning_dialog_close()
            DeleteSubnetsAndAddressRange.wait_for_subnet_delete_warning_dialog_disappear(timeout=8)
            continue

        if VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnet.subnetid, fail_if_false=False):
            logger.warn("Subnet [{}] is not deleted and is still visible in table".format(subnet.subnetid))
        else:
            logger.debug("Subnet [{}] is not visible in table".format(subnet.subnetid))
            delete_count += 1

    if delete_count < total_length:
        logger.warn("Not all Subnets deleted successfully")
        error_msg_list.append("Not all Subnets deleted successfully")
    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Error Seen During Subnet Delete - \n [{}]".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)

    navigate_to_addresses_and_identifiers_page()
    logger.info("-- Verifying Subnet Delete in Edit Addresses and Identifiers Page --")
    if VerifySubnetsAndRangeAddressIdentifiersPage.verify_ipv4_subnet_addressrange_table_is_not_empty(timeout=8, fail_if_false=False) is False:
        logger.debug("No Data available in the table.All subnets deleted")
        return True

    for subnet in subnet_obj:
        if VerifySubnetsAndAddressRange.verify_subnet_exists_in_addressidentifierspage_table(subnet.subnetid, fail_if_false=False):
            logger.warn("Subnet [{}] is still visible!".format(subnet.subnetid))
            error_msg_list.append("Subnet [{}] is still visible!".format(subnet.subnetid))
        else:
            logger.debug("Subnet [{}] deleted successfully".format(subnet.subnetid))

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def enable_disable_addressrange_of_ipv4subnet(subnetid, addressrange_list):
    '''
    Keyword to enable/disable address ranges of a given subnet

    Arguments:
        subnetid            --
        addressrange_list   --
                <addressrange>(optional) --    Ranges to add to the subnet
                                    name*                         --   Address range name
                                    rangestart(optional)          --   range start IP
                                    rangeend(optional)            --   range end IP
                                    enable*                       --   Enable/Disable range (True/False)

    Return Value:
        Boolean True on success else Raises AssertionType exception

    INPUT Example :
        <addressrange rangename = "Test1" rangestart="1.1.1.10" rangeend="1.1.1.20" enable="True" />


    '''
    error_msg_list = []
    logger.info("-- Enable/Disable Address ranges of subnet [{}].".format(subnetid))
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    try:
        GeneralAddressesAndIdentifiers.enable_disable_addressrange(subnetid, addressrange_list)
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Error Seen During Enable/Disable of Range  - \n{}".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def add_ipv4_addressrange_to_edit_subnet(subnetid, addressrange_list):
    '''
    Function to add address ranges to create subnet form

    Arguments :
        subnetid                --  subnet ID of the subnet
        addressrange_list      -- list of address ranges to add containing the follwonig attributes :
                                    - name*           - range name
                                    - rangestart*     - starting IP address of range
                                    - rangeend*       - end ip address of range


    Input Example:
            <addressrange name = "test10" rangestart = "1.1.160.200" rangeend = "1.1.160.210"/>
            <addressrange name = "test11" rangestart = "1.1.160.220" rangeend = "1.1.160.230"/>

        * required attributes

    Return Value :
        Returns a boolean True on success ELSE Raises an  Exception of type AssertionError

    '''
    logger.info("-- Adding Address Ranges to Subnet [{}]".format(subnetid))
    error_msg_list = []
    errors_on_form = []
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()
    if not VerifySubnetsAndAddressRange.verify_edit_subnet_form_visible_for_subnetid(subnetid, fail_if_false=False):
        EditSubnetsAndAddressRange.click_edit_subnet_icon(subnetid)
        EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_visible(timeout=8, fail_if_false=True)

    try:
        _add_ipv4_addressrange_to_subnet(addressrange_list)

    except AssertionError as Ex:
        logger.warn("Exception during range addition : \n {}".format(Ex.message))
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

    for add_range in addressrange_list:
        if not VerifySubnetsAndAddressRange.verify_range_exists_in_edit_subnet_table(add_range.name, fail_if_false=False):
            logger.warn("Range [{}] is not visible in subnet table.Not created.".format(add_range.name))
            error_msg_list.append("Range [{}] is not visible in subnet table.Not created.".format(add_range.name))
        else:
            logger.debug("Range [{}] is visible in subnet table".format(add_range.name))

    EditSubnetsAndAddressRange.click_subnet_update_button()
    errors_on_form = EditSubnetsAndAddressRange.get_all_errors_on_editsubnet_dialog()
    if errors_on_form:
        error_msg_list += errors_on_form
        EditSubnetsAndAddressRange.click_update_subnet_cancel_button()
    else:
        logger.info("No Errors Seen in Edit subnet form")

    EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_disappear(timeout=8)

    try:
        VerifySubnetsAndAddressRange.verify_range_unavailable_for_operation_on_addition(subnetid, addressrange_list)
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]
    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Error Seen During Subnet Creation - \n [{}]".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def edit_ipv4_addressrange_in_subnet(subnetid, addressrange_list):
    '''
    Function to edit the address ranges of a subnet

    Arguments:
        subnetid*           --  subnet ID of the subnet.Acts as the subnet identifier
        addressrange_list  --  list of address ranges to edit
                                    <addressrange>
                                        name*                                     -- current address range name
                                        newname(optional)                         -- new range name
                                        rangestart(optional)                      -- new range start IP
                                        rangeend(optional)                        -- new range end IP
                                        enable(optional)                          -- Enable/Disable range (True/False)
        * required attributes

    Return Value :
        Returns True on success else Raises an  Exception of type AssertionError

    '''
    logger.info("-- Editing Address Ranges of Subnet [{}]".format(subnetid))
    error_msg_list = []
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()
    if not VerifySubnetsAndAddressRange.verify_edit_subnet_form_visible_for_subnetid(subnetid, fail_if_false=False):
        EditSubnetsAndAddressRange.click_edit_subnet_icon(subnetid)
        EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_visible(timeout=8, fail_if_false=True)

    try:
        _edit_ipv4_addressrange_in_edit_subnet(addressrange_list)
        EditSubnetsAndAddressRange.click_subnet_update_button()

    except AssertionError as Ex:
        logger.warn("Exception during range Edit : \n {}".format(Ex.message))
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]
        if EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_visible(fail_if_false=False):
            EditSubnetsAndAddressRange.click_update_subnet_cancel_button()

    EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_disappear(timeout=8)
    try:
        GeneralAddressesAndIdentifiers.enable_disable_addressrange(subnetid, addressrange_list)
    except AssertionError as Ex:
        logger.warn("Errors During Enabling/Disabling ranges- \n{}".format(Ex.message))
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]
    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Error Seen During Subnet Creation - \n [{}]".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def delete_ipv4_addressrange_from_subnet(subnetid, addressrange_list):
    '''
    Function to delete address ranges from a subnet

    Arguments:
        subnetid*                             -- subnet ID of the subnet.Acts as the subnet identifier
        addressrange_list                     -- list of address ranges to delete
            <addressrange>
                names*                           -- multiple range names as a comma(,) seperated string

        * required attributes

    Input Example :
        <addressrange names = "test10new,test11new" />
        <addressrange names = "test12new" />

    Return Value :
        Returns a boolean True on success ELSE Raises an  Exception of type AssertionError
    '''
    logger.info("-- Deleting Address Ranges from Subnet [{}]".format(subnetid))
    error_msg_list = []
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    if not VerifySubnetsAndAddressRange.verify_edit_subnet_form_visible_for_subnetid(subnetid, fail_if_false=False):
        EditSubnetsAndAddressRange.click_edit_subnet_icon(subnetid)
        EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_visible(timeout=8, fail_if_false=True)

    try:
        _delete_ipv4_addressrange_from_edit_subnet(addressrange_list)
    except AssertionError as Ex:
        logger.warn("Exception during range deletion:\n{}".format(Ex.message))
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

    EditSubnetsAndAddressRange.click_subnet_update_button()
    EditSubnetsAndAddressRange.wait_for_update_subnet_dialog_disappear(timeout=10)
    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Error Seen During Subnet Update - \n [{}]".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)

    logger.info("-- Verifying Address Range Delete in Addresses and Identifiers Page --")
    navigate_to_addresses_and_identifiers_page()
    try:
        GeneralAddressesAndIdentifiers.expand_addressrange_collapser_addressesidentifiers_page(subnetid)
        GeneralAddressesAndIdentifiers.wait_for_ipv4subnet_table_addressesidentifiers_page(subnetid)
        VerifySubnetsAndRangeAddressIdentifiersPage.verify_range_delete_in_table(subnetid, addressrange_list)
        GeneralAddressesAndIdentifiers.collapse_addressrange_collapser_addressesidentifiers_page(subnetid)
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def verify_ipv4_subnet_and_addressrange_in_edit_dialog(subnet_obj):
    '''
    Function to verify the Subnet and address range attributes in Edit Address and Identifiers Dialog

    Arguments:
        subnet_obj    -- List of subnet objects

    Return Value :
        returns a Boolean True on success else raises an AssertionError exception

    Input Example:
        <ipv4subnet subnetid = "4.4.4.0" subnetmask="255.255.255.0" gateway = "4.4.4.1" domain="hpe.com" dns1="2.2.2.2" dns2="4.4.4.3" dns3 = "1.4.4.4">
        </ipv4subnet>

        <ipv4subnet subnetid = "1.1.160.0" subnetmask="255.255.255.0" gateway = "1.1.160.1" domain="hp.com"  dns1="1.1.160.5" dns2="1.1.160.3" dns3 = "1.1.161.120">
            <addressrange name = "test1" rangestart="1.1.160.30" rangeend="1.1.160.40" enable="False" />
            <addressrange name = "test2" rangestart="1.1.160.25" rangeend="1.1.160.29" enable="True" />

        </ipv4subnet>
    '''
    logger.info("---- Verifying IPV4 Subnet and Address Ranges in Edit Address and Identifiers Form ----")
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    if not VerifySubnetsAndAddressRange.verify_edit_addressesidentifiers_ipv4_subnet_table_is_not_empty(timeout=8, fail_if_false=False):
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
        raise AssertionError("No subnets have been defined")

    try:
        VerifySubnetsAndRangeEditDialog.verify_ipv4_subnet_and_range_attributes(subnet_obj)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)
    except AssertionError as Ex:
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
        raise AssertionError(Ex.message)

    logger.debug("Return Value - True")
    return True


def verify_ipv4_subnet_and_addressrange_in_addressesidentifiers_page(subnet_obj):
    '''
    Function to verify the Subnet and address range attributes in Address And Identifiers Page

    Arguments:
        subnet_obj    -- List of subnet objects

    Return Value :
        returns a Boolean True on success else raises an AssertionError exception

    Input Example:
        <ipv4subnet subnetid = "4.4.4.0" subnetmask="255.255.255.0" gateway = "4.4.4.1" domain="hpe.com" dns1="2.2.2.2" dns2="4.4.4.3" dns3 = "1.4.4.4">
        </ipv4subnet>

        <ipv4subnet subnetid = "1.1.160.0" subnetmask="255.255.255.0" gateway = "1.1.160.1" domain="hp.com"  dns1="1.1.160.5" dns2="1.1.160.3" dns3 = "1.1.161.120">
            <addressrange name = "test1" rangestart="1.1.160.30" rangeend="1.1.160.40" enable="False" />
            <addressrange name = "test2" rangestart="1.1.160.25" rangeend="1.1.160.29" enable="True" />

        </ipv4subnet>
    '''
    logger.info("---- Verifying IPV4 Subnet and Address Ranges in Address and Identifiers Page ----")
    error_msg_list = []
    navigate_to_addresses_and_identifiers_page()

    if not VerifySubnetsAndAddressRange.verify_ipv4_subnet_addressrange_label_visible(fail_if_false=False):
        logger.warn("Label 'IPv4 Subnets and Address Ranges' not seen")
        error_msg_list.append("Label 'IPv4 Subnets and Address Ranges' not seen")
    else:
        logger.debug("Label 'IPv4 Subnets and Address Ranges' seen in addresses and identifiers page")

    if not VerifySubnetsAndRangeAddressIdentifiersPage.verify_ipv4_subnet_addressrange_table_is_not_empty(timeout=8, fail_if_false=False):
        raise AssertionError("No subnets have been defined")

    try:
        VerifySubnetsAndRangeAddressIdentifiersPage.verify_ipv4_subnet_and_range_attributes(subnet_obj)
    except AssertionError as Ex:
        error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

    if error_msg_list:
        raise AssertionError(error_msg_list)
    logger.debug("return Value - True")
    return True


def verify_ipv4_addressranges_of_subnet_in_edit_dialog(subnetid, addressrange_list):
    '''
    Function to verify the Address Range attributes of a subnet

    Arguments:
        subnetid          --  Subnet ID the address ranges are part of
        addressrange_list --  List of Address Range objects

    Return Value :
        returns a Boolean True on success else raises an AssertionError exception

    Input Example:
        <addressrange name = "test10" rangestart = "1.1.160.200" rangeend = "1.1.160.210" enable="True" />
        <addressrange name = "test11" rangestart = "1.1.160.220" rangeend = "1.1.160.230" enable="False" />

    '''
    logger.info("---- Verifying IPV4 Address Ranges of Subnet [{}] from Edit Address And Identifiers Form ----".format(subnetid))
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    GeneralAddressesAndIdentifiers.expand_addressrange_collapser_edit_dialog(subnetid)
    GeneralAddressesAndIdentifiers.wait_for_ipv4subnet_addressrange_table_edit_dialog(subnetid)
    try:
        VerifySubnetsAndRangeEditDialog.verify_ipv4_address_range_attributes(subnetid, addressrange_list)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)
    except AssertionError as Ex1:
        logger.warn(Ex1.message)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
        raise AssertionError(Ex1.message)

    logger.debug("Return Value - True")
    return True


def verify_ipv4_addressranges_of_subnet_in_addressesidentifiers_page(subnetid, addressrange_list):
    '''
    Function to verify the Address Range attributes of a subnet in addresses identifiers page

    Arguments:
        subnetid          --  Subnet ID the address ranges are part of
        addressrange_list --  List of Address Range objects

    Return Value :
        returns a Boolean True on success else raises an AssertionError exception

    Input Example:
        <addressrange name = "test10" rangestart = "1.1.160.200" rangeend = "1.1.160.210" enable="True" />
        <addressrange name = "test11" rangestart = "1.1.160.220" rangeend = "1.1.160.230" enable="False" />

    '''
    logger.info("---- Verifying IPV4 Address Ranges of Subnet [{}] in Addresses and Identifiers page ----".format(subnetid))
    navigate_to_addresses_and_identifiers_page()

    GeneralAddressesAndIdentifiers.expand_addressrange_collapser_addressesidentifiers_page(subnetid)
    GeneralAddressesAndIdentifiers.wait_for_ipv4subnet_table_addressesidentifiers_page(subnetid)
    try:
        VerifySubnetsAndRangeAddressIdentifiersPage.verify_ipv4_address_range(subnetid, addressrange_list)

    except AssertionError as Ex:
        logger.warn(Ex.message)
        raise AssertionError(Ex.message)
    logger.debug("Return Value - True")
    return True


def verify_addressrange_state(subnetid, addressrange_obj):
    '''
    Function to verify the address range state in Edit address and identifiers form as well as Address And Identifiers Page.
    Function checks if the range is enable or disabled.If disabled it also checks that no IPs are available

    Arguments:
        subnetid           -- subent ID the range is part of
        addressrange_obj   -- list of address range objects

    Return Value :
        returns a Boolean True on success else raises an AssertionError exception

    Input Example:
        <addressrange name = "test1" rangestart="1.1.160.30" rangeend="1.1.160.40" enable="False" />
        <addressrange name = "test2" rangestart="1.1.160.25" rangeend="1.1.160.29" enable="True" />

    '''
    error_msg_list = []

    logger.info("---- Verifying Address Range state of subnet [{}] in Edit Address and Identifiers form ----".format(subnetid))
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    GeneralAddressesAndIdentifiers.expand_addressrange_collapser_edit_dialog(subnetid)
    GeneralAddressesAndIdentifiers.wait_for_ipv4subnet_addressrange_table_edit_dialog(subnetid)

    for addressrange in addressrange_obj:
        if VerifySubnetsAndRangeEditDialog.verify_range_exists_in_table(addressrange.name, fail_if_false=False) is False:
            logger.warn("Range '{}' is not visible for subnet [{}]!".format(addressrange.name, subnetid))
            error_msg_list.append("Range '{}' is not visible for subnet [{}]!".format(addressrange.name, subnetid))
        else:
            logger.info("--Verifying Range {} Checkbox state".format(addressrange.name))
            if addressrange.enable.lower() == 'true' and VerifySubnetsAndAddressRange.verify_range_checkbox_selected(addressrange.name) is True:
                logger.debug("Range {} is ENABLED as Expected".format(addressrange.name))
            elif addressrange.enable.lower() == 'false' and VerifySubnetsAndAddressRange.verify_range_checkbox_selected(addressrange.name) is False:
                logger.debug("Range {} is DISABLED as expected".format(addressrange.name))
            else:
                logger.warn("Range {} state should be : '{}' but is not set to the same".format(addressrange.name, 'ENABLED' if addressrange.enable.lower() == 'true' else 'DISABLED'))
                error_msg_list.append("Range {} state should be : '{}' but is not set to the same".format(addressrange.name, 'ENABLED' if addressrange.enable.lower() == 'true' else 'DISABLED'))
            try:
                VerifySubnetsAndRangeEditDialog.verify_rangestate_and_availablecount(addressrange.name, addressrange.enable)
            except AssertionError as Ex:
                logger.warn(Ex.message)
                error_msg_list.append(Ex.message)
    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_ok()
    error_msg = GeneralAddressesAndIdentifiers.get_dialog_error_summary_details()
    if error_msg:
        logger.warn("Error Seen During Subnet Creation - \n [{}]".format(error_msg))
        error_msg_list.append(error_msg)
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=10)

    logger.debug("{}".format('-' * 10))
    logger.info("---- Verifying Address Range state of subnet [{}] in Address and Identifiers Page ----".format(subnetid))
    navigate_to_addresses_and_identifiers_page()
    GeneralAddressesAndIdentifiers.expand_addressrange_collapser_addressesidentifiers_page(subnetid)
    GeneralAddressesAndIdentifiers.wait_for_ipv4subnet_table_addressesidentifiers_page(subnetid)

    for addressrange in addressrange_obj:
        try:
            if VerifySubnetsAndRangeAddressIdentifiersPage.verify_range_exists_in_table(addressrange.name, fail_if_false=False) is False:
                errormsg = "Range '{}' is not visible for subnet [{}]!".format(addressrange.name, subnetid)
                logger.warn(errormsg)
                error_msg_list.append(errormsg)
            else:
                VerifySubnetsAndRangeAddressIdentifiersPage.verify_rangestate_and_availablecount(addressrange.name, addressrange.enable)
        except AssertionError as Ex:
            logger.warn(Ex.message)
            error_msg_list.append(Ex.message)
    logger.debug("{}".format('-' * 10))

    if error_msg_list:
        raise AssertionError(error_msg_list)

    logger.debug("Return Value - True")
    return True


def delete_subnet_verify_warning_and_associations_in_dialog(subnetid, associated_obj_list):
    '''
    Function to delete an associated  subnet and verify that a warning is visible , and to verify that the associated objects are listed in the warning dialog

    Parameters:
        subnetid                  - subnet id of the subnet to delete
        associated_obj_list       - list of the associated objects names (networks,LEs,EGs)

    Return Value:
        Boolean True on success else raises an AssertionError exception

    '''
    association_count = 0
    error_msg_list = []
    logger.info("-- Delete Subnet [{}] and Verify the associations shown in warning dialog".format(subnetid))
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    if not VerifySubnetsAndAddressRange.verify_edit_addressesidentifiers_ipv4_subnet_table_is_not_empty(timeout=10, fail_if_false=False):
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
        raise AssertionError("No Data available in the table")
    if VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnetid, fail_if_false=False) is False:
        raise AssertionError("Subnet [{}] does not exist".format(subnetid))

    if not DeleteSubnetsAndAddressRange.wait_for_delete_subnet_button(subnetid, fail_if_false=False):
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
        raise AssertionError("Delete subnet button not visible!!")

    DeleteSubnetsAndAddressRange.click_delete_subnet_button(subnetid)
    if DeleteSubnetsAndAddressRange.wait_for_subnet_delete_warning_dialog(fail_if_false=False):
        warning_msg = DeleteSubnetsAndAddressRange.get_subnet_delete_warning_dialog_message()
        logger.debug("Warning Seen on trying to delete subnet [{}] - \n{}".format(subnetid, warning_msg))
        GeneralAddressesAndIdentifiers.expand_all_collapsibles_subnet_deletewarning_dialog(timeout=10)
        for associated_obj in associated_obj_list:
            association_count = 0
            if VerifySubnetsAndAddressRange.verify_subnet_delete_associated_object_visible(associated_obj, fail_if_false=False):
                logger.debug("'{}' is visible in subnet delete warning dialog".format(associated_obj))
                association_count = GeneralAddressesAndIdentifiers.get_associatedobject_visible_count_subnetdelete_warning(associated_obj)
                if association_count > 1:
                    errmsg = "'{}' association is displayed {} times in subnet delete warning dialog".format(associated_obj, association_count)
                    logger.warn(errmsg)
                    error_msg_list.append(errmsg)
            else:
                errmsg = "{} is NOT displayed in the subnet delete warning dialog".format(associated_obj)
                logger.warn(errmsg)
                error_msg_list.append(errmsg)

        DeleteSubnetsAndAddressRange.click_delete_warning_dialog_close()
        DeleteSubnetsAndAddressRange.wait_for_subnet_delete_warning_dialog_disappear(timeout=8)
    else:
        error_msg_list.append("No Warning seen on Delete")

    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)
    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def delete_range_verify_warning_and_associations_in_dialog(subnetid, addressrange, associated_obj_list):
    '''
    Function to delete an associated  range and verify that a warning is visible , and to verify that the associated objects are listed in the warning dialog

    Parameters:
        subnetid                  - subnet id the range belongs to
        addressrange              - range to delete
        associated_obj_list       - list of the associated objects names (networks,LEs,EGs)

    Return Value:
        Boolean True on success else raises an AssertionError exception

    '''
    association_count = 0
    error_msg_list = []
    logger.info("-- Delete Range [{}] and verify the associations shown in the warning dialog".format(addressrange))
    try:
        _open_edit_addressesidentifiers_dialog_from_settings_page()
    except AssertionError as Ex:
        logger.warn(Ex.message)
        error_msg_list.append(Ex.message)
        _open_edit_addressesidentifiers_dialog_from_actions_menu()

    if VerifySubnetsAndAddressRange.verify_subnet_exists_in_editaddressidentifiers_table(subnetid, fail_if_false=False) is False:
        raise AssertionError("Subnet [{}] does not exist".format(subnetid))

    GeneralAddressesAndIdentifiers.expand_addressrange_collapser_edit_dialog(subnetid)
    GeneralAddressesAndIdentifiers.wait_for_ipv4subnet_addressrange_table_edit_dialog(subnetid)

    VerifySubnetsAndRangeEditDialog.verify_range_exists_in_table(addressrange, fail_if_false=True)

    if DeleteSubnetsAndAddressRange.wait_for_edit_dialog_delete_range_button(addressrange, fail_if_false=False) is False:
        GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
        GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)

        raise AssertionError("Delete range button not visible for range {}!!".format(addressrange))

    DeleteSubnetsAndAddressRange.click_edit_dialog_delete_range_button(addressrange)

    if DeleteSubnetsAndAddressRange.wait_for_range_delete_warning_dialog(fail_if_false=False):
        delete_warning = DeleteSubnetsAndAddressRange.get_range_delete_warning_dialog_message()
        logger.debug("Warning seen on trying to delete range [{}] - \n {}".format(addressrange, delete_warning))
        GeneralAddressesAndIdentifiers.expand_all_collapsibles_range_deletewarning_dialog(timeout=10)
        for associated_obj in associated_obj_list:
            association_count = 0
            if VerifySubnetsAndAddressRange.verify_range_delete_associated_object_visible(associated_obj, fail_if_false=False):
                logger.debug("'{}' is visible in range delete warning dialog".format(associated_obj))
                association_count = GeneralAddressesAndIdentifiers.get_associatedobject_visible_count_rangedelete_warning(associated_obj)
                if association_count > 1:
                    errmsg = "'{}' association is displayed '{}' times in range delete warning dialog".format(associated_obj, association_count)
                    logger.warn(errmsg)
                    error_msg_list.append(errmsg)
            else:
                errmsg = "{} is NOT displayed in the range delete warning dialog".format(associated_obj)
                logger.warn(errmsg)
                error_msg_list.append(errmsg)

        DeleteSubnetsAndAddressRange.click_delete_warning_dialog_close()
        DeleteSubnetsAndAddressRange.wait_for_range_delete_warning_dialog_disappear(timeout=8)
    else:
        error_msg_list.append("No Warning seen on Delete")

    GeneralAddressesAndIdentifiers.click_edit_addresses_and_identifiers_dialog_cancel()
    GeneralAddressesAndIdentifiers.wait_for_edit_addresses_and_identifiers_form_disappear(timeout=8)

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def verify_networks_association_or_disassociation_to_subnet(subnetid, associationstate, networks_list):
    '''
    Function to verify the Association/Disassociation of network to/from a subnet.

    Arguments:
        Arguments:
        subnetid                 -- subnetid of the subnet the network is associated with
        associationstate         -- True/False - True if verification is for network association , False if verification is from network disassociation
        networks_list            -- list of network names

    Return Value:
        Boolean True on success else raises an AssertionError exception
    '''
    logger.info("-- Verifying Network associations with subnet [{}] ".format(subnetid))
    error_msg_list = []
    navigate_to_addresses_and_identifiers_page()

    if not VerifySubnetsAndAddressRange.verify_subnet_exists_in_addressidentifierspage_table(subnetid, fail_if_false=False):
        raise AssertionError("The subnet [{}] does not exist".format(subnetid))
    if str(associationstate).lower() == 'true':
        for network in networks_list:
            if VerifySubnetsAndAddressRange.verify_associated_networks_visible_in_addressesidentifiers_page_table(subnetid, network, fail_if_false=False):
                logger.debug("Network {} is associated with subnet {}".format(network, subnetid))
            else:
                errmsg = "Network {} is not associated with subnet {}.Not visible in Subnet table".format(network, subnetid)
                logger.warn(errmsg)
                error_msg_list.append(errmsg)
    else:
        if VerifySubnetsAndAddressRange.verify_associated_networks_unset(subnetid, fail_if_false=False):
            logger.debug("No networks are associated with the subnet {}".format(subnetid))
            return True
        for network in networks_list:
            if VerifySubnetsAndAddressRange.verify_associated_networks_visible_in_addressesidentifiers_page_table(subnetid, network, fail_if_false=False):
                errmsg = "Network {} is still associated with the subnet {}".format(network, subnetid)
                logger.warn(errmsg)
                error_msg_list.append(errmsg)
            else:
                logger.debug("Network {} is not longer associated with subnet {}".format(network, subnetid))

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def get_ipv4_subnet_and_addressranges_in_addressidentifiers_page():
    '''
    Function to get the table data of subnet in Address and identifiers page

    Return Value:
        raises an AssertionError exception if no subnet are defined

    '''
    logger.info("-- Getting Subnet and Addresse ranges Table")

    navigate_to_addresses_and_identifiers_page()
    VerifySubnetsAndRangeAddressIdentifiersPage.verify_ipv4_subnet_addressrange_table_is_not_empty(fail_if_false=False)
    table_headers = GeneralAddressesAndIdentifiers.get_ipv4_subnet_addressranges_table_headers(timeout=8, fail_if_false=False)
    table_data = GeneralAddressesAndIdentifiers.get_ip4_subnet_addressranges_table_data(timeout=8, fail_if_false=False)

    if 'no subnets' in table_data.lower():
        raise AssertionError("No subnets have been defined")

    return table_headers + '\n' + table_data


def get_ipv4_addresses_count():
    '''
    Function to get the total address pool count as displayed in Settings page under Addresses and idenitifiers Link

    Return value:
        IP address count as integer
    '''
    logger.info("-- Getting Total IPV4 Addresses Count from settings page")
    if GeneralAddressesAndIdentifiers.wait_for_addresses_and_identifiers_page_visible(fail_if_false=False):
        GeneralAddressesAndIdentifiers.click_settings_link()
    navigate()
    GeneralAddressesAndIdentifiers.refresh_settings_page_and_wait_for_ipv4_addresses_count(timeout=10)
    total_count = GeneralAddressesAndIdentifiers.get_total_ipv4_addresses_count(timeout=10)

    if str(total_count).lower() in ("not set", "none", None, ''):
        logger.debug("IPV4 Addresses is [{}].'0' IPs available".format(total_count))
        total_count = 0
    else:
        logger.debug("Total IPV4 Addresses Available : {}".format(total_count))
    logger.debug("Return Vaue - {}".format(total_count))
    return int(total_count)


def get_count_of_allocatedip_in_addressrange(subnetid, rangename):
    '''
    Function to get the allocated ip count if the address range of the subnet specified

    Parameters:
        subnetid     - subnetid the range belongs to
        rangename    - range name

    return value:
        returns the allocated ip count on success else raise an AssertionError exception
    '''
    navigate_to_addresses_and_identifiers_page()

    if not VerifySubnetsAndRangeAddressIdentifiersPage.verify_ipv4_subnet_addressrange_table_is_not_empty(timeout=8, fail_if_false=False):
        raise AssertionError("No subnets have been defined")

    GeneralAddressesAndIdentifiers.expand_addressrange_collapser_addressesidentifiers_page(subnetid)
    GeneralAddressesAndIdentifiers.wait_for_ipv4subnet_table_addressesidentifiers_page(subnetid)
    return GetSubnetsAndAddressRangeAttributes.get_addressrange_allocatedcount_addressesidentifiers_page(rangename)


# ################# IP POOL FUNCTIONS END #################################


def appliance_factory_reset(user_name, appliance_password):
    """ factory reset appliance  """

    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    s2l = ui_lib.get_s2l()
    default_wait = PerfConstants.DEFAULT_SYNC_TIME

    logger._log_to_console_and_log_file("factory reset appliance")
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_APPLIANCE)
    ui_lib.wait_for_element_visible(
        FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN, default_wait)
    ui_lib.wait_for_element_and_click(
        FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(
        FusionSettingsPage.ID_ELEMENT_FACTORY_RESET)
    ui_lib.wait_for_element_visible(
        FusionSettingsPage.ID_FACTORY_RESET_PAGE_HEADER, default_wait)

    """ Confirm appliance reset """
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_FACTORY_RESET_PAGE_HEADER, default_wait):
        _confirm_factoty_reset()

    ui_lib.wait_for_element(
        FusionSettingsPage.ID_ELEMENT_RESETTING_PROGRESS, default_wait)
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_ELEMENT_RESETTING_PROGRESS):
        logger._log_to_console_and_log_file(
            "Appliance factory reset has been started")
        ui_lib.wait_for_element_notvisible(
            FusionSettingsPage.ID_ELEMENT_RESETTING_PROGRESS, 1200)
        if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_FACTORY_RESET_PAGE_HEADER, default_wait):
            ui_lib.wait_for_element_and_click(
                FusionSettingsPage.ID_BTN_CANCEL_FACTORY_RESET)
    else:
        logger._warn("Appliance factory reset is not yet started")
        ui_lib.fail_test("Failed to start reset appliance", True)

    """  Accepting EULA page  """
    if ui_lib.wait_for_element_visible(FusionLoginPage.ID_BTN_EULA_AGREE, default_wait):
        ui_lib.wait_for_element_and_click(FusionLoginPage.ID_BTN_EULA_AGREE)
        if ui_lib.wait_for_element_visible(FusionLoginPage.ID_BTN_OK_CONVERGED_INFRA_SUPPORT, default_wait):
            ui_lib.wait_for_element_and_click(
                FusionLoginPage.ID_BTN_OK_CONVERGED_INFRA_SUPPORT)
    else:
        ui_lib.fail_test("Failed to reset appliance", True)

    """ Login into appliance with default IP address and default credentials """
    ui_lib.wait_for_element_visible(
        FusionLoginPage.ID_INPUT_LOGIN_USER, default_wait)
    ui_lib.wait_for_element_and_input_text(
        FusionLoginPage.ID_INPUT_LOGIN_USER, user_name)
    ui_lib.wait_for_element_and_input_text(
        FusionLoginPage.ID_INPUT_LOGIN_PASSWORD, "admin")
    ui_lib.wait_for_element_and_click(FusionLoginPage.ID_BTN_LOGIN_BUTTON)

    """ Changing appliance default password """
    if (appliance_password is not None) or (len(appliance_password) >= 8):
        if ui_lib.wait_for_element_visible(FusionLoginPage.ID_INPUT_NEW_PASSWORD, default_wait):
            ui_lib.wait_for_element_and_input_text(
                FusionLoginPage.ID_INPUT_NEW_PASSWORD, appliance_password)
            ui_lib.wait_for_element_and_input_text(
                FusionLoginPage.ID_INPUT_CONFIRM_PASSWORD, appliance_password)
            ui_lib.wait_for_element_and_click(
                FusionLoginPage.ID_BTN_OK_PASSWORD_SCREEN)
    else:
        logger._warn(
            "Mandatory fields for changing default password can't be empty and should be at least 8 characters")

    s2l.wait_until_page_contains_element(
        FusionDashboardPage.ID_PAGE_LABEL, PerfConstants.FUSION_LOGIN_TIME, "Failed to load the Login Page")
    if not ui_lib.wait_for_element(FusionDashboardPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to Settings page", True)
    else:
        logger._log_to_console_and_log_file(
            "Successfully navigated to settings page after factory reset")
        return True


def _confirm_factoty_reset():
    """ Confirm factory reset """

    logger._log_to_console_and_log_file(
        ui_lib.get_text(FusionSettingsPage.ID_FACTORY_RESET_WARNING))
    ui_lib.wait_for_checkbox_and_select(
        FusionSettingsPage.ID_CHECKBOX_PREVENT_NEWORK_SETTINGS)
    ui_lib.wait_for_element_and_click(
        FusionSettingsPage.ID_BTN_START_FACTORY_RESET)
    ui_lib.wait_for_checkbox_and_select(
        FusionSettingsPage.ID_CHECKBOX_CONFIRM_FACTORY_RESET)
    ui_lib.wait_for_element_and_click(
        FusionSettingsPage.ID_BTN_CONFIRM_FACTORY_RESET)


def add_snmp_trap_forwarding_destination(*snmp_obj):
    """ add_snmp_trap_forwarding_destination

        Example:
        | `add_snmp_trap_forwarding_destination
    """

    """ Retrieve data from datasheet """
    if isinstance(snmp_obj, test_data.DataObj):
        snmp_obj = [snmp_obj]
    elif isinstance(snmp_obj, tuple):
        snmp_obj = list(snmp_obj[0])
    # variable to hold number of forwarding
    snmp_to_add = len(snmp_obj)
    add_snmp_flag = True
    for snmp in snmp_obj:
        # Check whether mandatory fields are empty or not
        if (snmp.trapForwarding == "" or snmp.port == "" or
                snmp.communityString == ""):
            add_snmp_flag = False
            raise ui_lib.NonFatalError(
                "Mandatory fields for adding SNMP Trap Forwarding can't be empty")
            continue
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_SNMP_PANEL)
    if ui_lib.get_text(FusionSettingsPage.ID_LABEL_SNMP_TRAP_DESTINATION_COUNT) == 'none':
        snmp_count = 0
    else:
        snmp_count = int(
            ui_lib.get_text(FusionSettingsPage.ID_LABEL_SNMP_TRAP_DESTINATION_COUNT))
    ui_lib.move_to_element_and_click(
        FusionSettingsPage.ID_LINK_SNMP, FusionSettingsPage.ID_LINK_EDIT_SNMP)
    ui_lib.wait_for_element_visible(
        FusionSettingsPage.ID_LABEL_EDIT_SNMP_SETTINGS)
    for snmp in snmp_obj:
        if ui_lib.table_contains(FusionSettingsPage.ID_LABEL_TRAP_DESTINATION, snmp.trapForwarding):
            logger._warn(
                "Trap Forwarding Destination '%s' is already present" % snmp.trapForwarding)
            add_snmp_flag = False
            continue
        logger.debug("Editing SNMP Trap Forwarding.")
        # add snmp trap forwarding
        ui_lib.wait_for_element_and_click(
            FusionSettingsPage.ID_BTN_ADD_TRAP_DESTINATION)
        logger.info("Opening Add SNMP Trap Forwarding page..")
        if not ui_lib.wait_for_element(FusionSettingsPage.ID_INPUT_TRAP_DESTINATION_ADD_TRAP_DESTINATION,
                                       PerfConstants.DEFAULT_SYNC_TIME):
            add_snmp_flag = False
            raise ui_lib.NonFatalError(
                "SNMP Trap Forwarding page is not opened")
        else:
            logger.info("Typing Trap Forwarding Destination..")
            ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_TRAP_DESTINATION_ADD_TRAP_DESTINATION,
                                                   snmp.trapForwarding)
            logger.info("Typing Port..")
            ui_lib.wait_for_element_and_input_text(
                FusionSettingsPage.ID_INPUT_PORT_ADD_TRAP_DESTINATION, snmp.port)
            logger.info("Typing Community String..")
            ui_lib.wait_for_element_and_input_text(
                FusionSettingsPage.ID_INPUT_COMMUNITY_STRING_ADD_TRAP_DESTINATION, snmp.communityString)
            ui_lib.wait_for_element_and_click(
                FusionSettingsPage.ID_BTN_ADD_ADD_TRAP_DESTINATION)
            if not ui_lib.table_contains(FusionSettingsPage.ID_LABEL_TRAP_DESTINATION, snmp.trapForwarding):
                add_snmp_flag = False
                raise ui_lib.NonFatalError(
                    "Trap Forwarding Destination '%s' was not added correctly" % snmp.trapForwarding)
                continue
            ui_lib.wait_for_element_and_click(
                FusionSettingsPage.ID_BTN_OK_EDIT_SNMP_SETTINGS)
            ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_SNMP_PANEL)
            snmp_count_updated = int(
                ui_lib.get_text(FusionSettingsPage.ID_LABEL_SNMP_TRAP_DESTINATION_COUNT))
            if snmp_count_updated == snmp_count + snmp_to_add:
                logger.info("Trap Forwarding Successfully Added")
                add_snmp_flag = True
            else:
                logger.warn("Not All Trap Forwarding Successfully Added")
                add_snmp_flag = False
        return add_snmp_flag


def create_support_dump_from_data_file(create_dump_support_obj):
    """Create Dump Support"""
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    time.sleep(10)
    CreateSupportDump.click_create_support_dump()
    CreateSupportDump.wait_create_support_dump_dialog_shown()

    if create_dump_support_obj.supportdumpencryption == "enable":
        CreateSupportDump.choose_enable_support_dump_encryption()

    CreateSupportDump.click_yes_create()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok("", message="Create support dump", timeout=600)
    FusionUIBase.show_activity_sidebar()
    logger.debug("Create support dump activity OK!")
    # TO DO download support dump file
    return True


def add_all_licenses_from_data_file(*license_obj):
    """ Add all Licenses from data file to appliance """
    BuiltIn().log("Add all Licenses from data file to appliance", console=True)
    s2l = ui_lib.get_s2l()

    """ Call function to navigate to licenses """
    _Navigate_To_Licenses()

    """ Retrieve data from datasheet """
    if isinstance(license_obj, test_data.DataObj):
        license_obj = [license_obj]
    elif isinstance(license_obj, tuple):
        license_obj = list(license_obj[0])

    for lic in license_obj:
        verify_data_file_license(lic)

        license_key = getattr(lic, 'content')

        """ Entering inputs in ADD License Page """
        ui_lib.wait_for_element_and_click(
            FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_visible(
            FusionSettingsPage.ID_MENU_ACTION_ADDLICENSE)
        ui_lib.wait_for_element_and_click(
            FusionSettingsPage.ID_MENU_ACTION_ADDLICENSE)
        ui_lib.wait_for_element_visible(FusionSettingsPage.ID_DLG_ADDLICENSE)
        s2l.input_text(FusionSettingsPage.ID_INPUT_LICENSEKEY, license_key)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DLG_BTN_ADD)

        """ Check for Error messages """
        if ui_lib.wait_for_element(FusionSettingsPage.ID_ADDLICENSE_ERR_MSG):
            strErr = s2l._get_text(FusionSettingsPage.ID_ADDLICENSE_ERR_MSG)
            ui_lib.wait_for_element_and_click(
                FusionSettingsPage.ID_DLG_BTN_CANCEL)
            BuiltIn().fail("Unable to Add License with key %s, and the Err Msg from OneView is %s" %
                           (license_key, strErr))


def verify_data_file_license(license_obj):
    """ verify data file license"""
    if hasattr(license_obj, 'content'):
        content = getattr(license, 'content')

        if content == '':
            BuiltIn().fail("Content attribute was empty in data file")
    else:
        BuiltIn().fail(
            "No content attribute was detected for license in data file")


def validate_appliance_version(version):
    """ validating the appliance verison"""
    # navigate to settings page
    navigate()
    logger.info("validating the version of the appliance to which it is updated")
    # obtaining the version number from the settings Page
    version_number = Updateappliance.get_appliance_version()
    logger.info("version no. obtained from ui page is %s" % version_number)

    build_number = version_number.split('-')
    # getting the build version and comparing the same with the user data
    try:
        if build_number[1] == version:
            logger.info("validated successfully that the appliance is updated to the expected build")
        else:
            ui_lib.fail_test("Failing the verification since the appliance is not updated to the expected version")
    except IndexError as e:
        logger.debug("Index error: build version can't be verified")
        raise e
    return True


def get_version():
    """ Returns appliance version"""
    # navigate to settings page
    navigate()
    version_number = Updateappliance.get_appliance_version()
    logger.info("version no. obtained from ui page is %s" % version_number)
    return version_number


def download_cidebug_logs(folder=None):
    """ Download ciDebug Logs
        Download the ciDebug logs from Fusion
        Arguments:
            folder - the destination folder
    """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()

    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_DIAGNOSTIC_TOOLS_LINK, timeout=30, fail_if_false=True)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DIAGNOSTIC_TOOLS_LINK)

    # Get the URL for the ciDebug log file and download the file
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN, timeout=30)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_CIDEBUG_LOGS, fail_if_false=True)
    ui_lib.download_file(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_CIDEBUG_LOGS, folder)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_SETTINGS_LINK, fail_if_false=True)

    logger.info('ciDebug log downloaded successfully in path "{0}"'.format(folder))
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_SETTINGS_LINK)


def download_fixme_installation_details(folder=None):
    """Download fixme installation details to specified loaction"""
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_APPLIANCE_LINK)
    Updateappliance.click_action_button(timeout=PerfConstants.UPLOAD_PATCH_FILE * 4, fail_if_false=True)
    logger.info("Downloading fixme Installation details")
    ui_lib.download_file(FusionSettingsPage.ID_DWNLD_FIXME_INSTALLATION_DETAILS, folder)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_SETTINGS_LINK, fail_if_false=True)
    logger.info('Fixme installation details downloaded successfully in path "{0}"'.format(folder))
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_SETTINGS_LINK)
