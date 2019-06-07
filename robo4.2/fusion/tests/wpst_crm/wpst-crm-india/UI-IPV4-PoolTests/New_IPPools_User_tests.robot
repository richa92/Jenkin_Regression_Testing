*** Settings ***
Documentation    User Privilege tests for IPv4 Subnet and Range Pools
Resource    TestConfig.robot
Force Tags    Buildup
Suite Setup    Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers
Library    RoboGalaxyLibrary
Library    FusionLibrary
Library    String

*** Test Cases ***

0.IpV4 Range Pools -User Privilege Tests - Login and Create users
    Set Log Level    TRACE
    Log Variables
    Log into Fusion Appliance As Administrator
    Fusion UI Create User  @{TestData.users}

0.IP Ranges Cleanup and create pre req subnet
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange    @{TestData.ippoolsuser}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[4]}
    Log To Console   ${Status}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Fusion UI Logout of Appliance
    Log to Console    ==========================================================================

# =======================================================================================================================
# ====================================== USER PRIVILEGE SCENATIOS ======================================================
# =======================================================================================================================

1.login as NETWORK ADMINISTRATOR - Create ipv4 subnets and ranges
    # F258_UI_TC_164
    Log into Fusion Appliance As NetworkAdmin
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[0]}
    Log To Console   ${Status}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsuser[0]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsuser[0]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Fusion UI Logout of Appliance
    Log to Console    ==========================================================================

2.login as BACKUP ADMINISTRATOR - Try to click on Address and Identifiers Edit link and List ipv4 address ranges
    # F258_UI_TC_163
    Log into Fusion Appliance As BackupAdmin
    ${Status}=   Fusion Ui Validate Settings Page Addressesidentifiers Edit LInk For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Validate Addressesidentifiers actions menu Edit option For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    Log to Console  ===== List IPV4 Subnets ====================
    ${Status}=    Fusion Ui Get Ipv4 Subnet And Addressranges
    Log to Console   ${Status}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance

3.login as READ ONLY USER - Try to click on Address and Identifiers Edit link and List ipv4 address ranges
    Log into Fusion Appliance As ReadOnly
    ${Status}=   Fusion Ui Validate Settings Page Addressesidentifiers Edit LInk For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Validate Addressesidentifiers actions menu Edit option For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    Log to Console  ===== List IPV4 Subnets ====================
    ${Status}=    Fusion Ui Get Ipv4 Subnet And Addressranges
    Log to Console   ${Status}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance

4.login as SERVER ADMINISTRATOR - Create/Edit and delete
    # F258_UI_TC_163
    Log into Fusion Appliance As ServerAdmin
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[1]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpectedErrorMessage2}=    Convert To Lowercase   ${expectedmsg22}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpectedErrorMessage2}   Expected Error Message not Seen.
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[5]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpectedErrorMessage5}=    Convert To Lowercase   ${expectedmsg24}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpectedErrorMessage5}   Expected Error Message not Seen.
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[2]}
    log to console    ${Status}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after edit
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsuser[2]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsuser[2]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsuser[0]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpectedErrorMessage4}=    Convert To Lowercase   ${expectedmsg23}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpectedErrorMessage4}   Expected Error Message not Seen.
    Log to Console    ==========================================================================
    Log to Console  ===== List IPV4 Subnets ====================
    ${Status}=    Fusion Ui Get Ipv4 Subnet And Addressranges
    Log to Console   ${Status}
    Fusion UI Logout of Appliance

5.login as STORAGE ADMINISTRATOR -click on Address and Identifiers Edit link-Try to Create and Edit ipv4 address range
    # F258_UI_TC_163
    Log into Fusion Appliance As StorageAdmin
    ${Status}=   Fusion Ui Validate Settings Page Addressesidentifiers Edit LInk For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Validate Addressesidentifiers actions menu Edit option For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    Log to Console  ===== List IPV4 Subnets ====================
    ${Status}=    Fusion Ui Get Ipv4 Subnet And Addressranges
    Log to Console   ${Status}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance

6.Login as SOFTWARE ADMINISTRATOR- Check privileges and List subnets
    # F258_UI_TC_163
    Log into Fusion Appliance As SoftwareAdmin
    ${Status}=   Fusion Ui Validate Settings Page Addressesidentifiers Edit LInk For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Validate Addressesidentifiers actions menu Edit option For User
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should be equal    '${Status}'   'True'   Error-${Status}
    Log to Console    ==========================================================================
    Log to Console  ===== List IPV4 Subnets ====================
    ${Status}=    Fusion Ui Get Ipv4 Subnet And Addressranges
    Log to Console   ${Status}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance

7.login as CUSTOM USER -click on Address and Identifiers Edit link-Try to Create and Edit ipv4 address range
    # F258_UI_TC_163
    Log into Fusion Appliance As specified user    CustomUser
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[1]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpectedErrorMessage2}=    Convert To Lowercase   ${expectedmsg22}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpectedErrorMessage2}   Expected Error Message not Seen.
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[5]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpectedErrorMessage5}=    Convert To Lowercase   ${expectedmsg24}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpectedErrorMessage5}   Expected Error Message not Seen.
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[6]}
    log to console    ${Status}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after edit
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsuser[6]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsuser[6]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsuser[0]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpectedErrorMessage4}=    Convert To Lowercase   ${expectedmsg23}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpectedErrorMessage4}   Expected Error Message not Seen.
    Log to Console    ==========================================================================
    Log to Console  ===== List IPV4 Subnets ====================
    ${Status}=    Fusion Ui Get Ipv4 Subnet And Addressranges
    Log to Console   ${Status}
    Fusion UI Logout of Appliance

8.Login as NETWORK ADMINISTRATOR -Edit and Delete Range
    # F258_UI_TC_164
    Log into Fusion Appliance As NetworkAdmin
    # edit subnet
    ${Status}=    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[3]}
    Log To Console   ${Status}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after edit
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsuser[3]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsuser[3]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # delete
    ${Status}=    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsuser[0]}
    Log To Console   ${Status}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance

Final-Cleanup after tests
    Log into Fusion Appliance As Administrator
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange    @{TestData.ippoolsuser}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance
