*** Settings ***
Documentation        OVF564 Create SP with unassigned network from SPT with assigned network

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
Create SP with unassigned network from SPT with assigned network
    ${resps} =    Add Server Profile Templates from variable    ${createSPTP019}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed
    ${rc} =  Validate Server Profile Templates Connections Network Applied  ${createSPTP019}
    Should be true    ${rc}     msg=Failed to apply connetion network as expected

    ${resps} =    Add Server Profiles from variable    ${createSPP019}
    Validate Server Profile Applied Successfully    ${resps}
    ${rc} =  Validate Server Profiles Connections Network Applied  ${createSPP019}
    Should be true    ${rc}    msg=Failed to apply server profile connections

    ${resps} =    Update Server Profiles from Template    ${createSPP019}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed