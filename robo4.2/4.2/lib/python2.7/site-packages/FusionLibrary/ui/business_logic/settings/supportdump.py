# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Settings Page
"""
from FusionLibrary.ui.business_logic.base import TakeScreenShotWhenReturnFalseDeco, FusionUIBase
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.ui.business_logic.settings.supportdump_elements import CreateSupportDumpElements
from RoboGalaxyLibrary.utilitylib import logging as logger


class CreateSupportDump(object):

    @classmethod
    def click_create_support_dump(cls, timeout=5, fail_if_false=True):
        logger.debug("click Create support dump ")
        ui_lib.wait_for_element_and_click(CreateSupportDumpElements.ID_CREATE_SUPPORT_DUMP, timeout, fail_if_false)

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def wait_create_support_dump_dialog_shown(cls, timeout=5, fail_if_false=True):
        logger.debug("wait create support dump dialog shown")
        ui_lib.wait_for_element_visible(CreateSupportDumpElements.ID_DIALOG_CREATE_SUPPORT_DUMP, timeout,
                                        fail_if_false)

    @classmethod
    def choose_enable_support_dump_encryption(cls, timeout=5, fail_if_false=True):
        logger.debug("choose Enable support dump encryption")
        FusionUIBase.wait_for_checkbox_and_select(CreateSupportDumpElements.ID_CHECKBOX_ENABLE_SUPPORT_DUMP_ENCRYPTION, timeout, fail_if_false)

    @classmethod
    def click_yes_create(cls, timeout=5, fail_if_false=True):
        logger.debug("click Yes,create")
        ui_lib.wait_for_element_and_click(CreateSupportDumpElements.ID_BUTTON_YES_CREATE, timeout, fail_if_false)

    @classmethod
    def click_cancel_create(cls, timeout=5, fail_if_false=True):
        logger.debug("click Yes,create")
        ui_lib.wait_for_element_and_click(CreateSupportDumpElements.ID_BUTTON_CANCEL, timeout, fail_if_false)


class VerifySupportDump(object):

    @classmethod
    @TakeScreenShotWhenReturnFalseDeco
    def verify_create_support_dump_link_exists(cls, timeout=5, fail_if_false=False):
        logger.debug("Verifying Create Support Dump Link Exists")
        return ui_lib.wait_for_element_visible(CreateSupportDumpElements.ID_CREATE_SUPPORT_DUMP, timeout, fail_if_false)
