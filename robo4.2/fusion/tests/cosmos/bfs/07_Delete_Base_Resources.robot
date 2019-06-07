*** Settings ***
Documentation    Tests to remove Profiles, Enclosures, LIG
...              EG and Networks.
Resource                           resource.txt
Suite Setup                     BFS OV Suite Setup     ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown
*** Test Cases ***
Remove Server Profiles Async
    [Documentation]        Remove All Server Profiles from OneView
    [Tags]    TEARDOWN  REMOVEPROFILE
    ${profiles} =    Fusion Api Get Server Profiles
    :FOR    ${profile}  IN  @{profiles['members']}
    \   Run Keyword If  '${profile['serverHardwareUri']}' == 'None'     Continue For Loop
    \   ${server} =   Fusion Api Get Server Hardware  uri=${profile['serverHardwareUri']}
    \   Power off Server    ${server['name']}
    ${responses} =  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}   timeout=3000    interval=15
    Run Keyword If  ${responses} is not ${Null}  Verify Server profile exists

Remove SPP
    [Documentation]        Remove All SPP file from OV
    [Tags]  REMOVESPP
    #Delete SPP From Fusion    ${APPLIANCE_IP}    ${admin_credentials['userName']}     ${admin_credentials['password']}      ${updated_spp_name}
    ${responses} =  Remove All Firmware Bundles
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}

Delete Base Storage Resources
    [Tags]    TEARDOWN    R-SB
    [Documentation]    Remove Storage Volumes, Template, Pools and Storage Systems
    Remove Storage Volumes Async   ${delete_storage_volumes_from_OV_only}  ?suppressDeviceUpdates=true
    Remove All Storage Volume Templates Async
    Remove ALL Storage Systems Async

Remove Logical Enclosure from OV
    [Documentation]     Remove Logical Enclosure from OV
    [Tags]    REMOVELE  Synergy
    Remove All LEs Async

Delete Base Resources ENCLOSURES
    [Documentation]     Remove Enclosures
    [Tags]  TEARDOWN  R-ENC  C7K
    Remove All Enclosures async  ${VERIFY}  timeout=600

Delete Base Resources Enclosure Groups
    [Documentation]     Remove Enclosure Groups
    [Tags]  TEARDOWN   R-EG
    Remove All Enclosure Groups  ${VERIFY}

Delete Base Resources LIGs
    [Documentation]     Remove LIG
    [Tags]  TEARDOWN  R-LIG
    Remove All LIGs  ${VERIFY}

Delete Base Resources Ethernet Networks
    [Documentation]     Remove Ethernet Networks
    [Tags]  TEARDOWN  R-ETH
    Remove All Ethernet Networks Async  ${VERIFY}

Remove FCOE Network
    [Documentation]     Remove FCOE Networks
    [Tags]  TEARDOWN  R-FCOE
    Remove All FCoE Networks
    ${resp} =  Fusion Api Get Fcoe Networks
    Run Keyword Unless  '${resp['count']}' == '0'    Fail     msg = Not All FCoE Networks were deleted

Delete Base Resources FC Networks
    [Documentation]     Remove FC Networks
    [Tags]  TEARDOWN  R-FC
    Remove All FC Networks Async  ${VERIFY}

Delete Base Resources SAN Manager
    [Documentation]     Remove San Manager
    [Tags]  TEARDOWN   R-SM
    Remove All San Managers Async  ${VERIFY}
