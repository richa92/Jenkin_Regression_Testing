*** Settings ***
Documentation        OVF564 Edit SP from assigned network to unassigned when server is power off

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
Edit SP from assigned network to unassigned when server is power off
    ${resps} =    Add Server Profiles from variable    ${createProfileP005}
    Validate Server Profile Applied Successfully    ${resps}
    Wait For ALL Server Profile In Normal State

    ${rc} =  Validate Server Profiles Connections Network Applied  ${createProfileP005}
    Should be true    ${rc}    msg=Failed to apply server profile connections

    ${resps} =    Edit Server Profiles from variable    ${editProfileP005}
    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task2    ${resp}    20min    5

    ${rc} =  Validate Server Profiles Connections Network Applied  ${editProfileP005}
    Should be true    ${rc}    msg=Failed to apply server profile connections