# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Create Support Dump Page
"""
import time
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
from FusionLibrary.ui.business_logic.settings.supportdump import *


def create_dump_support(create_dump_support_obj):
    """Create Dump Support"""
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    time.sleep(10)
    CreateSupportDump.click_create_support_dump()
    CreateSupportDump.wait_create_support_dump_dialog_shown()
    if create_dump_support_obj.supportdumpencryption == "enable":
        CreateSupportDump.choose_enable_support_dump_encryption()
    CreateSupportDump.click_yes_create()
    FusionUIBase.show_activity_sidebar()
    FusionUIBase.wait_activity_action_ok("", message="Create support dump", timeout=600)
    FusionUIBase.show_activity_sidebar()
    logger.debug("Create support dump activity OK!")
    # TO DO download support dump file
    return True


def validate_create_support_dump_link_exists():
    FusionUIBase.navigate_to_section(SectionType.SETTINGS)
    return VerifySupportDump.verify_create_support_dump_link_exists()
