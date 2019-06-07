# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''
Created on Feb 17,2016

This file contains all element ID on Fusion AlertFIlter Page
'''


class NotificationElements(object):

    ID_NOTIFICATION = "xpath=.//*[@id='fs-settings-emailnotifications-panel']//a[@class='hp-anchor-uri']"
    ID_NOTIFICATION_TITLE = "xpath=//*[@id='hp-settings-details-title']"
    ID_BUTTON_NOTIFICATION_ACTIONS = "xpath=.//*[@id='hp-settings-actions']/label"
    ID_BUTTON_EDIT_NOTIFICATION = "xpath=.//*[@id='hp-edit-emailnotification']"
    ID_EDIT_NOTIFICATION_PAGE_TITLE = "xpath=//*[@id='hp-change-page-container']/section/header/h1/span"
    ID_INPUT_NOTIFICATION_SEND_TESTMAIL = "xpath=.//*[@id='hp-test-email']"
    ID_BUTTON_NOTIFICATION_SEND_MAIL = "xpath=.//*[@id='fs-test-email-submit']"
    ID_BUTTON_NOTIFICATION_CANCEL_MAIL = "xpath=.//*[@id='fs-test-email-cancel']"
    ID_INPUT_NOTIFICATION_SENDING_EMAIL = "xpath=//*[@id='cic-notification-emailedit-senderemail']"
    ID_TOGGLE_NOTIFICATION_ENABLE_ALTER_EMAIL = "//a[@id='cic-notification-alerts-enablebutton-hpToggle' and @class='hp-toggle']"
    ID_TOGGLE_ALERTS_ENABLED = "xpath=//*[@id='cic-notification-alerts-enablebutton-hpToggle']//li[@class='hp-on']"
    ID_TOGGLE_ALERT_EMAIL_FILTER = "xpath=//*[@id='cic-notification-addemail-enabled-hpToggle']/ol/li"
    ID_TOGGLE_ALERT_EMAIL_FILTER_ENABLED = "xpath=//*[@id='cic-notification-addemail-enabled-hpToggle']//li[@class='hp-on']"
    ID_TOGGLE_ALERT_EMAIL_FILTER_DISABLED = "xpath=//*[@id='cic-notification-addemail-enabled-hpToggle']//li[@class='hp-off']"
    ID_BUTTON_EMAIL_NOTIFICATION_ADD = "xpath=.//*[@id='cic-notification-emailedit-ok']"
    ID_BUTTON_EDIT_NOTIFICATION_CANCEL = "xpath=//*[@id='cic-notification-emailedit-cancel']"
    ID_CHECKBOX_SMTP = "xpath=.//*[@id='cic-notification-emailedit-smtpoptions']"
    ID_INPUT_SMTP_SERVER = "xpath=.//*[@id='cic-notification-emailedit-smtpserver-servername']"
    ID_INPUT_SMTP_PORT = "xpath=.//*[@id='cic-notification-emailedit-smtpserver-serverport']"


class CreateAlertFilterElements(object):

    ID_ALERT_PAGE_TITLE = "xpath=//*[@id='cic-notification-alert-header']"
    ID_BUTTON_ADD_ALERT_FILTER = "xpath=.//*[@id='cic-notification-alerts-addnotify-button']"
    ID_INPUT_ALERT_NAME = "xpath=.//*[@id='cic-notification-addemail-name']"
    ID_SELECT_ALERT_FILTER_RESOURCE_SCOPE = "xpath=.//*[@id='cic-notification-addemail-scope']//following::span[@class='hp-search-icon']"
    ID_BUTTON_SCOPE_NAME = "xpath=.//*[@id='cic-notification-addemail-scope']//span[contains(text(),'%s')]"
    ID_INPUT_ALERT_EMAIL_ADDRESS = "xpath=.//*[@id='cic-notification-addemail-emailaddresses']"
    ID_BUTTON_ADD_ALERT = "xpath=.//*[@id='cic-notification-alerts-add-button']"
    ID_TEXT_ALERT_EXISTING_NAME = "xpath=//label[contains(text(),'This name already exists.')]"
    ID_BUTTON_ALERT_FILTER_CANCEL = "xpath=//*[@id='cic-notification-alerts-cancel-button']"
    ID_NOTIFICATION_TABLE = "xpath=//table[@id='cic-notification-alerts-table']"
    ID_ALERT_LIST = "xpath=//*[@id='cic-notification-alerts-table']"
    ID_BUTTON_ALERT_FILTER_OK = "xpath=//*[@id='cic-notification-emailedit-ok']"
    ID_SELECT_GUIDED_STATE = "xpath=//div[@id='cic-notification-addemail-guided-div']//span[contains(text(),'%s')]"


class ChooseAlertCriteriaElements(object):
    ID_RADIO_ALERT_CRITERIA_PREDEFINED = "xpath=.//*[@id='cic-notification-addemail-pre-defined-radio']"
    ID_RADIO_ALERT_FILTER_GUIDED = "xpath=//*[@id='cic-notification-addemail-guided-radio']"
    ID_RADIO_ALERT_FILTER_ADVANCED = "xpath=//*[@id='cic-notification-addemail-advanced-radio']"
    ID_SELECT_ALERT_FILTER_PRE_ALERTS = "xpath=//li[@id='cic-notification-addemail-pre-defined-div']//div[contains(text(),'All alerts')]"
    ID_TEXT_ALERT_FILTER_GUIDED_ALERTS = "xpath=//*[@id='cic-notification-addemail-guided-div']//ul[@class='hp-tokens']"
    ID_SELECT_ALERT_FILTER_GUIDED = "xpath=.//*[@id='cic-notification-addemail-guided-div']//following::span[@class='hp-search-icon']"
    ID_TABLE_ALERT_FILTER_GUIDED_LIST_ADD = "//*[@id='cic-notification-addemail-guided-div']//following::span[@class='hp-name'][descendant::text()[contains(.,'Status:Disabled')]]"
    ID_TEXT_ALERT_FILTER_ADVANCED_ALERTS = "xpath=.//*[@id='cic-notification-addemail-advanced']"
    ID_BUTTON_ALERT_FILTER_PRE_ALERTS_SCROLL = "xpath=//li[@id='cic-notification-addemail-pre-defined-div']//span[contains(text(),'All critical or warning alerts')]"
    ID_TEXT_PRE_SELECTED = "xpath=.//*[@id='cic-notification-addemail-pre-defined-div']//div[contains(text(),'All critical or warning alerts')]"
    ID_SELECT_PREDEFINED_ALERTS = "xpath=//li[@id='cic-notification-addemail-pre-defined-div']//span[contains(text(),'%s')]"


class EditAlertFilterElements(object):
    ID_BTN_EDIT_ALERT_FILTER = "xpath=//table[@id='cic-notification-alerts-table']//tr[td[contains(text(),'%s')]]/td//div[@class='hp-edit']"
    ID_SELECT_ALERT_CRITERIA = "xpath=//div[@id='cic-notification-addemail-guided-div']//span[contains(text(),'%s')]"
    ID_RADIO_ALERT_FILTER_ADVANCED = "xpath=//*[@id='cic-notification-addemail-advanced-radio']"
    ID_INPUT_EDIT_ALERT_EMAIL_ADDRESS = "xpath=.//*[@id='cic-notification-addemail-emailaddresses']"
    ID_RADIO_ALERT_FILTER_GUIDED = "xpath=//*[@id='cic-notification-addemail-guided-radio']"
    ID_BTN_ALERT_FILTER_GUIDED = "xpath=.//*[@id='cic-notification-addemail-guided-div']//following::span[@class='hp-search-icon']"
    ID_BUTTON_OK_EDIT_FILTER = "xpath=.//*[@id='cic-notification-alerts-edit-ok-button']"
    ID_COMBO_RESOURCE_SCOPE = "xpath=.//*[@id='cic-notification-addemail-scope']//span[contains(text(),'%s')]"
    ID_BTN_ALERT_FILTER_RESOURCE_SCOPE = "xpath=.//*[@id='cic-notification-addemail-scope']//following::span[@class='hp-search-icon']"
    ID_TEXT_COMPLETED = "xpath=//div[@id='hp-page-notifications']//div[@class='hp-state']"
    ID_BUTTON_OK_EDIT_FILTER_NOTIFICATION = "xpath=.//*[@id='cic-notification-emailedit-ok']"
    ID_BTN_REMOVE_SCOPE = "xpath=//div[@id='cic-notification-addemail-scope']//li[span[contains(text(),'%s')]]/span[@class='hp-close']"
    ID_TEXT_SCOPES = "xpath=//div[@id='cic-notification-addemail-scope']//ul[@class='hp-tokens']"
    ID_TEXT_ALERT_CRITERIA = "xpath=.//*[@id='cic-notification-addemail-advanced']"


class DeleteAlerFiltertElements(object):
    ID_BTN_DELETE_ALERT_FILTER = "xpath=//table[@id='cic-notification-alerts-table']//tr[td[contains(text(),'%s')]]/td//div[@class='hp-close']"
    ID_BTN_OK_DELETE = "xpath=//*[@id='cic-notification-emailedit-ok']"
    ID_TABLE_ALERT_NAME = "xpath=//table[@id='cic-notification-alerts-table']//td[contains(text(),'%s')]"
