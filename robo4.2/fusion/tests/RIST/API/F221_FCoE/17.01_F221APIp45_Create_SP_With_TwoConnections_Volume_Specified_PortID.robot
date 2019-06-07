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
Test Setup           Login And Clear Test Environtment    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
F221APIp045 Create SP with Primary And Secondary Connections with Private Volume with User Specified IDs

    ${resps} =    Add Server Profiles from variable    ${createProfileP45}

    Validate Server Profile Applied Successfully    ${resps}

    Validate Server Profile Primary Connection And Volume Boot Status    ${createProfileP45}    priority    Primary    ${False}

    ${expected_portid_list} =    Create List    ${createProfileP45[0]['connections'][0]['portId']}     ${createProfileP45[0]['connections'][1]['portId']}

    :FOR    ${resp}    IN    @{resps}
    \       Log To Console    resp_is_${resp}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections    2
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage     1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    portId    ${expected_portid_list}



