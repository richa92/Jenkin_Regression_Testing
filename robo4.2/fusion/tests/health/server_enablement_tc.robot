*** Settings ***
Documentation    Server operations and server profile with BIOS and Boot mode options
Library            FusionLibrary
Library            RoboGalaxyLibrary
Library            OperatingSystem
Library            BuiltIn
Library            Collections
Library            XML
Library            String
Library            json
Library            Process
Suite Setup        Fusion Api Login Appliance    ${Appliance}     ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance
Resource        ../../Resources/api/fusion_api_resource.txt
Variables        data_variables_server_enablement.py


*** Variables ***
${Appliance}        16.83.14.82

*** Test Cases ***
Add server
    Log    Adding server        console=True
    Add Server hardware from variable async    ${server_hardwares}
    ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${host_name}'"
    Return From Keyword If    ${resp['count']}==0    FAIL    Server addition to OV failed

Power on server
    Log    Powering on server        console=True
    Power on Server    ${host_name}
    ${power_state}=    Get Server Power    ${host_name}
    Run keyword if    '${power_state}'!='On'    FAIL    Server power on failed

Refresh server
    Log    Refreshing server    console=True
    ${resp}=    Refresh Server Hardware    ${host_name}
    Run keyword if    ${resp['status_code']} != 202    FAIL    Server refresh failed
    Run keyword if    ${resp['status_code']} == 202    Wait for task2    ${resp}    timeout=1200  interval=5

Reset server from OV
    Log    Resetting server from OV    console=True
    Reset Server    ${host_name}

Power off server
    Log    Powering off server    console=True
    Power off Server    ${host_name}
    ${power_state}=    Get Server Power    ${host_name}
    Run keyword if    '${power_state}'!='Off'    FAIL    Server power off failed

Reset server from ilo
    Log    Resetting server from ilo    console=True
    Reset Server Hardware iLO via cpqlocfg and Wait for Refresh to Finish    ${host_name}

Add server profile with UEFIOptimized and delete SP
    Remove All Alerts
    ${r}=    Add Non Existing Server Profiles    ${SP_1}
    Log    Response:${r}    console=True
    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=1200  interval=10
    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP1[0]['name']}'"
    Return From Keyword If  ${resp['count']}==0  FAIL    Server profile creation failed
    ${r}=    Remove Server Profile  ${SP_1[0]}  force=${True}
    Run keyword if    '${r['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10

Add server profile with UEFI and delete SP
    Remove All Alerts
    ${r}=    Add Non Existing Server Profiles    ${SP_2}
    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=1200  interval=10
    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP2[0]['name']}'"
    Return From Keyword If  ${resp['count']}==0  FAIL    Server profile creation failed
    ${r}=    Remove Server Profile  ${SP_2[0]}  force=${True}
    Run keyword if    '${r['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10

Add server profile with UEFI
    Remove All Alerts
    ${r}=    Add Non Existing Server Profiles    ${SP_3}
    ${task}=    Run keyword if    '${r[0]['status_code']}'=='202'    Wait for task2    ${r}    timeout=1200  interval=10
    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP3[0]['name']}'"
    Return From Keyword If  ${resp['count']}==0  FAIL    Server profile creation failed

Remove server profile
    ${r}=    Remove Server Profile  ${SP_3[0]}  force=${True}
    Run keyword if    '${r['status_code']}'=='202'    Wait for task2    ${r}    timeout=600  interval=10
    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${SP3[0]['name']}'"
    Return From Keyword If  ${resp['count']}!=0  FAIL    Server profile creation failed

Remove server hardwares
    Remove All DL Server Hardware Async
