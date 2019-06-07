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
F1407APIp39 Edit SP To Change From Primary Boot To Non Bootable And Remove Boot Volume


    ${resps} =    Edit Server Profiles from variable    ${editProfileP30}

    :FOR    ${resp}    IN    @{resps}
    \       Log To Console    resp_is_${resp}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections     1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage      0
    \       Validate Server Profile Primary Connection And Volume Boot Status    ${createProfileP01P02P34P35P36}    priority    NotBootable

