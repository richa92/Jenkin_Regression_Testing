*** Settings ***
Documentation        OVF2     APIp035 Validate group session is authorized to perform a specified resource action

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
OVF2_API_p035 Validate group session is authorized to perform a specified resource action
    [Documentation]   p035 Validate group session is authorized to perform a specified resource action
    Log To Console    \n- Test Case: OVF2APIp035 Validate group session is authorized to perform a specified resource action
    credential Login     ${p005_credentials_list}
    :FOR     ${credential}     IN     @{p005_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    Validate Session Authorized Action    ${sht_auth_aciton}
    \        Should Be True    ${ret}
    Log To Console    \n- Test Case: Successfully: p035 Validate group session is authorized to perform a specified resource action
