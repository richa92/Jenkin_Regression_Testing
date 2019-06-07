# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
""" Fusion Enclosure Group UI page."""
import time
from FusionLibrary.ui.business_logic.servers.logicalenclosures import C7000CommonOperationLogicalEnclosures
from FusionLibrary.ui.business_logic.servers.enclosuregroups import *
from RoboGalaxyLibrary.data import test_data
from RoboGalaxyLibrary.ui.common.PerfConstants import PerfConstants
from FusionLibrary.ui.business_logic.base import SectionType
from FusionLibrary.ui.business_logic.servers.enclosuregroups import (CommonOperationEnclosureGroups,
                                                                     DeleteEnclosureGroups)
from FusionLibrary.ui.business_logic.servers.enclosuregroups import CreateEnclosureGroups
from FusionLibrary.ui.business_logic.servers.enclosuregroups import EditEnclosureGroups
from FusionLibrary.ui.servers.enclosuregroups_elements import FusionEnclosureGroupsPage


def navigate():
    logger.info("Navigate to Enclosure Groups page")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)


def create_enclosure_group(eg_obj):
    """ Create Enclosure Group    """

    logger.info("Create Enclosure Group")
    navigate()

    for eg in eg_obj:
        logger.info("Adding a EG with name '{0}'".format(eg.name))
        if C7000CommonOperationEnclosureGroups.verify_enclosure_group_not_exist(eg.name, 10, False) is False:
            logger.warn("Enclosure Group '%s' already exists" % eg.name)
            continue

        C7000CreateEnclosureGroups.click_create_enclosure_group_button()
        C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        if eg.name == "" or eg.name.lower() == "empty":
            ui_lib.fail_test("Enclosure Group name is not defined")
        else:
            C7000CreateEnclosureGroups.input_enclosure_group_name(eg.name)

        if not hasattr(eg, "switch"):
            logger.warn("no switch child elements in <encgroup> node [ %s ]" % eg.name)
        else:
            for switch_obj in eg.switch:
                C7000CreateEnclosureGroups.input_select_logical_interconnect_group(switch_obj.bay, switch_obj.lig)
        if hasattr(eg, "script"):
            FusionUIBase.select_view_by_name('Configuration Script')
            C7000CreateEnclosureGroups.input_configuration_script(eg.script)

        C7000CreateEnclosureGroups.click_create_button()
        C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)

        if C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.info("Enclosure Group '%s' created successfully" % eg.name)
        else:
            ui_lib.fail_test("creating Enclosure Group '%s' failed" % eg.name)

    logger.debug("Return Value = True")
    return True


def create_tbrid_enclosure_group(eg_obj):
    """ Create a enclosure group for Tbird enclosure

    Arguments:
      <encgroup>
          name*                 --  Name of enclosure group as a string.
          enclosure_count*      --  Enclosure count as number. 3 is max.
          ipv4_addresses*       --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
          deployment_network_type   -- Deployment network type. Possible value: None|Internal|External
          power_mode            --  Power mode for enclosure group. Possible value: Redundant power feed|Redundant power supply
          <enclosure> optional, for select LIG for interconnect bay (can be multiple)
            no*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            <switch> required, for specifying interconnect model
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig             --  Logical interconnect group name to be selected.

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}
        <encgroups>
            <encgroup name="OVA-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      deployment_network_type="None"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_OVAEncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" lig="LIG_OVAEncICM" />
                </enclosure>
            </encgroup>
            <encgroup name="Reg2-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_Reg2EncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" />
                </enclosure>
            </encgroup>
            <encgroup name="Reg1-EG"
                      enclosure_count="1"
                      ipv4_addresses="Use address pool"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_Reg1EncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" />
                </enclosure>
                <ipv4addresspool name = "Testrange-1" action = "add" />
            </encgroup>
        </encgroups>

    """
    logger.info("Create Tbird Enclosure Group")
    navigate()

    logger.info("Before check")

    for eg in eg_obj:
        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' already exists" % eg.name)
            continue
        logger.info("After check of exists")
        TBirdCreateEnclosureGroups.click_create_enclosure_group_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        logger.info("Enclosure Group '%s' " % eg.name)

        if eg.name == "" or eg.name == "empty":
            ui_lib.fail_test("EG name is not specified")
        else:
            TBirdCreateEnclosureGroups.input_enclosure_group_name(eg.name)
        TBirdCreateEnclosureGroups.select_enclosure_count(eg.enclosure_count)
        if hasattr(eg, "deployment_network_type"):
            TBirdCreateEnclosureGroups.select_deployment_network_type(eg.deployment_network_type)

        if eg.ipv4_addresses.lower() == 'use address pool':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_address_pool()
            if hasattr(eg, 'ipv4addresspool'):
                rangepool_obj = eg.ipv4addresspool
                for range in rangepool_obj:
                    if hasattr(range, 'action'):
                        if not _select_ipv4_addresses_in_use_address_pool(range.name, range.action, 15, False):
                            TBirdCreateEnclosureGroups.click_cancel_button()
                            ui_lib.fail_test("Unable to select IP addresses from Pool")
        elif eg.ipv4_addresses.lower() == 'use dhcp':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_dhcp()
        elif eg.ipv4_addresses.lower() == 'manage externally':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_manage_externally()
        else:
            ui_lib.fail_test("Unexpected ipv4_addresses attrbiute '%s'" % eg.ipv4_addresses)

        if hasattr(eg, 'enclosure'):
            enc_list_obj = eg.enclosure if isinstance(eg.enclosure, list) else [eg.enclosure]
            FusionUIBase.select_view_by_name("Interconnect Bay Configuration")

            for enc_obj in enc_list_obj:
                enc_no = enc_obj.no
                for switch_obj in enc_obj.switch:
                    switch_no = switch_obj.bay
                    if hasattr(switch_obj, 'lig'):
                        switch_lig = switch_obj.lig
                        TBirdCreateEnclosureGroups.make_choose_lig_input_into_viewpoint(enc_no, switch_no, timeout=8)
                        TBirdCreateEnclosureGroups.input_select_lig(enc_no, switch_no, switch_lig, timeout=8)

        if hasattr(eg, 'power_mode'):
            FusionUIBase.select_view_by_name("Power and Thermal Environmental Settings")
            TBirdCreateEnclosureGroups.select_power_mode(eg.power_mode)

        logger.info("Before click grp create")
        TBirdCreateEnclosureGroups.click_create_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)

        TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name)

        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.info("Enclosure Group '%s' created successfully" % eg.name)
        else:
            BuiltIn().fail("Creating Enclosure Group %s failed" % eg.name)

    logger.debug("Return Value = True")
    return True


def validate_lig_selection_when_create_enclosure_group(eg_obj):
    """ Validate lig panel when creating an Tbird enclosure group, used for F332, the enclosure_count must be 1

    Arguments:
      <encgroup>
          name*                 --  Name of enclosure group as a string.
          enclosure_count*      --  Enclosure count as number. 3 is max.
          ipv4_addresses*       --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
          power_mode            --  Power mode for enclosure group. Possible value: Redundant power feed|Redundant power supply
          <enclosure> optional, for select LIG for interconnect bay (can be multiple)
            no*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            <switch> required, for specifying interconnect model
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig             --  Logical interconnect group name to be selected.
                <verify> optional, for all virtual interconnect validation(can be multiple).
                    id*         -- Interconnect bay no as integer which need to verify. e.g. 1-6
                    lig*        -- Which lig was displayed in input box. e.g. None| ICM1
                <displayed> optional -- check displayed lig list
                    lig*        -- All optional LIG in pop-up combo menu.

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}
        <encgroups>
            <encgroup name="Reg2-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" lig="ICM1">
                        <verify id="1" lig="ICM1" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="None" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                        <displayed lig="ICM1" />
                        <displayed lig="ICM1-4" />
                        <displayed lig="ICM1-4-2" />
                    </switch>
                    <switch bay="1" lig="None">
                        <verify id="1" lig="None" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="None" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="1" lig="ICM1-4">
                        <verify id="1" lig="ICM1-4" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="ICM1-4" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="1" lig="ICM1-4-2">
                        <verify id="1" lig="ICM1-4-2" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="ICM1-4-2" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="2">
                        <displayed lig="ICM2" />
                        <displayed lig="ICM2-5" />
                    </switch>
                    <switch bay="3">
                        <displayed lig="ICM3" />
                        <displayed lig="ICM3-6" />
                    </switch>
                    <switch bay="4">
                        <displayed lig="ICM1" />
                        <displayed lig="ICM1-4" />
                        <displayed lig="ICM1-4-2" />
                    </switch>
                    <switch bay="5">
                        <displayed lig="ICM5" />
                        <displayed lig="ICM2-5" />
                    </switch>
                    <switch bay="6">
                        <displayed lig="ICM6" />
                        <displayed lig="ICM3-6" />
                    </switch>
                </enclosure>
            </encgroup>

    """
    logger.info("Create Tbird Enclosure Group")
    navigate()

    not_exists = 0
    logger.info("Before check")

    for eg in eg_obj:
        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' already exists" % eg.name)
            not_exists += 1
            continue
        logger.info("After check of exists")
        TBirdCreateEnclosureGroups.click_create_enclosure_group_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        logger.info("Enclosure Group '%s' " % eg.name)

        if eg.name == "" or eg.name == "empty":
            ui_lib.fail_test("EG name is not specified")
        else:
            TBirdCreateEnclosureGroups.input_enclosure_group_name(eg.name)
        TBirdCreateEnclosureGroups.select_enclosure_count(eg.enclosure_count)

        if eg.ipv4_addresses.lower() == 'use address pool':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_address_pool()
            if hasattr(eg, 'ipv4addresspool'):
                rangepool_obj = eg.ipv4addresspool
                for range in rangepool_obj:
                    if hasattr(range, 'action'):
                        if not _select_ipv4_addresses_in_use_address_pool(range.name, range.action, 15, False):
                            TBirdCreateEnclosureGroups.click_cancel_button()
                            ui_lib.fail_test("Unable to select IP addresses from Pool")
        elif eg.ipv4_addresses.lower() == 'use dhcp':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_dhcp()
        elif eg.ipv4_addresses.lower() == 'manage externally':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_manage_externally()
        else:
            ui_lib.fail_test("Unexpected ipv4_addresses attrbiute '%s'" % eg.ipv4_addresses)

        if hasattr(eg, 'enclosure'):
            enc_list_obj = eg.enclosure if isinstance(eg.enclosure, list) else [eg.enclosure]
            FusionUIBase.select_view_by_name("Interconnect Bay Configuration")

            for enc_obj in enc_list_obj:
                enc_no = enc_obj.no
                for switch_obj in enc_obj.switch:
                    switch_no = switch_obj.bay
                    TBirdCreateEnclosureGroups.make_choose_lig_input_into_viewpoint(enc_no, switch_no, timeout=8)
                    TBirdCreateEnclosureGroups.click_search_combo_box_menu(enc_no, switch_no)
                    TBirdCreateEnclosureGroups.wait_for_search_combo_menu_visible(enc_no, switch_no)

                    logger.info("Verify existing LIG can be displayed on correct bay...")
                    if hasattr(switch_obj, 'displayed'):
                        for lig_obj in switch_obj.displayed:
                            switch_lig = lig_obj.lig
                            TBirdVerifyEnclosureGroups.verify_drop_down_option_for_lig(enc_no, switch_no, switch_lig)
                        logger.info("All LIGs are found in search combo menu!")

                    if hasattr(switch_obj, 'lig'):
                        switch_lig = switch_obj.lig
                        TBirdCreateEnclosureGroups.input_select_lig(enc_no, switch_no, switch_lig, timeout=8)
                        if TBirdCreateEnclosureGroups.wait_change_lig_confirm_dialog_visible():
                            TBirdCreateEnclosureGroups.click_select_lig_button()

                        if hasattr(switch_obj, 'verify'):
                            for lig_verify in switch_obj.verify:
                                verify_no = lig_verify.id
                                verify_lig = lig_verify.lig
                                TBirdVerifyEnclosureGroups.verify_selected_lig_for_enclosure(enc_no, verify_no, verify_lig, timeout=8)
                    else:
                        TBirdCreateEnclosureGroups.click_search_combo_box_menu(enc_no, switch_no)
                        TBirdCreateEnclosureGroups.wait_for_search_combo_menu_invisible(enc_no, switch_no)

        if hasattr(eg, 'power_mode'):
            FusionUIBase.select_view_by_name("Power")
            TBirdCreateEnclosureGroups.select_power_mode(eg.power_mode)

        logger.info("Before click grp create")
        TBirdCreateEnclosureGroups.click_create_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)
        FusionUIBase.show_activity_sidebar()
        FusionUIBase.wait_activity_action_ok(eg.name, 'Create', timeout=30, fail_if_false=False)
        FusionUIBase.show_activity_sidebar()

        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.info("Enclosure Group '%s' created successfully" % eg.name)
        else:
            ui_lib.fail_test("Creating Enclosure Group %s failed" % eg.name)

    return True if not not_exists else False


def validate_selection_of_LIG_conflicts_with_previously_selected_when_creating_eg(eg_obj):
    """ Validate selection of a LIG conflicts with a previously selected LIG when creating EG.
        Used for F332, the enclosure_count must be 1

    Arguments:
      <encgroup>
          name*                 --  Name of enclosure group as a string.
          enclosure_count*      --  Enclosure count as number. 3 is max.
          ipv4_addresses*       --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
          power_mode            --  Power mode for enclosure group. Possible value: Redundant power feed|Redundant power supply
          <enclosure> optional, for select LIG for interconnect bay (can be multiple)
            no*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            <switch> required, for specifying interconnect model
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig             --  Logical interconnect group name to be selected.
                change          --  Whether accept to change used LIG. value:true|false
                expect_msg      --  Define the prompt message expect value.
                <verify> optional, for all virtual interconnect validation(can be multiple).
                    id*         -- Interconnect bay no as integer which need to verify. e.g. 1-6
                    lig*        -- Which lig was displayed in input box. e.g. None| ICM1

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}
        <encgroups>
            <encgroup name="Reg2-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1"
                            lig="ICM1"
                            change="True">
                        <verify id="1" lig="ICM1" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="None" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="4"
                            lig="ICM1-4"
                            change="False"
                            expect_msg='The logical interconnect group "%s" conflicts with an already selected logical interconnect group'>
                        <verify id="1" lig="ICM1" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="ICM1" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="4"
                            lig="ICM1-4-2"
                            change="False"
                            expect_msg='The logical interconnect group "%s" conflicts with an already selected logical interconnect group'>
                        <verify id="1" lig="ICM1-4-2" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="ICM1-4-2" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                </enclosure>
            </encgroup>
        </encgroups>

    """
    logger.info("Create Tbird Enclosure Group")
    navigate()

    not_exists = 0
    logger.info("Before check")
    for eg in eg_obj:
        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' already exists" % eg.name)
            not_exists += 1
            continue
        logger.info("After check of exists")
        TBirdCreateEnclosureGroups.click_create_enclosure_group_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        logger.info("Enclosure Group '%s' " % eg.name)

        if eg.name == "" or eg.name == "empty":
            ui_lib.fail_test("EG name is not specified")
        else:
            TBirdCreateEnclosureGroups.input_enclosure_group_name(eg.name)
        TBirdCreateEnclosureGroups.select_enclosure_count(eg.enclosure_count)

        if eg.ipv4_addresses.lower() == 'use address pool':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_address_pool()
            if hasattr(eg, 'ipv4addresspool'):
                rangepool_obj = eg.ipv4addresspool
                for range in rangepool_obj:
                    if hasattr(range, 'action'):
                        if not _select_ipv4_addresses_in_use_address_pool(range.name, range.action, 15, False):
                            TBirdCreateEnclosureGroups.click_cancel_button()
                            ui_lib.fail_test("Unable to select IP addresses from Pool")
        elif eg.ipv4_addresses.lower() == 'use dhcp':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_dhcp()
        elif eg.ipv4_addresses.lower() == 'manage externally':
            TBirdCreateEnclosureGroups.tick_ipv4_addresses_manage_externally()
        else:
            ui_lib.fail_test("Unexpected ipv4_addresses attrbiute '%s'" % eg.ipv4_addresses)

        if hasattr(eg, 'enclosure'):
            enc_list_obj = eg.enclosure if isinstance(eg.enclosure, list) else [eg.enclosure]
            FusionUIBase.select_view_by_name("Interconnect Bay Configuration")
            for enc_obj in enc_list_obj:
                enc_no = enc_obj.no
                for switch_obj in enc_obj.switch:
                    switch_no = switch_obj.bay
                    TBirdCreateEnclosureGroups.make_choose_lig_input_into_viewpoint(enc_no, switch_no, timeout=8)
                    TBirdCreateEnclosureGroups.click_search_combo_box_menu(enc_no, switch_no)
                    TBirdCreateEnclosureGroups.wait_for_search_combo_menu_visible(enc_no, switch_no)

                    switch_lig = switch_obj.lig
                    TBirdCreateEnclosureGroups.input_select_lig(enc_no, switch_no, switch_lig, timeout=8)
                    if TBirdCreateEnclosureGroups.wait_change_lig_confirm_dialog_visible():
                        msg = TBirdCreateEnclosureGroups.get_eg_change_confirm_prompt(switch_lig)
                        expect_msg = switch_obj.expect_msg % switch_lig

                        if getattr(switch_obj, "change", None).lower() == "true":
                            TBirdCreateEnclosureGroups.click_select_lig_button()
                        else:
                            TBirdCreateEnclosureGroups.click_cancel_select_lig_button()

                        if hasattr(switch_obj, "expect_msg"):
                            if expect_msg in msg:
                                logger.info("The prompt message contaions expect message.")
                            else:
                                ui_lib.fail_test("The warning message is not correct, fail the test.")

                    for lig_verify in switch_obj.verify:
                        verify_no = lig_verify.id
                        verify_lig = lig_verify.lig
                        TBirdVerifyEnclosureGroups.verify_selected_lig_for_enclosure(enc_no, verify_no, verify_lig, timeout=8)

        TBirdCreateEnclosureGroups.click_cancel_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)

        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_not_exist(eg.name, 10, False):
            logger.info("Enclosure Group '%s' validate successfully" % eg.name)
        else:
            ui_lib.fail_test("Validating Enclosure Group %s failed" % eg.name)

    return True if not not_exists else False


def validate_enclosure_group_info(eg_obj):
    """ Validate all information for enclosure groups

    Arguments:
      <encgroups>
          name*                 --  Name of enclosure group as a string.
          <general> optional    --  Define expected value for 'General' information
              ipv4_addresses*   --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
              usedby            --  The EG used by other parts, possible value: 1 logical enclosure, 2 server profile templates
          <power> optional      --  Define expected value for 'Power' information
              power_mode*       --  Power mode for enclosure group. Possible value: Redundant power feed|Redundant power supply
          <enclosure> optional  --  Define expected value for 'Interconnect Bay Configuration'
              no*               --  enclosure number, according this to verify related logical interconnect group . Possible value: 1|2|3.
            <switch>            --  Physical switches and LIGs information
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig*             --  Logical interconnect group name to be selected.
                type            --  Physical interconnect type
          <settings> optional   --  Define expected value for 'OS Deployment Settings'
            - networktype*      --  The deployment network type Possible value: None|Internal External

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}

        <informations>
            <encgroup name="EGp0001">
                <general ipv4_addresses="Manage externally" usedby="None" />
                <power power_mode="Redundant power feed" />
                <enclosure no="1">
                    <switch bay="1" lig="ICM1-4-2" type="Virtual Connect SE 16Gb FC Module for Synergy" />
                    <switch bay="4" lig="ICM1-4-2" type="Virtual Connect SE 16Gb FC Module for Synergy" />
                </enclosure>
                <settings networktype="None" />
            </encgroup>
        </informations>

    """
    logger.info("Validate Tbird Enclosure Group")
    navigate()

    total = len(eg_obj)
    not_exists = 0

    for n, eg in enumerate(eg_obj):
        logger.info("{2} No: {0} --- Total: {1} {2}".format((n + 1), total, '-' * 14))
        if not TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, timeout=10, fail_if_false=False):
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            not_exists += 1
            continue

        TBirdCommonOperationEnclosureGroups.click_enclosure_group(eg.name)

        if hasattr(eg, "general"):
            logger.info("verifying [ General ] info of a eg '%s'" % eg.name)
            TBirdCommonOperationEnclosureGroups.select_view_by_name("General")

            general_obj = eg.general[0] if isinstance(eg.general, list) else eg.general
            ipv4_addresses = general_obj.ipv4_addresses
            TBirdVerifyEnclosureGroups.verify_general_ipv4_address(expect_value=ipv4_addresses)
            if hasattr(general_obj, 'usedby'):
                usedby = general_obj.usedby
                TBirdVerifyEnclosureGroups.verify_general_used_by(expect_value=usedby)

        if hasattr(eg, "power"):
            logger.info("verifying [ Power ] info of a eg '%s'" % eg.name)
            TBirdCommonOperationEnclosureGroups.select_view_by_name("Power")

            power_obj = eg.power[0] if isinstance(eg.power, list) else eg.power
            power_mode = power_obj.power_mode
            TBirdVerifyEnclosureGroups.verify_power_mode(expect_value=power_mode)

        if hasattr(eg, "enclosure"):
            logger.info("verifying [ Interconnect Bay Configuration ] info of a eg '%s'" % eg.name)
            TBirdCommonOperationEnclosureGroups.select_view_by_name("Interconnect Bay Configuration")

            enc_list_obj = eg.enclosure if isinstance(eg.enclosure, list) else [eg.enclosure]
            for enc_obj in enc_list_obj:
                enc_no = enc_obj.no
                for switch_obj in enc_obj.switch:
                    switch_no = switch_obj.bay
                    switch_lig = switch_obj.lig
                    TBirdVerifyEnclosureGroups.verify_interconnect_bay_configuration_used_lig(enc_no, switch_no, expect_value=switch_lig)

                    if hasattr(switch_obj, 'type'):
                        switch_type = switch_obj.type
                        TBirdVerifyEnclosureGroups.verify_interconnect_bay_configuration_icm_type(enc_no, switch_no, expect_value=switch_type)

        if hasattr(eg, "settings"):
            logger.info("verifying [ OS Deployment Settings ] info of a eg '%s'" % eg.name)
            TBirdCommonOperationEnclosureGroups.select_view_by_name("OS Deployment Settings")

            settings_obj = eg.settings[0] if isinstance(eg.settings, list) else eg.settings
            networktype = settings_obj.networktype
            TBirdVerifyEnclosureGroups.verify_os_deployment_settings_network_type(expect_value=networktype)

    return True if not not_exists else False


def delete_enclosure_group(eg_obj):
    """ Delete Enclosure Group    """

    logger.info("Delete Enclosure Group")

    navigate()
    failed_times = 0

    for eg in eg_obj:
        if not CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            failed_times += 1
            continue
        if CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name):
            CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
            # wait target enclosure group get focus
            logger.info("Wait for enclosure group %s to be selected." % eg.name)

            retry_times = 0
            while retry_times < 3:
                if CommonOperationEnclosureGroups.verify_enclosure_group_seleted(eg.name, 5, False) is False:
                    logger.warn("Failed to select enclosure group %s, re-trying" % eg.name)
                    retry_times += 1
                    CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select enclosure group %s." % eg.name)
                failed_times += 1
                continue

            DeleteEnclosureGroups.select_actions_delete()
            if DeleteEnclosureGroups.verify_enclosure_group_cannot_delete(5, False):
                failed_times += 1
                DeleteEnclosureGroups.click_close_button()
                logger.warn("Enclosure group '%s' is used by something and can not be deleted." % eg.name)
                continue
            DeleteEnclosureGroups.wait_delete_dialog_shown()
            DeleteEnclosureGroups.click_yes_delete_button()
            DeleteEnclosureGroups.wait_delete_dialog_disappear()

            if DeleteEnclosureGroups.wait_enclosure_group_show_not_found(eg.name, 10, False):
                logger.info("Enclosure Group '%s' is deleted successfully" % eg.name)
                # in order to prevent from UI racing issue.
                BuiltIn().sleep(3)
            elif DeleteEnclosureGroups.verify_all_enclosure_groups_not_found(10, False):
                logger.info("All enclosure group are deleted successfully")
                BuiltIn().sleep(3)
            else:
                BuiltIn().fail("Not able to delete Enclosure Group %s" % eg.name)

    if failed_times > 0:
        logger.warn("Return Value = False")
        return False
    else:
        logger.debug("Return Value = True")
        return True


def edit_enclosure_group(eg_obj):
    """ Edit Enclosure Group    """
    failed_times = 0
    logger.info("Edit Enclosure Group")

    navigate()

    for eg in eg_obj:
        if not C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            failed_times += 1
            continue
        if C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name):
            C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
            # wait target enclosure group get focus
            logger.info("Wait for enclosure group %s to be selected." % eg.name)

            retry_times = 0
            while retry_times < 3:
                if C7000CommonOperationEnclosureGroups.verify_enclosure_group_seleted(eg.name, 5, False) is False:
                    logger.warn("Failed to select enclosure group %s, re-trying" % eg.name)
                    retry_times += 1
                    C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select enclosure group %s." % eg.name)
                failed_times += 1
                continue

            C7000EditEnclosureGroups.select_actions_edit()
            C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_shown()

            if hasattr(eg, "newname"):
                C7000EditEnclosureGroups.input_enclosure_group_name(eg.newname)
            # Use to edit switch and script
            if hasattr(eg, "switch"):
                for switch_obj in eg.switch:
                    logger.info("- About to choose LIG %s for bay %s" % (switch_obj.lig, switch_obj.bay))
                    # wait old name present in text box
                    time.sleep(3)
                    # input new name
                    C7000EditEnclosureGroups.input_select_logical_interconnect_group(switch_obj.bay, switch_obj.lig)
                    if C7000EditEnclosureGroups.wait_edit_enclosure_group_confirm_dialog_shown():
                        C7000EditEnclosureGroups.click_select_button()

            if hasattr(eg, "script"):
                C7000EditEnclosureGroups.input_configuration_script(eg.script)

            C7000EditEnclosureGroups.click_ok_button()
            C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_disappear()

    if failed_times > 0:
        logger.warn("Return Value = False")
        return False
    else:
        logger.debug("Return Value = True")
        return True


def edit_tbird_enclosure_group(*eg_obj):
    """ Create a enclosure group for Tbird enclosure
asdads
    Arguments:
      <encgroup>
          name*                 --  Name of enclosure group as a string.
          new_name              --  New name of enclosure group
          enclosure_count      --  Enclosure count as number. 3 is max.
          ipv4_addresses       --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
          power_mode            --  Power mode for enclosure group. Possible value: Redundant power feed|Redundant power supply
          <enclosure> optional, for select LIG for interconnect bay (can be multiple)
            no*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            <switch> required, for specifying interconnect model
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig             --  Logical interconnect group name to be selected.

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}
        <encgroups>
            <encgroup name="OVA-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_OVAEncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" lig="LIG_OVAEncICM" />
                </enclosure>
            </encgroup>
            <encgroup name="Reg2-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_Reg2EncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" />
                </enclosure>
            </encgroup>
            <encgroup name="Reg1-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_Reg1EncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" />
                </enclosure>
            </encgroup>
        </encgroups>
    """

    logger.info("Edit Tbird Enclosure Group")
    navigate()
    if isinstance(eg_obj, test_data.DataObj):
        eg_obj = [eg_obj]
    elif isinstance(eg_obj, tuple):
        eg_obj = list(eg_obj[0])
    logger.info("Before check")
    for enclosuregroup in eg_obj:
        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_not_exist(enclosuregroup.name, 10, False):
            ui_lib.fail_test("Enclosure group '%s' does not exist" % enclosuregroup.name)
        logger.info("After check of exists")
        TBirdCommonOperationEnclosureGroups.click_enclosure_group(enclosuregroup.name)
        TBirdEditEnclosureGroups.select_actions_edit()
        TBirdEditEnclosureGroups.wait_edit_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        logger.info("Enclosure Group '%s' " % enclosuregroup.name)

        if hasattr(enclosuregroup, 'new_name'):
            TBirdCreateEnclosureGroups.input_enclosure_group_name(enclosuregroup.new_name)

        if hasattr(enclosuregroup, 'ipv4_addresses'):
            if enclosuregroup.ipv4_addresses.lower() == 'use address pool':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_address_pool()
            elif enclosuregroup.ipv4_addresses.lower() == 'use dhcp':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_dhcp()
            elif enclosuregroup.ipv4_addresses.lower() == 'manage externally':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_manage_externally()
            else:
                ui_lib.fail_test("Unexpected ipv4_addresses attrbiute '%s'" % enclosuregroup.ipv4_addresses)

        if hasattr(enclosuregroup, 'enclosure'):
            enc_list_obj = enclosuregroup.enclosure if isinstance(enclosuregroup.enclosure, list) else [enclosuregroup.enclosure]
            FusionUIBase.select_view_by_name("Interconnect Bay Configuration")

            for enc_obj in enc_list_obj:
                for switch_obj in enc_obj.switch:
                    if hasattr(switch_obj, 'lig'):
                        TBirdCreateEnclosureGroups.make_choose_lig_input_into_viewpoint(enc_obj.no, switch_obj.bay)
                        TBirdCreateEnclosureGroups.input_select_lig(enc_obj.no, switch_obj.bay, switch_obj.lig)

        if hasattr(enclosuregroup, 'power_mode'):
            FusionUIBase.select_view_by_name("Power and Thermal Environmental Settings")
            TBirdCreateEnclosureGroups.select_power_mode(enclosuregroup.power_mode)

        logger.info("Before click grp create")
        TBirdCreateEnclosureGroups.click_create_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)
        ret1, ret2 = FusionUIBase.get_error_message_from_dialog(10)
        if ret1 is True:
            logger.warn("Error message encountered, stopping test")
            logger.warn(ret2)
            ui_lib.fail_test("Creating Enclosure Group %s failed" % enclosuregroup.name)

        FusionUIBase.show_activity_sidebar()
        TBirdCommonOperationEnclosureGroups.wait_activity_action_ok(enclosuregroup.name, fail_if_false=True)

        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(enclosuregroup.name, 10, False):
            logger.info("Enclosure Group '%s' created successfully" % enclosuregroup.name)
        else:
            ui_lib.fail_test("Creating Enclosure Group %s failed" % enclosuregroup.name)


def validate_lig_selection_when_edit_tbird_enclosure_group(eg_obj):
    """ Validate lig panel when creating an Tbird enclosure group, used for F332, the enclosure_count must be 1

    Arguments:

      <encgroup>
          name*                 --  Name of enclosure group as a string.
          new_name              --  New name of enclosure group
          enclosure_count*      --  Enclosure count as number. 3 is max.
          ipv4_addresses*       --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
          power_mode            --  Power mode for enclosure group. Possible value: Redundant power feed|Redundant power supply
          <enclosure> optional, for select LIG for interconnect bay (can be multiple)
            no*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            <switch> required, for specifying interconnect model
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig             --  Logical interconnect group name to be selected.
                <verify> optional, for all virtual interconnect validation(can be multiple).
                    id*         -- Interconnect bay no as integer which need to verify. e.g. 1-6
                    lig*        -- Which lig was displayed in input box. e.g. None| ICM1
                <displayed> optional -- check displayed lig list
                    lig*        -- All optional LIG in pop-up combo menu.

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}
        <encgroups>
            <encgroup name="Reg2-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" lig="ICM1">
                        <verify id="1" lig="ICM1" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="None" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                        <displayed lig="ICM1" />
                        <displayed lig="ICM1-4" />
                        <displayed lig="ICM1-4-2" />
                    </switch>
                    <switch bay="1" lig="None">
                        <verify id="1" lig="None" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="None" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="1" lig="ICM1-4">
                        <verify id="1" lig="ICM1-4" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="ICM1-4" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="1" lig="ICM1-4-2">
                        <verify id="1" lig="ICM1-4-2" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="ICM1-4-2" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="2">
                        <displayed lig="ICM2" />
                        <displayed lig="ICM2-5" />
                    </switch>
                    <switch bay="3">
                        <displayed lig="ICM3" />
                        <displayed lig="ICM3-6" />
                    </switch>
                    <switch bay="4">
                        <displayed lig="ICM1" />
                        <displayed lig="ICM1-4" />
                        <displayed lig="ICM1-4-2" />
                    </switch>
                    <switch bay="5">
                        <displayed lig="ICM5" />
                        <displayed lig="ICM2-5" />
                    </switch>
                    <switch bay="6">
                        <displayed lig="ICM6" />
                        <displayed lig="ICM3-6" />
                    </switch>
                </enclosure>
            </encgroup>

    """
    logger.info("Edit Tbird Enclosure Group")
    navigate()

    not_exists = 0

    for eg in eg_obj:
        if not TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            not_exists += 1
            continue
        logger.info("After check of exists")

        TBirdCommonOperationEnclosureGroups.click_enclosure_group(eg.name)
        TBirdEditEnclosureGroups.select_actions_edit()
        TBirdEditEnclosureGroups.wait_edit_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        logger.info("Enclosure Group '%s' " % eg.name)

        if hasattr(eg, 'new_name'):
            TBirdCreateEnclosureGroups.input_enclosure_group_name(eg.new_name)

        if hasattr(eg, 'ipv4_addresses'):
            if eg.ipv4_addresses.lower() == 'use address pool':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_address_pool()
            elif eg.ipv4_addresses.lower() == 'use dhcp':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_dhcp()
            elif eg.ipv4_addresses.lower() == 'manage externally':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_manage_externally()
            else:
                ui_lib.fail_test("Unexpected ipv4_addresses attrbiute '%s'" % eg.ipv4_addresses)

        if hasattr(eg, 'enclosure'):
            enc_list_obj = eg.enclosure if isinstance(eg.enclosure, list) else [eg.enclosure]
            FusionUIBase.select_view_by_name("Interconnect Bay Configuration")

            for enc_obj in enc_list_obj:
                enc_no = enc_obj.no
                for switch_obj in enc_obj.switch:
                    switch_no = switch_obj.bay
                    TBirdCreateEnclosureGroups.make_choose_lig_input_into_viewpoint(enc_no, switch_no, timeout=8)
                    TBirdCreateEnclosureGroups.click_search_combo_box_menu(enc_no, switch_no)
                    TBirdCreateEnclosureGroups.wait_for_search_combo_menu_visible(enc_no, switch_no)

                    logger.info("Verify existing LIG can be displayed on correct bay...")
                    if hasattr(switch_obj, 'displayed'):
                        for lig_obj in switch_obj.displayed:
                            switch_lig = lig_obj.lig
                            TBirdVerifyEnclosureGroups.verify_drop_down_option_for_lig(enc_no, switch_no, switch_lig)
                        logger.info("All LIGs are found in search combo menu!")

                    if hasattr(switch_obj, 'lig'):
                        switch_lig = switch_obj.lig
                        TBirdCreateEnclosureGroups.input_select_lig(enc_no, switch_no, switch_lig, timeout=8)
                        if TBirdCreateEnclosureGroups.wait_change_lig_confirm_dialog_visible():
                            TBirdCreateEnclosureGroups.click_select_lig_button()

                        if hasattr(switch_obj, 'verify'):
                            for lig_verify in switch_obj.verify:
                                verify_no = lig_verify.id
                                verify_lig = lig_verify.lig
                                TBirdVerifyEnclosureGroups.verify_selected_lig_for_enclosure(enc_no, verify_no, verify_lig, timeout=8)
                    else:
                        TBirdCreateEnclosureGroups.click_search_combo_box_menu(enc_no, switch_no)
                        TBirdCreateEnclosureGroups.wait_for_search_combo_menu_invisible(enc_no, switch_no)

        if hasattr(eg, 'power_mode'):
            TBirdCommonOperationEnclosureGroups.select_view_by_name("Power")
            TBirdCreateEnclosureGroups.select_power_mode(eg.power_mode)
        logger.info("Before click grp create")
        TBirdEditEnclosureGroups.click_ok_button()
        TBirdEditEnclosureGroups.wait_edit_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)
        ret1, ret2 = FusionUIBase.get_error_message_from_dialog(10)
        if ret1 is True:
            logger.warn("Error message encountered, stopping test")
            logger.warn(ret2)
            ui_lib.fail_test("Editing Enclosure Group %s failed" % eg.name)
        FusionUIBase.show_activity_sidebar()
        TBirdCommonOperationEnclosureGroups.wait_activity_action_ok(eg.name, fail_if_false=True)
        FusionUIBase.show_activity_sidebar()

    return True if not not_exists else False


def validate_selection_of_LIG_conflicts_with_previously_selected_when_editing_eg(eg_obj):
    """ Validate lig panel when creating an Tbird enclosure group, used for F332, the enclosure_count must be 1

    Arguments:

      <encgroup>
          name*                 --  Name of enclosure group as a string.
          new_name              --  New name of enclosure group
          enclosure_count*      --  Enclosure count as number. 3 is max.
          ipv4_addresses*       --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
          <enclosure> optional, for select LIG for interconnect bay (can be multiple)
            no*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            <switch> required, for specifying interconnect model
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig             --  Logical interconnect group name to be selected.
                <verify> optional, for all virtual interconnect validation(can be multiple).
                    id*         -- Interconnect bay no as integer which need to verify. e.g. 1-6
                    lig*        -- Which lig was displayed in input box. e.g. None| ICM1
                <displayed> optional -- check displayed lig list
                    lig*        -- All optional LIG in pop-up combo menu.

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}
        <encgroups>
            <encgroup name="EGp0001"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1"
                            lig="ICM1"
                            change="True">
                        <verify id="1" lig="ICM1" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="None" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="4"
                            lig="ICM1-4"
                            change="False"
                            expect_msg='The logical interconnect group "%s" conflicts with an already selected logical interconnect group'>
                        <verify id="1" lig="ICM1" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="None" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                    <switch bay="4"
                            lig="ICM1-4-2"
                            change="True"
                            expect_msg='The logical interconnect group "%s" conflicts with an already selected logical interconnect group'>
                        <verify id="1" lig="ICM1-4-2" />
                        <verify id="2" lig="None" />
                        <verify id="3" lig="None" />
                        <verify id="4" lig="ICM1-4-2" />
                        <verify id="5" lig="None" />
                        <verify id="6" lig="None" />
                    </switch>
                </enclosure>
            </encgroup>
        </encgroups>

    """
    logger.info("Edit Tbird Enclosure Group")
    navigate()

    not_exists = 0

    for eg in eg_obj:
        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_not_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            not_exists += 1
            continue
        logger.info("After check of exists")

        TBirdCommonOperationEnclosureGroups.click_enclosure_group(eg.name)
        TBirdEditEnclosureGroups.select_actions_edit()
        TBirdEditEnclosureGroups.wait_edit_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        logger.info("Enclosure Group '%s' " % eg.name)

        if hasattr(eg, 'new_name'):
            TBirdCreateEnclosureGroups.input_enclosure_group_name(eg.new_name)

        if hasattr(eg, 'ipv4_addresses'):
            if eg.ipv4_addresses.lower() == 'use address pool':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_address_pool()
            elif eg.ipv4_addresses.lower() == 'use dhcp':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_dhcp()
            elif eg.ipv4_addresses.lower() == 'manage externally':
                TBirdCreateEnclosureGroups.tick_ipv4_addresses_manage_externally()
            else:
                ui_lib.fail_test("Unexpected ipv4_addresses attrbiute '%s'" % eg.ipv4_addresses)

        if hasattr(eg, 'enclosure'):
            enc_list_obj = eg.enclosure if isinstance(eg.enclosure, list) else [eg.enclosure]
            FusionUIBase.select_view_by_name("Interconnect Bay Configuration")
            for enc_obj in enc_list_obj:
                enc_no = enc_obj.no
                for switch_obj in enc_obj.switch:
                    switch_no = switch_obj.bay
                    TBirdCreateEnclosureGroups.make_choose_lig_input_into_viewpoint(enc_no, switch_no,
                                                                                    timeout=8)
                    TBirdCreateEnclosureGroups.click_search_combo_box_menu(enc_no, switch_no)
                    TBirdCreateEnclosureGroups.wait_for_search_combo_menu_visible(enc_no, switch_no)
                    switch_lig = switch_obj.lig
                    TBirdCreateEnclosureGroups.input_select_lig(enc_no, switch_no, switch_lig, timeout=8)
                    if TBirdCreateEnclosureGroups.wait_change_lig_confirm_dialog_visible():
                        msg = TBirdCreateEnclosureGroups.get_eg_change_confirm_prompt(switch_lig)
                        expect_msg = switch_obj.expect_msg % switch_lig
                        if getattr(switch_obj, "change", None).lower() == "true":
                            TBirdCreateEnclosureGroups.click_select_lig_button()
                        else:
                            TBirdCreateEnclosureGroups.click_cancel_select_lig_button()
                        if hasattr(switch_obj, "expect_msg"):
                            if expect_msg in msg:
                                logger.info("The prompt message contaions expect message.")
                            else:
                                ui_lib.fail_test("The warning message is not correct, fail the test.")
                    for lig_verify in switch_obj.verify:
                        verify_no = lig_verify.id
                        verify_lig = lig_verify.lig
                        TBirdVerifyEnclosureGroups.verify_selected_lig_for_enclosure(enc_no, verify_no, verify_lig, timeout=8)

        TBirdCreateEnclosureGroups.click_cancel_button()
        TBirdCreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)
        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.info("Enclosure Group '%s' validate successfully" % eg.name)
        else:
            ui_lib.fail_test("Validating Enclosure Group %s failed" % eg.name)

    return True if not not_exists else False


def create_enclosure_groups_by_create_and_createplus_button(eg_obj):
    logger.info("Navigate to Enclosure Groups page")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)
    """ Create Enclosure Group and Verify  """

    logger.info("Before check")

    create_order = 0

    for eg in eg_obj:
        if C7000CommonOperationEnclosureGroups.verify_enclosure_group_not_exist(eg.name, 10, False) is False:
            logger.warn("Enclosure group '%s' already exists" % eg.name)
            continue

        logger.info("After check of exists")
        C7000CreateEnclosureGroups.click_create_enclosure_group_button()
        C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_shown(PerfConstants.DEFAULT_SYNC_TIME)
        logger.info("Enclosure Group '%s' " % eg.name)
        if eg.name == "" or eg.name.lower() == "empty":
            ui_lib.fail_test("EG name is not specified")
        else:
            C7000CreateEnclosureGroups.input_enclosure_group_name(eg.name)

        if not hasattr(eg, "switch"):
            ui_lib.fail_test("no switch child elements in <encgroup> node(%s)" % eg.name)

        for switch_obj in eg.switch:
            C7000CreateEnclosureGroups.input_select_logical_interconnect_group(switch_obj.bay, switch_obj.lig)
        if hasattr(eg, "script"):
            C7000CreateEnclosureGroups.input_configuration_script(eg.script)

        logger.info("Before click grp create")
        create_order += 1

        """Test Create Button """
        if create_order == 1:
            C7000CreateEnclosureGroups.click_create_button()
            C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(PerfConstants.DEFAULT_SYNC_TIME)
            if C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
                logger.info("Enclosure Group '%s' created successfully" % eg.name)
            else:
                ui_lib.fail_test("Creating Enclosure Group %s failed" % eg.name)

        """Test Create+ Button """
        if create_order == 2:
            C7000CreateEnclosureGroups.click_create_plus_button()
            C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 30)
            if C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
                logger.info("Enclosure Group '%s' created successfully" % eg.name)
            else:
                ui_lib.fail_test("Creating enclosure group '%s' failed" % eg.name)
            C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_shown()

        """Test Cancel Button"""
        if create_order == 3:
            time.sleep(5)
            cancel_retry_time = 0
            while cancel_retry_time < 3:
                C7000CreateEnclosureGroups.click_cancel_button(5)
                if C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(5, False):
                    break
                cancel_retry_time += 1

            C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(10)
            if C7000CommonOperationEnclosureGroups.verify_enclosure_group_not_exist(eg.name, 10, False):
                logger.info("Enclosure group '%s' has not been created as expected - clicking 'Cancel' button should not create enclosure group" % eg.name)
            else:
                ui_lib.fail_test("Enclosure group '%s' has been created UNEXPECTEDLY by click Cancel" % eg.name)

    verify_order = 1

    for eg in eg_obj:
        """This EG has not be created, skip verify"""
        if verify_order == 3:
            logger.info("This EG has not be created, skip verify")
            break

        C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, True)
        C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)

        for switch_obj in eg.switch:
            C7000CommonOperationEnclosureGroups.verify_enclosure_group_logical_interconnect_group(switch_obj.bay, switch_obj.lig, 10)
        if hasattr(eg, "script"):
            C7000CommonOperationEnclosureGroups.verify_enclosure_group_configuration_script(eg.script, 10)
        verify_order += 1
    return True


def validate_cannot_create_enclosure_group_using_existing_name(eg_obj):
    """ Create an Enclosure Group which already exists
        Then enter a new name to create
        Finally,delete the Enclosure Group
    """

    logger.info("trying to create Enclosure Group using an existing EG's name, and check if the expected error message occurs ...")
    logger.info("navigate to Enclosure Groups page")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS, time_for_loading=3)
    C7000CreateEnclosureGroups.click_create_enclosure_group_button()
    C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_shown(10)

    for eg in eg_obj:
        if eg.name == "" or eg.name.lower() == "empty":
            ui_lib.fail_test("enclosure group name is not defined")
        else:
            C7000CreateEnclosureGroups.input_enclosure_group_name(eg.name)

        if not hasattr(eg, "switch"):
            ui_lib.fail_test("no switch child elements in <encgroups> node(%s)" % eg.name)

        for switch_obj in eg.switch:
            C7000CreateEnclosureGroups.input_select_logical_interconnect_group(switch_obj.bay, switch_obj.lig)
        if hasattr(eg, "script"):
            C7000CreateEnclosureGroups.input_configuration_script(eg.script)

        C7000CreateEnclosureGroups.click_create_button()

        if C7000CreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear(timeout=10, fail_if_false=False) is False:
            status, msg = FusionUIBase.get_error_message_from_dialog()
            if status is True and (("Unable to create enclosure group" and
                                    "The group name specified is already used by another enclosure group" and
                                    "Enter a unique enclosure group name") in msg):
                logger.info("successfully verified the expected error message, result of verifying parameter is '%s'" % msg)
                C7000CreateEnclosureGroups.click_cancel_button()
                return True
            else:
                logger.warn("failed to get the expected error message, and unexpected error message found: '%s'" % msg)
                C7000CreateEnclosureGroups.click_cancel_button()
                return False
        else:
            logger.warn("failed to get the expected error message: "
                        "'Unable to create enclosure group', "
                        "'The group name specified is already used by another enclosure group', "
                        "and 'Enter a unique enclosure group name', "
                        "when using '%s' as the existing name to create enclosure group")
            return False


def validate_cannot_delete_enclosure_group_used_by_enclosure(eg_obj):

    for eg in eg_obj:
        logger.info("Navigate to EG page")
        FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)
        C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, True)
        C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
        DeleteEnclosureGroups.select_actions_delete()
        if DeleteEnclosureGroups.verify_enclosure_group_cannot_delete(5, False) and eg.enclosurerelated.lower() != "none":
            DeleteEnclosureGroups.click_close_button()
            logger.info("Enclosure group '%s' is used by something and can not be deleted - as expected." % eg.name)

        return True


def validate_cannot_update_configuration_script_with_command_in_blacklist(eg_obj):
    """
        Edit enclosure group to modify configuration script, using any command in blacklist
        Delete command in blacklist
        Check on the enclosures, configured with this EG

    """
    logger.info("Navigate to EG page")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)
    logger.info("Ready to Modify EG Configuration script ")

    for eg in eg_obj:
        if C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False) is False:
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            return False
        else:
            C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
            # wait target enclosure group get focus
            logger.info("Wait for enclosure group %s to be selected." % eg.name)

            retry_times = 0
            while retry_times < 3:
                if C7000CommonOperationEnclosureGroups.verify_enclosure_group_seleted(eg.name, 5, False) is False:
                    logger.warn("Failed to select enclosure group %s, re-trying" % eg.name)
                    retry_times += 1
                    C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select enclosure group %s." % eg.name)
                return False

            C7000EditEnclosureGroups.select_actions_edit()
            C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_shown()
            FusionUIBase.select_view_by_name('Configuration Script')

            for script_obj in eg.script:

                C7000EditEnclosureGroups.input_configuration_script(script_obj.script)

                C7000EditEnclosureGroups.click_ok_button()
                status, msg = FusionUIBase.get_error_message_from_dialog(10)

                if status is True and (("Unable to edit enclosure group" and "The configuration script contains disallowed commands") in msg):
                    logger.info("cannot update Enclosure Group's 'Configuration Script' with a command in blacklist:[%s] - as expected" % eg.script)
                else:
                    logger.warn("failed to get the expected error message when Edit Enclosure Group to update 'Configuration Script' with a command in blacklist")
                    return False
            C7000EditEnclosureGroups.input_configuration_script("config script")
            C7000EditEnclosureGroups.click_ok_button()
            C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_disappear()

    return True


def modify_enclosure_group_name(eg_obj):
    for eg in eg_obj:
        logger.info("Navigate to EG page")
        FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)
        C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, True)
        C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
        C7000CommonOperationEnclosureGroups.verify_enclosure_group_configuration_script(eg.script, 10)
        C7000EditEnclosureGroups.select_actions_edit()
        C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_shown()
        if hasattr(eg, "newname"):
            C7000EditEnclosureGroups.input_enclosure_group_name(eg.newname)
        C7000EditEnclosureGroups.click_ok_button()
        C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_disappear()
        C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.newname, 10)

    return True


def modify_enclosure_group_new_configuration_script(eg_obj):
    logger.info("Navigate to EG page")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS)
    logger.info("Ready to Modify EG Configuration script ")

    for eg in eg_obj:
        if C7000CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False) is False:
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            return False
        else:
            C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
            # wait target enclosure group get focus
            logger.info("Wait for enclosure group %s to be selected." % eg.name)

            retry_times = 0
            while retry_times < 3:
                if C7000CommonOperationEnclosureGroups.verify_enclosure_group_seleted(eg.name, 5, False) is False:
                    logger.warn("Failed to select enclosure group %s, re-trying" % eg.name)
                    retry_times += 1
                    C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
                    continue
                break

            if retry_times >= 3:
                logger.warn("Failed to select enclosure group %s." % eg.name)
                return False

            C7000EditEnclosureGroups.select_actions_edit()
            C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_shown()
            FusionUIBase.select_view_by_name('Configuration Script')
            C7000EditEnclosureGroups.input_configuration_script(eg.script)
            C7000EditEnclosureGroups.click_ok_button()
            C7000EditEnclosureGroups.wait_edit_enclosure_group_dialog_disappear(10)
            C7000CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
            C7000CommonOperationEnclosureGroups.verify_enclosure_group_configuration_script(eg.script, 10)
    return True


def open_create_enclosure_group_dialog():
    navigate()
    logger.info("Open Create enclosure group dialog")
    if not CreateEnclosureGroups.is_create_enclosure_group_dialog_open():
        CreateEnclosureGroups.click_create_enclosure_group_button()
        CreateEnclosureGroups.wait_create_enclosure_group_dialog_shown()

    return True


def close_create_enclosure_group_dialog():
    logger.info("Close Create enclosure group dialog")
    if CreateEnclosureGroups.is_create_enclosure_group_dialog_open():
        CreateEnclosureGroups.click_cancel_button()
        CreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear()

    return True


def close_edit_enclosure_group_dialog():
    navigate()
    logger.info("Close Edit enclosure group dialog")
    if CreateEnclosureGroups.is_edit_enclosure_group_dialog_open():
        C7000EditEnclosureGroups.click_cancel_button()
        CreateEnclosureGroups.wait_create_enclosure_group_dialog_disappear()

    return True


def select_panel_selector_lig():
    logger.info("Validating panel selector [Interconnect bay configuration]")
    if not CommonOperationEnclosureGroups.is_panel_selector_active():
        CommonOperationEnclosureGroups.open_panel_selector()

    CommonOperationEnclosureGroups.click_panel_selector_lig()

    if CommonOperationEnclosureGroups.is_panel_lig_active():
        logger.warn("Interconnect bay configuration panel is not active")
        return False

    logger.info("Interconnect bay configuration panel is active")

    return True


def select_panel_selector_general():
    logger.info("Validating panel selector [General]")
    if not CommonOperationEnclosureGroups.is_panel_selector_active():
        CommonOperationEnclosureGroups.open_panel_selector()

    CommonOperationEnclosureGroups.click_panel_selector_general()

    if CommonOperationEnclosureGroups.is_panel_general_active():
        logger.warn("General panel is not active")
        return False

    logger.info("General panel is active")

    return True


def select_panel_selector_configscript():
    logger.info("Validating panel selector [Configuration script]")
    if not CommonOperationEnclosureGroups.is_panel_selector_active():
        CommonOperationEnclosureGroups.open_panel_selector()

    C7000CommonOperationEnclosureGroups.click_panel_selector_configscript()

    if C7000CommonOperationEnclosureGroups.is_panel_configscript_active():
        logger.warn("Configuration script panel is not active")
        return False

    logger.warn("Configuration script panel is active")

    return True


def validate_panel_selector_in_create_enclosure_group_dialog():
    open_create_enclosure_group_dialog()
    logger.info("Validating panel selector in Create enclosure group dialog")
    validation_result = True

    # Validate "Interconnect bay configuration" panel should be active after selected
    validation_result = select_panel_selector_lig()

    # Validate "General" panel should be active after selected
    validation_result = select_panel_selector_general()

    # Validate "Configuration script" panel should be active after selected
    validation_result = select_panel_selector_configscript()

    close_create_enclosure_group_dialog()

    return validation_result


def delete_all_enclosure_groups():
    selenium2lib = ui_lib.get_s2l()
    if not selenium2lib._is_element_present(FusionEnclosureGroupsPage.ID_PAGE_LABEL):
        navigate()

    encgroup_list = [ui_lib.get_text(el) for el in selenium2lib._element_find(FusionEnclosureGroupsPage.ID_ENC_GROUP_LIST, False, False)]
    count = 0
    for encgroupname in encgroup_list:
        logger._log_to_console_and_log_file("Deleting Enclosure Groups: {0}".format(encgroupname))
        encgroup_obj = test_data.DataObj()
        encgroup_obj.add_property('name', encgroupname)
        eg_obj = (encgroup_obj,)
        encgroup_delete_status = delete_enclosure_group(eg_obj)

        if encgroup_delete_status:
            logger._log_to_console_and_log_file("'{0}' enclosure group is deleted Successfully".format(encgroupname))
            count += 1
        else:
            logger.warn("Failed to delete enclosure group: {0}".format(encgroupname))

    if count == len(encgroup_list):
        logger._log_to_console_and_log_file("All enclosure group deleted successfully from appliance")
        return True
    else:
        logger.warn("Failed to delete '{0}' enclosure group from appliance".format(len(encgroup_list) - count))
        return False


def verify_enclosuregroup(*eg_obj):
    '''
    Function to verify EG creation or Update
    Returns true if verification is successful without errors else returns the error string
    '''

    logger._log_to_console_and_log_file("\n*** Verifying Enclosure Group ***")
    error = 0
    error_string = ''

    if not ui_lib.wait_for_element(FusionEnclosureGroupsPage.ID_PAGE_LABEL):
        navigate()

    if isinstance(eg_obj, test_data.DataObj):
        eg_obj = [eg_obj]
    elif isinstance(eg_obj, tuple):
        eg_obj = list(eg_obj[0])

    # iterate through every EG object and verify
    for encgrp in eg_obj:
        ui_lib.refresh_browser(FusionEnclosureGroupsPage.ID_PAGE_LABEL, FusionEnclosureGroupsPage.WAIT_TIME)
        ui_lib.refresh_browser(FusionEnclosureGroupsPage.ID_PAGE_LABEL, FusionEnclosureGroupsPage.WAIT_TIME)
        encgpname = ''
        # check if the dataobj has newname attribute , if yes check if the EG with new name is present and Verify it else Verify the EG in name attribute
        if hasattr(encgrp, 'newname'):
            # if newname is not seen default to name
            if ui_lib.wait_for_element_visible(FusionEnclosureGroupsPage.XPATH_EG_NAME % encgrp.newname):
                encgpname = encgrp.newname
            else:
                encgpname = encgrp.name
        else:
            encgpname = encgrp.name

        logger._log_to_console_and_log_file("\nVerifying Enclosure Group : '{}'".format(encgpname))
        if not ui_lib.wait_for_element_visible(FusionEnclosureGroupsPage.XPATH_EG_NAME % encgpname):
            logger._warn("Enclosure group '{}' does not exist".format(encgpname))
            continue
        encGroup = FusionEnclosureGroupsPage.XPATH_EG_NAME % encgpname
        logger._log_to_console_and_log_file("Enclosure group '{}' Seen in the table".format(encgpname))
        ui_lib.wait_for_element_and_click(encGroup)

        ligs_list = []
        if hasattr(encgrp, 'lig'):
            ligs_list = encgrp.lig
        else:
            logger._log_to_console_and_log_file("-- LIGs not Specified")
        # if enclosure type is c7000
        if encgrp.type.lower() == 'c7000':
            # check LIG
            if ligs_list:
                # goto IC bay Config section
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.ID_EG_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.LINK_EG_IC_BAY_CONFIGURATION, FusionEnclosureGroupsPage.WAIT_TIME)

                for lig in ligs_list:
                    # check if the lig given as input for the bay is visible in UI
                    if ui_lib.wait_for_element_visible(FusionEnclosureGroupsPage.XPATH_EG_C7000_IC_BAY_LIG % (lig.bay, lig.name), FusionEnclosureGroupsPage.WAIT_TIME):
                        logger._log_to_console_and_log_file("LIG for Bay {} set correctly to {}".format(lig.bay, lig.name))
                    else:
                        logger._warn("LIG for Bay {} NOT set correctly to {}".format(lig.bay, lig.name))
                        error += 1
                        error_string += "LIG for Bay {} NOT set correctly to {}\t".format(lig.bay, lig.name)

            # check config script
            if hasattr(encgrp, 'configurationscript'):
                # goto Config script section
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.ID_EG_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.LINK_EG_GENERAL, FusionEnclosureGroupsPage.WAIT_TIME)

                config_script_ui = ui_lib.get_text(FusionEnclosureGroupsPage.XPATH_EG_CONFIGURATION_SCRIPT, FusionEnclosureGroupsPage.WAIT_TIME)
                if encgrp.configurationscript.lower() in config_script_ui.lower():
                    logger._log_to_console_and_log_file("Configuration Script Set Correctly to : '{}'".format(config_script_ui))
                else:
                    logger._warn("Configuration Script not set correctly. Expected : '{}' , As seen in UI : '{}'".format(encgrp.configurationscript, config_script_ui))
                    error += 1
                    error_string += "Configuration Script not set correctly. Expected : '{}' , As seen in UI : '{}'\t".format(encgrp.configurationscript, config_script_ui)
            else:
                logger._log_to_console_and_log_file("-- Configuration Script not Specified")

        elif encgrp.type.lower() == 'tbird':

            # check enclosure count is same as no.of enclosures in EG
            index_count = 0
            for count in range(1, int(encgrp.enccount) + 1):
                if ui_lib.wait_for_element_visible(FusionEnclosureGroupsPage.XPATH_EG_TBIRD_ENCLOSURE_ICBAYS % (count)):
                    index_count += 1
            if index_count == int(encgrp.enccount):
                logger._log_to_console_and_log_file("No of enclosure Index displayed is same as No.of Enclosure count {}".format(encgrp.enccount))
            else:
                logger._warn("No of enclosure Index displayed is '{}' which is NOT same as No.of Enclosure count {}".format(index_count, encgrp.enccount))
                error += 1
                error_string += "No of enclosure Index displayed is '{}' which is NOT same as No.of Enclosure count {}\t".format(index_count, encgrp.enccount)

            # check LIGs
            if ligs_list:
                # goto IC bay COnfig section
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.ID_EG_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.LINK_EG_IC_BAY_CONFIGURATION, FusionEnclosureGroupsPage.WAIT_TIME)

                # check LIG for each enclosure
                for count in range(1, int(encgrp.enccount) + 1):
                    # check if the enclosure is visible
                    if ui_lib.wait_for_element_visible(FusionEnclosureGroupsPage.XPATH_EG_TBIRD_ENCLOSURE % count):
                        logger._log_to_console_and_log_file("\nChecking The LIGs of Enclosure {}".format(count))

                        # check the following
                        # LIG of bay 1 is same as that of Bay 4 which are same as BaySet 1 mentioned in input
                        # LIG of bay 2 is same as that of Bay 5 which are same as BaySet 2 mentioned in input
                        # LIG of bay 3 is same as that of Bay 6 which are same as BaySet 3 mentioned in input
                        for lig in ligs_list:
                            ic_lig_bayset_member1 = FusionEnclosureGroupsPage.XPATH_EG_TBIRD_ENCLOSURE_IC_BAY_LIG % (count, count, lig.bay, lig.name)
                            # check if the bay set members have the LIG same as input
                            if ui_lib.wait_for_element_visible(ic_lig_bayset_member1):
                                logger._log_to_console_and_log_file("LIG for Bay {} set correctly to {}".format(lig.bay, lig.name))
                            else:
                                logger._warn("LIG for Bay {} NOT set correctly to {}".format(lig.bay, lig.name))
                                error += 1
                                error_string += "LIG for Bay {} NOT set correctly to {}\t".format(lig.bay, lig.name)

                            if FusionEnclosureGroupsPage.LIG_REDUNDANCY[lig.redundancy.upper()].lower() == "redundant" or FusionEnclosureGroupsPage.LIG_REDUNDANCY[lig.redundancy.upper()].lower() == "highlyavailable":
                                ic_lig_bayset_member2 = FusionEnclosureGroupsPage.XPATH_EG_TBIRD_ENCLOSURE_IC_BAY_LIG % (count, count, str(int(lig.bayset) + FusionEnclosureGroupsPage.BAY_SET_MEMBER_INCREMENT), lig.name)
                                # check if the bay set members have the LIG same as input
                                if ui_lib.wait_for_element_visible(ic_lig_bayset_member2):
                                    logger._log_to_console_and_log_file("LIG for Bay {} set correctly to {}".format(str(int(lig.bayset) + FusionEnclosureGroupsPage.BAY_SET_MEMBER_INCREMENT), lig.name))
                                else:
                                    logger._warn("LIG for Bay {} NOT set correctly to {}".format(str(int(lig.bayset) + FusionEnclosureGroupsPage.BAY_SET_MEMBER_INCREMENT), lig.name))
                                    error += 1
                                    error_string += "LIG for Bay {} NOT set correctly to {}\t".format(str(int(lig.bayset) + FusionEnclosureGroupsPage.BAY_SET_MEMBER_INCREMENT), lig.name)

                                # Check if both the LIGs are same
                                ic_bayset_member1_ligname = ui_lib.get_text(FusionEnclosureGroupsPage.XPATH_EG_TBIRD_ENCLOSURE_IC_BAY_LIG_NAME % (count, count, lig.bayset))
                                ic_bayset_member2_ligname = ui_lib.get_text(FusionEnclosureGroupsPage.XPATH_EG_TBIRD_ENCLOSURE_IC_BAY_LIG_NAME % (count, count, str(int(lig.bayset) + FusionEnclosureGroupsPage.BAY_SET_MEMBER_INCREMENT)))

                                if ic_bayset_member1_ligname.lower() == ic_bayset_member2_ligname.lower():
                                    logger._log_to_console_and_log_file("BaySet {} members have same LIG".format(lig.bayset))
                                else:
                                    logger._warn("BaySet {} members DO NOT have same LIG, while they should!!".format(lig.bayset))
                                    error += 1
                                    error_string += "BaySet {} members DO NOT have same LIG, while they should!!\t".format(lig.bayset)

            # Check IP addresses
            if hasattr(encgrp, 'ipv4addresses'):
                # goto General section
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.ID_EG_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.LINK_EG_GENERAL, FusionEnclosureGroupsPage.WAIT_TIME)
                ipv4_addresses_mode = ui_lib.get_text(FusionEnclosureGroupsPage.XPATH_EG_IPV4_ADDRESSES, FusionEnclosureGroupsPage.WAIT_TIME)
                if encgrp.ipv4addresses.lower().replace(" ", "") in ipv4_addresses_mode.lower().replace(" ", ""):
                    logger._log_to_console_and_log_file("Ipv4 Addresses Mode set correctly to : '{}'".format(ipv4_addresses_mode))

                    # if pool verify that all the ranges added are seen
                    if encgrp.ipv4addresses.lower() == 'pool':
                        ipaddresses_ranges = encgrp.ipv4addresspool
                        for iprange in ipaddresses_ranges:
                            if ui_lib.wait_for_element_visible(FusionEnclosureGroupsPage.XPATH_EG_IPV4_ADDRESSES_RANGES_DISPLAYED % iprange.rangename, FusionEnclosureGroupsPage.WAIT_TIME):
                                # check if the range is set for removal
                                if hasattr(iprange, "action"):
                                    if str(iprange.action).lower() == "remove":
                                        logger._warn("The IPV4 range '{}' is still seen in UI , while it should have gotten removed".format(iprange.rangename))
                                        error += 1
                                        error_string += "The IPV4 range '{}' is still seen in UI , while it should have gotten removed".format(iprange.rangename)
                                logger._log_to_console_and_log_file("Ipv4 Range '{}' has been added successfully and is seen in UI".format(iprange.rangename))

                                # verify that the ip range is displayed just once
                                range_elements = ui_lib.get_s2l()._current_browser().find_elements_by_xpath("//*[@id='cic-encgrp-more-details-ipv4AddressPools-table']//*[translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')=translate('%s','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')]" % iprange.rangename)

                                if len(range_elements) > 1:
                                    logger._warn("The IP range '{}' is displayed {} times in the UI.IT should be displayed just once.".format(iprange.rangename, len(range_elements)))
                                    error += 1
                                    error_string += "The IP range '{}' is displayed {} times in the UI.IT should be displayed just once.".format(iprange.rangename, len(range_elements))
                                else:
                                    logger._log_to_console_and_log_file("IP range '{}' is displayed just once as expected".format(iprange.rangename))
                            else:
                                # check if the range is set for removal
                                if hasattr(iprange, "action"):
                                    if str(iprange.action).lower() == "remove":
                                        logger._log_to_console_and_log_file("The IPV4 range '{}' is not seen in UI.It has been successfully removed".format(iprange.rangename))
                                        continue
                                error += 1
                                logger._warn("Ipv4 Range '{}' has NOT been added and is NOT seen in UI".format(iprange.rangename))
                                error_string += "Ipv4 Range '{}' has NOT been added and is NOT seen in UI\t".format(iprange.rangename)

                else:
                    logger._warn("Ipv4 Addresses Mode not set correctly. Expected : '{}' , As seen in UI : '{}'".format(encgrp.ipv4addresses, ipv4_addresses_mode))
                    error += 1
                    error_string += "Ipv4 Addresses Mode not set correctly. Expected : '{}' , As seen in UI : '{}'\t".format(encgrp.ipv4addresses, ipv4_addresses_mode)

            else:
                logger._log_to_console_and_log_file("-- IPV4 Addresses not Specified")

            # check power mode
            if hasattr(encgrp, 'powermode'):
                # goto Power section
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.ID_EG_DROPDOWN)
                ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.LINK_EG_POWER, FusionEnclosureGroupsPage.WAIT_TIME)
                power_mode_ui = ui_lib.get_text(FusionEnclosureGroupsPage.XPATH_EG_POWER_MODE, FusionEnclosureGroupsPage.WAIT_TIME)
                if encgrp.powermode.lower().replace(" ", "") in power_mode_ui.lower().replace(" ", ""):
                    logger._log_to_console_and_log_file("Power Mode Set Correctly to : '{}'".format(power_mode_ui))
                else:
                    logger._warn("Power Mode not set correctly. Expected : '{}' , As seen in UI : '{}'".format(encgrp.powermode, power_mode_ui))
                    error += 1
                    error_string += "Power Mode not set correctly. Expected : '{}' , As seen in UI : '{}'\t".format(encgrp.powermode, power_mode_ui)
            else:
                logger._log_to_console_and_log_file("-- Power Mode not Specified")
        else:
            logger._warn("Invalid Enclosure Type . Should either be 'C7000' or 'TBird'")
            # clicking cancel
            ui_lib.wait_for_element_and_click(FusionEnclosureGroupsPage.ID_BTN_ENCLOSURE_GROUP_CANCEL, 10)
            continue

    if error > 0:
        return error_string
    else:
        return True


def validate_privilege_against_delete_enclosure_group(eg_obj):
    """ Validate user privilege for Delete Enclosure Group    """

    logger.info("Validate user privilege for Delete Enclosure Group")

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS, time_for_loading=5)
    failed_times = 0
    error_string = ''

    for encgrp in eg_obj:
        if not CommonOperationEnclosureGroups.verify_enclosure_group_exist(encgrp.name, 10, False):
            logger.warn("Enclosure group '%s' does not exist" % encgrp.name)
            failed_times += 1
            continue
        else:
            CommonOperationEnclosureGroups.click_enclosure_group(encgrp.name)
            # wait target enclosure group get focus
            logger.info("Wait for enclosure group %s to be selected." % encgrp.name)

            if CommonOperationEnclosureGroups.verify_enclosure_group_seleted(encgrp.name, 5, False) is False:
                failed_times += 1
                logger.warn("Failed to select enclosure group %s" % encgrp.name)
                continue

            # check if user has privilege to click on Edit buttion
            if not TBirdVerifyEnclosureGroups.verify_action_button_exists(10, False):
                raise AssertionError("User does not have privilege to click on Action button or Action button is not visible.")

            # check if user is able to visible edit option
            CommonOperationEnclosureGroups.click_actions_button(10, False)
            if not TBirdVerifyEnclosureGroups.verify_delete_button_exists(10, False):
                raise AssertionError("User does not have privilege to click on Delete button or Delete button is not visible to the user.")

    if failed_times > 0:
        raise AssertionError("Enclosure group does not exist or failed to select")
    else:
        return True


def delete_enclosure_group_ifnot_capture_errors(eg_obj):
    """ Delete Enclosure Group, if deletion fails,
        capture and log error messages.
    """

    logger.info("Delete Enclosure Group with more validations")

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS, time_for_loading=5)
    failed_times = 0
    error_msg = " "
    error_confirm_msg = " "
    error_string = " "

    for eg in eg_obj:
        if not CommonOperationEnclosureGroups.verify_enclosure_group_exist(eg.name, 10, False):
            logger.warn("Enclosure group '%s' does not exist" % eg.name)
            failed_times += 1
            continue
        else:
            CommonOperationEnclosureGroups.click_enclosure_group(eg.name)
            # wait target enclosure group get focus
            logger.info("Wait for enclosure group %s to be selected." % eg.name)

            if CommonOperationEnclosureGroups.verify_enclosure_group_seleted(eg.name, 5, False) is False:
                logger.warn("Failed to select enclosure group %s" % eg.name)
                failed_times += 1
                continue

            DeleteEnclosureGroups.select_actions_delete()
            if DeleteEnclosureGroups.verify_enclosure_group_cannot_delete(5, False):
                error_msg = DeleteEnclosureGroups.get_delete_error_text(10, False)
                error_confirm_msg = DeleteEnclosureGroups.get_delete_error_message_confirm_details(10, False)
                error_string += error_msg + "\n"
                error_string += error_confirm_msg + "\t"
                failed_times += 1
                logger.warn("Failed to delete enclosure group from appliance. Enclosure group '%s' is %s" % (eg.name, error_confirm_msg))
                DeleteEnclosureGroups.click_close_button()
                DeleteEnclosureGroups.wait_delete_error_dialog_disappears(10, False)
                continue
            DeleteEnclosureGroups.wait_delete_dialog_shown()
            DeleteEnclosureGroups.click_yes_delete_button()
            DeleteEnclosureGroups.wait_delete_dialog_disappear()

            if DeleteEnclosureGroups.wait_enclosure_group_show_not_found(eg.name, 10, False):
                logger.info("Enclosure Group '%s' is deleted successfully" % eg.name)
                # in order to prevent from UI racing issue.
                BuiltIn().sleep(3)
            else:
                BuiltIn().fail("Not able to delete Enclosure Group %s" % eg.name)

    if failed_times > 0:
        if (len(error_string) > 0):
            raise AssertionError(error_string)
        else:
            # Error occured but there is no error text, hence sending False to the script
            return False
    else:
        return True


def validate_privilege_against_edit_enclosure_group(eg_obj):
    """ Validate user privilege for Edit Enclosure Group    """

    logger.info("Validate user privilege for Edit Enclosure Group")

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS, time_for_loading=5)
    failed_times = 0
    error_string = ''

    for encgrp in eg_obj:
        msg = ""
        if not CommonOperationEnclosureGroups.verify_enclosure_group_exist(encgrp.name, 10, False):
            logger.warn("Enclosure group '%s' does not exist" % encgrp.name)
            failed_times += 1
            continue
        else:
            CommonOperationEnclosureGroups.click_enclosure_group(encgrp.name)
            # wait target enclosure group get focus
            logger.info("Wait for enclosure group %s to be selected." % encgrp.name)

            if CommonOperationEnclosureGroups.verify_enclosure_group_seleted(encgrp.name, 5, False) is False:
                failed_times += 1
                logger.warn("Failed to select enclosure group %s" % encgrp.name)
                continue

            # check if user has privilege to click on Edit buttion
            if not TBirdVerifyEnclosureGroups.verify_action_button_exists(10, False):
                raise AssertionError("User does not have privilege to click on Action button or Action button is not visible.")

            # check if user is able to visible edit option
            CommonOperationEnclosureGroups.click_actions_button(10, False)
            if not TBirdVerifyEnclosureGroups.verify_edit_button_exists(10, False):
                msg = TBirdCommonOperationEnclosureGroups.get_message_on_action_button(15, False)
                raise AssertionError("User does not have privilege to click on Edit button or Edit button is not visible to the user.msg {}".format(msg))
            else:
                logger.info("Edit button exists")
    if failed_times > 0:
        raise AssertionError("Enclosure group does not exist or failed to select")
    else:
        return True


def edit_tbird_enclosure_group_ifnot_capture_errors(eg_obj):
    """ Edit a enclosure group for Tbird enclosure
asdads
    Arguments:
      <encgroup>
          name*                 --  Name of enclosure group as a string.
          new_name              --  New name of enclosure group
          ipv4_addresses       --  IPv4 addresses mode. Possible value: Use address pool|Use DHCP|Manage externally
          power_mode            --  Power mode for enclosure group. Possible value: Redundant power feed|Redundant power supply
          <enclosure> optional, for select LIG for interconnect bay (can be multiple)
            no*                 --  Whether to create new logical interconnect group or using existing LIG. Possible value: true|false.
            <switch> required, for specifying interconnect model
                bay*            --  Interconnect bay no as integer. e.g. 1
                lig             --  Logical interconnect group name to be selected.

    * Required Arguments

    Example:
        data/encgroup -> @{TestData.encgroups}
        <encgroups>
            <encgroup name = "eg1" new_name = "eg11"  ipv4_addresses = 'use address pool'>
                <ipv4addresspool name = "test1"  action = "remove"  />
                <ipv4addresspool name = "test"  action = "add"  />
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_OVAEncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" lig="LIG_OVAEncICM" />
                </enclosure>
            </encgroup>
            <encgroup name="Reg2-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_Reg2EncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" />
                </enclosure>
            </encgroup>
            <encgroup name="Reg1-EG"
                      enclosure_count="1"
                      ipv4_addresses="Manage externally"
                      power_mode="Redundant power feed">
                <enclosure no="1">
                    <switch bay="1" />
                    <switch bay="2" />
                    <switch bay="3" lig="LIG_Reg1EncICM" />
                    <switch bay="4" />
                    <switch bay="5" />
                    <switch bay="6" />
                </enclosure>
            </encgroup>
        </encgroups>
    """

    logger.info("Edit Tbird Enclosure Group with more validations")
    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS, time_for_loading=5)
    logger.info("Before check")
    failed_times = 0
    error_msg_list = []

    for enclosuregroup in eg_obj:
        errors_on_form = []
        if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_not_exist(enclosuregroup.name, 5, False):
            logger.warn("Enclosure group '%s' does not exist" % enclosuregroup.name)
            failed_times += 1
            continue
        else:
            logger.info("After check of exists")
            TBirdCommonOperationEnclosureGroups.click_enclosure_group(enclosuregroup.name)
            TBirdEditEnclosureGroups.select_actions_edit()
            if not TBirdEditEnclosureGroups.wait_edit_enclosure_group_dialog_shown(5, False):
                logger.warn("Edit enclosure group dialog button is not visible for %s" % enclosuregroup.name)
                failed_times += 1
                continue
            logger.info("Enclosure Group '%s' " % enclosuregroup.name)

            if hasattr(enclosuregroup, 'new_name'):
                TBirdCreateEnclosureGroups.input_enclosure_group_name(enclosuregroup.new_name)

            if hasattr(enclosuregroup, 'ipv4_addresses'):
                if enclosuregroup.ipv4_addresses.lower() == 'use address pool':
                    TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_address_pool()
                    if hasattr(enclosuregroup, 'ipv4addresspool'):
                        rangepool_obj = enclosuregroup.ipv4addresspool
                        for range in rangepool_obj:
                            if hasattr(range, 'action'):
                                logger.info(range.name)
                                if not _select_ipv4_addresses_in_use_address_pool(range.name, range.action, 15, False):
                                    failed_times += 1
                                    error_msg_list.append("Error occured while selecting the IPV4 Address Ranges for enclosure group - {}".format(enclosuregroup.name))

                elif enclosuregroup.ipv4_addresses.lower() == 'use dhcp':
                    TBirdCreateEnclosureGroups.tick_ipv4_addresses_use_dhcp()
                elif enclosuregroup.ipv4_addresses.lower() == 'manage externally':
                    TBirdCreateEnclosureGroups.tick_ipv4_addresses_manage_externally()
                else:
                    failed_times += 1
                    error_msg_list.append("Unexpected ipv4_addresses attrbiute {} for enclosure group {} -".format(enclosuregroup.ipv4_addresses, enclosuregroup.name))

            if hasattr(enclosuregroup, 'enclosure'):
                enc_list_obj = enclosuregroup.enclosure if isinstance(enclosuregroup.enclosure, list) else [enclosuregroup.enclosure]
                FusionUIBase.select_view_by_name("Interconnect Bay Configuration")

                for enc_obj in enc_list_obj:
                    for switch_obj in enc_obj.switch:
                        if hasattr(switch_obj, 'lig'):
                            TBirdCreateEnclosureGroups.make_choose_lig_input_into_viewpoint(enc_obj.no, switch_obj.bay)
                            lig_selection_errors = _select_logical_interconnect_group(enc_obj.no, switch_obj.bay, switch_obj.lig, 5, False)
                            if lig_selection_errors:
                                logger._warn("Error while selecting LIGs!! Edit might Fail\n")
                                failed_times += 1
                                error_msg_list.append("Error while selecting LIGs!! Edit might Fail {}".format(lig_selection_errors))
                            else:
                                logger.info("LIGs selected successfully")

            if hasattr(enclosuregroup, 'power_mode'):
                FusionUIBase.select_view_by_name("Power")
                TBirdCreateEnclosureGroups.select_power_mode(enclosuregroup.power_mode)

            logger.info("Before click grp create")
            errors_on_form = FusionUIBase.get_all_error_message_on_form(EditEnclosureGroupElements.ID_DIALOG_EDIT_ENCLOSURE_GROUP)
            if errors_on_form:
                failed_times += 1
                error_msg_list += errors_on_form + "\t"
                logger.info("Clicking Cancel")
                TBirdEditEnclosureGroups.click_cancel_button(5, False)
                continue
            else:
                logger.info("- No errors Seen")
                TBirdEditEnclosureGroups.click_ok_button(5, False)
                if not TBirdEditEnclosureGroups.wait_edit_enclosure_group_dialog_disappear(5, False):
                    errors_on_form = FusionUIBase.get_all_error_message_on_form(EditEnclosureGroupElements.ID_DIALOG_EDIT_ENCLOSURE_GROUP)
                    ret1, ret2 = FusionUIBase.get_error_message_from_dialog(5)
                    if errors_on_form or ret1:
                        failed_times += 1
                        if errors_on_form:
                            error_msg_list += errors_on_form
                            logger.warn("Error Seen on form during  Edit EG '{}'\n{}".format(enclosuregroup.name, errors_on_form))
                        if ret1 is True:
                            logger.warn("Error message encountered, stopping test")
                            logger.warn(ret2)
                        # if add form is still seen click cancel
                        if not TBirdEditEnclosureGroups.wait_edit_enclosure_group_dialog_disappear(5, False):
                            logger._log_to_console_and_log_file("Clicking Cancel")
                            TBirdEditEnclosureGroups.click_cancel_button(5, False)
                        continue

                FusionUIBase.show_activity_sidebar()
                if hasattr(enclosuregroup, 'new_name'):
                    if not TBirdCommonOperationEnclosureGroups.wait_activity_action_ok(enclosuregroup.new_name, fail_if_false=False):
                        failed_times += 1
                else:
                    if not TBirdCommonOperationEnclosureGroups.wait_activity_action_ok(enclosuregroup.name, fail_if_false=False):
                        failed_times += 1

                if hasattr(enclosuregroup, 'new_name'):
                    if TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(enclosuregroup.new_name, 5, False):
                        logger.info("Enclosure Group '%s' created successfully" % enclosuregroup.name)
                elif TBirdCommonOperationEnclosureGroups.verify_enclosure_group_exist(enclosuregroup.name, 5, False):
                    logger.info("Enclosure Group '%s' created successfully" % enclosuregroup.name)
                else:
                    failed_times += 1
                    logger.warn("Editing Enclosure Group %s failed" % enclosuregroup.name)

    if failed_times > 0:
        logger._warn("\n***Edit Enclosure Group completed with errors!!***\n")
        return error_msg_list
    else:

        return True


def _select_ipv4_addresses_in_use_address_pool(rangename, action, timeout=5, fail_if_false=True):
    if str(action).lower() == "add":
        if TBirdVerifyEnclosureGroups.is_range_side_message_present(fail_if_false=False):
            logger.warn("No Address Ranges have been created!!Hence cannot Add ranges")
            return False

        if TBirdVerifyEnclosureGroups.is_create_eg_add_addressrange_button_present(fail_if_false=False):
            TBirdCreateEnclosureGroups.click_add_address_range_button(timeout=timeout, fail_if_false=fail_if_false)
        elif TBirdVerifyEnclosureGroups.is_edit_eg_add_addressrange_button_present(fail_if_false=False):
            TBirdEditEnclosureGroups.click_add_address_range_button(timeout=timeout, fail_if_false=fail_if_false)
        else:
            logger.warn("'Add Address Range' Button not visible!!")
            return False

        if TBirdVerifyEnclosureGroups.is_iprange_name_present(rangename, fail_if_false=False):
            logger.info("Adding Address Range - '{}'".format(rangename))
            TBirdEditEnclosureGroups.click_on_iprange_name(rangename)
            TBirdEditEnclosureGroups.click_add_iprange_button(timeout=timeout, fail_if_false=fail_if_false)
        else:
            logger.warn("-- The specified range '{}' is not seen in the Add ranges table.".format(rangename))
            TBirdEditEnclosureGroups.click_cancel_iprange_button(timeout=timeout, fail_if_false=fail_if_false)
            return False
    elif (str(action).lower() == "remove"):
        if not TBirdVerifyEnclosureGroups.verify_range_name_present_in_table(rangename, fail_if_false=False):
            logger.warn("Ip range '{}' is not added already to remove".format(rangename))
            return False

        logger.info("Removing ip range '{}' from the EG".format(rangename))
        TBirdEditEnclosureGroups.click_remove_iprange_option(rangename, timeout=timeout, fail_if_false=fail_if_false)
        TBirdEditEnclosureGroups.click_edit_delete_iprange_confirm(timeout=timeout, fail_if_false=fail_if_false)
    else:
        logger.warn("Wrong action value - {}.Action can either be 'add' or 'remove'.".format(action))
        return False
    return True


def _select_logical_interconnect_group(enc_no, switch_no, switch_lig, timeout=5, fail_if_false=True):
    logger.info("Select logical interconnect group [ %s ] for <enclosure: %s, bay: %s> " % (switch_lig, enc_no, switch_no))
    error = 0
    error_string = ''
    match_found = ''
    TBirdCreateEnclosureGroups.input_lig(enc_no, switch_no, switch_lig, 5, False)
    # check for any suggestions displayed - at the least 'no matches' must be displayed
    if not TBirdVerifyEnclosureGroups.verify_for_search_combo_menu(enc_no, (switch_no), 5, False):
        logger.warn("No Search Suggestions displayed.Should At least display 'No matches'\n")
    else:
        match_found = TBirdCreateEnclosureGroups.get_combo_header_for_lig(enc_no, (switch_no), 5, False)
        logger.info("Search Suggestion : {} ".format(match_found))

        # check if None is displayed as an option - if yes raise warning
        if TBirdVerifyEnclosureGroups.verify_drop_down_option_for_lig(enc_no, (switch_no), 5, False):
            logger._warn("'None' is displayed as one of the search suggestions. Which is incorrect!!")
            error += 1
            error_string += "'None' is displayed as one of the search suggestions. Which is incorrect!!\t"

    if match_found:
        if match_found.lower().replace(" ", "").strip() == 'nomatches':
            logger._warn("No Matches for LIG  {} .It is not present/created. Selecting 'None' \n".format(switch_lig.strip()))
            error += 1
            error_string += "No Matches for LIG  {} .It is not present/created. Selecting 'None' \t".format(switch_lig.strip())
            # selecting none
            TBirdCreateEnclosureGroups.select_none_for_lig(enc_no, (switch_no), 5, False)

        else:
            logger.info("Match Found for LIG  {} .Selecting from the Dropdown".format(switch_lig.strip()))
            # click on the search button to list the matches - select the LIG if present else raise error and select None
            if TBirdCreateEnclosureGroups.select_lig(enc_no, switch_no, switch_lig, 5, False):
                logger.info("LIG selected : {}".format(switch_lig.strip()))
            else:
                logger._warn("\nSuggestions say : {} ,BUT LIG '{}' is not seen in the dropdown . Selecting 'None' \n".format(match_found, switch_lig.strip()))
                error += 1
                error_string += "Suggestions say : {} ,BUT LIG '{}' is not seen in the dropdown . Selecting 'None' \t".format(match_found, switch_lig.strip())
                # selecting none
                TBirdCreateEnclosureGroups.select_none_for_lig(enc_no, (switch_no), 5, False)

        # return None if no errors
    if error > 0:
        return error_string
    else:
        return None


def validate_privilege_against_create_enclosure_group(eg_obj):
    """ Validate user privileges for Create Enclosure Group    """

    logger.info("Validate user privilege for Create Enclosure Group")

    FusionUIBase.navigate_to_section(SectionType.ENCLOSURE_GROUPS, time_for_loading=5)
    failed_times = 0

    for encgrp in eg_obj:

        if CommonOperationEnclosureGroups.verify_enclosure_group_exist(encgrp.name, 10, False):
            logger.warn("Enclosure group '%s' already exists" % encgrp.name)
            failed_times += 1
            continue
        else:
            if not TBirdVerifyEnclosureGroups.verify_create_enclosure_group_button_exists(10, False):
                raise AssertionError("User does not have privilege to click on Create Enclosure Group button or Create Enclosure Group button is not visible.")
            else:
                logger.info("Create Enclosure Group Button exists")
    if failed_times > 0:
        raise AssertionError("Enclosure group exists")
    else:
        return True
