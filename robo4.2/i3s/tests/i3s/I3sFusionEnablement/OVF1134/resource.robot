*** Settings ***
Library           json
Library           copy
Resource          ${fusion_api_resource}
Resource          ../Resources/api/resource.robot
Variables         ./ovf_1134_me_data.py
Variables         ./environment_data.py
Variables          ../../../testdata/i3s_QA_testdata.py

*** Variables ***
${X-Api-Version}    800
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${fusion_api_resource}       ../fusion/Resources/api/fusion_api_resource.txt

*** Keywords ***
Create firmware bundle payload
    [Documentation]    Generate Firmware body
    [Arguments]    ${firmware_payload}
    ${payload} =    Copy Dictionary    ${firmware_payload}
    ${status}       run keyword and return status    Dictionary should contain key    ${payload}    firmwareBaselineUri
    ${firmware_uri}=    Get Firmware Bundle By Version    ${payload['firmwareBaselineUri']}
    run keyword if    '${status}'=='True' and '${payload['firmwareBaselineUri']}' != ''    Set to Dictionary    ${payload}    firmwareBaselineUri    ${firmware_uri}
    [Return]    ${payload}

Perform deploy operation
    [Documentation]    To power on/off and verify ping function
    [Arguments]    ${serverprofile}
    Power On Profile Server    ${serverprofile['serverHardwareUri']}
    Log to console    ${serverprofile['serverHardwareUri']}
    #Get i3s Appliance Cluster IP and Login to i3s appliance
    ${resp} =    Fusion Api Get i3sCluster IP
    ${i3S_IP} =    Get From Dictionary    ${resp['members'][0]}    primaryIPV4
    Log to console    ${i3S_IP}
    Login to Appliance via SSH    ${i3S_IP}    ${SSHUSER}    ${SSHPASSWORD}    ${TIMEOUT}
    ${mgmt_ip} =    Get Server Profile Management IP    ${serverprofile}
    Ping Profile Management IP    ${mgmt_ip}
    Power Off Profile Server    ${serverprofile['serverHardwareUri']}
    Sleep    50