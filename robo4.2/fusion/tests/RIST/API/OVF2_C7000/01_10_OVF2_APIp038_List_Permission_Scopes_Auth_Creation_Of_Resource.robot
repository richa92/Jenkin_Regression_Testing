*** Settings ***
Documentation        OVF2     APIp038 Lists the permission scopes which authorize creation of a resource with an association to a specified resource

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
OVF2_API_p038 Lists the permission scopes which authorize creation of a resource with an association to a specified resource
    [Documentation]   p038 Lists the permission scopes which authorize creation of a resource with an association to a specified resource
    Log To Console    \n- Test Case: OVF2APIp038 Lists the permission scopes which authorize creation of a resource with an association to a specified resource
    credential Login     ${p001_credentials_list}
    :FOR     ${credential}     IN     @{p001_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    Lists The Permission Scopes Auth Creation Resource    &&associatedCategory=logical-interconnect-groups&&resourceCategory=ethernet-networks
    \        Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p038 Lists the permission scopes which authorize creation of a resource with an association to a specified resource
