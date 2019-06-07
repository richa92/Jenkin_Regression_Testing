*** Settings ***
Documentation        OVF564 Delete SP with unassigned network successfully when server is power off

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
Delete SP with unassigned network successfully to when server is power off
    ${resps} =  Add Server Profiles from Variable    ${createProfileP010}
    Validate Server Profile Applied Successfully     ${resps}
    ${rc} =  Validate Server Profiles Connections Network Applied  ${createProfileP010}
    Should be true    ${rc}    msg=Failed to apply server profile connections

    ${rc} =  Delete Server Profile And Validate The Deletion  ${createProfileP010}    ${False}
    Should Match     ${rc}    PASS