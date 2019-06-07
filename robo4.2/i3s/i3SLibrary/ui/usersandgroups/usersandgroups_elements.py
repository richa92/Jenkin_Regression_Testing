# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
'''

This file contains all element ID on i3S Users and Groups page/screen
'''


class UserRoles:
    FULL = 'Full'
    READONLY = 'Read only'
    SERVERADMIN = 'Server administrator'
    NETWORKADMIN = 'Network administrator'
    BACKUPADMIN = 'Backup administrator'
    STORAGEADMIN = 'Storage administrator'


class i3SUserandGroupsPage(object):
    ID_PAGE_LABEL = "//div[@class='hp-page-label']/h1[text()='Users and Groups']"
    ID_LINK_ADD_USER = "link=Add user"
    ID_ELEMENT_USERNAME_BASE = "xpath=//td[@class='' and text()='%s']"  # Replace %s with username
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1[text()='Users and Groups']"

    # Users Table
    ID_USERS_TABLE = "xpath=//table[@id='fs-users-table']"
    ID_USERS_TABLE_NAME_COLUMN = 1
    ID_ALL_USERNAME_LIST = '{0}//tr/td[{1}]'.format(ID_USERS_TABLE, ID_USERS_TABLE_NAME_COLUMN)

    # Action Menu
    ID_MENU_ACTION_MAIN_BTN = "xpath=//label[text()='Actions']"
    ID_MENU_ACTION_ADD = "link=Add"
    ID_MENU_ACTION_EDIT_USER = "link=Edit"
    ID_MENU_ACTION_REMOVE_USER = "id=cic-user-remove-action"

    # Add user
    ID_INPUT_USER_LOGIN_NAME = "id=fs-user-loginname"
    ID_INPUT_USER_FULL_NAME = "id=fs-user-fullname"
    ID_INPUT_USER_INITIAL_PASSWORD = "id=fs-user-initialpasswd"
    ID_INPUT_USER_CONFIRM_PASSWORD = "id=fs-user-confirmpasswd"
    ID_RADIO_ROLE_SPECIALIZED = "id=fs-user-role-name-specialized"
    ID_RADIO_ROLE_FULL = "id=fs-user-role-name-full"
    ID_RADIO_ROLE_READ_ONLY = "id=fs-user-role-name-readonly"
    ID_INPUT_USER_EMAIL = "id=fs-user-email"
    ID_INPUT_USER_OFFICE_PHONE = "id=fs-user-officephone"
    ID_INPUT_USER_MOBILE_PHONE = "id=fs-user-mobilephone"
    ID_BTN_USER_ADD = "id=fs-user-add"
    ID_BTN_USER_ADD_PLUS = "id=fs-user-add-again"
    ID_BTN_USER_ADD_CANCEL = "id=fs-user-add-cancel"
    ID_CHECKBOX_BACKUP_ADMINISTRATOR = "id=fs-user-role-0"
    ID_CHECKBOX_NETWORK_ADMINISTRATOR = "id=fs-user-role-1"
    ID_CHECKBOX_SERVER_ADMINISTRATOR = "id=fs-user-role-2"
    ID_CHECKBOX_STORAGE_ADMINISTRATOR = "id=fs-user-role-3"
    ID_CREATE_USER_DIALOG_FORM_MESSAGE = "hp-form-message"
    ID_CREATE_USER_MESSAGE_TEXT = "xpath=//span[@class='hp-form-message-text']"
    ID_CREATE_USER_FIELD_ERROR = "xpath=//label[@class='hp-error']"

    # EDIT USER
    ID_INPUT_EDIT_LOGIN_NAME = "id=fs-user-edit-loginname"
    ID_INPUT_EDIT_CURRENTPWD = "id=fs-usersettings-currentpasswd"
    ID_INPUT_EDIT_FULL_NAME = "xpath=//*[@id='fs-user-edit-fullname']"
    ID_INPUT_EDIT_INITIAL_PASSWORD = "id=fs-user-edit-newpasswd"
    ID_INPUT_EDIT_CONFIRM_PASSWORD = "id=fs-user-edit-confirmpasswd"
    ID_RADIO_EDIT_ROLE_SPECIALIZED = "id=fs-edit-user-role-name-specialized"
    ID_RADIO_EDIT_ROLE_FULL = "id=fs-edit-user-role-name-full"
    ID_RADIO_EDIT_ROLE_READ_ONLY = "id=fs-edit-user-role-name-readonly"
    ID_INPUT_EDIT_EMAIL = "id=fs-user-edit-email"
    ID_INPUT_EDIT_OFFICE_PHONE = "id=fs-user-edit-officephone"
    ID_INPUT_EDIT_MOBILE_PHONE = "id=fs-user-edit-mobilephone"
    ID_CHECKBOX_EDIT_BACKUP_ADMINISTRATOR = "xpath=//*[@id='fs-user-edit-role-0']"
    ID_CHECKBOX_EDIT_NETWORK_ADMINISTRATOR = "id=fs-user-edit-role-1"
    ID_CHECKBOX_EDIT_SERVER_ADMINISTRATOR = "id=fs-user-edit-role-2"
    ID_BTN_EDIT_OK = "id=fs-user-edit"
    ID_BTN_EDIT_CANCEL = "id=fs-user-edit-cancel"
    ID_TILE_USER_DETAILS = "id=cic-user-details-title"

    # Delete User
    ID_CONFIRM_REMOVE_DIALOG_PROMPT = "xpath=//div[@class='hp-dialog']//div[@class='hp-prompt']"
    ID_CONFIRM_REMOVE_DIALOG_TITLE = "//div[@class='hp-dialog']/header/h1"
    ID_BTN_YES_CONFIRM_REMOVE = "xpath=//button[text()='Yes, remove']"
    ID_BTN_CANCEL_CONFIRM_REMOVE = "css=button.hp-cancel"

    # Unauthorized dialog
    ID_USER_UNATHORIZED_MSG = "//div[@class='hp-dialog']//div[@id='fs-user-unauthorized-msg']"
    ID_USER_UNATHORIZED_BTN = "//div[@class='hp-dialog']//button[@class='hp-ok hp-primary']"
    # VIEW
    ID_COMBO_MENU_VIEW = "css=div.hp-value"
    ID_LINK_ALL_ROLES = "xpath=//li[text()='All roles']",
    ID_LINK_INFRA_ADMINISTARTOR = "xpath=//li[text()='Infrastructure administrator']"
    ID_LINK_READ_ONLY = "xpath=//li[text()='Read only']"
    ID_LINK_BACKUP_ADMINISTRATOR = "xpath=//li[text()='Backup administrator']"
    ID_LINK_NETWORK_ADMINISTRATOR = "xpath=//li[text()='Network administrator']"
    ID_LINK_SERVER_ADMINISTRATOR = "xpath=//li[text()='Server administrator']"

    # AD function objects
    # this worked for 1.10
    ID_LINK_AD_USERS = "link=Add Directory Group"

    ID_COMBO_AUTH_SER = "xpath=//*[@id='fs-user-group-add-div']/fieldset/ol/li/a/span[@class='selectBox-arrow']"
    ID_COMBO_AUTH_LIST = "xpath=//*[@id='fs-user-group-add-div']/fieldset[1]/ol/li[1]/a"

    ID_INPUT_AD_USR_NAME = "xpath=//*[@id='fs-dir-credentials-username']"
    ID_INPUT_AD_PSW = "xpath=//*[@id='fs-dir-credentials-password']"
    ID_BTN_AD_USER_CONNECT = "//*[@id='fs-connect']"

    ID_ELEMENT_AD_USERNAME = "xpath=html/body/ul[2]/li[2]/a[text()='%s']"
    ID_COMBO_AD_GP = "xpath=//fieldset/ol/li/div/div[@class='hp-search-combo-control']"
    ID_COMBO_AD_GP_LIST = "xpath=//*[@id='fs-group-name-hp-select-combo-input']"

    ID_RADIO_AD_FULL_ROLE = "xpath=//*[@id='fs-user-role-full']"
    ID_RADIO_AD_READ_ROLE = "xpath=//*[@id='fs-user-role-readonly']"
    ID_RADIO_AD_SPECIALIZED_ROLE = "xpath=//*[@id='fs-user-role-specialized']"
    ID_BTN_ADD_AD_USRGP = "xpath=//*[@id='fs-add-user-group']"
    ID_ELEMENT_AD_DETAILS = "xpath=//*[@id='fs-users-table']/tbody/tr[*]/td[contains(text(),'%s')]"

    ID_CHECKBOX_AD_BACKUP_ADMINISTRATOR = "xpath=//*[@id='fs-user-role-2']"
    ID_CHECKBOX_AD_NETWORK_ADMINISTRATOR = "xpath=//*[@id='fs-user-role-3']"
    ID_CHECKBOX_AD_SERVER_ADMINISTRATOR = "xpath=//*[@id='fs-user-role-4']"
    ID_CHECKBOX_AD_STORAGE_ADMINISTRATOR = "xpath=//*[@id='fs-user-role-5']"

    ID_CHECKBOX_EDIT_STORAGE_ADMINISTRATOR = "xpath=//*[@id='fs-user-edit-role-3']"

    # Edit Current session user
    ID_SESSION_CONTROL = "xpath =.//*[@id='hp-session-control']/div[1]"
    ID_SESSION_LOGOUT = "xpath =//a[@id='hp-session-logout']"
    ID_CURRENT_SESSION_USER = "id=hp-session-user"
    ID_EDIT_CURRENT_USER_DIALOG = "id=user-settings-edit-dialog"
    ID_EDIT_CURRENT_SESSION_USER = "id=hp-session-user-edit"
    ID_INPUT_CURRENT_USER_FULL_NAME = "xpath =//input[@id='fs-usersettings-fullname']"
    ID_INPUT_CURRENT_PASSWORD = "xpath =//input[@id='fs-usersettings-currentpasswd']"
    ID_INPUT_NEW_PASSWORD = "id=fs-usersettings-newpasswd"
    ID_INPUT_CONFIRM_PASSWORD = "id=fs-usersettings-confirmpasswd"
    ID_INPUT_CURRENT_USER_EMAIL = "id=fs-usersettings-email"
    ID_INPUT_CURRENT_USER_OFFICE_PHN = "id=fs-usersettings-officephone"
    ID_INPUT_CURRENT_USER_MOBILE_PHN = "id=fs-usersettings-mobilephone"
    ID_BTN_CONFIRM_EDIT = "id=fs-usersettings-edit"
    ID_BTN_CANCEL_EDIT = "id=fs-usersettings-edit-cancel"
    ID_USER_NAME = "id=cic-user-name"
    ID_USER_FULLNAME = "id=cic-user-fullname"
    ID_USER_EMAIL = "id=cic-user-email"
    ID_USER_OFFICEPHONE = "id=cic-user-officephone"
    ID_USER_MOBILEPHONE = "id=cic-user-mobilephone"
    ID_SAME_PWD_MSG = "id=hp-form-message"

    # for AD link add user changes
    # for create user fun

    ID_LINK_ADD = "xpath=//*[@id='cic-user-add-link']/a[text()='Add Local User']"
    # for AD function
    ID_ELEMENT_ADDOMAIN = "xpath=//*[@id='fs-user-group-add-div']/fieldset/ol/li[1]/a"
    ID_ELEMENT_USER_SESSION = "xpath=//*[@id='hp-session-control']"
    ID_ELEMENT_EDIT = "xpath=//*[@id='hp-session-user-edit']"
    ID_ELEMENT_ROLE = "xpath=//*[@id='fs-usersettings-roles-list']/label[contains(text(),'%s')]"
    ID_USER_EDIT_CANCEL = "xpath=//*[@id='fs-usersettings-edit-cancel']"
    ID_ELEMENT_USER_NAME = "xpath=//*[@id='hp-session-user' and text()='%s']"
    ID_ELEMENT_USER_ROLE_LABEL = "xpath=//*[@id='fs-usersettings-edit-roles']/label"
    ID_ELEMENT_HEADER = "xpath.//*[@id='fs-user-group-header']/h1[text()='Add Directory User or Group']"

    # page validation for users and groups

    ID_ELEMENT_USER_NAME_DATA_VAL = "xpath=//*[@id='cic-user-details-title' and text()='%s']"
    ID_ELEMENT_USER_NAME_VAL = "xpath=//*[@id='fs-users-table']//td[text()='%s']"

    ID_ELEMENT_USER_ROLES_VAL_NET_SER = "xpath=.//div[@id='cic-user-roletype' and text()='%s' and text()='%s']"
    ID_ELEMENT_USER_ROLES_VAL_NET_SER_BACK = "xpath=.//div[@id='cic-user-roletype' and text()='%s' and text()='%s' and text()='%s']"
    ID_ELEMENT_USER_SINGLE_ROLES_VAL = "xpath=.//div[@id='cic-user-roletype' and text()='%s']"

    ID_USER_EMAIL_VAL = "xpath=.//*[@id='cic-user-email' and text()='%s']"
    ID_OFFICE_PHONE_VAL = "xpath=.//*[@id='cic-user-officephone' and text()='%s']"

    ID_MOBILE_PHONE_VAL = "xpath=.//*[@id='cic-user-mobilephone' and text()='%s']"
    ID_FULL_NAME_VAL = "xpath=.//*[@id='cic-user-fullname' and text()='%s']"

    # added for user role validation in the robot tests
    ID_ELEMENT_SESSION_USER = "xpath=//*[@id='fs-usersettings-loginname' and text()='%s']"
    ID_ELEMENT_USER_NAME_AD_ADDED = "xpath=//*[@id='hp-session-user' and text()='Local\'&'%s']"

    ID_ELEMENT_HEADER = "xpath.//*[@id='fs-user-group-header']/h1[text()='Add Directory User or Group']"
