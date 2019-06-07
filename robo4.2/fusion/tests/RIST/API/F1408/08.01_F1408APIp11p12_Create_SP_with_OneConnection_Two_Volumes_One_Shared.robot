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
Test Setup           Login And Clear Test Environtment    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F1408APIp011p012 Create SP With Connection Two Volumes One Shared

    ${resps} =    Add Server Profiles from variable    ${createProfileP11P12P61}

    Validate Server Profile Applied Successfully    ${resps}

    ${sp_uri} =    Get Server Profile URI    ${createProfileP11P12P61[0]['name']}
    ${vol_uri} =     Get Server Profile Boot Volume Uri Or Check Other Info    ${sp_uri}    volumeUri    False    True
    Validate Server Profile Volume Info    ${vol_uri}    shareable    False
    ${vol_uri} =     Get Server Profile Boot Volume Uri Or Check Other Info    ${sp_uri}    volumeUri    False    False
    Validate Server Profile Volume Info    ${vol_uri}    shareable    True

    Validate Server Profile Primary Connection And Volume Boot Status    ${createProfileP11P12P61}    priority    Primary
