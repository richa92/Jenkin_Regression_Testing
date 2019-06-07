from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase, ClassMethodType
from RoboGalaxyLibrary.utilitylib import logging as logger
import re
from FusionLibrary.ui.business_logic.settings.addressandidentifiers_elements import CreateIPPoolElements, EditIPPoolElements, VerifyIPPoolsElements, GeneralIPPoolElements, DeleteIPPoolElements, GetIPPoolsElements
from FusionLibrary.libs.utils import common
from datetime import datetime


class _BaseEditAddressesAndIdentifiers(object):

    e = GeneralIPPoolElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_edit_addresses_and_identifiers_dialog_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Edit Addresses and Identifiers dialog.")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_ADDRESSES_AND_IDENTIFIERS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_edit_addresses_and_identifiers_form_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Edit Addresses and identifiers form to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_ADDRESSES_AND_IDENTIFIERS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_addresses_and_identifiers_edit_link(cls):
        logger.debug("Clicking Address and identifiers Edit Link")
        ui_lib.move_to_element_and_click(cls.e.ID_LINK_ADDRESSES_AND_IDENTIFIER, cls.e.ID_LINK_EDIT_ADDRESSES_AND_IDENTIFIERS)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_edit_dialog_ipv4subnet_table_nodata_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for 'No subnets defined' message to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_IPV4_SUBNET_ADDRESS_RANGE_NO_DATA, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_addresses_and_identifiers_dialog_ok(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Edit Address and identifiers form OK button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_ADDRESSES_AND_IDENTIFIERS_OK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_changes_lost_warning_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Warning dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_CHANGES_LOST_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_addresses_and_identifiers_form_proceed(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking 'Yes, Proceed'")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_ADDRESSIDENTIFIERS_PROCEED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_addresses_and_identifiers_dialog_cancel(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Edit Address and identifiers form CANCEL button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_ADDRESSES_AND_IDENTIFIERS_CANCEL, timeout, fail_if_false)
        if cls.wait_for_changes_lost_warning_dialog(fail_if_false=False):
            cls.click_edit_addresses_and_identifiers_form_proceed()

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_notvisible_in_edit_addressidentifiers_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Wait for 'update' to yield result")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_HPSTATUS_UPDATE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_error_status_visible_in_edit_address_form_footer(cls, timeout=5, fail_if_false=True):
        logger.debug("check if Error status is visible")
        return ui_lib.wait_for_element_visible(cls.e.ID_IPV4_EDIT_ERROR_STATUS, timeout, fail_if_false)


class GeneralAddressesAndIdentifiers(_BaseEditAddressesAndIdentifiers):

    e = GeneralIPPoolElements

    @classmethod
    def get_idpart(cls, idlocator):
        '''
        Function to get the id part in the locator passed in format id=xxx
        '''
        logger.debug("getting ID part of locator '{}'".format(idlocator))
        search_result = re.search(r"^id=(.*)", idlocator.replace(' ', ''))
        if search_result is not None:
            idlocator = search_result.group(1)
        return idlocator

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_settings_link(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Settings Link in address and identifiers page")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_ADDRESSES_AND_IDENTIFIERS_PAGE_SETTINGS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_addresses_and_identifiers_page_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Addresses and identifiers page to be visible")
        return ui_lib.wait_for_element_visible(cls.e.ID_HEADER_ADDRESSES_AND_IDENTIFIERS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_addresses_and_identifiers_link_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Addresses and identifiers Link")
        return ui_lib.wait_for_element_visible(cls.e.ID_LINK_ADDRESSES_AND_IDENTIFIER, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_addresses_and_identifiers_link(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Address and identifiers Link")
        ui_lib.wait_for_element_and_click(cls.e.ID_LINK_ADDRESSES_AND_IDENTIFIER, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_addresses_and_identifiers_page_actions_menu(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Addresses And Identifiers Page Actions Menu")
        return ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_ACTION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_addresses_and_identifiers_page_actions_menu(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Address and identifiers Actions Menu dropdown")
        return ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ACTION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_actions_menu_option(cls, option_text, timeout=5, fail_if_false=True):
        logger.debug("Waiting for actions menu {} option".format(option_text))
        return ui_lib.wait_for_element("link=%s" % option_text, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_actions_edit(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Edit from Address and identifiers Actions dropdown")
        ui_lib.wait_for_element_and_click(cls.e.LINK_EDIT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addresses_identifiers_error_status_message_summary(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Edit Addresses And Identifiers dialog error status message summary")
        return ui_lib.get_text(cls.e.ID_SUBNET_ERROR_MESSAGE_SUMMARY, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addresses_identifiers_error_status_message_details(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Edit Addresses And Identifiers dialog error status message Details")
        return ui_lib.get_text(cls.e.ID_SUBNET_ERROR_MESSAGE_DETAILS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_addressrange_checkbox_disabled(cls, subnetid, rangename, timeout=5, fail_if_false=True):
        return ui_lib.wait_for_element_visible(cls.e.ID_CHECKBOX_EDIT_ADDRESSESIDENTIFIERS_RANGE_DISABLED % (subnetid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_ipv4_subnet_addressrange_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        tableid = cls.get_idpart(tableid)
        logger.debug("Witing for address range table")
        return ui_lib.wait_for_element_visible(cls.e.ID_TABLE_ADDRESS_RANGE_OF_SUBNET.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def expand_addressrange_collapser(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        tableid = cls.get_idpart(tableid)
        if cls.wait_for_ipv4_subnet_addressrange_table(tableid, subnetid, fail_if_false=False):
            logger.debug("Collapser for subnet [{}] already expanded".format(subnetid))
            return True
        logger.debug("Expanding Address Range collapser of subnet [{}]".format(subnetid))
        return ui_lib.wait_for_element_and_click(cls.e.ID_RANGE_COLLAPSER.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_dialog_error_summary_details(cls):
        error_status_summary = ''
        error_status_details = ''
        if cls.wait_for_update_notvisible_in_edit_addressidentifiers_dialog(timeout=180, fail_if_false=False) is False:
            msg = "Failed to wait for Edit Addresses And Identifiers dialog 'Update' result to occur!"
            logger.warn(msg)
            cls.click_edit_addresses_and_identifiers_dialog_cancel()
            raise AssertionError(msg)
        if cls.wait_for_error_status_visible_in_edit_address_form_footer(fail_if_false=False):
            error_status_summary = cls.get_addresses_identifiers_error_status_message_summary()
            error_status_details = cls.get_addresses_identifiers_error_status_message_details()
            return error_status_summary + '.' + error_status_details
        return None

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def enable_disable_addressrange(cls, subnetid, addressrange_list):
        '''
        Function to Enable/Disable address ranges of a given subnet.

        Arguments:
            subnetid            --
            addressrange_list   --
                    <addressrange>(optional) --    Ranges to add to the subnet
                                        name*                         --   Address range name
                                        rangestart(optional)          --   range start IP
                                        rangeend(optional)            --   range end IP
                                        enable(optional)              --   Enable/Disable range (True/False)
        Return Value:
            Boolean True on success else Raises AssertionError exception

        '''
        error_msg_list = []
        edit_addressesidentifiers_dialog_subnettable_id = cls.e.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG
        VerifySubnetsAndAddressRange.verify_subnet_exists_in_table(edit_addressesidentifiers_dialog_subnettable_id, subnetid, fail_if_false=True)

        cls.expand_addressrange_collapser(edit_addressesidentifiers_dialog_subnettable_id, subnetid)
        cls.wait_for_ipv4_subnet_addressrange_table(edit_addressesidentifiers_dialog_subnettable_id, subnetid)

        for addressrange in addressrange_list:
            rangename = getattr(addressrange, "newname", addressrange.name)
            if VerifySubnetsAndAddressRange.verify_range_exists(edit_addressesidentifiers_dialog_subnettable_id, rangename, fail_if_false=False) is False:
                logger.warn("Range '{}' is not visible for subnet [{}]!".format(rangename, subnetid))
                error_msg_list.append("Range '{}' is not visible for subnet [{}]!".format(rangename, subnetid))
                continue

            if addressrange.has_property("enable"):
                if addressrange.enable.lower() == "true":
                    logger.debug("Enabling address range : {}".format(rangename))
                    cls.select_addressrange_checkbox(subnetid, rangename)
                else:
                    logger.debug("Disabling address range : {}".format(rangename))
                    cls.unselect_addressrange_checkbox(subnetid, rangename)
            else:
                logger.warn("'enable' parameter not specified in input")
        if error_msg_list:
            raise AssertionError(error_msg_list)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def select_addressrange_checkbox(cls, subnetid, rangename, timeout=5, fail_if_false=True):
        logger.debug("Selecting checkbox for range [{}]".format(rangename))
        ui_lib.scroll_into_view(cls.e.ID_CHECKBOX_EDIT_ADDRESSESIDENTIFIERS_ADDRESS_RANGE % (subnetid, rangename))
        ui_lib.wait_for_checkbox_and_select(cls.e.ID_CHECKBOX_EDIT_ADDRESSESIDENTIFIERS_ADDRESS_RANGE % (subnetid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def unselect_addressrange_checkbox(cls, subnetid, rangename, timeout=5, fail_if_false=True):
        logger.debug("De-Selecting checkbox for range [{}]".format(rangename))
        ui_lib.scroll_into_view(cls.e.ID_CHECKBOX_EDIT_ADDRESSESIDENTIFIERS_ADDRESS_RANGE % (subnetid, rangename))
        ui_lib.wait_for_checkbox_and_unselect(cls.e.ID_CHECKBOX_EDIT_ADDRESSESIDENTIFIERS_ADDRESS_RANGE % (subnetid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def collapse_addressrange_collapser(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        tableid = cls.get_idpart(tableid)
        logger.debug("Collapsing Address Range collapser of subnet [{}]".format(subnetid))
        return ui_lib.wait_for_element_and_click(cls.e.ID_EXPANDED_RANGE_COLLAPSER.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def collapse_addressrange_collapser_addressesidentifiers_page(cls, subnetid, timeout=5, fail_if_false=True):
        return cls.collapse_addressrange_collapser(cls.e.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def expand_all_collapsibles(cls, locator, timeout=5):
        logger.debug("Expanding all Collapsible in dialog")
        search_result = re.search(r"^xpath=(.*)", locator)
        if search_result is not None:
            locator = search_result.group(1)

        s2l = ui_lib.get_s2l()
        clickcount = 0
        collapsercount = 0
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            try:
                ui_lib.wait_for_element_visible(locator, fail_if_false=False)
                collapsibleelements = s2l._current_browser().find_elements_by_xpath(locator)
                collapsercount += len(collapsibleelements)
                for element in collapsibleelements:
                    element.click()
                    clickcount += 1
                if clickcount == collapsercount and clickcount > 0:
                    return True
            except Exception as Ex:
                pass
        return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def expand_all_collapsibles_subnet_deletewarning_dialog(cls, timeout=5):
        logger.debug("Expanding All the Associated Objects collapsibles displayed in the Subnet delete warning, to display the object names")
        return cls.expand_all_collapsibles(cls.e.ID_COLLAPSIBLE_DELETE_SUBNET_WARNING, timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def expand_all_collapsibles_range_deletewarning_dialog(cls, timeout=5):
        logger.debug("Expanding All the Associated Objects collapsibles displayed in the Range delete warning, to display the object names")
        return cls.expand_all_collapsibles(cls.e.ID_COLLAPSIBLE_DELETE_ADDRESS_RANGE_WARNING, timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_associated_object_visible_count(cls, locator):
        logger.debug("Getting associated object visible count")
        search_result = re.search(r"^xpath=(.*)", locator)
        if search_result is not None:
            locator = search_result.group(1)
        return len(ui_lib.get_s2l()._current_browser().find_elements_by_xpath(locator))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_associatedobject_visible_count_subnetdelete_warning(cls, associated_obj):
        return cls.get_associated_object_visible_count(cls.e.ID_DELETE_SUBNET_WARNING_ASSOCIATED_OBJECT % associated_obj.lower())

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_associatedobject_visible_count_rangedelete_warning(cls, associated_obj):
        return cls.get_associated_object_visible_count(cls.e.ID_DELETE_RANGE_WARNING_ASSOCIATED_OBJECT % associated_obj.lower())

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def expand_addressrange_collapser_edit_dialog(cls, subnetid, timeout=5, fail_if_false=True):
        return cls.expand_addressrange_collapser(cls.e.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def expand_addressrange_collapser_addressesidentifiers_page(cls, subnetid, timeout=5, fail_if_false=True):
        return cls.expand_addressrange_collapser(cls.e.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_ipv4subnet_addressrange_table_edit_dialog(cls, subnetid, timeout=5, fail_if_false=True):
        return cls.wait_for_ipv4_subnet_addressrange_table(cls.e.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_ipv4subnet_table_addressesidentifiers_page(cls, subnetid, timeout=5, fail_if_false=True):
        return cls.wait_for_ipv4_subnet_addressrange_table(cls.e.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def refresh_settings_page_and_wait_for_ipv4_addresses_count(cls, timeout=5):
        logger.debug("Refreshing page and waiting for IPV4 addresses Count")
        return ui_lib.refresh_browser(cls.e.ID_IPV4_ADDRESSES_TOTAL_COUNT, timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_total_ipv4_addresses_count(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting Total IPV4 addresses count")
        return ui_lib.get_text(cls.e.ID_IPV4_ADDRESSES_TOTAL_COUNT, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_ipv4_subnet_addressranges_table_headers(cls, timeout=5, fail_if_false=True):
        return ui_lib.get_text(cls.e.ID_TABLE_IPV4_SUBNET_HEADERS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_ip4_subnet_addressranges_table_data(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting IPV4 Subnet and Addresses Table Data")
        return ui_lib.get_text(cls.e.ID_TABLE_IPV4_SUBNET_DATA, timeout, fail_if_false)


class CreateSubnetsAndAddressRange(object):

    e = CreateIPPoolElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_add_ipv4_subnet_and_range_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Add IPV4 subnet and address range Button")
        return ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_ADD_IPV4_SUBNET_AND_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_add_ipv4_subnet_and_range_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add IPV4 subnet and address range button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_IPV4_SUBNET_AND_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_add_subnet_addressrange_dialog_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Edit subnet and adress range dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_IPV4_SUBNET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_add_subnet_addressrange_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Add subnet and address range dialog to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_IPV4_SUBNET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_subnetid(cls, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to subnetid textbox".format(subnetid))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IPV4_SUBNETID, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_subnetmask(cls, subnetmask, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to subnet mask textbox".format(subnetmask))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IPV4_SUBNET_MASK, subnetmask, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_gateway(cls, gateway, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to gateway textbox".format(gateway))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IPV4_GATEWAY, gateway, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_domain(cls, domain_name, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to domain name textbox".format(domain_name))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IPV4_DOMAIN_NAME, domain_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_dns1(cls, dns1, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to dns1 textbox".format(dns1))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IPV4_DNS1, dns1, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_dns2(cls, dns2, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to dns2 textbox".format(dns2))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IPV4_DNS2, dns2, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_dns3(cls, dns3, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to dns3 textbox".format(dns3))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_IPV4_DNS3, dns3, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_subnet_add_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add IPV4 subnet and address range ADD button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_SUBNET_ADD, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_subnet_add_plus_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add IPV4 subnet and address range ADD+ button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_SUBNET_ADD_PLUS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_add_subnet_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add IPV4 subnet and address range CANCEL button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_SUBNET_CANCEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_add_addressrange_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Add address range Button")
        return ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_ADD_ADDRESS_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_add_subnet_add_addressrange_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add Address Range button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_ADD_ADDRESS_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_add_range_dialog_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Add range dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_ADD_IPV4_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_add_range_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for add range dialog to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_ADD_IPV4_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_rangename(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to range name textbox".format(rangename))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_RANGE_NAME, rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_range_startip(cls, startip, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to First ip textbox".format(startip))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_RANGE_STARTIP, startip, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def input_range_endip(cls, endip, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to Last ip textbox".format(endip))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_ADD_RANGE_ENDIP, endip, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_range_add_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add Address range ADD button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_RANGE_ADD, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_range_add_plus_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add Address range ADD+ button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_RANGE_ADD_PLUS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_range_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add Address range CANCEL button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_RANGE_CANCEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_add_range_warning_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Add range warning dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_ADD_RANGE_DIALOG_NOTIFICATION, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_add_range_warning_text(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting warning text")
        return ui_lib.get_text(cls.e.ID_TEXT_ADD_RANGE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_add_range_warning_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Add Address range Warning CLOSE button")
        ui_lib.wait_for_element_and_click(cls.e.ID_ADD_RANGE_WARNING_CLOSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_all_errors_on_addsubnet_dialog(cls):
        return FusionUIBase.get_all_error_message_on_form(GeneralIPPoolElements.ID_DIALOG_ADD_IPV4_SUBNET)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_all_errors_on_addrange_dialog(cls):
        return FusionUIBase.get_all_error_message_on_form(GeneralIPPoolElements.ID_DIALOG_ADD_RANGE)


class EditSubnetsAndAddressRange(object):
    e = EditIPPoolElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_subnet_add_range_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Wait for Update subnet Add Range Button")
        return ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_UPDATE_SUBNET_ADD_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_update_subnet_add_range_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Update Subnet Add Address range button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_UPDATE_SUBNET_ADD_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_subnet_icon(cls, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Clicking Edit icon of subnet [{}]".format(subnetid))
        ui_lib.wait_for_element_and_click(cls.e.ID_ICON_EDIT_SUBNET % subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_subnet_dialog_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Wait for Edit subnet dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_SUBNET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_subnet_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Edit subnet dialog to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_SUBNET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_subnetid(cls, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to subnetid textbox".format(subnetid))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_SUBNET_ID, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_subnetmask(cls, subnetmask, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to subnet mask textbox".format(subnetmask))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_SUBNET_MASK, subnetmask, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_gateway(cls, gateway, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to gateway textbox".format(gateway))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_GATEWAY, gateway, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_domain(cls, domain_name, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to domain name textbox".format(domain_name))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_DOMAIN_NAME, domain_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_dns1(cls, dns1, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to dns1 textbox".format(dns1))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_DNS1, dns1, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_dns2(cls, dns2, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to dns2 textbox".format(dns2))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_DNS2, dns2, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_dns3(cls, dns3, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to dns3 textbox".format(dns3))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_DNS3, dns3, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_subnet_update_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Update IPV4 subnet and address range UPDATE button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_UPDATE_SUBNET, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_update_subnet_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Update IPV4 subnet and address range CANCEL button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_SUBNET_CANCEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_subnet_edit_range_icon(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Waiting for uodate subnet Edit range icon")
        return ui_lib.wait_for_element_visible(cls.e.ID_ICON_UPDATE_SUBNET_EDIT_RANGE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_update_subnet_edit_range_icon(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Clicking Edit icon of range [{}]".format(rangename))
        ui_lib.wait_for_element_and_click(cls.e.ID_ICON_UPDATE_SUBNET_EDIT_RANGE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_range_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Update range dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_UPDATE_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_range_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for update range dialog to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_UPDATE_RANGE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_range_name(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to range name textbox".format(rangename))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_RANGE_NAME, rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_input_range_startip(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Range start IP input")
        return ui_lib.wait_for_element_visible(cls.e.ID_INPUT_UPDATE_RANGE_STARTIP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_range_startip(cls, startip, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to range start IP textbox".format(startip))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_RANGE_STARTIP, startip, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def update_range_endip(cls, endip, timeout=5, fail_if_false=True):
        logger.debug("Providing input [{}] to range End IP textbox".format(endip))
        ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_UPDATE_RANGE_ENDIP, endip, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_update_range_ok_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking update Range OK button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_UPDATE_RANGE_OK, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_update_range_cancel_button(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking update Range CANCEL button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_UPDATE_RANGE_CANCEL, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_all_errors_on_editsubnet_dialog(cls):
        return FusionUIBase.get_all_error_message_on_form(GeneralIPPoolElements.ID_DIALOG_UPDATE_IPV4_SUBNET)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_all_errors_on_editrange_dialog(cls):
        return FusionUIBase.get_all_error_message_on_form(GeneralIPPoolElements.ID_DIALOG_EDIT_ADDRESS_RANGE)


class DeleteSubnetsAndAddressRange(object):

    e = DeleteIPPoolElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_delete_warning_dialog_close(cls, timeout=5, fail_if_false=True):
        logger.debug("Clicking Delete warning Dialog close button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_DELETE_WARNING_CLOSE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_update_subnet_delete_range_button(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Wauting fro update subnet delete range button")
        return ui_lib.wait_for_element_visible(cls.e.ID_UPDATE_SUBNET_RANGE_DELETE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_update_subnet_delete_range_button(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Clicking Delete range button")
        ui_lib.wait_for_element_and_click(cls.e.ID_UPDATE_SUBNET_RANGE_DELETE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_range_delete_warning_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for delete range warning dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_DELETE_RANGE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_range_delete_warning_dialog_message(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting range delete warning dialog text")
        return ui_lib.get_text(cls.e.ID_TEXT_DELETE_RANGE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_range_delete_warning_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for delete range warning dialog to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_DELETE_RANGE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_delete_subnet_button(cls, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Delete subnet button for : {}".format(subnetid))
        return ui_lib.wait_for_element_visible(cls.e.ID_SUBNET_DELETE % subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_delete_subnet_button(cls, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Clicking Delete for subnet with id - [{}]".format(subnetid))
        ui_lib.wait_for_element_and_click(cls.e.ID_SUBNET_DELETE % subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_subnet_delete_warning_dialog(cls, timeout=5, fail_if_false=True):
        logger.debug("Wauting for delete subnet warning dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_SUBNET_DELETE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_subnet_delete_warning_dialog_message(cls, timeout=5, fail_if_false=True):
        logger.debug("Getting delete subnet dialog warning text")
        return ui_lib.get_text(cls.e.ID_TEXT_SUBNET_DELETE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_subnet_delete_warning_dialog_disappear(cls, timeout=5, fail_if_false=True):
        logger.debug("Waiting for Subnet delete warning dialog to disappear")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_SUBNET_DELETE_WARNING, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_edit_dialog_delete_range_button(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Waiting for delete range icon in Edit addresses and identifiers dialog")
        return ui_lib.wait_for_element_visible(cls.e.ID_BUTTON_EDIT_ADDRESSESIDENTIFIERS_DELETE_RANGE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_edit_dialog_delete_range_button(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Clicking Delete range button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_ADDRESSESIDENTIFIERS_DELETE_RANGE % rangename, timeout, fail_if_false)


class VerifySubnetsAndAddressRange(object):

    e = VerifyIPPoolsElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_exists_in_add_subnet_table(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Checking if range '{}' exists in Add subnet table".format(rangename))
        return ui_lib.wait_for_element_visible(GeneralIPPoolElements.ID_TABLE_ADD_SUBNET_ADD_RANGE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_exists(cls, tableid, rangename, timeout=5, fail_if_false=True):
        logger.debug("Checking if range '{}' exists".format(rangename))
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.wait_for_element_visible(cls.e.ID_GENERIC_ADDRESSRANGE_IN_TABLE.format(tableid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_subnet_exists_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Checking if subnet '{}' exists".format(subnetid))
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.wait_for_element_visible(cls.e.ID_GENERIC_SUBNET_IN_TABLE.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_subnet_exists_in_editaddressidentifiers_table(cls, subnetid, timeout=5, fail_if_false=True):
        return cls.verify_subnet_exists_in_table(GeneralIPPoolElements.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_subnet_exists_in_addressidentifierspage_table(cls, subnetid, timeout=5, fail_if_false=True):
        return cls.verify_subnet_exists_in_table(GeneralIPPoolElements.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_unavailable_for_operation_on_addition(cls, subnetid, addressrange_list):
        '''
        Function to verify that the range is unavailable for operation by default on addition

        Parameters:
            Subnetid                -- subnet id the range belongs to
            addressrange_list       -- list of address range objects to check

        input example :
            <addressrange name = "Test101" rangestart="1.1.1.10" rangeend="1.1.1.20" />

        return Value:
            boolean True on success , else raises and AssertionError
        '''
        error_msg_list = []
        tableid = GeneralAddressesAndIdentifiers.get_idpart(GeneralIPPoolElements.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG)

        GeneralAddressesAndIdentifiers.expand_addressrange_collapser(tableid, subnetid)
        GeneralAddressesAndIdentifiers.wait_for_ipv4_subnet_addressrange_table(tableid, subnetid)
        for addressrange in addressrange_list:
            if cls.verify_range_exists(tableid, addressrange.name, fail_if_false=False) is False:
                logger.warn("Range '{}' is not visible for subnet [{}]!".format(addressrange.name, subnetid))
                error_msg_list.append("Range '{}' is not visible for subnet [{}]!".format(addressrange.name, subnetid))
                continue
            if GeneralAddressesAndIdentifiers.wait_for_addressrange_checkbox_disabled(subnetid, addressrange.name, fail_if_false=False) is True:
                logger.debug("Range {} state checkbox is unavailable for operation by default".format(addressrange.name))
            else:
                logger.warn("Range {} state checkbox should not be available for operation by default, But is !!".format(addressrange.name))
                error_msg_list.append("Range {} state checkbox should not be available for operation by default, But is !!".format(addressrange.name))
        if error_msg_list:
            raise AssertionError(error_msg_list)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_update_subnet_and_addressrange_table_is_not_empty(cls, timeout=5, fail_if_false=True):
        logger.debug("Check if subnet table is not Empty")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_EDIT_SUBNET_ADDRESS_RANGE_NODATA, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_exists_in_edit_subnet_table(cls, rangename, timeout=5, fail_if_false=True):
        logger.debug("Checking if range '{}' exists in edit subnet table".format(rangename))
        return ui_lib.wait_for_element_visible(GeneralIPPoolElements.ID_TABLE_EDIT_SUBNET_EDIT_RANGE % rangename, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_addressesidentifiers_ipv4_subnet_table_is_not_empty(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking if the the subnet table in Edit form is not empty")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_TABLE_EDIT_ADDRESSIDENTIFIERS_SUBNET_NODATA, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_subnetid_is_not_editable(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking if subnet ID is editable")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_INPUT_SUBNET_ID_EDITABLE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_subnet_mask_is_not_editable(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking if subnet mask is editable")
        return ui_lib.wait_for_element_notvisible(cls.e.ID_INPUT_SUBNET_MASK_EDITABLE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_subnet_form_visible_for_subnetid(cls, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Verify if Edit subnet form is visible for subnet : {}".format(subnetid))
        return ui_lib.wait_for_element_visible(cls.e.ID_TEXT_UPDATE_SUBNET_HEADER % subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_checkbox_selected(cls, rangename):
        logger.debug("Checking if range Checkbox is selected")
        return ui_lib.is_checkbox_selected(cls.e.ID_CHECKBOX_ADDRESSRANGE % rangename)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_associated_networks_unset(cls, subnetid, timeout=5, fail_if_false=True):
        logger.debug("checking if associated Newtork is unset")
        return ui_lib.wait_for_element_visible(cls.e.ID_UNSET_ASSOCIATED_NETWORKS_IN_ADDRESSIDENTIFIERS_PAGE % subnetid, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_associated_networks_visible_in_addressesidentifiers_page_table(cls, subnetid, associated_network, timeout=5, fail_if_false=True):
        logger.debug("Checking for the associated network '{}' for subnet '{}'".format(associated_network, subnetid))
        return ui_lib.wait_for_element_visible(cls.e.ID_ASSOCIATED_NETWORKS_IN_ADDRESSIDENTIFIERS_PAGE % (subnetid, associated_network.lower()), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_subnet_delete_associated_object_visible(cls, associated_obj, timeout=5, fail_if_false=True):
        logger.debug("Checking if '{}' is visble in subnet delete warning".format(associated_obj))
        return ui_lib.wait_for_element_visible(cls.e.ID_SUBNET_DELETE_ASSOCIATED_OBJECT % associated_obj.lower(), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_delete_associated_object_visible(cls, associated_obj, timeout=5, fail_if_false=True):
        logger.debug("Checking if '{}' is visble in range delete warning".format(associated_obj))
        return ui_lib.wait_for_element_visible(cls.e.ID_RANGE_DELETE_ASSOCIATED_OBJECT % associated_obj.lower(), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_delete(cls, tableid, subnetid, addressrange_list):
        '''
        Function to Verify that the specified ranges have been deleted for the given subnet from the given table
        raises an AssertionError exception if the ranges are visible
        '''
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        error_msg_list = []
        addressrangename_list = []
        for range in addressrange_list:
            addressrangename_list += range.names.split(',')

        for addressrange in addressrangename_list:
            logger.info("-- Verifying Range {} is deleted from subnet [{}]".format(addressrange, subnetid))
            if cls.verify_range_exists(tableid, addressrange, fail_if_false=False):
                logger.warn("Range '{}' is still visible for subnet [{}]!".format(addressrange, subnetid))
                error_msg_list.append("Range '{}' is still visible for subnet [{}]!".format(addressrange, subnetid))
            else:
                logger.debug("{} Range deleted successfully.".format(addressrange))

        if error_msg_list:
            raise AssertionError(error_msg_list)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_subnet_attributes(cls, tableid, subnet_obj, timeout=5, fail_if_false=True):
        '''
        Function to verify the Subnet attributes

        Arguments:
            tableid                -- ID of the table the range is present in
            subnetobj               -- List of Subnet objects

        Return Value :
            returns a Boolean True on success else raises an AssertionError exception

        Input Example:

            <ipv4subnet subnetid = "4.4.4.0" subnetmask="255.255.255.0" gateway = "4.4.4.1" domain="hpe.com" dns1="2.2.2.2" dns2="4.4.4.3" dns3 = "1.4.4.4">
            </ipv4subnet>
            <ipv4subnet subnetid = "1.1.1.0" subnetmask="255.55.255.0" gateway = "" domain="" dns3 = "" hellfire="yes">  Only for Hellfire Data
            </ipv4subnet>

            <ipv4subnet subnetid = "1.1.160.0" subnetmask="255.255.255.0" gateway = "1.1.160.1" domain="hp.com"  dns1="1.1.160.5" dns2="1.1.160.3" dns3 = "1.1.161.120">
                <addressrange name = "test1" rangestart="1.1.160.30" rangeend="1.1.160.40" enable="False" />
                <addressrange name = "test2" rangestart="1.1.160.25" rangeend="1.1.160.29" enable="True" />
            </ipv4subnet>

            <ipv4subnet subnetid = "1.1.160.0" subnetmask="255.255.255.0" gateway = "" domain=""  dns1="1.1.160.5" dns2="1.1.160.3" dns3 = "1.1.161.120" hellfire="yes" > Only for Hellfire Data
                <addressrange name = "test1" rangestart="1.1.160.30" rangeend="1.1.160.40" enable="False" />
                <addressrange name = "test2" rangestart="1.1.160.25" rangeend="1.1.160.29" enable="True" />
            </ipv4subnet>
        '''
        error_msg_list = []
        for subnet in subnet_obj:
            addressrange_list = []
            deleted_addressrange_list = []
            if subnet.has_property("newsubnetid"):
                subnetid = subnet.newsubnetid
            else:
                subnetid = subnet.subnetid
            if cls.verify_subnet_exists_in_table(tableid, subnetid, fail_if_false=False) is False:
                logger.debug("Subnet [{}] does not exist".format(subnetid))
                error_msg_list.append("Subnet [{}] does not exist".format(subnetid))
                continue

            logger.info("-- Verifying Subnet [{}] attributes".format(subnetid))
            logger.debug("Subnet ID  : {}".format(subnetid))
            if subnet.has_property("subnetmask"):
                subnetmask = GetSubnetsAndAddressRangeAttributes.get_subnetmask_in_table(tableid, subnetid)
                if not subnetmask.lower() == subnet.subnetmask.lower():
                    logger.debug("Subnet Mask is not set to [{}] but is [{}]".format(subnet.subnetmask, subnetmask))
                    error_msg_list.append("Subnet Mask is not set to [{}] but is [{}] for subnet {}".format(subnet.subnetmask, subnetmask, subnetid))
            if subnet.has_property("gateway"):
                if subnet.has_property("hellfire"):
                    if (subnet.gateway == ""):
                        gateway = GetSubnetsAndAddressRangeAttributes.get_gateway_unset_in_table(tableid, subnetid)
                        logger.debug("Gateway is --{}--".format(gateway))
                    else:
                        gateway = GetSubnetsAndAddressRangeAttributes.get_gateway_in_table(tableid, subnetid)
                        logger.debug("Gateway is --{}--".format(gateway))
                else:
                    gateway = GetSubnetsAndAddressRangeAttributes.get_gateway_in_table(tableid, subnetid)
                    if not gateway.lower() == subnet.gateway.lower():
                        logger.debug("Gateway  is not set to [{}] but is [{}]".format(subnet.gateway, gateway))
                        error_msg_list.append("Gateway  is not set to [{}] but is [{}] for subnet {}".format(subnet.gateway, gateway, subnetid))
            if subnet.has_property("domain"):
                if subnet.has_property("hellfire"):
                    logger.debug("Domain name is --{}--".format(subnet.domain))
                    if (subnet.domain == ""):
                        domain_name = GetSubnetsAndAddressRangeAttributes.get_domainname_unset_in_table(tableid, subnetid)
                        logger.debug("Domain name after is --{}--".format(domain_name))
                    else:
                        domain_name = GetSubnetsAndAddressRangeAttributes.get_domainname_in_table(tableid, subnetid)
                else:
                    domain_name = GetSubnetsAndAddressRangeAttributes.get_domainname_in_table(tableid, subnetid)
                    if not domain_name.lower() == subnet.domain.lower():
                        logger.debug("Domain Name is not set to [{}] but is [{}]".format(subnet.domain, domain_name))
                        error_msg_list.append("Domain Name is not set to [{}] but is [{}] for subnet {}".format(subnet.domain, domain_name, subnetid))
            if cls.verify_dns_unset_in_table(tableid, subnetid, timeout=4, fail_if_false=False):
                dns = None
            else:
                dns = GetSubnetsAndAddressRangeAttributes.get_dns_in_table(tableid, subnetid)

            if subnet.has_property("dns1"):
                if not subnet.dns1.lower() in dns.lower():
                    logger.debug("DNS1 is not set to [{}] but is [{}]".format(subnet.dns1, dns))
                    error_msg_list.append("DNS1 is not set to [{}] but is [{}] for subnet {}".format(subnet.dns1, dns, subnetid))
            if subnet.has_property("dns2"):
                if not subnet.dns2.lower() in dns.lower():
                    logger.debug("DNS2 is not set to [{}] but is [{}]".format(subnet.dns2, dns))
                    error_msg_list.append("DNS2 is not set to [{}] but is [{}] for subnet {}".format(subnet.dns2, dns, subnetid))
            if subnet.has_property("dns3"):
                if not subnet.dns3.lower() in dns.lower():
                    logger.debug("DNS3 is not set to [{}] but is [{}]".format(subnet.dns3, dns))
                    error_msg_list.append("DNS3 is not set to [{}] but is [{}] for subnet {}".format(subnet.dns3, dns, subnetid))

            addressrange_list += getattr(subnet, "addressrange", [])
            addressrange_list += getattr(subnet, "add_addressrange", [])
            addressrange_list += getattr(subnet, "edit_addressrange", [])
            delete_addressrange_list = getattr(subnet, "remove_addressrange", [])

            GeneralAddressesAndIdentifiers.expand_addressrange_collapser(tableid, subnetid)
            GeneralAddressesAndIdentifiers.wait_for_ipv4_subnet_addressrange_table(tableid, subnetid)

            if addressrange_list:
                try:
                    cls.verify_ipv4_addressrange_attributes(tableid, subnetid, addressrange_list)
                except AssertionError as Ex:
                    logger.warn("Exception during Address Range attribute verification for subnet [{}] : \n{}".format(subnetid, Ex.message))
                    error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]
            if delete_addressrange_list:
                try:
                    cls.verify_range_delete(tableid, subnetid, delete_addressrange_list)
                except AssertionError as Ex:
                    logger.warn("Exception during Deleted Address Range verification for subnet [{}] : \n{}".format(subnetid, Ex.message))
                    error_msg_list = error_msg_list + Ex.message if isinstance(Ex.message, list) else error_msg_list + [Ex.message, ]

        if error_msg_list:
            raise AssertionError(error_msg_list)
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_addressrange_attributes(cls, tableid, subnetid, addressrange_list):
        '''
        Function to verify the Address range attributes

        Arguments:
            tableid                -- ID of the table the range is present in
            subnetid               -- Subnet ID of the subnet the range is part of
            addressrange_list      -- List of addressrange objects of the following syntax in input :
                                    <addressrange name = "test1" rangestart="1.1.160.30" rangeend="1.1.160.40" enable="True" />
        Return Value :
            returns a Boolean True on success else raises an AssertionError exception

        '''
        error_msg_list = []
        logger.info("-- Verifying Address Range attributes of Subnet [{}]".format(subnetid))
        for addressrange in addressrange_list:
            if addressrange.has_property("newname"):
                rangename = addressrange.newname
            else:
                rangename = addressrange.name
            if cls.verify_range_exists(tableid, rangename, fail_if_false=False) is False:
                logger.warn("Range '{}' is not visible for subnet [{}]!".format(rangename, subnetid))
                error_msg_list.append("Range '{}' is not visible for subnet [{}]!".format(rangename, subnetid))
                continue

            logger.debug("--Verifying Range [{}] attributes".format(rangename))
            startip = ''
            endip = ''
            available_count = ''
            ip_count = ''
            range_count = ''

            if addressrange.has_property("rangestart"):
                startip = GetSubnetsAndAddressRangeAttributes.get_addressrange_startip(tableid, rangename)
                if startip.lower() != addressrange.rangestart.lower():
                    logger.debug("Range Start IP not set to [{}] but is set to [{}]".format(addressrange.rangestart, startip))
                    error_msg_list.append("Range Start IP not set to [{}] but is set to [{}] for range {}".format(addressrange.rangestart, startip, rangename))
            if addressrange.has_property("rangeend"):
                endip = GetSubnetsAndAddressRangeAttributes.get_addressrange_endip(tableid, rangename)
                if endip.lower() != addressrange.rangeend.lower():
                    logger.debug("Range End IP not set to [{}] but is set to [{}]".format(addressrange.rangeend, endip))
                    error_msg_list.append("Range End IP not set to [{}] but is set to [{}] for range {}".format(addressrange.rangeend, endip, rangename))
            if addressrange.has_property("enable"):
                try:
                    cls.verify_rangestate_and_available_count(tableid, rangename, addressrange.enable)
                except AssertionError as Ex:
                    logger.warn(Ex.message)
                    error_msg_list.append(Ex.message)

            if startip and endip:
                ip_count = common.get_ip_count(startip, endip)
                logger.debug("--Verifying Range Count")
                range_count = GetSubnetsAndAddressRangeAttributes.get_addressrange_count(tableid, rangename)
                if str(range_count) != str(ip_count):
                    logger.debug("Range count is set to '{}' but should be '{}'".format(range_count, ip_count))
                    error_msg_list.append("Range count is set to '{}' but should be '{}' for range {}".format(range_count, ip_count, rangename))
                else:
                    logger.debug("Range count displayed as : {}".format(range_count))
        if error_msg_list:
            raise AssertionError(error_msg_list)
        logger.debug("Verify Address Range attributes Return Value - True")
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_subnet_addressrange_label_visible(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking if the IPV4 subnet and address range label is visible")
        return ui_lib.wait_for_element_visible(cls.e.ID_LABEL_IPV4_SUBNET_ADDRESSRANGES, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_dns_unset_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Checking if DNS is unset")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.wait_for_element_visible(cls.e.ID_GENERIC_DNS_UNSET.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_rangestate_and_available_count(cls, tableid, rangename, rangeenable, timeout=5, fail_if_false=True):
        '''
        Function to verify the range state and the IP available count of an address range

        Arguments:
            tableid      -- ID of the table to check the range state in
            rangename    -- range name
            rangeenable  -- range state (true/false for enabled/disabled respectively)

        Return Value:
            returns a Boolean true on success else raises AssertionError Exception
        '''
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        logger.info("--- Verifying Input Range state with Available count of range {}".format(rangename))
        available_count = ''
        available_count = GetSubnetsAndAddressRangeAttributes.get_addressrange_availablecount(tableid, rangename)
        if rangeenable.lower() == 'true' and \
                cls.verify_range_available_disabled(tableid, rangename, fail_if_false=False) is False and \
                str(available_count) > str(0):
            logger.debug("Range is ENABLED and available count is '{}'".format(available_count))
        elif rangeenable.lower() == 'false' and \
                cls.verify_range_available_disabled(tableid, rangename, fail_if_false=False) is True:
            if str(available_count).lower() == 'disabled':
                logger.debug("Range is DISABLED and available count is '{}'".format(available_count))
            else:
                raise AssertionError("Range is DISABLED but the available count text is set to '{}'".format(available_count))
        else:
            raise AssertionError("Range state should be : '{}' but is not set to the same.The IP available count is : '{}'".format('ENABLED' if rangeenable.lower() == 'true' else 'DISABLED', available_count))
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_available_disabled(cls, tableid, rangename, timeout=5, fail_if_false=True):
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        logger.debug("Checking if range Available count is set to disabled")
        return ui_lib.wait_for_element_visible(GetIPPoolsElements.ID_TEXT_RANGE_AVAILABLE_DISABLED.format(tableid, rangename), timeout, fail_if_false)


class VerifySubnetsAndRangeEditDialog(VerifySubnetsAndAddressRange):

    e1 = GeneralIPPoolElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_exists_in_table(cls, rangename, timeout=5, fail_if_false=True):
        return cls.verify_range_exists(cls.e1.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG, rangename)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_subnet_and_range_attributes(cls, subnet_obj, timeout=5, fail_if_false=True):
        return cls.verify_ipv4_subnet_attributes(cls.e1.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG, subnet_obj, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_address_range_attributes(cls, subnetid, addressrange_list):
        return cls.verify_ipv4_addressrange_attributes(cls.e1.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG, subnetid, addressrange_list)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_rangestate_and_availablecount(cls, rangename, rangeenable, timeout=5, fail_if_false=True):
        return cls.verify_rangestate_and_available_count(cls.e1.ID_TABLE_IPV4_SUBNET_EDIT_ADDRESSESIDENTIFIERS_DIALOG, rangename, rangeenable, timeout, fail_if_false)


class VerifySubnetsAndRangeAddressIdentifiersPage(VerifySubnetsAndAddressRange):

    e1 = GeneralIPPoolElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_subnet_addressrange_table_is_not_empty(cls, timeout=5, fail_if_false=True):
        logger.debug("Checking if the Subnet table in Addresses and identifiers page is not empty")
        return ui_lib.wait_for_element_notvisible(VerifyIPPoolsElements.ID_TABLE_ADDRESSESIDENTIFIERS_PAGE_SUBNET_NODATA, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_delete_in_table(cls, subnetid, addressrange_list):
        return cls.verify_range_delete(cls.e1.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, subnetid, addressrange_list)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_range_exists_in_table(cls, rangename, timeout=5, fail_if_false=True):
        return cls.verify_range_exists(cls.e1.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, rangename)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_subnet_and_range_attributes(cls, subnet_obj, timeout=5, fail_if_false=True):
        return cls.verify_ipv4_subnet_attributes(cls.e1.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, subnet_obj, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_ipv4_address_range(cls, subnetid, addressrange_list):
        return cls.verify_ipv4_addressrange_attributes(cls.e1.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, subnetid, addressrange_list)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_rangestate_and_availablecount(cls, rangename, rangeenable, timeout=5, fail_if_false=True):
        return cls.verify_rangestate_and_available_count(cls.e1.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, rangename, rangeenable, timeout, fail_if_false)


class GetSubnetsAndAddressRangeAttributes(object):

    e = GetIPPoolsElements

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_subnetmask_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Getting SubnetMask")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_SUBNETMASK_IN_TABLE.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_gateway_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Getting Gateway")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_GATEWAY_IN_TABLE.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    def get_gateway_unset_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Getting Gateway")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_GATEWAY_UNSET_IN_TABLE.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_domainname_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Getting Domain name")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_DOMAIN_IN_TABLE.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    def get_domainname_unset_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Getting Domain Empty name")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_DOMAIN_UNSET_IN_TABLE.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_dns_in_table(cls, tableid, subnetid, timeout=5, fail_if_false=True):
        logger.debug("Getting DNS")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_DNS_IN_TABLE.format(tableid, subnetid), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addressrange_startip(cls, tableid, rangename, timeout=5, fail_if_false=True):
        logger.debug("Getting address range start IP")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_RANGE_STARTIP.format(tableid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addressrange_endip(cls, tableid, rangename, timeout=5, fail_if_false=True):
        logger.debug("Getting address range end IP")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_RANGE_ENDIP.format(tableid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addressrange_count(cls, tableid, rangename, timeout=5, fail_if_false=True):
        logger.debug("Getting address range count")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_RANGE_COUNT.format(tableid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addressrange_availablecount(cls, tableid, rangename, timeout=5, fail_if_false=True):
        logger.debug("Getting address range Available count")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_RANGE_AVAILABLE.format(tableid, rangename), timeout)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addressrange_allocatedcount(cls, tableid, rangename, timeout=5, fail_if_false=True):
        logger.debug("Getting address range Allocated count")
        tableid = GeneralAddressesAndIdentifiers.get_idpart(tableid)
        return ui_lib.get_text(cls.e.ID_TEXT_GENERIC_RANGE_ALLOCATED.format(tableid, rangename), timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_addressrange_allocatedcount_addressesidentifiers_page(cls, rangename, timeout=5, fail_if_false=True):
        return cls.get_addressrange_allocatedcount(GeneralIPPoolElements.ID_TABLE_IPV4_SUBNET_ADDRESSES_IDENTIFIERS_PAGE, rangename, timeout, fail_if_false)
