*** Settings ***
Documentation        OVF564 Create SP with FC function type and unassigned network

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
Create SP with Ethernet function type and unassigned network

    ${resps} =    Add Server Profiles from variable    ${createProfileP002}

    Validate Server Profile Applied Successfully    ${resps}

    ${rc} =  Validate Server Profiles Connections Network Applied  ${createProfileP002}
    Should be true    ${rc}    msg=Failed to apply server profile connections