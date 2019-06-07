"""
     SANs Page
"""
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
from FusionLibrary.ui.business_logic.storage.sans import *
from RoboGalaxyLibrary.data.test_data import DataObj
from robot.libraries.BuiltIn import time


def edit_sans(*sans_obj):
    """ Edit SANs """
    FusionUIBase.navigate_to_section(SectionType.SANS)
    if isinstance(sans_obj, DataObj):
        sans_obj = [sans_obj]
    elif isinstance(sans_obj, tuple):
        sans_obj = list(sans_obj)

    for n, sans in enumerate(sans_obj):
        CommonOperationSANs.wait_for_sans_shown(sans.name)
        CommonOperationSANs.select_sans(sans.name)
        EditSANs.select_action_edit()
        EditSANs.wait_edit_sans_dialog_shown()
        logger.debug("Edit SANs")

        if sans.automatezoning.lower().strip() == "yes":
            logger.debug("choose automate zoning  Yes")
            EditSANs.choose_automate_zoning(automate_zoning=True)
        elif sans.automatezoning.lower().strip() == "no":
            logger.debug("choose automate zoning  No")
            EditSANs.choose_automate_zoning(automate_zoning=False)
        else:
            logger.info("the automate zoning type is not correct ")
            return False

        EditSANs.click_sans_edit_ok()
        if EditSANs.wait_edit_sans_dialog_disappear(fail_if_false=False) is False:
            EditSANs.click_sans_edit_ok()
            EditSANs.wait_edit_sans_dialog_disappear()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(sans.name, message="Updating SAN...", timeout=10)
        logger.debug("Edit SANs activity OK!")
        FusionUIBase.show_activity_sidebar()
    return True


def verify_sans(*sans_obj):
    """Verify SANs """
    FusionUIBase.navigate_to_section(SectionType.SANS)
    if isinstance(sans_obj, DataObj):
        sans_obj = [sans_obj]
    elif isinstance(sans_obj, tuple):
        sans_obj = list(sans_obj)

    for n, sans in enumerate(sans_obj):
        CommonOperationSANs.wait_for_sans_shown(sans.name)
        CommonOperationSANs.select_sans(sans.name)
        CommonOperationSANs.wait_for_sans_title_shown(sans.name)
        VerifySANs.verify_general_state(sans.state)
        VerifySANs.verify_general_type(sans.type)
        VerifySANs.verify_principal_switch(sans.principalswitch)
        VerifySANs.verify_san_manager(sans.sanmanager)
        VerifySANs.verify_associated_networks(sans.associatednetworks)
        VerifySANs.verify_zoned(sans.zoned)
        VerifySANs.verify_automate_zoning(sans.automatezoning)
        # VerifySANs.verify_use_aliases(sans.usealiases)
        logger.debug("%s verify completed" % sans.name)

    return True


def verify_can_not_use_invalid_text_for_zone_and_alias_format(*sans_obj):
    """ Verify Can not use invalid text for zone and alias format"""
    FusionUIBase.navigate_to_section(SectionType.SANS)
    for n, sans in enumerate(sans_obj):
        CommonOperationSANs.wait_for_sans_shown(sans.name)
        CommonOperationSANs.select_sans(sans.name)
        EditSANs.select_action_edit()
        EditSANs.wait_edit_sans_dialog_shown()
        time.sleep(5)
        EditSANs.click_zone_name_format(5, True)
        EditSANs.input_text_into_zone_name_format("!")
        EditSANs.click_sans_edit_ok()
        time.sleep(5)
        if EditSANs.verify_edit_sans_error_message("Unable to set an alias or zone name format", 10, True) is True:
            return True
        else:
            return False


def check_zone_name_format(*sans_obj):
    """ Check Zone Name Format"""
    FusionUIBase.navigate_to_section(SectionType.SANS)
    for n, sans in enumerate(sans_obj):
        CommonOperationSANs.wait_for_sans_shown(sans.name)
        CommonOperationSANs.select_sans(sans.name)
        EditSANs.select_action_edit()
        EditSANs.wait_edit_sans_dialog_shown()
        time.sleep(5)

        EditSANs.choose_sans_zoning_policy("SIAT")
        EditSANs.click_zone_name_format(5, True)
        EditSANs.check_sans_zone_name_format_token_with_zoning_policy_siat(5, True)

        EditSANs.choose_sans_zoning_policy("SISSS")
        EditSANs.click_zone_name_format(5, True)
        EditSANs.check_sans_zone_name_format_token_with_zoning_policy_sisss(5, True)
        EditSANs.add_zone_name_format_token("server initiator WWPN")
        return True
