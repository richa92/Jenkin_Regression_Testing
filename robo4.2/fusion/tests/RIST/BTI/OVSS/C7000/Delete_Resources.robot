*** Settings ***
Documentation     Delete Base and Storage Resources
Resource          resource.txt
Suite Setup       Suite Setup
Suite Teardown    Suite Teardown

*** Test Cases ***
C7000 OVSS Delete Resources Remove Profiles
    [Documentation]  Remove profiles
    Power off ALL servers    control=PressAndHold
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5

C7000 OVSS Delete Resources Remove Storage Volumes
    [Documentation]  Remove SV
    ${resplist}=  Remove All Storage Volumes Async  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10

C7000 OVSS Delete Resources Remove SVT
    [Documentation]  Remove SVT
    ${resplist} =  Remove ALL Storage Volume Templates Async

C7000 OVSS Delete Resources Remove Storage Systems
    [Documentation]  Remove SS
    Remove ALL Storage Systems Async

C7000 OVSS Delete Resources Remove Enclosures
    [Documentation]  Remove enclosures
    ${resp}=         Fusion Api Get Appliance Version
    ${mode_type}=    Set Variable  ${resp["modelNumber"]}
    Run Keyword If   '${mode_type}' == 'HPE OneView VM - VMware vSphere'
    ...              Remove All Enclosures Async  timeout=600  interval=5

C7000 OVSS Delete Resources Remove EGS
    [Documentation]  Remove EGs
    Remove All Enclosure Groups

C7000 OVSS Delete Resources Remove LIGs
    [Documentation]  Remove LIGs
    Remove All LIGs

C7000 OVSS Delete Resources Remove Networks
    [Documentation]  Remove networks
    Remove All Network Sets
    Remove All Ethernet Networks
    Remove All FC Networks
    Remove All FCoE Networks

C7000 OVSS Delete Resources Remove SAN Managers
    [Documentation]  Remove san managers
    Sleep    60s
    Remove ALL San Managers Async