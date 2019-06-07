# (C) Copyright 2019 Hewlett-Packard Enterprise Company, L.P.
"""
    Networks Page
"""
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.networking.networks_elements import GeneralNetworksElements
from FusionLibrary.ui.business_logic.networking.networks_elements import CreateNetworksElements
from FusionLibrary.ui.business_logic.networking.networks_elements import EditNetworksElements
from FusionLibrary.ui.business_logic.networking.networks_elements import EditScopeElements
from FusionLibrary.ui.business_logic.networking.networks_elements import DeleteNetworksElements
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.general import activity
from datetime import datetime
import types


class CommonOperationNetworks(object):
    """
        Common Operations for Networks
    """
    @property
    def edit_networks_formid(self):
        """
            On the Network Page, edit Network form id
        """
        return GeneralNetworksElements.ID_EDIT_NETWORKS_FORM

    @classmethod
    def get_network_count(cls):
        """
            On the Network Page, get network count
        """
        return ui_lib.get_text(GeneralNetworksElements.ID_NETWORK_COUNT)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_not_exist(cls, network, timeout=5, fail_if_false=True):
        """
            On the Network Page, verify that the network does not exist
        """
        logger.debug("verify Network '%s' is not existing" % network)
        if ui_lib.wait_for_element_notvisible(GeneralNetworksElements.ID_TABLE_NETWORK % network, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_exist(cls, network, timeout=5, fail_if_false=True):
        """
            On the Network Page, verify that the network does exist
        """
        logger.debug("verify network '%s' is existing" % network)
        if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_TABLE_NETWORK % network, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_locate_error_exists(cls, timeout=5, fail_if_false=True):
        """
            On the Network Page, verify if the unable to locate error exists
        """
        locateerror = "Unable to locate the item you requested."
        logger.debug("verify if '%s' error exists on the screen" % locateerror)
        if ui_lib.is_visible(GeneralNetworksElements.UNABLE_TO_LOCATE_ERROR % locateerror, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_status_ok(cls, network, timeout=5, fail_if_false=True):
        """
            On the Network Page, verify that a specific networks status is OK
        """
        logger.debug("verify whether network %s is ok" % network)
        if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_OK % network, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_status_warn(cls, network, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that a specific networks status is WARN
        """
        logger.debug("verify whether network %s is warning" % network)
        if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_WARN % network, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_status_error(cls, network, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that a specific networks status is an error
        """
        logger.debug("verify whether network %s is error" % network)
        if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_ERROR % network, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_network_list(cls, timeout=5):
        """
             On the Network Page, get the list of networks
        """
        logger.debug("Get all network names from table")
        network_list = []
        if ui_lib.wait_for_element(GeneralNetworksElements.ID_TABLE_NETWORKS, timeout):
            network_list = FusionUIBase.get_multi_elements_text(GeneralNetworksElements.ID_TABLE_NETWORKS, timeout, fail_if_false=True)
        return network_list

    @classmethod
    def click_network(cls, network, timeout=5):
        """
             On the Network Page, click a specific network
        """
        logger.debug("select network %s" % network)
        ui_lib.wait_for_element_and_click(GeneralNetworksElements.ID_TABLE_NETWORK % network, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_network_selected(cls, network, timeout=5, fail_if_false=True):
        """
            Wait until the specific network is selected
        """
        logger.debug("wait network '%s' is selected" % network)
        if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_TABLE_NETWORK_SELECTED % network, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_network_show_not_found(cls, network, timeout=5, fail_if_false=True):
        """
             On the Network Page, wait for network status = not found
        """
        logger.info("wait network status indicates to 'not found'")
        if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_TABLE_NETWORK_DELETED % network, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_action_button(cls, timeout=5):
        """
             On the Network Page, click the action menu button
        """
        logger.debug("click action button")
        ui_lib.wait_for_element_and_click(GeneralNetworksElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_network_status_ok(cls, network, timeout=10, fail_if_false=True):
        """
             On the Network Page, wait for the network status to be OK
        """
        start = datetime.now()
        logger.debug("waiting for network '%s' status indicates to ok" % network)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_OK % network, timeout=2, fail_if_false=False):
                logger.debug("network '%s' status is ok as expected." % network)
                return True
            elif ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_WARN % network, timeout=2, fail_if_false=False):
                err_msg = "network '%s' status is warning not as expected." % network
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_ERROR % network, timeout=2, fail_if_false=False):
                err_msg = "network '%s' status is error not as expected." % network
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("network status is unknown, waiting ...")
                continue
        err_msg = "Timeout to wait for network '%s' status indicates to ok." % network
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_network_status_ok_or_warn(cls, network, timeout=10, fail_if_false=True):
        """
             On the Network Page, wait for the network status to be OK or WARN
        """
        start = datetime.now()
        logger.debug("waiting for network '%s' status indicates to ok or warning" % network)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_OK % network, timeout=5, fail_if_false=False):
                logger.debug("network '%s' status is ok as expected." % network)
                return True
            elif ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_WARN % network, timeout=5, fail_if_false=False):
                logger.debug("network '%s' status is warning as expected." % network)
                return True
            elif ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_ERROR % network, timeout=5, fail_if_false=False):
                err_msg = "network '%s' status is error not as expected." % network
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("network '%s' status is unknown, waiting ..." % network)
                continue
        err_msg = "Timeout to wait for network '%s' status indicates to ok or warn." % network
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_network_status_error(cls, network, timeout=10, fail_if_false=True):
        """
             On the Network Page, wait for the network status to be an error
        """
        start = datetime.now()
        logger.debug("waiting for network '%s' status indicates to error" % network)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_OK % network, timeout=5, fail_if_false=False):
                err_msg = "network '%s' status is ok not as expected." % network
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_WARN % network, timeout=5, fail_if_false=False):
                logger.debug("network '%s' status is warning not as expected." % network)
                return False
            elif ui_lib.wait_for_element_visible(GeneralNetworksElements.ID_STATUS_NETWORK_ERROR % network, timeout=5, fail_if_false=False):
                logger.debug("network '%s' status is error as expected." % network)
                return True
            else:
                logger.debug("network '%s' status is unknown, waiting ..." % network)
                continue
        err_msg = "Timeout to wait for network status indicates to error."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    def get_general_type(cls, timeout=5):
        """
             On the Network Page, get the network type
        """
        logger.debug("Get network type")
        return FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_TYPE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_type(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network type is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_TYPE, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network type is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network type is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_vlan(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network vlan is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_VLAN, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network vlan is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network vlan is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_purpose(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network purpose is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_PURPOSE, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network purpose is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network purpose is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_subnetid(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network subnet id is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_SUBNETID, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("SubnetID is '%s' as expected" % actual_value)
            return True
        else:
            msg = "SubnetID is '%s' not as expected '%s'" % (actual_value, expect_value)
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_preferred_bandwidth(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network preferred bandwidth is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_PREFERRED_BANDWIDTH, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network preferred bandwidth is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network preferred bandwidth is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_maximum_bandwidth(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network maximum bandwidth is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_MAXIMUM_BANDWIDTH, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network maximum bandwidth is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network maximum bandwidth is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_smart_link(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network smart link is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_SMART_LINK, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network smart link is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network smart link is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_private_network(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that private network is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_PRIVATE_NETWORK, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network private network is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network private network is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_uplink_set(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network uplink set is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_UPLINK_SET, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network uplink set is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network uplink set is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by_server_profiles(cls, expect_list, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network used by server profiles is as expected
        """
        actual_list = FusionUIBase.get_multi_elements_text(GeneralNetworksElements.ID_TEXT_GENERAL_USED_BY_SERVER_PROFILES, timeout, fail_if_false)
        if (expect_list is None) or len(expect_list) == 0:
            expect_list = ['no server profiles']
        expect_list = [expect_list] if not isinstance(expect_list, types.ListType) else expect_list
        match_count = 0
        for expect_value in expect_list:
            for actual_value in actual_list:
                if actual_value.lower().strip() == expect_value.lower().strip():
                    match_count += 1
        if match_count == len(actual_list) == len(expect_list):
            logger.debug("network is used by server profile(s) '%s' as expected" % actual_list)
            return True
        else:
            msg = "network is used by server profile(s) '%s' not as expected" % actual_list
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by_storage_systems(cls, expect_list, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network used by storage systems is as expected
        """
        actual_list = FusionUIBase.get_multi_elements_text(GeneralNetworksElements.ID_TEXT_GENERAL_USED_BY_STORAGE_SYSTEMS, timeout, fail_if_false)
        if (expect_list is None) or len(expect_list) == 0:
            expect_list = ['no storage systems']
        expect_list = [expect_list] if not isinstance(expect_list, types.ListType) else expect_list
        match_count = 0
        for expect_value in expect_list:
            for actual_value in actual_list:
                if actual_value.lower().strip() == expect_value.lower().strip():
                    match_count += 1
        if match_count == len(actual_list) == len(expect_list):
            logger.debug("network is used by storage system(s) '%s' as expected" % actual_list)
            return True
        else:
            msg = "network is used by storage system(s) '%s' not as expected" % actual_list
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_member_of(cls, expect_list, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network member of is as expected
        """
        actual_list = FusionUIBase.get_multi_elements_text(GeneralNetworksElements.ID_TEXT_GENERAL_MEMBER_OF, timeout, fail_if_false)
        if (expect_list is None) or len(expect_list) == 0:
            expect_list = ['none']
        expect_list = [expect_list] if not isinstance(expect_list, types.ListType) else expect_list
        match_count = 0
        for expect_value in expect_list:
            for actual_value in actual_list:
                if actual_value.lower().strip() == expect_value.lower().strip():
                    match_count += 1
        if match_count == len(actual_list) == len(expect_list):
            logger.debug("network is member of '%s' as expected" % actual_list)
            return True
        else:
            msg = "network is member of '%s' not as expected" % actual_list
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_associate_with_san(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network associated san is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_ASSOCIATE_WITH_SAN, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network is associate with san '%s' as expected" % actual_value)
            return True
        else:
            msg = "network is associate with san '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_link_stability_interval(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Network Page, verify that network link stability interval
              is as expected
        """
        actual_value = FusionUIBase.get_text(GeneralNetworksElements.ID_TEXT_GENERAL_LINK_STABILITY_INTERVAL, timeout, fail_if_false)
        if actual_value.lower().strip() == expect_value.lower().strip():
            logger.debug("network link stability interval is '%s' as expected" % actual_value)
            return True
        else:
            msg = "network link stability interval is '%s' not as expected" % actual_value
            if fail_if_false is True:
                ui_lib.fail_test(msg)
            else:
                logger.warn(msg)
                return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_network_title(cls, network, timeout=10, fail_if_false=True):
        """
             On the Network Page, verify that network title is as expected
        """
        logger.info('verifying [ Network title= %s ] is visible' % network)
        ui_lib.wait_for_element(GeneralNetworksElements.ID_PAGE_LABEL, timeout=timeout, fail_if_false=fail_if_false)


class CreateNetworks(object):
    """
        Create Networks Dialog
    """
    @classmethod
    def click_create_network_button(cls, timeout=5):
        """
             On the Network Page, click network button
        """
        logger.debug("click create network button ")
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_BUTTON_CREATE_NETWORK, timeout, fail_if_false=True)

    @classmethod
    def select_action_create(cls, timeout=5):
        """
             On the Network Page, click action menu and select create
        """
        logger.debug("select action create")
        ui_lib.wait_for_element_and_click(GeneralNetworksElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_SELECT_ACTION_CREATE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_network_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
             Wait for the Create Network Dialog to be shown
        """
        logger.info('waiting create network dialog to show up ')
        if ui_lib.wait_for_element_visible(CreateNetworksElements.ID_DIALOG_CREATE_NETWORK, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_name(cls, name, timeout=5):
        """
             On the Create Network Dialog, input network name
        """
        logger.debug("input name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateNetworksElements.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def choose_type(cls, type_name, timeout=5):
        """
        Ethernet, Fibre Channel, FCoE
        """
        logger.debug("choose type '%s'" % type_name)
        if type_name.lower().strip() == 'ethernet':
            ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_RADIO_ETHERNET_TYPE, timeout, fail_if_false=True)
        elif type_name.lower().replace(' ', '') == 'fibrechannel':
            ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_RADIO_FIBRE_CHANNEL_TYPE, timeout, fail_if_false=True)
        elif type_name.lower().strip() == 'fcoe':
            ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_RADIO_FCOE_TYPE, timeout, fail_if_false=True)
        else:
            ui_lib.fail_test("unsupported network type '%s', please specify 'Ethernet', 'Fibre Channel', or 'FCoE'" % type_name)

    @classmethod
    def select_fabric_type(cls, type_name, timeout=5):
        """
             On the Create Network Dialog, select the fabric type
        """
        logger.debug("select fabric type '%s'" % type_name)
        expect_options = ["Fabric attach", "Direct attach"]
        FusionUIBase.para_should_be_in_list(expect_options, type_name)
        for option in expect_options:
            if type_name.lower().replace(' ', '') == option.lower().replace(' ', ''):
                type_name = option
                break
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_DROPDOWN_FABRIC_TYPE, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_SELECT_FABRIC_TYPE % type_name, timeout, fail_if_false=True)

    @classmethod
    def input_select_associate_with_san(cls, san, timeout=10):
        """
             On the Create Network Dialog, select san to associate network with
        """
        logger.debug("select san '%s'" % san)
        ui_lib.wait_for_element_and_input_text(CreateNetworksElements.ID_INPUT_ASSOCIATE_WITH_SAN, san, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_SELECT_ASSOCIATE_WITH_SAN % san, timeout, fail_if_false=True)

    @classmethod
    def select_vlan(cls, vlan_type, timeout=5):
        """
             On the Create Network Dialog, select vlan
        """
        logger.debug("select Vlan '%s'" % vlan_type)
        expect_options = ["Tagged", "Untagged", "Tunnel"]
        FusionUIBase.para_should_be_in_list(expect_options, vlan_type)
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_DROPDOWN_VLAN, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_SELECT_VLAN % vlan_type, timeout, fail_if_false=True)

    @classmethod
    def input_vlan_id(cls, vlan_id, timeout=5):
        """
             On the Create Network Dialog, input vlan id
        """
        logger.debug("input vlan id '%s'" % vlan_id)
        ui_lib.wait_for_element_and_input_text(CreateNetworksElements.ID_INPUT_NETWORK_VLAND_ID, vlan_id, timeout, fail_if_false=True)

    @classmethod
    def select_subnetid(cls, subnetid, timeout=10):
        """
             On the Create Network Dialog, select subnet id
        """
        logger.debug("Selecting subnetID : {}".format(subnetid))
        ui_lib.wait_for_element_and_input_text(CreateNetworksElements.ID_INPUT_SUBNETID, subnetid, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_OPTION_SUBNETID % subnetid, timeout, fail_if_false=True)

    @classmethod
    def select_purpose(cls, purpose, timeout=5):
        """
             On the Create Network Dialog, select the purpose
        """
        logger.debug("select purpose '%s'" % purpose)
        expect_options = ["General", "Management", "VM Migration", "Fault Tolerance", "iSCSI"]
        FusionUIBase.para_should_be_in_list(expect_options, purpose)
        for option in expect_options:
            if purpose.lower().replace(' ', '') == option.lower().replace(' ', ''):
                purpose = option
                break
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_DROPDOWN_PURPOSE, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_SELECT_PURPOSE % purpose, timeout, fail_if_false=True)

    @classmethod
    def input_preferred_bandwidth(cls, bandwidth, timeout=5):
        """
             On the Create Network Dialog, input preferred bandwidth
        """
        logger.debug("input preferred bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(CreateNetworksElements.ID_INPUT_PREFERRED_BANDWIDTH, bandwidth, timeout, fail_if_false=True)

    @classmethod
    def input_maximum_bandwidth(cls, bandwidth, timeout=5):
        """
             On the Create Network Dialog, input maximum bandwidth
        """
        logger.debug("input maximum bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(CreateNetworksElements.ID_INPUT_MAXIMUM_BANDWIDTH, bandwidth, timeout, fail_if_false=True)

    @classmethod
    def toggle_login_redistribution(cls, method, timeout=5):
        """
             On the Create Network Dialog, toggle login redistribution
        """
        logger.debug("toggle login redistribution '%s'" % method)
        currect_is_auto = ui_lib.wait_for_element_visible(CreateNetworksElements.ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO_VISIBLE, timeout=2, fail_if_false=False)
        if (currect_is_auto is True) and (method.lower() == "manual"):
            ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO, timeout, fail_if_false=True)
        elif (currect_is_auto is False) and (method.lower() == "auto"):
            ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_TOGGLE_LOGIN_REDISTRIBUTION_MANUAL, timeout, fail_if_false=True)

    @classmethod
    def input_link_stability_interval(cls, interval, timeout=5):
        """
             On the Create Network Dialog, input link stability interval
        """
        logger.debug("input link_stability_interval '%s' second(s)" % interval)
        ui_lib.wait_for_element_and_input_text(CreateNetworksElements.ID_INPUT_LINK_STABILITY_INTERVAL, interval, timeout, fail_if_false=True)

    @classmethod
    def tick_smart_link(cls, timeout=5):
        """
             On the Create Network Dialog, check smart link
        """
        logger.debug("check smart link")
        FusionUIBase.wait_for_checkbox_and_select(CreateNetworksElements.ID_CHECKBOX_SMART_LINK, timeout, fail_if_false=True)

    @classmethod
    def untick_smart_link(cls, timeout=5):
        """
             On the Create Network Dialog, uncheck smart link
        """
        logger.debug("uncheck smart link")
        FusionUIBase.wait_for_checkbox_and_unselect(CreateNetworksElements.ID_CHECKBOX_SMART_LINK, timeout, fail_if_false=True)

    @classmethod
    def tick_private_network(cls, timeout=5):
        """
             On the Create Network Dialog, check private network
        """
        logger.debug("check private network")
        FusionUIBase.wait_for_checkbox_and_select(CreateNetworksElements.ID_CHECKBOX_PRIVATE_NETWORK, timeout, fail_if_false=True)

    @classmethod
    def untick_private_network(cls, timeout=5):
        """
             On the Create Network Dialog, uncheck private network
        """
        logger.debug("uncheck private network")
        FusionUIBase.wait_for_checkbox_and_unselect(CreateNetworksElements.ID_CHECKBOX_PRIVATE_NETWORK, timeout, fail_if_false=True)

    @classmethod
    def click_create_button(cls, timeout=5):
        """
             On the Create Network Dialog, click create button
        """
        logger.debug("click create")
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_BUTTON_CREATE, timeout, fail_if_false=True)

    @classmethod
    def click_create_plus_button(cls, timeout=5):
        """
             On the Create Network Dialog, click create plus button
        """
        logger.debug("click create+")
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_BUTTON_CREATE_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        """
             On the Create Network Dialog, click cancel button
        """
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(CreateNetworksElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_network_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
             On the Create Network Dialog, select the purpose
        """
        logger.debug("waiting for create network dialog to disappear ")
        ui_lib.wait_for_element_notvisible(CreateNetworksElements.ID_DIALOG_CREATE_NETWORK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_bulk_assign_enet(cls, timeout=550, fail_if_false=True):
        """
             On the Create Network Dialog, wait for the bulk enet creation
        """
        logger.debug("waiting for bulk enet creation")
        activity.navigate()
        return ui_lib.wait_for_element(GeneralNetworksElements.ID_BULK_ENET_ASSIGN_ACTVITY, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_verifying_message_shown(cls, timeout=5, fail_if_false=True):
        """
             On the Create Network Dialog, verify parms message is shown
        """
        logger.debug("waiting for verifying parameters message to show up ")
        if ui_lib.wait_for_element_visible(CreateNetworksElements.ID_TEXT_VERIFYING_PARAMETERS, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_verifying_message_disappear(cls, timeout=5, fail_if_false=True):
        """
             Wait for verifying parms message to disappear
        """
        logger.debug("waiting for verifying parameters message to disappear ")
        if ui_lib.wait_for_element_notvisible(CreateNetworksElements.ID_TEXT_VERIFYING_PARAMETERS, timeout, fail_if_false):
            return True
        else:
            return False


class EditNetworks(object):
    """
        Edit Networks Dialog
    """
    @classmethod
    def select_action_edit(cls, timeout=5):
        """
             On the networkpage, select the action menu edit action
        """
        logger.debug("select edit network action")
        ui_lib.wait_for_element_and_click(GeneralNetworksElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditNetworksElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_network_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Edit Network Dialog to appear
        """
        logger.debug("waiting for edit network dialog to show up ")
        ui_lib.wait_for_element_visible(EditNetworksElements.ID_DIALOG_EDIT_NETWORK, timeout, fail_if_false)

    @classmethod
    def get_type(cls, timeout=5):
        """
             On the Edit Network Dialog, get the network type
        """
        logger.debug("get network type")
        return FusionUIBase.get_text(EditNetworksElements.ID_TEXT_TYPE, timeout, fail_if_false=True).lower()

    @classmethod
    def input_name(cls, name, timeout=5):
        """
             On the Edit Network Dialog, input the network name
        """
        logger.debug("input name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditNetworksElements.ID_INPUT_NAME, name, timeout, fail_if_false=True)

    @classmethod
    def input_select_associate_with_san(cls, san, timeout=5):
        """
             On the Edit Network Dialog, input the san associated with the network
        """
        logger.debug("input associate with SAN '%s'" % san)
        ui_lib.wait_for_element_and_input_text(EditNetworksElements.ID_INPUT_ASSOCIATE_WITH_SAN, san, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditNetworksElements.ID_SELECT_ASSOCIATE_WITH_SAN % san, timeout, fail_if_false=True)

    @classmethod
    def input_preferred_bandwidth(cls, bandwidth, timeout=5):
        """
             On the Edit Network Dialog, input preferred bandwidth
        """
        logger.debug("input preferred bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(EditNetworksElements.ID_INPUT_PREFERRED_BANDWIDTH, bandwidth, timeout, fail_if_false=True)

    @classmethod
    def input_maximum_bandwidth(cls, bandwidth, timeout=5):
        """
             On the Edit Network Dialog, input the maximum bandwidth
        """
        logger.debug("input maximum bandwidth '%s'" % bandwidth)
        ui_lib.wait_for_element_and_input_text(EditNetworksElements.ID_INPUT_MAXIMUM_BANDWIDTH, bandwidth, timeout, fail_if_false=True)

    @classmethod
    def select_subnetid(cls, subnetid, timeout=5, fail_if_false=True):
        """
             On the Edit Network Dialog, select the subnet id
        """
        logger.debug("Editing subnetID to : {}".format(subnetid))
        ui_lib.wait_for_element_and_input_text(EditNetworksElements.ID_INPUT_EDIT_SUBNETID, subnetid, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(EditNetworksElements.ID_OPTION_EDIT_SUBNETID % subnetid, timeout, fail_if_false)

    @classmethod
    def toggle_login_redistribution(cls, method, timeout=5):
        """
             On the Edit Network Dialog, toggle the login redistribution
        """
        logger.debug("toggle login redistribution '%s'" % method)
        current_is_auto = ui_lib.wait_for_element_visible(EditNetworksElements.ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO_VISIBLE, timeout=2, fail_if_false=False)
        if (current_is_auto is True) and (method.lower() == "manual"):
            ui_lib.wait_for_element_and_click(EditNetworksElements.ID_TOGGLE_LOGIN_REDISTRIBUTION_AUTO, timeout, fail_if_false=True)
        elif (current_is_auto is False) and (method.lower() == "auto"):
            ui_lib.wait_for_element_and_click(EditNetworksElements.ID_TOGGLE_LOGIN_REDISTRIBUTION_MANUAL, timeout, fail_if_false=True)

    @classmethod
    def input_link_stability_interval(cls, interval, timeout=5):
        """
             On the Edit Network Dialog, input link stability interval
        """
        logger.debug("input link_stability_interval '%s' second(s)" % interval)
        ui_lib.wait_for_element_and_input_text(EditNetworksElements.ID_INPUT_LINK_STABILITY_INTERVAL, interval, timeout, fail_if_false=True)

    @classmethod
    def select_purpose(cls, purpose, timeout=5):
        """
             On the Edit Network Dialog, select the network purpose
        """
        logger.debug("select purpose '%s'" % purpose)
        expect_options = ["General", "Management", "VM Migration", "Fault Tolerance"]
        FusionUIBase.para_should_be_in_list(expect_options, purpose)
        for option in expect_options:
            if purpose.lower().replace(' ', '') == option.lower().replace(' ', ''):
                purpose = option
                break
        ui_lib.wait_for_element_and_click(EditNetworksElements.ID_DROPDOWN_PURPOSE, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditNetworksElements.ID_SELECT_PURPOSE % purpose, timeout, fail_if_false=True)

    @classmethod
    def tick_smart_link(cls, timeout=5):
        """
             On the Edit Network Dialog, check the smart link
        """
        logger.debug("check smart link")
        FusionUIBase.wait_for_checkbox_and_select(EditNetworksElements.ID_CHECKBOX_SMART_LINK, timeout, fail_if_false=True)

    @classmethod
    def untick_smart_link(cls, timeout=5):
        """
             On the Edit Network Dialog, uncheck the smart link
        """
        logger.debug("uncheck smart link")
        FusionUIBase.wait_for_checkbox_and_unselect(EditNetworksElements.ID_CHECKBOX_SMART_LINK, timeout, fail_if_false=True)

    @classmethod
    def tick_private_network(cls, timeout=5):
        """
             On the Edit Network Dialog, check the private network
        """
        logger.debug("check private network")
        FusionUIBase.wait_for_checkbox_and_select(EditNetworksElements.ID_CHECKBOX_PRIVATE_NETWORK, timeout, fail_if_false=True)

    @classmethod
    def untick_private_network(cls, timeout=5):
        """
             On the Edit Network Dialog, uncheck the private network
        """
        logger.debug("uncheck private network")
        FusionUIBase.wait_for_checkbox_and_unselect(EditNetworksElements.ID_CHECKBOX_PRIVATE_NETWORK, timeout, fail_if_false=True)

    @classmethod
    def click_ok_button(cls, timeout=5):
        """
             On the Edit Network Dialog, click ok button
        """
        logger.debug("click ok")
        ui_lib.wait_for_element_and_click(EditNetworksElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        """
             On the Edit Network Dialog, click cancel button
        """
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(EditNetworksElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_network_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
             Wait for the Edit Network Dialog to disappear
        """
        logger.debug("waiting for edit network dialog to disappear ")
        ui_lib.wait_for_element_notvisible(EditNetworksElements.ID_DIALOG_EDIT_NETWORK, timeout, fail_if_false)


class DeleteNetworks(object):
    """
        Delete Networks Dialog
    """
    @classmethod
    def select_action_delete(cls, timeout=5):
        """
             On the Network Page, select the action menu delete action
        """
        logger.debug("select delete network action")
        ui_lib.wait_for_element_and_click(GeneralNetworksElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(DeleteNetworksElements.ID_SELECT_ACTION_DELETE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_network_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
             On the Network Page, wait for the delete network dialog to be shown
        """
        logger.debug("waiting for delete network dialog to show up ")
        ui_lib.wait_for_element_visible(DeleteNetworksElements.ID_DIALOG_DELETE, timeout, fail_if_false)

    @classmethod
    def click_yes_delete(cls, timeout=5):
        """
             On the Delete Network Dialog, click the yes delete button
        """
        logger.debug("click 'Yes, delete'")
        ui_lib.wait_for_element_and_click(DeleteNetworksElements.ID_BUTTON_YES_DELETE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel(cls, timeout=5):
        """
             On the Delete Network Dialog, click the cancel button
        """
        logger.debug("click 'cancel'")
        ui_lib.wait_for_element_and_click(DeleteNetworksElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_network_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
            Wait for Delete Network Dialog to disappear
        """
        logger.debug("waiting for delete network dialog to disappear ")
        ui_lib.wait_for_element_notvisible(DeleteNetworksElements.ID_DIALOG_DELETE, timeout, fail_if_false)


class VerifyNetworks(object):
    """
        Verify Network values
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_edit(cls, timeout=5, fail_if_false=True):
        """
             On the Network Page, select the action menu edit action
        """
        logger.debug("Verify [ Edit ] item in [ Action ] menu")
        return ui_lib.wait_for_element_visible(EditNetworksElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_actions_noauthorization(cls, expect_value, timeout=5, fail_if_false=True):
        """
             On the Edit Network Dialog, verify the user authorization is as expected
        """
        logger.debug("Verifying for 'user authorization' ...\nExpected message: '%s'" % expect_value)
        return FusionUIBase.verify_element_text("Actions", EditNetworksElements.ID_TEXT_ACTION_NO_AUTHORIZATION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_network_button_visible(cls, timeout=5, fail_if_false=False):
        """
             On the Network Page, verify the create network botton is visible
        """
        logger.debug("Verifying 'create network' button is visible ")
        return ui_lib.wait_for_element_visible(CreateNetworksElements.ID_BUTTON_CREATE_NETWORK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_should_exist_in_edit_page(cls, name, timeout=5, fail_if_false=True):
        """
             On the Edit Network Dialog, verify scope exists on the edit page
        """
        logger.debug("verify [ scope '%s' ] exist in scope edit page" % name)
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_TABLE_SCOPE_NAME % name, timeout, fail_if_false)


class _BaseEditScopeForNetworks(object):

    """
    This class holds all edit scope operation of networks
    It can work with C7000 & TBird
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_scope_button(cls, timeout=5, fail_if_false=True):
        """
             On the scope page, click the edit button
        """
        logger.debug("Click [ Edit ] button on enclosure scope page")
        if ui_lib.wait_for_element(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false) \
                and ui_lib.wait_for_element_visible(EditScopeElements.ID_HEADER_SCOPE, timeout=timeout, fail_if_false=fail_if_false)\
                and ui_lib.wait_for_element_notvisible(EditScopeElements.ID_TEXT_SCOPE_NOT_LOAD, timeout=timeout, fail_if_false=fail_if_false):
            ui_lib.find_element_and_move(EditScopeElements.ID_HEADER_SCOPE)
            ui_lib.wait_for_element_visible(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false)
            ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_EDIT, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_open(cls, timeout=5, fail_if_false=True):
        """
             Wait for the edit scope dialog to open
        """
        logger.debug("wait [ Edit ] dialog open")
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_DIALOG_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_close(cls, timeout=5, fail_if_false=True):
        """
            wait for the edit scope dialog to close
        """
        logger.debug("wait [ Edit ] dialog close")
        return ui_lib.wait_for_element_notvisible(EditScopeElements.ID_DIALOG_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_assign_scope_dialog_open(cls, timeout=5, fail_if_false=True):
        """
             wait for the assigned scope dialog to open
        """
        logger.debug("wait [ Assign to Scopes ] dialog open")
        return ui_lib.wait_for_element_visible(EditScopeElements.ID_DIALOG_ASSIGN, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_assign_scope_dialog_close(cls, timeout=5, fail_if_false=True):
        """
             wait for the assigned scope dialog to close
        """
        logger.debug("wait [ Assign to Scopes ] dialog close")
        return ui_lib.wait_for_element_notvisible(EditScopeElements.ID_DIALOG_ASSIGN, timeout, fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        """
            click OK button
        """
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        """
            click cancel button
        """
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def click_close_button(cls, timeout=5):
        """
            click close button
        """
        logger.debug("click [ Close ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CLOSE, timeout, fail_if_false=True)

    @classmethod
    def click_assign_button(cls, timeout=5):
        """
            click assign button
        """
        logger.debug("click [ Assign ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ASSIGN, timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, timeout=5):
        """
            click add button
        """
        logger.debug("click [ Add ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        """
            click add .bplus button
        """
        logger.debug("click [ Add+ ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_assign_button(cls, timeout=5):
        """
            click assign cancel  button
        """
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_BUTTON_CANCEL_ASSIGN, timeout, fail_if_false=True)

    @classmethod
    def input_scope_name(cls, name, wait_timeout=5):
        """
            input scope name
        """
        logger.debug("input scope name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditScopeElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_scope_name(cls, name, wait_timeout=5):
        """
            click scope name
        """
        logger.debug("click scope name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_scope_icon(cls, name, wait_timeout=5):
        """
            click remove scope icon
        """
        logger.debug("click to remove scope '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopeElements.ID_TABLE_REMOVE_SCOPE % name, wait_timeout, fail_if_false=True)


class EditScopeForNetworks(_BaseEditScopeForNetworks):
    """
    """
    pass


class C7000EditScopeForNetworks(_BaseEditScopeForNetworks):
    """
    """
    pass


class TBirdEditScopeForNetworks(_BaseEditScopeForNetworks):
    """
    """
    pass
