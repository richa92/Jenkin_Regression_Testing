*** Settings ***
Documentation        OVF564 Create SP from SPT with different assigned network

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
OVF564 Create SP from SPT with different assigned network
    ${resps} =    Add Server Profile Templates from variable    ${createSPTP018}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed

    ${rc} =  Validate Server Profile Templates Connections Network Applied  ${createSPTP018}
    Should be true    ${rc}     msg=Failed to apply connetion network as expected

    ${resps} =    Add Server Profiles from variable    ${createSPP018}
        :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed

    ${resps} =    Update Server Profiles from Template    ${createSPP018}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed