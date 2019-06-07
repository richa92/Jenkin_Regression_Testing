# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Drive Enclosures Page
"""

from FusionLibrary.ui.business_logic.storage.drive_enclosures_elements import *
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.networking.interconnects_elements import *
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco
from datetime import datetime
from FusionLibrary.ui.business_logic.servers.enclosures_elements import GeneralEnclosuresElements


class VerifyDriveEnclosures(object):

    @classmethod
    def verify_drives_view_drive_uid_toggle(cls, drive):
        ui_lib.verify_on_off_toggle(DriveEnclosuresElements.ID_DRIVES_VIEW_UID_OFF_BY_BAY_NUMBER % drive.bay,
                                    DriveEnclosuresElements.ID_DRIVES_VIEW_UID_ON_BY_BAY_NUMBER % drive.bay)

    @classmethod
    def click_collapser_and_verify_expanded(cls, drive):
        drive_bay = drive.bay

        ui_lib.wait_for_element_and_click(
            DriveEnclosuresElements.ID_DRIVES_VIEW_COLLAPSER_BY_DRIVE_BAY_NUMBER % drive_bay,
            fail_if_false=True)

        expand_was_successful = ui_lib.wait_for_element(
            DriveEnclosuresElements.ID_DRIVES_VIEW_EXPANDED_COLLAPSER_BY_DRIVE_BAY_NUMBER % drive_bay)

        if expand_was_successful:
            logger.info("Collapser expanded successfully for Drive: %s" % drive_bay)
        else:
            ui_lib.fail_test("Collapser did not expand successfully for Drive: %s" % drive_bay)

    @classmethod
    def verify_drives_view_drive_expander_fields(cls, drive):
        ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVES_VIEW_SERIAL_NUMBER_BY_BAY_NUMBER %
                                (drive.bay, drive.serial_number), fail_if_false=True)
        logger.info("Succesfully verified that drive %s has expected Serial Number: %s" % (drive.bay, drive.serial_number))

        ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVES_VIEW_AUTHENTIC_BY_BAY_NUMBER %
                                (drive.bay, drive.authentic), fail_if_false=True)
        logger.info("Succesfully verified that drive %s has expected Authentic: %s" % (drive.bay, drive.authentic))

        ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVES_VIEW_FIRMWARE_BY_BAY_NUMBER %
                                (drive.bay, drive.firmware), fail_if_false=True)
        logger.info("Succesfully verified that drive %s has expected Firmware: %s" % (drive.bay, drive.firmware))

        ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVES_VIEW_LINK_RATE_BY_BAY_NUMBER %
                                (drive.bay, drive.link_rate), fail_if_false=True)
        logger.info("Succesfully verified that drive %s has expected Link Rate: %s" % (drive.bay, drive.link_rate))

        ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVES_VIEW_RPM_BY_BAY_NUMBER %
                                (drive.bay, drive.rpm), fail_if_false=True)
        logger.info("Succesfully verified that drive %s has expected RPM: %s" % (drive.bay, drive.rpm))

        ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVES_VIEW_TEMPERATURE_BY_BAY_NUMBER %
                                (drive.bay, drive.temperature), fail_if_false=True)
        logger.info("Succesfully verified that drive %s has expected Temperature: %s" % (drive.bay, drive.temperature))

    @classmethod
    def verify_collapser(cls, drive):
        drive_bay = drive.bay

        if drive.model == 'empty':
            logger.info("Drive Bay: %s is empty. Has no collapser to verify", drive_bay)
        else:
            cls.click_collapser_and_verify_expanded(drive)
            cls.verify_drives_view_drive_expander_fields(drive)

    @classmethod
    def verify_drives_view_drive_server_profile(cls, drive):
        drive_bay = drive.bay
        drive_server_profile = drive.server_profile

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_SERVER_PROFILE_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive_server_profile:
            logger.info("Successfully verified that Drive %s has expected Server Profile of '%s'" % (drive_bay, drive_server_profile))
        else:
            ui_lib.fail_test("Server Profile: %s of Drive: %s did not match expected Server Profile: '%s'" % (text, drive_bay, drive_server_profile))

    @classmethod
    def verify_drives_view_drive_logical_jbod(cls, drive):
        drive_bay = drive.bay
        drive_logical_jbod = drive.logical_jbod

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_LOGICAL_JBOD_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive_logical_jbod:
            logger.info("Successfully verified that Drive %s has expected Logical JBOD of '%s'" % (drive_bay, drive_logical_jbod))
        else:
            ui_lib.fail_test("Logical JBOD: %s of Drive: %s did not match expected Logical JBOD: '%s'" % (text, drive_bay, drive_logical_jbod))

    @classmethod
    def verify_drives_view_drive_firmware(cls, drive):
        drive_bay = drive.bay
        drive_firmware = drive.firmware

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_DRIVE_BAY_BY_NUMBER % drive_bay
                               + "/" + DriveEnclosuresElements.ID_DRIVES_VIEW_FIRMWARE_POSITION, fail_if_false=True)
        if text == drive_firmware:
            logger.info("Successfully verified that Drive %s has expected Firmware of '%s'" % (drive_bay, drive_firmware))
        else:
            ui_lib.fail_test("Firmware: %s of Drive: %s did not match expected Firmware: '%s'" % (text, drive_bay, drive_firmware))

    @classmethod
    def verify_drives_view_drive_capacity(cls, drive):
        drive_bay = drive.bay
        drive_capacity = drive.capacity

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_CAPACITY_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL_TYPE_AND_CAPACITY %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive_capacity:
            logger.info("Successfully verified that Drive %s has expected Capacity of '%s'" % (drive_bay, drive_capacity))
        else:
            ui_lib.fail_test("Capacity: %s of Drive: %s did not match expected Capacity: '%s'" % (text, drive_bay, drive_capacity))

    @classmethod
    def verify_drives_view_drive_type(cls, drive):
        drive_bay = drive.bay
        drive_type = drive.type

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_TYPE_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL_TYPE_AND_CAPACITY %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive_type:
            logger.info("Successfully verified that Drive %s has expected Type of '%s'" % (drive_bay, drive_type))
        else:
            ui_lib.fail_test("Type: %s of Drive: %s did not match expected Type: '%s'" % (text, drive_bay, drive_type))

    @classmethod
    def verify_drives_view_drive_status(cls, drive):
        drive_bay = drive.bay
        drive_status = drive.status

        ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVES_VIEW_STATUS_BY_BAY_NUMBER
                                % (drive_bay, drive_status), fail_if_false=True)

        logger.info("Successfully verified that Drive: %s has Status: %s" % (drive_bay, drive_status))

    @classmethod
    def verify_drives_view_drive_model(cls, drive):
        drive_bay = drive.bay

        index_in_table_head = ui_lib.get_html_element_index_in_row(
            DriveEnclosuresElements.ID_ROW_DRIVES_VIEW_TABLE_HEAD,
            DriveEnclosuresElements.ID_DRIVES_VIEW_MODEL_COLUMN_HEAD)

        text = ui_lib.get_text(DriveEnclosuresElements.ID_DRIVES_VIEW_TABLE_CELL %
                               (drive_bay, str(index_in_table_head)), fail_if_false=True)

        if text == drive.model:
            logger.info("Successfully verified that Drive %s has expected Model of '%s'" % (drive_bay, drive.model))
        else:
            ui_lib.fail_test("Drive Model: %s of Drive: %s did not match expected Drive Status: '%s'" % (text, drive_bay, drive.model))

    @classmethod
    def verify_bay_hover_over_uid(cls, drive):
        ui_lib.verify_on_off_toggle(DriveEnclosuresElements.ID_DRIVE_UID_OFF_IN_HOVER_OVER % drive.bay,
                                    DriveEnclosuresElements.ID_DRIVE_UID_ON_IN_HOVER_OVER % drive.bay)

    @classmethod
    def verify_bay_hover_over(cls, drive):
        drive_bay = drive.bay
        drive_status = drive.status
        drive_capacity = drive.capacity
        drive_type = drive.type
        drive_logical_jbod = drive.logical_jbod
        drive_server_profile = drive.server_profile

        if drive.model == 'empty':
            logger.info('''Skipping verification of hover over for empty bay.
                        No information for hover over to display''')
        else:
            ui_lib.move_to_element_verify_visible_move_away(
                DriveEnclosuresElements.ID_DRIVE_BAY_BY_NUMBER % drive_bay,
                DriveEnclosuresElements.ID_DRIVE_STATUS_IN_HOVER_OVER % drive_status,
                DriveEnclosuresElements.ID_DRIVE_BAY_NUMBER_IN_HOVER_OVER % drive_bay,
                DriveEnclosuresElements.ID_DRIVE_TYPE_IN_HOVER_OVER % drive_type,
                DriveEnclosuresElements.ID_DRIVE_CAPACITY_IN_HOVER_OVER % drive_capacity,
                DriveEnclosuresElements.ID_DRIVE_LOGICAL_JBOD_IN_HOVER_OVER % drive_logical_jbod,
                DriveEnclosuresElements.ID_DRIVE_SERVER_PROFILE_IN_HOVER_OVER % drive_server_profile)

            # Add back in after F636 is dev complete
            # cls.verify_bay_hover_over_uid()

    @classmethod
    def verify_bay_status(cls, drive):
        drive_bay = drive.bay
        drive_status = drive.status

        if drive.model == 'empty':
            logger.info('Skipping verification of status for empty bay %s' % drive_bay)
        else:
            ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVE_BAY_STATUS_BY_BAY_NUMBER
                                    % (drive_bay, drive_status), fail_if_false=True)
            logger.info('Successfully verified that Bay %s has expected Status: %s' % (drive_bay, drive_status))

    @classmethod
    def verify_bay_uid_toggle(cls, drive):
        ui_lib.verify_on_off_toggle(DriveEnclosuresElements.ID_DRIVE_BAY_UID_OFF_BY_BAY_NUMBER % drive.bay,
                                    DriveEnclosuresElements.ID_DRIVE_BAY_UID_ON_BY_BAY_NUMBER % drive.bay)

    @classmethod
    def verify_bay_displays_correct_capacity(cls, drive):
        drive_bay = drive.bay
        drive_capacity = drive.capacity

        if drive.model == 'empty':
            ui_lib.wait_for_element(DriveEnclosuresElements.ID_EMPTY_DRIVE_BAY_BY_NUMBER_AND_CAPACITY
                                    % (drive_bay), fail_if_false=True)
            logger.info('Successfully verified that drive bay %s has a capacity of empty' % drive_bay)
        else:
            ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVE_BAY_BY_NUMBER_AND_CAPACITY
                                    % (drive_bay, drive_capacity), fail_if_false=True)
            logger.info('Successfully verified that drive bay %s has a capacity of %s' % (drive_bay, drive_capacity))

    @classmethod
    def verify_bay_exists(cls, drive):
        drive_bay = drive.bay

        if drive.model == 'empty':
            ui_lib.wait_for_element(DriveEnclosuresElements.ID_EMPTY_DRIVE_BAY_BY_NUMBER % drive_bay, fail_if_false=True)
        else:
            ui_lib.wait_for_element(DriveEnclosuresElements.ID_DRIVE_BAY_BY_NUMBER % drive_bay, fail_if_false=True)

        logger.info("Successfully verified that bay %s exists" % drive_bay)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_not_exist(cls, drive_enclosure, timeout=10, fail_if_false=True):
        logger.info("verify [ DRIVE ENCLOSURE '%s' ] is not existing" % drive_enclosure)
        ui_lib.wait_for_element_notvisible(DriveEnclosuresElements.ID_TABLE_DRIVE_ENCLOSURES % drive_enclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosures_exist(cls, drive_enclosure, timeout=10, fail_if_false=True):
        logger.info("verify [ DRIVE ENCLOSURE '%s' ] is existing" % drive_enclosure)
        ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_TABLE_DRIVE_ENCLOSURES % drive_enclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_title(cls, drive_enclosure, timeout=10, fail_if_false=True):
        logger.info('verifying [ Drive Enclosure title %s ] is visible' % drive_enclosure)
        ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_DRIVE_ENCLOSURE_TITLE % drive_enclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_is_selected(cls, drive_enclosure, timeout=10, fail_if_false=True):
        logger.info('verify [Drive Enclosure %s ] is selected' % drive_enclosure)
        ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE_SELECTED % drive_enclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_drive_enclosure_link(cls, drive_enclosure, timeout=10, fail_if_false=True):
        logger.info('Clicking [Drive Enclosure %s] link from Enclosure page' % drive_enclosure)
        ui_lib.wait_for_element_and_click(DriveEnclosuresElements.ID_ENCLOSURE_SERVER_BAY_LINK % drive_enclosure, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_state(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ State ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("state", DriveEnclosuresElements.ID_TEXT_STATE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_power(cls, view, expect_value, timeout=10, fail_if_false=True):
        logger.info("verify [ Power ] in %s view, expected value is [ %s ]" % (view, expect_value))
        ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_TEXT_POWER, timeout, fail_if_false)
        FusionUIBase.verify_element_text("power", DriveEnclosuresElements.ID_TEXT_POWER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_logical_interconnect(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Logical interconnect ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Logical interconnect", DriveEnclosuresElements.ID_TEXT_LOGICAL_INTERCONNECT, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_number_of_drives(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Number of drives ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Number of drives", DriveEnclosuresElements.ID_NUMBER_OF_DRIVES, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_temperature(cls, view, expect_value, timeout=5, fail_if_false=True):
        if expect_value:
            logger.info("verify [ Temperature ] in %s view, expected value is [ %s ]" % (view, expect_value))
            FusionUIBase.verify_element_text("Temperature", DriveEnclosuresElements.ID_TEMPERATURE, expect_value, timeout, fail_if_false)
        else:
            temperature = ui_lib.get_text(DriveEnclosuresElements.ID_TEMPERATURE, timeout=10, fail_if_false=True)
            try:
                tempvalue = int(temperature)
                logger.info('Drive enclosure temperature is %s' % tempvalue)
            except ValueError:
                logger.info('Driver enclosure temperature is not integer -- %s' % temperature)
                ui_lib.fail_test('Driver enclosure temperature is not integer -- %s' % temperature)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_model(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Model ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Model", DriveEnclosuresElements.ID_DRIVE_ENCLOSURE_MODEL, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_interconnect_bay_set(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Interconnect bay set ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Interconnect bay set", DriveEnclosuresElements.ID_INTERCONNECT_BAY_SET, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_serial_number(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Serial number ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Serial number", DriveEnclosuresElements.ID_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_part_number(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Part number ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Part number", DriveEnclosuresElements.ID_PART_NUMBER, expect_value, timeout, fail_if_false)

#  Firmware

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_io_adapter1(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Firmware ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Firmware", DriveEnclosuresElements.ID_FIRMWARE_1, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_firmware_io_adapter2(cls, view, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ Firmware ] in %s view, expected value is [ %s ]" % (view, expect_value))
        FusionUIBase.verify_element_text("Firmware", DriveEnclosuresElements.ID_FIRMWARE_2, expect_value, timeout, fail_if_false)

# UID

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_drive_enclosure_uid(cls, drive_enclosure_name, expect_value, timeout=5, fail_if_false=True):
        logger.info("verify [ UID ] in Overview, expected value is [ %s ]" % expect_value)
        if 'off' in expect_value.lower():
            ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_STATUS_UID_LIGHT_OFF, timeout, fail_if_false)
            logger.debug("drive_enclosure UID '%s' status is 'off' as expected." % drive_enclosure_name)
        else:
            ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_STATUS_UID_LIGHT_ON, timeout, fail_if_false)
            logger.debug("drive_enclosure UID '%s' status is 'on' as expected." % drive_enclosure_name)


class CommonOperationDriveEnclosure(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_drive_enclosure_status_ok_or_warn(cls, drive_enclosure_name, timeout=10, fail_if_false=True):
        start = datetime.now()
        # logger.warn("________________________________")
        logger.debug("waiting for drive_enclosure hardware '%s' status change to 'ok' or 'warn' ..." % drive_enclosure_name)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_STATUS_DRIVE_ENCLOSURE_OK % drive_enclosure_name, timeout=5, fail_if_false=False):
                logger.debug("drive_enclosure hardware '%s' status is 'ok' as expected." % drive_enclosure_name)
                return True
            elif ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_STATUS_DRIVE_ENCLOSURE_WARN % drive_enclosure_name, timeout=5, fail_if_false=False):
                logger.debug("drive_enclosure hardware '%s' status is 'warn' as expected." % drive_enclosure_name)
                return True
            elif ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_STATUS_DRIVE_ENCLOSURE_ERROR % drive_enclosure_name, timeout=5, fail_if_false=False):
                err_msg = "drive_enclosure hardware '%s' status is 'error' not as expected." % drive_enclosure_name
                ui_lib.fail_test(err_msg)
            else:
                logger.debug("drive_enclosure hardware '%s' status is unknown, waiting ..." % drive_enclosure_name)
                continue
        err_msg = "Timeout to waiting drive_enclosure hardware '%s' status change to 'ok' or 'warn'." % drive_enclosure_name
        ui_lib.fail_test(err_msg)


class PowerOnDriveEnclosure(object):

    @classmethod
    def select_action_power_on(cls, timeout=5):
        logger.debug("click 'Actions' menu and select 'Power on'")
        ui_lib.wait_for_element_and_click(DriveEnclosuresElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(PowerOnDriveEnclosureElements.ID_SELECT_ACTION_POWER_ON, timeout, fail_if_false=True)

    @classmethod
    def click_power_on_button(cls, timeout=5):
        logger.debug("click 'Power on' button ...")
        ui_lib.wait_for_element_and_click(PowerOnDriveEnclosureElements.ID_SELECT_ACTION_POWER_ON, timeout, fail_if_false=True)


class PowerOffDriveEnclosure(object):

    @classmethod
    def select_action_power_off(cls, timeout=5):
        logger.debug("select action 'Power off'")
        ui_lib.wait_for_element_and_click(DriveEnclosuresElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(PowerOffDriveEnclosureElements.ID_SELECT_ACTION_POWER_OFF, timeout, fail_if_false=True)

    @classmethod
    def click_power_off_button_confirm_yes(cls, timeout=5):
        logger.debug('click button Yes, Power off')
        ui_lib.wait_for_element_and_click(PowerOffDriveEnclosureElements.ID_BUTTON_POWEROFF_CONFIRM_YES, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(PowerOffDriveEnclosureElements.ID_BUTTON_POWEROFF_CONFIRM_CANCEL, timeout=timeout, fail_if_false=True)


class ResetDriveEnclosure(object):

    @classmethod
    def select_action_reset(cls, timeout=5):
        logger.debug("select action 'Reset'")
        ui_lib.wait_for_element_and_click(DriveEnclosuresElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(ResetDriveEnclosureElements.ID_SELECT_ACTION_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_reset_button(cls, timeout=5):
        logger.debug("click button 'Reset'")
        ui_lib.wait_for_element_and_click(ResetDriveEnclosureElements.ID_BUTTON_RESET, timeout, fail_if_false=True)

    @classmethod
    def click_reset_button_confirm_yes(cls, timeout=5):
        logger.debug("click Yes, Reset")
        ui_lib.wait_for_element_and_click(ResetDriveEnclosureElements.ID_BUTTON_RESET_CONFIRM_YES, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        logger.debug("click button 'Cancel'")
        ui_lib.wait_for_element_and_click(ResetDriveEnclosureElements.ID_BUTTON_RESET_CONFIRM_CANCEL, timeout=timeout, fail_if_false=True)


class RefreshDriveEnclosure(object):

    @classmethod
    def select_action_refresh(cls, timeout=5):
        logger.debug("select action 'Refresh'")
        ui_lib.wait_for_element_and_click(DriveEnclosuresElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RefreshDriveEnclosureElements.ID_SELECT_ACTION_REFRESH, timeout, fail_if_false=True)


class TurnOnDriveEnclosureUID(object):

    @classmethod
    def click_uid_button(cls, timeout=5):
        logger.debug("click button 'UID' to turn on")
        ui_lib.wait_for_element_and_click(DriveEnclosuresElements.ID_BUTTON_UID_LIGHT, timeout, fail_if_false=True)

    @classmethod
    def wait_until_uid_on(cls, drive_enclosure_name, timeout=160, fail_if_false=True):
        logger.debug("waiting for drive_enclosure UID '%s' status to turn On ..." % drive_enclosure_name)
        ui_lib.wait_for_element_visible(DriveEnclosuresElements.ID_STATUS_UID_LIGHT_ON, timeout, fail_if_false=True)


class TurnOffDriveEnclosureUID(object):

    @classmethod
    def click_uid_button(cls, timeout=5):
        logger.debug("click button 'UID' to turn off")
        ui_lib.wait_for_element_and_click(DriveEnclosuresElements.ID_BUTTON_UID_LIGHT, timeout, fail_if_false=True)

    @classmethod
    def wait_until_uid_off(cls, drive_enclosure_name, timeout, fail_if_false=True):
        logger.debug("waiting for drive_enclosure UID '%s' status to go off ..." % drive_enclosure_name)
        ui_lib.wait_for_element_notvisible(DriveEnclosuresElements.ID_STATUS_UID_LIGHT_ON, timeout, fail_if_false=True)
