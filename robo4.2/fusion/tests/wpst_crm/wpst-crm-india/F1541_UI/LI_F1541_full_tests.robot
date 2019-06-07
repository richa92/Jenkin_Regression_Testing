*** Settings ***
Documentation      Continuous Integration Tests for RoboGalaxy dev Branch for F1212
Resource           F1541OVAConfig.txt
Force Tags         Buildup
Suite Setup         Load Test Data and Open Browser
Suite Teardown      Logout And Close All Browsers
Library             Dialogs
Library             Collections
Library             String

*** Variables ***
${ExpectedmsgDowngraddbb}        Unable to update firmware on the logical interconnect. Downgrading firmware without selecting the Force Installation option is not supported.
#${ExpectedErrorMsg1}=           Unable to update firmware for the logical interconnect SGH420HHYA-LIG_B1 as an attempt was made to downgrade the firmware without selecting the force option.
${ExpectedDowngrademsgBB2}         Retry update firmware operation with 'Force Installation' option selected.

${Permissible_IC_STATES_BeforeUpdate}=    ['configured','unmanaged']
${Permissible_IC_STATES_AfterUpdate}=    ['configured']
#${li_list} =    SGH420HHYA-LIG_B1

*** Test Cases ***
Firmware Update via Logical Interconnect level

    Set Log Level    TRACE
    Log Variables
    ${user}=    Get Data By Property    ${TestData.users}   name    Administrator
    Fusion UI Login to Appliance   ${user[0].name}

    ############# F1541 Firmware test scenarios   #####



TC01 Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using Parallel mode (downgrade G3)
    Log To Console      "###############Staging firmware update of  Hill Module when IC state is configured ############"
    [Documentation]      "RPM support FW update via LI: Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM )with force flag using Parallel mode(downgrade G3)"
    Log to Console      "F1541_UI_TC01 -->  Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using Parallel mode (downgrade G3) "
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new     @{TestData.Update_firmware_stg_RPM_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new     @{TestData.Update_firmware_active_RPM_downgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "



TC02 Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Odd/Even Mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Odd/Even Mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC10 -->  Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Odd/Even Mode without force flag (upgrade) "
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new     @{TestData.Update_firmware_stg_SCEXE_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new     @{TestData.Update_firmware_active_SCEXE_upgrade_oddeven}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "




TC03 Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using using Serial mode (downgrade G3)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "1.3.1.1 RPM support FW update via LI: Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using using Serial mode (downgrade G3)"
    Log to Console      "F1541_UI_TC02 -->  Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using using Serial mode (downgrade G3)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_downgrade_serial}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "



TC04 Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Parallel Mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Parallel Mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC11 -->  Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Parallel Mode without force flag (upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXE_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXE_upgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "



TC05 Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using Odd/Even mode (downgrade G3)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "1.3.1.1 RPM support FW update via LI: Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using Odd/Even mode (downgrade G3)"
    Log to Console      "F1541_UI_TC03 -->  Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) with force flag using Odd/Even mode (downgrade G3)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_downgrade_oddeven}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    



TC06 Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Serial Mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "1.3.1.1 RPM support FW update via LI: Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Serial Mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC12 -->  Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES) using Serial Mode without force flag (upgrade) "
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXE_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXE_upgrade_serial}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    
    


    
TC07 Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Parallel Mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "1.3.1.1 RPM support FW update via LI: Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Parallel Mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC13 -->  Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Parallel Mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

  #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_downgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "


   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_downgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    


TC08 Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Odd/Even mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "1.3.1.1 RPM support FW update via LI: Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Odd/Even mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC15 -->  Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Odd/Even mode without force flag (upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********

    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_upgrade_oddeven}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    




TC09 Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Serial Mode with force flag (upgrade Same version )
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "1.3.1.1 RPM support FW update via LI: Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Serial Mode with force flag (Same version )"
    Log to Console    "F1541_UI_TC14 -->  Verify that oneview should allow activation of already staged RPM firmware version (from RPM to RPM) using Serial Mode with force flag (Same version )"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_upgarde_sameversion}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_upgrade_sameversion}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
      


TC10 Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Parallel mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Parallel mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC07 -->  Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Parallel mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXES_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

  #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXES_downgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"


    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    


TC11 Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) using Odd/Even mode without force flag (upgrade G3)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    " RPM support FW update via LI: Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) using Odd/Even mode without force flag (upgrade G3)"
    Log to Console    "F1541_UI_TC04 -->  Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) using Odd/Even mode without force flag (upgrade G3)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_upgrade_oddeven}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    

TC12 Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Odd/Evenmode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Odd/Evenmode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC08 -->  Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Odd/Evenmode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXES_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

  #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXES_downgrade_oddeven}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"


    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    
 
TC13 Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) using Parallel mode without force flag (upgrade G3)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    " RPM support FW update via LI: Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) using Parallel mode without force flag (upgrade G3)"
    Log to Console    "F1541_UI_TC05 -->  Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM ) using Parallel mode without force flag (upgrade G3)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_upgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    
 
TC14 Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Serial mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Serial mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC09 -->  Verify that oneview should allow activation of already staged SCEXES firmware version (from RPM to SCEXES ) using Serial mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********

    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXES_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

  #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXES_downgrade_serial}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"


    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    


TC15 Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM )using serial mode without force flag (upgrade G3)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    " RPM support FW update via LI: Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM )using serial mode without force flag (upgrade G3)"
    Log to Console    "F1541_UI_TC06 -->  Verify that oneview should allow activation of already staged rpm firmware version (from scexes to RPM )using serial mode without force flag (upgrade G3)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_upgrade_serial}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    

TC16 Verify that oneview should allow activation of already staged scexes firmware version (from scexes to scexes )using parallel mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify that oneview should allow activation of already staged scexes firmware version (from scexes to scexes )using parallel mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC16 -->  Verify that oneview should allow activation of already staged scexes firmware version (from scexes to scexes )using parallel mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXES_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

  #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXES_downgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXES_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

  #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXES_downgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    
TC17 Verify that oneview should allow activation of already staged scexes firmware version (from scexes to scexes)using serial mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify that oneview should allow activation of already staged scexes firmware version (from scexes to scexes) using serial mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC17 -->  Verify that oneview should allow activation of already staged scexes firmware version (from scexes to scexes) using serial mode without force flag (upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXE_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXE_upgrade_serial}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    

TC18 Verify the FW Update operation (Stage + Activate) from scexes to scexes firmware version using parallel mode with force flag (same version)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from scexes to scexes firmware version using parallel mode with force flag (same version)"
    Log to Console    "F1541_UI_TC27 -->  Verify the FW Update operation (Stage + Activate) from scexes to scexes firmware version using parallel mode with force flag (same version)"

    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""



   #################Update firware (STAGE + ACTIVATE ) OF ALL VC MODULES #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_parallel_SCEXE}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    


TC19 Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using serial mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using serial mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC19 -->  Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using serial mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


   ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_downgrade_serial_RPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
    

TC20 Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using serial mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using serial mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC25 -->  Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using serial mode without force flag (upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}


    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""



   #################Update firware (STAGE + ACTIVATE ) OF ALL VC MODULES #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_upgrade_serial_SCEXE}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "


TC21 Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using Odd/even mode with force flag (Downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using Odd/even mode with force flag (Downgrade)"
    Log to Console      "F1541_UI_TC23 -->  Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using Odd/even mode with force flag (Downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


   ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_downgrade_oddeven_RPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"
    
     ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_downgrade_oddeven_RPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"
    

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
        

TC22 Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using Serial mode without force flag (Upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using Serial mode without force flag (Upgrade)"
    Log to Console    "F1541_UI_TC21 -->  Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using Serial mode without force flag (Upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""



   #################Update firware (STAGE + ACTIVATE ) OF ALL VC MODULES #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_upgrade_serial_RPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "


TC23 Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using parallel mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using parallel mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC24 -->  Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using parallel mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


   ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_downgrade_parallel_SCEXE}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    
    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "


TC24 Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using parallel mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using parallel mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC18 -->  Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using parallel mode without force flag (upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""



   #################Update firware (STAGE + ACTIVATE ) OF ALL VC MODULES #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_upgrade_parallel_RPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "

TC25 Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using Odd/Even mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using Odd/Even mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC26-->  Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using Odd/Even mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


   ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_downgrade_oddeven_SCEXE}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    
    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "

TC26 Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using Odd/Even mode without force flag (upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using Odd/Even mode without force flag (upgrade)"
    Log to Console    "F1541_UI_TC20 -->  Verify the FW Update operation (Stage + Activate) from scexes to RPM firmware version using Odd/Even mode without force flag (upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""



   #################Update firware (STAGE + ACTIVATE ) OF ALL VC MODULES #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_upgrade_oddeven_RPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "

TC27 Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using parallel mode without force flag (Upgrade)
    Log To Console   "###############Staging + activation of firmware update of  all vc  Modules when IC state are configured ############"
    [Documentation]    "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using parallel mode without force flag (Upgrade)"
    Log to Console    "F1541_UI_TC22 -->  Verify the FW Update operation (Stage + Activate) from RPM to RPM firmware version using parallel mode without force flag (Upgrade)"
    Log To Console    ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=    Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =    Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""

   #################Update firware (STAGE + ACTIVATE ) OF ALL VC MODULES #####################
    ${Status}=  fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_upgrade_parallel_RPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
                              
TC28 Verify the FW update by Performing staging of RPM type, then perform staging of Scexe type Then do activation and ensure that Scexe type gets activated(Dowmgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the FW update by Performing staging of RPM type, then perform staging of Scexe type Then do activation and ensure that Scexe type gets activated"
    Log to Console      "F1541_UI_TC28 -->  Verify the FW update by Performing staging of RPM type, then perform staging of Scexe type Then do activation and ensure that Scexe type gets activated
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXES_downgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "
    
   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_SCEXES_downgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "

TC29 Verify FW by Performing staging of Scexe type, then perform staging of RPM type. then do activation and ensure that RPM type gets activated(Upgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify FW by Performing staging of Scexe type, then perform staging of RPM type. then do activation and ensure that RPM type gets activated"
    Log to Console      "F1541_UI_TC29 -->  Verify FW by Performing staging of Scexe type, then perform staging of RPM type. then do activation and ensure that RPM type gets activated
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_SCEXE_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "

    #################STAGING FIRMWARE on ICMS#####################
    ${Status}=    fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_stg_RPM_upgrade}[0]
    run keyword if    '${status}'=='False'    Fail      " Staging of firmware failed "
    
   #################ACTIVATE THE STAGED FIRMWARE #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_active_RPM_upgrade_parallel}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "

TC30 Verify the LI FW Update operation (Stage + Activate) from scexes to SCXERPM firmware version using parallel mode with force flag (downgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using Odd/Even mode with force flag (downgrade)"
    Log to Console      "F1541_UI_TC50-->  Verify the FW Update operation (Stage + Activate) from RPM to scexes firmware version using Odd/Even mode with force flag (downgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


   ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_downgrade_parallel_SCEXERPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    
    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "

TC31 Verify the LI FW Update operation (Stage + Activate) from RPM to SCXERPM firmware version using serial mode without force flag (upgrade)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the LI FW Update operation (Stage + Activate) from RPM to SCXERPM firmware version using serial mode without force flag (upgrade)"
    Log to Console      "F1541_UI_TC51--> Verify the LI FW Update operation (Stage + Activate) from RPM to SCXERPM firmware version using serial mode without force flag (upgrade)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


   ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_upgrade_serial_SCEXERPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    
    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "

TC32 Verify the LI FW Update operation (Stage + Activate) from RPM to SCXERPM firmware version using Odd/Even mode with force flag (same version)
    Log To Console      "###############Staging and activation of firmware update of vc Modules when IC state are configured ############"
    [Documentation]      "RPM support FW update via LI: Verify the LI FW Update operation (Stage + Activate) from RPM to SCXERPM firmware version using Odd/Even mode with force flag (same version)"
    Log to Console      "F1541_UI_TC52--> Verify the LI FW Update operation (Stage + Activate) from RPM to SCXERPM firmware version using Odd/Even mode with force flag (same version)
    Log To Console      ****Validation of  the interconnect states before  FW update triggers **********
    ${li_list_1}=     Get Variable Value   ${TestData.LIGlistvariable[0].name}

    ${li_list} =     Create list     ${li_list_1}

    #################VERIFY IC STATE OF LI BEFORE UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured""


   ################# UPDATE FIRMWARE (STAGE + ACTIVATE ) #####################
    ${Status}=     fusion_ui_update_firmware_logical_interconnect_new      @{TestData.Update_firmware_upgrade_oddeven_SCEXERPM}[0]
    run keyword if    '${status}'=='False'    Fail      "Firmware activation of icms Failed"

    #################VERIFY THE UI IC FIRMWARE VERSION and COMPARE with actual  IC version #####################
    ${Status}=      fusion_ui_validation_interconnect_firmware_from_li      ${li_list}      ${TestData.firmware1}
    ${Status1}=    Get From List    ${Status}   0
    run keyword if    '${status1}'=='False'    Fail      " Validation of  interconnects firmware versions are failed "

    #################VERIFY IC STATE OF LI AFTER UPGRADE #####################
    ${Status}=    fusion_ui_verify_ic_state_of_li      ${li_list}    ${Permissible_IC_STATES_AfterUpdate}
    run keyword if    '${status}'=='False'    Fail      " IC states are not as Desired state "Configured" "

    ############ VERIFY THE ALERT MESSAGES on ACTIVITY PAGE ########################################
    ${Status}=     fusion_ui_validation_c7k_updatefirmwarealerts_in_li  @{TestData.logicalconnect}[0]
    run keyword if    '${status}'=='False'    Fail      " Validation of alert messages are failed "
                                                                                                                                  