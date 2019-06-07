*** Settings ***
Documentation    Tests to remove Profiles, Enclosures, LIG
...              EG and Networks.
Resource                        resource.txt
Suite Setup                     Patch Suite Setup    ${admin_credentials}
Suite Teardown                  Patch Suite Teardown
*** Test Cases ***
Delete Profiles
    [Tags]    TEARDOWN    TBIRD   C7000   R-SP
    [Documentation]    Remove Profiles
     ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=600    interval=5
    Run Keyword If   ${responses} is not ${null}    Verify Server profile exists

Delete Base Storage Resources
    [Tags]    TEARDOWN    TBIRD   C7000   R-SB
    [Documentation]    Remove Storage Volumes, Template, Pools and Storage Systems
    Remove Storage Volumes Async   ${storage_volumes}  ?suppressDeviceUpdates=true
    Remove All Storage Volume Templates Async
    Remove ALL Storage Systems Async

Remove Logical Enclosure from OV
    [Documentation]     Remove Logical Enclosure from OV
    [Tags]    TBIRD   REMOVELE
    Remove All LEs Async
    Log All Warning and Critical Alerts

Delete Base Resources ENCLOSURES
    [Documentation]     Remove Enclosures
    [Tags]  TEARDOWN  C7000   R-ENC
    Remove All Enclosures async  ${VERIFY}  1200

Delete OS Deployment Servers
    [Documentation]     Remove San Manager
    [Tags]  TEARDOWN   I3S    TBIRD   R-OSDS
    Remove OS Deployment Server    ${deployment_server}

Delete Base Resources Enclosure Groups
    [Documentation]     Remove Enclosure Groups
    [Tags]  TEARDOWN   TBIRD   C7000   R-EG
    Remove All Enclosure Groups  ${VERIFY}

Delete Base Resources LIGs
    [Documentation]     Remove LIG
    [Tags]  TEARDOWN  TBIRD   C7000   R-LIG
    Remove All LIGs  ${VERIFY}

Delete Base Resources SASLIGs
    [Documentation]     Delete Base Resources SASLIGs
    [Tags]    TEARDOWN  TBIRD   C7000    R-SASLIG
    Remove All SAS LIGs   ${VERIFY}

Delete Base Resources I3S Networks
    [Documentation]     Remove Ethernet Networks
    [Tags]  TEARDOWN  I3S   R-I3S   TBIRD
    Remove Ethernet Networks Async    ${i3s_networks}   ${VERIFY}

Delete Base Resources Network Sets
    [Documentation]     Remove Network Sets
    [Tags]  TEARDOWN  TBIRD   C7000   R-NS
    Remove All Networks Sets Async  ${VERIFY}

Delete Base Resources Ethernet Networks
    [Documentation]     Remove Ethernet Networks
    [Tags]  TEARDOWN  TBIRD   C7000   R-ETH
    Remove Ethernet Networks Async    ${ethernet_networks}   ${VERIFY}

Remove FCOE Network
    [Documentation]     Remove FCOE Networks
    [Tags]  TEARDOWN  TBIRD   C7000   R-FCOE
    Remove All FCoE Networks
    ${resp} =  Fusion Api Get Fcoe Networks
    Run Keyword Unless  '${resp['count']}' == '0'    Fail     msg = Not All FCoE Networks were deleted

Delete Base Resources FC Networks
    [Documentation]     Remove FC Networks
    [Tags]  TEARDOWN  TBIRD   C7000   R-FC
    Remove All FC Networks Async  ${VERIFY}

Delete Base Resources SAN Manager
    [Documentation]     Remove San Manager
    [Tags]  TEARDOWN   TBIRD   C7000   R-SM
    Remove All San Managers Async  ${VERIFY}
