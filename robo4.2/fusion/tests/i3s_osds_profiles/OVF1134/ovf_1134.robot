*** Settings ***
Documentation     OVF1134: i3S - Lifecycle - OS Volumes persist during Server Profile un-assign
...               and assign (rollback, move, hibernate aka suspend-resume)
Resource          resource.robot
Suite Setup       Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown    I3S Suite Teardown
Test Setup        I3S Test Setup


*** Test Cases ***
OVTC52997
    [Documentation]    Verify OS volume is created in i3s when SP is created.
    [Tags]    OVF1134_TC01

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

OVTC52998
    [Documentation]    Verify OS volume will not be created in i3s when un-assigned SP is created.
    [Tags]    OVF1134_TC02

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create un-assigned server profile
    Set To Dictionary    ${sp_body}    serverHardwareUri=${None}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume is assigned to server profile '${sp_body['name']}'
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should be equal as strings    '${os_vol}'    'None'    msg=Volume is not created

OVTC52999
    [Documentation]    Verify OS volume is retained when SP is made unassigned
    [Tags]    OVF1134_TC03

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${blnUnassignProf} =    Unassign I3S Server Profile    ${sp_body['name']}
    Should Be True    ${blnUnassignProf}    Failed to unassign server profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume is retained after unassining profile '${sp_body['name']}'
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should Not be equal as strings    '${os_vol}'    'None'    msg=OS volume is not retained when SP is made unassigned

OVTC53000
    [Documentation]    Verify OS volume is retained when SP is made unassigned
    ...                and assigned back with same server hardware.
    [Tags]    OVF1134_TC04

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${blnUnassignProf}=    Unassign I3S Server Profile    ${sp_body['name']}
    Should Be True    ${blnUnassignProf}    Failed to unassign server profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume is retained after unassining profile '${sp_body['name']}'
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should Not be equal as strings    '${os_vol}'    'None'    msg=OS volume is retained for server profile

    ${blnEditPorf}=    Edit I3S Server Profile    ${serverprofiles}
    Should Be True    ${blnEditPorf}    Failed to update server profile '${serverprofiles['name']}'

    Log    \nVerifying whether OS Volume is retained after assigning hardware to profile '${serverprofiles['name']}'
    ${os_vol}=    Get OS Volume From Server Profile    ${serverprofiles['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS Volume is retained after assigning hardware to profile '${serverprofiles['name']}'

OVTC53002
    [Documentation]    Verify OS volume is retained when SP is assigned
                ...    with different server hardware of same SHT from different enclosure in same LE.
    [Tags]    OVF1134_TC07

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${blnSwapProfile} =    Swap Server profile to different Server    ${sp_body['name']}    ${servers[2]}
    Should Be True    ${blnSwapProfile}    Failed To Swap profile to Different Server

    Log    \nValidating Os Volume after changing server profile hardware
    ${os_vol_after_update_sh}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol_after_update_sh}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof1} =    Get Profile From OS Volume    ${os_vol_after_update_sh}
    Should Be Equal    ${sp_body['name']}    ${prof1}    Os Volume ${os_vol_after_update_sh} associted to profile ${sp_body['name']} is not present in I3S

    Log    Verifying OS volume is retained when SP is assigned with different server hardware of same SHT from same enclosure
    Should Be Equal    ${os_vol}    ${os_vol_after_update_sh}    New Os Volume is created after assining SP with different server os same SHT from same enclosure

OVTC53004
    [Documentation]    Verify OS volume is deleted and
                ...    re-created when SP is assigned with different server hardware of different SHT in same LE.
    [Tags]    OVF1134_TC08

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    # Swap profile to different hardware
    ${blnSwapProfile} =    Swap Server profile to different Server    ${sp_body['name']}    ${servers[3]}
    Should Be True    ${blnSwapProfile}    Failed To Swap profile to Different Server

    ${os_vol_after_update_sh}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol_after_update_sh}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Log    Verifying OS volume is retained when SP is assigned with different server hardware of same SHT from same enclosure
    Should Not Be Equal    ${os_vol}    ${os_vol_after_update_sh}    Os Volume is retained when SP is assigned with different server os different SHT

OVTC53005
    [Documentation]    Verify OS volume is deleted and cannot be retained when corresponding SP is deleted (force)
    [Tags]    OVF1134_TC09

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    Delete Server Profile    ${sp_body['name']}
    ${resp1}=    Get Resource by URI    ${osVolUri}
    Should Be Equal As Integers    ${resp1['status_code']}    404    Failed to delete profile OS volume after deleting profile

OVTC53008
    [Documentation]    Verify the OS volume is deleted and dont re-create
    ...                when changed the deployment plan in unassigned SP.
    [Tags]    OVF1134_TC12

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${blnUnassignProf}=    Unassign I3S Server Profile    ${sp_body['name']}
    Should Be True    ${blnUnassignProf}    Failed to unassign profile '${sp_body['name']}'

    ${blnChangeOsdp}=    Change Server Profile OSDP    ${sp_body['name']}    ${osdps[1]['name']}
    Should Be True    ${blnChangeOsdp}    msg=Faile to change the deployment plan in SP.

    Log    \nVerifying whether OS Volume is recreated to unassigned profile '${sp_body['name']}' after changing OSDP
    ${os_vol_after_changing_dp}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should be Equal   '${os_vol_after_changing_dp}'    'None'    msg=OS Volume is recreated when changed the deployment plan in unassigned SP '${sp_body['name']}'

OVTC53009
    [Documentation]    Verify the OS volume is deleted when removed the deployment plan in SP.
    [Tags]    OVF1134_TC13

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${blnChangeOsdp}=    Change Server Profile OSDP To None    ${sp_body['name']}
    Should Be True    ${blnChangeOsdp}    msg=Faile to remove the deployment plan in SP.
    ${resp1}=    Get Resource by URI    ${osVolUri}
    Should Be Equal As Integers    ${resp1['status_code']}    404    Failed to delete profile OS volume after deleting profile

OVTC53012
    [Documentation]    Verify the creation of Server profile with boot settings or connections missing
    [Tags]    OVF1134_TC16

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${sp_payload}=    Create Server Profile POST Payload    ${sp_body}
    Remove From Dictionary    ${sp_payload}    boot
    Remove From Dictionary    ${sp_payload}    bootMode
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${resp}=    Fusion API Create Server Profile    ${sp_payload}
    ${status}=    Run Keyword And Return Status    should be equal as integers    ${resp['status_code']}    202
    ${task_resp}=    Run Keyword If    '${status}'=='True'    Wait For Task    ${resp}    timeout=1200    interval=5
    ${task_status}=  Run Keyword If    '${status}'=='True'    Run Keyword And Return Status    should be equal    ${task_resp['taskState']}    Completed
    Should Not Be True    ${task_status}    Server Profile ${sp_body['name']} is created successfully which is not expected

OVTC53013
    [Documentation]    Verify the behaviour of SP when deleted the iscsi connection in the software section of SP.
    [Tags]    OVF1134_TC17

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile '${sp_body['name']}'

    Log    \n OS Volume uri before deleting the iscsi connection of profile '${sp_body['name']}'   console=True
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${blnDeleteIscsi}=    Delete iscsi connection From SP    ${sp_body['name']}
    Should Not Be True    ${blnDeleteIscsi}    \Profile '${sp_body['name']}' created without errors
    ${resp1}=    Get Resource by URI    ${osVolUri}
    Should Be Equal As Integers    ${resp1['status_code']}    404    OS volume is not deleted after deleting SP

OVTC53015
    [Documentation]    Verify the behaviour of server profile if we change the bandwidth of the connections in SP.
    [Tags]    OVF1134_TC19

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \n OS Volume uri before deleting the iscsi connection of profile '${sp_body['name']}'   console=True
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Log    \nEdit server profile and change the connection bandwidth to 3500    console=True
    ${spbody}=    Get Server Profile    ${sp_body['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connectionSettings}=    Get from dictionary    ${spbody}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    Set to dictionary    ${connections[0]}    requestedMbps    3500
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20

    ${os_vol1}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should be equal as strings    '${os_vol1}'    '${os_vol}'    msg=OS volume deleted from SP '${spbody['name']}' after changing bandwidth in connection

OVTC53016
    [Documentation]    Verify the behaviour of server profile after upgrade/downgrade of firmware.
    [Tags]    OVF1134_TC20

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile '${sp_body['name']}'

    Log    \n OS Volume uri before deleting the iscsi connection of profile '${sp_body['name']}'   console=True
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${payload} =    Create Server Profile PUT Payload    ${sp_body}
    ${fw_payload} =    Create firmware bundle payload    ${firmware}
    Set To Dictionary    ${payload}    firmware=${fw_payload}

    # append profile type dynamically
    ${default_type} =    Get Server Profile Type
    ${status}    ${return}    Run Keyword and Ignore Error    Get From Dictionary    ${payload}    type
    ${type} =    Set Variable If    '${status}'=='PASS'    ${return}    ${default_type}
    Set to Dictionary    ${payload}    type    ${type}

    ${profile_dto} =     Get Resource  SP:${sp_body['name']}
    ${profile_etag} =     Get From Dictionary        ${profile_dto}    eTag
    ${profile_uri} =  Get From Dictionary        ${profile_dto}    uri
    Set to dictionary    ${payload}    eTag    ${profile_etag}
    ${resp} =  Fusion Api Edit Server Profile  body=${payload}  uri=${profile_uri}  param=?ignoreServerHealth=true
    ${task_resp}    Wait for task2    ${resp}    timeout=3600

    Log    \nVerifying whether OS Volume is assigned to server profile '${sp_body['name']}'
    ${os_vol1}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should be equal as strings    '${os_vol1}'    '${os_vol}'    msg=OS volume deleted from SP '${spbody['name']}' after changing bandwidth in connection

OVTC53017
    [Documentation]    Verify the behaviour of server profile if we change the boot order in SP.
    [Tags]    OVF1134_TC21

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \n OS Volume uri before deleting the iscsi connection of profile '${sp_body['name']}'   console=True
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Log    \nChange boot order to PXE    console=True
    ${spbody}=    Get Server Profile    ${sp_body['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${boot}=    Get from dictionary    ${spbody}    boot
    ${boot_order}=    Get from Dictionary    ${boot}    order
    Set List value    ${boot_order}    0    PXE
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20

    Log    \nVerify volume should created in server profile ${sp_body['name']}    console=True
    ${os_vol1}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should be equal as strings    '${os_vol1}'    '${os_vol}'    msg=OS volume deleted from SP '${spbody['name']}' after changing bandwidth in connection

OVTC53019
    [Documentation]    Verify the behaviour of server profile after adding a new connection to it
    [Tags]    OVF1134_TC22

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \n OS Volume uri before deleting the iscsi connection of profile '${sp_body['name']}'   console=True
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Log    \nAdding new connection to profile    console=True
    ${spbody}=    Get Server Profile    ${sp_body['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connectionSettings}=    Get from dictionary    ${spbody}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    ${networkUri}=    replace string using regexp    ${new_profile_connection['networkUri']}    ETH:    ${EMPTY}
    ${networkUri}=    Get Ethernet URI    ${networkUri}
    Set To Dictionary    ${new_profile_connection}    networkUri    ${networkUri}
    Append To List    ${connections}    ${new_profile_connection}
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20

    ${os_vol1}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should be equal as strings    '${os_vol1}'    '${os_vol}'    msg=OS volume deleted from SP '${spbody['name']}' after changing bandwidth in connection

OVTC54018
    [Documentation]    Verify the OS volume is deleted and re-created when changed the custom attributes in SP.
    [Tags]    OVF1134_TC28

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${osds_settings} =    Set OS Deployment settings    ${osDeploymentSettings}
    ${spbody} =    Get Server Profile    ${sp_body['name']}
    Set To Dictionary    ${spbody}    osDeploymentSettings=${osDeploymentSettings}
    ${sp_uri} =    Get from dictionary    ${spbody}    uri

    ${resp}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    Should Be True    ${blnStatus}    Failed to update SP Custom attributes

    ${os_vol_after_changing_cas}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol_after_changing_cas}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Log    Verify the OS volume is deleted and re-created when changed the custom attributes in SP
    Should Not Be Equal    ${os_vol}    ${os_vol_after_changing_cas}    Os Volume is retained when SP is custom attributes changed

OVTC54020
    [Documentation]    Verify OS volume is retained
                ...    when SP is assigned with different server hardware of same SHT from same enclosure.
    [Tags]    OVF1134_TC30

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${blnSwapProfile} =    Swap Server profile to different Server    ${sp_body['name']}    ${servers[1]}
    Should Be True    ${blnSwapProfile}    Failed To Swap profile to Different Server

    Log    \nValidating Os Volume after changing server profile hardware
    ${os_vol_after_update_sh}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol_after_update_sh}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof1} =    Get Profile From OS Volume    ${os_vol_after_update_sh}
    Should Be Equal    ${sp_body['name']}    ${prof1}    Os Volume ${os_vol_after_update_sh} associted to profile ${sp_body['name']} is not present in I3S

    Log    Verifying OS volume is retained when SP is assigned with different server hardware of same SHT from same enclosure
    Should Be Equal    ${os_vol}    ${os_vol_after_update_sh}    New Os Volume is created after assining SP with different server os same SHT from same enclosure

OVTC54021
    [Documentation]    LE deletion should fail when it has assigned server profiles
    [Tags]    OVF1134_TC31

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${uri} =    Get Logical Enclosure URI    ${le['name']}
    ${resp} =     fusion api delete logical enclosure    uri=${uri}    param=?force=True
    ${blnDeleteLE} =    Capture Task Status    ${resp}    1200
    Should Not Be True    ${blnDeleteLE}    LE is deleted when it has assigned server profiles

OVTC54022
    [Documentation]    Verify the OS volume is deleted and re-created when changed the deployment plan in SP.
    [Tags]    OVF1134_TC32

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${sp_body['name']}

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${osdp_uri} =    Get OSDP URI    ${osdps[1]['name']}
    ${spbody} =    Get Server Profile    ${sp_body['name']}
    Set To Dictionary    ${spbody['osDeploymentSettings']}    osDeploymentPlanUri=${osdp_uri}
    ${sp_uri} =    Get from dictionary    ${spbody}    uri

    ${resp}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    Should Be True    ${blnStatus}    Failed to update SP Custom attributes

    ${os_vol_after_changing_osdp}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol_after_changing_osdp}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Log    Verify the OS volume is deleted and re-created when changed the deployment plan in SP
    Should Not Be Equal    ${os_vol}    ${os_vol_after_changing_osdp}    Os Volume is retained when OSDP changed in SP

*** Comments ***
OVF1134_TCX1
    [Documentation]    LE deletion should be successful when it has un-assigned server profiles
    ...    When LE having only the unassigned SP's is deleted, then the OS volumes associated with those un-assigned SP's should be deleted.
    [Tags]    OVF1134_TCX1

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    ${blnUnassignProf} =    Unassign I3S Server Profile    ${sp_body['name']}
    Should Be True    ${blnUnassignProf}    Failed to unassign server profile '${sp_body['name']}'

    ${uri} =    Get Logical Enclosure URI    ${le['name']}
    ${resp} =     fusion api delete logical enclosure    uri=${uri}    param=?force=True
    ${blnDeleteLE} =    Capture Task Status    ${resp}    1200
    Should Be True    ${blnDeleteLE}    LE is not deleted when it has un-assigned server profiles

    Log    \nVerifying whether OS Volume is retained after unassining profile '${sp_body['name']}'
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should Not be equal as strings    '${os_vol}'    'None'    msg=OS volume is not retained when SP is made unassigned

    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal As Strings    ${prof}    ${None}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is present in I3S
