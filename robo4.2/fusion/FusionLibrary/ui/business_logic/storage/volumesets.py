"""
    Methods and classes used on the Volume Sets Page
"""
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.storage.volumeset_elements import GeneralVolumeSetElements
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime


class CommonOperationVolumeSets(object):
    """
        Common Operations Volume Sets
    """

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volumeset_not_exist(cls, volumeset, storage_system_name, timeout=5, fail_if_false=True):
        """
            On the Volume Sets Page, verify that a specific volumeset does not exist
        """
        logger.debug("verify volumeset '%s' does not exist" % volumeset)
        if ui_lib.wait_for_element_notvisible(GeneralVolumeSetElements.ID_TABLE_VOLUMESET % (volumeset, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volumeset_exist(cls, volumeset, storage_system_name, timeout=5, fail_if_false=True):
        """
            On the Volume Sets Page, verify that a specific volumeset does exist
        """
        logger.debug("verify volumeset '%s' is existing" % volumeset)
        if ui_lib.wait_for_element_visible(GeneralVolumeSetElements.ID_TABLE_VOLUMESET % (volumeset, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volumeset_error(cls, volumeset, storage_system_name, timeout=5, fail_if_false=True):
        """
            On the Volume Sets Page, verify that a specific volumeset is in error
        """
        logger.debug("verify whether volumeset %s is in error" % volumeset)
        if ui_lib.wait_for_element_visible(GeneralVolumeSetElements.ID_STATUS_VOLUMESET_ERROR % (volumeset, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def click_volumeset(cls, volumeset_name, storage_system_name, timeout=5):
        """
            On the Volume Sets Page, select a specific volume set
        """
        logger.debug("select volumeset '%s'" % volumeset_name)
        ui_lib.wait_for_element_and_click(GeneralVolumeSetElements.ID_TABLE_VOLUMESET % (volumeset_name, storage_system_name), timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_volumeset_selected(cls, volumeset_name, storage_system_name, timeout=5, fail_if_false=True):
        """
            On the Volume Sets Page, wait until a specific volumeset is selected
        """
        logger.debug("wait volumeset '%s' selected" % volumeset_name)
        if ui_lib.wait_for_element_visible(GeneralVolumeSetElements.ID_TABLE_VOLUMESET_SELECTED % (volumeset_name, storage_system_name), timeout, fail_if_false):
            return True
        else:
            return False

    @classmethod
    def get_notification_message(cls, log_prefix="debug", timeout=5):
        """
            On the Volume Sets Page, get the notification message
        """
        msg = FusionUIBase.get_text(GeneralVolumeSetElements.ID_TEXT_NOTIFICATION_MESSAGE, timeout)
        resolution = FusionUIBase.get_text(GeneralVolumeSetElements.ID_TEXT_NOTIFICATION_RESOLUTION, timeout)
        if log_prefix == "debug":
            logger.debug('Message: %s \nResolution: %s' % (msg, resolution))
        else:
            logger.warn('Message: %s \nResolution: %s' % (msg, resolution))

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_activity_action_ok(cls, volumeset, timeout=5, fail_if_false=True):
        """
            On the Volume Sets Page, wait for the activity to show action=OK
        """
        logger.debug("wait activity action completed")
        start = datetime.now()
        while (datetime.now() - start).total_seconds() < timeout:
            actionname = ""

            if ui_lib.wait_for_element_visible(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_OK % volumeset, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volumeset)
                logger.debug("activity action '%s' status is ok" % actionname)
                return True
            elif ui_lib.wait_for_element_visible(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_WARN % volumeset, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volumeset)
                logger.debug("activity action '%s' status is warn" % actionname)
                ui_lib.wait_for_element_and_click(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_WARN % volumeset)
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_MESSAGE)
                logger.warn(msg)
                return False
            elif ui_lib.wait_for_element_visible(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_ERROR % volumeset, timeout=5, fail_if_false=False):
                actionname = FusionUIBase.get_text(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_TITLE % volumeset)
                logger.debug("activity action '%s' status is error" % actionname)
                ui_lib.wait_for_element_and_click(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_ACTION_ERROR % volumeset)
                msg = FusionUIBase.get_multi_elements_text(GeneralVolumeSetElements.ID_TEXT_ACTIVITY_MESSAGE)
                logger.warn(msg)
                return False
            else:
                logger.debug("activity action '%s' status is unknown" % actionname)
                continue

        err_msg = "Timeout for waiting for activity of Volume Set [ %s ] change to [ ok ]." % volumeset
        if fail_if_false is False:
            logger.warn(err_msg)
            return False
        else:
            ui_lib.fail_test(err_msg)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_volumeset_title(cls, volumeset, timeout=10, fail_if_false=True):
        """
            On the Volume Sets Page, verify the title
        """
        logger.info('verifying [ Volume Set title= %s ] is visible' % volumeset)
        ui_lib.wait_for_element(GeneralVolumeSetElements.ID_PAGE_LABEL, timeout=timeout, fail_if_false=fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_storage_system_link(cls, timeout=5):
        """
            On the Volume Sets Page, click the storage system link
        """
        logger.debug("Click storage system link on volume sets screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeSetElements.ID_LINK_STORAGE_SYSTEMS, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_volumes_link(cls, timeout=5):
        """
            On the Volume Sets Page, click the volumes link
        """
        logger.debug("Click used by volumes link on volume sets screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeSetElements.ID_LINK_USED_BY_VOLUMES, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def click_volume_template_link(cls, timeout=5):
        """
            On the Volume Sets Page, click the volume template link
        """
        logger.debug("Click used by volume templates link on volume sets screen")
        ui_lib.wait_for_element_and_click(GeneralVolumeSetElements.ID_LINK_USED_BY_TEMPLATES, timeout, fail_if_false=True)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_no_volumeset_action_menu(cls):
        """
            On the Volume Sets Page, verify that no action menu exists
        """
        logger.debug("Check action button visible on volume sets screen")
        if ui_lib.wait_for_element_visible(GeneralVolumeSetElements.ID_ACTION_BUTTON, timeout=3):
            return True
        else:
            return False
