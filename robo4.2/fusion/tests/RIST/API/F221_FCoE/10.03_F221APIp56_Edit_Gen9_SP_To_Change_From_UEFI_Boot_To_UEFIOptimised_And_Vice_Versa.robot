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
F221APIp56 Edit Gen9 SP To Change From UEFI Boot To UEFIOptimised And Vice Versa


    ${resps} =    Edit Server Profiles from variable    ${editProfileP56}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections     2
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage      1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    mode    UEFIOptimized


    ${resps} =    Edit Server Profiles from variable    ${editProfileP55P56ViceVersa}

    :FOR    ${resp}    IN    @{resps}
    \       ${task} =    Wait For Task     ${resp}    20min    5s
    \       Server Profile Special Section Check After Created Or Edited    ${task}    connections     2
    \       Server Profile Special Section Check After Created Or Edited    ${task}    sanStorage      1
    \       Server Profile Special Section Check After Created Or Edited    ${task}    mode    UEFI


