*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to Teardown the appliance.
...     First Test is to unassign Server Profile before removing all the resources that were added in other EPIC MAT Test Suites.
...     TAGS:                      CLEAN UP
Library  time
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
#Variables                       ./data_variables_tbird.py

*** Test Cases ***

Remove Server Profiles Async
    [Tags]    TEARDOWN  REMOVEPROFILE
    [Documentation]        Remove All Server Profiles from OneView
    ${profiles} =    Fusion Api Get Server Profiles
    :FOR    ${profile}  IN  @{profiles['members']}
    \   Run Keyword If  '${profile['serverHardwareUri']}' == 'None'     Continue For Loop
    \   ${server} =   Fusion Api Get Server Hardware  uri=${profile['serverHardwareUri']}
    \   Power off Server    ${server['name']}
    ${responses} =  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}   timeout=3000    interval=15
    Run Keyword If  ${responses} is not ${Null}  Verify Server profile exists

Remove Server Profile Templates
    [Tags]    TEARDOWN  REMOVE-SPT
    [Documentation]        Remove Server Profiles Templates for servers
    Remove All SPT
    Verify Server Profile Templates exist

Remove Logical Enclosure from OV
    [Tags]    TEARDOWN  REMOVE-LE
    [Documentation]        Remove All LE from OneView appliance
    Remove All LEs

Remove EG
    [Tags]    TEARDOWN  REMOVE-EG
    [Documentation]        Remove Enclosure Group from OneView appliance
    Remove All Enclosure Groups     ${VERIFY}

Remove LIG
    [Tags]    TEARDOWN  REMOVE-LIG
    [Documentation]        Remove All LIGs and SAS LIGs from OneView appliance
    Remove All LIGS     ${VERIFY}
    Remove All SAS LIGs      ${VERIFY}

Remove Network Set
    [Tags]    TEARDOWN  REMOVE-NS
    [Documentation]        Remove NetworkSets from OneView appliance
    Remove All Networks Sets Async      ${VERIFY}

Remove FC Network
    [Tags]    TEARDOWN  REMOVE-FC
    [Documentation]        Remove FC Networks from OneView appliance
    Remove All FC Networks Async    ${VERIFY}

Remove FCOE Network
    [Tags]    TEARDOWN  REMOVE-FCOE
    [Documentation]        Remove FCOE Networks from OneView appliance
    Remove All FCoE Networks
    ${resp} =   Fusion Api Get Fcoe Networks
    Run Keyword Unless  '${resp['count']}' == '0'    Fail     msg=Not All FCoE Networks were deleted

Remove Ethernet Network
    [Tags]    TEARDOWN  REMOVE-ETH
    [Documentation]        Remove Ethernet Networks from OneView appliance
    Remove All Ethernet Networks Async  ${VERIFY}

Remove Storage Volume
    [Tags]    TEARDOWN  REMOVE-VOL
    [Documentation]        Remove Existing Storage Volumes from OneView only and Storage Volumes from OneView and storage system
    ${response_e} =  Remove Storage Volumes Async  ${existing_storage_volumes}   ?suppressDeviceUpdates=true
    ${response_n} =  Remove Storage Volumes Async  ${storage_volumes}  ?suppressDeviceUpdates=false
    Run Keyword If  ${response_e} is not ${null}  Wait For Task2  ${response_e}
    Run Keyword If  ${response_n} is not ${null}  Wait For Task2  ${response_n}
    ${response} =   Remove ALL Storage Volumes Async    ?suppressDeviceUpdates=true
    Run Keyword If  ${response} is not ${null}  Run Keyword for List    ${response}  Wait For Task2

Remove Storage Volume Templates
    [Tags]    TEARDOWN  REMOVE-SVT
    [Documentation]        Remove Storage Volume Template from OneView appliance
    Remove All Storage Volume Templates Async

Remove Storage System
    [Tags]    TEARDOWN  REMOVE-SYS
    [Documentation]        Remove Storage System from OneView appliance
    Remove All Storage Systems Async

Remove San Manager
    [Tags]    TEARDOWN  REMOVE-SM
    [Documentation]        Remove SAN Manager from OneView appliance
    Remove All San Managers Async     ${VERIFY}

#Remove SPP
#    [Tags]   TEARDOWN  REMOVESPP
#    [Documentation]        Remove SPP from OneView appliance
#    Delete SPP From Fusion    ${APPLIANCE_IP}    ${admin_credentials['userName']}     ${admin_credentials['password']}      ${spp_details['spp']}

Remove Users
    [Tags]    TEARDOWN  REMOVEUSER
    [Documentation]        Remove Users from OneView appliance
    Remove All Users    ${VERIFY}