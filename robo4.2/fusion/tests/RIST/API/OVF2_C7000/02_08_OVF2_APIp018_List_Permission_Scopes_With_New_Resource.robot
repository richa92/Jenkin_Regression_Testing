*** Settings ***
Documentation        OVF2     APIp018 Lists the permission scopes which authorize an action that includes an association change when the base resource does not exist

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF2_C7000.txt


Variables            ${DATA_FILE}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF2_API_p018-2 Lists the permission scopes which authorize an action that includes an association change when the base resource does not exist
    [Documentation]   p018 Lists the permission scopes which authorize an action that includes an association change when the base resource does not exist
    Log To Console    \n- Test Case: OVF2APIp018 Lists the permission scopes which authorize an action that includes an association change when the base resource does not exist
    credential Login     ${p005_credentials_list}
    :FOR     ${credential}     IN     @{p005_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    Lists The Permission Scopes    ${true}    &category=logical-interconnect-groups&associatedCategory=ethernet-networks
    \        Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p018 Lists the permission scopes which authorize an action that includes an association change when the base resource does not exist