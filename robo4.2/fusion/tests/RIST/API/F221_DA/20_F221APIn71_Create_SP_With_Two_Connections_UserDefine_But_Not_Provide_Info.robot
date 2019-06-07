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
F221APIn071 Create SP with Two Connections with User Defined But Not Provide Info

    ${resps} =    Add Server Profiles from variable    ${createProfileN71}

    Validate Server Profile Creation Or Edit Failed As Expected    ${resps}    create    BootTargetNotSpecifiedForUserDefinedBoot


