# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Logical Enclosure UI page."""
from FusionLibrary.ui.servers.logicalenclosures_elements import FusionLogicalEnclosuresPage
from FusionLibrary.ui.business_logic.base import FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.networking import interconnects, logicalinterconnects
from FusionLibrary.ui.servers import serverhardware
from FusionLibrary.ui.settings import settings
from FusionLibrary.ui.business_logic.base import SectionType, FusionUIConst
# from FusionLibrary.ui.business_logic.servers.logicalenclosures import *
import re
from FusionLibrary.ui.business_logic.servers.logicalenclosures import (VerifyLogicalEnclosures,
                                                                       C7000VerifyLogicalEnclosures,
                                                                       TBirdVerifyLogicalEnclosures,
                                                                       CommonOperationLogicalEnclosures,
                                                                       C7000CommonOperationLogicalEnclosures,
                                                                       TBirdCommonOperationLogicalEnclosures,
                                                                       TBirdCreateLogicalEnclosures,
                                                                       TBirdDeleteLogicalEnclosures,
                                                                       ReapplyConfiguration,
                                                                       TBirdReapplyConfiguration,
                                                                       C7000ReapplyConfiguration,
                                                                       UpdateFromGroup,
                                                                       TBirdUpdateFromGroup,
                                                                       C7000UpdateFromGroup,
                                                                       CreateSupportDump,
                                                                       TBirdCreateSupportDump,
                                                                       C7000CreateSupportDump,
                                                                       EditLogicalEnclosures,
                                                                       TBirdEditLogicalEnclosures,
                                                                       C7000EditLogicalEnclosures,
                                                                       UpdateFirmware,
                                                                       TBirdUpdateFirmware
                                                                       )

from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants


def navigate():
    logger.info("Navigate to LE page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_ENCLOSURES)


def create_tbird_logical_enclosure(le_obj):
    """ Create Logical Enclosure
    Arguments:
      name*                     --  Name of Logical Enclosure as a string.
      firmwarebaseline*         --  Firmware baseline to be updated.
      enclosures*               --  Enclosure to create LE
      forceinstall              --  If we should force install the firmware
      encgroup*                 --  Enclosure group to create LE

    * Required Arguments

    Example:
        data/LogicalEnclosures/Create -> @{TestData.LogicalEnclosures.Create}
        <LogicalEnclosures>
            <Create>
                <LogicalEnclosure name="LE_SYNERGY" enclosures="CN754404R6, CN754406WB, CN754406XL" encgroup="EG_SYNERGY" firmwarebaseline="Service Pack for ProLiant version gen9snap6" forceinstall="True">
                    <None/>
                </LogicalEnclosure>
            </Create>
        </LogicalEnclosures>
    """

    navigate()

    logger.debug("Creating T-Bird logical enclosure...")

    count = 0
    failed = 0
    total_len = len(le_obj)
    create_le_list = []
    for n, le in enumerate(le_obj):
        # check if LE is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Adding a LE with name '{0}'".format(le.name))
        ui_lib.get_s2l().capture_page_screenshot()
        if not TBirdVerifyLogicalEnclosures.verify_logical_enclosure_not_exist(le.name, fail_if_false=False):
            logger.warn("LE '{0}' already exists".format(le.name))
            continue
        create_le_list.append(le)
        TBirdCreateLogicalEnclosures.click_create_logical_enclosure()
        TBirdCreateLogicalEnclosures.wait_create_le_dialog_shown()
        TBirdCreateLogicalEnclosures.input_name(le.name)

        add_plus = False

        if n < total_len - 1:
            add_plus = True

        TBirdCreateLogicalEnclosures.input_select_enclosures_dropdown(le.enclosures)
        TBirdCreateLogicalEnclosures.input_select_enclosure_group(le.encgroup)

        fwbaseline = getattr(le, "firmwarebaseline", "")
        if fwbaseline:
            TBirdCreateLogicalEnclosures.input_select_firmware_baseline(le.firmwarebaseline)
            forceinstall = getattr(le, "forceinstall", "False")
            if forceinstall.lower() == "true":
                TBirdCreateLogicalEnclosures.select_force_install()
        else:
            logger.debug("No Firmware Baseline Specified")

        if add_plus is True:
            TBirdCreateLogicalEnclosures.click_create_plus_button()
        else:
            TBirdCreateLogicalEnclosures.click_create_button()
            TBirdCreateLogicalEnclosures.wait_create_le_dialog_disappear()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        # verify if exist in table list
        TBirdVerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name, timeout=15)
        count += 1

    if TBirdCreateLogicalEnclosures.wait_create_le_dialog_disappear(fail_if_false=False) is False:
        TBirdCreateLogicalEnclosures.click_cancel_button()

        TBirdCreateLogicalEnclosures.wait_create_le_dialog_disappear()

    # basic verification
    for n, le in enumerate(create_le_list):
        # check LE activity
        FusionUIBase.show_activity_sidebar()
        if not TBirdCommonOperationLogicalEnclosures.wait_sidebar_activity_action_ok(le.name, timeout=6000, fail_if_false=False):
            failed += 1
            logger.info("Add LE {0} failed!".format(le.name))
        else:
            logger.info("Add LE {0} successfully".format(le.name))
        FusionUIBase.show_activity_sidebar()

    if count == 0:
        logger.warn("No LE added!")
        logger.warn("Return Value = False")
        return False

    if failed > 0:
        logger.warn("[ %d ] LE added task failed!" % failed)
        logger.warn("Return Value = False")
        return False

    if count != total_len:
        logger.warn("Not able to create all LEs!")
        logger.warn("Return Value = False")
        return False

    logger.debug("Return Value = True")
    return True


def logical_enclosure_firmware_update(le_obj):
    """ Update firmware for logical enclosures
    Arguments:
      name*                     --  Name of Logical Enclosure as a string.
      firmwarebaseline*         --  Firmware baseline to be updated.
      firmwarerange             --  The hardware range to update firmware
      forceinstall              --  If we should force install the firmware
      activationmethod          --  Orchestrated or Parallel

    * Required Arguments

    Example:
        data/LogicalEnclosures/LogicalEnclosuresVerifyFirmware -> @{TestData.LogicalEnclosures.LogicalEnclosuresVerifyFirmware}
        <LogicalEnclosures>
            <LogicalEnclosuresUpdateFirmware>
                <LogicalEnclosure name="LE_SYNERGY" firmwarebaseline="Service Pack for ProLiant version gen9snap6" firmwarerange="Frame link modules only" forceinstall="true">
                    <None/>
                </LogicalEnclosure>
            </LogicalEnclosuresVerifyFirmware>
        </LogicalEnclosures>

    """

    logger.debug("Update firmware for logical enclosures...")
    navigate()

    total_len = len(le_obj)
    update_firmware_list = []
    for n, le in enumerate(le_obj):
        logger.info("--- <firmwares> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("update logical enclosure firmware with name '%s' ..." % le.name)
        CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)

        UpdateFirmware.click_actions_update_firmware()
        UpdateFirmware.wait_update_firmware_dialog_open()

        _update_firmware_operation(le)

        UpdateFirmware.click_ok_button()

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
        if status is True:
            logger.warn("unexpected error occurred: %s" % msg)
            ui_lib.fail_test(msg)

        UpdateFirmware.wait_update_firmware_dialog_closed(timeout=60)

        update_firmware_list.append(le)

    # basic verification
    for n, le in enumerate(update_firmware_list):
        # check LE activity
        FusionUIBase.show_activity_sidebar()
        TBirdCommonOperationLogicalEnclosures.wait_sidebar_activity_action_ok(le.name, timeout=3600)
        FusionUIBase.show_activity_sidebar()
        logger.info("Update LE firmware {0} successfully".format(le.name))

    return True


def select_logical_enclosure(le_name):
    navigate()

    logger.info("Selecting a LE with name '{0}'".format(le_name))
    if VerifyLogicalEnclosures.verify_logical_enclosure_exist(le_name, fail_if_false=False):
        CommonOperationLogicalEnclosures.click_logical_enclosure(le_name)
        CommonOperationLogicalEnclosures.wait_for_le_selected(le_name)
        return True
    else:
        logger.warn("LE '{0}' does not exist".format(le_name))
        ui_lib.get_s2l().capture_page_screenshot()
        return False


def delete_tbird_logical_enclosure(*le_obj):
    """ Delete Logical Enclosure    """
    navigate()

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    logger.debug("Deleting LEs...")

    count = 0
    to_verify = []
    for n, le in enumerate(le_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(le_obj), '-' * 14))
        logger.info("Removing a logical enclosure with name %s" % le.name)
        if not select_logical_enclosure(le.name):
            continue

        TBirdDeleteLogicalEnclosures.select_actions_delete()
        TBirdDeleteLogicalEnclosures.wait_delete_dialog_shown()
        if TBirdDeleteLogicalEnclosures.wait_checkbox_force_remove_logical_enclosure_shown(fail_if_false=False) is True:
            TBirdDeleteLogicalEnclosures.tick_force_remove_logical_enclosure()
        TBirdDeleteLogicalEnclosures.click_yes_delete_button()
        TBirdDeleteLogicalEnclosures.wait_delete_dialog_disappear(timeout=30)
        to_verify.append(le.name)
        count += 1

    if count == 0:
        msg = "no target logical enclosure exists!"
        logger.warn(msg)
        logger.warn("Return Value = False")
        return False

    ret = True
    for n, eg_name in enumerate(to_verify):
        FusionUIBase.show_activity_sidebar()
        if TBirdCommonOperationLogicalEnclosures.wait_sidebar_activity_action_ok(eg_name, timeout=1200, fail_if_false=False) is False:
            ret = False
        FusionUIBase.show_activity_sidebar()

        if TBirdVerifyLogicalEnclosures.verify_logical_enclosure_not_exist(eg_name, fail_if_false=False):
            logger.info("Remove logical enclosure {0} successfully".format(eg_name))
        elif TBirdDeleteLogicalEnclosures.wait_le_show_not_found(eg_name, fail_if_false=False):
            logger.info("Logical enclosure status appear as 'not found', remove logical enclosure {0} successfully.".format(eg_name))
        else:
            msg = "The logical enclosure does not disappear in 10s!"
            logger.warn(msg)
            logger.warn("Return Value = False")
            return False

    if count != len(le_obj):
        logger.warn("Not able to remove all logical enclosures!")
        logger.warn("Return Value = False")
        return False

    if ret is True:
        logger.debug("Return Value = True")
    else:
        logger.warn("Return Value = False")

    return ret


def edit_logical_enclosure(*le_obj):
    """ Edit Logical Enclosure    """
    failed_times = 0
    logger.info("Edit Logical Enclosure")

    navigate()

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:
        if C7000VerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name, 10, False) is False:
            logger.warn("Logical enclosure '%s' does not exist" % le.name)
            failed_times += 1
            continue
        else:
            C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
            # wait target logical enclosure get focus
            logger.info("Wait for logical enclosure %s to be selected." % le.name)

            retry_times = 0
            while retry_times < 3:
                if C7000CommonOperationLogicalEnclosures.verify_logical_enclosure_selected(le.name, 5, False) is False:
                    logger.warn("Failed to select logical enclosure %s, re-trying" % le.name)
                    retry_times += 1
                    C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select logical enclosure %s." % le.name)
                failed_times += 1
                continue

            C7000EditLogicalEnclosures.click_actions_edit()
            C7000EditLogicalEnclosures.wait_edit_logical_enclosure_dialog_shown()

            if hasattr(le, "newname"):
                C7000EditLogicalEnclosures.input_logical_enclosure_name(le.newname)
            if hasattr(le, "script"):
                C7000EditLogicalEnclosures.input_configuration_script(le.script)

            C7000EditLogicalEnclosures.click_ok_button()
            C7000EditLogicalEnclosures.wait_edit_logical_enclosure_dialog_disappear()

    if failed_times > 0:
        logger.warn("Return Value = False")
        return False
    else:
        logger.info("Return Value = True")
        return True


def reapply_logical_enclosure_configuration(*le_obj):
    """ Reapply configuration of Logical Enclosure    """
    failed_times = 0
    logger.info("Reapply configuration of Logical Enclosure")

    navigate()

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:
        if TBirdVerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name, 10, False) is False:
            logger.warn("Logical enclosure '%s' does not exist" % le.name)
            failed_times += 1
            continue
        else:
            C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
            # wait target logical enclosure get focus
            logger.info("Wait for logical enclosure %s to be selected." % le.name)

            retry_times = 0
            while retry_times < 3:
                if C7000CommonOperationLogicalEnclosures.verify_logical_enclosure_selected(le.name, 5, False) is False:
                    logger.warn("Failed to select logical enclosure %s, re-trying" % le.name)
                    retry_times += 1
                    C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select logical enclosure %s." % le.name)
                failed_times += 1
                continue

            C7000ReapplyConfiguration.click_actions_reapply()
            C7000ReapplyConfiguration.wait_reapply_logical_enclosure_dialog_shown()
            C7000ReapplyConfiguration.click_ok_button()
            C7000ReapplyConfiguration.wait_reapply_logical_enclosure_dialog_disappear()
            C7000CommonOperationLogicalEnclosures.wait_activity_action_ok()

    if failed_times > 0:
        logger.warn("Return Value = False")
        return False
    else:
        logger.debug("Return Value = True")
        return True


def logical_enclosure_update_from_group(*le_obj):
    """ Update from Group    """
    failed_times = 0
    logger.info("Update from Group")

    navigate()

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:
        if C7000VerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name, 10, False) is False:
            logger.warn("Logical enclosure '%s' does not exist" % le.name)
            failed_times += 1
            continue
        else:
            C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
            # wait target logical enclosure get focus
            logger.info("Wait for logical enclosure %s to be selected." % le.name)

            retry_times = 0
            while retry_times < 3:
                if C7000CommonOperationLogicalEnclosures.verify_logical_enclosure_selected(le.name, 5, False) is False:
                    logger.warn("Failed to select logical enclosure %s, re-trying" % le.name)
                    retry_times += 1
                    C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select logical enclosure %s." % le.name)
                failed_times += 1
                continue

            if not C7000UpdateFromGroup.verify_and_click_actions_update(5, False):
                logger.warn("Logical enclosure %s doesn't have update button." % le.name)
                failed_times += 1
                continue

            C7000UpdateFromGroup.wait_update_from_group_dialog_shown()
            C7000UpdateFromGroup.click_ok_button()
            C7000UpdateFromGroup.tick_update_prompt_checkbox()
            C7000UpdateFromGroup.click_confirm_button()
            C7000UpdateFromGroup.wait_update_from_group_dialog_disappear()
            FusionUIBase.show_activity_sidebar()
            C7000CommonOperationLogicalEnclosures.wait_sidebar_activity_action_ok(le.name, timeout=3600)

    if failed_times > 0:
        logger.warn("Return Value = False")
        return False
    else:
        logger.debug("Return Value = True")
        return True


def create_logical_enclosure_support_dump(*le_obj):
    """ Create logical enclosure support dump    """
    failed_times = 0
    logger.info("Create logical enclosure support dump")

    navigate()

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:
        if not C7000VerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name, 10, False):
            logger.warn("Logical enclosure '%s' does not exist" % le.name)
            failed_times += 1
            continue
        if C7000VerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name):
            C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
            # wait target logical enclosure get focus
            logger.info("Wait for logical enclosure %s to be selected." % le.name)

            retry_times = 0
            while retry_times < 3:
                if C7000CommonOperationLogicalEnclosures.verify_logical_enclosure_selected(le.name, 5, False) is False:
                    logger.warn("Failed to select logical enclosure %s, re-trying" % le.name)
                    retry_times += 1
                    C7000CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select logical enclosure %s." % le.name)
                failed_times += 1
                continue

            C7000CreateSupportDump.click_actions_create_support_dump()
            C7000CreateSupportDump.wait_create_support_dump_dialog_shown()
            if hasattr(le, "encryption"):
                if le.encryption == "false":
                    C7000CreateSupportDump.tick_disable_encryption()
            C7000CreateSupportDump.click_ok_button()
            C7000CreateSupportDump.wait_create_support_dump_dialog_disappear()
            C7000CommonOperationLogicalEnclosures.wait_activity_action_ok()

    if failed_times > 0:
        logger.warn("Return Value = False")
        return False
    else:
        logger.debug("Return Value = True")
        return True


def verify_logical_enclosure_warn(le_obj):
    """Verify Logical Enclosure Warn"""
    logger.info("Navigate to Logical Enclosure page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_ENCLOSURES)

    for le in le_obj:
        if C7000VerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name, timeout=5, fail_if_false=False) is False:
            logger.warn("logical enclosure '%s' does NOT exist" % le.name)
            return False
        else:
            if C7000CommonOperationLogicalEnclosures.verify_logical_enclosure_warn(le.name, timeout=10, fail_if_false=False) is False:
                le_status = CommonOperationLogicalEnclosures.get_logical_enclosure_status(le.name, fail_if_false=True)
                logger.warn("failed to get 'WARN' status from logical enclosure '%s', got '%s' instead" % (le.name, le_status.upper()))
                return False
            else:
                logger.info("successfully got 'WARN' status from logical enclosure '%s'" % le.name)

    return True


def verify_logical_enclosure_consistency_state(le_obj):
    """Verify consistency of Logical Enclosures"""
    logger.info("Navigate to Logical Enclosure page")
    navigate()
    for le in le_obj:
        CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
        le_consistency_state = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_LE_CONSISTENCY_STATE, FusionLogicalEnclosuresPage.WAIT_TIME)
        logger._log_to_console_and_log_file("LE consistency State is : {}".format(le_consistency_state))
        logger.info("Expected state is: %s" % le.consistency_state)
        ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_CONSISTENCY_STATE % le.consistency_state, fail_if_false=True)


def validate_tbird_logical_enclosure_consistency_state(le_obj):
    """Validate tbird consistency of Logical Enclosures
    Arguments:
      name*                --  Name of Logical Enclosure as a string.
      consistency_state*   --  Consistency state of logical enclosure.
      message              --  The warning message of logical enclosure

    * Required Arguments

    Example:
        data/LogicalEnclosures -> @{TestData.LogicalEnclosures}
        <LogicalEnclosures>
            <le name="LE_SYNERGY"
                consistency_state="Inconsistent with group"
                message="The logical enclosure is inconsistent with its enclosure group %s."
                eg="EG_SYNERGY" />
        </LogicalEnclosures>

    """
    logger.info("Validate logical enclosure consistent state")
    navigate()

    not_exist = 0
    for le in le_obj:
        if not TBirdVerifyLogicalEnclosures.verify_logical_enclosure_exist(le.name, 10, False):
            logger.warn("The [ logical enclosure %s ] is not exists." % le.name)
            not_exist += 1
            continue

        TBirdCommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
        TBirdCommonOperationLogicalEnclosures.wait_for_le_selected(le.name)

        TBirdVerifyLogicalEnclosures.verify_logical_enclosure_consistency_state(le.consistency_state)

        if hasattr(le, "message") and hasattr(le, "eg"):
            expect_value = le.message % le.eg
            TBirdVerifyLogicalEnclosures.verify_logical_enclosure_warning_message(expect_value)

    return True if not not_exist else False


def validate_logical_enclosure_firmware(le_obj):
    """Validate Logical Enclosure Firmware
    Arguments:
      name*             --  Name of Logical Enclosure as a string.
      Firmwares*        --  Firmware list to be verified.

    * Required Arguments

    Example:
        data/LogicalEnclosures/LogicalEnclosuresVerifyFirmware -> @{TestData.LogicalEnclosures.LogicalEnclosuresVerifyFirmware}
        <LogicalEnclosures>
            <LogicalEnclosuresVerifyFirmware>
                <LogicalEnclosure name="LE_SYNERGY">
                    <Firmwares>
                        <firmware type="server" server_name="CN754404R6, bay 1" name="System ROM" installed="I37 v2.20 (05/13/2016)"/>
                        <firmware type="em" name="CN754404R6,frame link module 1" installed="1.01.00"/>
                        <firmware type="enclosure" name="CN754404R6" baseline="not set"/>
                    </Firmwares>
                </LogicalEnclosure>
            </LogicalEnclosuresVerifyFirmware>
        </LogicalEnclosures>

    """
    logger.info("Validate Logical Enclosure Firmware...")
    navigate()
    fail_count = 0
    for le in le_obj:
        logger.info("verifying logical enclosure firmware with name '%s' ..." % le.name)
        CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
        FusionUIBase.select_view_by_name("Firmware")
        VerifyLogicalEnclosures.click_expand_firmware_detail_button()

        firmwares = le.Firmwares
        total = len(firmwares)
        failed = 0
        verified = 0

        for n, firmware in enumerate(firmwares):
            logger.info("--- <firmwares> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
            logger.info("verifying a firmware component with name '%s' ..." % firmware.name)
            firmware_type = getattr(firmware, "type", "server")
            verify = False

            if firmware_type.lower() == "server":
                server_uri = VerifyLogicalEnclosures.get_server_hardware_uri_by_name(firmware.server_name, timeout=10)
                uri_split = server_uri.split("/")
                if hasattr(firmware, 'installed'):
                    if VerifyLogicalEnclosures.verify_server_firmware_installed(uri_split[-1], firmware.name, firmware.installed):
                        verify = True
                    else:
                        logger.warn("firmware verify failed")
                        failed += 1
                if hasattr(firmware, 'baseline'):
                    if VerifyLogicalEnclosures.verify_server_firmware_baseline(uri_split[-1], firmware.name, firmware.baseline):
                        verify = True
                    else:
                        logger.warn("firmware verify failed")
                        failed += 1
            else:
                if hasattr(firmware, 'installed'):
                    if VerifyLogicalEnclosures.verify_common_firmware_installed(firmware.name, firmware.installed):
                        verify = True
                    else:
                        logger.warn("firmware verify failed")
                        failed += 1
                if hasattr(firmware, 'baseline'):
                    if VerifyLogicalEnclosures.verify_common_firmware_baseline(firmware.name, firmware.baseline):
                        verify = True
                    else:
                        logger.warn("firmware verify failed")
                        failed += 1

            if verify is True:
                verified += 1

        if failed > 0:
            logger.warn("%d firmware component verify failed!" % failed)
            fail_count += 1
        if total > verified:
            logger.warn("only %d firmware component was verified!" % verified)
            fail_count += 1

    if fail_count > 0:
        ui_lib.fail_test("%d logical enclosures firmware verify failed!" % fail_count)

    return True


def validate_logical_enclosure_firmware_when_updating_firmware(le_obj):
    """ Validate Logical Enclosure Firmware When Updating firmware for logical enclosures
    Arguments:
      name*                     --  Name of Logical Enclosure as a string.
      Firmwares*                --  Firmware list to be verified.
      firmwarebaseline*         --  Firmware baseline to be updated.
      firmwarerange             --  The hardware range to update firmware
      forceinstall              --  If we should force install the firmware
      activationmethod          --  Orchestrated or Parallel

    * Required Arguments

    Example:
        data/LogicalEnclosures/LogicalEnclosuresVerifyFirmware -> @{TestData.LogicalEnclosures.LogicalEnclosuresVerifyFirmware}
        <LogicalEnclosures>
            <LogicalEnclosuresUpdateFirmware>
                <LogicalEnclosure name="LE_SYNERGY" firmwarebaseline="Service Pack for ProLiant version gen9snap6" firmwarerange="Frame link modules only" forceinstall="true">
                    <Firmwares>
                        <firmware type="server" server_name="CN754404R6, bay 1" name="System ROM" installed="I37 v2.20 (05/13/2016)"/>
                        <firmware type="em" name="CN754404R6,frame link module 1" installed="1.01.00"/>
                        <firmware type="enclosure" name="CN754404R6" baseline="not set"/>
                    </Firmwares>
                </LogicalEnclosure>
            </LogicalEnclosuresVerifyFirmware>
        </LogicalEnclosures>

    """

    logger.debug("Update firmware for logical enclosures...")
    navigate()
    fail_count = 0

    for n, le in enumerate(le_obj):
        logger.info("update logical enclosure firmware with name '%s' ..." % le.name)
        CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
        UpdateFirmware.click_actions_update_firmware()
        UpdateFirmware.wait_update_firmware_dialog_open()

        _update_firmware_operation(le)

        UpdateFirmware.click_expand_all_link()

        firmwares = le.Firmwares
        total = len(firmwares)
        failed = 0
        verified = 0

        for n, firmware in enumerate(firmwares):
            logger.info("--- <firmwares> ---: {2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
            logger.info("verifying a firmware component with name '%s' ..." % firmware.name)
            firmware_type = getattr(firmware, "type", "server")
            verify = False

            if firmware_type.lower() == "server":
                server_uri = VerifyLogicalEnclosures.get_server_hardware_uri_by_name_when_update_firmware(firmware.server_name, timeout=10)
                uri_split = server_uri.split("/")
                if hasattr(firmware, 'installed'):
                    if VerifyLogicalEnclosures.verify_server_firmware_installed_when_update_firmware(uri_split[-1], firmware.name, firmware.installed):
                        verify = True
                    else:
                        failed += 1
                if hasattr(firmware, 'baseline'):
                    if VerifyLogicalEnclosures.verify_server_firmware_baseline_when_update_firmware(uri_split[-1], firmware.name, firmware.baseline):
                        verify = True
                    else:
                        failed += 1
            else:
                if hasattr(firmware, 'installed'):
                    if VerifyLogicalEnclosures.verify_common_firmware_installed_when_update_firmware(firmware.name, firmware.installed):
                        verify = True
                    else:
                        failed += 1
                if hasattr(firmware, 'baseline'):
                    if VerifyLogicalEnclosures.verify_common_firmware_baseline_when_update_firmware(firmware.name, firmware.baseline):
                        verify = True
                    else:
                        failed += 1

            if verify is True:
                verified += 1

        if failed > 0:
            logger.warn("%d firmware component verify failed!" % failed)
            fail_count += 1
        if total > verified:
            logger.warn("only %d firmware component was verified!" % verified)
            fail_count += 1

        UpdateFirmware.click_cancel_button()
        UpdateFirmware.wait_update_firmware_dialog_closed(timeout=60)

    if fail_count > 0:
        ui_lib.fail_test("%d logical enclosures firmware verify failed!" % fail_count)

    return True


def _update_firmware_operation(le):
    """Page operation for update logical enclosure firmware"""

    UpdateFirmware.select_firmware_baseline(le.firmwarebaseline)

    firmware_range = getattr(le, "firmwarerange", "")
    if firmware_range:
        UpdateFirmware.select_firmware_update_for(firmware_range)
    else:
        logger.debug("No Update firmware for Specified")

    if getattr(le, "forceinstall", "False").lower() == "true":
        UpdateFirmware.select_force_install()
    else:
        logger.debug("Update firmware without force install")
    activation_method = getattr(le, "activationmethod", "")
    if activation_method:
        UpdateFirmware.select_li_activation_method(activation_method)
    else:
        logger.debug("No Logical interconnect activation type Specified")


def delete_logical_enclosure(*le_obj):
    """ Delete Logical Enclosures
    Returns true if delete is successful without errors else returns the error string
    """

    error = 0
    error_string = ''
    error_status = False
    logger._log_to_console_and_log_file("\n*** Delete Logical Enclosures ***")
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:

        logger._log_to_console_and_log_file("Deleting Logical Enclosure :  %s" % le.name)
        ui_lib.refresh_browser(FusionLogicalEnclosuresPage.ID_PAGE_LABEL, FusionLogicalEnclosuresPage.WAIT_TIME)

        if not ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_NAME % le.name):
            logger._warn("Logical Enclosure '{}' does not exist".format(le.name))
            continue

        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_ACTION_MAIN_BTN, FusionLogicalEnclosuresPage.WAIT_TIME):
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTION_MAIN_BTN)
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_DELETE_BTN):
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_DELETE_BTN)
            else:
                logger._warn("Delete Option is not seen in drop down in UI !! User may not have delete privilege\n")
                error += 1
                error_string += "Delete Option is not seen in drop down in UI !! User may not have delete privilege.\t"
                break
        else:
            logger._warn("Actions Button is not seen in UI !! User may not have delete privilege\n")
            error += 1
            error_string += "Actions Button is not seen in UI !! User may not have delete privilege.\t"
            break

        # check for delete warning - seen if the resource is in hosting other entities
        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_DELETE_ERROR, FusionLogicalEnclosuresPage.WAIT_TIME):
            delete_warning = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_DELETE_WARNING)
            logger._warn("Following Delete Warning Seen : '{}'".format(delete_warning))
            logger._warn("Unable to delete LE : {}".format(le.name))
            error += 1
            error_string += "Following Delete Warning Seen : '{}'\t".format(delete_warning)
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LE_DELETE_CANCEL)
            continue

        # if Force delete is seen log it and select the checkbox
        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_FORCE_DELETE):
            logger._log_to_console_and_log_file("--Selecting 'Force delete Logical Enclosure'")
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LE_FORCE_DELETE)

        # proceed with delete
        ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_DELETE_CONFIRMATION, FusionLogicalEnclosuresPage.WAIT_TIME)
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_DELETE_CONFIRMATION)

        # check if any error is seen on clicking delete
        error_status = ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_DELETE_HP_STATUS_ERROR)
        if error_status:
            logger._warn("Error seen during DELETE!!")
            logger._warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_DELETE_FORM_MESSAGE_SUMMARY)))
            logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_DELETE_FORM_MESSAGE_DETAILS)))
            error += 1
            error_string += ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_DELETE_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_DELETE_FORM_MESSAGE_DETAILS) + "\t"
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LE_DELETE_CANCEL)
            continue

        # wait for the delete operation to complete
        timeout = 1
        while timeout <= FusionLogicalEnclosuresPage.TIMEOUT:
            logger._log_to_console_and_log_file("Deletion in progress...")
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_COMPLETE, FusionLogicalEnclosuresPage.DELETE_LE_TIME):
                logger._log_to_console_and_log_file("Deletion Completed.")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_ERROR, FusionLogicalEnclosuresPage.DELETE_LE_TIME):
                # if error is seen during delete log it
                logger._warn("--Error during Deletion")
                error += 1
                error_string += "--Error during Deletion\t"
                break
            timeout += (FusionLogicalEnclosuresPage.DELETE_LE_TIME * 2) / 60.0

        # refresh browser
        ui_lib.refresh_browser(FusionLogicalEnclosuresPage.ID_PAGE_LABEL, FusionLogicalEnclosuresPage.WAIT_TIME)

        # check if the LE is still seen or not
        # if LE has not been delete try force deleting again
        if ui_lib.wait_for_element_notvisible(FusionLogicalEnclosuresPage.XPATH_LE_NAME % le.name, FusionLogicalEnclosuresPage.WAIT_TIME):
            logger._log_to_console_and_log_file("Logical Enclosure '{}' is deleted successfully".format(le.name))
        else:
            logger._warn("Logical Enclosure '{}' has not been deleted and is still visible in UI.".format(le.name))
            if _force_delete_le(le.name):
                logger._log_to_console_and_log_file("LE deleted successfully.")
            else:
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_NAME % le.name, FusionLogicalEnclosuresPage.WAIT_TIME):
                    logger._warn("Logical Enclosure '{}' has not been deleted and is visible in the table even after waiting for {} minutes for task completion" .format(le.name, timeout))
                    error += 1
                    error_string += "Logical Enclosure '{}' has not been deleted and is visible in the table even after waiting for {} minutes for task completion\t" .format(le.name, timeout)

    # return error string if error is seen else return true
    if error > 0:
        logger._warn("\n*** Deletion Completed with errors ***")
        return error_string
    else:
        logger._log_to_console_and_log_file("\n*** Deletion Completed Successfully ***")
        return True


def _force_delete_le(le_name):
    '''
    function to force delete LE
    '''
    # if no error has occurred until now , try deleting the LE again selecting Force delete
    logger._log_to_console_and_log_file("--Trying Force delete")
    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTION_MAIN_BTN)
    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_DELETE_BTN, FusionLogicalEnclosuresPage.WAIT_TIME)
    # if Force delete is seen log it and select the checkbox
    if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_FORCE_DELETE):
        logger._log_to_console_and_log_file("--Selecting 'Force delete Logical Enclosure'")
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LE_FORCE_DELETE)
    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_DELETE_CONFIRMATION, FusionLogicalEnclosuresPage.WAIT_TIME)

    # wait for the delete operation to complete
    timeout = 1
    while timeout <= FusionLogicalEnclosuresPage.TIMEOUT:
        logger._log_to_console_and_log_file("Deletion in progress...")
        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_COMPLETE, FusionLogicalEnclosuresPage.DELETE_LE_TIME):
            logger._log_to_console_and_log_file("Deletion Completed.")
            return True
        elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_ERROR, FusionLogicalEnclosuresPage.DELETE_LE_TIME):
            # if error is seen during delete log it
            logger._warn("--Error during Deletion")
            return False
        timeout += FusionLogicalEnclosuresPage.DELETE_LE_TIME / 60.0
    return False


def update_tbird_logical_enclosure_firmware_new(*firmware_obj):
    '''
    Function to update TBIRD LE firmware
    Returns an error string if any error is seen during update
    else returns true

    DATAFILE EXAMPLE :
        <firmware1 bundle="Hafnium 166 Chloride 106 Carbon 22 2016 07 08 version 2016.07.08.66" upgradefor="Shared infrastructure"
                forceinstall="no" activationtype="parallel" lename="TestLE" unmanagedic="No"
                appip="10.10.0.91"  appuname="root" appasswd="hpvse1" dcs="False" proceedonwarning='yes'
                expectedicfwversion = "k:1.0.0.166,cl10:1.05,cl20:1.05">

            <enclosure name="WPSTENC100" emip="fe80::1658:d0ff:fe41:4330%bond0,fe80::1658:d0ff:fe41:43e0%bond0" />
        </firmware1>

    attributes:
        bundle*            - Firmware bundle to use for update
        upgradefor*        - upgrade FW for shared infra,shared infra and profiles or em only
        forceinstall      - Yes or No
        activationtype    - orchestrated or parallel | default is orchestrated
        lename *           - le name to perform update on
        unmanagedic       - Yes or No
        appip*             - appliance IP (CIM IP)
        appuname*          - appliance user name
        appasswd*          - appliance password
        dcs               - True or False
        proceedonwarning  - yes or No
        expectedicfwversion* - expected versions of the ICMs as a comma separated string like 'k:1.0.167,cl10:1.05'

        <enclosure>*
            name*            - enclosure name as displayed
            emip*            - em ipv6 IPs , both the active and standby as a comma separated string , with the interface used in CIM mentioned

        * required attributes
    '''
    failed_times = 0
    error_string = ''
    errors_on_form = ''
    navigate()

    logger.info("TBIRD Logical Enclosure firmware Upgrade")
    for fw in firmware_obj:
        if not VerifyLogicalEnclosures.verify_logical_enclosure_exist(fw.lename, 10, False):
            logger.warn("Logical enclosure '%s' does not exist" % fw.lename)
            failed_times += 1
            continue
        if VerifyLogicalEnclosures.verify_logical_enclosure_exist(fw.lename):
            TBirdCommonOperationLogicalEnclosures.click_logical_enclosure(fw.lename)
            # wait target logical enclosure get focus
        if not TBirdVerifyLogicalEnclosures.verify_le_consistency_state('consistent', 10):
            ui_lib.fail_test("The state of %s is not Consistent" % fw.lename)
        if TBirdVerifyLogicalEnclosures.verify_action_button_exists():
            TBirdUpdateFirmware.click_actions()
            if TBirdVerifyLogicalEnclosures.verify_updatefirmware_button_exists():
                TBirdUpdateFirmware.click_update_firmware()
            else:
                error_string += "Update Firmware Option not seen in actions menu.User may not have Update Firmware privilege\t"
                return error_string
        else:
            error_string += "Actions button not seen.User may not have privilege\t"
            return error_string

        ''' Select the firmware bundle to be used for FW upgrade '''
        TBirdUpdateFirmware.input_select_update_firmware_baseline(fw.bundle)
        TBirdUpdateFirmware.input_select_update_option()
        TBirdUpdateFirmware.input_select_update_for(fw.upgradefor)
        ''' Select unmanaged interconnects if check box is visible,Check box visible only if h/w has Unamanged ICMs'''
        if (fw.has_property('unmanagedic')):
            if fw.unmanagedic == 'yes':
                TBirdUpdateFirmware.tick_unmanaged_checkbox()
            else:
                TBirdUpdateFirmware.untick_unmanaged_checkbox()

        if (fw.has_property('forceinstall')):
            if fw.forceinstall == "yes":
                TBirdUpdateFirmware.tick_forceinstall_checkbox()
                ''' Check the warning message displayed '''
                if not TBirdVerifyLogicalEnclosures.verify_force_install_warning(10, False):
                    ui_lib.fail_test("Expected message not seen for Force Option")

        if (fw.has_property('activationtype')):
            TBirdUpdateFirmware.input_select_activate_type(fw.activationtype)
            if fw.activationtype == "parallel":
                if not TBirdVerifyLogicalEnclosures.verify_parallel_activation_warning(timeout=10):
                    ui_lib.fail_test("Expected error message not seen for parallel mode selection")
            else:
                if not TBirdVerifyLogicalEnclosures.verify_orchestrated_activation_warning(timeout=10):
                    ui_lib.fail_test("Expected error message not seen for Orchestrated mode selected")

        TBirdUpdateFirmware.click_ok_button()
        if not TBirdVerifyLogicalEnclosures.verify_update_form_not_visible(timeout=15):
            status, errors_on_form = TBirdUpdateFirmware.get_errors_on_firmwareupdate_dialog()

        if errors_on_form:
            logger.warn("unexpected error occurred")
            error_string += error_string + str(errors_on_form)
            failed_times += 1
            # if form is still seen click cancel
            if not TBirdVerifyLogicalEnclosures.verify_update_form_not_visible(timeout=15):
                TBirdUpdateFirmware.click_cancel_button()
            continue
        else:
            logger.info("- No errors Seen")
        timeout = 1
        firmware_update_timeout = FusionUIConst.CONST_FW_UPDATE_TIMEOUT
        firmware_update_logging_time = FusionUIConst.CONST_FW_UPDATE_LOGGING_TIME
        while timeout <= firmware_update_timeout:
            logger.info("FW Update in progress")
            # log step in progress
            if TBirdVerifyLogicalEnclosures.wait_firmware_update_step(timeout=15):
                text = TBirdUpdateFirmware.get_firmware_update_step(timeout=firmware_update_timeout)
                logger.info("Step in progress : %s" % text)
            if TBirdVerifyLogicalEnclosures.wait_firmware_update_complete(timeout=15):
                logger.info("FW Upgrade Completed.")
                break
            elif TBirdVerifyLogicalEnclosures.wait_firmware_update_warning(timeout=15):
                logger.warn("FW Upgrade Completed but with warning")
                break
            elif TBirdVerifyLogicalEnclosures.wait_firmware_update_error(timeout=15):
                logger.warn("--Error during FW Upgrade")
                failed_times += 1
                error_string += "--Error during FW Upgrade\t"
                break
            timeout += (firmware_update_logging_time * 3) / 60.0
        if timeout > firmware_update_timeout:
            logger.warn("Either FW Upgrade of LE '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!".format(fw.lename, timeout))
            failed_times += 1
            error_string += "Either FW Upgrade of LE '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!\t".format(fw.lename, timeout)
            # if add Form is still seen click cancel

            if not TBirdVerifyLogicalEnclosures.verify_update_form_not_visible(timeout=15):
                TBirdUpdateFirmware.click_cancel_button()
    # return error string if error is seen else return true
    if failed_times > 0:
        return error_string

    logger.info("\n*** FW Upgrade Completed Successfully ***")
    return True


def update_tbird_logical_enclosure_firmware(*firmware_obj):
    '''
    Function to update TBIRD LE firmware
    Returns an error string if any error is seen during update
    else returns true
    '''
    logger.info("****TBIRD Logical Enclosure firmware Upgrade ****")

    error = 0
    error_string = ''
    error_status = ''
    errors_on_form = ''
    upgradefor = ''
    # if not in LE page navigate
    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(firmware_obj, test_data.DataObj):
        firmware_obj = [firmware_obj]
    elif isinstance(firmware_obj, tuple):
        firmware_obj = list(firmware_obj[0])

    for fw in firmware_obj:
        logger.info("*** Starting Firmware Upgrade Activity for LE '{}' ***".format(fw.lename))
        # check if the LE is present
        if not select_logicalenclosure(fw.lename):
            logger.warn("Unable to select Logical Enclosure '%s'.It may not be present" % fw.lename)
            error += 1
            error_string += "Unable to select Logical Enclosure '%s'.It may not be present\t" % fw.lename
            continue

        ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_LE_DETAILS, FusionLogicalEnclosuresPage.WAIT_TIME)
        # got to LE overview
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_MENU_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.LINK_OVERVIEW)

        # verify LE state is Consistent - IF Inconsistent throw a warning
        le_consistency_state = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_LE_CONSISTENCY_STATE, FusionLogicalEnclosuresPage.WAIT_TIME)
        logger.info("LE consistency State is : {}".format(le_consistency_state))
        if le_consistency_state.lower() != 'consistent':
            logger.warn("LE consistency State is : {} , but should be : 'Consistent'. FW update Might fail".format(le_consistency_state))

        # click FW upgrade from actions menu - Report error if user has no privileges
        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_ACTION_MAIN_BTN, FusionLogicalEnclosuresPage.WAIT_TIME):
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTION_MAIN_BTN)
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FIRMWARE_UPGRADE, FusionLogicalEnclosuresPage.WAIT_TIME):
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FIRMWARE_UPGRADE)
            else:
                logger.warn("Update Firmware Option not seen in actions menu.User may not have Update Firmware privilege")
                error += 1
                error_string += "Update Firmware Option not seen in actions menu.User may not have Update Firmware privilege\t"
                return error_string
        else:
            logger.warn("Actions button not seen.User may not have privilege")
            error += 1
            error_string += "Actions button not seen.User may not have privilege\t"
            return error_string

        ''' Select the firmware bundle to be used for FW upgrade '''
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FIRMWARE_DROPDOWN)
        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_SELECT_FROM_DROPDOWN % fw.bundle):
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_SELECT_FROM_DROPDOWN % fw.bundle)
            logger.info("Selected FW bundle - {}".format(fw.bundle))
        else:
            logger.warn("Firmware Bundle '{}' not seen in dropdown.Canceling Upgrade".format(fw.bundle))
            error += 1
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
            continue

        ''' Select the update mode '''
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_UPGRADE_FOR_DROPDOWN)
        if fw.upgradefor.lower() == "shared infrastructure":
            upgradefor = "Shared infrastructure"
        elif fw.upgradefor.lower() == "shared infrastructure and profiles":
            upgradefor = "Shared infrastructure and profiles"
        elif fw.upgradefor.lower() == "frame link modules only":
            upgradefor = "Frame link modules only"
        else:
            logger.warn("Invalid upgrade for option - '{}'.Clicking Cancel".format(upgradefor))
            error += 1
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
            continue

        # select upgrade mode
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_SELECT_FROM_DROPDOWN % fw.upgradefor)
        logger.warn("Selected Upgrade Mode - {}".format(upgradefor))

        ''' Select  unmanaged interconnects if checkbox is visible'''
        if (fw.has_property('unmanagedic') and ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_UNMANAGED_INTERCONNECT_CHECKBOX, FusionLogicalEnclosuresPage.WAIT_TIME)):
            if fw.unmanagedic == 'yes':
                ui_lib.wait_for_checkbox_and_select(FusionLogicalEnclosuresPage.ID_UNMANAGED_INTERCONNECT_CHECKBOX)
                logger.info("Selecting Unmanaged IC checkbox")
            else:
                ui_lib.wait_for_checkbox_and_unselect(FusionLogicalEnclosuresPage.ID_UNMANAGED_INTERCONNECT_CHECKBOX)
                logger._log_to_console_and_log_file("De-Selecting UnManaged IC checkbox")

        ''' Select Force install as per input, check for warning message '''
        if (fw.has_property('forceinstall')):
            # warning_text = "Downgrading the firmware can result in the installation of unsupported firmware and cause hardware to cease operation."
            if fw.forceinstall == "yes":
                logger._log_to_console_and_log_file("Selecting Force Install")
                ui_lib.wait_for_checkbox_and_select(FusionLogicalEnclosuresPage.ID_FORCE_INSTALL)
                logger._log_to_console_and_log_file("Selecting Force Install")
                ''' Check the warning message displayed '''
                if not ui_lib.wait_for_element_text(FusionLogicalEnclosuresPage.ID_FORCE_INSTALL_WARNING, FusionLogicalEnclosuresPage.FW_DOWNGRADE_WARNING_MSG):
                    logger._warn("Following Warning message for force install is not displayed - ")
                    error += 1
                    error_string += "Following Warning message for force install is not displayed - {}\t".format(FusionLogicalEnclosuresPage.FW_DOWNGRADE_WARNING_MSG)
                else:
                    logger._log_to_console_and_log_file("Following Warning message displayed as expected for force install - ")
                logger._log_to_console_and_log_file(FusionLogicalEnclosuresPage.FW_DOWNGRADE_WARNING_MSG)

        ''' Select activation type , check for warning message '''
        if (fw.has_property('activationtype') and ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_ACTIVATION_CONTENT, FusionLogicalEnclosuresPage.WAIT_TIME)):
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTIVATION_TYPE % fw.activationtype)
            logger._log_to_console_and_log_file("Selecting Activation Type - {}".format(fw.activationtype))
            if fw.activationtype == "parallel":
                warning_text = FusionLogicalEnclosuresPage.PARALLEL_ACTIVATION_WARNING_MSG
                locator = FusionLogicalEnclosuresPage.ID_PARALLEL_WARNING
            else:
                warning_text = FusionLogicalEnclosuresPage.ORCHASTRATED_ACTIVATION_WARNING_MSG
                locator = FusionLogicalEnclosuresPage.ID_ORCHESTRATED_WARNING
            if not ui_lib.wait_for_element_text(locator, warning_text):
                logger._warn("Following Warning message for activation type '{}' is not displayed - '{}'".format(fw.activationtype, warning_text))
                error += 1
                error_string += "Following Warning message for activation type '{}' is not displayed - '{}'\t".format(fw.activationtype, warning_text)
            else:
                logger._log_to_console_and_log_file("Following Warning message for activation type '{}' displayed as expected - '{}'".format(fw.activationtype, warning_text))

        # click OK to begin firmware update
        logger._log_to_console_and_log_file("Clicking OK")
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FIRMWARE_UPDATE_OK)

        ''' Check for error status and error messages on form on the same page '''
        # check for errors after clicking create button - check Error status as well
        logger._log_to_console_and_log_file("Checking For errors - if any - After clicking on OK Button")
        # get errors if the form is still visible
        if not ui_lib.wait_for_element_notvisible(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM, FusionLogicalEnclosuresPage.WAIT_TIME):
            errors_on_form = base_page.get_errors_on_form(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM)
            error_status = ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_HP_STATUS_ERROR, FusionLogicalEnclosuresPage.WAIT_TIME)
        if error_status or errors_on_form:
            error += 1
            if errors_on_form:
                error_string += errors_on_form + "\t"
            if error_status:
                logger._warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY)))
                logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS)))
                error_string += ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS) + "\t"
            # if form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
            continue
        else:
            logger._log_to_console_and_log_file("- No errors Seen")

        # wait for FW upgrade operation to complete
        timeout = 1
        while timeout <= FusionLogicalEnclosuresPage.FW_UPGRADE_TIMEOUT:
            logger._log_to_console_and_log_file("FW Update in progress...")
            # log step in progress
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STEP, 10):
                logger._log_to_console_and_log_file("Step in progress : {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_UPDATE_STEP)))

            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_COMPLETE, FusionLogicalEnclosuresPage.FW_UPGRADE_TIME):
                logger._log_to_console_and_log_file("FW Upgrade Completed.")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_WARNING, FusionLogicalEnclosuresPage.FW_UPGRADE_TIME):
                logger._warn("FW Upgrade Completed but with warning")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_ERROR, FusionLogicalEnclosuresPage.FW_UPGRADE_TIME):
                logger._warn("--Error during FW Upgrade")
                error += 1
                error_string += "--Error during FW Upgrade\t"
                break
            timeout += (FusionLogicalEnclosuresPage.FW_UPGRADE_TIME * 3) / 60.0

        if timeout > FusionLogicalEnclosuresPage.FW_UPGRADE_TIMEOUT:
            logger._warn("Either FW Upgrade of LE '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!".format(fw.lename, timeout))
            error += 1
            error_string += "Either FW Upgrade of LE '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!\t".format(fw.lename, timeout)
            # if add form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)

    # return error string if error is seen else return true
    if error > 0:
        logger._warn("\n*** FW Upgrade Completed with errors ***")
        return error_string

    logger._log_to_console_and_log_file("\n*** FW Upgrade Completed Successfully ***")
    return True


def select_logicalenclosure(le_name):
    """ Select Switch
        Example:
        | `Select Switch`      |     |
    """
    navigate()
    if ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LE_NAME % le_name):
        ui_lib.wait_for_element_visible("xpath=//h1[@id='cic-logicalenclosure-details-title' and (text()='%s')]" % le_name)
        logger._log_to_console_and_log_file("The  Logical Enclosure '%s' is selected " % le_name)
        return True
    else:
        logger._log_to_console_and_log_file("The  Logical Enclosure '%s' is not present" % le_name)
        return False


def create_logical_enclosure(*le_obj):
    """ Create Logical Enclosures
    Returns true is creation is successful without errors else returns the error string
    """
    error = 0
    error_string = ''
    error_status = False
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:

        logger._log_to_console_and_log_file("Creating Logical Enclosure with name %s" % le.name)
        ui_lib.refresh_browser(FusionLogicalEnclosuresPage.ID_PAGE_LABEL, FusionLogicalEnclosuresPage.WAIT_TIME)

        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_NAME % le.name):
            logger._warn("Logical Enclosure '%s' is already present" % le.name)
            continue

        # check for privilege
        if not ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LINK_CREATE_LOGICAL_ENCLOSURES):
            logger._warn("Create Logical Enclosure Button is not seen in UI!! User may not have create privilege.")
            error += 1
            error_string += "Create Logical Enclosure Button is not seen in UI!! User may not have create privilege.\t"
            break

        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LINK_CREATE_LOGICAL_ENCLOSURES)
        ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_INPUT_LE_NAME)

        # Providing Input
        ui_lib.wait_for_element_and_input_text(FusionLogicalEnclosuresPage.ID_INPUT_LE_NAME, le.name)

        # if Enclosures are not specified Skip creation
        if not hasattr(le, 'enclosure'):
            logger._warn("Enclosures not specified !! Skipping creation !! Check Input")
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_BTN_LE_ADD_CANCEL)
            continue

        # click on the drop down
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ENCLOSURE_SELECT_DROPDOWN)

        # if the input is not seen in drop down skip creation
        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_INPUT_LE_ENCLOSURE_SELECT % str(le.enclosure).strip(), FusionLogicalEnclosuresPage.WAIT_TIME):
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_INPUT_LE_ENCLOSURE_SELECT % str(le.enclosure).strip())
        else:
            logger._warn("Enclosure  option {} not seen in dropdown.Skipping creation".format(str(le.enclosure).strip()))
            error += 1
            error_string += "Enclosure  option {} not seen in dropdown.Skipping creation".format(str(le.enclosure).strip())
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_BTN_LE_ADD_CANCEL)
            continue

        # if Enclosure Group is  not specified Skip creation
        if not hasattr(le, 'enclosuregroup'):
            logger._warn("Enclosure Group not specified !! Skipping creation !! Check Input")
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_BTN_LE_ADD_CANCEL)
            continue

        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_INPUT_EG_SELECT_DROPDOWN)
        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_INPUT_EG_SELECT % str(le.enclosuregroup).strip(), FusionLogicalEnclosuresPage.WAIT_TIME):
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_INPUT_EG_SELECT % str(le.enclosuregroup).strip())
        else:
            logger._warn("Enclosure Group option {} not seen in dropdown.Skipping creation".format(str(le.enclosuregroup).strip()))
            error += 1
            error_string += "Enclosure Group option {} not seen in dropdown.Skipping creation".format(str(le.enclosuregroup).strip())
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_BTN_LE_ADD_CANCEL)
            continue

        # select firmware baseline if specified
        if hasattr(le, 'firmwarebaseline'):
            if le.firmwarebaseline.strip() is not '':
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.XPATH_FIRMWARE_BASELINE_DROPDOWN, FusionLogicalEnclosuresPage.WAIT_TIME)
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_FIRMWARE_BASELINE_OPTIONS % str(le.firmwarebaseline).strip(), FusionLogicalEnclosuresPage.WAIT_TIME):
                    logger._log_to_console_and_log_file("Selecting Firmware Baseline : {}".format(str(le.firmwarebaseline).strip()))
                    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.XPATH_FIRMWARE_BASELINE_OPTIONS % str(le.firmwarebaseline).strip(), FusionLogicalEnclosuresPage.WAIT_TIME)

                    # select force installation according to input
                    if hasattr(le, "forceinstallation"):
                        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FIRMWARE_FORCE_INSTALL):
                            if le.forceinstallation.lower() == "true":
                                logger._log_to_console_and_log_file("Selecting 'Force Install")
                                ui_lib.wait_for_checkbox_and_select(FusionLogicalEnclosuresPage.ID_FIRMWARE_FORCE_INSTALL, FusionLogicalEnclosuresPage.WAIT_TIME)
                            else:
                                logger._log_to_console_and_log_file("Unchecking 'Force Install'")
                                ui_lib.wait_for_checkbox_and_unselect(FusionLogicalEnclosuresPage.ID_FIRMWARE_FORCE_INSTALL, FusionLogicalEnclosuresPage.WAIT_TIME)
                        else:
                            logger._warn("'Force install'  checkbox is not seen in UI")
                            error += 1
                            error_string += "'Force install' checkbox is not seen in UI\t"
                else:
                    logger._warn("Firmware Baseline option '{}' not seen in dropdown!!".format(str(le.firmwarebaseline).strip()))
                    error += 1
                    error_string += "Firmware Baseline option '{}' not seen in dropdown!!\t".format(str(le.firmwarebaseline).strip())
        else:
            logger._log_to_console_and_log_file("No Firmware Baseline Specified")

        # check for errors before clicking create button
        errors_on_form = base_page.get_errors_on_form(FusionLogicalEnclosuresPage.LE_ADD_FORM)
        if errors_on_form:
            error += 1
            error_string += errors_on_form + "\t"
            logger._log_to_console_and_log_file("Clicking Cancel")
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_BTN_LE_ADD_CANCEL)
            continue
        else:
            logger._log_to_console_and_log_file("- No errors Seen")

        # click create
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LE_CREATE_BTN)

        # check for errors after clicking create button - check status as well
        logger._log_to_console_and_log_file("Checking For errors - if any - After clicking on Create Button")
        # get errors if the form is still visible
        if not ui_lib.wait_for_element_notvisible(FusionLogicalEnclosuresPage.ID_LE_ADD_FORM, FusionLogicalEnclosuresPage.WAIT_TIME):
            errors_on_form = base_page.get_errors_on_form(FusionLogicalEnclosuresPage.LE_ADD_FORM)
            error_status = ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_ADD_HP_STATUS_ERROR)
        if error_status or errors_on_form:
            error += 1
            if errors_on_form:
                error_string += errors_on_form + "\t"
            if error_status:
                logger._warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_ADD_FORM_MESSAGE_SUMMARY)))
                logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_ADD_FORM_MESSAGE_DETAILS)))
                error_string += ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_ADD_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_ADD_FORM_MESSAGE_DETAILS) + "\t"
            # if add form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_ADD_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_BTN_LE_ADD_CANCEL)
            continue
        else:
            logger._log_to_console_and_log_file("- No errors Seen")

        # wait for Create operation to complete
        timeout = 1

        while timeout <= FusionLogicalEnclosuresPage.TIMEOUT:
            logger._log_to_console_and_log_file("Creation in progress...")
            # log step in progress
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STEP, 10):
                logger._log_to_console_and_log_file("Step in progress : {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_UPDATE_STEP)))

            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_COMPLETE, FusionLogicalEnclosuresPage.CREATE_LE_TIME):
                logger._log_to_console_and_log_file("Creation Completed.")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_WARNING, FusionLogicalEnclosuresPage.CREATE_LE_TIME):
                logger._warn("Creation Completed but with warning")
                break
            elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_UPDATE_STATUS_ERROR, FusionLogicalEnclosuresPage.CREATE_LE_TIME):
                logger._warn("--Error during creation")
                error += 1
                error_string += "--Error during Creation\t"
                break
            timeout += (FusionLogicalEnclosuresPage.CREATE_LE_TIME * 3) / 60.0

        if timeout > FusionLogicalEnclosuresPage.TIMEOUT:
            logger._warn("Either Creation of LE '{}' has not completed or Create Complete Alert is not seen , even after waiting for {} minutes!!".format(le.name, timeout))
            # if add form is still seen click cancel
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_ADD_FORM):
                logger._log_to_console_and_log_file("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_BTN_LE_ADD_CANCEL)

        # creation state from activity page
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_LE_PANEL_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.LINK_LE_ACTIVITY)
        logger._log_to_console_and_log_file("\nChecking Logical Enclosure Creation Activity State from Activity Page")
        ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_ACTIVITY_RESOURCE_VIEW, 25)
        ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_CREATE_ACTIVITY, 25)
        task_state = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_CREATE_ACTIVITY_STATE, 10)
        if 'completed' in task_state.lower():
            logger._log_to_console_and_log_file("Logical Enclosure Creation Activity State From activity Page is 'Completed'")
        elif 'warning' in task_state.lower():
            logger._warn("Logical Enclosure Creation Activity State From activity Page is - '{}'".format(task_state))
        else:
            logger._warn("Logical Enclosure Creation Activity State From activity Page is - '{}'".format(task_state))
            error += 1
            error_string += "Logical Enclosure Creation Activity State From activity Page is - '{}'".format(task_state)

        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_NAME % le.name):
            logger._log_to_console_and_log_file("Logical Enclosure '%s' is Seen in UI" % le.name)
        else:
            logger._warn("Logical Enclosure '%s' is NOT Seen in UI It may not have been created" % le.name)
            error += 1
            error_string += "Logical Enclosure '%s' is NOT Seen in UI It may not have been created" % le.name

    # return error string if error is seen else return true
    if error > 0:
        logger._warn("\n*** Creation Completed with errors ***")
        return error_string
    else:
        logger._log_to_console_and_log_file("\n*** Creation Completed Successfully ***")
        return True


def validate_le_firmware_upgrade_activity_details(*firmware_obj):
    '''
    Function to Validate the Update activity in the LE activity page
    Returns the issues and resolution seen in case of Update error ALONG with message TEST FAILED
    Else returns the Overall Update activity Message , containing the Message TEST PASSED

    DATAFILE EXAMPLE :

        <firmware1 bundle="Hafnium 166 Chloride 106 Carbon 22 2016 07 08 version 2016.07.08.66" upgradefor="Shared infrastructure"
                forceinstall="no" activationtype="parallel" lename="TestLE" unmanagedic="No"
                appip="10.10.0.91"  appuname="root" appasswd="hpvse1" dcs="False" proceedonwarning='yes'  unmanagedicnames='<unmanaged_ic_names-comma seperated>'
                expectedicfwversion = "k:1.0.0.166,cl10:1.05,cl20:1.05">

            <enclosure name="WPSTENC100" emip="fe80::1658:d0ff:fe41:4330%bond0,fe80::1658:d0ff:fe41:43e0%bond0" />
       </firmware1>

    attributes
        bundle*            - Firmware bundle to use for update
        upgradefor*        - upgrade FW for shared infra,shared infra and profiles or em only
        forceinstall       - Yes or No
        activationtype     - orchestrated or parallel | default is orchestrated
        lename *           - le name to perform update on
        unmanagedic        - Yes or No
        unmanagedicnames   - unmanaged ICM names as comma separated string
        appip*             - appliance IP (CIM IP)
        appuname*          - appliance user name
        appasswd*          - appliance password
        dcs               - True or False
        proceedonwarning  - yes or No
        expectedicfwversion* - expected versions of the ICMs as a comma separated string like 'k:1.0.167,cl10:1.05'

        <enclosure>*
            name*            - enclosure name as displayed
            emip*            - em ipv6 IPs , both the active and standby as a comma separated string , with the interface used in CIM mentioned

        * required attributes
    '''

    failed_times = 0
    error_string = ""
    activity_string = ""
    navigate()
    for fw in firmware_obj:
        if not VerifyLogicalEnclosures.verify_logical_enclosure_exist(fw.lename, 10, False):
            logger.warn("Logical enclosure '%s' does not exist" % fw.lename)
            failed_times += 1
            continue
        if VerifyLogicalEnclosures.verify_logical_enclosure_exist(fw.lename):
            TBirdCommonOperationLogicalEnclosures.click_logical_enclosure(fw.lename)
            # wait target logical enclosure get focus
        if not TBirdVerifyLogicalEnclosures.verify_le_consistency_state('Consistent', 10,):
            ui_lib.fail_test("the LE state of %s is not in Consistent state" % fw.lename)
        li_list_ui = _get_li_list_of_le(fw.lename)

        if li_list_ui:
            logger.info("LI's Part of the Logical Enclosure are -  %s" % li_list_ui)
        else:
            logger.warn("Unable to get the LI list of LE")
            activity_string += "LE {} ,has No LI".format(fw.lename)

        FusionUIBase.select_view_by_name("Firmware")
        server_hardware_list = TBirdUpdateFirmware.get_server_hardware_list(fw.lename)
        logger.info("Server Hardware list is %s" % server_hardware_list)
        if server_hardware_list:
            logger.info("Server Hardware part of the LE - {}".format(server_hardware_list))
        FusionUIBase.select_view_by_name("Activity")
        (status, activity_state) = TBirdUpdateFirmware.get_le_activity_state('Logical enclosure firmware update', timeout=10)
        logger.info("LE Activity State is %s" % activity_state)
        if not status:
            failed_times += 1
            error_string += "Could not find the state of the Firmware update from logs\t"
        else:
            if 'completed' in activity_state.lower():
                activity_string += "TEST PASSED.Firmware update completed Successfully for LE {}\t".format(fw.lename)
            else:
                failed_times += 1
                error_string += "TEST FAILED.Firmware upgrade did not complete as expected for LE %s. State returned : %s\t" % (fw.lename, activity_state)

        TBirdUpdateFirmware.click_activity_collapser()
        fw_activity_overall_details = TBirdUpdateFirmware.get_activity_details(10)
        # get overall activity details
        if fw_activity_overall_details:
            logger.info("\n------- LE Firmware Activity Overall Details -------\n{}\n".format(fw_activity_overall_details))
            activity_string += fw_activity_overall_details + '\t'
        fw_activity_issue_details = TBirdUpdateFirmware.get_activity_issue_details(10, False)
        # get overall issue details
        if fw_activity_issue_details:
            logger.warn("LE Firmware Activity Overall Issue - \n{}".format(fw_activity_issue_details))
            failed_times += 1
            error_string += fw_activity_issue_details + '\t'
        fw_activity_resolution_details = TBirdUpdateFirmware.get_activity_resolution_details(10, False)
        if fw_activity_resolution_details:
            logger.warn("LE Firmware Activity Resolution Details - \n{}".format(fw_activity_resolution_details))
            failed_times += 1
            error_string += fw_activity_issue_details + '\t'
        '''Check for the EM Activity Details,issue and resolution'''
        em_list = fw.enclosure
        for em in em_list:
            logger.info("name is %s" % em.name)
            fw_em_activity_overall_details = TBirdUpdateFirmware.get_em_activity_details(em.name, 10, False)
            # get em overall activity details
            if fw_em_activity_overall_details:
                logger.info("\n------- LE Firmware EM Activity Overall Details -------\n{}\n".format(fw_em_activity_overall_details))
                activity_string += fw_activity_overall_details + '\t'
            # get em overall issue details
            fw_em_activity_issue_details = TBirdUpdateFirmware.get_em_activity_issue_details(em.name, 10, False)
            if fw_em_activity_issue_details:
                logger.warn("LE Firmware EM Activity Overall Issue - \n{}".format(fw_em_activity_issue_details))
                failed_times += 1
                error_string += fw_em_activity_issue_details + '\t'
            # get em overall issue resolution
            fw_activity_resolution_details = TBirdUpdateFirmware.get_em_activity_resolution_details(em.name, 10, False)
            if fw_activity_resolution_details:
                logger.warn("LE Firmware EM Activity Resolution Details - \n{}".format(fw_activity_resolution_details))
                failed_times += 1
                error_string += fw_activity_resolution_details + '\t'
        '''check for unmanaged interconnect activity details'''
        if hasattr(fw, 'unmanagedic'):
            if fw.unmanagedic.lower() == 'yes':
                logger.info("Checking the Overall Unmanaged IC FW update activity state")
                unmanaged_activity_state = TBirdUpdateFirmware.get_unmanaged_activity_state(10)
                logger.info("State is %s" % unmanaged_activity_state)
                if 'Completed' in unmanaged_activity_state:
                    logger.info("Unmanaged IC FW update Activity completed successfully")
                else:
                    logger.warn("Unmanaged IC FW update State is - {}".format(unmanaged_activity_state))
                    failed_times += 1
                    error_string += "Unmanaged IC FW update State is - {}".format(unmanaged_activity_state) + '\t'
                unmanaged_ics = fw.unmanaged_ic1
                for ic in unmanaged_ics:
                    logger.info("Checking Activity Messages for Unmanaged Interconnects")
                    fw_unmanaged_activity_details = TBirdUpdateFirmware.get_unmanaged_activity_details(ic.icname, 10, False)
                    if fw_unmanaged_activity_details:
                        logger.info("\n------- Unmanaged Firmware update Overall Activity Details -------\n{}\n".format(fw_unmanaged_activity_details))
                        activity_string += fw_activity_overall_details + '\t'

        '''check for LI activity details'''
        for li in li_list_ui:
            if TBirdVerifyLogicalEnclosures.wait_li_sh_activity(li, 15, False):
                if fw.upgradefor.lower() not in ("shared infrastructure", "shared infrastructure and profiles"):
                    logger.warn("\nLI Firmware update has been triggered for LI '{}' though Upgrade option selected is '{}'!!".format(li, fw.upgradefor))
                    failed_times += 1
            else:
                if fw.upgradefor.lower() in ("shared infrastructure", "shared infrastructure and profiles"):
                    logger.warn("\nNo Activity Message Seen for update of logical Interconnect '{}' though upgrade option is '{}'!!".format(li, fw.upgradefor))
                    failed_times += 1
                    continue
            fw_li_activity_overall_details = TBirdUpdateFirmware.get_li_sh_activity_details(li, 15, False)
            logger.info("Activity is %s" % fw_li_activity_overall_details)
            if fw_li_activity_overall_details:
                if "No update required".lower() in fw_li_activity_overall_details.lower() and fw.forceinstall.lower() == "yes":
                    failed_times += 1
                    error_string += fw_li_activity_overall_details + "\t"
                    logger.warn("'No Update Required' Message is seen , though Force flag is selected")
                else:
                    activity_string += fw_li_activity_overall_details + "\t"
            # li activity issue details and description
            fw_li_activity_issue_details = TBirdUpdateFirmware.get_li_sh_activity_issue_details(li, 10, False)
            if fw_li_activity_issue_details:
                logger.warn("LE Firmware SP Activity Overall Issue - \n{}".format(fw_li_activity_issue_details))
                failed_times += 1
                error_string += fw_li_activity_issue_details + '\t'
            # get li overall issue resolution
            fw_li_activity_resolution_details = TBirdUpdateFirmware.get_li_sh_activity_resolution_details(li, 10, False)
            if fw_li_activity_resolution_details:
                logger.warn("LE Firmware SP Activity Resolution Details - \n{}".format(fw_li_activity_resolution_details))
                failed_times += 1
                error_string += fw_li_activity_resolution_details + '\t'

        '''check for server hardware activity details'''
        for sh in server_hardware_list:
            if TBirdVerifyLogicalEnclosures.wait_li_sh_activity(sh, 15, False):
                if fw.upgradefor.lower() in ("shared infrastructure", "frame link modules only"):
                    logger.warn("\Server Firmware update has been triggered for Server Hardware '{}' though Upgrade option selected is '{}'!!".format(sh, fw.upgradefor))
                    failed_times += 1
            else:
                if fw.upgradefor.lower() == "shared infrastructure and profiles":
                    logger.warn("\nNo Activity Message Seen for update of server Hardware '{}' though upgrade option is '{}'!!".format(sh, fw.upgradefor))
                    failed_times += 1
                    continue
            fw_sh_activity_overall_details = TBirdUpdateFirmware.get_li_sh_activity_details(sh, timeout=15, fail_if_false=False)
            if fw_sh_activity_overall_details:

                logger.info("Activity is %s" % fw_sh_activity_overall_details)
                if "No update required".lower() in fw_sh_activity_overall_details.lower() and fw.forceinstall.lower() == "yes":
                    failed_times += 1
                    error_string += fw_sh_activity_overall_details + "\t"
                    logger.warn("'No Update Required' Message is seen , though Force flag is selected")
                else:
                    activity_string += fw_sh_activity_overall_details + "\t"
            # server hardware activity issue details and description
            fw_sh_activity_issue_details = TBirdUpdateFirmware.get_li_sh_activity_issue_details(sh, 10, False)
            if fw_sh_activity_issue_details:
                logger.warn("LE Firmware SP Activity Overall Issue - \n{}".format(fw_sh_activity_issue_details))
                failed_times += 1
                error_string += fw_sp_activity_issue_details + '\t'
            # get server hardware overall issue resolution
            fw_sh_activity_resolution_details = TBirdUpdateFirmware.get_li_sh_activity_resolution_details(sh, 10, False)
            if fw_sh_activity_resolution_details:
                logger.warn("LE Firmware SP Activity Resolution Details - \n{}".format(fw_sh_activity_resolution_details))
                failed_times += 1
                error_string += fw_sh_activity_resolution_details + '\t'
        if failed_times > 0:
            return error_string
        else:
            return activity_string


def verify_le_frmware_upgrade_activity_details(*firmware_obj):
    '''
    Function to verify the UPdate activity in the LE activity page
    Returns the issues and resolutions seen in case of Update error ALONG with message TEST FAILED
    Else returns the Overall Update activity Message , containing the Message TEST PASSED
    '''

    em_activity_details = ""
    em_activity_issue = ""
    em_activity_resoultion = ""

    li_activity_details = ""
    li_issue = ""
    li_resolution = ""

    sp_issue = ""
    sp_activity_details = ""
    sp_resolution = ""

    activity_state = ""
    error = 0
    error_string = ""

    activity_string = ""
    li_list_ui = []
    server_profiles_list = []
    li_element_list = []

    # if not in LE page navigate
    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(firmware_obj, test_data.DataObj):
        firmware_obj = [firmware_obj]
    elif isinstance(firmware_obj, tuple):
        firmware_obj = list(firmware_obj[0])

    for fw in firmware_obj:
        # select the LE
        if not select_logicalenclosure(fw.lename):
            logger._warn("Unable to select Logical Enclosure '%s'.It may not be present" % fw.lename)
            error += 1
            error_string += "Unable to select Logical Enclosure '%s'.It may not be present\t" % fw.lename
            continue

        logger.info("\n******* FIRMWARE UPDATE ACTIVITY DETAILS FOR LE - '{}' *******\n".format(fw.lename))

        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_MENU_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.LINK_OVERVIEW)

        # verify LE state is Consistent
        le_consistency_state = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_LE_CONSISTENCY_STATE, FusionLogicalEnclosuresPage.WAIT_TIME)
        logger.info("LE consistency State is : {}".format(le_consistency_state))
        if le_consistency_state.lower() != 'consistent':
            logger.warn("LE consistency State is : {} , but should be : 'Consistent'".format(le_consistency_state))
            error += 1
            error_string += "LE consistency State is : {} , but should be : 'Consistent'".format(le_consistency_state)

        ''' Get the  LI list in the LE . This is needed for validation '''
        # get the list even if only EM update is selected , to verify that LI update has not been triggered
        li_list_ui = []
        li_list_ui = _get_li_list_of_le(fw.lename)

        if li_list_ui:
            logger.info("LI's Part of the Logical Enclosure are -  %s" % li_list_ui)
        else:
            logger.warn("Unable to get the LI list of LE")
            error += 1
            error_string += "LE {} ,has No LI".format(fw.lename)

        ''' get Server profiles in LE for validation '''
        # get this list even if profiles is not selected , to verify that no update has been triggered on profiles
        server_profiles_list = []
        server_profiles_list = _get_server_profiles_in_le(fw.lename)

        if server_profiles_list:
            logger.info("Server Profiles part of the LE - {}".format(server_profiles_list))

        ''' Verify the firmware  upgrade status in LE activity page '''
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_MENU_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTIVITY)
        ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_ACTIVITY_RESOURCE_VIEW, 20)

        # get Update activity status
        (status, activity_state) = _get_le_activity_state("Logical enclosure firmware update")
        if not status:
            logger.warn("Could not find the state of the Firmware update from logs")
            error += 1
            error_string += "Could not find the state of the Firmware update from logs\t"
        else:
            if 'completed' in activity_state.lower():
                logger.info("TEST PASSED.Firmware update completed Successfully for LE {}".format(fw.lename))
                activity_string += "TEST PASSED.Firmware update completed Successfully for LE {}\t".format(fw.lename)
            else:
                logger.warn("TEST FAILED.Firmware upgrade did not complete as expected for LE %s. State returned : %s" % (fw.lename, activity_state))
                error += 1
                error_string += "TEST FAILED.Firmware upgrade did not complete as expected for LE %s. State returned : %s\t" % (fw.lename, activity_state)

            ''' Expand the Update firmware for LE '''
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTIVITY_COLLAPSER)

            '''Check the Overall Activity MEssage if visible'''
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_OVERALL_ACTIVITY_DETAILS, FusionLogicalEnclosuresPage.WAIT_TIME):
                fw_activity_overall_details = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_OVERALL_ACTIVITY_DETAILS)
                logger.info("\n------- LE Firmware Activity Overall Details -------\n{}\n".format(fw_activity_overall_details))
                activity_string += fw_activity_overall_details + '\t'
            # issue
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_OVERALL_ACTIVITY_ISSUE, 10):
                fw_activity_overall_issue = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_OVERALL_ACTIVITY_ISSUE)
                logger.warn("LE Firmware Activity Overall Issue - \n{}".format(fw_activity_overall_issue))
                error += 1
                error_string += fw_activity_overall_issue + '\t'
            # resolution
            if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_OVERALL_ACTIVITY_RESOLUTION, 10):
                fw_activity_overall_resolution = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_OVERALL_ACTIVITY_RESOLUTION)
                logger.warn("LE Firmware Activity Overall Resolution - \n{}".format(fw_activity_overall_resolution))
                error += 1
                error_string += fw_activity_overall_resolution + '\t'
            logger.info("--------------------------------------------\n")

            '''Check for the EM Activity Details,issue and resolution if any'''
            em_list = fw.enclosure
            for em in em_list:
                # get overall activity details
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_EM_ACTIVITY_DETAILS % em.name, FusionLogicalEnclosuresPage.WAIT_TIME):
                    logger.info("------- EM '{}' Activity Logs -------\n".format(em.name))
                    em_activity_details = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_EM_ACTIVITY_DETAILS % em.name)
                    logger.info("EM Upgrade Activity Details - \n'{}'\n".format(em_activity_details))
                    error_string += em_activity_details + "\t"
                    # if no update required is seen in message treat it as an error - since this operation should not
                    # be successful without force option
                    if "No update required".lower() in em_activity_details.lower() and fw.forceinstall.lower() == "yes":
                        error += 1
                        logger.warn("'No Update Required' Message is seen , though Force flag is selected")
                    else:
                        activity_string += em_activity_details + "\t"
                else:
                    logger.warn("No upgrade activity Message is seen for EM '{}'!!".format(em.name))
                    error += 1
                    continue

                # check for issue
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_EM_ACTIVITY_ISSUE % em.name, FusionLogicalEnclosuresPage.WAIT_TIME):
                    em_activity_issue = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_EM_ACTIVITY_ISSUE % em.name)
                    if em_activity_issue:
                        logger.warn("EM Upgrade activity Issue Seen - \n'{}'\n".format(em_activity_issue))
                        error += 1
                        error_string += "EM Upgrade activity Issue Seen - '{}'\t".format(em_activity_issue)
                # check for resolution
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_EM_ACTIVITY_RESOULTION % em.name, FusionLogicalEnclosuresPage.WAIT_TIME):
                    em_activity_resoultion = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_EM_ACTIVITY_RESOULTION % em.name)
                    if em_activity_resoultion:
                        logger._warn("EM Upgrade activity Issue Resolution - \n'{}'\n".format(em_activity_resoultion))
                        error += 1
                        error_string += "EM Upgrade activity Issue Resolution - '{}'\t".format(em_activity_resoultion)

                logger._log_to_console_and_log_file("--------------------------------------------\n")

            ''' Check for the LI Activity Details,issue and resolution if any '''
            for li in li_list_ui:
                # check if activity messages if seen , and it corresponds to the upgrade option selected i.e shared infra, shared infra and profiles or EM only
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY % li, FusionLogicalEnclosuresPage.WAIT_TIME):
                    if fw.upgradefor.lower() not in ("shared infrastructure", "shared infrastructure and profiles"):
                        logger.warn("\nLI Firmware update has been triggered for LI '{}' though Upgrade option selected is '{}'!!".format(li, fw.upgradefor))
                        error += 1
                else:
                    if fw.upgradefor.lower() in ("shared infrastructure", "shared infrastructure and profiles"):
                        logger.warn("\nNo Activity Message Seen for LI update of '{}' though upgrade option is '{}'!!".format(li, fw.upgradefor))
                        error += 1
                        continue
                # get overall activity details
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY_DESC % li, FusionLogicalEnclosuresPage.WAIT_TIME):
                    logger.info("------- LI '{}' Activity Logs -------\n ".format(li))
                    li_activity_details = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY_DESC % li)
                    logger.info("LI Upgrade Activity Details - \n'{}'\n".format(li_activity_details))
                    error_string += li_activity_details + "\t"
                    # if no update required is seen in message and force flag is true in input treat it as an error - since this operation should not
                    # be successful without force option
                    if "No update required".lower() in li_activity_details.lower() and fw.forceinstall.lower() == "yes":
                        error += 1
                        logger.warn("'No Update Required' Message is seen , though Force flag is selected")
                    else:
                        activity_string += li_activity_details + "\t"

                # check for issue
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ISSUE % li, FusionLogicalEnclosuresPage.WAIT_TIME):
                    li_issue = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ISSUE % li)
                    if li_issue:
                        logger.warn("LI Upgrade Activity Issue Seen - \n'{}'\n".format(li_issue))
                        error += 1
                        error_string += "LI Upgrade Activity Issue Seen - '{}'\t".format(li_issue)
                # check for resolution
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_RESOLUTION % li, FusionLogicalEnclosuresPage.WAIT_TIME):
                    li_resolution = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_RESOLUTION % li)
                    if li_resolution:
                        logger.warn("LI Upgrade Activity Issue Resolution - \n'{}'\n".format(li_resolution))
                        error += 1
                        error_string += "LI Upgrade Activity Issue Resolution - '{}'\t".format(li_resolution)

                logger.info("--------------------------------------------\n")

            '''check for unmanaged interconnect activity details,issue and resolution if any'''
            if hasattr(fw, 'unmanagedic'):
                if fw.unmanagedic.lower() == 'yes':
                    logger.info("Checking the Overall Unmanaged IC FW update activity state")
                    unmanaged_ic_activity_state = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_UNMANAGED_FW_ACTIVITY_STATE, 15)
                    logger.info("stateis %s" % unmanaged_ic_activity_state)
                    if 'completed' in unmanaged_ic_activity_state:
                        logger.info("Unmanaged IC FW update Activity completed successfully")
                    else:
                        logger.warn("Unmanaged IC FW update State is - {}".format(unmanaged_ic_activity_state))
                        error += 1
                        error_string += "Unmanaged IC FW update State is - {}".format(unmanaged_ic_activity_state) + '\t'

                    # get unmanaged ICs from input
                    unmanaged_ics = fw.unmanaged_ic1
                    logger.info("Checking Activity Messages for Unmanaged Interconnects")
                    for ic in unmanaged_ics:
                        # get overall activity details
                        if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY_DESC % ic.icname, FusionLogicalEnclosuresPage.WAIT_TIME):
                            logger.info("------- Unmanaged interconnect Update '{}' Activity Logs -------\n".format(ic.icname))
                            unmanaged_ic_activity_details = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY_DESC % ic.icname)
                            logger.info("Unmanaged interconnect Update Activity Details - \n'{}'\n".format(unmanaged_ic_activity_details))
                            activity_string += unmanaged_ic_activity_details + "\t"
                    error_string += activity_string + '\t'

            '''Check for the profiles Activity Details,issue and resolution if any'''
            for sp in server_profiles_list:
                # check if activity messages if seen , and it corresponds to the upgrade option selected i.e shared infra and profiles
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY % sp, FusionLogicalEnclosuresPage.WAIT_TIME):
                    if fw.upgradefor.lower() in ("shared infrastructure", "frame link modules only"):
                        logger.warn("\nProfile Firmware update has been triggered for Server Profile '{}' though Upgrade option selected is '{}'!!".format(sp, fw.upgradefor))
                        error += 1
                else:
                    if fw.upgradefor.lower() == "shared infrastructure and profiles":
                        logger.warn("\nNo Activity Message Seen for Profile update of server Profile '{}' though upgrade option is '{}'!!".format(sp, fw.upgradefor))
                        error += 1
                        continue
                # get overall activity details
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY_DESC % sp, FusionLogicalEnclosuresPage.WAIT_TIME):
                    logger.info("------- Profile Update '{}' Activity Logs -------\n".format(sp))
                    sp_activity_details = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ACTIVITY_DESC % sp)
                    logger.info("Profile Upgrade Activity Details - \n'{}'\n".format(sp_activity_details))
                    error_string += sp_activity_details + "\t"
                    # if no update required is seen in message and force flag is true in input treat it as an error - since this operation should not
                    # be successful without force option
                    if "No update required".lower() in sp_activity_details.lower() and fw.forceinstall.lower() == "yes":
                        error += 1
                        logger.warn("'No Update Required' Message is seen , though Force flag is selected")
                    else:
                        activity_string += sp_activity_details + "\t"

                # check for issue
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ISSUE % sp, FusionLogicalEnclosuresPage.WAIT_TIME):
                    sp_issue = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_ISSUE % sp)
                    if sp_issue:
                        logger.warn("Profile Upgrade Activity Issue Seen - \n'{}'\n".format(sp_issue))
                        error += 1
                        error_string += "Profile Upgrade Activity Issue Seen - '{}'\t".format(sp_issue)
                # check for resolution
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_RESOLUTION % sp, FusionLogicalEnclosuresPage.WAIT_TIME):
                    sp_resolution = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_FORM_LI_SP_RESOLUTION % sp)
                    if sp_resolution:
                        logger.warn("Profile Upgrade Activity Issue Resolution - \n'{}'\n".format(sp_resolution))
                        error += 1
                        error_string += "Profile Upgrade Activity Issue Resolution - '{}'\t".format(sp_resolution)

                logger.info("--------------------------------------------\n")

            # close the activity
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTIVITY_COLLAPSER_ACTIVE)

        logger.info("***************************************************\n")

    # if error return the error string with TEST FAILED , else return the activity details with TEST PASSED
    if error > 0:
        return error_string
    else:
        return activity_string


def _get_li_list_of_le(le_name):
    '''
    Function to Get the  LI list in the LE .
    Returns Empty list of unable to retrieve
    '''
    li_element_list = []
    error = 0
    # navigate to LE Page
    navigate()
    # select the LE
    if not select_logical_enclosure(le_name):
        logger.warn("Unable to select Logical Enclosure '%s'.It may not be present" % le_name)
        error += 1
        return []
    FusionUIBase.select_view_by_name('Overview')
    li_element_list = CommonOperationLogicalEnclosures.get_logical_interconnects_of_le(fail_if_false=False)
    logger.info("li_element_list is %s" % li_element_list)
    return li_element_list


def _get_server_profiles_in_le(le_name):
    '''
    Function to get list of Server profiles in LE
    Returns Empty list of unable to retrieve
    '''
    server_profiles_list = []
    server_profiles_elements = []
    selenium2libObj = ui_lib.get_s2l()
    error = 0

    # if not in LE page navigate
    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    # select the LE
    if not select_logicalenclosure(le_name):
        logger._warn("Unable to select Logical Enclosure '%s'.It may not be present" % le_name)
        error += 1
        return []

    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_MENU_SELECTOR)
    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.LINK_FIRMWARE, FusionLogicalEnclosuresPage.WAIT_TIME)
    ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_FIRMWARE_TABLE_WRPAAPER, FusionLogicalEnclosuresPage.WAIT_TIME)

    server_profiles_elements = selenium2libObj._current_browser().find_elements_by_xpath(FusionLogicalEnclosuresPage.XPATH_LE_SERVER_PROFILES)
    try:
        for sp_element in server_profiles_elements:
            server_profiles_list.append(sp_element.text)
    except:
        server_profiles_elements = selenium2libObj._current_browser().find_elements_by_xpath(FusionLogicalEnclosuresPage.XPATH_LE_SERVER_PROFILES)
        for sp_element in server_profiles_elements:
            server_profiles_list.append(sp_element.text)
    return server_profiles_list


def _get_le_activity_state(activity_label):
    '''
    Get the Activity State of any LE activity
    - Takes the Activity label as an input parameter
    - returns True and the state if the activity is found
      else returns false and ''
    '''
    # if not in LE activity page navigate
    if not ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_ACTIVITY_RESOURCE_VIEW, 20):
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_MENU_SELECTOR)
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_ACTIVITY)
        ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_ACTIVITY_RESOURCE_VIEW, 20)

    ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_UPDAtE_ACTIVITY % activity_label, PerfConstants.PROFILE_POWER_VALIDATION)
    # check if the activity is seen in the activity page and get state of present
    if ui_lib.wait_for_element(FusionLogicalEnclosuresPage.XPATH_LE_UPDAtE_ACTIVITY % activity_label):
        state = ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_UPDATE_ACTIVITY_STATE % activity_label)
        return (True, state)
    else:
        logger._warn("'%s' is not present in Activity page" % activity_label)
        return (False, '')


def verify_li_and_ic_firmware_versions(*firmware_obj):
    '''
    Function to validate if the installed and baseline versions of Interconnects
    in Logical interconnect is same as that installed in the IC after LE FW update

    Function also gets the installed version from the actual hardware and verifies it is same as that displayed in Appliance
    '''

    li_list_ui = []
    error = 0
    message_list = []
    li_element_list = []
    expected_version_list = []

    # if not in LE page navigate
    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(firmware_obj, test_data.DataObj):
        firmware_obj = [firmware_obj]
    elif isinstance(firmware_obj, tuple):
        firmware_obj = list(firmware_obj[0])

    for fw in firmware_obj:
        # select the LE
        if not select_logicalenclosure(fw.lename):
            logger._warn("Unable to select Logical Enclosure '%s'.It may not be present" % fw.lename)
            error += 1
            continue

        ''' Get the  LI list in the LE . This is needed for validation '''
        li_list_ui = []
        li_list_ui = _get_li_list_of_le(fw.lename)

        # if LI details are not retrievable abort current verification and continue to next LE FW upgrade verification
        if not li_list_ui:
            logger._warn("Unable to get logical Enclosure LI details.Hence skipping LI and IC validation for LE '{}'".format(fw.lename))
            error += 1
            continue
        logger._log_to_console_and_log_file("LI's Part of the Logical Enclosure are -  %s" % li_list_ui)

        ''' Navigate to LI page and Validate if the firmware version is reflected in the LI page for the interconnects '''
        logger._log_to_console_and_log_file("\n***********VERIFY INSTALLED FW AND BASELINE FW VERSIONS IN LI PAGE ARE SAME********************\n")

        ''' Check the interconnect firmware version in LI page , also verify with the actual installed version in the interconnects'''
        (status, ic_firm) = logicalinterconnects.verify_interconnect_firmware_from_li(li_list_ui, firmware_obj)
        logger._log_to_console_and_log_file("******************************")
        status = True
        ''' Validate the messages in activity page of interconnects if the previous step passed'''
        if status:
            # checking the installed version with the expected version from input
            # provide expected version as a comma separated list Eg. - k:version,cl10:version,cl20:version
            temp_list = []
            if (not hasattr(fw, 'type')) or (fw.type) != 'c7k':

                if hasattr(fw, 'expectedicfwversion'):
                    expected_version_list = [element.split(':')[1] for element in fw.expectedicfwversion.split(',')]

                logger._log_to_console_and_log_file("***********VERIFYING ALERT MESSAGES AND FIRMWARE VERSIONS OF INTERCONNECTS FROM INTERCONNECTS PAGE**********\n")
                for key in ic_firm:
                    if expected_version_list:
                        logger._log_to_console_and_log_file("--Checking if the Installed Version shown in UI is same as expected--")
                        if ic_firm[key] in expected_version_list:
                            logger._log_to_console_and_log_file("Version expected is same as version installed : {}".format(ic_firm[key]))
                        else:
                            logger._warn("Version installed : {} is not in version expected list : {} !!".format(ic_firm[key], expected_version_list))
                            error += 1
                        logger._log_to_console_and_log_file("--------------------------------------------\n")

                    # verify if the installed and baseline version shown in the IC page are same
                    logger._log_to_console_and_log_file("--Checking if the Installed and Baseline Version of the IC '{}' shown in General section of UI,are same--".format(key))
                    return_value = interconnects.verify_ic_installed_baseline_firmware_versions(key)
                    # if return value is false set error flag
                    if not return_value:
                        error += 1
                    logger._log_to_console_and_log_file("--------------------------------------------\n")

                    message_list = [msg % (key, ic_firm[key]) for msg in FusionLogicalEnclosuresPage.LI_MESSAGE_LIST]
                    logger._log_to_console_and_log_file("Checking following Messages are see in Activity Page of Interconnect '{}' -\n{}\n".format(key, message_list))
                    if interconnects.verify_interconnect_recent_activity(key, message_list):
                        logger._log_to_console_and_log_file("All the expected alerts are present in Activity page of Interconnect '{}'\n".format(key))
                    else:
                        logger._log_to_console_and_log_file("Not All expected alert messages found for Interconnect '%s'" % key)
                        error += 1
                    logger._log_to_console_and_log_file("--------------------------------------------\n")
            else:

                if hasattr(fw, 'expectedicfwversionUI'):
                    expected_version_list = [element.split('=')[1] for element in fw.expectedicfwversion.split(',')]
                    expected_version_list_act = [element.split('=')[1] for element in fw.expectedicfwversion.split(',')]
                    expected_version_list_expui = [element.split('=')[1] for element in fw.expectedicfwversionUI.split(',')]

                logger._log_to_console_and_log_file("***********VERIFYING ALERT MESSAGES AND FIRMWARE VERSIONS OF INTERCONNECTS FROM INTERCONNECTS PAGE**********\n")
                # for key in ic_firm:
                for key, ver in zip(ic_firm, expected_version_list_act):

                    if expected_version_list:
                        logger._log_to_console_and_log_file("--Checking if the Installed Version shown in UI is same as expected--")
                        if ic_firm[key] in expected_version_list_expui:
                            logger._log_to_console_and_log_file("Version expected is same as version installed : {}".format(ic_firm[key]))
                        else:
                            logger._warn("Version installed : {} is not in version expected list : {} !!".format(ic_firm[key], expected_version_list_expui))
                            error += 1
                        logger._log_to_console_and_log_file("--------------------------------------------\n")

                    # verify if the installed and baseline version shown in the IC page are same
                    logger._log_to_console_and_log_file("--Checking if the Installed and Baseline Version of the IC '{}' shown in General section of UI,are same--".format(key))
                    return_value = interconnects.verify_ic_installed_baseline_firmware_versions(key)
                    # if return value is false set error flag
                    if not return_value:
                        error += 1
                    logger._log_to_console_and_log_file("--------------------------------------------\n")

                    # message_list = [msg % (key, ic_firm[key]) for msg in FusionLogicalEnclosuresPage.LI_MESSAGE_LIST]
                    message_list = [msg % (key, ver) for msg in FusionLogicalEnclosuresPage.LI_MESSAGE_LIST_C7K]
                    #   ##############################
                    logger._log_to_console_and_log_file("Checking following Messages are see in Activity Page of Interconnect '{}' -\n{}\n".format(key, message_list))
                    if interconnects.verify_interconnect_recent_activity(key, message_list):
                        logger._log_to_console_and_log_file("All the expected alerts are present in Activity page of Interconnect '{}'\n".format(key))
                    else:
                        logger._log_to_console_and_log_file("Not All expected alert messages found for Interconnect '%s'" % key)
                        error += 1
                    logger._log_to_console_and_log_file("--------------------------------------------\n")
        else:
            logger._warn("Interconnects firmware version is NOT set as expected after upgrade.")
            logger._warn("One or more components may not be upgraded as expected")
            error += 1
    logger._log_to_console_and_log_file("\n********************************************\n")
    # if error return false else return True
    if error > 0:
        return False
    else:
        return True


def update_logical_enclosure_firmware(*enclosure_list):
    """ Update  Logical Enclosure Firmware
        This function is  to update enclosure firmware

        Example:
            update_logical_enclosure_firmware(*enclosure_list)
    """
    flag = True
    error_string, error_status, errors_on_form, upgradefor = '', '', '', ''

    if isinstance(enclosure_list, test_data.DataObj):
        enclosure_list = [enclosure_list]
    elif isinstance(enclosure_list, tuple):
        enclosure_list = list(enclosure_list)

    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    count = 0
    for enclosure in enclosure_list:
        if not select_logicalenclosure(enclosure.enclosurename):
            logger._log_to_console_and_log_file("%s Enclosure is not available" % enclosure.enclosurename)
            count = count + 1
            continue

        if ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_MENU_ACTION_MAIN_BTN):

            error = 0

            if not (ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_MENU_ACTION_UPDATE_FIRMWARE)):

                logger._warn("Update Firmware Option not seen in actions menu.User may not have Update Firmware privilege")
                error += 1
                error_string += "Update Firmware Option not seen in actions menu.User may not have Update Firmware privilege\t"
                raise AssertionError(error_string)
        else:
            logger._warn("Actions button not seen.User may not have privilege")
            error += 1
            error_string += "Actions button not seen.User may not have privilege\t"
            raise AssertionError(error_string)

        ''' Select the SPP file for firmware update'''
        ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FIRMWARE_DROPDOWN)

        if not (ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_SELECT_FROM_DROPDOWN % enclosure.firmware)):

            logger.warn("Firmware Bundle '{}' not seen in dropdown.Canceling Upgrade".format(enclosure.firmware))
            flag = False
            count = count + 1
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
            continue

        if enclosure.forceinstall.lower() == "true":
            logger._log_to_console_and_log_file("Updating Firmware with Force")
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FIRMWARE_BASELINE_CHECKBOX)
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_UPGRADE_FOR_DROPDOWN)
            if (str(enclosure.sharinfra) == "Shared infrastructure") or (str(enclosure.sharinfra) == "Shared infrastructure and profiles") or (str(enclosure.sharinfra) == "Onboard administrators only"):

                upgradefor = str(enclosure.sharinfra)
                logger._log_to_console_and_log_file("Selected Upgrade Mode is - {}".format(upgradefor))

            else:
                logger._warn("Invalid upgrade for option - '{}'.Clicking Cancel".format(upgradefor))
                flag = False
                count = count + 1
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
                # continue
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_SELECT_FROM_DROPDOWN % upgradefor)
            logger._log_to_console_and_log_file("Selected Upgrade Mode - {}".format(upgradefor))

        else:
            logger._log_to_console_and_log_file("Updating Firmware without Force")
            #  code for select Share,shar and profile ,OA only
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_UPGRADE_FOR_DROPDOWN)
            if (str(enclosure.sharinfra) == "Shared infrastructure") or (str(enclosure.sharinfra) == "Shared infrastructure and profiles") or (str(enclosure.sharinfra) == "Onboard administrators only"):

                upgradefor = str(enclosure.sharinfra)

            else:
                logger._warn("Invalid upgrade for option - '{}'.Clicking Cancel".format(upgradefor))
                flag = False
                count = count + 1
                ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
                continue
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_SELECT_FROM_DROPDOWN % upgradefor)
            logger._log_to_console_and_log_file("Selected Upgrade Mode - {}".format(upgradefor))

            ''' Select  the unmanaged interconnects if checkbox is visible'''
            if (enclosure.has_property('unmanagedic') and ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_UNMANAGED_INTERCONNECT_CHECKBOX, FusionLogicalEnclosuresPage.WAIT_TIME)):
                if enclosure.unmanagedic == 'yes':
                    ui_lib.wait_for_checkbox_and_select(FusionLogicalEnclosuresPage.ID_UNMANAGED_INTERCONNECT_CHECKBOX)
                    logger._log_to_console_and_log_file("Selecting Unmanaged IC checkbox")
                else:
                    ui_lib.wait_for_checkbox_and_unselect(FusionLogicalEnclosuresPage.ID_UNMANAGED_INTERCONNECT_CHECKBOX)
                    logger._log_to_console_and_log_file("De-Selecting UnManaged IC checkbox")

        ''' # click OK to begin firmware update  '''
        logger._log_to_console_and_log_file("Clicking OK on LE update Firmware")
        if enclosure.negbb_triggeronly == 'Yes':
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_UPDATE_FIRMWARE_OK_BUTTON)
            return True
        else:
            ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_UPDATE_FIRMWARE_OK_BUTTON)

            ''' Check error messages appears on LE FW update page '''

            logger._log_to_console_and_log_file("Checking For errors - After clicking on OK Button of Firmware update in LE page")

            if not ui_lib.wait_for_element_notvisible(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM, FusionLogicalEnclosuresPage.WAIT_TIME):
                errors_on_form = base_page.get_errors_on_form(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM)
                error_status = ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_HP_STATUS_ERROR, FusionLogicalEnclosuresPage.WAIT_TIME)
            if error_status or errors_on_form:
                flag = False
                count = count + 1
                if errors_on_form:
                    error_string += errors_on_form + "\t"
                if error_status:
                    logger._warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY)))
                    logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS)))
                    flag = False
                    count = count + 1
                    error_string += ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalEnclosuresPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS) + "\t"
                # if form is still seen click cancel
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM):
                    logger._log_to_console_and_log_file("Clicking Cancel")
                    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
                    flag = False
                    count = count + 1
                continue
            else:
                logger._log_to_console_and_log_file("No errors Seen on LE Firmware update page")

            ''' Checking the Firmware update progress once FW upgrade started'''
            if (ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_PROGRESS_BAR, PerfConstants.DEFAULT_SYNC_TIME)):

                value_sec = 1
                while value_sec < FusionLogicalEnclosuresPage.FW_UPDATE_TIME:

                    value_sec = value_sec + 2
                    if (ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_PROGRESS_BAR, PerfConstants.DEFAULT_SYNC_TIME)):
                        logger.info("1.Update Firmware  is in Progress in LE and waited for " + str(value_sec))
                    if (ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_CMPLETE_XPATH, PerfConstants.DEFAULT_SYNC_TIME)):
                        logger.info("Firmware update Completed on LE page successfully.\n")
                        action_status_time = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_STATUS_BAR)
                        A_status_time = re.search('Completed\d+\w\d+s', action_status_time)
                        if A_status_time:

                            Completewithtime = A_status_time.group()
                            ActualTimeTaken = re.search('\d+\w+', Completewithtime)
                            CompletedTimeonly = ActualTimeTaken.group()
                            logger.info("Actual Time Taken for Firmware update is : " + str(CompletedTimeonly))

                        break
                    elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_WARNING_XPATH, FusionLogicalEnclosuresPage.ID_LE_UPDATE_WAIT_TIME):

                        logger._warn("Firmware update Completed but with warning on LE page")
                        flag = False

                        break
                    elif ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_ERROR_XPATH, FusionLogicalEnclosuresPage.ID_LE_UPDATE_WAIT_TIME):
                        logger._warn("--Error during Firmware update on LE page")
                        flag = False

                        break

                if value_sec > FusionLogicalEnclosuresPage.FW_UPDATE_TIME:

                    logger.warn("Either FW Upgrade of LE '{}' has not completed , even after waiting for {} minutes!!".format(enclosure.enclosurename, value_sec))
                    flag = False
                    error_string += "Either FW Upgrade of LE '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!\t".format(enclosure.enclosurename, value_sec)
                # if add form is still seen click cancel
                if ui_lib.wait_for_element_visible(FusionLogicalEnclosuresPage.ID_LE_FW_UPDATE_FORM):
                    logger.info("Clicking Cancel")
                    ui_lib.wait_for_element_and_click(FusionLogicalEnclosuresPage.ID_FW_CANCEL)
            else:
                logger.warn("No progress bar Seen on LE Firmware upgrade task ")
                flag = False

            action_status = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_STATUS_BAR)
            if "Completed" in action_status:
                logger.info(action_status)
                logger.info("Update firmware is successfully completed for %s enclosure" % enclosure.enclosurename)
            else:

                logger._warn("Failed to do update firmware for %s enclosure" % enclosure.enclosurename)
                flag = False

                continue
    if flag:
        return True
    else:
        raise AssertionError("LE Firmware update failed")


def verify_ilo_ipv4ips_of_servers_in_le_within_range_pool(le_name, range_list):
    '''
    Function to verify the Ipv4 IP's assigned to the Server ILOs of the server profiles in the logical Enclosure
    are from the IP pool range associated with the Enclosure group of the LE.
    '''
    error = 0
    enclosure_list_ui = []
    enc_server_list = []
    navigate()

    if not select_logicalenclosure(le_name):
        raise AssertionError("Unable to select Logical Enclosure '%s'.It may not be present" % le_name)

    # get the enclosures in LE
    FusionUIBase.select_view_by_name('Overview', timeout=5, fail_if_false=False)
    enclosure_list_ui = CommonOperationLogicalEnclosures.get_enclosure_list_from_le(5, False)

    for enclosure in enclosure_list_ui:
        enc_server_list_temp = []
        enc_server_list_temp = serverhardware._list_servers(enclosure)
        if(enc_server_list_temp):
            enc_server_list += enc_server_list_temp
        else:
            logger.warn("No servers found for enclosure '{}'".format(enclosure))

    # get the ilo ipv4 ip of each server and verify if the ips are in subnet
    for servername in enc_server_list:
        serverilo_dict = {}
        serverilo_dict = serverhardware._get_server_hardware_info(servername, 'IloIpv4')
        if serverilo_dict:
            logger.debug("\nILO ipv4 address of server {} is {}".format(servername, serverilo_dict['IloIpv4']))
            if settings.is_ip_in_subnet(serverilo_dict['IloIpv4'], range_list):
                logger.debug("The Server '{}' ILO ipv4 address '{}' is within the defined custom range".format(servername, serverilo_dict['IloIpv4']))
            else:
                error += 1
        else:
            logger.warn("No ILO IPV4 address found for server '{}'.It May not have been assigned!!".format(servername))
            error += 1
    if error > 0:
        raise AssertionError("One or More of IPs of Server ILOs is not in specified range")
    return True


def verify_ic_ipv4address_of_li_in_le_within_range_pool(le_name, range_list):
    '''
    Function to verify the ipv4 IP's assigned to the Interconnects of the Logical Interconnects in a Logical Enclosure
    are from the IP pool range assigned to the Enclosure group of the LE
    '''
    li_list_ui = []
    li_ic_ipv4_address_dict = {}
    error = 0
    navigate()

    if not select_logicalenclosure(le_name):
        raise AssertionError("Unable to select Logical Enclosure '%s'.It may not be present" % le_name)

    li_list_ui = []
    li_list_ui = _get_li_list_of_le(le_name)

    if li_list_ui:
        for li in li_list_ui:
            li_ic_ipv4_address_dict = {}
            # get ic : ipv4 address dictionary
            li_ic_ipv4_address_dict = logicalinterconnects.get_ic_ipv4_address_in_li(li)
            if li_ic_ipv4_address_dict:
                ic_list = li_ic_ipv4_address_dict.keys()
                for ic in ic_list:
                    if settings.is_ip_in_subnet(li_ic_ipv4_address_dict[ic], range_list):
                        logger.debug("IP '{}' assigned to IC '{}' is from the Custom range defined in input".format(li_ic_ipv4_address_dict[ic], ic))
                    else:
                        error += 1
                        logger.warn("IP '{}' assigned to IC '{}' is not from any of the custom range".format(li_ic_ipv4_address_dict[ic], ic))
            else:
                logger.warn("Could not get the IPs of any of the ICs in the LI {}.It may not have been assigned!!".format(li))
                error += 1
    else:
        raise AssertionError("No LIs found for the Logical Enclosure {}".format(le_name))
    if error > 0:
        raise AssertionError("One or more Ips of ICs not in defined range")
    return True


def reapply_li_configuration_of_le(le_name, wait_for_task_complete='true'):
    '''
    Function to reapply configuration of the LIs in the LE mentioned
    If wait_for_task_complete is true then function waits till task completes
    else it just triggers a reapply and returns
    '''
    # navigate
    navigate()
    error = 0
    # select the LE
    if not select_logical_enclosure(le_name):
        logger.warn("Unable to select the Logical Enclosure '%s'.It may not be present" % le_name)
        error += 1
        return False

    ''' Get the  LI list in the LE . This is needed for validation '''
    li_list_ui = []
    li_list_ui = _get_li_list_of_le(le_name)
    if not li_list_ui:
        logger.warn("Unable to get logical Enclosure LI details.Hence skipping LI reapply configuration for LE '{}'".format(le_name))
        error += 1
        return False
    logger.info("LI's Part of the Logical Enclosure are -  %s" % li_list_ui)

    for li_name in li_list_ui:
        if logicalinterconnects.reapply_li_configuration(li_name, wait_for_task_complete):
            logger.info("Reapply Configuration of LI {} was successfully triggered".format(li_name))
        else:
            logger.warn("Reapply Configuration of LI {} was not successfull".format(li_name))
            error += 1
    if error > 0:
        return False
    return True


def verify_ic_stacking_domain_role_of_le(*firmware_obj):
    '''
    Function to verify the stacking domain role of the IC's in the LI of the LE.
    At least half of the IC's should be master , and the other half subordinate
    In case the IC under consideration does not have a stacking role (like chlorides) an appropriate message is logged and it is not considered

    Returns a boolean value
    '''
    error = 0
    # if not in LE page navigate
    if not ui_lib.wait_for_element(FusionLogicalEnclosuresPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(firmware_obj, test_data.DataObj):
        firmware_obj = [firmware_obj]
    elif isinstance(firmware_obj, tuple):
        firmware_obj = list(firmware_obj[0])

    for fw in firmware_obj:
        # select the LE
        if not select_logicalenclosure(fw.lename):
            logger._warn("Unable to select Logical Enclosure '%s'.It may not be present" % fw.lename)
            error += 1
            continue

        ''' Get the  LI list in the LE . This is needed for validation '''
        li_list_ui = []
        li_list_ui = _get_li_list_of_le(fw.lename)

        # if LI details are not retrievable abort current verification and continue to next LE FW upgrade verification
        if not li_list_ui:
            logger._warn("Unable to get logical Enclosure LI details.Hence skipping LI and IC validation for LE '{}'".format(fw.lename))
            error += 1
            return False
        logger._log_to_console_and_log_file("LI's Part of the Logical Enclosure are -  %s" % li_list_ui)

        for li in li_list_ui:
            sub_count = 0
            master_count = 0
            li_ic_stacking_role_dict = {}
            li_ic_stacking_role_dict = logicalinterconnects.get_ic_stacking_domain_role_of_li(li)
            if li_ic_stacking_role_dict:
                ic_list = li_ic_stacking_role_dict.keys()
                for ic in ic_list:
                    logger._log_to_console_and_log_file("Stacking Domain Role of ic {} is - {}".format(ic, li_ic_stacking_role_dict[ic]))
                    if li_ic_stacking_role_dict[ic].lower() == 'master':  # and not found_master:
                        logger._log_to_console_and_log_file("IC {} is the MASTER".format(ic))
                        master_count += 1
                    elif li_ic_stacking_role_dict[ic].lower() == 'subordinate':
                        logger._log_to_console_and_log_file("IC {} is SUBORDINATE".format(ic))
                        sub_count += 1
                # at least one IC is expected to be marked master
                if master_count:
                    # no of Masters in an LI should be half of the Potashes in the LI
                    if not master_count == len(ic_list) / 2:
                        logger._warn("{} of the IC's of LI are marked as MASTER!!".format(master_count))
                        # check the number of MASTERs and SUBORDINATEs in the LI list
                        if master_count == len(ic_list):
                            logger._warn("Looks like ALL the ICs in the LI are in MASTER Role!! Something is Wrong!!")
                        error += 1
                else:
                    logger._warn("Looks like no IC's are in MASTER role!!")
                    error += 1
                # at least one IC is expected to be marked as subordinate
                if sub_count:
                    # no of Subordinates in an LI should be half of the Potashes in the LI
                    if not sub_count == len(ic_list) / 2:
                        logger._warn("{} of the IC's of LI are marked as SUBORDINATE!!".format(master_count))
                        if sub_count == len(ic_list):
                            logger._warn("Looks like ALL the ICs in the LI are in SUBORDINATE Role!! Something is Wrong!!")
                        error += 1
                else:
                    logger._warn("Looks like no IC's are marked as SUBORDINATE!!")
                    error += 1
            else:
                logger._warn("No Stacking Domain Role found for any of the ICs")
    # return false if the stacking roles are not as expected else return True if all is well
    if error > 0:
        logger._warn("Not All ICs Stacking Domain Role is correct!!")
        return False
    return True


def verify_logical_enclosure_interconnect_bay_licensing(*le_obj):
    """
    This Function verifies the Logical Enclosure Interconnect Bay Licensing values with data provided
    """
    logger.info("Navigate to Logical Enclosure page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_ENCLOSURES)

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:
        if not select_logicalenclosure(le.name):
            raise AssertionError("Unable to select Logical Enclosure '%s'.It may not be present" % le.name)

        FusionUIBase.select_view_by_name("Interconnect Bay Licensing")

        for switch_obj in le.switches:
            TBirdVerifyLogicalEnclosures.verify_le_interconnect_bay_licensing_intent(switch_obj.icmName, switch_obj.enclosure, switch_obj.intent)
            TBirdVerifyLogicalEnclosures.verify_le_interconnect_bay_licensing_icm_bay(switch_obj.icmName, switch_obj.enclosure, switch_obj.bay)
            TBirdVerifyLogicalEnclosures.verify_le_interconnect_bay_licensing_li(switch_obj.icmName, switch_obj.enclosure, switch_obj.logicalInterconnect)
    return True


def verify_logical_enclosure_interconnect_bay_licensing_editpanel(*le_obj):
    """ Verify Logical Enclosure Inerconnect Bay Licensing Edit panel.
        verifies Interconnect, License Intent & Logical Interconnect for given bay
    data file example:
    <license_intents>
        <le name= "LE1" >
        <switches>
        <switch bay= "3" enclosure= "FVTVP30001" icmName= "FVTVP30001, interconnect 3"  logicalInterconnect="LE1-lig-A"
          intent="Yes"  intentEdit="Yes automatic" logicalInterconnectEdit="LE1-lig-A" icmModel="Virtual Connect SE 40Gb F8 Module for Synergy" />
        <switch bay= "2" enclosure= "FVTVP30001" icmName= "FVTVP30001, interconnect 2" logicalInterconnect="Manually"    intent="No"
         logicalInterconnectEdit="Unmanaged" icmModel="Synergy 40Gb F8 Switch Module" intentUpdate="Yes" />

        </switches>
        </le>
    </license_intents>
    """
    logger.info("Navigate to Logical Enclosure page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_ENCLOSURES)

    if isinstance(le_obj, test_data.DataObj):
        le_obj = [le_obj]
    elif isinstance(le_obj, tuple):
        le_obj = list(le_obj[0])

    for le in le_obj:
        if not select_logicalenclosure(le.name):
            raise AssertionError("Unable to select Logical Enclosure '%s'.It may not be present" % le.name)

        FusionUIBase.select_view_by_name("Interconnect Bay Licensing")
        TBirdEditLogicalEnclosures.click_interconnect_bay_licensing_editbutton()

        for switch_obj in le.switches:
            iblrow_data = TBirdVerifyLogicalEnclosures.get_le_interconnect_bay_licensing_editpanel_Baydata(switch_obj.enclosure, switch_obj.bay, timeout=20)
            if hasattr(switch_obj, "intentEdit"):  # since we donot check this attr for "Synergy 40Gb F8 Switch", no error is thrown
                if re.search(switch_obj.intentEdit, iblrow_data):

                    logger.info(" %s Matches expected %s." % (re.search(switch_obj.intentEdit, iblrow_data).group(), switch_obj.intentEdit))
                else:
                    raise AssertionError("intent obtained %s is not same as expected %s" % ("None", switch_obj.intentEdit))
            else:
                logger.warn("no intentEdit attribute provided . Skipping intent Check")

            if re.search(switch_obj.icmModel, iblrow_data):
                logger.info(" ICM Found %s is same as expected %s" % (re.search(switch_obj.icmModel, iblrow_data).group(), switch_obj.icmModel))
            else:
                raise AssertionError("ICM  expected %s is not same as or not found" % (switch_obj.icmModel))

            if re.search(switch_obj.logicalInterconnectEdit, iblrow_data):
                logger.info(" ICM Found %s is same as expected.%s" % (re.search(switch_obj.logicalInterconnectEdit, iblrow_data).group(), switch_obj.logicalInterconnect))
            else:
                raise AssertionError("logical interconnect %s not same as or Not found" % (switch_obj.logicalInterconnectEdit))

            if switch_obj.icmModel == FusionUIConst.CONST_HAFNIUM_POTASSIUM:
                if switch_obj.intent == switch_obj.intentUpdate:
                    logger.info("\n License Intent %s is same as expected intent %s. so No action needed" % (switch_obj.intentEdit, switch_obj.intentUpdate))
                else:
                    TBirdVerifyLogicalEnclosures.toggle_le_interconnect_bay_licensing_editpanel_intent(switch_obj.enclosure, switch_obj.bay, timeout=20)

    TBirdVerifyLogicalEnclosures.click_le_interconnect_bay_licensing_editpanel_ok_button()
    return True


def verify_ic_state_of_le(permissible_ic_states=["configured", "unmanaged"], *lename):
    '''
    Function to verify the state of the Interconnect belonging to the Logical interconnects of the LE
    The default permissible states are configures and unmanaged.

    User may pass the desired states as a list of strings.

    Returns True if the IC state is in the List passed else returns false
    '''
    error = 0
    # if not in LE page navigate
    navigate()
    for n, le in enumerate(*lename):
        logger.info("logicalEnclosure No: {0} --- Total: {1} ".format((n + 1), len(lename) + 1))
        logger.info("LE name '{0}'".format(le.lename))
        # select the LE
        if not select_logical_enclosure(le.lename):
            logger.warn("Unable to select Logical Enclosure '%s'.It may not be present" % le.lename)
            error += 1
            continue

        ''' Get the  LI list in the LE . This is needed for validation '''
        li_list_ui = _get_li_list_of_le(le.lename)
        # if LI details are not retrievable abort current verification and continue to next LE FW upgrade verification
        if not li_list_ui:
            logger.warn("Unable to get logical Enclosure LI details.Hence skipping LI and IC validation for LE '{}'".format(le.lename))
            error += 1
            continue
        logger.info("LI's Part of the Logical Enclosure are -  %s" % li_list_ui)
        # verify the LI state is consistent and verify the IC states are in the permissible states list passed
        if logicalinterconnects.verify_ic_state_of_li(li_list_ui, permissible_ic_states):
            logger.info("All interconnects of the LE are in desired state")
        else:
            logger.warn("One or More Interconnects of the LE are not in desired state")
            error += 1
    # return true if no error else fails the test
    if error > 0:
        ui_lib.fail_test("validation failures observed in LE")
    return True


def verify_li_stacking_health(*firmware_obj):
    '''
    Function to verify that the Stacking Health of the LI id 'redundantly connected'
    Applicable to only IRF configurations

    Returns a boolean value
    '''
    li_stakcing_health = None
    error = 0
    # if not in LE page navigate
    navigate()

    if isinstance(firmware_obj, test_data.DataObj):
        firmware_obj = [firmware_obj]
    elif isinstance(firmware_obj, tuple):
        firmware_obj = list(firmware_obj[0])

    for fw in firmware_obj:
        # select the LE
        if not select_logical_enclosure(fw.lename):
            logger.warn("Unable to select Logical Enclosure '%s'.It may not be present" % fw.lename)
            error += 1
            continue

        ''' Get the  LI list in the LE . This is needed for validation '''
        li_list_ui = []
        li_list_ui = _get_li_list_of_le(fw.lename)

        # if LI details are not retrievable abort current verification and continue to next LE FW upgrade verification
        if not li_list_ui:
            logger.warn("Unable to get logical Enclosure LI details.Hence skipping LI and IC validation for LE '{}'".format(fw.lename))
            error += 1
            return False
        logger.info("LI's Part of the Logical Enclosure are -  %s" % li_list_ui)

        # get the stacking health of each LI and verify
        for li in li_list_ui:
            li_stakcing_health = logicalinterconnects.get_li_stacking_health(li)
            if li_stakcing_health:
                # verify if the stacking health is 'redundantly connected'
                if li_stakcing_health.lower().strip().replace(' ', '') == 'redundantlyconnected':
                    logger.info("The stacking health of the LI '{}' is 'Redundantly connected'".format(li))
                else:
                    logger.warn("The stacking health of the LI '{}' is '{}' . But it should be 'Redundantly connected'".format(li, li_stakcing_health))
                    error += 1
            else:
                logger.warn("Unable to get the LI {} stacking Health".format(li))
                error += 1

    if error > 0:
        logger.warn("Not all LI stacking Health is as expected")
        return ui_lib.fail_test("All LI stacking health status is not as expected", captureScreenshot)
    return True


def edit_potassium_interconnect_bay_licensing(le_obj):
    """ Edit Logical Enclosure Inerconnect Bay Licensing.
        Edits Interconnect, License Intent for given bay to enable or disable it
    data file example:
    <license_intents>
        <le name="LE_SYNERGY" >
            <icms>
                <icm bay= "3" enclosure= "CN744502F0" icmName= "CN744502F0, interconnect 3" logicalInterconnect="Manually" intent="No" logicalInterconnectEdit="automatic" icmModel="Virtual Connect SE 40Gb F8 Module for Synergy" intentUpdate="Yes" />
                <icm bay= "6" enclosure= "CN744502F0" icmName= "CN744502F0, interconnect 6" logicalInterconnect="Manually" intent="No" logicalInterconnectEdit="automatic" icmModel="Virtual Connect SE 40Gb F8 Module for Synergy" intentUpdate="Yes" />
            </switches>
        </le>
    </license_intents>
    """
    logger.info("Navigate to Logical Enclosure page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_ENCLOSURES)

    for le in le_obj:
        CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
        CommonOperationLogicalEnclosures.wait_for_le_selected(le.name)

        FusionUIBase.select_view_by_name("Interconnect Bay Licensing")

        for icm_obj in le.icms:
            TBirdVerifyLogicalEnclosures.verify_le_interconnect_bay_licensing_intent(icm_obj.bay, icm_obj.enclosure,
                                                                                     icm_obj.intent, timeout=10)
        TBirdEditLogicalEnclosures.click_interconnect_bay_licensing_editbutton(timeout=20)
        for icm_obj in le.icms:
            li_data = TBirdVerifyLogicalEnclosures.get_le_interconnect_bay_licensing_editpanel_Baydata(icm_obj.enclosure, icm_obj.bay, timeout=20)
            if re.search(icm_obj.icmModel, li_data):
                logger.info(" ICM Found %s is same as expected %s" % (re.search(icm_obj.icmModel, li_data).group(), icm_obj.icmModel))
            else:
                ui_lib.fail_test("ICM  expected %s is not same as or not found" % (icm_obj.icmModel))

            if re.search(icm_obj.logicalInterconnectEdit, li_data):
                logger.info(" ICM Found %s is same as expected.%s" % (re.search(icm_obj.logicalInterconnectEdit, li_data).group(), icm_obj.logicalInterconnect))
            else:
                ui_lib.fail_test("ICM %s not same as or Not found" % (icm_obj.logicalInterconnectEdit))

            if icm_obj.icmModel == FusionUIConst.CONST_HAFNIUM_POTASSIUM:
                TBirdVerifyLogicalEnclosures.toggle_le_interconnect_bay_licensing_editpanel_intent(icm_obj.enclosure, icm_obj.bay)

    TBirdVerifyLogicalEnclosures.click_le_interconnect_bay_licensing_editpanel_ok_button()
    TBirdVerifyLogicalEnclosures.wait_for_le_interconnect_bay_licensing_editpanel_ok_button_invisible(timeout=30)
    return True


def validate_potassium_interconnect_bay_licensing(le_obj):
    logger.info("Navigate to Logical Enclosure page")
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_ENCLOSURES)

    for le in le_obj:
        CommonOperationLogicalEnclosures.click_logical_enclosure(le.name)
        CommonOperationLogicalEnclosures.wait_for_le_selected(le.name)

        FusionUIBase.select_view_by_name("Interconnect Bay Licensing")

        for icm_obj in le.icms:
            TBirdVerifyLogicalEnclosures.verify_le_interconnect_bay_licensing_intent(icm_obj.bay,
                                                                                     icm_obj.enclosure,
                                                                                     icm_obj.intentUpdate)
    return True


def delete_all_appliance_logical_enclosures():
    """ Returns true if delete is successful without errors else returns the error string
    Example: Fusion UI Delete All Appliance Logical Enclosures """
    """ Navigate to Logical Interconnects Page """
    navigate()
    if not VerifyLogicalEnclosures.verify_logical_enclosures_exists():
        logger.warn("logical enclosure does not exist")
        return False
    le_list = CommonOperationLogicalEnclosures.get_logical_enclosure_list()
    count = 0
    for le_name in le_list:
        logger.info("Deleting LE: %s" % le_name)
        le_obj = test_data.DataObj()
        le_obj.add_property('name', le_name)
        le_obj = (le_obj,)
        le_delete_status = delete_tbird_logical_enclosure(le_obj)
        if le_delete_status is False:
            ui_lib.fail_test("Failed to delete LE: {0}".format(le_name))
        else:
            logger.info("'{0}' LE is deleted Successfully".format(le_name))
            count += 1
    if count == len(le_list):
        logger._log_to_console_and_log_file("All logical enclosure deleted successfully from appliance")
        return True
    else:
        ui_lib.fail_test("Failed to delete '{0}' logical enclosure from appliance".format(len(le_list) - count))
