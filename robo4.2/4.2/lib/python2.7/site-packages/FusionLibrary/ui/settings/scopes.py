#    (C) Copyright 2016 Hewlett-Packard Development Company, L.P.
"""
    Scopes Page
"""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.business_logic.settings.scopes import *
from FusionLibrary.ui.business_logic.settings.scopes import VerifyScopes, CommonOperationScopes
from FusionLibrary.ui.business_logic.base import SectionType, SubSectionType
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.servers.enclosures import VerifyEnclosures
from FusionLibrary.ui.business_logic.servers.serverhardware import VerifyHardware
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.servers.enclosures import _BaseCommonOperationEnclosures
from FusionLibrary.ui.business_logic.servers.serverhardware import CommonOperationServerHardware, VerifyHardware
from FusionLibrary.ui.business_logic.networking.networksets import CommonOperationNetworkSets, VerifyNetworkSets
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import CommonOperationLogicalInterconnect, VerifyLogicalInterconnects
from FusionLibrary.ui.business_logic.networking.logicalinterconnectgroups import CommonOperationLogicalInterconnectGroups, VerifyLogicalInterconnectGroups
from FusionLibrary.ui.business_logic.networking.networks import CommonOperationNetworks
from FusionLibrary.ui.business_logic.networking.interconnects import CommonOperationInterconnects
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.networking.interconnects import VerifyInterconnects
from FusionLibrary.ui.business_logic.settings.scopes_elements import GeneralScopesElements
from FusionLibrary.ui.general import activity

import sys


def navigate():
    if CommonOperationScopes.is_on_scopes_page() is False:
        FusionUIBase.navigate_to_section(SectionType.SETTINGS, time_for_loading=3)
        FusionUIBase.navigate_to_section_by_link(SubSectionType.Settings.SCOPES[0], SubSectionType.Settings.SCOPES[1], time_for_loading=3, sub_section=True)


def validate_scopes_page_buttons():
    navigate()
    return CommonOperationScopes.verify_scopes_page_buttons()


def select_scopes_dropdown():
    return CommonOperationScopes.select_scopes_from_dropdown()


def create_scope(*scopes_obj):
    """ Create Scope
        Example:
        | `Create Scope`      | ${myScopeList}    |
    """

    logger.info("Create Scope")
    navigate()
    if isinstance(scopes_obj, test_data.DataObj):
        scopes_obj = [scopes_obj]
    elif isinstance(scopes_obj, tuple):
        scopes_obj = list(scopes_obj[0])

    fail_if_exist = 0

    for scope in scopes_obj:
        if VerifyScopes.verify_scope_existed(scope.name, 5, False):
            fail_if_exist += 1
            logger.warn("scope %s already exists" % scope.name)
            continue
        have_resource = False
        CreateScopes.click_create_scope_button()
        logger.info("Creating scope %s" % scope.name)
        CreateScopes.wait_create_scope_dialog_open()
        CreateScopes.input_name(scope.name)
        if hasattr(scope, 'description'):
            CreateScopes.input_description(scope.description)
        if hasattr(scope, 'resources'):
            for n, resource in enumerate(scope.resources):
                have_resource = True
                _Add_Resource_To_Scope_Add(resource)
        CreateScopes.click_create_plus_button()
        VerifyScopes.verify_create_plus_complete()
        CreateScopes.click_cancel_button()
        CreateScopes.wait_create_scope_dialog_close()

        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(scope.name, 'Create', timeout=60, fail_if_false=True)
        if have_resource:
            FusionUIBase.wait_activity_action_ok(scope.name, 'Update Resource Assignments', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()

        CommonOperationScopes.select_scope(scope.name)
        VerifyScopes.verify_scope_created(scope.name)

    if fail_if_exist > 0:
        return False
    return True


def delete_scope(*scopes_obj):
    """ Delete Scope

        Example:
        | `Delete Scope`      | ${myScopeList}    |
    """
    logger.info("Delete Scope")
    navigate()
    if isinstance(scopes_obj, test_data.DataObj):
        scopes_obj = [scopes_obj]
    elif isinstance(scopes_obj, tuple):
        scopes_obj = list(scopes_obj[0])

    total = len(scopes_obj)
    not_exists = 0
    deleted = 0

    for n, scope in enumerate(scopes_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("deleting a scope named '%s'" % scope.name)
        if VerifyScopes.verify_scope_existed(scope.name, 5, False) is True:
            select_scope(scope.name)
            DeleteScopes.click_delete_scope_button()
            DeleteScopes.click_yes_delete_button()
            DeleteScopes.wait_delete_scope_dialog_close()
            FusionUIBase.show_activity_sidebar()
            if not FusionUIBase.wait_activity_action_ok(scope.name, 'Delete', timeout=60, fail_if_false=False):
                FusionUIBase.show_activity_sidebar()
                continue
            FusionUIBase.show_activity_sidebar()
            VerifyScopes.verify_scope_not_existed(scope.name)
            deleted += 1
        else:
            logger.warn("scope '%s' does NOT exist! ..." % scope.name)
            not_exists += 1
            continue

    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no scope to delete! all %s scope(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        return False
    else:
        if deleted < total:
            logger.warn("not all of the scope(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
            if deleted + not_exists == total:
                logger.warn("%s not-existing scope(s) is skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                return False
            else:
                ui_lib.fail_test("%s not-existing scope(s) is skipped, %s scope(s) left is failed being deleted " % (not_exists, total - deleted - not_exists))

    logger.info("all of the scope(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def select_scope(scope_name):
    """ Select Scope  """
    logger.info("Selecting scope %s :" % scope_name)
    navigate()
    CommonOperationScopes.select_scope(scope_name)
    VerifyScopes.verify_scope_created(scope_name)
    return True


def edit_scope(*scope_obj):
    """ Edit Scope    """
    logger.info("Edit Scope")
    navigate()
    if isinstance(scope_obj, test_data.DataObj):
        scope_obj = [scope_obj]
    elif isinstance(scope_obj, tuple):
        scope_obj = list(scope_obj[0])
    fail_if_exist = 0
    #    Looping to edit all the resources present in the resources.txt file
    for scope in scope_obj:
        logger.info("Editing scope %s" % scope.name)
        if scope.has_property("new_name"):
            if scope.new_name != scope.name and VerifyScopes.verify_scope_existed(scope.new_name, 5, False):
                fail_if_exist += 1
                logger.warn("scope %s already exists, can't edit scope" % scope.new_name)
                continue

        have_resource = False
        #    Selecting the given scope
        if CommonOperationScopes.select_scope(scope.name):
            #    Clicking on edit button and verifying the edit options page
            CommonOperationScopes.wait_for_scopes_load()
            EditScopes.click_edit_scope_button()
            EditScopes.wait_edit_scope_dialog_open()
            if scope.has_property("new_name"):
                data = _Verify_Parameter(scope.new_name, "Scope Name")
                if not (data == "none" or data == ""):
                    EditScopes.input_name(data)
            #    deleting resources
            if hasattr(scope, 'remove_resources'):
                for n, resource in enumerate(scope.remove_resources):
                    have_resource = True
                    logger.info("Deleting resource %s from scope" % resource.name)
                    #   EditScopes.remove_resources_by_name(resource.name)
                    EditScopes.click_remove_resources_button()
                    EditScopes.input_and_select_remove_resource_category(resource.category)
                    EditScopes.click_remove_resources_button_from_scope()
                    #   EditScopes.click_ok_button()
                    #   VerifyScopes.verify_resource_deleted(resource.name)
            #    add resources
            if hasattr(scope, 'add_resources'):
                for n, resource in enumerate(scope.add_resources):
                    have_resource = _Add_Resource_To_Scope(resource) or have_resource
            EditScopes.click_ok_button()
            EditScopes.wait_edit_scope_dialog_close()

        if have_resource:
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok(scope.name, 'Update', timeout=120, fail_if_false=True)
            FusionUIBase.show_activity_sidebar()

    if fail_if_exist > 0:
        return False
    return True


def _remove_resource_from_scope(resource):

    logger.info("Deleting the resource %s from scope" % resource.name)
    EditScopes.click_remove_resources_button()
    EditScopes.input_and_select_remove_resource_category(resource.category)
    EditScopes.remove_resources_by_name(resource.name)
    EditScopes.click_remove_resources_button_from_scope()
    EditScopes.click_ok_button()
    EditScopes.wait_edit_scope_dialog_close()
    return True


def _verify_resource_deleted(resource):
    logger.info("Verify Deleting the resource %s from scope" % resource.name)
    EditScopes.click_edit_scope_button()
    EditScopes.click_remove_resources_button()
    EditScopes.input_and_select_remove_resource_category(resource.category)
    VerifyScopes.verify_resource_deleted(resource)
    return True


def validate_resource_can_be_added_to_scope(*scope_obj):
    """ Validate Resource Can Be Added To Scope    """
    logger.info("Validate Resource Can Be Added To Scope")
    navigate()
    if isinstance(scope_obj, test_data.DataObj):
        scope_obj = [scope_obj]
    elif isinstance(scope_obj, tuple):
        scope_obj = list(scope_obj[0])
    fail_if_exist = 0
    #    Looping to edit all the resourcs present in the resources.txt file
    for scope in scope_obj:
        logger.info("Editing scope %s" % scope.name)
        #    Selecting the given scope
        if CommonOperationScopes.select_scope(scope.name):
            #    Clicking on edit button and verifying the edit options page
            EditScopes.click_edit_scope_button()
            EditScopes.wait_edit_scope_dialog_open()
            #    Verify resources
            if scope.has_property("resources"):
                _Add_Resource_To_Scope(scope.resources)
            EditScopes.click_cancel_button()
            EditScopes.wait_edit_scope_dialog_close()
    if fail_if_exist > 0:
        return False
    return True


def validate_resource_assigned_to_scope(*scopes_obj):
    """ validate resource
        Example:
        | `validate resource assigned to scope`      | ${myScopeList}    |
    """

    logger.info("validate resource assigned to scope")
    navigate()
    if isinstance(scopes_obj, test_data.DataObj):
        scopes_obj = [scopes_obj]
    elif isinstance(scopes_obj, tuple):
        scopes_obj = list(scopes_obj[0])

    #    Scope category verify function map
    categories = {'Enclosures': VerifyEnclosures.verify_enclosure_exist,
                  'Server Hardware': VerifyHardware.verify_server_hardware_exist,
                  'Ethernet Networks': CommonOperationNetworks.verify_network_exist,
                  'Fibre Channel Networks': CommonOperationNetworks.verify_network_exist,
                  'FCoE Networks': CommonOperationNetworks.verify_network_exist,
                  'Network Sets': VerifyNetworkSets.verify_network_set_existed,
                  'Logical Interconnect Groups': VerifyLogicalInterconnectGroups.verify_lig_exist,
                  'Logical Interconnects': VerifyLogicalInterconnects.verify_logical_interconnect_exist,
                  'Interconnects': VerifyInterconnects.verify_interconnect_exist}

    #    Scope category convert map
    get_category = {'Enclosures': 'enclosure',
                    'Server Hardware': 'server hardware',
                    'Ethernet Networks': 'ethernet network',
                    'Fibre Channel Networks': 'fibre channel network',
                    'FCoE Networks': 'fcoe network',
                    'Network Sets': 'network set',
                    'Logical Interconnect Groups': 'logical interconnect group',
                    'Logical Interconnects': 'logical interconnect',
                    'Interconnects': 'interconnect'
                    }

    for scope in scopes_obj:
        if hasattr(scope, 'resources'):
            resource_categories = []
            for n, resource in enumerate(scope.resources):
                if resource.category not in resource_categories:
                    resource_categories.append(resource.category)

            for category in resource_categories:
                navigate()
                CommonOperationScopes.select_scope(scope.name)
                CommonOperationScopes.click_resource_link(get_category.get(category))

                for n, resource in enumerate(scope.resources):
                    if category == resource.category:
                        categories.get(category)(resource.name, 20)

    return True


def delete_all_scopes():
    """ Remove All Scopes    """
    logger.info("Remove All Scopes")
    navigate()
    #    get the list of scopes
    if not CommonOperationScopes.wait_for_scopes_load():
        logger.info("There is no scopes")
        return True
    scopes = CommonOperationScopes.get_scope_list()
    for scope in scopes:
        if VerifyScopes.verify_scope_existed(scope, 5, False) is True:
            select_scope(scope)
            DeleteScopes.click_delete_scope_button()
            DeleteScopes.click_yes_delete_button()
            DeleteScopes.wait_delete_scope_dialog_close()
            #    VerifyScopes.verify_scope_deleted(scope)
            VerifyScopes.verify_scope_not_existed(scope)
    return True


def _Add_Resource_To_Scope(resource):
    """_Add_Resource_To_Scope
       Add resource to scope while editing the scope.
        Example:
        | _Add_Resource_To_Scope(Resource)"""

    if VerifyScopes.verify_edit_resource_existed(resource.name):
        logger.info("Resource %s is already added to the given scope" % resource.name)
        return False
    else:
        EditScopes.click_add_resources_button()
        EditScopes.wait_add_resources_dialog_open()
        EditScopes.input_and_select_resource_category(resource.category)
        EditScopes.input_resource_name(resource.name)
        EditScopes.click_resource_name(resource.name)
        EditScopes.click_add_button()
        EditScopes.wait_add_resources_dialog_close()
    return True


def _Add_Resource_To_Scope_Add(resource):
    """_Add_Resource_To_Scope_Add
      Add resource to scope while creating the scope.
        Example:
        | _Add_Resource_To_Scope_Add(Resource)"""

    if VerifyScopes.verify_add_resource_existed(resource.name):
        logger.info("Resource %s is already added to the given scope" % resource.name)
        return True
    else:
        CreateScopes.click_add_resources_button()
        CreateScopes.wait_add_resources_dialog_open()
        CreateScopes.input_and_select_resource_category(resource.category)
        CreateScopes.input_resource_name(resource.name)
        CreateScopes.click_resource_name(resource.name)
        CreateScopes.click_add_button()
        CreateScopes.wait_add_resources_dialog_close()
    return True


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


def validate_ligscopes_each_element():
    """ Navigate to Logical Interconnects Page """
    logger.info("validate_ligscopes")
    return CommonOperationScopes.verify_lig_scopes()


def validate_networkscopes_each_element():
    """ Navigate to Networks Page """
    logger.info("validate_Networkscopes")
    return CommonOperationScopes.verify_network_scopes()


def validate_networksetsscopes_each_element():
    """ Navigate to Networksets Page """
    logger.info("validate_networksetscopes")
    return CommonOperationScopes.verify_networkset_scopes()


def validate_enclosurescopes_each_element():
    """ Navigate to enclsoures Page """
    logger.info("validate_enclosurescopes")
    return CommonOperationScopes.verify_enclosure_scopes()


def validate_interconnectsscopes_each_element():
    """ Navigate to Interconnects Page """
    logger.info("validate_Interconnectscopes")
    return CommonOperationScopes.verify_interconnects_scopes()


def validate_liscopes_each_element():
    """ Navigate to LI Page """
    logger.info("validate_LogicalInterconnectscopes")
    return CommonOperationScopes.verify_li_scopes()


def validate_serverhwscopes_each_element():
    """ Navigate to SH Page """
    logger.info("validate_ServerHwScopes")
    return CommonOperationScopes.verify_serverhw_scopes()


def filter_by_scope(xpath_id, *scope_obj):
    """ Filters the resources by scope name
    """
    logger.info("Scope parameter for grouping ")
    if isinstance(scope_obj, test_data.DataObj):
        scope_obj = [scope_obj]
    elif isinstance(scope_obj, tuple):
        scope_obj = list(scope_obj[0])
    #    Looping to edit all the resourcs present in the resources.txt file
    for scope in scope_obj:
        logger.info("Filtering scope %s" % scope.name)
        CommonOperationScopes.verify_filter_by_scope(xpath_id, scope.name)

    return True


def filter_by_all_scope(xpath_id, *scope_obj):
    """ Filter the Resources by All Scopes
    :param scope_obj:
    :return:
    """
    logger.info("Scope parameter for grouping ")
    if isinstance(scope_obj, test_data.DataObj):
        scope_obj = [scope_obj]
    elif isinstance(scope_obj, tuple):
        scope_obj = list(scope_obj[0])

    for scope in scope_obj:
        logger.info("Filtering scope %s" % scope.name)
        logger.info("Filtering scope %s" % xpath_id)
        CommonOperationScopes.verify_filter_by_all_scope(xpath_id, scope.name)
    validate_resource_assigned_for_two_scopes(scope_obj)
    return True


def validate_resource_assigned_for_two_scopes(*scopes_obj):
    """ validate resource
        Example:
        | `validate resource assigned to scope`      | ${myScopeList}    |
    """

    logger.info("validate resource assigned to scope")

    if isinstance(scopes_obj, test_data.DataObj):
        scopes_obj = [scopes_obj]
    elif isinstance(scopes_obj, tuple):
        scopes_obj = list(scopes_obj[0])

    #    Scope category verify function map
    categories = {'Enclosures': VerifyEnclosures.verify_enclosure_exist,
                  'Server Hardware': VerifyHardware.verify_server_hardware_exist,
                  'Ethernet Networks': CommonOperationNetworks.verify_network_exist,
                  'Fibre Channel Networks': CommonOperationNetworks.verify_network_exist,
                  'FCoE Networks': CommonOperationNetworks.verify_network_exist,
                  'Network Sets': VerifyNetworkSets.verify_network_set_existed,
                  'Logical Interconnect Groups': VerifyLogicalInterconnectGroups.verify_lig_exist,
                  'Logical Interconnects': VerifyLogicalInterconnects.verify_logical_interconnect_exist,
                  'Interconnects': VerifyInterconnects.verify_interconnect_exist}

    #    Scope category convert map
    get_category = {'Enclosures': 'enclosure',
                    'Server Hardware': 'server hardware',
                    'Ethernet Networks': 'ethernet networks',
                    'Fibre Channel Networks': 'fibre channel networks',
                    'FCoE Networks': 'fcoe networks',
                    'Network Sets': 'network sets',
                    'Logical Interconnect Groups': 'logical interconnect groups',
                    'Logical Interconnects': 'logical interconnects',
                    'Interconnects': 'interconnects'
                    }

    for scope in scopes_obj:
        if hasattr(scope, 'resources'):
            resource_categories = []
            for n, resource in enumerate(scope.resources):
                if resource.category not in resource_categories:
                    resource_categories.append(resource.category)

            for category in resource_categories:
                logger.info("received categoryfor validation %s" % category)
                for n, resource in enumerate(scope.resources):
                    if category == resource.category:
                        logger.info("search for resource %s" % resource.name)
                        if not categories.get(category)(resource.name, 20):
                            logger.info("the required category of resources not found")
                            return False
    return True


def filter_by_any_scope(xpath_id, *scope_obj):
    """ Filter the Resources by All Scopes
    :param scope_obj:
    :Return:
    """
    logger.info("Scope parameter for grouping ")
    if isinstance(scope_obj, test_data.DataObj):
        scope_obj = [scope_obj]
    elif isinstance(scope_obj, tuple):
        scope_obj = list(scope_obj[0])

    #    Looping to edit all the resourcs present in the resources.txt file
    for scope in scope_obj:
        logger.info("Filtering scope %s" % scope.name)
        CommonOperationScopes.verify_filter_by_any_scope(xpath_id, scope.name)
    validate_resource_assigned_for_two_scopes(scope_obj)
    return True


def verify_is_on_scopes_page():
    if CommonOperationScopes.is_on_scopes_page() is True:
        return True
    else:
        return FusionUIBase.fail_test_or_return_false("Failed to find the required eleemnt")


def get_scope_name():
    return CommonOperationScopes.get_scope_name()


def get_scope_description():
    return CommonOperationScopes.get_scope_description()


def get_scope_count():
    return CommonOperationScopes.get_scope_count()


def verify_error_msg_for_duplicate_scope(*scopes_obj):

    logger.info("Create and verify Scope")
    navigate()
    if isinstance(scopes_obj, test_data.DataObj):
        scopes_obj = [scopes_obj]
    elif isinstance(scopes_obj, tuple):
        scopes_obj = list(scopes_obj[0])
    for scope in scopes_obj:
        have_resource = False
        CreateScopes.click_create_scope_button()
        logger.info("Creating scope %s" % scope.name)
        CreateScopes.wait_create_scope_dialog_open()
        CreateScopes.input_name(scope.name)
        if hasattr(scope, 'description'):
            CreateScopes.input_description(scope.description)
        if hasattr(scope, 'resources'):
            for resource in enumerate(scope.resources):
                have_resource = True
                _Add_Resource_To_Scope_Add(resource)
        CreateScopes.click_create_plus_button()

        validate_msg = CommonOperationScopes.get_scopename_validate_message()
        err_msg = CommonOperationScopes.get_scope_error_message()
        CreateScopes.click_cancel_button()
        CreateScopes.wait_create_scope_dialog_close()
        if validate_msg is not None:
            return validate_msg
        if err_msg is not None:
            return err_msg
        else:
            return FusionUIBase.fail_test_or_return_false("Failed to find the element")


def edit_verify_scope(*scope_obj):
    """ Edit Scope    """
    logger.info("Edit and Verify Scope")
    navigate()
    if isinstance(scope_obj, test_data.DataObj):
        scope_obj = [scope_obj]
    elif isinstance(scope_obj, tuple):
        scope_obj = list(scope_obj[0])
    fail_if_exist = 0
    #    Looping to edit all the resources present in the resources.txt file
    for scope in scope_obj:
        logger.info("Editing scope %s" % scope.name)
        if scope.has_property("new_name"):
            if scope.new_name != scope.name and VerifyScopes.verify_scope_existed(scope.new_name, 5, False):
                fail_if_exist += 1
                logger.warn("scope %s already exists, can't edit scope" % scope.new_name)
                continue
        #    Selecting the given scope
        if CommonOperationScopes.select_scope(scope.name):
            #    Clicking on edit button and verifying the edit options page
            CommonOperationScopes.wait_for_scopes_load()
            EditScopes.click_edit_scope_button()
            EditScopes.wait_edit_scope_dialog_open()
            if scope.has_property("new_name"):
                data = _Verify_Parameter(scope.new_name, "Scope Name")
                if not (data == "none" or data == ""):
                    EditScopes.input_name(data)
    EditScopes.click_ok_button()

    validate_msg = CommonOperationScopes.get_scopename_validate_message()
    EditScopes.click_cancel_button()
    EditScopes.wait_edit_scope_dialog_close()
    if validate_msg is None and fail_if_exist == 0:
        FusionUIBase.fail_test_or_return_false("Failed to find the required element")
    else:
        return validate_msg


def click_settings_link():
    """ Click Settings Link
        Example:
        | `Click Settings Link` |
    """
    CommonOperationScopes.click_settings_link()


def create_scope_boundary_check(correct_name, scopes_obj):
    """ Create Scope Boundary Check
        Example:
        | `Create Scope Boundary Check` | ${correct_name} | ${myScopeList} |
    """
    logger.info("Create Scope")
    navigate()
    if isinstance(scopes_obj, test_data.DataObj):
        scopes_obj = [scopes_obj]
    elif isinstance(scopes_obj, tuple):
        scopes_obj = list(scopes_obj[0])
    fail_if_exist = 0
    for scope in scopes_obj:
        if VerifyScopes.verify_scope_existed(scope.name, 5, False):
            fail_if_exist += 1
            logger.warn("scope %s already exists" % scope.name)
            continue
        have_resource = False
        CreateScopes.click_create_scope_button()
        logger.info("Creating scope %s" % scope.name)
        CreateScopes.wait_create_scope_dialog_open()
        CreateScopes.input_name(scope.name)
        if hasattr(scope, 'description'):
            CreateScopes.input_description(scope.description)
        if hasattr(scope, 'resources'):
            for resource in enumerate(scope.resources):
                have_resource = True
                _Add_Resource_To_Scope_Add(resource)
        CreateScopes.click_create_plus_button()
        VerifyScopes.verify_create_plus_complete()
        CreateScopes.click_cancel_button()
        CreateScopes.wait_create_scope_dialog_close()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(correct_name, 'Create', timeout=60, fail_if_false=True)
        if have_resource:
            FusionUIBase.wait_activity_action_ok(correct_name, 'Update Resource Assignments', timeout=160, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
        CommonOperationScopes.select_scope(correct_name)
        VerifyScopes.verify_scope_created(correct_name)
    if fail_if_exist > 0:
        return FusionUIBase.fail_test_or_return_false("failed to verify resources")
    return True


def validate_user_privilege():
    """ validate user  """
    logger.info("navigating scope")
    navigate()

    if VerifyScopes.verify_create_scope_button_not_exist(fail_if_false=False) is True:
        logger.info("user has no privilege to create scope")
        VerifyScopes.verify_user_authorizaton(fail_if_false=False)
        return True
    else:
        return FusionUIBase.fail_test_or_return_false("Unexpected behaviour")


def assign_scope_bulk_networks(*scope_obj):
    """ Edit Scope    """
    logger.info("Edit Scope")
    navigate()
    if isinstance(scope_obj, test_data.DataObj):
        scope_obj = [scope_obj]
    elif isinstance(scope_obj, tuple):
        scope_obj = list(scope_obj[0])
    fail_if_exist = 0
    #    Looping to edit all the resources present in the resources.txt file
    for scope in scope_obj:
        logger.info("Editing scope %s" % scope.name)
        if scope.has_property("new_name"):
            if scope.new_name != scope.name and VerifyScopes.verify_scope_existed(scope.new_name, 5, False):
                fail_if_exist += 1
                logger.warn("scope %s already exists, can't edit scope" % scope.new_name)
                continue

        #    Selecting the given scope
        if CommonOperationScopes.select_scope(scope.name):
            #    Clicking on edit button and verifying the edit options page
            CommonOperationScopes.wait_for_scopes_load()
            EditScopes.click_edit_scope_button()
            EditScopes.wait_edit_scope_dialog_open()
            EditScopes.click_add_resources_button()
            EditScopes.wait_add_resources_dialog_open()
            EditScopes.input_and_select_resource_category(scope.category)
            CommonOperationScopes.load_bulk_enets()
            EditScopes.click_add_button()
            EditScopes.wait_add_resources_dialog_close()
            EditScopes.click_ok_button()
            EditScopes.wait_edit_scope_dialog_close()
    if fail_if_exist > 0:
        return FusionUIBase.fail_test_or_return_false("Failed to assign bulk resource")
    return True


def get_appliance_state_for_scope():
    logger.info("verify Appliance State")
    return CommonOperationScopes.get_appliance_state_scope()


def get_scopes_list():
    logger.info("Getting all scopes list")
    navigate()
    return CommonOperationScopes.get_scope_list()


def validate_bulk_resource_list(*scope_obj):

    logger.info("get resources list by scope name")
    navigate()
    if CommonOperationScopes.wait_for_scope_bulk_assign(*scope_obj):
        navigate()
        resource = CommonOperationScopes.verify_bulk_resource(*scope_obj)
        resource_list = resource[0].split('\n')
        return resource_list
    else:
        FusionUIBase.fail_test_or_return_false("Failed to wait for assignment of resources")
