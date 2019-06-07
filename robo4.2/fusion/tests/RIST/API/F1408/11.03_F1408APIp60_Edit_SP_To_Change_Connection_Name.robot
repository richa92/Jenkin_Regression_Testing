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
F1408APIp60 Edit Gen9 SP To Change Connection Name


    ${resps} =    Edit Server Profiles from variable    ${editProfileP60}

    ${expected_name_list} =    Create List    ${editProfileP60[0]['connections'][0]['name']}     ${editProfileP60[0]['connections'][1]['name']}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections     2
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage      1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    name     ${expected_name_list}



