*** Settings ***
Documentation       OSDS_profiles-SP data volumes tests
Resource            resource.robot
Suite Setup         Login To Appliance And Verify Prerequisites and Add Storage Volumes     ${fusion_ip}    ${admin_credentials}
...                 ${storage_volumes}
Suite Teardown      I3S Suite Teardown
Test Setup          I3S Test Setup


*** Test Cases ***

OVTC57641
    [Documentation]     Create SP with SAN volumes
    [Tags]              TC01

    ${sp_body} =            copy.deepcopy               ${sp_with_fc}
    #Create server profile
    ${blnCreateProf} =      Create I3S Server Profile   ${sp_body}
    Should Be True          ${blnCreateProf}            Failed to create profile '${sp_body['name']}'

    #Edit Sp and Add volumes
    ${tc01_editSp} =            copy.deepcopy               ${sp_with_fc}
    Remove From Dictionary      ${tc01_editSp}              sanStorage
    Set To Dictionary           ${tc01_editSp}              sanStorage=${sanStorage_volumes_add1}
    ${blnEditProf}=             Edit I3S Server Profile     ${tc01_editSp}
    Run Keyword If              '${blnEditProf}'!='True'    Fail
    ...                         Failed to update profile '${tc01_editSp['name']}' with different DP

    #Power ON the SP and wait
    Power on Server     SH:${sp_body['serverHardwareUri']}
    Sleep               420

    #Get the Management IP and Ping the IP
    ${ipv4} =                       Get Server Profile Management IP    ${sp_body}
    Ping Profile Management IP      ${ipv4}

    #Edit Sp and Add volumes
    ${sp_dto} =                 Get Resource                SP:${sp_body['name']}
    Remove From Dictionary      ${sp_dto}                   created             modified            status      state
    ...                         status_code
    ...                         headers
    ${san_volume_attachment}=   server_profile.verify storage volume            ${sanStorage_volumes_add2}
    ${san_updated_list}=        Combine Lists               ${sp_dto['sanStorage']['volumeAttachments']}
    ...                         ${san_volume_attachment['volumeAttachments']}
    Set To Dictionary           ${sp_dto['sanStorage']}     volumeAttachments   ${san_updated_list}
    ${resp} =                   Fusion Api Edit Server Profile Template         body=${sp_dto}      uri=${sp_dto['uri']}
    Wait For Task2              ${resp}                     timeout=60          interval=5

    # Verify the storage volumes in the host through SSH
    Sleep               60
    Open Connection And Log In              ${ipv4}     root    Welcome123#
    Execute Command     esxcli storage core adapter rescan --all
    sleep               60
    ${output1} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output1}

    #Delete the shared volume and Edit the SP
    ${sp_dto} =                 Delete Profile Volume   ${sp_body['name']}      ${storage_volumes[8]['properties']['name']}
    Remove From Dictionary      ${sp_dto}               created                 modified    status      state   status_code
    ...                         headers
    Set to Dictionary           ${sp_dto}
    ${resp} =                   Fusion Api Edit Server Profile                  ${sp_dto}   uri=${sp_dto['uri']}
    Wait For Task2              ${resp}                 timeout=600             interval=5

    #Delete the Private volume and Edit the SP
    ${sp_dto} =                 Delete Profile Volume   ${sp_body['name']}      ${storage_volumes[9]['properties']['name']}
    Remove From Dictionary      ${sp_dto}               created                 modified    status      state   status_code
    ...                         headers
    Set to Dictionary           ${sp_dto}
    ${resp} =                   Fusion Api Edit Server Profile                  ${sp_dto}   uri=${sp_dto['uri']}
    Wait For Task2              ${resp}                 timeout=600             interval=5

    # Verify the storage volumes in the host through SSH
    Sleep               60
    Open Connection And Log In              ${ipv4}     root    Welcome123#
    Execute Command     esxcli storage core adapter rescan --all
    sleep               60
    ${output2} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output2}

    # Checking the volume
    Run Keyword if      """${output1}""" == """${output2}"""    Fail

OVTC57642
    [Documentation]     Create SP with iscsi volumes
    [Tags]              TC02

    ${sp_body} =            copy.deepcopy               ${sp_with_iscsi}
    #Create server profile
    ${blnCreateProf} =      Create I3S Server Profile   ${sp_body}
    Should Be True          ${blnCreateProf}            Failed to create profile '${sp_body['name']}'

    #Edit Sp and Add volumes
    ${sp_dto} =                 Get Resource                SP:${sp_body['name']}
    Remove From Dictionary      ${sp_dto}                   created             modified            status      state
    ...                         status_code
    ...                         headers
    ${san_volume_attachment}=   server_profile.verify storage volume            ${iscsi_volumes_settings_add1}
    ${san_updated_list}=        Combine Lists               ${sp_dto['sanStorage']['volumeAttachments']}
    ...                         ${san_volume_attachment['volumeAttachments']}
    Set To Dictionary           ${sp_dto['sanStorage']}     volumeAttachments   ${san_updated_list}
    ${resp} =                   Fusion Api Edit Server Profile Template         body=${sp_dto}      uri=${sp_dto['uri']}
    Wait For Task2              ${resp}                     timeout=60          interval=5

    #Power ON the SP and wait
    Power on Server     SH:${sp_body['serverHardwareUri']}

    #Get the Management IP and Ping the Server
    Sleep       420
    ${ipv4} =   Get Server Profile Management IP    ${sp_body}
    Ping Profile Management IP                      ${ipv4}

    #Edit Sp and Add volumes
    ${sp_dto} =                 Get Resource                SP:${sp_body['name']}
    Remove From Dictionary      ${sp_dto}                   created             modified            status      state
    ...                         status_code
    ...                         headers
    ${san_volume_attachment}=   server_profile.verify storage volume            ${iscsi_volumes_settings_add2}
    ${san_updated_list}=        Combine Lists               ${sp_dto['sanStorage']['volumeAttachments']}
    ...                         ${san_volume_attachment['volumeAttachments']}
    Set To Dictionary           ${sp_dto['sanStorage']}     volumeAttachments   ${san_updated_list}
    ${resp} =                   Fusion Api Edit Server Profile Template         body=${sp_dto}      uri=${sp_dto['uri']}
    Wait For Task2              ${resp}                     timeout=60          interval=5

    #iSCSI Storage setup for ESXi Hosts From The Command Line
    Sleep               60
    Open Connection And Log In      ${ipv4}     root    Welcome123#
    Execute Command     esxcli iscsi software set -e true
    Execute Command     esxcli iscsi adapter discovery sendtarget add -A vmhba64 -a 10.1.42.10:3260
    Execute Command     esxcli iscsi adapter discovery rediscover -A vmhba64

    # Verify the storage volumes through SSH
    sleep               120
    ${output1} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output1}

    #Delete the shared volume and Edit the SP
    ${sp_dto} =                 Delete Profile Volume   ${sp_body['name']}      ${storage_volumes[10]['properties']['name']}
    Remove From Dictionary      ${sp_dto}               created                 modified    status      state   status_code
    ...                         headers
    Set to Dictionary           ${sp_dto}
    ${resp} =                   Fusion Api Edit Server Profile                  ${sp_dto}   uri=${sp_dto['uri']}
    Wait For Task2              ${resp}                 timeout=600             interval=5

    #Delete the Private volume and Edit the SP
    ${sp_dto} =                 Delete Profile Volume   ${sp_body['name']}      ${storage_volumes[11]['properties']['name']}
    Remove From Dictionary      ${sp_dto}               created                 modified    status      state   status_code
    ...                         headers
    Set to Dictionary           ${sp_dto}
    ${resp} =                   Fusion Api Edit Server Profile                  ${sp_dto}   uri=${sp_dto['uri']}
    Wait For Task2              ${resp}                 timeout=600             interval=5

    # Verify the storage volumes through SSH
    sleep               60
    Execute Command     esxcli iscsi adapter discovery rediscover -A vmhba64
    sleep               120
    ${output2} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output2}

    # Comparing the volumes
    Run Keyword if      """${output1}""" == """${output2}"""    Fail

OVTC57643
    [Documentation]     Create SPT with SAN volumes
    [Tags]              TC03

    ${spt_body} =       copy.deepcopy   ${spt_with_fc}
    ${sp_body} =        copy.deepcopy   ${sp1_from_spt}
    ${sp_list}=         Create List
    Append To List      ${sp_list}      ${sp_body}

    # Create server profile Template
    ${blnCreateProf} =      Create I3S SPT      ${spt_body}
    Should Be True          ${blnCreateProf}    Failed to create profile '${spt_body['name']}'

    # Create Server Profile from the SPT
    ${blnCreateSPfromSPT} =     Create I3S SP From I3S SPT          ${sp_body}
    Run Keyword If              '${blnCreateSPfromSPT}'!='True'     Fail    Failed to create profile    '${sp_body['name']}

    #Edit SPT and Add volumes
    ${spt_dto} =                Get Resource                SPT:${spt_body['name']}
    Remove From Dictionary      ${spt_dto}                  created             modified    status      state   status_code
    ...                         headers
    ${san_volume_attachment}=   server_profile.verify storage volume            ${sanStorage_volumes_add1_spt}
    ${san_updated_list}=        Combine Lists               ${spt_dto['sanStorage']['volumeAttachments']}
    ...                         ${san_volume_attachment['volumeAttachments']}
    Set To Dictionary           ${spt_dto['sanStorage']}    volumeAttachments   ${san_updated_list}
    ${resp} =                   Fusion Api Edit Server Profile Template         body=${spt_dto}
    ...                         uri=${spt_dto['uri']}
    Wait For Task2              ${resp}                     timeout=60          interval=5

    #update the server Profile with the edited SPT
    ${resp} =       Update Server Profiles from Template    ${sp_list}
    ${task_resp}    Wait for task2                          ${resp}     timeout=3600    interval=5

    #Power ON the SP and wait
    Power on Server     SH:${sp_body['serverHardwareUri']}

    #Get the Management IP and Login through SSH
    Sleep       420
    ${ipv4} =   Get Server Profile Management IP    ${sp_body}
    Ping Profile Management IP                      ${ipv4}

    #Edit SPT and Add volumes
    ${spt_dto} =                Get Resource                SPT:${spt_body['name']}
    Remove From Dictionary      ${spt_dto}                  created             modified    status      state   status_code
    ...                         headers
    ${san_volume_attachment}=   server_profile.verify storage volume            ${sanStorage_volumes_add2_spt}
    ${san_updated_list}=        Combine Lists               ${spt_dto['sanStorage']['volumeAttachments']}
    ...                         ${san_volume_attachment['volumeAttachments']}
    Set To Dictionary           ${spt_dto['sanStorage']}    volumeAttachments   ${san_updated_list}
    ${resp} =                   Fusion Api Edit Server Profile Template         body=${spt_dto}
    ...                         uri=${spt_dto['uri']}
    Wait For Task2              ${resp}                     timeout=60          interval=5

    #update the server Profile with the edited SPT
    ${resp} =       Update Server Profiles from Template    ${sp_list}
    ${task_resp}    Wait for task2                          ${resp}     timeout=3600    interval=5

    # Verify the storage volumes in the host through SSH
    Sleep               60
    Open Connection And Log In              ${ipv4}     root    Welcome123#
    ${output1} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output1}

    #Delete the shared volume and Edit the SPT
    ${spt_dto} =                Delete SPT Volume   ${spt_body['name']}     ${storage_volumes[8]['properties']['name']}
    Remove From Dictionary      ${spt_dto}          created                 modified        status      state   status_code
    ...                         headers
    Set to Dictionary           ${spt_dto}
    ${resp} =                   Fusion Api Edit Server Profile              ${spt_dto}      uri=${spt_dto['uri']}
    Wait For Task2              ${resp}             timeout=600             interval=5

    #Delete the Private volume and Edit the SPT
    ${spt_dto} =                Delete SPT Volume   ${spt_body['name']}     ${storage_volumes1[0]['properties']['name']}
    Remove From Dictionary      ${spt_dto}          created                 modified        status      state   status_code
    ...                         headers
    Set to Dictionary           ${spt_dto}
    ${resp} =                   Fusion Api Edit Server Profile              ${spt_dto}      uri=${spt_dto['uri']}
    Wait For Task2              ${resp}             timeout=600             interval=5

    #update the server Profile with the edited SPT
    ${resp} =       Update Server Profiles from Template    ${sp_list}
    ${task_resp}    Wait for task2                          ${resp}     timeout=3600    interval=5

    # Verify the storage volumes through SSH
    sleep               60
    Execute Command     esxcli iscsi adapter discovery rediscover -A vmhba64
    sleep               120
    ${output2} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output2}

    Run Keyword if      """${output1}""" == """${output2}"""    Fail

OVTC57644
    [Documentation]     Create SPT with iscsi volumes
    [Tags]              TC04

    ${spt_body} =   copy.deepcopy   ${spt_with_iscsi}
    ${sp_body} =    copy.deepcopy   ${sp2_from_spt}

    ${sp_list}=         Create List
    Append To List      ${sp_list}      ${sp_body}

    # Create server profile Template
    ${blnCreateProf} =      Create I3S SPT      ${spt_body}
    Should Be True          ${blnCreateProf}    Failed to create profile '${spt_body['name']}'

    # Create Server Profile from the SPT
    ${blnCreateSPfromSPT} =     Create I3S SP From I3S SPT          ${sp_body}
    Run Keyword If              '${blnCreateSPfromSPT}'!='True'     Fail    Failed to create profile    '${sp_body['name']}

    #Edit Spt and Add volumes
    ${spt_dto} =                Get Resource                SPT:${spt_body['name']}
    Remove From Dictionary      ${spt_dto}                  created             modified    status      state   status_code
    ...                         headers
    ${san_volume_attachment}=   server_profile.verify storage volume            ${iscsi_volumes_settings_add1_spt}
    ${san_updated_list}=        Combine Lists               ${spt_dto['sanStorage']['volumeAttachments']}
    ...                         ${san_volume_attachment['volumeAttachments']}
    Set To Dictionary           ${spt_dto['sanStorage']}    volumeAttachments   ${san_updated_list}
    ${resp} =                   Fusion Api Edit Server Profile Template         body=${spt_dto}
    ...                         uri=${spt_dto['uri']}
    Wait For Task2              ${resp}                     timeout=60          interval=5

    #Update the Server Profile from the template
    ${resp} =       Update Server Profiles from Template    ${sp_list}
    ${task_resp}    Wait for task2                          ${resp}     timeout=3600    interval=5

    #Power ON the SP and wait
    Power on Server     SH:${sp_body['serverHardwareUri']}

    #Get the Management IP and Ping
    Sleep       420
    ${ipv4} =   Get Server Profile Management IP    ${sp_body}
    Ping Profile Management IP                      ${ipv4}

    #Edit SPT and Add volumes
    ${spt_dto} =                Get Resource                SPT:${spt_body['name']}
    Remove From Dictionary      ${spt_dto}                  created             modified    status      state   status_code
    ...                         headers
    ${san_volume_attachment}=   server_profile.verify storage volume            ${iscsi_volumes_settings_add2_spt}
    ${san_updated_list}=        Combine Lists               ${spt_dto['sanStorage']['volumeAttachments']}
    ...                         ${san_volume_attachment['volumeAttachments']}
    Set To Dictionary           ${spt_dto['sanStorage']}    volumeAttachments   ${san_updated_list}
    ${resp} =                   Fusion Api Edit Server Profile Template         body=${spt_dto}
    ...                         uri=${spt_dto['uri']}
    Wait For Task2              ${resp}                     timeout=60          interval=5

    #update the server Profile with the edited SPT
    ${resp} =       Update Server Profiles from Template    ${sp_list}
    ${task_resp}    Wait for task2                          ${resp}     timeout=3600    interval=5

    #iSCSI Storage setup for ESXi Hosts From The Command Line
    Sleep               60
    Open Connection And Log In      ${ipv4}     root    Welcome123#
    Execute Command     esxcli iscsi software set -e true
    Execute Command     esxcli iscsi adapter discovery sendtarget add -A vmhba64 -a 10.1.42.10:3260
    Execute Command     esxcli iscsi adapter discovery rediscover -A vmhba64

    # Verify the storage volumes through SSH
    sleep               60
    ${output1} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output1}

    #Delete the shared volume and Edit the SPT
    ${spt_dto} =                Delete SPT Volume   ${spt_body['name']}     ${storage_volumes[10]['properties']['name']}
    Remove From Dictionary      ${spt_dto}          created                 modified        status      state   status_code
    ...                         headers
    Set to Dictionary           ${spt_dto}
    ${resp} =                   Fusion Api Edit Server Profile              ${spt_dto}      uri=${spt_dto['uri']}
    Wait For Task2              ${resp}             timeout=600             interval=5

    #Delete the Private volume and Edit the SP
    ${spt_dto} =                Delete SPT Volume   ${spt_body['name']}     ${storage_volumes1[1]['properties']['name']}
    Remove From Dictionary      ${spt_dto}          created                 modified        status      state   status_code
    ...                         headers
    Set to Dictionary           ${spt_dto}
    ${resp} =                   Fusion Api Edit Server Profile              ${spt_dto}      uri=${spt_dto['uri']}
    Wait For Task2              ${resp}             timeout=600             interval=5

    #update the server Profile with the edited SPT
    ${resp} =       Update Server Profiles from Template    ${sp_list}
    ${task_resp}    Wait for task2                          ${resp}     timeout=3600    interval=5

    # Verify the storage volumes in the host through SSH
    Sleep               60
    Open Connection And Log In              ${ipv4}     root    Welcome123#
    ${output2} =        Execute Command     esxcli storage nmp device list
    Log to Console      ${output2}

    Run Keyword if      """${output1}""" == """${output2}"""    Fail


*** Keywords ***

Delete Profile Volume
    [Documentation]    Delete the SAN volume from Server Profile
    [Arguments]         ${sp_name}                  ${vol1}
    ${sp_resp} =        Get Server Profile          ${sp_name}
    ${volume_uri1} =    Get Storage Volume URI      ${vol1}
    ${vol_count} =      Get Length                  ${sp_resp['sanStorage']['volumeAttachments']}
    :For                ${index}                    In Range            ${vol_count}
    \                   run keyword if              '${sp_resp['sanStorage']['volumeAttachments'][${index}]['volumeUri']}'=='${volume_uri1}'
    \                   ...                         run keywords
    \                   ...                         Remove From List    ${sp_resp['sanStorage']['volumeAttachments']}   ${index}
    \                   ...                         AND
    \                   ...                         Exit For Loop
    \                   Continue For Loop
    Set To Dictionary   ${sp_resp}
    [Return]            ${sp_resp}

Delete SPT Volume
    [Documentation]    Delete the SAN volume from Server Profile Template
    [Arguments]         ${spt_name}                 ${vol1}
    ${spt_resp} =       Get Server Profile Template                     ${spt_name}
    ${volume_uri1} =    Get Storage Volume URI      ${vol1}
    ${vol_count} =      Get Length                  ${spt_resp['sanStorage']['volumeAttachments']}
    :For                ${index}                    In Range            ${vol_count}
    \                   run keyword if              '${spt_resp['sanStorage']['volumeAttachments'][${index}]['volumeUri']}'=='${volume_uri1}'
    \                   ...                         run keywords
    \                   ...                         Remove From List    ${spt_resp['sanStorage']['volumeAttachments']}
    \                   ...                         ${index}
    \                   ...                         AND
    \                   ...                         Exit For Loop
    \                   Continue For Loop
    Set To Dictionary   ${spt_resp}
    [Return]            ${spt_resp}

