*** Settings ***
Documentation       Reimage Oneview and I3S
Resource            ../resource.robot
Library             DateTime
Suite Setup         Set Log Level    TRACE

*** Test Cases ***
Get number of i3s appliances in the test ring
    [Documentation]    1-Get number of i3s appliances in the test ring
    [Tags]    critical    INITIAL-SETUP    INITIAL-I3S
    ${i3s_appliances_count} =    Get Length    ${i3s_appliances}
    Set Suite Variable    ${i3s_appliances_count}

Get number of OV appliances in the test ring
    [Documentation]    2-Get number of OV appliances in the test ring
    [Tags]    critical    INITIAL-SETUP
    ${ov_appliances_count} =    Get Length    ${ov_appliances}
    Set Suite Variable    ${ov_appliances_count}

Install I3S build on I3S appliances
    [Documentation]    3-Install I3S build on I3S appliances
    [Tags]    critical    INITIAL-SETUP    INITIAL-I3S
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \    Login to Appliance via SSH    ${i3s_ip}
    \    ${output} =   Execute Command  /sbin/hponcfg -f /ci/etc/usb-reimage/ilo_ribcl_developer_usb_reimage.xml
    \    Should Contain    ${output}    succeeded
    \    Start Command    reboot -f now
    \    Wait Until Keyword Succeeds    10min  3sec  Appliance is unreachable    ${i3s_ip}

Install OV build on OV appliances
    [Documentation]    4-Install OV build on OV appliances
    [Tags]    critical    INITIAL-SETUP
    ${ov_appliances_count} =    Get Length    ${ov_appliances}
    Login to Appliance via SSH    ${ov_appliances[0]}
    ${output}    ${rc} =    Execute Command    cat /ci/etc/network | grep CLUSTER_MGMT_MASK    return_stdout=True    return_rc=True
    ${cluster_formed} =    run keyword if    ${rc} == 0    set variable    True
    Run Keyword IF    ${ov_appliances_count}==2 and ${cluster_formed}    Trigger on 2 node withcluster
    ...    ELSE IF    ${ov_appliances_count}==2 and ${cluster_formed} is None    Trigger on 2 node withoutcluster
    ...    ELSE    Trigger on 1 node

Check OV appliances reachable post install complete time
    [Documentation]    5-Check OV appliances reachable post install complete time
    [Tags]    critical    INITIAL-SETUP
    ${DateTime} =    Get Current Date
    Log    Time: ${DateTime}    console=True
    Sleep    1h 45min
    :FOR    ${ov_ip}    IN    @{ov_appliances}
    \    Wait Until Keyword Succeeds    30min    3sec    resource.Wait For Appliance To Become Pingable    ${ov_ip}
    \    Login to Appliance via SSH    ${ov_ip}

Check OV appliances webapps started
    [Documentation]    6-Check OV appliances webapps started
    [Tags]    critical    INITIAL-SETUP
    :FOR    ${ov_ip}    IN    @{ov_appliances}
    \    Wait For Appliance To Be Ready    [${ov_ip}]

Check I3S appliances reachable post install complete time
    [Documentation]    7-Check I3S appliances reachable post install complete time
    [Tags]    critical    INITIAL-SETUP    INITIAL-I3S
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \    Wait Until Keyword Succeeds    50min    3sec    resource.Wait For Appliance To Become Pingable    ${i3s_ip}

Check I3S appliances webapps started
    [Documentation]    8-Check I3S appliances webapps started
    [Tags]    critical    INITIAL-SETUP    INITIAL-I3S
    :FOR    ${i3s_ip}    IN    @{i3s_appliances}
    \    Wait Until Keyword Succeeds    10min    3sec    Wait For Appliance To Be Ready    [${i3s_ip}]

Accept eula
    [Documentation]    9-Accept eula
    [Tags]    critical    INITIAL-SETUP
    Login to Appliance via SSH    ${OV_ACTIVE}
    ${output} =    Execute Command    curl -ikg -X POST -H 'Content-Type: application/json' https://localhost/rest/appliance/eula/save -d '{"supportAccess":"yes"}'
    Should Contain    ${output}    ${status}

Change default Admin password
    [Documentation]    10-Change default Admin password
    [Tags]    critical    INITIAL-SETUP
    Login to Appliance via SSH    ${OV_ACTIVE}
    ${output} =    Execute Command    curl -ikg -X POST -H 'Content-Type: application/json' -H 'X-API-Version: 300' https://localhost/rest/users/changePassword -d '{"newPassword":"${NEW_PASSWORD}", "oldPassword":"admin", "userName":"Administrator"}'

Login to Ov Appliance using ipv6
    [Documentation]    11-Login to Ov Appliance using ipv6
    [Tags]    critical    INITIAL-SETUP
    ${admin_credentials} =    Create Dictionary    userName=${DEFAULT_USER}
    ...                                            password=${NEW_PASSWORD}
    Set Suite Variable    ${admin_credentials}    ${admin_credentials}
    ${Response}    ${SessionId} =    Fusion Api Login Appliance    [${OV_ACTIVE}]    ${admin_credentials}    300

Configure OV with ip4
    [Documentation]    12-Configure OV with ip4
    [Tags]    critical    INITIAL-SETUP
    ${Response} =    Fusion Api Configure Appliance Interfaces    ${network}    300
    ${Resp} =    Fusion Api Get Resource    ${Response['headers']['Location']}
    ${Errors} =    Get From Dictionary    ${Resp}    taskErrors
    ${error_count} =    Get Length    ${Errors}
    Should be True    ${error_count} == 0    msg=Errors encountered while configuring OV with ipv4
    Wait Until Keyword Succeeds    5min    3sec    resource.Wait For Appliance To Become Pingable    ${fusion_IP}
