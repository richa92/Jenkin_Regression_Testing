*** Settings ***
Documentation        OVF564 Delete SPT with unassigned network

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
Delete SPT with unassigned network

    ${resps} =    Add Server Profile Templates from variable    ${createSPTP020}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed
    ${rc} =  Validate Server Profile Templates Connections Network Applied  ${createSPTP020}
    Should be true    ${rc}     msg=Failed to apply connetion network as expected

    Log to console and Log file    Deleting SPT with unassigned network
    ${rc} =  Fusion API Delete Server Profile Template       ${createSPTP020[0]["name"]}
    Should be true    ${rc}    msg=Failed to Delete The Server Profile Template with Unassigned network
