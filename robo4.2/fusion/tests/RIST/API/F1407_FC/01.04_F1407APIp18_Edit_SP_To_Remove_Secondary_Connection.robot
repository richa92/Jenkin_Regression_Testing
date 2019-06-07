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
F1407APIp18 Edit SP To Remove Secondary Connection

    ${resps} =    Edit Server Profiles from variable    ${editProfileP18}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections    1

