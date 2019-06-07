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
ROBOT_LIBRARY_VERSION = '0.0'

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.facilities.settings_elements import FusionSettingsPage
from FusionLibrary.ui.general.base_elements import FusionBasePage
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.general.login_elements import FusionLoginPage
from datetime import datetime
import os


def navigate():
    navigate_settings_base(FusionSettingsPage.ID_PAGE_LABEL,
                           FusionBasePage.ID_MENU_LINK_SETTINGS)

    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to Settings page", True)


def navigate_settings_base(currentpage, menulink):
    logger._log_to_console_and_log_file('Navigating to "{0}"'.format(currentpage))
    if not ui_lib.wait_for_element(currentpage):
        ui_lib.wait_for_element_and_click(FusionBasePage.ID_MAIN_MENU_CONTROL)
        ui_lib.wait_for_element(FusionBasePage.ID_MENU_LINK_USERS_AND_GROUPS, 10)
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

    # Get the URL for the audit log file and download the file
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_visible(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_AUDIT_LOGS, fail_if_false=True)
    ui_lib.download_file(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_AUDIT_LOGS, folder)


def create_self_signed_certificate(*props):
    """ Create Self Signed Certificate

        Not Yet Implemented


        Example:
        | `Create Self Signed Certificate`      |     |
    """
    pass


def create_certificate_signing_request(*props):
    """ Create Certificate Signing Request

        Not Yet Implemented


        Example:
        | `Create Certificate Signing Request`      |     |
    """
    pass


def import_certificate(cert):
    """ Import Certificate

        Not Yet Implemented


        Example:
        | `Import Certificate`      |     |
    """
    pass


def update_appliance():
    """ Update Appliance

        Not Yet Implemented


        Example:
        | `Update Appliance`      |     |
    """
    pass


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
    editoption = s2l.get_text(FusionSettingsPage.ID_TOGGLE_BTN_SERVICE_ACCESS)
    if editoption.lower() == isEnabled.lower():
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK_SUPPORT_ACCESS)
    elif editoption == "Enabled" and isEnabled == "Disabled":
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_TOGGLE_OFF)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK_SUPPORT_ACCESS)
    else:
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_TOGGLE_ON)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_OK_SUPPORT_ACCESS)
    ui_lib.wait_for_element(FusionSettingsPage.ID_LABEL_STATUS)
    lablestatus = s2l.get_text(FusionSettingsPage.ID_LABEL_STATUS)
    if lablestatus.lower() == isEnabled.lower():
        logger._log_to_console_and_log_file("Services access is successfully updated from '%s' to '%s'" % (editoption, isEnabled))
        return True
    else:
        logger._warn("Failed to edit Services access ")
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

    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_DOWNLOAD_BACKUP)

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


def restore_from_backup(backupdirectory):
    """ Restore From Backup : restore backup for fusion appliance,

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

    logger._log_to_console_and_log_file("Restart Appliance")
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_MENU_ACTION_RESTART)
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_RESTART):
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_YES_CONFIRM_SHUTDOWN)
    else:
        ui_lib.fail_test('Failed: The message while restarting the appliance is not displayed')
    # Checking whether the fusion appliance started restarting or not
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_WAITING, PerfConstants.RESTART_LABEL_VISIBLE):
        logger._log_to_console_and_log_file("The fusion appliance is restarted successfully and getting shutdown")
    else:
        ui_lib.fail_test('Failed: The fusion appliance failed to restart')
    # Checking whether the fusion appliance is shut down or not
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_UNAVAILABLE, PerfConstants.STARTING_PROGRESS_VISIBLE):
        logger._log_to_console_and_log_file("The fusion appliance is shutdown successfully ")
    else:
        ui_lib.fail_test('Failed: The fusion appliance failed to shutdown the appliance in the restart procedure')
    # Checking whether the fusion appliance started to power on or not
    if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_STARTING, PerfConstants.STARTING_PROGRESS_VISIBLE):
        logger._log_to_console_and_log_file("The fusion appliance is powering on")
    else:
        ui_lib.fail_test('Failed: The fusion appliance failed to power on after it is shutdown')
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


def edit_appliance_details(*props):
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
    s2l.mouse_over(FusionSettingsPage.ID_LINK_ADDRESS_AND_IDENTIFIER)
    s2l.mouse_up("//div[@id='cic-settings-guid-panel']/header/a[text()='Edit']")

    # Check for the edit link, if now highlighted by mouse over then the fn will exit.
    if not ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_EDIT_ADDRESS_AND_IDENTIFIER):
        ui_lib.fail_test("Not able to edit Address and Identifier", True)

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
        for x in xrange(0, int(edit_obj[0].mac.autoflag[0].addautogenratedcount)):
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
        for x in xrange(0, int(edit_obj[0].wwn.autoflag[0].addautogenratedcount)):
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
        return False
    else:
        # No Error, Clicking on add
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ADD_CUSTOM_RANGE)
        if ui_lib.wait_for_element_visible(FusionSettingsPage.ID_LABEL_CUSTOM_ADD_OVERLAPPING_ERROR):
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_CANCEL_MAC_CUSTOM_ADD)
            logger._warn(" Cannot create overlapping pool. Please select a different range, CURRENT RANGE PASSED - '%s'" % addrange.rangefrom)
            return False
        else:
            # check for custom range in table after addition.
            from_element = s2l._table_element_finder.find_by_content(s2l._current_browser(), table_locator, addrange.rangefrom)
            to_element = s2l._table_element_finder.find_by_content(s2l._current_browser(), table_locator, addrange.to)

            if from_element is None or to_element is None:
                logger._warn(" Custom Range not reflecting in table, range starting from %s" % addrange.rangefrom)
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
        return False
    else:
        logger._log_to_console_and_log_file("Added AUTO GENERATED RANGE")
        return auto_from


def editDevelopmentSettings(*props):
    """ Create Support Dump

        Not Yet Implemented


        Example:
        | `Create Support Dump`      |     |
    """
    pass


def editSecurity(*props):
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

    for lic in license_obj:

        """ Get the License name strlicense"""
        if (lic.licensepath).endswith("OneView_16.dat"):
            logger._log_to_console_and_log_file("check for the existence of HP OneView license ")
            strlicense = "HP OneView"
        elif (lic.licensepath).endswith("OneView_no_ilo100.dat"):
            logger._log_to_console_and_log_file("check for the existence of HP OneView w/o iLO license")
            strlicense = "HP OneView w/o iLO"
        else:
            logger._log_to_console_and_log_file("Given license is not supported by fusion")
            continue

        """ Call function to check the availability of license """
        strVal = check_availability_licenses(strlicense)
        if not strVal:
            logger._log_to_console_and_log_file("License %s does not exists,Add the license now ")
            fopen = open(lic.licensepath)
            strLincenseKey = fopen.read()
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
            ui_lib.wait_for_element_visible(FusionSettingsPage.ID_DLG_ADDLICENSE)
            s2l.input_text(FusionSettingsPage.ID_INPUT_LICENSEKEY, strLincenseKey)
            ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DLG_BTN_ADD)

            """ Check for Error messages """
            if not ui_lib.wait_for_element(FusionSettingsPage.ID_ADDLICENSE_ERR_MSG):

                if not check_availability_licenses(strlicense):
                    logger._warn("Fail in Adding License %s" % strlicense)
                else:
                    logger._log_to_console_and_log_file("License %s is added successfully" % strlicense)

            else:
                strErr = s2l._get_text(FusionSettingsPage.ID_ADDLICENSE_ERR_MSG)
                logger._log_to_console_and_log_file("Unable to Add License %s,and the Err Msg is %s" % (strlicense, strErr))
                ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DLG_BTN_CANCEL)
        else:
            logger._log_to_console_and_log_file("License %s available with licenses,Check the other License" % strlicense)
    return True


def check_availability_licenses(strlicense):
    """ check_availability_licenses

        Example:
        | check_availability_licenses("HP OneView")
    """

    s2l = ui_lib.get_s2l()

    """ Call function to navigate to licenses """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        _Navigate_To_Licenses()

    """ Check the availability of license in Licenses Page and get the License Number """
    if ui_lib.wait_for_element(FusionSettingsPage.ID_LICENSE_AVAILABILITY % strlicense):
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_AVAILABLE_LICENSE % strlicense)
        intAvailableLicense = s2l._get_text(FusionSettingsPage.ID_AVAILABLE_LICENSE % strlicense)
        intAvlLicense = intAvailableLicense.split()

        if int(intAvlLicense[0].strip()) > 0:
            logger._log_to_console_and_log_file("License %s available with %s licenses" % (strlicense, str(intAvlLicense[0])))
            return True
        else:
            logger._log_to_console_and_log_file("License %s available with %s licenses" % (strlicense, str(intAvlLicense[0])))
            return False
    else:
        logger._log_to_console_and_log_file("License %s not available " % strlicense)
        return False


def _Navigate_To_Licenses():
    """ _Navigate_To_Licenses

        Example:
        | _Navigate_To_Licenses()
    """

    """ Navigate to Settings Page """
    if not ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element_and_click(FusionBasePage.ID_MAIN_MENU_CONTROL)
        ui_lib.wait_for_element(FusionBasePage.ID_MENU_LINK_USERS_AND_GROUPS, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionBasePage.ID_MENU_LINK_SETTINGS)
        ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL)

    if ui_lib.wait_for_element(FusionSettingsPage.ID_PAGE_LABEL):
        logger._log_to_console_and_log_file("Navigated succesfully to Settings Page")
        ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_OVERVIEW)
        ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_LICENSE)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_LINK_LICENSE)

        if ui_lib.wait_for_element(FusionSettingsPage.ID_LINK_OVERVIEW_DROPDOWN % 'Licenses'):
            logger._log_to_console_and_log_file("Navigated succesfully to Licenses")
            return True
        else:
            ui_lib.fail_test("Fail to Navigate Licenses")
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
    if dServer.domainName in directories:
        logging._log_to_console_and_log_file("Removing directory server '%s'" % dServer.domainName)
        # Press the Edit Icon (next to Security).
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_SECURITY_EDIT)
        # wait until table is visible
        ui_lib.wait_for_element(FusionSettingsPage.ID_BTN_ADD_DIRECTORY_SETTINGS)
        # click X to delete the server
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_DIRECTORY_DEL % dServer.domainName)
        # confirm yes
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_REMOVE_SERVER_YES_BUTTON)
        # validate server is deleted
        if ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SERVER_ALREADY_ADDED):
            logging._log_to_console_and_log_file("ERROR deleting the directory server '%s' was not deleted" % dServer.domainName)
            return False
    else:
        if fail_on_err:
            logging._log_to_console_and_log_file("Cannot delete - directory server did not exist in the list: '%s'" % dServer.domainName)
            ui_lib.fail_test("Cannot delete - directory server did not exist: '%s'" % dServer.domainName)
        return False


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
    itemCount = len(selenium2lib.get_list_items("xpath=//*[@id='fs-settings-authn-dir-type-select']"))

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
    itemIndex = 0
    while (selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT) != desiredText) and (itemIndex < itemCount):
        # Log the current item we see
        logger._log_to_console_and_log_file("Got text: '" + selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT) + "'")
        # Press the key of the first letter of the desired text
        selenium2lib.press_key(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT, desiredText[0])
        # Confirm the selection by pressing Enter - this initiates the change we need on the UI to pick up the selection
        selenium2lib.press_key(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT, '\\13')
        # Make sure we don't do this more times than there are items in the list
        itemIndex += 1

    # Fail if we didn't find it
    if selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT) != desiredText:
        ui_lib.fail_test("Desired text " + desiredText + " not found.")
        return False
    # Log that we do indeed have the desired text
    logger._log_to_console_and_log_file("Finally got text: '" + selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT) + "'")
    # NOTE: If the UI seems to be going haywire & preventing Selenium from hitting "Add Directory", insert an Enter key-press here
    selenium2lib.press_key(FusionSettingsPage.ID_ELEMENT_LDAP_SELECT, '\\13')

    # Search context
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_UID, dServer.userNamefield)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_ORG, dServer.org)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_TOP, dServer.top)

    # Credentials (Username & Password)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_AUTHN_USERNAME, dServer.userName)
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_AUTHN_PASSWORD, dServer.userPswd)

    # Add Directory Server button
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ADD_DIRECTORY)
    # IP address or host name
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_IPADDRESS, dServer.server)
    # Directory server port
    ui_lib.wait_for_element_and_input_text(FusionSettingsPage.ID_INPUT_SERVER_PORT, dServer.port)
    # Directory server Certificate
    # fopen = open(os.environ['ROBOPATH'] + dServer.cert)
    fopen = open(dServer.cert)
    cert = fopen.read()
    cert = cert.replace('\n', '\\n').replace('\r', '')
    browser = selenium2lib._current_browser()
    browser.execute_script("document.getElementById('%s').value = '%s';" % (FusionSettingsPage.JS_ID_INPUT_CERTIFICATE, cert))
    # Click on Add button
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_DIRECTORY_SERVER_ADD)

    # validate server is added
    ui_lib.wait_for_element(FusionSettingsPage.ID_BTN_ADD_DIR)
    ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_ADD_DIR)
    if ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SERVER_ALREADY_ADDED):
        logging._log_to_console_and_log_file("Directory server '%s' is added in the appliance" % dServer.domainName)
        ui_lib.wait_for_element_and_click(FusionSettingsPage.ID_BTN_DIR_SERVER_CANCEL)
        return True

    ui_lib.wait_for_element(FusionSettingsPage.ID_ELEMENT_SECURYTY_HEADER)
    # ui_lib.wait_for_element(FusionSettingsPage.ID_SECURITY_EDIT)
    directories = selenium2lib.get_text(FusionSettingsPage.ID_ELEMENT_DIRECTORIES)
    if dServer.domainName in directories:
        logging._log_to_console_and_log_file("Directory server '%s' is added in the appliance" % dServer.domainName)
        return True

    ui_lib.fail_test("failed to add directory server '%s'  in the appliance" % dServer.domainName)
    return False
