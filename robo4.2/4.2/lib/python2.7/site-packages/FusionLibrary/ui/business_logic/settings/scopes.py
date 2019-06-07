# (C) Copyright 2016 Hewlett-Packard Development Company, L.P.
"""
    Scopes Page
"""


from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from FusionLibrary.ui.business_logic.settings.scopes_elements import *
from FusionLibrary.ui.business_logic.base import FusionUIBase
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.networking import networks
from FusionLibrary.ui.business_logic.networking.logicalinterconnectgroups import CommonOperationLogicalInterconnectGroups
from FusionLibrary.ui.business_logic.networking.networksets import CommonOperationNetworkSets
from FusionLibrary.ui.business_logic.networking.networks import CommonOperationNetworks
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import CommonOperationLogicalInterconnect
from FusionLibrary.ui.business_logic.servers.enclosures import _BaseCommonOperationEnclosures
from FusionLibrary.ui.business_logic.networking.interconnects import CommonOperationInterconnects
from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from FusionLibrary.ui.general import activity


class CommonOperationScopes(object):

    @classmethod
    def verify_filter_by_scope(cls, xpath_id, name, timeout=5, fail_if_false=True):
        logger.debug("select scope %s" % name)
        if not ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_SCOPE_TABLE % xpath_id, timeout, fail_if_false):
            return ui_lib.fail_test("failed to find the element")
        ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_ALL_SCOPE % xpath_id, timeout, fail_if_false)
        if not ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_FILTER_BY_TABLE_ITEM % (xpath_id, name), timeout, fail_if_false):
            return ui_lib.fail_test("failed to find element")
        CommonOperationScopes.set_allscope_as_default(xpath_id)
        return True

    @classmethod
    def set_allscope_as_default(cls, xpath_id, timeout=5, fail_if_false=True):

        if ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_ALL_SCOPE % xpath_id, timeout, fail_if_false):
            ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_PAGE_SELECT % xpath_id, timeout, fail_if_false)
            return True

    @classmethod
    def verify_filter_by_all_scope(cls, xpath_id, name, timeout=5, fail_if_false=True):
        logger.debug("select scope %s" % name)
        if not ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_SCOPE_TABLE % xpath_id, timeout, fail_if_false):
            return ui_lib.fail_test("Failed to select Scope")
        if not ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_FILTER_BY_TABLE_ITEM % (xpath_id, name), timeout, fail_if_false):
            return ui_lib.fail_test("Failed to select scope")
        if ui_lib.is_visible(VerifyScopesElements.ID_ALL_RESOURCE, timeout, fail_if_false):
            ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_ALL_RESOURCE, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_PAGE_SELECT % xpath_id, timeout, fail_if_false)
        return True

    @classmethod
    def verify_filter_by_any_scope(cls, xpath_id, name, timeout=5, fail_if_false=True):
        logger.debug("select scope %s" % name)
        if not ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_SCOPE_TABLE % xpath_id, timeout, fail_if_false):
            return ui_lib.fail_test("Failed to select scope")
        if not ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_FILTER_BY_TABLE_ITEM % (xpath_id, name), timeout, fail_if_false=True):
            return ui_lib.fail_test("Failed to select scope")
        if ui_lib.is_visible(VerifyScopesElements.ID_ANY_RESOURCE, timeout, fail_if_false):
            ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_ANY_RESOURCE, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(VerifyScopesElements.ID_PAGE_SELECT % xpath_id, timeout, fail_if_false)
        return True

    @classmethod
    def get_appliance_state_scope(cls, timeout=5, fail_if_false=True):
        logger.debug("get appliance state for scope")
        for x in range(0, 20):
            if ui_lib.wait_for_element_visible(GeneralScopesElements.ID_MAIN_MENU, timeout, fail_if_false):
                logger.info("Main menu is visible")
                activity.navigate()
                if ui_lib.wait_for_element_visible(GeneralScopesElements.ID_ACTIVITY_LABEL, timeout, fail_if_false):
                    logger.info("Activity page is visible")
                    networks.navigate()
                    if ui_lib.wait_for_element_visible(GeneralScopesElements.ID_NETWORK_PAGE_LABEL, timeout, fail_if_false):
                        logger.info("scopes page is visible")
                    else:

                        state = ui_lib.wait_for_element_visible(GeneralScopesElements.ID_APPLIANCE_STATE, timeout, fail_if_false)
                        if state is True:
                            return ui_lib.fail_test("Appliance is temporarily unavailable")
                else:
                    state = ui_lib.wait_for_element_visible(GeneralScopesElements.ID_APPLIANCE_STATE, timeout, fail_if_false)
                    if state is True:
                        return ui_lib.fail_test("Appliance is temporarily unavailable")
            else:
                state = ui_lib.wait_for_element_visible(GeneralScopesElements.ID_APPLIANCE_STATE, timeout, fail_if_false)
                if state is True:
                    return ui_lib.fail_test("Appliance is temporarily unavailable")
        return True

    @classmethod
    def select_scopes_from_dropdown(cls, fail_if_false=True):
        logger.debug("Select Scopes from dropdown")
        return FusionUIBase.select_view_by_name("Scopes")

    @classmethod
    def verify_lig_scopes(cls, timeout=5, fail_if_false=True):
        ligs_list = CommonOperationLogicalInterconnectGroups.get_lig_list()
        for lig_name in ligs_list:
            logger.debug("selecting LIG: %s" % lig_name)
            lig_select_status = ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_LIG_TABLE % lig_name, timeout, fail_if_false)
            logger.debug("the lig_select_status is %s" % lig_select_status)
            if lig_select_status is False:
                logger._warn("Failed to click LIG: {0}".format(lig_name))
                return ui_lib.fail_test("Failed to click LIG")
            else:
                logger.debug("'{0}' LIG is selected Successfully ".format(lig_name))
            msg = 'No scopes'
            return ui_lib.wait_for_element_text_match(GeneralScopesElements.ID_SCOPE_MESSAGE, msg, fail_if_false)

    @classmethod
    def verify_network_scopes(cls, timeout=5, fail_if_false=True):
        Networks_list = CommonOperationNetworks.get_network_list()
        for network_name in Networks_list:
            logger.debug("selecting Network: %s" % network_name)
            network_select_status = ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_NETWORK_TABLE % network_name, timeout, fail_if_false)
            logger.debug("the network_select_status is %s" % network_select_status)
            if network_select_status is False:
                logger._warn("Failed to click Network: {0}".format(network_name))
                return ui_lib.fail_test("Failed to click the element")
            else:
                logger.debug("'{0}' Network is selected Successfully".format(network_name))
            msg = 'No scopes'
            return ui_lib.wait_for_element_text_match(GeneralScopesElements.ID_SCOPE_MESSAGE, msg, fail_if_false)

    @classmethod
    def verify_networkset_scopes(cls, timeout=5, fail_if_false=True):
        NETWORKSETS_list = CommonOperationNetworkSets.get_network_sets_list()
        for NETWORKSETS_name in NETWORKSETS_list:
            logger.debug("selecting NETWORKSETS: %s" % NETWORKSETS_name)
            NETWORKSETS_select_status = ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_NETWORKSETS_TABLE % NETWORKSETS_name, timeout, fail_if_false)
            logger.debug("the network_select_status is %s" % NETWORKSETS_select_status)
            if NETWORKSETS_select_status is False:
                logger._warn("Failed to click NETWORKSETS: {0}".format(NETWORKSETS_name))
                return ui_lib.fail_test("Failed to click the element")
            else:
                logger.debug("'{0}' NETWORKSETS is selected Successfully".format(NETWORKSETS_name))
            msg = 'No scopes'
            return ui_lib.wait_for_element_text_match(GeneralScopesElements.ID_SCOPE_MESSAGE, msg, fail_if_false)

    @classmethod
    def verify_interconnects_scopes(cls, timeout=5, fail_if_false=True):
        INTERCONNECTS_list = CommonOperationInterconnects.get_interconnect_list()
        for INTERCONNECTS_name in INTERCONNECTS_list:
            logger.debug("selecting INTERCONNECTS: %s" % INTERCONNECTS_name)
            INTERCONNECTS_select_status = ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_INTERCONNECTS_TABLE % INTERCONNECTS_name, timeout, fail_if_false)
            logger.debug("the INTERCONNECTS_select_status is %s" % INTERCONNECTS_select_status)
            if INTERCONNECTS_select_status is False:
                logger._warn("Failed to click INTERCONNECTS: {0}".format(INTERCONNECTS_name))
                return ui_lib.fail_test("Failed to click the element")
            else:
                logger.debug("'{0}' INTERCONNECTS is selected Successfully".format(INTERCONNECTS_name))
            msg = 'No scopes'
            return ui_lib.wait_for_element_text_match(GeneralScopesElements.ID_SCOPE_MESSAGE, msg, fail_if_false)

    @classmethod
    def verify_enclosure_scopes(cls, timeout=5, fail_if_false=True):
        ENCLOSURES_list = _BaseCommonOperationEnclosures.get_enclosure_list(timeout=5)
        for ENCLOSURES_name in ENCLOSURES_list:
            logger.debug("selecting ENCLOSURE: %s" % ENCLOSURES_name)
            ENCLOSURES_select_status = ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_ENCLOSURE_TABLE % ENCLOSURES_name, timeout, fail_if_false)
            logger.debug("the ENCLOSURES_select_status is %s" % ENCLOSURES_select_status)
            if ENCLOSURES_select_status is False:
                logger._warn("Failed to click ENCLOSURE: {0}".format(ENCLOSURES_name))
                return ui_lib.fail_test("Failed to click the element")
            else:
                logger.debug("'{0}' ENCLOSURE is selected Successfully".format(ENCLOSURES_name))
            msg = 'No scopes'
            return ui_lib.wait_for_element_text_match(GeneralScopesElements.ID_SCOPE_MESSAGE, msg, fail_if_false)

    @classmethod
    def verify_li_scopes(cls, timeout=5, fail_if_false=True):
        LI_list = CommonOperationLogicalInterconnect.get_li_list()
        logger.debug("the LI list is %s" % LI_list)
        for LI_name in LI_list:
            logger.debug("selecting LI: %s" % LI_name)
            LI_select_status = ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_LI_TABLE % LI_name, timeout, fail_if_false)
            logger.debug("the LI_select_status is %s" % LI_select_status)
            if LI_select_status is False:
                logger._warn("Failed to click LI: {0}".format(LI_name))
                return ui_lib.fail_test("Failed to click the element")
            else:
                logger.debug("'{0}' LI is selected Successfully".format(LI_name))
            msg = 'No scopes'
            return ui_lib.wait_for_element_text_match(GeneralScopesElements.ID_SCOPE_MESSAGE, msg, fail_if_false)

    @classmethod
    def verify_serverhw_scopes(cls, timeout=5, fail_if_false=True):
        ui_lib.wait_for_element(GeneralScopesElements.ID_SERVERHW_TABLE)
        SERVERHW_list = CommonOperationServerHardware.get_server_hardware_list()
        for SERVERHW_name in SERVERHW_list:
            logger._log_to_console_and_log_file("selecting SERVERHW: %s" % SERVERHW_name)
            SERVERHW_select_status = ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_SERVERHW_TABLE % SERVERHW_name, 10, fail_if_false)
            logger.debug("the SERVERHW_select_status is %s" % SERVERHW_select_status)
            if SERVERHW_select_status is False:
                logger._warn("Failed to click SERVERHW: {0}".format(SERVERHW_name))
                return ui_lib.fail_test("Failed to click the element")
            else:
                logger._log_to_console_and_log_file("'{0}' SERVERHW is selected Successfully".format(SERVERHW_name))
        msg = 'No scopes'
        return ui_lib.wait_for_element_text_match(GeneralScopesElements.ID_SCOPE_MESSAGE, msg, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scopes_page_buttons(cls, timeout=5, fail_if_false=True):

        logger.debug("Check [ create Scope is present]")
        logger.debug("Check [ Action Button is present]")
        logger.debug("Check [ help Button is present]")
        scope = ui_lib.wait_for_element_visible(CreateScopesElements.ID_BUTTON_CREATE_SCOPE, timeout, fail_if_false)
        logger.debug("checking scope %s" % scope)
        helpbtn = ui_lib.wait_for_element_visible(GeneralScopesElements.ID_SCOPE_HELP_ICON, timeout, fail_if_false)
        logger.debug("checking Help %s" % helpbtn)
        activitybtn = ui_lib.wait_for_element_visible(GeneralScopesElements.ID_SCOPE_ACTIVITY_ICON, timeout, fail_if_false)
        logger.debug("checking Activity %s" % activitybtn)
        if scope and helpbtn and activitybtn:
            return True
        else:
            ui_lib.fail_test("The mandatory scopes page buttons were not present")

    @classmethod
    def load_bulk_enets(cls, timeout=5, fail_if_false=True):
        """ This function will select 1500 bulk enets from a dropdown by scrolling and clicking on load more
            until all the networks are selected at a single stretch from scopes page for resource assignment.
        """
        selenium2lib = ui_lib.get_s2l()
        while ui_lib.is_visible(GeneralScopesElements.ID_MOUSE_OVER, timeout, fail_if_false):
            selenium2lib.mouse_over(GeneralScopesElements.ID_MOUSE_OVER)
            ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_MOUSE_OVER, timeout, fail_if_false)

        if ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_TABLE_ENETS_LIST, timeout, fail_if_false):
            ActionChains(selenium2lib._current_browser()).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

            return True

    @classmethod
    def select_scope(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("select scope %s" % name)
        if not ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false):
            logger.debug("unable to select the required scope")
            return False
        return ui_lib.wait_for_element(GeneralScopesElements.ID_VERIFY_SCOPE_TITLE % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def is_on_scopes_page(cls, wait_timeout=5, fail_if_false=False):
        logger.debug("Determine if current page is Scopes")
        return ui_lib.wait_for_element_visible(GeneralScopesElements.ID_PAGE_LABEL, wait_timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_for_scopes_load(cls, wait_timeout=10, fail_if_false=False):
        logger.debug("Determine if Scopes load completely")
        return ui_lib.wait_for_element_visible(GeneralScopesElements.ID_PAGE_OVERVIEW, wait_timeout, fail_if_false)

    @classmethod
    def click_scope_title(cls, wait_timeout=5):
        logger.debug("Click [ Scopes title ]")
        ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_LINK_SCOPES, wait_timeout, fail_if_false=True)

    @classmethod
    def wait_for_scope_bulk_assign(cls, scope_obj, timeout=5, fail_if_false=True):
        logger.debug("verify bulk resource")
        logger.debug("verify bulk resource %s" % scope_obj)
        activity.navigate()
        return ui_lib.wait_for_element(GeneralScopesElements.ID_SCOPEASSIGN_ACTVITY, 750, fail_if_false)

    @classmethod
    def verify_bulk_resource(cls, scope_obj, timeout=5, fail_if_false=True):
        logger.debug("verify bulk resource")
        logger.debug("verify bulk resource %s" % scope_obj)

        if ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_TABLE_SCOPE_NAME % scope_obj, timeout, fail_if_false):
            if ui_lib.wait_for_element(GeneralScopesElements.ID_RESOURCE_TABLE):
                scope_list = ui_lib.get_multi_elements_text(GeneralScopesElements.ID_RESOURCE_TABLE, timeout, fail_if_false)
                logger.info("scopelist is %s" % scope_list)
                return scope_list
        else:
            ui_lib.fail_test("Failed to get resource list")

    @classmethod
    def get_scope_list(cls, wait_timeout=5):
        logger.debug("Get Scope List")
        scope_list = []
        if ui_lib.wait_for_element(GeneralScopesElements.ID_TABLE_SCOPE_NAME_LIST):
            scope_list = ui_lib.get_multi_elements_text(GeneralScopesElements.ID_TABLE_SCOPE_NAME_LIST, wait_timeout, fail_if_false=True)
        return scope_list

    @classmethod
    def click_resource_link(cls, category, wait_timeout=5):
        logger.debug("Click [ Resource ] : %s" % category)
        ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_LINK_SCOPE_RESOURCE % category, wait_timeout, fail_if_false=True)

    @classmethod
    def click_settings_link(cls, timeout=5, fail_if_false=True):
        logger.debug("Click settings link")
        ui_lib.wait_for_element_and_click(GeneralScopesElements.ID_SETTINGS_LINK, timeout, fail_if_false)

    @classmethod
    def get_scope_name(cls, timeout=5, fail_if_false=True, hidden_element=False):
        logger.debug("Scope Name is : %s" % ui_lib.get_text(GeneralScopesElements.ID_SCOPE_NAME, timeout, fail_if_false, hidden_element))
        return ui_lib.get_text(GeneralScopesElements.ID_SCOPE_NAME, timeout, fail_if_false, hidden_element)

    @classmethod
    def get_scope_description(cls, timeout=5, fail_if_false=True, hidden_element=False):
        logger.debug("Scope Description is : %s" % ui_lib.get_text(GeneralScopesElements.ID_SCOPE_DESCRIPTION, timeout, fail_if_false, hidden_element))
        return ui_lib.get_text(GeneralScopesElements.ID_SCOPE_DESCRIPTION, timeout, fail_if_false, hidden_element)

    @classmethod
    def get_scope_count(cls, timeout=5, fail_if_false=True, hidden_element=False):
        logger.debug("Get Scope Count")
        return ui_lib.get_text(GeneralScopesElements.ID_SCOPE_COUNT, timeout, fail_if_false, hidden_element)

    @classmethod
    def get_scope_error_message(cls, timeout=5, fail_if_false=True, hidden_element=False):
        logger.debug("Get scope error message")
        return ui_lib.get_text(GeneralScopesElements.ID_SCOPE_ERROR_TEXT, timeout, fail_if_false, hidden_element)

    @classmethod
    def get_scopename_validate_message(cls, timeout=5, fail_if_false=True, hidden_element=False):
        logger.debug("Get scopename validate mesaage")
        if ui_lib.is_visible(GeneralScopesElements.ID_SCOPE_NAME_VALIDATE_MSG, timeout, fail_if_false):
            return ui_lib.get_text(GeneralScopesElements.ID_SCOPE_NAME_VALIDATE_MSG, timeout, fail_if_false, hidden_element)
        else:
            return None

    @classmethod
    def get_enets_list(cls, timeout=5, fail_if_false=True):
        logger.debug("Get Enets List")
        enets_list = []
        if ui_lib.wait_for_element(GeneralScopesElements.ID_TABLE_ENETS_LIST):
            enets_list = ui_lib.get_multi_elements_text(GeneralScopesElements.ID_TABLE_ENETS_LIST, timeout, fail_if_false)
            return enets_list


class CreateScopes(object):

    @classmethod
    def click_create_scope_button(cls, wait_timeout=5):
        logger.debug("click Create scope button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_CREATE_SCOPE, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_scope_dialog_open(cls, wait_timeout=5, fail_if_false=True):
        logger.debug('waiting create scope dialog open')
        return ui_lib.wait_for_element_visible(CreateScopesElements.ID_DIALOG_CREATE_SCOPE, wait_timeout, fail_if_false)

    @classmethod
    def input_name(cls, name, wait_timeout=5):
        logger.debug("input scope name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateScopesElements.ID_INPUT_SCOPE_NAME, name, wait_timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, wait_timeout=5):
        logger.debug("input scope description '%s'" % description)
        ui_lib.wait_for_element_and_input_text(CreateScopesElements.ID_INPUT_SCOPE_DESCRIPTION, description, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_resources_button(cls, wait_timeout=5):
        logger.debug("click add resources button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_ADD_RESOURCE, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_resources_button(cls, wait_timeout=5):
        logger.debug("click remove resources button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_REMOVE_RESOURCE, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_resources_dialog_open(cls, wait_timeout=5, fail_if_false=True):
        logger.debug('waiting add resources dialog open')
        return ui_lib.wait_for_element_visible(CreateScopesElements.ID_DIALOG_ADD_RESOURCE, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_resources_dialog_close(cls, wait_timeout=5, fail_if_false=True):
        logger.debug("wait add resources dialog close")
        return ui_lib.wait_for_element_notvisible(CreateScopesElements.ID_DIALOG_ADD_RESOURCE, wait_timeout, fail_if_false)

    @classmethod
    def input_and_select_resource_category(cls, category, wait_timeout=5):
        logger.debug("input and select resource category %s" % category)
        FusionUIBase.choose_combo_option_by_text(CreateScopesElements.ID_COMBO_RESOURCE_CATEGORY, category, wait_timeout, fail_if_false=True)

    @classmethod
    def input_resource_name(cls, name, wait_timeout=5):
        logger.debug("input resource name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(CreateScopesElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_resource_name(cls, name, wait_timeout=5):
        logger.debug("click resource name '%s'" % name)
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_TABLE_RESOURCE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, wait_timeout=5):
        logger.debug("click add button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_ADD, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, wait_timeout=5):
        logger.debug("click add+ button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_ADD_AGAIN, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_add_resource_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_ADD_RESOURCE_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    def remove_resources_by_name(cls, name, wait_timeout=5):
        logger.debug("remove resource %s" % name)
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_ICON_REMOVE_RESOURCE % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_create_button(cls, wait_timeout=5):
        logger.debug("click create button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_CREATE, wait_timeout, fail_if_false=True)

    @classmethod
    def click_create_plus_button(cls, wait_timeout=5):
        logger.debug("click create+ button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_CREATE_SCOPE_PLUS, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(CreateScopesElements.ID_BUTTON_CREATE_SCOPE_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_scope_dialog_close(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("wait create resource dialog close")
        return ui_lib.wait_for_element_remove(CreateScopesElements.ID_DIALOG_CREATE_SCOPE, wait_timeout, fail_if_false)


class EditScopes(object):

    @classmethod
    def click_edit_scope_button(cls, wait_timeout=5):
        logger.debug("click edit scope button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_ACTIONS, wait_timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_ACTIONS_EDIT_SCOPE, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_open(cls, wait_timeout=5, fail_if_false=True):
        logger.debug('waiting edit scope dialog open')
        return ui_lib.wait_for_element_visible(EditScopesElements.ID_DIALOG_EDIT_SCOPE, wait_timeout, fail_if_false)

    @classmethod
    def input_name(cls, name, wait_timeout=5):
        logger.debug("input scope name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditScopesElements.ID_INPUT_SCOPE_NAME, name, wait_timeout, fail_if_false=True)

    @classmethod
    def input_description(cls, description, wait_timeout=5):
        logger.debug("input scope description '%s'" % description)
        ui_lib.wait_for_element_and_input_text(EditScopesElements.ID_INPUT_SCOPE_DESCRIPTION, description, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_resources_button(cls, wait_timeout=5):
        logger.debug("click add resources button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_ADD_RESOURCE, wait_timeout, fail_if_false=True)

    @classmethod
    def click_remove_resources_button(cls, wait_timeout=5):
        logger.debug("click remove resources button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_REMOVE_RESOURCE, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_resources_dialog_open(cls, wait_timeout=5, fail_if_false=True):
        logger.debug('waiting add resources dialog open')
        return ui_lib.wait_for_element_visible(EditScopesElements.ID_DIALOG_ADD_RESOURCE, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_resources_dialog_close(cls, wait_timeout=5, fail_if_false=True):
        logger.debug("wait add resources dialog close")
        return ui_lib.wait_for_element_notvisible(EditScopesElements.ID_DIALOG_ADD_RESOURCE, wait_timeout, fail_if_false)

    @classmethod
    def input_and_select_resource_category(cls, category, wait_timeout=5):
        logger.debug("input and select resource category %s" % category)
        FusionUIBase.choose_combo_option_by_text(EditScopesElements.ID_COMBO_RESOURCE_CATEGORY, category, wait_timeout, fail_if_false=True)

    @classmethod
    def input_and_select_remove_resource_category(cls, category, timeout=5, fail_if_false=True):
        logger.debug("input and select resource category [ %s ]" % category)
        FusionUIBase.choose_option_by_text(EditScopesElements.ID_COMBO_REMOVE_RESOURCE_CATEGORY, category, timeout, fail_if_false)

    @classmethod
    def input_resource_name(cls, name, wait_timeout=5):
        logger.debug("input resource name '%s'" % name)
        ui_lib.wait_for_element_and_input_text(EditScopesElements.ID_INPUT_SEARCH_TEXT, name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_resource_name(cls, name, wait_timeout=5):
        logger.debug("click resource name '%s'" % name)
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_TABLE_RESOURCE_NAME % name, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, wait_timeout=5):
        logger.debug("click add button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_ADD, wait_timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, wait_timeout=5):
        logger.debug("click add+ button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_ADD_AGAIN, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_add_resource_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_ADD_RESOURCE_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    def remove_resources_by_name(cls, name, wait_timeout=5):
        logger.debug("remove resource %s" % name)
        if ui_lib.wait_for_element_and_click(EditScopesElements.ID_SELECT_RESOURCE_NAME % name, wait_timeout, fail_if_false=True):
            return True
        else:
            ui_lib.fail_test("unable to remove the element")

    @classmethod
    def click_ok_button(cls, wait_timeout=5):
        logger.debug("click ok button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_OK, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_EDIT_SCOPE_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_remove_resource_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(DeleteScopesElements.ID_BUTTON_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_scope_dialog_close(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("wait edit scope dialog close")
        return ui_lib.wait_for_element_remove(EditScopesElements.ID_DIALOG_EDIT_SCOPE, wait_timeout, fail_if_false)

    @classmethod
    def click_remove_resources_button_from_scope(cls, wait_timeout=5, fail_if_false=True):
        logger.debug("click remove resources button")
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_REMOVE_RESOURCE_FROM_SCOPE, wait_timeout, fail_if_false)


class DeleteScopes(object):

    @classmethod
    def click_delete_scope_button(cls, wait_timeout=5):
        logger.debug("click delete Scope button")
        ui_lib.wait_for_element_and_click(DeleteScopesElements.ID_ACTION_MAIN_BTN, wait_timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(DeleteScopesElements.ID_ACTION_MENU_DELETE_SCOPE, wait_timeout, fail_if_false=True)

    @classmethod
    def click_yes_delete_button(cls, wait_timeout=5):
        logger.debug("click 'Yes, delete' button")
        ui_lib.wait_for_element_and_click(DeleteScopesElements.ID_BTN_DELETE_SCOPE, wait_timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, wait_timeout=5):
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(DeleteScopesElements.ID_BTN_CANCEL, wait_timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_delete_scope_dialog_close(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("wait delete scope dialog close")
        return ui_lib.wait_for_element_remove(DeleteScopesElements.ID_DIALOG_DELETE_SCOPE, wait_timeout, fail_if_false)


class VerifyScopes(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_existed(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("verify Scope '%s' existed ..." % name)
        return ui_lib.wait_for_element(GeneralScopesElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_not_existed(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("verify Scope '%s' not existed ..." % name)
        return ui_lib.wait_for_element_notvisible(GeneralScopesElements.ID_TABLE_SCOPE_NAME % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_resource_existed(cls, name, wait_timeout=5, fail_if_false=False):
        logger.debug("verify resource existed")
        if ui_lib.wait_for_element_visible(VerifyScopesElements.ID_ADD_RESOURCES_TABLE, 2, fail_if_false):
            return ui_lib.wait_for_element(VerifyScopesElements.ID_ADD_RESOURCES_TABLE_ITEM % name, wait_timeout, fail_if_false)
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_resource_existed(cls, name, wait_timeout=5, fail_if_false=False):
        logger.debug("verify resource existed")
        if ui_lib.wait_for_element_visible(VerifyScopesElements.ID_EDIT_RESOURCES_TABLE, 2, fail_if_false):
            return ui_lib.wait_for_element(VerifyScopesElements.ID_EDIT_RESOURCES_TABLE_ITEM % name, wait_timeout, fail_if_false)
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_deleted(cls, name, wait_timeout=20, fail_if_false=True):
        logger.debug("verify delete scope successful")
        return ui_lib.wait_for_element(VerifyScopesElements.ID_TABLE_SCOPE_DELETED % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_resource_deleted(cls, name, wait_timeout=10, fail_if_false=True):
        logger.debug("verify delete resource successful")
        return ui_lib.wait_for_element_remove(VerifyScopesElements.ID_ICON_REMOVE_RESOURCE % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_created(cls, name, wait_timeout=5, fail_if_false=True):
        logger.debug("verify create scope successful")
        return ui_lib.wait_for_element(VerifyScopesElements.ID_VERIFY_SCOPE_TITLE % name, wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_plus_complete(cls, wait_timeout=10, fail_if_false=True):
        logger.debug("verify scope create+ complete")
        if not ui_lib.wait_for_element_hidden(VerifyScopesElements.ID_CREATE_SCOPE_FORM_MESSAGE, wait_timeout, False):
            ui_lib.fail_test("scope create failed")
        return ui_lib.wait_for_element_text(VerifyScopesElements.ID_INPUT_SCOPE_NAME, "", wait_timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_scope_button_not_exist(cls, timeout=5, fail_if_false=True):
        logger.debug("verify create Scope button is not existed")
        return ui_lib.wait_for_element_notvisible(CreateScopesElements.ID_BUTTON_CREATE_SCOPE, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_user_authorizaton(cls, timeout=5, fail_if_false=True):
        ui_lib.wait_for_element_and_click(EditScopesElements.ID_BUTTON_ACTION_MENU, timeout, fail_if_false)
        return ui_lib.wait_for_element_visible(EditScopesElements.ID_BUTTON_AUTH, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_scope_resources(cls, resource, timeout=5, fail_if_false=True):
        logger.debug("verify Scope Resources")
        return ui_lib.wait_for_element(VerifyScopesElements.ID_LINK_SCOPE_RESOURCE_NAME % resource, timeout, fail_if_false)
