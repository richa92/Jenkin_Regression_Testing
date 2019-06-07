from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common import ui_lib
import time
from FusionLibrary.ui.business_logic.base import (FusionUIBase, SectionType, FusionUIConst)
from FusionLibrary.ui.business_logic.settings.licenses import (VerifyLicense, GeneralLicense, AddLicense)
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.ui.business_logic.base import ScreenshotDeco


def navigate():
    if GeneralLicense.is_licenses_page() is False:
        FusionUIBase.navigate_to_section(SectionType.SETTINGS, time_for_loading=3)
        GeneralLicense.click_license_title()


def add_license(*licenses_obj):

    logger.info("Add License to appliance")

    """ Retrieve data from datasheet """
    if isinstance(licenses_obj, test_data.DataObj):
        licenses_obj = [licenses_obj]
    elif isinstance(licenses_obj, tuple):
        licenses_obj = list(licenses_obj[0])

    navigate()

    count = 0
    total_len = len(licenses_obj)
    for n, lic_obj in enumerate(licenses_obj):
        # check if license is existing
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Adding a license with type '{0}'".format(lic_obj.type))
        if lic_obj.type == FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED:
            if VerifyLicense.verify_oneview_license_exist(fail_if_false=False):
                if VerifyLicense.verify_required_server_oneview_license_exist(timeout=2, fail_if_false=False) is False:
                    logger.warn("License with type '{0}' already exists".format(lic_obj.type))
                    continue
        elif lic_obj.type == FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED_WITHOUT_ILO:
            if VerifyLicense.verify_oneview_wo_ilo_license_exist(fail_if_false=False):
                if VerifyLicense.verify_required_server_oneview_wo_ilo_license_exist(timeout=2, fail_if_false=False) is False:
                    logger.warn("License with type '{0}' already exists".format(lic_obj.type))
                    continue
        elif lic_obj.type == FusionUIConst.CONST_LICENSE_ONEVIEW_SYNERGY_FCUPGRADE:
            if VerifyLicense.verify_oneview_fcupgrade_license_exists(fail_if_false=False):
                logger.info("License with type '{0}' already exists".format(lic_obj.type))
            # We allow multiple License to be added even if FCupgrade license is already present
        else:
            ui_lib.fail_test("Not supported attribute 'type' of license data node")

        AddLicense.select_actions_add()
        AddLicense.wait_add_license_dialog_shown()
        AddLicense.input_license_key(lic_obj.content)

        AddLicense.click_add_button()
        if AddLicense.wait_add_license_dialog_disappear(fail_if_false=False) is False:
            logger.warn("Failed to add license with type '%s'" % lic_obj.type)
            # encounter error
            msg = FusionUIBase.get_error_message_from_dialog()
            if msg[0] is True:
                logger.warn(msg[1])
            else:
                logger.warn("Failed to get error message in dialog")

            AddLicense.click_cancel_button()
            continue

        # verify
        time.sleep(8)
        if lic_obj.type == FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED:
            if VerifyLicense.verify_oneview_license_exist(fail_if_false=False) is False:
                logger.warn("Not found license with type '{0}'".format(lic_obj.type))
                continue
            else:
                if VerifyLicense.verify_required_server_oneview_license_exist(timeout=2, fail_if_false=False):
                    logger.warn("Not found license with type '{0}'".format(lic_obj.type))
                    continue
        elif lic_obj.type == FusionUIConst.CONST_LICENSE_ONEVIEW_ADVANCED_WITHOUT_ILO:
            if VerifyLicense.verify_oneview_wo_ilo_license_exist(fail_if_false=False) is False:
                logger.warn("Not found license with type '{0}'".format(lic_obj.type))
                continue
            else:
                if VerifyLicense.verify_required_server_oneview_wo_ilo_license_exist(timeout=2, fail_if_false=False):
                    logger.warn("Not found license with type '{0}'".format(lic_obj.type))
                    continue

        count += 1

    if count == 0:
        logger.warn("No license added!")
        return False

    if count != total_len:
        logger.warn("Not all licenses added!")
        return False

    return True


def verify_required_server_oneview_license(number):
    logger.info("Verify number of required server oneview license")

    navigate()

    VerifyLicense.verify_required_server_oneview_license(number)

    return True


def verify_required_server_oneview_wo_ilo_license(number):
    logger.info("Verify number of required server oneview w/o iLo license")

    navigate()

    VerifyLicense.verify_required_server_oneview_wo_ilo_license(number)

    return True


def verify_licensed_server_oneview_license(number):
    logger.info("Verify number of licensed server oneview license")

    navigate()

    VerifyLicense.verify_licensed_server_oneview_license(number)

    return True


def verify_licensed_server_oneview_wo_ilo_license(number):
    logger.info("Verify number of licensed server oneview w/o iLo license")

    navigate()

    VerifyLicense.verify_licensed_server_oneview_wo_ilo_license(number)

    return True


def verify_required_fcupgrade_license(count):
    logger.info("Verify number of required fcupgrade license")

    navigate()
    if count == 1:
        msg = "%s interconnect bay needs license" % count
    else:
        msg = "%s interconnect bays need licenses" % count
    VerifyLicense.verify_required_oneview_fcupgrade_license(msg)

    return True


def verify_licensed_fcupgrade_interconnects(count):
    logger.info("Verify number of licensed interconnects")

    navigate()
    if count == 1:
        msg = "%s interconnect bay licensed" % count
    else:
        msg = "%s interconnect bays licensed" % count
    VerifyLicense.verify_licensed_interconnect_oneview(msg)

    return True


def verify_available_fcupgrade_licenses(count):
    logger.info("Verify available number of licensed FCupgrade license")

    navigate()
    if count == 1:
        msg = "%s license available" % count
    else:
        msg = "%s licenses available" % count
    VerifyLicense.verify_available_fcupgrade_license(msg)

    return True


def validate_no_fc_license():
    navigate()
    return VerifyLicense.verify_fc_license_not_exist()


def validate_add_button_exists_on_license_page():
    logger.info("Verify Add button Exists On License Page")
    navigate()
    return VerifyLicense.verify_add_button_exist()


def _add_license_action(lic_obj):
    AddLicense.select_actions_add()
    AddLicense.wait_add_license_dialog_shown()
    AddLicense.input_license_key(lic_obj.content)
    AddLicense.click_add_button()
    return AddLicense.wait_add_license_dialog_disappear(fail_if_false=False)


def add_fc_licenses(licenses_obj):
    """
    This function will list all parameters in xml file and add them.
    license xml example:
    <licenses>
        <license type="Synergy 8Gb FC Upgrade" content='9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"' />
        <license type="Synergy 8Gb FC Upgrade" content='YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"' />
    </licenses>
    """
    logger.info("Add FC License to appliance")
    navigate()
    total_len = len(licenses_obj)
    failure_cnt = 0
    for n, lic_obj in enumerate(licenses_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        logger.info("Adding FC license with type '{0}'".format(lic_obj.type))
        if lic_obj.type != FusionUIConst.CONST_LICENSE_ONEVIEW_SYNERGY_FCUPGRADE:
            err_msg = "The license type is not FC licenses, please correct."
            ui_lib.fail_test(err_msg)
        if not _add_license_action(lic_obj):
            logger.warn("Failed to add license with type {}".format(lic_obj.type))
            msg = FusionUIBase.get_error_message_from_dialog()
            if msg[0] is True:
                logger.warn(msg[1])
            else:
                logger.warn("Failed to get error message in dialog")
            AddLicense.click_cancel_button()
            failure_cnt += 1
            continue
        if VerifyLicense.verify_oneview_fcupgrade_license_exists(fail_if_false=False):
            expected_text = "%s license%s available" % ((n + 1), '' if n == 0 else 's')
            if not VerifyLicense.verify_available_fcupgrade_license(expected_text, timeout=5, fail_if_false=False):
                failure_cnt += 1
    return False if failure_cnt else True


def validate_error_when_adding_invalid_or_duplicated_fc_licenses(licenses_obj):
    logger.info("Add Invalid FC License to appliance")
    navigate()
    total_len = len(licenses_obj)
    failure_cnt = 0
    for n, lic_obj in enumerate(licenses_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total_len, '-' * 14))
        if _add_license_action(lic_obj):
            ScreenshotDeco()
            logger.debug("Failed, added {} negative license without error".format(lic_obj.type))
            failure_cnt += 1
            continue
        else:
            if VerifyLicense.verify_error_message_when_add_invalid_or_duplicated_license(lic_obj.negative_type):
                logger.info("As expected that {} cannot be added.".format(lic_obj.negative_type))
            else:
                failure_cnt += 1
                ScreenshotDeco()
                logger.debug("Although cannot added negative license, but error message is not correct.")
            AddLicense.click_cancel_button()
    return False if failure_cnt else True


def validate_add_license_button_exists():
    navigate()
    logger.info("Verify Add button Exists On License Page")
    return VerifyLicense.verify_add_button_exist()
