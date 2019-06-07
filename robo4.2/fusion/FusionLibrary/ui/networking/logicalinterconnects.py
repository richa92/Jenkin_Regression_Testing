# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
"""
    Logical  Interconnect Page
"""


from FusionLibrary.ui.business_logic.base import FusionUIBaseElements
from FusionLibrary.ui.networking.logicalinterconnects_elements import FusionLogicalInterconnectsPage
from FusionLibrary.ui.general import base_page
from FusionLibrary.ui.networking import interconnects
from FusionLibrary.ui.general import activity
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import VerifyLogicalInterconnects
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import CommonOperationLogicalInterconnect
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import UpdateFromGroupOperations
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import EditLogicalInterconnects
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import EditScopeForLogicalInterconnect
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import ReapplyConfiguration
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import InterconnectLinkPortsOperations
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import GeneralLogicalInterconnectsElements
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import TBirdLogicalInterconnectsUpdateFirmware
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import C7000LogicalInterconnectsUpdateFirmware
from FusionLibrary.ui.business_logic.networking.logicalinterconnects import UpdateLogicalInterconnectFirmware
from FusionLibrary.ui.business_logic.networking.interconnects import CommonOperationInterconnects
from FusionLibrary.ui.business_logic.base import FusionUIBase, SectionType
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.utilitylib import logging
from RoboGalaxyLibrary.ui.common import ui_lib
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from RoboGalaxyLibrary.utilitylib import logging as logger
from datetime import datetime, timedelta
import os
import re
from robot.libraries.BuiltIn import BuiltIn


def navigate():
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS)


def edit_logical_interconnect(*editlis_obj):
    """ Edit Logical Interconnects
     Arguments:
      <li>
          name*                         --  Name of logical interconnect as a string.
        <snmpv3>**                      --  Optional, for configuring snmpv3 related settings. if not present, use default snmpv3 settings
            snmpv3enabled                   --  Whether to enable snmpv3 settings, possible value: ENABLED|DISABLED
            <adduser>                       -- Optional,adds snmpv3 users
            <edit_snmpuser>                 -- Optional,Edits snmp user
            <remove_snmpuser>               -- Optional,removes snmp user
            <add_snmpv3_trapdestination>    -- Optional, for adding snmp trap destination. Accept multiple nodes.
            <edit_snmpv3_trapdestination>   -- Optional, for editing existing snmp trap destination. Accept multiple nodes.
            <remove_snmpv3_trapdestination> -- Optional, for removing existing snmp trap destination. Accept multiple nodes.
        </snmpv3>
    <li>
    * Required Arguments
    ** Applicable only for feature toggle in OVF292/OVF293
        Example:
        data/li -> @{TestData.li}
        <li name="LI-LE">
            <snmpv3 snmpv3enabled ="true" readcommunity="public" syscontact="none">
                <adduser action="add" username="user1" security_level="none"></adduser>
                <edit_snmpuser action="add" username="user2" security_level="none"></edit_snmpuser>
                <edit_snmpuser action="edit" ausernmae="user2" auth_protocol="MD5"
                              authentication_password="Password1" confirm_auth_password="Password1"
                              priv_protocol="AES-192" privacy_password="Password2"
                              confirm_priv_password="Password2"></edit_snmpuser>

                <remove_snmpuser user="user1"></remove_snmpuser>
                <add_snmpv3_trapdestination action="add" trapdestination="192.168.148.11"  trapformat="snmpv3" notification_type="Trap"  snmp_user="user1" ></add_snmpv3_trapdestination>
                <edit_snmpv3_trapdestination action="edit" trapdestination="192.168.148.11" new_trapdestination="10.101.11.1" trapformat="snmpv3" notification_type="Trap"  snmp_user="user2" ></edit_snmpv3_trapdestination>
                <remove_snmpv3_trapdestination trapdestination="10.101.11.1"> </remove_snmpv3_trapdestination>
            </snmpv3>
        </li>
    """
    s2l = ui_lib.get_s2l()

    if not s2l._is_element_present(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        navigate()
    if isinstance(editlis_obj, test_data.DataObj):
        editlis_obj = [editlis_obj]
    elif isinstance(editlis_obj, tuple):
        editlis_obj = list(editlis_obj[0])

    for logicalinterconnects in editlis_obj:
        navigate()
        editliname = logicalinterconnects.name
        if not select_logical_interconnect(editliname):
            logging._warn("Exiting Edit LI Function, Not selected LI %s" % editliname)
            continue
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_MENU_ACTION_LS_EDIT)
        s2l.wait_until_page_contains_element(FusionLogicalInterconnectsPage.ID_ELEMENT_EDIT_EDIT_LOGICAL_INTERCONNECTS)

        # CODE TO ADD LOGICAL UPLINK SET TO EXISTING LOGICAL INTERCONNECT
        if(logicalinterconnects.has_property("add_lus")):
            logger.info("entered")
            total_lus = len(logicalinterconnects.add_lus)
            for i, uplink_set in enumerate(logicalinterconnects.add_lus):
                logger.info("Add uplink set {2} No: {0} --- Total: {1} {2}".format((i + 1), total_lus, '-' * 14))
                if i < total_lus - 1:
                    _edit_li_create_uplink_set(uplink_set, add_plus=True)
                else:
                    _edit_li_create_uplink_set(uplink_set)
                # to Edit Li with QoS configuration
        if(logicalinterconnects.has_property("qos_configuration_type")):
            logger.info("select QOS section in LI page")
            EditLogicalInterconnects.select_quality_of_service_section()
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            logger.info("QOS selected")

        # CODE TO REMOVE AN UPLINK FROM AN INTERCONNECT
        if(logicalinterconnects.has_property("removeuplink")):
            for uplink in logicalinterconnects.removeuplink:
                blndeleteuplink = _delete_logical_interconnect_uplink(uplink)
                if blndeleteuplink:
                    logging._log_to_console_and_log_file("The uplink is removed successfully for logical interconnect is updated successfully %s" % uplink.name)
                else:
                    logging._warn("The uplink is not removed successfully for logical interconnect is updated successfully %s" % uplink.name)
        else:
            logging._log_to_console_and_log_file("User have not opted to delete uplink")

        # CODE TO EDIT GIVEN FC UPLINK FROM AN INTERCONNECT

        if(logicalinterconnects.has_property("edituplink")):
            for uplink in logicalinterconnects.edituplink:
                blisettings1 = _edit_logical_interconnect_fcuplink(uplink)
        # code to add Interconnect Settings
        if(logicalinterconnects.has_property("lisettings")):
            for settings in logicalinterconnects.lisettings:
                _add_logical_interconnect_settings(settings)
        else:
            logging._log_to_console_and_log_file("User dint provide any data for updating the interconnect settings in the data sheet")

        if(logicalinterconnects.has_property("lldpsettings")):
            for settings in logicalinterconnects.lldpsettings:
                _add_logical_interconnect_lldp_settings(settings)
        else:
            logging.info("User did not provide any data for updating the lldp settings in the data sheet")

        # code to add Utilization Sampling
        if(logicalinterconnects.has_property("utilizationsampling")):
            for utilizationsampling in logicalinterconnects.utilizationsampling:
                _add_logical_interconnect_utilizationsampling(utilizationsampling)
        else:
            logging._log_to_console_and_log_file("There is no data for editing the utilization sampling in the data sheet")

        # code to add SNMP
        if(logicalinterconnects.has_property("snmp")):
            for snmp in logicalinterconnects.snmp:
                _add_logical_interconnect_snmp(snmp)
        else:
            logging._log_to_console_and_log_file("User dint provide any data for editing the snmp data in the data sheet")

        # The below variant snmpv3 is appliacble only for feature toggle in OVF292 and OVF293
        if(logicalinterconnects.has_property("snmpv3")):
            FusionUIBase.select_view_by_name('SNMP')
            _add_logical_interconnect_snmpv3(logicalinterconnects.snmpv3)
        # code to add edit and delete SNMP traps to the interconnect
        if(logicalinterconnects.has_property("SNMPtraps")):
            for SNMPTrap in logicalinterconnects.SNMPtraps:
                if SNMPTrap.SNMPOperation == "Add":
                    blnSNMPTrap = add_SNMP_trap_dest(SNMPTrap)
                elif SNMPTrap.SNMPOperation == "Edit":
                    blnSNMPTrap = edit_SNMP_trap_dest(SNMPTrap)
                elif SNMPTrap.SNMPOperation == "Delete":
                    blnSNMPTrap = delete_SNMP_trap_dest(SNMPTrap)
                # Validation and reporting the status
                if blnSNMPTrap:
                    logging._log_to_console_and_log_file("The SNMP Trap destination is updated successfully for the logical interconnect %s" % SNMPTrap.destination)
                else:
                    logging._warn("The SNMP Trap destination is not updated successfully for the logical interconnect %s" % SNMPTrap.destination)
        else:
            logging._log_to_console_and_log_file("User dint provide any data for editing the snmp trap destination in the data sheet")

        # CODE TO ADD AND REMOVE SNMP ACCESS FOR AN INTERCONNECT
        if(logicalinterconnects.has_property("SNMPAccess")):
            for SNMP_Access in logicalinterconnects.SNMPAccess:
                if SNMP_Access.SNMPMode == "Add":
                    blnSNMPAccess = add_SNMP_Access(SNMP_Access)
                elif SNMP_Access.SNMPMode == "Delete":
                    blnSNMPAccess = delete_SNMP_Access(SNMP_Access)
                # Validation and reporting the status
                if blnSNMPAccess:
                    logging._log_to_console_and_log_file("The SNMP Access data is updated successfully for the logical interconnect %s" % SNMP_Access.subnet)
                else:
                    logging._warn("The SNMP Access data is not updated successfully for the logical interconnect %s" % SNMP_Access.subnet)
        else:
            logging._log_to_console_and_log_file("There is no data for editing the snmp access in the data sheet")

        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_LS_EDIT)
        if VerifyLogicalInterconnects.verify_uplinkset_error_message_visible(fail_if_false=False):
            error = VerifyLogicalInterconnects.get_uplinkset_error_message()
            logger.info("The error is %s" % error)
            CommonOperationLogicalInterconnect.click_create_uplinkset_cancel_button()
            EditLogicalInterconnects.click_edit_li_cancel_button()
            ui_lib.fail_test("failed to create uplinkset  %s" % error)
        elif VerifyLogicalInterconnects.verify_edit_li_error_message_visible(fail_if_false=False):
            error = EditLogicalInterconnects.get_edit_li_error_message()
            logger.info(error)
            EditLogicalInterconnects.click_edit_li_cancel_button()
            return error
        else:
            logger.info("proceed further")

        # Code to verify the detials which are edited are reflecting properly or not
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_LINK_OVERIVEW)

        # Validating interconnect settings
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_LINK_INTERCONNECT_SETTINGS)
        if(logicalinterconnects.has_property("lisettings")):
            for settings in logicalinterconnects.lisettings:
                ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_MAC_FAILOVER, PerfConstants.DEFAULT_SYNC_TIME)
                strMACachefailover = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_MAC_FAILOVER)
                strMACrefreshinterval = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_MAC_REFRESH_INTERVAL)
                strIGMPSnooping = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_IGMP_SNOOPING)
                strIGMPSnoopinginterval = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_IGMP_SNOOPING_INTERVAL)
                if strMACachefailover == "Enabled" and settings.cachefailover == "True":
                    blnTemp = "True"
                elif strMACachefailover == "Disabled" and settings.cachefailover == "False":
                    blnTemp = "True"
                else:
                    blnTemp = "False"
                strrefreshinterval = settings.refreshinterval
                if strrefreshinterval in strMACrefreshinterval:
                    blnTemp1 = "True"
                else:
                    blnTemp1 = "False"
                if strIGMPSnooping == "Enabled" and settings.IGMPSnooping == "True":
                    blnTemp2 = "True"
                elif strIGMPSnooping == "Disabled" and settings.IGMPSnooping == "False":
                    blnTemp2 = "True"
                else:
                    blnTemp2 = "False"
                stridletimeoutinterval = settings.idletimeoutinterval
                if stridletimeoutinterval in strIGMPSnoopinginterval:
                    blnTemp3 = "True"
                else:
                    blnTemp3 = "False"
                if blnTemp == "True" and blnTemp1 == "True" and blnTemp2 == "True" and blnTemp3 == "True":
                    logging._log_to_console_and_log_file("The interconnect settings are updated successfully for the interconnect %s " % logicalinterconnects.name)
                else:
                    logging._warn("The interconnect settings are not updated successfully for the interconnect %s " % logicalinterconnects.name)

        # Validating utilization sampling
        if(logicalinterconnects.has_property("utilizationsampling")):
            for utilizationsampling in logicalinterconnects.utilizationsampling:
                strintervalbetweensamples = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_INTERVAL_BETWEEN_SAMPLES)
                strnumberofsamples = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_TOTAL_NUMBER_OF_SAMPLES)

                strIntsamples = utilizationsampling.Intsamples
                if strIntsamples in strintervalbetweensamples:
                    blnTemp = "True"
                else:
                    blnTemp = "False"
                strtotalnumbersamples = utilizationsampling.totalnumbersamples
                if str(strtotalnumbersamples) in str(strnumberofsamples):
                    blnTemp1 = "True"
                else:
                    blnTemp1 = "False"
                if blnTemp == "True" and blnTemp1 == "True":
                    logging._log_to_console_and_log_file("The utilization sampling settings are updated successfully for the interconnect %s " % logicalinterconnects.name)
                else:
                    logging._warn("The utilization sampling settings are not updated successfully for the interconnect %s " % logicalinterconnects.name)

        # Validating SNMP settings
        if(logicalinterconnects.has_property("snmp")):
            for snmp in logicalinterconnects.snmp:
                strSNMPstatus = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP)
                strsystemcontact = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SYSTEM_CONTACT)
                strcommstring = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_COMM_STRING)
                if strSNMPstatus == "Enabled" and snmp.snmpen == "True":
                    blnTemp = "True"
                elif strSNMPstatus == "Disabled" and snmp.snmpen == "False":
                    blnTemp = "True"
                else:
                    blnTemp = "False"
                if strsystemcontact.lower() == (snmp.systemcontact).lower():
                    blnTemp1 = "True"
                else:
                    blnTemp1 = "False"
                if strcommstring.lower() == (snmp.community).lower():
                    blnTemp2 = "True"
                else:
                    blnTemp2 = "False"
                if blnTemp == "True" and blnTemp1 == "True" and blnTemp2 == "True":
                    logging._log_to_console_and_log_file("The SNMP settings are updated successfully for the interconnect %s " % logicalinterconnects.name)
                else:
                    logging._warn("The SNMP settings are not updated successfully for the interconnect %s " % logicalinterconnects.name)

        # Validating SNMP trap settings
        if(logicalinterconnects.has_property("SNMPtraps")):
            for SNMPTrap in logicalinterconnects.SNMPtraps:
                # Validating ADD SNMP trap settings
                if SNMPTrap.SNMPOperation == "Add":
                    blnTemp = s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_TRAP_DEST % SNMPTrap.destination)
                    if blnTemp:
                        strcommstring = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_COMM_STRING % SNMPTrap.destination)
                        strformat = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_FORMAT % SNMPTrap.destination)
                        strseverity = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_SEVERITY % SNMPTrap.destination)
                        strvcm = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_VCM % SNMPTrap.destination)
                        strvcenet = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_VCENET % SNMPTrap.destination)
                        strvcfc = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_VCFC % SNMPTrap.destination)
                        if strcommstring.lower() == (SNMPTrap.community).lower():
                            blnTemp6 = "True"
                        else:
                            blnTemp6 = "False"

                        if strformat.lower() == (SNMPTrap.Trapformat).lower():
                            blnTemp1 = "True"
                        else:
                            blnTemp1 = "False"

                        if strseverity.lower() == (SNMPTrap.Severity).lower():
                            blnTemp2 = "True"
                        elif strseverity == "All" and SNMPTrap.Severity == "Critical,Major,Minor,Warning,Normal,Info,Unknown":
                            blnTemp2 = "True"
                        else:
                            blnTemp2 = "False"

                        if strvcm.lower() == (SNMPTrap.VCMTraps).lower():
                            blnTemp3 = "True"
                        else:
                            blnTemp3 = "False"

                        if strvcenet.lower() == (SNMPTrap.VCEnetTraps).lower():
                            blnTemp4 = "True"
                        else:
                            blnTemp4 = "False"

                        if strvcfc.lower() == (SNMPTrap.VCFCTraps).lower():
                            blnTemp5 = "True"
                        else:
                            blnTemp5 = "False"
                        if blnTemp1 == "True" and blnTemp2 == "True" and blnTemp3 == "True" and blnTemp4 == "True" and blnTemp5 == "True" and blnTemp6 == "True":
                            logging._log_to_console_and_log_file("The given trap destination is added successfully to the particular interconnect %s" % logicalinterconnects.name)
                        else:
                            logging._log_to_console_and_log_file("The given trap destination is not added successfully to the particular interconnect %s" % logicalinterconnects.name)

                # Validating edit SNMP trap settings
                elif SNMPTrap.SNMPOperation == "Edit":
                    blnTemp = s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_TRAP_DEST % SNMPTrap.newdestination)
                    if blnTemp:
                        strcommstring = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_COMM_STRING % SNMPTrap.destination)
                        strformat = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_FORMAT % SNMPTrap.destination)
                        strseverity = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_SEVERITY % SNMPTrap.destination)
                        strvcm = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_VCM % SNMPTrap.destination)
                        strvcenet = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_VCENET % SNMPTrap.destination)
                        strvcfc = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_VCFC % SNMPTrap.destination)
                        if strcommstring == SNMPTrap.community:
                            blnTemp6 = "True"
                        else:
                            blnTemp6 = "False"

                        if strformat == SNMPTrap.Trapformat:
                            blnTemp1 = "True"
                        else:
                            blnTemp1 = "False"

                        if strseverity == SNMPTrap.Severity:
                            blnTemp2 = "True"
                        elif strseverity == "All" and SNMPTrap.Severity == "Critical,Major,Minor,Warning,Normal,Info,Unknown":
                            blnTemp2 = "True"
                        else:
                            blnTemp2 = "False"

                        if strvcm == SNMPTrap.VCMTraps:
                            blnTemp3 = "True"
                        else:
                            blnTemp3 = "False"

                        if strvcenet == SNMPTrap.VCEnetTraps:
                            blnTemp4 = "True"
                        else:
                            blnTemp4 = "False"

                        if strvcfc == SNMPTrap.VCFCTraps:
                            blnTemp5 = "True"
                        else:
                            blnTemp5 = "False"
                        if blnTemp1 == "True" and blnTemp2 == "True" and blnTemp3 == "True" and blnTemp4 == "True" and blnTemp5 == "True" and blnTemp6 == "True":
                            logging._log_to_console_and_log_file("The given trap destination is added successfully to the particular interconnect %s" % logicalinterconnects.name)
                        else:
                            logging._warn("The given trap destination is not added successfully to the particular interconnect %s" % logicalinterconnects.name)

                # Validating delete SNMP trap settings
                elif SNMPTrap.SNMPOperation == "Delete":
                    ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_MAC_FAILOVER % SNMPTrap.destination)
                    blnTemp = s2l._get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_MAC_FAILOVER % SNMPTrap.destination)
                    if not blnTemp:
                        logging._log_to_console_and_log_file("The delete SNMP Trap destination is not present for the interconnect %s " % logicalinterconnects.name)
                    else:
                        logging._warn("The delete SNMP Trap destination is present for the interconnect %s " % logicalinterconnects.name)

        # Validating SNMP Access settings
        if(logicalinterconnects.has_property("SNMPAccess")):
            for SNMP_Access in logicalinterconnects.SNMPAccess:
                if SNMP_Access.SNMPMode == "Add":
                    ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_ACCESS % SNMP_Access.subnet)
                    blnTemp = s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_ACCESS % SNMP_Access.subnet)
                    if blnTemp:
                        logging._log_to_console_and_log_file("The SNMP Access is added successfuilly for the interconnect %s " % logicalinterconnects.name)
                    else:
                        logging._warn("The SNMP Access is added successfuilly for the interconnect %s " % logicalinterconnects.name)
                elif SNMP_Access.SNMPMode == "Delete":
                    blnTemp = s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_ACCESS % SNMP_Access.subnet)
                    if not blnTemp:
                        logging._log_to_console_and_log_file("The SNMP Access is deleted successfuilly for the interconnect %s " % logicalinterconnects.name)
                    else:
                        logging._warn("The SNMP Access is not deleted successfuilly for the interconnect %s " % logicalinterconnects.name)

    return True


def update_logical_interconnect_from_group(li_obj):
    '''
    update the logical interconnect configuration from LIG
    '''
    failed_times = 0
    logger.info("Update logical interconnect from LIG")
    logger.info(li_obj)

    navigate()

    for li in li_obj:
        if not VerifyLogicalInterconnects.verify_logical_interconnect_exist(li.name, 10, False):
            logger.warn("Logical interconnect %s does not exist" % li.name)
            failed_times += 1
            continue
        else:
            CommonOperationLogicalInterconnect.click_logical_interconnect(li.name)
            # wait target logical interconnect get focus
            logger.info("Wait for logical interconnect %s to be selected." % li.name)

            if not CommonOperationLogicalInterconnect.wait_logical_interconnect_selected(li.name):
                logger.warn("Failed to select logical interconnect %s" % li.name)
                failed_times += 1
                continue
            li_type = VerifyLogicalInterconnects.verify_logical_interconnect_type(li.name)
            logger.info("Logical interconnect  type is %s" % li_type)
            if li_type == 'sas':
                update_li = UpdateFromGroupOperations.verify_and_click_sas_actions_update()
            elif li_type == 'nonsas':
                update_li = UpdateFromGroupOperations.verify_and_click_actions_update()
            logger.info("Update Logical interconnect from group is %s" % update_li)
            if update_li is True:
                UpdateFromGroupOperations.wait_update_from_group_dialog_shown()
                UpdateFromGroupOperations.click_yes_update_button()

                if UpdateFromGroupOperations.is_second_confirm_required() is True:
                    UpdateFromGroupOperations.tick_i_have_read_checkbox()
                    UpdateFromGroupOperations.click_yes_update_button_for_second_confirm()

                if UpdateFromGroupOperations.wait_update_from_group_dialog_disappear(timeout=180, fail_if_false=False):
                    FusionUIBase.show_activity_sidebar()
                    if FusionUIBase.wait_activity_action_ok(li.name, 'Update from group', timeout=900, fail_if_false=False):
                        logger.info("'wait_activity_action_ok' = TRUE for updating '%s' LI from group " % li.name)
                        FusionUIBase.show_activity_sidebar()
                    else:
                        logger.warn("'wait_activity_action_ok' = FALSE, skip to next logical interconnect ... ")
                        FusionUIBase.show_activity_sidebar()
                        continue

                CommonOperationLogicalInterconnect.wait_logical_interconnect_status_ok(li.name, timeout=180, fail_if_false=False)
            else:
                logger.info("Logical interconnect %s is as same as LIG, no need to update" % li.name)

    if failed_times > 0:
        logger.warn("There are more thant 1 update failed!")
        return False

    return True


def update_firmware_tbird_logical_interconnect(*objfwbundle):
    """
    This function will update the firmware for the interconnects present in the LI.

    DATAFILE EXAMPLE:
        <fwbuname basename="Hafnium 166 Chloride 106 Carbon 22 2016 07 08 version 2016.07.08.66" updateaction="Update firmware (stage + activate)"  force ="No"
                    mode = "Parallel" LIname="TestLE-LIG-Test-FWUP" appip="10.10.0.91"  appuname="root" appasswd="hpvse1" dcs="False" proceedonwarning="no">

                <enclosure name="WPSTENC100" emip="fe80::1658:d0ff:fe41:4330%bond0,fe80::1658:d0ff:fe41:43e0%bond0" />

        </fwbuname>

        attributes:
            basename *           -Firmware bundle to use for update
            updateaction*        - stage or stage_activation or activation only
            mode*                - parallel or orchestrated | default is orchestrated
            force                - yes or no
            LIname*               - LI to perform update on
            appip*               - appliance IP (CIM IP)
            appuname*            - appliance user name
            appasswd*            - appliance password
            dcs                 - True or False
            proceedonwarning    - yes or No

            <enclosure>*
                name*            - enclosure name as displayed
                emip*            - em ipv6 IPs , both the active and standby as a comma separated string , with the interface used in CIM mentioned

            * required attributes

    """
    logger.info("Upgrading Firmware")

    if isinstance(objfwbundle, test_data.DataObj):
        objfwbundle = [objfwbundle]
    elif isinstance(objfwbundle, tuple):
        objfwbundle = list(objfwbundle[0])

    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)

    for logicalinterconnet in objfwbundle:

        if not VerifyLogicalInterconnects.verify_logical_interconnect_exist(logicalinterconnet.LIname, 5, False):
            logger.warn("Logical interconnect %s does not exist" % logicalinterconnet.LIname)
            continue
        else:
            CommonOperationLogicalInterconnect.click_logical_interconnect(logicalinterconnet.LIname, 5, False)
            # wait target logical interconnect get focus
            logger.info("Wait for logical interconnect %s to be selected." % logicalinterconnet.LIname)

            if not CommonOperationLogicalInterconnect.wait_logical_interconnect_selected(logicalinterconnet.LIname, 5, False):
                logger.warn("Failed to select logical interconnect %s" % logicalinterconnet.LIname)
                continue

        TBirdLogicalInterconnectsUpdateFirmware.click_action_button(timeout=10)
        TBirdLogicalInterconnectsUpdateFirmware.click_action_update_firmware(timeout=10)

        TBirdLogicalInterconnectsUpdateFirmware.wait_and_select_update_action(logicalinterconnet.updateaction)

        if str(logicalinterconnet.updateaction).lower() != "activate firmware":
            TBirdLogicalInterconnectsUpdateFirmware.select_firmware_baseline(logicalinterconnet.basename)
            if str(logicalinterconnet.force).lower() == "yes":
                TBirdLogicalInterconnectsUpdateFirmware.click_force_installation_checkbox()

        if str(logicalinterconnet.updateaction).lower() != "stage firmware for later activation":
            if logicalinterconnet.mode.lower() == 'orchestrated':
                TBirdLogicalInterconnectsUpdateFirmware.choose_activation_type_orchestrated()
            elif logicalinterconnet.mode.lower() == 'parallel':
                TBirdLogicalInterconnectsUpdateFirmware.choose_activation_type_parallel()
            else:
                ui_lib.fail_test("Please check activation type, Only 'Orchestrated, Parallel' allowed")

        if logicalinterconnet.updateaction.lower() == "activate firmware":
            if TBirdLogicalInterconnectsUpdateFirmware.wait_and_check_module_not_available_warning_exists():
                message = TBirdLogicalInterconnectsUpdateFirmware.get_module_not_available_warning()
                TBirdLogicalInterconnectsUpdateFirmware.click_update_firmware_cancel_button()
                ui_lib.fail_test(message, True)

        TBirdLogicalInterconnectsUpdateFirmware.click_update_firmware_ok_button()

        if TBirdLogicalInterconnectsUpdateFirmware.check_not_supported_for_orchestrated_warning(timeout=60, fail_if_false=False):
            if logicalinterconnet.proceedonwarning.lower() == 'yes':
                TBirdLogicalInterconnectsUpdateFirmware.click_update_firmware_ok_button()
            else:
                TBirdLogicalInterconnectsUpdateFirmware.click_update_firmware_cancel_button()
                ui_lib.fail_test('Update firmware warning shown', True)

        if not VerifyLogicalInterconnects.verify_update_firmware_started(timeout=60, fail_if_false=False):
            # If update firmware not started, trying to collect notification messages, and failing tests
            if TBirdLogicalInterconnectsUpdateFirmware.click_and_expand_update_firmware_status():
                update_msg = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_success_notification(fail_if_false=False)
                logger.info("Update message in success block is:" + update_msg)
                if update_msg is None:
                    update_msg = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_warning_notification(fail_if_false=False)
                    logger.info("Update message in success block is:" + update_msg)
            ui_lib.fail_test("Firmware update has not started, Something went wrong", True)
        else:
            # Update firmware started, then process the below
            TBirdLogicalInterconnectsUpdateFirmware.click_and_expand_update_firmware_status()

            startTime = datetime.now()
            timeOutAt = startTime + timedelta(seconds=PerfConstants.FIRMWARE_UPDATE_TIMEOUT)

            while True:
                if VerifyLogicalInterconnects.verify_update_firmware_progressbar_is_visible(fail_if_false=False):
                    message = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_progressbar_state_message(fail_if_false=False)
                    logger.info("Upgrade still in progress, State: " + message)

                    if TBirdLogicalInterconnectsUpdateFirmware.wait_for_update_firmware_success(timeout=30, fail_if_false=False):
                        logger.info("Update firmware successfully completed")
                else:
                    logger.info("Progress completed")
                    break

                if not datetime.now() < timeOutAt:
                    ui_lib.fail_test("Maximum timeout reached. Started '{0}' and exited at '{1}'".format(startTime, timeOutAt), True)

            # Is completed with success message
            if TBirdLogicalInterconnectsUpdateFirmware.wait_for_update_firmware_success(fail_if_false=False):
                logger.info(" In the success block")
                time = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_time_taken()
                logger.info(" The firmware updated started for the LI" + logicalinterconnet.LIname + "is %s time " % time)

                update_msg = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_success_notification()
                logger.info("update message in success block is:" + update_msg)
                LIname = str(logicalinterconnet.LIname)

                if logicalinterconnet.updateaction.lower() == "stage firmware for later activation":
                    if "Stage complete" in update_msg:
                        logger.info("Firmware is successfully staged to %s version to update interconnect" % logicalinterconnet.basename)
                        LImessage_list = ["Staging started for logical interconnect %s" % (logicalinterconnet.LIname),
                                          "Stage success for logical interconnect %s" % (logicalinterconnet.LIname)]
                        alertspresent = verify_tbird_updatefirmwarealerts_li(LImessage_list)
                        if(alertspresent):
                            logger.info("The required alerts are found in LI activity page")
                        else:
                            logger.warn("The required alerts are not found in LI activity page, Please check")

                        (status, ic_firm, ic_installedversion) = validate_interconnect_firmware_from_li(logicalinterconnet)

                        for key in ic_firm and ic_installedversion:
                            message_list = ["Staging started for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key]),
                                            "Staging success for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key])]

                            logger.info("Now at the interconnect %s" % key)
                            if interconnects.verify_interconnect_recent_activity(key, message_list):
                                logger.info("All the expected alerts are present in interconnects page")
                            else:
                                ui_lib.fail_test("The expected alerts are not found in interconnects %s" % key, True)
                    else:
                        ui_lib.fail_test(update_msg, True)

                elif logicalinterconnet.updateaction.lower() == "activate firmware":
                    if "Activate complete" in update_msg:
                        logger.info("Interconnects are successfully activated to the %s baseline version" % logicalinterconnet.basename)
                        LImessage_list = ["Activation started for logical interconnect %s" % (logicalinterconnet.LIname),
                                          "Activate success for logical interconnect %s" % (logicalinterconnet.LIname)]
                        alertspresent = verify_tbird_updatefirmwarealerts_li(LImessage_list)
                        if(alertspresent):
                            logger.info("The required alerts are found in LI activity page")
                        else:
                            logger.info("The required alerts are not found in LI activity page, Please check")
                        (status, ic_firm, ic_installedversion) = validate_interconnect_firmware_from_li(logicalinterconnet)
                        logger.info("Status of all interconnects firmware version validation is %s" % status)
                        logger.info("But any case proceeding with alerts validation in interconnect page")
                        if status:
                            for key in ic_firm and ic_installedversion:
                                message_list = ["Activation started for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key]),
                                                "Activation success for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key])]

                                if interconnects.verify_interconnect_recent_activity(key, message_list):
                                    logger.info("All the expected alerts are present in interconnects page")
                                else:
                                    ui_lib.fail_test("The expected alerts are not found in interconnects %s" % key, True)
                            logger.info("All the interconnects are updated as expected. Checking done ")
                        else:
                            ui_lib.fail_test("All the interconnects are not updated as expected.Please check", True)
                    else:
                        ui_lib.fail_test(update_msg, True)

                elif logicalinterconnet.updateaction.lower() == "update firmware (stage + activate)":
                    if "Stage complete" and "Activate complete" in update_msg:
                        logger.info("Update firmware action(Stage+Activate) is successful")
                        LImessage_list = ["Update started for logical interconnect %s" % (logicalinterconnet.LIname),
                                          "Update success for logical interconnect %s" % (logicalinterconnet.LIname)]
                        alertspresent = verify_tbird_updatefirmwarealerts_li(LImessage_list)
                        if(alertspresent):
                            logger.info("The required alerts are found in LI activity page")
                        else:
                            logger.info("The required alerts are not found in LI activity page, Please check")
                        (status, ic_firm, ic_installedversion) = validate_interconnect_firmware_from_li(logicalinterconnet)
                        if status:
                            for key in ic_firm and ic_installedversion:
                                message_list = ["Staging started for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key]),
                                                "Staging success for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key]),
                                                "Activation started for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key]),
                                                "Activation success for the interconnect %s with firmware version %s from baseline" % (key, ic_firm[key])]

                                if interconnects.verify_interconnect_recent_activity(key, message_list):
                                    logger.info("All the expected alerts are present in interconnects page")
                                else:
                                    ui_lib.fail_test("The expected alerts are not found in interconnects page", True)
                        else:
                            ui_lib.fail_test("All the interconnects are not updated as expected.Please check", True)
                    else:
                        ui_lib.fail_test(update_msg, True)

            # Is completed with warning message
            elif TBirdLogicalInterconnectsUpdateFirmware.wait_for_update_firmware_warning(fail_if_false=False):
                message = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_warning_notification()
                logger.info("Firmware Update action you started has some warnings, Please check \n")
                logger.info("\n" + message)
                ui_lib.fail_test(message, True)

            # Is completed with error message
            elif TBirdLogicalInterconnectsUpdateFirmware.wait_for_update_firmware_error(fail_if_false=False):
                logger.info("Firmware Update is failed")
                message = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_error_notification(timeout=15)
                logger.info("\n" + message)

                # code to extract the interconnects name on which the activation is failed
                if "Stage failed" not in message:
                    temp1 = message.split(":")[1]
                    string = temp1.lstrip()
                    span = 3
                    words = string.split(" ")
                    newlist = []
                    for i in range(0, len(words), span):
                        str1 = words[i] + ' ' + words[i + 1] + ' ' + words[i + 2]
                        logger.info("\n" + str1)
                        newlist.append(str1)
                    logger.info(newlist)

                    for Interconnectlist in newlist:
                        interconnects.select_interconnect(Interconnectlist)
                        errortext = CommonOperationInterconnects.get_error_message_notification()
                        logger.info("\n Error message from interconnect page is:\n" + errortext)
                    logger.info("Displayed the list of failed interconnects and their corresponding errors")

                ui_lib.fail_test(message, True)

            else:
                ui_lib.fail_test("Failed to verify update firmware through LI.", True)
    # If control reaches here, then looks everything went fine, returning positive response.
    return True


def update_firmware_tbird_natasha_li_affected_components(objlogicalinterconnect):
    """
    This function will verify affected components tables exists when update the firmware for the SAS LI.
    """
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS)

    for logicalconnect in objlogicalinterconnect:
        if hasattr(logicalconnect, 'LIname'):
            CommonOperationLogicalInterconnect.click_logical_interconnect(logicalconnect.LIname)

        logging.debug("Opening Update firmware Dialog")

        UpdateLogicalInterconnectFirmware.click_sas_actions_update_firmware()

        return UpdateLogicalInterconnectFirmware.verify_sas_li_fw_affected_components_table()


def update_firmware_tbird_natasha_li(objfwbundle):
    """
    This function will update the firmware for the interconnects present in the LI.
    """
    logger.info("upgrading firmware for natasha li")

    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS)

    selenium2lib = ui_lib.get_s2l()

    for logicalconnect in objfwbundle:
        error = 0
        if hasattr(logicalconnect, 'LIname'):
            CommonOperationLogicalInterconnect.click_logical_interconnect(logicalconnect.LIname)

        UpdateLogicalInterconnectFirmware.click_sas_actions_update_firmware()

        logging.debug("Opening Update firmware Dialog")
        if hasattr(logicalconnect, "updateaction"):
            UpdateLogicalInterconnectFirmware.select_update_option(logicalconnect.updateaction)
        if hasattr(logicalconnect, "basename"):
            UpdateLogicalInterconnectFirmware.select_firmware_baseline(logicalconnect.basename)
        if hasattr(logicalconnect, "force"):
            UpdateLogicalInterconnectFirmware.check_force_option(logicalconnect.force)
        if hasattr(logicalconnect, "mode"):
            UpdateLogicalInterconnectFirmware.select_activation_mode(logicalconnect.mode)

        UpdateLogicalInterconnectFirmware.click_ok_button()

        if UpdateLogicalInterconnectFirmware.verify_update_firmware_notification():
            return UpdateLogicalInterconnectFirmware.check_update_firmware_status(logicalconnect)
        else:
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_CLICK_MAINPANE, 2):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_CLICK_MAINPANE, 2)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_NEW_SELECT_ALERT, 2)
                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ACTIVITY_NEW_SUCCESS_DETAILS, 2):
                    update_msg = selenium2lib.get_text(FusionLogicalInterconnectsPage.ID_ACTIVITY_NEW_SUCCESS_DETAILS)
                    logging.debug("update message in success block is:" + update_msg)
                elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ACTIVITY_NEW_WARNING_DETAILS, 2):
                    update_msg = selenium2lib.get_text(FusionLogicalInterconnectsPage.ID_ACTIVITY_NEW_WARNING_DETAILS)
                return update_msg
            else:
                logger.debug("Firmware update has not started because of the reason mentioned below")
                error1 = ui_lib.get_text("//*[@id='hp-form-message']/div[1]/span")
                error2 = ui_lib.get_text("//*[@id='hp-form-message']/div[1]/following-sibling::div[@class='hp-form-message-details']")
                logger.debug("Displaying the error message from UI \n" + error1)
                logger.debug("\n" + error2)
                error += 1
                logging.debug("error count is:%d" % error)
                UpdateLogicalInterconnectFirmware.click_cancel_button()
                return error2


def verify_tbird_updatefirmwarealerts_li(message_list):
    """
    This function will navigate to the activity page and will validate the LI related alerts. Input is a list
    of messages that needs to be validated.
    """

    found = 0
    if not FusionUIBase.select_view_by_name("Activity"):
        return False

    for message in message_list:

        if CommonOperationLogicalInterconnect.wait_logical_interconnect_activity_message(message, timeout=15):
            timeago = TBirdLogicalInterconnectsUpdateFirmware.get_timeago_text_from_li_activity_tab(message)
            logger.debug("Event found at -  %s" % timeago)

            # look for the activity message in last two hours
            if (timeago):
                if timeago[1].lower() == "hours" and int(timeago[0]) > 2:
                    logger.warn("Expected message %s found is not within last 2 hours!! Discarding Old activity Message" % message)
                    continue
                elif timeago[1].lower() in ("months", "year", "years"):
                    logger.warn("Expected message '{}' found is of '{}'!!".format(message, timeago))
                    continue
                found += 1
                logger.debug("\nActivity : '%s'  found in IC activity page" % message)
            else:
                logger.debug("\nMessage %s is found but testscript failed to extract exact time" % message)
                continue

        else:
            logger._warn("Expected message '%s' is not found in activity page:" % message)

    if (found == len(message_list)):
        logger.info("All the excepted messages found in LI activity page", also_console=True)
        return True
    else:
        logger.info("All the excepted messages are not found in LI activity page", also_console=True)
        return False


def validate_interconnect_firmware_from_li(objfwbundle):
    """
    This function will compare interconnect installed firmware with baseline firmware. Imput is a list
    of logical interconnects.
    """

    if isinstance(objfwbundle, test_data.DataObj):
        objfwbundle = [objfwbundle]
    elif isinstance(objfwbundle, tuple):
        objfwbundle = list(objfwbundle[0])

    emip = dict()
    ic_firm = dict()
    ic_installedversion = dict()

    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)

    error_flag = 0
    for logicalconnect in objfwbundle:

        for enc in logicalconnect.enclosure:
            emip[enc.name] = enc.emip

        logger.debug("EM ip got here is :{}".format(emip))
        logger.debug("Getting the list of interconnects and firmware versions")

        if not FusionUIBase.select_view_by_name("Firmware"):
            return False

        length = TBirdLogicalInterconnectsUpdateFirmware.get_interconnect_count_from_firmware_table()
        logger.info("The number of ics is %s" % length)

        # If no interconnect is listed in firmware table
        if length == 0:
            return (False, ic_firm, ic_installedversion)

        if str(logicalconnect.updateaction).lower() != "stage firmware for later activation":

            for index in xrange(1, length + 1):
                (ic, installed_fw, baseline_fw) = TBirdLogicalInterconnectsUpdateFirmware.get_firmware_details(index)
                m = re.match(".*/.*/", installed_fw)
                if m:
                    installed_fw = installed_fw.split()[0]
                ic_firm[ic] = baseline_fw
                ic_installedversion[ic] = installed_fw

                if baseline_fw != installed_fw:
                    logger.debug("Installed firmware '{0}' on interconnect '{1}' is not same as baseline firmware '{2}'".format(installed_fw, ic, baseline_fw))
                    error_flag = error_flag + 1
                else:
                    logger.debug("Installed firmware '{0}' on interconnect '{1}' is same as baseline firmware '{2}'".format(installed_fw, ic, baseline_fw))

                data = ic.split(",")
                enc_name = data[0]
                ic_bay_number = data[1].split()[1]
                logger.debug("Enclosure name : %s , bay : %s" % (enc_name, ic_bay_number))

                dcs = False
                if logicalconnect.dcs == 'True':
                    dcs = True
                ic_version = interconnects.verify_tbird_ic_version(emip[enc_name], enc_name, ic_bay_number, logicalconnect.appip, logicalconnect.appuname, logicalconnect.appasswd, dcs=dcs)
                if ic_version:
                    if(ic_version.split(' ')[-1] in installed_fw or installed_fw.split('.')[-1] in ic_version):
                        logger.debug("The firmware version expected is installed in the interconnect. The version returned is %s " % ic_version)
                    else:
                        logger.warn("The firmware version expected is not installed in the interconnect")
                        error_flag = error_flag + 1
                else:
                    logger.warn("IC version is unable to get with EM details provided...please re-check EM details")
                    error_flag = error_flag + 1

            if(error_flag != 0):
                logger.warn("Some mismatch in the versions comparison, please check")
                return (False, ic_firm, ic_installedversion)
            else:
                logger.debug(" Versions comparisons went well, Firmware activation is successful")
                return (True, ic_firm, ic_installedversion)

        else:
            logger.debug("Entered else part")

            for index in xrange(1, length + 1):
                (ic, installed_fw, baseline_fw) = TBirdLogicalInterconnectsUpdateFirmware.get_firmware_details(index)
                baseline_fw = baseline_fw.split()[0]
                ic_firm[ic] = baseline_fw
                ic_installedversion[ic] = installed_fw
                logger.debug("Baseline firmware: '%s'" % baseline_fw)

            return (True, ic_firm, ic_installedversion)


def update_firmware(*firmwareBase_obj):
    '''
    "[LEGACY]"
    update_firmware function to update the firmware on different  interconnects
    '''

    bflag = True
    error_string, error_status, errors_on_form, upgradefor = '', '', '', ''
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()
    logging._log_to_console_and_log_file("Updating Li firmware ....")
    if isinstance(firmwareBase_obj, test_data.DataObj):
        firmwareBase_obj = [firmwareBase_obj]
    elif isinstance(firmwareBase_obj, tuple):
        firmwareBase_obj = list(firmwareBase_obj[0])
    for firmwareBase in firmwareBase_obj:
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_LI_XPATH % firmwareBase.name)
        firmware_baseline = selenium2lib.get_text(FusionLogicalInterconnectsPage.ID_FIRMWARE_BASELINE)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_MENU_ACTION_UPDATE_FIRMWARE)
        logger.info("Navigating to update firmware page")
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_UPDATE_ACTION)
        logger.info("Clicked UPDATE_ACTION and it is visible")
        ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_SELECT_UPDATE_ACTION % firmwareBase.updateaction, PerfConstants.DEFAULT_SYNC_TIME)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_UPDATE_ACTION % firmwareBase.updateaction)
        logger.info("Checking update action to perform")
        # Perform the activation  of already Staged firmware
        if (str(firmwareBase.updateaction) == "Activate firmware"):
            logger.info("Inside active FW update Block\n")
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_UPDATE_ACTION % firmwareBase.updateaction)
            firmware_baseline = selenium2lib.get_text(FusionLogicalInterconnectsPage.ID_GET_FIRMWAREBASELINE)
            logger.info("Firmware version from oneview : " + str(firmware_baseline))
            if (firmware_baseline == firmwareBase.updateFirmware):
                if selenium2lib._is_element_present(FusionLogicalInterconnectsPage.ID_VALIDATE_ACTIVATE_FIRMWARE):
                    logger.info("Firmware with baseline %s is already activated" % firmwareBase.updateFirmware)
                    bflag = False
                else:
                    logger.info("Selecting firmware for : " + str(firmwareBase.updateaction))
                    logger.info("In the Activate Block ")
                    if (str(firmwareBase.ethernetupdate) == "Parallel") or (str(firmwareBase.ethernetupdate) == "Serial") or (str(firmwareBase.ethernetupdate) == "Odd/even"):
                        logger.info(" Inside a Ethernet update selection ")
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ETHERNET_CH_XPATH)
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ETHERNET_CHANNEL_XPATH % firmwareBase.ethernetupdate)

                    if (str(firmwareBase.ethrdelay) == "Yes"):
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_ETHRE_DELAY_XPATH)
                        ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_XPATH_ETHRE_DELAY_XPATH, firmwareBase.ethrdelayvalue)

                    if (str(firmwareBase.neg_delay) == "Yes"):
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_ETHRE_DELAY_XPATH)
                        ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_XPATH_ETHRE_DELAY_XPATH, firmwareBase.neg_delayeth_value)

                    # Check the error message on  ethernet section
                    if (str(firmwareBase.select_neg) == "Yes"):
                        eth_unselect_error_msg = ''
                        ethselectlist = firmwareBase.ethselect_neg.split(',')
                        for ebay in ethselectlist:
                            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_XPATH_ETHERNET_SELECT % str(ebay)):

                                logging._log_to_console_and_log_file("Unselecting ethernet interconnect : " + str(ebay))
                                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_ETHERNET_SELECT % str(ebay))
                            else:
                                logging._warn("Ethernet interconnects not available ")
                                bflag = False
                        eth_unselect_error_msg = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_XPATH_ETH_INTERCONNECTS)
                        import re
                        pm = re.search('Select at least one interconnect for activation', eth_unselect_error_msg)
                        if pm:
                            logger.info("Found the Error message on ethernet elective section- {}".format(pm.group()))
                        else:

                            logger.warn("not Found the Error message")
                            bflag = False

                    if (str(firmwareBase.ethselective) == "Yes"):
                        elist = firmwareBase.ethselectivebay.split(',')
                        for ebay in elist:
                            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_XPATH_ETHERNET_SELECT % str(ebay)):
                                logger.info("unselecting ethernet interconnect : " + str(ebay))
                                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_ETHERNET_SELECT % str(ebay))
                            else:
                                logger.warn("Ethernet interconnects not available ")
                                bflag = False
                    if (str(firmwareBase.fiberchannelupdate) == "Parallel") or (str(firmwareBase.fiberchannelupdate) == "Serial") or (str(firmwareBase.fiberchannelupdate) == "Odd/even"):
                        logger.info(" Inside a Fiber channel update selection ")
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FIBER_FC_CHANNEL_XPATH)
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_FC_XPATHA % firmwareBase.fiberchannelupdate)

                    # check error msg on activate page

                        if (str(firmwareBase.select_neg) == "Yes"):
                            fc_unselect_error_msg = ''
                            fcselectlist = firmwareBase.fcselect_neg.split(',')
                            for ebay in fcselectlist:
                                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_XPATH_FC_SELCTIVE % str(ebay)):

                                    logging._log_to_console_and_log_file("Unselecting FC interconnect : " + str(ebay))
                                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_FC_SELCTIVE % str(ebay))
                                else:
                                    logging._warn("FC interconnects not available ")
                                    bflag = False
                            fc_unselect_error_msg = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_XPATH_FC_INETRCONNECTS)

                            pm = re.search('Select at least one interconnect for activation', fc_unselect_error_msg)
                            if pm:
                                logger.info("Found the Error message on fc selective section - {}".format(pm.group()))
                            else:

                                logger.warn("not Found the Error message on fc section")
                                bflag = False

                        if (str(firmwareBase.fiberdelay) == "Yes"):
                            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_FIBER_DELAY_XPATH)
                            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_XPATH_FIBER_DELAY_XPATH, firmwareBase.fiberdelayvalue)

                        if (str(firmwareBase.neg_delay) == "Yes"):
                            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_FIBER_DELAY_XPATH)
                            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_XPATH_FIBER_DELAY_XPATH, firmwareBase.neg_delayfc_value)
                            ui_lib.scroll_into_view(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
                            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
                            delay_eth_error_msg = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_ethrnet_empydelay_err)
                            delay_fc_error_msg = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_FC_empt_del_err)
                            pmeth = re.search('This field is required', delay_eth_error_msg)
                            pmfc = re.search('This field is required', delay_fc_error_msg)
                            if pmeth:
                                logger.info("Found the Error message on FCdelay section - {}".format(pmeth.group()))
                            else:
                                logger.warn("not Found the Error message on fc section")
                                bflag = False
                            if pmfc:
                                logger.info("Found the Error message on on fcdelay section - {}".format(pmfc.group()))
                            else:

                                logger.warn("not Found the Error message on  fc section")
                                bflag = False
                            # if form is still seen click cancel
                            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                                logger._log_to_console_and_log_file("Clicking Cancel")
                                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)

                        if (str(firmwareBase.fcselective) == "Yes"):
                            flist = firmwareBase.fcselective.split(',')
                            for fbay in flist:
                                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_XPATH_FC_SELCTIVE % str(fbay)):
                                    logger.info("Un selecting fc interconnect : " + str(fbay))
                                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_FC_SELCTIVE % str(fbay))
                                else:
                                    logger.warn("FC interconnects not available ")
                        if firmwareBase.negbb_triggeronly == 'Yes':

                            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE):
                                logging._log_to_console_and_log_file("Inside neg test on LI activation Firmware")
                                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
                                return True
                            else:
                                logger.warn("OK button not appeared on LI page")
                                return False
                        else:
                            ui_lib.scroll_into_view(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
                            if not ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE):
                                logger.info("OK button not visible\n")
                                # if active form is still seen click cancel
                                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                                    logger._log_to_console_and_log_file("Clicking Cancel")
                                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)
                                    return False
                            ''' Check error messages appears on LI FW update page '''
                            logger.info("Checking For Errors - After clicking on OK Button of Firmware update in LI page")
                            if not ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM, FusionLogicalInterconnectsPage.WAIT_TIME):
                                errors_on_form = base_page.get_errors_on_form(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM)
                                error_status = ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_HP_STATUS_ERROR, FusionLogicalInterconnectsPage.WAIT_TIME)
                            if error_status or errors_on_form:
                                if errors_on_form:
                                    error_string += errors_on_form + "\t"
                                if error_status:
                                    logger.warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY)))
                                    logger._log_to_console_and_log_file("Inside error check .... ")
                                    bflag = False
                                    logger.warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS)))
                                    bflag = False
                                    error_string += ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS) + "\t"
                                # if form is still seen click cancel
                                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                                    logger.info("Clicking Cancel")
                                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)
                            else:
                                logger.info("No errors Seen on LI Firmware update page")
                            ''' # Check the Progress of Firmware upgrade on LI page  '''
                            # Added the code for measure progress of activation of  already staged firmware
                            timeout = 0
                            start_active = datetime.now()
                            while timeout < FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
                                if (ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_PROGRESS_BAR, PerfConstants.DEFAULT_SYNC_TIME)):
                                    logger.info("Activation of staged Firmware  is in Progress in LI and waited for " + str(timeout))
                                if (ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_CMPLETE_XPATH, PerfConstants.DEFAULT_SYNC_TIME)):
                                    logger.info("Firmware activation Completed on LI page.\n")
                                    bflag = True
                                    break
                                elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_WARNING_XPATH, FusionLogicalInterconnectsPage.UPDATE_WAIT_TIME):
                                    logger.warn("Firmware activation Completed but with warning on LI page")
                                    bflag = False
                                    break
                                elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ERROR_XPATH, FusionLogicalInterconnectsPage.UPDATE_WAIT_TIME):
                                    logger.warn("Error during Firmware activation on LI page")
                                    bflag = False
                                    break

                                timeout = (datetime.now() - start_active).seconds
                            if timeout > FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
                                logger.warn("Either FW Upgrade of LI '{}' has not completed , even after waiting for {} minutes!!".format(firmwareBase.name, timeout))
                                bflag = False
                                error_string += "Either FW Upgrade of LI '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!\t".format(firmwareBase.name, timeout)
                            # if add form is still seen click cancel
                            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                                logger.info("Clicking Cancel")
                                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)
                            if ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_UPDATE_SUCCESS % firmwareBase.name, PerfConstants.LOGICAL_INTERCONNECT_UPDATE_FIRMWARE):
                                logger.info("Firmware Update is success")
                                bflag = True
                            elif ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_UPDATE_WARNING % firmwareBase.name, PerfConstants.LOGICAL_INTERCONNECT_UPDATE_FIRMWARE):
                                logger.warn("Firmware Update is done with warnings")
                            elif ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_UPDATE_FAILED % firmwareBase.name, PerfConstants.LOGICAL_INTERCONNECT_UPDATE_FIRMWARE):
                                logger.warn("Firmware Update is failed")
            else:
                raise ValueError("The given firmware baseline is invalid")
                bflag = False

        elif (str(firmwareBase.updateaction) == "Stage firmware for later activation"):
            logger.info("1.In Stage firmware for later activation FW upgrade")
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_UPDATE_ACTION % firmwareBase.updateaction, 15)
            logger.info("Selecting firmware for : " + str(firmwareBase.updateaction))
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_CLICK_UPDATE_FiRMWARE_FOR, 25)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_FIRMWARE_DROPDOWN % firmwareBase.updateFirmware)
            if (str(firmwareBase.force) == "Yes"):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_CHKBOX_FORCE_FIRMWARE_UPDATE)
            ui_lib.scroll_into_view(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
            logger.info("***success on scrolling Ok Button")
            ''' # click OK to begin firmware update  '''
            if firmwareBase.negbb_triggeronly == 'Yes':

                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE):
                    logging._log_to_console_and_log_file("Inside neg tests on  LI update Firmware")
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
                    return True
                else:
                    logger._warn("OK button not appeared on LI page")
                    return False
            else:

                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
                ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ACTVITY_UPDATE_FIRMWARE)
                ''' Check error messages appears on LI FW update page '''
                logger.info("Checking For errors - After clicking on OK Button of Firmware update in LI page")
                if not ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM, FusionLogicalInterconnectsPage.WAIT_TIME):
                    errors_on_form = base_page.get_errors_on_form(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM)
                    error_status = ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_HP_STATUS_ERROR, FusionLogicalInterconnectsPage.WAIT_TIME)
                if error_status or errors_on_form:
                    if errors_on_form:
                        error_string += errors_on_form + "\t"
                    if error_status:
                        logger.warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY)))
                        logger.info("Inside error check block.... ")
                        bflag = False
                        logger.warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS)))
                        bflag = False
                        error_string += ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS) + "\t"
                    # if form is still seen click cancel
                    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                        logger.info("Clicking Cancel")
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)
                else:
                    logger.info("No errors Seen on LI Firmware update page")
                ''' # Check the Progress of Firmware upgrade on LI page  '''
                if (ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_PROGRESS_BAR, PerfConstants.DEFAULT_SYNC_TIME)):
                    logger.info("checking whether firmware is updated Successfully or updated with warnings")
                    # Added code to check Stage firmware is in progress
                    timeout = 0
                    start_stg = datetime.now()
                    while timeout < FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
                        timeout = (datetime.now() - start_stg).seconds
                        if (ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_PROGRESS_BAR, PerfConstants.DEFAULT_SYNC_TIME)):
                            logger.info("Staging of Update Firmware  is in Progress in LI and waited for " + str(timeout))
                        if (ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_CMPLETE_XPATH, PerfConstants.DEFAULT_SYNC_TIME)):
                            logger.info("Staging of Firmware update Completed on LI page.\n")
                            break
                        elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_WARNING_XPATH, FusionLogicalInterconnectsPage.UPDATE_WAIT_TIME):
                            logger.warn("Firmware update Completed but with warning on LI page")
                            bflag = False
                            break
                        elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ERROR_XPATH, FusionLogicalInterconnectsPage.UPDATE_WAIT_TIME):
                            logger.warn("--Error during Staging Firmware update on LI page")
                            bflag = False
                            break
                    if timeout > FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
                        logger._warn("Either FW Upgrade of LI '{}' has not completed , even after waiting for {} minutes!!".format(firmwareBase.name, timeout))
                        bflag = False
                        error_string += "Either FW Upgrade of LI '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!\t".format(firmwareBase.name, timeout)
                    # if add form is still seen click cancel
                    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                        logger.info("Clicking Cancel")
                        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)
                else:
                    logger.warn("progress not appeared after clicking OK button on FW update page")
                    break

        elif (str(firmwareBase.updateaction) == "Update firmware (stage + activate)"):
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_UPDATE_ACTION % firmwareBase.updateaction)
            logger.info(" Inside a Stage + Activate FW update ")
            logger.info("Selecting firmware for : " + str(firmwareBase.updateaction))
            selenium2lib.click_element(FusionLogicalInterconnectsPage.ID_CLICK_UPDATE_FiRMWARE_FOR)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_FIRMWARE_DROPDOWN % firmwareBase.updateFirmware)
            if (str(firmwareBase.force) == "Yes"):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_CHKBOX_FORCE_FIRMWARE_UPDATE)
            if (str(firmwareBase.ethernetupdate) == "Parallel") or (str(firmwareBase.ethernetupdate) == "Serial") or (str(firmwareBase.ethernetupdate) == "Odd/even"):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ETHERNET_CH_XPATH)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ETHERNET_CHANNEL_XPATH % firmwareBase.ethernetupdate)

            # Change default delay of ethernet channel

            if (str(firmwareBase.ethrdelay) == "Yes"):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_ETHRE_DELAY_XPATH)
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_XPATH_ETHRE_DELAY_XPATH, firmwareBase.ethrdelayvalue)

            if (str(firmwareBase.fiberchannelupdate) == "Parallel") or (str(firmwareBase.fiberchannelupdate) == "Serial") or (str(firmwareBase.fiberchannelupdate) == "Odd/even"):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FIBER_FC_CHANNEL_XPATH)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_FC_XPATHA % firmwareBase.fiberchannelupdate)
            # Change default delay of fiber channel
            if (str(firmwareBase.fiberdelay) == "Yes"):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_XPATH_FIBER_DELAY_XPATH)
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_XPATH_FIBER_DELAY_XPATH, firmwareBase.fiberdelayvalue)

            ui_lib.scroll_into_view(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_FIRWARE_UPDATE)

            ''' Check error messages appears on LI FW update page '''
            logger.info("Checking For errors - After clicking on OK Button of Firmware update in LI page")

            if not ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM, FusionLogicalInterconnectsPage.WAIT_TIME):
                errors_on_form = base_page.get_errors_on_form(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM)
                error_status = ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_HP_STATUS_ERROR, FusionLogicalInterconnectsPage.WAIT_TIME)
            if error_status or errors_on_form:
                if errors_on_form:
                    error_string += errors_on_form + "\t"
                if error_status:
                    logger._warn("Error Summary - {}".format(ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY)))
                    logger.info("Inside error check .... ")
                    bflag = False
                    logger._warn("Error Details - {}".format(ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS)))
                    bflag = False
                    error_string += ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_SUMMARY) + "." + ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_LE_FW_UPDATE_FORM_MESSAGE_DETAILS) + "\t"
                # if form is still seen click cancel
                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                    logger.info("Clicking Cancel")
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)

            else:
                logger.info("No errors Seen on LI Firmware update page")
            # Added the code for measure progress of activate already staged firmware
            timeout = 0
            start_update = datetime.now()
            while timeout < FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
                timeout = (datetime.now() - start_update).seconds
                if (ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_PROGRESS_BAR, PerfConstants.DEFAULT_SYNC_TIME)):
                    logger.info("Stage + Activation of Firmware  is in Progress in LI and waited for " + str(timeout))
                if (ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_CMPLETE_XPATH, PerfConstants.DEFAULT_SYNC_TIME)):
                    logger.info(" Stage + Activation update Firmware  Completed on LI page.\n")
                    bflag = True
                    break
                elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_WARNING_XPATH, FusionLogicalInterconnectsPage.UPDATE_WAIT_TIME):

                    logger.warn(" Stage + Activation Firmware update  Completed but with warning on LI page")
                    bflag = False
                    break
                elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ERROR_XPATH, FusionLogicalInterconnectsPage.UPDATE_WAIT_TIME):
                    logger.warn("Error during Stage + Activation Firmware update  on LI page")
                    bflag = False
                    break
            if timeout > FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
                logger._warn("Either FW Upgrade of LI '{}' has not completed , even after waiting for {} minutes!!".format(firmwareBase.name, timeout))
                bflag = False
                error_string += "Either FW Upgrade of LI '{}' has not completed or FW Upgrade Complete Alert is not seen , even after waiting for {} minutes!!\t".format(firmwareBase.name, timeout)
            # if add form is still seen click  cancel
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_LE_FW_UPDATE_FORM):
                logger.info("Clicking Cancel")
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_FW_CANCEL)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTVITY_UPDATE_FIRMWARE)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTIVITY_BAR % firmwareBase.name)
            if ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_UPDATE_SUCCESS % firmwareBase.name, PerfConstants.LOGICAL_INTERCONNECT_UPDATE_FIRMWARE):
                logger.info("Firmware Update is success")
                bflag = True
            elif ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_UPDATE_WARNING % firmwareBase.name, PerfConstants.LOGICAL_INTERCONNECT_UPDATE_FIRMWARE):
                logger.info("Firmware Update is done with warnings")
                bflag = False
            elif ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_UPDATE_FAILED % firmwareBase.name, PerfConstants.LOGICAL_INTERCONNECT_UPDATE_FIRMWARE):
                logger.warn("Firmware Update is failed")
                bflag = False
            else:
                logger.warn("Firmware Update hasn't started")
                bflag = False
        else:
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_CANCEL_FIRMWARE_UPDATE)
            logger.warn("The given firmware baseline is invalid")
            bflag = False
    return bflag


def redistribute_logins(*lis_obj):
    s2l = ui_lib.get_s2l()
    if isinstance(lis_obj, test_data.DataObj):
        lis_obj = [lis_obj]
    elif isinstance(lis_obj, tuple):
        lis_obj = list(lis_obj[0])
    navigate()

    # select logical interconnect
    for logicalinterconnects in lis_obj:
        if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_LOGICAL_SWITCH_BASE % logicalinterconnects.name):
            s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_LOGICAL_SWITCH_BASE % logicalinterconnects.name)

            # click on action menu
            s2l.click_element(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
            s2l.click_element(FusionLogicalInterconnectsPage.ID_MENU_ACTION_REDISTR_LOGIN)
            # validate Redistribute Logins page opened or not
            if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_REDISTRIBUTE_LOGIN_TITLE):
                if logicalinterconnects.has_property("redistributelogins"):
                    for redistributelogin in logicalinterconnects.redistributelogins:
                        # validate uplink set
                        if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_UPLINK_SET % redistributelogin.uplinkset):
                            logging._log_to_console_and_log_file("Successfully able to validate uplink set     %s  in the redistribute login page " % redistributelogin.uplinkset)
                        else:
                            logging._log_to_console_and_log_file("failed to validate uplink  set   %s  in the redistribute login page " % redistributelogin.uplinkset)
                            ui_lib.fail_test("failed to validate uplink  set in the redistribute login page", "True")

                        # validate ports
                        if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_INTERCONNECT_PORT % redistributelogin.ports):
                            logging._log_to_console_and_log_file("Successfully able  to validate up link port    %s  in the redistribute login page " % redistributelogin.ports)
                        else:
                            logging._log_to_console_and_log_file("failed to validate uplink port    %s  in the redistribute login page " % redistributelogin.ports)
                            ui_lib.fail_test("failed to validate uplink port set in the redistribute login page", "True")

                        # validate status
                        label = s2l.get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_STATUS % redistributelogin.ports)
                        if label == redistributelogin.status:
                            logging._log_to_console_and_log_file("Successfully able  to validate up link status    %s  in the redistribute login page " % redistributelogin.status)
                        else:
                            logging._log_to_console_and_log_file("failed to validate uplink status    %s  in the redistribute login page " % redistributelogin.status)
                            ui_lib.fail_test("failed to validate up link status in the redistribute login page", "True")

                        # validate interconnect logins
                        label = s2l.get_text(FusionLogicalInterconnectsPage.ID_ELEMENT_LOGIN % redistributelogin.ports)
                        if label == redistributelogin.logins:
                            logging._log_to_console_and_log_file("Successfully able  to validate up link status    %s  in the redistribute login page " % redistributelogin.logins)
                        else:
                            logging._log_to_console_and_log_file("failed to validate logins    %s  in the redistribute login page " % redistributelogin.logins)
                            ui_lib.fail_test("failed to validate logins in the redistribute login page", "True")
            else:
                logging._log_to_console_and_log_file("not able to open Redistribute Logins page  ")
                ui_lib.fail_test("not able to open Redistribute Logins page", "True")

        else:
            logging._log_to_console_and_log_file("logical interconnect  %s not found in the page " % logicalinterconnects.name)
            ui_lib.fail_test("logical interconnect  %s not found in the page", "True")


def reapply_configuration(*lic_obj):
    """ [LEGACY]
        Validate Consistency/Inconsistency Reapply Configuration  for Logical Interconnect  from Logical Interconnect Group"""

    logging._log_to_console_and_log_file("Validate Reapply Configuration for Logical Interconnect")
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(lic_obj, test_data.DataObj):
        lic_obj = [lic_obj]
    elif isinstance(lic_obj, tuple):
        lic_obj = list(lic_obj[0])

    for lic in lic_obj:
        lic_list = [el.text for el in selenium2lib._element_find(FusionLogicalInterconnectsPage.ID_LIC_LIST, False, False)]
        if lic.name not in lic_list:
            logger._warn("Logical Interconnect '%s' does not exist" % lic.name)
            continue

    # Select Logical Interconnect
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_LIC_NAME_BASE % lic.name)
    # Logical Interconnect has changed to disconnected
    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_HEALTH_STATUS_ERROR):
        if selenium2lib._is_element_present(FusionLogicalInterconnectsPage.ID_CONFIGURE_FAILURE):
            logging._warn("The stacking health has changed to disconnected. Verify that the interconnects in the logical interconnect are configured and are fully stacked(redundantly connected).")
    else:
        warning_msg = ""
        ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_HEALTH_STATUS_WARNING)
        if selenium2lib._is_element_present(FusionLogicalInterconnectsPage.ID_WARNING_MSG):
            warning_msg = selenium2lib.get_text(FusionLogicalInterconnectsPage.ID_WARNING_MSG)
        # capturing the warning message and comparing the sub string with captured string
        if ('The logical interconnect is inconsistent with the logical interconnect group' in warning_msg) or (warning_msg == "") or (warning_msg != ""):
            if(warning_msg != ""):
                logging._log_to_console_and_log_file("Activity message before updating from group: " + warning_msg)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
            # Boolean variable
            boolaction = False
            # Update from LIC group before reapply configuration
            if ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_MENU_ACTION_UPDATE_FRM_GRP):
                boolaction = True
                ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_UPDATE_FROM_GRP_DIALOG, PerfConstants.DEFAULT_SYNC_TIME)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_YES_UPDATE_LIC)
                if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_HEALTH_STATUS_OK, PerfConstants.UPDATE_FROM_GRP):
                    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_UPDATE_FROM_GRP_MSG):
                        logging._log_to_console_and_log_file("Update from Logical Interconnect Group done successfully")
                    else:
                        logging._warn()
            if boolaction:
                # reapply configuration to LIC
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_MENU_ACTION_REAPPLY_CONF, PerfConstants.UPDATE_ACTIVITY)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.XPATH_LI_REAPPLY_CONFIG_BUTTON, PerfConstants.UPDATE_ACTIVITY)
            ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_UPDATE_PROGRESS, PerfConstants.UPDATE_ACTIVITY)
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_HEALTH_STATUS_OK, PerfConstants.UPDATE_ACTIVITY):
                ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_CONFIGURATION_SUCCESS_MSG)
                logger._log_to_console_and_log_file("Reapply Configuration of logical-interconnect '%s' is done successfully" % lic.name)
            elif ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_WARNING_MSG):
                logger._warn("Reapply Configuration of logical-interconnect '%s' is unsuccessful" % lic.name)
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_WARNING_MSG):
                warning_msg = selenium2lib.get_text(FusionLogicalInterconnectsPage.ID_WARNING_MSG)
                logging._warn("Activity message after reapply configuration is: " + warning_msg)
        elif ('uplink ports null are non operational' in warning_msg):
            logging._warn(warning_msg + " Verify that all uplink ports used by this uplink set are enabled and linked.")


def create_support_dump(*lic_obj):
    """ Create and Download support dump for logical interconnect, the download will happen at 'C:\\DownloadFolder'
        NOTE :
        > As downloading fusion appliance back-up involves windows object,
        > and to handle the download window, we need to add below mentioned lines of code
        > in 'C:\tools\Python27\Lib\site-packages\Selenium2Library\resources\firefoxprofile\prefs.js'
        >
                user_pref("browser.download.folderList",2);
                user_pref("browser.download.dir",'C:\\DownloadFolder');
                user_pref("browser.helperApps.neverAsk.saveToDisk","application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
                user_pref("browser.download.manager.scanWhenDone", false);
                user_pref("browser.download.manager.showAlertOnComplete", true);
                user_pref("browser.download.manager.useWindow", false);
                user_pref("browser.helperApps.alwaysAsk.force", false);

        > This will make sure the download happens silently at the directory specified
    """
    logging._log_to_console_and_log_file("Create and download Support Dump")
    if isinstance(lic_obj, test_data.DataObj):
        lic_obj = [lic_obj]
    elif isinstance(lic_obj, tuple):
        lic_obj = list(lic_obj[0])
    for lic in lic_obj:
        logging._log_to_console_and_log_file("create support dump  with name.... %s" % lic.name)
        logging._log_to_console_and_log_file("Path..%s" % lic.downloadpath)
        backupdirectory = lic.downloadpath
    # CODE TO CREATE DOWNLOAD DIRECTORY AND DELETE FILES INSIDE, IF DIRECTORY EXISTS
        if not os.path.exists(backupdirectory):
            os.makedirs(backupdirectory)
        for root, dirs, files in os.walk(backupdirectory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        if not select_logical_interconnect(lic.name):
            logging._warn("Given logical interconnect is not selected %s" % lic.name)
            continue
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_MENU_ACTION_CREATE_SUPPORT_DUMP)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_YES_CREATE_SUPPORT_DUMP)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTVITY_SUPPORT_DUMP)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_CLICK_ACTIVITY)
        if ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_TIMESTAMP_SUPPORT_DUMP):
            logging._log_to_console_and_log_file("Creation of support dump started")
            if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_VALIDATE_SUCCESS % lic.name, PerfConstants.LOGICALINTERCONNECT_SUPPORT_DUMP):
                logging._log_to_console_and_log_file("Support dump created successfully")
            else:
                logging._log_to_console_and_log_file("Creation of Support dump failed")
        else:
            logging._log_to_console_and_log_file("Support dump not yet started")
        foldersize = os.path.getsize(os.path.join(backupdirectory))
        while os.listdir(backupdirectory) == []:
            BuiltIn().sleep(2)
        # CODE TO WAIT TILL THE DOWNLOAD IS IN PROGRESS
        finalfoldersize = 0
        while foldersize != finalfoldersize:
            BuiltIn().sleep(2)
            finalfoldersize = os.path.getsize(os.path.join(backupdirectory))
            logging._log_to_console_and_log_file("final folder size %s" % finalfoldersize)
            start = datetime.now()
            if(datetime.now() - start).total_seconds() > PerfConstants.DOWNLOAD_BACKUP_TIMEOUT:
                break


def select_logical_interconnect(liname):
    """ select_logical_interconnect """

    navigate()
    logger.info("Selecting a LI with name '{0}'".format(liname))
    if VerifyLogicalInterconnects.verify_logical_interconnect_exist(liname, fail_if_false=False):
        CommonOperationLogicalInterconnect.click_logical_interconnect(liname)
        CommonOperationLogicalInterconnect.wait_logical_interconnect_selected(liname)
        # Validating the status of LI before selection
        CommonOperationLogicalInterconnect.wait_logical_interconnect_status_ok(liname)
        return True
    else:
        logger.warn("LI '{0}' does not exist".format(liname))
        ui_lib.get_s2l().capture_page_screenshot()
        return False


def _add_logical_interconnect_settings(lisetting):
    """ add Logical interconnect settings

        Example:
        | `add Logical Interconnect settings`      |     |
    """
    s2l = ui_lib.get_s2l()
    FusionUIBase.select_view_by_name(view_name="Interconnect Settings", timeout=5, fail_if_false=False)
    # CODE TO UPDATE THE INTERCONENCT SETTINGS FOR THE GIVEN LOGICAL INTERCONNECT
    if (lisetting.has_property("cachefailover")):
        if(lisetting.cachefailover == "True"):
            ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_CHKBOX_CACHE_FAILOVER)
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHKBOX_CACHE_FAILOVER)
    if (lisetting.has_property("refreshinterval")):
        if not (lisetting.refreshinterval == ""):
            ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_INPUT_REFRESHINTERVAL, lisetting.refreshinterval)
            s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_REFRESHINTERVAL, lisetting.refreshinterval)
    if (lisetting.has_property("IGMPSnooping")):
        if lisetting.IGMPSnooping == "True":
            ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_CHKBOX_CACHE_IGMPSNOOPING, PerfConstants.DEFAULT_SYNC_TIME)
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHKBOX_CACHE_IGMPSNOOPING)
            ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_INPUT_IDLETTIMEINTERVAL, lisetting.refreshinterval)
            s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_IDLETTIMEINTERVAL, lisetting.idletimeoutinterval)
    # F702- LI edits added for lldptagging and lldpenhancedtlv
    if (lisetting.has_property("lldptagging")):
        lldp_tagged = lisetting.lldptagging
        if(lldp_tagged == "TRUE"):
            EditLogicalInterconnects.tick_interconnect_settings_lldp_tagging()
        else:
            EditLogicalInterconnects.untick_interconnect_settings_lldp_tagging()
    if (lisetting.has_property("lldpenhancedtlv")):
        lldp_enhanced_tlv = lisetting.lldpenhancedtlv
        if(lldp_enhanced_tlv == "TRUE"):
            EditLogicalInterconnects.tick_interconnect_settings_lldp_enhancedtlv()
        else:
            EditLogicalInterconnects.untick_interconnect_settings_lldp_enhancedtlv()
    if (lisetting.has_property("pausefloodprotection")):
        pause_flood_protection = lisetting.pausefloodprotection
        if pause_flood_protection == "TRUE":
            EditLogicalInterconnects.tick_interconnect_settings_pause_flood_protection()
        else:
            EditLogicalInterconnects.untick_interconnect_settings_pause_flood_protection()


def _add_logical_interconnect_lldp_settings(lldpsetting):
    FusionUIBase.select_view_by_name(view_name="Interconnect Settings", timeout=5, fail_if_false=False)
    # CODE TO UPDATE THE INTERCONENCT SETTINGS FOR THE GIVEN LOGICAL INTERCONNECT
    # F1048- LI edit added for lldp tagging and lldpenhancedtlv
    if (lldpsetting.has_property("lldptagging")):
        lldp_tagged = lldpsetting.lldptagging
        if lldp_tagged == "TRUE":
            EditLogicalInterconnects.tick_interconnect_settings_lldp_tagging()
        else:
            EditLogicalInterconnects.untick_interconnect_settings_lldp_tagging()

    if (lldpsetting.has_property("lldpenhancedtlv")):
        lldp_enhanced_tlv = lldpsetting.lldpenhancedtlv
        if lldp_enhanced_tlv == "TRUE":
            EditLogicalInterconnects.tick_interconnect_settings_lldp_enhancedtlv()
        else:
            EditLogicalInterconnects.untick_interconnect_settings_lldp_enhancedtlv()


def _add_logical_interconnect_utilizationsampling(lsutilizationsampling):
    """ add Logical Interconnect utilizationsampling

        Example:
        | `add Logical Interconnect utilizationsampling`      |     |
    """

    if (lsutilizationsampling.has_property("Intsamples")):
        if not (lsutilizationsampling.Intsamples == ""):
            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_INPUT_INTSAMPLES, lsutilizationsampling.Intsamples)

    if (lsutilizationsampling.has_property("totalnumbersamples")):
        if not (lsutilizationsampling.totalnumbersamples == ""):
            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_INPUT_TOTALINTSAMPLES, lsutilizationsampling.totalnumbersamples)


def _add_logical_interconnect_snmp(snmp):
    """ add Logical Interconnect SNMP

        Example:
        | `add Logical Interconnect SNMP`      |     |
    """

    if (snmp.has_property("snmpen")):
        if(snmp.snmpen == "True"):
            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_INPUT_SNMP_SYS_CON, snmp.systemcontact)
            ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_INPUT_SNMP_COMMUNITY, snmp.community)


def _delete_logical_interconnect_uplink(uplink):
    """ delete Logical Interconnect uplink

        Example:
        | `delete Logical Interconnect uplink`      |     |
    """
    s2l = ui_lib.get_s2l()

    if not s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_UPLINK_NAME % uplink.name):
        logging._log_to_console_and_log_file("not able to find uplink %s to delete " % uplink.name)
        s2l.capture_page_screenshot()
        return False
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_DELETE_UPLINK % uplink.name)
    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_BTN_CONFIRM_DELETE_UPLINK):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_CONFIRM_DELETE_UPLINK)
    else:
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_DELETE_UPLINK % uplink.name)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_CONFIRM_DELETE_UPLINK)

    if ui_lib.wait_for_element_notvisible(FusionLogicalInterconnectsPage.ID_ELEMENT_UPLINK_NAME % uplink.name, PerfConstants.INTERCONNECT_ELEMENT_VISIBLE):
        logging._log_to_console_and_log_file("The Uplink set %s is deleted successfully " % uplink.name)
        return True
    else:
        logging._warn("The Uplink set %s is not deleted successfully " % uplink.name)
        s2l.capture_page_screenshot()
        return False


def add_SNMP_trap_dest(SNMPTrap):
    """ add SNMP Trap Destination

        Example:
        | `add SNMP Trap Dest`      |     |
    """
    s2l = ui_lib.get_s2l()

    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_DESTINATION % SNMPTrap.destination):
        logging._log_to_console_and_log_file("The given trap destination is already added to the particular interconnect %s" % SNMPTrap.destination)
        return True

    ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_BTN_ADD_SNMP_TRAPS_DEST, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_SNMP_TRAPS_DEST)
    if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_INPUT_TRAP_ADDRESS, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_SNMP_TRAPS_DEST)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_INPUT_TRAP_ADDRESS)
    s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_TRAP_ADDRESS, SNMPTrap.destination)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_INPUT_COMMUNITY_STRING)
    s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_COMMUNITY_STRING, SNMPTrap.community)
    Snmptrapformat = SNMPTrap.Trapformat
    if Snmptrapformat.lower() == "snmpv1":
        s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_SNMPV1)
    else:
        s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_SNMPV2)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_SEVERITY)
    SeverityList = SNMPTrap.Severity.split(',')
    for Severity in SeverityList:
        if Severity.lower() == "critical":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_CRITICAL)
        elif Severity.lower() == "major":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_MAJOR)
        elif Severity.lower() == "minor":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_MINOR)
        elif Severity.lower() == "warning":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_WARNING)
        elif Severity.lower() == "normal":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_NORMAL)
        elif Severity.lower() == "info":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_INFO)
        elif Severity.lower() == "unknown":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_UNKNOWN)
        else:
            logging._log_to_console_and_log_file("No severity is selected")
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_SEVERITY)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_VCMTRAPS)
    if SNMPTrap.VCMTraps != "":
        s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCMTRAPS)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_VCMTRAPS)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_VCENETTRAPS)
    VCEnetTrapList = SNMPTrap.VCEnetTraps.split(',')
    for VCEnetTrap in VCEnetTrapList:
        if VCEnetTrap.lower() == "portstatus":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_PORT_STATUS)
        elif VCEnetTrap.lower() == "portthreshold":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_PORT_THRESHOLDS)
        elif VCEnetTrap.lower() == "other":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_OTHER)
        else:
            logging._log_to_console_and_log_file("No severity is selected")
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_VCENETTRAPS)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_VCFCSTATUS)
    VCFCTrapsList = SNMPTrap.VCFCTraps.split(',')
    for VCFCTraps in VCFCTrapsList:
        if VCFCTraps.lower() == "portstatus":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCFCSTATUS_PORT_STATUS)
        elif VCFCTraps.lower() == "other":
            s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCFCSTATUS_OTHER)
        else:
            logging._log_to_console_and_log_file("No severity is selected")
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_VCFCSTATUS)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_SNMP_TRAP)
    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_DESTINATION % SNMPTrap.destination):
        logging._log_to_console_and_log_file("The given trap destination is added successfully to the particular interconnect %s" % SNMPTrap.destination)
        return True
    else:
        logging._warn("The given trap destination is not added successfully to the particular interconnect %s" % SNMPTrap.destination)
        s2l.capture_page_screenshot()
        return False


def edit_SNMP_trap_dest(SNMPTrap):
    """ edit SNMP Trap Destination

        Example:
        | `edit SNMP Trap Dest`      |     |
    """
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_DESTINATION % SNMPTrap.destination, PerfConstants.DEFAULT_SYNC_TIME):
        logging._warn("The given trap destination is not added as the trap destination. Add the destination and then edit it %s" % SNMPTrap.destination)
        s2l.capture_page_screenshot()
        return False
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BUTTON_EDIT_TRAP % SNMPTrap.destination)
    s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_TRAP_ADDRESS, SNMPTrap.newdestination)
    s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_COMMUNITY_STRING, SNMPTrap.community)
    Snmptrapformat = SNMPTrap.Trapformat
    if Snmptrapformat.lower() == "snmpv1":
        s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_SNMPV1)
    else:
        s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_SNMPV2)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_SEVERITY)
    SeverityList = ["Critical", "Major", "Minor", "Warning", "Normal", "Info", "Unknown"]
    EditSeverityList = SNMPTrap.Severity.split(',')
    for Severity in SeverityList:
        if Severity in EditSeverityList:
            if Severity.lower() == "critical":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_CRITICAL)
            elif Severity.lower() == "major":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_MAJOR)
            elif Severity.lower() == "minor":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_MINOR)
            elif Severity.lower() == "warning":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_WARNING)
            elif Severity.lower() == "normal":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_NORMAL)
            elif Severity.lower() == "info":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_INFO)
            elif Severity.lower() == "unknown":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_UNKNOWN)
            else:
                logging._log_to_console_and_log_file("No severity is selected")
        else:
            if Severity.lower() == "critical":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_CRITICAL)
            elif Severity.lower() == "major":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_MAJOR)
            elif Severity.lower() == "minor":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_MINOR)
            elif Severity.lower() == "warning":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_WARNING)
            elif Severity.lower() == "normal":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_NORMAL)
            elif Severity.lower() == "info":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_INFO)
            elif Severity.lower() == "unknown":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_SEVERITY_UNKNOWN)
            else:
                logging._log_to_console_and_log_file("No severity is selected")
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_SEVERITY)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_VCMTRAPS)
    if SNMPTrap.VCMTraps != "":
        s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCMTRAPS)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_VCMTRAPS)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_VCENETTRAPS)
    VCEnetTrapList = ["portstatus", "portthresholds", "other"]
    EditVCEnetTrapList = SNMPTrap.VCEnetTraps.split(',')
    for VCEnetTrap in VCEnetTrapList:
        if VCEnetTrap in EditVCEnetTrapList:
            if VCEnetTrap.lower() == "portstatus":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_PORT_STATUS)
            elif VCEnetTrap.lower() == "portthreshold":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_PORT_THRESHOLDS)
            elif VCEnetTrap.lower() == "other":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_OTHER)
            else:
                logging._log_to_console_and_log_file("No severity is selected")
        else:
            if VCEnetTrap.lower() == "portstatus":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_PORT_STATUS)
            elif VCEnetTrap.lower() == "portthreshold":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_PORT_THRESHOLDS)
            elif VCEnetTrap.lower() == "other":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCENETTRAPS_OTHER)
            else:
                logging._log_to_console_and_log_file("No severity is selected")

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_VCENETTRAPS)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_EXPAND_VCFCSTATUS)
    VCFCTrapList = ["portstatus", "other"]
    EditVCFCTrapsList = SNMPTrap.VCFCTraps.split(',')
    for VCFCTraps in VCFCTrapList:
        if VCFCTraps in EditVCFCTrapsList:
            if VCFCTraps.lower() == "portstatus":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCFCSTATUS_PORT_STATUS)
            elif VCFCTraps.lower() == "other":
                s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCFCSTATUS_OTHER)
            else:
                logging._log_to_console_and_log_file("No severity is selected")
        else:
            if VCFCTraps.lower() == "portstatus":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCFCSTATUS_PORT_STATUS)
            elif VCFCTraps.lower() == "other":
                s2l.unselect_checkbox(FusionLogicalInterconnectsPage.ID_CHECK_VCFCSTATUS_OTHER)
            else:
                logging._log_to_console_and_log_file("No severity is selected")
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_VCFCSTATUS)

    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BUTTON_EDIT_OK)


def delete_SNMP_trap_dest(SNMPTrap):
    """ delete SNMP Trap Destination

        Example:
        | `delete SNMP Trap Dest`      |     |
    """
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_DESTINATION % SNMPTrap.destination, PerfConstants.DEFAULT_SYNC_TIME):
        logging._warn("The given trap destination is not present for the particular interconnect %s" % SNMPTrap.destination)
        s2l.capture_page_screenshot()
        return False
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_DELETE_TRAP % SNMPTrap.destination)
    if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_BUTTON_REMOVE, PerfConstants.DEFAULT_SYNC_TIME):
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_DELETE_TRAP % SNMPTrap.destination)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BUTTON_REMOVE)
    if not s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_DESTINATION % SNMPTrap.destination):
        logging._log_to_console_and_log_file("The given trap destination is deleted successfully to the particular interconnect %s" % SNMPTrap.destination)
        return True
    else:
        logging._warn("The given trap destination is not deleted successfully to the particular interconnect %s" % SNMPTrap.destination)
        s2l.capture_page_screenshot()
        return False


def add_SNMP_Access(SNMP_Access):
    """ add SNMP Access

        Example:
        | `add SNMP Access`      |     |
    """
    s2l = ui_lib.get_s2l()
    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_SUBNET % SNMP_Access.subnet):
        logging._log_to_console_and_log_file("The given trap destination is already added to the particular interconnect %s" % SNMP_Access.subnet)
        return True
    ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_BTN_ADD_SNMP_ACCESS, PerfConstants.DEFAULT_SYNC_TIME)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_SNMP_ACCESS)
    ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_INPUT_SUBNET, SNMP_Access.subnet)
    s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_SUBNET, SNMP_Access.subnet)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BUTTON_ADD_SNMP)
    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_SNMP_SUBNET % SNMP_Access.subnet):
        logging._log_to_console_and_log_file("The given trap destination is added successfully to the particular interconnect %s" % SNMP_Access.subnet)
        return True
    else:
        logging._warn("The given trap destination is not added successfully to the particular interconnect %s" % SNMP_Access.subnet)
        s2l.capture_page_screenshot()
        return False


def delete_SNMP_Access(SNMP_Access):
    """ delete SNMP Access

        Example:
        | `delete SNMP Access`      |     |
    """
    s2l = ui_lib.get_s2l()
    if not ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_ELEMENT_DESTINATION % SNMP_Access.subnet, PerfConstants.DEFAULT_SYNC_TIME):
        logging._warn("The given trap destination is not present for the particular interconnect %s" % SNMP_Access.subnet)
        s2l.capture_page_screenshot()
        return False
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BUTTON_DELETE_SNMP % SNMP_Access.subnet)
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BUTTON_REMOVE)
    if not s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_DESTINATION % SNMP_Access.subnet):
        logging._log_to_console_and_log_file("The given trap destination is deleted successfully to the particular interconnect %s" % SNMP_Access.subnet)
        return True
    else:
        logging._warn("The given trap destination is not deleted successfully to the particular interconnect %s" % SNMP_Access.subnet)
        s2l.capture_page_screenshot()
        return False


def _edit_logical_interconnect_fcuplink(uplink):
    s2l = ui_lib.get_s2l()
    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_UPLINK_NAME % uplink.name):
        s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_UPLINK_EDIT % uplink.name)
        if (uplink.has_property("newname")):
            ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_INPUT_UPLINK_NAME, PerfConstants.FUSION_PAGE_SYNC)
            s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_UPLINK_NAME, (uplink.newname).strip())

            if (uplink.has_property("networks")):
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COMBO_NETWORK)
                if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_SEARCHFORANOTHER):
                    s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_SEARCHFORANOTHER)

                if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_NETWORK_NAME % uplink.networks):
                    s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_NETWORK_NAME % uplink.networks)
                else:
                    logging._log_to_console_and_log_file("network  %s not found " % uplink.networks)

                if (uplink.has_property("ports")):
                    name = uplink.ports
                    name = name.split(':')
                    s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_INTERCONNECT_EDIT)

                    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_FC_SEARCHFORANOTHER):
                        s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_FC_SEARCHFORANOTHER)

                    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_NETWORK_NAME % name[0]):
                        s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_NETWORK_NAME % name[0])
                    else:
                        logging._log_to_console_and_log_file("network  %s not found " % name[0])

                    # select interconnect ports
                    name[1] = name[1][-1]
                    s2l.select_checkbox(FusionLogicalInterconnectsPage.ID_CHKBOX_UPLINK_PORT % name[1])
                    s2l.click_element(FusionLogicalInterconnectsPage.ID_BTN_UPLINK_OK)

                    ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_ELEMENT_UPLINK_NAME % uplink.newname, PerfConstants.FUSION_PAGE_SYNC)

                    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_UPLINK_NAME % uplink.newname):
                        logging._log_to_console_and_log_file("logical interconnect uplink is edited succesfully with new name %s not found " % uplink.newname)
                        return True
                    else:
                        logging._log_to_console_and_log_file("failed to add uplink ports")
                        s2l.capture_page_screenshot()
                        return False
    else:
        logging._log_to_console_and_log_file("to edit uplink set please provide the edit up link tag in the xml data sheet ")


def _add_lus_to_edit_li(lus):
    """ This function will add a new logical uplink set to existing logical interconnect."""
    """_add_lus_to_edit_li

        Example:
        | _add_lus_to_edit_li(lusname, ustype, mode, networks, nativenetwork, uplinkethports, preferredport, fcswitchandport):
    """
    logging._log_to_console_and_log_file("----- function call to add uplink Set %s " % lus.name)
    # filling values in UI as supplied via xml data sheet
    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_UPLINK_SET)
    # function to add uplink set
    _add_logical_uplink_set(lus.name, lus.networkType, lus.connectionMode, lus.networks, lus.native, lus.ports, lus.preferredPort, lus.ports)

    if ui_lib.wait_for_element_visible(FusionLogicalInterconnectsPage.ID_UPLINK_EXISTENCE % lus.name, PerfConstants.DEFAULT_SYNC_TIME):
        logging._log_to_console_and_log_file("-----Added Uplink Set with name %s" % lus.name)
    else:
        logging._log_to_console_and_log_file("-----Not Added Uplink Set with name %s" % lus.name)


def _add_logical_uplink_set(lusname, ustype, mode, networks, nativenetwork, uplinkethports, preferredport, fcswitchandport):
    """ This function will add the given logical uplink set of existing logical interconnect group. """
    """ _add_logical_uplink_set

        Example:
        | _add_logical_uplink_set(lusname, ustype, mode, networks, nativenetwork, uplinkethports, preferredport, fcswitchandport):
    """
    logging._log_to_console_and_log_file("adding inputs to Logical Uplink Set")
    selenium2lib = ui_lib.get_s2l()
    if not ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_INPUT_UPLINK_ADD_NAME, PerfConstants.DEFAULT_SYNC_TIME):
        logging._warn("Create Uplink set page for the add uplink set did not get launch")
    selenium2lib.input_text(FusionLogicalInterconnectsPage.ID_INPUT_UPLINK_ADD_NAME, lusname)
    if ustype == "ETHERNET":
        selenium2lib.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_ETHERNET)

        # selecting Connection Mode : AUTO or FAILOVER
        if mode == "AUTO":
            selenium2lib.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_AUTO_CONNECTION_MODE)
        if mode == "FAILOVER":
            selenium2lib.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_FAILOVER_CONNECTION_MODE)

        # Add Networks
        networkList = networks.split(';')
        if len(networkList) > 0:
            for network in networkList:
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_NETWORK_UPLINK_PAGE)
                netxPath = FusionLogicalInterconnectsPage.ID_ELEMENT_LOGICAL_SWITCH_BASE % network
                ui_lib.wait_for_element_and_click(netxPath)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_NETWORK_ADD)

            # Validating the networks
            for network in networkList:
                netxPath = FusionLogicalInterconnectsPage.ID_ELEMENT_LOGICAL_SWITCH_BASE % network
                selenium2lib.page_should_contain_element(netxPath)
            # Select native network
            selenium2lib.select_checkbox(FusionLogicalInterconnectsPage.ID_CHKBOX_NATIVE_BASE % nativenetwork)

        # Add uplink ports
        ethuplinkportList = uplinkethports.split(';')
        if len(ethuplinkportList) > 0:
            for port in ethuplinkportList:
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_UPLINK_PORTS)
                bayportList = port.split(':')
                bayno = bayportList[0][-1:]
                selenium2lib.input_text(FusionLogicalInterconnectsPage.ID_SEARCH_INPUT_UPLINK_PORT, bayportList[1])
                selenium2lib.wait_until_page_contains_element(FusionLogicalInterconnectsPage.ID_BTN_ADD_UPLINK_PORT)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_TABLE_ADD_PORT % (bayno, bayportList[1]))
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_ADD_UPLINK_PORT)

        # Add Preferred port, if mode selected as 'FAILOVER'
        if mode == "FAILOVER":
            prefportList = preferredport.split(':')
            prefbayno = prefportList[0][-1:]
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_CHKBOX_FAILOVER_PREFERRED_PORT % (prefbayno, prefportList[1]))

    elif ustype == "FIBRE_CHANNEL":
        logging._log_to_console_and_log_file("creating FC uplink set ")
        selenium2lib.select_checkbox(FusionLogicalInterconnectsPage.ID_RADIO_FIBERCHANNEL)
        fcswitchportlist = fcswitchandport.split(':')

        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_NETWORK_COMBO_LIST)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ETH_NETWORK_SELECT % networks)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_PORT_COMBO_LIST)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ETH_NETWORK_SELECT % fcswitchportlist[0])

        # selecting the port
        fcswitchportlist.pop(0)  # to remove the interconnect switch info from the list.
        for fcport in fcswitchportlist:
            selenium2lib.wait_until_page_contains_element(FusionLogicalInterconnectsPage.ID_CHKBOX_BASE % fcport)
            selenium2lib.select_checkbox(FusionLogicalInterconnectsPage.ID_CHKBOX_BASE % fcport)
    # click on create
    selenium2lib.click_element(FusionLogicalInterconnectsPage.ID_BTN_CREATE_LOGICAL_UPLINK_TEML)


def configure_port_monitoring(*lis_obj):
    """ configure_port_monitoring

        Example:
        | configure port monitoring`      |     |
    """

    s2l = ui_lib.get_s2l()
    if isinstance(lis_obj, test_data.DataObj):
        lis_obj = [lis_obj]
    elif isinstance(lis_obj, tuple):
        lis_obj = list(lis_obj[0])
    navigate()

    for logicalinterconnects in lis_obj:
        if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_LOGICAL_SWITCH_BASE % logicalinterconnects.name):
            s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_LOGICAL_SWITCH_BASE % logicalinterconnects.name)

            if logicalinterconnects.has_property("liportmonitoring"):
                # click on action menu
                s2l.click_element(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
                s2l.click_element(FusionLogicalInterconnectsPage.ID_BTN_CONF_PORT_MONITORING)

                if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_TITLE_CON_PORT_MON):

                    for configureport in logicalinterconnects.liportmonitoring:
                        if configureport.has_property("portmonitoring"):
                            label = s2l.get_text(FusionLogicalInterconnectsPage.ID_BTN_PORT_MONITORING % configureport.portmonitoring)
                            # select port monitoring "enable"  or "disable"
                            s2l.click_element(FusionLogicalInterconnectsPage.ID_BTN_PORT_MONITORING % configureport.portmonitoring)
                        # select port
                        if configureport.has_property("ports"):
                            s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_NETWORKANALYSER)

                            s2l.input_text(FusionLogicalInterconnectsPage.ID_INPUT_PORT_ANALYSER, configureport.ports)
                            s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_NETWORKANALYSER)

                        if configureport.has_property("monitoredport"):
                            if configureport.monitoredport == "True":
                                s2l.click_element(FusionLogicalInterconnectsPage.ID_BTN_ADD_PORT)
                                downlinks = (configureport.downlink).split(',')
                                interconnect = configureport.ports[:-3]
                                for downlink in range(len(downlinks)):
                                    # select down link ports
                                    if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_DOWNLINK_PORT % (downlinks[downlink], configureport.ports[:-3])):
                                        s2l.click_element(FusionLogicalInterconnectsPage.ID_ELEMENT_DOWNLINK_PORT % (downlinks[downlink], configureport.ports[:-3]))
                                        s2l.click_element(FusionLogicalInterconnectsPage.ID_BTN_ADDPLUS)

                                    else:
                                        logging._log_to_console_and_log_file("not able to find the down link port %s  " % downlinks[downlink])
                                        ui_lib.fail_test("not able to find the down link port  ", "True")

                        s2l.click_element(FusionLogicalInterconnectsPage.ID_BTN_PORT_CANCEL)

                        for downlink in range(len(downlinks)):

                            if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_CONFIGURE_PORT_ELEMENT_DOWNLINK_PORTS % (downlinks[downlink], configureport.ports[:-3])):
                                logging._log_to_console_and_log_file("successfully added down link port %s " % downlinks[downlink])
                            else:
                                logging._log_to_console_and_log_file("failed to add downlink port to monitor  %s  " % downlinks[downlink])
                                ui_lib.fail_test("failed to add downlink port to monitor  ", "True")

                        # click on ok button
                        s2l.click_element(FusionLogicalInterconnectsPage.ID_BTN_PORTMONITOR_OK)
                        # validate ports
                        if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_PORTMON_COMPLETED_INPROGRESS):
                            ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_ELEMENT_PORTMON_COMPLETED_INPROGRESS, PerfConstants.RESTORING_LABEL_VISIBLE)

                            # waiting for completed state
                            ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_ELEMENT_PORTMON_COMPLTED, PerfConstants.RESTORING_LABEL_VISIBLE)

                            if s2l._is_element_present(FusionLogicalInterconnectsPage.ID_ELEMENT_PORTMON_COMPLTED):
                                logging._log_to_console_and_log_file("successfully added port monitoring to the interconnect  %s " % logicalinterconnects.name)
                            else:
                                pass
                        else:
                            logging._log_to_console_and_log_file("failed to monitor port for the interconnect  %s " % logicalinterconnects.name)
                            ui_lib.fail_test("failed to monitor port for the interconnect ", "True")
                else:
                    logging._log_to_console_and_log_file("not able to open the configure port monitoring page for the interconnect %s " % logicalinterconnects.name)
                    ui_lib.fail_test("failed to open configure port monitoring page ", "True")
            else:
                logging._log_to_console_and_log_file("configure port monitoring attribute is not added in the interconnect xml tag ")

        else:
            logging._log_to_console_and_log_file("logical interconnect  %s not found in the page " % logicalinterconnects.name)
            ui_lib.fail_test("logical interconnect  %s not found in the page", "True")


def verify_logical_interconnects_status(lis_obj):

    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=10)

    for logicalinterconnects in lis_obj:
        name = logicalinterconnects.name

        logger._log_to_console_and_log_file("Start waiting until logical interconnects %s status change to OK" % name)

        if ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_TABLE_ITEM % name) is False:
            ui_lib.fail_test("Logical interconnect %s not found in the page" % name, "True")

        if ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_TALBE_ITEM_STATUS % name, timeout=1200) is False:
            ui_lib.fail_test("Logical interconnect %s status not change to OK in 20 miniutes" % name, "True")


def get_ic_ipv4_address_in_li(li_name):
    '''
    Function to get the IPV4 address of the IC mentioned
    returns a dictionary of ic name:ipv4 address ,
    if no ip is found appropriate error message is logged and an empty dictionary is returned
    '''
    ic_list = []
    ic_ipv4_address_dict = {}
    ic_ipv4_address = None
    # navigate to Logical Interconnects page
    navigate()

    # if the LI is not present
    if not select_logical_interconnect(li_name):
        logger.warn("Unable to Select the LI - {}. Might Not be present!!".format(li_name))
        return False

    ic_list = _get_interconnects_in_li(li_name)
    if not ic_list:
        logger.warn("Unable to get the Interconnects of LI {}".format(li_name))
        return {}

    for ic in ic_list:
        ic_ipv4_address = interconnects.get_ic_ipv4_address(ic)
        if ic_ipv4_address:
            ic_ipv4_address_dict[ic] = ic_ipv4_address

    return ic_ipv4_address_dict


def _get_interconnects_in_li(li_name):
    '''
    function to get a liost of all the interconnects part of an LI
    returns an empty list if no interconnects are found
    '''
    interconnect_list = []
    # navigate to Logical Interconnects page
    navigate()
    # select the LI
    if not select_logical_interconnect(li_name):
        return []
    # goto Firmware section
    FusionUIBase.select_view_by_name('Firmware')
    # get the  IC's in the LI
    logger.info("IC's in LI  {} are - ".format(li_name))
    interconnect_list = CommonOperationLogicalInterconnect.get_interconnect_list_from_firmware_table()
    logger.info("{}".format(interconnect_list))
    return interconnect_list


def verify_ic_state_of_li(li_list, permissible_ic_states):
    '''
    Function to verify the State of Interconnects part of an LI

    Takes a list of LI and permissible states list as input

    Return True id the IC state is in permissible list else returns false
    '''
    error = 0

    # navigate to Logical Interconnects page
    navigate()

    for li in li_list:
        # select the LI
        if not select_logical_interconnect(li):
            logger.warn("Unable to select Logical Interconnect '%s'.It may not be present" % li)
            error += 1
            continue
        # verify LI state is consistent
        CommonOperationLogicalInterconnect.click_logical_interconnect_general()
        li_state = CommonOperationLogicalInterconnect.get_li_consistency_state()

        if li_state:
            logging.info("LI Consistency State is : {}".format(li_state))
            if li_state.lower() != 'consistent':
                logging.warn("LI Consistency state is : {} BUT it should be : Consistent".format(li_state))
                error += 1
        else:
            logging.warn("Could not get State of LI {}".format(li))

        # get the  IC's in the LI
        ic_list = _get_interconnects_in_li(li)
        logger.info("interconnect list info %s" % ic_list)
        if not ic_list:
            logging.warn("Unable to get the Interconnects of LI {}".format(li))
            continue

        for ic in ic_list:
            # Get State of IC
            ic_state = interconnects.get_interconnect_state(ic)
            if ic_state:
                # verify if the state of IC is in the permissible state list
                if ic_state.lower() in permissible_ic_states:
                    logging.info("IC {} state is - {}".format(ic, ic_state))
                else:
                    logging.warn("IC {} state - {} , is not in permissible state list - {} ".format(ic, ic_state, permissible_ic_states))
                    error += 1
            else:
                logging.warn("Unable to get state of IC - {}".format(ic))
                error += 1
    if error > 0:
        ui_lib.fail_test("Validation failures observed in the LI and IC State")
    return True


def get_license_info_of_logical_interconnect(li_name):
    '''
    Returns License State & license count of LI.Accepts logical Interconnect name as input

    '''
    if select_logical_interconnect(li_name):
        CommonOperationLogicalInterconnect.click_logical_interconnect_general()
        logger.info("Get LI Synergy 8GB Upgrade License info")
        return CommonOperationLogicalInterconnect.get_logical_interconnect_license_info()
    else:
        return False


def wait_for_reapply_configuration_complete(li_name):
    '''
    Function to wait for reapply configuration to complete.Monitor the activity in activities page
    '''

    logger.info("waiting for LI Reapply Configuration Completion")

    # open the activity side bar
    FusionUIBase.show_activity_sidebar()
    # wait for reapply configuration to compltete
    FusionUIBase.wait_activity_action_ok(li_name, 'Reapply configuration', 900, fail_if_false=False)
    # closing the activity side bar
    FusionUIBase.show_activity_sidebar()
    # go to activity page and get the activity state of the reapply configuration
    FusionUIBase.select_view_by_name("Activity")
    task_state = CommonOperationLogicalInterconnect.get_activity_state_for_reapply(li_name)
    logger.info("LI Reapply COnfiguration  state - {}".format(task_state))

    if "completed" in task_state.lower():
        logger.info("LI Reapply COnfiguration of LI {} completed successfully".format(li_name))
        return True
    elif "warning" in task_state.lower():
        logger.warn("LI Reapply COnfiguration of LI {} completed with warning".format(li_name))
        return True
    elif "error" in task_state.lower():
        logger.warn("LI Reapply COnfiguration  of LI {} completed with errors".format(li_name))
        return False

    return True


def reapply_li_configuration(li_name, wait_for_task_complete='true'):
    '''
    Function to trigger LI reapply configuration
    If wait_for_task_complete is true then function waits till task completes
    else it just triggers a reapply and returns

    '''
    # navigate to Logical Interconnects page
    navigate()
    error = 0
    # if the LI is not present
    if not select_logical_interconnect(li_name):
        logging.warn("Unable to Select the LI - {}. Might Not be present!!".format(li_name))
        return False
    # click on actions and do reapply configuration
    ReapplyConfiguration.click_actions_reapply()
    ReapplyConfiguration.wait_reapply_logical_interconnect_dialog_shown()
    ReapplyConfiguration.click_ok_button()
    # wait for reapply configuration
    if str(wait_for_task_complete).lower() == 'true':
        if not wait_for_reapply_configuration_complete(li_name):
            logger.warn("Either Reapply COnfiguration for LI  '{}' has not completed or  Complete Alert is not seen , even after waiting for {} minutes!!".format(li_name, PerfConstants.WAIT_UNTIL_CONSTANT))
            error += 1

    if error > 0:
        return False
    return True


def get_ic_stacking_domain_role_of_li(li_name):
    '''
    Function to get the stacking domain role of the Interconnects in the LI
    '''
    s2l = ui_lib.get_s2l()
    # navigate to Logical Interconnects page
    if not ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    ic_list = []
    ic_name = ''
    ic_stacking_domain_role = None
    ic_domain_role_dict = {}

    # if the LI is not present
    if not select_logical_interconnect(li_name):
        logging._warn("Unable to Select the LI - {}. Might Not be present!!".format(li_name))
        return {}

    # get the number of IC's in the LI
    ic_list = _get_interconnects_in_li(li_name)

    if not ic_list:
        logging._warn("Unable to get the Interconnects of LI {}".format(li_name))
        return {}

    for ic in ic_list:
        # get stacking domain role
        ic_stacking_domain_role = interconnects.get_ic_stacking_domain_role(ic)
        if ic_stacking_domain_role:
            ic_domain_role_dict[ic] = ic_stacking_domain_role

    return ic_domain_role_dict


def add_label_to_logical_interconnect(*logicalinterconnect_list):
    """ add label to Logical Interconnect
        This function is to add label to Logical Interconnect
        Example:
            add_label_to_logical_interconnect(*logicalinterconnect_list)
    """
    s2l = ui_lib.get_s2l()
    logger._log_to_console_and_log_file("Function call to add label to logical interconnect ")

    if isinstance(logicalinterconnect_list, test_data.DataObj):
        logicalinterconnect_list = [logicalinterconnect_list]
    elif isinstance(logicalinterconnect_list, tuple):
        logicalinterconnect_list = list(logicalinterconnect_list)[0]

    if not ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        navigate()

    for logicalinterconnect_label in logicalinterconnect_list:
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_RESET)
        if not select_logical_interconnect(logicalinterconnect_label.name):
            return False

        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_DROPDOWN)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_DROPDOWN_SELECT_LABEL)

        logger._log_to_console_and_log_file("Adding label to logicalinterconnect '{0}'".format(logicalinterconnect_label.name))
        if ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_EDIT_LABEL):
            ui_lib.move_to_element_and_click(FusionLogicalInterconnectsPage.ID_LABEL, FusionLogicalInterconnectsPage.ID_EDIT_LABEL)
            if ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_EDIT_LABEL_PANEL):
                ui_lib.wait_for_element_and_input_text(FusionLogicalInterconnectsPage.ID_LABEL_NAME, logicalinterconnect_label.label)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ADD_LABEL_BTN)
                ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_OK_LABEL_BTN)
            else:
                logger._warn("Failed to navigate edit label panel")
                return False
        else:
            logger._warn("Could not find Edit button to add label")

        if ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_ADDED_LABEL % logicalinterconnect_label.label):
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ADDED_LABEL % logicalinterconnect_label.label)
            logicalinterconnect_lists = []
            ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_ALL_LI_LIST, PerfConstants.FUSION_PAGE_SYNC)
            logicalinterconnect_lists = [ui_lib.get_text(s) for s in s2l._element_find(FusionLogicalInterconnectsPage.ID_ALL_LI_LIST, False, False)]
            for logical_interconnect in logicalinterconnect_lists:
                if logical_interconnect == logicalinterconnect_label.name:
                    logger._log_to_console_and_log_file("Label {0} is successfully added to the logicalinterconnect '{1}'".format(logicalinterconnect_label.label, logicalinterconnect_label.name))
        else:
            logger._warn("Failed to add label to the selected logicalinterconnect")
            return False
    return True


def validate_interconnect_firmware(*interconnect_lis):
    """
    This function will compare interconnect installed firmware with baseline firmware
    """
    s2l = ui_lib.get_s2l()

    if not s2l._is_element_present(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    if isinstance(interconnect_lis, test_data.DataObj):
        interconnect_lis = [interconnect_lis]
    elif isinstance(interconnect_lis, tuple):
        interconnect_lis = list(interconnect_lis[0])

    flag = 0
    for li in interconnect_lis:
        if not select_logical_interconnect(li.name):
            return False

        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_LINK_OVERIVEW)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ELEMENT_OVERVIEW_FIRMWARE)
        for index in range(1, 3):
            installed_fw = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_SWITCH_FW_DETAILS % index + '/td[4]')
            baseline_fw = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_SWITCH_FW_DETAILS % index + '/td[5]')
            if baseline_fw != installed_fw:
                logger._warn("Installed firmware '{0}' on interconnect '{1}' is not same as baselined firmware '{2}'".format(installed_fw, baseline_fw, li.name))
                flag = flag + 1

        if flag != 0:
            logger._warn("Installed firmware '{0}' and baselined firmware '{1}' of interconnect '{2}' are not same".format(installed_fw, baseline_fw, li.name))
        else:
            logger._log_to_console_and_log_file("Installed firmware '{0}' on interconnect '{1}' is not same as baselined firmware '{2}'".format(installed_fw, baseline_fw, li.name))

    if flag != 0:
        return False
    else:
        return True


def verify_interconnect_firmware_from_li(li_list, *fw_obj):
    """
    This function compares interconnect installed firmware with baseline firmware. Input is a list
    of logical interconnects to validate and the Firmware update object

    Function also gets the installed firmware version from actual hardware and verifies it is same as the installed and baslined version

    Returns True/false along with a dictionary mapping the IC and Firmware version installed
    """

    ic_data = []
    emip_dict = {}
    ic_firmware_dict = {}
    error = 0
    enc_name = ""
    ic_bay = ""
    ic_version = ""
    s2l = ui_lib.get_s2l()

    if isinstance(fw_obj, test_data.DataObj):
        fw_obj = [fw_obj]
    elif isinstance(fw_obj, tuple):
        fw_obj = list(fw_obj[0])

    # navigate to Logical Interconnects page
    if not ui_lib.wait_for_element(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()

    logging.info("Validating Firmware of interconnects in LIs - {}".format(li_list))
    for fw in fw_obj:
        # form EM name:IP dictionary
        for enc in fw.enclosure:
            if (not hasattr(enc, 'type')) or (enc.type) != 'c7k':

                emip_dict[enc.name] = enc.emip

        for li in li_list:
            logging._log_to_console_and_log_file("------- Validating Firmware of Interconnects in LI - {} UI Page -----".format(li))
            # select the LI
            if not select_logical_interconnect(li):
                return False

            # get the number of IC's in the LI
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_PANEL_SELECTOR)
            ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.LINK_FIRMWARE)
            length = len(s2l._element_find(FusionLogicalInterconnectsPage.ID_INTERCONNECT_LIST, False, True))
            logging._log_to_console_and_log_file("Number of IC's in LI '{}' are - {}".format(li, length))

            # validate for each interconnect if the installed version displayed in UI is same as the Baseline version displayed in UI
            for index in range(1, length + 1):
                installed_fw = ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_INTECONNECTS_INSTALLED_FW % index)
                baseline_fw = ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_INTECONNECTS_BASELINE_FW % index)
                ic_name = ui_lib.get_text(FusionLogicalInterconnectsPage.XPATH_INTERCONNECT_NAME % index)
                logging._log_to_console_and_log_file("\n------------Verifying Firmware Versions for IC {}--------------\n".format(ic_name))

                installed_fw = installed_fw.split()[0]
                logging._log_to_console_and_log_file("Installed FW of IC '{}' is - {}".format(ic_name, installed_fw))
                logging._log_to_console_and_log_file("BaseLine FW of IC '{}' is - {}".format(ic_name, baseline_fw))
                # check if the installed and baselin versions displayed in UI are same
                if baseline_fw != installed_fw:
                    logging._warn("Installed firmware visible in UI '{}' of interconnect '{}' is not same as baselined firmware '{}' visible in UI".format(installed_fw, ic_name, baseline_fw))
                    error += 1
                else:
                    logging._log_to_console_and_log_file("Installed firmware visible in UI '{}' of  interconnect '{}' is same as baselined firmware '{}' visible in UI".format(installed_fw, ic_name, baseline_fw))

                ic_firmware_dict[ic_name] = installed_fw.split(' ')[0]
                ic_data = ic_name.split(",")
                enc_name = ic_data[0]
                ic_bay = ic_data[1].split()[1]

                # log in to EM and verify versions
                logging._log_to_console_and_log_file("\n******Verifying Firmware Versions from IC - {}********\n".format(ic_name))
                if (not hasattr(enc, 'type')) or (enc.type) != 'c7k':

                    ic_version = interconnects.verify_tbird_ic_version(emip_dict[enc_name], enc_name, ic_bay, fw.appip, fw.appuname, fw.appasswd, True if fw.dcs.lower() == 'true' else False)
                else:
                    ic_version = interconnects.verify_c7k_ic_version(ic_bay, fw.appip, fw.appuname, fw.appasswd, True if fw.dcs.lower() == 'true' else False)

                if ic_version:
                    if (ic_version.split(' ')[-1] in installed_fw or installed_fw.split('.')[-1] in ic_version) and (ic_version.split(' ')[-1] in baseline_fw or baseline_fw.split('.')[-1] in ic_version):
                        logging._log_to_console_and_log_file("The Baseline version '{}' and the installed version '{}' returned from IC are the same".format(baseline_fw, ic_version))
                    else:
                        logging._warn("The firmware Baseline version '{}' is not installed in the interconnect. The version installed returned from IC is '{}' ".format(baseline_fw, ic_version))
                        error += 1
                else:
                    logging._warn("Unable to get Firmware Version from IC!!")
                    error += 1

            if error == 0:
                logging._log_to_console_and_log_file("Installed firmware and baselined firmware  are same for all interconnects in LI '{}'".format(li))
            logging._log_to_console_and_log_file("\n----------------------------------------------------------------\n")

    if error > 0:
        return (False, ic_firmware_dict)
    else:
        return (True, ic_firmware_dict)


def get_li_stacking_health(liname):
    """
    This function  gets the stacking health status of the LI in Logical interconnects Page

    Returns stacking health status of the LI
    """
    li_stacking_health = None
    # navigate to Logical Interconnects Page
    navigate()
    # select the LI
    if not select_logical_interconnect(liname):
        return False

    FusionUIBase.select_view_by_name('General')
    # get the stacking health in LI
    li_stacking_health = CommonOperationLogicalInterconnect.get_li_stacking_health_status()
    logger.info("stacking health status in LI is '{}'".format(li_stacking_health))
    return li_stacking_health


def verify_logical_interconnect(*inc_obj):
    """ This function is  to verify the Logical Interconnect information

        Example:
       verify_logical_interconnect(*logical_interconnect_obj)
    """
    """ validate_qos_configuration

    Arguments:
      <li>
          name*                     --  Name of logical interconnect  as a string.
         QoS*                       -- To verify QoS type in logical interconnects page possible values:Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
        * Required Arguments

    Example:
        data/lis -> @{TestData.lis}
        <lis>
            <li  name="Enc-76-LIG1"
                 QoS="Passthrough"
            </li>
        </lis>
        """
    """ validates snmpv3 configuration

    Arguments:
      <li>
          name*                 --  Name of logical interconnect  as a string.
         <snmpv3>               -- To verify snmpv3 in logical interconnects
             <snmpuser>         -- To verify snmp user configurations
             <trapdestination>  --  To verify snmpv3 trapdestination settings
         </snmpv3>
        </li>
        * Required Arguments

    Example:
        data/lis -> @{TestData.lis}
        <verifyli>
            <li  name="LI-LE">
                 <snmpv3 snmpv3enabled="true" readcommunity="public">
                     <snmpuser username="user1" security_level="none"></snmpuser>
                     <trapdestination trapdestination="10.1.101.1" trapformat="snmpv3" notificationtype="Trap" username="user1"
                         vcm_traps="Legacy"></trapdestination>
                </snmpv3>
            </li>
        <verifyli>
    """
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS)

    if isinstance(inc_obj, test_data.DataObj):
        inc_obj = [inc_obj]
    elif isinstance(inc_obj, tuple):
        inc_obj = list(inc_obj[0])

    total = len(inc_obj)
    not_exists = 0
    verified_pass = 0

    for n, inc in enumerate(inc_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        logger.info("verifying Logical Interconnect info of Logical Interconnect named '%s'" % inc.name)

        if not VerifyLogicalInterconnects.verify_logical_interconnect_exist(inc.name, timeout=5, fail_if_false=False):
            logger.warn("Logical Interconnect '%s' does not exist" % inc.name)
            not_exists += 1
            continue

        CommonOperationLogicalInterconnect.click_logical_interconnect(inc.name, timeout=5)
        if hasattr(inc, 'qos'):
            FusionUIBase.select_view_by_name('Quality of Service')
            VerifyLogicalInterconnects.verify_quality_of_service_qos_configuration_type(inc.QoS)
        FusionUIBase.select_view_by_name(view_name="Interconnect Settings", timeout=5, fail_if_false=False)

        if hasattr(inc, 'pausefloodprotection'):
            logger.info("verifying Pause flood protection status")
            if not VerifyLogicalInterconnects.verify_pause_flood_status(inc.pausefloodprotection, fail_if_false=False):
                logger.info("Pause flood protection is '%s'" % (inc.pausefloodprotection))
                ui_lib.fail_test("Pause flood protection status is '%s'" % (inc.pausefloodprotection))

        if hasattr(inc, 'snmpv3'):
            _verify_logical_interconnect_snmp(inc.snmpv3)

        result = {}
        settings_list = inc.lldpsettings
        for m, settings in enumerate(settings_list):
            num = m + 1
            if hasattr(settings, 'lldptagging'):
                if not VerifyLogicalInterconnects.verify_taggedlldp_status(settings.lldptagging):
                    logger.warn("'lldp status' of Logical interconnect '%s' is not '%s', verification failed." % (inc.name, settings.lldptagging))
                    result['lldp_status_%d' % num] = False
                else:
                    result['lldp_status_%d' % num] = True

            if hasattr(settings, 'lldpenhancedtlv'):
                if not VerifyLogicalInterconnects.verify_enhancedlldp_status(settings.lldpenhancedtlv):
                    logger.warn("'lldp status' of Logical interconnect '%s' is not '%s', verification failed." % (inc.name, settings.lldpenhancedtlv))
                    result['lldpenhanced_status_%d' % num] = False
                else:
                    result['lldpenhanced_status_%d' % num] = True

            if hasattr(settings, 'alertmessage'):
                if not VerifyLogicalInterconnects.verify_logicalinterconnects_alert_message(settings.alertmessage):
                    logger.warn("'Alert' of Logical interconnect '%s' is not '%s', verification failed." % (inc.name, settings.alertmessage))
                    result['Alert%d' % num] = False
                else:
                    result['Alert%d' % num] = True
        verified_pass += 1
    logger.info("{0} == Summary == {0}".format('-' * 14))
    if total - not_exists == 0:
        logger.warn("no logical interconnect to verify info against! all %s logical interconnect(s) is NOT existing, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
        ui_lib.fail_test("Test failed No LI to update", captureScreenshot)
    else:
        if verified_pass < total:
            logger.warn("not all of the elements are successfully verified PASS - %s out of %s passed " % (verified_pass, total))
            if verified_pass + not_exists == total:
                logger.warn("%s not-existing li elements skipped, keyword '%s' returns a 'False'" % (not_exists, sys._getframe().f_code.co_name))
                ui_lib.fail_test("Not existing li elements", captureScreenshot)
            else:
                logger.warn("%s not-existing li elements skipped, "
                            "%s li element(s) left is failed being verified PASS " % (not_exists, total - verified_pass - not_exists))
                ui_lib.fail_test("failuremsg", captureScreenshot)

    logger.info("all of the li element(s) is successfully verified PASS - %s out of %s " % (verified_pass, total))
    return True


def validation_c7k_updatefirmwarealerts_li(*objfwbundle):
    """
    This  function is to validate the alert messages found for li  firmware  update operations
    Example :
            validation_c7k_updatefirmwarealerts_li(*objfwbundle)
    """

    logger.info(objfwbundle)
    selenium2lib = ui_lib.get_s2l()
    failed_times = 0
    if not selenium2lib._is_element_present(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()
    s2l = ui_lib.get_s2l()
    selenium2lib = ui_lib.get_s2l()
    found = 0

    if isinstance(objfwbundle, test_data.DataObj):

        objfwbundle = [objfwbundle]
    elif isinstance(objfwbundle, tuple):
        objfwbundle = list(objfwbundle[0])

    for logicalconnect in objfwbundle:

        LImessage_list = ["Staging started for logical interconnect %s" % (logicalconnect.LIname),
                          "Stage success for logical interconnect %s" % (logicalconnect.LIname),
                          "Activation started for logical interconnect %s" % (logicalconnect.LIname),
                          "Activate success for logical interconnect %s" % (logicalconnect.LIname)]

        LImessage_list_stage = ["Staging started for logical interconnect %s" % (logicalconnect.LIname),
                                "Stage success for logical interconnect %s" % (logicalconnect.LIname)]
        LImessage_list_update = ["Update started for logical interconnect %s" % (logicalconnect.LIname),
                                 "Update success for logical interconnect %s" % (logicalconnect.LIname)]

        if logicalconnect.stage == "Yes":

            message_list = LImessage_list_stage
            num_message = len(message_list)
            # CommonOperationLogicalInterconnect.click_logical_interconnect_view(10, fail_if_false=False)

            if not (CommonOperationLogicalInterconnect.click_logical_interconnect_activity(10)):
                selenium2lib.capture_page_screenshot()
                logger.warn("failed to select activity..please check")
                failed_times += 1

            for message in message_list:
                if (CommonOperationLogicalInterconnect.wait_logical_interconnect_activity_message(message, 10, fail_if_false=False)):
                    BuiltIn().sleep(5)
                    time = (GeneralLogicalInterconnectsElements.ID_ACTIVITY_MESSAGE % message) + "/td[4]/div[2]"
                    selenium2lib.mouse_over(time)
                    BuiltIn().sleep(7)
                    selenium2lib.mouse_over(time)
                    timeago = (ui_lib.get_text(time, 10)).split()
                    logger.info("Event found at -  %s" % timeago)

                # look for the activity message in last two hours
                    if (timeago):
                        if timeago[1].lower() == "hours" and int(timeago[0]) > 2:
                            logger.warn("Expected message %s found is not within last 2 hours!! Discarding Old activity Message" % message)
                            continue
                        elif timeago[1].lower() in ("months", "year", "years"):
                            logger.warn("Expected message '{}' found is of '{}'!!".format(message, timeago))
                            continue
                        found += 1
                        logger.info("\nActivity : '%s'  found in IC activity page" % message)
                    else:
                        logger.info("\nMessage %s is found but testscript failed to extract exact time" % message)
                        continue
                else:
                    logger.warn("Expected message '%s' is not found in activity page:" % message)
        elif logicalconnect.update == "Yes":

            message_list = LImessage_list_update
            num_message = len(message_list)

            if not (CommonOperationLogicalInterconnect.click_logical_interconnect_activity(10, fail_if_false=False)):
                selenium2lib.capture_page_screenshot()
                logger.warn("failed to select activity..please check")
                failed_times += 1

            for message in message_list:
                if (CommonOperationLogicalInterconnect.wait_logical_interconnect_activity_message(message, 10, fail_if_false=False)):
                    BuiltIn().sleep(5)
                    time = (GeneralLogicalInterconnectsElements.ID_ACTIVITY_MESSAGE % message) + "/td[4]/div[2]"
                    selenium2lib.mouse_over(time)
                    BuiltIn().sleep(7)
                    selenium2lib.mouse_over(time)
                    timeago = (ui_lib.get_text(time, 10)).split()
                    logger.info("Event found at -  %s" % timeago)

                # look for the activity message in last two hours
                    if (timeago):
                        if timeago[1].lower() == "hours" and int(timeago[0]) > 2:
                            logger.warn("Expected message %s found is not within last 2 hours!! Discarding Old activity Message" % message)
                            continue
                        elif timeago[1].lower() in ("months", "year", "years"):
                            logger.warn("Expected message '{}' found is of '{}'!!".format(message, timeago))
                            continue
                        found += 1
                        logger.info("\nActivity : '%s'  found in IC activity page" % message)
                    else:
                        logger.info("\nMessage %s is found but testscript failed to extract exact time" % message)
                        continue
                else:
                    logger.warn("Expected message '%s' is not found in activity page:" % message)

        else:
            message_list = LImessage_list
            num_message = len(message_list)

            if not (CommonOperationLogicalInterconnect.click_logical_interconnect_activity(10, fail_if_false=False)):
                selenium2lib.capture_page_screenshot()
                logger.warn("failed to select activity..please check")
                failed_times += 1
            for message in message_list:
                if (CommonOperationLogicalInterconnect.wait_logical_interconnect_activity_message(message, 10, fail_if_false=False)):
                    BuiltIn().sleep(5)
                    time = (GeneralLogicalInterconnectsElements.ID_ACTIVITY_MESSAGE % message) + "/td[4]/div[2]"
                    selenium2lib.mouse_over(time)
                    BuiltIn().sleep(7)
                    selenium2lib.mouse_over(time)
                    timeago = (ui_lib.get_text(time, 10)).split()
                    logger.info("Event found at -  %s" % timeago)

                # look for the activity message in last two hours
                    if (timeago):
                        if timeago[1].lower() == "hours" and int(timeago[0]) > 2:
                            logger.warn("Expected message %s found is not within last 2 hours!! Discarding Old activity Message" % message)
                            continue
                        elif timeago[1].lower() in ("months", "year", "years"):
                            logger.warn("Expected message '{}' found is of '{}'!!".format(message, timeago))
                            continue
                        found += 1
                        logger.info("\nActivity : '%s'  found in IC activity page" % message)
                    else:
                        logger.info("\nMessage %s is found but testscript failed to extract exact time" % message)
                        continue
                else:
                    logger.warn("Expected message '%s' is not found in activity page:" % message)

        if (found == num_message):
            logger.info("All the excepted messages found in LI activity page")
            return True
        else:
            logger.warn("All the excepted messages are not found in LI activity page")
            return False


def validate_error_message_li(*objfwbundle):
    """
    This  function validates  the negative alert messages
    """
    logger.info(objfwbundle)
    selenium2lib = ui_lib.get_s2l()
    failed_times = 0
    if not selenium2lib._is_element_present(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        ui_lib.wait_for_element(FusionUIBaseElements.ID_MAIN_MENU_CONTROL, PerfConstants.DEFAULT_SYNC_TIME)
        navigate()
    s2l = ui_lib.get_s2l()
    selenium2lib = ui_lib.get_s2l()
    found = 0

    if isinstance(objfwbundle, test_data.DataObj):

        objfwbundle = [objfwbundle]
    elif isinstance(objfwbundle, tuple):
        objfwbundle = list(objfwbundle[0])

    for logicalconnect in objfwbundle:

        li_message_list = ["unable to update firmware for the logical interconnect SGH420HHYA-LIG_B1 as an attempt was made to downgrade the firmware without selecting the force option."]

        num_message = len(li_message_list)

        if not (CommonOperationLogicalInterconnect.click_logical_interconnect_activity(10, fail_if_false=False)):
            selenium2lib.capture_page_screenshot()
            logger.warn("failed to select activity..please check")
            failed_times += 1

        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_SELECT_ACTIVITY_VIEW_LI)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_COLLAPSE_XPATH)
        li_neg_message = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_Notification_ACTXPATH_PATH)

        logging._log_to_console_and_log_file("Message found : " + str(li_neg_message))
        return li_neg_message


def display_interconnects_link_ports_in_li(lis_obj):
    """
        This function hover the each port and display the
        interconnect port information at LI level.
    """

    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)

    for logicalinterconnects in lis_obj:

        name = logicalinterconnects.name

        if not VerifyLogicalInterconnects.verify_logical_interconnect_exist(name, 5, False):
            logger.warn("Logical interconnect %s does not exist" % name)
            failed_times += 1
            continue
        else:
            CommonOperationLogicalInterconnect.click_logical_interconnect(name, 5, False)
            # wait target logical interconnect get focus
            logger.info("Wait for logical interconnect %s to be selected." % name)

            if not CommonOperationLogicalInterconnect.wait_logical_interconnect_selected(name, 5, False):
                logger.warn("Failed to select logical interconnect %s" % name)
                failed_times += 1
                continue

            encl_list = []
            encl_list = InterconnectLinkPortsOperations.get_enclosure_list_from_logical_interconnect(5)
            encl_len = (len(encl_list))

            logger.info("Interconnect Link Ports information  for %s Enclosures" % (len(encl_list)))

            count = 1
            for encl in encl_list:
                bay_list = InterconnectLinkPortsOperations.get_interconnect_bay_list(count, 5, False)
                for bay in bay_list:
                    bay_label = InterconnectLinkPortsOperations.get_interconnect_bay_label(count, bay, 5, False)
                    icm_model = InterconnectLinkPortsOperations.get_interconnect_bay_model(count, bay, 5, False)
                    logger.info(icm_model)
                    icm_model = str(icm_model).split(":")
                    logger.info("---------------------------------------\n")
                    logger.info("enclosure name is - %s" % encl)
                    logger.info("Interconnect bay is - %s" % bay_label)
                    logger.info("Interconnect Model is - %s" % icm_model[1])
                    logger.info("---------------------------------------\n")
                    if ("Virtual Connect SE 40Gb F8 Module for Synergy" in icm_model[1]):

                        # Mouse over to each port and capture the state, connected and port status..
                        for i in range(1, 5):

                            port = InterconnectLinkPortsOperations.get_overview_mouseover_port_information(count, bay, i, 5, False)
                            status = InterconnectLinkPortsOperations.get_overview_mouseover_port_status(count, bay, i, 5, False)
                            state = InterconnectLinkPortsOperations.get_overview_mouseover_port_state(count, bay, i, 5, False)
                            connected_to = InterconnectLinkPortsOperations.get_overview_mouseover_port_connectedto(count, bay, i, 5, False)
                            logger.info("hovered over cxp port information")
                            logger.info("port - %s status is - %s" % (port, status))
                            logger.info("State - %s" % state)
                            logger.info("Connected to - %s" % connected_to)

                    # hover the extender interconnect to display state, connected to information
                    elif(("Synergy 20Gb Interconnect Link Module" in icm_model[1])):
                        # Mouse over to each port and capture the state, connected and port status..
                        for i in range(1, 3):

                            port = InterconnectLinkPortsOperations.get_overview_mouseover_port_information_of_extender_interconnect(count, bay, i, 5, False)
                            status = InterconnectLinkPortsOperations.get_overview_mouseover_port_status_of_extender_interconnect(count, bay, i, 5, False)
                            state = InterconnectLinkPortsOperations.get_overview_mouseover_port_state_of_extender_interconnect(count, bay, i, 5, False)
                            connected_to = InterconnectLinkPortsOperations.get_overview_mouseover_port_connectedto_of_extender_interconnect(count, bay, i, 5, False)
                            loger.info("hovered over cxp port information")
                            logger.info("port - %s status is - %s" % (port, status))
                            logger.info("State - %s" % state)
                            logger.info("Connected to - %s" % connected_to)

                    # hover the extender interconnect to display state, connected to information
                    elif(("Synergy 10Gb Interconnect Link Module" in icm_model[1])):
                        # Mouse over to each port and capture the state, connected and port status..
                        for i in range(1, 2):

                            port = InterconnectLinkPortsOperations.get_overview_mouseover_port_information_of_extender_interconnect(count, bay, i, 5, False)
                            status = InterconnectLinkPortsOperations.get_overview_mouseover_port_status_of_extender_interconnect(count, bay, i, 5, False)
                            state = InterconnectLinkPortsOperations.get_overview_mouseover_port_state_of_extender_interconnect(count, bay, i, 5, False)
                            connected_to = InterconnectLinkPortsOperations.get_overview_mouseover_port_connectedto_of_extender_interconnect(count, bay, i, 5, False)
                            logger.info("hovered over cxp port information")
                            logger.info("port - %s status is - %s" % (port, status))
                            logger.info("State - %s" % state)
                            logger.info("Connected to - %s" % connected_to)
                count += 1


def validate_qos_configuration_in_li(*editlis_obj):
    """ validate_qos_configuration

    Arguments:
      <li>
          name*                     --  Name of logical interconnect  as a string.
          verifytype*               -- to verify the QoS type in LIG possible values:Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          VERIFYFCOE*               -- To verify if fcoelossless class is available in Custom (with FCoE lossless) type
          qos_configuration_type*   --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          classname*                --  name of the class possible value:FCoE lossless
          qos_type                  --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
          verifyingpassthroughoptions* --  To verify the option for QoS type Passthrough possible value:none
          dot1p_priority             --    Specifies the dot1p priority value to remark for the egressing packets. This provides flexibility to control priority treatment for packets at the next hops based on the remarked dot1p value
    * Required Arguments

    Example:
        data/lis -> @{TestData.lis}
        <lis>
            <li  name="Enc-76-LIG1"
                 verifytype = "Custom (with FCoE lossless)"
                                 VERIFYFCOE ="None"
                                 QoS = "passthrough"
                 qos_type="Custom (with FCoE lossless)"
                 verifyingpassthroughoptions="None"
                                 sharevalue = "1,3,6,9,12,15"
                                 egresspriority = "0, 1, 3, 4, 6, 7"
                                 dot1pvalue = "0,1,2,3,4,5"
                                 dscpvalue = "DSCP_10_AF11,DSCP_10_AF11, DSCP_0_CS0, DSCP_12_AF12, DSCP_14_AF13, DSCP_8_CS1" dot1p_dscp_mappings="2,4,6,8,10,12,14,16"
            </li>
        </lis>
     Example for attribute "dot1p_priority":
        data/lis -> @{TestData.lis}
        <lis>
         <li  name="Enc-76-LIG1"
              qos_configuration_type = "Custom (with FCoE lossless)"
              classname="Class3"
              classEnable="Enabled/Disabled"
              dot1p_priority="1,2,4,5,6,7"
           </li>
        </lis>
    """
    s2l = ui_lib.get_s2l()

    if not s2l._is_element_present(FusionLogicalInterconnectsPage.ID_PAGE_LABEL):
        navigate()
    if isinstance(editlis_obj, test_data.DataObj):
        editlis_obj = [editlis_obj]
    elif isinstance(editlis_obj, tuple):
        editlis_obj = list(editlis_obj[0])

    for logicalinterconnects in editlis_obj:
        navigate()
        editliname = logicalinterconnects.name
        if not select_logical_interconnect(editliname):
            ui_lib.fail_test("Exiting Edit LI Function, Not selected LI %s" % editliname)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_ACTION_MAIN_BTN)
        ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_MENU_ACTION_LS_EDIT)
        s2l.wait_until_page_contains_element(FusionLogicalInterconnectsPage.ID_ELEMENT_EDIT_EDIT_LOGICAL_INTERCONNECTS)
        FusionUIBase.select_view_by_name('Quality of Service')
        if hasattr(logicalinterconnects, 'verifytype'):
            EditLogicalInterconnects.verify_quality_of_service_qos_configuration_type(logicalinterconnects.verifytype)
        if hasattr(logicalinterconnects, 'VERIFYFCOE'):
            logger.info("Verifying FCoE lossless")
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            if EditLogicalInterconnects.verify_fcoelosssless_class_exists(logicalinterconnects.classname):
                logger.info("FCoE lossless class is available in QoS customWithFCoE")
                if not EditLogicalInterconnects.verify_fcoe_lossless_class_no_edit_option(logicalinterconnects.classname):
                    ui_lib.fail_test("Unexpected behaviour EDIT option is  available")
                logger.info("As expected unable to edit FCoElossless class EDIT option is not available")
            else:
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("FCoE lossless class is not available in QoS customWithFCoE")
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            if EditLogicalInterconnects.verify_fcoelosssless_class_exists(logicalinterconnects.classname, fail_if_false=False):
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("FCoE lossless name is available")
            else:
                logger.info("As expected FCoE lossless class is not available in QoS customWithoutFCoE")
                # verifying share and maxshare
        if hasattr(logicalinterconnects, 'verifyingeditoption'):
            values_list = []
            logger.info("Navigate to edit option")
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            share = EditLogicalInterconnects.get_fcoeshare()
            maxshare = EditLogicalInterconnects.get_fcoemaxshare()
            values_list.append(share)
            values_list.append(maxshare)
            logger.info("list value is % s" % values_list)
            EditLogicalInterconnects.click_cancel_button()
            return values_list
        if hasattr(logicalinterconnects, 'verifytype'):
            EditLogicalInterconnects.verify_quality_of_service_qos_configuration_type(logicalinterconnects.verifytype)
        if hasattr(logicalinterconnects, 'verifyingpassthroughoptions'):
            if VerifyLogicalInterconnects.verify_passthrough_options():
                logger.info("verified passthrough options does not exist")
            else:
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("passthrough options are visible")
        if hasattr(logicalinterconnects, 'verifyqosoptions'):
            count_qos = 0
            qos_list = [item.strip() for item in logicalinterconnects.verifyqosoptions.split(',')]
            uplink_list = [item.strip() for item in logicalinterconnects.uplink.split(',')]
            downlink_list = [item.strip() for item in logicalinterconnects.downlink.split(',')]
            for qos in qos_list:
                count_uplink = 0
                count_downlink = 0
                EditLogicalInterconnects.select_qos_configuration_type(qos)
                if qos != qos_list[0]:
                    for uplink in uplink_list:
                        EditLogicalInterconnects.select_qos_uplink_classfication(uplink)
                        count_uplink += 1
                    if count_uplink != len(uplink_list):
                        ui_lib.fail_test("failed to verify all the uplink options ")
                    for downlink in downlink_list:
                        EditLogicalInterconnects.select_qos_downlink_classfication(downlink)
                        count_downlink += 1
                    if count_uplink != len(downlink_list):
                        ui_lib.fail_test("failed to verify all the downlink options ")
                count_qos += 1
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_custom)
            EditLogicalInterconnects.click_ok_button()
            # Code to verify the detials which are edited are reflecting properly or not
            if count_qos == len(qos_list):
                return True
            else:
                ui_lib.fail_test("failed to verify all the QoS configuration options")
        if hasattr(logicalinterconnects, 'validatedisableclass'):
            logger.info("Check value for the disabled class")
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            isclassenabled = EditLogicalInterconnects.get_class_enabled(logicalinterconnects.classno)
            validatedisableclass = EditLogicalInterconnects.get_share_value(logicalinterconnects.classno, logicalinterconnects.share)
            if isclassenabled == "No" and int(validatedisableclass) == 0:
                logger.info("value 0 is allowed for disabled class")
            else:
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("value 0 is not allowed for enabled class")
                # validating the negative Scenario.error message should be poped up for invalid values such as -1, .10, abcd, @#$% etc
        if hasattr(logicalinterconnects, 'validateshareormax'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            EditLogicalInterconnects.click_qos_class(fail_if_false=False)
            logger.info("Field value %s" % logicalinterconnects.fieldvalues)
            if logicalinterconnects.validateshareormax == "max-share":
                if not EditLogicalInterconnects.input_shareormax(logicalinterconnects.validateshareormax, logicalinterconnects.fieldvalues):
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    EditLogicalInterconnects.click_cancel_button()
                    ui_lib.fail_test("Failed to log text into the textbox")("Failed to log text into the textbox")
                EditLogicalInterconnects.click_max_text()
                error = EditLogicalInterconnects.get_error_message()
                if (error == logicalinterconnects.error) or (error == logicalinterconnects.error2):
                    logger.info("invalid values such as -1, .10, abcd, @#$% etc are not allowed for maxshare values")
                else:
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    EditLogicalInterconnects.click_cancel_button()
                    ui_lib.fail_test("invalid values such as -1, .10, abcd, @#$% etc are allowed")
                EditLogicalInterconnects.click_traffic_cancel_button()
            elif logicalinterconnects.validateshareormax == "share":
                if not EditLogicalInterconnects.input_shareormax(logicalinterconnects.validateshareormax, logicalinterconnects.fieldvalues):
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    EditLogicalInterconnects.click_cancel_button()
                    ui_lib.fail_test("Failed to log text into the textbox")
                EditLogicalInterconnects.click_class_ok_button()
                error = EditLogicalInterconnects.get_error_message()
                if (error == logicalinterconnects.error) or (error == logicalinterconnects.error2):
                    logger.info("invalid values such as -1, .10, abcd, @#$% etc are not allowed for maxshare values")
                else:
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    EditLogicalInterconnects.click_cancel_button()
                    ui_lib.fail_test("invalid values such as -1, .10, abcd, @#$% etc are allowed")
                EditLogicalInterconnects.click_traffic_cancel_button()
            else:
                EditLogicalInterconnects.click_traffic_cancel_button()
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("invalid value")
        if hasattr(logicalinterconnects, 'verify_besteffort'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            EditLogicalInterconnects.input_classname(logicalinterconnects.text, fail_if_false=False)
            logger.info("Best effort is not editable")
            EditLogicalInterconnects.click_traffic_cancel_button()
            # validating the negative Scenario.error message should be poped up if classname is not unique
        if hasattr(logicalinterconnects, 'verify_uniquename'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            unique = EditLogicalInterconnects.get_uniquename()
            logger.info("list value is %s" % unique)
            classes = [item.strip() for item in logicalinterconnects.classes.split(',')]
            logger.info("Classes value %s" % classes)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            EditLogicalInterconnects.input_classname(logicalinterconnects.text)
            EditLogicalInterconnects.click_class_ok_button()
            error = EditLogicalInterconnects.get_error_message()
            if (unique == classes) and (error == logicalinterconnects.error):
                logger.info("Successfully verified that all classnames are unique")
            else:
                EditLogicalInterconnects.click_cancel_button()
                EditLogicalInterconnects.click_traffic_cancel_button()
                ui_lib.fail_test("class names are not unique ")
            EditLogicalInterconnects.click_traffic_cancel_button()
        if hasattr(logicalinterconnects, 'verify_traffic'):
            count_traffic = 0
            traffic_list = [item.strip() for item in logicalinterconnects.verify_traffic.split(',')]
            total_traffic = len(traffic_list)
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            for traffic in traffic_list:
                if not VerifyLogicalInterconnects.verify_traffic_option(traffic):
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    EditLogicalInterconnects.click_cancel_button()
                    ui_lib.fail_test("failed to verify traffic class fields")
            EditLogicalInterconnects.click_traffic_cancel_button()
        if hasattr(logicalinterconnects, 'mappings'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            class_list = [item.strip() for item in logicalinterconnects.classname.split(',')]
            nomapping_list = [item.strip() for item in logicalinterconnects.clasnosmapping.split(',')]
            mapping_list = [item.strip() for item in logicalinterconnects.mappings.split(',')]
            for class1 in class_list:
                EditLogicalInterconnects.select_editoption(class1)
                EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                EditLogicalInterconnects.input_share_values(logicalinterconnects.sharevalue)
                EditLogicalInterconnects.tick_dot1p_values(logicalinterconnects.dot1pvalues)
                EditLogicalInterconnects.tick_dscp_values(logicalinterconnects.dscpvalues)
                EditLogicalInterconnects.click_class_ok_button()
                EditLogicalInterconnects.select_classname(class1)
                for value in mapping_list:
                    if value != "No mappings":
                        if not VerifyLogicalInterconnects.verify_mappings_visibility(value):
                            ui_lib.fail_test("failed to verify the DOTIP and DSCP VALUES for selected Class")
                        logger.info(" Sucessfully verifying DOT1P and DSCP values for  %s" % class1)
            for class1 in nomapping_list:
                EditLogicalInterconnects.select_classname(class1)
                for value in mapping_list:
                    if value == "No mappings":
                        logger.info("value is %s" % value)
                        if not VerifyLogicalInterconnects.verify_mappings_visibility(value):
                            ui_lib.fail_test("failed to verify NO mappings values for  %s" % class1)
                        logger.info(" Sucessfully verifying NO mappings values for  %s" % class1)
        if hasattr(logicalinterconnects, 'dot1p'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            doip_list = [item.strip() for item in logicalinterconnects.dot1p.split(',')]
            EditLogicalInterconnects.click_qos_class(fail_if_false=False)
            for qos in doip_list:
                if not VerifyLogicalInterconnects.verify_dot1poption(qos):
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    EditLogicalInterconnects.click_cancel_button()
                    ui_lib.fail_test("failed to verify dot1pvalue is not present in selected QoS type")
            EditLogicalInterconnects.click_traffic_cancel_button()
            # validating the negative Scenario.error message should be poped up if classname exceeds 225 chaeracters
        if hasattr(logicalinterconnects, 'uniqueclass'):
            logger.info("%s" % logicalinterconnects.uniqueclass)
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            EditLogicalInterconnects.input_classname(logicalinterconnects.uniqueclass)
            EditLogicalInterconnects.click_class_ok_button()
            error = EditLogicalInterconnects.get_error_message()
            logger.info(" error message %s" % error)
            if not error:
                ui_lib.fail_test(" error message did not pop up ")
            if (error == logicalinterconnects.error):
                logger.info("As expected error message is poped up if classname exceeds 225 characters")
            else:
                EditLogicalInterconnects.click_traffic_cancel_button()
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("error message is not poped up if classname exceeds 225 characters")
            EditLogicalInterconnects.click_traffic_cancel_button()
            # validating the negative Scenario.error message should be poped up if Best effort class share values is less than 1
        if hasattr(logicalinterconnects, 'verifysharevalues'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            class_list = [item.strip() for item in logicalinterconnects.classname.split(',')]
            initial_value = EditLogicalInterconnects.get_share_value(logicalinterconnects.besteffort, logicalinterconnects.share)
            set_value = int(initial_value) / 2
            for class1 in class_list:
                EditLogicalInterconnects.select_editoption(class1)
                EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                EditLogicalInterconnects.input_share_values(set_value)
                EditLogicalInterconnects.click_class_ok_button()
                class_value = EditLogicalInterconnects.get_share_value(class1, logicalinterconnects.share)
                logger.info("share value for selected class is %s" % class_value)
                best_effort = EditLogicalInterconnects.get_share_value(logicalinterconnects.besteffort, logicalinterconnects.share)
                actual_value = int(initial_value) - int(class_value)
                logger.info("best effort share value is adjusted and it is less than 100 %s " % best_effort)
                if int(best_effort) == int(actual_value) and int(best_effort) > 1:
                    logger.info("best effort share value is adjusted and it is less than 100")
                    set_value = int(best_effort) + 1
                    initial_value = EditLogicalInterconnects.get_share_value(logicalinterconnects.besteffort, logicalinterconnects.share)
                else:
                    logger.info("share value execeeds 100  ")
                    ui_lib.wait_for_element_and_click(FusionLogicalInterconnectsPage.ID_BTN_OK_LS_EDIT)
                    error = EditLogicalInterconnects.get_qos_error_msg(timeout=30)
                    if (error == logicalinterconnects.error):
                        logger.info("Best efforts value is less than 1 %s " % error)
                    else:
                        EditLogicalInterconnects.click_cancel_button()
                        ui_lib.fail_test("error message is not poped up when besteffort value is lees than 1")
        if hasattr(logicalinterconnects, 'verifyqossettings'):
            logger.info("Verifying qos Settings")
            EditLogicalInterconnects.select_quality_of_service_section()
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
        if hasattr(logicalinterconnects, 'qosconfigurationtype'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qosconfigurationtype)
            if not EditLogicalInterconnects.verify_fcoe_lossless_class_no_edit_option(logicalinterconnects.classname):
                ui_lib.fail_test("Unexpected behaviour!!FCoElossless class is editable ")
            logger.info("As expected unable to edit FCoElossless class EDIT option is not available")
        if hasattr(logicalinterconnects, 'priorities'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            if not EditLogicalInterconnects.select_editoption(logicalinterconnects.Classname):
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("Failed to click edit button")
            if not EditLogicalInterconnects.click_qos_class(fail_if_false=False):
                EditLogicalInterconnects.click_traffic_cancel_button()
                ui_lib.fail_test("Failed to enable qos class")
            if EditLogicalInterconnects.select_egress_priority(logicalinterconnects.priority, fail_if_false=False):
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("Failed! Priority 3 is available in the list")
            EditLogicalInterconnects.click_traffic_cancel_button()
            logger.info("Successfully verified that priority 3 is not available in the list")
        if hasattr(logicalinterconnects, 'dot1p_priority'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            besteffort_fcoe_priority = EditLogicalInterconnects.get_besteffort_fcoe_priority()
            logger.info(besteffort_fcoe_priority)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            classenable_list = [item.strip() for item in logicalinterconnects.classenable.split('/')]
            logger.info("classEnable_list value %s" % classenable_list)
            total_len = len(classenable_list)
            logger.info("length of classenable_list values are %d" % total_len)
            for classenable in classenable_list:
                logger.info("value in list is %s" % classenable)
                if classenable == ("Enabled"):
                    EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                    if VerifyLogicalInterconnects.verify_priority_availability(True):
                        logger.info("Egress DOT1P priorities are available")
                        dot1p_priority_list = [item.strip() for item in logicalinterconnects.dot1p_priority.split(',')]
                        logger.info("DOT1P_Priority_list value %s" % dot1p_priority_list)
                        EditLogicalInterconnects.click_dot1p_priority_dropdown()
                        logger.info("dropdown list displayed")
                        for i in dot1p_priority_list:
                            dot1p_priority_ui = EditLogicalInterconnects.select_dot1p_priority(i)
                            logger.info(dot1p_priority_ui)
                            logger.info(i)
                            if re.search(i, dot1p_priority_ui):
                                if dot1p_priority_ui != besteffort_fcoe_priority[0] and dot1p_priority_ui != besteffort_fcoe_priority[1]:
                                    logger.info("%s is not Best Effort and FCoE class priority" % dot1p_priority_ui)
                                else:
                                    logger.info("Best Effort and FCoE class priorities are available in Egress DOT1P priority dropdown list")
                                    ui_lib.fail_test("Unexpected Behaviour")
                            else:
                                ui_lib.fail_test("priority doesn't get matched")
                    else:
                        ui_lib.fail_test("Egress DOT1P priorities are available by defect")
                elif classenable == ("Disabled"):
                    EditLogicalInterconnects.click_qos_class_disable()
                    if VerifyLogicalInterconnects.verify_priority_availability(False):
                        logger.info("Egress DOT1P priorities are not available")
                    else:
                        ui_lib.fail_test("Egress DOT1P priorities are not available by defect")
                else:
                    ui_lib.fail_test("Invalid values")
            EditLogicalInterconnects.click_traffic_cancel_button()
        if hasattr(logicalinterconnects, 'enableclass'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            classname_list = [item.strip() for item in logicalinterconnects.enableclass.split(',')]
            total_class = [item.strip() for item in logicalinterconnects.classeslist.split(',')]
            classes = [item.strip() for item in logicalinterconnects.classeslist.split(',')]
            for name in classname_list:
                count = 0
                EditLogicalInterconnects.select_editoption(name)
                EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                EditLogicalInterconnects.input_share_values(logicalinterconnects.Sharevalues)
                if not EditLogicalInterconnects.click_qos_real_class():
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    ui_lib.fail_test("Failed to disable class")
                EditLogicalInterconnects.click_class_ok_button()
                real_time_value = EditLogicalInterconnects.get_real_time_value_of_class(name)
                logger.info("select value [ %s ]" % real_time_value)
                if(real_time_value == 'Yes'):
                    logger.info("The real time is enabled")
                else:
                    EditLogicalInterconnects.click_cancel_button()
                    return False
            for classname in classes:
                real_time_value = EditLogicalInterconnects.get_real_time_coloumn_value(classname)
                logger.info("Real time value for the class is %s" % classname)
                if (real_time_value == 'Yes'):
                    logger.info("The real time is enabled")
                    if (name == classname):
                        logger.info("The real time is enabled for the class %s" % classname)
                        count += 1
                else:
                    logger.info("The real time value is not enabled for remaining classes ")
            if count == 1:
                logger.info("Real Time is enabled only for one class")
            else:
                EditLogicalInterconnects.click_cancel_button()
                ui_lib.fail_test("Real Time is enabled only for more than one class")
        if hasattr(logicalinterconnects, 'mapping_availability'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            logger.info("clicking the edit button of the given class")
            EditLogicalInterconnects.select_editoption(logicalinterconnects.classname)
            classenable_list = [item.strip() for item in logicalinterconnects.classenable.split('/')]
            logger.info("classEnable_list value %s" % classenable_list)
            total_len = len(classenable_list)
            logger.info("length of classenable_list values are %d" % total_len)
            for classenable in classenable_list:
                logger.info("value in list is %s" % classenable)
                if classenable == ("Enabled"):
                    EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                    if VerifyLogicalInterconnects.verify_dot1p_and_dscp_availability(True):
                        logger.info("DOT1P and DSCP mappings are available")
                        dot1p_value_list = [item.strip() for item in logicalinterconnects.dot1pvalue.split(',')]
                        logger.info("dot1p_value_list value %s" % dot1p_value_list)
                        total_len = len(dot1p_value_list)
                        logger.info("length of dot1p_value_list values are %d" % total_len)
                        dot1p_current_list = [item.strip() for item in logicalinterconnects.dot1pcurrent.split(',')]
                        logger.info("dot1_current_list value %s" % dot1p_current_list)
                        total_len = len(dot1p_current_list)
                        logger.info("length of dot1p_current_list values are %d" % total_len)
                        total_len = total_len + 1
                        for i in range(1, total_len):
                            dot1p_value = EditLogicalInterconnects.get_text_dot1p_value(i)
                            logger.info(dot1p_value)
                            dot1p_current = EditLogicalInterconnects.get_text_dot1p_current(i)
                            logger.info(dot1p_current)
                            if dot1p_value == dot1p_value_list[i - 1] and dot1p_current == dot1p_current_list[i - 1]:
                                logger.info("%s Initial configuration verified successfully for DOT1P" % i)
                            else:
                                ui_lib.fail_test("Initial configuration not verified for DOT1P")
                        dscp_value_list = [item.strip() for item in logicalinterconnects.dscpvalue.split('/')]
                        logger.info("dscp_value_list value %s" % dscp_value_list)
                        total_len = len(dscp_value_list)
                        logger.info("length of dscp_value_list values are %d" % total_len)

                        dscp_current_list = [item.strip() for item in logicalinterconnects.dscpcurrent.split(',')]
                        logger.info("dscp_current_list value %s" % dscp_current_list)
                        total_len = len(dscp_current_list)
                        logger.info("length of dot1p_current_list values are %d" % total_len)
                        total_len = total_len + 1
                        for i in range(1, total_len):
                            dscp_value = EditLogicalInterconnects.get_text_dscp_value(i)
                            logger.info(dscp_value)
                            dscp_current = EditLogicalInterconnects.get_text_dscp_current(i)
                            logger.info(dscp_current)
                            if dscp_value == dscp_value_list[i - 1] and dscp_current == dscp_current_list[i - 1]:
                                logger.info(" %s Initial configuration verified successfully for DSCP" % i)
                            else:
                                ui_lib.fail_test("Initial configuration not verified for DSCP")
                    else:
                        ui_lib.fail_test("DOT1P and DSCP mappings are not available by defect")
                elif classenable == ("Disabled"):
                    EditLogicalInterconnects.click_qos_class_disable()
                    if not VerifyLogicalInterconnects.verify_dot1p_and_dscp_availability(False):
                        ui_lib.fail_test("DOT1P and DSCP mappings are available by defect")
                    else:
                        logger.info("DOT1P and DSCP mappings are removed")
                else:
                    ui_lib.fail_test("Invalid values")
            EditLogicalInterconnects.click_traffic_cancel_button()
        if hasattr(logicalinterconnects, 'qostype'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            values_list1 = []
            values_list2 = []
            values_list3 = []
            class_list = [item.strip() for item in logicalinterconnects.classname.split(',')]
            value_list = [item.strip() for item in logicalinterconnects.value.split(',')]
            for value in class_list:
                EditLogicalInterconnects.select_editoption(value)
                EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                EditLogicalInterconnects.input_share_values(logicalinterconnects.share)
                EditLogicalInterconnects.input_maxshare_value(logicalinterconnects.maxshare)
                EditLogicalInterconnects.click_class_ok_button()
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            for value in class_list:
                val = EditLogicalInterconnects.get_class_enabled(value)
                values_list1.append(val)
                logger.info("successfully got text for enabled %s" % values_list1)
                val = EditLogicalInterconnects.get_share_value(value, logicalinterconnects.sharetext)
                values_list2.append(val)
                logger.info("successfully got text for share %s" % values_list2)
                val = EditLogicalInterconnects.get_maxsharevalue(value)
                values_list3.append(val)
                logger.info("successfully got text for maxshare %s" % values_list3)
            EditLogicalInterconnects.click_cancel_button()
            return values_list1, values_list2, values_list3
        if hasattr(logicalinterconnects, 'realclass'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.realclass)
            if not VerifyLogicalInterconnects.verify_realclass_invisibility(fail_if_false=False):
                ui_lib.fail_test("Unexpected behaviour real class is visible when clas is disabled")
            EditLogicalInterconnects.click_qos_class(fail_if_false=False)
            EditLogicalInterconnects.click_qos_real_class()
            check_list = [item.strip() for item in logicalinterconnects.share.split(',')]
            logger.info("Check_list value %s" % check_list)
            total_len = len(check_list)
            logger.info("No of values to be checked are %d" % total_len)
            for value in check_list:
                if (int(value) <= 50):
                    EditLogicalInterconnects.input_share_values(value)
                    EditLogicalInterconnects.click_class_ok_button()
                    sharevalue = EditLogicalInterconnects.get_share_value(logicalinterconnects.realclass, logicalinterconnects.sharetext)
                    maxsharevalue = EditLogicalInterconnects.get_maxsharevalue(logicalinterconnects.realclass)
                    if (sharevalue == maxsharevalue):
                        logger.info("Sucessfully verified share and maxshare has same values after enabling real class in the table")
                    else:
                        ui_lib.test_fail("share and maxshare has different values")
                else:
                    EditLogicalInterconnects.select_editoption(logicalinterconnects.realclass)
                    EditLogicalInterconnects.input_share_values(value)
                    EditLogicalInterconnects.click_class_ok_button()
                    error = EditLogicalInterconnects.get_error_message()
                    logger.info(error)
                    EditLogicalInterconnects.click_traffic_cancel_button()
                    EditLogicalInterconnects.click_cancel_button()
                    return error
        if hasattr(logicalinterconnects, 'Reset'):
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_configuration_type)
            i = 0
            values_list1 = []
            values_list2 = []
            values_list3 = []
            values_list4 = []
            class_list = [item.strip() for item in logicalinterconnects.classname.split(',')]
            value_list = [item.strip() for item in logicalinterconnects.value.split(',')]
            for value in class_list:
                EditLogicalInterconnects.select_editoption(value)
                EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                EditLogicalInterconnects.input_share_values(logicalinterconnects.share)
                EditLogicalInterconnects.input_maxshare_value(logicalinterconnects.maxshare)
                EditLogicalInterconnects.tick_dot1p_values(logicalinterconnects.dot1p1)
                EditLogicalInterconnects.tick_dscp_values(logicalinterconnects.dscp1)
                EditLogicalInterconnects.click_class_ok_button()
            EditLogicalInterconnects.click_reset_button()
            for value in class_list:
                val = EditLogicalInterconnects.get_class_enabled(value)
                values_list1.append(val)
                logger.info("successfully got text for enabled %s" % values_list1)
                val = EditLogicalInterconnects.get_share_value(value, logicalinterconnects.sharetext)
                values_list2.append(val)
                logger.info("successfully got text for share %s" % values_list2)
                val = EditLogicalInterconnects.get_maxsharevalue(value)
                values_list3.append(val)
                logger.info("successfully got text for maxshare %s" % values_list3)
                EditLogicalInterconnects.select_classname(value)
                logger.info("got the values %s" % value_list)
                val = EditLogicalInterconnects.get_dot1p_dscp_mapping_values(value_list[i])
                logger.info("Retrieved value is %s" % val)
                values_list4.append(val)
                logger.info("successfully got text for DSCP DOt1p mappings %s" % values_list4)
                i += 1
            EditLogicalInterconnects.click_cancel_button()
            return values_list1, values_list2, values_list3, values_list4
        if hasattr(logicalinterconnects, 'verifypriorities'):
            dot1p_priority = [item.strip() for item in logicalinterconnects.priority1.split(',')]
            EditLogicalInterconnects.select_qos_configuration_type(logicalinterconnects.qos_type)
            EditLogicalInterconnects.select_editoption(logicalinterconnects.besteffort)
            value = EditLogicalInterconnects.select_egress_fields()
            EditLogicalInterconnects.click_class_ok_button()
            if not value:
                ui_lib.fail_test("egress priority values is editable for Best Effort  %s " % value)
            logger.info("egress priority values is  not  editable for Best Effort ")
            priority_list = [item.strip() for item in logicalinterconnects.priority.split(',')]
            class_list = [item.strip() for item in logicalinterconnects.classname.split(',')]
            i = 0
            for class1 in class_list:
                EditLogicalInterconnects.select_editoption(class1)
                EditLogicalInterconnects.click_qos_class(fail_if_false=False)
                EditLogicalInterconnects.input_share_values(logicalinterconnects.share)
                if not EditLogicalInterconnects.select_egress_priority(priority_list[i]):
                    ui_lib.fail_test("failed to select egrees value from dropdown")
                i += 1
                EditLogicalInterconnects.click_class_ok_button()
            dot1p = []
            validate1 = EditLogicalInterconnects.get_egress_priority_values()
            dot1p.append(validate1)
            logger.info("egress priority %s" % dot1p)
            logger.info("egress &&&& %s" % validate1)
            dot1p.append(dot1p_priority)
            EditLogicalInterconnects.click_cancel_button()
            return dot1p
        EditLogicalInterconnects.click_cancel_button()
        return True


def get_uplinkSet_data(liname):
    """
    Function to get Uplink Set data
    """
    navigate()
    data = []
    if not select_logical_interconnect(liname):
        logger.warn("%s name is not present" % liname)
    CommonOperationLogicalInterconnect.click_logical_uplink()
    uls = CommonOperationLogicalInterconnect.get_uplinkset_data()
    if uls:
        data = uls.split("\n")
    return data


def get_alert_message_li(liname):
    """
    Function to get alert message in LI
    """
    navigate()
    if not select_logical_interconnect(liname):
        logger.warn("%s name is not present" % liname)
    if not CommonOperationLogicalInterconnect.verify_alert_msg_exist():
        logger.info("Alert message is not visible. Hence failing the test case")
        FusionUIBase.fail_test_or_return_false("Alert message is not visible. Hence failing the test case")
    return CommonOperationLogicalInterconnect.get_alert_msg()


def get_active_message_list_li(liname):
    '''
    funtion returns the list of Active Messages
    Example:
       get_active_message_list_li    li_name
    '''
    navigate()
    if not select_logical_interconnect(liname):
        logger.warn("%s name is not present" % liname)
    FusionUIBase.select_view_by_name("Activity")
    msg_list, state_list = CommonOperationLogicalInterconnect.get_li_active_message_list()
    active_list = []
    actindex = [mesg for mesg, state in enumerate(state_list) if state == "Active"]
    for msgstate in actindex:
        active_list.append(msg_list[msgstate])

    return active_list


def get_li_uplinkset_data(liname, uplink):
    '''
    function returns Uplinkset data of LI page
    example: get_li_uplinkset_data  li_name  uplink_name
    '''
    navigate()
    if not select_logical_interconnect(liname):
        logger.warn("%s name is not present" % liname)
    FusionUIBase.select_view_by_name("Uplink Sets")
    CommonOperationLogicalInterconnect.click_li_uplink_set(uplink)
    return CommonOperationLogicalInterconnect.get_uplink_set_data(uplink)


def get_li_uplinkset_port_data(li_obj):
    '''
    Return uplink set port data of li page for data validations
    example:
        get_li_uplinkset_port_data    {li_obj}
        <li_obj>
    <uplinks  liname= "SGH439WJKT-LIG_UI_f1682" uplinkname="Uplink1" port="Q1.1"  />
    <uplinks  liname= "SGH439WJKT-LIG_UI_f1682" uplinkname="Uplink1" port="Q2.1"  />
    </li_obj>

    '''

    navigate()

    port_data_list = []
    for uls in list(li_obj[0]):
        select_logical_interconnect(uls.liname)
        FusionUIBase.select_view_by_name("Uplink Sets")
        CommonOperationLogicalInterconnect.click_li_uplink_set(uls.uplinkname)
        uplinkdata = CommonOperationLogicalInterconnect.get_uplink_set_port_data(uls.uplinkname, uls.port)
        port_data_list.append(uplinkdata)
        # collapse the uplinksection after the data validation is done
        CommonOperationLogicalInterconnect.click_li_uplink_set(uls.uplinkname)
    return port_data_list


def edit_scope_for_logical_interconnect(li_list):
    """ edit scope for logical interconnect
        This function is to edit scope for logical interconnect
        Example:
            Edit_Scope_for_logical_interconnect(LI_list)
    """
    logger.info("Function call to edit scope for logical interconnect ")
    navigate()
    for li in li_list:
        if not select_logical_interconnect(li.name):
            FusionUIBase.fail_test_or_return_false("Failed to find the target logical interconnect")
        FusionUIBase.select_view_by_name("Scopes")
        EditScopeForLogicalInterconnect.click_edit_scope_button()
        EditScopeForLogicalInterconnect.wait_edit_scope_dialog_open()
        if li.has_property("scopes"):
            scope_list = li.scopes.split(',')
            for scope in scope_list:
                if not VerifyLogicalInterconnects.verify_scope_should_exist_in_edit_page(scope, 2, fail_if_false=False):
                    EditScopeForLogicalInterconnect.click_assign_button()
                    EditScopeForLogicalInterconnect.wait_assign_scope_dialog_open()
                    EditScopeForLogicalInterconnect.input_scope_name(scope)
                    EditScopeForLogicalInterconnect.click_scope_name(scope)
                    EditScopeForLogicalInterconnect.click_add_button()
                    EditScopeForLogicalInterconnect.wait_assign_scope_dialog_close()
        if li.has_property("remove_scopes"):
            remove_scope_list = li.remove_scopes.split(',')
            for scope in remove_scope_list:
                if VerifyLogicalInterconnects.verify_scope_should_exist_in_edit_page(scope, timeout=5):
                    EditScopeForLogicalInterconnect.click_remove_scope_icon(scope)
        EditScopeForLogicalInterconnect.click_ok_button()
        EditScopeForLogicalInterconnect.wait_edit_scope_dialog_close()
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(li.name, 'Update', timeout=60, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()
    return True


def validate_user_privileges(*editlis_obj):
    """ validate_user_privileges

        Example:
        | `validate_user_privileges     |
    Arguments:
      <li>
          name*                     --  Name of logical interconnect group as a string.
          qos_configuration_type*   --  Possible value: Passthrough/Custom (with FCoE lossless)|Custom (without FCoE lossless)
    * Required Arguments

    Example:
        data/ligs -> @{TestData.ligs}
        <li>
            <li  name="Enc-78-LIG1"
                 qos_configuration_type = "Custom (with FCoE lossless)"
            </li>
        </li>

    """

    navigate()
    if isinstance(editlis_obj, test_data.DataObj):
        editlis_obj = [editlis_obj]
    elif isinstance(editlis_obj, tuple):
        editlis_obj = list(editlis_obj[0])

    total = len(editlis_obj)
    not_exists = 0
    verified_pass = 0

    for logicalinterconnects in editlis_obj:
        navigate()
        editliname = logicalinterconnects.name
        if not VerifyLogicalInterconnects.verify_logical_interconnect_exist(editliname, timeout=5, fail_if_false=False):
            ui_lib.fail_test("Exiting Edit LI Function, Not selected LI %s" % editliname)
        logger.info("Seclected the LI succesfully")
        if not EditLogicalInterconnects.click_actions_menu():
            ui_lib.fail_test("failed to verify visibility under actions menu")
    return True


def _edit_li_create_uplink_set(uplink_set, add_plus=False):
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType
    logger.info("Function to call to edit uplink set %s" % uplink_set_name)

    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    if uplink_set_type == "Ethernet":
        __edit_li_add_ethernet_uplink_set(uplink_set)
    elif uplink_set_type == "Tunnel":
        __edit_li_add_tunnel_uplink_set(uplink_set)
    elif uplink_set_type == "Untagged":
        __edit_li_add_untagged_uplink_set(uplink_set)
    elif uplink_set_type == "Fibre Channel":
        __edit_li_add_fc_uplink_set(uplink_set)
    else:
        ui_lib.fail_test("Not support changing uplink set type '%s'" % uplink_set_type)

    # TODO: simple verify selected networks & uplink ports

    # hit add button
    if add_plus is False:  # add
        EditLogicalInterconnects.click_create_uplink_set_add()
        logger.info("create button clicked")
        EditLogicalInterconnects.wait_confirmation_dialog_appear()
        EditLogicalInterconnects.check_correct_confirmation_ask_for(uplink_set.confirmation)
        EditLogicalInterconnects.tick_confirmation_checkbox()
        EditLogicalInterconnects.click_perform_action_button()
        if not EditLogicalInterconnects.wait_create_uplink_set_dialog_disappear():
            msg = EditLogicalInterconnects.get_uplinkset_error_message()
            EditLogicalInterconnects.click_create_uplinkset_cancel_button()
            EditLogicalInterconnects.wait_create_uplink_set_dialog_disappear(15, False)
            ui_lib.fail_test(msg)

    else:  # add plus
        EditLogicalInterconnects.click_create_uplink_set_add_plus()
        EditLogicalInterconnects.wait_confirmation_dialog_appear()
        EditLogicalInterconnects.check_correct_confirmation_ask_for(uplink_set.confirmation)
        EditLogicalInterconnects.tick_confirmation_checkbox()
        EditLogicalInterconnects.click_perform_action_button()


def __edit_li_add_ethernet_uplink_set(uplink_set):
    __edit_li_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __edit_li_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network_list = [item.strip() for item in uplink_set.networks.split(',')]
    if network_list:
        EditLogicalInterconnects.click_create_uplink_set_add_networks()
        EditLogicalInterconnects.wait_create_uplink_set_add_networks_to_dialog_shown()
        for i, network_name in enumerate(network_list):
            EditLogicalInterconnects.input_create_uplink_set_add_networks_to_search_network(network_name)
            EditLogicalInterconnects.wait_create_uplink_set_add_networks_to_table_row_shown(network_name)
            if i == len(network_list) - 1:
                EditLogicalInterconnects.click_create_uplink_set_add_networks_to_add()
            else:
                EditLogicalInterconnects.click_create_uplink_set_add_networks_to_add_plus()
        EditLogicalInterconnects.wait_create_uplink_set_add_networks_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - choose native network
    native_network = getattr(uplink_set, "native", "")
    if native_network != "":
        EditLogicalInterconnects.tick_create_uplink_set_native_network(native_network)

    # verify if present in table list
    for network in network_list:
        EditLogicalInterconnects.wait_create_uplink_set_network_table_row_shown(network)

    # - ports
    __edit_li_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __edit_li_open_dialog_and_set_uplink_set_name_and_type(uplink_set):
    uplink_set_name = uplink_set.name
    uplink_set_type = uplink_set.networkType
    if EditLogicalInterconnects.verify_add_uplink_set_dialog_shown(fail_if_false=False) is False:
        # sometimes user might be adding Uplink Set using Create+ button therefore the dialog won't be closed
        # when the next item adding action is calling this function, so add this verify to avoid the unnecessary click/wait
        EditLogicalInterconnects.click_add_uplink_set()
        EditLogicalInterconnects.wait_create_uplink_set_dialog_shown()
    EditLogicalInterconnects.input_create_uplink_set_name(uplink_set_name)
    EditLogicalInterconnects.select_create_uplink_set_type(uplink_set_type)


def __edit_li_set_connection_mode_and_lacp(uplink_set):
    # choose connection mode, LACP timer for ethernet, tunnel, untagged
    # - connection mode
    connection_mode = uplink_set.connectionMode.lower()
    if connection_mode == "auto":
        logger.info("entered")
        logger.info(uplink_set.lacptimer)
        uplink_set_lacp_timer = uplink_set.lacptimer
        EditLogicalInterconnects.tick_create_uplink_set_connection_mode_automatic()
        if uplink_set_lacp_timer != "":
            EditLogicalInterconnects.select_create_uplink_set_lacp_timer(uplink_set_lacp_timer)
    elif connection_mode == "failover":
        EditLogicalInterconnects.tick_create_uplink_set_connection_mode_failover()
    else:
        ui_lib.fail_test(
            "Unexpected ethernet connection mode '%s' of uplink set '%s'" % (connection_mode, uplink_set.name))


def __edit_li_add_tunnel_uplink_set(uplink_set):
    __edit_li_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __edit_li_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        EditLogicalInterconnects.select_create_uplink_set_tunnel_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __edit_li_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __edit_li_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(';')]
    logger.info(port_list)
    if port_list:
        EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports()
        EditLogicalInterconnects.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            portattr = port_tag.split(':')
            # This is added to handle autonegotiation, as a new speed attribute is introduced
            #  ensure for Synergy the value will be like bay:Q1:Auto or bay:Q1:1
            #  ensure for C7000 the value will be like bay:Q1.1:Auto or bay:Q1.1
            if len(portattr) > 2:
                bay_no = portattr[0]
                if (portattr[2] != "Auto" and portattr[2] != "40 Gb/s"):
                    port_name = portattr[1] + ':' + portattr[2]
                else:
                    port_name = portattr[1]
                    port_speed = portattr[2]
            else:
                bay_no = portattr[0]
                port_name = portattr[1]

            EditLogicalInterconnects.input_create_uplink_set_add_uplink_ports_to_search_port(port_name, timeout=10)

            EditLogicalInterconnects.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name, timeout=10)
            EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name, timeout=10)

            if i == len(port_list) - 1:
                EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports_to_add()
                EditLogicalInterconnects.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear(15)
            else:
                EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports_to_add_plus()

    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        portattr = port_tag.split(':')
        if len(portattr) > 2:
            bay_no = portattr[0]
            if (portattr[2] != "Auto" and portattr[2] != "40 Gb/s"):
                port_name = portattr[1] + ':' + portattr[2]
                EditLogicalInterconnects.wait_create_uplink_set_port_table_row_shown(bay_no, port_name)

            else:
                port_name = portattr[1]
                port_speed = portattr[2]
                EditLogicalInterconnects.wait_create_uplink_set_port_table_row_shown(bay_no, port_name, 10)
                EditLogicalInterconnects.select_create_uplink_set_ethernet_port_speed(port_name, port_speed, 10, False)

        else:
            bay_no, port_name = port_tag.split(':')
            EditLogicalInterconnects.wait_create_uplink_set_port_table_row_shown(bay_no, port_name, 10, False)


def __edit_li_add_untagged_uplink_set(uplink_set):
    __edit_li_open_dialog_and_set_uplink_set_name_and_type(uplink_set)
    __edit_li_set_connection_mode_and_lacp(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        EditLogicalInterconnects.select_create_uplink_set_untagged_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")

    # - ports
    __edit_li_add_uplink_set_ethernet_tunnel_or_untagged_network(uplink_set)


def __edit_li_add_fc_uplink_set(uplink_set):
    __edit_li_open_dialog_and_set_uplink_set_name_and_type(uplink_set)

    # - networks
    network = uplink_set.networks
    if network != "":
        EditLogicalInterconnects.select_create_uplink_set_fc_network(network)
    else:
        ui_lib.fail_test("no [ networks ] attribute specified in data file when create uplink set > add networks")
    # - ports
    port = uplink_set.ports
    interconnect = uplink_set.interconnect
    # -- interconnect
    if interconnect == "":
        ui_lib.fail_test("no [ interconnect ] attribute specified in data file when create uplink set > add networks")
    if port == "":
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add networks")

    __edit_li_add_uplink_set_fc_network(uplink_set)
    # -- port & port speed
    port_list = [item.strip() for item in port.split(',')]
    for port_and_speed in port_list:
        bay_no, port_name, port_speed = port_and_speed.split(':')
        bay_no = bay_no.replace('bay', '')
        EditLogicalInterconnects.select_create_uplink_set_fc_port_speed(bay_no, port_name, port_speed)


def __edit_li_add_uplink_set_fc_network(uplink_set):
    port_list = [item.strip() for item in uplink_set.ports.split(',')]
    if port_list:
        EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports()
        EditLogicalInterconnects.wait_create_uplink_set_add_uplink_ports_to_dialog_shown()
        for i, port_tag in enumerate(port_list):
            bay_no, port_name, port_speed = port_tag.split(':')
            bay_no = bay_no.lower().replace('bay', '')
            EditLogicalInterconnects.input_create_uplink_set_add_uplink_ports_to_search_port(port_name)
            EditLogicalInterconnects.wait_create_uplink_set_add_uplink_ports_to_table_row_shown(bay_no, port_name)
            EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports_to_table_row(bay_no, port_name)
            if i == len(port_list) - 1:
                EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports_to_add()
            else:
                EditLogicalInterconnects.click_create_uplink_set_add_uplink_ports_to_add_plus()
        EditLogicalInterconnects.wait_create_uplink_set_add_uplink_ports_to_dialog_disappear()
    else:
        ui_lib.fail_test("no [ ports ] attribute specified in data file when create uplink set > add uplink ports")

    # verify if present in table list
    for i, port_tag in enumerate(port_list):
        bay_no, port_name, port_speed = port_tag.split(':')
        bay_no = bay_no.lower().replace('bay', '')
        C7000CreateLogicalInterconnectGroups.wait_create_uplink_set_port_table_row_shown(bay_no, port_name)


def _validation_of_update_firmware(firmwareBasename):
    # Check error messages,progress bar and warning messages appears on logical interconnect firmware update page '''
    error_string = ''
    error_status = ''
    fw_flag = True
    logger.info("Checking For errors - After clicking on OK Button of Firmware update in LI page")
    if not C7000LogicalInterconnectsUpdateFirmware.wait_for_update_firmware_notvisible(5, False):
        error_status = C7000LogicalInterconnectsUpdateFirmware.wait_for_error_visible_on_li_form(5, False)

        if error_status:
            logger.debug("Error Summary - {}".format(C7000LogicalInterconnectsUpdateFirmware.get_message_summary_on_li_form(5, False)))
            fw_flag = False
            logger.debug("Error Details - {}".format(C7000LogicalInterconnectsUpdateFirmware.get_message_details_on_li_form(5, False)))
            error_string += (C7000LogicalInterconnectsUpdateFirmware.get_message_summary_on_li_form(5, False)) + "." + (C7000LogicalInterconnectsUpdateFirmware.get_message_details_on_li_form(5, False)) + "\t"
            C7000LogicalInterconnectsUpdateFirmware.click_cancel_button()
            return fw_flag
    else:
        logger.info("No errors Seen on li update Firmware  page")
    # ''' # Check the Progress of Firmware upgrade on li page  '''
    if (C7000LogicalInterconnectsUpdateFirmware.wait_for_progressbar_on_updatefirmware()):
        logger.info("checking whether firmware is updated Successfully or updated with warnings")
    # Added the code for measure progress of firmware update for already staged firmware
        timeout = 0
        start_active = datetime.now()
        while timeout < FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
            if VerifyLogicalInterconnects.verify_update_firmware_progressbar_is_visible(fail_if_false=False):
                progress_message = TBirdLogicalInterconnectsUpdateFirmware.get_update_firmware_progressbar_state_message(fail_if_false=False)
                logger.info("Upgrade still in progress State : %s in li Page" % progress_message)
                logger.info("Upgrade still in progress in li and waited for %s " % timeout)
            if C7000LogicalInterconnectsUpdateFirmware.wait_for_update_firmware_success(timeout=5, fail_if_false=False):
                logger.info("Firmware update Completed on li page.\n")
                fw_flag = True
                break

            elif C7000LogicalInterconnectsUpdateFirmware.wait_for_update_firmware_warning(timeout=5, fail_if_false=False):
                logger.info("Firmware update Completed but with warning on li page")
                fw_flag = False
                break

            elif C7000LogicalInterconnectsUpdateFirmware.wait_for_update_firmware_error(timeout=5, fail_if_false=False):
                logger.debug("Error during Firmware update on LI page")
                fw_flag = False
                break

            timeout = (datetime.now() - start_active).seconds
        if timeout > FusionLogicalInterconnectsPage.FW_UPDATE_TIME:
            logger.info("Either FW Upgrade of LI %s  has not completed , even after waiting for %s  minutes!!" % firmwareBasename, timeout)
            fw_flag = False
            error_string += "Either FW Upgrade of LI %s  has not completed or FW Upgrade Complete Alert is not seen , even after waiting for %s  minutes!!\t" % (firmwareBasename, timeout)
        # if add form is still seen click cancel
        if C7000LogicalInterconnectsUpdateFirmware.check_activation_dialog(5, False):
            logger.info("Activation firmware appeared")
            C7000LogicalInterconnectsUpdateFirmware.click_cancel_button()
    else:
        logger.debug("progress bar not appeared after clicking OK button for activate staged firmwareFW update page")
        if C7000LogicalInterconnectsUpdateFirmware.check_activation_dialog(5, False):
            logger.info("Activation firmware appeared")
            C7000LogicalInterconnectsUpdateFirmware.click_cancel_button()
        fw_flag = False

    return fw_flag


def update_firmware_new(*firmwareBase_obj):
    '''
    This  Function will  update the firmware for the interconnects present in the li.

    DATAFILE EXAMPLE:
        <firmware1 name="SGH420HHYA-LIG_B1" updateaction="Update firmware (stage + activate)" updateFirmware="Service Pack for ProLiant, gen9snap6" ethernet_update="Parallel" fibre_channel_update="Parallel" force="No" fibre_delay="No" eth_delay="No" eth_delay_value="1" fibre_delay_value="1"/>


        attributes:
            name                 -  LI to Perform update on
            updateFirmware            -Firmware bundle to use for update
            updateaction        - stage or stage_activation or activation only
            ethernet_update                - parallel or serial or Odd/Even
            fibre_channel_update              - parallel or serial or Odd/Even
            force                - yes or no
            fibre_delay               -  yes or no
            eth_delay            -  yes or no
            eth_delay_value        - provide values from 1 to 5
            fibre_delay_value      - provide values from 1 to 5


    '''

    fw_flag = True
    if isinstance(firmwareBase_obj, test_data.DataObj):
        firmwareBase_obj = [firmwareBase_obj]
    elif isinstance(firmwareBase_obj, tuple):
        firmwareBase_obj = list(firmwareBase_obj[0])

    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)

    logger.info("Updating Li firmware ....")
    for firmwareBase in firmwareBase_obj:
        if not VerifyLogicalInterconnects.verify_logical_interconnect_exist(firmwareBase.name, 5, False):
            logger.info("Logical interconnect %s does not exist" % firmwareBase.name)
            fw_flag = False
            break
        else:
            CommonOperationLogicalInterconnect.click_logical_interconnect(firmwareBase.name, 5, False)
            # wait target logical interconnect get focus
            logger.info("Wait for logical interconnect %s to be selected." % firmwareBase.name)
            if not CommonOperationLogicalInterconnect.wait_logical_interconnect_selected(firmwareBase.name, 5, False):
                logger.info("Failed to select logical interconnect %s" % firmwareBase.name)
                fw_flag = False
                break

        firmware_baseline = C7000LogicalInterconnectsUpdateFirmware.get_firmware_baseline_on_li_form()
        TBirdLogicalInterconnectsUpdateFirmware.click_action_button(timeout=10)
        TBirdLogicalInterconnectsUpdateFirmware.click_action_update_firmware(10, False)
        TBirdLogicalInterconnectsUpdateFirmware.wait_and_select_update_action(firmwareBase.update_action, 5, False)
        logger.info("Clicked UPDATE_ACTION and it is visible")
        # Perform the activation  of already Staged firmware
        if getattr(firmwareBase, 'update_action', '') == 'Activate firmware':
            logger.info("Inside active FW update Block\n")
            C7000LogicalInterconnectsUpdateFirmware.click_select_update_action_on_li(firmwareBase.update_action, 5, False)
            firmware_baseline = C7000LogicalInterconnectsUpdateFirmware.get_firmware_baseline_on_li()
            logger.info("Firmware version from oneview : %s " % firmware_baseline)
            if firmware_baseline == firmwareBase.update_Firmware:
                if C7000LogicalInterconnectsUpdateFirmware.check_active_firmware_present_on_li():
                    logger.info("Firmware with baseline %s is already activated" % firmwareBase.update_Firmware)
                    fw_flag = False
                else:
                    logger.info(" Selecting firmware for : %s  " % firmwareBase.update_action)
                    if (getattr(firmwareBase, 'ethernet_update', '') == "Parallel") or (getattr(firmwareBase, 'ethernet_update', '') == "Serial") or (getattr(firmwareBase, 'ethernet_update', '') == "Odd/even"):
                        logger.info(" Inside a Ethernet update selection ")
                        C7000LogicalInterconnectsUpdateFirmware.select_update_action(firmwareBase.ethernet_update)
                    if (getattr(firmwareBase, 'eth_delay', '') == "Yes") or (getattr(firmwareBase, 'neg_delay', '') == "Yes"):
                        C7000LogicalInterconnectsUpdateFirmware.input_ethernet_delay(firmwareBase.eth_delay_value, 5, False)
                    if getattr(firmwareBase, 'neg_delay', '') == "Yes":
                        C7000LogicalInterconnectsUpdateFirmware.input_ethernet_delay(firmwareBase.neg_eth_delay_value, 5, False)

                    # Check the error message on  ethernet section
                    if getattr(firmwareBase, 'select_neg', '') == "Yes":
                        eth_unselect_error_msg = ''
                        eth_select_list = firmwareBase.neg_select_eth.split(',')
                        for ebay in eth_select_list:
                            enclosure_name = firmwareBase.enc_name
                            if not C7000LogicalInterconnectsUpdateFirmware.untick_activation_ethernet_icm(ebay, enclosure_name, 5, False):
                                logger.info("Ethernet interconnects not available ")
                                fw_flag = False

                        eth_unselect_error_msg = C7000LogicalInterconnectsUpdateFirmware.get_error_message_from_li_ethernet_icms()
                        import re
                        pattern_match = re.search('Select at least one interconnect for activation', eth_unselect_error_msg)
                        if pattern_match:
                            logger.info("Found the Error message on ethernet elective section- {}".format(pattern_match.group()))
                        else:
                            logger.info("not Found the Error message")
                            fw_flag = False
                    if getattr(firmwareBase, 'eth_select', '') == "Yes":
                        eth_list = firmwareBase.eth_select_bay.split(',')
                        for ebay in eth_list:
                            enclosure_name = firmwareBase.enc_name
                            if not C7000LogicalInterconnectsUpdateFirmware.untick_activation_ethernet_icm(ebay, enclosure_name, 5, False):
                                logger.info("Ethernet interconnects not available ")
                                fw_flag = False
                    if (getattr(firmwareBase, 'fibre_channel_update', '') == "Parallel") or (getattr(firmwareBase, 'fibre_channel_update', '') == "Serial") or (getattr(firmwareBase, 'fibre_channel_update', '') == "Odd/even"):
                        logger.info(" Inside a Fiber channel update selection ")
                        C7000LogicalInterconnectsUpdateFirmware.select_fibre_channel_activation(firmwareBase.fibre_channel_update, 5, False)

                    # check error msg on activate page
                        if getattr(firmwareBase, 'select_neg', '') == "Yes":
                            fc_unselect_error_msg = ''
                            fc_select_list = firmwareBase.neg_select_fc.split(',')
                            for ebay in fc_select_list:
                                enclosure_name = firmwareBase.enc_name
                                if not C7000LogicalInterconnectsUpdateFirmware.untick_activation_fc_icm(ebay, enclosure_name, 5, False):
                                    logger.info("FC interconnects not available ")
                                    fw_flag = False
                            fc_unselect_error_msg = C7000LogicalInterconnectsUpdateFirmware.get_error_message_from_li_fibre_icms()

                            pattern_match = re.search('Select at least one interconnect for activation', fc_unselect_error_msg)
                            if pattern_match:
                                logger.info("Found the Error message on fc selective section - {}".format(pattern_match.group()))
                            else:
                                logger.info("not Found the Error message on fc section")
                                fw_flag = False

                        if getattr(firmwareBase, 'fibre_delay', '') == "Yes":
                            C7000LogicalInterconnectsUpdateFirmware.input_fibre_delay(firmwareBase.fibre_delay_value, 5, False)

                        if getattr(firmwareBase, 'neg_delay', '') == "Yes":
                            C7000LogicalInterconnectsUpdateFirmware.input_ethernet_delay(firmwareBase.neg_eth_delay_value, 5, False)
                            C7000LogicalInterconnectsUpdateFirmware.input_fibre_delay(firmwareBase.neg_delayfc_value, 5, False)
                            C7000LogicalInterconnectsUpdateFirmware.scroll_firmware_ok_button_into_view()
                            C7000LogicalInterconnectsUpdateFirmware.click_ok_button()
                            result = C7000LogicalInterconnectsUpdateFirmware.get_error_message_from_activation()
                            error_eth = re.search('This field is required', str(result['delay_eth_error_msg']))
                            error_fc = re.search('This field is required', str(result['delay_fc_error_msg']))
                            if error_eth:
                                logger.info("Found the Error message on FCdelay section - {}".format(error_eth.group()))
                            else:
                                logger.info("not Found the Error message on fc section")
                                fw_flag = False
                            if error_fc:
                                logger.info("Found the Error message on on fcdelay section - {}".format(error_fc.group()))
                            else:

                                logger.info("not Found the Error message on  fc section")
                                fw_flag = False
                            # if form is still seen click cancel
                            C7000LogicalInterconnectsUpdateFirmware.click_cancel_button(10)

                        if getattr(firmwareBase, 'fc_select', '') == "Yes":
                            fc_list = firmwareBase.fc_select_bay.split(',')
                            for fbay in fc_list:
                                enclosure_name = firmwareBase.enc_name
                                if not C7000LogicalInterconnectsUpdateFirmware.untick_activation_fc_icm(fbay, enclosure_name, 5, False):

                                    logger.info("FC interconnects not available ")
                        if getattr(firmwareBase, 'neg_test_trigger', '') == 'Yes':
                            fw_flag = C7000LogicalInterconnectsUpdateFirmware.click_ok_button()

                        else:
                            C7000LogicalInterconnectsUpdateFirmware.scroll_firmware_ok_button_into_view()
                            fw_ok_flag = C7000LogicalInterconnectsUpdateFirmware.click_ok_button()
                            if not fw_ok_flag:
                                if TBirdLogicalInterconnectsUpdateFirmware.click_update_firmware_cancel_button():
                                    return False
                            ''' Check error messages appears on LI FW update page '''
                            logger.info("Checking For Errors - After clicking on OK Button of Firmware update in LI page")

                            fw_flag = _validation_of_update_firmware(firmwareBase.name)
            else:
                raise ValueError("The given firmware baseline is invalid")
                fw_flag = False

        elif getattr(firmwareBase, 'update_action', '') == "Stage firmware for later activation":
            logger.info("In Stage firmware for later activation FW upgrade")
            logger.info("Selecting firmware for : %s " % firmwareBase.update_action)
            C7000LogicalInterconnectsUpdateFirmware.click_update_firmware_on_li(firmwareBase.update_action)
            C7000LogicalInterconnectsUpdateFirmware.select_firmware_level_from_drowpdown(firmwareBase.update_Firmware, 5, False)
            if getattr(firmwareBase, 'force', '') == "Yes":
                C7000LogicalInterconnectsUpdateFirmware.click_force_installation_checkbox()
            C7000LogicalInterconnectsUpdateFirmware.scroll_firmware_ok_button_into_view()
            logger.info("***success on scrolling Ok Button")
            ''' # Click OK to begin firmware update  '''
            if getattr(firmwareBase, 'neg_test_trigger', '') == 'Yes':
                fw_flag = C7000LogicalInterconnectsUpdateFirmware.click_ok_button()
            else:
                C7000LogicalInterconnectsUpdateFirmware.click_ok_button()
                C7000LogicalInterconnectsUpdateFirmware.wait_activity_updatefirmware_visible_on_li()
                ''' Check error messages appears on LI FW update page '''
                logger.info("Checking For errors - After clicking on OK Button of Firmware update in LI page")
                fw_flag = _validation_of_update_firmware(firmwareBase.name)
        elif getattr(firmwareBase, 'update_action', '') == "Update firmware (stage + activate)":
            logger.info(" Inside a Stage + Activate FW update ")
            logger.info("Selecting firmware for : %s " % firmwareBase.update_action)
            C7000LogicalInterconnectsUpdateFirmware.click_update_firmware_on_li(firmwareBase.update_action)
            C7000LogicalInterconnectsUpdateFirmware.select_firmware_level_from_drowpdown(firmwareBase.update_Firmware, 5, False)
            if getattr(firmwareBase, 'force', '') == "Yes":
                C7000LogicalInterconnectsUpdateFirmware.click_force_installation_checkbox()
            if (getattr(firmwareBase, 'ethernet_update', '') == "Parallel") or (getattr(firmwareBase, 'ethernet_update', '') == "Serial") or (getattr(firmwareBase, 'ethernet_update', '') == "Odd/even"):
                C7000LogicalInterconnectsUpdateFirmware.select_update_action(firmwareBase.ethernet_update)
            # Change  default  delay of ethernet channel
            if getattr(firmwareBase, 'eth_delay', '') == "Yes":
                C7000LogicalInterconnectsUpdateFirmware.input_ethernet_delay(firmwareBase.eth_delay_value, 5, False)
            if (getattr(firmwareBase, 'fibre_channel_update', '') == "Parallel") or (getattr(firmwareBase, 'fibre_channel_update', '') == "Serial") or (getattr(firmwareBase, 'fibre_channel_update', '') == "Odd/even"):

                C7000LogicalInterconnectsUpdateFirmware.select_fibre_channel_activation(firmwareBase.fibre_channel_update, 5, False)
            # Change   default delay of fiber  channel
            if getattr(firmwareBase, 'fibre_delay', '') == "Yes":
                C7000LogicalInterconnectsUpdateFirmware.input_fibre_delay(firmwareBase.fibre_delay_value, 5, False)
            C7000LogicalInterconnectsUpdateFirmware.scroll_firmware_ok_button_into_view()
            if C7000LogicalInterconnectsUpdateFirmware.click_ok_button():
                # ''' Check error messages appears on LI FW update page '''
                logger.info(" Checking For errors - After clicking on OK Button of Firmware update in LI page")
                fw_flag = _validation_of_update_firmware(firmwareBase.name)
        else:
            C7000LogicalInterconnectsUpdateFirmware.click_cancel_button()
            ui_lib.fail_test(" The given firmware baseline is invalid")
    return fw_flag


def get_logical_interconnect_uplinkset_ports_info(logicalinterconnects):
    """ This function returns the uplink port speed and fc port login
        Example:
        <logicalinterconnect>
            <li name = "LE-Group_1 logical interconnect group" uplink_name = "US_FA2" port = "Q2:2" port_speed = "yes" port_login = "yes"/>
            <li name = "LE-Group_1 logical interconnect group" uplink_name = "US_FA2" port = "Q2:3" port_speed = "yes" port_login = "yes"/>
        </logicalinterconnect>
    """

    navigate()
    output = []
    if not select_logical_interconnect(logicalinterconnects.name):
        ui_lib.fail_test("failed to select the logical interconnect %s" % logicalinterconnects.name)
    else:
        FusionUIBase.select_view_by_name(view_name="Uplink Sets", timeout=5, fail_if_false=False)
        CommonOperationLogicalInterconnect.expand_uplinkset_name(logicalinterconnects.uplink_name)

    if logicalinterconnects.port_speed.lower() == 'yes':
        logger.info("Fetching uplink port speed")
        portspeed = CommonOperationLogicalInterconnect.get_uplink_portspeed(logicalinterconnects.uplink_name, logicalinterconnects.port)
        output.append(portspeed)

    if logicalinterconnects.port_login.lower() == 'yes':
        logger.info("Fetching Login count")
        fc_port_login_count = CommonOperationLogicalInterconnect.get_fc_port_login(logicalinterconnects.uplink_name, logicalinterconnects.port)
        output.append(fc_port_login_count)
    return output


def verify_mac_table_exist(logicalinterconnects):
    """ This function verify whether the MAC table exist or not

        Arguments:
        name*             --  Name of LI as a string.

        * Required Arguments

        Example:
        data/editlogicalinterconnect -> @{TestData.editlogicalinterconnect}
        <editlogicalinterconnect>
            <logicalinterconnect name="AR56-EN11-Group_1 logical interconnect group">
            </logicalinterconnect>
        </editlogicalinterconnect>
    """
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)
    if not select_logical_interconnect(logicalinterconnects.name):
        ui_lib.fail_test("Existing Edit LI Function, Not selected LI %s" % name)
    if VerifyLogicalInterconnects.verify_mac_download_table_in_action_menu():
        logger.info("MAC Address Table verified in Action menu")
    if EditLogicalInterconnects.click_logical_mac_address():
        VerifyLogicalInterconnects.verify_mac_download_table_in_mac_address_view()
        logger.info("MAC Address Table verified Under Mac Address Field in LI page")
        return True


def verify_functions_of_mac_table(lis_obj):
    """ This function verify the functions of mac table dropdown boxes

        Example:
        | `Verify Functions Of Mac Table Dropdown Boxes`      |     |

        Example:
        data/editlogicalinterconnect -> @{TestData.editlogicalinterconnect}
        <editlogicalinterconnect>
        <logicalinterconnect name="AR56-EN11-Group_1 logical interconnect group">
            <li all="All" get_mac_table_entries="115" mac_table_key="Interconnect/Interface/Address/Type/Network/External VLAN/Internal VLAN" mac_table_values="AR56-EN11, interconnect 1/LAG 26/50:65:F3:5E:15:0D/Learned/enet4/115/3" verify_interconnect="AR56-EN11, interconnect 1" verify_network="enet4" verify_interconnect_network="" verify_external_vlan_id="101" interconnect="AR56-EN11, interconnect 1" interface="LAG 27" address="FE:07:59:D0:00:23" network="enet1" external_vlan="115" internal_vlan="9" />
            <li interconnect="All" verify_tunnel_untagged="Tunnel" interface="LAG 27" address="FE:07:59:D0:00:23" network="enet2" external_vlan="Tunnel" internal_vlan="9" />
            <li interconnect="All" verify_tunnel_untagged="Untagged" interface="LAG 27" address="FE:07:59:D0:00:23" network="enet3" external_vlan="Untagged" internal_vlan="9"/>
        </logicalinterconnect>
    </editlogicalinterconnect>
    """
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)

    if isinstance(lis_obj, test_data.DataObj):
        lis_obj = [lis_obj]

    mac_data_index = 0
    for logicalinterconnects in lis_obj:
        if not select_logical_interconnect(logicalinterconnects.name):
            ui_lib.fail_test("Existing Edit LI Function, Not selected LI %s" % logicalinterconnects.name)
        EditLogicalInterconnects.click_logical_mac_address()
        for _, logicalinterconnects in enumerate(logicalinterconnects.li):

            if logicalinterconnects.has_property("get_mac_table_entries"):
                mac_table_keys = logicalinterconnects.mac_table_key.split('/')
                mac_table_values = logicalinterconnects.mac_table_values.split('/')
                mac_table_value_length = len(mac_table_values)
                for key in mac_table_keys:
                    VerifyLogicalInterconnects.verify_mac_table_keys_visible(key)
                EditLogicalInterconnects.select_all_interconnect()
                EditLogicalInterconnects.input_and_select_vlanid(logicalinterconnects.get_mac_table_entries)
                EditLogicalInterconnects.click_update()
                mac_data_index = mac_data_index + 2
                for i in range(mac_data_index, 3):
                    mac_table_data = EditLogicalInterconnects.get_mac_table_entries(i)
                    logger.info("Mac Table Enteries are %s" % mac_table_data)
                    for value in mac_table_values:
                        if value in mac_table_data:
                            logger.info("Verified Mac Table value is %s" % value)
                        else:
                            ui_lib.fail_test("Mac table doesn't contain valid enteries")
                    logger.info("Mac Table generated with valid values")

            if logicalinterconnects.has_property("all"):
                VerifyLogicalInterconnects.verify_interconnect_dropdown_default_value(logicalinterconnects.all)

            if logicalinterconnects.has_property("verify_interconnect"):
                EditLogicalInterconnects.select_specific_interconnect(logicalinterconnects.verify_interconnect)
                EditLogicalInterconnects.click_update()
                interconnects_list = EditLogicalInterconnects.get_interconnect_name_list(logicalinterconnects.verify_interconnect)
                logger.info("Interconnects in list are %s" % interconnects_list)
                _verify_interconnects(logicalinterconnects.verify_interconnect, interconnects_list)

            if logicalinterconnects.has_property("verify_interconnect_network"):
                EditLogicalInterconnects.select_specific_interconnect(logicalinterconnects.interconnect)
                EditLogicalInterconnects.input_and_select_network(logicalinterconnects.network)
                EditLogicalInterconnects.click_update()
                interconnects_name_list = EditLogicalInterconnects.get_interconnect_name_list(logicalinterconnects.interconnect)
                logger.info(interconnects_name_list)
                networks_list = EditLogicalInterconnects.get_network_name_list()
                del networks_list[0]  # To eliminate combo box value which is none
                logger.info("Networks in List are %s" % networks_list)
                _verify_networks(logicalinterconnects.network, networks_list)
                _verify_interconnects(logicalinterconnects.interconnect, interconnects_name_list)

            if logicalinterconnects.has_property("verify_network"):
                EditLogicalInterconnects.select_all_interconnect()
                EditLogicalInterconnects.input_and_select_network(logicalinterconnects.verify_network)
                EditLogicalInterconnects.click_update()
                networks_list = EditLogicalInterconnects.get_network_name_list()
                del networks_list[0]  # To eliminate combo box value which is none
                logger.info("Networks in List are %s" % networks_list)
                _verify_networks(logicalinterconnects.verify_network, networks_list)

            if logicalinterconnects.has_property("verify_external_vlan_id"):
                EditLogicalInterconnects.select_all_interconnect()
                EditLogicalInterconnects.input_and_select_vlanid(logicalinterconnects.external_vlan)
                EditLogicalInterconnects.click_update()
                vlan_list = EditLogicalInterconnects.get_vlan_id_list()
                del vlan_list[0]  # To eliminate combo box value which is none
                logger.info("Vlan in List are %s" % vlan_list)
                _verify_vlan(logicalinterconnects.external_vlan, vlan_list)

            if logicalinterconnects.has_property("verify_tunnel_untagged"):
                EditLogicalInterconnects.select_all_interconnect()
                EditLogicalInterconnects.input_and_select_network(logicalinterconnects.network)
                EditLogicalInterconnects.click_update()
                networks_list = EditLogicalInterconnects.get_network_name_list()
                del networks_list[0]  # To eliminate combo box value which is none
                logger.info("Networks in List are %s" % networks_list)
                _verify_networks(logicalinterconnects.network, networks_list)
                vlan_list = EditLogicalInterconnects.get_vlan_id_list()
                del vlan_list[0]  # To eliminate combo box value which is none
                logger.info("Vlan in List are %s" % vlan_list)
                _verify_vlan(logicalinterconnects.external_vlan, vlan_list)
        return True


def verify_mac_address_in_mac_table(lis_obj):
    """ This function verify the functions of mac table dropdown boxes for MAC Address search

        Example:
        | `Verify MAC Address Dropdown Boxes`      |     |

        Example data:
            {'bay': b'AR56-EN11, bay 9', 'mac_address': ['72:18:95:20:00:05'], 'name': b'AR56-EN11-Group_1 logical interconnect group', 'port': ['FlexibleLOM 1:1-c']}

        Arguments:
        name*             --  Name of LI.
        Mac Address*      --  Mac Address of the connections in server
        Port*             --  Port assigned for server
        bay*              --  Server bay number

        * Required Arguments

    """
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)

    editliname = lis_obj["name"]
    logger.info("Mac Address is %s" % lis_obj["mac_address"])
    mac_address_length = len(lis_obj["mac_address"])
    logger.info("Total number of Mac Address is %s" % mac_address_length)
    logger.info("Port name is %s" % lis_obj["port"])
    # lis_obj["bay"][-1] - say if bay is AR56-EN11, bay 1, only the bay number eg:1 alone needed to append to the interface
    # This way the interface formed in MAC Table eg: downlink 1-c
    bay = lis_obj["bay"][-1]
    logger.info("Bay Number is %s" % bay)
    if not select_logical_interconnect(editliname):
        ui_lib.fail_test("Existing Edit LI Function, Not selected LI %s" % editliname)
    EditLogicalInterconnects.click_logical_mac_address()
    for i in range(mac_address_length):
        EditLogicalInterconnects.input_mac_address(lis_obj["mac_address"][i])
        EditLogicalInterconnects.click_update()
        logger.info("Port is %s" % lis_obj["port"][i])
        port = (lis_obj["port"][i])
        # port[-1] - only the port variable say if port is 1:1-c, only the variable eg:c alone needed to append to the interface
        # This way the interface formed in MAC Table
        port = port[-1]
        logger.info("Port Number is %s" % port)
        interface = "downlink " + bay + "-" + port
        logger.info("Interface is %s" % interface)
        VerifyLogicalInterconnects.verify_mac_address_and_server_port(interface, lis_obj["mac_address"][i])
        logger.info("Mac Address of server profile verified successfully")

    return True


def verify_default_gateway_mac_address(lis_obj):
    """ This function verify the functions of mac table dropdown boxes for Gateway MAC Address search

        Example:
        | `Verify Default Gateway Mac Address`      |     |

        Example data:
            {'mac_address': ['72-18-95-2b-a0-f5'], 'name': b'AR56-EN11-Group_1 logical interconnect group'}

        Arguments:
        name*             --  Name of LI.
        Mac Address*      --  Mac Address of the connections in server

        * Required Arguments

    """
    FusionUIBase.navigate_to_section(SectionType.LOGICAL_INTERCONNECTS, time_for_loading=5)
    editliname = lis_obj["name"]
    if not select_logical_interconnect(editliname):
        ui_lib.fail_test("Existing Edit LI Function, Not selected LI %s" % editliname)
    EditLogicalInterconnects.click_logical_mac_address()
    mac = lis_obj["mac_address"]
    mac = mac.replace("-", ":")
    mac = mac.upper()
    logger.info("Mac Address is %s" % mac)
    EditLogicalInterconnects.input_mac_address(mac)
    EditLogicalInterconnects.click_update()
    mac_address_list = EditLogicalInterconnects.get_mac_address_list()
    del mac_address_list[0]  # To eliminate combo box value which is none
    logger.info("Mac Address is %s" % mac_address_list)
    for mac_address in mac_address_list:
        if mac_address == mac:
            logger.info("specified Default Gateway Mac address [%s] only displayed" % mac_address)
        else:
            ui_lib.fail_test("Specified Default Gateway Mac address [%s] not displayed" % mac_address)
    return True


def _verify_interconnects(data_interconnect, interconnects_list):
    """ This function iterate the interconnect list and verify that the list contains only the interconnect mentioned in data

        Example:
        | `verify interconnects`      |     |
    """
    for interconnect in interconnects_list:
        if interconnect == data_interconnect:
            logger.info("Specified interconnect only displayed")
        else:
            ui_lib.fail_test("Specified interconnect not displayed")


def _verify_networks(data_network, networks_list):
    """ This function iterate the network list and verify that the list contains only the network mentioned in data

        Example:
        | `verify networks`      |     |
    """
    for network in networks_list:
        if network == data_network:
            logger.info("Specified network only displayed")
        else:
            ui_lib.fail_test("Specified network not displayed")


def _verify_vlan(data_vlan, vlan_list):
    """ This function iterate the vlan list and verify that the list contains only the vlan mentioned in data

        Example:
        | `verify vlan`      |     |
    """
    for vlan in vlan_list:
        if vlan == data_vlan:
            logger.info("Specified vlan id only displayed")
        else:
            ui_lib.fail_test("Specified vlan id not displayed")


def _add_logical_interconnect_snmpv3(snmpv3):
    if hasattr(snmpv3, "snmpv3enabled"):
        if snmpv3.snmpv3enabled.lower() == 'enabled':
            EditLogicalInterconnects.toggle_snmpv3_enabled()
        elif snmpv3.snmpv3enabled.lower() == 'disabled':
            EditLogicalInterconnects.toggle_snmpv3_disabled()
    if hasattr(snmpv3, "tbirdsnmpv3enabled"):
        VerifyLogicalInterconnects.verify_tbird_snmpv3_enabled(snmp_obj.snmpv3enabled)
    if getattr(snmpv3, 'remove_snmpuser', None):
        for n, remove_obj in enumerate(snmpv3.remove_snmpuser):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmpv3.remove_snmpuser), '-' * 14))
            __edit_li_remove_snmp_user(remove_obj)

    if getattr(snmpv3, 'adduser', None):
        _add_snmp_v3_user(snmpv3)
    if getattr(snmpv3, 'edit_snmpuser', None):
        for n, edit_obj in enumerate(snmpv3.edit_snmpuser):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmpv3.edit_snmpuser), '-' * 14))
            __edit_li_edit_snmp_user(edit_obj)

    # - Add snmpv3 trap destinations
    if getattr(snmpv3, 'add_snmpv3_trapdestination', None):
        __edit_li_add_snmpv3_trap_destination(snmpv3)
    # - Edit snmpv3 trap destination
    if getattr(snmpv3, 'edit_snmpv3_trapdestination', None):
        for n, edit_obj in enumerate(snmpv3.edit_snmpv3_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmpv3.edit_snmpv3_trapdestination), '-' * 14))
            __edit_li_edit_snmpv3_trap_destination(edit_obj)
    # - remove snmpv3 trap destination
    if getattr(snmpv3, 'remove_snmpv3_trapdestination', None):
        for n, remove_obj in enumerate(snmpv3.remove_snmpv3_trapdestination):
            logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), len(snmpv3.remove_snmpv3_trapdestination), '-' * 14))
            __edit_li_remove_snmpv3_trap_destination(remove_obj)


def __edit_li_remove_snmp_user(remove_obj):
    ''' Removes existing snmp users
    <remove_snmpuser
    user*        -- snmpv3 username
    remove_error -- throws appropriate error in the UI page if the users attempts to remove a snmpv3user
                    that is currently used in any of the trap destination
    resolution   -- Resolution steps provided in the UI page to remove the snmpv3user  when user try remove a snmpv3
                     user currently held in any of the trap destination
    * Required Arguments

    Examples:


        <remove_snmpuser user="user2" remove_error="user2 cannot be removed while it is being used by one or more trap destinations."
            resolution="Remove the associated trap destinations first and try again. Alternatively, edit the trap destinations
            to specify a different user and try again.">
        </remove_snmpuser>

        <remove_snmpuser user="user1"></remove_snmpuser>
    '''

    logger.info("Remove snmp user with user '{0}'".format(remove_obj.user))
    EditLogicalInterconnects.click_remove_snmp_user_icon(remove_obj.user)
    VerifyLogicalInterconnects.wait_remove_snmp_user_confirm_dialog_shown()
    # if not EditLogicalInterconnects.wait_remove_snmp_user_confirmation_shown():
    if hasattr(remove_obj, 'remove_error'):
        remove_error = remove_obj.remove_error + "\n" + "\n" + remove_obj.resolution
        if VerifyLogicalInterconnects.verify_remove_snmpv3_user_error(remove_error):
            EditLogicalInterconnects.click_snmp_error_close_button()

    elif hasattr(remove_obj, 'traps_associated'):
        EditLogicalInterconnects.click_snmp_user_delete_error_icon()
        text = EditLogicalInterconnects.get_text_associated_trap_destination()
        logger.info("traps are %s" % text)
        traps = [item.strip() for item in remove_obj.traps_associated.split(',')]
        for i, trap in enumerate(traps):
            logger.info("trap is %s" % trap)
            VerifyLogicalInterconnects.verify_snmpv3_trap_associated_user(trap)
        EditLogicalInterconnects.click_snmp_error_close_button()
    else:
        EditLogicalInterconnects.click_remove_snmp_user_confirm()
        VerifyLogicalInterconnects.wait_remove_snmp_user_confirm_dialog_disappear()
        VerifyLogicalInterconnects.wait_snmp_user_table_disappear(remove_obj.user)
        return True


def __edit_li_edit_snmp_user(usr_obj):
    ''' Edits exisiting snmpv3 users
        <edit_snmpuser
        username*                   --  Snmpv3 user name
        security_level             --  Security level to be chosen for user.values can be none, authentication or authenticationandprivacy
        auth_protocol               --  authentication protocol to be provided if user chooses
                                        authentication or authenticationandprivacy as security level.
       authentication_password      --  password for authentication protocol.Must be 8-31 alphanumeric characters
       confirm_auth_password        --  password set for authentication_password should be passed
       priv_protocol                --  privacy protocol to be provided if user chooses
                                        authenticationandprivacy as security level
        privacy_password            --  password for privacy protocol.Must be 8-31 alphanumeric characters
       confirm_priv_password        --  password set for privacy_password should be passed
         * Required Arguments

         Examples:
         <edit_snmpuser username= "user1"  security_level="none"></edit_snmpuser>

        <edit_snmpuser username= "user3"  security_level="authentication" auth_protocol="MD5"
        authentication_password="Password1" confirm_auth_password="Password1"></edit_snmpuser>

        <edit_snmpuser username= "user6"
              security_level="authenticationandprivacy" auth_protocol="MD5"
              authentication_password="Password1" confirm_auth_password="Password1"
              priv_protocol="AES-128" privacy_password="Password2"
              confirm_priv_password="Password2"></edit_snmpuser>
    '''

    logger.info("Editing SNMP USer %s " % usr_obj.username)
    EditLogicalInterconnects.click_edit_snmp_user(usr_obj.username)
    VerifyLogicalInterconnects.wait_edit_snmp_user_confirm_dialog_shown()
    __add_user(usr_obj)
    return True


def _add_snmp_v3_user(snmp_obj):
    ''' Adds snmpv3 users
    <adduser
    username*                   --  Snmpv3 user name
    security_level*             --  Security level to be chosen for user.values can be none, authentication or authenticationandprivacy
    auth_protocol               --  authentication protocol to be provided if user chooses
                                    authentication or authenticationandprivacy as security level.
   authentication_password      --  password for authentication protocol.Must be 8-31 alphanumeric characters
   confirm_auth_password        --  password set for authentication_password should be passed
   priv_protocol                --  privacy protocol to be provided if user chooses
                                    authenticationandprivacy as security level
    privacy_password            --  password for privacy protocol.Must be 8-31 alphanumeric characters
   confirm_priv_password        --  password set for privacy_password should be passed
   action*                      --  option to be given as add or add_plus. adds user with the option "add"

     * Required Arguments

     Examples:
     <adduser username= "user1"  security_level="none" action="add"></adduser>

    <adduser username= "user3"  security_level="authentication" auth_protocol="MD5"
    authentication_password="Password1" confirm_auth_password="Password1" action="add"></adduser>

    <adduser username= "user6"
          security_level="authenticationandprivacy" auth_protocol="MD5"
          authentication_password="Password1" confirm_auth_password="Password1"
          priv_protocol="AES-192" privacy_password="Password2"
          confirm_priv_password="Password2" action="add"></adduser>
        '''

    logger.info("Adding user for SNMPv3")
    add_length = len(snmp_obj.adduser)
    logger.info("Number of users to be added is %s" % add_length)
    EditLogicalInterconnects.click_add_snmp_user()
    VerifyLogicalInterconnects.verify_add_snmp_user_dialog_visible()
    for index, usr_obj in enumerate(snmp_obj.adduser):
        if index != add_length:
            logger.info("Adding user %s" % usr_obj.username)
            EditLogicalInterconnects.input_add_snmp_user_name(usr_obj.username)
            __add_user(usr_obj)
        else:
            if index == add_length or error_flag == 1:
                if usr_obj.action == "edit":
                    VerifyLogicalInterconnects.wait_edit_snmp_user_confirm_dialog_disappear()
                elif usr_obj.action == "add":
                    VerifyLogicalInterconnects.wait_add_snmp_user_dialog_disappear()
    return True


def __add_user(usr_obj):
    error_flag = 0
    logger.info("configuring add user details")
    if usr_obj.security_level.lower() == "none":
        EditLogicalInterconnects.select_security_level_none()

    elif usr_obj.security_level.lower() == "authentication":
        EditLogicalInterconnects.select_security_level_authentication()
    elif usr_obj.security_level.lower() == "authenticationandprivacy":
        if VerifyLogicalInterconnects.verify_security_level_authentication_and_privacy_visibility():
            EditLogicalInterconnects.select_security_level_authentication_and_privacy()
        else:
            logger.info("The security level is enabled as authentication and privacy in FIPS/CNSA mode ")
    else:
        ui_lib.fail_test("invalid option for user type")
    if usr_obj.security_level == "authentication" or usr_obj.security_level == "authenticationandprivacy":
        EditLogicalInterconnects.click_dropdown_authentication_protocol()
        list = EditLogicalInterconnects.get_authentication_protocols()
        logger.info("available authentication protocols are %s" % list)
        if usr_obj.auth_protocol in list:
            EditLogicalInterconnects.select_authentication_protocol(usr_obj.auth_protocol)
            if hasattr(usr_obj, "authentication_password"):
                EditLogicalInterconnects.input_authentication_password(usr_obj.authentication_password)
                EditLogicalInterconnects.input_confirm_authentication_password(usr_obj.confirm_auth_password)
        else:
            logger.warn("authentication protocol %s provided by the user is invalid. Hence the current snmpv3 user canot be added" % usr_obj.auth_protocol)
            EditLogicalInterconnects.click_add_snmp_user_cancel()
            return False

    if usr_obj.security_level == "authenticationandprivacy":
        EditLogicalInterconnects.click_dropdown_privacy_protocol()
        list = EditLogicalInterconnects.get_privacy_protocols()
        logger.info("available privacy protocols are %s" % list)
        if usr_obj.priv_protocol in list:
            EditLogicalInterconnects.select_authentication_and_privacy_protocol(usr_obj.priv_protocol)
            if hasattr(usr_obj, "privacy_password"):
                EditLogicalInterconnects.input_privacy_password(usr_obj.privacy_password)
                EditLogicalInterconnects.input_confirm_privacy_password(usr_obj.confirm_priv_password)
        else:
            logger.warn(" privacy protocol provided by the user is invalid.Hence SNMPv3 user cannot be added in the current LIG")
            EditLogicalInterconnects.click_add_snmp_user_cancel()
            return False
    if usr_obj.action == "add":
        EditLogicalInterconnects.click_add_snmp_user_add()
    elif usr_obj.action == "edit":
        EditLogicalInterconnects.click_add_snmp_user_edit()
    elif usr_obj.action == "add_plus":
        EditLogicalInterconnects.click_add_snmp_user_add_plus()
    if hasattr(usr_obj, "max_user_error"):
        if VerifyLogicalInterconnects.verify_add_max_snmp_user_error_message(usr_obj.max_user_error):
            EditLogicalInterconnects.click_add_snmp_user_cancel()
            error_flag += 1
            return error_flag

    elif hasattr(usr_obj, "auth_password_error"):
        if VerifyLogicalInterconnects.verify_invalid_authentication_password_error_message(usr_obj.auth_password_error):
            EditLogicalInterconnects.click_add_snmp_user_cancel()

    elif hasattr(usr_obj, "privacy_password_error"):
        if VerifyLogicalInterconnects.verify_invalid_privacy_password_error_message(usr_obj.privacy_password_error):
            EditLogicalInterconnects.click_add_snmp_user_cancel()

    elif hasattr(usr_obj, "invalid_username_error"):
        if VerifyLogicalInterconnects.verify_invalid_username_error_message(usr_obj.invalid_username_error):
            EditLogicalInterconnects.click_add_snmp_user_cancel()

    elif hasattr(usr_obj, "duplicate_username_error"):
        if VerifyLogicalInterconnects.verify_duplicate_username_error_message(usr_obj.duplicate_username_error):
            EditLogicalInterconnects.click_add_snmp_user_cancel()

    return True


def __edit_li_add_snmpv3_trap_destination(snmp_obj):
    '''
     Adds trap destination for snmpv3
    <trapdestination>
    trapdestination*   --  Trap Destination for snmpv3
    trapformat*        --  Trap Format. Possible value: SNMPv1|SNMPv2|SNMPv3
    notification_type* --  Whether to enable notification type, Possible value : TRAP|INFORM.Applicable only for Trap Format snmpv3.

   snmp_user           --  To choose the snmpv3 user. If not, default user will be selected.Applicable only for Trap Format snmpv3.
   port                --  Port configuration
   engineid
   communitystring     --  Optional,Community string as string value. Applicable only for Trap Formats snmpv1 and snmpv2.
   severity            --  Sets severity of the trap. possible values are:
                            Critical-> The SNMP manager cannot manage installed components.
                            Major->One or more of the component's subsystems is not operating properly, causing serious disruption to functions.
                            Minor->One or more of the component's subsystems is not operating properly, causing slight disruption to functions.
                            Warning-> The component has a potential problem.
                            Normal->The component is fully functional.
                            Info->Operational information on the fully functioning component.
                            Unknown->The SNMP manager has not yet established communication with the component.
   vcm_traps           --   Trap category for VCM (Virtual Connect Manager) possible values are:
                                Legacy ->When the software changes status, configuration status, or redundancy mode.
    enet_traps         --  Ethernet Trap Categories. Possible values are:
                              Port Status ->When a link changes from being up or down.
                              Port Thresholds->Throughput utilization thresholds are exceeded.
                              Other->Authentication failures.
   fc_traps            --  Fiber Channel trap categories. Possible values are:
                            Port Status->When a link changes from being up or down.
                            Other->Authentication failures.
   </trapdestination>
     * Required Arguments

     Examples:
     <trapdestination trapdestination= "10.101.11.14"  trapformat="snmpv3" notification_type="Trap"  snmp_user="user5" ></trapdestination>
     <trapdestination trapdestination= "10.101.11.15"  trapformat="snmpv3" port="165" notification_type="Inform" engineid="0XFFFFfffffffff" snmp_user="user5" vcm_traps="legacy"
     enet_traps="Port status, Other" fc_traps="Port status, Other"  ></trapdestination>

          <trapdestination trapdestination= "10.101.11.16"  trapformat="snmpv2" communitystring="public"
          severity="Crtical, Major" vcm_traps="legacy" enet_traps="Port status, Other" fc_traps="Port status, Other"  ></trapdestination>
         vcm_traps

    '''
    logger.info("- configure Trap Destination settings for snmpv3")
    td_list = snmp_obj.add_snmpv3_trapdestination
    td_len = len(td_list)
    EditLogicalInterconnects.click_add_trap_destination()
    VerifyLogicalInterconnects.wait_add_trap_destination_dialog_shown()

    for index, td_obj in enumerate(td_list):
        if index != td_len:
            EditLogicalInterconnects.input_add_trap_destination_trap_destination(td_obj.trapdestination)
            __add_trap_values(td_obj)
        else:
            if index == td_len or error_flag == 1:
                if td_obj.action == "add":
                    EditLogicalInterconnects.wait_add_trap_destination_dialog_disappear()
                elif td_obj.action == "edit":
                    EditLogicalInterconnects.wait_edit_trap_destination_dialog_disappear()
    return True


def __edit_li_edit_snmpv3_trap_destination(td_obj):
    '''
     Edits trap destination for snmpv3
    <edit_trapdestination>
    trapdestination*   --  Trap Destination for snmpv3
    new_trapdestination -- New trap destination
    trapformat*        --  Trap Format. Possible value: SNMPv1|SNMPv2|SNMPv3
    notification_type --  Whether to enable notification type, Possible value : TRAP|INFORM.Applicable only for Trap Format snmpv3.

   snmp_user           --  To choose the snmpv3 user. If not, default user will be selected.Applicable only for Trap Format snmpv3.
   port                --  Port configuration
   engineid
   communitystring     --  Optional,Community string as string value. Applicable only for Trap Formats snmpv1 and snmpv2.
   severity            --  Sets severity of the trap. possible values are:
                            Critical-> The SNMP manager cannot manage installed components.
                            Major->One or more of the component's subsystems is not operating properly, causing serious disruption to functions.
                            Minor->One or more of the component's subsystems is not operating properly, causing slight disruption to functions.
                            Warning-> The component has a potential problem.
                            Normal->The component is fully functional.
                            Info->Operational information on the fully functioning component.
                            Unknown->The SNMP manager has not yet established communication with the component.
   vcm_traps           --   Trap category for VCM (Virtual Connect Manager) possible values are:
                                Legacy ->When the software changes status, configuration status, or redundancy mode.
    enet_traps         --  Ethernet Trap Categories. Possible values are:
                              Port Status ->When a link changes from being up or down.
                              Port Thresholds->Throughput utilization thresholds are exceeded.
                              Other->Authentication failures.
   fc_traps            --  Fiber Channel trap categories. Possible values are:
                            Port Status->When a link changes from being up or down.
                            Other->Authentication failures.
   </edit_trapdestination>
     * Required Arguments

     Examples:
     <edit_trapdestination trapdestination= "10.101.11.14" new_trapdestionation="10.1.1.1" trapformat="snmpv3" notification_type="Trap"  snmp_user="user5" ></edit_trapdestination>
     <edit_trapdestination trapdestination= "10.101.11.15"  trapformat="snmpv3" port="165" notification_type="Inform" engineid="0XFFFFfffffffff" snmp_user="user5" vcm_traps="legacy"
     enet_traps="Port status, Other" fc_traps="Port status, Other"  ></edit_trapdestination>

          <edit_trapdestination trapdestination= "10.101.11.16"  trapformat="snmpv2" communitystring="public"
          severity="Crtical, Major" vcm_traps="legacy" enet_traps="Port status, Other" fc_traps="Port status, Other"  ></edit_trapdestination>
         vcm_traps

    '''
    logger.info("- Edit Trap Destination settings")

    if hasattr(td_obj, 'new_trapdestination'):
        EditLogicalInterconnects.click_edit_trap_destination_icon(td_obj.trapdestination)
        VerifyLogicalInterconnects.wait_edit_trap_destination_dialog_shown()
        EditLogicalInterconnects.input_add_trap_destination_trap_destination(td_obj.new_trapdestination)
        __add_trap_values(td_obj)
    return True


def __add_trap_values(td_obj):
    error_flag = 0
    if hasattr(td_obj, 'communitystring'):
        EditLogicalInterconnects.input_add_trap_destination_community_string(td_obj.communitystring)
    if hasattr(td_obj, 'trapformat'):

        if td_obj.trapformat.lower() == "snmpv1":
            EditLogicalInterconnects.tick_add_trap_destination_trap_format_snmpv1()
        elif td_obj.trapformat.lower() == "snmpv2":
            EditLogicalInterconnects.tick_add_trap_destination_trap_format_snmpv2()
            if not VerifyLogicalInterconnects.verify_snmpv3_trap_destination_notification_visibility():
                logger.info("Successfully verified that notification type is disabled for snmpv2")
                if not VerifyLogicalInterconnects.view_snmpv3_trap_destination_snmp_user_visibility():
                    logger.info("Successfully verified that users are disabled for snmpv2")
        elif td_obj.trapformat.lower() == "snmpv3":
            EditLogicalInterconnects.tick_add_trap_destination_trap_format_snmpv3()
    if hasattr(td_obj, 'notification_type'):
        if td_obj.notification_type == "trap":
            EditLogicalInterconnects.disable_snmpv3_trap_destination_notification()
        elif td_obj.notification_type == "inform":
            EditLogicalInterconnects.enable_snmpv3_trap_destination_notification()
    if hasattr(td_obj, 'engineid'):
        EditLogicalInterconnects.input_add_trap_destination_engine_id(td_obj.engineid)
    if hasattr(td_obj, 'snmp_user'):
        EditLogicalInterconnects.click_dropdown_snmpv3_user_in_trap_destination()
        list = EditLogicalInterconnects.get_snmpv3_user_in_trap_destination()
        if td_obj.snmp_user in list:
            logger.info("successfully verified that user is displayed in the list")
        else:
            logger.warn("user is not added in the snmp. Please add a user and then use it in trap destination")
            EditLogicalInterconnects.click_add_trap_destination_cancel()
            return False
        EditLogicalInterconnects.select_snmpv3_user_in_trap_destination(td_obj.snmp_user)
    if hasattr(td_obj, 'port'):
        EditLogicalInterconnects.input_trap_destination_port(td_obj.port)

        # detail configuration for severity, VCM traps etc
    if hasattr(td_obj, 'severity'):
        severity = [item.strip() for item in td_obj.severity.split(',')]
        EditLogicalInterconnects.click_add_severity()
        for i, severe in enumerate(severity):
            EditLogicalInterconnects.select_trap_destination_severity(severe)

    if hasattr(td_obj, 'vcm_traps'):
        traps = [item.strip() for item in td_obj.vcm_traps.split(',')]
        EditLogicalInterconnects.click_add_vcm_traps()
        for i, trap in enumerate(traps):
            EditLogicalInterconnects.select_trap_destination_vcm_trap(trap)

    if hasattr(td_obj, 'enet_traps'):
        enet_traps = [item.strip() for item in td_obj.enet_traps.split(',')]
        EditLogicalInterconnects.click_add_vc_enet_traps()
        for i, trap in enumerate(enet_traps):
            EditLogicalInterconnects.select_trap_destination_vc_enet_traps(trap)

    if hasattr(td_obj, 'fc_traps'):
        fc_traps = [item.strip() for item in td_obj.fc_traps.split(',')]
        EditLogicalInterconnects.click_add_vc_fc_traps()
        for i, trap in enumerate(fc_traps):
            EditLogicalInterconnects.select_trap_destination_vc_fc_traps(trap)
    if td_obj.action == "add":
        EditLogicalInterconnects.click_add_trap_destination_add()
    elif td_obj.action == "edit":
        EditLogicalInterconnects.click_edit_trap_destination_ok()
    elif td_obj.action == "add_plus":
        EditLogicalInterconnects.click_add_trap_destination_add_plus()
        logger.info("edited successfully")
    if hasattr(td_obj, 'trap_error'):
        max_trap_error = td_obj.trap_error + "\n" + td_obj.resolution
        if VerifyLogicalInterconnects.verify_max_trap_error_message(max_trap_error):
            EditLogicalInterconnects.click_add_trap_destination_cancel()
            error_flag += 1
            return error_flag
    elif hasattr(td_obj, 'snmp_user_error'):
        if VerifyLogicalInterconnects.verify_no_snmp_user_error_msg(td_obj.snmp_user_error):
            EditLogicalInterconnects.click_add_trap_destination_cancel()

    elif hasattr(td_obj, 'port_error'):
        if VerifyLogicalInterconnects.verify_invalid_port_error(td_obj.port_error):
            EditLogicalInterconnects.click_add_trap_destination_cancel()

    elif hasattr(td_obj, 'engineid_error'):
        if VerifyLogicalInterconnects.verify_invalid_engine_id_error(td_obj.engineid_error):
            EditLogicalInterconnects.click_add_trap_destination_cancel()

    return True


def __edit_li_remove_snmpv3_trap_destination(remove_obj):
    ''' Removes existing trap destination

    <remove_snmpv3_trapdestination
    trapdestination*        -- snmpv3 trapdestination

    * Required Arguments

    Example:

   <remove_snmpv3_trapdestination trapdestination="10.101.11.1" ></remove_snmpv3_trapdestination>

    '''

    logger.info("Remove snmpv3 trap destination with Destination '{0}'".format(remove_obj.trapdestination))
    EditLogicalInterconnects.click_remove_snmpv3_trap_destination_icon(remove_obj.trapdestination)
    VerifyLogicalInterconnects.wait_remove_snmpv3_trap_destination_confirm_dialog_shown()
    EditLogicalInterconnects.click_remove_trap_destination_yes_remove()
    VerifyLogicalInterconnects.wait_remove_snmpv3_trap_destination_confirm_dialog_disappear()
    VerifyLogicalInterconnects.wait_trap_destination_table_row_disappear(remove_obj.trapdestination)


def _verify_logical_interconnect_snmp(snmp):
    logger.info("Verifying configuration in SNMP view...")

    FusionUIBase.select_view_by_name('SNMP')
    snmp = snmp[0] if isinstance(snmp, list) else snmp

    if hasattr(snmp, 'snmpv3_enabled'):
        VerifyLogicalInterconnects.verify_snmpv3_enabled(snmp.snmpv3_enabled)

        # - snmp user
    if hasattr(snmp, 'snmpuser'):
        logger.info("Verifying SNMP users...")
        snmp_snmpuser = snmp.snmpuser
        for user in snmp_snmpuser:
            if VerifyLogicalInterconnects.verify_snmp_users_user_visiblity(user.username):
                logger.info("Successfully verified that snmp user %s exist" % user.username)
            else:
                logger.warn("Unable to view snmp user")
                return False
            if hasattr(user, 'privacy_protocol'):
                VerifyLogicalInterconnects.verify_snmpv3_user_privacy_protocol(user.username, user.privacy_protocol)

            if hasattr(user, 'authentication_protocol'):
                VerifyLogicalInterconnects.verify_snmpv3_user_auth_protocol(user.username, user.authentication_protocol)
            if hasattr(user, 'security_level'):
                VerifyLogicalInterconnects.verify_snmpv3_user_security_level(user.username, user.security_level)

            # - trap destination
    if hasattr(snmp, 'trapdestination'):
        logger.info("Verifying SNMP trap destination settings...")

        snmp_trapdestination = snmp.trapdestination

        for trap_item in snmp_trapdestination:

            if not VerifyLogicalInterconnects.verify_snmp_trap_destinations_destination_visiblity(trap_item.trapdestination):
                logger.warn("unable to view trap destination")
                return False
            else:
                CommonOperationLogicalInterconnect.click_snmpv3_trap_destination_values(trap_item.trapdestination)

            if hasattr(trap_item, 'port'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_port(trap_item.trapdestination, trap_item.port)
            if hasattr(trap_item, 'trapformat'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_format(trap_item.trapdestination, trap_item.trapformat)

            if hasattr(trap_item, 'communitystring'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_community_string(trap_item.trapdestination, trap_item.communitystring)
            if hasattr(trap_item, 'notificationtype'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_notification_type(trap_item.trapdestination, trap_item.notificationtype)
            if hasattr(trap_item, 'engineid'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_engineid(trap_item.trapdestination, trap_item.engineid)
            if hasattr(trap_item, 'username'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_username(trap_item.trapdestination, trap_item.username)

            if hasattr(trap_item, 'severity'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_severity(trap_item.trapdestination, trap_item.severity)
            if hasattr(trap_item, 'vcm_traps'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_vcm_traps(trap_item.trapdestination, trap_item.vcm_traps)
            if hasattr(trap_item, 'enet_traps'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_enet_traps(trap_item.trapdestination, trap_item.enet_traps)
            if hasattr(trap_item, 'fc_traps'):
                VerifyLogicalInterconnects.verify_snmp_trap_destinations_fc_traps(trap_item.trapdestination, trap_item.fc_traps)
            VerifyLogicalInterconnects.close_snmpv3_trap_destination_values(trap_item.trapdestination)
    if hasattr(snmp, 'snmpaccess'):
        logger.info("Verifying SNMP access...")
        snmp_access = snmp.snmpaccess

        for access_item in snmp_access:
            CommonOperationLogicalInterconnect.verify_snmp_access_ip_or_subnet_exist(access_item.iporsubnet)

    return True
