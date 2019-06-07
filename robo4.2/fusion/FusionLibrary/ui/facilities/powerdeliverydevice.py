# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Power Delivery Page
"""


import re
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.business_logic.facilities.powerdeliverydevice_elements import FusionPowerDeliveryDevicePage
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
import time


def navigate():
    FusionUIBase.navigate_to_section(SectionType.POWER_DELIVERY_DEVICES)


def add_power_delivery_device(*pdd_obj):
    """ This function is to add power delivery device
    add_power_delivery_device

        Example:
        add_power_delivery_device(*pdd_obj)
    """

    s2l = ui_lib.get_s2l()
    if not s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_LINK_ADD_POWER_DELIVERY_DEVICE)
    s2l.wait_until_page_contains_element(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_IPADDRESS)

    """ Retrieve data from data sheet """
    if isinstance(pdd_obj, test_data.DataObj):
        pdd_obj = [pdd_obj]
    elif isinstance(pdd_obj, tuple):
        pdd_obj = list(pdd_obj[0])

    for pddevice in pdd_obj:
        ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_SELECT_BOX_LABEL)
        ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_DROPDOWN_OPTION % pddevice.type)

        logger._log_to_console_and_log_file("*****************Adding power delivery device %s ************** " % pddevice.type)

        """ PDD type is hp intelligent power distribution unit """
        if (pddevice.type).lower() == "hp intelligent power distribution unit":
            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_IPADDRESS, pddevice.ip)
            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_USERNAME, pddevice.usrname)
            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_PWD, pddevice.password)
        else:

            """ PDD type is Power Feed,Breaker Panel,Branch circuit,Rack,Load Segment,Power strip,Outlet """
            if (pddevice.name == "" or pddevice.model == "" or pddevice.ratedcapacity == "" or pddevice.linevoltage == ""):
                logger._warn("Mandatory fields for adding PDU can't be empty for type %s" % pddevice.type)
                continue

            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_NAME, pddevice.name)
            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_MODEL, pddevice.model)

            """ Entering input for capacity  and Voltage"""
            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_CAPACITY, pddevice.ratedcapacity)
            if(s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ERR_CAPACITY_RANGE)):
                strerr1 = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ERR_CAPACITY_RANGE)
                if ("Enter a value between 1 and 9999" in strerr1):
                    logger._warn("Err message %s popup" % strerr1)
                    continue

            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_VOLTAGE, pddevice.linevoltage)
            if(s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ERR_VOLTAGE_RANGE)):
                strerr2 = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ERR_VOLTAGE_RANGE)
                if ("Enter a value between 1 and 999" in strerr2):
                    logger._warn("Err message %s popup" % strerr2)
                    continue

            """ Selecting values for volts and power feed if the input is not empty else default values """
            if not(pddevice.volts == ""):
                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_VOLTS_BOX_LABEL)
                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_DROPDOWN_OPTION % pddevice.volts)
            else:
                logger._log_to_console_and_log_file("As the given input is empty, default value Single Phase is selected for Volts")

            if not(pddevice.powerfeed == ""):
                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_POWERFEED_BOX_LABEL)
                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_DROPDOWN_OPTION % pddevice.powerfeed)
            else:
                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_POWERFEED_BOX_LABEL)
                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_DROPDOWN_OPTION % 'A')
                logger._log_to_console_and_log_file("As the given input is empty, default value A is selected for Power feed")

            """ input for optional parameters """
            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_PARTNUMBER, pddevice.partnumber)
            s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_SERIALNUMBER, pddevice.serialnumber)

            """  Add Connections """
            if hasattr(pddevice, 'connection'):
                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADD_CONNECTION)
                ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_INPUT_SEARCH_ADDCONN, PerfConstants.DEFAULT_SYNC_TIME)
                if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_INPUT_SEARCH_ADDCONN):
                    logger._log_to_console_and_log_file("Navigated to Add Connections Page")

                    """ Check for None Available text """
                    if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_TEXT_VERIFY):
                        logger._warn("No connections are available in Add Connections Page")
                        ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN_CANCEL)
                        continue
                    else:
                        for connection in pddevice.connection:
                            if(connection.conname == ""):
                                logger._warn("Mandatory fields for adding pdd connections can't be empty")
                                continue
                            if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ADD_CONN_CHOICE % connection.conname.strip()):
                                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_ADD_CONN_CHOICE % connection.conname.strip())
                                logger._log_to_console_and_log_file("Selected the given connection name %s" % connection.conname)
                                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN_ADDPLUS)

                    ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN_CANCEL, PerfConstants.DEFAULT_SYNC_TIME)
                    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN_CANCEL)

                    """ Validation in Add pdu page after the connections are added """
                    for connection in pddevice.connection:
                        if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_CONN_VERIFY % connection.conname.strip()):
                            logger._log_to_console_and_log_file("Added connection %s is available in Add PDU page" % connection.conname)
                        else:
                            ui_lib.fail_test("Added connection %s is not available in Add PDU page" % connection.conname)

                else:
                    ui_lib.fail_test("Fail to navigate Add Connections Page")

        """ Clicking on Add plus button for concurrent addition """
        if (pddevice.type).lower() == "hp intelligent power distribution unit":
            s2l.click_button(FusionPowerDeliveryDevicePage.ID_BTN_ADD_PLUS_POWER_DELIVERY_DEVICE)
        else:
            s2l.click_button(FusionPowerDeliveryDevicePage.ID_BTN_ADD_PLUS_MANUAL_POWER_DELIVERY_DEVICE)

        ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_ADD_PDU_MSG, PerfConstants.DEFAULT_SYNC_TIME)
        straddmsg = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ADD_PDU_MSG)

        """ Check for the err msg if displays """
        if (pddevice.type).lower() == "hp intelligent power distribution unit":
            if straddmsg.strip() == "Verifying parameters...":
                ui_lib.wait_for_element_notvisible(FusionPowerDeliveryDevicePage.ID_VERIFY_STATUS, PerfConstants.ADD_PDU_ERR_TIME)

            if(s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ADD_PDU_ERR_DETAILS)):
                straddmsg1 = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ADD_PDU_MSG)
                if straddmsg1.strip() == "Unable to add power delivery device":
                    logger._log_to_console_and_log_file("Unable to add pdu %s" % pddevice.ip)
                    msgText = s2l._get_text(FusionPowerDeliveryDevicePage.ID_ADD_PDU_ERR_DETAILS)
                    logger._warn(msgText)

                    strSearchText1 = "The power delivery device is already being managed by another management system"
                    strSearchText2 = "already been added"

                    if (strSearchText2 in msgText):
                        logger._warn("This pdu %s is already added to this appliance,Provide new PDU details" % pddevice.ip)
                        continue

                    if (strSearchText1 in msgText):
                        if pddevice.force == "true":
                            s2l.select_checkbox(FusionPowerDeliveryDevicePage.ID_CHK_FORCE_ADD_PDU)
                            s2l.click_button(FusionPowerDeliveryDevicePage.ID_BTN_ADD_PLUS_POWER_DELIVERY_DEVICE)
                        else:
                            continue

                        """ Check for the err msg after force adding """
                        s2l.wait_until_page_contains(straddmsg, PerfConstants.ADD_PDU_ERR_TIME)
                        ui_lib.wait_for_element_notvisible(FusionPowerDeliveryDevicePage.ID_VERIFY_STATUS, PerfConstants.ADD_PDU_ERR_TIME)
                        straddmsg3 = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ADD_PDU_MSG)

                        if straddmsg3.strip() == "Unable to add power delivery device":
                            logger._warn("Unable to add PDU %s after force adding,Check the pdu details" % pddevice.ip)
                            continue
                        else:
                            logger._log_to_console_and_log_file("Forcily adding the pdu %s" % pddevice.ip)
                    else:
                        logger._warn("Error msg displayed while adding pdu is %s" % msgText)
                        continue
                else:
                    continue

        else:
            straddmsg = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ADD_PDU_MSG)
            logger._log_to_console_and_log_file(straddmsg)
            if (straddmsg.strip() == "Added" + " " + pddevice.name):
                logger._log_to_console_and_log_file("PDU %s with name %s is added" % (pddevice.type, pddevice.name))

    if (pddevice.type).lower() == "hp intelligent power distribution unit":
        s2l.click_button(FusionPowerDeliveryDevicePage.ID_BTN_CANCEL_POWER_DELIVERY)
    else:
        ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_BTN_PDU_ADD_CANCEL_MANUAL)
        s2l.click_button(FusionPowerDeliveryDevicePage.ID_BTN_PDU_ADD_CANCEL_MANUAL)

    """ Verifying the Newly added PDU in existing PDU list """
    for pddevice in pdd_obj:
        ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_POWER_DELIVERY_DEVICE_LIST, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_notvisible(FusionPowerDeliveryDevicePage.ID_ADD_STATUS, PerfConstants.ADD_PDU_TIME)
        time.sleep(3)
        if (pddevice.type).lower() == "hp intelligent power distribution unit":
            if pddevice.has_property('force') and (pddevice.force).lower() == "false":
                logger._log_to_console_and_log_file("PDU %s is not available in pdu list as the force is false" % pddevice.ip)
                continue
            pddhp_pdu_obj = FusionPowerDeliveryDevicePage.ID_PDU_IN_LIST
            pddhp_pdu = s2l._get_text(pddhp_pdu_obj % pddevice.ip)
            pddevice.name = (pddhp_pdu).strip()

        logger._log_to_console_and_log_file("######## Verifying the Newly added PDU %s in pdu list #######" % pddevice.name)

        if not select_power_delivery_device(pddevice.name):
            ui_lib.fail_test("Newly added pdu %s is not available in PDU list " % pddevice.name)
        elif not ui_lib.wait_for_element_visible(FusionPowerDeliveryDevicePage.ID_ADD_IPDU_COMPLETED, FusionPowerDeliveryDevicePage.ADD_MAX_TIME):
            logger._warn('Timeout for wait adding pdu %s completed' % pddevice.name)
        else:
            if not (pddevice.type).lower() == "hp intelligent power distribution unit":
                _validate_power_delivery_device(pddevice.name, pdd_obj)
            logger._log_to_console_and_log_file('Add PDU %s successful' % pddevice.name)

    return True


def delete_power_delivery_device(*pdd_obj):
    """ This function is to delete power delivery device
    delete_power_delivery_device

        Example:
       fusion ui delete power delivery device  @{TestData.powerdeliverydevices}
    """
    failed_times = 0
    s2l = ui_lib.get_s2l()
    """ Navigate to Power Delivery Device Page """
    if not s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_PAGE_LABEL):
        navigate()

    if isinstance(pdd_obj, test_data.DataObj):
        pdd_obj = [pdd_obj]
    elif isinstance(pdd_obj, tuple):
        pdd_obj = list(pdd_obj[0])

    for pddevice in pdd_obj:
        ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_POWER_DELIVERY_DEVICE_LIST)

        """ Getting the hp intelligent power distribution unit name on providing the ip """
        if (pddevice.type).lower() == "hp intelligent power distribution unit":
            if pddevice.has_property('force') and (pddevice.force).lower() == "true":
                pddhp_pdu_obj = "xpath=//*/tbody//td[contains(text(), '%s')][1]"
                ui_lib.wait_for_element_visible(pddhp_pdu_obj % pddevice.ip)
                pddhp_pdu = s2l._get_text(pddhp_pdu_obj % pddevice.ip)
                pddevice.name = (pddhp_pdu).strip()
            else:
                continue

        """ Selecting and deleting the Power Delivery Device """
        logger._log_to_console_and_log_file("************** Deleting Power Delivery Device %s ********** " % pddevice.name)
        if not select_power_delivery_device(pddevice.name):
            logger._warn("Failed to select PDU %s" % pddevice.name)
            s2l.capture_page_screenshot()
            failed_times += 1
            continue
        else:
            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_ACTION_MAIN_BTN)
            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_ACTION_MENU_DELETE_PDD)
            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_CONFIRM_DELETE)
            ui_lib.wait_for_element_remove(FusionPowerDeliveryDevicePage.ID_ELEMENT_PDD_NAME_BASE % pddevice.name)

            """ validation after deletion """
            ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_POWER_DELIVERY_DEVICE_LIST)
            ui_lib.wait_for_element_remove(FusionPowerDeliveryDevicePage.ID_ELEMENT_PDD_NAME_BASE % pddevice.name, PerfConstants.DEFAULT_SYNC_TIME)
            ui_lib.wait_for_element_notvisible(FusionPowerDeliveryDevicePage.ID_ELEMENT_PDD_NAME_BASE % pddevice.name, PerfConstants.REMOVE_PDD_TIME)

            logger._log_to_console_and_log_file("Checking for pdd %s in the UI after deleting" % pddevice.name)
            if not(s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ELEMENT_PDD_NAME_BASE % pddevice.name)):
                logger._log_to_console_and_log_file('%s pdd deleted successfully' % pddevice.name)
            else:
                ui_lib.fail_test(" The Power Delivery Device " + pddevice.name + " not deleted successfully", "True")
                s2l.capture_page_screenshot()
                failed_times += 1

    if failed_times > 0:
        return False
    else:
        return True


def edit_power_delivery_device(*pdd_obj):
    """ This function is to edit power delivery device
    edit_power_delivery_device

        Example:
        edit_power_delivery_device(*pdd_obj)
    """
    failed_times = 0
    s2l = ui_lib.get_s2l()
    if not s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_PAGE_LABEL):
        navigate()

    if isinstance(pdd_obj, test_data.DataObj):
        pdd_obj = [pdd_obj]
    elif isinstance(pdd_obj, tuple):
        pdd_obj = list(pdd_obj[0])

    """ Selecting the given PDU """
    for pddevice in pdd_obj:
        if select_power_delivery_device(pddevice.name):
            logger._log_to_console_and_log_file("************* Editing PDU %s ******************** " % pddevice.name)
            s2l.click_element(FusionPowerDeliveryDevicePage.ID_ACTION_MAIN_BTN)
            s2l.click_element(FusionPowerDeliveryDevicePage.ID_ACTION_MENU_EDIT_PDU)
            ui_lib.wait_for_element_visible(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_NAME)

            """ Editing pdu type """
            if pddevice.has_property('type') and (pddevice.type).lower() != "hp intelligent power distribution unit" and pddevice.type != "":
                for key in pddevice.type:
                    s2l.press_key(FusionPowerDeliveryDevicePage.ID_SELECT_BOX_LABEL_EDITPDU, key)
                s2l.press_key(FusionPowerDeliveryDevicePage.ID_SELECT_BOX_LABEL_EDITPDU, chr(int(13)))
                logger._log_to_console_and_log_file("pdu type is updated as %s " % pddevice.type)

            """ Editing various fields """
            if pddevice.has_property('newname') and pddevice.newname != "":
                s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_NAME, pddevice.newname)
                pddevice.name = pddevice.newname

            if pddevice.has_property('model') and pddevice.model != "":
                s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_MODEL, pddevice.model)

            if pddevice.has_property('capacity') and pddevice.ratedcapacity != "":
                s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_CAPACITY, pddevice.ratedcapacity)
                if(s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ERR_CAPACITY_RANGE)):
                    strerr1 = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ERR_CAPACITY_RANGE)
                    if ("Enter a value between 1 and 9999" in strerr1):
                        logger._warn("Err message %s popup" % strerr1)
                        s2l.capture_page_screenshot()
                        failed_times += 1
                        continue

            if pddevice.has_property('voltage') and pddevice.linevoltage != "":
                s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_VOLTAGE, pddevice.linevoltage)
                if(s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ERR_VOLTAGE_RANGE)):
                    strerr2 = s2l.get_text(FusionPowerDeliveryDevicePage.ID_ERR_VOLTAGE_RANGE)
                    if ("Enter a value between 1 and 999" in strerr2):
                        logger._warn("Err message %s popup" % strerr2)
                        s2l.capture_page_screenshot()
                        failed_times += 1
                        continue

            if pddevice.has_property('volts') and pddevice.volts != "":
                for key in pddevice.volts:
                    s2l.press_key(FusionPowerDeliveryDevicePage.ID_VOLTS_BOX_LABEL, key)
                s2l.press_key(FusionPowerDeliveryDevicePage.ID_VOLTS_BOX_LABEL, chr(int(13)))

            if pddevice.has_property('powerfeed') and pddevice.powerfeed != "":
                s2l.press_key(FusionPowerDeliveryDevicePage.ID_POWERFEED_BOX_LABEL, pddevice.powerfeed)
                s2l.press_key(FusionPowerDeliveryDevicePage.ID_POWERFEED_BOX_LABEL, chr(int(13)))

            if pddevice.has_property('partnumber') and pddevice.partnumber != "":
                s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_PARTNUMBER, pddevice.partnumber)
            if pddevice.has_property('serialnumber') and pddevice.serialnumber != "":
                s2l.input_text(FusionPowerDeliveryDevicePage.ID_INPUT_PDD_SERIALNUMBER, pddevice.serialnumber)

            """ Add\Remove connections while editing based on connection attribute in datasheet"""
            if hasattr(pddevice, 'connection'):
                for connection in pddevice.connection:

                    if(connection.conname == ""):
                        logger._warn("Mandatory fields for adding pdd connections can't be empty")
                        s2l.capture_page_screenshot()
                        failed_times += 1
                        continue
                    else:
                        """ Add connections """
                        if((connection.addremoveconn).lower() == "true"):
                            logger._log_to_console_and_log_file("Add Connection %s to the pdu %s" % (connection.conname, pddevice.name))
                            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADD_CONNECTION_EDITPDU, fail_if_false=True)
                            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_ADD_CONN_EDITPDU % connection.conname.strip(), fail_if_false=True)
                            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN, fail_if_false=True)
                            # ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_EDIT_ADDCONN, fail_if_false=True)
                            """
                            if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_INPUT_SEARCH_ADDCONN):
                                logger._log_to_console_and_log_file("Navigated to Add Connections Page")

                                if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_TEXT_VERIFY):
                                    logger._warn("No connections are available in Add Connections Page")
                                    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN_CANCEL)
                                    continue

                                if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_ADD_CONN_CHOICE % connection.conname.strip()):
                                    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_ADD_CONN_CHOICE % connection.conname.strip())
                                    logger._log_to_console_and_log_file("Selected the given connection name %s" % connection.conname)
                                    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN)
                                else:
                                    logger._warn("Given input connection %s is not available in connection list to add" % connection.conname)
                                    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_ADDCONN_CANCEL)
                                    continue

                                if s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_CONN_EDITPDU % (connection.conname).strip()):
                                    logger._log_to_console_and_log_file("Added connection %s exists" % connection.conname)
                                else:
                                    logger._warn("Newly added connection %s not exists" % connection.conname)
                                    continue
                                """
                        elif((connection.addremoveconn).lower() == "false"):
                            """ Remove connections """
                            logger._log_to_console_and_log_file("Removing Connection %s from pdu %s" % (connection.conname, pddevice.name))
                            if not s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_CONN_EDITPDU % (connection.conname).strip()):
                                logger._warn("Connection '%s' is not present,give available connections as input" % connection.conname)
                                s2l.capture_page_screenshot()
                                failed_times += 1
                                continue
                            else:
                                ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_REMOVE_CONN_EDITPDU % (connection.conname).strip(), fail_if_false=True)
                                if not s2l._is_element_present(FusionPowerDeliveryDevicePage.ID_CONN_EDITPDU % (connection.conname).strip()):
                                    logger._log_to_console_and_log_file("Deletion successful,Connection %s is not exists after deleting" % connection.conname)
                                else:
                                    logger._warn("Fail in deleting Connection %s" % connection.conname)
                                    s2l.capture_page_screenshot()
                                    failed_times += 1
                                    continue
                        else:
                            logger._log_to_console_and_log_file("No Edit action on pdu %s connection %s" % (pddevice.name, connection.conname))

            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_BTN_EDIT_OK, fail_if_false=True)
            """ Verifying the pdu in pd device list after editing"""
            if select_power_delivery_device(pddevice.name):
                logger._log_to_console_and_log_file("After editing PDU %s is available in PDU list" % pddevice.name)
            else:
                ui_lib.fail_test("After editing PDU %s is not available in PDU list" % pddevice.name)

    if failed_times > 0:
        return False
    else:
        return True


def select_power_delivery_device(pddname):
    """ This function is to Select Power Delivery Device
    select_power_delivery_device

        Example:
       select_power_delivery_device(pddname)
    """
    selenium2lib = ui_lib.get_s2l()
    navigate()

    if selenium2lib._is_element_present(FusionPowerDeliveryDevicePage.ID_PAGE_LABEL):

        """ check for Power Delivery Device exists """
        if not (selenium2lib._is_element_present(FusionPowerDeliveryDevicePage.ID_ELEMENT_PDD_NAME_BASE % pddname.strip())):
            logger._warn("Power Delivery Device '%s' is not present" % pddname)
            selenium2lib.capture_page_screenshot()
            return False
        else:
            """ Select if Power Delivery Device exists """
            ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_ELEMENT_PDD_NAME_BASE % pddname.strip())
            ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_ELEMENT_PDD_NAME_BASE % pddname.strip() + "/ancestor::tr[contains(@class, hp-selected)]")
#             logger._log_to_console_and_log_file("Selected the Power Delivery Device %s successfully" % pddname)
            return True
    else:
        logger._log_to_console_and_log_file("Fail in navigating to Power Delivery Device Page")
        selenium2lib.capture_page_screenshot()
        return False


def _validate_power_delivery_device(pddname, *pdd_obj):
    """ This function is to validate Power Delivery Device through general view
    _validate_power_delivery_device

        Example:
       _validate_power_delivery_device(pddname)
    """

    s2l = ui_lib.get_s2l()
    """ Retrieving the pdd details of the given pdd name """
    pddevice = []
    for pddevice in pdd_obj[0]:
        if "name" in pddevice.properties:
            if (pddevice.name == pddname):
                break

    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_SELECT_BOX_OVERVIEW)
    ui_lib.wait_for_element_and_click(FusionPowerDeliveryDevicePage.ID_SELECT_GENERAL)

    """ dictionary to create xpath for the fields and values in General view """
    data = {'Type': 'deviceType', 'Model': 'model', 'Rated capacity': 'ratedCapacity', 'Line voltage': 'lineVoltage', 'Part number': 'partNumber',
            'Power feed': 'powerFeed', 'Serial number': 'serialNumber'}

    """ datasheet values for comparison """
    datadict_datasheet = {'type': pddevice.type, 'model': pddevice.model, 'ratedCapacity': pddevice.ratedcapacity, 'lineVoltage': pddevice.linevoltage,
                          'partnumber': pddevice.partnumber, 'powerFeed': pddevice.powerfeed, 'serialnumber': pddevice.serialnumber}

    """ Looping to compare available pdd field values with the values passed from datasheet"""
    for k, v in data.items():
        ui_lib.wait_for_element(FusionPowerDeliveryDevicePage.ID_ITEMS_GENERAL % (k, v))
        val = s2l._get_text(FusionPowerDeliveryDevicePage.ID_ITEMS_GENERAL % (k, v))

        """ for comparison making the data keys to same as datadict_datasheet keys"""
        if " " in k:
            k = re.sub('\s', '', k)
        for key in datadict_datasheet:
            if key.lower() == k.lower():
                if not len(datadict_datasheet[key]) > 0:
                    if key.lower() == "powerfeed":
                        datadict_datasheet[key] = "A"
                    else:
                        datadict_datasheet[key] = "not Set"

                if val.lower() == datadict_datasheet[key].lower():
                    boolverify = True
                    break
                else:
                    boolverify = False
                    logger._warn("The available appliance value is %s for field %s and given input is %s" % (val, k, datadict_datasheet[key]))
    if boolverify:
        logger._log_to_console_and_log_file("The pdd %s created successfully with the given input data" % pddname)
    else:
        ui_lib.fail_test("The pdd %s is not created with the given input" % pddname)
