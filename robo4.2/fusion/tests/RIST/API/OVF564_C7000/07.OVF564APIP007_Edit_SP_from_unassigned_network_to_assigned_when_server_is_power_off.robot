*** Settings ***
Documentation        OVF564 Edit SP from unassigned network to assigned when server is power off

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
OVF564 Edit SP from unassigned network to assigned when server is power off
    # Create server profile with unassigned network
    ${resps} =    Add Server Profiles from variable    ${createProfileP007}
    Validate Server Profile Applied Successfully    ${resps}
    ${rc} =  Validate Server Profiles Connections Network Applied  ${createProfileP007}
    Should be true    ${rc}    msg=Failed to apply server profile connections

    # Edit server profile
    ${resps} =    Edit Server Profiles from Variable    ${editProfileP007}
    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task2     ${resp}    20min    5
    ${rc} =  Validate Server Profiles Connections Network Applied  ${editProfileP007}
    Should be true    ${rc}    msg=Failed to apply server profile connections