*** Settings ***
Documentation                   F1408 SP with Connection and Volume

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
F1408APIp54 Edit SP To Change Server Hardware Type


    ${resps} =    Edit Server Profiles from variable    ${editProfileP54}

    :FOR    ${resp}    IN    @{resps}
    \       log to console    resp_is_${resp}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections     1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage      1

