""" SAN Manager UI Keywords """
from FusionLibrary.ui.sanmanager import sanmanagers


class FusionSanmanagerUIKeywords(object):
    """
    SAN Managers page functions
    """

    def fusion_ui_navigate_to_san_managers_page(self):
        """ Navigate to the san managers page
        Example:
        | Fusion UI Navigate To SAN Managers Page |
        """
        sanmanagers.navigate()

    def fusion_ui_san_manager_change_tab(self, tab_name):
        """To change tab on SAN manager page to different value
            Example:
            | Fusion UI SAN Manager Change Tab <tab name>|
        """
        return sanmanagers.sanmgr_change_tab(tab_name)

    def fusion_ui_add_san_manager(self, version, *sanmanager_obj):
        """To add SAN Manager to the appliance
            Example:
            | Fusion UI Add San Manager      | @{sanmanager}|
        """
        return sanmanagers.add_san_managers(version, *sanmanager_obj)

    def fusion_ui_remove_san_manager(self, *sanmanager_obj):
        """ remove san manager from fusion appliance
            Example:
            | Fusion UI remove san manager | @{sanmanager}|
        """
        return sanmanagers.remove_san_managers(*sanmanager_obj)

    def fusion_ui_remove_all_san_managers(self):
        """ remove all san managers from fusion appliance
            Example:
            | Fusion UI remove all san managers |
        """
        return sanmanagers.remove_all_san_managers()

    def fusion_ui_edit_san_manager(self, *sanmanager_obj):
        """To add SAN Manager to the appliance
            Example:
            | Fusion UI Edit San Manager      | @{sanmanager}|
        """
        return sanmanagers.edit_san_managers(*sanmanager_obj)

    def fusion_ui_refresh_san_manager(self, *sanmanager_obj):
        """To add SAN Manager to the appliance
            Example:
            | Fusion UI Refresh San Manager      | @{sanmanager}|
        """
        return sanmanagers.refresh_san_managers(*sanmanager_obj)

    def fusion_ui_navigate_to_san_managers_page_negative(self):
        """ Navigate to the san managers page
        Example:
        | Fusion UI Navigate To SAN Managers Page Negative |
        """
        sanmanagers.navigate_to_san_managers_page_negative()

    def fusion_ui_open_add_san_manager_dialog(self):
        """To open add san manger dialog
            Example:
            | Fusion UI Add San Manager Dialog |
        """
        return sanmanagers.open_add_san_manager_dialog_page()

    def fusion_ui_close_add_san_manager_dialog(self):
        """To close add san manger dialog
            Example:
            | Fusion UI Close San Manager Dialog |
        """
        return sanmanagers.close_add_san_manager_dialog()

    def fusion_ui_add_san_manager_click_type(self, stype):
        """To click type in add san manager dialog
            Example:
            | Fusion UI Add San Manager Click Type |
        """
        return sanmanagers.add_san_manager_click_type(stype)

    def fusion_ui_add_san_manager_click_add(self):
        """To click add button in add san manager dialog
            Example:
            | Fusion UI Add San Manager Click ADD |
        """
        return sanmanagers.add_san_manager_click_add()

    def fusion_ui_add_san_manager_click_add_plus(self):
        """To click add plus button in add san manager dialog
            Example:
            | Fusion UI Add San Manager Click ADD + |
        """
        return sanmanagers.add_san_manager_click_add_plus()

    def fusion_ui_add_san_manager_click_cancel(self):
        """Click cancel on add san manager dialog
            Example:
            | Fusion UI Add San Manager Click Cancel |
        """
        return sanmanagers.add_san_manager_click_cancel()

    def fusion_ui_san_manager_user_input_host_name(self, host):
        """To input values in the hostname field on screen
            Example:
            | Fusion UI San Manager user input host name "values" |
        """
        return sanmanagers.add_user_input_host_name(host)

    def fusion_ui_san_manager_validate_hostname_character_only(self):
        """Validate hostname should contain character only
            Example:
            | Fusion UI San Manager Validate Hostname Character Only |
        """
        return sanmanagers.validate_hostname_should_contain_character_only()

    def fusion_ui_san_manager_user_input_username(self, username):
        """To input values in the username field on screen
            Example:
            | Fusion UI San Manager user input username | ${username} |
        """
        return sanmanagers.add_user_input_username(username)

    def fusion_ui_san_manager_user_input_password(self, password):
        """To input values in the password field on screen
            Example:
            | Fusion UI San Manager user input password | ${password} |
        """
        return sanmanagers.add_user_input_pswd(password)

    def fusion_ui_validate_unable_add_san_manager(self, err_type):
        """Validate Unable to Add SAN manager error
            Example:
            | Fusion UI Validate Unable Add SAN Manager |${err_type} |
        """
        return sanmanagers.validate_unable_add_san_manager(err_type)

    def fusion_ui_san_manager_validate_port_numerics_only(self):
        """Validate port should contain numerics within a range only
            Example:
            | Fusion UI san manager Validate Port Numerics Only |
        """
        return sanmanagers.validate_port_should_contain_numeric_only()

    def fusion_ui_san_manager_user_input_port(self, port):
        """To input values in the port field on screen
            Example:
            | Fusion UI san manager user input port "values" |
        """
        return sanmanagers.add_user_input_port(port)

    def fusion_ui_san_manager_validate_field_required(self):
        """Validate field required message appears
            Example:
            | Fusion UI san manager Validate Field Required" |
        """
        return sanmanagers.validate_field_required()

    def fusion_ui_san_manager_validate_tabs(self):
        """Validate tab required message appears
            Example:
            | Fusion UI san manager Validate tab Required" |
        """
        return sanmanagers.validate_tab_required()

    def fusion_ui_san_manager_validate_managedsans_count_link(self):
        """Validate link required message appears
            Example:
            | Fusion UI san manager Validate managedsans count link" |
        """
        return sanmanagers.verify_sanmanager_managedsans_count_link()

    def fusion_ui_san_manager_validate_managedsan_link(self):
        """Validate link required message appears
            Example:
            | Fusion UI san manager Validate managedsans count link" |
        """
        return sanmanagers.verify_sanmanager_managedsan_link()

    def fusion_ui_san_manager_validate_san_managers_count_dashboard(self, *sanmanager_obj):
        """Validate link required message appears
            Example:
            | Fusion UI san manager Validate managedsans count from dashboard" |
        """
        return sanmanagers.verify_sanmanagers_count_dashboard(*sanmanager_obj)

    def fusion_ui_san_manager_action_menu_set(self, action_option):
        """Select an action from the action menu
            Example:
            | Fusion UI san manager action menu set {action option} |
        """
        return sanmanagers.sanmanager_action_menu_set(action_option)

    def fusion_ui_highlight_san_manager(self, sanmgr_value):
        """Highlight san manager specified at left menu
            Example:
            | Fusion UI highlight san manager| ${sanmgr_value}
        """
        return sanmanagers.highlight_san_manager(sanmgr_value)

    def fusion_ui_san_manager_edit__user_input_password(self, password):
        """To input values in the password field on screen
            Example:
            | Fusion UI San Manager user input password | ${password} |
        """
        return sanmanagers.edit_user_input_pswd(password)

    def fusion_ui_san_manager_edit__user_input_username(self, username):
        """To input values in the password field on screen
            Example:
            | Fusion UI San Manager user input password | ${password} |
        """
        return sanmanagers.edit_user_input_username(username)

    def fusion_ui_san_manager_edit__user_input_hostname(self, hostname):
        """To input values in the password field on screen
            Example:
            | Fusion UI San Manager user input password | ${password} |
        """
        return sanmanagers.edit_user_input_hostname(hostname)

    def fusion_ui_edit_san_manager_click_ok(self):
        """Click cancel on add san manager dialog
            Example:
            | Fusion UI Add San Manager Click Cancel |
        """
        return sanmanagers.edit_san_manager_click_ok()

    def fusion_ui_edit_san_manager_click_cancel(self):
        """Click cancel on add san manager dialog
            Example:
            | Fusion UI Add San Manager Click Cancel |
        """
        return sanmanagers.edit_san_manager_click_cancel()

    def fusion_ui_validate_unable_to_edit_san_manager(self, err_type):
        """Validate Unable to Add SAN manager error
            Example:
            | Fusion UI Validate Unable Edit SAN Manager |${err_type} |
        """
        return sanmanagers.validate_unable_to_edit_san_manager(err_type)

    def fusion_ui_create_users(self, *sanmanager_obj):
        """Create a fusion user
            Example:
            | Fusion UI Create User
        """
        return sanmanagers.create_oneview_users(*sanmanager_obj)

    def fusion_ui_verify_san_manager_actions_unauthorized_users(self, user):
        """Validate unauthorized user error on san manager screen
            Example:
            | Fusion UI Verify SAN manager actions unauthorized users |${user} |
        """
        return sanmanagers.verify_san_manager_actions_unauthorized_users(user)

    def fusion_ui_click_map_level(self, maplevel):
        """Click level on Map section
            Example:
            | Fusion UI Click Map Level |${maplevel} |
        """
        return sanmanagers.click_map_level(maplevel)

    def fusion_ui_validate_map_level_page(self, pagetitle):
        """Validate Map level page titel on san manager
            Example:
            | Fusion UI Validate Map Level Page |${page_title} |
        """
        return sanmanagers.validate_page_title(pagetitle)

    def fusion_ui_click_san_manager_edit_help(self):
        """Click help link on edit san manager screen
            Example:
            | Fusion UI Click SAN manager edit help |
        """
        return sanmanagers.click_san_manager_edit_help()
