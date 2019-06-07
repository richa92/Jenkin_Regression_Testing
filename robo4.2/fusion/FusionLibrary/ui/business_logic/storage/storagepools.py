'''
    Storage Pools
'''
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.storagepools_elements import GeneralStoragePoolElements
from FusionLibrary.ui.business_logic.storage.storagepools_elements import EditStoragePoolElements
from FusionLibrary.ui.business_logic.storage.storagepools_elements import RefreshStoragePoolElements
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime


class CommonOperationStoragePools(object):
    '''
        Common Operation functions for Storage Pools
    '''
    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pool_not_exist(cls, storage_pool, storage_system_name, timeout=5, fail_if_false=True):
        '''
            Verify Storage Pool does not exist
        '''
        logger.debug("verify storage system '%s' is not existing" % storage_pool)
        if ui_lib.wait_for_element_notvisible(GeneralStoragePoolElements.ID_TABLE_STORAGE_POOL % (storage_pool, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pool_exist(cls, storage_pool, storage_system_name, timeout=5, fail_if_false=True):
        '''
            Verify storage pool does exist
        '''
        logger.debug("verify storage system '%s' is existing" % storage_pool)
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_TABLE_STORAGE_POOL % (storage_pool, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pool_status_ok(cls, storage_pool, storage_system_name, timeout=5, fail_if_false=True):
        '''
            Verify Storage Pool status = OK
        '''
        logger.debug("verify whether storage system %s is ok" % storage_pool)
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_OK % (storage_pool, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pool_warn(cls, storage_pool, storage_system_name, timeout=5, fail_if_false=True):
        '''
            Verify Storage Pool status = WARN
        '''
        logger.debug("verify whether storage system %s is warning" % storage_pool)
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_WARN % (storage_pool, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storage_pool_error(cls, storage_pool, storage_system_name, timeout=5, fail_if_false=True):
        '''
            Verify Storage Pool status = error
        '''
        logger.debug("verify whether storage system %s is error" % storage_pool)
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_ERROR % (storage_pool, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_storage_pool(cls, storage_pool_name, storage_system_name, timeout=5):
        '''
            On the Storage Pool Page, click a specific storage pool
        '''
        logger.debug("select storage pool '%s'" % storage_pool_name)
        ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_TABLE_STORAGE_POOL % (storage_pool_name, storage_system_name), timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_pool_selected(cls, storage_pool_name, storage_system_name, timeout=5, fail_if_false=True):
        '''
            Wait for storage pool to be selected
        '''
        logger.debug("wait storage pool '%s' selected" % storage_pool_name)
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_TABLE_STORAGE_POOL_SELECTED % (storage_pool_name, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_storage_pool_status(cls, storage_pool_name, storage_system_name, timeout=5, fail_if_false=True):
        '''
            Get the status of a specific storage pool
        '''
        logger.debug("get storage pool '%s' status ..." % storage_pool_name)
        ret = ui_lib.get_text(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL % (storage_pool_name, storage_system_name), timeout=timeout, fail_if_false=fail_if_false, hidden_element=True)
        logger.debug("status of storage pool '%s (%s)' is '%s'" % (storage_pool_name, storage_system_name, ret))
        return ret

    @classmethod
    def click_action_button(cls, timeout=5):
        '''
            On the Storage Pool Page, click the action button
        '''
        logger.debug("click action button")
        ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_ongoing_disappear(cls, timeout=10, fail_if_false=True):
        '''
            wait for progress bar to indicate complete
        '''
        logger.debug("wait progress bar complete")
        if ui_lib.wait_for_element_remove(GeneralStoragePoolElements.ID_STATUS_NOTIFICATION_ONGOING, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_ok_shown(cls, timeout=5, fail_if_false=True):
        '''
            Wait for progress bar to be OK
        '''
        logger.debug("wait progress bar - 'ok'")
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_NOTIFICATION_OK, timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_warn_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for progress bar to show warn
        '''
        logger.debug("wait progress bar - 'warn'")
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_NOTIFICATION_WARN, timeout, fail_if_false):
            cls.get_notification_message()
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_ok_or_warn_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for progress bar to show OK or warn
        '''
        logger.debug("wait progress base - 'ok' or 'warn'")
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_NOTIFICATION_OK, timeout, fail_if_false=False):
            return True
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_NOTIFICATION_WARN, timeout, fail_if_false):
            cls.get_notification_message()
            return True
        else:
            cls.get_notification_message(log_prefix='_warn')
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_progress_error_shown(cls, timeout=5, fail_if_false=True):
        '''
            wait for progress bar to show error
        '''
        logger.debug("wait progress bar - error")
        if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_NOTIFICATION_ERROR, timeout, fail_if_false):
            cls.get_notification_message()
            return True
        else:
            return False

    @classmethod
    def get_notification_message(cls, log_prefix="debug", timeout=5):
        '''
            Get the notification message
        '''
        msg = FusionUIBase.get_text(GeneralStoragePoolElements.ID_TEXT_NOTIFICATION_MESSAGE, timeout)
        resolution = FusionUIBase.get_text(GeneralStoragePoolElements.ID_TEXT_NOTIFICATION_RESOLUTION, timeout)
        if log_prefix == "debug":
            logger.debug('Message: %s \nResolution: %s' % (msg, resolution))
        else:
            logger.warn('Message: %s \nResolution: %s' % (msg, resolution))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_pool_status_ok(cls, storage_pool, storage_system_name, timeout=10, fail_if_false=True):
        '''
            wait for the storage pool status = OK
        '''
        start = datetime.now()
        logger.debug("wait for Storage Pool [ %s ] status to be [ ok ]" % storage_pool)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_OK % (storage_pool, storage_system_name), timeout=2, fail_if_false=False):
                logger.debug("Storage Pool [ %s ] status is [ ok ]" % storage_pool)
                return True
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_WARN % (storage_pool, storage_system_name), timeout=2, fail_if_false=False):
                err_msg = "Storage Pool [ %s ] status is [ warning ], not an expected [ ok ]" % storage_pool
                logger.debug(err_msg)
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_ERROR % (storage_pool, storage_system_name), timeout=2, fail_if_false=False):
                err_msg = "Storage Pool [ %s ] status is [ error ], not an expected [ ok ]" % storage_pool
                logger.debug(err_msg)
                if fail_if_false is False:
                    logger.warn(err_msg)
                    return False
                else:
                    ui_lib.fail_test(err_msg)
            else:
                logger.debug("Storage Pool [ %s ] status is [ unknown ]" % storage_pool)
                continue
        err_msg = "Timeout for waiting for the status of Storage Pool [ %s ] to change to [ ok ]." % storage_pool
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_pool_status_disabled(cls, storage_pool, storage_system_name, timeout=10, fail_if_false=True):
        '''
            Wait for the storage pool status to be disabled
        '''
        start = datetime.now()
        logger.debug("wait for Storage Pool [ %s ] status to be [ disabled ]" % storage_pool)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_DISABLED % (storage_pool, storage_system_name), timeout=2, fail_if_false=False):
                logger.debug("retrieved status of Storage Pool [ %s ] is [ disabled ]" % storage_pool)
                return True
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_WARN % (storage_pool, storage_system_name), timeout=2, fail_if_false=False):
                err_msg = "retrieved status of Storage Pool [ %s ] is [ warning ], not an expected [ disabled ]" % storage_pool
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_ERROR % (storage_pool, storage_system_name), timeout=2, fail_if_false=False):
                err_msg = "retrieved Storage Pool [ %s ] is [ error ], not an expected [ disabled ]" % storage_pool
                return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)
            else:
                logger.debug("retrieved stats of Storage Pool [ %s ] is [ unknown ]" % storage_pool)
                continue
        err_msg = "Timeout for waiting for the status of Storage Pool [ %s ] to change to [ disabled ]." % storage_pool
        return FusionUIBase.fail_test_or_return_false(err_msg, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_pool_status_ok_or_warn(cls, storage_pool, storage_system_name, timeout=10, fail_if_false=True):
        '''
            Wait for the storage pool status to be OK or WARN
        '''
        start = datetime.now()
        logger.debug("wait storage system '%s' status is ok or warning" % storage_pool)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_OK % (storage_pool, storage_system_name), timeout=5, fail_if_false=False):
                logger.debug("storage system status is ok")
                return True
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_WARN % (storage_pool, storage_system_name), timeout=5, fail_if_false=False):
                logger.debug("storage system status is warning")
                return True
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_ERROR % (storage_pool, storage_system_name), timeout=5, fail_if_false=False):
                logger.debug("storage system status is error")
                return False
            else:
                logger.debug("storage system status is unknown")
                continue

        err_msg = "Timeout for waiting for the status of Storage Pool [ %s ] to change to [ ok ] or [ warn ]." % storage_pool
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_storage_pool_status_error(cls, storage_pool, storage_system_name, timeout=10, fail_if_false=True):
        '''
            Wait for the storage pool status to be error
        '''
        start = datetime.now()
        logger.debug("wait storage system '%s' status is ok or warning" % storage_pool)
        while (datetime.now() - start).total_seconds() < timeout:
            if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_OK % (storage_pool, storage_system_name), timeout=5, fail_if_false=False):
                logger.debug("storage system status is ok")
                return False
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_WARN % (storage_pool, storage_system_name), timeout=5, fail_if_false=False):
                logger.debug("storage system status is warning")
                return False
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_STATUS_STORAGE_POOL_ERROR % (storage_pool, storage_system_name), timeout=5, fail_if_false=False):
                logger.debug("storage system status is error")
                return True
            else:
                logger.debug("storage system status is unknown")
                continue

        err_msg = "Timeout for waiting for the status of Storage Pool [ %s ] to change to [ error ]." % storage_pool
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, storage_pool, timeout=5, fail_if_false=True):
        '''
            Wait for the activity to complete
        '''
        logger.debug("wait activity action completed")
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            actionname = ""

            if ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_OK % storage_pool, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_TITLE % storage_pool)
                logger.debug("activity action '%s' status is ok" % actionname)
                return True
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_WARN % storage_pool, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_TITLE % storage_pool)
                logger.debug("activity action '%s' status is warn" % actionname)
                ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_WARN % storage_pool)
                msg = FusionUIBase.get_multi_elements_text(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_MESSAGE)
                logger.warn(msg)
                return False
            elif ui_lib.wait_for_element_visible(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_ERROR % storage_pool, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_TITLE % storage_pool)
                logger.debug("activity action '%s' status is error" % actionname)
                ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_ACTION_ERROR % storage_pool)
                msg = FusionUIBase.get_multi_elements_text(GeneralStoragePoolElements.ID_TEXT_ACTIVITY_MESSAGE)
                logger.warn(msg)
                return False
            else:
                logger.debug("activity action '%s' status is unknown" % actionname)
                continue

        err_msg = "Timeout for waiting for activity of Storage Pool [ %s ] change to [ ok ]." % storage_pool
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_storagepools_title(cls, storagepool, timeout=10, fail_if_false=True):
        '''
            Wait for storage pool title on storage pool page
        '''
        logger.info('verifying [ Storage Pool title= %s ] is visible' % storagepool)
        ui_lib.wait_for_element(GeneralStoragePoolElements.ID_PAGE_LABEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_system_link(cls, timeout=5):
        '''
            On the Storage Pool Page, click storage system link
        '''
        logger.debug("Click storage system link on storage pool screen")
        ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_LINK_STORAGE_SYSTEMS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_used_by_volumes_link(cls, timeout=5):
        '''
            On the Storage Pool Page, click used by volumes link
        '''
        logger.debug("Click used by volumes link on storage pool screen")
        ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_LINK_USED_BY_VOLUMES, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_used_by_template_link(cls, timeout=5):
        '''
            On the Storage Pool Page, click used by templates link
        '''
        logger.debug("Click used by template link on storage pool screen")
        ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_LINK_USED_BY_TEMPLATES, timeout, fail_if_false=True)


class EditStoragePools(object):
    """
        Edit Storage Pools
    """
    e = EditStoragePoolElements

    @classmethod
    def select_action_edit(cls, timeout=5, fail_if_false=True):
        '''
            On the Storage Pool Page, click on action menu button
        '''
        logger.debug("select action 'Edit'")
        ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_BUTTON_ACTIONS, timeout=timeout, fail_if_false=fail_if_false)
        ui_lib.wait_for_element_and_click(cls.e.ID_SELECT_ACTION_EDIT, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_storage_pool_dialog_open(cls, timeout=5, fail_if_false=True):
        '''
            Wait for the Edit storage pool dialog to open
        '''
        logger.debug("wait for [ Edit Storage Pool ] dialog to get opened")
        if ui_lib.wait_for_element_visible(cls.e.ID_DIALOG_EDIT_STORAGE_POOL, timeout, fail_if_false):
            logger.debug("successfully opened [ Edit Storage Pool ] dialog")
            return True
        else:
            msg = "[ Edit Storage Pool ] dialog did NOT get opened"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)

    @classmethod
    def tick_state_as_managed(cls, timeout=5, fail_if_false=True):
        '''
            On the Edit Storage Pool Dialog, choose radio button for managed
        '''
        logger.debug("choose 'State' option as 'Managed' ...")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_STATE_MANAGED, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def tick_state_as_discovered(cls, timeout=5, fail_if_false=True):
        '''
            On the Edit Storage Pool Dialog, choose radio button for discovered
        '''
        logger.debug("choose 'State' option as 'Discovered' ...")
        ui_lib.wait_for_element_and_click(cls.e.ID_RADIO_STATE_DISCOVERED, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    def click_ok_button(cls, timeout=5):
        '''
            On the Edit Storage Pool Dialog, click OK button
        '''
        logger.debug("click [ OK ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_OK, timeout, fail_if_false=True)

    @classmethod
    def click_cancel_button(cls, timeout=5):
        '''
            On the Edit Storage Pool Dialog, click cancel button
        '''
        logger.debug("click [ Cancel ] button")
        ui_lib.wait_for_element_and_click(cls.e.ID_BUTTON_CANCEL, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_edit_storage_pool_dialog_close(cls, timeout=10, fail_if_false=True):
        '''
            wait for the edity storage pool dialog to close
        '''
        logger.debug("wait for [ Edit Storage Pool ] dialog to get closed")
        if ui_lib.wait_for_element_notvisible(cls.e.ID_DIALOG_EDIT_STORAGE_POOL, timeout, fail_if_false):
            logger.debug("successfully closed [ Add Storage Pool ] dialog")
            return True
        else:
            msg = "[ Add Storage Pool ] did NOT get closed"
            return FusionUIBase.fail_test_or_return_false(msg, fail_if_false=fail_if_false)


class RefreshStoragePools(object):
    '''
        Refresh storage pools
    '''
    @classmethod
    def select_actions_refresh(cls, timeout=5):
        '''
            On the Storage Pool Page, select action menu refresh
        '''
        logger.debug("select refresh")
        ui_lib.wait_for_element_and_click(GeneralStoragePoolElements.ID_BUTTON_ACTIONS, timeout, fail_if_false=True)
        ui_lib.wait_for_element_and_click(RefreshStoragePoolElements.ID_SELECT_ACTION_REFRESH, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_state_refreshing(cls, timeout=15, fail_if_false=True):
        '''
            wait for general state = refreshing to show
        '''
        logger.debug("wait general state show refreshing")
        ui_lib.wait_for_element(GeneralStoragePoolElements.ID_TEXT_GENERAL_STATE, timeout, fail_if_false)
        if ui_lib.wait_for_element_text(GeneralStoragePoolElements.ID_TEXT_GENERAL_STATE, "Refreshing", timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_general_state_configured(cls, timeout=10, fail_if_false=True):
        '''
            wait for general state configured to show
        '''
        logger.debug("wait general state show configured")
        if ui_lib.wait_for_element_text(GeneralStoragePoolElements.ID_TEXT_GENERAL_STATE, "Configured", timeout, fail_if_false):
            return True
        else:
            return False
