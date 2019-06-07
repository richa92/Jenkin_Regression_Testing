*** Settings ***
Documentation                   Gen10 DL Server Licensing tests

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             XML
Library             String
Library             Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables           ${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}     16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
OVS28827 No OV licenses Add DLs with ilo licenses
    [Tags]    OVS28827-1-3-2
    Delete All Fusion License with ssh
    Add Gen10 DL servers as managed  ${Gen10_DLs_With_ilo}
    Verify SH Licenses      ${dl_servers_IPs_keys}
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneView

OVS28827 Edit DL licensing intent to without ilo
    [Tags]    OVS28827-1-3-3
    ${resp} =     Patch Server Hardware  ${DL180_name}  op=replace  path=/licensingIntent  value=OneViewNoiLO
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${resp} =     Refresh Server Hardware  SH:${DL180_name}
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO
    Remove All DL Server Hardware Async

OVS28827 No OV licenses Add DLs without ilo licenses
    [Tags]    OVS28827-1-3-4
    Delete All Fusion License with ssh
    Add Gen10 DL servers as managed  ${Gen10_DLs_Without_ilo}
    Verify SH Licenses      ${dl_servers_IPs_keys}
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO

OVS28827 Edit DL licensing intent to with ilo
    [Tags]    OVS28827-1-3-5
    ${resp} =     Patch Server Hardware  ${DL180_name}  op=replace  path=/licensingIntent  value=OneView
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${resp} =     Refresh Server Hardware  SH:${DL180_name}
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneView
    Remove All DL Server Hardware Async

OVS28827 Add OV with iLO licenses - but add DL without ilo
    [Tags]    OVS28827-1-4-1
    Delete All Fusion License with ssh
    Add Licenses from variable		${licensesWithIlo}
    Add Gen10 DL servers as managed  ${Gen10_DLs_Without_ilo}
    ${licenses} =  Run cpqlocfg and Remove Licenses  ${DL180_IP}
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO
    ${resp} =     Patch Server Hardware  ${DL180_name}  op=replace  path=/licensingIntent  value=OneView
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${resp} =     Refresh Server Hardware  SH:${DL180_name}
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneView

OVS28827 Change License from OV to OV and expect error msg
    [Tags]    OVS28827-1-4-2
    Run Negative Tasks for List     ${patch_dl_server_task2}
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneView
    Remove All DL Server Hardware Async

OVS28827 Add OV without iLO licenses - but add DL with ilo
    [Tags]    OVS28827-1-4-3
    Delete All Fusion License with ssh
    ${li_type} =   Set Variable    'HPE OneView Advanced w/o iLO'
    Add Licenses from variable		${licensesWithoutIlo}
    Add Gen10 DL servers as managed  ${Gen10_DLs_With_ilo}
    ${licenses} =  Run cpqlocfg and Remove Licenses  ${DL180_IP}
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneView
    ${resp} =     Patch Server Hardware  ${DL180_name}  op=replace  path=/licensingIntent  value=OneViewNoiLO
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${resp} =     Refresh Server Hardware  SH:${DL180_name}
    Wait For Task2    ${resp}    timeout=1000    interval=15
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO
    Verify Licenses Count 	639  ${li_type}

OVS28827 Change License from NoOV to OV and expect error msg
    [Tags]    OVS28827-1-4-4
    Run Negative Tasks for List     ${patch_dl_server_task}
    ${server} =  Get Resource  SH:${DL180_name}
    Verify Resource  ${server}  licensingIntent=OneViewNoiLO

*** Keywords ***
Setup
    [Documentation]    Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

Clean Up
    [Documentation]    Teardown
    Fusion Api Logout Appliance
    Remove All DL Server Hardware Async

Add Gen10 DL servers as managed
    [Documentation]    Add Gen10 DL servers as managed
    [Arguments]  ${DLs}
    ${newDLs} =     Copy dictionary     ${DLs}
    ${resps}=    Add Server hardware from variable    ${newDLs}
    Wait For Task2    ${resps}  timeout=10m  interval=5

Add Licenses
    [Documentation]    Add licenses
    Log    Adding new licenses    console=true
    Add Licenses From Variable    ${licenses}

Get SH Licenses
    [Documentation]    Get SH Licenses
    [Arguments]  ${sh_ip}
    ${licenses} =  Run cpqlocfg and Get Licenses  ${sh_ip}
    log to console		${licenses}

Verify SH Licenses
    [Documentation]    Verify SH Licenses
    Log    Verify SH Licenses    console=true
    [Arguments]  ${sh_list}
    :FOR    ${sh}    IN    @{sh_list}
    \       ${sh_ip} =   Set Variable    ${sh['IP']}
    \       ${sh_li} =   Set Variable    ${sh['key']}
    \       ${resp} =    Run cpqlocfg and Get Licenses  ${sh_ip}
    \       ${resp_xml}=    Parse XML    ${resp}
    \       ${li} =  Get Element  ${resp_xml}  LICENSE
    \       ${realSH_li} =   XML.Get Element Attribute  ${li}  VALUE  LICENSE_KEY
    \       Should Match    ${sh_li}    ${realSH_li}

Verify Licenses Count
    [Documentation]    Verify Licenses Count
    Log    Verify Licenses Count    console=true
    [Arguments]  ${count}  ${product}
    ${availCap} =   Set Variable    0
    ${resp} =  Get All Licenses
    :FOR    ${li}    IN    @{resp}
    \       Continue For Loop If  '${li['product']}' != ${product}
    \       ${availCap} =  Run Keyword if  '${li['product']}' == ${product}  Get From Dictionary  ${li}  availableCapacity
    log to console		${availCap}
    should be equal as integers   ${availCap}   ${count}

Delete All Fusion License with ssh
    [Documentation]    Deletes all the licenses from the appliance with ssh.
	${cmd} =   Set Variable    echo y | /ci/bin/licmgr --type key --delete all
	Run Command Via SSH   ${APPLIANCE_IP}   ${ssh_credentials['userName']}   ${ssh_credentials['password']}   ${cmd}   ${FUSION_PROMPT}   ${FUSION_TIMEOUT}

Set Server License with OneView
    [Documentation]  Patch server hardware licensetype to oneview.
    ...              Example:
    ...                PSet Server License with OneView  ${ENC1SHBAY3}
    ...              Data Required:
    ...                Server Hardware name
    [Arguments]  ${name}
    ${name} =  replace string using regexp  ${name}  SH:  ${EMPTY}
    ${op} =   Set Variable    replace
    ${path} =   Set Variable    /licensingIntent
    ${value} =   Set Variable    OneView
    Log    Patching Server Hardware ${name} with op=${op} path=${path} and value=${value}    console=True
    ${uri} =  Get Server Hardware URI  ${name}
    ${dict} =  Create Dictionary  op=${op}  path=${path}  value=${value}
    ${payload} =  Create List  ${dict}
    ${resp} =  fusion api patch server hardware  ${payload}  ${uri}
    [return]  ${resp}
