*** Settings ***
Documentation                   Delete Base and Storage Resources
Resource                        resource.txt
Suite Setup                     Suite Setup
Suite Teardown                  Suite Teardown

*** Test Cases ***
Syerngy OVSS Delete Resources Remove Profiles
    [Documentation]  Remove profiles
    Power off ALL servers    control=PressAndHold
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5

Syerngy OVSS Delete Resources Remove Storage Volumes
    [Documentation]  Remove SV
    ${resplist}=  Remove All Storage Volumes Async  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10

Syerngy OVSS Delete Resources Remove SVT
    [Documentation]  Remove SVT
    ${resplist} =  Remove ALL Storage Volume Templates Async
    
Syerngy OVSS Delete Resources Remove Storage Systems
    [Documentation]  Remove SS
    Remove ALL Storage Systems Async

Syerngy OVSS Delete Resources Remove Logical Enclosures
    [Documentation]  Remove LE
    Remove All LEs    force=${True}    timeout=1800    interval=10

Syerngy OVSS Delete Resources Remove EGs
    [Documentation]  Remove EG
    Remove All Enclosure Groups
    Sleep    30s    SAS LIGS still associated to

Syerngy OVSS Delete Resources Remove LIGs
    [Documentation]  Remove LIG and SASLIG
    Remove All SAS LIGs
    Remove All LIGs

Syerngy OVSS Delete Resources Remove Networks
    [Documentation]  Remove networks
    Remove All Network Sets
    Remove All Ethernet Networks
    Remove All FC Networks
    Remove All FCoE Networks

Syerngy OVSS Delete Resources Remove SAN Managers
    [Documentation]  Remove san managers
    Sleep    60s
    Remove ALL San Managers Async
