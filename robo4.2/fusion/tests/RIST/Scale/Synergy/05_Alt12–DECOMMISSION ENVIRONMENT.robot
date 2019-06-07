*** Settings ***
Documentation                   This Test Suite performs decommission/cleanup of the environmen by deleting resources
Resource                        resource.txt
Suite Setup                     Scale Suite Setup     ${scaleuser_credentials}
Suite Teardown                  Scale Suite Teardown

*** Test Cases ***
Delete Server Profiles
    [Tags]    TEARDOWN      DELETESP
    [Documentation]        Removes all Server Profiles from OV
    ${responses}=  Remove All Server Profiles Async
    Run Keyword for List with kwargs  ${responses}  Wait For Task2   timeout=1200    interval=10
    Run Keyword If   ${responses} is not ${Null}   Verify Server profile exists

Delete Server Profile Templates
    [Tags]    TEARDOWN      DELETESPT
    [Documentation]        Remove Server Profiles Templates for servers
    Remove All SPT
    Verify Server Profile Templates exist

Delete Logical Enclosures
    [Tags]    TEARDOWN      DELETELE
    [Documentation]        Remove Logical Enclosures from OneView
    Remove All LEs Async

Delete Logical Interconnect Groups
    [Tags]    TEARDOWN      DELETELIG
    [Documentation]        Remove All LIGs and SAS LIGs from OneView appliance
    Remove All LIGs     ${VERIFY}
    Remove All SAS LIGs      ${VERIFY}

Delete Storage Volumes
    [Tags]    TEARDOWN      DELETEVOL
    [Documentation]        Remove All Storage Volumes from OV
    ${response}=    Remove ALL Storage Volumes Async    ?suppressDeviceUpdates=false
    Run Keyword If  ${response} is not ${null}  Run Keyword for List    ${response}  Wait For Task2

Delete Storage Systems
    [Tags]    TEARDOWN      DELETESTORAGESSYS
    [Documentation]        Remove All Storage Systems from OV
    Remove All Storage Systems Async

Delete Network Sets
    [Tags]    TEARDOWN      DELETENETWORKSET
    [Documentation]        Remove NetworkSets from OneView appliance
    Remove All Networks Sets Async      ${VERIFY}

Delete FC Network
    [Tags]    TEARDOWN      DELETEFCNW
    [Documentation]        Remove FC Networks from OneView appliance
    Remove All FC Networks Async    ${VERIFY}

Delete FCOE Network
    [Tags]    TEARDOWN      DELETEFCOENW
    [Documentation]        Remove FCOE Networks from OneView appliance
    Remove All FCoE Networks
    ${resp} =   Fusion Api Get Fcoe Networks
    Run Keyword Unless  '${resp['count']}' == '0'    Fail     msg=Not All FCoE Networks were deleted

Delete Ethernet Network
    [Tags]    TEARDOWN      DELETEETHNW
    [Documentation]        Remove Ethernet Networks from OneView appliance
    Remove All Ethernet Networks Async  ${VERIFY}

Delete SAN Managers
    [Tags]    TEARDOWN      DELETESANMGR
    [Documentation]        Remove SAN Manager from OneView appliance
    Remove All San Managers Async     ${VERIFY}