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
Test Setup           Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F221APIp58 Edit SP To Change Private To Shared Volume


    ${resps} =    Edit Server Profiles from variable    ${editProfileP58_Pre}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage     1


    ${resps} =    Edit Server Profiles from variable    ${editProfileP58}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage     2
    \       ${sp_uri} =    Get Server Profile URI    ${editProfileP58[0]['name']}
    \       ${vol_uri} =     Get Server Profile Boot Volume Uri Or Check Other Info    ${sp_uri}    volumeUri    False    True
    \       Validate Server Profile Volume Info    ${vol_uri}    shareable    False
    \       ${vol_uri} =     Get Server Profile Boot Volume Uri Or Check Other Info    ${sp_uri}    volumeUri    False    False
    \       Validate Server Profile Volume Info    ${vol_uri}    shareable    True