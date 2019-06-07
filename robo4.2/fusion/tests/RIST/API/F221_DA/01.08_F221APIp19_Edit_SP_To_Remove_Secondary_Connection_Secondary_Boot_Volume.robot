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


*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F221APIp19 Edit SP To Remove Secondary Connection And Secondary Boot Volume

    ${resps} =    Edit Server Profiles from variable    ${editProfileP19}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections    1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage     1
