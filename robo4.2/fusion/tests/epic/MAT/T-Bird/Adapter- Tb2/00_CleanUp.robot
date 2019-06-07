*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to Teardown the appliance.
...     First Test is to unassign Server Profile before removing all the resources that were added in other EPIC MAT Test Suites.
...     TAGS:                      CLEAN UP
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***

Remove Server Profiles Async
    [Tags]    TEARDOWN  REMOVEPROFILE
    [Documentation]     Remove Server Profiles for BL and DL servers
    ${profiles} =    Fusion Api Get Server Profiles
    :FOR    ${profile}  IN  @{profiles['members']}
    \   Run Keyword If  '${profile['serverHardwareUri']}' == 'None'     Continue For Loop
    \   ${server} =   Fusion Api Get Server Hardware  uri=${profile['serverHardwareUri']}
    \   Power off Server    ${server['name']}
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=5
    Run Keyword If   ${responses} is not ${Null}   Verify Server profile exists

Remove Logical Enclosure from OV
    [Tags]    TEARDOWN  REMOVELE
    [Documentation]        Remove Logical Enclosures from OneView
    Remove All LEs Async

Delete Base Storage Resources
    [Tags]    TEARDOWN        DELETE-STORAGE-BASE
    [Documentation]        Remove Storage Volumes,Template, Pools and Storage Systems
    Remove ALL Storage Systems Async

Remove EG
    [Tags]    TEARDOWN  REMOVE-EG
    [Documentation]        Remove Enclosure Group from OneView appliance
    Remove All Enclosure Groups     ${VERIFY}

Remove LIG
    [Tags]    TEARDOWN  REMOVE-LIG
    [Documentation]        Remove All LIGs and SAS LIGs from OneView appliance
    Remove All LIGS     ${VERIFY}

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

Remove San Manager
    [Tags]    TEARDOWN  REMOVE-SM
    [Documentation]        Remove SAN Manager from OneView appliance
    Remove All San Managers Async     ${VERIFY}

Remove Users
    [Tags]    TEARDOWN  REMOVEUSER
    [Documentation]        Remove Users from OneView appliance
    Remove All Users    ${VERIFY}
