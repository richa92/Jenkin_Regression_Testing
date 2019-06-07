# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Networks Page
"""

from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
# from FusionLibrary.ui.general import base_page
# from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.networking.networks_elements import FusionNetworksPage
from FusionLibrary.ui.business_logic.networking.networks import CommonOperationNetworks
from FusionLibrary.ui.business_logic.networking.networks import CreateNetworks
from FusionLibrary.ui.business_logic.networking.networks import EditNetworks
from FusionLibrary.ui.business_logic.networking.networks import DeleteNetworks
from FusionLibrary.ui.business_logic.networking.networks import VerifyNetworks
from FusionLibrary.ui.business_logic.networking.networks import EditScopeForNetworks
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.utilitylib import logging as logger


BW_MIN = 0.1
BW_MAX = 20.0
DEFAULT_PREFERRED_BW = 2.5
LINK_STABILITY_MIN = 1
LINK_STABILITY_MAX = 1800


def navigate():
    """
        Navigate to the Networks Page
    """
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if not ui_lib.wait_for_element(FusionNetworksPage.ID_PAGE_LABEL):
        ui_lib.fail_test("Failed to navigate to network page", True)


def create_fcoe_network(*net_obj):
    """ Create FCoE Network

    Arguments:
      name*        --  Name of FCoE network as a string.
      vlan         --  VLAN ID string. Set only if vlan_tag is 'Tagged'.
      maxbandswdth  --  Maximum bandwidth. Should be greater than 'preferredbw' argument. Defaults to 10 Gb/s.
      preferredbw  --  Preferred Bandwidth. Defaults to 2.5 Gb/s.
      san   --   Associated SAN.

    * Required Arguments

    Example:
        <myNetworks>
            <network name="300" vlan="300" maxbandwdth="10" san="wpstsw9_FID120-10:00:00:27:f8:2e:e8:98"/>
        </myNetworks>
    """
    s2l = ui_lib.get_s2l()

    if not ui_lib.wait_for_element(FusionNetworksPage.ID_PAGE_LABEL):
        navigate()

    logger._log_to_console_and_log_file("Create FCoE network")

    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj[0])

    ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_LINK_CREATE_NETWORK)
    ui_lib.wait_for_element(FusionNetworksPage.ID_INPUT_NETWORK_NAME)

    for net in net_obj:
        logger._log_to_console_and_log_file("")

        # Set network Name
        ui_lib.wait_for_element_and_input_text(FusionNetworksPage.ID_INPUT_NETWORK_NAME, net.name)

        # Select Ethernet Type
        s2l.select_checkbox(FusionNetworksPage.ID_RADIO_FCOE_TYPE)

        # Associating SAN with network for automation of zoning on the networks
        if not (net.san).upper() == "":
            ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_COMBO_ASSOCIATE_SAN)
            CreateNetworks.input_select_associate_with_san(net.san)

        else:
            logger._log_to_console_and_log_file("SAN not specified")

            if net.has_property("vlan"):
                ui_lib.wait_for_element_and_input_text(FusionNetworksPage.ID_INPUT_NETWORK_VLAND_ID, net.vlan)
            else:
                ui_lib.fail_test("Vlan ID not specified.")

        # Set Preferred bandwidth
        if net.has_property('preferredbw'):
            net.preferredbw = float(net.preferredbw)

            if not ((net.preferredbw >= BW_MIN) and (net.preferredbw <= BW_MAX)):
                ui_lib.fail_test("Invalid Preferred Bandwidth value specified (%s). Should be between %s and %s" % (net.preferredbw, BW_MIN, BW_MAX))
            else:
                ui_lib.wait_for_element_and_input_text(FusionNetworksPage.ID_INPUT_NETWORK_PREF_BANDWIDTH, str(net.preferredbw))
        else:
            # Use Default Bandwidth value
            net.preferredbw = float(DEFAULT_PREFERRED_BW)

        # Set Max bandwidth
        if net.has_property('maxbandwdth'):
            net.maxbandwdth = float(net.maxbandwdth)

            if not ((net.maxbandwdth >= BW_MIN) and (net.maxbandwdth <= BW_MAX)):
                ui_lib.fail_test("Invalid Max Bandwidth value specified (%s). Should be between %s and %s" % (net.maxbandwdth, BW_MIN, BW_MAX))
            elif not net.maxbandwdth >= net.preferredbw:
                ui_lib.fail_test("Invalid Max Bandwidth value specified (%s). Should be greater than Preferred Bandwidth (%s)" % (net.maxbandwdth, net.preferredbw))
            else:
                ui_lib.wait_for_element_and_input_text(FusionNetworksPage.ID_INPUT_NETWORK_MAXS_BANDWIDTH, str(net.maxbandwdth))

        # Click on the create plus button
        s2l.click_button(FusionNetworksPage.ID_BTN_CREATE_NETWORK_PLUS)
        s2l.page_should_not_contain("Failed to add fcoe network")

        if s2l._page_contains("Unable to add fcoe network"):
            ui_lib.fail_test("Unable to add fcoe network '{0}': {1}".format(net.name, s2l._get_text(FusionNetworksPage.ID_CREATE_NETWORK_MESSAGE_DETAILS)))
        else:
            logger._log_to_console_and_log_file("Successfully created FCOE network %s" % net.name)

        ui_lib.wait_for_condition(lambda: s2l._get_value(FusionNetworksPage.ID_INPUT_NETWORK_NAME) == "", fail_if_false=True)

    # Close Network Dialog
    s2l.click_button(FusionNetworksPage.ID_BTN_CLOSE_NETWORK)
    ui_lib.wait_for_element_remove(FusionNetworksPage.ID_CREATE_NETWORK_DIALOG)

    # perform validation if required
    if test_data.get_variable("Validate"):
        validate_network_exists(net_obj, fail_if_false=False)


def create_ethernet_networks(*net_obj):
    """ Create Ethernet Networks

    Arguments:
      name*            --      Name of ethernet network as a string.
      smart*           --      true/false for Smart Link.
      private*         --      true/false indicator for Private Network
      vlantype         --      Vlan Tag. Defaults to 'Tagged'.
      vlan             --      VLAN ID string. Set only if type is 'Tagged'.
      subnetid         --      Subnet ID . Set only for tagged/untagged networks.
      purpose          --      Purpose string. Ignored if not specified.
      maxbandswdth     --      Maximum bandwidth. Should be greater than 'preferredbw' argument. Defaults to 10 Gb/s.
      preferredbw      --      Preferred Bandwidth. Defaults to 2.5 Gb/s.
      remove_if_exists --      true/false for remove specified ethernet network if exists.

    * Required Arguments

    Example:
        <myNetworks>
            <network name="300"  smart="true" private="false" vlan="300" subnetid="1.1.1.0" purpose="" maxbandwdth="5"/>
        </myNetworks>
    """
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj)
    count = 0
    new_net_obj = []
    logger.info("{0} PREPARATION  {0}".format('-' * 17))

    for n, net in enumerate(net_obj):
        name = net.name
        if getattr(net, 'remove_if_exists', 'true').lower() == 'true':
            remove_if_exists = True
        else:
            remove_if_exists = False

        if not CommonOperationNetworks.verify_network_not_exist(name, fail_if_false=False):
            logger.warn("Network '{0}' already exists".format(name))
            if remove_if_exists is True:
                logger.info("Removing the network since 'remove_if_exists' is set to 'True'")
                if not delete_network(name, fail_if_false=False):
                    count += 1
                else:
                    new_net_obj.append(net)
            else:
                logger.warn("Error: Would not able to create the existing network '%s'." % name)
                count += 1
        else:
            new_net_obj.append(net)

    for n, net in enumerate(new_net_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(net_obj), '-' * 14))
        logger.info("Adding a ethernet network with name '{0}'".format(net.name))
        if n == 0:
            FusionUIBase.show_activity_sidebar()
            CreateNetworks.click_create_network_button()
        CreateNetworks.wait_create_network_dialog_shown()
        CreateNetworks.input_name(net.name)
        CreateNetworks.choose_type("Ethernet")
        if getattr(net, 'vlantype', '') != '':
            CreateNetworks.select_vlan(net.vlantype)
        if getattr(net, 'vlantype', '') == '' or net.vlantype.lower().strip() == "tagged":
            CreateNetworks.input_vlan_id(net.vlan)
        if getattr(net, 'purpose', '') != '':
            CreateNetworks.select_purpose(net.purpose)
        if getattr(net, 'vlantype', '') != '':
            if (net.vlantype.lower().strip() == 'untagged' or net.vlantype.lower().strip() == 'tagged') and net.has_property('subnetid'):
                CreateNetworks.select_subnetid(net.subnetid)
        if getattr(net, 'preferredbw', '') != '':
            CreateNetworks.input_preferred_bandwidth(net.preferredbw)
        if getattr(net, 'maxbandwdth', '') != '':
            CreateNetworks.input_maximum_bandwidth(net.maxbandwdth)

        if hasattr(net, 'smart'):
            FusionUIBase.para_should_be_in_list(["true", "false"], net.smart.lower())
            if net.smart.lower() == "true":
                CreateNetworks.tick_smart_link()
            else:
                CreateNetworks.untick_smart_link()
        if hasattr(net, 'private'):
            FusionUIBase.para_should_be_in_list(["true", "false"], net.private.lower())
            if net.private.lower() == "true":
                CreateNetworks.tick_private_network()
            else:
                CreateNetworks.untick_private_network()

        if n == (len(new_net_obj) - 1):
            CreateNetworks.click_create_button()
        else:
            CreateNetworks.click_create_plus_button()
            # TODO: Alex Chen: only show in short time, selenium may not catch it.
            # CreateNetworks.wait_verifying_message_shown()
            # CreateNetworks.wait_verifying_message_disappear(timeout=15)

        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)

        if hasattr(net, 'vlan'):
            vlan_range = net.vlan
            maximum_network = vlan_range.split("-", 1)
            if len(maximum_network) > 1:
                CreateNetworks.wait_for_bulk_assign_enet()
                navigate()
                net_count = CommonOperationNetworks.get_network_count()
                logger.info("network count is %s" % net_count)
                maximum_network = int(maximum_network[0]) + 1
                logger.info("max count is %s" % maximum_network)
                logger.info("name count is %s" % name)
                if net_count >= maximum_network:
                    logger.info("Successfully created the bulk networks : %s" % net_count)
                    # below declaration to create a network name pattern for bulk n/w creation using vlan id range
                    net.name = net.name + '_' + str(maximum_network)

                    logger.info("Net name is : %s " % net.name)
                    continue

                else:
                    ui_lib.fail_test("Failed to create the bulk networks")

        # FusionUIBase.wait_activity_action_ok(net.name, message="Create ethernet-networks", timeout=40)
        # 20150715 commented out since UI changed with "Create" only instead of "Create ethernet-networks"
        else:
            FusionUIBase.wait_activity_action_ok(net.name, message="Create", timeout=40)
    CreateNetworks.wait_create_network_dialog_disappear(timeout=10)
    FusionUIBase.show_activity_sidebar()
    logger.info("{0} VERIFICATION {0}".format('-' * 17))
    for n, net in enumerate(new_net_obj):
        CommonOperationNetworks.wait_network_status_ok(net.name)
        logger.info("Add ethernet network {0} successfully".format(net.name))

    if count > 0:
        logger.warn("Failure: Not able to create some of ethernet networks, please check all warning messages")
        return False

    return True


def create_fc_networks(*net_obj):
    """ Create FC Network

    Arguments:
      name*        --  Name of the network.
      fabrictype*  --  Fabric Type for network.
      preferredbw  --  Preferred Bandwidth. Defaults to 2.5Gb/s. Should be between 0.1 and 20.
      maxbandsdth  --  Maximum bandwidth. Should be greater than 'preferredbw' argument. Defaults to 10 Gb/s. Should be between 0.1 and 20.
      san          --  Associated SAN. Required for Fabric attach type.
      autologin    --  True/False parameter to indicate Login redistribution set to Auto. False = Manual. Required for Fabric attach type.
      linkstime    --  Link Stability Interval. Integer between 1 and 1800. Defaults to 30.

    Example:
        <fcnetworks>
            <fcnetwork *name="FA to 3Par Path 1" *fabrictype="FABRIC ATTACH" autologin="true" linkstime="50"  san="wpstsw9_FID120-10:00:00:27:f8:2e:e8:98"/>
            <fcnetwork *name="3par-b" *fabrictype="DIRECT ATTACH" preferredbw="8"  maxbandwdth="8"  />
        </fcnetworks>

    """
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj)
    count = 0
    new_net_obj = []
    logger.info("{0} PREPARATION  {0}".format('-' * 17))
    for n, net in enumerate(net_obj):
        name = net.name
        if getattr(net, 'remove_if_exists', 'true').lower() == 'true':
            remove_if_exists = True
        else:
            remove_if_exists = False

        if not CommonOperationNetworks.verify_network_not_exist(name, fail_if_false=False):
            logger.warn("Network '{0}' already exists".format(name))
            if remove_if_exists is True:
                logger.info("Removing the network since 'remove_if_exists' is set to 'True'")
                if not delete_network(name, fail_if_false=False):
                    count += 1
                else:
                    new_net_obj.append(net)
            else:
                logger.warn("Error: Would not able to create the existing network '%s'." % name)
                count += 1
        else:
            new_net_obj.append(net)

    for n, net in enumerate(new_net_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(net_obj), '-' * 14))

        logger.info("Adding a fc network with name '{0}'".format(net.name))

        if n == 0:
            FusionUIBase.show_activity_sidebar()
            CreateNetworks.click_create_network_button()
        CreateNetworks.wait_create_network_dialog_shown()
        CreateNetworks.input_name(net.name)
        CreateNetworks.choose_type("Fibre Channel")
        CreateNetworks.select_fabric_type(net.fabrictype)
        if getattr(net, 'preferredbw', '') != '':
            CreateNetworks.input_preferred_bandwidth(net.preferredbw)
        if getattr(net, 'maxbandwdth', '') != '':
            CreateNetworks.input_maximum_bandwidth(net.maxbandwdth)
        if net.fabrictype.lower() == "fabric attach":
            if getattr(net, 'san', '') != '':
                CreateNetworks.input_select_associate_with_san(net.san)
            FusionUIBase.para_should_be_in_list(["true", "false"], net.autologin.lower())
            if net.autologin.lower() == "true":
                method = "Auto"
            else:
                method = "Manual"
            CreateNetworks.toggle_login_redistribution(method)
            if getattr(net, 'linkstime', '') != '':
                CreateNetworks.input_link_stability_interval(net.linkstime)

        if n == (len(new_net_obj) - 1):
            CreateNetworks.click_create_button()
        else:
            CreateNetworks.click_create_plus_button()
            # TODO: Alex Chen: only show in short time, selenium may not catch it.
            # CreateNetworks.wait_verifying_message_shown()
            # CreateNetworks.wait_verifying_message_disappear(timeout=15)
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        # FusionUIBase.wait_activity_action_ok(net.name, message="Create fc-networks", timeout=40)
        # 20150715 commented out since UI changed with "Create" only instead of "Create fc-networks"
        FusionUIBase.wait_activity_action_ok(net.name, message="Create", timeout=40)
    CreateNetworks.wait_create_network_dialog_disappear(timeout=10)
    FusionUIBase.show_activity_sidebar()
    logger.info("{0} VERIFICATION {0}".format('-' * 17))
    for n, net in enumerate(new_net_obj):
        CommonOperationNetworks.wait_network_status_ok(net.name)
        logger.info("Add fc network {0} successfully".format(net.name))
    if count > 0:
        logger.warn("Failure: Not able to create some of fc networks, please check all warning messages")
        return False

    return True


def validate_network_exists(net_obj, fail_if_false=True):
    """
        Verify that the network exists
    """
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    return_code = True
    for net in net_obj:
        rc = CommonOperationNetworks.verify_network_exist(net.name, fail_if_false=False)
        if not rc:
            logger.warn("Network %s does not exist" % net.name)
            return_code = return_code and rc
        else:
            if CommonOperationNetworks.verify_locate_error_exists():
                selenium2lib = ui_lib.get_s2l()
                selenium2lib.reload_page()
    if fail_if_false is True:
        ui_lib.fail_test("Error: Some of networks does not exist")
    return return_code


def validate_network_does_not_exist(net_obj, fail_if_false=True):
    """
        Verify that the network does not exist
    """
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    return_code = True
    for net in net_obj:
        logger.info("Validating network '%s' does not exist" % net.name)
        rc = CommonOperationNetworks.verify_network_not_exist(net.name, fail_if_false=False)
        if not rc:
            logger.warn("Network %s does exist" % net.name)
            return_code = return_code and rc
    if fail_if_false is True:
        ui_lib.fail_test("Error: Some of networks exist")
    return return_code


def delete_all_appliance_networks():
    """
        Delete all networks on the appliance
    """
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    net_list = CommonOperationNetworks.get_network_list()
    net_obj_list = []
    for net_name in net_list:
        # logger.info("Deleting network %s" % net_name)
        net_obj = test_data.DataObj()
        net_obj.add_property('name', net_name)
        net_obj_list.append(net_obj)
    return delete_networks(*net_obj_list)


def delete_network(network, fail_if_false=True):
    """
        Delete a specific network
    """
    select_network(network)
    # 20150715 commented out since UI changed with "Delete" only instead of "Delete fc/ethernet-networks"
    # network_type = CommonOperationNetworks.get_general_type()
    # if network_type.lower() == "Fibre Channel".lower():
    #     activity_subject = "Delete fc-networks"
    # elif network_type.lower() == "Ethernet".lower():
    #     activity_subject = "Delete ethernet-networks"
    # elif network_type.lower() == "FCoE".lower():
    #     activity_subject = "Delete fcoe-networks"
    # else:
    #     activity_subject = "Unknown"
    DeleteNetworks.select_action_delete()
    DeleteNetworks.wait_delete_network_dialog_shown()
    DeleteNetworks.click_yes_delete()
    DeleteNetworks.wait_delete_network_dialog_disappear()
    FusionUIBase.show_activity_sidebar()
    # FusionUIBase.wait_activity_action_ok(network, activity_subject, timeout=50)
    # 20150715 commented out since UI changed with "Delete" only instead of "Delete fc/ethernet-networks"
    FusionUIBase.wait_activity_action_ok(network, 'Delete', timeout=50)
    FusionUIBase.show_activity_sidebar()
    if CommonOperationNetworks.wait_network_show_not_found(network, timeout=15, fail_if_false=False):
        logger.info("Network status appear as 'not found', remove network {0} successfully.".format(network))
        return True
    elif CommonOperationNetworks.verify_network_not_exist(network, timeout=5, fail_if_false=False):
        logger.info("Remove network {0} successfully".format(network))
        return True
    else:
        if fail_if_false is True:
            ui_lib.fail_test("The network does not disappear in 20s!")
        else:
            logger.warn("The network does not disappear in 20s!")


def delete_networks(*net_obj):
    """ Delete  Network """
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj)

    count = 0
    for n, net in enumerate(net_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(net_obj), '-' * 14))
        logger.info("Deleting a network with name %s" % net.name)
        if not select_network(net.name):
            count += 1
            continue

        delete_network(net.name)
    if count > 0:
        logger.warn("Not able to delete some of networks, please check warning message")
        return False
    return True


def edit_fc_networks(*net_obj):
    """ Edit FC Network    """
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj)
    count = 0
    for n, net in enumerate(net_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(net_obj), '-' * 14))
        logger.info("Editing a network with name '{0}'".format(net.name))
        if not select_network(net.name):
            count += 1
            continue

        EditNetworks.select_action_edit()
        EditNetworks.wait_edit_network_dialog_shown()
        if getattr(net, 'newname', '') != '':
            name = net.newname
            EditNetworks.input_name(net.newname)
        else:
            name = net.name

        if getattr(net, 'preferredbw', '') != '':
            EditNetworks.input_preferred_bandwidth(net.preferredbw)
        if getattr(net, 'maxbandwdth', '') != '':
            EditNetworks.input_maximum_bandwidth(net.maxbandwdth)
        networktype = EditNetworks.get_type()
        if networktype == "fabric attach":
            if getattr(net, 'san', '') != '':
                EditNetworks.input_select_associate_with_san(net.san)
            if getattr(net, 'autologin', '') != '':
                FusionUIBase.para_should_be_in_list(["true", "false"], net.autologin.lower())
                if net.autologin.lower() == "true":
                    method = "Auto"
                else:
                    method = "Manual"
                EditNetworks.toggle_login_redistribution(method)
            if getattr(net, 'linkstime', '') != '' and getattr(net, 'autologin', '') != '' and net.autologin != 'false':
                EditNetworks.input_link_stability_interval(net.linkstime)
        EditNetworks.click_ok_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        EditNetworks.wait_edit_network_dialog_disappear(timeout=10)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, "Update ethernet-networks", timeout=10)
        FusionUIBase.show_activity_sidebar()
        CommonOperationNetworks.wait_network_status_ok(name)
        logger.info("Edit network {0} successfully".format(net.name))
    if count > 0:
        logger.warn("Not able to edit some of networks, please check warning message")
        return False
    return True


def edit_ethernet_networks(*net_obj):
    """ Edit ethernet network    """

    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj)
    count = 0
    for n, net in enumerate(net_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(net_obj), '-' * 14))
        logger.info("Editing a network with name '{0}'".format(net.name))
        if not select_network(net.name):
            count += 1
            continue
        EditNetworks.select_action_edit()
        EditNetworks.wait_edit_network_dialog_shown()
        if getattr(net, 'newname', '') != '':
            name = net.newname
            EditNetworks.input_name(net.newname)
        else:
            name = net.name
        EditNetworks.select_purpose(net.purpose)
        if getattr(net, 'preferredbw', '') != '':
            EditNetworks.input_preferred_bandwidth(net.preferredbw)
        if getattr(net, 'maxbandwdth', '') != '':
            EditNetworks.input_maximum_bandwidth(net.maxbandwdth)

        if getattr(net, 'smart', '') != '':
            FusionUIBase.para_should_be_in_list(["true", "false"], net.smart.lower())
            if net.smart.lower() == "true":
                EditNetworks.tick_smart_link()
            else:
                EditNetworks.untick_smart_link()
        if getattr(net, 'private', '') != '':
            FusionUIBase.para_should_be_in_list(["true", "false"], net.private.lower())
            if net.private.lower() == "true":
                EditNetworks.tick_private_network()
            else:
                EditNetworks.untick_private_network()
        if getattr(net, 'subnetid', '') != '':
            EditNetworks.select_subnetid(net.subnetid)

        EditNetworks.click_ok_button()
        status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
        if status is True:
            ui_lib.fail_test(msg)
        EditNetworks.wait_edit_network_dialog_disappear(timeout=10)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(name, "Update", timeout=10)
        FusionUIBase.show_activity_sidebar()
        CommonOperationNetworks.wait_network_status_ok(name)
        logger.info("Edit network {0} successfully".format(net.name))
    if count > 0:
        logger.warn("Not able to edit some of networks, please check warning message")
        return False
    return True


def edit_ethernet_networks_capture_errors(*net_obj):
    """
    Keyword to Edit ethernet networks and capture any errors displayed on form or on the Footer .

    returns True on success else Raises an AssertionError Excetption in case of Error


    Input Example :
        <network name="EthVlan20"  newname="EthVlan20-Edited" smart="true" private="false" vlantype = "Tagged" vlan="20" subnetid = "100.100.100.0" purpose="General" maxbandwdth="5" />

    """

    error_msg_list = []
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj)
    count = 0
    try:
        for n, net in enumerate(net_obj):
            errors_on_form = []
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(net_obj), '-' * 14))
            logger.info("Editing a network with name '{0}'".format(net.name))
            if not select_network(net.name):
                count += 1
                continue
            EditNetworks.select_action_edit()
            EditNetworks.wait_edit_network_dialog_shown()
            if getattr(net, 'newname', '') != '':
                name = net.newname
                EditNetworks.input_name(net.newname)
            else:
                name = net.name

            if getattr(net, 'purpose', '') != '':
                EditNetworks.select_purpose(net.purpose)
            if getattr(net, 'preferredbw', '') != '':
                EditNetworks.input_preferred_bandwidth(net.preferredbw)
            if getattr(net, 'maxbandwdth', '') != '':
                EditNetworks.input_maximum_bandwidth(net.maxbandwdth)
            if getattr(net, 'smart', '') != '':
                FusionUIBase.para_should_be_in_list(["true", "false"], net.smart.lower())
                if net.smart.lower() == "true":
                    EditNetworks.tick_smart_link()
                else:
                    EditNetworks.untick_smart_link()
            if getattr(net, 'private', '') != '':
                FusionUIBase.para_should_be_in_list(["true", "false"], net.private.lower())
                if net.private.lower() == "true":
                    EditNetworks.tick_private_network()
                else:
                    EditNetworks.untick_private_network()
            if getattr(net, 'subnetid', '') != '':
                EditNetworks.select_subnetid(net.subnetid)

            EditNetworks.click_ok_button()

            errors_on_form = FusionUIBase.get_all_error_message_on_form(CommonOperationNetworks().edit_networks_formid)
            if errors_on_form:
                logger.warn("Error displayed on form for network {} - \n{}".format(net.name, errors_on_form))
                error_msg_list.append(errors_on_form)
                EditNetworks.click_cancel_button()
                continue
            else:
                logger.debug("No errors on Form")
                status, msg = FusionUIBase.get_error_message_from_dialog(timeout=5)
                if status is True:
                    logger.warn("Error Displayed for network {} - \n{}".format(net.name, msg))
                    EditNetworks.click_cancel_button()
                    error_msg_list.append(msg)
                    continue

            EditNetworks.wait_edit_network_dialog_disappear(timeout=10)
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok(name, "Update", timeout=10)
            FusionUIBase.show_activity_sidebar()
            CommonOperationNetworks.wait_network_status_ok(name)
            logger.info("Edit network {0} successfully".format(net.name))
    except Exception as Ex:
        # to handle any exceptions and close the edit dialog , so that subsequent tests can proceed
        if EditNetworks.wait_edit_network_dialog_shown(fail_if_false=False):
            EditNetworks.click_cancel_button()
        raise Ex

    if count > 0:
        logger.warn("Not able to edit some of networks, please check warning message")
        error_msg_list.append("Not able to edit some of networks, please check warning message")

    if error_msg_list:
        raise AssertionError(error_msg_list)
    return True


def verify_ethernet_network(*net_obj):
    """
        On the Networks Page, verify the ethernet networks
    """
    FusionUIBase.navigate_to_section(SectionType.NETWORKS)
    if isinstance(net_obj, test_data.DataObj):
        net_obj = [net_obj]
    elif isinstance(net_obj, tuple):
        net_obj = list(net_obj)
    count = 0
    for n, net in enumerate(net_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(net_obj), '-' * 14))
        logger.info("Verifying a network with name '{0}'".format(net.name))
        if not select_network(net.name):
            count += 1
            continue

        general_obj = net.General

        if hasattr(general_obj, "Type"):
            CommonOperationNetworks.verify_general_type(general_obj.Type.expected_value, 5, True)

        if hasattr(general_obj, "Vlan"):
            CommonOperationNetworks.verify_general_vlan(general_obj.Vlan.expected_value, 5, True)

        if hasattr(general_obj, "Purpose"):
            CommonOperationNetworks.verify_general_purpose(general_obj.Purpose.expected_value, 5, True)

        if hasattr(general_obj, "subnetid"):
            CommonOperationNetworks.verify_general_subnetid(general_obj.subnetid.expected_value)

        if hasattr(general_obj, "PreferredBandwidth"):
            CommonOperationNetworks.verify_general_preferred_bandwidth(general_obj.PreferredBandwidth.expected_value, 5, True)

        if hasattr(general_obj, "MaximumBandwidth"):
            CommonOperationNetworks.verify_general_maximum_bandwidth(general_obj.MaximumBandwidth.expected_value, 5, True)

        if hasattr(general_obj, "SmartLink"):
            CommonOperationNetworks.verify_general_smart_link(general_obj.SmartLink.expected_value, 5, True)

        if hasattr(general_obj, "PrivateNetwork"):
            CommonOperationNetworks.verify_general_private_network(general_obj.PrivateNetwork.expected_value, 5, True)

        if hasattr(general_obj, "UplinkSet"):
            CommonOperationNetworks.verify_general_uplink_set(general_obj.UplinkSet.expected_value, 5, True)

        if hasattr(general_obj, "UsedBy"):
            expect_list = []
            for used_by in general_obj.UsedBy:
                expect_value = used_by.expected_value
                expect_list.append(expect_value)
            CommonOperationNetworks.verify_general_used_by_server_profiles(expect_list, 5, True)

        logger.info("Verify network {0} successfully".format(net.name))
    if count > 0:
        logger.warn("Not able to edit some of networks, please check warning message")
        return False
    return True


def select_network(name):
    """ Select Network  """
    logger.info("Selecting a network with name {0}".format(name))
    if CommonOperationNetworks.verify_locate_error_exists():
        selenium2lib = ui_lib.get_s2l()
        selenium2lib.reload_page()
    if CommonOperationNetworks.verify_network_exist(name, fail_if_false=False):
        CommonOperationNetworks.click_network(name)
        CommonOperationNetworks.wait_network_selected(name)
        return True
    else:
        logger.warn("Network '{0}' does not exist".format(name))
        return False


def _list_networks():
    """ This function is to list the networks in appliance
        Example:
       _list_networks()
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to Network Page """
    if not ui_lib.wait_for_element(FusionNetworksPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(FusionNetworksPage.ID_NETWORK_LIST)
    networkdict = {}
    network_list = [ui_lib.get_webelement_attribute("text", el) for el in s2l._element_find(FusionNetworksPage.ID_NETWORK_LIST_NAMES, False, False)]
    for netobj in network_list:
        nettype = s2l._get_text(FusionNetworksPage.ID_NETWORK_TYPE % str(netobj))
        networkdict[netobj] = nettype
    return networkdict


def _list_networks_vlan():
    """ This function is to list the networks in appliance with the corresponding VLAN ID
        Example:
       _list_networks_vlan()
    """
    s2l = ui_lib.get_s2l()
    """ Navigate to Network Page """
    if not ui_lib.wait_for_element(FusionNetworksPage.ID_PAGE_LABEL):
        navigate()
    ui_lib.wait_for_element(FusionNetworksPage.ID_NETWORK_LIST)
    networkdict = {}
    network_list = [ui_lib.get_webelement_attribute("text", el) for el in s2l._element_find(FusionNetworksPage.ID_NETWORK_LIST_NAMES, False, False)]
    for netobj in network_list:
        vlan = s2l._get_text(FusionNetworksPage.ID_NETWORK_VLAN % str(netobj))
        networkdict[netobj] = vlan
    return networkdict


def action_visibility_check():
    """ Action Visibility check"""

    """ Loading Test data and selenium library """
    # selenium2lib = ui_lib.get_s2l()

    if not ui_lib.wait_for_element_visible(FusionNetworksPage.ID_ACTION_MAIN_BTN):
        logger._log_to_console_and_log_file("Action tab is not available")
        return False
    else:
        logger._log_to_console_and_log_file("Action tab is available")
        return True


def add_label_to_networks(network_obj):
    """
        On the Networks Page, add the label to the networks
    """

    s2l = ui_lib.get_s2l()
    """ Navigate to Network Page """
    logger._log_to_console_and_log_file("Function call to add label for each network ")
    if not ui_lib.wait_for_element(FusionNetworksPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(network_obj, test_data.DataObj):
        network_obj = [network_obj]
    elif isinstance(network_obj, tuple):
        network_obj = list(network_obj)

    for net in network_obj:
        ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_LINK_RESET)
        if not select_network(net.networkname):
            return False

        ui_lib.wait_for_element(FusionNetworksPage.ID_NETWORK_LIST)

        ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_COMBO_MENU_VIEW)
        ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_DROPDOWN_SELECTION)
        if ui_lib.wait_for_element(FusionNetworksPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionNetworksPage.ID_LABEL, FusionNetworksPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionNetworksPage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionNetworksPage.ID_LABEL_NAME, net.lname, 20)
                ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_ADD_LABEL_BTN)
                ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_OK_LABEL_BTN)
            else:
                logger._warn("Failed to navigate edit label panel")
                return False
        else:
            logger._warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionNetworksPage.ID_ADDED_LABEL % net.lname):
            ui_lib.wait_for_element_and_click(FusionNetworksPage.ID_ADDED_LABEL % net.lname)
            network_list = []
            ui_lib.wait_for_element(FusionNetworksPage.ID_NETWORK_LIST_NAMES)
            network_list = [ui_lib.get_text(s) for s in s2l._element_find(FusionNetworksPage.ID_NETWORK_LIST_NAMES, False, False)]
            for network in network_list:
                if network.lower() == net.networkname.lower():
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the network '{1}'".format(net.lname, net.networkname))
                else:
                    logger._warn("Failed to add label to the selected network")
                    return False
    return True


def validate_privileges_edit_network(nets_obj):
    """
        The function will validate the user permissions for edit network in the Action Menu based.

        Arguments:

            network object

    """
    logger.info("\nVerify Actions Menu for users")
    navigate()
    for n, net_obj in enumerate(nets_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(nets_obj), '-' * 14))
        logger.info("Verifying User Permissions for a network with name %s" % net_obj.name)
        select_network(net_obj.name)
        logger.info("Verifying Permissions")
        CommonOperationNetworks.click_action_button()
        logger.info("Verifying 'Edit' Action visible")
        if hasattr(net_obj, "NoAuthorization"):
            exp_msg = getattr(net_obj, "NoAuthorization")
            logger.info("expected message for users with no authorization is %s" % exp_msg)
            VerifyNetworks.verify_actions_noauthorization(exp_msg)
        else:
            VerifyNetworks.verify_actions_edit()
        logger.info("Permissions Verified")
    return True


def create_network_button_visibility_check():
    """ Create Network link visibility check"""
    navigate()
    return VerifyNetworks.verify_create_network_button_visible()


def edit_scope_for_networks(network_list):
    """ Edit scope for Networks
        This function is to edit scope for networks
        Example:
            edit_scope_for_networks(network_list)
    """
    logger.info("Function call to edit scope for networks ")
    navigate()
    for network in network_list:
        if not select_network(network.name):
            FusionUIBase.fail_test_or_return_false("Failed to find target networks")
        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForNetworks.click_edit_scope_button()
        EditScopeForNetworks.wait_edit_scope_dialog_open()
        if network.has_property("scopes"):
            scope_list = network.scopes.split(',')
            for scope in scope_list:
                if not VerifyNetworks.verify_scope_should_exist_in_edit_page(scope, 2, fail_if_false=False):
                    EditScopeForNetworks.click_assign_button()
                    EditScopeForNetworks.wait_assign_scope_dialog_open()
                    EditScopeForNetworks.input_scope_name(scope)
                    EditScopeForNetworks.click_scope_name(scope)
                    EditScopeForNetworks.click_add_button()
                    EditScopeForNetworks.wait_assign_scope_dialog_close()
        if network.has_property("remove_scopes"):
            remove_scope_list = network.remove_scopes.split(',')
            for scope in remove_scope_list:
                if VerifyNetworks.verify_scope_should_exist_in_edit_page(scope, timeout=5):
                    EditScopeForNetworks.click_remove_scope_icon(scope)
        EditScopeForNetworks.click_ok_button()
        EditScopeForNetworks.wait_edit_scope_dialog_close()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(network.name, 'Update', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
    return True
