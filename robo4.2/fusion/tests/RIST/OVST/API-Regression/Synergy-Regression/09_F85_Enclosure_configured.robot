*** Settings ***
Resource    resource.txt
Documentation    Test Cases to Perform E-Fuse actions thru Patch Enclosure API
...              on configured Enclosure


Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Library           json
Library           Collections
Library           String
Library           json
Library           SSHLibrary
Library           OperatingSystem
Library           RoboGalaxyLibrary            # DVTs Robot Framework extensions
Library           FusionLibrary                # DVTs Robot Framework extensions

*** Variables ***

${devicebays}    deviceBays
${interconnectbays}    interconnectBays
${timeout}    600s
${interval}   20s

*** Test Cases ***

Refresh Enclosure
    [Documentation]    Refresh Enclosure
    [Tags]  REFRESH
    Log    Refresh Enclosure    console=True
    ${responses}=    Refresh Enclosures Async    ${enclosure}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=5000    interval=20

Set UID on Enclosure and EM
    [Documentation]    Set UID on Enclosure and EM Thru Patch Enclosure
    [Tags]  UID_ENC
    [Template]    Update Data on Enclosure List
    ${uid_on_data}
    ${em_bay1_uid_on}
    ${em_bay2_uid_on}
    ${uid_off_data}
    ${em_bay1_uid_off}
    ${em_bay2_uid_off}

Hard Reset ILO Thru Patch Enclosure
    [Documentation]    Hard Reset ILO Thru Patch Enclosure
    [Tags]  RESET_ILO
    ${name} =     Get From Dictionary  @{dev_bay1_reset}[0]  name
    ${respdata} =    Get Enclosure    ${name}
    ${resource_name} =    Get BayResource URI    @{dev_bay1_reset}[0]    ${respdata}    ${devicebays}
    Update Data on Enclosure List    ${dev_bay1_reset}
    Wait Until Keyword Succeeds  ${timeout}  ${interval}  Get task by param  param=?filter="'name'='Refresh' AND associatedResource.resourceUri='${resource_name}' AND taskState='Running'"&sort=created:descending&count=1
    ${resource_name2} =    Get BayResource URI    @{dev_bay2_reset}[0]    ${respdata}    ${devicebays}
    Update Data on Enclosure List    ${dev_bay2_reset}
    Wait Until Keyword Succeeds  ${timeout}  ${interval}  Get task by param  param=?filter="'name'='Refresh' AND associatedResource.resourceUri='${resource_name2}' AND taskState='Running'"&sort=created:descending&count=1

Set UID and Reset Server ILO
    [Documentation]    Set UID on server and reset ilo Thru Patch Enclosure
    [Tags]  RESET_SRV_ILO
    Log    Set UID on Server thru patch server    console=True
    ${resp}=    Patch Server Hardware  ${server['name']}  op=replace  path=/uidState  value=On
    ${task}=    Run Keyword If  ${resp} is not ${null}    Task Status Should Be    ${resp}    expected_state=${taskstate}
    Run Keyword If  ${task} is not ${null}     Task Message Should Be    ${task}    expected_message=${uid_srv_expected_msg}
    Log    Reset Server ILO thru patch server    console=True
    ${ilo_resp} =    Reset Server Hardware iLO    ${server['name']}
    ${ilo_task}=    Run Keyword If  ${ilo_resp} is not ${null}     Task Status Should Be    ${ilo_resp}    expected_state=${taskstate}
    Run Keyword If  ${ilo_task} is not ${null}     Task Message Should Be    ${ilo_task}    expected_message=${reset_srv_expected_msg}
    Log    Set UID off Server thru patch server    console=True
    ${uid_off_resp}=    Patch Server Hardware  ${server['name']}  op=replace  path=/uidState  value=Off
    ${uid_off_task}=    Run Keyword If  ${uid_off_resp} is not ${null}     Task Status Should Be    ${uid_off_resp}    expected_state=${taskstate}
    Run Keyword If  ${uid_off_task} is not ${null}     Task Message Should Be    ${uid_off_task}    expected_message=${uid_off_srv_expected_msg}
    Wait Until Keyword Succeeds    ${timeout}    ${interval}    Server Refresh Complete    ${server}

E-Fuse InterConnects
    [Documentation]  E-Fuse InterConnects on Enclosure Thru Patch Enclosure
    [Tags]    EFUSE_IC
    Log  E-Fuse InterConnects on Enclosure    console=True
    E-Fuse Actions on Interconnects and Blades in Enclosure    ${efuse_bay3}    baytype=${interconnectbays}
    E-Fuse Actions on Interconnects and Blades in Enclosure    ${efuse_bay6}    baytype=${interconnectbays}

E-Fuse Blades
    [Documentation]  E-Fuse Blades on Enclosure Thru Patch Enclosure
    [Tags]    EFUSE_BLADES
    Log    E-Fuse Blades on Enclosure    console=True
    E-Fuse Actions on Interconnects and Blades in Enclosure    ${efuse_bay1_blade}    baytype=${devicebays}
    E-Fuse Actions on Interconnects and Blades in Enclosure    ${efuse_bay2_blade}    baytype=${devicebays}


Failover EM
    [Documentation]    Failover EM thru patch enclosure
    [Tags]  FAIL_OVER_EM
    Log  FailOver EM on Enclosure    console=True
    ${name} =     Get From Dictionary  @{failover_bay1_em}[0]  name
    ${encUri} =    Get Enclosure URI    ${name}
    ${encData}=    Get Enclosure    ${name}
    ${managerRole} =    Get From Dictionary  ${encData['managerBays'][0]}  role
    Run Keyword If  '${managerRole}' == 'Standby'    Update Data on Enclosure List    ${failover_bay1_em}
    ${refresh_taskresp}=    Run Keyword If  '${managerRole}' == 'Standby'    Get task by param  param=?filter="'name'='Refresh' AND associatedResource.resourceUri='${encUri}'"&sort=created:descending&count=1
    Run Keyword If  ${refresh_taskresp} is not ${null}     Wait For Task2   ${refresh_taskresp}   timeout=1800    interval=20
    ${manager2Role} =    Get From Dictionary  ${encData['managerBays'][1]}  role
    Run Keyword If  '${manager2Role}' == 'Standby'    Update Data on Enclosure List    ${failover_bay2_em}
    ${refresh_taskresp2}=    Run Keyword If  '${manager2Role}' == 'Standby'    Get task by param  param=?filter="'name'='Refresh' AND associatedResource.resourceUri='${encUri}'"&sort=created:descending&count=1
    Run Keyword If  ${refresh_taskresp2} is not ${null}     Wait For Task2   ${refresh_taskresp2}   timeout=1800    interval=20

E-Fuse EM

    [Documentation]    E-Fuse EM thru patch enclosure
    [Tags]  EFUSE_EM
    Remove All Alerts
    ${name} =     Get From Dictionary  @{efuse_em_bay1}[0]  name
    ${encUri} =    Get Enclosure URI    ${name}
    ${encData}=    Get Enclosure    ${name}
    ${managerRole} =    Get From Dictionary  ${encData['managerBays'][0]}  role
    Run Keyword If  '${managerRole}' == 'Standby'    Update Data on Enclosure List    ${efuse_em_bay1}
    ...    ELSE IF  '${managerRole}' == 'Active'    EFuse Action Should Fail on Active Enclosure    ${efuse_em_bay1}
    ${remove_alertresp}=    Run Keyword If  '${managerRole}' == 'Standby'    Wait Until Keyword Succeeds    ${timeout}    ${interval}  Get Alert By Param   param=?filter=description like 'The frame link module in bay 1 has been removed.'
    ${add_alertresp}=    Run Keyword If  '${managerRole}' == 'Standby'    Wait Until Keyword Succeeds    ${timeout}    ${interval}  Get Alert By Param   param=?filter=description like 'The frame link module in bay 1 has been inserted.'
    ${manager2Role} =    Get From Dictionary  ${encData['managerBays'][1]}  role
    Run Keyword If  '${manager2Role}' == 'Standby'    Update Data on Enclosure List    ${efuse_em_bay2}
    ...    ELSE IF  '${manager2Role}' == 'Active'    EFuse Action Should Fail on Active Enclosure    ${efuse_em_bay2}


Reset EM
    [Documentation]    Reset EM thru patch enclosure
    [Tags]  RESET_EM
    Remove All Alerts
    ${name} =     Get From Dictionary  @{reset_em_bay1}[0]  name
    ${encUri} =    Get Enclosure URI    ${name}
    ${encData}=    Get Enclosure    ${name}
    ${managerRole} =    Get From Dictionary  ${encData['managerBays'][0]}  role
    Update Data on Enclosure List    ${reset_em_bay1}
    ${refresh_taskresp}=    Run Keyword If  '${managerRole}' == 'Active'    Get task by param  param=?filter="'name'='Refresh' AND associatedResource.resourceUri='${encUri}'"&sort=created:descending&count=1
    Run Keyword If  ${refresh_taskresp} is not ${null}     Wait For Task2   ${refresh_taskresp}   timeout=2000    interval=20
    ${manager2Role} =    Get From Dictionary  ${encData['managerBays'][1]}  role
    Update Data on Enclosure List    ${reset_em_bay2}
    ${refresh_taskresp2}=    Run Keyword If  '${manager2Role}' == 'Active'    Get task by param  param=?filter="'name'='Refresh' AND associatedResource.resourceUri='${encUri}'"&sort=created:descending&count=1
    Run Keyword If  ${refresh_taskresp2} is not ${null}     Wait For Task2   ${refresh_taskresp2}   timeout=2000    interval=20
    Update Data on Enclosure List    ${reset_em_bay1}
    ${refresh_taskresp3}=    Run Keyword If  '${managerRole}' == 'Active'    Get task by param  param=?filter="'name'='Refresh' AND associatedResource.resourceUri='${encUri}'"&sort=created:descending&count=1
    Run Keyword If  ${refresh_taskresp3} is not ${null}     Wait For Task2   ${refresh_taskresp3}   timeout=2000    interval=20
