*** Settings ***
Documentation                   F1407 SP with Connection and Volume

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
F1407APIn03 Create SP With One Connection Non Volume

    ${resps} =    Add Server Profiles from variable    ${createProfileN03}

    Validate Server Profile Creation Or Edit Failed As Expected    ${resps}    create    BootSettingsNotAllowed

