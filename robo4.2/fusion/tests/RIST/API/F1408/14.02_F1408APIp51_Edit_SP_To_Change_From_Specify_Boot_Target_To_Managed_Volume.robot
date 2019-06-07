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
F1408APIp51 Edit SP To Change From Specify Boot Target To Managed Volume


    ${resps} =    Edit Server Profiles from variable    ${editProfileP51}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections     2
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage      1

