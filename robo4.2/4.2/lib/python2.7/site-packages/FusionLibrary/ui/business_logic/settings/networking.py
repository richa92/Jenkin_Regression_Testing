# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Settings Page
"""
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.settings.networking_elements import C7000_GeneralNetworingElements, \
    C7000_EditNetworkingElements
from RoboGalaxyLibrary.utilitylib import logging as logger


class VerifyNetworking(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_host_name_shown(cls, hostname, timeout=5, fail_if_false=True):
        logger.debug("wait for 'Host name' field shows up")
        return ui_lib.wait_for_element_visible(C7000_GeneralNetworingElements.ID_TEXT_HOST_NAME_VALUE % hostname, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_host_name(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify host name ,except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("host name", C7000_GeneralNetworingElements.ID_TEXT_HOST_NAME, except_value,
                                                timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_assignment(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv4 assignment, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("ipv4 assignment", C7000_GeneralNetworingElements.ID_TEXT_IPV4_ASSIGNMENT,
                                                except_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_address(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv4 address, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("ipv4 address", C7000_GeneralNetworingElements.ID_TEXT_IPV4_ADDRESS,
                                                except_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_subnet_mask_or_cidr(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv4 subnet mask or CIDR, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("ipv4 subnet mask or CIDR",
                                                C7000_GeneralNetworingElements.ID_TEXT_IPV4_SUBNET_MASK_OR_CIDR, except_value,
                                                timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_gateway_address(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv4 gateway address, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("ipv4 gateway address",
                                                C7000_GeneralNetworingElements.ID_TEXT_IPV4_GATEWAY_ADDRESS, except_value,
                                                timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv6_assignment(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv6 assignment, except value is [%s]" % except_value, )
        return FusionUIBase.verify_element_text("ipv6 assignment", C7000_GeneralNetworingElements.ID_TEXT_IPV6_ASSIGNMENT,
                                                except_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv6_address(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv6 address, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("ipv6", C7000_GeneralNetworingElements.ID_TEXT_IPV6_ADDRESS,
                                                except_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv6_subnet_mask_or_cidr(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv6 subnet mask or CIDR, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("ipv6 subnet mask or CIDR",
                                                C7000_GeneralNetworingElements.ID_TEXT_IPV6_SUBNET_MASK_OR_CIDR,
                                                except_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv6_gateway_address(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify ipv6 gateway address, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("ipv6 gateway address",
                                                C7000_GeneralNetworingElements.ID_TEXT_IPV6_GATEWAY_ADDRESS,
                                                except_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_preferred_dns_server(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify preferred dns server, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("preferred dns server",
                                                C7000_GeneralNetworingElements.ID_TEXT_PREFERRED_DNS_SERVER,
                                                except_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_alternate_dns_server(cls, except_value, timeout=5, fail_if_false=True):
        logger.debug("verify alternate dns server, except value is [%s]" % except_value)
        return FusionUIBase.verify_element_text("alternate dns server",
                                                C7000_GeneralNetworingElements.ID_TEXT_ALTERNATE_DNS_SERVER,
                                                except_value, timeout, fail_if_false)


class EditNetworking(object):

    @classmethod
    def click_networking(cls, timeout=5):
        logger.debug("click networking ")
        ui_lib.wait_for_element_and_click(C7000_GeneralNetworingElements.ID_NETWORKING, timeout, fail_if_false=True)

    @classmethod
    def select_action_edit(cls, timeout=5):
        logger.debug("select action edit")
        ui_lib.wait_for_element_and_click(C7000_GeneralNetworingElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_networking_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit networking dialog shown")
        ui_lib.wait_for_element_visible(C7000_EditNetworkingElements.ID_DIALOG_EDIT_NETWORKING, timeout, fail_if_false)

    @classmethod
    def select_edit_general_networking(cls, timeout=5):
        logger.debug("select general networking ")
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_DROPDOWN_NETWORKINGTYPE_SELECTOR, timeout,
                                          fail_if_false=True)
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_SELECT_GENERAL_PANEL, timeout, fail_if_false=True)

    @classmethod
    def select_edit_ipv4_networking(cls, timeout=5):
        logger.debug("select ipv4 networking ")
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_DROPDOWN_NETWORKINGTYPE_SELECTOR, timeout,
                                          fail_if_false=True)
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_SELECT_IPV4_PANEL, timeout, fail_if_false=True)

    @classmethod
    def select_edit_ipv6_networking(cls, timeout=5):
        logger.debug("select ipv6 networking ")
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_DROPDOWN_NETWORKINGTYPE_SELECTOR, timeout,
                                          fail_if_false=True)
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_SELECT_IPV6_PANEL, timeout, fail_if_false=True)

    @classmethod
    def select_edit_dns_networking(cls, timeout=5):
        logger.debug("select dns networking ")
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_DROPDOWN_NETWORKINGTYPE_SELECTOR, timeout,
                                          fail_if_false=True)
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_SELECT_DNS_PANEL, timeout, fail_if_false=True)

    @classmethod
    def input_appliance_host_name(cls, appliance_host_name, timeout=5):
        logger.debug("input appliance host name %s" % appliance_host_name)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_APPLIANCE_HOST_NAME, appliance_host_name,
                                               timeout, fail_if_false=True)

    @classmethod
    def choose_ipv4_address_assignment(cls, address_assignment_type, timeout=5):
        logger.debug("choose ipv4 address assignment type  '%s'" % address_assignment_type)
        if address_assignment_type.lower().strip() == 'manual':
            ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_RADIO_IPV4_ADDRESS_ASSIGNMENT_MANUAL, timeout,
                                              fail_if_false=True)
        elif address_assignment_type.lower().strip() == 'dhcp':
            ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_RADIO_IPV4_ADDRESS_ASSIGNMENT_DHCP, timeout,
                                              fail_if_false=True)
        else:
            ui_lib.fail_test(
                "unsupported address assignment type '%s', please specify 'Manual' or 'DHCP'" % address_assignment_type)

    @classmethod
    def input_ipv4_address(cls, ipv4_address, timeout=5):
        logger.debug("input ipv4 address %s" % ipv4_address)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_IPV4_ADDRESS, ipv4_address, timeout,
                                               fail_if_false=True)

    @classmethod
    def input_ipv4_subnet_mask_or_cidr(cls, mask_or_cidr, timeout=5):
        logger.debug("input ipv4 subnet mask or CIDR %s" % mask_or_cidr)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_IPV4_SUBNET_MASK_OR_CIDR, mask_or_cidr,
                                               timeout, fail_if_false=True)

    @classmethod
    def input_ipv4_gateway_address(cls, gateway_address, timeout=5):
        logger.debug("input ipv4 gateway address %s" % gateway_address)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_IPV4_GATEWAY_ADDRESS, gateway_address,
                                               timeout, fail_if_false=True)

    @classmethod
    def input_preferred_dns_server(cls, preferred_dns_server, timeout=5):
        logger.debug("input preferred dns server %s" % preferred_dns_server)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_PREFERRED_DNS_SERVER,
                                               preferred_dns_server, timeout, fail_if_false=True)

    @classmethod
    def input_alternate_dns_server(cls, alternate_dns_server, timeout=5):
        logger.debug("input alternate dns server %s" % alternate_dns_server)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_ALTERNATE_DNS_SERVER,
                                               alternate_dns_server, timeout, fail_if_false=True)

    @classmethod
    def choose_ipv6_address_assignment(cls, address_assignment_type, timeout=5):
        logger.debug("choose ipv6 address assignment type  '%s'" % address_assignment_type)
        if address_assignment_type.lower().strip() == 'unassign':
            ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_RADIO_IPV6_ADDRESS_ASSIGNMENT_UNASSIGN, timeout,
                                              fail_if_false=True)
        elif address_assignment_type.lower().strip() == 'dhcpv6':
            ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_RADIO_IPV6_ADDRESS_ASSIGNMENT_DHCPV6, timeout,
                                              fail_if_false=True)
        elif address_assignment_type.lower().strip() == 'manual':
            ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_RADIO_IPV6_ADDRESS_ASSIGNMENT_MANUAL, timeout,
                                              fail_if_false=True)
        else:
            ui_lib.fail_test(
                "unsupported address assignment type '%s', please specify 'Manual','Unassign' or 'DHCPv6'" % address_assignment_type)

    @classmethod
    def click_networking_edit_ok(cls, timeout=5):
        logger.debug("click networking_edit_ok ")
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_networking_edit_cancel(cls, timeout=5):
        logger.debug("click networking_edit_cancel ")
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def input_ipv6_address(cls, ipv6_address, timeout=5):
        logger.debug("input ipv6 address %s" % ipv6_address)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_IPV6_ADDRESS, ipv6_address, timeout,
                                               fail_if_false=True)

    @classmethod
    def input_ipv6_subnet_mask_or_cidr(cls, mask_or_cidr, timeout=5):
        logger.debug("input ipv6 subnet mask or CIDR %s" % mask_or_cidr)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_IPV6_SUBNET_MASK_OR_CIDR, mask_or_cidr,
                                               timeout, fail_if_false=True)

    @classmethod
    def input_ipv6_gateway_address(cls, gateway_address, timeout=5):
        logger.debug("input ipv6 gateway address %s" % gateway_address)
        ui_lib.wait_for_element_and_input_text(C7000_EditNetworkingElements.ID_INPUT_IPV6_GATEWAY_ADDRESS, gateway_address,
                                               timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_applying_network_settings_progress_bar_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait edit applying network settings progress bar shown")
        ui_lib.wait_for_element_visible(C7000_EditNetworkingElements.ID_PROGRESS_BAR_APPLYING_NETWORK_SETTINGS, timeout,
                                        fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_applying_network_settings_progress_bar_disappear(cls, timeout=1000, fail_if_false=True):
        logger.debug("wait edit applying network settings progress bar disappear")
        ui_lib.wait_for_element_notvisible(C7000_EditNetworkingElements.ID_PROGRESS_BAR_APPLYING_NETWORK_SETTINGS, timeout,
                                           fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_appliance_host_name(cls, timeout=5):
        logger.debug("get appliance host name")
        return FusionUIBase.get_text(C7000_EditNetworkingElements.ID_TEXT_HOST_NAME, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_appliance_ip_address(cls, timeout=5):
        logger.debug("get appliance ip address")
        return FusionUIBase.get_text(C7000_EditNetworkingElements.ID_TEXT_APPLIANCE_IP_ADDRESS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_settings(cls, timeout=5):
        logger.debug("click settings back to main page")
        ui_lib.wait_for_element_and_click(C7000_EditNetworkingElements.ID_TEXT_SETTINGS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_networking_panel_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("wait for networking panel disappear")
        ui_lib.wait_for_element_notvisible(C7000_EditNetworkingElements.ID_TEXT_SETTINGS, timeout, fail_if_false)
