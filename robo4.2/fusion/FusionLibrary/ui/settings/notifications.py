# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''
Created on Mar 7,2016

This file contains all functions for notification Page
'''

from FusionLibrary.ui.general import base_page
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
from FusionLibrary.ui.business_logic.settings.notifications import GeneralNotification, CreateAlertNotificationFilter, VerifyAlertFilter, EditAlertFilter, DeleteALertFilter


def navigate():
    if GeneralNotification.is_notification_page() is False:
        FusionUIBase.navigate_to_section(SectionType.SETTINGS, time_for_loading=3)
        GeneralNotification.click_notification()


def create_alert_filter_with_predefined_criteria(*alert_obj):
    """ Create alert filter with alert criteria and Scope
    Arguments:
        name*       --  Name of alert as a string.
        email*      --  Email for sending the notification.
        scope*      --  Scope name.
        criteria*   --  Alert criteria is the alert state with which we can filter the alert.
    * Required Arguments

    Example:
        date/alerts-> @{TestData.alerts}
        <alertFilter_with_predefined_criteria>
        <alert name="Alert1" criteria="predefined" email="rooplekha.mukherji@hpe.com">
            <add_predefined_criteria>
                <criteria status="All critical or warning alerts"/>
            </add_predefined_criteria>
            <add_scope>
                <scope name="Scope 1"/>
            </add_scope>
        </alert>
        </alertFilter_with_predefined_criteria>
    """
    navigate()
    if isinstance(alert_obj, test_data.DataObj):
        alert_obj = [alert_obj]
    elif isinstance(alert_obj, tuple):
        alert_obj = list(alert_obj[0])
    fail_if_exist = 0
    for alert in alert_obj:
        if VerifyAlertFilter.verify_alert_exist_in_alert_table(alert.name, 5, False)is True:
            fail_if_exist += 1
            logger.warn("filter %s already exists" % alert.name)
            continue
        _navigate_to_add_alert_filter_page(alert.name, alert.email)
        CreateAlertNotificationFilter.click_predefined_allalerts()
        for n, criteria in enumerate(alert.add_predefined_criteria):
            CreateAlertNotificationFilter.select_predefined_criteria(criteria.status)
        CreateAlertNotificationFilter.click_scope_for_alert_filter()
        for n, scope in enumerate(alert.add_scope):
            CreateAlertNotificationFilter.click_scope_name(scope.name)
        CreateAlertNotificationFilter.click_scope_for_alert_filter()
        CreateAlertNotificationFilter.input_email_address_for_alert_filter(alert.email)
        CreateAlertNotificationFilter.click_add_alert_filter()
        CreateAlertNotificationFilter.click_ok_edit_notification()
        VerifyAlertFilter.verify_alert_is_created(alert.name, timeout=20)
    if fail_if_exist > 0:
        ui_lib.fail_test("not all of the filter(s) is successfully created - %s filter already exist " % fail_if_exist)
    return True


def validate_choose_alert_criteria(*alert_obj):
    """ Choose between the alert criteria Pre-defined to Guided to Advanced and validate
        that the same alert criteria is displayed across.
    """
    navigate()
    if isinstance(alert_obj, test_data.DataObj):
        alert_obj = [alert_obj]
    elif isinstance(alert_obj, tuple):
        alert_obj = list(alert_obj[0])

    for alert in alert_obj:
        _navigate_to_add_alert_filter_page(alert.name, alert.email)
        CreateAlertNotificationFilter.click_predefined_criteria_for_alert_filter()
        CreateAlertNotificationFilter.click_predefined_allalerts()
        CreateAlertNotificationFilter.click_predefined_from_list()
        VerifyAlertFilter.verify_predefined_criteria_is_displayed()
        CreateAlertNotificationFilter.click_guided_criteria_for_alert_filter()
        VerifyAlertFilter.verify_guided_criteria_displayed()

        if CreateAlertNotificationFilter.get_predefined_criteria_selected() in CreateAlertNotificationFilter.get_guided_criteria_selected():
            logger.info("Predefined and guided alert criteria has same values")
        else:
            ui_lib.fail_test("Pre-defined guided values differ")
        CreateAlertNotificationFilter.click_guided_criteria_drop_down()
        CreateAlertNotificationFilter.click_guided_criteria_from_list()
        VerifyAlertFilter.verify_guided_criteria_displayed()
        CreateAlertNotificationFilter.click_advanced_criteria_for_alert_filter()
        newtext = CreateAlertNotificationFilter.get_guided_criteria_selected().split()
        word = " "
        for x in newtext:
            word = word + " " + x

        advancedtext = word.strip(" ")
        if advancedtext.lower() in CreateAlertNotificationFilter.get_advanced_criteria_displayed():
            logger.info("Alert is displayed as a query")
        else:
            ui_lib.fail_test("Pre-defined guided values differ")
        CreateAlertNotificationFilter.click_cancel_edit_alert_filter()
        CreateAlertNotificationFilter.click_cancel_edit_notification()
    return True


def edit_alert_filter(*alert_obj):
    """ Edit Alert filter by adding/removing  alert criteria ,scope, email address.
        Validating that in edit filter default alert criteria is Advanced.

        Arguments:
        name*       --  Name of alert as a string.
        email*      --  Email for sending the notification.
        scope*      --  Scope name.
        criteria*   --  Alert criteria is the alert state with which we can filter the alert.
        * Required Arguments
        Examples:
        <edit_alertFilter>
        <alert name="Alert1">
            <add_alertcriteria>
                <alertcriteria state="status:ok"/>
                <alertcriteria state="status:unknown"/>
            </add_alertcriteria>
            <add_scope>
                <scope name="Scope 2"/>
            </add_scope>
            <add_email>
                <email address="neha@hpe.com"/>
            </add_email>
        </alert>
    </edit_alertFilter>
    """
    navigate()
    if isinstance(alert_obj, test_data.DataObj):
        alert_obj = [alert_obj]
    elif isinstance(alert_obj, tuple):
        alert_obj = list(alert_obj[0])
    total = len(alert_obj)
    not_exists = 0
    edited = 0
    for alert in alert_obj:
        if VerifyAlertFilter.verify_alert_exist_in_alert_table(alert.name, 5, False)is True:
            logger.debug("Edit Alert filter by adding new scope and Alert Criteria for %s ..." % alert.name)
            EditAlertFilter.click_edit_alert_filter(alert.name, timeout=10)
            VerifyAlertFilter.verify_advanced_radio_selected_by_default()
            if hasattr(alert, 'remove_alertcriteria'):
                for n, alertcriteria in enumerate(alert.remove_alertcriteria):
                    if alertcriteria.status in EditAlertFilter.get_alert_criteria_displayed():
                        new_status = EditAlertFilter.get_alert_criteria_displayed().replace(alertcriteria.status, "")
                        EditAlertFilter.input_new_alert_criteria(new_status)
                    else:
                        logger.warn("Given alert criteria was not added earlier to the alert filter")
            if hasattr(alert, 'add_alertcriteria'):
                for n, alertcriteria in enumerate(alert.add_alertcriteria):
                    if alertcriteria.state in EditAlertFilter.get_alert_criteria_displayed():
                        logger.warn("Alert state is already exist in filter")
                    else:
                        new_status = EditAlertFilter.get_alert_criteria_displayed() + " " + alertcriteria.state
                        EditAlertFilter.input_new_alert_criteria(new_status)
            if hasattr(alert, 'remove_scope'):
                for n, scope in enumerate(alert.remove_scope):
                    if scope.name in EditAlertFilter.get_scopes_added():
                        EditAlertFilter.click_to_remove_scope(scope.name)
                        EditAlertFilter.click_to_scope_for_edit_filter()
                    else:
                        logger.warn("Scope does not exist in filter")
            if hasattr(alert, 'add_scope'):
                EditAlertFilter.click_to_scope_for_edit_filter()
                for n, scope in enumerate(alert.add_scope):
                    EditAlertFilter.input_and_select_scope(scope.name)
                    EditAlertFilter.click_to_scope_for_edit_filter()
            if hasattr(alert, 'replace_email'):
                previous_email = ""
                for n, email in enumerate(alert.replace_email):
                    text = previous_email + "\n" + email.address
                    EditAlertFilter.input_email_addres_edit_alert(text)
                    previous_email = EditAlertFilter.get_email_address()
            if hasattr(alert, 'add_email'):
                for n, email in enumerate(alert.add_email):
                    if email.address in EditAlertFilter.get_email_address():
                        logger.warn("email address already added")
                    else:
                        previous_email = EditAlertFilter.get_email_address()
                        text = previous_email + "\n" + email.address
                        EditAlertFilter.input_email_addres_edit_alert(text)
            EditAlertFilter.click_ok_edit_alert_filter()
            EditAlertFilter.click_ok_edit_filter_notification()
            VerifyAlertFilter.verify_update_notification_completed(timeout=20)
            FusionUIBase.show_activity_sidebar()
            FusionUIBase.wait_activity_action_ok("", 'Update notifications', timeout=60, fail_if_false=True)
            FusionUIBase.show_activity_sidebar()
            edited += 1
        else:
            logger.warn("Alert Filter '%s' does NOT exist! ..." % alert.name)
            not_exists += 1
            continue
    if total - not_exists == 0:
        logger.warn("no alert filter to edited! all filter(s) is NOT existing")
        return False
    else:
        if edited < total:
            logger.warn("not all of the filter(s) is successfully edited - %s out of %s edited " % (edited, total))
            return False
    logger.info("all of the alert filter(s) is successfully edited - %s out of %s " % (edited, total))
    return True


def create_alert_filter_with_guided_criteria(*alert_obj):
    """ Create Alert Filter with alert criteria selected from Guided Criteria
    """
    navigate()
    if isinstance(alert_obj, test_data.DataObj):
        alert_obj = [alert_obj]
    elif isinstance(alert_obj, tuple):
        alert_obj = list(alert_obj[0])
    fail_if_exist = 0
    for alert in alert_obj:
        if VerifyAlertFilter.verify_alert_exist_in_alert_table(alert.name, 5, False)is True:
            fail_if_exist += 1
            logger.warn("filter %s already exists" % alert.name)
            continue
        _navigate_to_add_alert_filter_page(alert.name, alert.email)
        CreateAlertNotificationFilter.click_guided_criteria_for_alert_filter()
        CreateAlertNotificationFilter.click_guided_criteria_drop_down()
        for n, criteria in enumerate(alert.add_guided_criteria):
            CreateAlertNotificationFilter.select_alert_criteria(criteria.status)
        CreateAlertNotificationFilter.click_guided_criteria_drop_down()
        CreateAlertNotificationFilter.click_scope_for_alert_filter()
        for n, scope in enumerate(alert.add_scope):
            CreateAlertNotificationFilter.click_scope_name(scope.name)
            CreateAlertNotificationFilter.click_scope_for_alert_filter()
        CreateAlertNotificationFilter.input_email_address_for_alert_filter(alert.email)
        CreateAlertNotificationFilter.click_add_alert_filter()
        CreateAlertNotificationFilter.click_ok_edit_notification()
        VerifyAlertFilter.verify_update_notification_completed(timeout=15)
        VerifyAlertFilter.verify_alert_is_created(alert.name, timeout=15)
    if fail_if_exist > 0:
        ui_lib.fail_test("not all of the filter(s) is successfully created - %s filter already exist " % fail_if_exist)
    return True


def create_alert_filter_with_advanced_criteria(*alert_obj):
    """ Creating Alert Filter by adding alert criteria under Advanced criteria
    """
    navigate()
    if isinstance(alert_obj, test_data.DataObj):
        alert_obj = [alert_obj]
    elif isinstance(alert_obj, tuple):
        alert_obj = list(alert_obj[0])
    fail_if_exist = 0
    for alert in alert_obj:
        if VerifyAlertFilter.verify_alert_exist_in_alert_table(alert.name, 5, False)is True:
            fail_if_exist += 1
            logger.warn("filter %s already exists" % alert.name)
            continue
        _navigate_to_add_alert_filter_page(alert.name, alert.email)
        CreateAlertNotificationFilter.click_advanced_criteria_for_alert_filter()
        for n, criteria in enumerate(alert.add_advanced_criteria):
            alertstatus = CreateAlertNotificationFilter.get_advanced_criteria_displayed() + " " + "status:" + criteria.status
            CreateAlertNotificationFilter.input_advanced_criteria(alertstatus)
        CreateAlertNotificationFilter.click_scope_for_alert_filter()
        for n, scope in enumerate(alert.add_scope):
            CreateAlertNotificationFilter.click_scope_name(scope.name)
        CreateAlertNotificationFilter.click_scope_for_alert_filter()
        CreateAlertNotificationFilter.input_email_address_for_alert_filter(alert.email)
        CreateAlertNotificationFilter.click_add_alert_filter()
        CreateAlertNotificationFilter.click_ok_edit_notification()
        VerifyAlertFilter.verify_update_notification_completed(timeout=15)
        VerifyAlertFilter.verify_alert_is_created(alert.name, timeout=15)
    if fail_if_exist > 0:
        ui_lib.fail_test("not all of the filter(s) is successfully created - %s filter already exist " % fail_if_exist)
    return True


def delete_alert_filter(*alert_obj):
    """ Deleting the Alert Filters created
    """
    navigate()
    if isinstance(alert_obj, test_data.DataObj):
        alert_obj = [alert_obj]
    elif isinstance(alert_obj, tuple):
        alert_obj = list(alert_obj[0])
    total = len(alert_obj)
    not_exists = 0
    deleted = 0
    for alert in alert_obj:
        if VerifyAlertFilter.verify_alert_exist_in_alert_table(alert.name, 5, False)is True:
            DeleteALertFilter.click_action_menu_delete()
            DeleteALertFilter.click_delete_alert_filter(alert.name)
            DeleteALertFilter.click_ok_delete_filter()
            VerifyAlertFilter.verify_alert_filter_is_deleted(alert.name)
            deleted += 1
        else:
            logger.warn("Alert Filter '%s' does NOT exist! ..." % alert.name)
            not_exists += 1
            continue
    if total - not_exists == 0:
        logger.warn("no alert filter to delete! all filter(s) is NOT existing")
        return False
    elif deleted < total:
        logger.warn("not all of the alert filter(s) is successfully deleted - %s out of %s deleted " % (deleted, total))
        return False
    logger.info("all of the alert filter(s) is successfully deleted - %s out of %s " % (deleted, total))
    return True


def _navigate_to_add_alert_filter_page(alert, email):
    """ Navigate to ALert filter creation page
    """
    GeneralNotification.click_notification_action()
    GeneralNotification.click_edit_notification()
    GeneralNotification.input_sender_email(email)
    if CreateAlertNotificationFilter.wait_disable_to_visible():
        CreateAlertNotificationFilter.click_enable_edit_notification_page()
    CreateAlertNotificationFilter.click_add_alert_email_filter()
    CreateAlertNotificationFilter.input_alert_name(alert)
    if not CreateAlertNotificationFilter.wait_enable_visible_alert_page():
        CreateAlertNotificationFilter.click_enable_alert_page()
