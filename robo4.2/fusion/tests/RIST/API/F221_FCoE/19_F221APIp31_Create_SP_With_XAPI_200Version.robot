*** Settings ***
Documentation                   F221 SP with Connection and Volume

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
F221APIp31 Create Gen9 SP With XAPI 200Version

    ${resps} =    Add Server Profiles from variable    ${createGen9ProfileP31}    ${HeaderP31P33}

    Validate Server Profile Applied Successfully    ${resps}


