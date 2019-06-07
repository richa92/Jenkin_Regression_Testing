# (C) Copyright 2019 Hewlett-Packard Enterprise Company, L.P.
"""
    Storage System Page
"""
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.storagesystems_elements import GeneralStorageSystemElements
from FusionLibrary.ui.business_logic.storage.storagesystems_elements import AddStorageSystemElements
from FusionLibrary.ui.business_logic.storage.storagesystems_elements import EditStorageSystemElements
from FusionLibrary.ui.business_logic.storage.storagesystems_elements import RemoveStorageSystemElements
from FusionLibrary.ui.business_logic.storage.storagesystems_elements import RefreshStorageSystemElements
from FusionLibrary.ui.business_logic.storage.storagesystems_elements import EditStorageSystemCredentialsElements
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import FusionUIConst
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime
import time


class CommonOperationStorageSystems(object):
    """
        Common Operations for Storage System
    """
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_not_exist(cls, storage_system, timeout=5, fail_if_false=True):
        """
            Verify that the storage system does not exist
        """
        logger.debug("verify storage system '%s' is not existing" % storage_system)
        if ui_lib.wait_for_element_notvisible(GeneralStorageSystemElements.ID_TABLE_STORAGE_SYSTEM % storage_system, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_exist(cls, storage_system, timeout=5, fail_if_false=True):
        """
            Verify that the storage system does exist
        """
        logger.debug("verify storage system '%s' is existing" % storage_system)
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_TABLE_STORAGE_SYSTEM % storage_system, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_locate_error_exists(cls, timeout=5, fail_if_false=True):
        """
            Verify that a locate error exists
        """
        locateerror = "Unable to locate the item you requested."
        logger.debug("verify if '%s' error exists on the screen" % locateerror)
        if ui_lib.is_visible(GeneralStorageSystemElements.UNABLE_TO_LOCATE_ERROR % locateerror, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_status_ok(cls, storage_system, timeout=5, fail_if_false=True):
        """
            Verify that the storage system status is OK
        """
        logger.debug("verify whether storage system %s is ok" % storage_system)
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_OK % storage_system, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_status_warn(cls, storage_system, timeout=5, fail_if_false=True):
        """
            Verify that the storage system status is a warn
        """
        logger.debug("verify whether storage system %s is warning" % storage_system)
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_WARN % storage_system, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_status_error(cls, storage_system, timeout=5, fail_if_false=True):
        """
            Verify that the storage system status is an error or not
        """
        logger.debug("verify whether storage system %s is error" % storage_system)
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_ERROR % storage_system, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_storage_system_list(cls, timeout=5):
        """
            Get all storage system names from table
        """
        logger.debug("get all storage system names from table")
        storage_system_list = []
        if ui_lib.wait_for_element(GeneralStorageSystemElements.ID_TABLE_STORAGE_SYSTEMS, timeout):
            storage_system_list = FusionUIBase.get_multi_elements_text(GeneralStorageSystemElements.ID_TABLE_STORAGE_SYSTEMS, timeout, fail_if_false=True)
        return storage_system_list

    @classmethod
    def click_storage_system(cls, storage_name, timeout=5):
        """
            Select a specific storage system name
        """
        logger.debug("select storage system %s" % storage_name)
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_TABLE_STORAGE_SYSTEM % storage_name, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_system_selected(cls, storage_name, timeout=5, fail_if_false=True):
        """
            Wait till a specific storage system is selected
        """
        logger.debug("waiting for storage system '%s' is selected" % storage_name)
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_TABLE_STORAGE_SYSTEM_SELECTED % storage_name, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_action_button(cls, timeout=5):
        """
            Click action button on the storage system page
        """
        logger.debug("click action button")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_ongoing_disappear(cls, timeout=10, fail_if_false=True):
        """
            Wait until the progress disappears from the storage system page
        """
        logger.debug("waiting for progress bar indicates to 'complete'")
        if ui_lib.wait_for_element_remove(GeneralStorageSystemElements.ID_STATUS_NOTIFICATION_ONGOING, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_ok_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait until progress bar shows OK on storage system page
        """
        logger.debug("waiting for progress bar indicates to 'ok'")
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_NOTIFICATION_OK, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_warn_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait until progress bar shows WARN on storage system page
        """
        logger.debug("waiting for progress bar indicates to 'warn'")
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_NOTIFICATION_WARN, timeout, fail_if_false):
            cls.get_notification_message()
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_ok_or_warn_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait until progress bar shows OK or WARN on storage system page
        """
        logger.debug("waiting for progress bar indicates to 'ok' or 'warn'")
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_NOTIFICATION_OK, timeout, fail_if_false=False):
            return True
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_NOTIFICATION_WARN, timeout, fail_if_false):
            cls.get_notification_message()
            return True
        else:
            cls.get_notification_message(log_prefix='_warn')
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_error_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait until progress bar shows ERROR on storage system page
        """
        logger.debug("waiting for progress bar indicates to error")
        if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_NOTIFICATION_ERROR, timeout, fail_if_false):
            cls.get_notification_message()
            return True
        else:
            return False

    @classmethod
    def get_notification_message(cls, log_prefix="_debug", timeout=5):
        """
            Get notification message from storage system page
        """
        msg = FusionUIBase.get_text(GeneralStorageSystemElements.ID_TEXT_NOTIFICATION_MESSAGE, timeout)
        resolution = FusionUIBase.get_text(GeneralStorageSystemElements.ID_TEXT_NOTIFICATION_RESOLUTION, timeout)
        if log_prefix == "_warn":
            logger.debug('Message: %s \nResolution: %s' % (msg, resolution))
        else:
            logger.warn('Message: %s \nResolution: %s' % (msg, resolution))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_system_status_ok(cls, storage_system, timeout=10, fail_if_false=True):
        """
            Wait until status = OK on storage system page
        """
        start = datetime.now()
        logger.debug("waiting for storage system '%s' status indicates to ok" % storage_system)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_OK % storage_system, timeout=2, fail_if_false=False):
                logger.debug("storage system '%s' status is ok as expected." % storage_system)
                return True
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_WARN % storage_system, timeout=2, fail_if_false=False):
                err_msg = "storage system '%s' status is warning not as expected." % storage_system
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_ERROR % storage_system, timeout=2, fail_if_false=False):
                err_msg = "storage system '%s' status is error not as expected." % storage_system
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("storage system status is unknown, waiting ...")
                continue
        err_msg = "Timeout to wait for storage system '%s' status indicates to ok." % storage_system
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_system_status_ok_or_warn(cls, storage_system, timeout=10, fail_if_false=True):
        """
            Wait until status = OK or WARN on storage system page
        """
        start = datetime.now()
        logger.debug("waiting for storage system '%s' status indicates to ok or warning" % storage_system)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_OK % storage_system, timeout=5, fail_if_false=False):
                logger.debug("storage system '%s' status is ok as expected." % storage_system)
                return True
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_WARN % storage_system, timeout=5, fail_if_false=False):
                logger.debug("storage system '%s' status is warning as expected." % storage_system)
                return True
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_ERROR % storage_system, timeout=5, fail_if_false=False):
                err_msg = "storage system '%s' status is error not as expected." % storage_system
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("storage system '%s' status is unknown, waiting ..." % storage_system)
                continue
        err_msg = "Timeout to wait for storage system '%s' status indicates to ok or warn." % storage_system
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_system_status_error(cls, storage_system, timeout=10, fail_if_false=True):
        """
            Wait until status = ERROR on storage system page
        """
        start = datetime.now()
        logger.debug("waiting for storage system '%s' status indicates to error" % storage_system)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_OK % storage_system, timeout=5, fail_if_false=False):
                err_msg = "storage system '%s' status is ok not as expected." % storage_system
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_WARN % storage_system, timeout=5, fail_if_false=False):
                logger.debug("storage system '%s' status is warning not as expected." % storage_system)
                return False
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_STATUS_STORAGE_SYSTEM_ERROR % storage_system, timeout=5, fail_if_false=False):
                logger.debug("storage system '%s' status is error as expected." % storage_system)
                return True
            else:
                logger.debug("storage system '%s' status is unknown, waiting ..." % storage_system)
                continue
        err_msg = "Timeout to wait for storage system status indicates to error."
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, storage_system, timeout=5, fail_if_false=True):
        """
            Wait until activity action completes on storage system page
        """
        logger.debug("wait activity action completed")
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            actionname = ""

            if ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_OK % storage_system, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_TITLE % storage_system)
                logger.debug("activity action '%s' status is ok" % actionname)
                return True
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_WARN % storage_system, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_TITLE % storage_system)
                logger.debug("activity action '%s' status is warn" % actionname)
                ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_WARN % storage_system)
                msg = FusionUIBase.get_multi_elements_text(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_MESSAGE)
                logger.warn(msg)
                return False
            elif ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_ERROR % storage_system, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_TITLE % storage_system)
                logger.debug("activity action '%s' status is error" % actionname)
                ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_ACTION_ERROR % storage_system)
                msg = FusionUIBase.get_multi_elements_text(GeneralStorageSystemElements.ID_TEXT_ACTIVITY_MESSAGE)
                logger.warn(msg)
                return False
            else:
                logger.debug("activity action '%s' status is unknown" % actionname)
                continue

        err_msg = "Timeout for waiting for activity of Storage System [ %s ] change to [ ok ]." % storage_system
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_system_volumes_link(cls, timeout=5):
        """
            Click link on storage system page for volumes
        """
        logger.debug("Click storage system volumes link")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_LINK_STORAGE_VOLUMES, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_system_pools_link(cls, timeout=5):
        """
            Click link on storage system page for pools
        """
        logger.debug("Click storage system pools link")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_LINK_STORAGE_POOLS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_volumesets_link(cls, timeout=5):
        """
            Click link on storage system page for volumesets
        """
        logger.debug("Click volumesets link")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_LINK_VOLUME_SETS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_network_link(cls, timeout=5):
        """
            Click link on storage system page for networks
        """
        logger.debug("Click storage system network link")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_LINK_NETWORKS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_sans_link(cls, timeout=5):
        """
            Click link on storage system page for SANS
        """
        logger.debug("Click sans_link")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_LINK_SANS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_system_page_title(cls, system, timeout=10, fail_if_false=True):
        """
            Verify storage system page title
        """
        logger.info('verifying [ Storage System page title= %s ] is visible' % system)
        ui_lib.wait_for_element(GeneralStorageSystemElements.ID_PAGE_LABEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def determine_element_to_use(cls, system_type, action):
        """
            Given the system type, determine the elements to use
        """
        logger.info('Determine system for %s' % action)
        storage_system_element_map = {
            FusionUIConst.CONST_STORAGE_SYSTEM_TYPE_STORESERV.lower(): {
                "input_ip_address_or_host_name": AddStorageSystemElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME,
                "input_user_name": AddStorageSystemElements.ID_INPUT_USER_NAME,
                "input_password": AddStorageSystemElements.ID_INPUT_PASSWORD
            },
            FusionUIConst.CONST_STORAGE_SYSTEM_TYPE_STOREVIRTUAL.lower(): {
                "input_ip_address_or_host_name": AddStorageSystemElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME_VIRTUAL,
                "input_user_name": AddStorageSystemElements.ID_INPUT_USER_NAME_VIRTUAL,
                "input_password": AddStorageSystemElements.ID_INPUT_PASSWORD_VIRTUAL
            },
            FusionUIConst.CONST_STORAGE_SYSTEM_TYPE_NIMBLE.lower(): {
                "input_ip_address_or_host_name": AddStorageSystemElements.ID_INPUT_IP_ADDRESS_OR_HOST_NAME_NSA,
                "input_user_name": AddStorageSystemElements.ID_INPUT_USER_NAME_NSA,
                "input_password": AddStorageSystemElements.ID_INPUT_PASSWORD_NSA
            }
        }

        element = storage_system_element_map[system_type.lower()][action]
        return element


class AddStorageSystems(object):
    """
        Add Storage System dialog
    """

    @classmethod
    def click_add_storage_system_button(cls, timeout=5):
        """
            Click link on storage system page for networks
        """
        logger.debug("click add storage system button")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_ADD_STORAGE_SYSTEM, timeout, fail_if_false=True)

    @classmethod
    def select_actions_add(cls, timeout=5):
        """
            Select add from action menu on storage system page
        """
        logger.debug("select add")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_ACTION_ADD, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_storage_system_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Add Storage System dialog to appear
        """
        logger.debug("waiting for add storage system dialog to show up")
        if ui_lib.wait_for_element_visible(AddStorageSystemElements.ID_DIALOG_ADD_STORAGE_SYSTEM, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def select_storage_system_type_by_text(cls, storage_system_type, timeout=5, fail_if_false=True):
        """
            On the Add Storage System dialog, select type of storage system by text
        """
        logger.debug("validating test data '%s' for 'Storage System Type' ..." % storage_system_type)
        if FusionUIBase.is_test_data_valid(storage_system_type, 'SAN_Storage_System_Type', fail_if_false=False):
            logger.debug("select 'Storage system type' as '%s' ..." % storage_system_type)
            return FusionUIBase.choose_option_by_text(AddStorageSystemElements.ID_SELECT_STORAGE_SYSTEM_TYPE, storage_system_type, timeout=timeout, fail_if_false=fail_if_false)
        else:
            msg = "<test data invalid> '%s' for 'Storage System Type' is NOT valid" % storage_system_type
            return FusionUIBase.fail_test_or_return_false(msg)

    @classmethod
    def input_ip_address_or_host_name(cls, host, storage_system_type, timeout=5):
        """
            On the Add Storage System dialog, input host name or ip address
        """
        logger.debug("input '%sIP address or hostname' as '%s'" % ('Cluster ' if storage_system_type.lower() == FusionUIConst.CONST_STORAGE_SYSTEM_TYPE_STOREVIRTUAL.lower() else '', host))
        ui_lib.fail_test("<test data invalid> given value '%s' of parameter 'storage_system_type' is INVALID, please correct it according to actual UI page" % storage_system_type) if not FusionUIBase.is_test_data_valid(storage_system_type, 'SAN_Storage_System_Type', fail_if_false=False) else None
        locator = CommonOperationStorageSystems.determine_element_to_use(storage_system_type, "input_ip_address_or_host_name")
        ui_lib.wait_for_element_and_input_text(locator, host, timeout, fail_if_false=True)

    @classmethod
    def input_user_name(cls, name, storage_system_type, timeout=5):
        """
            On the Add Storage System dialog, input user name
        """
        logger.debug("input 'User name' as '%s'" % name)
        ui_lib.fail_test("<test data invalid> given value '%s' of parameter 'storage_system_type' is INVALID, please correct it according to actual UI page" % storage_system_type) if not FusionUIBase.is_test_data_valid(storage_system_type, 'SAN_Storage_System_Type', fail_if_false=False) else None
        locator = CommonOperationStorageSystems.determine_element_to_use(storage_system_type, "input_user_name")
        ui_lib.wait_for_element_and_input_text(locator, name, timeout, fail_if_false=True)

    @classmethod
    def input_password(cls, password, storage_system_type, timeout=5):
        """
            On the Add Storage System dialog, input password
        """
        logger.debug("input 'Password' as '%s'" % password)
        ui_lib.fail_test("<test data invalid> given value '%s' of parameter 'storage_system_type' is INVALID, please correct it according to actual UI page" % storage_system_type) if not FusionUIBase.is_test_data_valid(storage_system_type, 'SAN_Storage_System_Type', fail_if_false=False) else None
        locator = CommonOperationStorageSystems.determine_element_to_use(storage_system_type, "input_password")
        ui_lib.wait_for_element_and_input_text(locator, password, timeout, fail_if_false=True)

    @classmethod
    def click_connect_button(cls, timeout=5):
        """
            On the Add Storage System dialog, click the connect button
        """
        logger.debug('click connect button')
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_CONNECT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_connected_to_storage_system(cls, timeout=40, fail_if_false=True):
        """
            On the Add Storage System dialog, wait until the message connected to the system appears
        """
        logger.debug('wait connected to storage system')
        if ui_lib.wait_for_element_visible(AddStorageSystemElements.ID_TEXT_CONNECTED_STORAGE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_select_storage_domain(cls, storage_domain, timeout=5, fail_if_false=True):
        """
            On the Add Storage System dialog, input domain
        """
        logger.debug("input storage domain '%s'" % storage_domain)
        ui_lib.wait_for_element_and_input_text(AddStorageSystemElements.ID_INPUT_STORAGE_DOMAIN, storage_domain, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_STORAGE_DOMAIN % storage_domain, timeout, fail_if_false)

    @classmethod
    def select_storage_credentials_section(cls, timeout=5):
        """
            On the Add Storage System dialog, input credentials
        """
        logger.debug("select credentials section")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_PANEL_CREDENTIALS, timeout, fail_if_false=True)

    @classmethod
    def select_storage_general_section(cls, timeout=5):
        """
            On the Add Storage System dialog, select the General section of the page
        """
        logger.debug("select general section")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_PANEL_GENERAL, timeout, fail_if_false=True)

    @classmethod
    def select_storage_pools_section(cls, timeout=5):
        """
            On the Add Storage System dialog, select the Storage Pools section of the page
        """
        logger.debug("select storage pools section")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_PANEL_STORAGE_POOLS, timeout, fail_if_false=True)

    @classmethod
    def click_add_storage_pools_button(cls, timeout=5):
        """
            On the Add Storage System dialog, click the add storage pools button
        """
        logger.debug("click add storage pools button")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_ADD_STORAGE_POOLS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_storage_pools_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
            On the Add Storage System dialog, wait until the Add storage pool dialog is shown
        """
        logger.debug("waiting for add storage pools dialog to show up")
        if ui_lib.wait_for_element_visible(AddStorageSystemElements.ID_DIALOG_ADD_STORAGE_POOLS, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_select_storage_pool(cls, storage_pool, timeout=5, fail_if_false=True):
        """
            On the Add Storage System dialog, select the storage pool
        """
        logger.debug("input storage pool '%s'" % storage_pool)
        ui_lib.wait_for_element_and_input_text(AddStorageSystemElements.ID_INPUT_STORAGE_POOL, storage_pool, timeout, fail_if_false)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_STORAGE_POOL % storage_pool, timeout, fail_if_false)

    @classmethod
    def set_manage_option_for_pools(cls, pools, system, timeout=5, fail_if_false=True):
        """
            On the storage pools dialog, set the pool to managed
        """
        logger.debug("set 'Manage' option for storage pools '%s'" % pools)
        done_set = 0
        for n, pool in enumerate(pools):  # pylint: disable=W0612
            manage = True if getattr(pool, 'Manage', '').lower() == 'true' else False
            logger.debug("%stick 'Manage' checkbox for storage pool '%s' as test data attribute 'Manage' is '%s'" % ('' if manage else 'un', pool.name, pool.Manage))
            if system.lower() == FusionUIConst.CONST_STORAGE_SYSTEM_TYPE_STORESERV.lower():
                locator = AddStorageSystemElements.ID_CHECKBOX_MANAGE_STORAGE_POOL % pool.name
            else:
                locator = AddStorageSystemElements.ID_CHECKBOX_SELECT_STORAGE_POOL % pool.name         # nimble pools
            FusionUIBase.scroll_element_into_viewpoint(locator)
            ret = FusionUIBase.wait_for_checkbox_and_select(locator, timeout=timeout, fail_if_false=fail_if_false) if manage else FusionUIBase.wait_for_checkbox_and_unselect(locator, timeout=time, fail_if_false=fail_if_false)
            done_set += 1 if ret else None

        if done_set == len(pools):
            logger.debug("all %s storage pool(s) have been set for 'Manage' options" % done_set)
            return True
        else:
            msg = "not all the storage pool(s) have been set for 'Manage' options, %s of %s failed to be set" % (len(pools) - done_set, len(pools))
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def click_storage_pools_select_all_button(cls, timeout=5):
        """
            On the Add Storage System dialog, click the select all storage pools button
        """
        logger.debug("click 'Select all' button to tick 'Manage' checkbox for all storage pools")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_STORAGE_POOL_SELECT_ALL, timeout, fail_if_false=True)

    @classmethod
    def click_storage_pools_deselect_all_button(cls, timeout=5):
        """
            On the Add Storage System dialog, click the deselect all storage pools button
        """
        logger.debug("click 'Deselect all' button to untick 'Manage' checkbox for all storage pools")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_STORAGE_POOL_DESELECT_ALL, timeout, fail_if_false=True)

    @classmethod
    def click_storage_pools_confirm_add_button(cls, timeout=5):
        """
            On the storage pools dialog, click the confirm add button
        """
        logger.debug("click 'add' button to confirm add storage pool")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_STORAGE_POOL_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_storage_pools_confirm_add_plus_button(cls, timeout=5):
        """
            On the storage pools dialog, click the confirm add plus button
        """
        logger.debug("click 'add+' button to confirm add storage pool")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_STORAGE_POOL_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_storage_pools_cancel_button(cls, timeout=5):
        """
            On the storage pools dialog, click the cancel button
        """
        logger.debug("click 'cancel' to cancel add storage pool")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_STORAGE_POOL_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_storage_pools_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Add Storage Pools Dialog to disappear
        """
        logger.debug("waiting for add storage pools dialog to disappear")
        if ui_lib.wait_for_element_notvisible(AddStorageSystemElements.ID_DIALOG_ADD_STORAGE_POOLS, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def select_storage_system_ports_section(cls, timeout=5):
        """
            On the Add Storage System dialog, select the Ports Section
        """
        logger.debug("select storage system port section")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_DROPDOWN_PANEL_SELECTOR, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_PANEL_STORAGE_SYSTEM_PORTS, timeout, fail_if_false=True)

    @classmethod
    def select_vipnetwork(cls, vipnetwork, timeout=10, fail_if_false=True):
        """
            On the Add Storage System dialog, select the vip network
        """
        logger.debug("Selecting VIP network : {}".format(vipnetwork))
        ui_lib.wait_for_element_and_input_text(AddStorageSystemElements.ID_INPUT_VIPNETWORK, vipnetwork, timeout,
                                               fail_if_false)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_OPTION_VIPNETWORK % vipnetwork, timeout,
                                          fail_if_false)

    @classmethod
    def input_select_expected_san_network_and_port_group(cls, port, san_or_network, port_group='Auto', timeout=5):
        """
            On the Add Storage System dialog, input value for expected san network and port group
        """
        logger.debug("port: %s; expected SAN or network: %s; port_group: %s. " % (port, san_or_network, port_group))
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_CLOSE_EXPECTED_SAN_OR_NETWORK % port, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_input_text(AddStorageSystemElements.ID_INPUT_EXPECTED_SAN_OR_NETWORK % port, san_or_network, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_EXPECTED_SAN_OR_NETWORK % (port, san_or_network), timeout=10, fail_if_false=True)
        ui_lib.wait_for_element_and_input_text(AddStorageSystemElements.ID_INPUT_PORT_GROUP % port, port_group, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_SELECT_PORT_GROUP % (port, port_group), timeout, fail_if_false=True)

    @classmethod
    def click_add_button(cls, timeout=5):
        """
            On the Add Storage System dialog, click add button
        """
        logger.debug("click add button")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_ADD, timeout, fail_if_false=True)

    @classmethod
    def click_add_plus_button(cls, timeout=5):
        """
            On the Add Storage System dialog, click add plus button
        """
        logger.debug("click add+ button")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_ADD_PLUS, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        """
            On the Add Storage System dialog, click cancel button
        """
        logger.debug("click cancel button")
        ui_lib.wait_for_element_and_click(AddStorageSystemElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_add_storage_system_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Add Storage System dialog to disappear
        """
        logger.debug("waiting for add storage system dialog to disappear")
        if ui_lib.wait_for_element_notvisible(AddStorageSystemElements.ID_DIALOG_ADD_STORAGE_SYSTEM, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_message_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait for the adding message to appear on the screen
        """
        logger.debug("waiting for adding storage system message to show up")
        if ui_lib.wait_for_element_visible(AddStorageSystemElements.ID_TEXT_ADDING_STORAGE_SYSTEM, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_adding_message_disappear(cls, timeout=5, fail_if_false=True):
        """
            Wait for the adding message to disappear from the screen
        """
        logger.debug("waiting for adding storage system message to disappear")
        if ui_lib.wait_for_element_notvisible(AddStorageSystemElements.ID_TEXT_ADDING_STORAGE_SYSTEM, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_add_storage_system_error(cls, expect_value, timeout=5, fail_if_false=True):
        """
            Verify add storage system error
        """
        logger.debug("verify [ Storage System Error ] in general view, expected value is [ %s ] " % expect_value)
        return FusionUIBase.verify_element_text("Type", AddStorageSystemElements.ID_TEXT_ADD_ERROR_MESSAGE, expect_value, timeout, fail_if_false)


class EditStorageSystems(object):
    """
        Edit Storage System dialog
    """

    @classmethod
    def select_actions_edit(cls, timeout=5):
        """
            On the Storage System screen, select the edit action in the action menu
        """
        logger.debug("select edit")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditStorageSystemElements.ID_SELECT_ACTION_EDIT, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Edit Storage System dialog to appear
        """
        logger.debug("waiting for edit dialog to show up")
        if ui_lib.wait_for_element_visible(EditStorageSystemElements.ID_DIALOG_EDIT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_select_expected_san_network_and_port_group(cls, port, san_or_network, port_group='Auto', timeout=8):
        """
            On the Edit Storage System dialog, input the expected san netowrk and port group
        """
        logger.debug("port: %s; expected SAN or network: %s; port_group: %s. " % (port, san_or_network, port_group))
        ui_lib.wait_for_element_and_input_text(EditStorageSystemElements.ID_INPUT_EXPECTED_SAN_OR_NETWORK, san_or_network, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_input_text(EditStorageSystemElements.ID_INPUT_PORT_GROUP, port_group, timeout, fail_if_false=True)

    @classmethod
    def select_vipnetwork(cls, vipnetwork, timeout=10, fail_if_false=True):
        """
            On the Edit Storage System dialog, select the vipnetwork
        """
        logger.debug("Selecting VIP network : {}".format(vipnetwork))
        ui_lib.wait_for_element_and_input_text(EditStorageSystemElements.ID_INPUT_VIPNETWORK, vipnetwork, timeout,
                                               fail_if_false)
        ui_lib.wait_for_element_and_click(EditStorageSystemElements.ID_OPTION_VIPNETWORK % vipnetwork, timeout,
                                          fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        """
            On the Edit Storage System dialog, click the OK button
        """
        logger.debug("click 'ok' button")
        ui_lib.wait_for_element_and_click(EditStorageSystemElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        """
            On the Edit Storage System dialog, click the cancel button
        """
        logger.debug("click 'cancel' button")
        ui_lib.wait_for_element_and_click(EditStorageSystemElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Edit Storage System dialog to disappear
        """
        logger.debug("waiting for edit dialog to disappear")
        if ui_lib.wait_for_element_notvisible(EditStorageSystemElements.ID_DIALOG_EDIT, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_edit_storage_system_error(cls, expect_value, timeout=5, fail_if_false=True):
        """
            Verify the Edit Storage System has an error
        """
        logger.debug("verify [ Type ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Type", EditStorageSystemElements.ID_TEXT_EDIT_ERROR_MESSAGE, expect_value, timeout, fail_if_false)


class RemoveStorageSystems(object):
    """
        Remove Storage System dialog
    """

    @classmethod
    def select_actions_remove(cls, timeout=5):
        """
            On the Storage System Page, click the action menu remove link
        """
        logger.debug("select remove")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RemoveStorageSystemElements.ID_SELECT_ACTION_REMOVE, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait for the remove system dialog page to appear
        """
        logger.debug("waiting for remove dialog to show up")
        if ui_lib.wait_for_element_visible(RemoveStorageSystemElements.ID_DIALOG_REMOVE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_yes_remove_button(cls, timeout=5):
        """
            On the Remove Storage System dialog, click the yes, remove button
        """
        logger.debug("click 'yes, remove'")
        ui_lib.wait_for_element_and_click(RemoveStorageSystemElements.ID_BUTTON_YES_REMOVE, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        """
            On the Remove Storage System dialog, click the cancel button
        """
        logger.debug("click 'cancel'")
        ui_lib.wait_for_element_and_click(RemoveStorageSystemElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_remove_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Remove Storage System dialog to disappear
        """
        logger.debug("waiting for remove dialog to disappear")
        if ui_lib.wait_for_element_notvisible(RemoveStorageSystemElements.ID_DIALOG_REMOVE, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_system_show_not_found(cls, storagesystem, timeout=7, fail_if_false=True):
        """
            Wait for the Storage System Page to show that the storage system status is "not found"
        """
        logger.info("waiting for storage system status indicates to 'not found'")
        if ui_lib.wait_for_element_visible(RemoveStorageSystemElements.ID_TABLE_STORAGE_SYSTEM_DELETED % storagesystem, timeout, fail_if_false):
            return True
        else:
            return False


class RefreshStorageSystems(object):
    """
        Refresh Storage System dialog
    """

    @classmethod
    def select_actions_refresh(cls, timeout=5):
        """
            On the Storage System Page, select action menu refresh link
        """
        logger.debug("select refresh")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RefreshStorageSystemElements.ID_SELECT_ACTION_REFRESH, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_state_refreshing(cls, timeout=5, fail_if_false=True):
        """
            On the Storage System page, wait for message that the storage system is refreshing
        """
        logger.debug("waiting for general state indicates to refreshing")
        ui_lib.wait_for_element_text(GeneralStorageSystemElements.ID_TEXT_GENERAL_STATE, "Refreshing", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_state_configured(cls, timeout=5, fail_if_false=True):
        """
            On the Storage System page, wait for message that the storage system is configured
        """
        logger.debug("waiting for general state indicates to configured")
        ui_lib.wait_for_element_text(GeneralStorageSystemElements.ID_TEXT_GENERAL_STATE, "Configured", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storeserv_state_managed(cls, timeout=5, fail_if_false=True):
        """
            On the Storage System page, wait for message that the StoreServ storage system is managed
        """
        logger.debug("waiting for general state indicates to configured")
        ui_lib.wait_for_element_text(GeneralStorageSystemElements.ID_TEXT_GENERAL_STATE_STORESERV, "Managed", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storevirtual_state_managed(cls, timeout=5, fail_if_false=True):
        """
            On the Storage System page, wait for message that the StoreVirtual storage system is managed
        """
        logger.debug("waiting for general state indicates to configured")
        ui_lib.wait_for_element_text(GeneralStorageSystemElements.ID_TEXT_GENERAL_STATE_STOREVIRTUAL, "Managed", timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_nimble_state_managed(cls, timeout=5, fail_if_false=True):
        """
            On the Storage System page, wait for message that the Nimble storage system is managed
        """
        logger.debug("waiting for general state indicates to configured")
        ui_lib.wait_for_element_text(GeneralStorageSystemElements.ID_TEXT_GENERAL_STATE_NIMBLE, "Managed", timeout, fail_if_false)


class EditStorageSystemCredentials(object):
    """
        Edit Storage System Credentials dialog
    """

    @classmethod
    def select_actions_edit_credentials(cls, timeout=5):
        """
            On the Storage System page, select action menu edit credentials link
        """
        logger.debug("select edit credentials")
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_DROPDOWN_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(EditStorageSystemCredentialsElements.ID_SELECT_ACTION_EDIT_CREDENTIALS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_credentials_dialog_shown(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Edit Credentials Dialog to appear
        """
        logger.debug("waiting for edit credentials dialog to show up")
        if ui_lib.wait_for_element_visible(EditStorageSystemCredentialsElements.ID_DIALOG_EDIT_CREDENTIALS, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def input_ip_address_or_host_name(cls, hostname, timeout=5):
        """
            On the Edit Credentials Dialog, input the ip address or host name
        """
        logger.debug("input ip address or host name '%s'" % hostname)
        ui_lib.wait_for_element_and_input_text(EditStorageSystemCredentialsElements.ID_INPUT_IP_HOSTNAME, hostname, timeout, fail_if_false=True)

    @classmethod
    def input_user_name(cls, username, timeout=5):
        """
            On the Edit Credentials Dialog, input the user name
        """
        logger.debug("input user name '%s'" % username)
        ui_lib.wait_for_element_and_input_text(EditStorageSystemCredentialsElements.ID_INPUT_USERNAME, username, timeout, fail_if_false=True)

    @classmethod
    def input_password(cls, password, timeout=5):
        """
            On the Edit Credentials Dialog, input the password
        """
        logger.debug("input password '******'")
        ui_lib.wait_for_element_and_input_text(EditStorageSystemCredentialsElements.ID_INPUT_PASSWORD, password, timeout, fail_if_false=True)

    @classmethod
    def click_ok(cls, timeout=5):
        """
            On the Edit Credentials Dialog, click the ok button
        """
        logger.debug("click ok")
        ui_lib.wait_for_element_and_click(EditStorageSystemCredentialsElements.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel(cls, timeout=5):
        """
            On the Edit Credentials Dialog, click the cancel button
        """
        logger.debug("click cancel")
        ui_lib.wait_for_element_and_click(EditStorageSystemCredentialsElements.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_credentials_dialog_disappear(cls, timeout=5, fail_if_false=True):
        """
            Wait for the Edit Credentials Dialog to disappear
        """
        logger.debug("waiting for edit credentials dialog to disappear")
        if ui_lib.wait_for_element_notvisible(EditStorageSystemCredentialsElements.ID_DIALOG_EDIT_CREDENTIALS, timeout, fail_if_false):
            return True
        else:
            return False


class VerifyStorageSystem(object):
    """
        Verify Storage System values
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storagesystem_name(cls, storagesystem, storagesystem_type, timeout=10, fail_if_false=True):
        """
            verify the storage system name on Storage System screen against the datafile
        """
        logger.info('verifying [ Storage System Name %s ] is visible' % storagesystem)
        return FusionUIBase.verify_item_should_exist_in_master_table(storagesystem, item_type=storagesystem_type, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_state(cls, expect_value, storagesystem_type, timeout=5, fail_if_false=True):
        """
            verify the storage system state on Storage System screen against the datafile
        """
        logger.debug("verify [ state ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("State", GeneralStorageSystemElements.ID_TEXT_GENERAL_STATE % storagesystem_type, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_type(cls, expect_value, storagesystem_type, timeout=5, fail_if_false=True):
        """
            verify the storage system type on Storage System screen against the datafile
        """
        logger.debug("verify [ Type ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Type", GeneralStorageSystemElements.ID_TEXT_GENERAL_TYPE % storagesystem_type, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_user_name(cls, expect_value, storagesystem_type, timeout=5, fail_if_false=True):
        """
            verify the storage system user name on Storage System screen against the datafile
        """
        logger.debug("verify [ user name ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("User name", GeneralStorageSystemElements.ID_TEXT_GENERAL_USER_NAME % storagesystem_type, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_ip_host_name(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system ip/host name on Storage System screen against the datafile
        """
        logger.debug("verify [ IP / host name ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("IP / host name", GeneralStorageSystemElements.ID_TEXT_GENERAL_IP_HOST_NAME, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_storage_domain(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system domain on Storage System screen against the datafile
        """
        logger.debug("verify [ Storage domain ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Storage domain", GeneralStorageSystemElements.ID_TEXT_GENERAL_STORAGE_DOMAIN, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_model(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system model on Storage System screen against the datafile
        """
        logger.debug("verify [ Model ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Model", GeneralStorageSystemElements.ID_TEXT_GENERAL_MODEL, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_firmware(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system firmware on Storage System screen against the datafile
        """
        logger.debug("verify [ Firmware ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Firmware", GeneralStorageSystemElements.ID_TEXT_GENERAL_FIRMWARE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_wwn(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system wwn on Storage System screen against the datafile
        """
        logger.debug("verify [ WWN ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("WWN", GeneralStorageSystemElements.ID_TEXT_GENERAL_WWN, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_serial_number(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system serial number on Storage System screen against the datafile
        """
        logger.debug("verify [ Serial number ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Serial number", GeneralStorageSystemElements.ID_TEXT_GENERAL_SERIAL_NUMBER, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by_storage_pools(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system used by storage pools  on Storage System screen against the datafile
        """
        logger.debug("verify [ Used by storage pools ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Used by storage pools", GeneralStorageSystemElements.ID_TEXT_GENERAL_USED_BY_STORAGE_POOLS, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_used_by_storage_volumes(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system used by volumes on Storage System screen against the datafile
        """
        logger.debug("verify [ Used by storage volumes ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Used by storage volumes", GeneralStorageSystemElements.ID_TEXT_GENERAL_USED_BY_STORAGE_VOLUMES, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_mgmt_host_name(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system management host name on Storage System screen against the datafile
        """
        logger.debug("verify [ Nimble Host Name ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Group management IP / host name", GeneralStorageSystemElements.ID_TEXT_GENERAL_MGMT_HOST_NAME, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_software_version(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system software version on Storage System screen against the datafile
        """
        logger.debug("verify [ Software version ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Software version", GeneralStorageSystemElements.ID_TEXT_GENERAL_SOFTWARE_VERSION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_cluster_name(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system cluster name on Storage System screen against the datafile
        """
        logger.debug("verify [ Cluster name ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Cluster name", GeneralStorageSystemElements.ID_TEXT_GENERAL_CLUSTER_NAME, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_lun_mode(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system lun mode on Storage System screen against the datafile
        """
        logger.debug("verify [ LUN mode ] in Overview view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("LUN mode", GeneralStorageSystemElements.ID_TEXT_GENERAL_LUN_MODE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_nimble_lun_mode(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the nimble storage system lun mode on Storage System screen against the datafile
        """
        logger.debug("verify [ LUN mode ] in Overview view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("LUN mode", GeneralStorageSystemElements.ID_TEXT_GENERAL_NIMBLE_LUN_MODE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_nimble_software_version(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the nimble storage system software name on Storage System screen against the datafile
        """
        logger.debug("verify [ Software Version ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Software version", GeneralStorageSystemElements.ID_TEXT_GENERAL_NIMBLE_SOFTWARE_VERSION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_encryption(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the nimble storage system encryption on Storage System screen against the datafile
        """
        logger.debug("verify [ Encryption] in Overview view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Encryption", GeneralStorageSystemElements.ID_TEXT_GENERAL_ENCRYPTION, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_nimble_volumes(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the nimble storage system volumes on Storage System screen against the datafile
        """
        logger.debug("verify [ Volumes Link ] in Overview view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Volumes", GeneralStorageSystemElements.ID_TEXT_GENERAL_NIMBLE_VOLUMES, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_nimble_storage_pools(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the nimble storage system storage pools on Storage System screen against the datafile
        """
        logger.debug("verify [ Storage Pools Link ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Storage pools", GeneralStorageSystemElements.ID_TEXT_GENERAL_NIMBLE_STORAGE_POOLS, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_nimble_volumesets(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the nimble storage system volume sets on Storage System screen against the datafile
        """
        logger.debug("verify [ Used by volumesets ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Volume sets", GeneralStorageSystemElements.ID_TEXT_GENERAL_NIMBLE_VOLUMESETS, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_array_type(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system array type on Storage System screen against the datafile
        """
        logger.debug("verify [ Array Type] in Overview view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Array type", GeneralStorageSystemElements.ID_TEXT_GENERAL_ARRAY_TYPE, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_general_cluster_ip_host_name(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system cluster/ip/host name on Storage System screen against the datafile
        """
        logger.debug("verify [ Cluster IP / host name ] in general view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("IP / host name", GeneralStorageSystemElements.ID_TEXT_GENERAL_CLUSTER_IP_HOST_NAME, expect_value, timeout, fail_if_false)

    # - Utilization
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_utilization_total(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system utilization total on Storage System screen against the datafile
        """
        logger.debug("verify [ Total ] in utilization view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Total", GeneralStorageSystemElements.ID_TEXT_UTILIZATION_TOTAL, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_utilization_allocated(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system utilization allocated on Storage System screen against the datafile
        """
        logger.debug("verify [ Allocated ] in utilization view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Total", GeneralStorageSystemElements.ID_TEXT_UTILIZATION_ALLOCATED, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_utilization_free(cls, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system utilization free on Storage System screen against the datafile
        """
        logger.debug("verify [ Free ] in utilization view, expected value is [ %s ]" % expect_value)
        return FusionUIBase.verify_element_text("Total", GeneralStorageSystemElements.ID_TEXT_UTILIZATION_FREE, expect_value, timeout, fail_if_false)
    # }

    # { Storage pools
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pools_name_exist(cls, pool_name, timeout=5, fail_if_false=True):
        """
            verify the storage system storage pools name exists on Storage System screen against the datafile
        """
        logger.debug("verify [ Storage pools name '%s' ] exist in storage pools view" % pool_name)
        return ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_TEXT_STORAGE_POOLS_ROW_NAME % pool_name, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pools_state(cls, pool_name, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage systemstorage pools state on Storage System screen against the datafile
        """
        logger.debug("verify [ State ] of [ Storage pools name '%s' ] in storage pools view, expected value is [ %s ]" % (pool_name, expect_value))
        return FusionUIBase.verify_element_text("State", GeneralStorageSystemElements.ID_TEXT_STORAGE_POOLS_ROW_STATE % pool_name, expect_value, timeout, fail_if_false, hidden_element=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pools_allocated_capacity(cls, pool_name, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system storage pools allocated capacity on Storage System screen against the datafile
        """
        logger.debug("verify [ Allocated capacity ] of [ Storage pools name '%s' ] in storage pools view, expected value is [ %s ]" % (pool_name, expect_value))
        return FusionUIBase.verify_element_text("Total", GeneralStorageSystemElements.ID_TEXT_STORAGE_POOLS_ROW_ALLOCATED_CAPACITY % pool_name, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pools_total_capacity(cls, pool_name, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system storage pools total capacity on Storage System screen against the datafile
        """
        logger.debug("verify [ Total capacity ] of [ Storage pools name '%s' ] in storage pools view, expected value is [ %s ]" % (pool_name, expect_value))
        return FusionUIBase.verify_element_text("Total capacity", GeneralStorageSystemElements.ID_TEXT_STORAGE_POOLS_ROW_TOTAL_CAPACITY % pool_name, expect_value, timeout, fail_if_false)
    # }

    # { Storage System Ports
    @classmethod
    def make_storage_port_panel_into_viewpoint(cls, name):
        """
            Make the storage port panel come into view
        """
        logger.debug("Get [ Storage pool '%s' into view point ]" % name)
        FusionUIBase.scroll_element_into_viewpoint(GeneralStorageSystemElements.ID_BTN_STORAGE_SYSTEM_PORTS_FOLDING_PORT % name)
        time.sleep(1)
        FusionUIBase.scroll_element_into_viewpoint(GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_FAILOVER_STATE % name)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_port_exist(cls, port, timeout=5, fail_if_false=True):
        """
            verify the storage system port path exists on Storage System screen against the datafile
        """
        logger.debug("verify [ Storage system path port '%s' ] exist in Storage System Ports view" % port)
        return ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_PORT % port, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_state(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path state Storage System screen against the datafile
        """
        logger.debug("verify [ State ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("State", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_STATE % port, expect_value, timeout, fail_if_false, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_label(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path label on Storage System screen against the datafile
        """
        logger.debug("verify [ Label ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("Label", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_LABEL % port, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_protocol(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path protocol on Storage System screen against the datafile
        """
        logger.debug("verify [ Protocol ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("Protocol", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_PROTOCOL % port, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_expected_san_network(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path expected san network on Storage System screen against the datafile
        """
        logger.debug("verify [ Expected san network ] [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("Expected SAN/Network", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_EXPECTED_SAN_OR_NETWORK % port, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_actual_san(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path actual san on Storage System screen against the datafile
        """
        logger.debug("verify [ Actual san ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("Actual SAN", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_ACTUAL_SAN % (port, port), expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_port_group(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path port group on Storage System screen against the datafile
        """
        logger.debug("verify [ Port group ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("Port Group", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_ROW_PORT_GROUP % port, expect_value, timeout, fail_if_false)

    @classmethod
    def expand_storage_system_path_detail_panel(cls, port, timeout=5):
        """
            Expand the storage system path detail panel
        """
        logger.debug("click [ icon ] beside port column of [ Storage system path '%s' ] to expand storage system path detail panel" % port)
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_BTN_STORAGE_SYSTEM_PORTS_FOLDING_PORT % port, timeout, fail_if_false=True)
        ui_lib.wait_for_element_visible(GeneralStorageSystemElements.ID_PANEL_STORAGE_SYSTEM_PORTS_ROW_DETAIL % port, timeout, True)

    @classmethod
    def fold_storage_system_path_detail_panel(cls, port, timeout=5):
        """
            Fold the storage system path detail panel
        """
        logger.debug("click [ icon ] beside port column of [ Storage system path '%s' ] to fold storage system path detail panel" % port)
        ui_lib.wait_for_element_and_click(GeneralStorageSystemElements.ID_BTN_STORAGE_SYSTEM_PORTS_FOLDING_PORT % port, timeout, fail_if_false=True)
        ui_lib.wait_for_element_notvisible(GeneralStorageSystemElements.ID_PANEL_STORAGE_SYSTEM_PORTS_ROW_DETAIL % port, timeout, True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_wwpn(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system wwpn on Storage System screen against the datafile
        """
        logger.debug("verify [ WWPN ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("WWPN", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_WWPN % port, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_partner_port(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path partner port on Storage System screen against the datafile
        """
        logger.debug("verify [ Partner port ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("Partner port", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_PARTNER_PORT % port, expect_value, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_system_path_failover_state(cls, port, expect_value, timeout=5, fail_if_false=True):
        """
            verify the storage system path failover state on Storage System screen against the datafile
        """
        logger.debug("verify [ Failover state ] of [ Storage system path '%s' ] in Storage System Ports view, expected value is [ %s ]" % (port, expect_value))
        return FusionUIBase.verify_element_text("Failover state", GeneralStorageSystemElements.ID_TEXT_STORAGE_SYSTEM_PORTS_FAILOVER_STATE % port, expect_value, timeout, fail_if_false)
    # }
