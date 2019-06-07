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
F221APIp04p05 Create And Get SP With Two Connections Managed Volume

    ${resps} =    Add Server Profiles from variable    ${createsProfileP04P05P07P13P14}

    Validate Server Profile Applied Successfully    ${resps}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections    2

    Validate Server Profile Primary Connection And Volume Boot Status    ${createsProfileP04P05P07P13P14}    bootVolumeSource    ManagedVolume



