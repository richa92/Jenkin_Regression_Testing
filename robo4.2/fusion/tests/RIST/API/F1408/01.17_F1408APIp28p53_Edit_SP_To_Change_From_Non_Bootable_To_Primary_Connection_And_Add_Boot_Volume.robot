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
F1408APIp28 Edit SP To Change From Non Bootable To Primary Boot And Add Boot Volume


    ${resps} =    Edit Server Profiles from variable    ${editProfileP28}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections     1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage      1
    \       Validate Server Profile Primary Connection And Volume Boot Status    ${createProfileP01P02P34P35P36}    priority   Primary

