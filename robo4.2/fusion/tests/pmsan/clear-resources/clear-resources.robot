*** Settings ***
Documentation   Clear resources from appliance
...             - Deletes all profiles
...             - Deletes all storage volumes, all storage volume templates
...             - Removes all storage systems
...             - Removes logical enclosures, enclosures, LIGs, deletes networks, removes SAN managers
...             = USAGE =
...             | pybot | -v  APPLIANCE_IP:<IP> | -v DATA_FILE:data/preCheckIn-1200.py | .\clear-resources.robot
...             = Variables =
...             | APPLIANCE_IP | Required; IP address of the OneView appliance to use |
...             | DATA_FILE  | The data file to use for test run.  Contains variable definitions that may vary from system to system. |

Resource        ../../../Resources/api/fusion_api_resource.txt

Variables       ${DATA_FILE}

*** Test Cases ***
Log into the appliance
    Set Log Level       TRACE
    Fusion Api Login Appliance      ${APPLIANCE_IP}     ${ADMIN_CREDENTIALS}

Delete Profiles
    [Tags]    TEARDOWN    TBIRD   C7000   R-SP
    [Documentation]    Remove Profiles
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=600    interval=5
    Run Keyword If   ${responses} is not ${null}    Verify Server profile exists

Delete Base Storage Resources
    [Tags]    TEARDOWN    TBIRD   C7000   R-SB
    [Documentation]    Remove Storage Volumes, Template, Pools and Storage Systems
    ${responses}=   Remove All Storage Volumes Async    param=?suppressDeviceUpdates=false
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=600    interval=5
    Run Keyword If   ${responses} is not ${null}    Verify Server profile exists

    Remove All Storage Volume Templates Async
    Remove ALL Storage Systems Async

Delete Base Resources ENCLOSURES
    [Documentation]     Remove Enclosures
    [Tags]  TEARDOWN  C7000   R-ENC
    Remove All Enclosures async  ${VERIFY}  1200

Remove Logical Enclosure from OV
    [Documentation]     Remove Logical Enclosure from OV
    [Tags]    TBIRD   REMOVELE
    Remove All LEs Async
    Log All Warning and Critical Alerts

Delete Base Resources Enclosure Groups
    [Documentation]     Remove Enclosure Groups
    [Tags]  TEARDOWN   TBIRD   C7000   R-EG
    Remove All Enclosure Groups  ${VERIFY}

Delete Base Resources LIGs
    [Documentation]     Remove LIG
    [Tags]  TEARDOWN  TBIRD   C7000   R-LIG
    Remove All LIGs  ${VERIFY}

#Delete OS Deployment Servers
#    [Documentation]     Remove San Manager
#    [Tags]  TEARDOWN   TBIRD   C7000    R-OSDS
#    Remove OS Deployment Servers    ${deployment_server}

#Delete Base Resources Network Sets
#    [Documentation]     Remove Network Sets
#    [Tags]  TEARDOWN  TBIRD   C7000   R-NS
#    Remove All Networks Sets Async  ${VERIFY}

Delete Base Resources Ethernet Networks
    [Documentation]     Remove Ethernet Networks
    [Tags]  TEARDOWN  TBIRD   C7000   R-ETH
    Remove All Ethernet Networks Async

#Delete Base Resources I3S Networks
#    [Documentation]     Remove Ethernet Networks
#    [Tags]  TEARDOWN  I3S   R-I3S   TBIRD
#    Remove Ethernet Networks Async    ${i3s_networks}   ${VERIFY}

#Remove FCOE Network
#    [Documentation]     Remove FCOE Networks
#    [Tags]  TEARDOWN  TBIRD   C7000   R-FCOE
#    Remove All FCoE Networks
#    ${resp} =  Fusion Api Get Fcoe Networks
#    Run Keyword Unless  '${resp['count']}' == '0'    Fail     msg = Not All FCoE Networks were deleted

Delete Base Resources FC Networks
    [Documentation]     Remove FC Networks
    [Tags]  TEARDOWN  TBIRD   C7000   R-FC
    Remove All FC Networks Async  ${VERIFY}

Delete Base Resources SAN Manager
    [Documentation]     Remove San Manager
    [Tags]  TEARDOWN   TBIRD   C7000   R-SM
    Remove All San Managers Async  ${VERIFY}

Logout of the appliance
    Fusion Api Logout Appliance