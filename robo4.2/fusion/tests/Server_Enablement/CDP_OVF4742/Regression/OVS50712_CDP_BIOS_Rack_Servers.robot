*** Settings ***
Documentation    CDP - Profile operation on Rack servers
...                author : Sindhu V Kademane
Library            FusionLibrary
Library            RoboGalaxyLibrary
Library            OperatingSystem
Library            BuiltIn
Library            Collections
Library            XML
Library            String
Library            json
Library            Process
Suite Setup        Set up for rack servers
Suite Teardown    Tear down set up
Resource        resources.robot
Resource        ../../../../Resources/api/fusion_api_resource.txt
Variables        OVS50712_CDP_BIOS_Datafile.py


*** Test Cases ***
Add server
    [Documentation]    Add server
    Log    Adding server        console=True
    Add Server hardware from variable async    ${server_hardwares}
    :FOR    ${host_name}    in    @{host_names}
    \    ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${host_name}'"
    \    Return From Keyword If    ${resp['count']}==0    FAIL    Server addition to OV failed

Power off server
    [Documentation]    Power off server
    :FOR    ${host_name}    in    @{host_names}
    \    Log    Powering off server        console=True
    \    Power off Server    ${host_name}
    \    ${power_state}=    Get Server Power    ${host_name}
    \    Run keyword if    '${power_state}'!='Off'    FAIL    Server power on failed

Add server profile with boot mode
    [Documentation]    Add server profile with boot mode
    Remove All Alerts
    :FOR    ${SP}    in    @{SP_1s}
    \    ${r}=    Add Non Existing Server Profiles    ${SP}
    \    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10
    \    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP[0]['name']}'"
    \    Return From Keyword If  ${resp['count']}==0  FAIL    Server profile creation failed
    \    ${r}=    Remove Server Profile  ${SP[0]}  force=${True}
    \    Run keyword if    '${r['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10

Create Server Profiles with Server Hardware
    [Documentation]    Create Server Profiles with Server Hardware
    Remove All Alerts
    ${SP_1s_len} =    Get Length    ${SP_1s}
    :FOR   ${index}  in range  0   ${SP_1s_len}
    \    ${SP_assign}=   Get Variable Value      ${SP_1s[${index}]}
    \    Set to dictionary   ${SP_assign[0]}    serverHardwareUri    SH:${host_names[${index}]}
    \    ${r}=    Add Non Existing Server Profiles    ${SP_assign}
    \    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10
    \    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP_1s[${index}][0]['name']}'"
    \    Return From Keyword If  ${resp['count']}==0  FAIL    Server profile creation failed

Un-assign server profile
    [Documentation]    Un-assign server profile
    Remove All Alerts
    ${SP_1s_len} =    Get Length    ${SP_1s}
    :FOR   ${index}  in range  0   ${SP_1s_len}
    \    ${SP_assign}=   Get Variable Value      ${SP_1s[${index}]}
    \    Set to dictionary   ${SP_assign[0]}    serverHardwareUri    None
    \    ${resp}=    Edit Server Profile     ${SP_assign[0]}
    \    Run keyword if    '${resp['status_code']}'=='202'    Wait for task2    ${resp}    timeout=600  interval=10

Re-assign server profile
    [Documentation]    Re-assign server profile
    Remove All Alerts
    ${SP_1s_len} =    Get Length    ${SP_1s}
    :FOR   ${index}  in range  0   ${SP_1s_len}
    \    ${SP_assign}=   Get Variable Value      ${SP_1s[${index}]}
    \    Set to dictionary   ${SP_assign[0]}    serverHardwareUri    SH:${host_names[${index}]}
    \    ${resp}=    Edit Server Profile     ${SP_assign[0]}
    \    Run keyword if    '${resp['status_code']}'=='202'    Wait for task2    ${resp}    timeout=600  interval=10

Power on Servers in Profiles
    [Documentation]    Power on Servers in Profiles
    Log   Powering on Servers in Profiles    console=True
    :FOR   ${profile}  IN  @{SP_1s}
    \    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${profile[0]['name']}'"
    \    ${sh}=    Get from dictionary    ${resp['members'][0]}    serverHardwareUri
    \    Log    uri:${sh}    console=True
    \    ${server} =   Fusion Api Get Server Hardware     ${sh}
    \    Log    server:${server}    console=True
    \    ${power_state}=    Get Server Power    ${server['name']}
    \    Run Keyword If   '${power_state}' == 'On'    Log    Server Hardware ${server['name']} is powered on    console=true
    \    Run Keyword if   '${power_state}' == 'Off'    Power on Server    ${server['name']}

Remove server profile
    [Documentation]    Remove server profile
    ${SP_1s_len} =    Get Length    ${SP_1s}
    :FOR   ${index}  in range  0   ${SP_1s_len}
    \    Power off Server    ${host_names[${index}]}
    \    ${r}=    Remove Server Profile  ${SP_1s[${index}][0]}  force=${True}
    \    Run keyword if    '${r['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10
    \    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP_1s[${index}][0]['name']}'"
    \    Return From Keyword If  ${resp['count']}!=0  FAIL    Server profile creation failed

Create Unassigned profile with default BIOS overridden settings
    [Documentation]    Create Unassigned profile with default BIOS overridden settings
    Remove All Alerts
    :FOR    ${SP}    in    @{SP_2s}
    \    ${r}=    Add Non Existing Server Profiles    ${SP}
    \    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10
    \    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP[0]['name']}'"
    \    Return From Keyword If  ${resp['count']}==0  FAIL    Server profile creation failed

Edit profile and assign it to Server
    [Documentation]    Edit profile and assign it to Server
    Remove All Alerts
    ${SP_2s_len} =    Get Length    ${SP_2s}
    :FOR   ${index}  in range  0   ${SP_2s_len}
    \    ${SP_assign}=   Get Variable Value      ${SP_2s[${index}]}
    \    Set to dictionary   ${SP_assign[0]}    serverHardwareUri    None
    \    ${resp}=    Edit Server Profile     ${SP_assign[0]}
    \    Run keyword if    '${resp['status_code']}'=='202'    Wait for task2    ${resp}    timeout=600  interval=10
    \    Set to dictionary   ${SP_assign[0]}    serverHardwareUri    SH:${host_names[${index}]}
    \    ${resp}=    Edit Server Profile     ${SP_assign[0]}
    \    Run keyword if    '${resp['status_code']}'=='202'    Wait for task2    ${resp}    timeout=600  interval=10
    \    ${r}=    Remove Server Profile  ${SP_2s[${index}][0]}  force=${True}
    \    Run keyword if    '${r['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10

Create assigned profile with default BIOS overiridden settings
    [Documentation]    Create assigned profile with default BIOS overiridden settings
    Remove All Alerts
    ${SP_2s_len} =    Get Length    ${SP_2s}
    :FOR   ${index}  in range  0   ${SP_2s_len}
    \    ${SP_assign}=   Get Variable Value      ${SP_2s[${index}]}
    \    Set to dictionary   ${SP_assign[0]}    serverHardwareUri    SH:${host_names[${index}]}
    \    ${r}=    Add Non Existing Server Profiles    ${SP_assign}
    \    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10
    \    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP_2s[${index}][0]['name']}'"
    \    Return From Keyword If  ${resp['count']}==0  FAIL    Server profile creation failed
    \    ${r}=    Remove Server Profile  ${SP_2s[${index}][0]}  force=${True}
    \    Run keyword if    '${r['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10

Create assigned server profile with overridden BIOS settings
    [Documentation]    Create assigned server profile with overridden BIOS settings
    Remove All Alerts
    ${SP_3s_len} =    Get Length    ${SP_3s}
    :FOR   ${index}  in range  0   ${SP_3s_len}
    \    ${r}=    Add Non Existing Server Profiles    ${SP_3s[${index}]}
    \    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=1200  interval=10
    \    Power on Server    ${host_names[${index}]}
    \    Power off Server    ${host_names[${index}]}
    \    Power on Server    ${host_names[${index}]}
    \    Power off Server    ${host_names[${index}]}
    \    Power on Server    ${host_names[${index}]}
    \    Sleep    5m
    \    ${profile_diff_list}    ${ilo_diff_list}=    Check overridden BIOS settings    ${host_names[${index}]}    ${SP_3s[${index}]}
    \    Log    ${profile_diff_list}    console=True
    \    Log    ${ilo_diff_list}    console=True
    \    ${p_len}=    Get Length    ${profile_diff_list}
    \    ${i_len}=    Get Length    ${ilo_diff_list}
    \    Run keyword if    ${p_len}!=0 or ${i_len}!=0    FAIL    Bios settings in profile and ilo are different.
