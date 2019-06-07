*** Settings ***
Documentation        OVF2     APIp019 Lists the permission scopes which authorize an action that includes an association change when the base resource already existed

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
OVF2_API_p019 Lists the permission scopes which authorize an action that includes an association change when the base resource already existed
    [Documentation]   p019 Lists the permission scopes which authorize an action that includes an association change when the base resource already existed
    Log To Console    \n- Test Case: OVF2APIp019 Lists the permission scopes which authorize an action that includes an association change when the base resource already existed
    credential Login     ${p001_credentials_list}
    :FOR     ${credential}     IN     @{p001_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    Lists The Permission Scopes    ${false}    &category=logical-interconnect-groups&associatedCategory=ethernet-networks
    \        Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p019 Lists the permission scopes which authorize an action that includes an association change when the base resource already existed
