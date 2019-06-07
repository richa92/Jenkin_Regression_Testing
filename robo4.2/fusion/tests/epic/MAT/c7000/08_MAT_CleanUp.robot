*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to Teardown the appliance.
...     First Test is to unassign Server Profile before removing all the resources that were added in other EPIC MAT Test Suites.
...     TAGS:                      CLEAN UP
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Remove Server Profiles Async
    [Tags]    R-PROFILE
    [Documentation]     Remove Server Profiles for BL and DL servers
    Power off Servers in Profiles   ${server_profiles}
    Power off Servers in Profiles   ${dl_server_profiles}
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=5
    Run Keyword If   ${responses} is not ${Null}   Verify Server profile exists

Remove DL Servers from OV
    [Tags]    R-DLSERVER
    Remove All DL Server Hardware Async  ${VERIFY}  404  (?i)DL360 Gen9|DL360p Gen8|DL380p Gen8|DL380e Gen8|DL360 Gen9

Remove SPP
    [Tags]  R-SPP
    #Delete SPP From Fusion    ${APPLIANCE_IP}    ${admin_credentials['userName']}     ${admin_credentials['password']}      ${updated_spp_name}
    ${responses} =  Remove All Firmware Bundles
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}

Remove Enclosure from OV Async
    [Tags]    R-ENC
    Remove All Enclosures async  ${VERIFY}  timeout=500    interval=10

Remove EG
    [Tags]    R-EG
    Remove All Enclosure Groups     ${VERIFY}

Remove LIG
    [Tags]    R-LIG
    Remove All LIGS     ${VERIFY}

Remove Network Set
    [Tags]    R-NS
    Remove All Networks Sets Async      ${VERIFY}

Remove FC Network
    [Tags]    R-FC
    Remove All FC Networks Async    ${VERIFY}

Remove FCOE Network
    [Tags]    R-FCOE
    Remove All FCoE Networks
    ${resp} =   Fusion Api Get Fcoe Networks
    Run Keyword Unless  '${resp['count']}' == '0'    Fail     msg=Not All FCoE Networks were deleted

Remove Ethernet Network
    [Tags]    R-ETH
    Remove All Ethernet Networks Async  ${VERIFY}

Remove Storage Volume
    [Tags]    R-SVOL
    Remove All Storage Volumes Async    ?suppressDeviceUpdates=true

Remove Storage System
    [Tags]    R-SSYS
    Remove ALL Storage Systems Async

Remove San Manager
    [Tags]    R-SM
    Remove All San Managers Async  ${VERIFY}

Remove Users
    [Tags]    R-USER
    Remove All Users    ${VERIFY}

Remove Licenses
    [Tags]    R-LICENSE
    Delete All Fusion License     ${VERIFY}

