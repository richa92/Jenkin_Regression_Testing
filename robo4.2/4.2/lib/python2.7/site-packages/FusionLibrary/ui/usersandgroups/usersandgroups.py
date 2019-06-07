# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Users and Groups UI page."""

from RoboGalaxyLibrary.data import test_data
from FusionLibrary.ui.settings import settings
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import FusionUIBase
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.usersandgroups.usersandgroups_elements import FusionUserandGroupsPage
from FusionLibrary.ui.business_logic.base import FusionUIConst
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import GeneralUserandGroups
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import CreateUser
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import RemoveUser
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import AddDirectoryUserAndGroup
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import EditUser
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import EditCurrentSessionUser
from FusionLibrary.ui.business_logic.usersandgroups.usersandgroups import VerifyUser


def navigate():
    logger.info("Navigate to Users and Groups page")
    FusionUIBase.navigate_to_section(SectionType.USERS_AND_GROUPS)


def create_user(*user_obj):
    logger.info("add_user()")

    # Navigate to USERS page and click on the Actions -> Add
    navigate()

    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    # if the user exists or it is an AD or LDAP Group, skip
    users = []
    user_list = [u.lower() for u in GeneralUserandGroups.get_user_list()]
    for user in user_obj:
        if user.name.lower() == 'administrator':
            logger.info("No need to add Administrator")
            continue
        elif(user.has_property("domainName")):
            logger.info('Skipping: %s is LDAP or AD. No need to create user locally.' % user.name)
            continue
        elif user.name.lower() in user_list:
            logger.warn("User '{0}' already exists".format(user.name))
            continue
        else:
            users.append(user)

    # if there are no users to add, return
    if len(users) == 0:
        return True

    CreateUser.click_action_add_user_button()
    CreateUser.wait_add_user_dialog_shown()

    # Add all the users according the data provided
    for user in users:
        # If the user name is "Administrator" ignore adding the same.
        if not user.name == 'Administrator':
            CreateUser.input_login_name(user.name)

            # Fill in the details if fullname(Optional attribute) if specified
            if user.has_property('fullname'):
                CreateUser.input_full_name(user.fullname)
            CreateUser.input_initial_password(user.password)
            CreateUser.input_confirm_password(user.password)
            CreateUser.select_role(user.role)
            # Fill in the values for optional attributes (E-mail, office phone and mobile phone)
            if user.has_property('email'):
                CreateUser.input_email(user.email)
            if user.has_property('officephone'):
                CreateUser.input_office_phone(user.officephone)
            if user.has_property('mobilephone'):
                CreateUser.input_mobile_phone(user.mobilephone)

            # Click the Addplus and dynamically wait for the user to add
            CreateUser.click_add_plus_button()

            # if the name is in use already, warn and continue
            BuiltIn().sleep(3)
            if not CreateUser.varify_add_successful():
                continue
            GeneralUserandGroups.verify_error_message_no_exist()
            CreateUser.verify_add_plus_ok()

    # Click on the cancel button once all the users are done adding
    CreateUser.click_cancel_button()
    CreateUser.wait_add_user_dialog_disappear()
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

    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    # Navigate to the users and groups page if not already there
    navigate()
    error = 0
    for user in user_obj:
        # ignore administrator - note that this is checked below to see if we get the
        # correct message when trying to delete the administrator.  However Fusion
        # lists the account as 'administrator' not 'Administrator' in the list, so we
        # get an 'element not found' error.  Also, it appears that xpath2.0 is not supported,
        # so we can't make the locator lower case.

        if user.name.lower() == 'administrator':
            continue

        # if the user doesn't exist, warn and be done
        if not VerifyUser.verify_user_exist(user.name):
            logger.warn('%s does not exist in user list' % user.name)
        else:  # locate the user in the list and remove them
            logger.info('Removing user "%s"' % user.name)
            BuiltIn().sleep(5)
            GeneralUserandGroups.click_user(user.name)
            VerifyUser.verify_user_title(user.name)
            RemoveUser.click_action_remove_user_button()

            # make sure the remove dialog is displayed
            RemoveUser.wait_remove_user_dialog_shown()

            # delete the user
            RemoveUser.click_yes_remove_button()
            RemoveUser.wait_cannot_remove_user_dialog_disappear()

            if not VerifyUser.verify_user_not_exist(user.name):
                logger.warn("Not able to remove user %s" % user.name)
                error += 1
            else:
                logger.info("Successfully removed %s" % user.name)

    if error > 0:
        return False
    else:
        return True


def edit_users(*user_obj):
    """ Edit User
      This functions allows you to edit users in user page retrieving data from data.xml
 """
    # navigate to user page
    navigate()
    # retriveing data from datafile
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)
    fail = 0
    for user_name in user_obj:
        # find the user in the users table
        if str(user_name.name).lower() != 'administrator':
            GeneralUserandGroups.click_user(user_name.name)
        else:
            GeneralUserandGroups.click_user('administrator')
        EditUser.click_action_edit_button()
        EditUser.wait_edit_user_dialog_shown()
        BuiltIn().sleep(3)
        # enter full username
        if str(user_name.fullname) != "":
            if str(user_name.fullname) == "empty":
                EditUser.input_full_name("")
            else:
                EditUser.input_full_name(user_name.fullname)
        # enter password
        if str(user_name.name).lower() != 'administrator':
            if str(user_name.password) != "":
                if str(user_name.password) == "empty" or str(user_name.password) == "wpsthpvse1":
                    EditUser.input_initial_password("")
                    EditUser.input_confirm_password("")
                else:
                    EditUser.input_initial_password(user_name.password)
                    EditUser.input_confirm_password(user_name.password)
        else:
            # enter currentpwd
            if str(user_name.currentpwd) != "":
                if str(user_name.currentpwd) == "empty":
                    EditCurrentSessionUser.input_current_password("")
                else:
                    EditCurrentSessionUser.input_current_password(user_name.currentpwd)
        #  editing email,phone and mobile..etc,
        if str(user_name.email) != "":
            if str(user_name.email) == "empty":
                EditUser.input_email("")
            else:
                EditUser.input_email(user_name.email)
        if str(user_name.officephone) != "":
            if str(user_name.officephone) == "empty":
                EditUser.input_office_phone("")
            else:
                EditUser.input_office_phone(user_name.officephone)
        if str(user_name.mobilephone) != "":
            if str(user_name.mobilephone) == "empty":
                EditUser.input_mobile_phone("")
            else:
                EditUser.input_mobile_phone(user_name.mobilephone)
        if str(user_name.name).lower() != 'administrator':
            # applying single and multiple roles as well
            if user_name.role != "":
                if user_name.role == "empty":
                    logger.info("Role cannot be empty")
                else:
                    EditUser.edit_role_specialized(user_name.role)
                    # CreateUser.click_role_specialized(user_name.role)

        # after editing all fields click on OK button
        EditUser.click_ok_button()
        if not EditUser.wait_edit_user_dialog_disappear(5, False):
            fail += 1
            logger.warn("Edit User Failed")
            EditUser.click_cancel_button()
        if not VerifyUser.verify_user_exist(user_name.name):
            if str(user_name.name).lower() != 'administrator':
                logger.warn("Can not find User name %s" % user_name.name)
                fail += 1

    if fail > 0:
        return False
    else:
        return True


def add_active_directory_users_and_groups(*user_obj):
    '''
    Deprecated - add active usersand groups to the appliance
    '''
    add_directory_users_and_groups(*user_obj)


def add_directory_users_and_groups(*user_obj):
    '''
    add directory users and groups to the appliance
    '''
    # retrieving data from data file
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)
    navigate()

    adserver_added = False
    ldapserver_added = False
    fail = 0

    for adUser in user_obj:
        if(adUser.has_property("domainName")):
            if VerifyUser.verify_user_not_exist(adUser.egroup, adUser.domainName, True):
                logger.info("directory users and group not already added  '%s'  '%s'" % (adUser.egroup, adUser.domainName))
                # Add directory server if not previously added
                if adUser.authProto == 'AD' and adserver_added is False:
                    if settings.add_directory_server(adUser) is False:
                        # if directory server is not added exit keyword
                        logger.warn("not able to add directory 'AD'")
                        return False
                    adserver_added = True

                if adUser.authProto == 'LDAP' and ldapserver_added is False:
                    if settings.add_directory_server(adUser) is False:
                        # if directory server is not added exit keyword
                        logger.warn("not able to add directory 'LDAP'")
                        return False
                    ldapserver_added = True

                # Navigate to the 'Users and Groups' page
                navigate()
                # Wait for the 'Actions' menu to appear and select 'Add Directory Users and Groups'
                AddDirectoryUserAndGroup.click_action_add_group_button()
                # Wait for 'Add Directory User or Group' page to appear
                AddDirectoryUserAndGroup.wait_add_group_dialog_shown()
                # Select domain from the 'Directory' pull-down
                logger.info("choosing %s as directory" % adUser.domainName)
                AddDirectoryUserAndGroup.select_directory(adUser.domainName)

                # Group name
                AddDirectoryUserAndGroup.input_group_name(adUser.egroup)
                rolelist = adUser.role.split(",")
                # Role
                for role in range(0, len(rolelist)):
                        # Logic for a combination of roles to be chosen and also single roles chosen
                    if rolelist[role] == FusionUIConst.UserRoles.SERVERADMIN:
                        AddDirectoryUserAndGroup.tick_role_specialized()
                        AddDirectoryUserAndGroup.tick_server_administrator()
                    elif rolelist[role] == FusionUIConst.UserRoles.STORAGEADMIN:
                        AddDirectoryUserAndGroup.tick_role_specialized()
                        AddDirectoryUserAndGroup.tick_storage_administrator()
                    elif rolelist[role] == FusionUIConst.UserRoles.NETWORKADMIN:
                        AddDirectoryUserAndGroup.tick_role_specialized()
                        AddDirectoryUserAndGroup.tick_network_administrator()
                    elif rolelist[role] == FusionUIConst.UserRoles.BACKUPADMIN:
                        AddDirectoryUserAndGroup.tick_role_specialized()
                        AddDirectoryUserAndGroup.tick_backup_administrator()
                    elif rolelist[role] == FusionUIConst.UserRoles.FULL:
                        AddDirectoryUserAndGroup.tick_role_full()
                    elif rolelist[role] == FusionUIConst.UserRoles.READONLY:
                        AddDirectoryUserAndGroup.tick_role_read_only()

                # Credentials (username and password)
                # Click on 'Add' button
                AddDirectoryUserAndGroup.click_add_button()

                if not VerifyUser.verify_user_exist(adUser.egroup, adUser.domainName, True):
                    fail = fail + 1

    if fail > 0:
        return False
    else:
        return True


def remove_directory_user_or_group(*user_obj):
    '''
    remove active directory or ldap users and groups listed in the dcs_data.xml file
    '''

    # retrieving data from data file
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)
        navigate()
    error = 0
    for userGroup in user_obj:
        if(userGroup.has_property("domainName")):
            GeneralUserandGroups.click_user(userGroup.name, userGroup.domainName, True)
            RemoveUser.click_action_remove_user_button()
            # make sure the remove dialog is displayed
            RemoveUser.wait_remove_user_dialog_shown()

            # delete the user
            RemoveUser.click_yes_remove_button()
            RemoveUser.wait_cannot_remove_user_dialog_disappear()

            if not VerifyUser.verify_user_not_exist(userGroup.name, userGroup.domainName, True):
                logger.warn("Not able to remove group %s" % userGroup.name)
                error += 1
            else:
                logger.info("Successfully removed %s" % userGroup.name)

    if error > 0:
        return False
    else:
        return True


def edit_current_session_user(user_obj):
    """ Edit Current Session User
        This functions allows you to edit current session user whoever users listed in user page retrieving data from data.xml
    """
    logger.info("Edit Current Session User...")
    user = test_data.get().currentSessionUser
    user = user[0]

    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    # Login with current session user credentials
    EditCurrentSessionUser.input_login_user_name(user.name)
    EditCurrentSessionUser.input_login_password(user.password)
    EditCurrentSessionUser.click_login_button()
    if EditCurrentSessionUser.wait_login_dashboard_shown(30, False):
        logger.info("Login Successful")
    else:
        logger.warn("Login Fail. Invalid username or password. Enter correct credentials and try again.")
        return False

    EditCurrentSessionUser.click_current_session_user_edit_button()

    EditCurrentSessionUser.wait_edit_user_dialog_shown()
    # Edit full name
    if user.has_property('fullname'):
        EditCurrentSessionUser.input_full_name(user.fullname)
    # Enter current password
    if user.has_property('password'):
        EditCurrentSessionUser.input_current_password(user.password)
    # Enter New password
    if user.has_property('newpassword'):
        EditCurrentSessionUser.input_new_password(user.newpassword)
        EditCurrentSessionUser.input_confirm_password(user.newpassword)
    # Enter confirm password
    if user.has_property('confirmpassword'):
        EditCurrentSessionUser.input_confirm_password(user.confirmpassword)

    # Edit email
    if user.has_property('email'):
        EditCurrentSessionUser.input_email(user.email)
    # Edit office phone number
    if user.has_property('officephone'):
        EditCurrentSessionUser.input_office_phone(user.officephone)
    # Edit Mobile number
    if user.has_property('mobilephone'):
        EditCurrentSessionUser.input_mobile_phone(user.mobilephone)

    # Confirm Edit - Clicking OK
    EditCurrentSessionUser.click_ok_button()
    EditCurrentSessionUser.wait_edit_user_dialog_disappear()

    # Logging out
    logger.info("LOGOUT")
    EditCurrentSessionUser.click_logout_button()

    # Login with Current User if password has changed
    if user.has_property('newpassword'):
        logger.info("Login with new password")
        EditCurrentSessionUser.input_login_user_name(user.name)
        EditCurrentSessionUser.input_login_password(user.newpassword)
        EditCurrentSessionUser.click_login_button()
        if EditCurrentSessionUser.wait_login_dashboard_shown(30, False):
            logger.info("Changed Password of '%s' is verified Successfully" % user.name)
            # Logging out
            logger.info("LOGOUT")
            EditCurrentSessionUser.click_logout_button()
        else:
            logger.warn("Password verification of '%s' failed" % user.name)

    # Login with Administrator and verify edit
    logger.info("Login with Administrator")
    EditCurrentSessionUser.input_login_user_name(user.adminuser)
    EditCurrentSessionUser.input_login_password(user.adminpassword)
    EditCurrentSessionUser.click_login_button()
    if EditCurrentSessionUser.wait_login_dashboard_shown(30, False):
        logger.info("Administrator successfully logged in")
    else:
        logger.warn("Login Fail. Invalid username or password. Enter correct credentials and try again.")
        return False

    navigate()
    GeneralUserandGroups.click_user(user.name)
    VerifyUser.verify_user_title(user.name)
    VerifyUser.verify_user_login_name(user.name)
    if user.has_property("fullname"):
        VerifyUser.verify_user_full_name(user.fullname)
    if user.has_property("email"):
        VerifyUser.verify_user_email(user.email)
    if user.has_property("officephone"):
        VerifyUser.verify_user_office_phone(user.officephone)
    if user.has_property("mobilephone"):
        VerifyUser.verify_user_mobile_phone(user.mobilephone)

    return True


def userdata_validation(*user_obj):
    """ Verify User data

        The function validates the user data in the users and groups page.
        Example:
        | `userdata validation`      |     |
    """

    # retrieving data from data file
    if isinstance(user_obj, test_data.DataObj):
        user_obj = [user_obj]
    elif isinstance(user_obj, tuple):
        user_obj = list(user_obj)

    navigate()

    for user in user_obj:
        if user.name.lower() == "administrator" or user.has_property('domainName'):
            continue
        VerifyUser.verify_user_exist(user.name)
        GeneralUserandGroups.click_user(user.name)
        VerifyUser.verify_user_title(user.name)
        VerifyUser.verify_user_login_name(user.name)
        if user.has_property("fullname"):
            VerifyUser.verify_user_full_name(user.fullname)
        if user.has_property("email"):
            VerifyUser.verify_user_email(user.email)
        if user.has_property("officephone"):
            VerifyUser.verify_user_office_phone(user.officephone)
        if user.has_property("mobilephone"):
            VerifyUser.verify_user_mobile_phone(user.mobilephone)
    return True


def select_user(name):
    """ Select user from the users and groups page """

    navigate()
    VerifyUser.verify_user_exist(name)
    GeneralUserandGroups.click_user(name)


def remove_all_users():
    """ Removes all the user from Users and Groups Page """
    selenium2lib = ui_lib.get_s2l()

    if not selenium2lib._is_element_present(FusionUserandGroupsPage.ID_PAGE_LABEL):
        navigate()
#    status = []
    user_list = [ui_lib.get_text(u) for u in selenium2lib._element_find(FusionUserandGroupsPage.ID_ALL_USERNAME_LIST, False, False)]
    count = 0
    for user in user_list:
        user_obj = test_data.DataObj()
        logger._log_to_console_and_log_file(user)
        user_obj.add_property("name", user)
        user_obj = (user_obj)
        user_remove_status = remove_user(user_obj)
#        status.append(user_remove_status)

        if user_remove_status:
            if user not in ['administrator', 'technician']:
                logger._log_to_console_and_log_file("'{0}' User is deleted Successfully".format(user))
            else:
                logger._log_to_console_and_log_file("Can't or Shouldn't delete user - {0}'".format(user))
            count += 1
        else:
            logger.warn("Failed to delete user: {0}".format(user))
    if count == len(user_list):
        logger._log_to_console_and_log_file("All users deleted successfully from appliance")
        return True
    else:
        logger.warn("Failed to delete '{0}' users from appliance".format(len(user_list) - count))
        return False
