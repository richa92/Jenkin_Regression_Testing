from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.servers.enclosures_elements import GeneralEnclosuresElements
from FusionLibrary.ui.business_logic.servers.enclosures import TBirdCommonOperationEnclosures
from FusionLibrary.ui.business_logic.storage.drive_enclosures import *


def verify_drives_view(drive_enclosure_object):
    for drive_enclosure in drive_enclosure_object:
        FusionUIBase.click_item_from_master_table(drive_enclosure.name)
        FusionUIBase.select_view_by_name('Drives')

        logger.info("Verifying Drives View for Drive Enclosure: %s" % drive_enclosure.name)

        for drive in drive_enclosure.drives:
            VerifyDriveEnclosures.verify_drives_view_drive_status(drive)
            VerifyDriveEnclosures.verify_drives_view_drive_model(drive)
            VerifyDriveEnclosures.verify_drives_view_drive_type(drive)
            VerifyDriveEnclosures.verify_drives_view_drive_capacity(drive)
            VerifyDriveEnclosures.verify_drives_view_drive_logical_jbod(drive)
            VerifyDriveEnclosures.verify_drives_view_drive_server_profile(drive)

            if drive.model == 'empty':
                logger.info('No further verification required for empty drive in bay %s' % drive.bay)
            else:
                # Add back in after F636 is dev complete
                # VerifyDriveEnclosures.verify_drives_view_drive_uid_toggle(drive)
                VerifyDriveEnclosures.verify_collapser(drive)


def verify_component_view(drive_enclosure_object):
    for drive_enclosure in drive_enclosure_object:
        FusionUIBase.click_item_from_master_table(drive_enclosure.name)
        FusionUIBase.select_view_by_name('Overview')

        logger.info("Verifying Component View for Drive Enclosure: %s", drive_enclosure.name)

        for drive in drive_enclosure.drives:
            VerifyDriveEnclosures.verify_bay_exists(drive)
            VerifyDriveEnclosures.verify_bay_displays_correct_capacity(drive)

            if drive.model == 'empty':
                logger.info('No more verification required for empty drive in bay %s' % drive.bay)
            else:
                VerifyDriveEnclosures.verify_bay_status(drive)
                # Add back in after F636 is dev complete
                # VerifyDriveEnclosures.verify_bay_uid_toggle(drive)
                VerifyDriveEnclosures.verify_bay_hover_over(drive)


def verify_drives_link(drive_enclosure_object):
    for drive_enclosure in drive_enclosure_object:
        logger.info("Verifying Drives View for Drive Enclosure: %s", drive_enclosure.name)

        FusionUIBase.click_item_from_master_table(drive_enclosure.name)
        FusionUIBase.select_view_by_name('Overview')
        ui_lib.wait_for_element_and_click("link=Drives", fail_if_false=True)
        FusionUIBase.verify_view_by_name('Drives')


def validate_drive_enclosure_configuration(drive_enclosures_object):
    """
    Verify Drive enclosure configuration

    Example:
    <drive_enclosures>
            <drive_enclosure name="CN75120D7B, bay 3"
               state="Monitored"
               model="D3940 Stor Mod"
               power="On"
               logical_interconnect="none"
               number_of_drives="5"
               temperature=""
               interconnect_bay_set="1"
               serial_number="CN7452061Q"
               part_number="none"
               io_adapter_1="1.04"
               >
               <drives>
                   <item bay="1" status="/^warning|ok|error$/i" model="MM2000JEFRC" Type="SAS Unknown" Capacity="1 TiB" Firmware="HP01" RPM="na" Logical_JBOD="none" server_profile="none"/>
                   <item bay="6" status="/^warning|ok|error$/i" model="empty" Type="" Capacity="" Firmware="" RPM="" Logical_JBOD="" server_profile=""/>
               </drives>
               <io_adapters>
                    <item bay="1" status="/^warning|ok|error$/i" model="D3940 Stor Mod" state="linked" serial_number="PENTF0XRH7Q08O"/>
                </io_adapters>
            </drive_enclosure>
            </drive_enclosures>
    """

    logger.info("Validating drive enclosures")

    logger.info("Navigating to Drive Enclosures page")
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES)

    for de_obj in drive_enclosures_object:

        select_drive_enclosure(de_obj.name)

        verify_overview_section(de_obj)
        verify_general_section(de_obj)
        verify_hardware_section(de_obj)
        verify_firmware_section(de_obj)
        verify_io_adapters_section(de_obj)
        navigate_activity_section(de_obj)
        navigate_map_section(de_obj)
        navigate_labels_section(de_obj)
        verify_de_from_enclosure_page(de_obj)

#  Overview


def verify_overview_section(de_obj):

    FusionUIBase.select_view_by_name('Overview')
    logger.info("Verifying configuration in Overview view...")

    # if hasattr(de_obj, "drive_enclosures"):
    #     VerifyDriveEnclosures.verify_drive_enclosures_exist(de_obj.logical_interconnect)

    if hasattr(de_obj, "state"):
        VerifyDriveEnclosures.verify_drive_enclosure_state('Overview', de_obj.state)

    if hasattr(de_obj, "power"):
        VerifyDriveEnclosures.verify_drive_enclosure_power('Overview', de_obj.power)

    if hasattr(de_obj, "logical_interconnect"):
        VerifyDriveEnclosures.verify_drive_enclosure_logical_interconnect('Overview', de_obj.logical_interconnect)

    if hasattr(de_obj, "number_of_drives"):
        VerifyDriveEnclosures.verify_drive_enclosure_number_of_drives('Overview', de_obj.number_of_drives)

    if hasattr(de_obj, "temperature"):
        VerifyDriveEnclosures.verify_drive_enclosure_temperature('Overview', de_obj.temperature)

    if hasattr(de_obj, "model"):
        VerifyDriveEnclosures.verify_drive_enclosure_model('Overview', de_obj.model)

    if hasattr(de_obj, "interconnect_bay_set"):
        VerifyDriveEnclosures.verify_drive_enclosure_interconnect_bay_set('Overview', de_obj.interconnect_bay_set)

#  General


def verify_general_section(de_obj):

    FusionUIBase.select_view_by_name('General')
    logger.info("Verifying configuration in General view...")

    if hasattr(de_obj, "state"):
        VerifyDriveEnclosures.verify_drive_enclosure_state('General', de_obj.state)

    if hasattr(de_obj, "power"):
        VerifyDriveEnclosures.verify_drive_enclosure_power('General', de_obj.power)

    if hasattr(de_obj, "logical_interconnect"):
        VerifyDriveEnclosures.verify_drive_enclosure_logical_interconnect('General', de_obj.logical_interconnect)

    if hasattr(de_obj, "number_of_drives"):
        VerifyDriveEnclosures.verify_drive_enclosure_number_of_drives('General', de_obj.number_of_drives)

#  Hardware


def verify_hardware_section(de_obj):

    FusionUIBase.select_view_by_name('Hardware')
    logger.info("Verifying Enclosure configuration in Hardware view...")

    if hasattr(de_obj, "temperature"):
        VerifyDriveEnclosures.verify_drive_enclosure_temperature('Hardware', de_obj.temperature)

    if hasattr(de_obj, "model"):
        VerifyDriveEnclosures.verify_drive_enclosure_model('Hardware', de_obj.model)

    if hasattr(de_obj, "interconnect_bay_set"):
        VerifyDriveEnclosures.verify_drive_enclosure_interconnect_bay_set('Hardware', de_obj.interconnect_bay_set)

    if hasattr(de_obj, "serial_number"):
        VerifyDriveEnclosures.verify_drive_enclosure_serial_number('Hardware', de_obj.serial_number)

    if hasattr(de_obj, "part_number"):
        VerifyDriveEnclosures.verify_drive_enclosure_part_number('Hardware', de_obj.part_number)

#  Firmware


def verify_firmware_section(de_obj):

    FusionUIBase.select_view_by_name('Firmware')
    logger.info("Verifying configuration in Firmware view...")

    if hasattr(de_obj, "io_adapter_1"):
        VerifyDriveEnclosures.verify_firmware_io_adapter1('Firmware', de_obj.io_adapter_1)

    if hasattr(de_obj, "io_adapter_2"):
        VerifyDriveEnclosures.verify_firmware_io_adapter2('Firmware', de_obj.io_adapter_2)


def verify_io_adapters_section(de_obj):
    FusionUIBase.select_view_by_name('I/O Adapters')
    logger.info("Verifying configuration in I/O Adapters view...")


def navigate_activity_section(de_obj):
    FusionUIBase.select_view_by_name('Activity')
    logger.info("Navigating to Activity view...")


def navigate_map_section(de_obj):
    FusionUIBase.select_view_by_name('Map')
    logger.info("Navigating to Map view...")


def navigate_labels_section(de_obj):
    FusionUIBase.select_view_by_name('Labels')
    logger.info("Navigating to Labels view...")


def select_drive_enclosure(drive_enclosure_name):
    logger.info("Selecting an enclosure with name %s" % drive_enclosure_name)
    ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % drive_enclosure_name, fail_if_false=True)
    ui_lib.wait_for_element_and_click(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE % drive_enclosure_name, fail_if_false=True)
    ui_lib.wait_for_element_visible(GeneralEnclosuresElements.ID_TABLE_ENCLOSURE_SELECTED % drive_enclosure_name, fail_if_false=True)


def verify_de_from_enclosure_page(de_obj):
    """  Reset 1 or multiple drive_enclosure Hardware

    """

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURES, time_for_loading=5)
    logger.info("Verifying Drive enclosure link '%s' from Enclosure's page" % de_obj.name)
    enclosure = de_obj.name.split(',')
    enclosure = enclosure[0]
    TBirdCommonOperationEnclosures.click_enclosure(enclosure, timeout=10)
    TBirdCommonOperationEnclosures.wait_enclosure_selected(enclosure, timeout=10, fail_if_false=True)
    VerifyDriveEnclosures.click_drive_enclosure_link(de_obj.name, timeout=10, fail_if_false=True)
    VerifyDriveEnclosures.verify_drive_enclosure_title(de_obj.name, timeout=10, fail_if_false=True)
    VerifyDriveEnclosures.verify_drive_enclosure_is_selected(de_obj.name, timeout=10, fail_if_false=True)


def power_off_drive_enclosure(drive_enclosures_object):
    """ Power off 1 or multiple drive enclosure

    """
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES, time_for_loading=5)

    for de_obj in drive_enclosures_object:
        logger.info("powering off a drive enclosure named '%s'" % de_obj.name)
        VerifyDriveEnclosures.verify_drive_enclosures_exist(de_obj.name, fail_if_false=True)
        select_drive_enclosure(de_obj.name)
        FusionUIBase.select_view_by_name(view_name='Overview', timeout=5, fail_if_false=True)
        VerifyDriveEnclosures.verify_drive_enclosure_power('overview', expect_value='On', timeout=10, fail_if_false=True)
        PowerOffDriveEnclosure.select_action_power_off()
        PowerOffDriveEnclosure.click_power_off_button_confirm_yes()
        FusionUIBase.show_activity_sidebar()
        if FusionUIBase.wait_activity_action_ok_or_warn(de_obj.name, 'Power off', timeout=300, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            if CommonOperationDriveEnclosure.wait_drive_enclosure_status_ok_or_warn(de_obj.name, timeout=180, fail_if_false=False) is True:
                logger.info("drive enclosure '%s' is successfully Power off" % de_obj.name)
            else:
                logger.warn("drive enclosure '%s' is NOT successfully Power off or error occurred due to its status is neither 'ok' nor 'warn'" % de_obj.name)
                ui_lib.fail_test("drive enclosure '%s' is NOT successfully Power off or error occurred due to its status is neither 'ok' nor 'warn'" % de_obj.name)
        else:
            logger.warn("drive enclosure '%s' is NOT successfully Power off" % de_obj.name)
            ui_lib.fail_test("drive enclosure '%s' is NOT successfully Power off or error occurred due to its status is neither 'ok' nor 'warn'" % de_obj.name)


def power_on_drive_enclosure(drive_enclosures_object):
    """ Power on 1 or multiple drive enclosure

    """
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES, time_for_loading=5)

    for de_obj in drive_enclosures_object:
        logger.info("powering on a drive enclosure named '%s'" % de_obj.name)
        VerifyDriveEnclosures.verify_drive_enclosures_exist(de_obj.name, fail_if_false=True)
        select_drive_enclosure(de_obj.name)
        FusionUIBase.select_view_by_name(view_name='Overview', timeout=5, fail_if_false=True)
        VerifyDriveEnclosures.verify_drive_enclosure_power('overview', expect_value='Off', timeout=10, fail_if_false=True)
        PowerOnDriveEnclosure.select_action_power_on()
        FusionUIBase.show_activity_sidebar()
        if FusionUIBase.wait_activity_action_ok_or_warn(de_obj.name, 'Power on', timeout=300, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            if CommonOperationDriveEnclosure.wait_drive_enclosure_status_ok_or_warn(de_obj.name, timeout=180, fail_if_false=False) is True:
                logger.info("drive enclosure '%s' is successfully Power On" % de_obj.name)
            else:
                logger.warn("drive enclosure '%s' is NOT successfully Power On or error occurred due to its status is neither 'ok' nor 'warn'" % de_obj.name)
                ui_lib.fail_test("drive enclosure '%s' is NOT successfully Power On or error occurred due to its status is neither 'ok' nor 'warn'" % de_obj.name)
        else:
            logger.warn("drive enclosure '%s' is NOT successfully Power On" % de_obj.name)
            ui_lib.fail_test("drive enclosure '%s' is NOT successfully Power On or error occurred due to its status is neither 'ok' nor 'warn'" % de_obj.name)


def refresh_drive_enclosure(drive_enclosure_obj):
    """ Refresh 1 or multiple drive_enclosure Hardware

    """
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES, time_for_loading=5)

    for drive_enclosure in drive_enclosure_obj:
        logger.info("refresh a drive_enclosure hardware named '%s'" % drive_enclosure.name)
        VerifyDriveEnclosures.verify_drive_enclosures_exist(drive_enclosure.name, fail_if_false=True)
        select_drive_enclosure(drive_enclosure.name)
        FusionUIBase.select_view_by_name(view_name='Overview', timeout=5, fail_if_false=True)
        RefreshDriveEnclosure.select_action_refresh()
        FusionUIBase.show_activity_sidebar()
        if FusionUIBase.wait_activity_action_ok_or_warn(drive_enclosure.name, 'Refresh', timeout=300, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            if CommonOperationDriveEnclosure.wait_drive_enclosure_status_ok_or_warn(drive_enclosure.name, timeout=180, fail_if_false=False) is True:
                logger.info("drive_enclosure '%s' is successfully refreshed" % drive_enclosure.name)
            else:
                logger.warn("drive_enclosure '%s' is NOT successfully refreshed" % drive_enclosure.name)
                ui_lib.fail_test("drive enclosure '%s' is NOT successfully refreshed or error occurred due to its status is neither 'ok' nor 'warn'" % drive_enclosure.name)

        else:
            logger.warn("drive enclosure '%s' is NOT successfully refreshed" % drive_enclosure.name)
            ui_lib.fail_test("drive enclosure '%s' is NOT successfully refreshed or error occurred due to its status is neither 'ok' nor 'warn'" % drive_enclosure.name)


def reset_drive_enclosure(drive_enclosure_obj):
    """ Reset 1 or multiple drive_enclosure Hardware

    """
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES, time_for_loading=5)

    for drive_enclosure in drive_enclosure_obj:
        logger.info("reset a drive_enclosure hardware named '%s'" % drive_enclosure.name)
        VerifyDriveEnclosures.verify_drive_enclosures_exist(drive_enclosure.name, fail_if_false=False)
        select_drive_enclosure(drive_enclosure.name)
        FusionUIBase.select_view_by_name(view_name='Overview', timeout=5, fail_if_false=False)
        VerifyDriveEnclosures.verify_drive_enclosure_power('Overview', expect_value='On', timeout=10, fail_if_false=True)
        ResetDriveEnclosure.select_action_reset()
        ResetDriveEnclosure.click_reset_button_confirm_yes()
        FusionUIBase.show_activity_sidebar()
        if FusionUIBase.wait_activity_action_ok_or_warn(drive_enclosure.name, 'Reset', timeout=300, fail_if_false=False) is True:
            FusionUIBase.show_activity_sidebar()
            if CommonOperationDriveEnclosure.wait_drive_enclosure_status_ok_or_warn(drive_enclosure.name, timeout=180, fail_if_false=False) is True:
                logger.info("drive_enclosure '%s' is successfully reset" % drive_enclosure.name)
            else:
                logger.warn("drive_enclosure '%s' is NOT successfully reset" % drive_enclosure.name)
                ui_lib.fail_test("drive enclosure '%s' is NOT successfully reset or error occurred due to its status is neither 'ok' nor 'warn'" % drive_enclosure.name)
        else:
            logger.warn("drive enclosure '%s' is NOT successfully reset" % drive_enclosure.name)
            ui_lib.fail_test("drive enclosure '%s' is NOT successfully reset or error occurred due to its status is neither 'ok' nor 'warn'" % drive_enclosure.name)


def turn_on_drive_enclosure_uid(drive_enclosure_obj):
    """ Turn off UI for 1 or multiple drive_enclosure Hardware

    """
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES, time_for_loading=5)

    for drive_enclosure in drive_enclosure_obj:
        logger.info("Turning on UID named '%s'" % drive_enclosure.name)
        select_drive_enclosure(drive_enclosure.name)
        VerifyDriveEnclosures.verify_drive_enclosure_uid(drive_enclosure.name, expect_value='Off', timeout=10, fail_if_false=True)
        TurnOnDriveEnclosureUID.click_uid_button()
        TurnOnDriveEnclosureUID.wait_until_uid_on(drive_enclosure.name, timeout=120, fail_if_false=True)
        VerifyDriveEnclosures.verify_drive_enclosure_uid(drive_enclosure.name, expect_value='On', timeout=60, fail_if_false=True)


def turn_off_drive_enclosure_uid(drive_enclosure_obj):
    """ Turn off UI for 1 or multiple drive_enclosure Hardware

    """
    FusionUIBase.navigate_to_section(SectionType.DRIVE_ENCLOSURES, time_for_loading=5)

    for drive_enclosure in drive_enclosure_obj:
        logger.info("Turning Off UID named '%s'" % drive_enclosure.name)
        select_drive_enclosure(drive_enclosure.name)
        VerifyDriveEnclosures.verify_drive_enclosure_uid(drive_enclosure.name, expect_value='On', timeout=10, fail_if_false=True)
        TurnOffDriveEnclosureUID.click_uid_button()
        TurnOffDriveEnclosureUID.wait_until_uid_off(drive_enclosure.name, timeout=120, fail_if_false=True)
        VerifyDriveEnclosures.verify_drive_enclosure_uid(drive_enclosure.name, expect_value='Off', timeout=60, fail_if_false=True)
