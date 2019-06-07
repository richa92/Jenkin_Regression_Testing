# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Switches Page
"""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.business_logic.base import FusionUIBase, TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.cli.em import em_operation
from FusionLibrary.ui.business_logic.networking.switches import CommonOperationSwitches, VerifyOperationSwitches
import sys
import paramiko
import re
import time


def navigate():
    FusionUIBase.navigate_to_section(SectionType.SWITCHES)


def get_switch_state(switchname):
    '''
    function to get the switches state
    '''
    logger.info("Get Switch state and Model")

    navigate()
    # select the given switch
    if not select_switch(switchname):
        FusionUIBase.fail_test_or_return_false("Switch [%s] is not selected " % switchname)
    # verify action is not exists in switch
    VerifyOperationSwitches.verify_edit_notexist()
    VerifyOperationSwitches.verify_refresh_exist()
    # goto general section of the switch , if not already there
    CommonOperationSwitches.click_general_view()
    # get the switch state
    return CommonOperationSwitches.get_switch_state_and_model()


def get_switch_port_data(switchname):
    '''
    function to get vlan data from switch port
    '''
    logger.info("Retrive Networks which is assigned to switch port")
    navigate()
    # select the given switch
    if not select_switch(switchname):
        FusionUIBase.fail_test_or_return_false("Switch [%s] is not selected " % switchname)
    # goto general section of the switch , if not already there
    vlan_list = []
    if not CommonOperationSwitches.click_ports_in_dropdown():
        FusionUIBase.fail_test_or_return_false("Unable to select Ports in dropdown")
    # verify port channel and vPC Number are generated for switch ports
    if not VerifyOperationSwitches.verify_port_channel_generated():
        FusionUIBase.fail_test_or_return_false("PORT CHANNEL was not generated")
    if not VerifyOperationSwitches.verify_vpc_number_generated():
        FusionUIBase.fail_test_or_return_false("vPC NUMBER was not generated")
    i = 1
    flag = True
    while(flag):
        # get the switch port data
        if CommonOperationSwitches.get_table_row_data(i) is not None:
            # get port channel number
            if CommonOperationSwitches.get_port_data(i):
                vlan_data = CommonOperationSwitches.get_port_vlan_data(i)
                if vlan_data:
                    network_list = vlan_data.split("\n")
                    for net in network_list:
                        if re.match("^[a-zA-Z]+.*", net):
                            vlan_list.append(net)
                            logger.info("vlan data : %s" % net)
                    navigate()
            i = i + 1
        else:
            flag = False
    return vlan_list


def select_switch(switchname):
    """ Select switch
        Example:
        | `Select switch`      |     |
    """
    navigate()
    CommonOperationSwitches.click_switch(switchname)
    if VerifyOperationSwitches.verify_switch_selected(switchname):
        logger.info("The given switch is selected - %s" % switchname)
        return True
    else:
        FusionUIBase.fail_test_or_return_false("The given switch is not selected - %s" % switchname)


def verify_switch_edit(switchname):
    """ Verify switch edit option is available
        Example:
        | `Verify Switch Edit`      |  ${switchname}   |
    """
    navigate()
    # Select the given switch
    if not select_switch(switchname):
        FusionUIBase.fail_test_or_return_false("Switch [%s] is not selected " % switchname)
    return VerifyOperationSwitches.verify_edit_exist()


def enable_switch_port(*switch_obj):
    """ Enable / Disable switch port
    Example:
    | Switch Enable Port    | @{switch_list}
    """
    if isinstance(switch_obj, test_data.DataObj):
        switch_obj = [switch_obj]
    elif isinstance(switch_obj, tuple):
        switch_obj = list(switch_obj[0])

    navigate()

    for switch in switch_obj:
        logger.info("\nEditing Switch %s..." % switch.name)
        if(switch.name == ""):
            logger._warn("Mandatory field - name can't be empty")
            continue

        if not select_switch(switch.name):
            FusionUIBase.fail_test_or_return_false("Switch [%s] is not selected " % switch.name)
        port_number = switch.port[2:]
        if int(switch.port[:1]) >= 2:
            port_number = str(int(port_number) + int(switch.increment))
        if CommonOperationSwitches.edit_switch_port(port_number) is None:
            CommonOperationSwitches.click_ok_edit()
            return None
        CommonOperationSwitches.click_ok_edit()
    return CommonOperationSwitches.get_port_status(port_number)


def verify_switch_deleted(*switch_obj):
    """ After deleting Logical Switch, Switches will not exist in Switch page
    Example:
    | Verify Switches Deleted   | @{switch_list}
    """

    if isinstance(switch_obj, test_data.DataObj):
        switch_obj = [switch_obj]
    elif isinstance(switch_obj, tuple):
        switch_obj = list(switch_obj[0])

    navigate()
    for switch in switch_obj:
        if VerifyOperationSwitches.verify_switch_notexist(switch.name) is False:
            FusionUIBase.fail_test_or_return_false("SWITCH %s is visible" % switch.name)
    return True
