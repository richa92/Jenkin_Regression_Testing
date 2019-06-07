*** Settings ***
Documentation                   Remove the resources
Resource                        resource.txt
Suite Setup                     Run Keywords  Suite Setup  Check Do Not Delete
Suite Teardown                  Suite Teardown

*** Test Cases ***
Syerngy UPT Delete Resources Check Appliance State
    [Documentation]  Check appliance State
    ${state}=  Get Appliance State
    Run keyword if  '${state}'=='STARTING'  Wait Until Keyword Succeeds  120m  1s  Appliance State Should Match  ((?i)OK)
    Run keyword if  '${state}'=='UPGRADE'  Wait Until Keyword Succeeds  120m  1s  Appliance State Should Match  ((?i)OK)

Syerngy UPT Delete Resources Remove Profiles
    [Documentation]  Remove profiles
    Power off Servers in Profiles  ${all_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${all_profiles}  force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5

Syerngy UPT Delete Resources Remove Storage Volumes
    [Documentation]  Remove SV
    ${resplist}=  Remove All Storage Volumes Async  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10

Syerngy UPT Delete Resources Remove SVT
    [Documentation]  Remove SVT
    ${resplist} =  Remove ALL Storage Volume Templates Async
    
Syerngy UPT Delete Resources Remove Storage Systems
    [Documentation]  Remove SS
    Remove ALL Storage Systems Async

Syerngy UPT Delete Resources Remove Logical Enclosures
    [Documentation]  Remove LE
    Remove All LEs    force=${True}    timeout=1800    interval=10

Syerngy UPT Delete Resources Remove EGs
    [Documentation]  Remove EG
    Remove All Enclosure Groups
    Sleep    30s    SAS LIGS still associated to

Syerngy UPT Delete Resources Remove LIGs
    [Documentation]  Remove LIG and SASLIG
    Remove All SAS LIGs
    Remove All LIGs

Syerngy UPT Delete Resources Remove Networks
    [Documentation]  Remove networks
    Remove All Network Sets
    Remove All Ethernet Networks
    Remove All FC Networks
    Remove All FCoE Networks

Syerngy UPT Delete Resources Remove SAN Managers
    [Documentation]  Remove san managers
    Sleep    60s
    Remove ALL San Managers Async

Syerngy UPT Delete Resources Remove Users
    [Documentation]  Remove users
    Log  Removing USERS  console=True
    ${users} =    Fusion Api Get User
    Log  users:${users}
    :FOR    ${user}    IN    @{users['members']}
    \        Log  Removing ${user}  console=True
    \        Continue For Loop If    '${user['userName']}'=='administrator'
    \        Continue For Loop If    '${user['userName']}'=='HardwareSetup'
    \        ${resp} = 	Fusion Api Remove User    uri=${user['uri']}
