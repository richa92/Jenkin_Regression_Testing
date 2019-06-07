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
F221APIp22 Edit SP To Change Lun Setting From Auto To Manual


    ${resps} =    Edit Server Profiles from variable    ${editProfileP22}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    lunType     Manual

