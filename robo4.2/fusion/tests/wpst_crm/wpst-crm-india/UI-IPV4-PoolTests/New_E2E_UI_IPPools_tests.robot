*** Settings ***
Documentation    End to End Test cases for IPv4 Subnet and Range Pool
Resource    TestConfig.robot
Force Tags    Buildup
Suite Setup    Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers
Library    RoboGalaxyLibrary
Library    FusionLibrary
Library    String

*** Test Cases ***

0.IPV4 Address Pool-Login as administrator and clean UP
    Set Log Level    TRACE
    Log Variables
    Log into Fusion Appliance As Administrator
    Log to Console    *********Login Completed*********

CleanUP-Delete LE,EG,LIG,NETWORKS and SUBNETS
    ${Status}=    fusion_ui_delete_logical_enclosure    ${TestData.lesE2E[0]}
    Log to console  ${Status}
    ${Status}=    fusion_ui_delete_enclosure_group   ${TestData.encgroupsE2E[0]}
    Log to console  ${Status}
    ${Status}=   Run Keyword And Ignore Error    fusion_ui_delete_logical_interconnect_group    ${TestData.ligsE2E[0]}
    Log to console  ${Status}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}   ${TestData.ippoolsedite2e[0]}

Positive-Create Subnet and verify
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
    Fusion UI Logout of Appliance

Positive-Edit subnet
    #F258_UI_TC_09, F258_UI_TC_10, F258_UI_TC_11, F258_UI_TC_33, F258_UI_TC_51, F258_UI_TC_55, F258_UI_TC_77, F258_UI_TC_82, F258_UI_TC_87
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
    Fusion UI Logout of Appliance

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
    Fusion UI Logout of Appliance
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
    Fusion UI Logout of Appliance

Create LE
    Login to Fusion Appliance As Administrator
    Log To Console    ************Create LE**************************
    ${Status}=    Run Keyword And Ignore Error    fusion_ui_create_tbird_logical_enclosure    ${TestData.lesE2E[0]}
    Log To Console    ${Status}
    Log To Console    ******CREATE LE operations completed**********

3.Get allocated count and verify it is same as no of devices
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}
    ${allocatedcount2}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[5].name}
    ${allocatedcount1}=    Convert To Integer   ${allocatedcount1}
    ${allocatedcount2}=    Convert To Integer   ${allocatedcount2}
    ${TotalAllocatedCount}=    Evaluate    ${allocatedcount1}+${allocatedcount2}
    Should be equal as numbers    ${TotalAllocatedCount}    27    No.Of allocated IPs are ${TotalAllocatedCount} but total devices are 27!!

4.Get allocated count of disabled range and verify it is ZERO
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[6].name}
    Should Be Equal As Numbers    ${allocatedcount1}    0    IP has been allocated from range ${TestData.addressrangesE2E[9].name} though it is disabled!!Allocated count is ${allocatedcount1}

5.Verify IC IPv4 IPs are from custom ranges specified
    Log To Console   ****VERIFY THE IC IPV4 IP IS FROM CUSTOME RANGE DEFINED*********
    ${Status}=   fusion_ui_verify_ic_ipv4address_of_li_in_le_within_range_pool   ${TestData.lesE2E[0].name}   ${TestData.addressrangesE2E[4]}   ${TestData.addressrangesE2E[5]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   One or more of the IC ipv4 IPs are not from the custom range defined

6.Verify Server ILO IPv4 IPs are from custom ranges specified
    Log To Console   ****VERIFY THE SERVER ILO IPV4 IP IS FROM CUSTOME RANGE DEFINED*********
    ${Status}=   fusion_ui_verify_ilo_ipv4ips_of_servers_in_le_within_range_pool    ${TestData.lesE2E[0].name}   ${TestData.addressrangesE2E[4]}   ${TestData.addressrangesE2E[5]}
    Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   One or more of the Server ILO ipv4 IPs are not from the custom range defined

7.delete subnet and verify warning and association in warning
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg}=    Catenate  ${expectedmsg25}  ${TestData.ippoolsE2E[2].subnetid}  ${expectedmsg26}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    ${Status}=    Fusion Ui Delete Subnet Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.encgroupsE2E[0].name}    ${TestData.lesE2E[0].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

8.delete associated and allocated range and verify warning and association in dialog
    # F258_UI_TC_98, F258_UI_TC_101, F258_UI_TC_122, F258_UI_TC_136
    ${allocatedcount1}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[4].name}
    ${allocatedcount2}=    Fusion Ui Get Count Of allocatedip In Addressrange    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[5].name}
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
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Edit Ipv4 Addressrange In Subnet    ${TestData.ippoolsE2E[2].subnetid}    ${TestData.addressrangesE2E[0]}   ${TestData.addressrangesE2E[1]}   ${TestData.addressrangesE2E[2]}
    log to console    ${Status}
    ${Status}=    Convert To Lowercase   ${Status}
    ${ExpMsgE2E}=    Convert To Lowercase   ${expectedmsg27}
    Should Contain   ${Status}   ${ExpMsgE2E}    Expected Error Message not Seen
     Fusion UI Logout of Appliance

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
    Fusion UI Logout of Appliance

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

Final-CleanUP-Delete LE,EG,LIG,NETWORKS and SUBNETS
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[2]}   ${TestData.ippoolsedite2e[0]}
