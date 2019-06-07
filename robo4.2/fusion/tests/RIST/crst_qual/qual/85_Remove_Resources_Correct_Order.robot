*** Settings ***
Documentation    Remove Resources Correct Order
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Remove All Users
    [Tags]  85    RM_USERS
    Log    Removing USERS    console=${CONSOLE}
    ${users} =    Fusion Api Get User
    Log    users:${users}    console=${CONSOLE}
    :FOR    ${user}    IN    @{users['members']}
    \        Log    ${user}    console=${CONSOLE}
    \        Continue For Loop If    '${user['userName']}'=='administrator'
    \        Continue For Loop If    '${user['userName']}'=='HardwareSetup'
    \        ${resp} = 	Fusion Api Remove User    uri=${user['uri']}

Remove All Licenses
    [Tags]    85    RM_LICENSES
    ${getlicresp} =    Fusion Api Get Licenses
    :FOR    ${eachlic}     IN    @{getlicresp['members']}
    \       ${delResp} =    Fusion Api Remove License   uri=${eachlic['uri']}
    \       ${status} =     Run Keyword And Return Status  Should Be Equal As Integers    ${delResp["status_code"]}   204
    \       Run Keyword If    '${status}'!='PASS'     Log    License remove failed:${eachlic}       level=WARN    console=${CONSOLE}

Remove Firmware Bundles
    [Tags]   85    RM_FW
    Remove All Firmware Bundles

Remove Server Profiles
    [Tags]    85    RM_SP
    Wait For ALL Servers Complete Refresh
    ${resp} =    Remove All Server Profiles Async
    Wait For Task2    ${resp}    timeout=600    interval=20

Remove Rack Servers
    [Tags]    85    RM_DL
    Wait For ALL Servers Complete Refresh
    Remove All DL Server Hardware Async

Remove Logical Switches
    [Tags]    85    RM_LS
    Remove All LS

Remove Logical Switch Groups
    [Tags]    85    RM_LSG
    Remove All LSGs

Remove all Networks
    [Tags]    85    RM_NET
    Remove All Network Sets
    Remove All Ethernet Networks Async
    ${eth_networks}=    Fusion Api Get Ethernet Networks
    Should Be Equal As Integers    ${eth_networks["count"]}    0
    Remove All FC Networks
    Remove All FCoE Networks