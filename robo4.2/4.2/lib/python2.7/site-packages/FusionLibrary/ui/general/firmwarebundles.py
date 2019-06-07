# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Firmware Bundles page
"""


from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.keywords.vsphere import VsphereKeywords
from RoboGalaxyLibrary.keywords.ntnative import NativeOsKeywords
from FusionLibrary.ui.business_logic.general.firmwarebundles_elements import FusionFirmwareBundlePage
from FusionLibrary.ui.general.base_page import FusionUIBaseElements
from FusionLibrary.ui.general import base_page
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.general.firmwarebundles import CommonOperationFirmwareBundle, AddFirmwareBundle, RemoveFirmwareBundle, VerifyFirmwareBundle
from FusionLibrary.ui.business_logic.base import FusionUIBase
import time
import sys


def navigate():
    base_page.navigate_base(FusionFirmwareBundlePage.ID_PAGE_LABEL, FusionUIBaseElements.ID_MENU_LINK_FIRMWARE_BUNDLES, "css=span.hp-page-item-count")
    CommonOperationFirmwareBundle.wait_add_firmware_bundle_button_show()


def add_latest_firmware_bundle(fwbundles):
    # Adding the latest firmware bundles to the appliance
    logger.debug("Adding the latest firmware bundles")
    navigate()
    uploaded = 0
    for fwbundle in fwbundles:
        spp_repo = fwbundle.repo
        spp_ext = fwbundle.ext
        spp_filter = fwbundle.filter
        logger.debug("Adding the latest firmware bundle with repo [%s] extension [%s] and filter [%s]" % (spp_repo, spp_ext, spp_filter))
        fwbundle.spp = VsphereKeywords().get_LatestBuild_name(spp_repo, "", spp_ext, spp_filter)
        logger.debug("Latest firmware bundle is [%s]" % fwbundle.spp)
        uploaded = _add_firmware_bundle(fwbundle, uploaded)
        CommonOperationFirmwareBundle.refresh_browser_on_firmware_page()

    if len(fwbundles) == uploaded:
        logger.debug("SUCCESS : Added all the Firmware bundles mentioned in the data file.")
        return True
    else:
        logger.warn("FAILURE : Not able to add all Firmware Bundles as mentioned in the data file.")
        ui_lib.get_s2l().capture_page_screenshot()
        return False


def _add_firmware_bundle(fwbundle, uploaded):
        logger.debug("Adding the firmware bundles [ %s ]" % fwbundle.spp)
        fwname = fwbundle.spp
        fwsplit = fwname.split("/")
        fwbundle.spp = fwsplit[len(fwsplit) - 1].strip()
        AddFirmwareBundle.click_add_firmware_bundle_button()
        AddFirmwareBundle.wait_add_firmware_bundle_dialog_open()
        AddFirmwareBundle.click_select_file_button()

        def choose_spp_file():
                try:
                    """
                    Call AutoIt module to handle OS native file open dialog for choose upgrade file
                    Note: Must install pyautoit module at first
                    """
                    win32 = NativeOsKeywords()
                    logger.debug("Starting choosing SPP iso file to be uploaded %s" % (fwbundle.sppfilepath + fwbundle.spp))
                    win32.activate_window("File Upload")
                    logger.debug("Typing SPP iso file path into [ File Name ] text box")
                    win32.input_text("File Upload", "Edit1", (fwbundle.sppfilepath + fwbundle.spp))
                    logger.debug("Clicking [ Open ] button")
                    time.sleep(2)
                    win32.click_button("File Upload", "Button1")
                    time.sleep(2)
                    win32.wait_window_close("File Upload", timeout=30)
                except ImportError as e:
                    logger.debug("Can't choose file to be uploaded due to failed to import autoit module!\nPlease install it by 'pip install -U pyautoit'")
                    raise e

        if "win" in sys.platform:
            choose_spp_file()
        else:
            ui_lib.fail_test("This keyword can only choose file to be uploaded on windows platform")

        AddFirmwareBundle.click_ok_button()
        logger.debug("Waiting for uploading to be completed ...")

        if not AddFirmwareBundle.wait_form_message_disappear():
            status_text = AddFirmwareBundle.get_upload_error_text()
            if status_text is not None:
                if "already" in status_text:
                    logger.debug("Firmware bundle " + fwbundle.spp + " is already added")
                    uploaded += 1
                    AddFirmwareBundle.click_close_button()
                elif "enough" in status_text:
                    logger.debug("System has no enough space")
                    AddFirmwareBundle.click_close_button()
                    return uploaded
                elif "Adding" in status_text:
                    logger.debug("Firmware bundle is adding")
                    logger.debug("Click close button to close upload dialog due to known issue: QXCR1001497081")
                    AddFirmwareBundle.click_close_button()
                else:
                    ui_lib.fail_test("Unexpected error occur: %s" % status_text)
            else:
                AddFirmwareBundle.click_close_button(fail_if_false=False)

        AddFirmwareBundle.wait_add_firmware_bundle_dialog_close()

        fwname = fwbundle.spp
        fwsplit = fwname.split(".")
        fwtype = fwsplit[len(fwsplit) - 1].strip()
        # For SPP, the final name is "Service Pack for ProLiant". But for hotfix, it's different
        sspname = "Service Pack for ProLiant"
        if fwtype != "iso":
            sppname = fwname.split("." + fwtype)
            sppname[0] = sppname[0].strip()
            sspname = sppname[0].replace(".", "_")

        logger.debug("Verifying the firmware bundle upload at Activity Panel")
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(sspname, 'Add', timeout=600, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        logger.info("Successfully upload firmware bundle '%s'" % fwname)
        uploaded += 1

        return uploaded


def add_firmware_bundle(fwbundles):
    # adding the firmware bundles to the appliance
    logger.debug("Adding the firmware bundles..")
    navigate()

    uploaded = 0
    # Loop to upload the list of firmware bundles
    for fwbundle in fwbundles:
        uploaded = _add_firmware_bundle(fwbundle, uploaded)
        CommonOperationFirmwareBundle.refresh_browser_on_firmware_page()

    if len(fwbundles) == uploaded:
        logger.debug("SUCCESS : Added all the Firmware bundles mentioned in the data file.")
        return True
    else:
        logger.warn("FAILURE : Not able to add all Firmware Bundles as mentioned in the data file.")
        ui_lib.get_s2l().capture_page_screenshot()
        return False


def validate_firmware_bundle_component(fwbundles):
    # check the firmware bundles component
    logger.info("Validating the firmware bundles..")
    navigate()

    # Loop to upload the list of firmware bundles
    for fwbundle in fwbundles:
        logger.info("Start to validate firmware bundle [%s, %s]" % (fwbundle.sppname, fwbundle.firmwareversion))
        CommonOperationFirmwareBundle.click_firmware_bundle(fwbundle.sppname, fwbundle.firmwareversion)
        for index, component in enumerate(fwbundle.Components):
            name = getattr(component, 'name', '')
            version = getattr(component, 'version', '')
            VerifyFirmwareBundle.verify_firmware_component(name, version)


def delete_firmware_bundle(obj_fwbundle):

    logger.info("Deleting the firmware bundles..")

    """ Navigate to Firmware Bundle Page """
    navigate()

    fail_count = 0
    spp_len = len(obj_fwbundle)

    for spp in obj_fwbundle:
        logger.info("Deleting Firmware Bundle %s" % spp.firmwarename)

        """ Split the firmware to name and version """
        fwname = (spp.firmwarename).split(",")
        sppname = fwname[0].strip()
        firmwareversion = fwname[1].strip()

        """ Select the firmware in Firmware bundle page """
        if not CommonOperationFirmwareBundle.click_firmware_bundle(sppname, firmwareversion, fail_if_false=False):
            fail_count += 1
            continue

        RemoveFirmwareBundle.select_action_delete()
        RemoveFirmwareBundle.wait_remove_firmware_bundle_dialog_open()
        if RemoveFirmwareBundle.wait_yes_remove_button_shown():
            RemoveFirmwareBundle.click_yes_remove_button()
        else:
            RemoveFirmwareBundle.click_remove_bundle_button()
        RemoveFirmwareBundle.wait_remove_firmware_bundle_dialog_close()
        RemoveFirmwareBundle.wait_firmware_bundle_removed(sppname, firmwareversion)

    if fail_count > 0:
        ui_lib.fail_test("<%s> of <%s> firmware bundle select failed!" % (str(fail_count), str(spp_len)))


def validate_cannot_delete_firmware_bundle(obj_fwbundle):

    logger.info("Verify cannot delete the firmware bundles..")

    """ Navigate to Firmware Bundle Page """
    navigate()

    fail_count = 0
    spp_len = len(obj_fwbundle)

    for spp in obj_fwbundle:
        logger.info("Deleting Firmware Bundle %s" % spp.firmwarename)

        """ Split the firmware to name and version """
        fwname = (spp.firmwarename).split(",")
        sppname = fwname[0].strip()
        firmwareversion = fwname[1].strip()

        """ Select the firmware in Firmware bundle page """
        if not CommonOperationFirmwareBundle.click_firmware_bundle(sppname, firmwareversion, fail_if_false=False):
            fail_count += 1
            continue

        RemoveFirmwareBundle.select_action_delete()
        RemoveFirmwareBundle.wait_remove_firmware_bundle_dialog_open()
        if RemoveFirmwareBundle.wait_yes_remove_button_shown():
            RemoveFirmwareBundle.click_yes_remove_button()
        else:
            RemoveFirmwareBundle.click_remove_bundle_button()
        RemoveFirmwareBundle.wait_remove_firmware_bundle_dialog_close()
        RemoveFirmwareBundle.click_remove_error_title()
        RemoveFirmwareBundle.verify_remove_firmware_bundle_error_text()

    if fail_count > 0:
        ui_lib.fail_test("<%s> of <%s> firmware bundle select failed!" % (str(fail_count), str(spp_len)))
    else:
        logger.info("All firmware bundles verify successfully!")


def validate_firmware_bundle_task_error(obj_fwbundle):
    """ Validate Firmware Bundle Task Error
     Arguments:
      name*                  --  Name of Firmware Bundle.
      task*                  --  Task name to be verified
      error_message*         --  Firmware bundle upload error message.

    * Required Arguments

    Example:
        data/LogicalEnclosures/LogicalEnclosuresVerifyFirmware -> @{TestData.LogicalEnclosures.LogicalEnclosuresVerifyFirmware}
        <FirmwareBundles>
            <FirmwareBundles>
                <FirmwareBundle firmwarename="SPP2016020.2015_1204.63.iso, unknown version" error_message="Synergy Frame Link Module Firmware not present" task="Add">
                    <None/>
                </FirmwareBundle>
            </FirmwareBundles>
        </FirmwareBundles>

     """

    logger.info("Validate Firmware Bundle Task Error..")

    """ Navigate to Firmware Bundle Page """
    navigate()

    fail_count = 0
    spp_len = len(obj_fwbundle)

    for spp in obj_fwbundle:
        logger.info("Validating Firmware Bundle %s" % spp.firmwarename)

        """ Split the firmware to name and version """
        fwname = (spp.firmwarename).split(",")
        firmware_name = fwname[0].strip()
        firmware_version = fwname[1].strip()

        """ Select the firmware in Firmware bundle page """
        if not CommonOperationFirmwareBundle.click_firmware_bundle(firmware_name, firmware_version, fail_if_false=False):
            fail_count += 1
            continue

        FusionUIBase.select_view_by_name("Activity")

        CommonOperationFirmwareBundle.click_activity_collapser(spp.task)
        VerifyFirmwareBundle.verify_activity_contains_text(spp.error_message)

        logger.info("Firmware Bundle '%s' got the correct task content" % spp.firmwarename)

    if fail_count > 0:
        ui_lib.fail_test("<%s> of <%s> firmware bundle select failed!" % (str(fail_count), str(spp_len)))
    else:
        return True


def select_firmware_bundle(sppname, firmwareversion):
    """ Select firmware_bundle  """
    navigate()
    return CommonOperationFirmwareBundle.click_firmware_bundle(sppname, firmwareversion, fail_if_false=False)
