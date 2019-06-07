import re
from robot.libraries.BuiltIn import BuiltIn
import types
from functools import wraps
from RoboGalaxyLibrary.ui.common import ui_lib
from datetime import datetime
import time
from types import FunctionType
import sys
import traceback
from RoboGalaxyLibrary.data import test_data
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from RoboGalaxyLibrary.ui.common.ui_lib import fail_test, get_s2l
from RoboGalaxyLibrary.utilitylib import logging as logger
from selenium.webdriver.remote.webelement import WebElement
from Selenium2Library.locators.elementfinder import ElementFinder
from selenium.webdriver.support.ui import Select
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.testdata_validate import FusionUITestDataValidate
from RoboGalaxyLibrary.common.exceptions import ElementNotFoundException
from FusionLibrary.api.common.request import HttpVerbs
from FusionLibrary.api.servers.enclosure_groups import EnclosureGroup
from FusionLibrary.api.servers.server_hardware import ServerHardware
from FusionLibrary.api.servers.server_hardware_types import ServerHardwareTypes
from FusionLibrary.api.networking.logical_interconnect_groups import LogicalInterconnectGroup
from FusionLibrary.api.networking.logical_switch_groups import LogicalSwitchGroup
from FusionLibrary.api.networking.interconnect_types import InterconnectTypes
from FusionLibrary.api.settings.appliance_node_information import ApplianceNodeInformation
import inspect
# pylint: skip-file


class FusionUIConst(object):
    CONST_LICENSE_ONEVIEW_ADVANCED = "HPE OneView Advanced"
    CONST_LICENSE_ONEVIEW_ADVANCED_WITHOUT_ILO = "HPE OneView Advanced w/o iLO"
    CONST_LICENSE_ONEVIEW_SYNERGY_FCUPGRADE = "Synergy 8Gb FC Upgrade"

    CONST_POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
    CONST_CARBON = 'Virtual Connect SE 16Gb FC Module for Synergy'
    CONST_HAFNIUM_POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23'
    CONST_HAFNIUM_POTASSIUM = 'Synergy 40Gb F8 Switch Module'
    CONST_ZERO_WIDTH_SPACE = u'\u200B'
    CONST_FW_UPDATE_TIMEOUT = 90  # in minutes
    CONST_FW_UPDATE_LOGGING_TIME = 15   # in seconds
    CONST_STORAGE_SYSTEM_TYPE_STORESERV = FusionUITestDataValidate.ReferenceData['SAN_Storage_System_Type'][0]
    CONST_STORAGE_SYSTEM_TYPE_STOREVIRTUAL = FusionUITestDataValidate.ReferenceData['SAN_Storage_System_Type'][1]
    CONST_STORAGE_SYSTEM_TYPE_NIMBLE = FusionUITestDataValidate.ReferenceData['SAN_Storage_System_Type'][2]

    class UserRoles(object):
        ALL_SPECIALIZED_ROLES = 'Backup administrator,Network administrator,Server administrator,Storage administrator,Server firmware operator,Software administrator'
        FULL = 'Full'
        FULL_PRESENT_ON_UI = 'Infrastructure administrator'
        READONLY = 'Read only'
        SERVERADMIN = 'Server administrator'
        NETWORKADMIN = 'Network administrator'
        BACKUPADMIN = 'Backup administrator'
        STORAGEADMIN = 'Storage administrator'
        SOFTWAREADMIN = 'Software administrator'
        SERVERFIRMWAREOPERATOR = 'Server firmware operator'

    class Firmware(object):
        CONST_ACTIVATE_FIRMWARE_IMMEDIATELY = 'Immediately'
        CONST_ACTIVATE_FIRMWARE_SCHEDULED = 'Scheduled'
        CONST_ACTIVATE_FIRMWARE_NOT_SCHEDULED = 'Not scheduled'


class FusionUIBaseElements(object):
    ID_PAGE_LABEL = "xpath=//div[@class='hp-page-label']/h1"
    ID_MASTER_PANE = "xpath=//div[contains(@class, 'hp-master-pane')]"
    ID_ACTIVITY_CONTROL = "hp-activity-control"
    ID_ACTIVITY_NOTIFICATION = "//div[@id='hp-activity-notification']"
    ID_ACTIVE_ACTIVITY_NOTIFICATION = "//div[@id='hp-activity-notification'][contains(@class, 'hp-active')]"
    ID_ACTIVITY_MESSAGE = ID_ACTIVITY_NOTIFICATION + "//div[@class='hp-message']"
    ID_DASHBOARD = "hp-dashboard-primary"
    ID_EMPTYMESSAGE = "div.hp-empty-message"
    ID_GUIDED_SETUP_BUTTON = "cic-setup-checklist-control"
    ID_GUIDED_SETUP_PANEL = "cic-setup-checklist-flyout"
    ID_HELP = "css=div.hp-icon.hp-help"
    ID_HELP_ON_THIS_PAGE = "link=Help on this page"
    ID_HP_LOGO = "hp-logo"
    ID_MAIN_BANNER = "hp-main-banner"
    ID_MAIN_MENU = "hp-main-menu"
    ID_MAIN_MENU_CONTROL = "hp-main-menu-control"
    ID_MENU_ACTIVE = "css=#hp-main-menu.hp-active"
    ID_MENU_GROMMET = "css=#hp-main-menu.hp-grommet-menu"
    ID_SEARCH_CONTROL = "hp-search-control"
    ID_SESSION_CONTROL = "hp-session-control"
    ID_SESSION_LOGOUT = "hp-session-logout"
    ID_MENU_LINK_ACTIVITY = "link=Activity"
    ID_MENU_LINK_DASHBOARD = "link=Dashboard"
    ID_MENU_LINK_FIRMWARE_BUNDLES = "link=Firmware Bundles"
    ID_MENU_LINK_SERVER_PROFILE = "xpath=//*[@id='hp-main-menu']//a[text()='Server Profiles']"
    ID_MENU_LINK_LOGICAL_ENCLOSURES = "link=Logical Enclosures"
    ID_MENU_LINK_ENCLOSURE_GROUPS = "link=Enclosure Groups"
    ID_MENU_LINK_ENCLOSURES = "link=Enclosures"
    ID_MENU_LINK_SERVER_HARDWARE = "xpath=//*[@id='hp-main-menu']//a[text()='Server Hardware']"
    ID_MENU_LINK_SERVER_HARDWARE_TYPES = "link=Server Hardware Types"
    ID_MENU_LINK_LOGICAL_INTERCONNECT_GROUPS = "link=Logical Interconnect Groups"
    ID_MENU_LINK_LOGICAL_INTERCONNECTS = "link=Logical Interconnects"
    ID_MENU_LINK_LOGICAL_SWITCH_GROUPS = "link=Logical Switch Groups"
    ID_MENU_LINK_NETWORKS = "link=Networks"
    ID_MENU_LINK_NETWORK_SETS = "link=Network Sets"
    ID_MENU_LINK_SWITCHES = "link=Switches"
    ID_MENU_LINK_INTERCONNECTS = "link=Interconnects"
    ID_MENU_LINK_DATA_CENTERS = "link=Data Centers"
    ID_MENU_LINK_RACKS = "link=Racks"
    ID_MENU_LINK_POWER_DELIVERY_DEVICES = "link=Power Delivery Devices"
    ID_MENU_LINK_UNMANAGED_DEVICES = "link=Unmanaged Devices"
    ID_MENU_LINK_SETTINGS = "link=Settings"
    ID_MENU_LINK_STORAGE_SYSTEMS = "link=Storage Systems"
    ID_MENU_LINK_STORAGE_POOLS = "link=Storage Pools"
    ID_MENU_LINK_STORAGE_TEMPLATES = "link=Volume Templates"
    ID_MENU_LINK_STORAGE_VOLUMES = "xpath=//*[@id='hp-main-menu']//a[text()='Volumes']"
    ID_MENU_LINK_USERS_AND_GROUPS = "link=Users and Groups"
    ID_MENU_LINK_SAN_MANAGERS = "link=SAN Managers"
    ID_MENU_LINK_SAN = "link=SANs"
    ID_MENU_LINK_PROFILE_TEMPLATE = "link=Server Profile Templates"
    ID_SIDEBAR_CONTROL = 'hp-sidebar-control'
    ID_MENU_ONE_VIEW = "id=hp-main-menu-labels"
    ID_LINK_NETWORK_SET = "link=Network Sets"
    HELP_PAGE_TITLE = "HP OneView 1.05 help"
    HELP_PAGE_FRAME_NAME = "xpath=//frame[contains(@name, 'mainhelp_pane')]"
    ID_TABLE_MASTER_BASE = "xpath=.//div[@class='dataTables_scrollBody']/table[@class='hp-master-table hp-selectable dataTable']"
    ID_TABLE_MASTER_ITEM = "xpath=//table[@class='hp-master-table hp-selectable dataTable']/tbody/tr/td[translate(text(),'" + FusionUIConst.CONST_ZERO_WIDTH_SPACE + "','')='%s']"  # resource name
    MASTER_TABLE_ITEM = ID_TABLE_MASTER_BASE + "//td[text()='%s']"
    # ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='cic-profile-page']/div[@class='hp-sub-nav']/div[@class='hp-sidebar-control']/div[@class='hp-pin-right']"
    ID_BUTTON_RIGHT_SIDEBAR_ACTIVITY = "xpath=(//div[@class='hp-sidebar-control']/div[@class='hp-pin-right'])[2]"
    ID_RIGHT_SIDEBAR_TITLE = "xpath=.//*[@id='hp-activity-flyout']/header/h1[text()='Activity']"
    ID_ACTIVITY_BELL_ICON = "xpath=//div[@id='hp-activity-control']/div[@class='hp-icon hp-activity']"
    ID_ACTIVITY_SIDEBAR = "id=hp-activity-flyout"
    ID_TEXT_LIST_SIDEBAR_ACTIVITY_STATUS = "xpath=//*[@id='hp-flyout-activities']/li[1]/div[1]/div[1]"
    ID_TEXT_LIST_SIDEBAR_ACTIVITY_MESSAGE = "xpath=//*[@id='hp-flyout-activities']/li[1]/div[1]/div[2]"
    ID_TEXT_LIST_SIDEBAR_ACTIVITY_SOURCE = "xpath=//*[@id='hp-flyout-activities']/li[1]/div[1]/div[3]"
    ID_RIGHT_SIDEBAR_ACTIVITY = "xpath=//*[@id='hp-flyout-activities']/li[@class='hp-activity hp-active']/div[@class='hp-brief']/div[contains(@class, 'hp-status')]/span[contains(text(),'%s')]" \
                                "/../following-sibling::div[@class='hp-activity-source' and text()='%s']/preceding-sibling::div[@class='hp-activity-message']/p/span[text()='%s']"
    ID_TEXT_ACTIVITY_MESSAGE = "//*[@id='hp-flyout-activities']/li/div[@class='hp-full']/div/div[@class='hp-notification-details']"
    XPATH_PANEL_SELECTOR_VALUE = "xpath=//*[@class='hp-panel-selector hp-select']/div"

    # Search Generic-----------
    ID_MENU_LINK_BASE = "link=%s"
    ID_PAGE_LABEL_BASE = "xpath=//div[@class='hp-page-label']/h1[text()='%s']"
    ID_INPUT_SEARCH = "xpath=//div[@id='hp-search-input']/input"
    ID_SEARCH_BAR = "xpath=//h2[@id='hp-search-control']"
    ID_SEARCH_CLEAR = "xpath=//div[@id='hp-search-clear']"
    ID_LABEL_FIRMWARE_BUNDLE_BASE = "xpath=//div[@id='cic-fwdriver-page']//div[text()='%s']"
    ID_LABEL_ENCLOSURE_GROUPS_BASE = "xpath=//li[starts-with(@class,'hp-master-grid-item')]/header/div[text()='%s']"
    ID_LABEL_SERVER_HARDWARE_TYPE_BASE = "xpath=//div[@id='cic-servertypes-page']//div[text()='%s']"
    ID_MENU_LINK_REPORTS = "link=Reports"

    # Help page
    ID_HELP_CONTROL = "hp-help-control"
    HELP_PAGE_CONTENT_LIST = "xpath=//div[@class='toc']/dl/dd[%s]/table/tbody/tr/td[2]"
    HELP_PAGE_SUB_CONTENT = "xpath=//div[@class='toc']/dl/dd[%s]/dl/dd[%s]"
    HELP_PAGE_SUB_CONTENT_LIST = "xpath=//div[@class='toc']/dl/dd[%s]/dl/dd[%s]/table/tbody/tr/td[2]"
    ID_LINK_BROWSE_HELP = "href=/doc#/cic"

    # Change control pop-up
    ID_CHANGE_CONTROL_POPUP = "//div[@id='hp-form-changes-control']"
    ID_CHANGE_CONTROL_LABELS = "//li[@class='hp-form-change']"
    ID_CHANGE_MESSAGE_TEXT = "//span[@class='hp-form-message-text'][text()='REPLACE_THIS_TEXT']"
    ID_CHANGE_HISTORY_LABEL = "//div[@class='hp-form-change-label'][text()='REPLACE_THIS_LABEL']"
    ID_CHANGE_HISTORY_VALUE = "//div[@class='hp-form-change-value'][text()='REPLACE_THIS_VALUE']"

    # Editing labels of resource
    ID_LABEL_EDIT_LABELS_LABELS_PANEL = "xpath=//*[@id='hp-labels-show-panel']"
    ID_LINK_EDIT_LABELS_EDIT = "xpath=//*[@id='hp-labels-show-panel']/label/a"
    ID_DIALOG_EDIT_LABELS = "xpath=//header//span[contains(text(), 'Edit Labels')]/ancestor::*/div[@class='hp-dialog']"
    ID_BUTTON_EDIT_LABELS_ADD = "xpath=//*[@id='hp-labels-edit-add']"
    ID_ICON_EDIT_LABELS_SEARCH = "xpath=//*[@class='hp-search-combo-control']"
    ID_INPUT_EDIT_LABELS_NAME = "xpath=//*[@id='hp-labels-edit-search-input']"
    ID_BUTTON_EDIT_LABELS_OK = "xpath=//*[@id='hp-labels-edit-ok']"
    ID_BUTTON_EDIT_LABELS_CANCEL = "xpath=//*[@id='hp-labels-edit-cancel']"
    ID_ICON_EDIT_LABELS_HELP = "xpath=//*[@id='hp-labels-edit-header']/div/a"
    ID_ICON_EDIT_LABELS_REMOVE = "xpath=//*[@id='hp-labels-edit-table']//label[text()='%s']/../..//div[contains(@class, 'hp-close')]"  # label's name
    ID_LABEL_EDIT_LABELS_EXISTING_LABEL = "xpath=//*[@id='hp-labels-edit-table']//label[text()='%s']"


def TimeoutChecker(timeout_sec=30, interval_sec=5):
    """ TimeoutChecker
        Description : Function decorator for checking if decorated function return true in specified timeout_sec
    """
    def wrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            start_time = datetime.now()
            while True:
                result = f(*args, **kwargs)
                # None indicates immediately exit
                if result is None:
                    return False
                if result is True:
                    return True
                elif result is not False:
                    return result
                # if reach timeout
                if (datetime.now() - start_time).seconds >= timeout_sec:
                    # self.getLogger().warn("Page not loaded within %s secs!" % timeout_sec)
                    return False
                time.sleep(interval_sec)
        return wrapped_f
    return wrap


def NavigateDeco(section):
    def wrapper(f):
        @wraps(f)
        def action(*args, **kwargs):
            FusionUIBase().navigate_to_section(section)
            return f(*args, **kwargs)
        return action
    return wrapper


def ScreenshotDeco(enabled=True):
    def wrapper(f):
        @wraps(f)
        def action(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                exc_type, exc_instance, exc_traceback = sys.exc_info()
                formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
                if enabled is True:
                    if getattr(e, 'screen_captured', None) is None:
                        ui_lib.get_s2l().capture_page_screenshot()
                        BuiltIn().log("Took screenshot into %s" % BuiltIn().get_variable_value('${OUTPUT DIR}'), "DEBUG", console=True)
                message = 'Internal traceback:\n{0}\n{1}:\n{2}\n{3}'.format(
                    formatted_traceback,
                    exc_type.__name__,
                    '',
                    getattr(exc_instance, 'inner_exception_obj', '')
                )
                BuiltIn().log(message, "DEBUG", console=True)
                e.screen_captured = True

                raise e
        return action
    return wrapper


def TakeScreenShotWhenReturnFalseDeco(f):
    def action(*args, **kwargs):
        ret = f(*args, **kwargs)
        if ret is False:
            logger.debug("capture screenshot due to return value is False")
            ui_lib.get_s2l().capture_page_screenshot()
        return ret
    return action


class ScreenShotType(type):

    def __new__(mcs, classname, supers, classdict):  # @NoSelf
        for attr, attrval in classdict.items():
            if isinstance(attrval, FunctionType) and attr.startswith('_') is False:
                classdict[attr] = ScreenshotDeco(enabled=True)(attrval)
        return type.__new__(mcs, classname, supers, classdict)


class ClassMethodType(type):

    def __new__(mcs, classname, supers, classdict):  # @NoSelf
        for attr, attrval in classdict.items():
            if isinstance(attrval, FunctionType):
                classdict[attr] = classmethod(attrval)
        return type.__new__(mcs, classname, supers, classdict)


class SectionType:

    '''
    Just for hold 'enum' types (page link & page title) which can be passed to method navigateToSection as 1th parameter
    '''
    # GENERAL
    DASHBOARD = ('dashboard', 'Dashboard')
    ACTIVITY = ('activity', 'Activity')
    FIRMWARE_BUNDLES = ('fwdrivers', 'Firmware Bundles')
    REPORTS = ('report', 'Reports')

    # SERVERS
    SERVER_PROFILES = ('profiles', 'Server Profiles')
    SERVER_PROFILE_TEMPLATES = ('profile-templates', 'Server Profile Templates')
    ENCLOSURE_GROUPS = ('enclosuregroups', 'Enclosure Groups')
    LOGICAL_ENCLOSURES = ('logicalenclosures', 'Logical Enclosures')
    ENCLOSURES = ('enclosure', 'Enclosures')
    SERVER_HARDWARE = ('server-hardware', 'Server Hardware')
    SERVER_HARDWARE_TYPES = ('server-hardware-types', 'Server Hardware Types')

    # HYPERVISORS
    HYPERVISOR_CLUSTER_PROFILES = ('hypervisor-cluster-profiles', 'Hypervisor Cluster Profiles')

    # NETWORKING
    LOGICAL_INTERCONNECT_GROUPS = ('switchtemplate', 'Logical Interconnect Groups')
    LOGICAL_INTERCONNECTS = ('logicalswitch', 'Logical Interconnects')
    LOGICAL_SWITCH_GROUPS = ('torswitchgroup', 'Logical Switch Groups')
    LOGICAL_SWITCHES = ('torlogicalswitch', 'Logical Switches')
    NETWORKS = ('network', 'Networks')
    NETWORK_SETS = ('networkset', 'Network Sets')
    INTERCONNECTS = ('interconnect', 'Interconnects')
    SWITCHES = ('switch', 'Switches')

    # STORAGE
    VOLUME_TEMPLATES = ('storage-templates', 'Volume Templates')
    VOLUME_SETS = ('storage-volume-sets', 'Volume Sets')
    VOLUMES = ('storage-volumes', 'Volumes')
    STORAGE_POOLS = ('storage-pools', 'Storage Pools')
    STORAGE_SYSTEMS = ('storage-systems', 'Storage Systems')
    SANS = ('sans', 'SANs')
    SAN_MANAGERS = ('san-managers', 'SAN Managers')
    DRIVE_ENCLOSURES = ('driveenclosures', 'Drive Enclosures')

    # FACILITIES
    DATA_CENTERS = ('datacenter', 'Data Centers')
    RACKS = ('rack', 'Racks')
    POWER_DELIVERY_DEVICES = ('power-device', 'Power Delivery Devices')
    UNMANAGED_DEVICES = ('unmanaged', 'Unmanaged Devices')

    ##
    SETTINGS = ('settings', 'Settings')
    USERS_AND_GROUPS = ('user', 'Users and Groups')
    HARDWARE_SETUP = ('hardware-setup', 'Hardware Setup')
    VCENTERS = ('hypervisor-managers', 'vCenters')
    DEPLOYMENT_SERVERS = ('deployment-managers', 'Deployment Servers')
    OS_DEPLOYMENT_SERVERS = ('deployment-servers', 'OS Deployment Servers')


class SubSectionType(object):

    class Settings(object):

        APPLIANCE = ('settings/show/appliance/general', 'Appliance')
        BACKUP = ('settings/show/appliance/backup', 'Backup')
        NETWORKING = ('settings/show/networking', 'Networking')
        TIME_AND_LOCALE = ('settings/show/timeandlocale', 'Time and Locale')
        PROXY = ('settings/show/proxy', 'Proxy')
        LICENSE = ('settings/show/license/general', 'Licenses')
        SECURITY = ('settings/show/security/details', 'Security')
        NOTIFICATIONS = ('settings/show/emailnotification', 'Notifications')
        SCOPES = ('scopes', 'Scopes')
        ACTIVITY = ('settings/show/guid', 'Activity')
        SNMP = ('settings/show/snmp', 'SNMP')
        ADDRESSES_AND_IDENTIFIERS = ('settings/show/guid', 'Addresses and Identifiers')
        REMOTE_SUPPORT = ('settings/show/remotesupport/general', 'Remote Support')
        REPOSITORY = ('repository', 'Repository')


class FusionUIBase(object):

    # __metaclass__ = ClassMethodType

    class APIMethods(object):

        def __init__(self):
            self.fusion_client = HttpVerbs()
            s2l = ui_lib.get_s2l()
            token = s2l.get_cookie_value('token')
            host = s2l.get_location().strip('https://').split('/')[0]
            self.fusion_client._host = host
            self.fusion_client._sessionID = token
            self.fusion_client._headers['auth'] = token
            self.fusion_client._headers['X-Api-Version'] = self.fusion_client._currentVersion()

        def get_enclosure_group(self, eg_name=None, uri=None, param=None):
            if eg_name:
                param = "?filter=\"'name' = '%s'\"" % eg_name
            return EnclosureGroup(self.fusion_client).get(param=param, uri=uri)

        def get_logical_interconnect_group(self, lig_name=None, uri=None, param=None):
            if lig_name:
                param = "?filter=\"'name' = '%s'\"" % lig_name
            return LogicalInterconnectGroup(self.fusion_client).get(param=param, uri=uri)

        def get_interconnect_type(self, ict_name=None, uri=None, param=None):
            if ict_name:
                param = "?filter=\"'name' = '%s'\"" % ict_name
            return InterconnectTypes(self.fusion_client).get(param=param, uri=uri)

        def get_server_hardware_type_by_server_hardware_name(self, server_name=None, uri=None, param=None):
            logger.debug("Get server hardware type by server hardware [ %s ]" % server_name)
            if server_name:
                param = "?filter=\"'name' = '%s'\"" % server_name
            resp = ServerHardware(self.fusion_client).get(param=param, uri=uri)
            if resp['count'] == "0":
                return "Server hardware [ %s ] not found" % server_name
            sht_uri = resp['members'][0]["serverHardwareTypeUri"]
            resp = ServerHardwareTypes(self.fusion_client).get(uri=sht_uri)
            return resp["name"]

        def check_carbon_against_enclosure_group(self, eg_name):
            # check:
            #   - if Carbon interconnect model 'Virtual Connect SE 16Gb FC Module for Synergy' is existing in the given EG
            #   - if other Non-Carbon interconnect model is existing in the given EG
            logger.debug("checking if Carbon IC '%s' exists in EG '%s' ..." % (FusionUIConst.CONST_CARBON, eg_name))
            if len(eg_name) == 0:
                ui_lib.fail_test("given EG is empty, cannot get such a EG resource via API for further validation")

            eg = self.get_enclosure_group(eg_name=eg_name)
            ui_lib.fail_test("More than 1 Enclosure Group found with given name '%s', please provide more accurate name to validate the desired EG" % eg_name) if len(eg['members']) > 1 else None
            ui_lib.fail_test("Enclosure Group '%s' NOT found by the API call, " % eg_name) if len(eg['members']) == 0 else None

            interconnect_type_uri_list = []

            for eg_member in eg['members']:
                if eg_member['name'] == eg_name:
                    for ic_bay_mapping in eg_member['interconnectBayMappings']:
                        lig_uri = ic_bay_mapping['logicalInterconnectGroupUri']
                        lig = self.get_logical_interconnect_group(uri=lig_uri)
                        for ict in lig['interconnectMapTemplate']['interconnectMapEntryTemplates']:
                            ict_uri = ict['permittedInterconnectTypeUri']
                            if ict_uri not in interconnect_type_uri_list:
                                interconnect_type_uri_list.append(ict_uri)
                                logger.debug("[API Call]: got interconnect type URI <%s> from LIG <%s> of EG <%s>" % (ict_uri, lig['name'], eg_name))
                else:
                    continue

            interconnect_type_name_list = []

            if len(interconnect_type_uri_list) > 0:
                for ict_uri in interconnect_type_uri_list:
                    ict = self.get_interconnect_type(uri=ict_uri)
                    interconnect_type_name_list.append(ict['name']) if ict['name'] not in interconnect_type_name_list else None
                    logger.debug("[API Call]: interconnect type <%s> found in the given Enclosure Group <%s> at URI <%s>" % (ict['name'], eg_name, ict_uri))

            # check if Carbon 'Virtual Connect SE 16Gb FC Module for Synergy' exists in the interconnect type name list
            carbon_exists = True if FusionUIConst.CONST_CARBON in interconnect_type_name_list else False
            # check if other IC type than Carbon 'Virtual Connect SE 16Gb FC Module for Synergy' exists in the interconnect type name list
            non_carbon_exists = True if len([x for x in interconnect_type_name_list if x != FusionUIConst.CONST_CARBON]) > 0 else False

            carbon_existence = (carbon_exists, non_carbon_exists)

            return carbon_existence

        def get_oneview_model_type(self):
            appliance_version = {"C7000": "HPE OneView VM - VMware vSphere",
                                 "Synergy": "Synergy Composer"}
            resp = ApplianceNodeInformation(self.fusion_client).get_version()
            for app_type in appliance_version:
                if resp["modelNumber"].startswith(appliance_version[app_type]):
                    return app_type

        def get_logical_switch_group(self, lsg_name=None, uri=None, param=None):
            if lsg_name:
                param = "?filter=\"'name' = '%s'\"" % lsg_name
            return LogicalSwitchGroup(self.fusion_client).get(param=param, uri=uri)

    @classmethod
    def click_item_from_master_table(cls, item_name, timeout=5, time_for_loading=2):
        logger.debug("click item '%s' from master table ..." % item_name)
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.MASTER_TABLE_ITEM % item_name, timeout=timeout, fail_if_false=True)
        BuiltIn().sleep(time_for_loading)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_item_should_exist_in_master_table(cls, item_name, item_type='UNKNOWN', timeout=5, fail_if_false=True):
        logger.debug("verify {} '{}' should exist ...".format(item_type, item_name))
        if ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_TABLE_MASTER_ITEM % item_name, timeout=timeout, fail_if_false=fail_if_false):
            logger.debug("{} '{}' is successfully verified as visible within {} second(s)".format(item_type, item_name, timeout))
            return True
        else:
            msg = "{} '{}' is failed to be verified as visible within {} second(s)".format(item_type, item_name, timeout)
            return FusionUIBase.fail_test_or_return_false(message=msg, fail_if_false=fail_if_false)

    @classmethod
    def set_login_status(cls, status):
        """ _set_login_status
            Description : Function used for setting the login status, set true once you are logged in to applicance
        """
        test_data.set_variable(test_data.GlobalProperty.UiLoggedIn, status)

    @classmethod
    def get_login_status(cls):
        """ get_login_status
            Description : Function used for retrieving the login status.
        """
        status = test_data.get_variable(test_data.GlobalProperty.UiLoggedIn)
        if status is None:
            return False
        return status

    @classmethod
    def logged_in(cls):
        """ logged_in
            Description: Get the UI logged in status
            """
        return cls.get_login_status()

    @classmethod
    def wait_for_element_and_click(cls, locator, timeout=5, fail_if_false=False, js_click=False):
        """ _wait_for_element
            Description : waits for an element to exist in UI
        """
        selenium2lib = get_s2l()
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            # Occasionally, a DOM refresh will cause an exception here
            # if the object is changing state.  Catch the exception
            # to prevent a failure.
            try:
                if selenium2lib._is_element_present(locator) and \
                        selenium2lib._is_visible(locator):

                    if js_click is False:
                        selenium2lib.click_element(locator)
                    else:
                        element = ui_lib.get_s2l()._element_find(locator, first_only=True, required=False)
                        script = """
                            el = arguments[0];
                            el.click();
                        """
                        ui_lib.get_s2l()._current_browser().execute_script(script, element)
                    return True
            except:
                pass
            BuiltIn().sleep(0.1)

        if fail_if_false:
            fail_test("Failed to wait for element '%s'" % locator)
        return False

    @classmethod
    def get_webelement_attribute(cls, locator, attribute, timeout=5, fail_if_false=False):
        """ Function which adds a wrapper around retrieving
            webelement attributes to handle a
            StaleElementReferenceException.

            Example:
                 name = get_webelement_attribute("id=some_element", "text")

                 value = get_webelement_attribute("xpath=//path/to/element", "value")
        """

        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            try:
                webelement = ui_lib.get_s2l()._element_find(locator, True, False)

                if webelement is None:
                    time.sleep(0.1)
                    continue

                if attribute == "text":
                    return webelement.text
                elif attribute == "name":
                    return webelement.name
                else:
                    return webelement.get_attribute(attribute)
            except (StaleElementReferenceException):
                pass

        if fail_if_false:
            fail_test("Failed to get element attribute in %s seconds" % timeout)

        logger.warn(
            "Failed to get element within timeout due to StaleElementReferenceException on webelement")
        return None

    @classmethod
    def get_text(cls, obj, timeout=5, fail_if_false=False, hidden_element=False):
        """ StaleElementException safe function to return element text
            Works with either a locator or webelement object
            Example:
                 text = get_text("id=my_locator")
                 text = get_text(my_webelement_object)
        """
        s2l = get_s2l()
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            try:
                if isinstance(obj, str) or isinstance(obj, unicode):
                    if hidden_element is False:
                        return s2l._get_text(obj)
                    else:
                        elt = s2l._element_find(obj, True, False)
                        if elt:
                            return elt.get_attribute('textContent')
                elif isinstance(obj, WebElement):
                    if hidden_element is False:
                        return obj.text
                    else:
                        return obj.get_attribute('textContent')
                else:
                    raise TypeError("Cannot test for visibility with unknown type {0}".format(type(obj)))
            except Exception:
                pass

        if fail_if_false:
            fail_test("Fail to get element text in %s seconds" % timeout)

        logger.warn("Failed to get element visibility within timeout due to StaleElementReferenceException on webelement")
        return None

    @classmethod
    def get_multi_elements_text(cls, locator, timeout=5, fail_if_false=False, hidden_element=False):
        """
        Get text for all elements that match locator. Return result as list

        :param locator: expression for locating elements
        :param timeout:
        :param fail_if_false: set to True to fail the test case if can't get elements' text in :timeout seconds
        :param hidden_element: set to True to get text of hidden elements. (Selenium only give empty string for visible element)
        :return: all elements' text as list otherwise return None
        """
        s2l = get_s2l()
        start = datetime.now()
        ret = []
        while (datetime.now() - start).total_seconds() < timeout:
            try:
                elt_list = ElementFinder().find(s2l._current_browser(), locator)
                for elt in elt_list:
                    if hidden_element is False:
                        ret.append(elt.text)
                    else:
                        ret.append(elt.get_attribute('textContent'))

                return ret
            except Exception:
                ret = []

        if fail_if_false:
            fail_test("Failed to get multi elements text in %s seconds" % timeout)
        logger.warn("Failed to get multi elements visibility within %s seconds due to NoSuchElementException, Timeout or StaleElementReferenceException " % timeout)
        return None

    @classmethod
    def wait_for_checkbox_and_select(cls, locator, timeout=5, fail_if_false=True):
        """Selects checkbox identified by `locator`.

        Does nothing if checkbox is already selected. Key attributes for
        checkboxes are `id` and `name`. See `introduction` for details about
        locating elements.
        """
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            try:
                ui_lib.wait_for_element(locator)
                element = get_s2l()._get_checkbox(locator)
                while not element.is_selected():
                    element.click()
                    element = get_s2l()._get_checkbox(locator)
                return element
            except Exception:
                pass

            if fail_if_false:
                fail_test("Failed to select checkbox: [ %s ] in %s seconds" % (locator, timeout))

            logger.warn("Failed to select checkbox: " + locator)

        return None

    @classmethod
    def wait_for_checkbox_and_unselect(cls, locator, timeout=5, fail_if_false=True):
        """Unselects checkbox identified by `locator`.
        Does nothing if checkbox is already unselected. Key attributes for
        checkboxes are `id` and `name`. See `introduction` for details about
        locating elements.
        """
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            try:
                ui_lib.wait_for_element(locator)
                element = get_s2l()._get_checkbox(locator)
                while element.is_selected():
                    element.click()
                    element = get_s2l()._get_checkbox(locator)
                return element
            except Exception:
                time.sleep(0.1)

            if fail_if_false:
                fail_test("Failed to unselect checkbox: [ %s ] in %s seconds" % (locator, timeout))

            logger.warn("Failed to unselect checkbox within timeout due to StaleElementReferenceException on webelement")
        return None

    @classmethod
    def choose_option_by_text(cls, select_id, option_txt, timeout=5, fail_if_false=True):
        """
        Choose a option from a drop down box.
        Only work for Atlas style drop down box.

        :param select_id: the id attribute of select element in drop down box wrapper. Can accept s2l standard id expression like 'id=xxx', method will strip 'id=' prefix for you
        :param option_txt: text of the option to be selected
        :param timeout:
        :param fail_if_false: set to True to fail the test case if can't perform the action otherwise just return True/False
        :return: True/False if :fail_if_false set to False
        """
        m = re.search(r"^id=(.*)", select_id.replace(' ', ''))
        if m is not None:
            select_id = m.group(1)

        id_part = ' or '.join(["@id='%s'" % item for item in select_id.split('|')])

        # xpath1 = "xpath=//select[{id_part}]/..//div[@class='hp-select']|//select[{id_part}]/../a".format(id_part=id_part)
        xpath1 = "xpath=//select[{id_part}]/../div[contains(@class, 'hp-select') and not(contains(@class, 'hp-disabled'))]|//select[{id_part}]/../a".format(id_part=id_part)
        ui_lib.wait_for_element_and_click(xpath1, timeout=timeout, fail_if_false=True)

        # TODO: check if the control is disabled by checking class attribute (style 1: xpath1)
        click_flag = True
        classes = FusionUIBase.get_webelement_attribute(xpath1, "class", timeout=1, fail_if_false=False)
        if classes is not None:
            logger.debug("Got class attribute of combo box: %s" % classes)
            lst = [item.strip() for item in classes.split(' ')]

            if 'selectBox-disabled' in lst:
                click_flag = False

        xpath = "xpath=//select[%s]/../div/ol/li/span[text()='%s']" % (id_part, option_txt)

        if click_flag is True:
            if ui_lib.wait_for_element_visible(xpath, timeout=1, fail_if_false=False) is True:
                return ui_lib.wait_for_element_and_click(xpath, timeout=1, fail_if_false=True)
            else:
                xpath = "xpath=//ul[li/a[text()='%s']]" % option_txt
                elt_lst = ui_lib.get_s2l()._element_find(xpath, False, False)

                for elt in elt_lst:
                    style = elt.get_attribute('style')
                    if style is None or style == '':
                        continue

                    style_lst = [e for e in style.split(';') if e.strip() != '']
                    style_dict = dict(zip([k.split(':')[0].strip().lower() for k in style_lst], [k.split(':')[1].strip().lower() for k in style_lst]))
                    if style_dict.get('display') != 'none':
                        return elt.find_element_by_link_text(option_txt).click()
                else:
                    # 2016.3.7 Yulong Changed for UI change in 3.00.00-0238663
                    xpath = "xpath=//select[%s]/..//ol/li[text()='%s']" % (id_part, option_txt)

                    return ui_lib.wait_for_element_and_click(xpath, timeout, fail_if_false)
                    # if ui_lib.wait_for_element_visible(xpath, timeout=2, fail_if_false=False) is True:
                    #     ui_lib.wait_for_element_and_click(xpath, timeout=2, fail_if_false=fail_if_false)
                    # else:
                    #     BuiltIn().fail("Option '%s' not found" % option_txt)
        else:
            msg = "The combobox control is disabled, skip clicking operation"
            cls.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def choose_combo_option_by_text(cls, input_id, option_txt, timeout_sec=10, locator=None, fail_if_false=True):
        """
        Choose option only for a Atlas base combo box.
        This method will do following steps:
        1. input :option_txt into textbox(:input_id)
        2. choose option from drop down list

        :param input_id: id attribute of the input element which be wrapped in combo box. Can accept s2l standard expression like 'id=xxx'
        :param option_txt: text of the option to be selected
        :param timeout_sec:
        :param locator: expression for locating input element. Note that input_id will be no effect if locator is not None.
        :param fail_if_false: set to True to fail the test case if can't perform the action otherwise just return True/False
        :return: True/False if :fail_if_false set to False
        """
        if not isinstance(timeout_sec, types.IntType):
            timeout_sec = int(timeout_sec)
        # click search icon
        # ui_base.click("xpath=//input[@id='%s']/../div[@class='hp-search-combo-control']" % input_id)

        m = re.search(r"^id=(.*)", input_id.replace(' ', ''))
        if m is not None:
            input_id = m.group(1)

        if locator is None:
            ui_lib.wait_for_element_and_input_text("xpath=//input[@id='%s']" % input_id, option_txt, fail_if_false=fail_if_false)
            BuiltIn().should_be_true(ui_lib.wait_for_element_visible("xpath=//input[@id='%s']/..//div[@class='hp-search-combo-menu']" % input_id,
                                                                     timeout=timeout_sec, fail_if_false=fail_if_false), "Combo menu not show up")
            return ui_lib.wait_for_element_and_click("xpath=//input[@id='%s']/..//div[@class='hp-search-combo-menu']/ol//span[text()='%s']/.." % (input_id, option_txt),
                                                     timeout=timeout_sec, fail_if_false=fail_if_false)
        else:
            ui_lib.wait_for_element_and_input_text(locator, option_txt, fail_if_false=fail_if_false)
            BuiltIn().should_be_true(ui_lib.wait_for_element_visible("%s/..//div[@class='hp-search-combo-menu']" % locator,
                                                                     timeout=timeout_sec, fail_if_false=fail_if_false), "Combo menu not show up")
            return ui_lib.wait_for_element_and_click("%s/..//div[@class='hp-search-combo-menu']/ol//span[text()='%s']/.." % (locator, option_txt),
                                                     timeout=timeout_sec, fail_if_false=fail_if_false)

    @classmethod
    def toggle_button(cls, locator, turn_on, timeout=10):
        """
        Toggle a Atlas style button. The target button usually has 2 states(enabled/disabled)

        :param locator: expression for locating the toggle button
        :param turn_on: True to enable button, False to disable button
        :param timeout:
        """
        if ui_lib.wait_for_element_visible(locator, timeout, fail_if_false=False) is False:
            BuiltIn().fail("Target element [ %s ] does not show in page!" % locator)

        # get current state of target toggle button
        state = ui_lib.wait_for_element_class(locator, 'hp-checked', timeout=3, fail_if_false=False)
        if turn_on is True:
            if state is True:
                return
            else:
                # click button and wait animation finish
                ui_lib.wait_for_element_and_click(locator, fail_if_false=True)
                BuiltIn().should_be_true(ui_lib.wait_for_element_class(locator, 'hp-checked', timeout=1, fail_if_false=False), 'Failed to change toggle button [ %s ] state to on!' % locator)

        if turn_on is False:
            if state is False:
                return
            else:
                ui_lib.wait_for_element_and_click(locator, fail_if_false=True)
                BuiltIn().should_be_true(not ui_lib.wait_for_element_class(locator, 'hp-checked', timeout=1, fail_if_false=False), 'Failed to change toggle button [ %s ] state to off!' % locator)

    @classmethod
    def navigate_to_section(cls, section, time_for_loading=0):
        """
        Navigate to specific page - 1.

        :param section: Only accept variable of class 'SectionType'. e.g. SectionType.DASHBOARD
        :param time_for_loading: Wait some seconds after navigate to the page.
        """
        cls.navigate_to_section_by_link(section[0], section[1], time_for_loading)

        # If the Activity sidebar is opened from previous page, then close it first to avoid issues.
        if ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_RIGHT_SIDEBAR_TITLE, timeout=3, fail_if_false=False) is True:
            logger.debug("activity sidebar is opened on previous page, closing it first ...")
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_ACTIVITY_BELL_ICON, timeout=3, fail_if_false=True)

    @classmethod
    def navigate_to_section_by_link(cls, link, title, time_for_loading=0, sub_section=False):
        """
        Navigate to specific page - 2.

        :param link: text of the Link in top menu to be clicked
        :param title: Page label of target page
        :param time_for_loading: Wait some seconds after navigate to the page.
        :return:
        """
        logger.debug("navigate to %s [ %s ] by link '%s' " % ('sub section' if sub_section else 'section', title, link))
        s2l = ui_lib.get_s2l()
        ui_lib.wait_for_element_visible("//div[@id='hp-page-container'][contains(@class, 'hp-active')]", timeout=5, fail_if_false=True)

        locator = "//h1[.='Settings']" if title == 'Settings' else "xpath=//div[contains(@class, 'hp-page-label')]/h1[text()='%s']" % title
        if s2l._is_element_present(locator):
            logger.debug("already on [ %s ] page, function '%s' returns TRUE " % (title, sys._getframe().f_code.co_name))
            return True

        # open the menu and wait for it to be active
        if not sub_section and not s2l._is_element_present(FusionUIBaseElements.ID_MENU_ACTIVE):
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL)
            ui_lib.wait_for_element(FusionUIBaseElements.ID_MENU_ACTIVE)

        locator = "xpath=//a[@href='#/%s'][text()='%s']" % (link, title) if link == SectionType.ACTIVITY[0] else "//a[@href='#/%s']" % link
        # if the new menu style is active, the link may lie under a collapsed section
        if not sub_section and not ui_lib.is_visible(locator):
            ui_lib.wait_for_element_and_click(locator + '/parent::li/parent::ul/parent::li')

        ui_lib.wait_for_element_and_click(locator=locator, timeout=5, fail_if_false=True)

        # if the menu is still opened, close it
        if ui_lib.is_visible(FusionUIBaseElements.ID_MENU_ACTIVE):
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_MAIN_MENU_CONTROL)
            ui_lib.wait_for_element_remove(FusionUIBaseElements.ID_MENU_ACTIVE)

        locator = "xpath=//h1[.='Settings']" if title == 'Settings' else "xpath=//div[contains(@class, 'hp-page-label')]/h1[text()='%s']" % title
        ui_lib.wait_for_element_visible(locator=locator, timeout=5, fail_if_false=False)

        @TimeoutChecker(interval_sec=0.5)
        def check_action_btn_empty_msg():
            if ui_lib.wait_for_element_visible("xpath=//div[@class='hp-empty-message']", timeout=1, fail_if_false=False) is True:
                return True

            if ui_lib.wait_for_element_visible("xpath=//div[@class='hp-details-actions hp-drop-menu' and not(boolean(@style='display:none' or @style='display: none;'))]/label[text()='Actions']", timeout=1, fail_if_false=False) is True:
                return True

            if ui_lib.wait_for_element_visible("xpath=//ol[@class='hp-options']/../div[.='Overview']", timeout=1, fail_if_false=False) is True:
                return True

            return False

        if title == "Settings":
            BuiltIn().should_be_true(ui_lib.wait_for_element_visible("id=hp-settings-panels", fail_if_false=False),
                                     "Failed to navigate to page '%s'" % title)
        elif title == "Activity":
            BuiltIn().should_be_true(ui_lib.wait_for_element_visible("id=hp-activities", fail_if_false=False),
                                     "Failed to navigate to page '%s'" % title)
        else:
            BuiltIn().should_be_true(check_action_btn_empty_msg(), "Failed to navigate to page '%s'" % title)

        BuiltIn().sleep(time_for_loading)

    @classmethod
    def wait_item_status_in_table(cls, name, table_id, expected_state, timeout=30):
        """
        :param name: item name in table
        :param table_id: item table id, such as "DataTables_Table_2"
        :param expected_state: "hp-status hp-status-ok", "hp-status hp-status-error", "hp-status hp-status-warning"
        """
        XPATH_ITEM_STATUS = "xpath=//table[@id='%s']/tbody/tr/td[text()='%s']/../td/div[@class='%s']" % (table_id, name, expected_state)
        if ui_lib.wait_for_element_visible(XPATH_ITEM_STATUS, timeout=timeout, fail_if_false=False):
            return True
        else:
            return False
        # raise NotImplementedError()

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_error_message_from_dialog(cls, timeout=30, form_id=None):
        """
        Get error message in a dialog.

        :param timeout:
        :return: A tuple contains boolean and message. return (True, msg) if able to get error message otherwise return (False, None)
        """
        logger.debug("checking if 'Verifying parameters' reports any errors ...")
        msg = None
        if form_id is None:
            prefix_form_id = ''
        else:
            prefix_form_id = "form[@id='%s']/descendant::" % form_id

        if ui_lib.wait_for_element_notvisible("//*[contains(text(), 'Verifying parameters')]", timeout=180, fail_if_false=False) is False:
            msg = "failed to wait for 'Verifying parameters' result to occur in 180 seconds, " \
                  "please either check if there's issue on this dialog form, or extend this timeout to exceed 180"
            logger.warn(msg)
            return False, msg

        if ui_lib.wait_for_element_visible("xpath=//" + prefix_form_id + "div[@class='hp-form-message-summary']/div[@class='hp-status hp-status-error' "
                                                                         "or @class='hp-status hp-status-warning']", timeout, fail_if_false=False):
            msg = cls.get_text("xpath=//" + prefix_form_id + "div[@class='hp-form-message-summary']/span[@class='hp-form-message-text']", fail_if_false=True)
            msg = "%s\n%s" % (msg, cls.get_multi_elements_text("xpath=//" + prefix_form_id + "div[@id='hp-form-message']/div[@class='hp-form-message-details']", fail_if_false=True))
            logger.warn("error found by 'Verifying parameters': [%s]" % msg)
            return True, msg
        else:
            logger.debug("no error reported by 'Verifying parameters'")
            return False, msg

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_warning_message_from_dialog(cls, timeout=30):
        """
        Get warning message in a dialog.

        :param timeout:
        :return: A tuple contains boolean and message. return (True, msg) if able to get warning message otherwise return (False, None)
        """
        msg = None

        if ui_lib.wait_for_element_visible("xpath=//div[@class='hp-form-message-summary']/div[@class='hp-status hp-status-warning']", timeout, fail_if_false=False):
            msg = cls.get_text("xpath=//div[@class='hp-form-message-summary']/span[@class='hp-form-message-text']", fail_if_false=True)
            msg = "%s\n%s" % (msg, cls.get_multi_elements_text("xpath=//div[@id='hp-form-message']/div[@class='hp-form-message-details']", fail_if_false=True))
            return True, msg
        else:
            return False, msg

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def get_info_message_from_dialog(cls, timeout=30):
        """
        Get info message in a dialog.

        :param timeout:
        :return: A tuple contains boolean and message. return (True, msg) if able to get warning message otherwise return (False, None)
        """
        msg = None

        if ui_lib.wait_for_element_visible("xpath=//div[@class='hp-form-message-summary']/div[@class='hp-status hp-status-info']", timeout, fail_if_false=False):
            msg = cls.get_text("xpath=//div[@class='hp-form-message-summary']/span[@class='hp-form-message-text']", fail_if_false=True)
            msg = "%s\n%s" % (msg, cls.get_multi_elements_text("xpath=//div[@id='hp-form-message']/div[@class='hp-form-message-details']", fail_if_false=True))
            return True, msg
        else:
            return False, msg

    @classmethod
    def para_should_be_in_list(cls, expect_list, actual_para, raise_err=True):
        expect_list = expect_list if isinstance(expect_list, types.ListType) else [expect_list]
        tag = False
        for expect_para in expect_list:
            if expect_para.lower().strip().replace(' ', '') == actual_para.lower().strip().replace(' ', ''):
                tag = True
                break
        if (tag is False) and (raise_err is True):
            raise Exception("unacceptable parameter '%s', expecting '%s'" % (actual_para, expect_list))
        else:
            return tag

    @classmethod
    def select_options_by_txt(cls, locator, txt_list, timeout=5, fail_if_false=True):
        """
        Select option by option text for a native drop down box.

        :param locator: expression for locating native select element
        :param txt_list: Accept list. Specify which option to be selected. Note that select element must enable multiple selection function if :txt_list contains more than 1 item.
        :param timeout:
        :param fail_if_false:
        :return: :raise Exception: If target element is not a select element
        """
        if ui_lib.wait_for_element(locator, timeout, fail_if_false) is False:
            return False

        # verify if a select element
        elt = ElementFinder().find(ui_lib.get_s2l()._current_browser(), locator)[0]
        tag_name = elt.tag_name

        if tag_name.lower() != 'select':
            raise Exception("select_options_by_txt only can apply on native select element.")

        select_obj = Select(elt)

        if len(txt_list) > 1:
            if not select_obj.is_multiple:
                raise Exception("select_options_by_txt only can apply on native select element with attribute multiple=true if txt_list contains more the 1 item.")

            for txt in txt_list:
                select_obj.select_by_visible_text(txt)
        elif len(txt_list) == 1:
            select_obj.select_by_visible_text(txt_list[0])
        else:
            raise Exception("Parameter 'txt_list' can be a empty list.")

        return True

    @classmethod
    def wait_resource_remove_from_table_list(cls, locator, not_found_locator, timeout=10, fail_if_false=True):
        """ Wait specified fusion resource remove from table list on left of the page

        :param locator: element locator for testing if element is disappeared. e.g. xpath=//table/tbody/tr/td[text()='%s']
        :param not_found_locator: element locator for testing if specified resource status changes to hp-not-found. e.g. //table/tbody/tr[contains(@class, 'hp-not-found')]/td[text()='%s']
        :param timeout:
        :param fail_if_false: immediately make test case failed
        :return: True if resource is successfully removed from table. False if fail to remove resource
        """
        start = datetime.now()

        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(not_found_locator, timeout=1, fail_if_false=False) is True:
                return True

            if ui_lib.wait_for_element_notvisible(locator, timeout=1, fail_if_false=False) is True:
                return True

        msg = "specified resource not removed from table in %s second" % timeout
        if fail_if_false is True:
            ui_lib.fail_test(msg)
        else:
            logger.warn(msg)

        return False

    @classmethod
    def verify_element_text(cls, item_name, locator, expect_value, timeout=5, fail_if_false=True, hidden_element=False):
        """
        Date:   2015-04-03
                This is to verify if an element's text is the expected value
                - check the element (item_name = 'License') to see if its text is "HP OneView Advanced" (expect_value)
        :param item_name: like a field name "License", will be used to output the log message
        :param locator: xpath for the element
        :param expect_value: expected text of the element, like "HP OneView Advanced".
                             Can accept regular expression like r'/^ok|error$/i' (i indicate case insensitive)
        :param timeout:
        :param fail_if_false: will fail the test if set to True
        :return: True if the element's actual text is same as the given expect_value
        """
        logger.debug("verifying that '%s' should contain '%s' ..." % (item_name, expect_value))
        actual_value = FusionUIBase.get_text(locator, timeout, fail_if_false, hidden_element)

        m = re.search(r"^(?<!\\)/(.+)(?<!\\)/([i]*)$", expect_value.strip())

        if m is None:  # general comparison
            if actual_value.lower().strip() == expect_value.lower().strip():
                logger.debug("%s is '%s', same as the expected value - '%s'" % (item_name, actual_value, expect_value))
                return True
            else:
                msg = "%s is '%s', NOT same as the expected value - '%s'" % (item_name, actual_value, expect_value)
                return cls.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
        else:  # regular expression match
            regexp = m.group(1)
            flag = m.group(2)

            if flag == 'i':
                flag = re.IGNORECASE
            else:
                flag = 0

            prog = re.compile(regexp, flag)
            m = prog.match(actual_value.strip())

            if m is not None:
                logger.debug("%s is '%s', match the expected value - '%s'" % (item_name, actual_value, expect_value))
                return True
            else:
                msg = "%s is '%s', NOT match the expected value - '%s'" % (item_name, actual_value, expect_value)
                return cls.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def verify_element_text_for_exclusion(cls, item_name, locator, excluded_value, timeout=5, fail_if_false=True, hidden_element=False):
        """
        Date:   2015-04-03
                This is to verify if an element's text is the expected value
                - check the element (item_name = 'License') to see if its text is "HP OneView Advanced" (expect_value)
        :param item_name: like a field name "License", will be used to output the log message
        :param locator: xpath for the element
        :param excluded_value: expected text of the element, like "HP OneView Advanced"
                               Can accept regular expression like r'/^ok|error$/i' (i indicate case insensitive)
        :param timeout:
        :param fail_if_false: will fail the test if set to True
        :return: True if the element's actual text is same as the given expect_value
        """

        logger.debug("verifying that '%s' should NOT contain '%s' ..." % (item_name, excluded_value))
        m = re.search(r"^(?<!\\)/(.+)(?<!\\)/([i]*)$", excluded_value.strip())

        actual_value = FusionUIBase.get_text(locator, timeout, fail_if_false, hidden_element)
        if m is None:  # general comparison
            if actual_value.lower().strip() == excluded_value.lower().strip():
                msg = "%s is '%s', same as the not-expected value - '%s'" % (item_name, actual_value, excluded_value)
                logger.warn(msg)
                if fail_if_false is True:
                    ui_lib.fail_test(msg)
                else:
                    return False
            else:
                logger.debug("%s is '%s', not same as the not-expected value - '%s'" % (item_name, actual_value, excluded_value))
                return True
        else:  # regular expression match
            regexp = m.group(1)
            flag = m.group(2)

            if flag == 'i':
                flag = re.IGNORECASE
            else:
                flag = 0

            prog = re.compile(regexp, flag)
            m = prog.match(actual_value.strip())

            if m is not None:
                msg = "%s is '%s', match the excluded value - '%s'" % (item_name, actual_value, excluded_value)
                if fail_if_false is True:
                    ui_lib.fail_test(msg)
                else:
                    logger.warn(msg)
                    return False
            else:
                logger.debug("%s is '%s', not match the excluded value - '%s'" % (item_name, actual_value, excluded_value))
                return True

    @classmethod
    def verify_view_by_name(cls, expected_view_name):
        ui_lib.wait_for_element_text(FusionUIBaseElements.XPATH_PANEL_SELECTOR_VALUE, expected_view_name, fail_if_false=True)
        logger.info("Current view has been verified as expected view of '%s'" % expected_view_name)

    @classmethod
    def select_view_by_name(cls, view_name, timeout=5, fail_if_false=True):
        """
        Date:   2015-04-03
                This is to change view by given view_name, like 'Overview/Activity/Hardware/Ports/Map' on Server Hardware page, or other pages.
                - check the element (item_name = 'License') to see if its text is "HP OneView Advanced" (expect_value)
        :param view_name: like a field name "License", will be used to output the log message
        :param timeout:
        :param fail_if_false: will fail the test if set to True
        :return: True if the view name is not successfully changed to given name
        """

        current_view_name = FusionUIBase.get_text(FusionUIBaseElements.XPATH_PANEL_SELECTOR_VALUE, timeout=timeout, fail_if_false=fail_if_false)

        if current_view_name == view_name:
            logger.info("current view is already '%s', nothing to do" % view_name)
            return True
        else:
            XPATH_TARGET_VIEW = "xpath=//*[contains(@class, 'hp-panel-selector hp-select')]//ol/li/a[.='%s']" % view_name
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.XPATH_PANEL_SELECTOR_VALUE, timeout=timeout, fail_if_false=fail_if_false)
            ui_lib.wait_for_element_and_click(XPATH_TARGET_VIEW, timeout=timeout, fail_if_false=fail_if_false)
            current_view_name = FusionUIBase.get_text(FusionUIBaseElements.XPATH_PANEL_SELECTOR_VALUE, timeout=timeout, fail_if_false=fail_if_false)
            if current_view_name == view_name:
                logger.info("current view is successfully changed to '%s'" % view_name)
                return True
            else:
                logger.warn("current view(%s) is not successfully changed to '%s', might be timeout issue" % (current_view_name, view_name))
                return False

    '''
    Deprecating for show_activity_sidebar
    @classmethod
    def show_activity_sidebar(cls, timeout=5):
        logger.debug("click activity right sidebar")
        ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_BUTTON_RIGHT_SIDEBAR_ACTIVITY, timeout, fail_if_false=True)
    '''

    @classmethod
    def show_activity_sidebar(cls, timeout=5):
        ''' Creates an abstract, action-based method which encapsulates the UI interaction.  Implemented by clicking the
        activity bell icon and waiting for the activity panel to appear '''
        if ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_RIGHT_SIDEBAR_TITLE, timeout=3, fail_if_false=False) is False:
            logger.debug("opening the activity sidebar ...")
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_ACTIVITY_BELL_ICON, timeout, fail_if_false=True)
            # ui_lib.wait_for_element(FusionUIBaseElements.ID_ACTIVITY_SIDEBAR, timeout, fail_if_false=True)
            ui_lib.wait_for_element_visible(FusionUIBaseElements.ID_RIGHT_SIDEBAR_TITLE, timeout, fail_if_false=True)
        else:
            logger.debug("closing the activity sidebar ...")
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_ACTIVITY_BELL_ICON, timeout, fail_if_false=True)
            ui_lib.wait_for_element_notvisible(FusionUIBaseElements.ID_RIGHT_SIDEBAR_TITLE, timeout, fail_if_false=True)

    @classmethod
    def get_sidebar_activity_message_list(cls, fail_if_false=False):
        logger.debug("get a list of all activities' message from table of right sidebar ...", also_console=False)
        ret = []
        if ui_lib.wait_for_element(FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_MESSAGE):
            message_list = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_MESSAGE, fail_if_false=fail_if_false)
            ret = ["No message - 'FusionUIBase.get_multi_elements_text' got None"] if message_list is None else message_list
            logger.debug("_______<1.3.1>_______<get_sidebar_activity_message_list>: message list is <%s>" % message_list, also_console=False)

        logger.debug("_______<1.3.1>_______<get_sidebar_activity_message_list>: returns <%s>" % ret, also_console=False)
        return ret

    @classmethod
    def get_sidebar_activity_source_list(cls, fail_if_false=False):
        logger.debug("get a list of all activities' source from table of right sidebar ...", also_console=False)
        ret = []
        if ui_lib.wait_for_element(FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_SOURCE):
            source_list = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_SOURCE, fail_if_false=fail_if_false)
            ret = ["No source - 'FusionUIBase.get_multi_elements_text' got None"] if source_list is None else source_list
            logger.debug("_______<1.3.2>_______<get_sidebar_activity_source_list>: source list is <%s>" % source_list, also_console=False)

        logger.debug("_______<1.3.2>_______<get_sidebar_activity_source_list>: returns <%s>" % ret, also_console=False)
        return ret

    @classmethod
    def get_sidebar_activity_status_list(cls, fail_if_false=False):
        logger.debug("get a list of all activities' status from table of right sidebar ...", also_console=False)
        ret = []
        if ui_lib.wait_for_element(FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_STATUS):
            status_list = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_STATUS, fail_if_false=fail_if_false, hidden_element=True)
            ret = ["No status - 'FusionUIBase.get_multi_elements_text' got None"] if status_list is None else status_list
            logger.debug("_______<1.3.3>_______<get_sidebar_activity_status_list>: status list is <%s>" % status_list, also_console=False)

        logger.debug("_______<1.3.3>_______<get_sidebar_activity_status_list>: status list is <%s>" % ret, also_console=False)
        # logger.debug('======<%s>======' % status_list)
        return ret

    @classmethod
    def wrap_sidebar_activity_list(cls, timeout=5, fail_if_false=False):
        logger.debug("____<1.1>____<wrap_sidebar_activity_list>: wrap up message, source, status list of all activities from table of right sidebar ...", also_console=False)
        if ui_lib.is_visible(FusionUIBaseElements.ID_RIGHT_SIDEBAR_TITLE) is False:
            ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_RIGHT_SIDEBAR_ACTIVITY)

        key_list = ['message', 'source', 'status']

        start = datetime.now()
        flag = False
        locator_first_message = FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_MESSAGE
        locator_first_status = FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_STATUS
        locator_first_source = FusionUIBaseElements.ID_TEXT_LIST_SIDEBAR_ACTIVITY_SOURCE
        while (datetime.now() - start).total_seconds() < timeout:
            try:
                if flag is True:
                    logger.debug("____<1.2>____<wrap_sidebar_activity_list>: 'flag' is True, break while-loop", also_console=False)
                    break
                else:
                    if ui_lib.wait_for_element(locator_first_message, timeout=1):
                        logger.debug("_______<1.1.1>_______<wrap_sidebar_activity_list>: first 'message' is found by <%s>" % locator_first_message, also_console=False)
                        if ui_lib.wait_for_element(locator_first_status, timeout=1):
                            logger.debug("_______<1.1.2>_______<wrap_sidebar_activity_list>: first 'status' is found by <%s>" % locator_first_status, also_console=False)
                            if ui_lib.wait_for_element(locator_first_source, timeout=1):
                                logger.debug("_______<1.1.3>_______<wrap_sidebar_activity_list>: first 'source' is found by <%s>" % locator_first_source, also_console=False)
                                flag = True
                            else:
                                logger.debug("_______<1.1.3>_______<wrap_sidebar_activity_list>: first 'source' is NOT found by <%s>" % locator_first_source, also_console=False)
                                continue
                        else:
                            logger.debug("_______<1.1.2>_______<wrap_sidebar_activity_list>: first 'status' is NOT found by <%s>" % locator_first_status, also_console=False)
                            continue
                    else:
                        logger.debug("_______<1.1.1>_______<wrap_sidebar_activity_list>: first 'message' is NOT found by <%s>" % locator_first_message, also_console=False)
                        continue

            except Exception:
                pass

        if flag is False:
            msg = "failed to get the combination of 'message/source/status' elements of the first activity from the sidebar, " \
                  "this may be caused by 'status' element not showing up with in %s second(s)" % timeout
            logger.warn(msg)
            if fail_if_false:
                ui_lib.fail_test(msg)

        logger.debug("____<1.3>____<wrap_sidebar_activity_list>: start to get 3 lists of message/source/status ... ", also_console=False)
        value_message_list = cls.get_sidebar_activity_message_list(fail_if_false=fail_if_false)
        value_source_list = cls.get_sidebar_activity_source_list(fail_if_false=fail_if_false)
        value_status_list = cls.get_sidebar_activity_status_list(fail_if_false=fail_if_false)
        zipped_value_list = zip(value_message_list, value_source_list, value_status_list)
        activity_list = list(dict((key, value) for key, value in zip(key_list, zipped_value)) for zipped_value in zipped_value_list)
        logger.debug("____<1.4>____<wrap_sidebar_activity_list>: wrapped activity list is <%s>" % activity_list, also_console=False)
        return activity_list

    @classmethod
    def get_latest_activity_status(cls, source, message, fail_if_false=False):
        activity_list = cls.wrap_sidebar_activity_list(fail_if_false=fail_if_false)
        status = 'none'
        for activity in activity_list:
            if activity['source'] == source and activity['message'] == message:
                status = activity['status']
                break
        logger.debug("____<2.0>____<get_latest_activity_status>: latest status of ('%s','%s') is <%s>" % (source, message, status), also_console=False)
        return status

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, source, message, timeout=5, fail_if_false=False):
        logger.debug("waiting activity action of resource '%s' change to ok" % source)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            status = cls.get_latest_activity_status(source, message, fail_if_false=fail_if_false)
            if status == 'ok':
                logger.debug("activity action '%s' status is 'ok' as expected." % message)
                return True
            elif status == 'warning':
                logger.debug("activity action '%s' status is 'warning' not as expected." % message)
                ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_RIGHT_SIDEBAR_ACTIVITY % (status, source, message))
                msg = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_ACTIVITY_MESSAGE)
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
            elif status == 'error':
                logger.debug("activity action '%s' status is error not as expected." % message)
                ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_RIGHT_SIDEBAR_ACTIVITY % (status, source, message))
                msg = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_ACTIVITY_MESSAGE)
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
            elif status == 'none':
                logger.debug("activity action '%s' not found yet, waiting ..." % message)
                continue
            else:
                logger.debug("activity action '%s' status is '%s', waiting ..." % (message, status))
                BuiltIn().sleep(3)
                continue
        err_msg = "Timeout for waiting activity action completed in %s second(s)." % timeout
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok_or_warn(cls, source, message, timeout=5, fail_if_false=False):
        logger.debug("waiting activity action of resource '%s' change to ok" % source)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            status = cls.get_latest_activity_status(source, message, fail_if_false=fail_if_false)
            if status == 'ok':
                logger.debug("activity action '%s' status is 'ok' as expected." % message)
                return True
            elif status == 'warning':
                logger.debug("activity action '%s' status is 'warning' as expected." % message)
                ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_RIGHT_SIDEBAR_ACTIVITY % (status, source, message))
                msg = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_ACTIVITY_MESSAGE)
                logger.debug("detailed warning message is: \n[ %s ]" % msg)
                return True
            elif status == 'error':
                logger.debug("activity action '%s' status is error not as expected." % message)
                ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_RIGHT_SIDEBAR_ACTIVITY % (status, source, message))
                msg = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_ACTIVITY_MESSAGE)
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
            elif status == 'none':
                logger.debug("activity action '%s' not found yet, waiting ..." % message)
                continue
            else:
                logger.debug("activity action '%s' status is '%s', waiting ..." % (message, status))
                continue
        err_msg = "Timeout for waiting activity action completed in %s second(s)." % timeout
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_error(cls, source, message, timeout=5, fail_if_false=False):
        logger.debug("waiting activity action of resource '%s' change to error" % source)
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            status = cls.get_latest_activity_status(source, message, fail_if_false=fail_if_false)
            if status == 'error':
                logger.debug("activity action '%s' status is 'error' as expected." % message)
                return True
            elif status == 'warning':
                logger.debug("activity action '%s' status is 'warning' not as expected." % message)
                ui_lib.wait_for_element_and_click(FusionUIBaseElements.ID_RIGHT_SIDEBAR_ACTIVITY % (status, source, message))
                msg = FusionUIBase.get_multi_elements_text(FusionUIBaseElements.ID_TEXT_ACTIVITY_MESSAGE)
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
            elif status == 'ok':
                msg = "activity action '%s' status is ok not as expected." % message
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)
            elif status == 'none':
                logger.debug("activity action '%s' not found yet, waiting ..." % message)
                continue
            else:
                logger.debug("activity action '%s' status is '%s', waiting ..." % (message, status))
                continue
        err_msg = "Timeout for waiting activity action completed in %s second(s)." % timeout
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    def scroll_element_into_viewpoint(cls, locator, align_with_top=False):
        """
            Scrolls an element into viewpoint.
            Because selenium refuse to perform action on hidden element
            This method is usually used to bring element to be visible.
        """
        # TODO: wait element exist
        script = """
            el = arguments[0];
            el.scrollIntoView(%s);
        """ % ("true" if align_with_top else "false")
        counter = 1
        except_obj = None
        while counter <= 3:
            try:
                element = ui_lib.get_s2l()._element_find(locator, first_only=True, required=True)
                ui_lib.get_s2l()._current_browser().execute_script(script, element)
                break
            except StaleElementReferenceException as e:
                continue
        else:
            raise AssertionError("message")

    @classmethod
    def is_test_data_valid(cls, data_value, reference_data_key, fail_if_false=False):
        """
        Date:   2015-04-30
                This is to check if test data given for affinity is in the reference enum values.
                * Set "fail_if_false" = True if this field is required (can't be undefined, or left as blank string)
        :param data_value:
        :type data_value:
        :param reference_data_key:
        :type reference_data_key:
        :param fail_if_false:
        :type fail_if_false:
        :return:
        :rtype:
        """
        if FusionUITestDataValidate.check_enum(data_value, reference_data_key) is True:
            return True
        else:
            msg = "test data '%s' for '%s' is NOT found in reference data, it will be left as default " % (data_value, reference_data_key)
            if fail_if_false:
                logger.warn(msg)
                ui_lib.fail_test(msg)
            else:
                logger.debug(msg)
                return False

    @classmethod
    def fail_test_or_return_false(cls, message, fail_if_false=True):
        logger.warn(message)
        if fail_if_false is True:
            ui_lib.fail_test(message)
        else:
            return False

    @classmethod
    def get_all_error_message_on_form(cls, formid):
        '''
        Function to get all the errors seen on the form

        Input:
            formid   - ID of the form to collect the error messages from . Can be of format 'id=xyz' or 'xyz'
        Return Value:
            List of error messages else returns an empty list
        '''
        # get tableid if in format 'id=xyz'
        search_res = re.search(r"^id=(.*)", formid.replace(' ', ''))
        if search_res is not None:
            formid = search_res.group(1)

        error_elements = []
        error_msg_list = []
        selenium2libObj = ui_lib.get_s2l()
        try:
            error_elements = selenium2libObj._current_browser().find_element_by_id(formid).find_elements_by_class_name("hp-error")
        except (NoSuchElementException, StaleElementReferenceException, ElementNotFoundException) as Ex:
            error_elements = []
        if error_elements:
            logger.warn("Displaying Following errors : ...")
            for errorelement in error_elements:
                if errorelement.text not in (None, ""):
                    logger.warn("Error - '{}' for element : '{}'".format(errorelement.text, errorelement.get_attribute("for")))
                    error_msg_list.append(errorelement.text)
            return error_msg_list
        else:
            return []

    @classmethod
    def get_list_from_data_object(cls, data_obj):
        ret = data_obj
        if isinstance(data_obj, test_data.DataObj):
            ret = [data_obj]
        elif isinstance(data_obj, tuple):
            ret = list(data_obj)

        return ret

    class EditLabels(object):

        e = FusionUIBaseElements

        @classmethod
        def click_labels_panel(cls, timeout=5):
            ui_lib.wait_for_element_and_click(cls.e.ID_LABEL_EDIT_LABELS_LABELS_PANEL, timeout=timeout, fail_if_false=True)

        @classmethod
        def click_edit_link(cls, timeout=5):
            FusionUIBase.wait_for_element_and_click(cls.e.ID_LINK_EDIT_LABELS_EDIT, timeout=timeout, fail_if_false=True, js_click=True)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_dialog_open(cls, timeout=5, fail_if_false=True):
            logger.info("waiting for dialog 'Edit Labels' to open ...")
            if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_LABELS, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Edit Labels' successfully opened")
                return True
            else:
                msg = "failed to wait for dialog 'Edit Labels' to open within %s seconds" % timeout
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        def input_name(cls, name, timeout=5, fail_if_false=True):
            logger.debug("input 'Name' as '%s'" % name)
            ui_lib.wait_for_element_and_input_text(cls.e.ID_INPUT_EDIT_LABELS_NAME, name, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        def click_add_button(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'Add'")
            FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_LABELS_ADD, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

        @classmethod
        def click_remove_icon_of_label(cls, name, timeout=5, fail_if_false=True):
            logger.debug("click 'Remove' icon of label '%s'" % name)
            FusionUIBase.wait_for_element_and_click(cls.e.ID_ICON_EDIT_LABELS_REMOVE % name, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

        @classmethod
        def click_ok_button(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'OK'")
            FusionUIBase.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_LABELS_OK, timeout=timeout, fail_if_false=fail_if_false, js_click=True)

        @classmethod
        def click_cancel_button(cls, timeout=5, fail_if_false=True):
            logger.debug("click button 'Cancel'")
            ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_EDIT_LABELS_CANCEL, timeout=timeout, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def wait_dialog_close(cls, timeout=5, fail_if_false=True):
            logger.debug("waiting for dialog 'Edit Labels' to close ...")
            if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_LABELS, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("dialog 'Edit Labels' successfully closed")
                return True
            else:
                msg = "failed to wait for dialog 'Edit Labels' to close"
                return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def verify_label_should_not_exist(cls, label_name, timeout=5, fail_if_false=True):
            logger.debug("verify Label '%s' should NOT exist ..." % label_name)
            if ui_lib.wait_for_element_notvisible(cls.e.ID_LABEL_EDIT_LABELS_EXISTING_LABEL % label_name, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("Label '%s' is successfully verified as invisible within %s second(s)" % (label_name, timeout))
                return True
            else:
                msg = "Label '%s' is failed to be verified as invisible within %s second(s)" % (label_name, timeout)
                return FusionUIBase.fail_test_or_return_false(message=msg, fail_if_false=fail_if_false)

        @classmethod
        @TakeScreenShotWhenReturnFalseDeco
        def verify_label_should_exist(cls, label_name, timeout=5, fail_if_false=True):
            logger.debug("verify Label '%s' should exist ..." % label_name)
            if ui_lib.wait_for_element_visible(cls.e.ID_LABEL_EDIT_LABELS_EXISTING_LABEL % label_name, timeout=timeout, fail_if_false=fail_if_false):
                logger.debug("Label '%s' is successfully verified as visible within %s second(s)" % (label_name, timeout))
                return True
            else:
                msg = "Label '%s' is failed to be verified as visible within %s second(s)" % (label_name, timeout)
                return FusionUIBase.fail_test_or_return_false(message=msg, fail_if_false=fail_if_false)

    @classmethod
    def edit_labels_of_resources(cls, resource_obj):
        """ Edit Labels Of Resources
            Usage:
                ${data} =       | Get Data By Xpath                     | //LogicalSwitchGroups/EditLabels/resource     | eliminate_same_node=False
                ${result} =     | Fusion UI Edit Labels Of Resources    | @{data.resource}
                Should Be True  | ${result}                             | msg=Failed to edit labels of resources

            Test data example:
                1. data -> LogicalSwitchGroups -> EditLabels, place your RESOURCE list (type="LOGICAL_SWITCH_GROUPS", or others)
                    like below
                2. attribute 'type' for each 'resource' node, the available values are as same as the variable names
                    in class SectionType, like SERVER_PROFILES, SERVER_HARDWARE, LOGICAL_INTERCONNECT_GROUPS, etc., but only
                    for those that support LABEL feature, otherwise keyword will fail since no 'Labels' panel can be reached
                    from the 'View' dropdown at all.
                3. You have to define "eliminate_same_node=False" parameter to keyword "Get Data By Xpath" for loading test data,
                    otherwise the node "Add" or "Remove" will not be located by "Labels.Add" or "Labels.Remove"
                    when there's only ADD items or only REMOVE items defined.


                <EditLabels>
                    <resource name="LSG-CiscoNexus50xx" type="LOGICAL_SWITCH_GROUPS">
                        <Labels>
                            <Add>
                                <label name="Label_A1" />
                                <label name="Label_A2" />
                                <label name="Label_A3" />
                                <label name="Label_A4" />
                            </Add>
                            <Remove>
                                <label name="Label_A1" />
                                <label name="Label_A3" />
                            </Remove>
                        </Labels>
                    </resource>
                    <resource name="LSG-CiscoNexus55xx" type="LOGICAL_SWITCH_GROUPS">
                        <Labels>
                            <Add>
                                <label name="Label_B1" />
                                <label name="Label_B2" />
                            </Add>
                        </Labels>
                    </resource>
                    <resource name="LSG-CiscoNexus50xx">
                        <Labels>
                            <Remove>
                                <label name="Label_A2" />
                                <label name="Label_A4" />
                            </Remove>
                        </Labels>
                    </resource>
                </EditLabels>
        """

        resource_type_mapping = {s[0]: s[1] for s in inspect.getmembers(SectionType)}

        total = len(resource_obj)
        edited = 0
        not_exists = 0

        for n, res in enumerate(resource_obj):
            logger.info("{2} <Editing labels> No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
            logger.info("editing labels for a {} with name '{}' ...".format(res.type, res.name))
            # checking if the resource is already existing
            FusionUIBase.navigate_to_section(resource_type_mapping[res.type], time_for_loading=3)
            if not cls.verify_item_should_exist_in_master_table(res.name, item_type=res.type, fail_if_false=False):
                logger.warn("{} '{}' does NOT exist!".format(res.type, res.name))
                not_exists += 1
                continue

            cls.click_item_from_master_table(res.name)
            FusionUIBase.select_view_by_name(view_name='Labels', timeout=5, fail_if_false=False)

            if getattr(res, 'Labels', None):
                cls.EditLabels.click_labels_panel()
                cls.EditLabels.click_edit_link()
                cls.EditLabels.wait_dialog_open()
                if getattr(res.Labels, 'Add', None):
                    for i, label in enumerate(res.Labels.Add.label):
                        logger.info("{2} <Adding labels> No: {0} ... Total: {1} {2}".format((i + 1), len(res.Labels.Add.label), '.' * 14))
                        if cls.EditLabels.verify_label_should_not_exist(label_name=label.name, fail_if_false=False):
                            cls.EditLabels.input_name(label.name)
                            cls.EditLabels.click_add_button()

                if getattr(res.Labels, 'Remove', None):
                    for i, label in enumerate(res.Labels.Remove.label):
                        logger.info("{2} <Removing labels> No: {0} ... Total: {1} {2}".format((i + 1), len(res.Labels.Remove.label), '.' * 14))
                        if cls.EditLabels.verify_label_should_exist(label_name=label.name, fail_if_false=False):
                            cls.EditLabels.click_remove_icon_of_label(name=label.name)

                cls.EditLabels.click_ok_button()

                status, msg = FusionUIBase.get_error_message_from_dialog(timeout=10)
                if status is True:
                    logger.warn("unexpected error occurred: %s" % msg)
                    ui_lib.fail_test(msg)

                if cls.EditLabels.wait_dialog_close(timeout=10, fail_if_false=False) is True:
                    FusionUIBase.show_activity_sidebar()
                    if FusionUIBase.wait_activity_action_ok(res.name, 'Update Labels', timeout=10, fail_if_false=False) is True:
                        FusionUIBase.show_activity_sidebar()
                        logger.info("successfully edited labels for '%s'" % res.name)
                        edited += 1
                    else:
                        logger.warn("'wait_activity_action_ok' = FALSE, skip to next Logical Switch Group ... ")
                        FusionUIBase.show_activity_sidebar()
                        continue
                else:
                    logger.warn("'FusionUIBase.EditLabels.wait_dialog_close' = FALSE, skip to next Logical Switch Group ... ")
                    cls.EditLabels.click_cancel_button()
                    continue

            else:
                ui_lib.fail_test("node 'Labels' not found in test data under node 'resource'!")

            edited += 1

        logger.info("{0} == Summary == {0}".format('-' * 14))
        if total - not_exists == 0:
            logger.warn("no resource to edit! all %s resource(s) is NOT existing, test is considered FAIL" % not_exists)
            return False
        else:
            if edited < total:
                logger.warn("not all of the resource(s) is successfully edited - %s out of %s edited " % (edited, total))
                if edited + not_exists == total:
                    logger.warn("%s non-existing resource(s) is skipped, test is considered FAIL" % not_exists)
                    return False
                else:
                    ui_lib.fail_test("%s non-existing resource(s) is skipped, %s resource(s) left is failed being edited " % (not_exists, total - edited - not_exists))
            else:
                logger.info("all of the resource(s) is successfully edited - %s out of %s " % (edited, total))
                return True

        return True
