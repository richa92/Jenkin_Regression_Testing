*** Settings ***
Documentation                   Delete Base Resouces
...                               Used as a "Stand Alone" cleanup job to remove all resources prior to next test

Library        FusionLibrary
Library        BuiltIn
Library        Collections
Library        json
Library        Dialogs
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables                ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}        16.114.209.223
${DATA_FILE}        ./Regression_Data.py


*** Test Cases ***
Login
    Set Log Level	TRACE
    ${admin_session} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${session} =    Get From List    ${admin_session}     0
    ${status}    ${error} =    Run Keyword And Ignore Error     Get From Dictionary     ${session}    message
    Run Keyword If     '${status}'=='PASS'    Fail    Unable to login: ${error}

Remove all Profiles and Templates
    Power off ALL servers    control=PressAndHold
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

Remove All Volumes
    # Remove all volumes
    ${resplist}=    Remove ALL Storage Volumes Async  param=?suppressDeviceUpdates=false
    Wait For Task2    ${resplist}    timeout=60    interval=5

Remove ALl Volume Templates
    # Remove all volume templates
    Remove ALL Storage Volume Templates Async

Remove All Storage Systems
    Remove ALL Storage Systems Async

Remove All Enclosures
    ${resp}=         Fusion Api Get Appliance Version
    ${mode_type}=    Set Variable  ${resp["modelNumber"]}
    Run Keyword If   '${mode_type}' == 'HPE OneView VM - VMware vSphere'
    ...              Remove All Enclosures Async    VERIFY=${True}  timeout=600  interval=5

Remove all Logical Enclosures
    Remove All LEs    force=${True}    timeout=1800    interval=10

Remove All EGS
    Remove All Enclosure Groups
    Sleep    30s    SAS LIGS still associated to

Remove all LIGs
    Remove All SAS LIGs
    Remove All LIGs

Remove all Networks
    Remove All Network Sets
    Remove All Ethernet Networks
    Remove All FC Networks
    Remove All FCoE Networks

Remove all SAN Managers
    Sleep    60s
    Remove ALL San Managers Async

Remove All Users
    Log    Removing USERS    console=true
    ${users} =    Fusion Api Get User
    Log    users:${users}    console=true
    :FOR    ${user}    IN    @{users['members']}
    \        Log    ${user}    console=true
    \        Continue For Loop If    '${user['userName']}'=='administrator'
    \        Continue For Loop If    '${user['userName']}'=='HardwareSetup'
    \        ${resp} = 	Fusion Api Remove User    uri=${user['uri']}

Remove All Licenses
    ${getlicresp} =    Fusion Api Get Licenses
    :FOR    ${eachlic}     IN    @{getlicresp['members']}
    \       ${delResp} =    Fusion Api Remove License   uri=${eachlic['uri']}
    \       ${status} =     Run Keyword And Return Status  Should Be Equal As Integers    ${delResp["status_code"]}   204
    \       Run Keyword If    '${status}'!='PASS'     Log    License remove failed:${eachlic}       WARN    console=true

Logout
    Fusion Api Logout Appliance