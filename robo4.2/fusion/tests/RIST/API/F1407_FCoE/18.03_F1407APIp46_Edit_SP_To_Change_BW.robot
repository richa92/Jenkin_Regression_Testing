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
Test Setup           Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F1407APIp46 Edit SP To Change BW


    ${resps} =    Edit Server Profiles from variable    ${editProfileP48}


    :FOR    ${resp}    IN    @{resps}
    \       log To Console   resp_is_${resp}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections    2
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage     1


    Validate Server Profile Connections Bandwidth Applied    ${editProfileP48}