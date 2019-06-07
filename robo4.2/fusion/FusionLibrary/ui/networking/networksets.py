# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Network Sets Page
"""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.business_logic.networking.networksets import *
from FusionLibrary.ui.networking.networksets_elements import FusionNetworkSetsPage
from FusionLibrary.ui.business_logic.base import SectionType
import sys


def navigate():
    FusionUIBase.navigate_to_section(SectionType.NETWORK_SETS)


def create_network_set(*networksets_obj):
    """ Create Network Set
        Example:
        | `Create Network Set`      | ${myNetworkSetList}    |
    """

    logger.info("Create Network Set")
    navigate()
    if isinstance(networksets_obj, test_data.DataObj):
        networksets_obj = [networksets_obj]
    elif isinstance(networksets_obj, tuple):
        networksets_obj = list(networksets_obj[0])

    fail_if_exist = 0

    for netset in networksets_obj:
        CreateNetworkSets.click_create_network_set_button()
        logger.info("Creating network set %s" % netset.name)
        if VerifyNetworkSets.verify_network_set_existed(netset.name, 5, False):
            fail_if_exist += 1
            logger.warn("Network set %s already exists" % netset.name)
            continue
        CreateNetworkSets.wait_create_network_set_dialog_shown()
        CreateNetworkSets.input_name(netset.name)
        if netset.has_property("preferredbw"):
            CreateNetworkSets.input_preferred_bandwidth(netset.preferredbw)
        if netset.has_property("maxbandwdth"):
            CreateNetworkSets.input_maximum_bandwidth(netset.maxbandwdth)
        networkList = netset.networks.split(',')
        for network in networkList:
            _Add_Netwok_To_Networkset_Add(network.strip())
        for network in netset.native.split(","):
            network = network.strip()
            EditNetworkSets.select_untagged_checkbox(network)
        CreateNetworkSets.click_create_plus_button()
        VerifyNetworkSets.verify_create_plus_complete()
        CreateNetworkSets.click_cancel_button()
        CreateNetworkSets.wait_create_network_set_dialog_disappear()
        CommonOperationNetworkSets.select_network_set(netset.name)
        VerifyNetworkSets.verify_network_set_created(netset.name)
        networkList = netset.networks.split(',')
        if len(networkList) > 0:
            for network in networkList:
                VerifyNetworkSets.verify_network_set_networks(network)

    if fail_if_exist > 0:
        return False
    return True


def delete_network_set(*networksets_obj):
    """ Delete Network Set

        Example:
        | `Delete Network Set`      | ${myNetworkSetList}    |
    """
    logger.info("Delete Network Set")
    navigate()
    if isinstance(networksets_obj, test_data.DataObj):
        networksets_obj = [networksets_obj]
    elif isinstance(networksets_obj, tuple):
        networksets_obj = list(networksets_obj[0])

    total = len(networksets_obj)
    not_exists = 0
    deleted = 0

    for n, netset in enumerate(networksets_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a network set named '%s'" % netset.name)
        if VerifyNetworkSets.verify_network_set_existed(netset.name) is True:
            select_network_set(netset.name)
            DeleteNetworkSets.click_delete_network_set_button()
            DeleteNetworkSets.click_yes_delete_button()
            DeleteNetworkSets.wait_delete_network_set_dialog_disappear()
            if VerifyNetworkSets.verify_network_set_deleted(netset.name, fail_if_false=False):
                logger.info("Network Set '%s' is deleted successfully" % netset.name)
            elif VerifyNetworkSets.verify_all_network_sets_not_found(fail_if_false=False):
                logger.info("All Network Sets are deleted successfully")
            else:
                BuiltIn().fail("Not able to delete Network Set" % netset.name)
            deleted += 1

        else:
            logger.warn("network set '%s' does NOT exist! ..." % netset.name)
            not_exists += 1
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no network set to delete! all %s network set(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if deleted < total:
            logger.warn("not all of the network set(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s not-existing network set(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                logger.warn("%s not-existing network set(s) is skipped, %s network set(s) left is failed being deleted " % (not_exists, total - deleted - not_exists))
                return False

    logger.info("all of the network set(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def select_network_set(netsetname):
    """ Select Network Set  """
    logger.info("Selecting networkset %s :" % netsetname)
    BuiltIn().sleep(3)
    navigate()
    CommonOperationNetworkSets.select_network_set(netsetname)
    VerifyNetworkSets.verify_network_set_created(netsetname)
    return True


def edit_network_set(*netset_obj):
    """ Edit Network Set    """
    logger.info("Edit Network Set")
    navigate()
    if isinstance(netset_obj, test_data.DataObj):
        netset_obj = [netset_obj]
    elif isinstance(netset_obj, tuple):
        netset_obj = list(netset_obj[0])
    fail_if_exist = 0
    # Looping to edit all the networkwts present in the resources.txt file
    for netset in netset_obj:
        logger.info("Editing network set %s" % netset.name)
        if netset.has_property("new_name"):
            if netset.new_name != netset.name and VerifyNetworkSets.verify_network_set_existed(netset.new_name, 5, False):
                fail_if_exist += 1
                logger.warn("Network set %s already exists, can't edit network set" % netset.new_name)
                continue
        # Selecting the given networkset
        if select_network_set(netset.name):
            # Clicking on edit button and verifying the edit options page
            BuiltIn().sleep(2)
            EditNetworkSets.click_edit_network_set_button()
            EditNetworkSets.wait_edit_network_set_dialog_shown()
            if netset.has_property("new_name"):
                data = _Verify_Parameter(netset.new_name, "Networkset Name")
                if not (data == "none" or data == ""):
                    EditNetworkSets.input_name(data)
            # Editing bandwidths
            if netset.has_property("preferredbw"):
                data = _Verify_Parameter(netset.preferredbw, "Priffered bandwidth")
                if not (data == "none" or data == ""):
                    EditNetworkSets.input_preferred_bandwidth(data)
            if netset.has_property("maxbandwdth"):
                data = _Verify_Parameter(netset.maxbandwdth, "Maximum Bandwidth")
                if not (data == "none" or data == ""):
                    EditNetworkSets.input_maximum_bandwidth(data)
            # deleting networks
            if netset.has_property("remove_networks"):
                for network in netset.remove_networks.split(","):
                    network = network.strip()
                    logger.info("Deleting network %s from networkset" % network)
                    EditNetworkSets.remove_networks_by_name(network)
                    VerifyNetworkSets.verify_network_deleted(network)
            # add networks
            if netset.has_property("add_networks"):
                for network in netset.add_networks.split(","):
                    _Add_Netwok_To_Networkset(network.strip())
            # Making networks as native
            if netset.has_property("native"):
                for network in netset.native.split(","):
                    network = network.strip()
                    EditNetworkSets.select_untagged_checkbox(network)
            EditNetworkSets.click_ok_button()
            EditNetworkSets.wait_edit_network_set_dialog_disappear()
    if fail_if_exist > 0:
        return False
    return True


def _Add_Netwok_To_Networkset(network):
    """_Add_Netwok_To_Networkset
       Add network to network set while editing the networkset.
        Example:
        | _Add_Netwok_To_Networkset(Network)"""

    if VerifyNetworkSets.verify_edit_network_existed(network):
        logger.info("Network %s is already added to the given networkset" % network)
        return True
    else:
        EditNetworkSets.click_add_networks_button()
        CreateNetworkSets.wait_add_network_dialog_shown()
        EditNetworkSets.input_network_name(network)
        BuiltIn().sleep(3)
        EditNetworkSets.click_network_name(network)
        EditNetworkSets.click_add_button()
        CreateNetworkSets.wait_add_network_dialog_disappear()
    return True


def _Add_Netwok_To_Networkset_Add(network):
    """_Add_Netwok_To_Networkset_Add
      Add network to network set while creating the networkset.
        Example:
        | _Add_Netwok_To_Networkset_Add(Network)"""

    if VerifyNetworkSets.verify_add_network_existed(network):
        logger.info("Network %s is already added to the given networkset" % network)
        return True
    else:
        CreateNetworkSets.click_add_networks_button()
        CreateNetworkSets.wait_add_network_dialog_shown()
        CreateNetworkSets.input_network_name(network)
        BuiltIn().sleep(3)
        CreateNetworkSets.click_network_name(network)
        CreateNetworkSets.click_add_button()
        CreateNetworkSets.wait_add_network_dialog_disappear()
    return True


# def _Select_Given_Network_As_Native(NativeNetwork):
#     """ Selecting given network as native """
#     selenium2lib = ui_lib.get_s2l()
#
# if no network is needed to select as native unselecting the already selected native naetwork
#     NetworkNames = []
#     count = len(selenium2lib._element_find(FusionNetworkSetsPage.ID_NETWORK_NETWORKSET_TABLE_ROW, False, False))
# reading all the network names
#     for i in range(count):
#         j = str(i + 1)
#         NetworkNames.append(str(selenium2lib.get_text(FusionNetworkSetsPage.ID_NETWORK_NETWORKSET_TABLE_NAME_COLUMN % j)))
# Unselecting all the check boxes
#     for network in NetworkNames:
#         if ui_lib.wait_for_element(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % network, PerfConstants.FUSION_PAGE_SYNC):
#             selenium2lib.unselect_checkbox(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % network)
#
#     if NativeNetwork != '':
# Verifying the given network is already present or not.If present we will make it as native
#         if selenium2lib._is_element_present(FusionNetworkSetsPage.ID_ELEMENT_NETWORKSET_NETWORK_NAME % NativeNetwork):
#             logging._log_to_console_and_log_file("Selecting network %s as native" % NativeNetwork)
#             if ui_lib.wait_for_element(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % NativeNetwork, PerfConstants.FUSION_PAGE_SYNC):
#                 selenium2lib.select_checkbox(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % NativeNetwork)
#                 selenium2lib.select_checkbox(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % NativeNetwork)
#                 logging._log_to_console_and_log_file("Selected the network %s as native" % NativeNetwork)
#             else:
#                 logging._warn("Check box to check the native network is not visible")
#         else:
# Adding network if it is not added
#             _Add_Netwok_To_Networkset(NativeNetwork)
# Making the network as native if it is successfully added
#             if ui_lib.wait_for_element(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % NativeNetwork, PerfConstants.FUSION_PAGE_SYNC):
#                 selenium2lib.select_checkbox(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % NativeNetwork)
#                 selenium2lib.select_checkbox(FusionNetworkSetsPage.ID_CHECKBOX_NATIVE_NETWORK_NETWORKSET % NativeNetwork)
#                 logging._log_to_console_and_log_file("Selected the network %s as native" % NativeNetwork)
#             else:
#                 logging._warn("Check box to check the native network is not visible")
#     else:
#         logging._log_to_console_and_log_file("Provided empty value for Native network")


def _Verify_Parameter(data, parameter):
    """ verifies the parameter value before updating
    if Empty as value then it will return "" to update
    if "" as value this function will return none as value

    """
    if data == "":
        logger.info("Provided empty value for %s so ignoring the update of %s" % parameter)
        return "none"
    elif data.upper() == "EMPTY":
        logger.info("Provided empty as value for %s" % parameter)
        return ""
    else:
        logger.info("Provided valid value for %s" % parameter)
        return data


def add_label_to_network_set(networkset_obj):

    s2l = ui_lib.get_s2l()
    """ Navigate to Network Page """
    logger._log_to_console_and_log_file("Function call to add label for each network ")
    if not ui_lib.wait_for_element(FusionNetworkSetsPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(networkset_obj, test_data.DataObj):
        networkset_obj = [networkset_obj]
    elif isinstance(networkset_obj, tuple):
        networkset_obj = list(networkset_obj)

    for net in networkset_obj:
        ui_lib.wait_for_element_and_click(FusionNetworkSetsPage.ID_LINK_RESET)
        if not select_network_set(net.networksetname):
            return False

        ui_lib.wait_for_element(FusionNetworkSetsPage.ID_NETWORK_SET_TABLE)

        ui_lib.wait_for_element_and_click(FusionNetworkSetsPage.ID_LINK_VIEW)
        ui_lib.wait_for_element_and_click(FusionNetworkSetsPage.ID_DROPDOWN_SELECTION)
        if ui_lib.wait_for_element(FusionNetworkSetsPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionNetworkSetsPage.ID_LABEL, FusionNetworkSetsPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionNetworkSetsPage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionNetworkSetsPage.ID_LABEL_NAME, net.lname, 20)
                ui_lib.wait_for_element_and_click(FusionNetworkSetsPage.ID_ADD_LABEL_BTN)
                ui_lib.wait_for_element_and_click(FusionNetworkSetsPage.ID_OK_LABEL_BTN)
            else:
                logger._warn("Failed to navigate edit label panel")
                return False
        else:
            logger._warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionNetworkSetsPage.ID_ADDED_LABEL % net.lname):
            ui_lib.wait_for_element_and_click(FusionNetworkSetsPage.ID_ADDED_LABEL % net.lname)
            network_list = []
            ui_lib.wait_for_element(FusionNetworkSetsPage.ID_NETWORK_SET_LIST_NAMES)
            network_list = [ui_lib.get_text(s) for s in s2l._element_find(FusionNetworkSetsPage.ID_NETWORK_SET_LIST_NAMES, False, False)]
            for network in network_list:
                if network.lower() == net.networksetname.lower():
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the network '{1}'".format(net.lname, net.networksetname))
                else:
                    logger._warn("Failed to add label to the selected network")
                    return False
    return True


def edit_scope_for_networksets(network_set_list):
    """ edit scope for networksets
        This function is to edit scope for networkset
        Example:
            edit_scope_for_networksets(network_set_list)
    """
    logger.info("Function call to edit scope for networksets ")
    navigate()

    for network_set in network_set_list:
        if not select_network_set(network_set.name):
            FusionUIBase.fail_test_or_return_false("Failed to find target interconnects")

        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForNetworkSet.click_edit_scope_button()
        EditScopeForNetworkSet.wait_edit_scope_dialog_open()
        if network_set.has_property("scopes"):
            scope_list = network_set.scopes.split(',')
            for scope in scope_list:
                if not VerifyNetworkSets.verify_scope_should_exist_in_edit_page(scope, 2, fail_if_false=False):
                    EditScopeForNetworkSet.click_assign_button()
                    EditScopeForNetworkSet.wait_assign_scope_dialog_open()
                    EditScopeForNetworkSet.input_scope_name(scope)
                    EditScopeForNetworkSet.click_scope_name(scope)
                    EditScopeForNetworkSet.click_add_button()
                    EditScopeForNetworkSet.wait_assign_scope_dialog_close()

        if network_set.has_property("remove_scopes"):
            remove_scope_list = network_set.remove_scopes.split(',')
            for scope in remove_scope_list:
                if VerifyNetworkSets.verify_scope_should_exist_in_edit_page(scope, timeout=5):
                    EditScopeForNetworkSet.click_remove_scope_icon(scope)

        EditScopeForNetworkSet.click_ok_button()
        EditScopeForNetworkSet.wait_edit_scope_dialog_close()

        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(network_set.name, 'Update', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
    return True


def delete_all_network_sets():
    FusionUIBase.navigate_to_section(SectionType.NETWORK_SETS)
    if not CommonOperationNetworkSets.wait_for_network_set_load():
        logger.info("There is no Network sets")
        return True
    net_list = CommonOperationNetworkSets.get_network_sets_list()
    net_set_obj_list = []
    for net_set_name in net_list:
        logger.info("Deleting network sets %s" % net_set_name)
        net_set_obj = test_data.DataObj()
        net_set_obj.add_property('name', net_set_name)
        net_set_obj_list.append(net_set_obj)
    if isinstance(net_set_obj_list, test_data.DataObj):
        net_set_obj_list = [net_set_obj_list]
    elif isinstance(net_set_obj_list, tuple):
        net_set_obj_list = list(net_set_obj_list)
    return delete_network_set(net_set_obj_list)
