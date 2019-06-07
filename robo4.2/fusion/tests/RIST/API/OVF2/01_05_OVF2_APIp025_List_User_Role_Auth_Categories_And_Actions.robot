*** Settings ***
Documentation        OVF2     APIp025_Can list user role and  auth categories and actions

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


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_API_p025_Can list user role and auth categories and actions
    [Documentation]   p025_Can list user role  auth categories and actions
    Log To Console    \n- Test Case: OVF2APIp025_Can list user role  auth categories and actions
    credential Login     ${p001_credentials_list}
    :FOR     ${credential}     IN     @{p001_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    List Role Category Action
    \        Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p025_Can list user role  auth categories and actions
