*** Settings ***
Documentation    End to End Test cases for IPv4 Subnet and Range Pool
Resource    TestConfig.robot
Force Tags    Buildup
Test Setup    Load Test Data and Open Browser
Test Teardown    Logout And Close All Browsers
Library    RoboGalaxyLibrary
Library    FusionLibrary
Library    String

*** Test Cases ***

0.IPV4 Address Pool-Login as administrator and clean UP
    Set Log Level    TRACE
    Log Variables
    Login to Fusion appliance as Administrator
    Log to Console    *********Login Completed*********

CleanUP-Delete LE,EG,LIG,NETWORKS and SUBNETS
    Login to Fusion appliance as Administrator
    Run Keyword And Ignore Error    fusion_ui_delete_ethernet_network   ${TestData.myNetworksE2EVerify[4]}   ${TestData.myNetworksE2EVerify[5]}  ${TestData.myNetworksE2EVerify[6]}   @{TestData.myNetworksE2E}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippoolsE2E}

Positive-Create Subnet and verify\
    Login to Fusion appliance as Administrator
    ${Status}=    Fusion Ui create Ipv4 Subnet And Addressrange    @{TestData.ippoolsE2E}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    #Verify subnet and address range after creation
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Edit Dialog    ${TestData.ippoolsE2E[0]}   ${TestData.ippoolsE2E[1]}    ${TestData.ippoolsE2E[3]}   ${TestData.ippoolsE2E[4]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Verify Ipv4 Subnet And Addressrange In Addressesidentifiers Page    ${TestData.ippoolsE2E[0]}   ${TestData.ippoolsE2E[1]}    ${TestData.ippoolsE2E[3]}   ${TestData.ippoolsE2E[4]}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

#---------------Subnet - NETWORK(TAGGED/UNTAGGED) association-------------------

1.Positive-Create Network and associate Subnet-Verify association
    Login to Fusion appliance as Administrator
    # F258_UI_TC_143, F258_UI_TC_145, F258_UI_TC_146, F258_UI_TC_147, F258_UI_TC_159
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

2.Negative-Create Tagged network and try to associate with an already associated subnetID
    Login to Fusion appliance as Administrator
    ${Status}=    Run Keyword And Expect Error    *    fusion_ui_create_ethernet_network   ${TestData.myNetworksE2E[3]}
    Log To Console   ${Status}
    ${ExpMsg}=    set variable    Failed to wait for element 'xpath=//input[@id='cic-network-add-subnet-select-input']/..//div[@class='hp-search-combo-menu']/..//tr[td[text()='150.150.150.0']]'
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Should Be Equal   ${Status}   ${ExpMsg}   Expected Error not seen
    Log to Console    ==========================================================================

3.Negative-Create Untagged network and try to associate with an already associated subnetID
    Login to Fusion appliance as Administrator
    ${Status}=    Run Keyword And Expect Error    *    fusion_ui_create_ethernet_network   ${TestData.myNetworksE2E[4]}
    Log To Console   ${Status}
    ${ExpMsg}=    set variable    Failed to wait for element 'xpath=//input[@id='cic-network-add-subnet-select-input']/..//div[@class='hp-search-combo-menu']/..//tr[td[text()='200.200.200.0']]'
    ${Status}=    Convert To Lowercase    ${Status}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Should Be Equal   ${Status}   ${ExpMsg}   Expected Error not seen
    Log to Console    ==========================================================================

4.Negative-Edit Tagged network to another subnetID
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

5.Positive-Create Tagged network , and edit to associated SubnetID
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

6.Positive-Create Untagged network , and edit to associated SubnetID
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

7.Positive-Delete subnet associated with a network-verify warning and association in warning
    Login to Fusion appliance as Administrator
    # F258_UI_TC_43, F258_UI_TC_44, F258_UI_TC_99, F258_UI_TC_133
    # delete subnet
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[0]}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg}=    Catenate  ${expectedmsg25}  ${TestData.ippoolsE2E[0].subnetid}  ${expectedmsg26}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    ${Status}=    Run Keyword And Expect Error    *    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[1]}
    ${Status}=    Convert To Lowercase   '${Status}'
    ${ExpMsg}=    Catenate  ${expectedmsg25}  ${TestData.ippoolsE2E[1].subnetid}  ${expectedmsg26}
    ${ExpMsg}=    Convert To Lowercase    ${ExpMsg}
    Run Keyword And Continue On Failure    Should Contain    ${Status}   ${ExpMsg}   Expected Error Message not Seen.
    ${Status}=    Fusion Ui Delete Subnet Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[0].subnetid}   ${TestData.myNetworksE2E[0].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    ${Status}=    Fusion Ui Delete Subnet Verify warnIng And Associations In Dialog    ${TestData.ippoolsE2E[1].subnetid}   ${TestData.myNetworksE2E[1].name}
    log to console    ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

8.Positive-Delete Network and verify unset in subnet
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

9.Delete networks and subnets
    Login to Fusion appliance as Administrator
    ${Status}=    fusion_ui_delete_ethernet_network    ${TestData.myNetworksE2E[2]}
    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================
    # delete subnets
    ${Status}=    Fusion Ui Delete Ipv4 Subnet And Addressrange   ${TestData.ippoolsE2E[0]}   ${TestData.ippoolsE2E[1]}
    Log To Console   ${Status}
    Run Keyword And Continue On Failure    Should Be Equal   '${Status}'   'True'   ${Status}
    Log to Console    ==========================================================================

Final CleanUP-Delete LE,EG,LIG,NETWORKS and SUBNETS
    Login to Fusion appliance as Administrator
    Run Keyword And Ignore Error    fusion_ui_delete_ethernet_network   ${TestData.myNetworksE2EVerify[4]}   ${TestData.myNetworksE2EVerify[5]}  ${TestData.myNetworksE2EVerify[6]}   @{TestData.myNetworksE2E}
    Run Keyword And Ignore Error    Fusion Ui Delete Ipv4 Subnet And Addressrange   @{TestData.ippoolsE2E}
