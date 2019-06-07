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
F1407APIp59 Edit SP To Change Boot Volume Size And Validate


    ${sp_uri} =    Get Server Profile URI    ${editProfileP28[0]['name']}

    ${vol_uri} =     Get Server Profile Boot Volume Uri Or Check Other Info    ${sp_uri}    volumeUri    False

    log to console      vol_orig_size_string_is_${vol_orig_size}

    Validate Server Profile Volume Info    ${vol_uri}    provisionedCapacity    ${vol_orig_size}

    ${payload} =     Get Volume Payload    ${vol_uri}

    ${resps} =    Update Volume With Payload    ${payload}     provisionedCapacity    ${vol_modify_size}    ${vol_uri}

    Wait Until Keyword Succeeds    5min    5sec    Validate Server Profile Volume Info    ${vol_uri}    provisionedCapacity    ${vol_modify_size}

