*** Settings ***
Documentation        OVF2     APIp034 Validate user session is authorized to perform a specified resource action

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
OVF2_API_p034 Validate user session is authorized to perform a specified resource action
    [Documentation]   p034 Validate user session is authorized to perform a specified resource action
    Log To Console    \n- Test Case: OVF2APIp034 Validate user session is authorized to perform a specified resource action
    credential Login     ${p001_credentials_list}
    :FOR     ${credential}     IN     @{p001_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    Validate Session Authorized Action    ${sht_auth_aciton}
    \        Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p034 Validate user session is authorized to perform a specified resource action
