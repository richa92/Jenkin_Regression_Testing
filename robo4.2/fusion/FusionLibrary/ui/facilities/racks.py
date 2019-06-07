# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Racks page
"""


from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.general.dashboard_elements import FusionDashboardPage
from FusionLibrary.ui.business_logic.facilities.racks_elements import FusionRacksPage
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType

import Selenium2Library
import re
selenium2lib = Selenium2Library.Selenium2Library()


def navigate():
    FusionUIBase.navigate_to_section(SectionType.RACKS)


def add_data_centers(datacenterName, *params):
    raise NotImplementedError


def edit_data_center(datacenterName, *params):
    raise NotImplementedError


def remove_data_center(self, datacenterName):
    raise NotImplementedError


def select_data_center(self, datacenterName):
    raise NotImplementedError


def delete_rack(*rack_obj):
    """ delete_rack function to add the rack to the appliance
        Example:
        | `delete_rack`      |    $(rackname) |
    """
    failed_times = 0
    selenium2lib = ui_lib.get_s2l()
    logging._log_to_console_and_log_file("Removing rack")
    if isinstance(rack_obj, test_data.DataObj):
        rack_obj = [rack_obj]
    elif isinstance(rack_obj, tuple):
        rack_obj = list(rack_obj[0])
    for racks in rack_obj:
        logging._log_to_console_and_log_file("Removing Rack with name.... %s" % racks.name)
        if not select_rack(racks.name):
            logging._warn("Exiting rack function, Not selected Rack %s" % racks.name)
            selenium2lib.capture_page_screenshot()
            failed_times += 1
            continue
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_MENU_ACTION_REMOVE)
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DELETE_RACK_CONFIRM)
        if ui_lib.wait_for_element(FusionRacksPage.ID_REMOVE_VALIDATE % racks.name):
            logging._log_to_console_and_log_file("Rack is successfully Deleted with name %s" % racks.name)
        else:
            logging._log_to_console_and_log_file("Rack Deletion is failed %s " % racks.name)
            selenium2lib.capture_page_screenshot()
            failed_times += 1

    if failed_times > 0:
        return False
    else:
        return True


def remove_all_racks(name_pattern=None):
    logging._log_to_console_and_log_file("Removing all racks")
    selenium2lib = ui_lib.get_s2l()

    failed_times = 0
    navigate()

    for i in xrange(2, 999):
        rack_name = ''
        try:
            rack_name = selenium2lib.get_table_cell(FusionRacksPage.ID_RACK_LIST_TABLE, i, 2)
            if name_pattern is not None and re.search(name_pattern, rack_name) is None:
                continue
        except Exception:
            break

        if not select_rack(rack_name):
            logging._warn("Exiting rack function, Not selected Rack %s" % rack_name)
            selenium2lib.capture_page_screenshot()
            failed_times += 1
            continue

        if rack_name != '':
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ACTION_MAIN_BTN)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_MENU_ACTION_REMOVE)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DELETE_RACK_CONFIRM)
            if ui_lib.wait_for_element(FusionRacksPage.ID_REMOVE_VALIDATE % rack_name):
                logging._log_to_console_and_log_file("Rack is successfully Deleted with name %s" % rack_name)
            else:
                logging._log_to_console_and_log_file("Rack Deletion is failed %s " % rack_name)

    if failed_times > 0:
        return False
    else:
        return True


def add_rack(*rack_obj):
    """ add_rack function to add the rack to the appliance

        Example:
        | `add Rack`      |    $(rackname) |
    """
    logging._log_to_console_and_log_file("Adding rack")
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionRacksPage.ID_LINK_ADD_RACK):
        logging._log_to_console_and_log_file("Success")
        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_MENU_ONE_VIEW)
        ui_lib.wait_for_element_and_click(FusionDashboardPage.ID_LINK_RACKS)
    if isinstance(rack_obj, test_data.DataObj):
        rack_obj = [rack_obj]
    elif isinstance(rack_obj, tuple):
        rack_obj = list(rack_obj[0])
    for racks in rack_obj:
        logging._log_to_console_and_log_file("The racks data to add %s" % racks)
        # ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_ADD_RACK, 10)
        # ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_ADD_RACK, 3)
        ui_lib.wait_for_element_visible(FusionRacksPage.ID_LINK_ADD_RACK, 10)
        logging._log_to_console_and_log_file("click add rack button")
        ui_lib.wait_for_element_and_click("link=Add rack")
        if ui_lib.wait_for_element_visible("id=hp-change-page-container", timeout=10) is False:
            ui_lib.fail_test("Failed to open add rack dialog")
        _rack_general_properties(racks)
        # Function to add PDU
        addpdu = None
        if racks.has_property('addpdutorack'):
            addpdu = racks.addpdutorack
        if addpdu is None:
            logging._log_to_console_and_log_file("There is no data for pdu to be added")
        if isinstance(addpdu, (list)):
            for pdu in addpdu:
                _add_pdu_to_rack(pdu)
        # Function to edit PDU
        editpdu = None
        if racks.has_property('editpdu'):
            editpdu = racks.editpdu
        if editpdu is None:
            logging._log_to_console_and_log_file("There is no data for pdu to be edited")
        if isinstance(editpdu, (list)):
            for pdu in editpdu:
                _edit_pdu_rack(pdu)
        # Function to remove PDU
        removepdu = None
        if racks.has_property('removepdu'):
            removepdu = racks.removepdu
        if removepdu is None:
            logging._log_to_console_and_log_file("There is no data for pdu to be delete")
        if isinstance(removepdu, (list)):
            for pdu in removepdu:
                _remove_pdu_from_rack(pdu)
        # Function to add enclosure to rack
        add_enclosure = None
        if racks.has_property('addhardware'):
            add_enclosure = racks.addhardware
            if add_enclosure is None:
                logging._log_to_console_and_log_file("No data to add Hardware")
            if isinstance(add_enclosure, (list)):
                for enclosure in add_enclosure:
                    _add_enclosure_to_rack(enclosure)
        # Function to edit enclosure from the rack
        edit_enclosure = None
        if racks.has_property('edithardware'):
            edit_enclosure = racks.edithardware
            if edit_enclosure is None:
                logging._log_to_console_and_log_file("No data to edit Hardware")
            if isinstance(edit_enclosure, (list)):
                for enclosure in edit_enclosure:
                    _edit_enclosure_in_rack(enclosure)
        # Function to remove enclosure from the rack
        remove_enclosure = None
        if racks.has_property('removehardware'):
            remove_enclosure = racks.removehardware
            if remove_enclosure is None:
                logging._log_to_console_and_log_file("No data to remove Hardware")
            if isinstance(remove_enclosure, (list)):
                for enclosure in remove_enclosure:
                    _remove_enclosure_from_rack(enclosure)
        # Function to add server hardware to rack
        add_server = None
        if racks.has_property('addserver'):
            add_server = racks.addserver
            if add_server is None:
                logging._log_to_console_and_log_file("No data to remove server")
            if isinstance(add_server, (list)):
                for server in add_server:
                    _add_server_in_rack(server)
        # Function to edit server hardware to rack
        edit_server = None
        if racks.has_property('editserver'):
            edit_server = racks.editserver
            if edit_server is None:
                logging._log_to_console_and_log_file("No data to edit server")
            if isinstance(edit_server, (list)):
                for server in edit_server:
                    _edit_server_in_rack(server)
        # Function to remove server from the rack
        remove_server = None
        if racks.has_property('removeserver'):
            remove_server = racks.removeserver
            if remove_server is None:
                logging._log_to_console_and_log_file("No data to edit Hardware")
            if isinstance(remove_server, (list)):
                for server in remove_server:
                    _remove_server_from_rack(server)
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_BTN_ADD_PLUS_RACK)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_BTN_CANCEL_RACK)
    fail_times = 0
    for racks in rack_obj:
        if ui_lib.wait_for_element_visible(FusionRacksPage.ID_ELEMENT_RACK_NAME % racks.newname):
            logging._log_to_console_and_log_file("Rack added successfully with name %s " % racks.newname)
            if hasattr(racks, 'addpdutorack'):
                for item in racks.addpdutorack:
                    if (item).has_property('pduip'):
                        devicename = item.pduip
                    if (item).has_property('modelname'):
                        devicename = item.modelname
                    _verify_device_in_rack(racks.newname, devicename)
                    continue
            if hasattr(racks, 'addhardware'):
                for item in racks.addhardware:
                    devicename = item.name
                    _verify_device_in_rack(racks.newname, devicename)
                    continue
            if hasattr(racks, 'addserver'):
                for item in racks.addserver:
                    devicename = item.name
                    _verify_device_in_rack(racks.newname, devicename)
                    continue
        else:
            logging._log_to_console_and_log_file("Adding rack failed")
            selenium2lib.capture_page_screenshot()
            fail_times = fail_times + 1

    if fail_times > 0:
        return False

    return True


def edit_rack_properties(*rack_obj):
    failed_times = 0
    selenium2lib = ui_lib.get_s2l()
    logging._log_to_console("Editing the rack properties")
    if isinstance(rack_obj, test_data.DataObj):
        rack_obj = [rack_obj]
    elif isinstance(rack_obj, tuple):
        rack_obj = list(rack_obj[0])
    for racks in rack_obj:
        logging._log_to_console_and_log_file("Modifying Rack with name.... %s" % racks.name)
        rack = racks.name
        if not select_rack(rack):
            logging._warn("Exiting Edit Rack Function, Not selected Rack %s" % racks.name)
            continue
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_MENU_ACTION_EDIT)
        # Function to edit the general properties of rack
        edit_rack = None
        if racks.has_property('general'):
            edit_rack = racks.general
            if edit_rack is None:
                logging._log_to_console_and_log_file("No data to edit the general properties")
            if isinstance(edit_rack, (list)):
                for general in edit_rack:
                    logging._log_to_console_and_log_file("New data %s" % general.newname)
                    if _rack_general_properties(general) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to add PDU to the existing Rack
        add_hardware = None
        if racks.has_property('addpdutorack'):
            add_hardware = racks.addpdutorack
            if add_hardware is None:
                logging._log_to_console_and_log_file("No data to add PDU to the rack")
            if isinstance(add_hardware, (list)):
                for hardware in add_hardware:
                    if _add_pdu_to_rack(hardware) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to edit pdu
        edit_hardware = None
        if racks.has_property('editpdu'):
            edit_hardware = racks.editpdu
            if edit_hardware is None:
                logging._log_to_console_and_log_file("No data to edit the PDU")
            if isinstance(edit_hardware, (list)):
                for pdu in edit_hardware:
                    if _edit_pdu_rack(pdu) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to delete PDU
        remove_hardware = None
        if racks.has_property('removepdu'):
            remove_hardware = racks.removepdu
            if remove_hardware is None:
                logging._log_to_console_and_log_file("No data to remove PDU from the rack")
            if isinstance(remove_hardware, (list)):
                for pdu in remove_hardware:
                    if _remove_pdu_from_rack(pdu) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to add enclosure to rack
        add_enclosure = None
        if racks.has_property('addhardware'):
            add_enclosure = racks.addhardware
            if add_enclosure is None:
                logging._log_to_console_and_log_file("No data to add Hardware")
            if isinstance(add_enclosure, (list)):
                for enclosure in add_enclosure:
                    if _add_enclosure_to_rack(enclosure) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to edit enclosure from the rack
        edit_enclosure = None
        if racks.has_property('edithardware'):
            edit_enclosure = racks.edithardware
            if edit_enclosure is None:
                logging._log_to_console_and_log_file("No data to edit Hardware")
            if isinstance(edit_enclosure, (list)):
                for enclosure in edit_enclosure:
                    if _edit_enclosure_in_rack(enclosure) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to remove enclosure from the rack
        remove_enclosure = None
        if racks.has_property('removehardware'):
            remove_enclosure = racks.removehardware
            if remove_enclosure is None:
                logging._log_to_console_and_log_file("No data to remove Hardware")
            if isinstance(remove_enclosure, (list)):
                for enclosure in remove_enclosure:
                    if _remove_enclosure_from_rack(enclosure) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to add server hardware to rack
        add_server = None
        if racks.has_property('addserver'):
            add_server = racks.addserver
            if add_server is None:
                logging._log_to_console_and_log_file("No data to remove server")
            if isinstance(add_server, (list)):
                for server in add_server:
                    if _add_server_in_rack(server) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to edit server hardware to rack
        edit_server = None
        if racks.has_property('editserver'):
            edit_server = racks.editserver
            if edit_server is None:
                logging._log_to_console_and_log_file("No data to edit server")
            if isinstance(edit_server, (list)):
                for server in edit_server:
                    if _edit_server_in_rack(server) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1
        # Function to remove server from the rack
        remove_server = None
        if racks.has_property('removeserver'):
            remove_server = racks.removeserver
            if remove_server is None:
                logging._log_to_console_and_log_file("No data to edit Hardware")
            if isinstance(remove_server, (list)):
                for server in remove_server:
                    if _remove_server_from_rack(server) is False:
                        selenium2lib.capture_page_screenshot()
                        failed_times += 1

        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_UPDATE_RACK)

        if ui_lib.wait_for_element(FusionRacksPage.ID_UPDATE_VALIDATE):
            if failed_times > 0:
                logging._log_to_console_and_log_file("Rack is successfully updated, but got problems during updating")
                selenium2lib.capture_page_screenshot()
                return False
            else:
                logging._log_to_console_and_log_file("Rack is successfully updated")
                return True
        else:
            logging._log_to_console_and_log_file("Rack updation done with failure")
            selenium2lib.capture_page_screenshot()
            return False


def _edit_server_in_rack(server):
    '''
    _edit_server_from_rack function to edit server present in rack such as (servers both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Editing the server with name %s" % server.name)
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionRacksPage.ID_RACK_ITEM_IN_CONTAINER % server.name):
        logging._warn("Server %s not found in the appliance" % server.name)
        selenium2lib.capture_page_screenshot()
        return False

    js_to_execute = """$('.hp-rack-devices .hp-device-name').find('a').filter(function(){
    var name = $(this).html();
    console.log(name);
    if(!name)
        return false;
    else
        return name.indexOf('%s')!=-1;
}).mouseenter();
$('div:visible.hp-edit').click();""" % server.name

    selenium2lib.execute_javascript(js_to_execute)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROPDOWN_RACKSLOT)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_ROW % server.row)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_EDIT_SERVER_TO_RACK_CONFIRM)

    server_slot = selenium2lib.get_element_attribute(FusionRacksPage.ID_SERVER_NAME_IN_RACK % server.name)
    slot_no = re.search(r'Slots (\d+):\d+', server_slot).group(1)

    logging._log_to_console("Server slot is %s" % slot_no)

    if slot_no != server.row:
        logging._warn("Failed to edit server %s" % server.name)
        selenium2lib.capture_page_screenshot()
        return False
    else:
        logging._log_to_console_and_log_file("Server with name %s successfully edited" % server.name)
        return True

"""
def _edit_server_in_rack(server):
    '''
    _edit_server_from_rack function to edit server present in rack such as (servers both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Editing the server with name %s" % server.name)
    selenium2lib = ui_lib.get_s2l()
    found = None
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if len(server.name) > 0:
        logging._log_to_console_and_log_file("Add")
        if selenium2lib._is_element_present(FusionRacksPage.ID_DELETE_SERVER % server.name):
            logging._log_to_console_and_log_file("Editing the server")
            selenium2lib.mouse_over(FusionRacksPage.ID_DELETE_SERVER % server.name)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_EDIT_SERVER_ENCLOSURE % server.name)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ClICK_DROP_DOWN_ALIGNMENT)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_ALIGNMENT % server.position)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_DROP_DOWN_ROW)
            if 1 <= int(server.row) <= 42:
                    selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\38')
                    val1 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                    while selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT) != server.row:
                        found = True
                        selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\40')
                        val2 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                        if(val1 == val2):
                            found = False
                            break
                        else:
                            val1 = val2
                if not found:
                        logging._log_to_console_and_log_file("Please pass valid value")
                        selenium2lib.capture_page_screenshot()
                        return False
                    else:
                        logging._log_to_console_and_log_file("Valid value")
            else:
                logging._warn("Enter value between 1 and 42")
                selenium2lib.capture_page_screenshot()
                return False
            if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_POWER_CONNECTIONS):
                    all_connections = server.powerconnections.split('/')
                    if (len(all_connections) > 1):
                        ui_lib.wait_for_element_visible(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                        selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                    else:
                        logging._log_to_console_and_log_file("Connections are more than 1")
                    for connection in all_connections:
                        power_connections = connection.split('-')
                        if power_connections[0] == "hardware2":
                            selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                            break
                    for connections in all_connections:
                        enclosures_connections = connections.split('-')
                        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_POWERCONNECTION_SELECT_ENCLOSURE % (enclosures_connections[0], enclosures_connections[1]))
            else:
                logging._log_to_console_and_log_file("No Power connections available")
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_RACK_OK)
            '''
                        QXCR1001311022: [CST]  Irrelevant message is shown when PDU is edited.
                        Validation will fail because of above issue
                    '''
            if selenium2lib._is_element_present(FusionRacksPage.ID_EDIT_PDU_VALIDATE % server.name):
                logging._log_to_console_and_log_file("Server with name successfully edited %s" % server.name)
            else:
                logging._warn("Server with name is not updated %s" % server.name)
        else:
            logging._log_to_console_and_log_file("No Server with name %s is not present in the appliance" % server.name)
"""


def _remove_server_from_rack(server):
    '''
    _remove_server_from_rack function to delete server from rack such as (servers both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Removing server with name %s from the rack" % server.name)
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionRacksPage.ID_RACK_ITEM_IN_CONTAINER % server.name):
        logging._warn("Server %s not found in the appliance" % server.name)
        selenium2lib.capture_page_screenshot()
        return False

    js_to_execute = """$('.hp-rack-devices .hp-device-name').find('a').filter(function(){
    var name = $(this).html();
    console.log(name);
    if(!name)
        return false;
    else
        return name.indexOf('%s')!=-1;
}).mouseenter();
$('div:visible.hp-close').click();""" % server.name

    selenium2lib.execute_javascript(js_to_execute)
    if not selenium2lib._is_element_present(FusionRacksPage.ID_RACK_ITEM_IN_CONTAINER % server.name):
        logging._log_to_console_and_log_file("Server %s deleted" % server.name)
        return True
    else:
        logging._warn("Unable to Delete server %s" % server.name)
        selenium2lib.capture_page_screenshot()
        return False


"""
def _remove_server_from_rack(server):
    '''
   _remove_server_from_rack function to delete server from rack such as (servers both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Removing server with name %s from the rack" % server.name)
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if selenium2lib._is_element_present(FusionRacksPage.ID_DELETE_SERVER % server.name):
        logging._log_to_console_and_log_file("Removing Server")
        selenium2lib.mouse_over(FusionRacksPage.ID_DELETE_SERVER % server.name)
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DELETE_SERVER_CONFIRM % server.name)
        if not selenium2lib._is_element_present(FusionRacksPage.ID_DELETE_SERVER % server.name):
            logging._log_to_console_and_log_file("Server with name %s Deleted" % server.name)
        else:
            logging._warn("Unable to Delete Server with name %s" % server.name)
    else:
        logging._log_to_console_and_log_file("Server with name %s not found in appliance" % server.name)
"""


def _add_server_in_rack(server):
    '''
   _add_server_in_rack function to add server from rack such as (servers both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Adding server with name %s" % server.name)
    selenium2lib = ui_lib.get_s2l()

    if selenium2lib._is_element_present(FusionRacksPage.ID_RACK_ITEM_IN_CONTAINER % server.name):
        logging._warn("Server %s already present in the appliance" % server.name)
        selenium2lib.capture_page_screenshot()
        return False

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_RACK_ITEM_IN_CONTAINER % server.name, fail_if_false=True)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_ADD)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROPDOWN_RACKSLOT)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_ROW % server.row)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_EDIT_SERVER_TO_RACK_CONFIRM)

    if selenium2lib._is_element_present(FusionRacksPage.ID_RACK_ITEM_IN_CONTAINER % server.name):
        return True
    else:
        selenium2lib.capture_page_screenshot()
        return False


"""
def _add_server_in_rack(server):
    '''
   _add_server_in_rack function to add server from rack such as (servers both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Adding server hardware with name %s" % server.name)
    selenium2lib = ui_lib.get_s2l()
    found = None
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if len(server.name) > 0:
        if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % server.name):
            logging._log_to_console_and_log_file("Adding server with name %s" % server.name)
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_DEVICE, server.name)
            if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_SEARCH_HARDWARE % server.name):
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_SERVER)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_ADD)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ClICK_DROP_DOWN_ALIGNMENT)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_ALIGNMENT % server.position)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_DROP_DOWN_ROW)
                if 1 <= int(server.row) <= 42:
                    selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\38')
                    val1 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                    while selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT) != server.row:
                        found = True
                        selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\40')
                        val2 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                        if(val1 == val2):
                            found = False
                            break
                        else:
                            val1 = val2
                    if not found:
                        logging._log_to_console_and_log_file("Please pass valid value")
                        selenium2lib.capture_page_screenshot()
                        return False
                    else:
                        logging._log_to_console_and_log_file("Valid value")
                else:
                    logging._warn("Enter value between 1 and 42")
                    selenium2lib.capture_page_screenshot()
                    return False
                if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_POWER_CONNECTIONS):
                    all_connections = server.powerconnections.split('/')
                    if (len(all_connections) > 1):
                        ui_lib.wait_for_element_visible(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                        selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                    else:
                        logging._log_to_console_and_log_file("Connections are less than 2")
                    for connection in all_connections:
                        power_connections = connection.split('-')
                        if power_connections[0] == "hardware2":
                            selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                            break
                    for connections in all_connections:
                        server_connections = connections.split('-')
                        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_POWERCONNECTION_SELECT_SERVER % (server_connections[0], server_connections[1]))
                else:
                    logging._log_to_console_and_log_file("No Power connections available")
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_RACK_OK)
                if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_HARDWARE % server.name):
                    logging._log_to_console_and_log_file("Server with name %s added to the rack" % server.name)
                else:
                    logging._log_to_console_and_log_file("Server with name %s not added" % server.name)
        else:
            logging._log_to_console_and_log_file("Server with name %s is already present in the appliance" % server.name)
    else:
        logging._log_to_console_and_log_file("The data for adding server is empty")
        selenium2lib.capture_page_screenshot()
        return False
"""


def _edit_enclosure_in_rack(enclosure):
    '''
   _edit_enclosure_in_rack function to add enclosure present in rack such as (enclosures both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Editing the enclosure present in the rack %s" % enclosure.name)
    logging._log_to_console_and_log_file("Adding hardware")
    selenium2lib = ui_lib.get_s2l()
    found = None
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if len(enclosure.name) > 0:
        logging._log_to_console_and_log_file("Add")
        if selenium2lib._is_element_present(FusionRacksPage.ID_DELETE_SERVER % enclosure.name):
            logging._log_to_console_and_log_file("Editing the enclosure")
            selenium2lib.mouse_over(FusionRacksPage.ID_DELETE_SERVER % enclosure.name)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_EDIT_SERVER_ENCLOSURE % enclosure.name)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ClICK_DROP_DOWN_ALIGNMENT)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_ALIGNMENT % enclosure.position)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_DROP_DOWN_ROW)
            if 1 <= int(enclosure.row) <= 42:
                selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\38')
                val1 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                while selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT) != enclosure.row:
                    found = True
                    selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\40')
                    val2 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                    if(val1 == val2):
                        found = False
                        break
                    else:
                        val1 = val2
                if not found:
                    logging._log_to_console_and_log_file("Please pass valid value")
                    selenium2lib.capture_page_screenshot()
                    return False
                else:
                    logging._log_to_console_and_log_file("Valid value")
            else:
                logging._warn("Enter value between 1 and 42")
                selenium2lib.capture_page_screenshot()
                return False
            if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_POWER_CONNECTIONS):
                all_connections = enclosure.powerconnections.split('/')
                if (len(all_connections) > 3):
                    ui_lib.wait_for_element_visible(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                    selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                else:
                    logging._log_to_console_and_log_file("Connections are less than 3")
                for connection in all_connections:
                    power_connections = connection.split('-')
                    if power_connections[0] == "enclosures4" or power_connections[0] == "enclosures5" or power_connections[0] == "enclosures6":
                        selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                        break
                for connections in all_connections:
                    enclosures_connections = connections.split('-')
                    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_POWERCONNECTION_SELECT_ENCLOSURE % (enclosures_connections[0], enclosures_connections[1]))
            else:
                logging._log_to_console_and_log_file("No Power connections available")
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_RACK_OK)
            '''
                        QXCR1001311022: [CST]  Irrelevant message is shown when PDU is edited.
                        Validation will fail because of above issue
                    '''
            if selenium2lib._is_element_present(FusionRacksPage.ID_EDIT_PDU_VALIDATE % enclosure.name):
                logging._log_to_console_and_log_file("Enclosure with name successfully edited %s" % enclosure.name)
            else:
                logging._warn("Enclosure with name is not updated %s" % enclosure.name)
        else:
            logging._log_to_console_and_log_file("No Enclosure with name %s is not present in the appliance" % enclosure.name)


def _remove_enclosure_from_rack(enclosure):
    '''
    _remove_hardware_from_rack function to delete hardware from rack such as (enclosures both managed and unmanaged)
    '''
    logging._log_to_console_and_log_file("Removing enclosure %s from the rack" % enclosure.name)
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if selenium2lib._is_element_present(FusionRacksPage.ID_DELETE_SERVER % enclosure.name):
        logging._log_to_console_and_log_file("Removing Enclosure")
        selenium2lib.mouse_over(FusionRacksPage.ID_DELETE_SERVER % enclosure.name)
        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_REMOVE_PDU % enclosure.name)
        if not selenium2lib._is_element_present(FusionRacksPage.ID_DELETE_SERVER_CONFIRM % enclosure.name):
            logging._log_to_console_and_log_file("Enclosure with name %s Deleted" % enclosure.name)
        else:
            logging._warn("Unable to Delete Enclosure with name %s" % enclosure.name)
    else:
        logging._log_to_console_and_log_file("Enclosure with name %s not found in appliance" % enclosure.name)


def _add_enclosure_to_rack(enclosure):
    '''
    Execute _add_pdu_edit_rack function due to below issue
    QXCR1001311316 : [CST]  Inconsistent behavior while adding an enclosure in the existing rack
    '''
    '''
    _add_hardware_to_rack function is used to add unmanaged and managed enclosures
    '''
    logging._log_to_console_and_log_file("Adding hardware")
    selenium2lib = ui_lib.get_s2l()
    found = None
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if len(enclosure.name) > 0:
        logging._log_to_console_and_log_file("Add")
        if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % enclosure.name):
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_DEVICE, enclosure.name)
            if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_SEARCH_HARDWARE % enclosure.name):
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_HARDWARE)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_ADD)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ClICK_DROP_DOWN_ALIGNMENT)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_ALIGNMENT % enclosure.position)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_DROP_DOWN_ROW)
                if 1 <= int(enclosure.row) <= 42:
                    selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\38')
                    val1 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                    while selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT) != enclosure.row:
                        found = True
                        selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\40')
                        val2 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                        if(val1 == val2):
                            found = False
                            break
                        else:
                            val1 = val2
                    if not found:
                        logging._log_to_console_and_log_file("Please pass valid value")
                        selenium2lib.capture_page_screenshot()
                        return False
                    else:
                        logging._log_to_console_and_log_file("Valid value")
                else:
                    logging._warn("Enter value between 1 and 42")
                    selenium2lib.capture_page_screenshot()
                    return False
                if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_POWER_CONNECTIONS):
                    all_connections = enclosure.powerconnections.split('/')
                    if (len(all_connections) > 3):
                        ui_lib.wait_for_element_visible(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                        selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                    else:
                        logging._log_to_console_and_log_file("Connections are less than 3")
                    for connection in all_connections:
                        power_connections = connection.split('-')
                        if power_connections[0] == "enclosures4" or power_connections[0] == "enclosures5" or power_connections[0] == "enclosures6":
                            selenium2lib.unselect_checkbox(FusionRacksPage.ID_BEST_PRACTISE_CONNECTIONS)
                            break
                    for connections in all_connections:
                        enclosures_connections = connections.split('-')
                        ui_lib.wait_for_element_and_click(FusionRacksPage.ID_POWERCONNECTION_SELECT_ENCLOSURE % (enclosures_connections[0], enclosures_connections[1]))
                else:
                    logging._log_to_console_and_log_file("No PDU'S available")
            else:
                logging._warn("No matching records found")
                selenium2lib.capture_page_screenshot()
                return False
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_RACK_OK)
            if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_HARDWARE % enclosure.name):
                logging._log_to_console_and_log_file("Hardware with name %s added to the racks" % enclosure.name)
            else:
                logging._log_to_console_and_log_file("Hardware with name %s not added" % enclosure.name)
        else:
            logging._log_to_console_and_log_file("Hardware with %s name is already present in the appliance" % enclosure.name)
    else:
        logging._log_to_console_and_log_file("Data to add the hardware is empty")


def _edit_pdu_rack(pdu):
    '''
    _edit_pdu_rack function is used to edit the PDU settings present in the rack
    '''
    logging._log_to_console_and_log_file("Editing PDU with IP")
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionRacksPage.ID_RACK_PDU_ITEM_IN_CONTAINER % pdu.pduip):
        logging._warn("PD with %s IP not found in the appliance" % pdu.pduip)
        selenium2lib.capture_page_screenshot()
        return False

    js_to_execute = """$('.hp-power-device').find('div').filter(function(){
    var title = $(this).attr('title');
    console.log(title);
    if(!title)
        return false;
    else
        return title.indexOf('%s')!=-1;
}).mouseenter();
$('div:visible.hp-edit').click();""" % pdu.pduip

    selenium2lib.execute_javascript(js_to_execute)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_MOUNT_POS)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_ROW % pdu.position)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROPDOWN_RACKSLOT)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_ROW % pdu.row)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_EDIT_SERVER_TO_RACK_CONFIRM)

    pos_id = selenium2lib.get_element_attribute(FusionRacksPage.ID_ATTR_ID_PDU % pdu.pduip)

    if pdu.position == 'Left':
        if pos_id != 'pduLeftTop':
            logging._warn("PD position is incorrect! Should be in left")
            selenium2lib.capture_page_screenshot()
            return False
        else:
            logging._log_to_console_and_log_file("PD position is correct")
            return True
    elif pdu.position == 'Right':
        if pos_id != 'pduRightBottom':
            logging._warn("PD position is incorrect! Should be in right")
            selenium2lib.capture_page_screenshot()
            return False
        else:
            logging._log_to_console_and_log_file("PD position is correct")
            return True
    elif pdu.position == 'Center':
        server_slot = selenium2lib.get_element_attribute(FusionRacksPage.ID_ATTR_TITLE_PDU % pdu.pduip)
        slot_no = re.search(r'Slots \d+:(\d+)', server_slot).group(1)
        if slot_no != pdu.row:
            logging._warn("PD slot is incorrect! Should be %s" % slot_no)
            selenium2lib.capture_page_screenshot()
            return False
        else:
            logging._log_to_console_and_log_file("PD slot is correct")
            return True


"""
def _edit_pdu_rack(pdu):
    '''
    _edit_pdu_rack function is used to edit the PDU settings present in the rack
    '''
    logging._log_to_console_and_log_file("Editing PDU with IP")
    selenium2lib = ui_lib.get_s2l()
    found = None
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if (logicalinterconnectgroups.validate_trap_ip(pdu.pduip)):
        if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % pdu.pduip):
            logging._log_to_console_and_log_file("Editing PDU")
            selenium2lib.mouse_over(FusionRacksPage.ID_VALIDATE_PDU % pdu.pduip)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_EDIT_PDU % pdu.pduip)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ClICK_DROP_DOWN_ALIGNMENT)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_ALIGNMENT % pdu.position)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_DROP_DOWN_ROW)
            if 1 <= int(pdu.row) <= 42:
                    selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\38')
                    val1 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                    while selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT) != pdu.row:
                        found = True
                        selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\40')
                        val2 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                        if(val1 == val2):
                            found = False
                            break
                        else:
                            val1 = val2
                if not found:
                        logging._log_to_console_and_log_file("Please pass valid value")
                        selenium2lib.capture_page_screenshot()
                        return False
                    else:
                        logging._log_to_console_and_log_file("Valid value")
            else:
                logging._warn("Enter value between 1 and 42")
                selenium2lib.capture_page_screenshot()
                return False
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_EDIT_OK_PDU)
            '''
            QXCR1001311022: [CST]  Irrelevant message is shown when PDU is edited.
            Validation will fail because of above issue
            '''
            if selenium2lib._is_element_present(FusionRacksPage.ID_EDIT_PDU_VALIDATE % pdu.pduip):
                logging._log_to_console_and_log_file("PDU successfully edited with IP %s" % pdu.pduip)
            else:
                logging._warn("PDU with IP %s not edited" % pdu.pduip)
        else:
            logging._warn("PDU with IP %s is not present in the appliance" % pdu.pduip)
    else:
        logging._warn("Invalid IP")
"""


def _remove_pdu_from_rack(pdu):
    '''
    _remove_pdu_from_rack function is used to remove PDU present in the appliance
    '''
    logging._log_to_console_and_log_file("Removing PDU with IP %s from the appliance..." % pdu.pduip)
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionRacksPage.ID_RACK_PDU_ITEM_IN_CONTAINER % pdu.pduip):
        logging._warn("PD with %s IP not found in the appliance" % pdu.pduip)
        selenium2lib.capture_page_screenshot()
        return False

    # ui_lib.wait_for_element_and_click("xpath=//div[contains(@class, 'hp-power-device')]//div[@class='hp-device-name'][contains(@title, '%s')]/.." % pdu.pduip)
    # mouse_over method from selenium sometimes not work. So use javascript to do mouse hover then click delete icon to delete PDU
    js_to_execute = """$('.hp-power-device').find('div').filter(function(){
    var title = $(this).attr('title');
    console.log(title);
    if(!title)
        return false;
    else
        return title.indexOf('%s')!=-1;
}).mouseenter();
$('div:visible.hp-close').click();""" % pdu.pduip

    selenium2lib.execute_javascript(js_to_execute)
    # selenium2lib.mouse_down("xpath=//div[contains(@class, 'hp-power-device')]//div[@class='hp-device-name'][contains(@title, '%s')]/../div[@class='hp-close']" % pdu.pduip)
    # selenium2lib.mouse_up("xpath=//div[contains(@class, 'hp-power-device')]//div[@class='hp-device-name'][contains(@title, '%s')]/../div[@class='hp-close']" % pdu.pduip)

    if not selenium2lib._is_element_present(FusionRacksPage.ID_RACK_PDU_ITEM_IN_CONTAINER % pdu.pduip):
        logging._log_to_console_and_log_file("PD with %s IP deleted" % pdu.pduip)
        return True
    else:
        logging._warn("Unable to Delete PDU with IP %s" % pdu.pduip)
        selenium2lib.capture_page_screenshot()
        return False


"""
def _remove_pdu_from_rack(pdu):
    '''
    _remove_pdu_from_rack function is used to remove PDU present in the appliance
    '''
    logging._log_to_console_and_log_file("Removing PDU with IP %s from the appliance..." % pdu.pduip)
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    if (logicalinterconnectgroups.validate_trap_ip(pdu.pduip)):
        if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % pdu.pduip):
            logging._log_to_console_and_log_file("Remove PDU")
            selenium2lib.mouse_over(FusionRacksPage.ID_VALIDATE_PDU % pdu.pduip)
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_REMOVE_PDU % pdu.pduip)
            if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % pdu.pduip):
                logging._log_to_console_and_log_file("PDU with IP %s Deleted" % pdu.pduip)
            else:
                logging._warn("Unable to Delete PDU with IP %s" % pdu.pduip)
        else:
            logging._warn("PDU with IP %s not found in appliance" % pdu.pduip)
"""


def _add_pdu_to_rack(add_hardware):
    '''
    _add_pdu_to_rack function is used to add PDU to the existing rack
    '''
    logging._log_to_console_and_log_file("Adding PDU to the %s rack" % add_hardware.pduip)
    selenium2lib = ui_lib.get_s2l()

    if selenium2lib._is_element_present(FusionRacksPage.ID_RACK_PDU_ITEM_IN_CONTAINER % add_hardware.pduip):
        logging._warn("Already PDU Added with %s IP present in the appliance" % add_hardware.pduip)
        selenium2lib.capture_page_screenshot()
        return False

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_PUD_IN_RACK % add_hardware.pduip, fail_if_false=True)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_ADD)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_MOUNT_POS)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_ROW % add_hardware.position)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROPDOWN_RACKSLOT)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_RACK_ROW % add_hardware.row)

    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_EDIT_SERVER_TO_RACK_CONFIRM)

    if selenium2lib._is_element_present(FusionRacksPage.ID_RACK_PDU_ITEM_IN_CONTAINER % add_hardware.pduip):
        return True
    else:
        selenium2lib.capture_page_screenshot()
        return False


"""
def _add_pdu_to_rack(add_hardware):
    '''
    _add_pdu_to_rack function is used to add PDU to the existing rack
    '''
    logging._log_to_console_and_log_file("Adding PDU to the %s rack" % add_hardware.pduip)
    selenium2lib = ui_lib.get_s2l()
    found = None
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT_RACK)
    ip = add_hardware.pduip
    if (logicalinterconnectgroups.validate_trap_ip(ip)):
        if not selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % add_hardware.pduip):
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_DEVICE, add_hardware.pduip)
            if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_SEARCH_PDU % add_hardware.pduip):
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_PDU)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_ADD)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ClICK_DROP_DOWN_ALIGNMENT)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_SELECT_ALIGNMENT % add_hardware.position)
                ui_lib.wait_for_element_and_click(FusionRacksPage.ID_CLICK_DROP_DOWN_ROW)
                if 1 <= int(add_hardware.row) <= 42:
                    selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\38')
                    val1 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                    while selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT) != add_hardware.row:
                        found = True
                        selenium2lib.press_key(FusionRacksPage.ID_SELECT_POSITION_ELEMENT, '\\40')
                        val2 = selenium2lib.get_text(FusionRacksPage.ID_SELECT_POSITION_ELEMENT)
                        if(val1 == val2):
                            found = False
                            break
                        else:
                            val1 = val2
                    if not found:
                        logging._log_to_console_and_log_file("Please pass valid value")
                        selenium2lib.capture_page_screenshot()
                        return False
                    else:
                        logging._log_to_console_and_log_file("Valid value")
                else:
                    logging._warn("Enter value between 1 and 42")
                    selenium2lib.capture_page_screenshot()
                    return False
            ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ADD_RACK_OK)
            if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % add_hardware.pduip):
                logging._log_to_console_and_log_file("PDU with %s IP added to the appliance" % add_hardware.pduip)
        else:
            logging._warn("Already PDU Added with %s IP present in the appliance" % add_hardware.pduip)
    else:
        logging._warn("Invalid IP Address")
"""


def _rack_general_properties(general):
    '''
    _rack_general_properties is used to edit the general properties of the rack.
    '''
    selenium2lib = ui_lib.get_s2l()
    logging._log_to_console_and_log_file("Editing general properties of Rack...")
    if len(general.newname) > 0:
        ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_RACK_NAME, general.newname)
    else:
        logging._warn("The new name of the rack is empty")
        selenium2lib.capture_page_screenshot()
        return False
    if len(general.Thermal) > 0:
        ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_THRMAL_LIMIT, general.Thermal)
    else:
        logging._warn("The Thermal limit is empty")
    if ui_lib.wait_for_element(FusionRacksPage.ID_INPUT_SERIEL_NUMBER, 20):
        if len(general.serial) > 0:
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_SERIEL_NUMBER, general.serial)
        else:
            logging._log_to_console_and_log_file("Serial number is empty")
    else:
        logging._log_to_console_and_log_file("Element is not present")
    if len(general.rackheight) > 0:
        if 1 <= int(general.rackheight) <= 50:
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_SLOT_HEIGHT, general.rackheight)
        else:
            logging._warn("Enter value between 1 and 50")
            selenium2lib.capture_page_screenshot()
            return False
    else:
        logging._warn("Rack height is empty")
        selenium2lib.capture_page_screenshot()
        return False
    if len(general.height) > 0:
        if 12 <= int(general.height) <= 120.3:
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_RACK_HEIGHT, general.height)
        else:
            logging._warn("A value between 12 and 120.3 (in)")
            selenium2lib.capture_page_screenshot()
            return False
    else:
        logging._warn("Height of the rack is empty")
        selenium2lib.capture_page_screenshot()
        return False
    if len(general.width) > 0:
        if 12 <= int(general.width) <= 72:
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_RACK_WIDTH, general.width)
        else:
            logging._warn("A value between 12 and 72 (in)")
            selenium2lib.capture_page_screenshot()
            return False
    else:
        logging._warn("Width of the rack is empty")
        selenium2lib.capture_page_screenshot()
        return False
    if len(general.depth) > 0:
        if 12 <= int(general.depth) <= 72:
            ui_lib.wait_for_element_and_input_text(FusionRacksPage.ID_INPUT_RACK_DEPTH, general.depth)
        else:
            logging._warn("A value between 12 and 72(in)")
            selenium2lib.capture_page_screenshot()
            return False
    else:
        logging._warn("Depth of the rack is empty")
        selenium2lib.capture_page_screenshot()
        return False


def select_rack(rackName):
    """ Select Rack

        Example:
        | `Select Rack`      |     |
    """
    selenium2lib = ui_lib.get_s2l()
    logging._log_to_console_and_log_file("Selecting Rack with name %s :" % rackName)
    # Verifying Racks page is opened or not. Opening if it is not opened
    if not selenium2lib._is_element_present(FusionRacksPage.
                                            ID_LINK_ADD_RACK):
        logging._log_to_console_and_log_file("Success")
        selenium2lib.click_element(FusionDashboardPage.ID_MENU_ONE_VIEW)
        selenium2lib.click_element(FusionDashboardPage.ID_LINK_RACKS)

    if not ui_lib.wait_for_element(FusionRacksPage.ID_LINK_ADD_RACK, PerfConstants.FUSION_PAGE_SYNC):
        logging._warn("Unable to open the Racks page")
        selenium2lib.capture_page_screenshot()
        return False
    else:
        # Verifying the presence of multiple racks with same name
        ui_lib.wait_for_element_visible(FusionRacksPage.ID_ELEMENT_RACK_NAME % rackName, PerfConstants.SELECT_RACK)
        count = len(selenium2lib._element_find(FusionRacksPage.ID_ELEMENT_RACK_NAME % rackName, False, False))
        logging._log_to_console_and_log_file("Number of racks %s with same name" % int(count))
        if (count > 1):
            logging._warn("There are more than one rack with same name")
            selenium2lib.capture_page_screenshot()
            return False
        # Verifying the presence of given rack and selecting
        else:
            if ui_lib.wait_for_element_visible(FusionRacksPage.ID_ELEMENT_RACK_NAME % rackName, PerfConstants.SELECT_RACK):
                selenium2lib.click_element(FusionRacksPage.ID_ELEMENT_RACK_NAME % rackName)
                selenium2lib.click_element(FusionRacksPage.ID_ELEMENT_RACK_NAME % rackName)
                if ui_lib.wait_for_element(FusionRacksPage.ID_ELEMENT_RACK_HEADER % rackName, PerfConstants.FUSION_PAGE_SYNC):
                    logging._log_to_console_and_log_file("Given rack with name %s is selected" % rackName)
                    return True
                else:
                    logging._warn("unable to select the given rack %s :" % rackName)
                    selenium2lib.capture_page_screenshot()
                    return False
            else:
                logging._warn("Given rack %s is not present in the appliance" % rackName)
                selenium2lib.capture_page_screenshot()
                return False


def _verify_device_in_rack(rackname, devicename):
    """ This function verifies existence of PDU in rack    """

    selenium2lib = ui_lib.get_s2l()
    logging._log_to_console_and_log_file("Verifying the newly added hardware %s in Rack %s" % (devicename, rackname))
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_ELEMENT_RACK_NAME % rackname)
    ui_lib.wait_for_element_visible(FusionRacksPage.ID_VALIDATE_PDU % devicename, PerfConstants.DEFAULT_SYNC_TIME)

    if selenium2lib._is_element_present(FusionRacksPage.ID_VALIDATE_PDU % devicename):
        logging._log_to_console_and_log_file("Hardware '%s' is exist in Rack '%s'" % (devicename, rackname))
    else:
        logging._warn("Hardware '%s' is not exist in Rack '%s'" % (devicename, rackname))


def verify_enclosure_in_rack(rack_name, enclosure_name):
    """ function verifies the rack information such as enclosure slots are automatically detected and
    Fusion sets the rack height automatically using the HP Intelligent Rack Location Discovery Services.
    Example:
    |    Fusion UI Verify Enclosure In Rack    |    ${rack_name}    |    ${enclosure_name}
    """
    selenium2lib = ui_lib.get_s2l()
    if not select_rack(rack_name):
        logging._warn("Intelligent series rack '%s' is not present , please provide the valid rack name " % rack_name)
        return False
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_PANEL_SELECTOR)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_GENERAL)
    ui_lib.wait_for_element_visible(FusionRacksPage.ID_LABEL_RACK_MODEL, PerfConstants.DEFAULT_SYNC_TIME)
    val1 = ui_lib.get_text(FusionRacksPage.ID_LABEL_RACK_MODEL)
    val2 = ui_lib.get_text(FusionRacksPage.ID_INPUT_SLOT_HEIGHT)
    ui_lib.wait_for_element_and_click(FusionRacksPage.ID_LINK_LAYOUT)
    selenium2lib.mouse_over(FusionRacksPage.ID_LINK_ENCLOSURE_RACK % enclosure_name)
    val3 = ui_lib.get_text(FusionRacksPage.ID_LABEL_ENCL_U_HEIGHT % enclosure_name)
    count = 0
    if val2 not in val1:
        logging._warn("enclosure slots are not automatically detected even the Enclosure is placed in an HP Intelligent Series Rack")
        count = 1
    else:
        logging._log_to_console_and_log_file("enclosure slots are automatically detected since the Enclosure is placed in an HP Intelligent Series Rack")

    if val2 > val3:
        logging._log_to_console_and_log_file("Fusion has set the rack height automatically using the HP Intelligent Rack Location Discovery Services.")
    else:
        logging._warn("enclosure slots are automatically detected since the Enclosure is placed in an HP Intelligent Series Rack")
        count = 1

    if count == 0:
        return True
    else:
        return False
