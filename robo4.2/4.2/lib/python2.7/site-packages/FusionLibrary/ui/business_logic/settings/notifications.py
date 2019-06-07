'''
   Alert-Notification Functions
'''


from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase,\
    ClassMethodType
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.data import test_data
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.settings.notifications_elements import NotificationElements, CreateAlertFilterElements, ChooseAlertCriteriaElements, EditAlertFilterElements, DeleteAlerFiltertElements


class GeneralNotification(object):

    @classmethod
    def click_notification(cls, timeout=5):
        logger.debug("Click [ Notification title ]")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_NOTIFICATION, timeout, fail_if_false=True)

    @classmethod
    def is_notification_page(cls, timeout=5):
        logger.debug("Determine if current page is Notification")
        return ui_lib.wait_for_element_visible(NotificationElements.ID_NOTIFICATION_TITLE, timeout, fail_if_false=False)

    @classmethod
    def click_notification_action(cls, timeout=5):
        logger.debug("Click action")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_BUTTON_NOTIFICATION_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    def click_edit_notification(cls, timeout=5):
        logger.debug("Click edit notification")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_BUTTON_EDIT_NOTIFICATION, timeout, fail_if_false=True)

    @classmethod
    def get_edit_notification_page_title(cls, timeout=5):
        logger.debug("get the page title of edit notification page")
        return ui_lib.get_text(NotificationElements.ID_EDIT_NOTIFICATION_PAGE_TITLE, timeout, fail_if_false=True)

    @classmethod
    def input_sender_email(cls, email_address, timeout=5):
        logger.debug("Enter Sender email")
        ui_lib.wait_for_element_and_input_text(NotificationElements.ID_INPUT_NOTIFICATION_SENDING_EMAIL, email_address, timeout, fail_if_false=True)


class CreateAlertNotificationFilter(object):

    @classmethod
    def click_add_alert_email_filter(cls, timeout=5):
        logger.debug("Click action")
        ui_lib.wait_for_element_and_click(CreateAlertFilterElements.ID_BUTTON_ADD_ALERT_FILTER, timeout, fail_if_false=True)

    @classmethod
    def get_alert_filter_page_title(cls, timeout=5):
        logger.debug("get alert filter page title")
        return ui_lib.get_text(CreateAlertFilterElements.ID_ALERT_PAGE_TITLE, fail_if_false=True)

    @classmethod
    def input_alert_name(cls, alert_name, timeout=5):
        logger.debug("Enter alert name")
        ui_lib.wait_for_element_and_input_text(CreateAlertFilterElements.ID_INPUT_ALERT_NAME, alert_name, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_disable_to_visible(cls, timeout=5):
        logger.debug("wait and check if disable is there")
        return ui_lib.is_visible(NotificationElements.ID_TOGGLE_NOTIFICATION_ENABLE_ALTER_EMAIL, timeout, fail_if_false=True)

    @classmethod
    def click_enable_edit_notification_page(cls, timeout=5):
        logger.debug("click enable")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_TOGGLE_NOTIFICATION_ENABLE_ALTER_EMAIL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_enable_visible_alert_page(cls, timeout=5):
        logger.debug("wait if enable is displayed")
        return ui_lib.is_visible(NotificationElements.ID_TOGGLE_ALERT_EMAIL_FILTER, timeout, fail_if_false=True)

    @classmethod
    def click_enable_alert_page(cls, timeout=5):
        logger.debug("click enable")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_TOGGLE_ALERT_EMAIL_FILTER_ENABLED, timeout, fail_if_false=True)

    @classmethod
    def click_scope_for_alert_filter(cls, timeout=5):
        logger.debug("Scope drop down list")
        ui_lib.wait_for_element_and_click(CreateAlertFilterElements.ID_SELECT_ALERT_FILTER_RESOURCE_SCOPE, timeout, fail_if_false=True)

    @classmethod
    def click_scope_name(cls, scope, timeout=5):
        logger.debug("select the scope from list")
        ui_lib.wait_for_element_and_click(CreateAlertFilterElements.ID_BUTTON_SCOPE_NAME % scope, timeout, fail_if_false=True)

    @classmethod
    def input_email_address_for_alert_filter(cls, email_address, timeout=5):
        logger.debug("Enter the email to send the alert notification")
        ui_lib.wait_for_element_and_input_text(CreateAlertFilterElements.ID_INPUT_ALERT_EMAIL_ADDRESS, email_address, timeout, fail_if_false=True)

    @classmethod
    def click_add_alert_filter(cls, timeout=5):
        logger.debug("Click add to add filter")
        ui_lib.wait_for_element_and_click(CreateAlertFilterElements.ID_BUTTON_ADD_ALERT, timeout, fail_if_false=True)

    @classmethod
    def click_ok_edit_notification(cls, timeout=5):
        logger.debug("Click ok in edit notification page")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_BUTTON_EMAIL_NOTIFICATION_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_predefined_criteria_for_alert_filter(cls, timeout=5):
        logger.debug("Select predefined alert criteria")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_RADIO_ALERT_CRITERIA_PREDEFINED, timeout=5, fail_if_false=True)

    @classmethod
    def select_predefined_criteria(cls, criteria, timeout=5):
        logger.debug("Select predefined criteria as per user")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_SELECT_PREDEFINED_ALERTS % criteria, timeout, fail_if_false=True)

    @classmethod
    def click_predefined_allalerts(cls, timeout=5):
        logger.debug("select predefined all alert")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_SELECT_ALERT_FILTER_PRE_ALERTS, timeout, fail_if_false=True)

    @classmethod
    def click_predefined_from_list(cls, timeout=5):
        logger.debug("select predefined alert from list")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_BUTTON_ALERT_FILTER_PRE_ALERTS_SCROLL, timeout, fail_if_false=True)

    @classmethod
    def get_predefined_criteria_selected(cls, timeout=5):
        logger.debug("get the list of predefined criteria selected")
        return ui_lib.get_text(ChooseAlertCriteriaElements.ID_TEXT_PRE_SELECTED, timeout, fail_if_false=True)

    @classmethod
    def click_guided_criteria_for_alert_filter(cls, timeout=5):
        logger.debug("Select guided alert criteria")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_RADIO_ALERT_FILTER_GUIDED, timeout, fail_if_false=True)

    @classmethod
    def get_guided_criteria_selected(cls, timeout=5):
        logger.debug("get the list of guided criteria selected")
        return ui_lib.get_text(ChooseAlertCriteriaElements.ID_TEXT_ALERT_FILTER_GUIDED_ALERTS, timeout, fail_if_false=True)

    @classmethod
    def click_advanced_criteria_for_alert_filter(cls, timeout=5):
        logger.debug("Select advanced alert criteria")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_RADIO_ALERT_FILTER_ADVANCED, timeout, fail_if_false=True)

    @classmethod
    def get_advanced_criteria_displayed(cls, timeout=5):
        logger.debug("get the list of advanced criteria displayed")
        return ui_lib.get_webelement_attribute("value", ChooseAlertCriteriaElements.ID_TEXT_ALERT_FILTER_ADVANCED_ALERTS, timeout)

    @classmethod
    def click_guided_criteria_drop_down(cls, timeout=5):
        logger.debug("Edit guided alert criteria")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_SELECT_ALERT_FILTER_GUIDED, timeout, fail_if_false=True)

    @classmethod
    def click_guided_criteria_from_list(cls, timeout=5):
        logger.debug("add new guided alert criteria")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_TABLE_ALERT_FILTER_GUIDED_LIST_ADD, timeout, fail_if_false=True)

    @classmethod
    def select_alert_criteria(cls, state, timeout=5):
        logger.debug("Select the alert criteria from the list")
        ui_lib.wait_for_element_and_click(CreateAlertFilterElements.ID_SELECT_GUIDED_STATE % state, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_edit_alert_filter(cls, timeout=5):
        logger.debug("Cancel edit alert filter")
        ui_lib.wait_for_element_and_click(CreateAlertFilterElements.ID_BUTTON_ALERT_FILTER_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_edit_notification(cls, timeout=5):
        logger.debug("cancel edit notification")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_BUTTON_EDIT_NOTIFICATION_CANCEL, timeout, fail_if_false=True)

    @classmethod
    def input_advanced_criteria(cls, status, timeout=5):
        logger.debug("Enter the alert status for filter under Advanced Criteria")
        ui_lib.wait_for_element_and_input_text(ChooseAlertCriteriaElements.ID_TEXT_ALERT_FILTER_ADVANCED_ALERTS, status, timeout, fail_if_false=True)


class EditAlertFilter(object):

    @classmethod
    def click_edit_alert_filter(cls, alert, timeout=5):
        logger.debug("Edit alert filter created")
        ui_lib.wait_for_element_and_click(EditAlertFilterElements.ID_BTN_EDIT_ALERT_FILTER % alert, timeout, fail_if_false=True)

    @classmethod
    def get_alert_criteria_displayed(cls, timeout=5):
        logger.debug("get the displayed alert criteria")
        return ui_lib.get_webelement_attribute("value", EditAlertFilterElements.ID_TEXT_ALERT_CRITERIA, timeout, fail_if_false=True)

    @classmethod
    def input_new_alert_criteria(cls, criteria, timeout=5):
        logger.debug("Enter the updated alert states for filter")
        ui_lib.wait_for_element_and_input_text(EditAlertFilterElements.ID_TEXT_ALERT_CRITERIA, criteria, timeout, fail_if_false=True)

    @classmethod
    def get_email_address(cls, timeout=5):
        logger.debug("get the previous email address")
        return ui_lib.get_webelement_attribute("value", EditAlertFilterElements.ID_INPUT_EDIT_ALERT_EMAIL_ADDRESS, timeout, fail_if_false=True)

    @classmethod
    def input_email_addres_edit_alert(cls, email, timeout=5):
        logger.debug("add one more email added for the alert receiver '%s'" % email)
        ui_lib.wait_for_element_and_input_text(EditAlertFilterElements.ID_INPUT_EDIT_ALERT_EMAIL_ADDRESS, email, timeout, fail_if_false=True)

    @classmethod
    def click_ok_edit_alert_filter(cls, timeout=5):
        logger.debug("Click Ok for edit alert filter")
        ui_lib.wait_for_element_and_click(EditAlertFilterElements.ID_BUTTON_OK_EDIT_FILTER, timeout, fail_if_false=True)

    @classmethod
    def get_scopes_added(cls, timeout=5):
        logger.debug("get the scopes already added to the alert filter")
        return ui_lib.get_text(EditAlertFilterElements.ID_TEXT_SCOPES, timeout, fail_if_false=True)

    @classmethod
    def click_to_scope_for_edit_filter(cls, timeout=5):
        logger.debug("Scope drop down list")
        ui_lib.wait_for_element_and_click(EditAlertFilterElements.ID_BTN_ALERT_FILTER_RESOURCE_SCOPE, timeout, fail_if_false=True)

    @classmethod
    def input_and_select_scope(cls, scope, timeout=5):
        logger.debug("select the scope from list")
        ui_lib.wait_for_element_and_click(EditAlertFilterElements.ID_COMBO_RESOURCE_SCOPE % scope, timeout, fail_if_false=True)

    @classmethod
    def click_to_remove_scope(cls, scope, timeout=5):
        logger.debug("Remove the Scope")
        ui_lib.wait_for_element_and_click(EditAlertFilterElements.ID_BTN_REMOVE_SCOPE % scope, timeout, fail_if_false=True)

    @classmethod
    def click_ok_edit_filter_notification(cls, timeout=5):
        logger.debug("click Ok to update the edit changes")
        ui_lib.wait_for_element_and_click(EditAlertFilterElements.ID_BUTTON_OK_EDIT_FILTER_NOTIFICATION, timeout, fail_if_false=True)


class DeleteALertFilter(object):

    @classmethod
    def click_action_menu_delete(cls, timeout=5):
        logger.debug("Navigate to Delete alert Page")
        ui_lib.wait_for_element_and_click(NotificationElements.ID_BUTTON_NOTIFICATION_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(NotificationElements.ID_BUTTON_EDIT_NOTIFICATION, timeout, fail_if_false=True)

    @classmethod
    def click_delete_alert_filter(cls, alert, timeout=5):
        logger.debug("Delete the alert Filter")
        ui_lib.wait_for_element_and_click(DeleteAlerFiltertElements.ID_BTN_DELETE_ALERT_FILTER % alert, timeout, fail_if_false=True)

    @classmethod
    def click_ok_delete_filter(cls, timeout=5):
        logger.debug("click Ok to update the delete filter")
        ui_lib.wait_for_element_and_click(DeleteAlerFiltertElements.ID_BTN_OK_DELETE, timeout, fail_if_false=True)


class VerifyAlertFilter(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def check_if_alert_name_exists_for_alert_filter(cls, timeout=5, fail_if_false=True):
        logger.debug("Validate if the alert name already exist")
        ui_lib.wait_for_element_and_click(ChooseAlertCriteriaElements.ID_RADIO_ALERT_CRITERIA_PREDEFINED, timeout, fail_if_false)
        if ui_lib.wait_for_element_notvisible(CreateAlertFilterElements.ID_TEXT_ALERT_EXISTING_NAME, timeout, fail_if_false):
            return True
        else:
            logger.warn("Alert name already exist please use a new name")
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_alert_is_created(cls, alert_name, timeout=5, fail_if_false=True):
        logger.debug("validating if alert is created")
        if not ui_lib.wait_for_table_to_contain(CreateAlertFilterElements.ID_NOTIFICATION_TABLE, alert_name, timeout, fail_if_false):
            ui_lib.fail_test("The alert is not created")
        logger.debug("the alert is created ")
        return True

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_predefined_criteria_is_displayed(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify that pre-defined criteria is displayed")
        return ui_lib.wait_for_element_visible(ChooseAlertCriteriaElements.ID_TEXT_PRE_SELECTED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_guided_criteria_displayed(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify that  guided criteria is displayed")
        return ui_lib.wait_for_element_visible(ChooseAlertCriteriaElements.ID_TEXT_ALERT_FILTER_GUIDED_ALERTS, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_advanced_radio_selected_by_default(cls, timeout=5, fail_if_false=True):
        logger.debug("Verify that advanced criteria is selected by default in edit alert filter page")
        return ui_lib.get_webelement_attribute("checked", EditAlertFilterElements.ID_RADIO_ALERT_FILTER_ADVANCED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_update_notification_completed(cls, timeout=5, fail_if_false=True):
        logger.debug("verify that update notification task is competed")
        return ui_lib.wait_for_element_visible(EditAlertFilterElements.ID_TEXT_COMPLETED, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_alert_filter_is_deleted(cls, alert, timeout=5, fail_if_false=True):
        logger.debug("Verify that alert filter is deleted and is not listed in Notification page")
        return ui_lib.wait_for_element_notvisible(DeleteAlerFiltertElements.ID_TABLE_ALERT_NAME % alert, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_alert_exist_in_alert_table(cls, alert, timeout=5, fail_if_false=True):
        logger.debug("Verify that alert %s ...exist in alert table" % alert)
        return ui_lib.wait_for_element(DeleteAlerFiltertElements.ID_TABLE_ALERT_NAME % alert, timeout, fail_if_false)
