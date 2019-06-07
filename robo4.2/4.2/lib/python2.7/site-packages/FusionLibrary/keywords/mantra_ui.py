"""
RoboGalaxyLibrary Mantra keywords
"""
from FusionLibrary.ui.mantra.compliance import mantra_compliance_page
from FusionLibrary.ui.mantra.dashboard import dashboard
from FusionLibrary.ui.mantra.enclosures import enclosures
from FusionLibrary.ui.mantra.sample import sample
from FusionLibrary.ui.mantra.systemprofiles import systemprofiles
from FusionLibrary.ui.mantra.systemtypes import systemtypes
from FusionLibrary.ui.mantra.utils import mantraUtils
from FusionLibrary.ui.servers import serverhardware


class MantraUIKeywords(object):
    """ Mantra keywords """

    def go_to_server_profiles_page(self):
        """ Navigate to the Server Profiles Page
        Example:
        | Go to Server Profiles Page |
        """
        sample.navigateServerProfiles()

    def verify_string_label(self):
        """ Verify an string label
        Example:
        | Verify the String Label |
        """
        sample.VerStrLabel()

    def go_to_users_and_groups(self):
        """ Navigate to the Users and Groups Page
        Example:
        | Go to Users and Groups |
        """
        sample.navigateUsersAndGroups()

    def click_on_add_user(self):
        """ Click on Add User button
        Example:
        | Click on Add User |
        """
        sample.adduser()

    def fill_user_info(self, *user_obj):
        """ Fill the user info
        Example:
        | Administrator, password |
        """
        sample.fillinfo(*user_obj)

    def fill_user_info_negative(self):
        """ Fill the user info with invalid data
        Example:
        | Administrator, password |
        """
        sample.fillinfo_negative()

    ##########################################################################
    # Compliance page functions
    ##########################################################################
    def go_to_compliance_page(self):
        """ Navigate to the Compliance page
        Example:
        | Go to Compliance Page |
        """
        mantra_compliance_page.navigate()

    def set_ok_filter(self):
        """ Set the filter to show only the OK enclosures
        Example:
        | Set OK Filter |
        """
        mantra_compliance_page.set_ok_filter()

    def check_the_ok_enclosures(self):
        """ Check if only the ok enclosures are being displayed
        Example:
        | Check the OK Enclosures |
        """
        mantra_compliance_page.check_ok()

    ##########################################################################
    # Configuration
    ##########################################################################
    # def run_set_dcs_script(self):
        # """ Run the PS DCS configuration script
        # Example:
        # """
        # mantra_setdcs.configHardware()

    # def edit_csv_file(self, address):
        # """ Edit the IPConfig.csv file with the appliance address
        # Example:
        # | Edit CSV File |
        # """
        # mantra_setdcs.editfile(address)

    # def run_environment_setup_script(self, address):
        # """ Execute the Environment Setup Script
        # Example:
        # | Run Environment Setup Script |
        # """
        # envsetup.runscript(address)

    ##########################################################################
    # Dashboard page functions
    ##########################################################################
    def check_dashboard_page(self):
        """ Check if the Dashboard page elements are being displayed
        Example:
        | Check Dashboard Page |
        """
        dashboard.checkDashboardPage()

    def check_system_profiles_dashboard_status(self, expectedStatus):
        """ Check if the Dashboard page elements are being displayed
        Example:
        | Check System Profiles Dashboard Status    warning |
        """
        dashboard.checkSystemProfilesDashboardStatus(expectedStatus)

    def go_to_dashboard(self):
        """ Navigate to the dashboard
        Example:
        | Go To Dashboard |
        """
        dashboard.navigate()

    ##########################################################################
    # System Profile page functions
    ##########################################################################

    def create_empty_object(self):
        """ Return an empty object
        Example:
        | Create Empty object |
        """
        return None

    def add_rack_configuration(self, rack_name, converged_system, full_configuration):
        """ Add Rack to System Profile
        Example:
        | Add Rack to System Profile |
        """
        return systemprofiles.add_rack_configuration(rack_name, converged_system, full_configuration)

    def subtrack_rack_configuration(self, rack_name, converged_system):
        """ Subtrack Rack Configuration
        Example:
        | Subtrack Rack Configuration |
        """
        return systemprofiles.subtrack_rack_configuration(rack_name, converged_system)

    def verify_system_profile_contents(self, converged_system):
        """ Verify if the Contents UI reflects the the content from the Test Data XML
        Example:
        | Verify System Profiles Contents ${Contents}
        """
        return systemprofiles.verify_if_ui_contents_matches_configuration(converged_system)

    def read_converged_system_from_xml(self, XMLObject):
        """ Read a Data File to be used in another methods as a variable
         Example:
         | ${Contents} = Read Converged System from XML @{TestData.ConvergedSystemCS700V2}
        """
        return systemprofiles.read_converged_system_from_xml(XMLObject)

    def verify_if_system_profile_content_section_is_empty(self):
        """ Verify if System Profile Content Section is Empty
        Example:
        | Verify if System Profile Content Section is Empty |
        """
        systemprofiles.is_contents_section_empty()

    def go_to_system_profile_page(self):
        """ Navigate to System Profile page
        Example:
        | Go to System Profiles Page |
        """
        systemprofiles.navigate()

    def system_profiles_refresh_data(self):
        """ Refresh the server profile data
        Example:
        | System Profiles Refresh Data |
        """
        systemprofiles.refresh()

    def wait_for_system_profile_task(self, task_name):
        """ Wait for a specific system profile task.
        Example:
        | Wait for System Profile Task ${MyTaskName} |
        """
        systemprofiles.checkActivity(task_name)

    def access_and_check_the_system_profiles_map_page(self):
        """ Click on MAP button and check the contents
        Example:
        | Access and Check the System Profiles Map Page |
        """
        systemprofiles.navigateMap()

    def access_and_check_the_general_page(self):
        """ Click on General view button and check the contents
        Example:
        | Access and Check the General Page |
        """
        systemprofiles.navigateGeneral()

    def check_map_contents(self):
        """ Check all the elements in the System Profile MAP view tree
        Example:
        | Check Map Contents |
        """
        systemprofiles.checkMapContents()

    def check_general_contents(self):
        """ Check all the elements in the Overview/General side
        Example:
        | Check General Contents |
        """
        systemprofiles.checkGeneralContents()

    def check_contents(self):
        """ Check all the elements in the Overview/Contents side
        Example:
        | Check Contents |
        """
        systemprofiles.checkContents()

    def check_contents_is_green(self):
        """ Check each element in the Overview/Contents side is green (OK)
        Example:
        | Check Contents is Green |
        """
        systemprofiles.checkContentsIsGreen()

    def access_and_check_the_activity_page(self):
        """ Access the Activity page and check if the table is displayed
        Example:
        | Access and Check the Activity Page |
        """
        systemprofiles.navigateActivity()

    def check_system_profile_status(self, system_profile_name, expected_status):
        """ Verify if the status of a given system profile matches with the expected status.
        Example:
        | Check System Profile Status    MyCS700    OK |
        """
        systemprofiles.checkSystemProfileStatus(system_profile_name, expected_status)

    def get_system_profile_status(self, system_profile_name):
        """ Returns the status for the specified system proflile
        Example:
        | Get System Profile Status    MyCS700 |
        """
        return systemprofiles.get_system_profile_status(system_profile_name)

    def remove_rack_from_system_profile(self, rack_name):
        """ Edit a system profile, removing the specified rack from a System Profile.
        Example:
        | Remove Rack from System Profile    Rack-name |
        """
        systemprofiles.remove_rack(rack_name)

    def rename_system_profile(self, new_system_profile_name):
        """ Rename a system profile
        Example:
        | Rename System Profile    New System Profile Name |
        """
        systemprofiles.rename_system_profile(new_system_profile_name)

    def validate_system_profile_name(self, system_profile_name):
        """ Validate the System Profile Name
        Example:
        | Validate System Profile Name    System Profile Name |
        """
        systemprofiles.validate_system_profile_name(system_profile_name)

    def add_rack_to_system_profile(self, rack_name):
        """ Edit a system profile, removing the specified rack from a System Profile.
        Example:
        | Add Rack to System Profile    Rack-name |
        """
        systemprofiles.add_rack(rack_name)

    def validate_element_in_system_profile_contents(self, contents_category, contents_element):
        """ Verify if a resource is displayed on System Profile Contents section.
            This function can also be used to verify the number of a specific resource.
        Examples:
        | Validate Element in System Profile Contents    "Clusters"   "4 Server Profiles" |
        | Validate Element in System Profile Contents    "Clusters"   "4" |
        | Validate Element in System Profile Contents    "Clusters"   "Server Profiles" |
        """
        systemprofiles.check_content_resource(contents_category, contents_element)

    ##########################################################################
    # System Types page functions
    ##########################################################################
    def go_to_system_types_page(self):
        """ Navigate to System Types page
        Example:
        | Go to System Types Page |
        """
        systemtypes.navigate()

    def check_system_types_overview_elements(self):
        """ Check all the elements in the Overview page
        Example:
        | Check System Types Overview Elements |
        """
        systemtypes.checkOverviewPage()

    # ===========================================================================
    # method not yet implemented
    # def check_update(self):
    #     """ Click on Update button and submit a file
    #     Example:
    #     | Check Update |
    #     """
    #     systemtypes.update()
    # ===========================================================================

    def access_and_check_the_system_types_map_page(self):
        """ Click on MAP button and check the contents
        Example:
        | Access and Check the System Types Map Page |
        """
        systemtypes.navigateMap()

    ##########################################################################
    # Mantra Utils
    ##########################################################################
    def add_dcs_blade_for_cs700_hardware_expansion(self, address, encSettings):
        """ Add a blade on appliance
        Example:
        | Add DCS Blade for CS700 Hardware Expansion |
        """
        mantraUtils.add_DCS_Blade(address, encSettings)

    def dcs_change_fan_status(self, appliance_address, bay_number, enclosure_id, new_status):
        """ Change the status of an enclosure's fan (in DCS).
            Example:
        | DCS Change Fan Status  https://16.125.106.106  3  Enclosure-299  OP_STATUS_OK |
        """
        mantraUtils.DCS_change_fan_status(appliance_address, bay_number, enclosure_id, new_status)

    ##########################################################################
    # Enclosures page functions
    ##########################################################################
    def check_the_new_blade_at_front_view(self, encSettings):
        """ Check if the blade is being displayed at Front View
        Example:
        | Check the new blade at front view |
        """
        enclosures.wait_for_blade_to_be_added(encSettings)

    ##########################################################################
    # Server Hardware page functions
    ##########################################################################
    def wait_for_add_blade_task(self, encSettings):
        """ Check the status of the task related to the Add Blade
        Example:
        | Wait for Add Blade Task |
        """
        serverhardware.checkAddBladeTask(encSettings)
