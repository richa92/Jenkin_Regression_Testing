# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" i3S Users and Groups UI page."""

from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.ui.usersandgroups.usersandgroups_elements import i3SUserandGroupsPage
from i3SLibrary.ui.usersandgroups.usersandgroups_elements import UserRoles
from i3SLibrary.ui.general.base_elements import i3SBasePage
from i3SLibrary.ui.general import base_page
from i3SLibrary.ui.settings import settings
from i3SLibrary.ui.general.login_elements import i3SLoginPage
from i3SLibrary.ui.general.dashboard_elements import i3SDashboardPage
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants


def navigate():
    base_page.navigate_base(i3SUserandGroupsPage.ID_PAGE_LABEL, i3SBasePage.ID_MENU_LINK_USERS_AND_GROUPS, "css=span.hp-page-item-count")


def create_user(*user_obj):
    logger._log_to_console_and_log_file("add_user()")
    selenium2lib = ui_lib.get_s2l()

    # Navigate to USERS page and click on the Actions -> Add
    navigate()

    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    # if the user exists or it is an AD or LDAP Group, skip
    users = []
    user_list = [u.text.lower() for u in selenium2lib._element_find(i3SUserandGroupsPage.ID_ALL_USERNAME_LIST, False, False)]
    for user in user_obj:
        if user.name.lower() == 'administrator':
            logger._log_to_console_and_log_file("No need to add Administrator")
            continue
        elif(user.has_property("domainName")):
            logger._log_to_console_and_log_file('Skipping: %s is LDAP or AD. No need to create user locally.' % user.name)
            continue
        elif user.name.lower() in user_list:
            logger._warn("User '{0}' already exists".format(user.name))
            continue
        else:
            users.append(user)

    # if there are no users to add, return
    if len(users) == 0:
        return True

    ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
    # as users and groups add link changes for normal users adding the below code.
    if selenium2lib._is_element_present(i3SUserandGroupsPage.ID_LINK_ADD):
        selenium2lib.click_element(i3SUserandGroupsPage.ID_LINK_ADD)
    else:
        selenium2lib.element_should_be_visible(i3SUserandGroupsPage.ID_MENU_ACTION_ADD)
        selenium2lib.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_ADD)
    ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_INPUT_USER_LOGIN_NAME)

    # Add all the users according the data provided
    for user in users:
        # If the user name is "Administrator" ignore adding the same.
        if not user.name == 'Administrator':
            ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_INPUT_USER_LOGIN_NAME, user.name)
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_USER_LOGIN_NAME, user.name)

            # Fill in the details if fullname(Optional attribute) if specified
            if user.has_property('fullname'):
                selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_USER_FULL_NAME, user.fullname)
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_USER_INITIAL_PASSWORD, user.password)
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_USER_CONFIRM_PASSWORD, user.password)

            # Choose the privileges according to the input provided
            rolelist = user.role.split(",")
            for role in range(0, len(rolelist)):
                # Logic for a combination of roles to be chosen and also single roles chosen
                if rolelist[role] == UserRoles.SERVERADMIN:
                    selenium2lib.click_element(i3SUserandGroupsPage.ID_RADIO_ROLE_SPECIALIZED)
                    selenium2lib.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_STORAGE_ADMINISTRATOR)
                    selenium2lib.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_SERVER_ADMINISTRATOR)
                elif rolelist[role] == UserRoles.STORAGEADMIN:
                    selenium2lib.click_element(i3SUserandGroupsPage.ID_RADIO_ROLE_SPECIALIZED)
                    selenium2lib.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_STORAGE_ADMINISTRATOR)
                elif rolelist[role] == UserRoles.NETWORKADMIN:
                    selenium2lib.click_element(i3SUserandGroupsPage.ID_RADIO_ROLE_SPECIALIZED)
                    selenium2lib.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_NETWORK_ADMINISTRATOR)
                elif rolelist[role] == UserRoles.BACKUPADMIN:
                    selenium2lib.click_element(i3SUserandGroupsPage.ID_RADIO_ROLE_SPECIALIZED)
                    selenium2lib.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_BACKUP_ADMINISTRATOR)
                elif rolelist[role] == UserRoles.FULL:
                    selenium2lib.click_element(i3SUserandGroupsPage.ID_RADIO_ROLE_FULL)
                elif rolelist[role] == UserRoles.READONLY:
                    selenium2lib.click_element(i3SUserandGroupsPage.ID_RADIO_ROLE_READ_ONLY)

            # Fill in the values for optional attributes (E-mail, office phone and mobile phone)
            if user.has_property('email'):
                selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_USER_EMAIL, user.email)
            if user.has_property('officephone'):
                selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_USER_OFFICE_PHONE, user.officephone)
            if user.has_property('mobilephone'):
                selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_USER_MOBILE_PHONE, user.mobilephone)

            # Click the Addplus and dynamically wait for the user to add
            selenium2lib.click_button(i3SUserandGroupsPage.ID_BTN_USER_ADD_PLUS)

            # if the name is in use already, warn and continue
            warn_skip = False
            for text in ["This login name is already in use.", "At least one role must be selected."]:
                if ui_lib.page_contains(text):
                    logger._warn(text + "  '" + user.name + "'")
                    warn_skip = True
            if warn_skip:
                continue

            ui_lib.wait_for_element_text_match(i3SUserandGroupsPage.ID_CREATE_USER_MESSAGE_TEXT, ".+")
            if selenium2lib._is_visible("xpath=//div[@class='hp-status hp-status-error']"):
                ui_lib.fail_test(selenium2lib._get_text(i3SUserandGroupsPage.ID_CREATE_USER_MESSAGE_TEXT), True)

            ui_lib.wait_for_element_value(i3SUserandGroupsPage.ID_INPUT_USER_LOGIN_NAME, "")

    # Click on the cancel button once all the users are done adding
    selenium2lib.click_element(i3SUserandGroupsPage.ID_BTN_USER_ADD_CANCEL)
    return True


def verify_user(userName):
    """ Verify User

        Not Yet Implemented


        Example:
        | `Verify User`      |     |
    """
    pass


def remove_user(*user_obj):
    # get the s2lrary reference
    s2l = ui_lib.get_s2l()

    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    # Navigate to the users and groups page if not already there
    navigate()

    for user in user_obj:
        # ignore administrator - note that this is checked below to see if we get the
        # correct message when trying to delete the administrator.  However i3S
        # lists the account as 'administrator' not 'Administrator' in the list, so we
        # get an 'element not found' error.  Also, it appears that xpath2.0 is not supported,
        # so we can't make the locator lower case.
        if user.name.lower() == 'administrator':
            continue

        # create the locator in the user table
        locator = i3SUserandGroupsPage.ID_USERS_TABLE + "//td[text()='{0}']".format(user.name)

        # if the user doesn't exist, warn and be done
        if not s2l._is_element_present(locator):
            logger._warn('%s does not exist in user list' % user.name)
        else:  # locate the user in the list and remove them
            logger._log_to_console_and_log_file('Removing user "%s"' % user.name)
            s2l.element_should_be_visible(i3SUserandGroupsPage.ID_USERS_TABLE)
            ui_lib.ignore_staleElementRefException("table_column_should_contain", i3SUserandGroupsPage.ID_USERS_TABLE, i3SUserandGroupsPage.ID_USERS_TABLE_NAME_COLUMN, user.name)
            s2l.click_element(locator)
            ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
            s2l.element_should_be_visible(i3SUserandGroupsPage.ID_MENU_ACTION_REMOVE_USER)
            s2l.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_REMOVE_USER)

            # make sure the remove dialog is displayed
            s2l.element_should_be_visible(i3SUserandGroupsPage.ID_CONFIRM_REMOVE_DIALOG_PROMPT)
            ui_lib.wait_for_element_text_match(i3SUserandGroupsPage.ID_CONFIRM_REMOVE_DIALOG_TITLE,
                                               'Remove %s' % user.name,
                                               'Unexpected Remove dialog title.')

            # if the user is the administrator, be sure that the appropriate dialog is displayed
            if user.name.lower() == 'administrator':
                s2l.element_should_be_visible(i3SUserandGroupsPage.ID_USER_UNATHORIZED_MSG)
                s2l.element_should_be_visible(i3SUserandGroupsPage.ID_USER_UNATHORIZED_BTN)
                s2l.click_element(i3SUserandGroupsPage.ID_USER_UNATHORIZED_BTN)
            else:  # delete the user
                s2l.click_element(i3SUserandGroupsPage.ID_BTN_YES_CONFIRM_REMOVE)

                # make sure the activity message is displayed
                s2l.element_should_be_visible(i3SBasePage.ID_ACTIVE_ACTIVITY_NOTIFICATION)

                if ui_lib.wait_for_element_remove(i3SUserandGroupsPage.ID_USERS_TABLE + "//td[text()='{0}']".format(user.name)):
                    logger._log_to_console_and_log_file("Successfully removed %s" % user.name)
                else:
                    logger._warn("Not able to remove user %s" % user.name)


def edit_users(*user_obj):
    """ Edit User
      This functions allows you to edit users in user page retrieving data from data.xml
 """
    s2l = ui_lib.get_s2l()
    # navigate to user page
    navigate()
    # retriveing data from datafile
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    for user_name in user_obj:
        # find the user in the users table
        selector = i3SUserandGroupsPage.ID_USERS_TABLE + "//td[text()='{0}']".format(user_name.name)
        # if the user doesn't exist, warn and be done
        if not s2l._is_element_present(selector):
            logger._log_to_console_and_log_file("user is not available to edit %s " % user_name.name)
            logger._warn('{0} does not exist in user list'.format(user_name.name))
        else:  # locate the user in the list and edit them
            logger._log_to_console_and_log_file('Selecting user "{0}"'.format(user_name.name))
            s2l.element_should_be_visible(i3SUserandGroupsPage.ID_USERS_TABLE)
            s2l.table_column_should_contain(i3SUserandGroupsPage.ID_USERS_TABLE,
                                            i3SUserandGroupsPage.ID_USERS_TABLE_NAME_COLUMN,
                                            user_name.name)
            # select user in users table
            s2l.click_element(selector)
            # if the username is not equal to  administrator then edit users
            if str(user_name.name) != 'administrator':
                s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
                s2l.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
                s2l.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_EDIT_USER)
                s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                s2l.element_should_be_visible(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                # enter username
                if str(user_name.name) != "":
                    if str(user_name.name) == "empty":
                        s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME, "")
                    else:
                        s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME, user_name.name)
                # enter password
                if str(user_name.password) != "":
                    if str(user_name.password) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_INITIAL_PASSWORD, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_INITIAL_PASSWORD, user_name.password)
                # enter confirm password
                if str(user_name.password) != "":
                    if str(user_name.password) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_CONFIRM_PASSWORD, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_CONFIRM_PASSWORD, user_name.password)

                # applying single and multiple roles as well
                if user_name.role != "":
                    if user_name.role == "empty":
                        logger._log_to_console_and_log_file("Role cannot be empty %s " % user_name.role)
                    else:
                        # select role as full or readonly
                        if str(user_name.role) == "Infrastructure administrator":
                            s2l.click_element(i3SUserandGroupsPage.ID_RADIO_EDIT_ROLE_FULL)
                        elif str(user_name.role) == "Read only":
                            s2l.click_element(i3SUserandGroupsPage.ID_RADIO_EDIT_ROLE_READ_ONLY)
                        # spliting roles
                        else:
                            networkListtodelete = user_name.role.split(',')
                            if len(networkListtodelete) > 0:
                                # if role is specialized
                                s2l.click_element(i3SUserandGroupsPage.ID_RADIO_EDIT_ROLE_SPECIALIZED)
                                s2l.unselect_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_BACKUP_ADMINISTRATOR)
                                s2l.unselect_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_NETWORK_ADMINISTRATOR)
                                s2l.unselect_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_SERVER_ADMINISTRATOR)
                                s2l.unselect_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_STORAGE_ADMINISTRATOR)

                                # select roles one by one
                                for editrole in networkListtodelete:

                                    if str(editrole) == UserRoles.BACKUPADMIN:
                                        s2l._is_element_present(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_BACKUP_ADMINISTRATOR)
                                        s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_BACKUP_ADMINISTRATOR)
                                        logger._log_to_console_and_log_file("Selected the role as %s " % editrole)
                                    if str(editrole) == UserRoles.NETWORKADMIN:
                                        s2l._is_element_present(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_NETWORK_ADMINISTRATOR)
                                        s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_NETWORK_ADMINISTRATOR)
                                        logger._log_to_console_and_log_file("Selected the role as %s " % editrole)
                                    if str(editrole) == UserRoles.SERVERADMIN:
                                        s2l._is_element_present(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_SERVER_ADMINISTRATOR)
                                        s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_EDIT_SERVER_ADMINISTRATOR)
                                        logger._log_to_console_and_log_file("Selected the role as %s " % editrole)

                # continue editing email,phone and mobile..etc,,
                if str(user_name.email) != "":
                    if str(user_name.email) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_EMAIL, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_EMAIL, user_name.email)
                # enter officephone
                if str(user_name.officephone) != "":
                    if str(user_name.officephone) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_OFFICE_PHONE, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_OFFICE_PHONE, user_name.officephone)
                # enter mobilephone
                if str(user_name.mobilephone) != "":
                    if str(user_name.mobilephone) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_MOBILE_PHONE, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_MOBILE_PHONE, user_name.mobilephone)

                # after editing all fields click on OK button
                s2l.click_element(i3SUserandGroupsPage.ID_BTN_EDIT_OK)
                s2l.page_should_not_contain("Failed to Edit user")
                s2l.page_should_contain_element(i3SUserandGroupsPage.ID_ELEMENT_USERNAME_BASE % user_name.name)
                logger._log_to_console_and_log_file("Verifying user %s is present in the UI after Editing" % user_name.name)

            elif user_name.lower() == 'administrator':
                s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
                s2l.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
                s2l.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_EDIT_USER)

                # wait for fullname field should be visible
                s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                s2l.element_should_be_visible(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                # enter username
                if str(user_name) != "":
                    if str(user_name) == "empty":
                        s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME, "")
                    else:
                        s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME)
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_FULL_NAME, user_name)
                # enter currentpwd
                if str(user_name.currentpwd) != "":
                    if str(user_name.currentpwd) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_CURRENTPWD, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_CURRENTPWD, user_name.currentpwd)
                # enter password
                if str(user_name.password) != "":
                    if str(user_name.password) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_INITIAL_PASSWORD, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_INITIAL_PASSWORD, user_name.password)
                # enter confirm password
                if str(user_name.password) != "":
                    if str(user_name.password) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_CONFIRM_PASSWORD, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_CONFIRM_PASSWORD, user_name.password)
                # enter email
                if str(user_name.email) != "":
                    if str(user_name.email) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_EMAIL, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_EMAIL, user_name.email)
                # enter officephone
                if str(user_name.officephone) != "":
                    if str(user_name.officephone) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_OFFICE_PHONE, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_OFFICE_PHONE, user_name.officephone)
                # enter mobilephone
                if str(user_name.mobilephone) != "":
                    if str(user_name.mobilephone) == "empty":
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_MOBILE_PHONE, "")
                    else:
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_EDIT_MOBILE_PHONE, user_name.mobilephone)

                # after editing all fields click on OK button
                s2l.click_element(i3SUserandGroupsPage.ID_BTN_EDIT_OK)
                s2l.page_should_not_contain("Failed to Edit user")
                s2l.page_should_contain_element(i3SUserandGroupsPage.ID_ELEMENT_USERNAME_BASE % user_name.name)
                logger._log_to_console_and_log_file("Verifying user %s is present in the UI after Editing" % user_name.name)


def add_active_directory_users_and_groups(*user_obj):
    '''
    Deprecated - add active usersand groups to the appliance
    '''
    add_directory_users_and_groups(*user_obj)


def add_directory_users_and_groups(*user_obj):
    '''
    add directory users and groups to the appliance
    '''

    s2l = ui_lib.get_s2l()

    # retrieving data from data file
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)
    navigate()

    for adUser in user_obj:
        if(adUser.has_property("domainName")):
            if not s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_AD_DETAILS % adUser.egroup):
                logger._log_to_console_and_log_file("directory users and group not already added  '%s'  '%s'" % (adUser.egroup, adUser.domainName))
                # Add directory server if not previously added
                if (settings.add_directory_server(adUser) is True):
                    # Navigate to the 'Users and Groups' page
                    navigate()
                    # Wait for the 'Actions' menu to appear and select 'Add Directory Users and Groups'
                    ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
                    ui_lib.wait_for_element(i3SUserandGroupsPage.ID_LINK_AD_USERS, PerfConstants.DEFAULT_SYNC_TIME)

                    if s2l._is_element_present(i3SUserandGroupsPage.ID_LINK_AD_USERS):
                        ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_LINK_AD_USERS)
                        # Wait for 'Add Directory User or Group' page to appear
                        ui_lib.wait_for_element(i3SUserandGroupsPage.ID_ELEMENT_HEADER, PerfConstants.DEFAULT_SYNC_TIME)
                        # Select domain from the 'Directory' pull-down
                        if s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_ADDOMAIN):
                            # Pull-down the directory menu
                            s2l.click_element(i3SUserandGroupsPage.ID_ELEMENT_ADDOMAIN)
                            # logger._log_to_console_and_log_file("Selecting directory '%s'" % (adUser.domainName))
                            s2l.press_key(i3SUserandGroupsPage.ID_ELEMENT_ADDOMAIN, adUser.domainName)
                            s2l.press_key(i3SUserandGroupsPage.ID_ELEMENT_ADDOMAIN, '\\13')

                        # Credentials (username and password)
                        # logger._log_to_console_and_log_file("Enter credentials")
                        ui_lib.wait_for_element(i3SUserandGroupsPage.ID_INPUT_AD_USR_NAME, PerfConstants.DEFAULT_SYNC_TIME)
                        # Click on the password field first; otherwise it seems to mess-up the Directory selection
                        s2l.click_element(i3SUserandGroupsPage.ID_INPUT_AD_PSW)
                        s2l.click_element(i3SUserandGroupsPage.ID_INPUT_AD_USR_NAME)
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_AD_USR_NAME, adUser.userName)
                        s2l.input_text(i3SUserandGroupsPage.ID_INPUT_AD_PSW, adUser.userPswd)
                        # Click 'Connect' button to validate server connection
                        s2l.click_element(i3SUserandGroupsPage.ID_BTN_AD_USER_CONNECT)
                        # Group name
                        ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_COMBO_AD_GP)
                        s2l.input_text(i3SUserandGroupsPage.ID_COMBO_AD_GP_LIST, adUser.egroup)
                        s2l.click_element(i3SUserandGroupsPage.ID_INPUT_AD_USR_NAME)
                        rolelist = adUser.role.split(",")
                        # Role
                        for role in range(0, len(rolelist)):
                            # Logic for a combination of roles to be chosen and also single roles chosen
                            if rolelist[role] == UserRoles.SERVERADMIN:
                                s2l.click_element(i3SUserandGroupsPage.ID_RADIO_AD_SPECIALIZED_ROLE)
                                s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_AD_SERVER_ADMINISTRATOR)
                                s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_AD_STORAGE_ADMINISTRATOR)
                            elif rolelist[role] == UserRoles.STORAGEADMIN:
                                s2l.click_element(i3SUserandGroupsPage.ID_RADIO_ROLE_SPECIALIZED)
                                s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_STORAGE_ADMINISTRATOR)
                            elif rolelist[role] == UserRoles.NETWORKADMIN:
                                s2l.click_element(i3SUserandGroupsPage.ID_RADIO_AD_SPECIALIZED_ROLE)
                                s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_AD_NETWORK_ADMINISTRATOR)
                            elif rolelist[role] == UserRoles.BACKUPADMIN:
                                s2l.click_element(i3SUserandGroupsPage.ID_RADIO_AD_SPECIALIZED_ROLE)
                                s2l.select_checkbox(i3SUserandGroupsPage.ID_CHECKBOX_AD_BACKUP_ADMINISTRATOR)
                            elif rolelist[role] == UserRoles.FULL:
                                s2l.click_element(i3SUserandGroupsPage.ID_RADIO_AD_FULL_ROLE)
                            elif rolelist[role] == UserRoles.READONLY:
                                s2l.click_element(i3SUserandGroupsPage.ID_RADIO_AD_READ_ROLE)

                        # Click on 'Add' button
                        ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_BTN_ADD_AD_USRGP, 10, 3)
                        # fails now and again; adding sleep for now
                        BuiltIn().sleep(10)
                        # Back at 'Users and Groups' page, verify Named group is present
                        s2l.wait_until_page_contains_element(i3SUserandGroupsPage.ID_ELEMENT_AD_DETAILS % adUser.egroup)
                        # Validate directory user or group was added
                        if s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_AD_DETAILS % adUser.egroup):
                            logger._log_to_console_and_log_file("added directory users and group '%s' from '%s'" % (adUser.egroup, adUser.domainName))
                        else:
                            logger._log_to_console_and_log_file("not able to add directory users and group '%s'" % (adUser.egroup))
                            ui_lib.fail_test("not able to add directory users and group '%s' " % (adUser.egroup), "True")
                        # Validate role is applied properly for the directory users and groups
                        if s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_AD_DETAILS % adUser.role):
                            logger._log_to_console_and_log_file("validation successful for directory users roles '%s'" % (adUser.role))
                        else:
                            logger._log_to_console_and_log_file("not able validate directory roles '%s'" % (adUser.role))
                            ui_lib.fail_test("not able to add directory users and group role '%s' " % (adUser.role), "True")

                    else:
                        ui_lib.fail_test(" not able to add directory as Add directory users and group link is not available", "True")

                else:
                    # if directory server is not added exit keyword
                    ui_lib.fail_test("not able to add directory", "True")
            else:
                logger._log_to_console_and_log_file("directory group is already added  '%s'  '%s'" % (adUser.egroup, adUser.domainName))
    return True


def remove_directory_user_or_group(*user_obj):
    '''
    remove active directory or ldap users and groups listed in the dcs_data.xml file
    '''
    s2l = ui_lib.get_s2l()

    # retrieving data from data file
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)
        navigate()
    for userGroup in user_obj:
        if(userGroup.has_property("domainName")):
            if not s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_AD_DETAILS % userGroup.egroup):
                logger._log_to_console_and_log_file("No need to remove '%s' as this directory group does not exist. " % (userGroup.egroup))
            else:
                logger._log_to_console_and_log_file("Removing '%s'" % (userGroup.egroup))
                s2l.click_element(i3SUserandGroupsPage.ID_ELEMENT_USER_NAME_VAL % userGroup.egroup)
                s2l.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_MAIN_BTN)
                s2l.click_element(i3SUserandGroupsPage.ID_MENU_ACTION_REMOVE_USER)
                s2l.click_element(i3SUserandGroupsPage.ID_BTN_YES_CONFIRM_REMOVE)
    return True


def edit_current_session_user(user_obj):
    """ Edit Current Session User
        This functions allows you to edit current session user whoever users listed in user page retrieving data from data.xml
    """
    logger._log_to_console_and_log_file("Edit Current Session User...")
    selenium2lib = ui_lib.get_s2l()

    user = test_data.get().currentSessionUser
    user = user[0]

    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    # Login with current session user credentials
    if ui_lib.wait_for_element_visible(i3SLoginPage.ID_BTN_LOGIN_BUTTON, PerfConstants.DEFAULT_SYNC_TIME):
        selenium2lib.input_text(i3SLoginPage.ID_INPUT_LOGIN_USER, user.name)
        selenium2lib.input_text(i3SLoginPage.ID_INPUT_LOGIN_PASSWORD, user.password)
        ui_lib.wait_for_element_and_click(i3SLoginPage.ID_BTN_LOGIN_BUTTON)
        if ui_lib.wait_for_element_visible(i3SDashboardPage.ID_PAGE_LABEL, PerfConstants.i3S_LOGIN_TIME):
            logger._log_to_console_and_log_file("Login Successful")
        elif ui_lib.wait_for_element_visible(i3SLoginPage.ID_LABEL_LOGIN_STATUS):
            logger._warn("Login Fail. Invalid username or password. Enter correct credentials and try again.")
            return False
    # Check session user name and edit current session
    ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_SESSION_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
    current_user = selenium2lib.get_text(i3SUserandGroupsPage.ID_CURRENT_SESSION_USER)

    # check Login name
    if (user.name in current_user):
        ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_EDIT_CURRENT_SESSION_USER, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_EDIT_CURRENT_USER_DIALOG, PerfConstants.DEFAULT_SYNC_TIME)
        # Edit full name
        if user.has_property('fullname'):
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_CURRENT_USER_FULL_NAME, user.fullname)
        # Enter current password
        if user.has_property('password'):
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_CURRENT_PASSWORD, user.password)
        # Enter New password
        if user.has_property('newpassword'):
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_NEW_PASSWORD, user.newpassword)
        # Enter confirm password
        if user.has_property('confirmpassword'):
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_CONFIRM_PASSWORD, user.confirmpassword)

        # Edit email
        if user.has_property('email'):
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_CURRENT_USER_EMAIL, user.email)
        # Edit office phone number
        if user.has_property('officephone'):
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_CURRENT_USER_OFFICE_PHN, user.officephone)
        # Edit Mobile number
        if user.has_property('mobilephone'):
            selenium2lib.input_text(i3SUserandGroupsPage.ID_INPUT_CURRENT_USER_MOBILE_PHN, user.mobilephone)
        # Confirm Edit - Clicking OK
        ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_BTN_CONFIRM_EDIT)
        if ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_SAME_PWD_MSG, PerfConstants.DEFAULT_SYNC_TIME):
            ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_BTN_CANCEL_EDIT)

        # Logging out
        ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_SESSION_CONTROL)
        ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_SESSION_LOGOUT)
        logger._log_to_console_and_log_file("LOGOUT")

    # Login with Current User if password has changed
    if user.has_property('newpassword'):
        logger._log_to_console_and_log_file("Login with new password")
        if ui_lib.wait_for_element_visible(i3SLoginPage.ID_BTN_LOGIN_BUTTON, PerfConstants.DEFAULT_SYNC_TIME):
            selenium2lib.input_text(i3SLoginPage.ID_INPUT_LOGIN_USER, user.name)
            selenium2lib.input_text(i3SLoginPage.ID_INPUT_LOGIN_PASSWORD, user.newpassword)
            ui_lib.wait_for_element_and_click(i3SLoginPage.ID_BTN_LOGIN_BUTTON, PerfConstants.DEFAULT_SYNC_TIME)
            if ui_lib.wait_for_element_visible(i3SDashboardPage.ID_PAGE_LABEL, PerfConstants.i3S_LOGIN_TIME):
                logger._log_to_console_and_log_file("Changed Password of '%s' is verified Successfully" % user.name)
                # Logging out
                ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_SESSION_CONTROL)
                ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_SESSION_LOGOUT)
                logger._log_to_console_and_log_file("LOGOUT")
            else:
                logger._warn("Password verification of '%s' failed" % user.name)

    # Login with Administrator and verify edit
    logger._log_to_console_and_log_file("Login with Administrator")
    if ui_lib.wait_for_element_visible(i3SLoginPage.ID_BTN_LOGIN_BUTTON, PerfConstants.DEFAULT_SYNC_TIME):
        selenium2lib.input_text(i3SLoginPage.ID_INPUT_LOGIN_USER, user.adminuser)
        selenium2lib.input_text(i3SLoginPage.ID_INPUT_LOGIN_PASSWORD, user.adminpassword)
        ui_lib.wait_for_element_and_click(i3SLoginPage.ID_BTN_LOGIN_BUTTON, PerfConstants.DEFAULT_SYNC_TIME)
        if ui_lib.wait_for_element_visible(i3SDashboardPage.ID_PAGE_LABEL, PerfConstants.i3S_LOGIN_TIME):
            logger._log_to_console_and_log_file("Administrator successfully logged in")

        navigate()
        selector = i3SUserandGroupsPage.ID_USERS_TABLE + "//td[text()='{0}']".format(user.name)
        ui_lib.wait_for_element_and_click(selector)

        if user.has_property('name'):
            # Edit full name
            if selenium2lib.get_text(i3SUserandGroupsPage.ID_USER_NAME) == user.name:
                logger._log_to_console_and_log_file("Login name is same '%s'" % user.name)
            else:
                logger._warn("Login name is different")
                return False
        if user.has_property('fullname'):
            if selenium2lib.get_text(i3SUserandGroupsPage.ID_USER_FULLNAME) == user.fullname:
                logger._log_to_console_and_log_file(user.fullname)
            else:
                logger._warn("Full name is different")
                return False
        if user.has_property('email'):
            if selenium2lib.get_text(i3SUserandGroupsPage.ID_USER_EMAIL) == user.email:
                logger._log_to_console_and_log_file("email is same as edited '%s'" % user.email)
            else:
                logger._warn("email is different")
                return False
        if user.has_property('officephone'):
            if selenium2lib.get_text(i3SUserandGroupsPage.ID_USER_OFFICEPHONE) == user.officephone:
                logger._log_to_console_and_log_file("officephone is same as edited '%s'" % user.officephone)
            else:
                logger._warn("officephone is different")
                return False
        if user.has_property('mobilephone'):
            if selenium2lib.get_text(i3SUserandGroupsPage.ID_USER_MOBILEPHONE) == user.mobilephone:
                logger._log_to_console_and_log_file("mobilephone is same as edited '%s'" % user.mobilephone)
                return True
            else:
                logger._warn("mobilephone is different")
                return False


def userdata_validation(*user_obj):
    """ Verify User data

        The function validates the user data in the users and groups page.
        Example:
        | `userdata validation`      |     |
    """

    s2l = ui_lib.get_s2l()

    # retrieving data from data file
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    navigate()
    ui_lib.wait_for_element(i3SUserandGroupsPage.ID_PAGE_LABEL)
    ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_PAGE_LABEL)
    for user in user_obj:
        if s2l._is_element_present(i3SUserandGroupsPage.ID_PAGE_LABEL):
            logger._log_to_console_and_log_file("Navigated succesfully to users and groups  Page")
            """ check for user exists """
            if not select_user(user.name):
                logger._warn("user '%s' is not present" % user.name)
                ui_lib.fail_test("user does not exist..verify the user created or not", True)
            else:
                """ Select if user exists """
                ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_ELEMENT_USER_NAME_VAL % user.name)
                # validate users details
                if s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_USER_NAME_VAL % user.name):
                    logger._log_to_console_and_log_file("user name is validated")
                else:
                    ui_lib.fail_test("user is not selected ", True)
                # validate for user role
                user.role = user.role.split(",")
                if len(user.role) == 1:
                    if s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_USER_SINGLE_ROLES_VAL % user.role[0]):
                        logger._log_to_console_and_log_file("user role is validated")
                    else:
                        ui_lib.fail_test("failed to validate user role ", True)
                if len(user.role) == 2:
                    if s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_USER_ROLES_VAL_NET_SER % (user.role[0], user.role[1])):
                        logger._log_to_console_and_log_file("user role is validated")
                    else:
                        ui_lib.fail_test("failed to validate user role ", True)
                if len(user.role) == 3:
                    if s2l._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_USER_ROLES_VAL_NET_SER_BACK % (user.role[0], user.role[1], user.role[2])):
                        logger._log_to_console_and_log_file("user role is validated")
                    else:
                        ui_lib.fail_test("failed to validate user role ", True)

                # validate for email
                if user.has_property('email'):
                    # ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_USER_EMAIL_VAL, user.email)
                    if s2l._is_element_present(i3SUserandGroupsPage.ID_USER_EMAIL_VAL % user.email):
                        logger._log_to_console_and_log_file("user email is validated")
                    else:
                        ui_lib.fail_test("failed to validate user email ", True)

                # validate for user office ph number
                if user.has_property('officephone'):
                    # ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_OFFICE_PHONE_VAL, user.officephone)
                    if s2l._is_element_present(i3SUserandGroupsPage.ID_OFFICE_PHONE_VAL % user.officephone):
                        logger._log_to_console_and_log_file("user office phone number  is validated")
                    else:
                        ui_lib.fail_test("failed to validate user office phone number ", True)

                # validate for user mobilephone ph number
                if user.has_property('mobilephone'):
                    # ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_MOBILE_PHONE_VAL, user.mobilephone)
                    if s2l._is_element_present(i3SUserandGroupsPage.ID_MOBILE_PHONE_VAL % user.mobilephone):
                        logger._log_to_console_and_log_file("user mobile phone number  is validated")
                    else:
                        ui_lib.fail_test("failed to validate user mobile phone ", True)

                # validate for user full name
                if user.has_property('fullname'):
                    # ui_lib.wait_for_element_visible(i3SUserandGroupsPage.ID_MOBILE_PHONE_VAL, user.mobilephone)
                    if s2l._is_element_present(i3SUserandGroupsPage.ID_FULL_NAME_VAL % user.fullname):
                        logger._log_to_console_and_log_file("user fullname  is validated")
                    else:
                        ui_lib.fail_test("failed to validate user fullname ", True)

        else:
            logger._log_to_console_and_log_file("Fail in navigating to user and group page Page")
            return False


def select_user(name):
    """ Select user from the users and groups page """
    selenium2lib = ui_lib.get_s2l()
    navigate()

    if selenium2lib._is_element_present(i3SUserandGroupsPage.ID_PAGE_LABEL):
        logger._log_to_console_and_log_file("Navigated succesfully to user Page")

        """ check for user exists """
        if not selenium2lib._is_element_present(i3SUserandGroupsPage.ID_ELEMENT_USERNAME_BASE % name):
            logger._warn("user '%s' is not present" % name)
            return False
        else:
            """ Select if user exists """
            ui_lib.wait_for_element_and_click(i3SUserandGroupsPage.ID_ELEMENT_USERNAME_BASE % name)
            ui_lib.wait_for_element(i3SUserandGroupsPage.ID_ELEMENT_USERNAME_BASE % name + "/ancestor::tr[contains(@class, hp-selected)]")
            logger._log_to_console_and_log_file("Selected the user %s successfully" % name)
            return True
    else:
        logger._log_to_console_and_log_file("Fail in navigating to user Page")
        return False
