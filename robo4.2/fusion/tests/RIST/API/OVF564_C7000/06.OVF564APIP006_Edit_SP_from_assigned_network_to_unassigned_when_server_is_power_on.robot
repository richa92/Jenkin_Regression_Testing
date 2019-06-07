*** Settings ***
Documentation        OVF564 Edit SP from assigned network to unassigned when server is power on

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
Edit SP from assigned network to unassigned when server is power on
    ${resps} =    Add Server Profiles from variable    ${createProfileP006}
    Validate Server Profile Applied Successfully    ${resps}
    ${rc} =  Validate Server Profiles Connections Network Applied  ${createProfileP006}
    Should be true    ${rc}    msg=Failed to apply server profile connections

    Power on server    ${createProfileP006[0]["serverHardwareUri"]}

    ${resps} =    Edit Server Profiles from Variable    ${editProfileP006}
    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task2     ${resp}    20min    5    None Expected    Completed
    ${rc} =  Validate Server Profiles Connections Network Applied  ${editProfileP006}
    Should be true    ${rc}    msg=Failed to apply server profile connections