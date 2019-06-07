*** Settings ***
Documentation  Teardown for OVF518 Test Suite

Library  	        BuiltIn
Library		        FusionLibrary
Library		        Collections
Library             json
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./../global_variables.robot
Variables           ${DATA_FILE}

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

03 Remove the OVF518 Resources
    [Tags]    RemoveResources

    :FOR    ${eg}    IN    @{egs}
    \    ${resp} =    Fusion Api Get Enclosure Groups    param=?filter="'name' = '${eg['name']}'"
    \    ${count} =    Get From Dictionary    ${resp}    count
    \    Continue For Loop If    ${count}==0
    \    ${resp} =    Fusion Api Delete Enclosure Group    ${eg['name']}
    \    Wait For Task2    ${resp}    30    2

    :FOR    ${lig}    IN    @{ligs}
    \    ${resp} =    Fusion Api Get Lig    param=?filter="'name' = '${lig['name']}'"
    \    ${count} =    Get From Dictionary    ${resp}    count
    \    Continue For Loop If    ${count}==0
    \    ${resp} =    Delete Resource    LIG:${lig['name']}
    \    Wait For Task2    ${resp}    30    2

    :FOR   ${eth}    IN    @{ethernet_networks}
    \    ${resp} =    Fusion Api Get Ethernet Networks    param=?filter="'name' = '${eth['name']}'"
    \    ${count} =    Get From Dictionary    ${resp}    count
    \    Continue For Loop If    ${count}==0
    \    ${resp} =    Delete Resource    ETH:${eth['name']}
    \    Wait For Task2    ${resp}    30    2

    :FOR   ${fc}    IN    @{fc_networks}
    \    ${resp} =    Fusion Api Get Fc Networks    param=?filter="'name' = '${fc['name']}'"
    \    ${count} =    Get From Dictionary    ${resp}    count
    \    Continue For Loop If    ${count}==0
    \    ${resp} =    Delete Resource    FC:${fc['name']}
    \    Wait For Task2    ${resp}    30    2

    :FOR   ${fcoe}    IN    @{fcoe_networks}
    \    ${resp} =    Fusion Api Get FCoE Networks    param=?filter="'name' = '${fcoe['name']}'"
    \    ${count} =    Get From Dictionary    ${resp}    count
    \    Continue For Loop If    ${count}==0
    \    ${resp} =    Delete Resource    FCOE:${fcoe['name']}
    \    Wait For Task2    ${resp}    30    2

    ${resp} =    Remove Storage Volumes Async    ${storage_volumes}    ?suppressDeviceUpdates=false
    Wait For Task2    ${resp}    60    5

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
