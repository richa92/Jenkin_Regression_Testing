*** Settings ***
Documentation    Negative Test cases for IPv4 Subnet and range Pool
Resource    TestConfig.txt
Force Tags    Buildup
Suite Setup    Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers
#Test Setup    Load Test Data and Open Browser
#Test Teardown    Logout And Close All Browsers
Library    RoboGalaxyLibrary
Library    FusionLibrary
Library    String

*** Test Cases ***

0.IPV4 Address Pool Negative Operations - Login as administrator and clean UP
    Set Log Level    TRACE
    Log Variables
    Log into Fusion Appliance As Administrator
    Log to Console    *********Login Completed*********
    # pre req clean up
    #Run Keyword And Ignore Error   Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippools2}

#=======================================================================================================================
#======================================NEGATIVE SCENATIOS =============================================================
#=======================================================================================================================

1.Negative-Create Subnet-invalid subnet mask
    # F258_UI_TC_47
    Log To Console     Abhishek----
    Log To Console    Get Element Text  ${expectedmsg2}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[0]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg1}=    Convert To Lowercase   ${expectedmsg2}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg1}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

2.Negative-Create Subnet-Invalid subnet ID for the given subnet
    # F258_UI_TC_46
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[1]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[1]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg2}=    Convert To Lowercase   ${expectedmsg3}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg2}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

3.Negative-Create Subnet-invalid gateway
    # F258_UI_TC_48
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[2]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[2]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg3}=    Convert To Lowercase   ${expectedmsg4}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg3}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

4.Negative-Create Subnet-Please enter at least 1 digit in each byte
    # F258_UI_TC_46, F258_UI_TC_47, F258_UI_TC_48, F258_UI_TC_49
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
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[4]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[4]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg5}=    Convert To Lowercase   ${expectedmsg6}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg5}  4   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

6.Negative-Create Subnet-Address not within specified subnet
    # F258_UI_TC_39, F258_UI_TC_40, F258_UI_TC_71, F258_UI_TC_72, F258_UI_TC_76
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
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[6]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[6]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg7}=    Convert To Lowercase   ${expectedmsg8}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg7}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

8.Negative-Create Subnet -Please enter at least 1 digit in each byte for address range
    # F258_UI_TC_58
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[7]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[7]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg4}=    Convert To Lowercase   ${expectedmsg5}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg4}  2   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

9.Negative-Create Subnet -Warning during range addition
    # F258_UI_TC_57
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[8]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[8]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg9}=    Convert To Lowercase   ${expectedmsg9}
    Run Keyword And Continue On Failure    Should Contain    ${Status}    ${ExpMsg9}    Expected Error Message not Seen
    Log to Console    ==========================================================================

10.Negative-Create Subnet -Empty address range fields
    #  F258_UI_TC_69, F258_UI_TC_70
    #Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[9]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[9]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg5}=    Convert To Lowercase   ${expectedmsg6}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg5}  3   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

11.Negative-Create Subnet-Broadcast IP as input in subnet fields
    # F258_UI_TC_27,F258_UI_TC_28,F258_UI_TC_29,F258_UI_TC_30
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[10]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[10]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg10}=    Convert To Lowercase   ${expectedmsg10}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg10}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

12.Negative-Create Subnet-Multicast IP as input in subnet fields
    # F258_UI_TC_19,F258_UI_TC_20,F258_UI_TC_21,F258_UI_TC_22
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[11]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[11]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg11}=    Convert To Lowercase   ${expectedmsg11}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg11}  5   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

13.Negative-Create Subnet-Gateway should be within subnet range
    #Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippools2[12]}
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[12]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg13}=    Convert To Lowercase   ${expectedmsg12}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg13}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

14.Negative-Create Subnet-Multicast IP as input range fields
    # F258_UI_TC_67, F258_UI_TC_68
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[13]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg11}=    Convert To Lowercase   ${expectedmsg11}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg11}  2   Expected Error Message not Seen expected no.of times.
   Log to Console    ==========================================================================

15.Negative-Create Subnet-Provide invalid Ips in subnet inputs
    # F258_UI_TC_75
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[14]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg14}=    Convert To Lowercase   ${expectedmsg13}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg14}  6   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

16.Negative-Create Subnet and range-Provide invalid Ips in range inputs
    # F258_UI_TC_75
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[15]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg14}=    Convert To Lowercase   ${expectedmsg13}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg14}  2   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

17.Negative-Create Subnet and range-range cannot contain Gateway
    # F258_UI_TC_63
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[16]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg15}=    Convert To Lowercase   ${expectedmsg14}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg15}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

18.Negative-Create Subnet and range-DNS should not be same as gateway
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[17]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${expmsg}=    Catenate    ${expectedmsg15}   ${TestData.ippools2[17].gateway},   ${expectedmsg16}
    ${expmsg}=    Convert To Lowercase   ${expmsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${expmsg}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

19.Negative-Create Subnet-Duplicate
    # F258_UI_TC_12,F258_UI_TC_36
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[18]}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[18]}
    log to console    ${Status}
    ${ExpMsg}=    Set Variable   The subnet for Network ID - ${TestData.ippools2[18].subnetid} and Subnet Mask - ${TestData.ippools2[18].subnetmask} is overlapping with the subnet for Network ID - ${TestData.ippools2[18].subnetid} and Subnet Mask - ${TestData.ippools2[18].subnetmask}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg}=    Convert To Lowercase   ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

20.Negative-Create Subnet-provide loop back address for subnet fields
    #F258_UI_TC_15,F258_UI_TC_16,F258_UI_TC_17,F258_UI_TC_18
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[19]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg19}=    Convert To Lowercase   ${expectedmsg17}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg19}  5   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

21.Negative-Create Subnet-provide loop back address for range fields
    # F258_UI_TC_65, F258_UI_TC_66
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[20]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg19}=    Convert To Lowercase   ${expectedmsg17}
    Run Keyword And Continue On Failure    Should Contain X Times   ${Status}   ${ExpMsg19}  2   Expected Error Message not Seen expected no.of times.
    Log to Console    ==========================================================================

22.Negative-Create Subnet-invalid domain name
    # F258_UI_TC_50,
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[21]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg20}=    Convert To Lowercase   ${expectedmsg18}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg20}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

23.Negative-Create Subnet-range name exists-within subnet
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[22]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg21}=    Convert To Lowercase   ${expectedmsg19}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg21}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

24.Negative-Create Subnet-range name exists-across subnet
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[23]}    ${TestData.ippools2[24]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg21}=    Convert To Lowercase   ${expectedmsg19}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg21}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

25.Negative-Create Subnet-overlapping ranges
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[25]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsg22}=    Convert To Lowercase   ${expectedmsg20}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg22}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

26.Negative-Create Subnet-Range cannot contain DNS-F258_UI_TC_63
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui create Ipv4 Subnet And Addressrange    ${TestData.ippools2[26]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${expmsg}=    Catenate    ${expectedmsg21}    ${TestData.ippools2[26].dns1},   ${TestData.ippools2[26].dns2},   ${TestData.ippools2[26].dns3}
    ${expmsg}=    Convert To Lowercase   ${expmsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${expmsg}   Expected Error Message not Seen.
    Log to Console    ==========================================================================

Clean up after Tests
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippools2}
