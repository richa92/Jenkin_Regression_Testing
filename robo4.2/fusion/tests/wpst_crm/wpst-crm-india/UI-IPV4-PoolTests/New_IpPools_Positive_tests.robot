*** Settings ***
Documentation    Positive Test cases for IPv4 Subnet and Range Pool
Resource    TestConfig.robot
Force Tags    Buildup
Suite Setup    Load Test Data and Open Browser
Test Teardown    Close All Browsers
Library    RoboGalaxyLibrary
Library    FusionLibrary
Library    String

*** Test Cases ***

0.IPV4 Address Pool-Login as administrator and clean UP
    Set Log Level    TRACE
    Log Variables
    Login to Fusion Appliance As Administrator
    Log to Console    *********Login Completed*********
    Log To Console  ***** Clean up before tests-Delete Subnets *****
    Run Keyword And Ignore Error    fusion_ui_delete_ethernet_network   @{TestData.myNetworks}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippools}  @{TestData.ippoolsvlsm}  @{TestData.ippools_edit}   @{TestData.ippoolscount}

# =======================================================================================================================
# ======================================POSITIVE SCENATIOS ==============================================================
# =======================================================================================================================

1.List ipv4 subnets-BEFORE ANY SUBNET CREATION-No default range Present
    # encompasses test cases - F258_UI_TC_02,F258_UI_TC_03
    Login to Fusion Appliance As Administrator
    Log to Console  ================= List IPV4 Subnets ====================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Get Ipv4 Subnet And Addressranges
    ${Status}=    Convert To Lowercase   ${Status}
    ${expmsg}=    Convert To Lowercase   ${expectedmsg1}
    Should contain   ${Status}    ${expmsg}    Some Data present in table!! ${Status}
    Log to Console    ==========================================================================

2.Positive-Verify Total Pool count changes on subnet addition/deletion and on enabling/disabling ranges
    Login to Fusion Appliance As Administrator
    Log To console   =====Check IP count is not set/0 before any subnet creation=====
    ${count1}=    Fusion Ui Get Ipv4 Addresses Count
    Log To console  Total Pool Count: ${count1}
    Log to Console    ================================================
    Log To console   =====Create subnet but do not add range verify IP count is 0====
    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolscount[0]}
    ${count2}=    Fusion Ui Get Ipv4 Addresses Count
    Log To Console   Current IP Available Count : ${count2}
    Run Keyword And Continue On Failure    Should Be Equal   '${count2}'   '0'   Count should be zero but is not!!
    Log to Console    ================================================
    Log To console   =====Add range - verify IP count is not 0====
    Fusion Ui Add Ipv4 Addressrange To Subnet  ${TestData.ippoolscount[0].subnetid}    ${TestData.addressranges[10]}
    ${count3}=    Fusion Ui Get Ipv4 Addresses Count
    Log To Console   Current IP Available Count : ${count3}
    Run Keyword And Continue On Failure    Should Be Equal   '${count3}'   '11'   Count should be 11 but is not!!
    Log to Console    ================================================
    Log To console   =====Disable range - verify IP count becomes 0====
    Fusion Ui Enable disable Addressrange Of Ipv4Subnet  ${TestData.ippoolscount[0].subnetid}  ${TestData.addressranges[12]}
    ${count4}=    Fusion Ui Get Ipv4 Addresses Count
    Log To Console   Current IP Available Count : ${count4}
    Run Keyword And Continue On Failure    Should Be Equal   '${count4}'   '0'   Count should be zero but is not!!
    Log to Console    ================================================
    Log To console   =====Add another new range, verify count increases====
    Fusion Ui Add Ipv4 Addressrange To Subnet  ${TestData.ippoolscount[0].subnetid}    ${TestData.addressranges[11]}
    ${count5}=    Fusion Ui Get Ipv4 Addresses Count
    Log To Console   Current IP Available Count : ${count5}
    Run Keyword And Continue On Failure    Should Be Equal   '${count5}'   '6'   Count should be 6 but is not!!
    Log to Console    ================================================
    Log To console   =====Disable one of the ranges, enable another.verify count decreases by the number====
    Fusion Ui Enable disable Addressrange Of Ipv4Subnet  ${TestData.ippoolscount[0].subnetid}  ${TestData.addressranges[14]}  ${TestData.addressranges[13]}
    ${count6}=    Fusion Ui Get Ipv4 Addresses Count
    Log To Console   Current IP Available Count : ${count6}
    Run Keyword And Continue On Failure    Should Be Equal   '${count6}'   '11'   Count should be 11 but is not!!
    Log to Console    ================================================
    Log To console   =====Enable both ranges.verify count increases====
    Fusion Ui Enable disable Addressrange Of Ipv4Subnet  ${TestData.ippoolscount[0].subnetid}  ${TestData.addressranges[14]}  ${TestData.addressranges[15]}
    ${count7}=    Fusion Ui Get Ipv4 Addresses Count
    Log To Console   Current IP Available Count : ${count7}
    Run Keyword And Continue On Failure    Should Be Equal   '${count7}'   '17'   Count should be 17 but is not!!
    Log to Console    ================================================
    Log To console   =====Delete subnet and get IP count.Should be 0====
    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolscount[0]}
    ${count8}=    Fusion Ui Get Ipv4 Addresses Count
    Log To Console   Current IP Available Count : ${count8}
    Run Keyword And Continue On Failure    Should Be Equal   '${count8}'   '0'   Count should be zero but is not!!
    Log to Console    ================================================


3.Positive-Create Subnet and verify
    # F258_UI_TC_04, F258_UI_TC_05, F258_UI_TC_06, F258_UI_TC_31, F258_UI_TC_32 , F258_UI_TC_54 - VLSM, F258_UI_TC_80
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools[0]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    # encompasses test cases - F258_UI_TC_01,
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippools[0]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippools[0]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

4.Positive-Create Subnet and verify
    # F258_UI_TC_04, F258_UI_TC_05, F258_UI_TC_06, F258_UI_TC_31, F258_UI_TC_32 , F258_UI_TC_54 - VLSM, F258_UI_TC_80
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools[1]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    # encompasses test cases - F258_UI_TC_01,
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippools[1]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippools[1]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

5.Positive-Create Subnet with VLSM(Variable Length Subnet Mask)
    # F258_UI_TC_04, F258_UI_TC_05, F258_UI_TC_06, F258_UI_TC_31, F258_UI_TC_32 , F258_UI_TC_54 - VLSM, F258_UI_TC_80
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    @{TestData.ippoolsvlsm}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    # encompasses test cases - F258_UI_TC_01,
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    @{TestData.ippoolsvlsm}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    @{TestData.ippoolsvlsm}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

6.Positive-Edit subnet
    # F258_UI_TC_09, F258_UI_TC_10, F258_UI_TC_11, F258_UI_TC_33, F258_UI_TC_51, F258_UI_TC_55, F258_UI_TC_77, F258_UI_TC_82, F258_UI_TC_87
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippools_edit[0]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after edit
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippools_edit[0]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippools_edit[0]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

7.Positive-Edit subnet
    # F258_UI_TC_09, F258_UI_TC_10, F258_UI_TC_11, F258_UI_TC_33, F258_UI_TC_51, F258_UI_TC_55, F258_UI_TC_77, F258_UI_TC_82, F258_UI_TC_87
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippools_edit[1]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after edit
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippools_edit[1]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippools_edit[1]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

8.Positive-Add ranges to existing subnet
    # F258_UI_TC_32, F258_UI_TC_33, F258_UI_TC_37, F258_UI_TC_56
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Add Ipv4 Addressrange To Subnet  ${TestData.ippools_edit[0].subnetid}    ${TestData.addressranges[0]}  ${TestData.addressranges[1]}  ${TestData.addressranges[2]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Addressranges Of Subnet In Edit Dialog   ${TestData.ippools_edit[0].subnetid}    ${TestData.addressranges[0]}  ${TestData.addressranges[1]}  ${TestData.addressranges[2]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Addressranges Of Subnet In Addressesidentifiers Page    ${TestData.ippools_edit[0].subnetid}    ${TestData.addressranges[0]}  ${TestData.addressranges[1]}  ${TestData.addressranges[2]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

9.Positive-Edit Ranges in an existing subnet
    # F258_UI_TC_14, F258_UI_TC_32, F258_UI_TC_33, F258_UI_TC_60, F258_UI_TC_61, F258_UI_TC_73,
    # F258_UI_TC_109, F258_UI_TC_110, F258_UI_TC_111, F258_UI_TC_112, F258_UI_TC_113, F258_UI_TC_114, F258_UI_TC_115, F258_UI_TC_121
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Edit Ipv4 Addressrange In Subnet  ${TestData.ippools_edit[0].subnetid}   ${TestData.addressranges[3]}  ${TestData.addressranges[4]}  ${TestData.addressranges[5]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Addressranges Of Subnet In Edit Dialog    ${TestData.ippools_edit[0].subnetid}   ${TestData.addressranges[3]}  ${TestData.addressranges[4]}  ${TestData.addressranges[5]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Addressranges Of Subnet In Addressesidentifiers Page    ${TestData.ippools_edit[0].subnetid}   ${TestData.addressranges[3]}  ${TestData.addressranges[4]}  ${TestData.addressranges[5]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

10.Positive-delete ranges from existing subnet
    # F258_UI_TC_73, F258_UI_TC_83, F258_UI_TC_84, F258_UI_TC_95
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Delete Ipv4 Addressrange from Subnet  ${TestData.ippools_edit[0].subnetid}   ${TestData.addressranges[6]}  ${TestData.addressranges[7]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

11.Positive-Enable/Disable Address ranges
    # F258_UI_TC_34,F258_UI_TC_35
    Login to Fusion Appliance As Administrator
    ${Status}=   Fusion Ui Enable disable Addressrange Of Ipv4Subnet  ${TestData.ippools_edit[0].subnetid}  ${TestData.addressranges[8]}  ${TestData.addressranges[9]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Addressrange state    ${TestData.ippools_edit[0].subnetid}  ${TestData.addressranges[8]}  ${TestData.addressranges[9]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

12.Positive-List ipv4 subnets
    # encompasses test cases - F258_UI_TC_02,F258_UI_TC_03
    Login to Fusion Appliance As Administrator
    Log to Console  ================= List IPV4 Subnets ====================
    ${Status}=    Fusion Ui Get Ipv4 Subnet And Addressranges
    Log to Console    ${Status}

13.Positive-Delete Subnet
    # F258_UI_TC_42,
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsvlsm[1]}  ${TestData.ippoolsvlsm[2]}  ${TestData.ippoolsvlsm[4]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

CleanUP-Delete Subnets
    # F258_UI_TC_53, F258_UI_TC_169
    Login to Fusion Appliance As Administrator
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippools}  @{TestData.ippoolsvlsm}  @{TestData.ippools_edit}   @{TestData.ippoolscount}
    Log to Console    ==========================================================================
