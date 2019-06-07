'''
RoboGalaxyLibrary Fusion UI keywords

'''
from FusionLibrary.ui.storage import drive_enclosures
from FusionLibrary.ui.servers import enclosures
from FusionLibrary.ui.servers import enclosuregroups
from FusionLibrary.ui.servers import logicalenclosures
from FusionLibrary.ui.servers import serverprofiles
from FusionLibrary.ui.servers import serverprofiletemplates
from FusionLibrary.ui.servers import serverhardware
from FusionLibrary.ui.servers import serverhardwaretypes
from FusionLibrary.ui.hypervisors import vcenter
from FusionLibrary.ui.networking import logicalinterconnectgroups
from FusionLibrary.ui.networking import networks
from FusionLibrary.ui.networking import networksets
from FusionLibrary.ui.networking import logicalinterconnects
from FusionLibrary.ui.networking import interconnects
from FusionLibrary.ui.networking import logicalswitches
from FusionLibrary.ui.networking import logicalswitchgroups
from FusionLibrary.ui.networking import switches
from FusionLibrary.ui.usersandgroups import usersandgroups
from FusionLibrary.ui.general import first_time_wizard, rebranding
from FusionLibrary.ui.general import login_page
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.general import activity
from FusionLibrary.ui.general import dashboard
from FusionLibrary.ui.general import firmwarebundles
from FusionLibrary.ui.general import reports
from FusionLibrary.ui.facilities import datacenters
from FusionLibrary.ui.facilities import racks
from FusionLibrary.ui.facilities import powerdeliverydevice
from FusionLibrary.ui.facilities import unmanageddevices
from FusionLibrary.ui.settings import settings
from FusionLibrary.ui.storage import storagesystems
from FusionLibrary.ui.storage import storagepools
from FusionLibrary.ui.storage import volumesets
from FusionLibrary.ui.storage import storagetemplates
from FusionLibrary.ui.storage import volumes
from FusionLibrary.ui.storage import sans
from FusionLibrary.ui.settings import networking
from FusionLibrary.ui.settings import timeandlocale
from FusionLibrary.ui.settings import supportdump
from FusionLibrary.ui.settings import licenses
from FusionLibrary.ui.settings import scopes
from FusionLibrary.ui.general import customizedashboard
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.base import ScreenShotType
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.settings import notifications


class FusionUIKeywords(object):

    """ Fusion UI Keywords
    """
    __metaclass__ = ScreenShotType

    # #########################################################################
    # First Time Wizard page functions
    # #########################################################################

    def fusion_ui_configure_first_time_wizard(self):
        """ Perform the first time wizard configuration
        Example:
        | Fusion UI Configure First Time Wizard |
        """
        first_time_wizard.fusion_configure_first_time_wizard()

    # #########################################################################
    # Base page functions
    # #########################################################################
    def fusion_ui_verify_current_view(self, expected_view_name):
        """Verify that the current view is the expected view.
        Example:
        Fusion UI Verify Current View  Overview"""
        FusionUIBase.verify_view_by_name(expected_view_name)

    def fusion_ui_click_item_from_master_table(self, item_name):
        """ Click an item with provided name from the table
        that is on the left side of every page in the UI
        Example:
        Fusion UI Click Item From Master Table   0000A66101
        """
        FusionUIBase.click_item_from_master_table(item_name)

    def fusion_ui_logout_of_appliance(self):
        """ Log out of the Fusion appliance
        Example:
        | Fusion UI |
        """
        base_page.logout()

    def help_on_this_page_header(self):
        """ Compare the help page title with the page header
        Example:
        | Help On This Page Header |
        """
        base_page.help_on_this_page_header()

    def fusion_ui_search(self, search_fusion_page, search_keyword):
        """ Search for a Keyword in Fusion
        Example:
        | Fusion UI Search | Enclosures | MyEnclosure |
        """
        blnSearch = base_page.search(search_fusion_page, search_keyword)
        return blnSearch

    def fusion_ui_navigate_to_page(self, page_name):
        """ Gets the page name and navigates to that page
        Example:
        | Activity | Dashboard |
        """
        page_label = "xpath=//div[@class='hp-page-label']/h1[text()='%s']" % page_name
        link = "link=%s" % page_name
        if page_name.lower() == "dashboard":
            count = "css=span.hp-count"
            base_page.navigate_base(page_label, link, count)
        elif page_name.lower() == "settings":
            settings.navigate()
        else:
            count = "css=span.hp-page-item-count"
            base_page.navigate_base(page_label, link, count)

    def fusion_ui_get_errors_on_form(self, form_id):
        """
        Function to get all the errors seen on the form - Common for Create and edit operations
        Return error string separated by '\t' if errors are present else returns None

        Example :  error_String=   fusion_ui_get_errors_on_form    ${form_id}

        """
        return base_page.get_errors_on_form(form_id)

    # #########################################################################
    # Login page functions
    # #########################################################################
    def fusion_ui_login_to_appliance(self, user_name):
        """ Login to the fusion appliance
        Example:
        | Fusion UI Login to Appliance | Administrator |
        """
        return login_page.login(user_name)

    def fusion_ui_check_for_nec_at_login_page(self):
        """ Fusion UI Check For NEC at Login Page
        Example:

        | Fusion UI Check For NEC at Login Page |
        """

        return rebranding.product_name()

    # #########################################################################
    # Help page functions
    # #########################################################################
    def fusion_ui_help(self):
        """ Help icon appliance
        Example:

        | Fusion UI Help |
        """

        return rebranding.rebrand_help()

    # #########################################################################
    # Dashboard page functions
    # #########################################################################
    def fusion_ui_remove_dashboard_panels(self, *dashboard_panels):
        """ Remove dashboard panel according to the date in the xml file
        Example:
        | Fusion UI remove dashboard panel|   @{dashboardpanels}|
        """
        return customizedashboard.remove_dashboard_panels(*dashboard_panels)

    def fusion_ui_add_dashboard_panels(self, *dashboard_panels):
        """ Add dashboard panel according to the date in the xml file
        Example:
        | Fusion UI add dashboard panel|   @{dashboardpanels}|
        """
        return customizedashboard.add_dashboard_panels(*dashboard_panels)

    def fusion_ui_navigate_to_dashboard_page(self):
        """ Navigate to the dashboard page
        Example:
        | Fusion UI Navigate to Dashboard Page |
        """
        dashboard.navigate()

    def fusion_ui_create_dashboard(self, *dashboards):
        """ Create dashboard component
        Example:
        | Fusion UI create dashboard|   @{dashboards}|
        """
        return dashboard.create_dashboard(dashboards)

    def fusion_ui_edit_dashboard(self, *dashboards):
        """ Edit dashboard component
        Example:
        | Fusion UI edit dashboard|   @{dashboards}|
        """
        return dashboard.edit_dashboard(dashboards)

    def fusion_ui_delete_dashboard(self, *dashboards):
        """ Delete dashboard  component
        Example:
        | Fusion UI delete dashboard|   @{dashboards}|
        """
        return dashboard.delete_dashboard(dashboards)

    def fusion_ui_validate_c7000_pause_flood_alert(self, alert_message, *interconnect_obj):
        """Verify Pause flood alert
           This function verifies the pause flood alert on the interconnect page
        Example:
        | Fusion UI validate c7000 pause flood alert|   @{dashboards}|
        """
        return interconnects.validate_c7000_pause_flood_alert(alert_message, interconnect_obj)

    def fusion_ui_dashboard_should_exist(self, *dashboards):
        """ Verify if dashboard component exist
        Example:
        | Fusion UI dashboard should exist|   @{dashboards}|
        """
        return dashboard.verify_dashboard_exist(dashboards)

    def fusion_ui_validate_dashboard_graphs(self, *component_obj):
        """ Validate dashboard graphs
        example:
        | Fusion UI Validate dashboard graphs|    @{component_obj}|
        """
        return dashboard.validate_dashboard_graphs(component_obj)

    def fusion_ui_verify_dashboard_component_status(self, *component_obj):
        """ Verify dashboard component status
             Example:
             Fusion UI Verify Dashboard Component Status    |@{component_obj}|
        """
        return dashboard.verify_dashboard_component_status(component_obj)

    # #########################################################################
    # Activity page functions
    # #########################################################################
    def fusion_ui_navigate_to_activity_page(self):
        """ Navigate to the Activity page
        Example:
        | Fusion UI Navigate To Activity Page |
        """
        activity.navigate()

    def fusion_ui_assign_user_to_activity(self, *activities):
        """ Assign a user to particular activities
        Example:
        | Fusion UI Assign User To Activity | @{activities} |
        """
        return activity.assign_user(activities)

    def fusion_ui_clear_activity(self, *activities):
        """ Clear activities
        Example:
        | Fusion UI Clear Activity | @{activity list} |
        """
        return activity.clear_activity(activities)

    def fusion_ui_restore_activity(self, *activities):
        """ Restore a deleted activity
        Example:
        | Fusion UI Restore Activity | @{activity list} |
        """
        return activity.restore_activity(activities)

    def fusion_ui_assign_activity_to_user(self, actname, resource, timestamp, assignusername):
        """ This function is to assign the user to the given activity.
        This function is written wrt E2E UC3.During Runtime,dynamically it is taking parameters through script.
        To work explicitly need to pass all the four parameters.
        Example:
        _assignuser_name('Update started for interconnect CC-2-LI', 'CC-2-LI', 'Today 10.45 am', 'NetAdmin')
        """
        return activity._assignuser_name(actname, resource, timestamp, assignusername)

    def fusion_ui_verify_owner_Activity(self, actname, resource, timestamp, assignusername):
        """ This function is to verify the user name once the activity is assigned to any user.
        This function is written wrt E2E UC3.During Runtime,dynamically it is taking parameters through script.
        To work explicitly need to pass all the four parameters.
        Example:
        _verify_activity_owner('Update started for interconnect CC-2-LI', 'CC-2-LI', 'Today 10.45 am', 'NetAdmin')
        """
        return activity._verify_activity_owner(actname, resource, timestamp, assignusername)

    def fusion_ui_is_element_present_activity_page_without_time(self, elementtocheck, message):
        """ This function is to verify the activity in activity page.
        This function is written wrt E2E UC3.it will work only when we pass all the two parameters.
        Example:
        _is_element_present_activity_page_without_time('Firmware Update success', 'CC-2-LI')
        """
        return activity._is_element_present_activity_page_without_time(elementtocheck, message)

    def fusion_ui_is_element_present_in_activity_page(self, timestamp, elementtocheck, message):
        """ This function is to verify the activity in activity page.
        This function is written wrt E2E UC3.it will work only when we pass all the three parameters.
        Example:
        | Fusion UI Is Element Present In Activity Page | ${timestamp} | ${elementtocheck} | ${message} |
        """
        return serverprofiles._is_element_present_inactivity_page(message, elementtocheck, timestamp)

    def fusion_ui_verify_alert_page_details(self, activityname, resource, owner):
        """ This function is to validate activity page.
        Example:
        | Fusion UI Verify Alert Page Details | ${activityname} | ${resource} | ${owner} |
        """
        return activity.verify_alert_page_details(activityname, resource, owner)

    def fusion_ui_change_activity_state_in_activity_page(self, *activity_obj):
        """ Change activity state
        This function is to change activity state from 'active' to 'Cleared' State in Activity Page
        Example:
        | Fusion UI Change Activity State In Activity Page | @{activity_obj} |
        """
        return activity.change_activity_state_in_activity_page(activity_obj)

    def fusion_ui_verify_alertpage_information(self, *activity_obj):
        """
            Displays critical alerts based on state mentioned in test data.
            Validates alert present in OV or not
            Example:
            | Fusion ui verify alertpage information | @{activity_obj} |
        """
        return activity.verify_alertpage_information(activity_obj)

    def fusion_ui_verify_latest_activity(self):
        """
            Displays critical alerts based on state mentioned in test data.
            Validates alert present in OV or not
            Example:
            | Fusion UI Verify Latest Activity | @{activity_obj} |
        """
        return activity.get_latest_activity()

    # #########################################################################
    # Firmware Bundles page functions
    # #########################################################################
    def fusion_ui_navigate_to_firmware_bundles_page(self):
        """ Navigate to the Firmware Bundles Page
        Example:
        | Fusion UI Navigate To Firmware Bundles Page|
        """
        firmwarebundles.navigate()

    def fusion_ui_add_firmware_bundle(self, *objfwbundle):
        """ Add firmware bundle(s)
        Example:
        | Fusion UI Add Firmware Bundle | @{firmware bundles} |
        """
        return firmwarebundles.add_firmware_bundle(objfwbundle)

    def fusion_ui_add_latest_firmware_bundle(self, *objfwbundle):
        """ Add latest firmware bundle(s) by filter(s)
        Example:
        | Fusion UI Add Latest Firmware Bundle | @{firmware bundle filters}  |
        """
        return firmwarebundles.add_latest_firmware_bundle(objfwbundle)

    def fusion_ui_validate_firmware_bundle_component(self, *objfwbundle):
        """ Validate Firmware Bundle Component
        Example:
        | Fusion UI Validate Firmware Bundle Component | @{firmware bundles}  |
        """
        return firmwarebundles.validate_firmware_bundle_component(objfwbundle)

    def fusion_ui_delete_firmware_bundle(self, *objfwbundle):
        """ Delete a firmware bundle
        Example:
        | Fusion UI Delete Firmware Bundle | @{firmware bundles}
        """
        return firmwarebundles.delete_firmware_bundle(objfwbundle)

    def fusion_ui_validate_cannot_delete_firmware_bundle(self, *objfwbundle):
        """ Delete a firmware bundle
        Example:
        | Fusion Ui Validate Cannot Delete Firmware Bundle | @{firmware bundles}
        """
        return firmwarebundles.validate_cannot_delete_firmware_bundle(objfwbundle)

    def fusion_ui_validate_firmware_bundle_task_error(self, *objfwbundle):
        """ Validate Firmware Bundle Task Error
        Example:
        | Fusion Ui Validate Firmware Bundle Task Error | @{firmware bundles}
        """
        return firmwarebundles.validate_firmware_bundle_task_error(objfwbundle)

    # #########################################################################
    # Server Profiles page functions
    # #########################################################################
    def fusion_ui_navigate_to_server_profiles_page(self):
        """ Navigate to the Server Profiles Page
        Example:
        | Fusion UI Navigate To Server Profiles Page |
        """
        serverprofiles.navigate()

    def fusion_ui_select_server_profiles(self, profileNames):
        """ Select Server Profiles
        Example:
        | Fusion UI Select Server Profiles | @{Server Profile Names} |
        """
        return serverprofiles.select_server_profile(profileNames)

    def fusion_ui_verify_server_profile_status(self, expectedstatus, *profile_obj):
        """ Verify that server's status is OK
        Example:
        | Fusion UI Verify Server Profile Status |
        """
        return serverprofiles.verify_server_profile_status(expectedstatus, *profile_obj)

    def fusion_ui_validate_server_profile_status(self, expectedstatus, *profile_obj):
        """ Verify that server profile status
        Example:
        | Fusion UI Validate Server Profile Status |
        """
        return serverprofiles.validate_server_profile_status(expectedstatus, *profile_obj)

    def fusion_ui_validate_server_connections_error_state(self, *profile_obj):
        """ Verify that server's status is connections error
        Example:
        | Fusion UI Validate Server Connections Error State |
        """
        return serverprofiles.validate_server_profile_connections_error_state(*profile_obj)

    def fusion_ui_verify_server_profile_power_status(self, expectedpowerstatus, *profile_obj):
        """ Verify that the server's power status matches the expected state
           Note: the expected state will perform a text match with the status passed in.
        Example:
        | Fusion UI Verify Server Profile Power Status |
        """
        return serverprofiles.verify_server_profile_power_status(expectedpowerstatus, *profile_obj)

    def fusion_ui_validate_server_profile_consistency_state(self, *profile_obj):
        """ Verify that the server profile's state matches the expected state
        Example:
        | Fusion UI Verify Server Profile Consistency State | @{profiles} |
        """
        return serverprofiles.validate_server_profile_consistency_state(profile_obj)

    def fusion_ui_verify_server_profile_bios_settings_info(self, *profile_obj):
        """ Verify that the server's BIOS settings info for Server profile
        Example:
        | Fusion UI Verify Server BIOS Settings Info |
        """
        return serverprofiles.verify_server_profile_bios_settings_info(profile_obj)

    def fusion_ui_verify_server_profile_boot_settings_info(self, *profile_obj):
        """ Verify that the server's Boot Settings info for server profile
        Example:
        | Fusion UI Verify Server Profile Boot Settings info |
        """
        return serverprofiles.verify_server_profile_boot_settings_info(profile_obj)

    def fusion_ui_verify_server_profile_general_info(self, *profile_obj):
        """ Verify that the server's general information such as server hardware, server hardware type and enclosure group matches the expected value
        Example:
        | Fusion UI Verify Server Profile General Info |
        """
        return serverprofiles.verify_server_profile_general_info(profile_obj)

    def fusion_ui_verify_server_profile_connections_info(self, *profile_obj):
        """ Verify that the server's connections information such as ID, Name. Address, Network, Port and Boot
        Example:
        | Fusion UI Verify Server Profile Connections Info |
        """
        return serverprofiles.verify_server_profile_connections_info(profile_obj)

    def fusion_ui_verify_server_profile_advanced_info(self, *profile_obj):
        """ Verify that the server's advanced information such as UUID, Mac addresses, WWN addresses and Hide unused FlexNICs
        Example:
        | Fusion UI Verify Server Profile Advanced Info |
        """
        return serverprofiles.verify_server_profile_advanced_info(profile_obj)

    def fusion_ui_verify_server_profile_san_storage_info(self, *profile_obj):
        """ Verify that the server's SAN storage information
        Example:
        | Fusion UI Verify Server Profile SAN Storage Info | @{profiles}
        """
        return serverprofiles.verify_server_profile_san_storage_info(profile_obj)

    def fusion_ui_verify_server_profile_local_storage_info(self, *profile_obj):
        """ Verify that the server's Local storage information
        Example:
        | Fusion UI Verify Server Profile Local Storage Info | @{profiles}
        """
        return serverprofiles.verify_server_profile_local_storage_info(profile_obj)

    def fusion_ui_verify_server_profile_zoned_drive_exist(self, *profile_obj):
        """ Verify that the server's zoned drive created
        Example:
        | Fusion UI Verify Server Profile zoned drive exist | @{profiles}
        """
        return serverprofiles.verify_server_profile_zoned_drive_exist(profile_obj)

    def fusion_ui_verify_server_profile_zoned_drive_deleted(self, *zoneddrives):
        """ Verify that the server's zoned drive deleted
        Example:
        | Fusion UI Verify Server Profile zoned drive deleted | @{profiles}
        """
        return serverprofiles.verify_server_profile_zoned_drive_deleted(zoneddrives)

    def fusion_ui_server_profile_get_zoned_info(self, *profile_obj):
        """ Get server profile's JBOD details
        Example:
        | Fusion UI Server Profile get zoned drive info | @{profiles}
        """
        return serverprofiles.get_zoned_drive_info(profile_obj)

    def bak_fusion_ui_verify_server_profile_general_info(self, *profile_obj):
        """ Verify that the server's general information such as server hardware, server hardware type and enclosure group matches the expected value
        Example:
        | Fusion UI Verify Server Profile General Info |
        """
        return serverprofiles.verify_server_profile_general_info(*profile_obj)

    def bak_fusion_ui_create_server_profile(self, *profile_obj):
        """ Create a server profile
        Example:
        | Fusion UI Create Server Profile | @{Profiles} |
        """
        return serverprofiles.bak_create_server_profile(profile_obj)

    def fusion_ui_create_server_profile(self, *profile_obj):
        """ Create a server profile
        Example:
        | Fusion UI Create Server Profile | @{Profiles} |
        """
        return serverprofiles.create_server_profile(profile_obj)

    def fusion_ui_create_server_profile_async(self, *profile_obj):
        """ Create a server profile
        Example:
        | Fusion UI Create Server Profile Async | @{Profiles} |
        """
        return serverprofiles.create_server_profile_async(profile_obj)

    def fusion_ui_create_simple_server_profile_by_server_hardware(self, profile_name, server_name):
        """ Create a simplest server profile from 'Create profile' link on Server Hardware page
        Example:
        | Fusion UI Create Simple Server Profile By Server Hardware | ${profile name} | ${server name}
        """
        return serverprofiles.create_simple_server_profile_by_server_hardware(profile_name=profile_name, server_name=server_name)

    def fusion_ui_copy_server_profile(self, *profile_obj):
        """ Copy a server profile
        Example:
        | Fusion UI Copy Server Profile | @{Profiles} |
        """
        return serverprofiles.copy_server_profile(profile_obj)

    def fusion_ui_get_type_of_server_hardware(self, server_name):
        """ Get a server hardware's type,
            especially for BL server that its hardware type is unknown about 'xxx 1' or 'xxx 2',
            e.g., for an specified server, its type in OneView can be 'BL460c Gen8 1' sometimes, but also can be 'BL460c Gen8 2' other times,
            this keyword is to get its exact type for a specified server at a specified moment.
        Example:
        | Fusion UI Get Type Of Server Hardware | ${server name} |
        """
        return serverhardware.get_type_of_server_hardware(server_name)

    def fusion_ui_delete_server_profile(self, *profile_obj):
        """ Delete a server profile
        Example:
        | Fusion UI Delete Server Profile | @{profile list}
        """
        return serverprofiles.delete_server_profile(profile_obj)

    def fusion_ui_delete_server_profile_by_name(self, profile_name):
        """ Delete a server profile
        Example:
        | Fusion UI Delete Server Profile By Name | ${profile name}
        """
        return serverprofiles.delete_server_profile_by_name(profile_name)

    def fusion_ui_delete_all_appliance_server_profiles(self, wait_ongoing_task_complete=False):
        """ Delete all appliance server profiles
        Example:
        | Fusion UI Delete All Appliance Server Profiles |
        """
        return serverprofiles.delete_all_appliance_server_profiles(wait_ongoing_task_complete)

    def fusion_ui_update_server_profile_firmware(self, *profile_obj):
        """ Update a profile's firmware with the version specified in the profile object
        Example:
        | Fusion UI Update Server Profile Firmware | @{profiles}
        """
        serverprofiles.update_server_profile_firmware(profile_obj)

    def fusion_ui_move_server_profile(self, *profile_obj):
        """ Move a server profile according to data in profile object
        Example:
        | Fusion UI Move Server Profile | @{profile list}
        """
        serverprofiles.move_server_profile(profile_obj)

    def bak_fusion_ui_copy_server_profile(self, *profile_obj):
        """ Copy a server profile according to data file specifications
        Example:
        | Fusion UI Copy Server Profile | @{profile list}
        """
        return serverprofiles.copy_server_profile(profile_obj)

    def fusion_ui_power_on_server_profile(self, *profile_obj):
        """ Power on a server profile
        Example:
        | Fusion UI Power On Server Profile | @{profile name}
        """
        return serverprofiles.power_on_server_profile(profile_obj)

    def fusion_ui_power_on_server_profile_by_name(self, profile_name):
        """ Power on a server profile
        Example:
        | Fusion UI Power On Server Profile By Name| ${profile name}
        """
        return serverprofiles.power_on_server_profile_by_name(profile_name)

    def fusion_ui_power_off_server_profile(self, *profile_obj):
        """ Power off a server profile
        Example:
        | Fusion UI Power Off Server Profile | @{profile name}
        """
        return serverprofiles.power_off_server_profile(profile_obj)

    def fusion_ui_power_off_server_profile_by_name(self, profile_name):
        """ Power off a server profile by given name
        Example:
        | Fusion UI Power Off Server Profile By Name | ${profile name}
        """
        return serverprofiles.power_off_server_profile_by_name(profile_name)

    def fusion_ui_power_off_all_server_profiles(self):
        """ Power off a server profile by given name
        Example:
        | Fusion UI Power Off All Server Profiles
        """
        return serverprofiles.power_off_all_server_profiles()

    def fusion_ui_reset_server_profile(self, *profile_obj):
        """ Reset given server profile(s)
        Example:
        | Fusion UI Reset Server Profile | @{server profile object list} |
        """
        return serverprofiles.reset_server_profiles(profile_obj)

    def fusion_ui_reset_server_profile_by_name(self, profile_name):
        """ Reset given server profile
        Example:
        | Fusion UI Reset Server Profile By Name | ${server profile name} |
        """
        return serverprofiles.reset_server_profile_by_name(profile_name)

    def fusion_ui_cold_boot_server_profile(self, *profile_obj):
        """ Cold boot given server profile(s)
        Example:
        | Fusion UI Cold Boot Server Profile | @{server profile object list} |
        """
        return serverprofiles.cold_boot_server_profiles(profile_obj)

    def fusion_ui_cold_boot_server_profile_by_name(self, profile_name):
        """ Cold boot given server profile
        Example:
        | Fusion UI Cold Boot Server Profile By Name | ${server profile name} |
        """
        return serverprofiles.cold_boot_server_profile_by_name(profile_name)

    def fusion_ui_edit_server_profile(self, *profile_obj):
        """ Edit the server profile
        Example:
        | Fusion UI Edit Server Profile |
        """
        return serverprofiles.edit_server_profile(profile_obj)

    def bak_fusion_ui_edit_server_profile(self, *hardwareTypeName_obj):
        """ Edit the server profile
        Example:
        | Fusion UI Edit Server Profile |
        """
        return serverprofiles.edit_server_profile(hardwareTypeName_obj)

    def fusion_ui_edit_server_profile_for_dl(self, *profile_obj):
        """ Edit the server profile
        Example:
        | Fusion UI Edit Server Profile For DL |
        """
        return serverprofiles.edit_server_profile_for_dl(profile_obj)

    def fusion_ui_get_server_profile_attributes(self, name, attribute=None):
        """ Get Server Profile attribute values
        This function will return attributes from the server profiles page in the UI.
        If an attribute name is specified, only the value of that attribute will be returned as a string.
        If no attribute name is specified, all attribues in the page will be returned as a dictionary.
        NOTE: Currently only supporting the 'General' Server Profile information

        Example:
        | ${Server Profile attributes}=  | Get Server Profile Attributes | Encl1 |
        | ${Server Profile description}=  | Get Server Profile Attributes | Encl1 | Description |
        """
        return serverprofiles.get_server_profile_attributes(name, attribute)

    def fusion_ui_verify_can_not_create_profile_with_used_specified_ids(self, *profile_obj):
        """Verify can not create  a server profile with used specified ids
        Example:
        | Fusion UI Verify can not create  profile with used specified ids | @{Profiles} |

        """
        return serverprofiles.verify_can_not_create_profile_with_used_specified_ids(profile_obj)

    def fusion_ui_verify_can_not_create_server_profile_when_server_power_on(self, *profile_obj):
        """ Verify can not create  a server profile when server power on
        Example:
        | Fusion UI Verify can not create server profile when server power on| @{Profiles} |

        """
        return serverprofiles.verify_can_not_create_server_profile_when_server_power_on(profile_obj)

    def fusion_ui_verify_can_not_create_server_profile_with_bad_server_hardware(self, *profile_obj):
        """ Verify can not create server profile with bad server hardware
        Example:
        | Fusion UI Verify can not create server profile with bad server hardware| @{Profiles} |

        """
        return serverprofiles.verify_can_not_create_server_profile_with_bad_server_hardware(profile_obj)

    def fusion_ui_verify_can_not_create_server_profile_with_bad_enclosure_group(self, *profile_obj):
        """ Verify can not create server profile with bad enclosure_group
        Example:
        | Fusion UI Verify can not create server profile with bad enclosure_group| @{Profiles} |

        """
        return serverprofiles.verify_can_not_create_server_profile_with_bad_enclosure_group(profile_obj)

    def fusion_ui_verify_can_not_create_server_profile_with_error_configuration(self, *profile_obj):
        """ Verify can not create server profile with error configuration
        Example:
        | Fusion  UI Verify Can Not Create Server Profile With Error Configuration | @{Profiles} |
        """
        return serverprofiles.verify_can_not_create_server_profile_with_error_configuration(profile_obj)

    def fusion_ui_verify_can_edit_server_profile_general_info_when_server_power_on(self, *profile_obj):
        """ Verify can edit server profile basic info when server power on
        | Fusion  UI Verify Can Edit Server Profile General Info When Server Power On| @{Profiles} |

        """
        return serverprofiles.verify_can_edit_server_profile_general_info_when_server_power_on(profile_obj)

    def fusion_ui_verify_can_not_edit_server_profile_special_info_when_server_power_on(self, *profile_obj):
        """ Verify can not edit server profile when power on
        Example:
        | Fusion  UI Verify Can Not Edit Server Profile Special Info When Server Power On| @{Profiles} |
        """
        return serverprofiles.verify_can_not_edit_server_profile_special_info_when_server_power_on(profile_obj)

    def fusion_ui_verify_can_not_edit_server_profile_with_error_configuration(self, *profile_obj):
        """ Verify can not edit server profile with error configuration
        Example:
        | Fusion  UI Verify Can Not Edit Server Profile With Error Configuration| @{Profiles} |
        """
        return serverprofiles.verify_can_not_edit_server_profile_with_error_configuration(profile_obj)

    def fusion_ui_verify_server_profile_ui_view_function(self):
        """ Verify Server Profile UI view function
        Example:
        | Fusion UI Verify Server Profile UI view function|

        """
        return serverprofiles.verify_server_profile_ui_view_function()

    def fusion_ui_assign_server_profile(self, *profile_obj):
        """ Assign server profile according to data file specifications
        Example:
        | Fusion UI Assign Server Profile | @{profile list}
        """
        return serverprofiles.assign_profile(profile_obj)

    def fusion_ui_validate_pm_page(self, *profile_obj):
        """ Validate the PM UI page
        Example:
        | Fusion UI Validate PM Page
        """
        serverprofiles.validate_server_profile_ui(profile_obj)

    def fusion_ui_validate_help_text_for_managed_volume_on_add_connection_dialog(self, *profile_obj):
        """Validate help text for managed volume for managed volume
        Examples:
        | Fusion UI Validate Help Text for Managed Volume on Add Connection Dialog | @{profiles} |
        """
        return serverprofiles.validate_help_text_for_managed_volume_on_add_connection_dialog(profile_obj)

    def fusion_ui_validate_add_plus_on_add_connection_dialog(self, *profile_obj):
        """Validate add plus on add connections
        Examples:
        | Fusion UI Validate Add Plus on Add connection Dialog | @{profiles} |
        """
        return serverprofiles.validate_add_plus_on_add_connection_dialog(profile_obj)

    def fusion_ui_validate_user_specified_invisible_on_edit_connection_dialog(self, *profile_obj):
        """Validate user specified invisible on edit connection
        Example:
        | Fusion UI Validate User Specified Invisible on Edit Connection Dialog | @{profiles} |
        """
        return serverprofiles.validate_user_specified_invisible_on_edit_connection_dialog(profile_obj)

    def fusion_ui_pm_elements_should_exist(self, *profile_obj):
        """ Exist server profile manager elements
        Example:
        | Fusion UI PM Elements Should Exist | @{Profiles} |
        """
        serverprofiles.check_pm_elements(profile_obj)

    def fusion_ui_add_label_to_profile(self, *profile_label):
        """ Add label to profile
            Example:
            | Fusion UI Add Label To profile    | ${profile_label}|
        """
        return serverprofiles.add_label_to_profile(profile_label)

    def fusion_ui_create_server_profile_monitored_bays_should_not_show_in_list(self, *monitored_bays):
        """ Verify monitored blade bay should not shows in server hardware list
            Example:
            | Fusion Ui Create Server Profile Monitored Bays Should Not Show In List | @{monitored_bays}|
        """
        return serverprofiles.create_server_profile_monitored_bays_should_not_show_in_list(monitored_bays)

    def fusion_ui_profilemgr_negative_tests_at_create_profile_general_form(self, *profile_obj):
        """ Validate the behavior of general session using invalid data
            Example:
            | Fusion UI Profilemgr Negative Tests At Create Profile General Form   | ${profile_obj} |
        """
        return serverprofiles.negative_test_for_check_general_session(profile_obj)

    def fusion_ui_profilemgr_fill_boot_order(self, *profile_obj):
        """ Fill boot order page and check the position
            Example:
            | Fusion UI Profilemgr Fill Boot Order    | ${profile_obj} |
        """
        return serverprofiles.set_boot_order(profile_obj)

    def fusion_ui_profilemgr_disable_enable_boot_order(self):
        """ Enable and disable the boot order
            Example:
            | Fusion UI Profilemgr Disable Enable Boot Order |
        """
        return serverprofiles.unselect_and_select_boot_order()

    def fusion_ui_profilemgr_set_advanced_settings(self, *profile_obj):
        """ Set the advanced settings
            Example:
            | Fusion UI Profilemgr Set Advanced Settings    | ${profile_obj} |
        """
        return serverprofiles.fill_advanced_session(profile_obj)

    def fusion_ui_profilemgr_navigate_through_local_storage_initial_section(self):
        """ Navigate through Local Storage until clicks on the 'Create Logical Drive' button.
            Example:
            | Fusion UI Profilemgr Navigate Through Local Storage Initial Section |
        """
        return serverprofiles.navigate_through_local_storage()

    def fusion_ui_profilemgr_fails_on_filling_create_logical_drive_fields(self, profile_obj):
        """ Trying to fail on filling create logical drive fields
            Example:
           | Fusion UI Profilemgr Fails On Filling Create Logical Drive Fields | @{profile list} |
        """
        return serverprofiles.negative_test_for_check_local_storage(profile_obj)

    def fusion_ui_profilemgr_fails_on_filling_add_connections_fields(self, profile_obj):
        """ Trying to fail on filling add connections fields
            Example:
           | Fusion UI Profilemgr Fails On Filling Add Connections Fields | @{profile list} |
        """
        return serverprofiles.negative_test_for_profile_connections(profile_obj)

    def fusion_ui_profilemgr_negative_test_for_SAN(self, profile_obj):
        """ Verify that all error messages for PM SAN are shown correctly
            Example:
           | Fusion UI Profilemgr negative test for SAN | @{profile list} |
        """
        return serverprofiles.negative_test_for_SAN(profile_obj)

    def fusion_ui_profilemgr_access_advanced_settings(self):
        """
           | Fusion UI ProfileMGR access the advanced settings on the new profile form |
        """
        return serverprofiles.access_advanced_settings()

    def fusion_ui_profilemgr_click_create_new_profile_button(self):
        """
           | Fusion UI ProfileMGR click on the new profile button |
        """
        return serverprofiles.click_create_new_profile_button()

    def fusion_ui_profilemgr_form_click_create_profile(self):
        """
           | Fusion UI ProfileMGR click on the create profile button |
           | inside new profile form
        """
        return serverprofiles.form_click_create_profile_button()

    def fusion_ui_profilemgr_fill_general_Section(self, profile_obj):
        """
           | Fusion UI ProfileMGR fill general section with a profile |
        """
        return serverprofiles.fill_general_info(profile_obj)

    def fusion_ui_verify_create_server_profile_required_fields_for_connection_with_iscsi_boot(self, *profile_obj):
        """ Input blank fields for iSCSI boot when adding a connection during Create Server Profile
            and verify required fields error message is displayed
            Example:
            | Fusion UI Verify Create Server Profile Required Fields for Connection with iSCSI Boot |
            | @{Server Profile Data} |
        """
        return serverprofiles.verify_required_fields_for_iscsi_boot(profile_obj)

    def fusion_ui_validate_server_profile_task_step(self, *profile_obj):
        """ Validate server profile task step
        Example:
        | Fusion UI Validate Server Profile Task Step| @{Profiles} |
        """
        return serverprofiles.validate_server_profile_task_step(profile_obj)

    def fusion_ui_get_server_profile_error_message(self, *profile_obj):
        """ Get the error message from the "Server Profiles" page
        Example:
        | Fusion UI Get Server Profile Error Message| @{Profiles} |
        """
        return serverprofiles.get_server_profile_error_message(profile_obj)

    def fusion_ui_get_profile_connection_mac_address_and_port(self, *profile_obj):
        """ Get Mac Address and port information of the given  Profile connection
        Example:
        | Fusion UI Get Profile Connection Mac Address And Port| @{Profiles} |
        """
        return serverprofiles.get_profile_connection_mac_address_and_port(profile_obj)
    # #########################################################################
    # Server Profiles Template page functions
    # #########################################################################

    def fusion_ui_navigate_to_server_profile_template_page(self):
        """ Navigate to the Server Profiles Page
        Example:
        | Fusion UI Navigate To Server Profile Template Page |
        """
        return serverprofiletemplates.navigate()

    def fusion_ui_select_server_profile_template(self, templatename):
        """ Selects the respective Profile Template
        Example:
        | Fusion UI Select Server Profile Template |    ${templatename}    |
        """
        return serverprofiletemplates.select_profile_template(templatename)

    def fusion_ui_validate_server_profile_templates_actions_menu(self):
        """ Check server profile template action menu
        Example:
        | Fusion UI Validate Server Profile Template Actions Menu |
        """
        return serverprofiletemplates.validate_server_profile_templates_actions_menu()

    def fusion_ui_update_profile_from_template(self, server_profile):
        """
        Update profile from profile template
        Example:
            |Fusion UI Update Profile From Template    |   ${server_profile}|
        """
        return serverprofiles.update_profile_from_template(server_profile)

    def fusion_ui_create_server_profile_template(self, *profile_template_obj):
        """ Create server profile templates
            Example:
            | Fusion UI Create Server Profile Template | @{profile_templates}|
        """
        return serverprofiletemplates.create_server_profile_template(profile_template_obj)

    def fusion_ui_edit_server_profile_template(self, *profile_template_obj):
        """ Edit the server profile
        Example:
        | Fusion UI Edit Server Profile Template | @{profile_templates}|
        """
        return serverprofiletemplates.edit_server_profile_template(profile_template_obj)

    def fusion_ui_copy_server_profile_template(self, *profile_template_obj):
        """ Copy a server profile
        Example:
        | Fusion UI Copy Server Profile Template | @{profile_templates} |
        """
        return serverprofiletemplates.copy_server_profile_template(profile_template_obj)

    def fusion_ui_verify_server_profile_template_general_info(self, *profile_template):
        """ Verify general information of server profile templates
            Example:
            | Fusion Ui Verify Server Profile Template General Info | @{profile_templates}|
        """
        return serverprofiletemplates.verify_server_profile_template_general_info(profile_template)

    def fusion_ui_verify_server_profile_template_connections_info(self, *profile_obj):
        """ Verify that the server's connections information such as ID, Name. Address, Network, Port and Boot
        Example:
        | Fusion UI Verify Server Profile Template Connections Info |
        """
        return serverprofiletemplates.verify_server_profile_connections_info(profile_obj)

    def fusion_ui_verify_server_profile_template_advanced_info(self, *profile_obj):
        """ Verify that the server's advanced information such as UUID, Mac addresses, WWN addresses and iSCSI initiator name
        Example:
        | Fusion UI Verify Server Profile Template Advanced Info |
        """
        return serverprofiletemplates.verify_server_profile_template_advanced_info(profile_obj)

    def fusion_ui_verify_server_profile_template_local_storage_info(self, *profile_obj):
        """ Verify that the server profile template Local storage information
        Example:
        | Fusion UI Verify Server Profile Template Local Storage Info | @{profiles}
        """
        return serverprofiletemplates.verify_server_profile_template_local_storage_info(profile_obj)

    def fusion_ui_delete_server_profile_template(self, *profile_template_obj):
        """ Delete server profile template(s)
        Example:
        | Fusion UI Delete Server Profile Template | @{profile_template_list}
        """
        return serverprofiletemplates.delete_server_profile_template(profile_template_obj)

    def fusion_ui_delete_server_profile_template_by_name(self, profile_template_name):
        """ Delete a server profile template
        Example:
        | Fusion UI Delete Server Profile Template By Name | ${profile template name}
        """
        return serverprofiletemplates.delete_server_profile_template_by_name(profile_template_name)

    def fusion_ui_delete_all_server_profile_templates(self):
        """ Delete all server profile template(s)
        Example:
        | Fusion UI Delete All Server Profile Templates |
        """
        return serverprofiletemplates.delete_all_appliance_server_profile_templates()

    def fusion_ui_create_profile_from_template(self, *template_profile_obj):
        """ create profile from profile template
        Example:
        | Fusion UI Create Profile From Template| @{template_profile_obj} |
        """
        return serverprofiletemplates.create_profile_from_template(template_profile_obj)

    def fusion_ui_create_server_profile_from_template(self, *template_profile_obj):
        """ create profile from profile template
        Example:
        | Fusion UI Create Profile From Template| @{template_profile_obj} |
        """
        return serverprofiletemplates.create_server_profile_from_template(template_profile_obj)

    def fusion_ui_update_profile_template_connections(self, *profile_template_obj):
        """ Update a profile template
        Example:
        | Fusion Ui Update Profile Template Connections | @{profile_template_obj} |
        """
        return serverprofiletemplates.update_profile_template_connections(profile_template_obj)

    def fusion_ui_validate_server_profile_template_in_use_cannot_be_deleted(self, profile_template_obj):
        """ Validate that, the server profile template used by server profile(s) is not allowed to be deleted
        Example:
                    | Fusion UI Validate Server Profile Template In Use Cannot Be Deleted | @{profile template list}
        """
        return serverprofiletemplates.validate_server_profile_template_in_use_cannot_be_deleted(profile_template_obj)

    def fusion_ui_verify_create_server_profile_template_required_fields_for_connection_with_iscsi_boot(self, *profile_obj):
        """ Input blank fields for iSCSI boot when adding a connection during Create Server Profile Template
            and verify required fields error message is displayed
            Example:
            | Fusion UI Verify Create Server Profile Required Fields for Connection with iSCSI Boot |
            | @{Server Profile Data} |
        """
        return serverprofiletemplates.spt_verify_required_fields_for_iscsi_boot(profile_obj)

    def fusion_ui_validate_server_profile_cannot_be_deleted_when_power_on(self, profile_name):
        """ Validate that, the server profile can not be deleted when server power status is on
        Example:
                    | Fusion UI Validate Server Profile Cannot Be Deleted By Name When Power On | ${profile name}
        """
        return serverprofiles.validate_server_profile_cannot_be_deleted_when_power_on(profile_name)

    # #########################################################################
    # Enclosure Groups page functions
    # #########################################################################
    def fusion_ui_navigate_to_enclosure_groups_page(self):
        """ Navigate to the "Enclosure Groups" page
        Example:
        | Fusion UI Navigate to Enclosure Groups Page |
        """
        enclosuregroups.navigate()

    def fusion_ui_create_enclosure_group(self, *eg_obj):
        """ Create an enclosure group
        Example:
        | Fusion UI Create Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.create_enclosure_group(eg_obj)

    def fusion_ui_create_tbird_enclosure_group(self, *eg_obj):
        """ Create an Tbird enclosure group
        Example:
        | Fusion UI Create TBird Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.create_tbrid_enclosure_group(eg_obj)

    def fusion_ui_validate_lig_selection_when_create_enclosure_group(self, *eg_obj):
        """ Validate lig panel when creating an Tbird enclosure group
        Example:
        | Fusion UI Validate Lig Selection When Create Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.validate_lig_selection_when_create_enclosure_group(eg_obj)

    def fusion_ui_validate_selection_of_LIG_conflicts_with_previously_selected_when_creating_eg(self, *eg_obj):
        """ Validate selection of LIG conflicts with previously selected when creating EG
        Example:
        | Fusion UI Validate Selection Of LIG Conflicts With Previously Selected When Creating EG | @{enclosure group list} |
        """
        return enclosuregroups.validate_selection_of_LIG_conflicts_with_previously_selected_when_creating_eg(eg_obj)

    def fusion_ui_validate_enclosure_group_info(self, *eg_obj):
        """ This function is to navigate and validate enclosure group information.
        Example:
        | Fusion UI Validate Enclosure Group Info | @{enclosure group list} |
        """
        return enclosuregroups.validate_enclosure_group_info(eg_obj)

    def fusion_ui_validate_cannot_create_enclosure_group_using_existing_name(self, *eg_obj):
        """ Verify can not create enclosure group with same name as others
        Example:
        | Fusion UI Validate Cannot Create Enclosure Group Using Existing Name | @{enclosure group list} |
        """
        return enclosuregroups.validate_cannot_create_enclosure_group_using_existing_name(eg_obj)

    def fusion_ui_validate_cannot_update_configuration_script_with_command_in_blacklist(self, *eg_obj):
        """ Verify can not modify EG configuration script with command in blacklist
        Example:
        | Fusion UI modify configuration script with command in blacklist| @{enclosure group list} |

        """
        return enclosuregroups.validate_cannot_update_configuration_script_with_command_in_blacklist(eg_obj)

    def fusion_ui_create_enclosure_groups_by_create_and_createplus_button(self, *eg_obj):
        """ Create Enclosure Groups by Create and Creatplus button
        Example:
        | Fusion UI Create Enclosure Groups by Create and Creatplus button| @{enclosure group list} |

        """
        return enclosuregroups.create_enclosure_groups_by_create_and_createplus_button(eg_obj)

    def fusion_ui_modify_enclosure_group_new_configuration_script(self, *enc_obj):
        """Import Enclosure and Modify EG with new configuration_script
        Example:
        | Fusion UI modify enclosure group new configuration script| @{enclosure group list} |
        """
        return enclosuregroups.modify_enclosure_group_new_configuration_script(enc_obj)

    def fusion_ui_modify_enclosure_group_name(self, *eg_obj):
        """Modify Enclosure Gruop and LIG
        Example:
        | Fusion UI modify enclosure group and lig| @{enclosure group list} |
        """
        return enclosuregroups.modify_enclosure_group_name(eg_obj)

    def fusion_ui_validate_cannot_delete_enclosure_group_used_by_enclosure(self, *eg_obj):
        """Delete EG with enclosure
        Example:
        | Fusion UI Validate Cannot Delete Enclosure Gruop Used By Enclosure| @{enclosure group list} |
        """
        return enclosuregroups.validate_cannot_delete_enclosure_group_used_by_enclosure(eg_obj)

    def fusion_ui_edit_enclosure_group(self, *eg_obj):
        """ Edit enclosure group(s)
        Example:
        | Fusion UI Edit Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.edit_enclosure_group(eg_obj)

    def fusion_ui_edit_tbird_enclosure_group(self, *eg_obj):
        """ Edit enclosure group(s)
        Example:
        | Fusion UI Edit Tbird Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.edit_tbird_enclosure_group(eg_obj)

    def fusion_ui_validate_lig_selection_when_edit_tbird_enclosure_group(self, *eg_obj):
        """ Validate lig panel when editing an Tbird enclosure group
        Example:
        | Fusion UI Validate Lig Selection When Edit Tbird Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.validate_lig_selection_when_edit_tbird_enclosure_group(eg_obj)

    def fusion_ui_validate_selection_of_LIG_conflicts_with_previously_selected_when_editing_eg(self, *eg_obj):
        """ Validate selection of LIG conflicts with previously selected when edit EG
        Example:
        | Fusion UI Validate Selection Of LIG Conflicts With Previously Selected When Editing EG | @{enclosure group list} |
        """
        return enclosuregroups.validate_selection_of_LIG_conflicts_with_previously_selected_when_editing_eg(eg_obj)

    def fusion_ui_delete_enclosure_group(self, *eg_obj):
        """ Delete enclosure group(s)
        Example:
        | Fusion UI Delete Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.delete_enclosure_group(eg_obj)

    def fusion_ui_remove_all_enclosure_groups(self):
        """ Delete all enclosure group(s)
        Example:
        | Fusion UI Remove All Enclosure Groups |
        """
        return enclosuregroups.delete_all_enclosure_groups()

    def fusion_ui_verify_enclosuregroup(self, *eg_obj):
        """ Verify Enclosure group created/edited with the input
        Example:
        | Fusion UI Verify Enclosure Group | @{enclosure group list} |
        """
        return enclosuregroups.verify_enclosuregroup(eg_obj)

    def fusion_ui_validate_privilege_against_delete_enclosure_group(self, *eg_obj):
        """ Validate user privilege against delete enclosure group
        Example:
        | Fusion UI Validate Privilege Against Delete Enclosure Group | @{enclosure group list} |
           """
        return enclosuregroups.validate_privilege_against_delete_enclosure_group(eg_obj)

    def fusion_ui_delete_enclosure_group_ifnot_capture_errors(self, *eg_obj):
        """ Delete enclosure group(s) and capture errors if any
        Example:
        | Fusion UI Delete Enclosure Group Ifnot Capture Errors| @{enclosure group list} |
        """
        return enclosuregroups.delete_enclosure_group_ifnot_capture_errors(eg_obj)

    def fusion_ui_validate_privilege_against_edit_enclosure_group(self, *eg_obj):
        """ Validate user privilege against edit enclosure group
        Example:
        | Fusion UI Validate Privilege Against Edit Enclosure Group | @{enclosure group list} |
           """
        return enclosuregroups.validate_privilege_against_edit_enclosure_group(eg_obj)

    def fusion_ui_edit_tbird_enclosure_group_ifnot_capture_errors(self, *eg_obj):
        """ Edit TBird enclosure group(s) and capture errors if any
        Example:
        | Fusion UI Edit TBird Enclosure Group Ifnot Capture Errors| @{enclosure group list} |
        """
        return enclosuregroups.edit_tbird_enclosure_group_ifnot_capture_errors(eg_obj)

    def fusion_ui_validate_privilege_against_create_enclosure_group(self, *eg_obj):
        """ Validate user privilege against create enclosure group
        Example:
        | Fusion UI Validate Privilege Against Create Enclosure Group | @{enclosure group list} |
           """
        return enclosuregroups.validate_privilege_against_create_enclosure_group(eg_obj)

    # #########################################################################
    # Logical Enclosures page functions
    # #########################################################################
    def fusion_ui_navigate_to_logical_enclosures_page(self):
        """ Navigate to the "Logical Enclosures" page
        Example:
        | Fusion UI Navigate to Logical Enclosures Page |
        """
        logicalenclosures.navigate()

    def fusion_ui_create_tbird_logical_enclosure(self, *le_obj):
        """ Create an logical enclosure
        Example:
        | Fusion UI Create TBird Logical Enclosure | @{logical enclosure list} |
        """
        return logicalenclosures.create_tbird_logical_enclosure(le_obj)

    def fusion_ui_logical_enclosure_firmware_update(self, *le_obj):
        """ Update firmware for logical enclosures
        Example:
        | Fusion Ui Logical Enclosure Firmware Update | @{logical enclosure list} |
        """
        return logicalenclosures.logical_enclosure_firmware_update(le_obj)

    def fusion_ui_edit_logical_enclosure(self, *le_obj):
        """ Edit logical enclosure(s)
        Example:
        | Fusion UI Edit Logical Enclosure | @{logical enclosure list} |
        """
        return logicalenclosures.edit_logical_enclosure(le_obj)

    def fusion_ui_delete_tbird_logical_enclosure(self, *le_obj):
        """ Delete logical enclosure(s)
        Example:
        | Fusion UI Delete Logical Enclosure | @{logical enclosure list} |
        """
        return logicalenclosures.delete_tbird_logical_enclosure(le_obj)

    def fusion_ui_reapply_logical_enclosure_configuration(self, *le_obj):
        """ Reapply logical enclosure(s) Configuration
        Example:
        | Fusion UI Reapply Logical Enclosure Configuration | @{logical enclosure list} |
        """
        return logicalenclosures.reapply_logical_enclosure_configuration(le_obj)

    def fusion_ui_logical_enclosure_update_from_group(self, *le_obj):
        """ logical enclosure(s) Update From Group
        Example:
        | Fusion UI Logical Enclosure Update From Group | @{logical enclosure list} |
        """
        return logicalenclosures.logical_enclosure_update_from_group(le_obj)

    def fusion_ui_create_logical_enclosure_support_dump(self, *le_obj):
        """ Create logical enclosure(s) Support Dump
        Example:
        | Fusion UI Create Logical Enclosure Support Dump | @{logical enclosure list} |
        """
        return logicalenclosures.create_logical_enclosure_support_dump(le_obj)

    def fusion_ui_validate_logical_enclosure_firmware(self, *le_obj):
        """ Validate Logical Enclosure Firmware
        Example:
        | Fusion Ui Validate Logical Enclosure Firmware | @{logical enclosure list} |
        """
        return logicalenclosures.validate_logical_enclosure_firmware(le_obj)

    def fusion_ui_validate_logical_enclosure_firmware_when_updating_firmware(self, *le_obj):
        """ Validate Logical Enclosure Firmware
        Example:
        | Fusion Ui Validate Logical Enclosure Firmware When Updating Firmware | @{logical enclosure list} |
        """
        return logicalenclosures.validate_logical_enclosure_firmware_when_updating_firmware(le_obj)

    def fusion_ui_verify_logical_enclosure_consistency_state(self, *le_obj):
        """ Verify logical enclosure consistency state
        Example:
        | Fusion UI Verify Logical Enclosure Consistency State | @{logical enclosure list} |
        """
        return logicalenclosures.verify_logical_enclosure_consistency_state(le_obj)

    def fusion_ui_validate_tbird_logical_enclosure_consistency_state(self, *le_obj):
        """ Verify logical enclosure consistency state
        Example:
        | Fusion UI Validate Tbird Logical Enclosure Consistency State | @{logical enclosure list} |
        """
        return logicalenclosures.validate_tbird_logical_enclosure_consistency_state(le_obj)

    def fusion_ui_verify_logical_enclosure_warn(self, *le_obj):
        """ Verify Logical Enclosure Warn
        Example:
        | Fusion UI Verify Logical Enclosure Warn | @{logical enclosure list}|
        """
        return logicalenclosures.verify_logical_enclosure_warn(le_obj)

    def fusion_ui_delete_logical_enclosure(self, *le_obj):
        """ Delete LE
        Example:
        | fusion_ui_delete_logical_enclosure | @{LE group list} |
        """
        return logicalenclosures.delete_logical_enclosure(le_obj)

    def fusion_ui_update_tbird_logical_enclosure_firmware(self, *fw_obj):
        '''
        function to trigger LE firmware update
        returns boolean
        Example:
        fusion_ui_update_tbird_logical_enclosure_firmware | ${fw_obj}
        '''
        return logicalenclosures.update_tbird_logical_enclosure_firmware(fw_obj)

    def fusion_ui_validate_le_firmware_upgrade_activity_details(self, *fw_obj):
        '''
        Function to validate the firmware activity details
        returns the activity details with string TEST PASSED in case of success
        returns the error_string , issues and resolutions with string TEST FAILED in case of failure
        EXAMPLE :
            fusion_ui_verify_le_firmware_upgrade_activity_details  | ${fw_obj}
        '''
        return logicalenclosures.validate_le_firmware_upgrade_activity_details(*fw_obj)

    def fusion_ui_create_logical_enclosure(self, *le_obj):
        """ Create a logical enclosure
        Example:
        | fusion_ui_create_logical_enclosure | @{LE group list} |
        """
        return logicalenclosures.create_logical_enclosure(le_obj)

    def fusion_ui_verify_le_interconnect_bay_licensing(self, *le_obj):
        '''
        function to verify the elements in the Interconnect Bay licensing section in LogicalEnclosure,
        based on the Data passed in the object *le_obj
        Example::
        |fusion_ui_verify_le_interconnect_bay_licensing | @{le_obj list}
        Returns True.
        '''
        return logicalenclosures.verify_logical_enclosure_interconnect_bay_licensing(le_obj)

    def fusion_ui_verify_le_interconnect_bay_licensing_editpanel(self, *le_obj):
        '''
        function to verify data in Interconnect Bay licensing Edit panel in LogicalEnclosure
        based on the Data passed in the *le_obj
        Example::
        |fusion_ui_verify_le_interconnect_bay_licensing_editpanel | @{le_obj list}
        '''
        return logicalenclosures.verify_logical_enclosure_interconnect_bay_licensing_editpanel(le_obj)

    def fusion_ui_verify_le_frmware_upgrade_activity_details(self, *fw_obj):
        '''
        Function to verify the firmware activity details
        returns the activity details with string TEST PASSES in case of success
        returns the error_string , issues and resolutions with string TEST FAILED in case of failure
        EXAMPLE :
            fusion_ui_verify_le_frmware_upgrade_activity_details  | ${fw_obj}
        '''
        return logicalenclosures.verify_le_frmware_upgrade_activity_details(fw_obj)

    def fusion_ui_verify_li_and_ic_firmware_versions(self, *fw_obj):
        '''
        Function to validate if the installed and baseline versions of Interconnects
        in Logical interconnect is same as that installed in the IC after LE FW update

        Function also gets the installed version from the actual hardware and verifies it is same as that displayed in Appliance
        - It logs in to the CI manager and gets the installed Fw version on the IC
        EXAMPLE :
            fusion_ui_verify_li_and_ic_firmware_versions | ${fw_obj}
        '''
        return logicalenclosures.verify_li_and_ic_firmware_versions(fw_obj)

    def fusion_ui_verify_ic_state_of_le(self, permissible_ic_states=["configured", "unmanaged"], *fw_obj):
        '''
        Function to verify the state of the Interconnect belonging to the Logical interconnects of the LE
        The default permissible states are configures and unmanaged.

        User may pass the desired states as a list of strings.

        Returns True if the IC state is in the List passed else returns false
        EXAMPLE:
            fusion_ui_verify_ic_state_of_le | ${permissible_ic_states} | ${fw_obj}
        '''
        return logicalenclosures.verify_ic_state_of_le(permissible_ic_states, fw_obj)

    def fusion_ui_verify_ic_stacking_domain_role_of_le(self, *fw_obj):
        '''
        Function to verify the stacking domain role of the IC's in the LI of the LE.
        At least half of the IC's should be master , and the other half subordinate
        In case the IC under consideration does not have a stacking role (like chlorides) an appropriate message is logged and it is not considered

        Returns a boolean value
        EXAMPLE:
            fusion_ui_verify_ic_stacking_domain_role_of_le | ${fw_obj}
        '''

        return logicalenclosures.verify_ic_stacking_domain_role_of_le(fw_obj)

    def fusion_UI_reapply_li_configuration_of_le(self, lename, wait_for_task_complete='true'):
        '''
        Function to reapply configuration of the LIs in the LE mentioned
        If wait_for_task_complete is true then function waits till task completes
        else it just triggers a reapply and returns
        EXAMPLE:
            fusion_UI_reapply_li_configuration_of_le | ${lename} | ${wait_for_task_complete}
        '''

        return logicalenclosures.reapply_li_configuration_of_le(lename, wait_for_task_complete)

    def fusion_ui_verify_ic_ipv4address_of_li_in_le_within_range_pool(self, le_name, *editidentifiers_obj):
        '''
        Function to check if the ipv4 ips allocated to the ICs are form the custom range specified in input
        EXAMPLE:
           fusion_ui_verify_ic_ipv4address_of_li_in_le_within_range_pool | ${liname} | @{editidentifiers_obj}
        '''
        return logicalenclosures.verify_ic_ipv4address_of_li_in_le_within_range_pool(le_name, editidentifiers_obj)

    def fusion_ui_verify_ilo_ipv4ips_of_servers_in_le_within_range_pool(self, le_name, *edit_address_identifiers):
        '''
        Function to check if the ipv4 ips allocated to the server ilos are form the custom range specified in input
        EXAMPLE:
            fusion_ui_verify_ilo_ipv4ips_of_servers_in_le_within_range_pool | ${liname} | @{editidentifiers_obj}
        '''
        return logicalenclosures.verify_ilo_ipv4ips_of_servers_in_le_within_range_pool(le_name, edit_address_identifiers)

    def fusion_ui_select_logical_enclosure(self, enc_name):
        """ Selects respective logical enclosure from the enclosure list
        Example:
        | Fusion UI Select Logocal Enclosure |    ${enc_name}    |
        """
        return logicalenclosures.select_logicalenclosure(enc_name)

    def fusion_ui_update_logical_enclosure_firmware(self, *enclosure_list):
        """ Update Logical Enclosure Firmware
            This function is to update enclosure firmware
            Example:
            | Fusion UI Update Logical Enclosure Firmware| enclosure_list|
        """
        return logicalenclosures.update_logical_enclosure_firmware(*enclosure_list)

    # #########################################################################
    # Drive Enclosures
    # #########################################################################
    def fusion_ui_verify_drive_enclosures_drives_view(self, *drive_enclosure_object):
        """Verify that the 'Drives' view on the 'Drive Enclosures' page is
        displaying what it should be
        Example:
        Fusion UI Verify Drive Enclosures Drives View  @{drive_enclosure_list}"""
        drive_enclosures.verify_drives_view(drive_enclosure_object)

    def fusion_ui_verify_drive_enclosures_component_view(self, *drive_enclosure_object):
        """Verify the 'Component' view in the 'Overview' view of all enclosures.
        Example:
        Fusion UI Verify Drive Enclosures Component View  @{drive_enclosure_list}"""
        drive_enclosures.verify_component_view(drive_enclosure_object)

    def fusion_ui_validate_drive_enclosures_configuration(self, *drive_enclosure_object):
        """ Validate configuration of drive enclosure
        Example:
        | Fusion Ui Validate Drive Enclosure Configuration | @{drive enclosure list} |
        """
        drive_enclosures.validate_drive_enclosure_configuration(drive_enclosure_object)

    def fusion_ui_verify_drive_enclosures_drives_link(self, *drive_enclosures_object):
        """For each drive enclosure verify that the 'Drives' link on the 'Overview'
        view takes you to the 'Drives' view.
        Example:
        Fusion UI Verify Drive Enclosures Drives Link  @{drive_enclosure_list}"""
        drive_enclosures.verify_drives_link(drive_enclosures_object)

    def fusion_ui_power_off_drive_enclosure(self, *drive_enclosurehardware_obj):
        """ Remove drive_enclosure hardware
        Example:
        | Fusion UI Power Off drive_enclosure Hardware | ${drive_enclosure hw list} |
        """
        return drive_enclosures.power_off_drive_enclosure(drive_enclosurehardware_obj)

    def fusion_ui_power_on_drive_enclosure(self, *drive_enclosurehardware_obj):
        """ Power on given drive_enclosure
        Example:
        | Fusion UI Power On drive_enclosure Hardware | @{drive_enclosure hardware object} |
        """
        return drive_enclosures.power_on_drive_enclosure(drive_enclosurehardware_obj)

    def fusion_ui_reset_drive_enclosure(self, *drive_enclosurehardware_obj):
        """ Reset given drive_enclosure
        Example:
        | Fusion UI Reset drive_enclosure | @{drive_enclosure hardware object list} |
        """
        return drive_enclosures.reset_drive_enclosure(drive_enclosurehardware_obj)

    def fusion_ui_refresh_drive_enclosure(self, *drive_enclosurehardware_obj):
        """ Reset given drive_enclosure
        Example:
        | Fusion UI Reset drive_enclosure | @{drive_enclosure hardware object list} |
        """
        return drive_enclosures.refresh_drive_enclosure(drive_enclosurehardware_obj)

    def fusion_ui_turn_on_drive_enclosure_uid(self, *drive_enclosurehardware_obj):
        """ Turn on UID  given drive_enclosure
        Example:
        | Fusion UI turn on drive_enclosure | @{drive_enclosure hardware object list} |
        """
        return drive_enclosures.turn_on_drive_enclosure_uid(drive_enclosurehardware_obj)

    def fusion_ui_turn_off_drive_enclosure_uid(self, *drive_enclosurehardware_obj):
        """ Turn off UID given drive_enclosure
        Example:
        | Fusion UI turn off drive_enclosure | @{drive_enclosure hardware object list} |
        """
        return drive_enclosures.turn_off_drive_enclosure_uid(drive_enclosurehardware_obj)

    # #########################################################################
    # Enclosures page functions
    # #########################################################################
    def fusion_ui_navigate_to_enclosures_page(self):
        """ Navigate to the "Enclosures" page
        Example:
        | Fusion Ui Navigate To Enclosures Page |
        """
        enclosures.navigate()

    def fusion_ui_add_enclosure(self, *enc_obj):
        """ Add new enclosure(s)
        Example:
        | Fusion UI Add Enclosure | @{enclosure list} |
        """
        return enclosures.add_enclosure(enc_obj)

    def fusion_ui_edit_enclosure(self, *enc_obj):
        """ Edit enclosure(s)
        Example:
        | Fusion UI Edit Enclosure | @{enclosure list} |

        Data file example:
            <editenclosures>
                <enclosure name="wpst32" new_name="wpst32_new"/>
                <enclosure name="wpst32_new" new_name="wpst32"/>
            </editenclosures>
        """
        return enclosures.edit_enclosure(enc_obj)

    def fusion_ui_reapply_enclosure_configuration(self, *enc_obj):
        """ Reapply configuration for enclosure(s)
        Example:
        | Fusion UI Edit Enclosure | @{enclosure list} |

        Data file example:
            <enclosures>
                <enclosure name="wpst32"/>
            </enclosures>
        """
        return enclosures.reapply_enclosure_configuration(enc_obj)

    def fusion_ui_refresh_enclosure(self, *enc_obj):
        """ Refresh enclosure(s)
        Example:
        | Fusion UI Refresh Enclosure | @{enclosure list} |

        Data file example:
            <enclosures>
                <enclosure name="wpst32"/>
            </enclosures>
        """
        return enclosures.refresh_enclosure(enc_obj)

    def fusion_ui_refresh_enclosure_by_name(self, enclosure_name, wait_for_refresh_complete=True):
        """
        Keyword to refresh enclosure by name.Function has an option to wait for the refresh task to complete or return without waiting

        Example:
        | fusion ui refresh enclosure by name  |  ${EnclosureName}  | True
                    OR
        | fusion ui refresh enclosure by name  |  ${EnclosureName}  | False
                    OR
        | fusion ui refresh enclosure by name  |  ${EnclosureName}

        """
        return enclosures.refresh_enclosure_by_name(enclosure_name, wait_for_refresh_complete)

    def fusion_ui_wait_for_enclosure_refresh_complete(self, enc_name, waittime=900):
        '''
        function to wait for the refresh task to complete
        Useful if the user wants to wait for a refresh already triggered/triggered automatically
        Default wait time is 900 seconds or 15 minutes
        Example:
            | fusion ui wait for enclosure refresh complete | ${enc_name} | ${waittime}
        '''
        return enclosures.wait_for_enclosure_refresh_complete(enc_name, waittime)

    def fusion_ui_remove_enclosure(self, *enc_obj):
        """ Remove enclosure(s)
        Example:
        | Fusion UI Remove Enclosure | @{enclosure list} |
        """
        return enclosures.remove_enclosure(enc_obj)

    def fusion_ui_update_enclosure_firmware(self, *enc_obj):
        """ Update enclosure(s) firmware
        Example:
        | Fusion UI Update Enclosure Firmware | @{enclosure list} |
        """
        enclosures.update_enclosure_firmware(enc_obj)

    def fusion_ui_validate_enclosure_lig(self, *enc_obj):
        """ Validate enclosure(s) LIG

        Examples:
        | Fusion UI Validate Enclosure LIG | @{enclosure list} |
        """
        return enclosures.validate_enclosure_lig(enc_obj)

    def fusion_ui_validate_enclosure_configuration(self, *enclosure_obj):
        """ Validate all configuration of enclosure
        Example:
        | Fusion Ui Validate Enclosure Configuration | @{enclosure list} |
        """
        return enclosures.validate_enclosure_configuration(enclosure_obj)

    def fusion_ui_validate_tbird_enclosure_configuration(self, *enclosure_obj):
        """ Validate all configuration of Tbird enclosure
        Example:
        | Fusion Ui Validate TBird Enclosure Configuration | @{enclosure list} |
        | Fusion Ui Validate TBird Enclosure Configuration | @{enclosure list} |
        """
        return enclosures.validate_tbird_enclosure_configuration(enclosure_obj)

    def fusion_ui_select_encl(self, enc_name):
        """ Selects the respective enclosure from the enclosure list
        Example:
        | Fusion UI Select Encl |    ${enc_name}    |
        """
        return enclosures.select_enclosure(enc_name)

    def fusion_ui_navigate_to_fan_details_page(self):
        """ Navigate to the "Fans UI" details page from Overview drop down
        Example:
        | Fusion UI Navigate To Fans Detail Page |
        """
        return enclosures.navigate_to_fan_details_page()

    def fusion_ui_get_fan_rules(self):
        """ Retrieving the Fan rules from FAN UI details page
        Example:
        | Fusion UI Get Fan rules |
        """
        return enclosures.get_fan_rules()

    def fusion_ui_mouse_hover_fan_bay(self, fan_bay):
        """ Verifying mouse hover functionality and retrieve the respective attributes"
        Example:
        | Fusion UI Mouse Hover Fan Bay |   ${fan_bay}   |
        """
        return enclosures.mouse_hover_fan_bay(fan_bay)

    def fusion_ui_navigate_to_fan_details_from_tooltip(self, fan_bay):
        """ Navigate to fan details page from the tooltip on the rear view of enclosure page
        Example:
        | Fusion UI Navigate To Fan Details From Tooltip |     ${fan_bay}   |
        """
        return enclosures.navigate_to_fan_details_from_tooltip(fan_bay)

    def fusion_ui_get_fan_details(self):
        """ Get fan values in the table from the fan details page
        Example:
        | Fusion UI Get Fan Details |
        """
        return enclosures.get_fan_details()

    def fusion_ui_get_fan_overview(self):
        """ Get fan values from fan overview page
        Example:
        | Fusion UI Get Fan Overview  |
        """
        return enclosures.get_fan_overview()

    def fusion_ui_get_fan_attribute(self, page_name, bay_num, attribute):
        """ Get fan attributes from fan overview/details page for the given bay number
        Example:
        | Fusion UI Get Fan Attribute  |   ${page_name}    ${bay_num}    ${attribute}
        """
        return enclosures.get_fan_attribute(page_name, bay_num, attribute)

    def fusion_ui_get_fan_count(self, fan_dict, status_type):
        """ Get the Fan count for the given type
        Example:
        | Fusion UI  get Fan Count        | ${fan_dict}  |  ${status_type}  |
        """
        return enclosures.get_fan_count(fan_dict, status_type)

    def fusion_ui_get_power_supply_details(self, enc_name):
        """ Get the power supply values in the table on the power supply details page

        Example:
        | `Get Power Supply Details`     |     ${enc_name}    |

        """
        return enclosures.get_power_supply_details(enc_name)

    def fusion_ui_get_power_supply_overview(self, enc_name):
        """ Get the power supply overview values in the enclosure front view on the Enclosures page

        Example:
        | `Get Power Supply Overview`    |    ${enc_name}    |

        """
        return enclosures.get_power_supply_overview(enc_name)

    def fusion_ui_get_power_supply_attribute(self, enc_name, page, bay_no, attribute):
        """ Get the power supply attribute for the PS in the given bay number

        Example:
        | `Get Power Supply Attribute`         | ${page}    | ${bay_no}    |    ${attribute} |

        """
        return enclosures.get_power_supply_attribute(enc_name, page, bay_no, attribute)

    def fusion_ui_get_power_supply_count(self, ps_dict, status_type):
        """ Get the power supply count for the given type

        Example:
        | `Get Power Supply Count`         | ${ps_dict}  |  ${type}  |

        """
        return enclosures.get_power_supply_count(ps_dict, status_type)

    def fusion_ui_navigate_to_powersupply_details_from_overview_bay_popup(self, enc_name, bay_no):
        """ Navigate to power supply details page from link in bay hover menu in overview page

        Example:
        | `Navigate To Powersupply Details From Bay`    |    ${enc_name}    |    ${bay_no}    |

        """
        return enclosures.navigate_to_powersupply_details_from_overview_bay_popup(enc_name, bay_no)

    def fusion_ui_get_powersupply_data_from_mouseover(self, enc_name, bay_no):
        """ Get the power supply overview values from mouseover in Enclosures overview
        Example:
        | `Get Powersupply Data From Mouseover`    |    ${enc_name}    |    ${bay_no}    |

        """
        return enclosures.get_powersupply_data_from_mouseover(enc_name, bay_no)

    def fusion_ui_verify_tbird_front_slot_content(self, row_no, bay_no):
        """ Checks the blades & CIM slots in Enclosures overview
        Example:
        | `Fusion UI Verify Tbird Front Slot Content`    |    ${row}    |    ${bay}    |

        """
        return enclosures.tbird_verify_front_slot_content(row_no, bay_no)

    def fusion_ui_verify_tbird_icm_graphic(self, device_no):
        """ Checks the ICM slots in the "Rear View" graphics of Enclosures overview.
            device_no: ICM bay number, 0-5 (zero-based)
        Example:
        | `Fusion UI Verify Tbird ICM Graphic`    |    ${device_no}    |

        """
        return enclosures.tbird_verify_back_icm_row(device_no)

    def fusion_ui_verify_tbird_em_fan_graphic(self, logical_row):
        """ Checks the EM & fan slots in the "Rear View" graphics of Enclosures overview
            Validates all devices on the same row of the enclosure rear.
            logical_row: Zero-based row no. wrt. only the EM & fan rows (0 = encl row 3, 1 = encl row 8)
        Example:
        | `Fusion UI Verify Tbird EM Fan Graphic`    |    ${logical_row}    |

        """
        return enclosures.tbird_verify_back_em_fan_row(logical_row)

    def fusion_ui_verify_tbird_power_supply_graphic(self, logical_row):
        """ Checks the power supply slots in the "Rear View" graphics of Enclosures overview
            Validates all devices on the same row of the enclosure rear.
            logical_row: Zero-based row no. wrt. only the power supply rows (0 = encl row 5, 1 = encl row 10)
        Example:
        | `Fusion UI Verify Tbird Power Supply Graphic`    |    ${logical_row}    |

        """
        return enclosures.tbird_verify_back_power_row(logical_row)

    def fusion_ui_verify_tbird_device_bay(self, bay_no):
        """ Checks the 12 blade slots in Enclosures details
        Example:
        | `Fusion UI Verify Tbird Device Bay`    |    ${bay}    |

        """
        return enclosures.tbird_verify_device_bay(bay_no)

    def fusion_ui_verify_tbird_interconnect_bay(self, bay_no):
        """ Checks the 6 ICM slots in Enclosures details
        Example:
        | `Fusion UI Tbird Verify Interconnect Bay`    |    ${bay}    |

        """
        return enclosures.tbird_verify_interconnect_bay(bay_no)

    def fusion_ui_verify_tbird_cim_bay(self, bay_no):
        """ Checks the two CIM slots in Enclosures details
        Example:
        | `Fusion UI Tbird Verify CIM Bay`    |    ${bay}    |

        """
        return enclosures.tbird_verify_cim_bay(bay_no)

    def fusion_ui_verify_tbird_em_bay(self, bay_no):
        """ Checks the two EM slots in Enclosures details
        Example:
        | `Fusion UI Tbird Verify EM Bay`    |    ${bay}    |

        """
        return enclosures.tbird_verify_em_bay(bay_no)

    # { Case related
    def fusion_ui_validate_should_not_readd_enclosure(self, *enc_obj):
        """ Validate appliance should not re-add monitored/managed enclosure which already monitored/manged by itself
        Example:
        | Fusion UI Validate Should Not Readd Enclosure | @{enclosure list} |
        """
        return enclosures.validate_should_not_readd_enclosure(enc_obj)

    def fusion_ui_validate_component_for_add_enclosure_dialog(self):
        """ Validate if "Add enclosure for management" & "Add enclosure for monitoring" raidobox controls exist on UI page, and also
            check related UI controls exist when choosing different raidobox
        Example:
        | Fusion UI Validate Component For Add Enclosure Dialog |
        """
        return enclosures.validate_ui_component_for_add_enclosure_dialog()

    def fusion_ui_validate_action_menu_for_monitored_enclosure(self, *enc_obj):
        """ Validate some action button such like 'Edit', 'reapply configuration' not apply on monitored enclosure
        Example:
        | Fusion UI Validate Action Menu For Monitored Enclosure | @{enclosure list} |
        """
        return enclosures.validate_action_menu_for_monitored_enclosure(enc_obj)

    def fusion_ui_validate_server_hardware_power_state_after_refresh_enclosure(self, *enc_obj):
        """ Validate if server hardware power state get updated after power on/off in oa and refreshing enclosure
        Example:
        | Fusion Ui Validate Server Hardware Power State After Refresh Enclosure | @{enclosure list} |
        """
        return enclosures.validate_server_hardware_power_state_after_refresh_enclosure(enc_obj)

    def fusion_ui_validate_server_hardware_power_state_after_reapply_enclosure_config(self, *enc_obj):
        """ Validate if server hardware power state get updated after power on/off in oa and reapply enclosure configuration
        Example:
        | Fusion Ui Validate Server Hardware Power State After Reapply Enclosure Config | @{enclosure list} |
        """
        return enclosures.validate_server_hardware_power_state_after_reapply_enclosure_config(enc_obj)
    # }

    def fusion_ui_remove_all_enclosures(self):
        """ Delete all enclosure(s)
        Example:
        | Fusion UI Remove All Enclosures |
        """
        return enclosures.delete_all_appliance_enclosure()

    def fusion_ui_add_label_to_enclosure(self, *enclosure_list):
        """ Add Label To Enclosure
        This function is to add label to enclosure
        Example:
        | Fusion UI Add Label To Enclosure    |    ${enclosure_list}    |
        """
        return enclosures.add_label_to_enclosure(enclosure_list)

    def fusion_ui_delete_enclosure_label(self, *enclosure_obj):
        """ delete enclosure label
        This function is to delete enclosure label
        Example:
             | Fusion UI Delete Enclosure Label    |    ${enclosure_obj}    |
        """
        return enclosures.delete_enclosure_label(enclosure_obj)

    def fusion_ui_update_enclosure_name(self, enc_name, new_enc_name):
        """ Update enclosure name
            This function will update the enclosure name to new enclosure name
            Example:
            | Fusion UI Update enclosure name    |    ${enc_name}    |    ${new_enc_name}    |
        """
        return enclosures.update_enclosure_name(enc_name, new_enc_name)

    def fusion_ui_turn_on_enclosure_uid(self, *enclosure_obj):
        """
            Turn on UID for of enclosure Modules
            Example:
            | Fusion Ui turn_on_enclosure_uid | @(IC data) |
        """
        return enclosures.turn_on_enclosure_uid(enclosure_obj)

    def fusion_ui_turn_off_enclosure_uid(self, *enclosure_obj):
        """
            Turn off UID for of enclosure Modules
            Example:
            | Fusion Ui turn_off_enclosure_uid | @(IC data) |
        """
        return enclosures.turn_off_enclosure_uid(enclosure_obj)

    def fusion_ui_validate_enclosure_uid_light_off(self, *enclosure_obj):
        """
            Verify UID off for all of enclosure Modules
            Example:
            | fusion_ui_validate_enclosure_uid_light_off | @(IC data) |
        """
        return enclosures.validate_enclosure_uid_light_off(enclosure_obj)

    def fusion_ui_validate_enclosure_task_step(self, *enclosure_obj):
        """ Validate enclosure task step
        Example:
        | Fusion UI Validate Enclosure Task Step| @{Enclosures} |
        """
        return enclosures.validate_enclosure_task_step(enclosure_obj)

    def fusion_ui_validate_enclosure_sub_task(self, *enclosure_obj):
        """ Validate enclosure task step
        Example:
        | Fusion UI Validate Enclosure Sub Task| @{Enclosures} |
        """
        return enclosures.validate_enclosure_sub_task(enclosure_obj)

    ##########################################################################
    # OA operation
    # #########################################################################

    # #########################################################################
    # Server Hardware page functions
    # #########################################################################
    def fusion_ui_navigate_to_server_hardware_page(self):
        """ Navigate to the "Server Hardware" page
        Example:
        | Fusion UI Navigate To Server Hardware Page |
        """
        serverhardware.navigate()

    def fusion_ui_get_server_powerstatus(self, server_name):
        """ Get the server's power status
        Example:
        | Fusion UI Get Server Powerstatus | ${Server Name} |
        """
        return serverhardware.get_server_powerstatus(server_name)

    def fusion_ui_get_profilename_associated_to_server(self, server_name):
        """ Get the profile name associated with a server
        Example:
        | Fusion UI Get Profilename Associated To Server | ${Server Name} |
        """
        return serverhardware.get_profilename_associated_to_server(server_name)

    def fusion_ui_power_off_all_server_hardware(self):
        """ Power off all servers in Fusion
        Example:
        | Fusion UI Power Off All Servers |
        """
        return serverhardware.power_off_all_server_hardware()

    def fusion_ui_add_server_hardware(self, *serverhardware_obj):
        """ Add server hardware to Fusion
        Example:
        | Fusion UI Add Server Hardware | ${Server hw list} |
        """
        return serverhardware.add_server_hardware(serverhardware_obj)

    def fusion_ui_remove_server_hardware(self, *serverhardware_obj):
        """ Remove server hardware
        Example:
        | Fusion UI Add Server Hardware | ${Server hw list} |
        """
        return serverhardware.remove_servers(serverhardware_obj)

    def fusion_ui_remove_server_hardware_by_name(self, server_name):
        """ Remove server hardware
        Example:
        | Fusion UI Remove Server Hardware By Name | ${server_name} |
        """
        return serverhardware.remove_server_by_name(server_name)

    def fusion_ui_power_off_server_hardware(self, *serverhardware_obj):
        """ Remove server hardware
        Example:
        | Fusion UI Power Off Server Hardware | ${Server hw list} |
        """
        return serverhardware.power_off_servers(serverhardware_obj)

    def fusion_ui_power_off_server_hardware_by_name(self, server_name):
        """ Power off given server
        Example:
        | Fusion UI Power Off Server Hardware By Name | ${server name} |
        """
        return serverhardware.power_off_server_by_name(server_name)

    def fusion_ui_power_on_server_hardware(self, *serverhardware_obj):
        """ Power on given server
        Example:
        | Fusion UI Power On Server Hardware | @{server hardware object} |
        """
        return serverhardware.power_on_servers(serverhardware_obj)

    def fusion_ui_power_on_server_hardware_by_name(self, server_name):
        """ Power on given server
        Example:
        | Fusion UI Power On Server Hardware By Name | ${server name} |
        """
        return serverhardware.power_on_server_by_name(server_name)

    def fusion_ui_reset_server(self, *serverhardware_obj):
        """ Reset given server
        Example:
        | Fusion UI Reset Server | @{server hardware object list} |
        """
        return serverhardware.reset_servers(serverhardware_obj)

    def fusion_ui_reset_server_by_name(self, server_name):
        """ Reset given server
        Example:
        | Fusion UI Reset Server By Name | ${server name} |
        """
        return serverhardware.reset_server_by_name(server_name)

    def fusion_ui_reset_ilo(self, *serverhardware_obj):
        """ Reset ilo of the given server hardware
        Example:
        | Fusion UI Reset Ilo | @{server hardware object list} |
        """
        return serverhardware.reset_ilo(serverhardware_obj)

    def fusion_ui_validate_server_hardware_task_status_from_activity_view(self, server_name, activity_task, action_name, expect_task_status):
        """ Validate server hardware task status from activity view
        Example:
        | Fusion UI Validate Server Hardware Task Status From Activity View | ${server hardware} ${activity task} ${action name} ${expect task status} |
        """
        return serverhardware.validate_server_hardware_task_status_from_activity_view(server_name, activity_task, action_name, expect_task_status)

    def fusion_ui_validate_reset_ilo_was_blocked(self, server_name, expected_msg):
        """ Validate Reset ilo was blocked with expected msg
        Example:
        | Fusion UI Validate Reset Ilo Was Blocked | ${server hardware}  ${expected_msg} |
        """
        return serverhardware.validate_reset_ilo_was_blocked(server_name, expected_msg)

    def fusion_ui_reset_link_module_by_name(self, enclosure_name, link_module_type):
        """ Reset link module of the given enclosure in standby/active way
        Example:
        | Fusion UI Reset Link Module By Name | ${enclosure name}  ${link module type} |
        """
        return enclosures.reset_link_module_by_name(enclosure_name, link_module_type)

    def fusion_ui_reset_link_module(self, *enclosure_obj):
        """ Reset link module of the given enclosures in standby/active way
        Example:
        | Fusion UI Reset Link Module | @{ enclosure obj list} |
        """
        return enclosures.reset_link_module(enclosure_obj)

    def fusion_ui_cold_boot_server(self, *serverhardware_obj):
        """ Cold boot given server
        Example:
        | Fusion UI Cold Boot Server | @{server hardware object list} |
        """
        return serverhardware.cold_boot_servers(serverhardware_obj)

    def fusion_ui_cold_boot_server_by_name(self, server_name):
        """ Cold boot given server
        Example:
        | Fusion UI Cold Boot Server By Name | ${server name} |
        """
        return serverhardware.cold_boot_server_by_name(server_name)

    def fusion_ui_refresh_server(self, *serverhardware_obj):
        """ Refresh given server
        Example:
        | Fusion UI Refresh Server | @{server hardware object list} |
        """
        return serverhardware.refresh_servers(serverhardware_obj)

    def fusion_ui_refresh_server_by_name(self, server_name):
        """ Refresh given server
        Example:
        | Fusion UI Refresh Server By Name | ${server name} |
        """
        return serverhardware.refresh_server_by_name(server_name)

    def fusion_ui_validate_server_hardware_page(self, *enclosure_obj):
        """ validate information on the "Server Hardware Types" page
        Example:
        | Fusion UI Validate Server Hardware Types Page |
        """
        return serverhardware.validate_server_hardware_page(enclosure_obj)

    def fusion_ui_validate_server_hardware_page_hardware(self, *server_obj):
        """ validate hardware information on the "Server Hardware" page
        Example:
        | Fusion UI Validate Server Hardware Page Hardware|
        """
        return serverhardware.validate_server_hardware_page_hardware(server_obj)

    def fusion_ui_validate_server_hardware_page_utilization(self, *server_obj):
        """ validate utilization information on the "Server Hardware" page
        Example:
        | Fusion UI Validate Server Hardware Page Utilization|
        """
        return serverhardware.validate_server_hardware_utilization(server_obj)

    def fusion_ui_validate_server_hardware_monitored_by_own(self, *server_obj):
        """ validate error message when trying to add server which is already monitored by own appliance
        Example:
        | Fusion UI Validate Server Hardware Monitored by Own|
        """
        return serverhardware.validate_server_hardware_monitored_by_own(server_obj)

    def fusion_ui_validate_server_hardware_meet_minimum_ilo4(self, *server_obj):
        """ validate error message when trying to add server which iLO4 FW is below minimum
        Example:
        | Fusion UI Validate Server Hardware Meet Minimum iLO4|
        """
        return serverhardware.validate_server_hardware_meet_minimum_ilo4(server_obj)

    def fusion_ui_get_server_firmware_version(self, server_name):
        """ Server Firmware details: Returns dictionary values for firmware version
            Example:
            | Fusion UI Get Server Firmware Version |    ${server_name} |
        """
        return serverhardware.get_server_firmware_version(server_name)

    def fusion_ui_validate_server_hardware_meet_minimum_ilo3(self, *server_obj):
        """ validate error message when trying to add server which iLO3 FW is below minimum
        Example:
        | Fusion UI Validate Server Hardware Meet Minimum iLO3|
        """
        return serverhardware.validate_server_hardware_meet_minimum_ilo3(server_obj)

    def fusion_ui_validate_server_hardware_meet_minimum_ilo2(self, *server_obj):
        """ validate error message when trying to add server which iLO2 FW is below minimum
        Example:
        | Fusion UI Validate Server Hardware Meet Minimum iLO2|
        """
        return serverhardware.validate_server_hardware_meet_minimum_ilo2(server_obj)

    def fusion_ui_validate_server_hardware_managed_by_own(self, *server_obj):
        """ validate error message when trying to add server which is managed by own
        Example:
        | Fusion UI Validate Server Hardware Already Managed By Own|
        """
        return serverhardware.validate_server_hardware_managed_by_own(server_obj)

    def fusion_ui_validate_server_hardware_meet_minimum_ilo_firmware_version(self, *server_obj):
        """ validate error message when trying to add server which is managed by own
        Example:
        | Fusion UI Validate Server Hardware Meet Minimum iLo Firmware Version |
        """
        return serverhardware.validate_server_hardware_meet_minimum_ilo_firmware_version(server_obj)

    def fusion_ui_validate_server_hardware_manage_single_blade(self, *server_obj):
        """ validate error message when trying to add server which is one of an enclosure's bays
        Example:
        | Fusion UI Validate Server Hardware Manage Single Blade | @{server list}
        """
        return serverhardware.validate_server_hardware_manage_single_blade(server_obj)

    def fusion_ui_validate_server_power(self, *server_obj):
        """ validate power action (on or off) and UI elements according to server's power state
        Example:
        | Fusion UI Validate Server Power | @{server list}
        """
        return serverhardware.validate_server_power(server_obj)

    def fusion_ui_validate_monitored_server_no_profile(self, *server_obj):
        """ validate that, if a server is added as 'Monitored', then it cannot create server profile
        Example:
        | Fusion UI Validate Monitored Server No Profile | @{server list}
        """
        return serverhardware.validate_monitored_server_no_profile(server_obj)

    def fusion_ui_delete_monitor_account(self, *server_obj):
        """ Delete _HPOneViewMonitor account on iLO
        Example:
        | Fusion UI Delete Monitor Account|
        """
        return serverhardware.delete_monitor_account(server_obj)

    def fusion_ui_force_refresh_server(self, *server_obj):
        """ Refresh server hardware by providing iLO credentials
        Example:
        | Fusion UI Force Refresh Server|
        """
        return serverhardware.force_refresh_server(server_obj)

    def fusion_ui_compare_two_dictionaries(self, dictionary1, dictionary2):
        """ it compares two dictionaries
        Example:
        | Fusion UI Power On Server | ${Server hw} |
        """
        return serverhardware._compare_two_dictionaries(dictionary1, dictionary2)

    def fusion_ui_power_on_all_servers(self):
        """ Power on all servers in Fusion
        Example:
        | Fusion UI Power On All Servers |
        """
        return serverhardware.power_on_all_servers()

    def fusion_ui_power_off_all_servers(self):
        """ Power off all servers in Fusion
        Example:
        | Fusion UI Power Off All Servers |
        """
        return serverhardware.power_of_all_servers()

    def fusion_ui_validate_server_utilization_panel(self, *server_obj):
        """
            This function will check the existence of ILO advanced license for server hardware,
            based on this utilization panel validation will be done.
            Example:
            | Fusion UI Validate Server Utilization Panel    |@{server_obj}|
        """
        return serverhardware.validate_server_utilization_panel(*server_obj)

    def fusion_ui_validate_server_temperature(self, *hw_obj):
        """
            This function will validate server hardware temperature by
            comparing temperature from Fusion UI and OA
            Example:
            | Fusion UI Validate Server Temperature |    @{hw_obj}|
        """
        return serverhardware.validate_sever_temperature(hw_obj)

    def fusion_ui_verify_alert_generated_in_appliance(self, *activity_obj):
        """
            This Function will check alert page for specific alert
            Example:
            |Fusion UI Verify Alert Generated In Appliance| @{activity_obj}|
        """
        return serverhardware.verify_alert_generated_in_appliance(activity_obj)

    def fusion_ui_validate_server_health_status(self, *server_obj):
        """
            validate whether server health status is as per expected or not
            Example:
            | Fusion UI Validate Server Health Status |    @{server_obj}    |
        """
        return serverhardware.validate_server_health_status(server_obj)

    def fusion_ui_create_labels_for_server_hardware(self, *serverhardware_label):
        """ Create labels For Server Hardware in the "Server Hardware" page
        Example:
        | Fusion UI Create Labels For Server Hardware | @{serverhardware_label} |
        """
        return serverhardware.create_labels_for_server_hardware(serverhardware_label)

    def fusion_ui_turn_on_server_uid(self, *server_obj):
        """
            Turn on UID for of server Modules
            Example:
            | Fusion Ui Turn On server UID | @(IC data) |
        """
        return serverhardware.turn_on_server_uid(server_obj)

    def fusion_ui_turn_off_server_uid(self, *server_obj):
        """
            Turn off UID for of server Modules
            Example:
            | Fusion Ui Turn Off server UID | @(IC data) |
        """
        return serverhardware.turn_off_server_uid(server_obj)

    def fusion_ui_validate_server_uid_light_off(self, *server_obj):
        """
            Verify UID off for all of server Modules
            Example:
            | fusion_ui_validate_server_uid_light_off | @(IC data) |
        """
        return serverhardware.validate_server_uid_light_off(server_obj)

    def fusion_ui_validate_server_sub_task(self, *server_obj):
        """ Validate Server task step
        Example:
        | Fusion UI Validate Server Sub Task| @{Servers} |
        """
        return serverhardware.validate_server_sub_task(server_obj)

    # #########################################################################
    # Server Hardware Types page functions
    # #########################################################################

    def fusion_ui_navigate_to_server_hardware_types_page(self):
        """ Navigate to the "Server Hardware Types" page
        Example:
        | Fusion UI Navigate To Server Hardware Types Page |
        """
        serverhardwaretypes.navigate()

    def fusion_ui_select_server_hardware_type(self, hardwaretype):
        """ Select the server hardware type on the "Server Hardware Types" page
        Example:
        | Fusion UI Select Server Hardware Type | ${hardware type}
        """
        serverhardwaretypes.select_server_hardware_type(hardwaretype)

    def fusion_ui_verify_server_hardware_type(self, *hardwareTypeName_obj):
        """ Verify the server hardware type on the "Server Hardware Types" page
        Example:
        | Fusion UI Verify Server Hardware Type
        """
        return serverhardwaretypes.verify_server_hardware_type(hardwareTypeName_obj)

    def fusion_ui_edit_server_hardware_type(self, *hardwareTypeName_obj):
        """ Edit the server hardware type on the "Server Hardware Types" page
        Example:
        | Fusion UI Edit Server Hardware Type |
        """
        return serverhardwaretypes.edit_server_hardware_type(hardwareTypeName_obj)

    def fusion_ui_cannot_change_sht_name_to_existing_name(self, *hardwareTypeName_obj):
        """ Change the server hardware type to existing name on the "Server Hardware Types" page
        Example:
        | Fusion UI Cannot Change Sht Name To Existing Name |
        """
        return serverhardwaretypes.cannot_change_sht_name_to_existing_name(hardwareTypeName_obj)

    def fusion_ui_delete_server_hardware_type(self, *hardwareTypeName_obj):
        """ Delete a server hardware type on the "Server Hardware Types" page
        Example:
        | Fusion UI Delete Server Hardware Type |
        """
        return serverhardwaretypes.delete_server_hardware_type(hardwareTypeName_obj)

    def fusion_ui_cannot_delete_server_hardware_type(self, *hardwareTypeName_obj):
        """ Delete a server hardware type on the "Server Hardware Types" page
        Example:
        | Fusion UI Cannot Delete Server Hardware Type |
        """
        return serverhardwaretypes.cannot_delete_server_hardware_type(hardwareTypeName_obj)

    def fusion_ui_delete_all_server_hardware_types(self):
        """ Delete all server hardware types on the "Server Hardware Types" page
        Example:
        | Fusion UI Delete All Server Hardware TypeS |
        """
        return serverhardwaretypes.delete_all_server_hardware_types()

    def fusion_ui_validate_server_hardware_types_page(self, *sht_obj):
        """ validate information on the "Server Hardware Types" page
        Example:
        | Fusion UI Validate Server Hardware Types Page |
        """
        return serverhardwaretypes.validate_server_hardware_type(sht_obj)

    def fusion_ui_validate_server_hardware_type_names_without_number_exist(self, *sht_obj):
        """ validate information on the "Server Hardware Types" page
        Example:
        | Fusion UI Validate Server Hardware Types Page |
        """
        return serverhardwaretypes.validate_server_hardware_types_name_without_number_exist(sht_obj)

    # #########################################################################
    # Logical Interconnect Groups page functions
    # #########################################################################
    def fusion_ui_navigate_to_logical_interconnect_groups_page(self):
        """ Navigate to the "Logical Interconnect Groups" page
        Example:
        | Fusion UI Navigate To Logical Interconnect Groups Page |
        """
        logicalinterconnectgroups.navigate()

    def fusion_ui_create_logical_interconnect_group(self, *icg_obj):
        """ Create a Logical Interconnect Group
        Example:
        | Fusion UI Create Logical Interconnect Group | @{LIG list} |
        """
        return logicalinterconnectgroups.create_logical_interconnect_group(icg_obj)

    def fusion_ui_create_natasha_logical_interconnect_group(self, *icg_obj):
        """ Create a natasha Logical Interconnect Group
        Example:
        | Fusion UI Create Natasha Logical Interconnect Group | @{LIG list} |
        """
        return logicalinterconnectgroups.create_natasha_logical_interconnect_group(icg_obj)

    def fusion_ui_create_tbird_logical_interconnect_group(self, *lig_obj):
        """ Create a Logical Interconnect Group On Tbird Appliance
        Example:
        | Fusion UI Create Tbird Logical Interconnect Group | @{LIG list} |
        """
        return logicalinterconnectgroups.create_tbird_logical_interconnect_group(lig_obj)

    def fusion_ui_delete_logical_interconnect_group(self, *icg_obj):
        """ Delete a logical interconnect group
        Example:
        | Fusion UI Delete Logical Interconnect Group | @{LIG list} |
        """
        return logicalinterconnectgroups.delete_logical_interconnect_group(icg_obj)

    def fusion_ui_edit_logical_interconnect_group(self, *lig_obj):
        """
            Fusion Ui Edit Logical Interconnect Group(contain C7000 and Tbird)
            Input:
                Data object with edit LIG data.
            Output:
                Returns True if all the LIGs are edited successfully else it will return False.
            Example:
            | Fusion Ui Edit Logical Interconnect Group      |  @{LIG list}   |
        """
        return logicalinterconnectgroups.edit_logical_interconnect_group(lig_obj)

    def fusion_ui_edit_natasha_logical_interconnect_group(self, *lig_obj):
        """
            Fusion Ui Edit Natasha Logical Interconnect Group
            Input:
                Data object with edit Natasha LIG data.
            Output:
                Returns True if all the Natasha LIGs are edited successfully else it will return False.
            Example:
            | fusion ui edit logical interconnect group      |  @{LIG list}   |
        """
        return logicalinterconnectgroups.edit_natasha_logical_interconnect_group(lig_obj)

    def fusion_ui_validate_logical_interconnect_group(self, *lig_obj):
        """
            Fusion Ui Validate Logical Interconnect Group
            Input:
                Data object with verify LIG data.
            Output:
                Returns True if all the LIGs are verified successfully else it will return False.
            Example:
            | Fusion Ui Validate Logical Interconnect Group      |  @{LIG list}   |
        """
        return logicalinterconnectgroups.verify_logical_interconnect_group(lig_obj)

    def fusion_ui_create_logical_interconnect_group_tbird(self, *icg_obj):
        """ Edit a Logical Interconnect Group for tbird
        Example:
        | Fusion UI Create Logical Interconnect Group tbird | @{LIG list} |
        """
        return logicalinterconnectgroups.create_logical_interconnect_group_tbird(icg_obj)

    def fusion_ui_edit_logical_interconnect_group_tbird(self, *icg_obj):
        """ Create a Logical Interconnect Group for tbird
        Example:
        | Fusion UI Create Logical Interconnect Group tbird | @{LIG list} |
        """
        return logicalinterconnectgroups.edit_logical_interconnect_group_tbird(icg_obj)

    def fusion_ui_validate_warning_message_when_edit_logical_interconnect_group(self, *lig_obj):
        """ Validate warning message when editing a logical interconnect group
        Example:
        | Fusion Ui Validate Warning Message When Edit Logical Interconnect Group | @{LIG list} |
        """
        return logicalinterconnectgroups.validate_warning_message_when_edit_logical_interconnect_group(lig_obj)

    def fusion_ui_verify_logical_interconnect_group(self, *icg_obj):
        """
        Verify The LIG after Create/Edit operation - for both tbird and c7000
        Example:
        | fusion_ui_verify_logical_interconnect_group | @{LIG_list} |
        """

        return logicalinterconnectgroups.verify_logical_interconnect_group(icg_obj)

    def fusion_ui_verify_logical_interconnect_group_tbird(self, *ligs_obj):
        """
        Verify The LIG after Create/Edit operation - for tbird
        Example:
        | fusion_ui_verify_logical_interconnect_group_tbird | @{LIG_list} |
        """

        return logicalinterconnectgroups.verify_logical_interconnect_group_tbird(ligs_obj)

    def fusion_ui_remove_all_logical_interconnect_groups(self):
        """ Delete all logical interconnect group(s)
        Example:
        | Fusion UI Remove All Logical Interconnect Groups |
        """
        return logicalinterconnectgroups.delete_all_appliance_ligs()

    def fusion_ui_validate_qos_configuration(self, *lig_obj):
        """
            Fusion Ui validate Qos Configuration
            Input:
                Data object with QoS data .
            Output:
                Returns True if all the QoS values  are verified successfully else it will return False.
            Example:
            | fusion ui validate qos configuration      |  @{LIG list}   |
                                                """
        return logicalinterconnectgroups.validate_qos_configuration(lig_obj)

    def fusion_ui_validate_user_privileges_logicalinterconnectgroups(self, *lig_obj):
        """
            It checks for Action menu visibility in "LIG" page
            Example:
            | Fusion UI Validate User Privileges Logicalinterconnectgroups |
        """
        return logicalinterconnectgroups.validate_user_privileges(lig_obj)

    def fusion_ui_get_qos_class_values(self, *lig_obj):
        """
            It gets the all class values in a qos table
            Example:
            | Fusion Ui Get Qos Class Values  |
        """
        return logicalinterconnectgroups.get_qos_class_values(lig_obj)

    # #########################################################################
    # Logical Interconnects page functions
    # #########################################################################
    def fusion_ui_navigate_to_logical_interconnects_page(self):
        """ Navigate to the "Logical Interconnects" page
        Example:
        | Fusion UI Navigate To Logical Interconnects Page |
        """
        logicalinterconnects.navigate()

    def fusion_ui_get_uplinkset_data(self, liname):
        """ Get Uplink Set Data in "Logical Interconnects" page
        Example:
        | Fusion UI Get Uplink Set Data | ${liname}
        """
        return logicalinterconnects.get_uplinkset_data(liname)

    def fusion_ui_logicalinterconnects_create_support_dump(self, *lic_obj):
        """ Create a support dump for a Logical Interconnect
        Example:
        | Fusion UI Logicalinterconnects Create Support Dump | @{interconnect list} |
        """
        logicalinterconnects.create_support_dump(lic_obj)

    def fusion_ui_logical_interconnects_reapply_configuration(self, *lic_obj):
        """ Re-apply a configuration for a logical interconnect
        Example:
        | Fusion UI Logical Interconnects Reapply Configuration | @{interconnect list} |
        """
        logicalinterconnects.reapply_configuration(lic_obj)

    def fusion_ui_update_firmware_tbird_logical_interconnect(self, *firmware_obj):
        """ Update the firmware for a logical interconnect of tbird enclosure
        Example:
        | Fusion UI Update Firmware Tbird Logical Interconnect | @{interconnect list} |
        """
        return logicalinterconnects.update_firmware_tbird_logical_interconnect(firmware_obj)

    def fusion_ui_update_firmware_tbird_natasha_logical_interconnect(self, *firmware_obj):
        """ Update the firmware for a natasha logical interconnect of tbird enclosure
        Example:
        | Fusion UI Update Firmware Tbird Natasha Logical Interconnect | @{interconnect list} |
        """
        return logicalinterconnects.update_firmware_tbird_natasha_li(firmware_obj)

    def fusion_ui_update_firmware_tbird_natasha_li_validate_affected_components(self, *li_obj):
        """ Update the firmware for a natasha logical interconnect of tbird enclosure.
            Verify affected components table exists.
        Example:
        | Fusion UI Update Firmware Tbird Natasha Li Validate Affected Components | @{interconnect list} |
        """
        return logicalinterconnects.update_firmware_tbird_natasha_li_affected_components(li_obj)

    def fusion_ui_update_firmware_logical_interconnect(self, *net_obj):
        """ Update the firmware for a logical interconnect
        Example:
        | Fusion UI Update Firmware Logical Interconnect | @{interconnect list} |
        """
        return logicalinterconnects.update_firmware(net_obj)

    def fusion_ui_update_logical_interconnect_from_group(self, *le_obj):
        """ logical interconnect(s) Update From Group
        Example:
        | Fusion UI Update Logical Interconnect From Group | @{logical interconnect list} |
        """
        return logicalinterconnects.update_logical_interconnect_from_group(le_obj)

    def fusion_ui_edit_logical_interconnects(self, *editlis_obj):
        """ logical interconnect(s) edit
        Example:
        | Fusion UI edit Logical Interconnect
        """
        return logicalinterconnects.edit_logical_interconnect(editlis_obj)

    def fusion_ui_configure_port_monitoring(self, *lis_obj):
        """ Configure Port Monitoring
        """
        logicalinterconnects.configure_port_monitoring(lis_obj)

    def fusion_ui_edit_logical_interconnects_port_monitoring(self, *lis_obj):
        """ Edit logical interconnect Port Monitoring
        """
        logicalinterconnects.configure_port_monitoring(lis_obj)

    def fusion_ui_edit_logical_interconnects_redistribute_logins(self, *lis_obj):
        """ edit logical interconnect redistribute logins
        """
        logicalinterconnects.edit_redistribute_logins(lis_obj)

    def fusion_ui_verify_logical_interconnects_status(self, *lis_obj):
        """ Verify logical interconnects status
        Example:
        | Fusion UI Verify Logical Interconnects Status |
        """
        logicalinterconnects.verify_logical_interconnects_status(lis_obj)

    def fusion_ui_validate_interconnect_firmware(self, *interconnect_list):
        """ Validate the installed interconnect firmware with base lined firmware
        Example:
        | Fusion UI Validate Interconnect Firmware | @{interconnect list} |
        """
        return logicalinterconnects.validate_interconnect_firmware(interconnect_list)

    def fusion_ui_select_logical_interconnect(self, liname):
        """ Select Logical Interconnect
        This function is to Select Logical Interconnect
        Example:
        | Fusion UI Select Logical Interconnect    |    ${liname}    |
        """
        return logicalinterconnects.select_logical_interconnect(liname)

    def fusion_ui_add_label_to_logical_interconnect(self, *logicalinterconnect_list):
        """ Add Label To Logical Interconnect
        This function is to add label to Logical Interconnect
        Example:
        | Fusion UI Add Label To Logical Interconnect    |    ${logicalinterconnect_list}    |
        """
        return logicalinterconnects.add_label_to_logical_interconnect(logicalinterconnect_list)

    def fusion_ui_get_ic_stacking_domain_role_of_li(self, li_name):
        '''
        Function to get the stacking domain role of the Interconnects in the LI
        return NONE if no stacking role found
        EXAMPLE:
            fusion_ui_get_ic_stacking_domain_role_of_li | ${li_name}
        '''

        return logicalinterconnects.get_ic_stacking_domain_role_of_li(li_name)

    def fusion_ui_get_li_license_info(self, li_name):
        '''
        Function to get the FC License State of LI from General Section
        Input:  li_name
        Returns the license state & count

        EXAMPLE:
            fusion_ui_get_li_license_info | ${li_name}
        '''
        return logicalinterconnects.get_license_info_of_logical_interconnect(li_name)

    def fusion_ui_verify_logical_interconnects(self, *inc_obj):
        """ Verify logical interconnects
        Example:
        | Fusion UI Verify Logical Interconnect |    @{li list}
        """
        return logicalinterconnects.verify_logical_interconnect(inc_obj)

    def fusion_ui_reapply_li_configuration(self, li_name, wait_for_task_complete='true'):
        '''
        Function to trigger LI reapply configuration
        If wait_for_task_complete is true then function waits till task completes
        else it just triggers a reapply and returns
        EXAMPLE:
            fusion_ui_reapply_li_configuration | ${li_name} | ${wait_for_task_complete}
        '''

        return logicalinterconnects.reapply_li_configuration(li_name, wait_for_task_complete)

    def fusion_ui_wait_for_reapply_configuration_complete(self, li_name):
        '''
        Function to wait for reapply configuration to complete.Monitor the activity in activities page
        returns boolean
        useful if user is waiting for a pre-triggered task to complete , or an automatically reapply to complete
        EXAMPLE :
            fusion_ui_wait_for_reapply_configuration_complete | ${li_name}
        '''
        return logicalinterconnects.wait_for_reapply_configuration_complete(li_name)

    def fusion_ui_verify_ic_state_of_li(self, li_list, permissible_state_list):
        '''
        Function to verify the State of Interconnects part of an LI

        Takes a list of LI and permissible states list as input

        Return True id the IC state is in permissible list else returns false

        EXAMPLE:
            fusion_ui_verify_ic_state_of_li | @{li_list} | @{permissible_state_list}
        '''
        return logicalinterconnects.verify_ic_state_of_li(li_list, permissible_state_list)

    def fusion_ui_get_ic_ipv4_address_in_li(self, liname):
        '''
        Function to get the ipv4 addresses of the ICs in the LI specified
        Returns a dictionary containing the ICname : ipv4 address as key value pair.

        Returns an empty dictionary if no addresses found for any IC
        EXAMPLE :
            fusion_ui_get_ic_ipv4_address_in_li | ${liname}
        '''
        return logicalinterconnects.get_ic_ipv4_address_in_li(liname)

    def fusion_ui_verify_li_stacking_health(self, *fw_obj):
        '''
        Function to verify that the Stacking Health of the LI id 'redundantly connected'
        Applicable to only IRF configurations

        Returns a boolean value
        EXAMPLE:
            fusion_ui_verify_li_stacking_health | ${fw_obj}
        '''
        return logicalenclosures.verify_li_stacking_health(fw_obj)

    def fusion_ui_get_li_stacking_health(self, liname):
        '''
        This function  gets the stacking health status of the LI in Logical interconnects Page

        Returns stacking health status of the LI
        EXAMPLE:
            fusion_ui_get_li_stacking_health | ${liname}
        '''
        return logicalinterconnects.get_li_stacking_health(liname)

    def fusion_ui_display_interconnects_link_ports_in_li(self, *lis_obj):
        '''
        Function to display interconnect link ports of the ICs in the LI

        EXAMPLE :
            fusion_ui_display_interconnects_link_ports_in_li | @{li_list}
        '''
        return logicalinterconnects.display_interconnects_link_ports_in_li(lis_obj)

    def fusion_ui_validate_qos_configuration_in_li(self, *lig_obj):
        """
            Fusion Ui Validate Qos Configuration In li
            Input:
                Data object with QoS data .
            Output:
                Returns True if all the QoS values  are verified successfully else it will return False.
            Example:
            | fusion ui validate qos configuration in li      |  @{LIG list}   |
                                                """
        return logicalinterconnects.validate_qos_configuration_in_li(lig_obj)

    def fusion_ui_validate_user_privileges_logicalinterconnects(self, *lig_obj):
        """ it checks for Action menu visibility in "LI" page
        Example:
        | Fusion UI Validate User Privileges Logicalinterconnects |
        """
        return logicalinterconnects.validate_user_privileges(lig_obj)

    def fusion_ui_get_logical_interconnect_uplinkset_ports_info(self, *logicalinterconnects_obj):
        """" Uplink Port speed and FC port login in LI
        Example:
            | fusion_ui_get_logical_interconnect_uplinkset_ports_info | ${logicalinterconnects} |
        """
        return logicalinterconnects.get_logical_interconnect_uplinkset_ports_info(*logicalinterconnects_obj)

    def fusion_ui_get_tbird_interconnect_fc_port_statistics(self, *inc_obj):
        """ This function is Used to verify the interconnect connector information
        Example:
        | Fusion UI Get Tbird Interconnect Fc Port Statistics | @{interconnect list} |
        """
        return interconnects.get_tbird_interconnect_fc_port_statistics(inc_obj)

    def fusion_ui_get_li_active_message_list(self, liname):
        """
        returns LI active message list
                Example:
                |fusion_ui_get_li_active_message_list|  li_name |
        """
        return logicalinterconnects.get_active_message_list_li(liname)

    def fusion_ui_get_li_uplink_data(self, liname, uplink):
        """
        returns LI message active list
         Example:

         fusion_ui_get_li_uplink_data   li_name  uplink_name
        """
        return logicalinterconnects.get_li_uplinkset_data(liname, uplink)

    def fusion_ui_get_li_uplink_port_data(self, *li_obj):
        '''
        returns LI uplink port data list
            Example:
            |fusion_ui_get_uplink_port_data|  li_obj |
            '''
        return logicalinterconnects.get_li_uplinkset_port_data(li_obj)

    def fusion_ui_verify_mac_table_exists(self, *li_obj):
        """It check whether the download MAC Table Download exist or not in LI page
        Example:
        | Fusion UI Verify Mac Table Exists |
        """
        return logicalinterconnects.verify_mac_table_exist(li_obj)

    def fusion_ui_verify_functions_of_mac_table(self, li_obj):
        """It Verify The functions of Mac table dropdown boxes
        Example:
        | Fusion UI Verify Functions Of Mac Table |
        """
        return logicalinterconnects.verify_functions_of_mac_table(li_obj)

    def fusion_ui_verify_mac_address_in_mac_table(self, li_obj):
        """It Verify The functions of Mac table Mac Address dropdown boxes
        Example:
        | Fusion UI Verify Mac Address In Mac Table |
        """
        return logicalinterconnects.verify_mac_address_in_mac_table(li_obj)

    def fusion_ui_verify_default_gateway_mac_address(self, li_obj):
        """It verify The functions of Mac table Mac Address dropdown boxes
        Example:
        | Fusion UI Verify Default Gateway Mac Address
        """
        return logicalinterconnects.verify_default_gateway_mac_address(li_obj)

    # #########################################################################
    # Networks page functions
    # #########################################################################

    def fusion_ui_create_ethernet_network(self, *net_obj):
        """ Create new ethernet network(s)
        Example:
        | Fusion UI Create Ethernet Network | ${network list} |
        """
        return networks.create_ethernet_networks(*net_obj)

    def fusion_ui_delete_ethernet_network(self, *net_obj):
        """ Delete ethernet networks(s)
        Example:
        | Fusion UI Delete Ethernet Network | ${network list} |
        """
        return networks.delete_networks(*net_obj)

    def fusion_ui_create_fc_network(self, *net_obj):
        """ Create new Fibre Channel network(s)
        Example:
        | Fusion UI Create FC Network |  ${network list} |
        """
        return networks.create_fc_networks(*net_obj)

    def fusion_ui_edit_fc_network(self, *net_obj):
        """ Edit an FC network according to data in SAW XML file
        Example:
        | Fusion UI Edit FC Network | ${network list} |
        """
        return networks.edit_fc_networks(*net_obj)

    def fusion_ui_edit_ethernet_network(self, *net_obj):
        """ Edit ethernet network according to data in SAW XML file
        Example:
        | Fusion UI Edit Ethernet Network | ${network list} |
        """
        return networks.edit_ethernet_networks(*net_obj)

    def fusion_ui_edit_ethernet_networks_capture_errors(self, *net_obj):
        """ Edit ethernet network and capture errors if any
        Example:
        | Fusion UI Edit Ethernet Network | ${network list} |
        """
        return networks.edit_ethernet_networks_capture_errors(*net_obj)

    def fusion_ui_verify_ethernet_network(self, *net_obj):
        """ Edit ethernet network according to data in SAW XML file
        Example:
        | Fusion UI Edit Ethernet Network | ${network list} |
        """
        return networks.verify_ethernet_network(*net_obj)

    def fusion_ui_delete_fc_network(self, *net_obj):
        """ Delete FC network(s)
        Example:
        | Fusion UI Delete FC Network | ${network list} |
        """
        return networks.delete_networks(*net_obj)

    def fusion_ui_delete_all_appliance_networks(self):
        """ Delete all networks on appliance
        Example:
        | Fusion UI Delete All Appliance Networks |
        """
        return networks.delete_all_appliance_networks()

    def fusion_ui_create_fcoe_network(self, *net_obj):
        """ Create new fcoe network(s)
        Example:
        | Fusion UI Create FCOE Network | ${network list} |
        """
        return networks.create_fcoe_network(net_obj)

    def fusion_ui_delete_fcoe_network(self, *net_obj):
        """ Delete fcoe networks(s)
        Example:
        | Fusion UI Delete fcoe Network | ${network list} |
        """
        return networks.delete_networks(*net_obj)

    def fusion_ui_action_visibility_check_networks(self):
        """ Navigate to "Networks" page
        Example:
        | Fusion UI Action Visibility Check |
        """
        return networks.action_visibility_check()

    def fusion_ui_add_label_to_networks(self, *network_label):
        """ Add label to networks in Fusion
        Example:
        | Fusion UI Add Label To Networks | @{network label} |
        """
        return networks.add_label_to_networks(network_label)

    def fusion_ui_navigate_to_networks_page(self):
        """ Navigate to the "Networks" page
        Example:
        | Fusion UI Navigate To Networks Page |
        """
        return networks.navigate()

    # #########################################################################
    # Network Sets page functions
    # #########################################################################
    def fusion_ui_navigate_to_network_sets_page(self):
        """ Navigate to the "Network Sets" page
        Example:
        | Fusion UI Navigate To Network Sets Page |
        """
        return networksets.navigate()

    def fusion_ui_create_network_set(self, *networksets_obj):
        """ Create new network set(s)
        Example:
        | Fusion UI Create Network Set | @{network set list} |
        """
        return networksets.create_network_set(networksets_obj)

    def fusion_ui_edit_network_set(self, *networksets_obj):
        """ Edit a network set according to the data in the SAW xml file
        Example:
        | Fusion UI Edit Network Set | @{network set list} |
        """
        return networksets.edit_network_set(networksets_obj)

    def fusion_ui_delete_network_set(self, *networksets_obj):
        """ Delete network set(s)
        Example:
        | Fusion UI Delete Network Set | @{network set list} |
        """
        return networksets.delete_network_set(networksets_obj)

    def fusion_ui_add_label_to_network_set(self, *networksets_label):
        """ Add label to network set
        Example:
        | Fusion UI Add Label To Network Set | @{network set label} |
        """
        return networksets.add_label_to_network_set(networksets_label)

    def fusion_ui_select_network_set(self, networkset_name):
        """ select network set
        Example:
        | Fusion UI Select Network Set | ${networkset_name} |
        """
        return networksets.select_network_set(networkset_name)

    def fusion_ui_delete_all_network_sets(self):
        """ Delete all network sets
        Example:
        |   Fusion UI Delete All Network Sets   |
        """
        return networksets.delete_all_network_sets()

    # #########################################################################
    # Interconnects page functions
    # #########################################################################
    def fusion_ui_navigate_to_interconnects_page(self):
        """ Navigate to the "Interconnects" page
        Example:
        | Fusion UI Navigate To Interconnects Page |
        """
        return interconnects.navigate()

    def fusion_ui_edit_interconnect(self, *interconnect_obj):
        """ Edit Interconnects based on SAW XML file
        Example:
        | Fusion UI Edit Interconnect | @{interconnect list} |
        """
        return interconnects.edit_interconnect(interconnect_obj)

    def fusion_ui_verify_fex_interconnect_uplinkport_editable(self, *interconnect_obj):
        """ Edit Interconnects based on SAW XML file
        Example:
        | Fusion UI Verify Fex Interconnect Uplinkport Editable | @{interconnect list} |
        """
        return interconnects.verify_fex_interconnect_uplinkport_editable(interconnect_obj)

    def fusion_ui_reapply_interconnect_configuration(self, *interconnect_obj):
        """ Re-apply interconnect configuration
        Example:
        | Fusion UI Reapply Configuration | @{interconnect list} |
        """
        return interconnects.reapply_configuration(interconnect_obj)

    def fusion_ui_c7000_reapply_configuration(self, *interconnect_obj):
        """ C7000 reapply configuration
        Example:
        | Fusion UI c7000 Reapply Configuration | @{interconnect list} |
        """
        return interconnects.c7000_reapply_configuration(interconnect_obj)

    def fusion_ui_clear_interconnect_port_counters(self, *interconnect_obj):
        """ Clear the port counters on the supplied interconnects
        Example:
        | Fusion UI Clear Port Counters | @{interconnect list} |
        """
        return interconnects.clear_port_counters(interconnect_obj)

    def fusion_ui_c7000_clear_port_counters(self, *interconnect_obj):
        """ C7000 Clear the port counters on the supplied interconnects
        Example:
        | Fusion UI c7000 Clear Port Counters | @{interconnect list} |
        """
        return interconnects.c7000_clear_port_counters(interconnect_obj)

    def fusion_ui_validate_interconnect(self, *interconnect_obj):
        """ Validate interconnect data reported
        Example
        | Fusion UI Validate Interconnect | @{interconnect list} |
        """
        return interconnects.validate_interconnect(interconnect_obj)

    def fusion_ui_verify_interconnect_general_view(self, interconnectname, enclname, *enc_obj):
        """
        This function is to navigate to drop down menus in interconnects page.
        Example:
        | Fusion UI Verify Interconnect General View | ${interconnectname}, ${enclname}, @{enclosure list} |
        """
        return interconnects.verify_interconnect_general_view(interconnectname, enclname, enc_obj)

    def fusion_ui_navigate_to_dropdown_menus(self, interconnectname, dropdownmenu):
        """ This function is to navigate to drop down menus in interconnects page.
        Example:
        | Fusion UI Navigate To Dropdown Menus | ${interconnectname}, ${dropdownmenu} |
        """
        return interconnects.navigate_to_dropdown_menus(interconnectname, dropdownmenu)

    def tbird_fetch_icm_data_from_em(self, *inc_obj):
        """
            This function establishesssh to EM and returns interconnect fru and general data as dictionary
            Example:
            | Tbird Fetch icm Data From EM     | @(IC data) |
        """
        return interconnects.get_icm_data_from_em(inc_obj)

    def tbird_fusion_ui_validate_support_dump(self, uname, psword, hostip, baynumber, script_path):
        """validate support dump generated
           This function validates the support dump by extracting them and seeing if the file contains the baynumber
        """
        return interconnects.validate_support_dump(uname, psword, hostip, baynumber, script_path)

    def fusion_ui_verify_interconnect_uplinkport_view(self, *inc_obj):
        """ This function is used to verify the interconnect downlink port information
        Example:
        | Fusion UI Verify Interconnect UplinkPort View | @{interconnect list} |
        """
        return interconnects.verify_interconnect_uplinkport_view(inc_obj)

    def fusion_ui_verify_interconnect_downlinkport_view_tbird(self, *inc_obj):
        """ This function is used to verify the interconnect downlink port information
        Example:
        | Fusion UI Verify Interconnect Downlinkport View Tbird | @{interconnect list} |
        """
        return interconnects.verify_interconnect_downlinkport_view_tbird(inc_obj)

    def fusion_ui_verify_interconnect_downlinkport_view(self, interconnectname, enclname, *enc_obj):
        """ This function is used to verify the interconnect downlink port information
        Example:
        | Fusion UI Verify Interconnect Downlinkport View | ${interconnectname}, ${enclname}, @{enclosure list} |
        """
        return interconnects.verify_interconnect_downlinkport_view(interconnectname, enclname, enc_obj)

    def fusion_ui_verify_interconnect_activity_view(self, interconnectname):
        """ This function is used to verify the interconnect activity details
        Example:
        | Fusion UI Verify Interconnect Activity View | ${interconnectname} |
        """
        return interconnects.verify_interconnect_activity_view(interconnectname)

    def fusion_ui_verify_interconnect_recent_activity(self, interconnectname, message_list):
        '''
        Function to verify if all the activity messages passed in the message list are seen in the Interconnect activity page
        return True/False
        EXAMPLE :
        fusion_ui_verify_interconnect_recent_activity | ${interconnectname} | ${message_list}
        '''

        return interconnects.verify_interconnect_recent_activity(interconnectname, message_list)

    def fusion_ui_validate_interconnect_connector_info_tbird(self, *inc_obj):
        """ This function is used to verify the interconnect connector information
        Example:
        | Fusion UI Validate Interconnect Connector Info Tbird | @{interconnect list} |
        """
        return interconnects.validate_tbird_interconnect_connector_info(inc_obj)

    def fusion_ui_get_interconnect_state(self, icname):
        '''
        function to get the IC state
        Takes the ic name as input
        Returns None if the IC is not found OR if the State cannot be retrieved

        EXAMPLE:
        fusion_ui_get_interconnect_state | ${icname}
        '''
        return interconnects.get_interconnect_state(icname)

    def fusion_ui_get_ic_stacking_domain_role(self, icname):
        '''
        function to get the stacking domain role of the IC
        EXAMPLE:
        fusion_ui_get_ic_stacking_domain_role | ${icname}
        '''
        return interconnects.get_ic_stacking_domain_role(icname)

    def fusion_ui_get_ic_ipv4_address(self, icname):
        '''
        function to get the ipv4 address assigned to the IC
        EXAMPLE:
            fusion_ui_get_ic_ipv4_address | ${icname}
        '''
        return interconnects.get_ic_ipv4_address(icname)

    def tbird_fusion_ui_chloride_power_off(self, *chl_obj):
        """
            Perform power OFF action of Interconnect Modules
            Example:
            | Tbird Fusion Ui Chloride Power Off | @(IC data) |
        """
        return interconnects.fusion_ui_chloride_power_off(chl_obj)

    def tbird_fusion_ui_chloride_reset(self, *chl_obj):
        """
            Perform Interconnect Modules Reset operation
            Example:
            | Tbird Fusion Ui Chloride Reset | @(IC data) |
        """
        return interconnects.fusion_ui_chloride_reset(chl_obj)

    def tbird_fusion_ui_chloride_power_on(self, *chl_obj):
        """
            Perform power OFF action of Interconnect Modules
            Example:
            | Tbird Fusion Ui Chloride Power Off | @(IC data) |
        """
        return interconnects.fusion_ui_chloride_power_on(chl_obj)

    def tbird_fusion_ui_chloride_uid_action(self, *chl_obj):
        """
            Perform UID LED Off and ON action of Interconnect Modules
            Example:
            | Tbird Fusion Ui Chloride UID Action | @(IC data) |
        """
        return interconnects.fusion_ui_chloride_uid_action(chl_obj)

    def tbird_fusion_ui_check_chloride_extender_ports(self, *chl_obj):
        """
            Validates Extender ports information of Interconnect Modules
            Example:
            | Tbird Fusion Ui Check Chloride Extender Ports | @(IC data) |
        """
        return interconnects.chloride_extender_ports(chl_obj)

    def tbird_fusion_ui_select_logical_enclosure(self, *le_obj):
        """
            Selects given Logical Enclosure on LE Page
            Example:
            | Tbird Fusion Ui Select Logical Enclosure | @(LE data) |
        """
        return logicalenclosures.select_logical_enclosure(le_obj)

    def tbird_fusion_ui_check_chloride_general_view(self, *chl_obj):
        """
            Check the contents of Interconnect Modules General page attributes
            Example:
            | Tbird Fusion Ui Check Chloride General View | @(IC data) |
        """
        return interconnects.fusion_ui_chloride_general_view(chl_obj)

    def tbird_fusion_ui_create_le_support_dump(self, *le_obj):
        """
            Collect Logical Enclosure Support Dump
            Example:
            | Tbird Fusion Ui Create Le Support Dump | @(IC data) |
        """
        return interconnects.fusion_ui_collect_le_support_dump(le_obj)

    def tbird_fusion_ui_check_chloride_check_priv(self, *chl_obj):
        """
            Check user capability with respect to Interconnect Modules
            Example:
            | Tbird Fusion Ui Check Chloride Priv | @(IC data) |
        """
        return interconnects.fusion_ui_chloride_check_priv(chl_obj)

    def fusion_ui_verify_interconnect_hyperlinks(self, *interconnect_obj):
        """ This function is used to verify the hyperlinks between the
        Interconnects page and Enclosures page
        | fusion ui verify interconnect hyperlink | @{interconnect list}
        """
        return interconnects.verify_interconnect_hyperlinks(interconnect_obj)

    def fusion_ui_validate_natasha_interconnects_user_permissions(self, user_role, *interconnect_obj):
        """ This function is used to verify the user permissions for the Action Menu
        on the Interconnects page for all natasha interconnects
        | fusion ui validate natasha interconnects action menu for user | ${user_role} | @{interconnect list}
        """
        return interconnects.validate_natasha_interconnect_user_permissions(user_role, interconnect_obj)

    def fusion_ui_validate_sylvite_interconnects_user_permissions(self, user_role, *interconnect_obj):
        """ This function is used to Verify the user permissions for the Action Menu
        on the Interconnects page - Applicable for Sylvite

        | fusion ui validate sylvite interconnects user permissions | ${user_role} | @{interconnect list}
        """
        return interconnects.validate_sylvite_interconnect_user_permissions(user_role, interconnect_obj)

    def fusion_ui_sylvite_downlink_edit(self, *interconnect_obj):
        """ Edit Downlink Ports of sylvite
        Example:
        | Fusion UI Edit Interconnect | @{interconnect list} |
        """
        return interconnects.sylvite_downlink_edit(interconnect_obj)

    def fusion_ui_interconnect_power_off(self, *interconnect_obj):
        """
            Perform power OFF action of Interconnect Modules
            Example:
            | Fusion Ui Interconnect Power Off | @(IC data) |
        """
        return interconnects.power_off_interconnect(interconnect_obj)

    def fusion_ui_interconnect_power_on(self, *interconnect_obj):
        """
            Perform power ON action of Interconnect Modules
            Example:
            | Fusion Ui Interconnect Power On | @(IC data) |
        """
        return interconnects.power_on_interconnect(interconnect_obj)

    def fusion_ui_turn_on_interconnect_uid(self, *interconnect_obj):
        """
            Turn on UID for of Interconnect Modules
            Example:
            | Fusion Ui Turn On interconnect uid | @(IC data) |
        """
        return interconnects.turn_on_interconnect_uid(interconnect_obj)

    def fusion_ui_turn_off_interconnect_uid(self, *interconnect_obj):
        """
            Turn off UID for of Interconnect Modules
            Example:
            | Fusion Ui Turn Off interconnect uid | @(IC data) |
        """
        return interconnects.turn_off_interconnect_uid(interconnect_obj)

    def fusion_ui_validate_interconnect_uid_light_off(self, *interconnect_obj):
        """
            Verify UID off for all of Interconnect Modules
            Example:
            | fusion_ui_validate_interconnect_uid_light_off | @(IC data) |
        """
        return interconnects.validate_interconnect_uid_light_off(interconnect_obj)

    def fusion_ui_interconnect_reset(self, *interconnect_obj):
        """
            Reset of Interconnect Modules
            Example:
            | Fusion Ui Interconnect Turn Off UID | @(IC data) |
        """
        return interconnects.reset_interconnect(interconnect_obj)

    def fusion_ui_reset_C7000_interconnect_loop_and_pause_flood_protection(self, *interconnect_obj):
        """
            Perform reset and loop protection of Interconnect Module
            Example:
            | Fusion Ui Reset Loop And Pause Interconnect | @(IC data) |
        """
        return interconnects.reset_C7000_interconnect_loop_and_pause_flood_protection(interconnect_obj)

    def fusion_ui_soft_reset_natasha_interconnect(self, *interconnect_obj):
        """
            Perform Soft Reset action of Natasha Interconnect Modules
            Example:
            | Fusion Ui Soft Reset Natasha Interconnect | @(IC data) |
        """
        return interconnects.soft_reset_natasha_interconnect(interconnect_obj)

    def fusion_ui_hard_reset_natasha_interconnect(self, *interconnect_obj):
        """
            Perform Hard Reset action of Natasha Interconnect Modules
            Example:
            | Fusion Ui Hard Reset Natasha Interconnect | @(IC data) |
        """
        return interconnects.hard_reset_natasha_interconnect(interconnect_obj)

    def fusion_ui_tbird_validate_interconnect_link_ports_information_and_alerts(self, *interconnect_obj):
        """
            Validates the Interconnect link ports information, if port status is error
            validates the corresponding alerts information too.
            Example:
            | Fusion UI Tbird Validate Interconnect Link Ports Information And Alerts| @{interconnect list} |
        """
        return interconnects.tbird_validate_interconnect_link_ports_information_and_alerts(interconnect_obj)

    def fusion_ui_validate_uplinkport_qosstatistics(self, *interconnects_obj):
        """ Verify quality of Service Statistics visible in uplink ports
           Example:
                | `Fusion Ui Validate UplinkPort QosStatistics`  | @{license obj}    |
        """
        return interconnects.validate_uplinkport_qosstatistics(interconnects_obj)

    def fusion_ui_validate_downlinkport_qosstatistics(self, *interconnects_obj):
        """ Verify quality of Service Statistics visible in downlink ports
           Example:
                | `Fusion Ui Validate downlinkPort QosStatistics`  | @{license obj}    |
        """
        return interconnects.validate_downlinkport_qosstatistics(interconnects_obj)

    def fusion_ui_get_interconnect_error_message(self, *interconnect_obj):
        """ Get the error message from the "Interconnects" page
        Example
        | Fusion UI Get Interconnect Error Message | @{interconnect list} |
        """
        return interconnects.get_interconnects_error_message(interconnect_obj)

    def fusion_ui_get_tbird_interconnect_uplink_port_speed(self, *inc_obj):
        """ Get Interconnects uplink ports speed
        Example:
        | Fusion UI Get Tbird Interconnect Uplink Port Speed | @{interconnect list} |
        """
        return interconnects.get_tbird_interconnect_uplink_port_speed(inc_obj)
    # ##########################################################################
    # Logical Switch Groups Functions
    # ##########################################################################

    def fusion_ui_navigate_to_logical_switch_groups_page(self):
        """ Navigate to the "Logical Switch Groups" page
        Example:
        | Fusion UI Navigate To LSG Page |
        """
        logicalswitchgroups.navigate()

    def fusion_ui_create_logical_switch_groups(self, *lsg_obj):
        """ Create new logical switch group
        Example:
        | Fusion UI Create Logical Switch Groups | ${lsg list} |
        """
        return logicalswitchgroups.create_logical_switch_groups(lsg_obj)

    def fusion_ui_edit_logical_switch_groups(self, *lsg_obj):
        """ Edit Logical Switch Groups
        Example:
        | Fusion UI Edit Logical Switch Groups | ${lsg list} |
        """
        return logicalswitchgroups.edit_logical_switch_groups(lsg_obj)

    def fusion_ui_delete_logical_switch_group_by_name(self, lsg_name):
        """ Delete Logical Switch Group
        Example:
        | Fusion UI Delete Logical Switch Group By Name | ${lsg name} |
        """
        return logicalswitchgroups.delete_logical_switch_group_by_name(lsg_name)

    def fusion_ui_delete_logical_switch_groups(self, *lsg_obj):
        """ Delete Logical Switch Group
        Example:
        | Fusion UI Delete Logical Switch Groups | ${lsg list} |
        """
        return logicalswitchgroups.delete_logical_switch_groups(lsg_obj)

    def fusion_ui_check_user_privileges(self, user_name):
        """Check write privilege for user
        Example:
        |Fusion UI Check User Privileges | BA |
        """
        return logicalswitchgroups.check_user_privileges(user_name)

    def fusion_ui_get_all_lsg_switch_type(self):
        """Check write privilege for user
        Example:
        |Fusion UI Get All Lsg Switch Type |
        """
        return logicalswitchgroups.get_all_lsg_switch_type()

    def fusion_ui_add_label_logical_switch_groups(self, *net_obj):
        """ !!! Deprecated !!!
                - Please try to use fusion_ui_edit_labels_of_logical_switch_groups() instead !!!
            Adding Label to LSG
        Example:
        |Fusion UI Add Label Logical Switch Groups | ${label list} |
        """
        return logicalswitchgroups.add_label_logical_switch_groups(net_obj)

    def fusion_ui_edit_labels_of_logical_switch_groups(self, *lsg_obj):
        """ Editing Labels of LSGs
        Example:
        |Fusion UI Edit Labels Of Logical Switch Groups | @{lsg list} |
        """
        return logicalswitchgroups.edit_labels_of_logical_switch_groups(lsg_obj)

    def fusion_ui_edit_labels_of_resources(self, *resource_obj):
        """ Editing Labels of Resources
        Example:
        |Fusion UI Edit Labels Of Resources | @{resource list} |
        """
        return FusionUIBase.edit_labels_of_resources(resource_obj)

    def fusion_ui_delete_label_logical_switch_groups(self, *net_obj):
        """ !!! Deprecated !!!
                - Please try to use fusion_ui_edit_labels_of_logical_switch_groups() instead !!!
            Delete Label from LSG
        Example:
        |Fusion UI Delete Label Logical Switch Groups | ${label list} |
        """
        return logicalswitchgroups.delete_label_logical_switch_groups(net_obj)

    def fusion_ui_edit_label_logical_switch_groups(self, *net_obj):
        """ !!! Deprecated !!!
                - Please try to use fusion_ui_edit_labels_of_logical_switch_groups() instead !!!
            Edit LSg Label
        Example:
        |Fusion UI Edit Label Logical Switch Groups | ${label list} |
        """
        return logicalswitchgroups.edit_label_logical_switch_groups(net_obj)

    def fusion_ui_filter_by_label_logical_switch_groups(self, *net_obj):
        """ Filter by LSG label
        Example:
        |Fusion UI Filter By Label Logical Switch Groups | ${label list} |
        """
        return logicalswitchgroups.filter_by_label_logical_switch_groups(net_obj)

    def fusion_ui_verify_interconnect_downlinkport_view_cisco(self, *interconnect_obj):
        """ This function is used to verify the interconnect downlink port information
        Example:
        | Fusion UI Verify Interconnect Downlinkport View Cisco|  @{interconnect list} |
        """
        return interconnects.verify_interconnect_downlinkport_view_cisco(interconnect_obj)

    def fusion_ui_add_label_to_interconnect(self, *interconnect_list):
        """ Add Label To Interconnect
        This function is to add label to Interconnect
        Example:
        | Fusion UI Add Label To Interconnect    |    ${interconnect_list}    |
        """
        return interconnects.add_label_to_interconnect(interconnect_list)

    def fusion_ui_select_interconnect(self, switchName):
        """ Select Interconnects
        This function is to select Interconnect
        Example:
        | Fusion UI Select Interconnect    |    ${switchName}    |
        """
        return interconnects.select_interconnect(switchName)

    ###########################################################################
    # Data Center page functions
    # #########################################################################
    def fusion_ui_navigate_to_data_centers_page(self):
        """ Navigate to the "Data Centers" page
        Example:
        | Fusion UI Navigate To Data Centers Page |
        """
        return datacenters.navigate()

    def fusion_ui_add_datacenter(self, *net_obj):
        """ Add new datacenter(s)
        Example:
        | Fusion UI Add Datacenter | @{Datacenter list} |
        """
        return datacenters.add_datacenter(net_obj)

    def fusion_ui_remove_datacenter(self, *net_obj):
        """ Remove the datacenters in list
        Example:
        | Fusion UI Remove Datacenter | @{Datacenter list} |
        """
        return datacenters.remove_datacenter(net_obj)

    def fusion_ui_verify_datacenter(self, *net_obj):
        """ Verify the datacenter(s)
        Example:
        | Fusion UI Verify Datacenter | @{Datacenter list} |
        """
        return datacenters.verify_datacenter(net_obj)

    def fusion_ui_delete_all_datacenters(self):
        """ delete all appliance datacenters
         Example:
        | Fusion UI Delete All Datacenters |
        """
        return datacenters.delete_all_datacenters()

    # #########################################################################
    # Racks page functions
    # #########################################################################
    def fusion_ui_navigate_to_racks_page(self):
        """ Navigate to the "Racks" page
        Example:
        | Fusion UI Navigate To Racks Page |
        """
        return racks.navigate()

    def fusion_ui_edit_rack(self, *rack_obj):
        """ Edit rack(s) according to SAW XML data
        Example:
        | Fusion UI Edit Rack | @{edit rack list} |
        """
        return racks.edit_rack_properties(rack_obj)

    def fusion_ui_remove_rack(self, *rack_obj):
        """ Remove rack(s)
        Example:
        | Fusion UI Remove Rack | @{rack list} |
        """
        return racks.delete_rack(rack_obj)

    def fusion_ui_add_rack(self, *rack_obj):
        """ Add rack(s)
        Example:
        | Fusion UI Add Rack | @{rack list} |
        """
        return racks.add_rack(rack_obj)

    def fusion_ui_remove_all_racks(self, name_pattern=None):
        """ Remove all existing racks
        Example:
        | Fusion UI Remove All Racks |
        """
        return racks.remove_all_racks(name_pattern)

    def fusion_ui_verify_enclosure_in_rack(self, rack_obj, enclosurename_obj):
        """ Verify Enclosure In Rack
        Example:
        | Fusion UI Verify Enclosure In Rack | ${rack_obj} | ${enclosurename_obj} |
        """
        return racks.verify_enclosure_in_rack(rack_obj, enclosurename_obj)

    # #########################################################################
    # Power Delivery Devices page functions
    # #########################################################################
    def fusion_ui_navigate_to_power_delivery_devices_page(self):
        """ Navigate to the "Power Delivery Devices" page
        Example:
        | Fusion UI Navigate To Power Delivery Devices Page |
        """
        powerdeliverydevice.navigate()

    def fusion_ui_add_power_delivery_device(self, *pdd_obj):
        """ Add Power Delivery Device(s)
        Example:
        | Fusion UI Add Power Delivery Device | @{pdd list} |
        """
        return powerdeliverydevice.add_power_delivery_device(pdd_obj)

    def fusion_ui_delete_power_delivery_device(self, *pdd_obj):
        """ Delete Power Delivery Device(s)
        Example:
        | Fusion UI Delete Power Delivery Device | @{pdd list} |
        """
        return powerdeliverydevice.delete_power_delivery_device(pdd_obj)

    def fusion_ui_edit_power_delivery_device(self, *pdd_obj):
        """ Edit Power Delivery Device(s) using SAW XML data
        Example:
        | Fusion UI Edit Power Delivery Device | @{pdd list} |
        """
        return powerdeliverydevice.edit_power_delivery_device(pdd_obj)

    # #########################################################################
    # Unmanaged Devices page functions
    # #########################################################################
    def fusion_ui_navigate_to_unmanaged_devices_page(self):
        """ Navigate to the "Unmanaged Devices" page
        Example:
        | Fusion UI Navigate To Unmanaged Devices Page |
        """
        return unmanageddevices.navigate()

    def fusion_ui_add_unmanaged_device(self, *uds_obj):
        """ Add unmanaged device(s)
        Example:
        | Fusion UI Add Unmanaged Device | @{ud list} |
        """
        return unmanageddevices.add_unmanaged_device(uds_obj)

    def fusion_ui_edit_unmanaged_device(self, *uds_obj):
        """ Edit unmanaged device(s) using SAW XML data
        Example:
        | Fusion UI Edit Unmanaged Device | @{ud list} |
        """
        return unmanageddevices.edit_unmanaged_device(uds_obj)

    def fusion_ui_remove_unmanaged_device(self, *uds_obj):
        """ Remove unmanaged device(s)
        Example:
        | Fusion UI Remove Unmanaged Device | @{ud list} |
        """
        return unmanageddevices.remove_unmanaged_device(uds_obj)

    # #########################################################################
    # Settings page functions
    # #########################################################################
    def fusion_ui_create_support_dump(self, create_support_dump_obj):
        """Create Support Dump according to the date in the xml file
         Example:
         | Fusion UI Create Support Dump  | ${ceate_support_dump} |

        """
        return supportdump.create_dump_support(create_support_dump_obj)

    def fusion_ui_validate_create_support_dump_link_exists(self):
        """ | Fusion UI Validate Create Support Dump Link Exists  | """
        return supportdump.validate_create_support_dump_link_exists()

    def fusion_ui_edit_time_and_locale(self, time_and_locale_obj):
        """Edit Time And Locale Settings according to the data in the  xml file
         Example:
        | Fusion UI Edit Time and Locale  | ${time_and_locale} |

        """
        return timeandlocale.edit_time_and_locale(time_and_locale_obj)

    def fusion_ui_verify_time_and_locale(self, time_and_locale_obj):
        """Verify Time And Locale Settings according to the data in the  xml file
         Example:
        | Fusion UI Verify Time and Locale  | ${time_and_locale} |

        """
        return timeandlocale.verify_time_and_locale(time_and_locale_obj)

    def fusion_ui_edit_C7000_networking(self, networking_obj):
        """Edit C7000 Networking Settings according to the data in the xml file
         Example:
        | Fusion UI Edit C7000 Networking | ${networking} |

        """
        return networking.edit_C7000_networking(networking_obj)

    def fusion_ui_verify_C7000_networking(self, networking_obj):
        """Verify C7000 Networking Settings according to the data in the xml file
         Example:
        | Fusion UI Verify C7000 Networking | ${networking} |

        """
        return networking.verify_C7000_networking(networking_obj)

    def fusion_ui_get_appliance_networking(self):
        """Verify C7000 Networking Settings according to the data in the xml file
         Example:
        | Fusion UI Get Appliance Networking | ${networking} |

        """
        return networking.get_appliance_hostname_and_ip_address()

    def fusion_ui_add_license(self, *license_obj):
        """Add licenses to appliance
         Example:
        | Fusion UI Add License | ${licenses} |

        """
        return licenses.add_license(license_obj)

    def fusion_ui_verify_required_server_oneview_license(self, number):
        """Verify number of licensed server oneview license
         Example:
        | Fusion UI Verify Licensed Server Oneview License | 2 |

        """
        return licenses.verify_required_server_oneview_license(number)

    def fusion_ui_verify_required_server_oneview_wo_ilo_license(self, number):
        """Verify number of licensed server oneview w/o iLo license
         Example:
        | Fusion UI Verify Licensed Server Oneview wo iLo License | 2 |

        """
        return licenses.verify_required_server_oneview_wo_ilo_license(number)

    def fusion_ui_verify_licensed_server_oneview_license(self, number):
        """Verify number of licensed server oneview license
         Example:
        | Fusion UI Verify Licensed Server Oneview License | 2 |

        """
        return licenses.verify_licensed_server_oneview_license(number)

    def fusion_ui_verify_licensed_server_oneview_wo_ilo_license(self, number):
        """Verify number of licensed server oneview w/o iLo license
         Example:
        | Fusion UI Verify Licensed Server Oneview wo iLo License | 2 |

        """
        return licenses.verify_licensed_server_oneview_wo_ilo_license(number)

    def fusion_ui_verify_required_fcupgrade_license(self, number):
        """Verify number of fcupgrade licenses required
         Example:
        | Fusion UI Verify required fcupgrade License | 2 |

        """
        return licenses.verify_required_fcupgrade_license(number)

    def fusion_ui_verify_licensed_fcupgrade_interconnects(self, number):
        """Verify number of licensed interconnects fcupgrade
         Example:
        | Fusion UI Verify Licensed fcupgrade interconnects | 2 |

        """
        return licenses.verify_licensed_fcupgrade_interconnects(number)

    def fusion_ui_verify_available_fcupgrade_licenses(self, number):
        """Verify available number of fcupgrade licenses
         Example:
        | Fusion UI Verify Licensed fcupgrade licenses | 2 |

        """
        return licenses.verify_available_fcupgrade_licenses(number)

    def fusion_ui_navigate_to_settings_page(self):
        """ Navigate to the "Settings" page
        Example:
        | Fusion UI Navigate To Settings Page |
        """
        return settings.navigate()

    def fusion_ui_edit_services_access(self, enabled):
        """ Edit the services access - function to enable or disable support access
        Example:
        | Fusion UI Edit Services Access | ${True} |
        | Fusion UI Edit Services Access | ${False} |
        """
        return settings.edit_services_access(enabled)

    def fusion_ui_restart(self):
        """ Restart the appliance
        Example:
        | Fusion UI Restart |
        """
        return settings.restart()

    def fusion_ui_shutdown(self):
        """ Shutdown the appliance
        Example:
        | Fusion UI Shutdown |
        """
        return settings.shut_down()

    def fusion_ui_download_audit_logs(self, *folder):
        """Download the Fusion audit logs to the folder specified
        Example:
        | Fusion UI Download Audit Logs | c:/MyAuditLogs |
        """
        if len(folder) == 0:
            folder = None
        elif len(folder) > 1:
            raise ui_lib.FatalError("Too many arguments to Fusion UI Download Audit Logs")
        else:
            folder = folder[0]
        return settings.download_audit_logs(folder)

    def fusion_ui_download_cidebug_logs(self, *folder):
        """Download the Fusion ciDebug logs to the folder specified
        Example:
        | Fusion UI Download Cidebug Logs | c:/MyciDebugLogs |
        """
        folder = folder[0]
        return settings.download_cidebug_logs(folder)

    def fusion_ui_edit_address_and_identifier(self, *edit_add_iden):
        """ edit_address_and_identifier

        Example:
        | Fusion UI_edit_address_and_identifier  ${TestData.editAddressIdentifier}|
        """
        return settings.edit_address_and_identifier(edit_add_iden)

    def fusion_ui_verify_address_and_identifier_used_number(self, *address_obj):
        """ verify_address_and_identifier_used_number

        Example:
        | Fusion UI Verify Address And Identifier Used Number ${TestData.AddressIdentifier}|
        """
        return settings.verify_address_and_identifier_used_number(address_obj)

    def fusion_ui_create_backup(self):
        """
        Create Backup : function to create fusion appliance backup
        """
        return settings.create_backup()

    def fusion_ui_download_backup(self, backupdirectory):
        """ Download Backup for fusion appliance, the download will happen at 'C:\\BackupDownloadFolder'
        NOTE :
        > As downloading fusion appliance back-up involves windows object,
        > and to handle the download window, we need to add below mentioned lines of code
        > in 'C:\Python27\Lib\site-packages\robotframework_selenium2library-1.2.0-py2.7.egg\Selenium2Library\resources\firefoxprofile\prefs.js'
        >
                user_pref("browser.download.folderList",2);
                user_pref("browser.download.dir",'C:\\BackupDownloadFolder');
                user_pref("browser.helperApps.neverAsk.saveToDisk","application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
                user_pref("browser.download.manager.scanWhenDone", false);
                user_pref("browser.download.manager.showAlertOnComplete", true);
                user_pref("browser.download.manager.useWindow", false);
                user_pref("browser.helperApps.alwaysAsk.force", false);

        > This will make sure the download happens silently at the directory specified
        """
        return settings.download_backup(backupdirectory)

    def fusion_ui_restore_from_backup(self, backupdirectory=None):
        """ Restore From Backup : restore backup for fusion appliance,

            NOTE : This code is dependent on download_backup function, execute download_backup then go for restore_from_backup

            PRE-REQUISITES :
                > AutoIT used to upload back-up file to the appliance.
                  Steps to configure AUTOIT,
                    1. Download autoit-v3-setup and pywin32-218.win-amd64-py2.7 (or pywin32-214.win32-py2.7) to your system
                    2. register AUTOITX3 , type on cmd prompt:
                        C:\Program Files (x86)\AutoIt3\AutoItX>regsvr32 AutoItX3_x64.dll
                        OR
                        C:\Program Files (x86)\AutoIt3\AutoItX>regsvr32 AutoItX3.dll
                    3. Download and install AUTOIT module from robot framework website.

        """
        return settings.restore_from_backup(backupdirectory)

    def fusion_ui_add_directory_server(self, *user_obj):
        """ add a server for OpenLDAP or Active Directory authentication
        Example:
        | Fusion UI Add Directory Server    ${directory_name} |
        """
        return settings.add_directory_server(*user_obj)

    def fusion_ui_del_directory_server(self, directory_name, fail_on_err=False):
        """ delete a OpenLDAP or Active Directory server for teardown
        Example:
        | Fusion UI Del Directory Server    ${directory_name}    ${fail_on_err}  |
        """
        return settings.del_directory_server(directory_name, fail_on_err)

    def fusion_ui_add_alert_notifications(self, *notifications_obj):
        """ Add Alert notification
        Example:
        | Fusion UI Add alert Notifications    | ${notifications_obj}     |
        """
        return settings.add_alert_notifications(notifications_obj)

    def fusion_ui_add_all_licenses_from_data_file(self, *license_obj):
        """ Add all licenses that contain their key in the data file
        Example:
        | Fusion UI Add All Licenses From Data File | ${license_obj} |
        """
        return settings.add_all_licenses_from_data_file(license_obj)

    def fusion_ui_create_support_dump_from_data_file(self, create_support_dump_obj):
        """Create Support Dump according to the date in the xml file
         Example:
         | Fusion UI Create Support Dump  | ${create_support_dump} |
        """
        return settings.create_support_dump_from_data_file(create_support_dump_obj)

    def fusion_ui_appliance_factory_reset(self, user_name, password):
        """ appliance factory reset
        Example:
        | Fusion UI Appliance Factory Reset    | ${user_name} | ${password}    |
        """
        return settings.appliance_factory_reset(user_name, password)

    def fusion_ui_add_snmp_trap_forwarding_destination(self, *snmp_obj):
        """ Edit SNMP Settings for Trap Forwarding
        Example:
        | Fusion UI Add SNMP Trap Forwarding Destination | ${snmp_obj} |
        """
        return settings.add_snmp_trap_forwarding_destination(snmp_obj)

    # ##########################################################################################
    #                IP Pools Keywords  #########
    # ##########################################################################################

    def fusion_ui_validate_settings_page_addressesidentifiers_edit_link_for_user(self):
        """ Keyword to check if the Edit icon is visible for a user on hovering over the Addresses and identifiers link in settings page.
            If visible check if the Edit dialog opens on clicking the icon
            raises exception if edit icon is visible

        Example:
           | fusion_ui_validate_settings_page_addressesidentifiers_edit_link_for_user |
        """
        return settings.validate_settings_page_addressesidentifiers_edit_link_for_user()

    def fusion_ui_validate_addressesidentifiers_actions_menu_edit_option_for_user(self):
        """ Keyword to check if the Edit option is visible for a user in actions menu of address and identifiers page
            If visible check if the Edit dialog opens on clicking edit
            raises exception if edit option is visible

        Example:
           | fusion_ui_validate_addressesidentifiers_actions_menu_edit_option_for_user |
        """
        return settings.validate_addressesidentifiers_actions_menu_edit_option_for_user()

    def fusion_ui_get_ipv4_subnet_and_addressranges(self):
        """
        Keyword to list the subnet and address range table

        Example:
            fusion_ui_get_ipv4_subnet_and_addressranges
        """
        return settings.get_ipv4_subnet_and_addressranges_in_addressidentifiers_page()

    def fusion_ui_get_ipv4_addresses_count(self):
        """
        Keyword to get the total IPV4 addresses count from settings page

        Example:
            ${count}=    fusion_ui_get_ipv4_addresses_count
        """

        return settings.get_ipv4_addresses_count()

    def fusion_ui_create_ipv4_subnet_and_addressrange(self, *subnet_obj):
        """
            Keyword to create subnet and  address ranges

        Example:
            fusion_ui_create_ipv4_subnet_and_addressrange   |   @{subnet_obj}

        """
        return settings.create_ipv4_subnet_and_addressrange(subnet_obj)

    def fusion_ui_edit_ipv4_subnet_and_addressrange(self, *subnet_obj):
        """
        Keyword to Edit an existing Subnet and address range

        Example:
            fusion_ui_edit_ipv4_subnet_and_addressrange |   @{subnet_obj}
        """
        return settings.edit_ipv4_subnet_and_addressrange(subnet_obj)

    def fusion_ui_delete_ipv4_subnet_and_addressrange(self, *subnet_obj):
        """
        Keyword to delete ipv4 subnet and address range

        Example:
            fusion_ui_delete_ipv4_subnet_and_addressrange  |  @{subnet_obj}
        """
        return settings.delete_ipv4_subnet_and_addressrange(subnet_obj)

    def fusion_ui_enable_disable_addressrange_of_ipv4subnet(self, subnetid, *addressrange_obj):
        """
        Keyword to Enable/Disable an Address range of an existing subnet

        Exmaple:
            fusion_ui_enable_disable_addressrange_of_subnet |  ${Subnetid} |  @{address_range_obj}
        """
        return settings.enable_disable_addressrange_of_ipv4subnet(subnetid, addressrange_obj)

    def fusion_ui_add_ipv4_addressrange_to_subnet(self, subnetid, *addressrange_obj):
        """
        Keyword to add Address range to an existing subnet

        Example:
            fusion_ui_add_ipv4_addressrange_to_subnet  |  ${Subnetid} |  @{address_range_obj}
        """
        return settings.add_ipv4_addressrange_to_edit_subnet(subnetid, addressrange_obj)

    def fusion_ui_edit_ipv4_addressrange_in_subnet(self, subnetid, *addressrange_obj):
        """
        Keyword to edit Address ranges of an existing subnet

        Example:
            fusion_ui_edit_ipv4_addressrange_in_subnet  |  ${Subnetid} |  @{address_range_obj}
        """
        return settings.edit_ipv4_addressrange_in_subnet(subnetid, addressrange_obj)

    def fusion_ui_delete_ipv4_addressrange_from_subnet(self, subnetid, *addressrange_obj):
        """
        Keyword to delete Address ranges of an existing subnet

        Example:
            fusion_ui_delete_ipv4_addressrange_from_subnet  |  ${Subnetid} |  @{address_range_obj}
        """
        return settings.delete_ipv4_addressrange_from_subnet(subnetid, addressrange_obj)

    def fusion_ui_get_count_of_allocatedip_in_addressrange(self, subnetid, rangename):
        """
        Keyword to get the allocated IP count of a range in a subnet

        Example:
            ${count}=  | fusion_ui_get_count_of_allocatedip_in_addressrange  | ${subnetid} | ${rangename}
        """
        return settings.get_count_of_allocatedip_in_addressrange(subnetid, rangename)

    def fusion_ui_verify_ipv4_subnet_and_addressrange_in_edit_dialog(self, *subnet_obj):
        """
        Keyword to verify the ipv4 subnet and address range attributes as displayed in
        edit addresses and identifiers dialog

        Example:
            fusion_ui_verify_ipv4_subnet_and_addressrange_in_edit_dialog | @{subnet_obj}
        """
        return settings.verify_ipv4_subnet_and_addressrange_in_edit_dialog(subnet_obj)

    def fusion_ui_verify_ipv4_subnet_and_addressrange_in_addressesidentifiers_page(self, *subnet_obj):
        """
        Keyword to verify the ipv4 subnet and address range attributes as displayed in
        address and identifiers page

        Example:
            fusion_ui_verify_ipv4_subnet_and_addressrange_in_addressesidentifiers_page | @{subnet_obj}
        """
        return settings.verify_ipv4_subnet_and_addressrange_in_addressesidentifiers_page(subnet_obj)

    def fusion_ui_verify_ipv4_addressranges_of_subnet_in_edit_dialog(self, subnetid, *addressrange_obj):
        """
        Keyword to verify the address ranges of a subnet in the edit addresses and identifiers dialog

        Example:
            fusion_ui_verify_ipv4_addressranges_of_subnet_in_edit_dialog |  ${Subnetid} |  @{address_range_obj}
        """
        return settings.verify_ipv4_addressranges_of_subnet_in_edit_dialog(subnetid, addressrange_obj)

    def fusion_ui_verify_ipv4_addressranges_of_subnet_in_addressesidentifiers_page(self, subnetid, *addressrange_obj):
        """
        Keyword to verify the address ranges of a subnet in the addresses and identifiers page

        Example:
            fusion_ui_verify_ipv4_addressranges_of_subnet_in_addressesidentifiers_page |  ${Subnetid} |  @{address_range_obj}
        """
        return settings.verify_ipv4_addressranges_of_subnet_in_addressesidentifiers_page(subnetid, addressrange_obj)

    def fusion_ui_verify_addressrange_state(self, subnetid, *addressrange_obj):
        """
        Keyword to verify the address range state of a subnet in edit dialog and addresses and identifiers page

        Example:
            fusion_ui_verify_addressrange_state |  ${Subnetid} |  @{address_range_obj}
        """

        return settings.verify_addressrange_state(subnetid, addressrange_obj)

    def fusion_ui_verify_networks_association_or_disassociation_to_subnet(self, subnetid, associationstate, *network_list):
        '''
        Keyword to verify the Association/ Disassociation of network to/from a subnet.

        Example:
            fusion_ui_verify_networks_association_or_disassociation_to_subnet | ${Subnetid} | True |  @{associated_network_list}

            OR

            fusion_ui_verify_networks_association_or_disassociation_to_subnet | ${Subnetid} | False |  @{disassociated_network_list}

        '''
        return settings.verify_networks_association_or_disassociation_to_subnet(subnetid, associationstate, network_list)

    def fusion_ui_delete_subnet_verify_warning_and_associations_in_dialog(self, subnetid, *associated_obj_list):
        """
        Keyword to delete a subnet and verify the specified associated resources are listed in the warning

        Example:
            fusion_ui_delete_subnet_verify_warning_and_associations_in_dialog | ${Subnetid} | @{associated_obj_list}
        """
        return settings.delete_subnet_verify_warning_and_associations_in_dialog(subnetid, associated_obj_list)

    def fusion_ui_delete_range_verify_warning_and_associations_in_dialog(self, subnetid, rangename, *associated_obj_list):
        """
        Keyword to delete a range of a subnet and verify the specified associated resources are listed in the warning

        Example:
            fusion_ui_delete_subnet_verify_warning_and_associations_in_dialog | ${Subnetid} | ${rangename} | @{associated_obj_list}
        """
        return settings.delete_range_verify_warning_and_associations_in_dialog(subnetid, rangename, associated_obj_list)

    def fusion_ui_is_ip_in_subnet(self, ip_to_verify, *editidentifiers_obj):
        '''
        function to verify if the ip specified is in  any one of the ranges provided as input. Returns a boolean value
        EXAMPLE:
            fusion_ui_is_ip_in_subnet | ${ip_to_verify} | @{editidentifiers_obj}
        '''
        return settings.is_ip_in_subnet(ip_to_verify, editidentifiers_obj)

    # ############### IP POOLS Keywords End #############################################

    def fusion_ui_settings(self):
        """ Access Settings for Required Information showing to the current brand
        Example:
        | Fusion UI Settings |
        """

        return rebranding.rebrand_certificates()
    # #########################################################################
    # Users and Groups page functions
    # #########################################################################

    def fusion_ui_navigate_to_users_and_groups_page(self):
        """ Navigate to the users and groups page
        Example:
        | Fusion UI Navigate To Users And Groups Page |
        """
        return usersandgroups.navigate()

    def fusion_ui_create_user(self, *user_obj):
        """ Create new user(s)
        Example:
        | Fusion UI Create User | @{user list} |
        | Fusion UI Create User | Get Data By Property   role  Network administrator |
        """
        return usersandgroups.create_user(*user_obj)

    def fusion_ui_remove_user(self, *user_obj):
        """ Remove user(s)
        Example:
        | Fusion UI Remove User | @{user list} |
        """
        return usersandgroups.remove_user(*user_obj)

    def fusion_ui_edit_users(self, *user_obj):
        """ Edit user(s)
        Example:
        | Fusion UI Edit Users | @{user list} |
        """
        return usersandgroups.edit_users(*user_obj)

    def fusion_ui_add_activedirectory_users(self, *user_obj):
        """ Add AD users
        Example:
        | Fusion UI Add Activedirectory Users | @{user list} |
        """
        return usersandgroups.add_active_directory_users_and_groups(*user_obj)

    def fusion_ui_add_directory_users(self, *user_obj):
        """ Add AD users
        Example:
        | Fusion UI Add Directory Users | @{user list} |
        """
        return usersandgroups.add_directory_users_and_groups(*user_obj)

    def fusion_ui_remove_directory_user_or_group(self, *user_obj):
        """ Remove directory users or groups
        Example:
        | Fusion UI Remove Directory User or Group | @{user list} |
        """
        return usersandgroups.remove_directory_user_or_group(*user_obj)

    def fusion_ui_edit_current_session_users(self, *user_obj):
        """ Edit current session user(s)
        Example:
        | Fusion UI Edit Current Session Users | @{user list} |
        """
        return usersandgroups.edit_current_session_user(user_obj)

    def fusion_ui_verify_userdata(self, *user_obj):
        """ Verify user data
        Example:
        | Fusion UI Verify Userdata | ${user name} |
        """

        return usersandgroups.userdata_validation(*user_obj)

    def fusion_ui_select_user(self, name):
        """ select user from the users and group page
        Example:
        | Fusion UI Select User    ${user} |
        """
        return usersandgroups.select_user(name)

    def fusion_ui_delete_all_appliance_users(self):
        """ Remove user(s)
        Example:
        | Fusion UI delete all appliance users |
        """
        return usersandgroups.remove_all_users()

    # #########################################################################
    # Storage Systems page functions
    # #########################################################################

    def fusion_ui_add_storage_systems(self, *storagesys_obj):
        """ Add storage systems to fusion appliance
            Exapmle:
            | Fusion UI add storage systems | @{storagesys}|
        """
        return storagesystems.add_storage_systems(*storagesys_obj)

    def fusion_ui_edit_storage_system(self, *storagesystemname):
        """ edit storage systems
            Exapmle:
            | Fusion UI edit storage systems | storagesytemname|
        """
        return storagesystems.edit_storage_systems(*storagesystemname)

    def fusion_ui_edit_storage_systems(self, *storagesystem):
        """ edit storage systems
            Exapmle:
            | Fusion UI edit storage systems | storagesytems|
        """
        return storagesystems.edit_storage_systems(*storagesystem)

    def fusion_ui_edit_credentials_storage_system(self, *storagesystemname):
        """ edit storage systems credentials
            Exapmle:
            | Fusion UI edit credentials storage systems | storagesytemname|
        """
        return storagesystems.edit_credentials_storage_system(*storagesystemname)

    def fusion_ui_edit_credentials_storage_system_negative(self, *storagesystemname):
        """ edit storage systems credentials
            Exapmle:
            | Fusion UI edit credentials storage systems | storagesytemname|
        """
        return storagesystems.edit_storage_system_credentials_negative(*storagesystemname)

    def fusion_ui_remove_storage_systems(self, *storagesys_obj):
        """ remove storage systems to fusion appliance
            Exapmle:
            | Fusion UI remove storage systems | @{storagesys}|
        """
        return storagesystems.remove_storage_systems(*storagesys_obj)

    def fusion_ui_refresh_storage_system(self, *storagesys_obj):
        """ refresh storage system
            Example:
            | Fusion UI refresh storage system | storagesystemname|
        """
        return storagesystems.refresh_storage_systems(*storagesys_obj)

    def fusion_ui_verify_storage_system(self, *storagesys_obj):
        """ verify storage system
            Example:
            | Fusion UI Verify Storage System | storagesystemname|
        """
        return storagesystems.verify_storage_system(*storagesys_obj)

    def fusion_ui_navigate_to_storage_systems_page(self):
        """ Navigate to the storage systems page
        Example:
        | Fusion UI Navigate to storage systems Page |
        """
        return storagesystems.navigate()

    def fusion_ui_delete_all_storage_systems(self):
        """ delete all storage system
            Example:
            | Fusion UI delete all storage systems
        """
        return storagesystems.delete_all_storage_systems()

    def fusion_ui_select_storage_system(self, storagesystemname):
        """ select storage system
            Example:
            | Fusion UI Select storage system    | ${storagesystemname}|
        """
        return storagesystems.select_storage_system(storagesystemname)

    def fusion_ui_verify_storage_system_links(self, *storagesys_links):
        """ verify storage system links
            Example:
            | Fusion UI Verify Storage System Links | @{storagesys_links}|
        """
        return storagesystems.verify_storage_system_links(*storagesys_links)

    # #########################################################################
    # Volume Sets page functions
    # #########################################################################

    def fusion_ui_navigate_to_volume_sets_page(self):
        """ Navigate to the volume sets page
        Example:
        | Fusion UI Navigate to Volume Sets Page |
        """
        return volumesets.navigate()

    def fusion_ui_verify_volume_set_links(self, *volumeset_links):
        """ verify volume sets links
            Example:
            | Fusion UI Verify Volume Set Links | @{volumeset_links}|
        """
        return volumesets.verify_volume_set_links(*volumeset_links)

    def fusion_ui_verify_no_volumeset_actions_exist(self):
        """ verify volume sets page does not have any actions
            Example:
            | Fusion UI Verify no Volumeset Actions Exist |
        """
        return volumesets.verify_no_actions_exist()

    def fusion_ui_verify_volume_sets(self, *volumesets_obj):
        """ verify volume sets page has volume sets listed
            Example:
            | Fusion UI Verify Volume Sets | @{volumesets}|
        """
        return volumesets.verify_volume_sets(*volumesets_obj)

    # #########################################################################
    # Storage Pools page functions
    # #########################################################################

    def fusion_ui_edit_storage_pools(self, *storagepool_obj):
        """ Edit storage pools
            Example:
            | Fusion UI Edit Storage Pools | @{storagepool}|
        """
        return storagepools.edit_storage_pools(storagepool_obj)

    def fusion_ui_refresh_storage_pool(self, storagepoolname, storagesystemname):
        """ refresh storage pool
            Example:
            | Fusion UI refresh storage pool | storagepoolname|
        """
        return storagepools.refresh_storage_pool(storagepoolname, storagesystemname)

    def fusion_ui_refresh_storage_pools(self, *storagepool_obj):
        """ refresh storage pool
            Example:
            | Fusion UI refresh storage pool | storagepoolname|
        """
        for pool in storagepool_obj:
            if not storagepools.refresh_storage_pool(pool.name, pool.storagename):
                return False
        return True

    def fusion_ui_navigate_to_storage_pools_page(self):
        """ Navigate to the storage pools page
        Example:
        | Fusion UI Navigate to storage pools Page |
        """
        return storagepools.navigate()

    def fusion_ui_verify_storage_pool_links(self, *storagepool_links):
        """ verify storage pool links
            Example:
            | Fusion UI Verify Storage pool Links | @{storagepool_links}|
        """
        return storagepools.verify_storage_pool_links(*storagepool_links)

    # #########################################################################
    # Storage Volume Template page functions
    # #########################################################################

    def fusion_ui_navigate_to_storage_volume_templates_page(self):
        """ Navigate to the storage volumes page
        Example:
        | Fusion UI Navigate to storage volume Templates Page |
        """
        return storagetemplates.navigate()

    def fusion_ui_create_storage_volume_templates(self, *storagetemplates_obj):
        """ create_storage_templates to fusion appliance
            Example:
            | Fusion UI create storage volume templates| @{storagetemplates}|
        """
        return storagetemplates.create_storage_volume_templates(*storagetemplates_obj)

    def fusion_ui_edit_storage_volume_template(self, *storagetemplates_obj):
        """ edit storage systems
            Example:
            | Fusion UI edit storage systems | @{storagetemplates}|
        """
        return storagetemplates.edit_storage_volume_templates(*storagetemplates_obj)

    def fusion_ui_edit_settings_storage_volume_template(self, reqdtemplatevolumecreation):
        """ edit storage volume template
            Example:
            | Fusion UI edit settings storage volume template| reqdtemplatevolumecreation  |
        """
        return storagetemplates.edit_settings_storage_volume_template(reqdtemplatevolumecreation)

    def fusion_ui_delete_storage_volume_template(self, *storagetemplates_obj):
        """ edit storage volume template
            Example:
            | Fusion UI delete storage volume template| @{storagetemplates}|
        """
        return storagetemplates.delete_storage_volume_templates(*storagetemplates_obj)

    def fusion_ui_delete_all_storage_templates(self):
        """ delete all  storage volume template
            Example:
            | Fusion UI delete all storage volume template
        """
        return storagetemplates.delete_all_storage_templates()

    def fusion_ui_select_storage_template(self, storagetemplatename):
        """ select storage volume template
            Example:
            | Fusion UI select storage template
        """
        return storagetemplates.select_storage_template(storagetemplatename)

    def fusion_ui_verify_volume_template_links(self, *storagetemplate_links):
        """ Verify volume template screen links
            Example:
            | Fusion UI Verify Volume Template Links  | @{storagetemplate_links}|
        """
        return storagetemplates.verify_volume_template_links(*storagetemplate_links)

    # #########################################################################
    # Storage Volume page functions
    # #########################################################################
    def fusion_ui_create_storage_volumes(self, *storagevolumes_obj):
        """ create storage volume for fusion appliance
            Example:
            | Fusion UI create storage volumes| @{storagevolumes_obj}|
        """
        return volumes.create_storage_volumes(*storagevolumes_obj)

    def fusion_ui_add_storage_volumes(self, *storagevolumes_obj):
        """ add_storage_volume for fusion appliance
            Example:
            | Fusion UI add storage volumes| @{storagevolumes_obj}|
        """
        return volumes.add_storage_volumes(storagevolumes_obj)

    def fusion_ui_edit_storage_volumes(self, *storagevolumes_obj):
        """ edit_storage_volume for fusion appliance
            Example:
            | Fusion UI edit storage volumes| @{storagevolumes_obj}|
        """
        return volumes.edit_storage_volumes(*storagevolumes_obj)

    def fusion_ui_refresh_storage_volumes(self, *storagevolumes_obj):
        """ refresh_storage_volume for fusion appliance
            Example:
            | Fusion UI refresh storage volumes| @{storagevolumes_obj}|
        """
        return volumes.refresh_storage_volumes(*storagevolumes_obj)

    def fusion_ui_delete_storage_volumes(self, *storagevolumes_obj):
        """ delete_storage_volume for fusion appliance
            Example:
            | Fusion UI delete storage volumes| @{storagevolumes_obj}|
        """
        return volumes.delete_storage_volumes(*storagevolumes_obj)

    def fusion_ui_delete_storage_volume(self, storagevolume, deletefrom):
        """ delete_storage_volume for fusion appliance
            Example:
            | Fusion UI delete storage volume| storagevolume|deletefrom|

            'deletefrom' paramter should be passed as 'ApplianceOnly', if a deletion only from appliance is desired.
        """
        return volumes.delete_storage_volume(storagevolume, deletefrom)

    def fusion_ui_validate_storage_volume_existing_by_name(self, volume_name):
        """validate storage volume existing by name
            Example:
            | Fusion UI Validate Storage Volume Existing By Name | ${volume_name} |
        """
        return volumes.validate_storage_volume_existing_by_name(volume_name)

    def fusion_ui_validate_storage_volume_not_existing_by_name(self, volume_name):
        """validate storage volume not existing by name
            Example:
            | Fusion UI Validate Storage volume Not Existing By Name | ${volume_naem} |
        """
        return volumes.validate_storage_volume_not_existing_by_name(volume_name)

    def fusion_ui_create_snapshots_storage_volume(self, *storagevolumesnapshots_obj):
        """ create_volume_snapshots for fusion appliance
            Example:
            | Fusion UI create snapshots storage volume| @{storagevolumesnapshots_obj}|
        """
        return volumes.create_volume_snapshots(*storagevolumesnapshots_obj)

    def fusion_ui_delete_storage_volume_snapshots_by_version(self, version=4.2, *volumesnapshots):
        """ delete volume snapshots for volume from fusion appliance
            Example:
            | Fusion UI delete snapshots storage volume| *volumesnapshots
        """
        return volumes.delete_volume_snapshots(version, *volumesnapshots)

    def fusion_ui_navigate_to_storage_volumes_page(self):
        """ Navigate to the storage volumes page
        Example:
        | Fusion UI Navigate to storage volumes Page |
        """
        return volumes.navigate()

    def fusion_ui_add_label_to_volume(self, *volume_label):
        """ Add label to volume
            Example:
            | Fusion UI Add Lable To Volume    | ${volume_label}|
        """
        return volumes.add_label_to_volume(volume_label)

    def fusion_ui_delete_all_storage_volumes(self):
        """ Delete all storage volumes
            Example:
            | Fusion UI delete all storage volumes |
        """
        return volumes.delete_all_storage_volume()

    def fusion_ui_select_storage_volume(self, storagevolumename):
        """ select storage volume
            Example:
            | Fusion UI select storage volume | ${storagevolumename}|
        """
        return volumes.select_storage_volume(storagevolumename)

    def fusion_ui_select_label_for_volume(self, volume_name, label):
        """ select_lable_for_volume for fusion appliance
            Example:
            | Fusion UI Select Label For Volume    | ${volume_name}    ${label}|
        """
        return volumes.select_label_for_volume(volume_name, label)

    def fusion_ui_add_storage_volume(self, *storagevolume_obj):
        """ Add existing storage volume
            Example:
            | Fusion UI Add Storage Volume     | @{storagevolume_obj}|
        """
        return volumes.add_storage_volume(storagevolume_obj)

    def fusion_ui_revert_storage_volume_snapshots(self, *storagevolumes_obj):
        """ revert created snapshot
            Example:
            | Fusion UI revert storage volume snapshots| @{storagevolumes_obj}|
        """
        return volumes.revert_created_snapshot(*storagevolumes_obj)

    def fusion_ui_create_volume_using_snapshot(self, *storagevolumes_obj):
        """ create volume using snapshot
            Example:
            | Fusion UI Create Volume Using Snapshot| @{storagevolumes_obj}|
        """
        return volumes.create_volume_using_snapshot(*storagevolumes_obj)

    def fusion_ui_verify_storage_volume(self, *storagevolume_obj):
        """ verify storage volume
            Example:
            | Fusion UI Verify Storage volume | @{storagevolume_obj}|
        """
        return volumes.verify_storage_volume(*storagevolume_obj)

    def fusion_ui_verify_volumes_links(self, *storagevolumes_links):
        """ Verify storage volumes screen links
            Example:
            | Fusion UI Verify Volumes Links  | @{storagevolumes_links}|
        """
        return volumes.verify_volume_links(*storagevolumes_links)

    def fusion_ui_verify_storage_volume_inconsistent(self, *storagevolumes_obj):
        """ create storage volume inconsistent for fusion appliance
            Example:
            | Fusion UI verify  storage volume inconsistent | @{storagevolumes_obj}|
        """
        return volumes.verify_storage_volume_inconsistent(*storagevolumes_obj)

    # #########################################################################
    # SAN Managers page functions
    # #########################################################################
    def fusion_ui_check_zone_name_format(self, *sans_obj):
        """SPSSp016 - F462 - Zone name format checkin
            Example:
            |Fusion UI Check zone name format| ${sans}
        """
        return sans.check_zone_name_format(*sans_obj)

    def fusion_ui_verify_can_not_use_invalid_text_for_zone_and_alias_format(self, *sans_obj):
        """ Verify Can not use invalid text for zone and alias format    2350
            Example:
            |Fusion UI Verify Can not use invalid text for zone and alias format| ${sans}
        """
        return sans.verify_can_not_use_invalid_text_for_zone_and_alias_format(*sans_obj)

    def fusion_ui_verify_sans(self, *sans_obj):
        """ Verify SANs according to the date in the xml file
             Example:
             | Fusion UI Verify SANs  | ${sans} |
        """
        return sans.verify_sans(*sans_obj)

    def fusion_ui_edit_sans(self, *sans_obj):
        """ Edit SANs according to the date in the xml file
             Example:
             | Fusion UI Edit SANs  | ${sans} |
        """
        return sans.edit_sans(*sans_obj)

    def fusion_ui_can_not_delete_enclosure(self, *enc_obj):
        """ Verify Can Not Delete enclosure(s)
        Example:
        | Fusion UI Can Not Delete Enclosure | @{enclosure list} |
        """
        return enclosures.can_not_remove_enclosure(enc_obj)

    def fusion_ui_validate_can_not_add_enclosure(self):
        """ Validate appliance should not add monitored/managed enclosure as network administrator
        Example:
        | Fusion UI Validate Can Not Add Enclosure |
        """
        return enclosures.validate_can_not_add_enclosure()

    def fusion_ui_validate_can_not_edit_enclosure(self, *enc_obj):
        """ Validate appliance should not edit monitored/managed enclosure use invalid name
        Example:
        | Fusion UI Validate Can Not Edit Enclosure | @{enclosure list} |
        """
        return enclosures.validate_can_not_edit_enclosure(enc_obj)

    def fusion_ui_validate_interconnect_error_state(self, *enc_obj):
        """ Validate critical interconnect has valid error message
        Example:
        | Fusion UI Validate Interconnect Error State | @{enclosure list} |
        """
        return enclosures.validate_interconnect_error_state(enc_obj)

    def fusion_ui_validate_interconnect_ok_state(self, *enc_obj):
        """ Validate critical interconnect has valid ok message
        Example:
        | Fusion UI Validate Interconnect OK State | @{enclosure list} |
        """
        return enclosures.validate_interconnect_ok_state(enc_obj)

    def fusion_ui_validate_logical_interconnect_state(self, *enc_obj):
        """  Validate critical logical interconnect has valid error message
        Example:
        | Fusion UI Validate Logical Interconnect State | @{enclosure list} |
        """
        return enclosures.validate_logical_interconnect_state(enc_obj)

    def fusion_ui_validate_blade_utilization(self, *enc_obj):
        """  Validate blade utilization
        Example:
        | Fusion UI Validate Blade Utilization | @{enclosure list} |
        """
        return enclosures.validate_blade_utilization(enc_obj)

    def fusion_ui_validate_blade_unsupported(self, *enc_obj):
        """  Validate blade unsupported
        Example:
        | Fusion UI Validate Blade Unsupported | @{enclosure list} |
        """
        return enclosures.validate_blade_unsupported(enc_obj)

    def fusion_ui_validate_eg_lig_exist(self, *enc_obj):
        """  Verify if interconnect group and enclosure group exist after enclosure was removed
        Example:
        | Fusion UI Validate EG LIG Exist | @{enclosure list} |
        """
        return enclosures.validate_interconnect_group_and_enclosure_group_exist(enc_obj)

    def fusion_ui_validate_eg_lig_not_exist(self, *enc_obj):
        """  Verify if interconnect group and enclosure group not exist after enclosure was removed
        Example:
        | Fusion UI Validate EG LIG Not Exist | @{enclosure list} |
        """
        return enclosures.validate_interconnect_group_and_enclosure_group_not_exist(enc_obj)

    def fusion_ui_validate_licensing_policy(self, *enc_obj):
        """  Verify if licensing policy as expected
        Example:
        | Fusion UI Validate Licensing Policy | @{enclosure list} |
        """
        return enclosures.validate_licensing_policy(enc_obj)

    def fusion_ui_validate_server_hardware_monitored(self, *server_obj):
        """ validate error message when trying to add server which is already monitored by own appliance
        Example:
        | Fusion UI Validate Server Hardware Monitored |
        """
        return serverhardware.validate_server_hardware_monitored(server_obj)

    def fusion_ui_validate_server_hardware_managed(self, *server_obj):
        """ validate server hardware which is managed by own applicance
        Example:
        | Fusion UI Validate Server Hardware Managed | ${Server hw list} |
        """
        return serverhardware.validate_server_hardware_managed(server_obj)

    def fusion_ui_validate_server_hardware_type_not_exist(self, *enclosure_obj):
        """ validate not exist on the "Server Hardware Types" page
        Example:
        | Fusion UI Validate Server Hardware Type Not Exist |
        """
        return serverhardwaretypes.validate_server_hardware_type_not_exist(enclosure_obj)

    def fusion_ui_validate_panel_selector_in_create_enclosure_group_dialog(self):
        """validate panel selector in Create enclosure group dialog
        Example:
        | Fusion UI Validate Panel Selector in Create Enclosure Group Dialog |
        """
        return enclosuregroups.validate_panel_selector_in_create_enclosure_group_dialog()

    ##########################################################################
    # Reports page functions
    ##########################################################################
    def fusion_ui_navigate_to_reports_page(self):
        """ Navigate to the Reports Page
        Example:
        | Fusion UI Navigate To Reports Page |
        """
        reports.navigate()

    def fusion_ui_export_and_verify_inventory_reports(self, inventory_path, inventory_name):
        """ Export and Verify inventory reports
            Exports the inventory and verifies the file at destination
        Example:
        | Fusion UI Export And Verify Inventory Reports    | ${inventory_path} |    ${inventory_name}    |
        """
        return reports.export_and_verify_inventory_reports(inventory_path, inventory_name)

    def fusion_ui_verify_reports_page_alerts_data_against_activity_page(self):
        """ Verify alerts data against activity page
            Verifies the alerts data present in reports and activity page are same or not
            Example:
            |Fusion UI Verify Reports Page Alerts Data Against Activity Page|
        """
        return reports.verify_reports_page_alerts_data_against_activity_page()

    ##########################################################################
    # vCenter functions
    # #########################################################################
    def fusion_ui_add_vcenter(self, *vcenter_obj):
        """ Add new vcenter(s)
        Example:
        | Fusion UI Add vcenter | @{vcenter list} |
        """
        return vcenter.add_vcenter(vcenter_obj)

    def fusion_ui_edit_vcenter_server_properties(self, *vcenter_obj):
        """Edit vcenter(s)
        Example:
         | Fusion UI Edit vCenter server properties | @{vcenter list} |
         """
        return vcenter.edit_vcenter_server_properties(vcenter_obj)

    def fusion_ui_delete_vCenter(self, vcenter_name):
        """ Delete vcenter
        Example:
        | Fusion UI Delete VCenter    |    ${vcenter_name} |
        """
        return vcenter.delete_vCenter(vcenter_name)

    def fusion_ui_delete_all_vcenters(self):
        """ Delete all vcenter(s)
        Example:
        | Fusion UI delete All vCenters |
        """
        return vcenter.delete_all_vcenters()

    ###########################################################################
    # Logical Switches Keywords
    ###########################################################################
    def fusion_ui_create_logical_switches(self, *ls_obj):
        """ Create Logical Switches
        Example:
        | Fusion UI Create Logical Switches | ${ls list} |
        """
        return logicalswitches.create_logical_switches(ls_obj)

    def fusion_ui_edit_logical_switches(self, *ls_obj):
        """ Edit Logical Switches
        Example:
        | Fusion UI Edit Logical Switches | ${ls list} |
        """
        return logicalswitches.edit_logical_switches(ls_obj)

    def fusion_ui_delete_logical_switch_by_name(self, ls_name):
        """ Delete Logical Switch By Name
        Example:
        | Fusion UI Delete Logical Switch By Name | ${ls name} |
        """
        return logicalswitches.delete_logical_switch_by_name(ls_name)

    def fusion_ui_delete_logical_switches(self, *ls_obj):
        """ Delete Logical Switches
        Example:
        | Fusion UI Delete Logical Switches | ${ls list} |
        """
        return logicalswitches.delete_logical_switches(ls_obj)

    def fusion_ui_create_ls(self, *lsg_obj):
        """
        !!! Deprecated !!!
            please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
              "Fusion UI Create Logical Switches"
              which is create_logical_switches() in this FusionLibrary/ui/networking/logicalswitches.py.

            [LEGACY]
            Create LS for fusion appliance
            Example:
            | Fusion UI create LS | @{ls} |
        """

        return logicalswitches.create_ls(lsg_obj)

    def fusion_ui_edit_ls(self, *ls_obj):
        """
        !!! Deprecated !!!
            please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
              "Fusion UI Edit Logical Switches"
        """
        """ [LEGACY]
            Edit LS for fussion appliance
            Example:
            | Fusion UI edit LS | @{ls} |
        """
        return logicalswitches.edit_ls(ls_obj)

    def fusion_ui_ls_update_from_group(self, *ls_obj):
        """ [LEGACY]
            UPdate LS for fusion appliance
            Example:
            | Fusion UI LS update from group | @{ls} |
        """
        return logicalswitches.ls_update_from_group(ls_obj)

    def fusion_ui_delete_ls(self, *ls_obj):
        """
        !!! Deprecated !!!
            please DO NOT change/maintain this keyword anymore, instead using/improving the keyword
              "Fusion UI Delete Logical Switches"
        """
        """ [LEGACY]
            Delet ls from appliance
            Example:
            | Fusion UI delete LS | @{ls}
        """
        return logicalswitches.delete_ls(ls_obj)

    def fusion_ui_show_ls(self, *ls_obj):
        """ [LEGACY]
            Show LS for appliance
            Example:
            | Fusion show ls | @{ls} |
        """
        # status, return_data = logicalswitches.show_ls(ls_obj)
        status, return_data = logicalswitches.get_ls_attributes(ls_obj)
        return status, return_data

    def fusion_ui_get_ils_data(self, *ls_obj):
        """
            Get Internal Link Set data
            Example:
            | Fusion UI Get Ils Data    | ls_name |
        """
        return logicalswitches.get_ils_data(ls_obj)

    def fusion_ui_get_ls_alert_msg(self, ls_name):
        """
            Get Internal Link Set data
            Example:
            | Fusion UI Get Ls Alert Msg    | ls_name |
        """
        return logicalswitches.get_ls_alert_msg(ls_name)

    def fusion_ui_check_privi_ls(self, *ls_obj):
        """ [LEGACY]
            Check privilages of login user
            Example:
            | Fusion check privi ls | @{ls} |
        """
        return logicalswitches.check_privi_ls(ls_obj)

    def fusion_switch_ssh(self, *user_obj):
        """ [LEGACY]
            Establish SSH connection and execute command on remote switch.
            Pass switch credentials and command to be executd on switch
            as argument
            Example :
            | Fusion switch ssh | @{switch_credential} |
        """
        logicalswitches.switch_ssh(user_obj)
        return True

    def fusion_ui_validation_interconnect_firmware_from_li(self, li_list, *firmware_obj):
        """
           Validation of the Logical interconnect Activity  of LI
           Example :
           | fusion_ui_validation_interconnect_firmware_from_li | @{firmware_obj} |
        """

        return logicalinterconnects.verify_interconnect_firmware_from_li(li_list, firmware_obj)

    def fusion_ui_validation_c7k_updatefirmwarealerts_in_li(self, *firmware_obj):
        """
        Validation of the Logical  interconnect Activity of li
        Example :
        | fusion_ui_validation_c7k_updatefirmwarealerts_in_li | @{firmware_obj} |
        """

        return logicalinterconnects.validation_c7k_updatefirmwarealerts_li(firmware_obj)

    def fusion_ui_validation_c7k_firmware_update_alerts_enclosure(self, encname):
        """
        Validation of the enclosure Activity for firmware upgarde operation
        Example :
        | fusion_ui_validation_c7k_firmware_update_alerts_enclosure | @{firmware_obj} |
        """
        return enclosures._get_enc_activity_details(encname)

    def fusion_ui_validate_error_on_create_server_profile(self, *profile_obj):
        """ Validate errors on create server profile
        Example:
        | Fusion UI Validate Error On Create Server Profile | @{Profiles} |
        """
        return serverprofiles.validate_error_on_create_server_profile(profile_obj)

    def fusion_ui_validate_privileges_edit_network(self, *net_obj):
        """ Validates privileges for different users to edit network
        Example:
        | Fusion UI Validate Privileges Edit Network | ${network list} |
        """
        return networks.validate_privileges_edit_network(net_obj)

    def fusion_ui_validate_create_network_button_exists(self):
        """ Validate Create Network Button Exists
        Example:
        | Fusion UI Validate Create Network Button Exists |
        """
        return networks.create_network_button_visibility_check()

    ##########################################################################
    # Tbird  Interconnect Link topology functions
    ##########################################################################

    def fusion_ui_tbird_validate_interconnectbayset_viewside_in_interconnectlinktopology(self, *enc_obj):
        """ Checks the blades & CIM slots in Enclosures overview
        Example:
        | `Fusion UI Verify Tbird Verify Port Extender Topology | @{enclosure list} |

        """
        return enclosures.tbird_validate_interconnectbayset_and_viewside_in_interconnectlinktopology(enc_obj)

    def fusion_ui_tbird_validate_interconnect_link_topology_numbering(self, *enc_obj):
        """ Checks the blades & CIM slots in Enclosures overview
        Example:
        | `Fusion UI Verify Tbird Validate Interconnect Link Topology Numbering| @{enclosure list} |

        """
        return enclosures.tbird_validate_interconnect_link_topology_numbering(enc_obj)

    ##########################################################################
    # Scope functions
    ##########################################################################

    def fusion_ui_create_scope(self, *scope_obj):
        """ Create Scope
        Example:
        | `Fusion UI Create Scope | @{scope list} |

        """
        return scopes.create_scope(scope_obj)

    def Fusion_ui_verify_error_msg_for_duplicate_scope(self, *scope_obj):
        """ Create Verify Scope
        Example:
        | Fusion UI Verify Error Msg For Duplicate Scope | @{scope_obj} |
        """
        return scopes.verify_error_msg_for_duplicate_scope(scope_obj)

    def fusion_ui_get_scope_description(self):
        """ Get Scope Description
        Example:
        | Fusion UI Get Scope Description |
        """
        return scopes.get_scope_description()

    def fusion_ui_validate_scope_page_buttons(self):
        """ Scope
        Example:
        | `Fusion UI Validate Scope Page Buttons | @{scope list} |
        """
        return scopes.validate_scopes_page_buttons()

    def fusion_ui_get_scope_count(self):
        """ Get Scope Count
        Example:
        | Fusion UI Get Scope Count |
        """
        return scopes.get_scope_count()

    def fusion_ui_delete_scope(self, *scope_obj):
        """ Delete Scope
        Example:
        | `Fusion UI Delete Scope | @{scope list} |

        """
        return scopes.delete_scope(scope_obj)

    def fusion_ui_edit_scope(self, *scope_obj):
        """ Edit Scope
        Example:
        | `Fusion UI Edit Scope | @{scope list} |

        """
        return scopes.edit_scope(scope_obj)

    def fusion_ui_select_scope(self, *scope_obj):
        """ Select Scope
        Example:
        | `Fusion UI Select Scope | @{scope list} |

        """
        return scopes.select_scope(scope_obj)

    def fusion_ui_validate_resource_can_be_added_to_scope(self, *scope_obj):
        """ Validate Resource Can Be Added To Scope
        Example:
        | `Fusion UI Validate Resource Can Be Added To Scope | @{scope list} |

        """
        return scopes.validate_resource_can_be_added_to_scope(scope_obj)

    def fusion_ui_validate_scope_can_be_assigned_to_enclosure(self, *enc_obj):
        """ Validate Scope Can Be Assigned To Enclosure
        Example:
        | `Fusion UI Validate Scope Can Be Assigned To Enclosure | @{Enclosure list} |

        """
        return enclosures.validate_scope_can_be_assigned_for_enclosure(enc_obj)

    def fusion_ui_validate_scope_can_be_assigned_to_server_hardware(self, *server_obj):
        """ Validate Scope Can Be Assigned To Server Hardware
        Example:
        | `Fusion UI Validate Scope Can Be Assigned To Server Hardware | @{Server list} |

        """
        return serverhardware.validate_scope_can_be_assigned_for_server_hardware(server_obj)

    def fusion_ui_validate_scope_assigned_to_enclosure(self, *enc_obj):
        """ Validate Scope Assigned To Enclosure
        Example:
        | `Fusion UI Validate Scope Assigned To Enclosure | @{Enclosure list} |

        """
        return enclosures.validate_scope_assign_for_enclosure(enc_obj)

    def fusion_ui_validate_scope_assigned_to_server_hardware(self, *server_obj):
        """ Validate Scope Assigned To Server Hardware
        Example:
        | `Fusion UI Validate Scope Assigned To Server Hardware | @{Server list} |

        """
        return serverhardware.validate_scope_assign_for_server_hardware(server_obj)

    def fusion_ui_edit_scope_for_enclosure(self, *enc_obj):
        """ Validate Edit Scope For Enclosure
        Example:
        | `Fusion UI Edit Scope For Enclosure | @{Enclosure list} |

        """
        return enclosures.edit_scope_for_enclosure(enc_obj)

    def fusion_ui_delete_enclosure(self, *enclosure_obj):
        """ delete enclosure
        This function is to delete enclosure
        Example:
             | Fusion UI Delete Enclosure |    ${enclosure_obj}    |
        """
        return enclosures.delete_enclosure(enclosure_obj)

    def fusion_ui_edit_scope_for_server_hardware(self, *server_obj):
        """ Edit Scope For Server Hardware
        Example:
        | `Fusion UI Edit Scope For Server Hardware | @{Server list} |

        """
        return serverhardware.edit_scope_for_server_hardware(server_obj)

    def fusion_ui_validate_resource_assigned_to_scope(self, *scopes_obj):
        """ validate resource
            Example:
            | `Fusion UI Validate Resource Assigned To Scope`      | ${myScopeList}    |
        """
        return scopes.validate_resource_assigned_to_scope(scopes_obj)

    def fusion_ui_delete_all_scopes(self):
        """ Remove All Scopes
           Example:
                | `Fusion UI Delete All Scopes` |
        """
        return scopes.delete_all_scopes()

    def fusion_ui_edit_scope_for_logical_interconnect_groups(self, *enc_obj):
        """ Validate Edit Scope For Logical Interconnect Groups
        Example:
        | `Fusion Ui Edit Scope For Logical Interconnect Groups | @{LIG list} |

        """
        return logicalinterconnectgroups.edit_scope_for_logical_interconnect_groups(enc_obj)

    def fusion_ui_edit_scope_for_logical_interconnect(self, *li_obj):
        """ Edit Scope For Logical Interconnect
        Example:
        | `Fusion UI Edit Scope For Logical Interconnect | @{LI list} |

        """
        return logicalinterconnects.edit_scope_for_logical_interconnect(li_obj)

    def fusion_ui_edit_scope_for_interconnects(self, *ic_obj):
        """ Edit Scope For Interconnects
        Example:
        | `Fusion UI Edit Scope For Interconnects | @{interconnect list} |

        """
        return interconnects.edit_scope_for_interconnects(ic_obj)

    def fusion_ui_edit_scope_for_networksets(self, *networkset_obj):
        """ Edit Scope For Network sets
        Example:
        | `Fusion UI Edit Scope For Network sets | @{network_set list} |

        """
        return networksets.edit_scope_for_networksets(networkset_obj)

    def fusion_ui_edit_scope_for_networks(self, *network_obj):
        """ Edit Scope For Networks
        Example:
        | `Fusion UI Edit Scope For Networks | @{network list} |

        """
        return networks.edit_scope_for_networks(network_obj)

    def fusion_ui_validate_ligscopes_each_element(self):
        """ Validate Delete Scopes
          Example:
                | `Fusion Ui Validate Ligscopes Each Element` |
       """
        return scopes.validate_ligscopes_each_element()

    def fusion_ui_validate_networkscopes_each_element(self):
        """ Validate Delete Scopes
            Example:
                | `Fusion Ui Validate Networkscopes Each Element` |
        """
        return scopes.validate_networkscopes_each_element()

    def fusion_ui_validate_enclosurescopes_each_element(self):
        """ Validate Delete Scopes
            Example:
                | `Fusion Ui Validate Enclosurescopes Each Element` |
        """
        return scopes.validate_enclosurescopes_each_element()

    def fusion_ui_validate_networksetsscopes_each_element(self):
        """ Validate Delete Scopes
            Example:
                | `Fusion Ui Validate Networksetsscopes Each Element` |
        """
        return scopes.validate_networksetsscopes_each_element()

    def fusion_ui_validate_Interconnectsscopes_each_element(self):
        """ Validate Delete Scopes
            Example:
                | `Fusion Ui Validate Interconnectsscopes Each Element` |
        """
        return scopes.validate_interconnectsscopes_each_element()

    def fusion_ui_validate_LIscopes_each_element(self):
        """ Validate Delete Scopes
            Example:
                | `Fusion Ui Validate LIscopes Each Element` |
        """
        return scopes.validate_liscopes_each_element()

    def fusion_ui_validate_SERVERHWscopes_each_element(self):
        """ Validate Delete Scopes
            Example:
                | `Fusion Ui Validate SERVERHWscopes Each Element` |
        """
        return scopes.validate_serverhwscopes_each_element()

    def fusion_ui_filter_by_scope(self, xpath_id, *scope_obj):
        """ validate resource
            Example:
                | `Fusion UI Filter by Scope`      |    ${xpath_category}   |   ${filter_name}  |    @{Scope_List}  |
        """
        return scopes.filter_by_scope(xpath_id, scope_obj)

    def fusion_ui_filter_by_all_scope(self, xpath_id, *scope_obj):
        """  validate resource
            Example:
            | `Fusion UI Filter by All Scope`      |    ${xpath_category}   |   @{Scope_List}   |
        """
        return scopes.filter_by_all_scope(xpath_id, scope_obj)

    def fusion_ui_filter_by_any_scope(self, xpath_id, *scope_obj):
        """  validate resource
            Example:
            | `Fusion UI Filter by Any Scope`      |    ${xpath_category}   |   @{Scope_List}   |
        """
        return scopes.filter_by_any_scope(xpath_id, scope_obj)

    def fusion_ui_validate_privilege_for_users(self):
        """ validate privilege for users
            Example:
                |   `Fusion UI Validate Privilege For Users`    |
        """
        return scopes.validate_user_privilege()

    def fusion_ui_select_scopes_dropdown(self):
        """ Validate Delete Scopes
            Example:
                | `Fusion Ui Select Scopes Dropdown` |
        """
        return scopes.select_scopes_dropdown()

    ########################################################################
    # Notification Alert Filter Creation
    ########################################################################

    def fusion_ui_create_alert_filter_with_predefined_criteria(self, *alert_obj):
        """ Create Alert Filter with ALert Criteria and Scope
        Example:
        | `Fusion UI Create ALert Filter With Predefined Criteria | @{alert list} |
        """
        return notifications.create_alert_filter_with_predefined_criteria(alert_obj)

    def fusion_ui_validate_choose_alert_criteria(self, *alert_obj):
        """  Choosing different alert criteria
        Example:
        | `Fusion UI Validate Choose Alert Criteria | @{alert list} |
        """
        return notifications.validate_choose_alert_criteria(alert_obj)

    def fusion_ui_navigate_to_scopes_page(self):
        """ Navigate to the Scopes Page
        Example:
        | Fusion UI Navigate To Scopes Page |
        """
        scopes.navigate()

    def fusion_ui_is_on_scopes_page(self):
        """ Verify Scopes Page
        Example:
        | Fusion UI Is On Scopes Page |
        """
        return scopes.verify_is_on_scopes_page()

    def fusion_ui_get_scope_name(self):
        """ Get Scope Name
        Example:
        | Fusion UI Get Scope Name |
        """
        return scopes.get_scope_name()

    def fusion_ui_edit_alert_filter(self, *alert_obj):
        """  Edit alert filter
        Example:
        | `Fusion UI Edit Alert Filter | @{alert list} |
        """
        return notifications.edit_alert_filter(alert_obj)

    def fusion_ui_delete_alert_filter(self, *alert_obj):
        """  Delete alert Filter
        Example:
        | `Fusion UI Delete Alert Filter | @{alert list} |
        """
        return notifications.delete_alert_filter(alert_obj)

    def fusion_ui_create_alert_filter_with_guided_criteria(self, *alert_obj):
        """  Create ALert Filter with Alert Criteria as Guided
        Example:
        | `Fusion UI Create Alert Filter With Guided Criteria | @{alert list} |
        """
        return notifications.create_alert_filter_with_guided_criteria(alert_obj)

    def fusion_ui_create_alert_filter_with_advanced_criteria(self, *alert_obj):
        """  Create ALert Filter with Alert Criteria As Advanced
        Example:
        | `Fusion UI Create Alert Filter With Advanced Criteria | @{alert list} |
        """
        return notifications.create_alert_filter_with_advanced_criteria(alert_obj)

    ##########################################################################
    # FC licenses functions
    ##########################################################################

    def fusion_ui_validate_no_fc_license(self):
        """ Validate no fc license
           Example:
                | `Fusion Ui Validate No Fc License`     |
        """
        return licenses.validate_no_fc_license()

    def fusion_ui_validate_add_button_exists_on_license_page(self):
        """ Validate  Add button exists on license page
           Example:
                | `Fusion Ui Validate Add Button Exists On License Page` |
        """
        return licenses.validate_add_button_exists_on_license_page()

    def fusion_ui_validate_no_license_on_server_hardware(self, *server_hardware_list):
        """ Validate there is no licenses on server hardware
           Example:
                | `Fusion Ui Validate No License On Server Hardware` | @{server hardware list}    |
        """
        return serverhardware.validate_no_license_on_server_hardware(server_hardware_list)

    def fusion_ui_verify_add_server_hardware_button_not_exists(self):
        """ It checks for absence of Add server hardware button in "ServerHardware" page
        Example:
        | Fusion UI Verify Add Server Hardware Button Not Exists |
        """
        return serverhardware.verify_add_server_hardware_button_notvisible()

    def fusion_ui_validate_privileges_edit_serverhardware(self, *serverhardware_obj):
        """ Validates privileges for different users to edit Serverhardware
        Example:
        | Fusion UI Validate Privileges Edit Serverhardware | ${ServerHardware list} |
        """
        return serverhardware.validate_privileges_edit_serverhardware(serverhardware_obj)

    def fusion_ui_add_fc_licenses(self, *licenses_obj):
        """ Add fcupgrade license
           Example:
                | `Fusion Ui Add Fc Licenses`  | @{license obj}    |
        """
        return licenses.add_fc_licenses(licenses_obj)

    def fusion_ui_validate_error_when_adding_invalid_or_duplicated_fc_licenses(self, *licenses_obj):
        """ Add invalid or duplicated fcupgrade license
           Example:
                | `Fusion Ui Validate Error When Adding Invalid Or Duplicated Fc License`  | @{license obj}    |
        """
        return licenses.validate_error_when_adding_invalid_or_duplicated_fc_licenses(licenses_obj)

    def fusion_ui_validate_add_license_button_exists(self):
        """Add licenses button visibility check
        Example:
        | Fusion UI Validate Add License Button Exists |
        """
        return licenses.validate_add_license_button_exists()

    def fusion_ui_edit_potassium_interconnect_bay_licensing(self, *le_obj):
        """ Edit potassium interconnect bay licensing status from logical enclosure
           Example:
                | `Fusion Ui Edit Potassium Interconnect Bay Licensing`  | @{license obj}    |
        """
        return logicalenclosures.edit_potassium_interconnect_bay_licensing(le_obj)

    def fusion_ui_validate_potassium_interconnect_bay_licensing(self, *le_obj):
        """ Validate potassium interconnect bay licensing status from logical enclosure
           Example:
                | `Fusion Ui Validate Potassium Interconnect Bay Licensing`  | @{license obj}    |
        """
        return logicalenclosures.validate_potassium_interconnect_bay_licensing(le_obj)

    def fusion_ui_validate_error_message_li(self, *firmware_obj):
        """
        Validation of the Logical interconnect Activity  of LI
        Example:
        | fusion_ui_validate_error_message_li | @{firmware_obj} |
        """
        return logicalinterconnects.validate_error_message_li(firmware_obj)

    def fusion_ui_get_alert_message_li(self, liname):
        """
        Validation of the Logical interconnect Activity  of LI
        Example:
        | Fusion UI Get Alert Message Li | ${Li_name} |
        """
        return logicalinterconnects.get_alert_message_li(liname)

    def fusion_ui_create_scope_boundary_check(self, correct_name, *scope_obj):
        """ Create scope exceeding boundary value for name and description
        Example:
        | Fusion UI Create Scope Boundary Check| ${correct_name} | @{scope_obj} |
        """
        return scopes.create_scope_boundary_check(correct_name, *scope_obj)

    def fusion_ui_appliance_state_for_scope(self):
        """ Assign bulk enets
            Example:
        | Fusion UI Appliance State For Scope |
        """
        return scopes.get_appliance_state_for_scope()

    def fusion_ui_assign_bulk_enets(self, *scope_obj):
        """ Assign bulk enets
                Example:
                | Fusion UI Assign Bulk Enets | @{scope list} |
        """
        return scopes.assign_scope_bulk_networks(*scope_obj)

    def fusion_ui_get_scopes_list(self):
        """ Getting scopes list
                Example:
                | Fusion UI Get Scopes List |
        """
        return scopes.get_scopes_list()

    def fusion_ui_validate_bulk_resource(self, *scope_obj):
        """ Validating bulk resource
            Example:
            | Fusion UI Validate Bulk Resource |
        """

        return scopes.validate_bulk_resource_list(scope_obj)

    def fusion_ui_click_settings_link_from_scopepage(self):
        """ Click Settings Link on Scopes Page
        Example:
        | Fusion UI Click Settings Link From Scopepage |
        """
        scopes.click_settings_link()

    def fusion_ui_edit_verify_scope(self, *scope_obj):
        """ Edit Verify Scope
        Example:
        | Fusion UI Edit Verify Scope | @{scope_obj} |
        """
        return scopes.edit_verify_scope(scope_obj)

    ##########################################################################
    # Switches functions
    ##########################################################################

    def fusion_ui_navigate_to_switch_page(self):
        """ Navigate to the "Switch" page
        Example:
        | Fusion UI Navigate To Switch Page |
        """
        switches.navigate()

    def fusion_ui_get_switch_state(self, switchname):
        """ Navigate to the "Switch" page
        Example:
        | Fusion UI Get Switch State |  ${switch}   |
        """
        return switches.get_switch_state(switchname)

    def fusion_ui_get_switch_port_data(self, switchname):
        """ Navigate to the "Switches" page
        Example:
        | Fusion UI Get Switch Port Data |  @{switch_obj}   |
        """
        return switches.get_switch_port_data(switchname)

    def fusion_ui_switch_edit(self, switchname):
        """ Verify edit option is available for switch
        Example:
        | Fusion UI Switch Edit |   ${switch}
        """
        return switches.verify_switch_edit(switchname)

    def fusion_ui_enable_switch_port(self, *switch_obj):
        """ Verify edit option is available for switch
        Example:
        | Fusion UI Enable Switch Port |   ${switch}
        """
        return switches.enable_switch_port(switch_obj)

    def fusion_ui_verify_switch_deleted(self, *switch_obj):
        """ Verify swutches are not exist in switches page
        Args:
            | Fusion UI Verify Switch Deleted | *switch_obj: |
        """
        return switches.verify_switch_deleted(switch_obj)

    def fusion_ui_delete_all_appliance_logical_enclosures(self):
        """ Fusion UI Delete All Appliance Logical Enclosures
        Example:
        | fusion_ui_delete_all_appliance_logical_enclosures |
        """
        return logicalenclosures.delete_all_appliance_logical_enclosures()

    def fusion_ui_update_appliance(self, *app_obj):
        """ update appliance
        Example:
        | Fusion UI Update Appliance  | ${path}
        """
        return settings.update_appliance(app_obj)

    def fusion_ui_validate_appliance_version(self, version):
        """ validate appliance version
        Example:
        | Fusion UI Validate Appliance Version | ${version}
        """
        return settings.validate_appliance_version(version)

    def fusion_ui_download_fixme_installation_details(self, folder):
        """Download the Fixme Installation Details to the folder specified
        Example:
        | Fusion UI Download Fixme Installation Details | c:/FixmeLogs |
        """
        return settings.download_fixme_installation_details(folder)

    def fusion_ui_get_appliance_version(self):
        """ get appliance version
        Example:
        | Fusion UI Get Appliance Version
        """
        return settings.get_version()

    ##########################################################################
    # Guided Setup functions
    ##########################################################################
    def fusion_ui_open_guided_setup(self):
        """ Open the guided setup panel
        Example:
        | Fusion UI Open Guided Setup |
        """
        base_page.open_guided_setup_panel()

    def fusion_ui_close_guided_setup(self):
        """ Close the guided setup panel
        Example:
        | Fusion UI Close Guided Setup |
        """
        base_page.close_guided_setup_panel()

    def fusion_ui_guided_setup_should_be_opened(self):
        """ Ensure the guided setup is opened
        Example:
        | Fusion UI Guided Setup Should Be Opened |
        """
        ui_lib.get_s2l().element_should_be_visible(FusionUIBaseElements.ID_GUIDED_SETUP_PANEL)

    def fusion_ui_guided_setup_should_be_closed(self):
        """ Ensure the guided setup is closed
        Example:
        | Fusion UI Guided Setup Should Not Be Opened |
        """
        ui_lib.get_s2l().element_should_not_be_visible(FusionUIBaseElements.ID_GUIDED_SETUP_PANEL)
