*** Settings ***

Resource    firmware_config.txt
Force Tags    Buildup
Suite Setup    Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers


*** Test Cases ***

0.User Privilege Tests - Login and Create users
    Set Log Level    TRACE
    Log Variables
    Log into Fusion Appliance As Administrator
    Fusion UI Create User    @{TestData.users}
    Log to Console    *********Test   - 0 Completed*********
    Fusion UI Logout of Appliance

################## USER PRIVILEGES TESTS ###################################

################################################################################################
#################################### LI user Tests #############################################
################################################################################################

1.Login as ReadOnly User and try a FW update from LI
    Log into Fusion Appliance As ReadOnly
    ${Status}=    Run Keyword and expect error    *   Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[0]

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg2user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

2.Login as ServerAdmin and try a FW update from LI
    Log into Fusion Appliance As ServerAdmin
    ${Status}=    Run Keyword and expect error    *    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[0]
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg2user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

3.Login as StorageAdmin and try a FW update from LI
    Log into Fusion Appliance As StorageAdmin
    ${Status}=    Run Keyword and expect error    *    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[0]
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg2user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

4.Login as BackupAdmin and try a FW update from LI
    Log into Fusion Appliance As BackupAdmin
    ${Status}=    Run Keyword and expect error    *    Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[0]
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg2user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

5.Login as Software Admin and try a FW update from LI
    Log into Fusion Appliance As SoftwareAdmin
    ${Status}=    Run Keyword and expect error    *   Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[0]

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg2user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

6.Login as Custom User and try a FW update from LI
    Log into Fusion Appliance As specified user    CustomUserLI
    ${Status}=    Run Keyword and expect error    *   Fusion UI update firmware tbird logical interconnect    @{TestData.logicalconnectNDFU}[0]

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg2user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

################################################################################################
#################################### LE user Tests #############################################
################################################################################################

1.Login as ReadOnly User and try a FW update from LE
    Log into Fusion Appliance As ReadOnly

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware2}

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg1user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

2.Login as NetworkAdmin and try a FW update from LE
    Log into Fusion Appliance As NetworkAdmin

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware2}

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg1user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

3.Login as StorageAdmin and try a FW update from LE
    Log into Fusion Appliance As StorageAdmin

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware2}

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg1user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

4.Login as BackupAdmin and try a FW update from LE
    Log into Fusion Appliance As BackupAdmin

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware2}

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg1user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

5.Login as Software Admin and try a FW update from LE
    Log into Fusion Appliance As SoftwareAdmin

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware2}

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg1user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance

6.Login as Custom User and try a FW update from LE
    Log into Fusion Appliance As specified user    CustomUserLE

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware2}

    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpectedMsg}=    Convert To Lowercase    ${ExpectedErrorMsg1user}
    Run Keyword and Continue on Failure    Should Contain    '${Status}'    ${ExpectedMsg}    Expected Message Not seen

    Fusion UI Logout of Appliance


################# FW UPGRADES ##################################################################

7.Login as NetworkAdmin and try a FW update from LI-downgrade
    Log into Fusion Appliance As NetworkAdmin

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
    Fusion UI Logout of Appliance

8.Login as ServerAdmin and try a FW update from LE-upgrade
    Log into Fusion Appliance As ServerAdmin

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE BEFORE FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE BEFORE FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_BeforeUpdate}   ${TestData.firmware2NDFW}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    ${Status}=    fusion_ui_update_tbird_logical_enclosure_firmware   ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    ${Status}

    Log to Console    ****** VERIFY LE FW UPDATE ACTIVITY ********

    ${Status}=    fusion_ui_validate_le_firmware_upgrade_activity_details    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Contain    ${Status}   TEST PASSED    LE FW Update Test FAILED

    Log to Console    ****** VERIFY IC FW ********
    ${Status}=    fusion_ui_verify_li_and_ic_firmware_versions    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Error during Firmware Version and IC activity Messages Validation

    Log To Console    ******VERIFY IC STACKING DOMAIN ROLE of LE AFTER FW UPDATE******
    ${Status}=    fusion_ui_verify_ic_stacking_domain_role_of_le    ${TestData.firmware2NDFW}
    Run Keyword and Continue on Failure    Should Be Equal    '${Status}'    'True'    Something Wrong with IC stacking Roles.FW update might Not be successfull!!

    Log to Console    ****** VERIFY IC STATE OF LE AFTER FW UPDATE ********
    ${Status}=    fusion_ui_verify_ic_state_of_le    ${Permissible_IC_STATES_AfterUpdate}    ${TestData.firmware2NDFW}
    Run Keyword If    '${Status}'=='True'    Log To Console    IC Sates as desired    ELSE    Fail

    Fusion UI Logout of Appliance

