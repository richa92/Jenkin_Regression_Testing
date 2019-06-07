"""
Fusion SAN UI Keywords
"""
from FusionLibrary.ui.san import san


class FusionSanUIKeywords(object):
    """
    SAN page functions
    """
    def fusion_ui_navigate_to_san_page(self):
        """ Navigate to the SAN  page
        Example:
        | Fusion UI Navigate To SAN  Page |
        """
        san.navigate_to_san_page()

    def fusion_ui_san_change_tab(self, tab_name):
        """To change tab on SAN page to different value
            Example:
            | Fusion UI SAN Tab Change <tab name>|
        """
        return san.san_change_tab(tab_name)

    def fusion_ui_san_highlight_san(self, san_name):
        """Click on a specific SAN on SAN page
            Example:
            | Fusion UI SAN Highlight SAN  <san_name> |
        """
        return san.highlight_san(san_name)

    def fusion_ui_verify_section_on_san_screen(self, section_name):
        """validates that the section selected is at top of screen
            Example:
            | Fusion UI Verify Section on SAN screen <section name>|
        """
        return san.validate_section_on_san_screen(section_name)

    def fusion_ui_san_validate_default_tab(self):
        """Verify Default tab shown on screen
            Example:
            | Fusion UI SAN Validate Default Tab|
        """
        return san.validate_default_tab()

    def fusion_ui_san_validate_tabs(self):
        """Verify tabs shown on screen
            Example:
            | Fusion UI SAN Validate Tabs|
        """
        return san.validate_tabs()

    def fusion_ui_san_validate_main_heading(self, san_value):
        """Verify Default main heading for SAN screen
            Example:
            | Fusion UI SAN Validate Main Heading <san_value>|
        """
        return san.validate_default_main_heading(san_value)

    def fusion_ui_san_check_activity_message(self, activity):
        """Verify activity exists in activity pane at right SAN screen
            Example:
            | Fusion UI SAN Check Activity Message | ${activity}}|
        """
        return san.check_for_activity(activity)

    def fusion_ui_san_display_activity(self):
        """Display or toggle activity section on SAN screen
            Example:
            | Fusion UI SAN Display Activity |
        """
        return san.display_san_activity()

    def fusion_ui_san_endpoints_click_update(self):
        """Click Update button in SAN Endpoints Section
            Example:
            | Fusion UI SAN Endpoints Click Update |
        """
        return san.san_endpoints_click_update()

    def fusion_ui_click_san_map_level(self, maplevel):
        """Click level on Map section
            Example:
            | Fusion UI Click SAN Map Level |${maplevel} |
        """
        return san.click_san_map_level(maplevel)

    def fusion_ui_validate_SAN_map_level_page(self, pagetitle):
        """Validate map level page title on SAN
            Example:
            | Fusion UI Validate SAN Map Level Page |${pagetitle} |
        """
        return san.validate_san_page_title(pagetitle)

    # #########################################################################
    # SAN action menu functions
    # #########################################################################

    def fusion_ui_open_san_actions_edit_dialog(self):
        """To open SAN actions menu, edit dialog
            Example:
            | Fusion UI Open Actions Edit Dialog |
        """
        return san.open_san_actions_edit_dialog_page()

    def fusion_ui_san_actions_validate(self):
        """validate the san actions menu options
            Example:
            | Fusion UI SAN Actions Validate|
        """
        return san.san_actions_validate()

    def fusion_ui_san_open_action(self, action_name):
        """Click Actions menu and choose action
            Example:
            | Fusion UI SAN Open Actions | ${action} |
        """
        return san.open_san_action(action_name)

    def fusion_ui_san_verify_general_section_titles(self):
        """Validate titles in General section
            Example:
            | Fusion UI san Verify General Section Titles |
        """
        return san.validate_general_section_titles()

    def fusion_ui_san_endpoints_user_input_filter(self, filter_name, values):
        """In SAN endpoints filter box, enter data
            Example:
            | Fusion UI SAN Endpoints User Input Filter | ${filter_name} ${values} |
        """
        return san.add_user_input_filter(filter_name, values)

    def fusion_ui_san_endpoints_validate_filter(self, line_count):
        """On SAN endpoints section, validate data is filtered
            Example:
            | Fusion UI SAN Endpoints Validate Filter | ${filter_name} ${values} |
        """
        return san.validate_filter(line_count)

    def fusion_ui_san_endpoints_validate_filter_message(self, msg):
        """On SAN endpoints section, validate filter message returned
            Example:
            | Fusion UI SAN Endpoints Validate Filter Message | ${msg} |
        """
        return san.validate_filter_message(msg)

    def fusion_ui_san_endpoints_click_download(self):
        """On SAN endpoints section, click Download endpoints button
            Example:
            | Fusion UI SAN Endpoints Click Download |
        """
        return san.endpoints_click_download()

    def fusion_ui_verify_san_actions_unauthorized_users(self, user):
        """Validate SAN Actions unauthorized users
            Example:
            | Fusion UI Verify San Actions Unauthorized Users |${user} |
        """
        return san.verify_san_actions_unauthorized_users(user)

    # #########################################################################
    # SAN edit page functions
    # #########################################################################

    def fusion_ui_open_san_zoning_edit_dialog(self):
        """Click Edit under Zoning Policy
            Example:
            | Fusion UI Open SAN Zoning Edit Dialog |
        """
        return san.open_san_zoning_edit_dialog()

    def fusion_ui_close_san_zoning_edit_dialog(self):
        """Click and close Edit SAN Dialog
            Example:
            | Fusion UI Close SAN Zoning Edit Dialog |
        """
        return san.close_edit_san_dialog()

    def fusion_ui_san_verify_edit_yes_message(self):
        """Validate message that appears on edit san screen
            if automate zoning = yes
            Example:
            | Fusion UI Verify Edit Yes message |
        """
        return san.validate_edit_yes_message()

    def fusion_ui_san_verify_edit_no_message(self):
        """Validate message that appears on edit san screen
            if automate zoning = no
            Example:
            | Fusion UI Verify Edit No message |
        """
        return san.validate_edit_no_message()

    def fusion_ui_san_edit_click_ok(self):
        """Click ok button on edit SAN dialog
            Example:
            | Fusion UI Edit SAN Click OK |
        """
        return san.edit_san_click_ok()

    def fusion_ui_san_edit_click_cancel(self):
        """Click cancel on edit san zoning page
            Example:
            | Fusion UI SAN Edit Click Cancel |
        """
        return san.edit_san_click_cancel()

    def fusion_ui_san_edit_set_automate_zoning(self, zone_value):
        """Change automate zoning to yes or no
            Example:
            | Fusion UI Set Automate Zoning  <zone_value> |
        """
        return san.set_edit_san_automate_zoning(zone_value)

    def fusion_ui_san_edit_set_zoning_policy(self, zone_policy):
        """Change zoning policy values
            Example:
            | Fusion UI Set Zoning Policy <zone_policy> |
        """
        return san.set_edit_san_zoning_policy(zone_policy)

    def fusion_ui_san_edit_set_use_alias(self, use_alias):
        """Change use alias value
            Example:
            | Fusion UI SAN Edit Set Use Alias <use_alias> |
        """
        return san.set_edit_san_use_alias(use_alias)

    def fusion_ui_san_edit_set_zone_name_format(self, zone_name):
        """Change zone name format value
            Example:
            | Fusion UI SAN Edit Set Zone Name Format <zone_name> |
        """
        return san.set_edit_san_zone_name_format(zone_name)

    def fusion_ui_san_edit_check_for_error(self):
        """Check that there is no error on the san page
            Example:
            | Fusion UI Set Zoning Policy <zone_policy> |
        """
        return san.check_for_error()

    def fusion_ui_san_verify_automate_zoning(self, zone_value):
        """validates that automated zoning is the value expected
            Example:
            | Fusion UI SAN Verify Automate Zoning <zone_value>|
        """
        return san.validate_automate_zoning(zone_value)

    def fusion_ui_san_verify_zoning_policy(self, zoning_policy):
        """validates that zoning policy is the value expected
            Example:
            | Fusion UI Verify Zoning Policy <zoning policy>|
        """
        return san.validate_zoning_policy(zoning_policy)

    def fusion_ui_san_verify_use_alias(self, use_alias):
        """Verify use alias value on screen is correct
            Example:
            | Fusion UI SAN Verify Use Alias <use_alias> |
        """
        return san.validate_use_alias(use_alias)

    def fusion_ui_san_edit_clear_out_input_box(self, field_name):
        """Clear out input box on SAN edit screen with field_name
            Example:
            | Fusion UI SAN Edit Clear Out Input Box <field name> |
        """
        return san.clear_out_san_edit_input_box(field_name)

    def fusion_ui_san_edit_validate_for_errors(self, err_type):
        """Validate the error passed in is on the screen
            Example:
            | Fusion UI SAN Edit Validate For Errors | ${err_type} |
        """
        return san.validate_for_edit_san_errors(err_type)

    def fusion_ui_san_validate_report(self, san_name):
        """Validate the heading and message on the Unexpected Zoning Report
            Example:
            | Fusion UI SAN Validate Report | ${san} |
        """
        return san.validate_for_report(san_name)

    def fusion_ui_click_san_edit_help(self):
        """Click help link on edit san screen
            Example:
            | Fusion UI Click SAN edit help |
        """
        return san.click_san_edit_help()

    # #########################################################################
    # SAN  page filter functions
    # #########################################################################

    def fusion_ui_san_validate_all_statuses_filter(self):
        """Validate All Statuses on the SAN Page
            Example:
            | Fusion UI SAN Validate All Statuses filter |
        """
        return san.validate_all_statuses_filter()

    def fusion_ui_san_validate_all_states_filter(self):
        """Validate All States on the SAN Page
            Example:
            | Fusion UI SAN Validate All States filter |
        """
        return san.validate_all_states_filter()
