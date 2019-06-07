*** Settings ***
Documentation    Common keywords for BIOS settings CDP
...             author : Sindhu V Kademane
Resource        ../../../../Resources/api/fusion_api_resource.txt
Library         json
Library         RoboGalaxyLibrary


*** Keywords ***

Check overridden BIOS settings
    [Documentation]     check for overridden BIOS settings
    [Arguments]    ${host}    ${profile}
    ${ilo_ip}=      Get Server Hardware iLO IP      ${host}
    Login to Fusion via SSH    ${Appliance}    ${root_user}    ${root_password}
    ${command} =    Set variable    curl -ksL --user ${ilo_UserName}:${ilo_Password} -X GET https://${ilo_ip}/redfish/v1/Systems/1/bios/
    ${resp}    ${stderr}   ${rc} =    Execute command    ${command}    return_stderr=True    return_rc=True
    Run Keyword If   ${rc} != 0    FAIL    command execution failed.
    ${resp} =    json.loads    ${resp}
    ${ilo_mismatch_list}=    Compare BIOS values in ilo and input    ${profile}    ${resp}
    ${profile_get} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${profile[0]['name']}'"
    ${profile_mismatch_list}=    Compare BIOS values in profile and input    ${profile}    ${profile_get}
    [Return]    ${profile_mismatch_list}    ${ilo_mismatch_list}

Compare BIOS values in ilo and input
    [Documentation]     compare BIOS values in ilo and input
    [Arguments]    ${profile_req}      ${ilo_bios}
    ${mismatch_list_ilo}    Create List
    ${ilo_b} =    json.dumps    ${ilo_bios}
    :FOR    ${bios_setting}     in      @{profile_req[0]['bios']['overriddenSettings']}
    \    ${key}    Set variable    Attributes.${bios_setting['id']}
    \    ${ret}=    Run keyword and ignore error    Dictionary should contain key      ${ilo_b}     ${bios_setting['id']}
    \    Log    ${ret}      console=True
    \    ${retn}=    Run keyword and ignore error    Dictionary should contain key      ${ilo_b}     ${key}
    \    Log    ${retn}      console=True
    \    Run keyword if    '${ret[0]}'=='FAIL' and '${retn[0]}'=='FAIL'    Log    ilo bios does not contain ${key}    console=True
    \    Run keyword if    '${ret[0]}'=='FAIL' and '${retn[0]}'=='FAIL'    Continue for loop
    \    ${ilo_key}=    Set variable if    '${ret[0]}'=='PASS'      ${bios_setting['id']}       ${key}
    \    Log    ilo_key:${ilo_key}      console=True
    \    Log    ilo_bios:${ilo_bios}      console=True
    \    Run keyword if    '${ret[0]}'=='PASS'    Run keyword if    '${bios_setting['value']}'!='${ilo_bios['Attributes']['${ilo_key}']}'    Log    BIOS value is not set at ilo.    console=True
    \    ...        ELSE    Run keyword if    '${ret[0]}'=='FAIL'    Run keyword if    '${bios_setting['value']}'!='${ilo_bios['${ilo_key}']}'    Log    BIOS value is not set at ilo.    console=True
    \    Run keyword if    '${ret[0]}'=='PASS'    Run keyword if    '${bios_setting['value']}'!='${ilo_bios['Attributes']['${ilo_key}']}'    Append to list    ${mismatch_list_ilo}    ${bios_setting['value']}
    \    ...        ELSE    Run keyword if    '${ret[0]}'=='FAIL'    Run keyword if    '${bios_setting['value']}'!='${ilo_bios['${ilo_key}']}'    Append to list    ${mismatch_list_ilo}    ${bios_setting['value']}
    [Return]    ${mismatch_list_ilo}

Compare BIOS values in profile and input
    [Documentation]     Compare BIOS values in profile and input
    [Arguments]     ${profile_body}     ${profile_get}
    ${mismatch_list_profile}    Create list
    :FOR    ${bios_setting}     in      @{profile_body[0]['bios']['overriddenSettings']}
    \    ${resp}=    Run keyword and ignore error   List should contain value      ${profile_get['members'][0]['bios']['overriddenSettings']}    ${bios_setting}
    \    Log    resp:${resp}     console=True
    \    Run keyword if    '${resp[0]}'=='FAIL'    Log    Profile does not contain ${bios_setting['id']}    console=True
    \    Run keyword if    '${resp[0]}'=='FAIL'    Append to list     ${mismatch_list_profile}     ${bios_setting['id']}
    [Return]    ${mismatch_list_profile}

Tear down set up
    [Documentation]    Tear down set up
    Log                     Removing Profiles                   console=True
    Power off ALL Servers   control=PressAndHold
    ${resp_list}=           Remove All Server Profiles Async    force=${True}
    Wait For Task2          ${resp_list}                        timeout=90m
    ${profiles} =           Fusion Api Get Server Profiles
    ${count}=               Convert To String                   ${profiles['count']}
    Run Keyword If          '${count}'!='0'                     FAIL    Deleting all Server Profiles did not succeed
    fusion api logout appliance

Set up for synergy
    [Documentation]     Suite set up for synergy
    Set log level   TRACE
    Fusion Api Login Appliance    ${Appliance}     ${admin_credentials}
    Add LIG from variable async     ${LIG_Data}
    Add Enclosure Group from variable    ${eg}
    Add Logical Enclosure from variable    ${le}

Set up for c7k
    [Documentation]     Suite set up for c7k
    Set log level   TRACE
    Fusion Api Login Appliance    ${Appliance}     ${admin_credentials}
    Add Enclosure Group from variable    ${c7k_enc_groups}
    Add Enclosures from variable        ${c7k_enclosures_managed}

Set up for rack servers
    [Documentation]     Suite set up for rack servers
    Set log level   TRACE
    Fusion Api Login Appliance    ${Appliance}     ${admin_credentials}
