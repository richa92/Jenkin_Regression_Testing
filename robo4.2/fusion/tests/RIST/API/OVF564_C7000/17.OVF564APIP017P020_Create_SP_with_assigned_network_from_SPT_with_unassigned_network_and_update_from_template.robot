*** Settings ***
Documentation        OVF564 Create SP with assigned network from SPT with unassigned network

Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py

Test Setup           Login And Clear Test Environtment    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
OVF564 Create SP with assigned network from SPT with unassigned network
    ${resps} =    Add Server Profile Templates from variable    ${createSPTP017}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed
    ${rc} =  Validate Server Profile Templates Connections Network Applied  ${createSPTP017}
    Should be true    ${rc}     msg=Failed to apply connetion network as expected

    ${resps} =    Add Server Profiles from variable    ${createSPP017}
    Validate Server Profile Applied Successfully    ${resps}
    ${rc} =  Validate Server Profiles Connections Network Applied  ${createSPP017}
    Should be true    ${rc}    msg=Failed to apply server profile connections

    ${resps} =    Update Server Profiles from Template     ${createSPP017}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed