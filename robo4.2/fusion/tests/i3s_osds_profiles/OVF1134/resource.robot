*** Settings ***
Library           json
Library           copy
Resource          ${fusion_api_resource}
Resource          ../Resources/api/resource.robot
Variables         ./ovf_1134_me_data.py
Variables         ./environment_data.py

*** Variables ***
${fusion_ip}        15.212.167.184
# ${X-Api-Version}    600
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${fusion_api_resource}       C:/Users/komerao/OVF1134/fusion/Resources/api/fusion_api_resource.txt

*** Keywords ***
Create firmware bundle payload
    [Documentation]    Generate Firmware body
    [Arguments]    ${firmware_payload}
    ${payload} =    Copy Dictionary    ${firmware_payload}
    ${status}       run keyword and return status    Dictionary should contain key    ${payload}    firmwareBaselineUri
    ${firmware_uri}=    Get Firmware Bundle By Version    ${payload['firmwareBaselineUri']}
    run keyword if    '${status}'=='True' and '${payload['firmwareBaselineUri']}' != ''    Set to Dictionary    ${payload}    firmwareBaselineUri    ${firmware_uri}
    [Return]    ${payload}
