# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
   Data Centers Page
"""

from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.facilities.datacenters_elements import FusionDataCenterPage
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType


def navigate():
    FusionUIBase.navigate_to_section(SectionType.DATA_CENTERS)


def edit_data_center(datacenterName, *params):
    raise NotImplementedError


def add_datacenter(*datacenter_obj):
    '''
    add_datacenter function to add data center into appliance
    '''
    '''
    QXCR1001317088
    Racks layout is not resetting after clicking on ADD+ button in Data center page.
    In DataCenter page when we click on Add data center button by giving valid input , adding racks to the data center
    clicking on ADD+ button it is added , All the fields are getting reset except the racks and rack layout
    what we have added in previous data center, and when we are going to add one more data center by giving valid input
    ,adding racks to the data center we are not able to add data center.
    '''
    logging._log_to_console_and_log_file("Adding Data center to the appliance")
    selenium2lib = ui_lib.get_s2l()
    navigate()
    flag = None
    if isinstance(datacenter_obj, test_data.DataObj):
        datacenter_obj = [datacenter_obj]
    elif isinstance(datacenter_obj, tuple):
        datacenter_obj = list(datacenter_obj[0])
    # Go into adding the data center
    fail = 0
    for datacenters in datacenter_obj:
        # Function to call _add_datacenter_property
        flag = _add_datacenter_property(datacenters)
        add_rack = None
        if datacenters.has_property('addrack'):
            add_rack = datacenters.addrack
        if add_rack is None:
            logging._log_to_console_and_log_file("There is no new rack to be added")

        if isinstance(add_rack, (list)):
            for rack in add_rack:
                _add_rack_to_datacenter(rack)
        if flag:
            ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_BTN_ADD_DATACENTER)
            ui_lib.wait_for_element_visible(FusionDataCenterPage.ID_LINK_ADD_DATA_CENTER)
            if selenium2lib._is_element_present(FusionDataCenterPage.ID_LINK_ADD_DATA_CENTER):
                logging._log_to_console_and_log_file("Data center is successfully added")
            else:
                logging._warn("Data Center is not added")
                selenium2lib.capture_page_screenshot()
                fail += 1
        else:
            ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_BTN_CANCEL_PLUS_DATACENTER)
            logging._warn("Data center is not added")
            selenium2lib.capture_page_screenshot()
            fail += 1
    if fail > 0:
        return False
    return True


def verify_datacenter(*datacenter_obj):
    '''
    verify_datacenter function to make sure data center was added as prescribed
    '''
    rtnCode = True
    selenium2lib = ui_lib.get_s2l()
    navigate()
    if isinstance(datacenter_obj, tuple):
        datacenter_obj = list(datacenter_obj[0])
    elif isinstance(datacenter_obj, test_data.DataObj):
        datacenter_obj = [datacenter_obj]

    # validating if data center and rack are present in ui after adding or not ....
    for datacenter in datacenter_obj:
        logging._log_to_console_and_log_file("Checking for presence of data center %s..." % str(datacenter.name))
        select_datacenter(datacenter.name)
        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_DROP_DOWN, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_DROP_DOWN + "/ol//a[text()='Overview']")
        if selenium2lib.get_text(FusionDataCenterPage.ID_OVERVIEW_PAGE) != "Overview":
            ui_lib.fail_test('Failed to switch to Overview view for data center %s' % datacenter.name)
        # Validate the data center's basic settings
        ui_lib.wait_for_element_visible("id=cic-datacenter-details-dimensions")
        dcWidth = float(datacenter.width)
        dcDepth = float(datacenter.depth)
        dcWidthInches = int((dcWidth - int(dcWidth)) * 12)
        dcDepthInches = int((dcDepth - int(dcDepth)) * 12)
        dcSize = '%d\' %d" x %d\' %d"' % (int(dcWidth), dcWidthInches, int(dcDepth), dcDepthInches)
        errMsg = 'UI property not set as expected!  In field %s, saw "%s", expected "%s"'
        _validate_property(dcSize, "id=cic-datacenter-details-dimensions", errMsg)
        _validate_property(getattr(datacenter, 'derating', "NA/JP (20%)"), "id=cic-datacenter-details-electricalDerating", errMsg)
        _validate_property(getattr(datacenter, 'defaultvoltage', "220 V"), "id=cic-datacenter-details-defaultPowerLineVoltage", errMsg)
        if datacenter.has_property("powercost") and datacenter.has_property("currency"):
            _validate_property(datacenter.powercost + " " + datacenter.currency + " / kWh", "id=cic-datacenter-details-powerCosts", errMsg)
        else:
            _validate_property(None, "id=cic-datacenter-details-powerCosts", errMsg)
        _validate_property(getattr(datacenter, 'coolingcapacity', None), "id=cic-datacenter-details-coolingCapacity", errMsg)
        _validate_property(getattr(datacenter, 'coolingmultiplier', "1.5"), "cic-datacenter-details-coolingMultiplier", errMsg)
        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_DROP_DOWN, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_DROP_DOWN + "/ol//a[text()='Map']")
        if selenium2lib.get_text(FusionDataCenterPage.ID_OVERVIEW_PAGE) != "Map":
            ui_lib.fail_test('Failed to switch to Map view for data center %s' % datacenter.name)
        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_MAP_PAGE)
        ui_lib.wait_for_element_visible(FusionDataCenterPage.ID_VAL_DC_IN_MAP % str(datacenter.name), PerfConstants.SELECT_DATACENTER)
        # Make sure the data center is present
        if selenium2lib._is_element_present(FusionDataCenterPage.ID_VAL_DC_IN_MAP % str(datacenter.name)):
            logging._log_to_console_and_log_file("Data center %s is present in the appliance" % str(datacenter.name))
            # Find out if racks were added
            add_rack = None
            if datacenter.has_property('addrack'):
                add_rack = datacenter.addrack
            if add_rack is None:
                logging._warn("No rack was to be added to this data center.  Check the XML configuration.")
            if isinstance(add_rack, (list)):
                # Make sure each expected rack is in fact present
                for rack in add_rack:
                    if ui_lib.wait_for_element_visible(FusionDataCenterPage.ID_VAL_RACK_IN_DC % str(rack.rname)):
                        logging._log_to_console_and_log_file("Rack(s) with name %s is present in Datacenter" % str(rack.rname))
                    else:
                        ui_lib.fail_test("Rack(s) with name %s is not present in the Datacenter" % str(rack.rname))
                        rtnCode = False
        else:
            ui_lib.fail_test("Data center %s is not present in the appliance" % str(datacenter.name))
            rtnCode = False
    return rtnCode


def _validate_property(expectedValue, xpath, errMsg):
    selenium2lib = ui_lib.get_s2l()
    propertyValue = str(selenium2lib.get_text(xpath))
    if expectedValue is None:
        expectedValue = "not set"

    logging._log_to_console_and_log_file('Checking that element "%s" text is equal to "%s"' % (xpath, expectedValue))
    if expectedValue != propertyValue:
        ui_lib.fail_test(errMsg % (xpath, propertyValue, expectedValue))


def _add_rack_to_datacenter(rack):
    '''
        _add_rack_to_datacenter function to add rack into the data center
    '''
    if rack is None:
        logging._log_to_console_and_log_file("No racks have been specified to add to this data center.")
        return
    selenium2lib = ui_lib.get_s2l()
    ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_DROP_DOWN)
    ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_LINK_LAYOUT_RACK)
    if len(rack.rname) > 0:
        logging._log_to_console_and_log_file("adding rack(s) with name '%s' to the data center" % str(rack.rname))
        ui_lib.wait_for_element_and_input_text(FusionDataCenterPage.ID_INPUT_UNPOSITIONED_RACK, str(rack.rname))
        ui_lib.wait_for_element_and_click("xpath=//legend[.='Unpositioned Racks']")
        if selenium2lib._is_element_present(FusionDataCenterPage.ID_VALIDATE_DATACENTER % str(rack.rname)):
            logging._log_to_console_and_log_file("rack(s) with name '%s' is present among the Unpositioned racks; adding..." % str(rack.rname))
            ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_SELECT_RACK)
            ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_BTN_ADD_UNPOSITIONED_RACK)
            logging._log_to_console_and_log_file("Added '%s' to the data center" % str(rack.rname))
        else:
            logging._warn("Rack '%s' has not been defined in Fusion, or is unavailable as an unpositioned rack" % str(rack.rname))
    else:
        logging._log_to_console_and_log_file("rack name should not be empty")
    if not selenium2lib._is_element_present(FusionDataCenterPage.ID_VALIDATE_DATACENTER % str(rack.rname)):
        logging._log_to_console_and_log_file("Rack(s) with name %s has been added to the datacenter's racks layout, and is cleared from the Unmanaged Racks list" % str(rack.rname))
    else:
        logging._warn("Rack(s) with name %s did not get cleared from the Unmanaged Racks list (recurrence of QXCR1001348527)" % str(rack.rname))


def _add_datacenter_property(newdatacenter):
    '''
        Adding property of new data center
    '''
    # Wait for the "Add Data Center" button to appear, then click it
    ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_LINK_ADD_DATA_CENTER)
    # Wait for one of the elements on the "Add Data Center" dialog to appear
    ui_lib.wait_for_element(FusionDataCenterPage.ID_INPUT_DATACENTER_NAME)

    # Make sure the default values are as expected, as per the ALM test case 14.1.6
    logging._log_to_console_and_log_file('Validating defaults in "Add Data Center" dialog')
    selenium2lib = ui_lib.get_s2l()

    derating = str(selenium2lib.get_text(FusionDataCenterPage.ID_COMBO_ELECTRICAL_DERATING))
    if derating != "NA/JP":
        ui_lib.fail_test('Default value for electrical derating is not NA/JP; saw "%s"' % derating)
    defaultVoltage = str(selenium2lib.get_value(FusionDataCenterPage.ID_INPUT_DEFAULT_VOLTAGE))
    if defaultVoltage != "220":
        ui_lib.fail_test('Default value for voltage is not 220; saw %s' % defaultVoltage)
    coolingMultiplier = str(selenium2lib.get_value(FusionDataCenterPage.ID_INPUT_COOLING_MULTIPLIER))
    if coolingMultiplier != "1.5":
        ui_lib.fail_test('Default value for cooling multiplier is not 1.5; saw %s' % coolingMultiplier)

    # Add the data center to Fusion
    logging._log_to_console_and_log_file("Adding Data center with name %s" % newdatacenter.name)

    # Validate & input the settings now
    if len(newdatacenter.name) > 0:
        if len(newdatacenter.width) > 0:
            if 4 <= float(newdatacenter.width) <= 165:
                if len(newdatacenter.depth) > 0:
                    if 4 <= float(newdatacenter.depth) <= 165:
                        selenium2lib.input_text(FusionDataCenterPage.ID_INPUT_DATACENTER_NAME, str(newdatacenter.name))
                        selenium2lib.input_text(FusionDataCenterPage.ID_INPUT_WIDTH_DATACENTER, newdatacenter.width)
                        selenium2lib.input_text(FusionDataCenterPage.ID_INPUT_DEPTH_DATACENTER, newdatacenter.depth)
                    else:
                        logging._warn("enter valid depth , depth is not in range")
                        selenium2lib.capture_page_screenshot()
                        return False
                else:
                    logging._warn("depth is empty")
                    selenium2lib.capture_page_screenshot()
                    return False
            else:
                logging._warn("enter valid width , width is not in range")
                selenium2lib.capture_page_screenshot()
                return False
        else:
            logging._warn("width is empty")
            selenium2lib.capture_page_screenshot()
            return False
    else:
        logging._warn("data center name should not be empty")
        selenium2lib.capture_page_screenshot()
        return False
    if 1 <= int(newdatacenter.defaultvoltage) <= 9999:
        selenium2lib.input_text(FusionDataCenterPage.ID_INPUT_DEFAULT_VOLTAGE, int(newdatacenter.defaultvoltage))
    else:
        logging._warn("enter valid no.")
        selenium2lib.capture_page_screenshot()
        return False
    if newdatacenter.currency:
        if 1 <= len(newdatacenter.currency) <= 10:
            if newdatacenter.currency.isalpha():
                selenium2lib.input_text(FusionDataCenterPage.ID_INPUT_CURRENCY, newdatacenter.currency)
            else:
                logging._warn("currency: Enter a valid currency (alphabetic characters only).")
                selenium2lib.capture_page_screenshot()
                return False
        else:
            logging._warn("currency: can't enter more than 10 character")
            selenium2lib.capture_page_screenshot()
            return False
    if 1 <= int(newdatacenter.powercost) <= 9999:
        selenium2lib.input_text(FusionDataCenterPage.ID_INPUT_POWER_COST, int(newdatacenter.powercost))
    if 1 <= int(newdatacenter.coolingcapacity) <= 9999:
        selenium2lib.input_text(FusionDataCenterPage.ID_INPUT_COOLING_CAPACITY, int(newdatacenter.coolingcapacity))
    if 1 <= int(newdatacenter.coolingmultiplier) <= 9999:
        ui_lib.wait_for_element_and_input_text(FusionDataCenterPage.ID_INPUT_COOLING_MULTIPLIER, int(newdatacenter.coolingmultiplier))
    return True


def remove_datacenter(*datacenter_obj):
    '''
    remove_datacenter function to remove the datacenter from the appliance
    '''
    logging._log_to_console_and_log_file("Removing datacenter")
    if isinstance(datacenter_obj, test_data.DataObj):
        datacenter_obj = [datacenter_obj]
    elif isinstance(datacenter_obj, tuple):
        datacenter_obj = list(datacenter_obj[0])

    for datacenter in datacenter_obj:
        logging._log_to_console_and_log_file("Removing datacenter with name.... %s" % datacenter.name)
        select_datacenter(datacenter.name)
        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_MENU_ACTION_REMOVE)

        ui_lib.wait_for_element_and_click(FusionDataCenterPage.ID_BTN_YES_REMOVE_CONFIRMATION)
        ui_lib.refresh_browser(FusionDataCenterPage.ID_MAIN_MENU, PerfConstants.DEFAULT_SYNC_TIME)
        if ui_lib.wait_for_element_remove(FusionDataCenterPage.ID_SELECT_DATACENTER % str(datacenter.name)):
            logging._log_to_console_and_log_file("Datacenter with name %s Deleted" % datacenter.name)
        else:
            ui_lib.fail_test("Unable to Delete datacenter with name %s" % datacenter.name)
    return True


def select_data_center(self, datacenterName):
    raise NotImplementedError


def select_datacenter(datacenterName):
    """ Select Datacenter

        Example:
        | `Select Datacenter`      |     |
    """
    selenium2lib = ui_lib.get_s2l()
    logging._log_to_console_and_log_file("Selecting Datacenter with the Datacenter name %s :" % datacenterName)
    # Verifying datacenter page is opened or not. Opening if it is not opened
    if not selenium2lib._is_element_present(FusionDataCenterPage.ID_LINK_ADD_DATA_CENTER):
        logging._log_to_console_and_log_file("Datacenter Page is opening")
        navigate()

    if not ui_lib.wait_for_element(FusionDataCenterPage.ID_LINK_ADD_DATA_CENTER, PerfConstants.FUSION_PAGE_SYNC):
        logging._warn("Unable to open the Datacenters page")
        selenium2lib.capture_page_screenshot()
        return False
    else:
        # Verifying the presence of multiple s with same name
        ui_lib.wait_for_element_visible(FusionDataCenterPage.ID_SELECT_DATACENTER % datacenterName, PerfConstants.SELECT_DATACENTER)
        count = len(selenium2lib._element_find(FusionDataCenterPage.ID_SELECT_DATACENTER % datacenterName, False, False))
        logging._log_to_console_and_log_file("Number of datacenters %s with same name" % int(count))
        # Verifying the presence of given datacenter and selecting
        if (count == 1):
            if ui_lib.wait_for_element_visible(FusionDataCenterPage.ID_SELECT_DATACENTER % datacenterName, PerfConstants.SELECT_DATACENTER):
                logging._log_to_console_and_log_file("Given datacenter with name %s is selected" % datacenterName)
                selenium2lib.click_element(FusionDataCenterPage.ID_SELECT_DATACENTER % datacenterName)
            else:
                ui_lib.fail_test("unable to select the given datacenter %s :" % datacenterName)
        elif (count > 1):
            ui_lib.fail_test("There is more than one datacenter with same name")
        else:
            # Data center count is 0 or somehow negative
            ui_lib.fail_test("Could not find the data center named %s" % datacenterName)


def delete_all_datacenters():
    """
    delete all appliance datacenter
    """

    selenium2lib = ui_lib.get_s2l()
    """ Navigate to Datacenter Page """
    if not selenium2lib._is_element_present(FusionDataCenterPage.ID_PAGE_LABEL):
        navigate()

    datacenter_list = [ui_lib.get_text(el) for el in selenium2lib._element_find(FusionDataCenterPage.ID_Datacenter_LIST_NAMES, False, False)]
    count = 0
    for datacenter_name in datacenter_list:
        logging._log_to_console_and_log_file("Deleting datacenter: {0}".format(datacenter_name))
        datacenter_obj = test_data.DataObj()
        datacenter_obj.add_property('name', datacenter_name)
        net_obj = (datacenter_obj,)
        datacenter_delete_status = remove_datacenter(net_obj)

        if datacenter_delete_status:
            logging._log_to_console_and_log_file("'{0}' datacenter is deleted Successfully".format(datacenter_name))
            count += 1
        else:
            logging._warn("Failed to delete datacenter: {0}".format(datacenter_name))

    if count == len(datacenter_list):
        logging._log_to_console_and_log_file("All datacenters deleted successfully for appliance")
        return True
    else:
        logging._warn("Failed to delete '{0}' datacenters from appliance".format(len(datacenter_list) - count))
        return False
