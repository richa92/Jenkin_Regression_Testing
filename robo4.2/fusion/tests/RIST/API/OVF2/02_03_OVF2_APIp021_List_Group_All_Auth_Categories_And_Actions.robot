*** Settings ***
Documentation        OVF2     APIp021_Can list group all auth categories and actions

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF2.txt


Variables            ${DATA_FILE}
Test Setup           Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_API_p021_Can list group all auth categories and actions
    [Documentation]   p021_Can list group all auth categories and actions
    Log To Console    \n- Test Case: OVF2APIp021_Can list group all auth categories and actions
    credential Login     ${p005_credentials_list}
    :FOR     ${credential}     IN     @{p005_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    List Categories And Actions
    \        Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p021_Can list ugroup all auth categories and actions
