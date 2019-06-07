*** Settings ***
Documentation    Positive Test cases for IPv4 Subnet and Range Pool
Resource    TestConfig.robot
Force Tags    Buildup
Test Setup    Load Test Data and Open Browser
Test Teardown    Close All Browsers
Library    RoboGalaxyLibrary
Library    FusionLibrary
Library    String

*** Test Cases ***

#=======================================================================================================================
#======================================POSITIVE SCENATIOS =============================================================
#=======================================================================================================================

Login as administrator and clean UP before Positive tests
    Set Log Level    TRACE
    Log Variables
    Login to Fusion Appliance As Administrator
    Log to Console    *********Login Completed*********
    Log To Console  ***** Clean up before tests-Delete Subnets *****
    # pre req clean up
    log to console    ==========CleanUP for negative tests==================
    Run Keyword And Ignore Error   Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippools2}
    Log To console    ======CleanUP-Delete NETWORKS and SUBNETS==========
    Run Keyword And Ignore Error    fusion_ui_delete_ethernet_network   ${TestData.myNetworksE2EVerify[4]}   ${TestData.myNetworksE2EVerify[5]}    ${TestData.myNetworksE2EVerify[6]}   @{TestData.myNetworksE2E}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange    @{TestData.ippoolsE2E}
    Log To Console   ====CleanUP for user tests
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange    @{TestData.ippoolsuser}
    Log to Console    ==========================================================================
    Log To console    ======CleanUP-Delete LE,EG,LIG,NETWORKS and SUBNETS
    ${Status}=    fusion_ui_delete_logical_enclosure    ${TestData.lesE2E[0]}
    Log to console  ${Status}
    ${Status}=    fusion_ui_delete_enclosure_group   ${TestData.encgroupsE2E[0]}
    Log to console  ${Status}
    ${Status}=   Run Keyword And Ignore Error    fusion_ui_delete_logical_interconnect_group    ${TestData.ligsE2E[0]}
    Log to console  ${Status}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}   ${TestData.ippoolsedite2e[0]}

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
    Log to Console   ${Status}
    Log to Console    ==========================================================================

13.Positive-Delete Subnet
    # F258_UI_TC_42,
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsvlsm[1]}  ${TestData.ippoolsvlsm[2]}  ${TestData.ippoolsvlsm[4]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

14-CleanUP-Delete Subnets after Positive tests
    # F258_UI_TC_53, F258_UI_TC_169
    Login to Fusion Appliance As Administrator
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippools}  @{TestData.ippoolsvlsm}  @{TestData.ippools_edit}   @{TestData.ippoolscount}
    Log to Console    ==========================================================================


# =======================================================================================================================
# ======================================NEGATIVE SCENATIOS =============================================================
# =======================================================================================================================

1.Negative-Create Subnet-invalid subnet mask
    # F258_UI_TC_47
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[0]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg1}=    Convert To Lowercase   ${expectedmsg2}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg1}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

2.Negative-Create Subnet-Invalid subnet ID for the given subnet
    # F258_UI_TC_46
    Login to Fusion Appliance As Administrator
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[1]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[1]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg2}=    Convert To Lowercase   ${expectedmsg3}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg2}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

3.Negative-Create Subnet-invalid gateway
    # F258_UI_TC_48
    Login to Fusion Appliance As Administrator
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[2]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[2]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg3}=    Convert To Lowercase   ${expectedmsg4}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg3}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

4.Negative-Create Subnet-Please enter at least 1 digit in each byte
    # F258_UI_TC_46, F258_UI_TC_47, F258_UI_TC_48, F258_UI_TC_49
    Login to Fusion Appliance As Administrator
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[3]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[3]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg4}=    Convert To Lowercase   ${expectedmsg5}
    ${ExpMsg14}=    Convert To Lowercase   ${expectedmsg13}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg4}  3   Expected Error Message not Seen expected no.of times.
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg14}  3   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

5.Negative-Create Subnet-empty subnet fields
    # F258_UI_TC_07,F258_UI_TC_23,F258_UI_TC_24,F258_UI_TC_25,F258_UI_TC_26
    Login to Fusion Appliance As Administrator
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[4]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[4]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg5}=    Convert To Lowercase   ${expectedmsg6}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg5}  4   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

6.Negative-Create Subnet-Address not within specified subnet
    # F258_UI_TC_39, F258_UI_TC_40, F258_UI_TC_71, F258_UI_TC_72, F258_UI_TC_76
    Login to Fusion Appliance As Administrator
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[5]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[5]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg6}=    Convert To Lowercase   ${expectedmsg7}
    ${expmsg}=    Catenate    ${ExpMsg6}    (1.1.1.1 , 1.1.1.254).
    Run Keyword And Continue On Failure    Should Contain X Times    ${Status}   ${expmsg}   4    Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Add Ipv4 Addressrange To Subnet  ${TestData.ippools2[5].subnetid}    ${TestData.addressranges[16]}
    Log To Console   ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    Run Keyword And Continue On Failure    Should Contain X Times    ${Status}   ${expmsg}   2    Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

7.Negative-Create Subnet-Please enter an ending address greater than the starting address
    # F258_UI_TC_62
    Login to Fusion Appliance As Administrator
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[6]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[6]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg7}=    Convert To Lowercase   ${expectedmsg8}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg7}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

8.Negative-Create Subnet -Please enter at least 1 digit in each byte for address range
    # F258_UI_TC_58
    Login to Fusion Appliance As Administrator
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[7]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[7]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg4}=    Convert To Lowercase   ${expectedmsg5}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg4}  2   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

9.Negative-Create Subnet -Warning during range addition
    # F258_UI_TC_57
    Login to Fusion Appliance As Administrator
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[8]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[8]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg9}=    Convert To Lowercase   ${expectedmsg9}
    Run Keyword And Continue On Failure    Should Contain    ${Status}    ${ExpMsg9}    Expected Error Message not Seen
    Log to Console    ==========================================================================

10.Negative-Create Subnet -Empty address range fields
    #  F258_UI_TC_69, F258_UI_TC_70
    Login to Fusion Appliance As Administrator
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[9]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[9]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg5}=    Convert To Lowercase   ${expectedmsg6}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg5}  3   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

11.Negative-Create Subnet-Broadcast IP as input in subnet fields
    # F258_UI_TC_27,F258_UI_TC_28,F258_UI_TC_29,F258_UI_TC_30
    Login to Fusion Appliance As Administrator
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[10]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[10]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg10}=    Convert To Lowercase   ${expectedmsg10}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg10}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

12.Negative-Create Subnet-Multicast IP as input in subnet fields
    # F258_UI_TC_19,F258_UI_TC_20,F258_UI_TC_21,F258_UI_TC_22
    Login to Fusion Appliance As Administrator
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[11]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[11]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg11}=    Convert To Lowercase   ${expectedmsg11}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg11}  4   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

13.Negative-Create Subnet-Gateway should be within subnet range
    Login to Fusion Appliance As Administrator
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[12]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[12]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg13}=    Convert To Lowercase   ${expectedmsg12}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg13}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

14.Negative-Create Subnet-Multicast IP as input range fields
    # F258_UI_TC_67, F258_UI_TC_68
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[13]}
    log to console    ${Status}
    ${ExpMsg}=    Set Variable   Address not within specified subnet (${TestData.ippools2[13].gateway} , ${TestData.ippools2[13].errormessage}).
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg}=    Convert To Lowercase   ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

15.Negative-Create Subnet-Provide invalid Ips in subnet inputs
    # F258_UI_TC_75
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[14]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg14}=    Convert To Lowercase   ${expectedmsg13}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg14}  6   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

16.Negative-Create Subnet and range-Provide invalid Ips in range inputs
    # F258_UI_TC_75
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[15]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg14}=    Convert To Lowercase   ${expectedmsg13}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg14}  2   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

17.Negative-Create Subnet and range-range cannot contain Gateway
    # F258_UI_TC_63
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[16]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg15}=    Convert To Lowercase   ${expectedmsg14}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg15}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

18.Negative-Create Subnet and range-DNS should not be same as gateway
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[17]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
	${expmsg}=    Catenate    ${expectedmsg28}   ${TestData.ippools2[17].gateway}
    ${ExpMsg28}=	Convert To Lowercase   ${expmsg}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg28}  3   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

19.Negative-Create Subnet-Duplicate
    # F258_UI_TC_12,F258_UI_TC_36
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[18]}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[18]}
    log to console    ${Status}
    ${ExpMsg}=    Set Variable   The specified subnet overlaps another subnet with subnet ID ${TestData.ippools2[18].subnetid}. Specify a different subnet.
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg}=    Convert To Lowercase   ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

20.Negative-Create Subnet-provide loop back address for subnet fields
    #F258_UI_TC_15,F258_UI_TC_16,F258_UI_TC_17,F258_UI_TC_18
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[19]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg19}=    Convert To Lowercase   ${expectedmsg17}
    ${expmsg}=    Catenate    ${expectedmsg28}   ${TestData.ippools2[19].gateway}
    ${ExpMsg28}=	Convert To Lowercase   ${expmsg}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg28}  3   Expected Error Message not Seen expected no.of times.
    Run Keyword And Continue On Failure    Should Contain	${Status}   ${ExpMsg19}  Expected Error Message not Seen.
    Log to Console    ========================================================================== 

21.Negative-Create Subnet-provide loop back address for range fields
    # F258_UI_TC_65, F258_UI_TC_66
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[20]}
    log to console    ${Status}
    ${ExpMsg}=    Set Variable   Address not within specified subnet (${TestData.ippools2[20].gateway} , ${TestData.ippools2[20].errormessage}).
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg}=    Convert To Lowercase   ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

22.Negative-Create Subnet-invalid domain name
    # F258_UI_TC_50,
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[21]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg20}=    Convert To Lowercase   ${expectedmsg18}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg20}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

23.Negative-Create Subnet-range name exists-within subnet
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[22]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg21}=    Convert To Lowercase   ${expectedmsg19}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg21}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

24.Negative-Create Subnet-range name exists-across subnet
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[23]}    ${TestData.ippools2[24]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg21}=    Convert To Lowercase   ${expectedmsg19}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg21}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

25.Negative-Create Subnet-overlapping ranges
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[25]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg22}=    Convert To Lowercase   ${expectedmsg20}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg22}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

26.Negative-Create Subnet-Range cannot contain DNS-F258_UI_TC_63
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[26]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${expmsg}=    Catenate    ${expectedmsg21}    ${TestData.ippools2[26].dns1},   ${TestData.ippools2[26].dns2},   ${TestData.ippools2[26].dns3}
    ${expmsg}=    Convert To Lowercase   ${expmsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${expmsg}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

Clean up after Negative Tests
    Login to Fusion Appliance As Administrator
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippools2}

# =======================================================================================================================
# ======================================netowrk SCENATIOS =============================================================
# =======================================================================================================================

Positive-Create Subnet and verify-networks-PreReq
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsE2E[0]}   ${TestData.ippoolsE2E[1]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsE2E[0]}   ${TestData.ippoolsE2E[1]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsE2E[0]}   ${TestData.ippoolsE2E[1]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

Positive-Create Subnet and verify-networks-PreReq
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsE2E[3]}   ${TestData.ippoolsE2E[4]}   ${TestData.ippoolsE2E[5]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsE2E[3]}   ${TestData.ippoolsE2E[4]}   ${TestData.ippoolsE2E[5]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsE2E[3]}   ${TestData.ippoolsE2E[4]}   ${TestData.ippoolsE2E[5]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    Run Keyword And Ignore Error    Fusion UI Logout of Appliance
#    Close All Browsers

#---------------Subnet - NETWORK(TAGGED/UNTAGGED) association------------------

1.Positive-Create Network and associate Subnet-Verify association
    # F258_UI_TC_143, F258_UI_TC_145, F258_UI_TC_146, F258_UI_TC_147, F258_UI_TC_159
#    Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    # create Network and associate subnet
    ${Status}=    fusion_ui_create_ethernet_network   ${TestData.myNetworksE2E[0]}    ${TestData.myNetworksE2E[1]}   ${TestData.myNetworksE2E[2]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #verify network
    ${Status}=    fusion_ui_verify_ethernet_network    ${TestData.myNetworksE2EVerify[0]}    ${TestData.myNetworksE2EVerify[1]}   ${TestData.myNetworksE2EVerify[2]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # check for associated network in subnet
    #${Status}=    fusion_ui_verify_associated_networks_of_subnet    ${TestData.ippoolsE2E[0].subnetid}   ${TestData.myNetworksE2E[0].name}    ${TestData.myNetworksE2E[2].name}
    ${Status}=    Fusion Ui Verify Networks association or Disassociation To Subnet   ${TestData.ippoolsE2E[0].subnetid}   True   ${TestData.myNetworksE2E[0].name}    ${TestData.myNetworksE2E[2].name}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # check for associated network in subnet
    #${Status}=    fusion_ui_verify_associated_networks_of_subnet    ${TestData.ippoolsE2E[1].subnetid}   ${TestData.myNetworksE2E[1].name}
    ${Status}=    Fusion Ui Verify Networks association or Disassociation To Subnet   ${TestData.ippoolsE2E[1].subnetid}   True   ${TestData.myNetworksE2E[1].name}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
#	Close All Browsers

2.Negative-Create Tagged network and try to associate with an already associated subnetID
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    ${Status}=    Run Keyword And Expect Error    *    fusion_ui_create_ethernet_network   ${TestData.myNetworksE2E[3]}
    Log To Console   ${Status}
    ${ExpMsg}=    set variable    Failed to wait for element 'xpath=//input[@id='cic-network-add-subnet-select-input']/..//div[@class='hp-search-combo-menu']/..//tr[td[text()='150.150.150.0']]'
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Should Be Equal   ${Status}   ${ExpMsg}   Expected Error not seen
    Log to Console    ==========================================================================
#	Close All Browsers

3.Negative-Create Untagged network and try to associate with an already associated subnetID
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    ${Status}=    Run Keyword And Expect Error    *    fusion_ui_create_ethernet_network   ${TestData.myNetworksE2E[4]}
    Log To Console   ${Status}
    ${ExpMsg}=    set variable    Failed to wait for element 'xpath=//input[@id='cic-network-add-subnet-select-input']/..//div[@class='hp-search-combo-menu']/..//tr[td[text()='200.200.200.0']]'
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Should Be Equal   ${Status}   ${ExpMsg}   Expected Error not seen
    Log to Console    ==========================================================================
#	Close All Browsers

4.Negative-Edit Tagged network to another subnetID
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    # create two networks with same vlan ID and subnet . Edit subnet of One.Error seen
    ${Status}=    fusion_ui_create_ethernet_network   ${TestData.myNetworksE2E[5]}    ${TestData.myNetworksE2E[6]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    fusion_ui_edit_ethernet_networks_capture_errors    ${TestData.myNetworksE2E[7]}
    Log To Console   ${Status}
    ${ExpMsg1}=    set variable    Network cannot be associated with subnet ${TestData.ippoolsE2E[3].subnetid}.
    ${ExpMsg2}=    set variable    One or more networks with the same VLAN ID 180 are associated with a subnet ${TestData.ippoolsE2E[5].subnetid}. Select subnet ${TestData.ippoolsE2E[5].subnetid} to be associated with this network.
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg1}=    Convert To Lowercase   ${ExpMsg1}
    ${ExpMsg2}=    Convert To Lowercase   ${ExpMsg2}
    Run Keyword and Continue on Failure   Should Contain    ${Status}    ${ExpMsg1}   Expected Error '${ExpMsg1}' Not seen
    Should Contain    ${Status}    ${ExpMsg2}   Expected Error '${ExpMsg2}' Not seen
    Log to Console    ==========================================================================
#	Close All Browsers

5.Positive-Create Tagged network , and edit to associated SubnetID
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    ${Status}=    fusion_ui_create_ethernet_network    ${TestData.myNetworksE2E[8]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #verify network
    ${Status}=    fusion_ui_verify_ethernet_network    ${TestData.myNetworksE2EVerify[3]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    fusion_ui_edit_ethernet_networks_capture_errors    ${TestData.myNetworksE2E[9]}
    Log To Console   ${Status}
    Log to Console    ==========================================================================
    #verify network
    ${Status}=    fusion_ui_verify_ethernet_network    ${TestData.myNetworksE2EVerify[4]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # check for associated network in subnet
    ${Status}=    Fusion Ui Verify Networks association or Disassociation To Subnet   ${TestData.ippoolsE2E[3].subnetid}  True   ${TestData.myNetworksE2E[9].newname}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
#	Close All Browsers

6.Positive-Create Untagged network , and edit to associated SubnetID
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    ${Status}=    fusion_ui_create_ethernet_network   ${TestData.myNetworksE2E[10]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #verify network
    ${Status}=    fusion_ui_verify_ethernet_network    ${TestData.myNetworksE2EVerify[5]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    fusion_ui_edit_ethernet_networks_capture_errors    ${TestData.myNetworksE2E[11]}
    Log To Console   ${Status}
    Log to Console    ==========================================================================
    #verify network
    ${Status}=    fusion_ui_verify_ethernet_network    ${TestData.myNetworksE2EVerify[6]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # check for associated network in subnet
    ${Status}=    Fusion Ui Verify Networks association or Disassociation To Subnet    ${TestData.ippoolsE2E[4].subnetid}   True    ${TestData.myNetworksE2E[11].newname}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
#	Close All Browsers

7.Positive-Delete subnet associated with a network-verify warning and association in warning
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    # F258_UI_TC_43, F258_UI_TC_44, F258_UI_TC_99, F258_UI_TC_133
    # delete subnet
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[0]}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg}=    Catenate  ${expectedmsg25}  ${TestData.ippoolsE2E[0].subnetid}  ${expectedmsg26}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    Fusion UI Logout of Appliance
    Login to Fusion appliance as Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[1]}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg}=    Catenate  ${expectedmsg25}  ${TestData.ippoolsE2E[1].subnetid}  ${expectedmsg26}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    Fusion UI Logout of Appliance
    Login to Fusion appliance as Administrator
    ${Status}=    Fusion Ui Delete Subnet Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[0].subnetid}   ${TestData.myNetworksE2E[0].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Delete Subnet Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[1].subnetid}   ${TestData.myNetworksE2E[1].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
#	Close All Browsers

8.Positive-Delete Network and verify unset in subnet
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    # F258_UI_TC_155, F258_UI_TC_156
    # delete the network with associated subnet
    ${Status}=    fusion_ui_delete_ethernet_network    ${TestData.myNetworksE2E[0]}   ${TestData.myNetworksE2E[1]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # check for dis associated network in subnet
    ${Status}=    Fusion Ui Verify Networks association or Disassociation To Subnet   ${TestData.ippoolsE2E[0].subnetid}   False  ${TestData.myNetworksE2E[0].name}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Networks association or Disassociation To Subnet   ${TestData.ippoolsE2E[1].subnetid}  False   ${TestData.myNetworksE2E[1].name}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
#	Close All Browsers

9.Delete networks and subnets
#	Load Test Data and Open Browser
	Login to Fusion appliance as Administrator
    ${Status}=    fusion_ui_delete_ethernet_network    ${TestData.myNetworksE2E[2]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # delete subnets
    ${Status}=    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[0]}   ${TestData.ippoolsE2E[1]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
#	Close All Browsers

CleanUP-Delete NETWORKS and SUBNETS-After network tests
 #   Load Test Data and Open Browser
    Login to Fusion appliance as Administrator
    Run Keyword And Ignore Error    fusion_ui_delete_ethernet_network   ${TestData.myNetworksE2EVerify[4]}   ${TestData.myNetworksE2EVerify[5]}  ${TestData.myNetworksE2EVerify[6]}   @{TestData.myNetworksE2E}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange    @{TestData.ippoolsE2E}
    Run Keyword And Ignore Error    Fusion UI Logout of Appliance
 #   Close All Browsers

# =======================================================================================================================
# ======================================user SCENATIOS =============================================================
# =======================================================================================================================

0.IpV4 Range Pools -User Privilege Tests - Login and Create users
 #   Load Test Data and Open Browser
    Set Log Level    TRACE
    Log Variables
    Login to Fusion Appliance As Administrator
    Fusion UI Create User  @{TestData.users}
    Log to Console    *********Test  - 0 Completed*********

0.IP Ranges create pre req subnet
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsuser[4]}
    Log To Console   ${Status}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Fusion UI Logout of Appliance
    Log to Console    ==========================================================================

1.login as NETWORK ADMINISTRATOR - Create ipv4 subnets and ranges
    # F258_UI_TC_164
    Login to Fusion Appliance As NetworkAdmin
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
    Login to Fusion Appliance As BackupAdmin
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
    Login to Fusion Appliance As ReadOnly
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
    Login to Fusion Appliance As ServerAdmin
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
    #${ExpectedErrorMessage5}=    Convert To Lowercase   ${expectedmsg22}
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
    Login to Fusion Appliance As StorageAdmin
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
    Login to Fusion Appliance As SoftwareAdmin
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
    Login to Fusion Appliance As specified user    CustomUser
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
    Login to Fusion Appliance As NetworkAdmin
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
    Fusion UI Logout of Appliance
    Login to Fusion appliance as Administrator
    ${Status}=    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsuser[0]}
    Log To Console   ${Status}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance

Final-Cleanup after user tests
    Login to Fusion Appliance As Administrator
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange    @{TestData.ippoolsuser}
    Log to Console    ==========================================================================
    Fusion UI Logout of Appliance


# =======================================================================================================================
# ======================================E2E SCENATIOS =============================================================
# =======================================================================================================================

Login as administrator and cleanUP-Before E2E tests
    Set Log Level    TRACE
    Log Variables
    Login to Fusion Appliance As Administrator
    Log to Console    *********Login Completed*********

    ${Status}=    fusion_ui_delete_logical_enclosure    ${TestData.lesE2E[0]}
    Log to console  ${Status}
    ${Status}=    fusion_ui_delete_enclosure_group   ${TestData.encgroupsE2E[0]}
    Log to console  ${Status}
    ${Status}=   Run Keyword And Ignore Error    fusion_ui_delete_logical_interconnect_group    ${TestData.ligsE2E[0]}
    Log to console  ${Status}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}   ${TestData.ippoolsedite2e[0]}

Positive-Create Subnet and verify-PreReq
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippoolsE2E[2]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog   ${TestData.ippoolsE2E[2]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsE2E[2]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

Positive-Edit subnet-PreReq
    # F258_UI_TC_09, F258_UI_TC_10, F258_UI_TC_11, F258_UI_TC_33, F258_UI_TC_51, F258_UI_TC_55, F258_UI_TC_77, F258_UI_TC_82, F258_UI_TC_87
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Edit Ipv4 Subnet And Addressrange    ${TestData.ippoolsedite2e[0]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after edit
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsedite2e[0]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsedite2e[0]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

#------------------------RANGE ASSOCIATION AND ALLOCATION-------------------------

1.Get allocated count and verify it is ZERO before creating LE
    Login to Fusion Appliance As Administrator
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}
    ${allocatedcount2}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[5].name}
    ${allocatedcount3}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[6].name}
    ${allocatedcount1}=    Convert To Integer   ${allocatedcount1}
    ${allocatedcount2}=    Convert To Integer   ${allocatedcount2}
    ${allocatedcount3}=    Convert To Integer   ${allocatedcount3}
    ${TotalAllocatedCount}=    Evaluate    ${allocatedcount1}+${allocatedcount2}+${allocatedcount3}
    Should be equal as numbers    ${TotalAllocatedCount}    0    Allocated count should be ZERO before LE creation but is '${TotalAllocatedCount}'

2.Create LIG and EG
    Login to Fusion Appliance As Administrator
    Log To Console    ******CREATE LIG**********
    ${Status}=    fusion_ui_create_tbird_logical_interconnect_group    ${TestData.ligsE2E[0]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log To Console    ******CREATE LIG operations completed**********
    Log To Console    ***********Create Enclosure Group*******************
    ${Status}=    fusion_ui_create_tbird_enclosure_group    ${TestData.encgroupsE2E[0]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    Log To Console    ******CREATE EG operations completed**********

Create LE
    Login to Fusion Appliance As Administrator
    Log To Console    ************Create LE**************************
    ${Status}=    Run Keyword And Ignore Error    fusion_ui_create_tbird_logical_enclosure    ${TestData.lesE2E[0]}
    Log To Console    ${Status}
    Log To Console    ******CREATE LE operations completed**********

3.Get allocated count and verify it is same as no of devices
    Login to Fusion Appliance As Administrator
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}
    ${allocatedcount2}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[5].name}
    ${allocatedcount1}=    Convert To Integer   ${allocatedcount1}
    ${allocatedcount2}=    Convert To Integer   ${allocatedcount2}
    ${TotalAllocatedCount}=    Evaluate    ${allocatedcount1}+${allocatedcount2}
    Should be equal as numbers    ${TotalAllocatedCount}    23    No.Of allocated IPs are ${TotalAllocatedCount} but total devices are 23!!

4.Get allocated count of disabled range and verify it is ZERO
    Login to Fusion Appliance As Administrator
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[6].name}
    Should Be Equal As Numbers    ${allocatedcount1}    0    IP has been allocated from range ${TestData.addressrangesE2E[9].name} though it is disabled!!Allocated count is ${allocatedcount1}

5.Verify IC IPv4 IPs are from custom ranges specified
    Login to Fusion Appliance As Administrator
    Log To Console   ****VERIFY THE IC IPV4 IP IS FROM CUSTOME RANGE DEFINED*********
    ${Status}=   fusion_ui_verify_ic_ipv4address_of_li_in_le_within_range_pool   ${TestData.lesE2E[0].name}   ${TestData.addressrangesE2E[4]}   ${TestData.addressrangesE2E[5]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   One or more of the IC ipv4 IPs are not from the custom range defined

6.Verify Server ILO IPv4 IPs are from custom ranges specified
    Login to Fusion Appliance As Administrator
    Log To Console   ****VERIFY THE SERVER ILO IPV4 IP IS FROM CUSTOME RANGE DEFINED*********
    ${Status}=   fusion_ui_verify_ilo_ipv4ips_of_servers_in_le_within_range_pool    ${TestData.lesE2E[0].name}   ${TestData.addressrangesE2E[4]}   ${TestData.addressrangesE2E[5]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   One or more of the Server ILO ipv4 IPs are not from the custom range defined

7.delete subnet and verify warning and association in warning
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg}=    Catenate  ${expectedmsg25}  ${TestData.ippoolsE2E[2].subnetid}  ${expectedmsg26}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    Fusion UI Logout of Appliance
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Delete Subnet Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.encgroupsE2E[0].name}    ${TestData.lesE2E[0].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

8.delete associated and allocated range and verify warning and association in dialog
    # F258_UI_TC_98, F258_UI_TC_101, F258_UI_TC_122, F258_UI_TC_136
    Login to Fusion Appliance As Administrator
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}
    ${allocatedcount2}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[5].name}
    Fusion UI Logout of Appliance
    Login to Fusion Appliance As Administrator
    ${Status}=    Run keyword If  ${allocatedcount1}>0   Fusion Ui Delete range Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}    ${TestData.encgroupsE2E[0].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Run Keyword If  ${Status}!=None   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Run keyword If   ${allocatedcount2}>0    Fusion Ui Delete range Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}    ${TestData.encgroupsE2E[0].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Run Keyword If  ${Status}!=None   Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

9.Edit Range in an existing subnet-Shrink
    # F258_UI_TC_81, F258_UI_TC_119
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Edit Ipv4 Addressrange In Subnet    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[0]}   ${TestData.addressrangesE2E[1]}   ${TestData.addressrangesE2E[2]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsgE2E}=    Convert To Lowercase   ${expectedmsg27}
    Should Contain   ${Status}   ${ExpMsgE2E}    Expected Error Message not Seen

10.Edit Range in an existing subnet-Grow
    # F258_UI_TC_117,
    Login to Fusion Appliance As Administrator
    ${Status}=    Fusion Ui Edit Ipv4 Addressrange In Subnet    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[3]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Addressranges Of Subnet In Edit Dialog    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[3]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Addressranges Of Subnet In Addressesidentifiers Page    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[3]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

11.delete LE,EG and verify allocated count becomes 0
    # F258_UI_TC_45, F258_UI_TC_92, F258_UI_TC_103, F258_UI_TC_135, F258_UI_TC_139, F258_UI_TC_140, F258_UI_TC_141
    Login to Fusion Appliance As Administrator
    ${Status}=    Run Keyword And Ignore Error    fusion_ui_delete_logical_enclosure    ${TestData.lesE2E[0]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg}=    Catenate  ${expectedmsg25}  ${TestData.ippoolsE2E[2].subnetid}  ${expectedmsg26}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    # verify allocated count is zero
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}
    Run Keyword And Continue On Failure    Should Be Equal   '${allocatedcount1}'   '0'   Allocated IP count should be Zero but is ${allocatedcount1}
    # verify allocated count is zero
    ${allocatedcount2}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[5].name}
    Run Keyword And Continue On Failure    Should Be Equal   '${allocatedcount2}'   '0'   Allocated IP count should be Zero but is ${allocatedcount2}
    # verify allocated count is zero
    ${allocatedcount3}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[6].name}
    Run Keyword And Continue On Failure    Should Be Equal   '${allocatedcount3}'   '0'   Allocated IP count should be Zero but is ${allocatedcount3}
    ${Status}=    fusion_ui_delete_enclosure_group   ${TestData.encgroupsE2E[0]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    ${Status}=   Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
