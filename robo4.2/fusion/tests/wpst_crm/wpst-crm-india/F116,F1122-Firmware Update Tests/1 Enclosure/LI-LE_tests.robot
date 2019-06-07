*** Settings *** *

Documentation    Continuous Integration Tests for RoboGalaxy dev Branch
Resource    firmware_config.txt
Force Tags    Buildup
Suite Setup    Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers
Library    Dialogs


*** Test Cases ***

Update firmware through LI tests-LOGIN
    Set Log Level    TRACE
    Log Variables
    ${user}=    Get Data By Property    ${TestData.users}    name    Administrator
    Fusion UI Login to Appliance    ${user[0].name}

    #fusion_ui_power_on_server_profile_by_name    ${TestData.CreateProfile[0].name}
    #fusion_ui_power_off_server_profile_by_name    ${TestData.CreateProfile[0].name}
    #fusion_ui_power_on_server_profile_by_name    ${TestData.CreateProfile[0].name}

    #Fusion UI Create User    @{TestData.users}

################## PRE REQ #################################

CleanUP-Delete LE,EG,LIG,NETWORKS and SUBNETS-FOR LE
    Fusion UI Logout of Appliance
    ${user}=    Get Data By Property    ${TestData.users}    name    Administrator
    Fusion UI Login to Appliance    ${user[0].name}

    fusion_ui_delete_server_profile_by_name    ${TestData.CreateProfile[0].name}
    ${Status}=    Run Keyword And Ignore Error    fusion_ui_delete_logical_enclosure    ${TestData.les[0]}

add firmware bundle
    fusion_ui_add_firmware_bundle    @{TestData.firmwarebundle}
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    Unable to add all firmware bundles

Positive-Create Subnet and verify
    ${Status}=    fusion_ui_create_ipv4_subnet_and_address_range    ${TestData.ippoolsE2E[0]}
    Log To Console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log to Console    ==========================================================================

Create Networks
    ${Status}=    fusion_ui_create_ethernet_network    @{TestData.myNetworks}
    Should Be Equal    '${Status}'    'True'    ${Status}

Create Logical Interconnect Group
    #Create LIG
    Log To Console    ******CREATE LIG**********
    ${Status}=    fusion_ui_create_tbird_logical_interconnect_group    @{TestData.ligs}
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******CREATE LIG operations completed**********

Create Enclosure Group
    # create EG
    ${Status}=    fusion_ui_create_tbird_enclosure_group    @{TestData.encgrp}
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******CREATE EG operations completed**********

#############################################################################################################################################################################


#Create LE-1 enc-multi LI-scenario testing
#    ${Status}=    Run Keyword And Ignore Error    fusion_ui_create_tbird_logical_enclosure    ${TestData.les[1]}
#    Log To Console    ******CREATE LE operations completed**********

Create LE-1 enc-redundant-scenario testing
    ${Status}=    Run Keyword And Ignore Error    fusion_ui_create_tbird_logical_enclosure    ${TestData.les[0]}
    Log To Console    ******CREATE LE operations completed**********

Create Server Profile
    fusion_ui_create_server_profile    ${TestData.CreateProfile[0]}
    fusion_ui_power_on_server_profile_by_name    ${TestData.CreateProfile[0].name}
    fusion_ui_power_off_server_profile_by_name    ${TestData.CreateProfile[0].name}
    fusion_ui_power_on_server_profile_by_name    ${TestData.CreateProfile[0].name}


#############################################################################################################
################################    LE TESTS    ####################################################
#############################################################################################################



################## LE Test - ORCHESTRATED -UPDATE ##########################################

1.POSITIVE-ORCHESTRATED-FW update for LE--Shared Infrastructure-UPDATE

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE BEFORE FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware2NDFW}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY ********

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

    Log to Console    ****** VERIFY IC FW ********
    ${Status}=    fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Error during Firmware Version and IC activity Messages Validation

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE AFTER FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware2NDFW}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

################## LE Test - ORCHESTRATED - SAME VERSION ##########################################

2.POSITIVE-ORCHESTRATED-FW update for LE--with force option-Shared Infrastructure-same version

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE BEFORE FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware1NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware1NDFW}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware    ${TestData.firmware1NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY ********

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware1NDFW}
    Run Keyword and Continue on Failure    Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

    Log to Console    ****** VERIFY IC FW ********
    ${Status}=    fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.firmware1NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Error during Firmware Version and IC activity Messages Validation

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE AFTER FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware1NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware1NDFW}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

############### LE - ORCHESTRATED - Downgrade ###################################

3.POSITIVE-ORCHESTRATED-Downgrade FW of LE--with force option-Shared Infrastructure
    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3NDFU.enclosure[0].name}    400

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE BEFORE FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware3NDFU}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware3NDFU}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware    ${TestData.firmware3NDFU}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY ********

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware3NDFU}
    Run Keyword and Continue on Failure    Should Contain    ${Status}    TEST PASSED
    ...    LE FW Update Test FAILED
    ${Status}=    fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.firmware3NDFU}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'
    ...    Error during Firmware Version and IC activity Messages Validation

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE AFTER FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware3NDFU}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY TC STATE OF LE AFTER FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware3NDFU}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail


##################### LI Upgrade - ORCHESTRATED######### ##################

1.POSITIVE-ORCHESTRATED-Update Firmware(Stage+Activate) test-(upgrade)
    
    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3.enclosure[0].name}    400

    Log To Console    ******Verifying the interconnect states before proceeding the test**********
    ${li_list}=    create List    ${TestData.logicalconnectNDFU[2].LIname}
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[2]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Stage+Activate through LI complete***********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail



#################### LI same Version Tests-With Force ORCHESTRATED #################################

2.POSITIVE-ORCHESTRATED-Staging to the baseline version for firmware update-same version-With Force

    #${user}=    Get Data By Property    ${TestData.users}    name    Administrator
    #Fusion UI Login to Appliance    ${user[0].name}

    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3NDFU.enclosure[0].name}    400

    ${li_list}=    create List    ${TestData.logicalconnectNDFU[0].LIname}
    Log To Console    ******Verifying the interconnect states before proceeding the test of LI ${TestData.logicalconnectNDFU[0].LIname}**********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[0]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Verify Firmware staging through LI complete**********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

3.POSITIVE-ORCHESTRATED-Activate to the staged baseline tests(upgrade)-same version-With Force
    #Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3NDFU.enclosure[0].name}    400

    ${li_list}=    create List    ${TestData.logicalconnectNDFU[1].LIname}
    Log To Console    ******Verifying the interconnect states before proceeding the test**********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[1]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Verify Firmware Activation through LI complete**********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail


################## LI Test - ORCHESTRATED - Downgrade ##########################################

4.POSITIVE-USER-ORCHESTRATED-FW update from LI-downgrade

    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3.enclosure[0].name}    400
    Log To Console    ******Verifying the interconnect states before proceeding the test**********
    ${li_list}=    create List    ${TestData.logicalconnectNDFU[3].LIname}
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[3]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Stage+Activate through LI complete***********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail
    
#################################################################################################################

################## LE Test - PARALLEL -UPDATE ##########################################

4.POSITIVE-PARALLEL-Upgrade FW of LE--without force-Shared Infrastructure
    fusion_ui_power_off_server_profile_by_name    ${TestData.CreateProfile[0].name}

    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware1.enclosure[0].name}    400

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE BEFORE FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware1}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware1}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    # UPDATE FIRMWARE
    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware    ${TestData.firmware1}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY ********
    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware1}
    Run Keyword and Continue on Failure    Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

    Log to Console    ****** VERIFY IC FW ********
    ${Status}=    fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.firmware1}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Error during Firmware Version and IC activity Messages Validation

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE AFTER FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware1}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware1}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail



##################################### LE TEST -PARALLEL -same version    #########################

5.POSITIVE-PARALLEL-Same Version FW update for LE--with force option-Shared Infrastructure
    #${user}=    Get Data By Property    ${TestData.users}    name    Administrator
    #Fusion UI Login to Appliance    ${user[0].name}

    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3NDFU.enclosure[0].name}    400
    #fusion_ui_power_off_server_profile_by_name    ${TestData.CreateProfile[0].name}

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE BEFORE FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware2}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware2}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware    ${TestData.firmware2}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY ********

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware2}
    Run Keyword and Continue on Failure    Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED

    Log to Console    ****** VERIFY IC FW ********
    ${Status}=    fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.firmware2}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Error during Firmware Version and IC activity Messages Validation

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE AFTER FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware2}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware2}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail


    
####################### LE PARALLEL DOWNGRADE #############################

6.POSITIVE-PARALLEL-Downgrade FW of LE--with force option-Shared Infrastructure
    
    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE BEFORE FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware3}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_BeforeUpdate}    ${TestData.firmware3}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware    ${TestData.firmware3}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY ********

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware3}
    Run Keyword and Continue on Failure    Should Contain    ${Status}    TEST PASSED    LE FW Update Test FAILED
    ${Status}=    fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.firmware3}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Error during Firmware Version and IC activity Messages Validation

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE AFTER FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware3}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY TC STATE OF LE AFTER FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware3}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    


##################### LI same Version Tests-With Force PARALLEL #################################

5.POSITIVE-PARALLEL-Staging to the baseline version for firmware update-same version-With Force

    ${li_list}=    create List    ${TestData.logicalconnect[3].LIname}
    Log To Console    ******Verifying the interconnect states before proceeding the test of LI ${TestData.logicalconnect[3].LIname}**********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnect}[3]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Verify Firmware staging through LI complete**********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

6.POSITIVE-PARALLEL-Activate to the staged baseline tests(upgrade)-same version-With Force
    ${li_list}=    create List    ${TestData.logicalconnect[4].LIname}
    Log To Console    ******Verifying the interconnect states before proceeding the test**********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnect}[4]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Verify Firmware Activation through LI complete**********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail


################ LI Upgrade - Disruptive Firmware Update Positive Tests ##################

7.POSITIVE-PARALLEL-Update Firmware(Stage+Activate) test-(upgrade)
    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3.enclosure[0].name}    400

    Log To Console    ******Verifying the interconnect states before proceeding the test**********
    ${li_list}=    create List    ${TestData.logicalconnect[2].LIname}
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnect}[2]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Stage+Activate through LI complete***********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail




################ LI Downgrade PARALLEL ##################

8.POSITIVE-PARALLEL-Update Firmware(Stage+Activate) test-(downgrade)

    Run Keyword and ignore error    fusion_ui_wait_for_enclosure_refresh_complete    ${TestData.firmware3NDFU.enclosure[0].name}    400

    Log To Console    ******Verifying the interconnect states before proceeding the test**********
    ${li_list}=    create List    ${TestData.logicalconnect[5].LIname}
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

    ${Status}=    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnect}[5]
    Run Keyword And Continue On Failure    Should Be Equal    '${Status}'    'True'    ${Status}
    Log To Console    ******Stage+Activate through LI complete***********

    Log To Console    ******Verifying the interconnect states After test **********
    ${Status}=    fusion_ui_verify_ic_state_of_li    ${li_list}    ${Permissible_IC_STATES_BeforeUpdate}
    Run Keyword If    '${status}'=='True'    Log To Console    IC states as Desired    ELSE    Fail

