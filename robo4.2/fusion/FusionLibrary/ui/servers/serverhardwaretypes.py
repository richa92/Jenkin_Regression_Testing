# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Server Hardware Type UI page."""

from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.cli.blade_info import blade_info
import re
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.servers.serverhardwaretypes import CommonOperationServerHardwareType, \
    EditServerHardwareType, DeleteServerHardwareType, VerifyServerHardwareType
from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware
from FusionLibrary.ui.servers.serverhardwaretypes_elements import FusionServerHardwareTypePage


def navigate():
    FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE_TYPES)


# begin - edit server hardware type
def edit_server_hardware_type(hardware_types_obj):
    """ Edit Hardware Type

    Arguments:
      <servertype>
          name*                     --  Name of server hardware type as a string.
          new_name                  --  New name to be edited
          desc                      --  Server hardware type description to be updated

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.editservertypes.Gen8}
        data/enclosures -> @{TestData.editservertypes.Gen9}
        <EditServerTypes>
            <Gen8>
                <serveryype name="BL465c Gen8 2" new_name="BL465c Gen8 2 updated" desc="Update Gen8 server type"/>
                <serveryype name="BL465c Gen8 2 updated" new_name="BL465c Gen8 2" desc="Revert the Gen8 server type"/>
            </Gen8>
            <Gen9>
                <serveryype name="BL460c Gen9 1" new_name="BL460c Gen9 1 updated" desc="Update Gen9 server type"/>
                <serveryype name="BL460c Gen9 1 updated" new_name="BL460c Gen9 1" desc="Revert the Gen9 server type"/>
            </Gen9>
        </EditServerTypes>

    """
    navigate()

    # select server hardware type
    count = 0
    for n, sht_obj in enumerate(hardware_types_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(hardware_types_obj), '-' * 14))
        logger.info("Editing a server hardware type with name '%s'" % sht_obj.name)
        if select_server_hardware_type(sht_obj.name) is False:
            continue

        EditServerHardwareType.select_actions_edit()
        EditServerHardwareType.wait_edit_sht_dialog_shown()
        if hasattr(sht_obj, 'new_name'):
            EditServerHardwareType.input_name(sht_obj.new_name)
        if hasattr(sht_obj, 'desc'):
            EditServerHardwareType.input_description(sht_obj.desc)
        EditServerHardwareType.click_ok_button()
        # TODO: handle duplicate name error
        if EditServerHardwareType.wait_edit_sht_dialog_disappear(fail_if_false=False) is False:
            # get error message
            msg = FusionUIBase.get_error_message_from_dialog()
            logger.warn("Got error message '%s' when editing server hardware type with name '%s'" % (msg[1], sht_obj.name))
            # close dialog
            EditServerHardwareType.click_cancel_button()
            EditServerHardwareType.wait_edit_sht_dialog_disappear()
            continue

        if hasattr(sht_obj, 'new_name'):
            VerifyServerHardwareType.verify_sht_exist(sht_obj.new_name)

        # check the sht name is updated in server hardware
        if not _click_used_by_server_hardware(sht_obj.new_name):
            continue

        count += 1

    if count == 0:
        logger.warn("No server hardware type edited!")
        return False

    if count != len(hardware_types_obj):
        logger.warn("Not able to edit all server hardware type!")
        return False

    return True
# end - edit server hardware type


# begin - change server hardware type name to existing name
def cannot_change_sht_name_to_existing_name(hardware_types_obj):
    """ change Hardware Type to an existing name

    Arguments:
      <servertype>
          name*                     --  Name of server hardware type as a string.
          desc                      --  Server hardware type description to be updated

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.EditServerTypes.Dupl}
        <EditServerTypes>
            <Dupl>
                <servertype name="BL465c Gen8 2" desc="Update to a duplicate name"/>
                <servertype name="BL460c Gen9 1" desc="Update to a duplicate name"/>
            </Dupl>
        </EditServerTypes>

    """
    navigate()

    # select server hardware type
    count = 0
    dupl_msg = 'A server hardware type already has either the original or the displayed name specified'

    sht_name_list = CommonOperationServerHardwareType.get_sht_list()

    for n, sht_obj in enumerate(hardware_types_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(hardware_types_obj), '-' * 14))
        logger.info("Changing a server hardware type with name '%s'" % sht_obj.name)

        if select_server_hardware_type(sht_obj.name) is False:
            continue

        EditServerHardwareType.select_actions_edit()
        EditServerHardwareType.wait_edit_sht_dialog_shown()

        # Generate the new name using existing sht name
        new_name = None

        for sht_name in sht_name_list:
            if sht_obj.name != sht_name:
                new_name = sht_name
                EditServerHardwareType.input_name(new_name)
                break

        if new_name is None:
            logger.warn("cannot get an appropriate existing sht name as the new name, maybe there's not sufficient SHTs existing")
            continue
        if hasattr(sht_obj, 'desc'):
            EditServerHardwareType.input_description(sht_obj.desc)

        EditServerHardwareType.click_ok_button()
        if EditServerHardwareType.wait_edit_sht_dialog_disappear(fail_if_false=False):
            logger.warn("The new name [%s] may not be an existing sht name, since the dialog is closed unexpectedly, means there's no expected error message found" % new_name)
            continue

        # get error message
        status, msg = FusionUIBase.get_error_message_from_dialog()
        if dupl_msg not in msg:
            ui_lib.get_s2l().capture_page_screenshot()
            logger.warn("Got UNEXPECTED error message '%s' when editing server hardware type with name '%s', the expected error message '%s' is not found" % (msg[1], sht_obj.name, dupl_msg))
            continue
        else:
            logger.info("Successfully got the expected error message '%s'" % dupl_msg)

        # close dialog
        EditServerHardwareType.click_cancel_button()
        EditServerHardwareType.wait_edit_sht_dialog_disappear()

        count += 1

    if count == 0:
        logger.warn("No server hardware type edited!")
        return False

    if count != len(hardware_types_obj):
        logger.warn("Not able to edit all server hardware type!")
        return False

    return True
# end - change server hardware type name to existing name


# begin - delete server hardware type
def delete_server_hardware_type(hardware_types_obj):
    """ Delete Hardware Type

    Arguments:
      <servertype>
          name*                     --  Specify server hardware type name to be deleted.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.DeleteServerTypes.Gen8}
        data/enclosures -> @{TestData.DeleteServerTypes.Gen9}
        <DeleteServerTypes>
            <Gen8>
                <servertype name="BL465c Gen8 2" />
            </Gen8>
            <Gen9>
                <servertype name="DL180 Gen9 1" />
            </Gen9>
        </DeleteServerTypes>

    """
    navigate()

    count = 0
    ret = True
    for n, sht_obj in enumerate(hardware_types_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(hardware_types_obj), '-' * 14))
        logger.info("Removing a server hardware type with name %s" % sht_obj.name)
        if not select_server_hardware_type(sht_obj.name):
            continue

        DeleteServerHardwareType.select_actions_delete()
        if DeleteServerHardwareType.wait_delete_dialog_shown(fail_if_false=False) is False:
            if DeleteServerHardwareType.wait_delete_error_dialog_shown(fail_if_false=False) is True:
                ui_lib.get_s2l().capture_page_screenshot()
                error_msg = DeleteServerHardwareType.get_delete_error_text()
                logger.warn("Got warn message '%s' when remove server hardware type with name %s" % (error_msg, sht_obj.name))
                DeleteServerHardwareType.click_close()
                DeleteServerHardwareType.wait_delete_error_dialog_disappear()
            else:
                ui_lib.get_s2l().capture_page_screenshot()
                logger.warn("Failed to delete server hardware type with name %s" % sht_obj.name)
            continue

        DeleteServerHardwareType.click_yes_delete_button()
        DeleteServerHardwareType.wait_delete_dialog_disappear()

        FusionUIBase.show_activity_sidebar()
        if FusionUIBase.wait_activity_action_ok(sht_obj.name, "Delete server hardware type", timeout=30, fail_if_false=False) is False:
            ret = False
        FusionUIBase.show_activity_sidebar()

        if VerifyServerHardwareType.verify_sht_not_exist(sht_obj.name, fail_if_false=False):
            logger.info("Remove server hardware type {0} successfully".format(sht_obj.name))
        elif DeleteServerHardwareType.wait_sht_show_not_found(sht_obj.name, fail_if_false=False):
            logger.info("server hardware type status appear as 'not found', remove server hardware type {0} successfully.".format(sht_obj.name))
        else:
            msg = "The server hardware type does not disappear in 10s!"
            logger.warn(msg)
            continue

        count += 1

    if count == 0:
        msg = "no target server hardware type exists!"
        logger.warn(msg)
        return False

    if count != len(hardware_types_obj):
        logger.warn("Not able to delete all server hardware type!")
        return False

    return ret
# end - delete server hardware type


# begin - can not delete server hardware type
def cannot_delete_server_hardware_type(hardware_types_obj):
    """ Can not Delete Hardware Type

    Arguments:
      <servertype>
          name*                     --  Specify server hardware type name to be deleted.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.DeleteServerTypesUsedBy}
        <DeleteServerTypes>
            <UsedBy>
                <servertype name="BL465c Gen8 2" />
            </UsedBy>
        </DeleteServerTypes>

    """
    navigate()

    count = 0
    ret = True
    failed_delete_info = 'A server hardware type cannot be deleted while it is being referenced ' \
                         'by server profile templates, server profiles or matches server hardware ' \
                         'that is under management.'

    for n, sht_obj in enumerate(hardware_types_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(hardware_types_obj), '-' * 14))
        logger.info("Removing a server hardware type with name %s" % sht_obj.name)

        if not select_server_hardware_type(sht_obj.name):
            continue

        DeleteServerHardwareType.select_actions_delete()

        if DeleteServerHardwareType.wait_delete_dialog_shown(fail_if_false=False):
            logger.warn("The server hardwware type %s should not be deleted, due to it's using by others" % sht_obj.name)
            continue

        if DeleteServerHardwareType.wait_delete_error_dialog_shown(fail_if_false=False):
            error_msg = DeleteServerHardwareType.get_delete_error_text()
            if error_msg != failed_delete_info:
                ui_lib.get_s2l().capture_page_screenshot()
                logger.warn("Got warn message '%s' when remove server hardware type with name %s" % (error_msg, sht_obj.name))
                continue
            logger.info('The server hardware type you are deleting is under management.')
            DeleteServerHardwareType.click_close()
            DeleteServerHardwareType.wait_delete_error_dialog_disappear()

        count += 1

    if count == 0:
        msg = "no target server hardware type exists!"
        logger.warn(msg)
        return False

    if count != len(hardware_types_obj):
        logger.warn("Not able to delete all server hardware type!")
        return False

    return ret
# end - can not delete server hardware type


# begin - delete_all_server_hardware_types
def delete_all_server_hardware_types():
    """ Delete All Hardware Types
    """
    navigate()

    count = 0
    ret = True

    # get all server hardware types name
    sht_names = CommonOperationServerHardwareType.get_sht_list()
    logger.info("About to delete all server hardware types: %r" % sht_names)

    for n, name in enumerate(sht_names):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(sht_names), '-' * 14))
        logger.info("Removing a server hardware type with name %s" % name)
        if not select_server_hardware_type(name):
            continue

        DeleteServerHardwareType.select_actions_delete()
        if DeleteServerHardwareType.wait_delete_dialog_shown(fail_if_false=False) is False:
            if DeleteServerHardwareType.wait_delete_error_dialog_shown(fail_if_false=False) is True:
                ui_lib.get_s2l().capture_page_screenshot()
                error_msg = DeleteServerHardwareType.get_delete_error_text()
                logger.warn("Got warn message '%s' when remove server hardware type with name %s" % (error_msg, name))
                DeleteServerHardwareType.click_close()
                DeleteServerHardwareType.wait_delete_error_dialog_disappear()
            else:
                ui_lib.get_s2l().capture_page_screenshot()
                logger.warn("Failed to delete server hardware type with name %s" % name)
            continue

        DeleteServerHardwareType.click_yes_delete_button()
        DeleteServerHardwareType.wait_delete_dialog_disappear()

        FusionUIBase.show_activity_sidebar()
        if FusionUIBase.wait_activity_action_ok(name, "Delete server hardware type", timeout=30, fail_if_false=False) is False:
            ret = False
        FusionUIBase.show_activity_sidebar()

        if VerifyServerHardwareType.verify_sht_not_exist(name, fail_if_false=False):
            logger.info("Remove server hardware type {0} successfully".format(name))
        elif DeleteServerHardwareType.wait_sht_show_not_found(name, fail_if_false=False):
            logger.info("server hardware type status appear as 'not found', remove server hardware type {0} successfully.".format(name))
        else:
            msg = "The server hardware type does not disappear in 10s!"
            logger.warn(msg)
            continue

        count += 1
        ui_lib.refresh_browser(FusionUIBaseElements.ID_MENU_ONE_VIEW, PerfConstants.DEFAULT_SYNC_TIME)

    if count == 0:
        msg = "no target server hardware type exists!"
        logger.warn(msg)
        return False

    if count != len(sht_names):
        logger.warn("Not able to delete all server hardware type!")
        return False

    return ret
# end - delete_all_server_hardware_types


# begin - select server hardware type
def select_server_hardware_type(hardware_type_name):
    """ Select Hardware Type  """
    navigate()

    logger.info("Select server hardware type - %s" % hardware_type_name)
    if VerifyServerHardwareType.verify_sht_exist(hardware_type_name, fail_if_false=False):
        CommonOperationServerHardwareType.click_sht(hardware_type_name)
        CommonOperationServerHardwareType.wait_sht_title_display(hardware_type_name)
        return True
    else:
        logger.warn("Server hardware type '{0}' does not exist".format(hardware_type_name))
        ui_lib.get_s2l().capture_page_screenshot()
        return False
# end - select server hardware type


# begin - verify server hardware type
def verify_server_hardware_type(hardware_types_obj):
    """ Delete Hardware Type

    Arguments:
      <servertype>
          name*                     --  Specify server hardware type name should be verified.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.servertypes.VerifyServerTypes.Gen8}}
        data/enclosures -> @{TestData.servertypes.VerifyServerTypes.Gen9}}
        <servertypes>
            <VerifyServerTypes>
                <Gen8>
                   <servertype name="BL465c Gen8 2" />
                </Gen8>>
                <Gen9>
                    <servertype name="DL180 Gen9 1" />
                </Gen9>
            </VerifyServerTypes>
        </servertypes>
    """

    navigate()

    count = 0

    for n, sht_obj in enumerate(hardware_types_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(hardware_types_obj), '-' * 14))
        logger.info("Verifying a server hardware type is used by ")

        if not select_server_hardware_type(sht_obj.name):
            continue

        # check the sht name is used by server hardware
        if not _click_used_by_server_hardware(sht_obj.name):
            continue

        # navigate to server hardware type page, continue the remaining verification
        navigate()
        select_server_hardware_type(sht_obj.name)

        # check the sht name is used by server profile
        if not _click_used_by_server_profile(sht_obj.name):
            continue

        count += 1

    if count == 0:
        msg = "No target server hardware type exists!"
        logger.warn(msg)
        return False

    if count != len(hardware_types_obj):
        logger.warn("Not able to verify all server hardware type!")
        return False

    return True
# end - verify server hardware type


# begin - validate_server_hardware_types
def validate_server_hardware_type(hardware_types_obj):
    """Reads the data of enclosure from datafile and retrieves server information and returns in the form of list.

    Arguments:
      <servertype>
          name*                     --  Name of server hardware type as a string.
          sh_name                   --  Name of server hardware as a string.
          server_model              --  Expected server model
          form_factor               --  Expected form factor
          description               --  Expected description
          used_by                   --  Expected used by
            <adapter> optional, for verify adapter information
                location*                               --  Adapter location to be verified
                model                                   --
                device_type                             --
                max_port_speed                          --
                physical_ports                          --
                virtual_ports                           --
                available_virtual_functions             --
                virtual_function_allocation_increment   --
                pxe                                     --
                ethernet                                --
                fc                                      --

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.verifyservertypes}
        <verifyservertypes>
            <servertype name="BL460c Gen8 1" sh_name="wpst20, bay 3" server_model="ProLiant BL460c Gen8" form_factor="Half-height" description="BL460c Gen8 1" used_by="none">
                <adapter location="Mezzanine 1" model="HP FlexFabric 10Gb 2-port 554M Adapter" device_type="Ethernet" max_port_speed="10 Gb/s" physical_ports="2" virtual_ports="8" available_virtual_functions="None"
                        virtual_function_allocation_increment="None" pxe="Yes" ethernet="Yes" fc="Yes"/>
                <adapter location="FlexibleLOM 1" model="HP FlexFabric 10Gb 2-port 554FLB Adapter" device_type="Ethernet" max_port_speed="10 Gb/s" physical_ports="2" virtual_ports="8" available_virtual_functions="None"
                        virtual_function_allocation_increment="None" pxe="Yes" ethernet="Yes" fc="Yes"/>
                <adapter location="Mezzanine 2" model="HP LPe1205A 8Gb FC HBA for BladeSystem c-Class" device_type="Fibre Channel" max_port_speed="8 Gb/s" physical_ports="2" virtual_ports="0" available_virtual_functions="None"
                        virtual_function_allocation_increment="None" pxe="No" ethernet="No" fc="Yes"/>
            </servertype>
        </verifyservertypes>

    """
    navigate()

    count = 0
    ret = True
    for n, sht_obj in enumerate(hardware_types_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(hardware_types_obj), '-' * 14))
        if hasattr(sht_obj, 'sh_name'):
            FusionUIBase.navigate_to_section(SectionType.SERVER_HARDWARE)
            CommonOperationServerHardware.click_server_hardware(sht_obj.sh_name)
            CommonOperationServerHardware.wait_server_hardware_selected(sht_obj.sh_name)
            sht_name = CommonOperationServerHardware.get_server_hardware_type(sht_obj.sh_name)
            setattr(sht_obj, 'name', sht_name)
            navigate()
        logger.info("Verifying a server hardware type with name %s" % sht_obj.name)
        if not select_server_hardware_type(sht_obj.name):
            ui_lib.fail_test("Unable to select Server Hardware Type named '%s'." % sht_obj.name)

        # general
        FusionUIBase.select_view_by_name('General')
        CommonOperationServerHardwareType.wait_sht_details_load_completed(sht_obj.name)
        if hasattr(sht_obj, 'server_model'):
            VerifyServerHardwareType.verify_general_server_model(sht_obj.server_model)

        if hasattr(sht_obj, 'form_factor'):
            VerifyServerHardwareType.verify_general_form_factor(sht_obj.form_factor)

        if hasattr(sht_obj, 'description'):
            VerifyServerHardwareType.verify_general_description(sht_obj.description)

        if hasattr(sht_obj, 'used_by'):
            VerifyServerHardwareType.verify_general_used_by(sht_obj.used_by, fail_if_false=False)

        # adapter
        if hasattr(sht_obj, 'adapter'):
            FusionUIBase.select_view_by_name('Adapters')
            for adapter_obj in sht_obj.adapter:
                if hasattr(adapter_obj, 'location'):
                    VerifyServerHardwareType.verify_adapter_location_exist(adapter_obj.location)

                if hasattr(adapter_obj, 'model'):
                    VerifyServerHardwareType.verify_adapter_model(adapter_obj.location, adapter_obj.model)

                if hasattr(adapter_obj, 'device_type'):
                    VerifyServerHardwareType.verify_adapter_device_type(adapter_obj.location, adapter_obj.device_type)

                if hasattr(adapter_obj, 'max_port_speed'):
                    VerifyServerHardwareType.verify_adapter_max_port_speed(adapter_obj.location, adapter_obj.max_port_speed)

                if hasattr(adapter_obj, 'physical_ports'):
                    VerifyServerHardwareType.verify_adapter_physical_port(adapter_obj.location, adapter_obj.physical_ports)

                if hasattr(adapter_obj, 'virtual_ports'):
                    VerifyServerHardwareType.verify_adapter_virtual_ports(adapter_obj.location, adapter_obj.virtual_ports)

                if hasattr(adapter_obj, 'available_virtual_functions'):
                    VerifyServerHardwareType.verify_adapter_available_virtual_functions(adapter_obj.location, adapter_obj.available_virtual_functions)

                if hasattr(adapter_obj, 'virtual_function_allocation_increment'):
                    VerifyServerHardwareType.verify_adapter_virtual_function_allocation_increment(adapter_obj.location, adapter_obj.virtual_function_allocation_increment)

                if hasattr(adapter_obj, 'ethernet'):
                    VerifyServerHardwareType.verify_adapter_ethernet(adapter_obj.location, adapter_obj.ethernet)

                if hasattr(adapter_obj, 'fc'):
                    VerifyServerHardwareType.verify_adapter_fc(adapter_obj.location, adapter_obj.fc)

                if hasattr(adapter_obj, 'iscsi'):
                    VerifyServerHardwareType.verify_adapter_iscsi(adapter_obj.location, adapter_obj.iscsi)

        count += 1

    if count == 0:
        msg = "no target server hardware type exists!"
        logger.warn(msg)
        return False

    if count != len(hardware_types_obj):
        logger.warn("Not able to verify all server hardware type!")
        return False

    return ret
# end - validate_server_hardware_types


# begin - verify server hardware type not exist
def validate_server_hardware_type_not_exist(hardware_types_obj):
    """ Validate Server Hardware Type Not Exist

    Arguments:
      <servertype>
          name*                     --  Name of server hardware type as a string.

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.noservertypes}
        <noservertypes>
            <servertype name="BL460c Gen8 1"/>
            <servertype name="BL460c Gen9 1"/>
        </noservertypes>

    """
    navigate()

    # select server hardware type
    count = 0
    for n, sht_obj in enumerate(hardware_types_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(hardware_types_obj), '-' * 14))
        logger.info("Verify a server hardware type not exist with name '%s'" % sht_obj.name)
        VerifyServerHardwareType.verify_sht_not_exist(sht_obj.name)

        count += 1

    if count == 0:
        logger.warn("All server hardware type verify failed!")
        return False

    if count != len(hardware_types_obj):
        logger.warn("Some server hardware type verify failed!")
        return False

    return True
# end - verify server hardware type not exist


# begin - validate_server_hardware_types_name_without_number_exist
def validate_server_hardware_types_name_without_number_exist(hardware_types_obj):
    """Validate if expected server hardware types name without tailing number exsit in system

    Arguments:
      <servertype>
          name*                     --  Name of server hardware type as a string. (don't include tailing number in name)

    * Required Arguments

    Example:
        data/enclosures -> @{TestData.verifyservertypesname}
        <verifyservertypesname>
            <servertype name="BL420c Gen8" />
            <servertype name="BL460c G7" />
        </verifyservertypesname>

    """
    navigate()

    count = 0

    hardware_types_obj = [item for n, item in enumerate(hardware_types_obj)]
    verified_sht_names = []

    # get all server hardware types name
    sht_names = CommonOperationServerHardwareType.get_sht_list()
    logger.info("About to verify all server hardware types name without number: %r" % sht_names)

    for sht_obj in hardware_types_obj:
        for name in sht_names:
            if name.startswith(sht_obj.name) is True:
                if name not in verified_sht_names:
                    verified_sht_names.append(name)
                    logger.info("Expected server hardware type '%s' exists in SHT page" % sht_obj.name)
                break
        else:
            logger.warn("Expected server hardware type '%s' not exsit in SHT page" % sht_obj.name)

    logger.debug(verified_sht_names)

    if len(verified_sht_names) != len(hardware_types_obj):
        logger.warn("Not all expected server hardware types exist in SHT page")
        return False

    return True
# end - validate_server_hardware_types_name_without_number_exist


def _retrieve_adapter_data(OAIP, bay_no, adapter_dict, *enclosure_obj):
    """Reads the data of enclosure from datafile and retrieves server information and returns in the form of lists."""
    ret_val = (True, [])
    if isinstance(enclosure_obj, test_data.DataObj):
        enclosure_obj = [enclosure_obj]
    elif isinstance(enclosure_obj, tuple):
        enclosure_obj = list(enclosure_obj[0][0])

    enclosure_data = ""
    for enclosure in enclosure_obj:
        if enclosure.oa1hostname == OAIP:
            enclosure_data = enclosure
            break
    if enclosure_data == "":
        logger._warn("Given encolsure ""%s"" information is not available in the data file please verify" % OAIP)
        ret_val = (False, [])
    else:
        OA_info_obj = blade_info(OAIP, enclosure_data.oa1username, enclosure_data.oa1password)
        ret_val = OA_info_obj.get_server_adapter_information(bay_no, adapter_dict)
    return ret_val


def _retrieve_general_data(OAIP, bay_no, Formfactor_dict, hw_type, *enclosure_obj):
    """Reads the data of enclosure from datafile and retrieves server information and returns in the form of lists."""
    ret_val = (True, [])
    if isinstance(enclosure_obj, test_data.DataObj):
        enclosure_obj = [enclosure_obj]
    elif isinstance(enclosure_obj, tuple):
        enclosure_obj = list(enclosure_obj[0][0])

    enclosure_data = ""
    for enclosure in enclosure_obj:
        if enclosure.oa1hostname == OAIP:
            enclosure_data = enclosure
            break
    if enclosure_data == "":
        logger._log_to_console_and_log_file("Given encolsure ""%s"" information is not available in the data file please verify" % OAIP)
        ret_val = (False, [])
    else:
        try:
            formfactor = Formfactor_dict[hw_type]
            OA_info_obj = blade_info(OAIP, enclosure_data.oa1username, enclosure_data.oa1password)
            model = str(OA_info_obj.get_server_model_from_OA(bay_no)).strip(' ')
            ret_val = [True, [model, formfactor]]
        except Exception as e:
            ret_val = (False, [])
            logger._warn("Given hardware type %s formfactor is not updated in the resource file. Exception is %s" % (hw_type, e))
    return ret_val


def _validate_general_information(hw_type, data_list):
    # Validating general tab information
    return_val = True
    selenium2lib = ui_lib.get_s2l()
    model = str(selenium2lib._get_text(FusionServerHardwareTypePage.ID_MODEL_TEXT))
    formfactor = str(selenium2lib._get_text(FusionServerHardwareTypePage.ID_FORMFACTOR_TEXT))
    if([model, formfactor] == data_list):
        logger._log_to_console_and_log_file("Values retrieved for the hardware type %s from appliance is %s and values from devices is %s" % (hw_type, str([model, formfactor]), str(data_list)))
        logger._log_to_console_and_log_file("Server Hardware type general information is matching properly for the type: %s" % hw_type)
    else:
        logger._warn("Values retrieved for the hardware type %s from appliance is %s and values from devices is %s" % (hw_type, str([model, formfactor]), str(data_list)))
        logger._warn("Server Hardware type general information is mismatching for the type: %s" % hw_type)
        return_val = False
    return return_val


def _validate_adapter_information(hw_type, data_list):
    # Validating adapter tab information
    return_val = True
    selenium2lib = ui_lib.get_s2l()
    count_hw_types_row = selenium2lib._element_find(FusionServerHardwareTypePage.ID_ADAPTER_INFO_TABLE_ROW, False, False)
    if(len(count_hw_types_row) == len(data_list)):
        for i in range(len(count_hw_types_row)):
            row_data = []
            row_content = len(selenium2lib._element_find(FusionServerHardwareTypePage.ID_ADAPTER_INFO_TABLE_SPECIFIC_ROW % str(i + 1), False, False))
            # retrieving the data from the hardware types page.
            for l in range(row_content):
                ui_lib.wait_for_element(FusionServerHardwareTypePage.ID_ADAPTER_INFO_TABLE_SPECIFIC_ROW % str(i + 1), PerfConstants.DEFAULT_SYNC_TIME)
                row_data.append(str(selenium2lib._get_text(FusionServerHardwareTypePage.ID_ADAPTER_INFO_TABLE_SPECIFIC_CELL % (str(i + 1), str(l + 1)))))
        localflag = False
        # Comparing the retrieved values with each type information retrieved from the device.
        for listdat in data_list:
            if(row_data[1] in listdat[1]):
                if((row_data[0] == listdat[0]) and (row_data[1] == listdat[1].strip('\r')) and (row_data[2] == listdat[2]) and (((row_data[3].replace(' ', '')).strip("/s")) == listdat[3]) and (row_data[4] == listdat[4])):
                    localflag = True
                else:
                    logger._log_to_console_and_log_file("Server Hardware type adapter information is mismatching for the adapter: %s" % row_data[1])
        if not localflag:
            return_val = False
            logger._warn("Server Hardware type adapter information is mismatching for the type: %s" % hw_type)
        else:
            logger._log_to_console_and_log_file("Server Hardware type adapter information is matching properly for the type: %s" % hw_type)
    else:
        return_val = False
        logger._warn("Server Hardware type information is mismatching for the type: %s" % hw_type)
    return return_val


def _click_used_by_server_hardware(sht_name):

    from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware

    try:
        CommonOperationServerHardwareType.click_used_by_server_hardware()
    except:
        logger.warn("Server hardware type [ %s ] are not used by any server hardware" % sht_name)
        return False

    server_name_list = CommonOperationServerHardware.get_server_hardware_list()
    for server_name in server_name_list:
        CommonOperationServerHardware.click_server_hardware(server_name)
        FusionUIBase.select_view_by_name(view_name='Hardware', timeout=8, fail_if_false=False)
        got_sht_name = CommonOperationServerHardware.get_server_hardware_type(server_name, fail_if_false=False)
        if got_sht_name != sht_name:
            ui_lib.get_s2l().capture_page_screenshot()
            logger.warn("Server hardware [%s] doesn't have server hardware type [%s]" % (server_name, sht_name))
            return False

        logger.info("Server hardware [%s] has server hardware type [%s]" % (server_name, sht_name))

    return True


def _click_used_by_server_profile(sht_name):
    # check server hardware type information by server profile
    from FusionLibrary.ui.business_logic.servers.serverprofiles import CommonOperationServerProfile

    try:
        CommonOperationServerHardwareType.click_used_by_server_profile()
    except:
        logger.warn("Server hardware type [ %s ] are not used by any server profile" % sht_name)
        return False

    server_profile_list = CommonOperationServerProfile.get_server_profile_list()

    for sp_name in server_profile_list:
        CommonOperationServerProfile.click_server_profile(sp_name)
        FusionUIBase.select_view_by_name('General', fail_if_false=False)
        got_sht_name = CommonOperationServerProfile.get_server_hardware_type_of_server_profile(sp_name, fail_if_false=False)
        if got_sht_name != sht_name:
            ui_lib.get_s2l().capture_page_screenshot()
            logger.warn("Server profile [%s] doesn't have server hardware type [%s]" % (sp_name, sht_name))
            return False
        logger.info("Server profile [%s] has server hardware type [%s]" % (sp_name, sht_name))

    return True
