*** Settings ***
Documentation     Delete the resources
Suite Setup       Run Keywords  Suite Setup  Check Do Not Delete
Suite Teardown    Suite Teardown
Resource          resource.txt

*** Test Cases ***
C7000 UPT Delete Resources Check Appliance State
    [Documentation]  Check appliance State
    ${state}=  Get Appliance State
    Run keyword if  '${state}'=='STARTING'  Wait Until Keyword Succeeds  90m  1s  Appliance State Should Match  ((?i)OK)
    Run keyword if  '${state}'=='UPGRADE'  Wait Until Keyword Succeeds  90m  1s  Appliance State Should Match  ((?i)OK)

C7000 UPT Delete Resources Remove Profiles
    [Documentation]  Remove profiles
    Power off Servers in Profiles  ${all_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable   ${all_profiles}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

C7000 UPT Delete Resources Remove Storage Volumes
    [Documentation]  Remove SV
    ${resplist}=  Remove All Storage Volumes Async  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10

C7000 UPT Delete Resources Remove SVT
    [Documentation]  Remove SVT
    ${resplist} =  Remove ALL Storage Volume Templates Async

C7000 UPT Delete Resources Remove Storage Systems
    [Documentation]  Remove SS
    Remove ALL Storage Systems Async

C7000 UPT Delete Resources Remove Enclosures
    [Documentation]  Remove enclosures
    ${resp}=         Fusion Api Get Appliance Version
    ${mode_type}=    Set Variable  ${resp["modelNumber"]}
    Run Keyword If   '${mode_type}' == 'HPE OneView VM - VMware vSphere'
    ...              Remove All Enclosures Async  timeout=600  interval=5

C7000 UPT Delete Resources Remove EGS
    [Documentation]  Remove EGs
    Remove All Enclosure Groups

C7000 UPT Delete Resources Remove LIGs
    [Documentation]  Remove LIGs
    Remove All LIGs

C7000 UPT Delete Resources Remove Networks
    [Documentation]  Remove networks
    Remove All Network Sets
    Remove All Ethernet Networks
    Remove All FC Networks
    Remove All FCoE Networks

C7000 UPT Delete Resources Remove SAN Managers
    [Documentation]  Remove san managers
    Sleep    60s
    Remove ALL San Managers Async

C7000 UPT Delete Resources Remove Users
    [Documentation]  Remove users
    Log  Removing USERS  console=True
    ${users} =    Fusion Api Get User
    Log  users:${users}
    :FOR    ${user}    IN    @{users['members']}
    \        Log  Removing ${user}  console=True
    \        Continue For Loop If    '${user['userName']}'=='administrator'
    \        Continue For Loop If    '${user['userName']}'=='HardwareSetup'
    \        ${resp} =    Fusion Api Remove User    uri=${user['uri']}