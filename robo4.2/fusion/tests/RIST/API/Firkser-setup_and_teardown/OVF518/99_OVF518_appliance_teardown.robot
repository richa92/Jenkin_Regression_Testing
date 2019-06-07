*** Settings ***
Documentation  Teardown for OVF518 Test Suite

Library  	        BuiltIn
Library		        FusionLibrary
Library		        Collections
Library             json
Resource            ./../../../../../Resources/api/fusion_api_resource.txt
Resource            ./../../global_variables.robot
Variables           ./../../OVF518/${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

Suite Teardown      Run Keywords    Fusion Api Logout Appliance


*** Variables ***
${APPLIANCE_IP}     ${None}
${DATA_FILE}        ${None}


*** Test Cases ***
01 Remove the Profiles
    Power off ALL servers
    ${resplist} =  Remove All Server Profiles Async  force=${True}
    Wait For Task2  ${resplist}  timeout=1500  interval=5

02 Remove the Templates
    Remove All Server Profile Templates Async

03 Remove LEs
    Remove all LEs

04 Remove EGs
    Remove all Enclosure Groups

05 Remove LIGs
    Remove all LIGs

06 Remove All Volumes
    ${resplist} =  Remove ALL Storage Volumes Async  param=?suppressDeviceUpdates=false
    Wait For Task2  ${resplist}  timeout=60  interval=5

07 Remove All Storage Systems
    Remove ALL Storage Systems Async

08 Remove Ethernet Networks
    Remove All Ethernet Networks

09 Remove FCoE Networks
    Remove All FCoE Networks

10 Remove Fibre Channel Networks
    Remove All FC Networks


*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
