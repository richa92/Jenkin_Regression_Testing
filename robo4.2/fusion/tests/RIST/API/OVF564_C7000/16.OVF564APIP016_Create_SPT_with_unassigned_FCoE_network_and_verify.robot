*** Settings ***
Documentation        OVF564 Create SPT with FCoE function type and unassigned network

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
Create SPT with FCoE function type and unassigned network

    ${resps} =    Add Server Profile Templates from variable    ${createSPTP016}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed

    ${rc} =  Validate Server Profile Templates Connections Network Applied  ${createSPTP016}
    Should be true    ${rc}     msg=Failed to apply connetion network as expected