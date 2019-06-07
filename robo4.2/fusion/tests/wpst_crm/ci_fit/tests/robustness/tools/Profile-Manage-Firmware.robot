*** Settings ***
Documentation        (Optionally upload SPP FW Bundle) Set manageFirmware in OneView server-profiles.
...                  Example workflow: Upload SPP Bundle from your local directory to OneView then update
...                                 time pybot -d /tmp/logs/Profile-Manage-Firmware/ -LTRACE -vSPP_BUNDLE_DIR:./ -vSPP_BUNDLE_NAME:SPPGen10Snap1.2017_0425.124.iso -vAPPLIANCE_IP:15.186.9.xx Profile-Manage-Firmware.robot
...                  Example workflow: Use the pre-uploaded SPP Bundle to update FW
...                                 time pybot -d /tmp/logs/Profile-Manage-Firmware/ -LTRACE -vSPP_BUNDLE_NAME:SPPGen10Snap1.2017_0425.124.iso -vAPPLIANCE_IP:15.186.9.xx Profile-Manage-Firmware.robot
...                  Default firmwareActivationType: Immediate, to override it use -vFIRMWARE_ACTIVATION_TYPE:[Immediate|NotScheduled|Scheduled]
...                  Default forceInstallFirmware: False, to override it use -vFORCE_INSTALL_FIRMWARE:[True|False]
...                  Default profile throttle: 3, to override it use -vPROFILE_THROTTLE:[None|<number of profiles at a time>]

Variables           ../resources/data_variables.py
Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             Collections
Library             ../resources/robustness-helper.py


*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${EMAIL_TO}                     None
${EMAIL_FROM}                   ${EMAIL_TO}
${SPP_BUNDLE_DIR}               None
${SPP_BUNDLE_NAME}              None
${SPP_BUNDLE_PATH}              ${SPP_BUNDLE_DIR}/${SPP_BUNDLE_NAME}
${tbirdEnv}                     None
${FW_UPDATE_WAIT_TIMEOUT}       30m
${FW_UPDATE_WAIT_INTERVAL}      10s
${EDIT_PROFILE_WAIT_TIMEOUT}    60m
${EDIT_PROFILE_WAIT_INTERVAL}   10s
${FIRMWARE_ACTIVATION_TYPE}     Immediate
${FORCE_INSTALL_FIRMWARE}       False
${FORCE_PROFILE_APPLY}          all
${PROFILE_THROTTLE}             3

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Check For SPP Bundle Argument
    Run Keyword If   "${SPP_BUNDLE_NAME}" == "${null}"   Fail   msg=SPP_BUNDLE_NAME is a required argument. Please provide it using -vSPP_BUNDLE_NAME:<SPP Name>.

Kick In Firmware Manager
    Run Keyword If   "${APPLIANCE_IP}" == "${EMPTY}" or "${SPP_BUNDLE_NAME}" == "${null}"   Fail   msg=There was a validation error. Please check the validation test case(s) and try again.
    Log Variables
    ${bundleUri} =   Load SPP FW Bundle
    Set Manage Firmware   ${bundleUri}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

*** Keywords ***
Set Manage Firmware
    [Documentation]   Set manage firmware and triggers update from profile.
    [Arguments]   ${bundleUri}   ${waitTime}=${EDIT_PROFILE_WAIT_TIMEOUT}   ${interval}=${EDIT_PROFILE_WAIT_INTERVAL}  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}   ${forceProfileApply}=false   ${throttle}=${Null}
    ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${FORCE_PROFILE_APPLY}"
    ...                    ELSE   Set Variable   ${EMPTY}
    ${FORCE_INSTALL_FIRMWARE} =   Convert To Boolean   ${FORCE_INSTALL_FIRMWARE}
    ${resp} =   Fusion Api Get Server Profiles
    ${profiles} =   Get From Dictionary   ${resp}   members
    ${firmwareAttr} =   Create Dictionary   firmwareActivationType=${FIRMWARE_ACTIVATION_TYPE}   firmwareBaselineUri=${bundleUri}   firmwareInstallType=FirmwareAndOSDrivers   forceInstallFirmware=${FORCE_INSTALL_FIRMWARE}   manageFirmware=${True}
    ${requestBody} =   Create Dictionary
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    ${l} =   Get Length   ${profiles}
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${p}   IN RANGE   0   ${l}
    \   ${sp} =   Get From List   ${profiles}   ${p}
    \    Set To Dictionary   ${requestBody}   firmware=${firmwareAttr}   type=${sp['type']}   uri=${sp['uri']}   serverHardwareUri=${sp['serverHardwareUri']}   affinity=${sp['affinity']}   connectionSettings=${sp['connectionSettings']}   eTag=${sp['eTag']}   name=${sp['name']}   boot=${sp['boot']}   bootMode=${sp['bootMode']}
    \   ${resp} =   Fusion Api Edit Server Profile   ${requestBody}   ${sp['uri']}   param=${param}
    \   Continue For Loop If   ${waitForTask} != ${True}
    \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \   ...   ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    \       Continue For Loop If   '${throttle}' == '${Null}'
    \       Continue For Loop If   ${parallel} != ${True}
    \       ${respLength} =   Get Length   ${respList}
    \       Continue For Loop If   ${respLength} != ${throttle}
    \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}   throttle=${throttle}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.
 
