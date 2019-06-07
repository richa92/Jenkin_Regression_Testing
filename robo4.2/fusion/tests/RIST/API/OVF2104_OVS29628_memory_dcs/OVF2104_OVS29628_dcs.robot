*** Settings ***
Documentation                   Using DCS tbird schema - synergy_3encl_demo - OVF2104 server memory inventory tests, positive and negative fault injection tests
...                            - Schematics to be used:  synergy_3encl_demo (tbird) and C7000_4Encl (C7000)
...                            -  Add DCS Base Resources networks
...                            -  Add Potash LIG, SAS LIG, create EG, and LE
...                            -  Remove Base Resources

Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}         ${FUSION_IP}
${DATA_FILE}        ./Dcs_Data.py
&{admin_credentials}         userName=${FUSION_ADMIN_LOGIN}         password=${FUSION_ADMIN_PASSWORD}

*** Test Cases ***
TestCase Check Monitored Gen10 server memory with Power On
    [Tags]    OVF2104-DCS-tbird-1-2
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1000    interval=5
    Should Match DCS Gen10 server memory  ${enc1_sy660}
    Power on Servers in Profiles    ${gen10_server_profiles}
    ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1000    interval=5
    Should Match DCS Gen10 server memory  ${enc1_sy660}

Add Base Resources
    [Tags]    OVF2104-DCS-tbird-ABR
	Add Ethernet Networks from variable	${ethernet_networks}
	Add FC Networks from variable  ${fc_networks}
	Add LIG from list  ${ligs}
	Add SAS LIG from list  ${sasligs}
   Add Enclosure Group from list  ${egs}

Add LE1
    [Tags]    Performance    logical_enclosures-condition-3encl
    Add Logical Enclosure from list  ${les}

TestCase Check Gen10 server memory with Power On
    [Tags]    OVF2104-DCS-tbird-3
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1000    interval=5
    Should Match DCS Gen10 server memory  ${enc1_sy660}
    # check the state - it should be collectedStale in PoweredOff state
    Wait Until Keyword Succeeds  180  10  DCS Memory State Check  ${enc1_sy660}     CollectedStale

    Power on Servers in Profiles    ${gen10_server_profiles}
    ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1000    interval=5
    Should Match DCS Gen10 server memory  ${enc1_sy660}
    # check the state - it should be collected in PoweredOn state
    Wait Until Keyword Succeeds  180  10  DCS Memory State Check  ${enc1_sy660}     Collected

    ${blade_id} =    Get Blade Id  Condor
    ${dcs_condor} =  DCS Api Get Blade  ${APPLIANCE_IP}  ${blade_id}
    ${dcs_condor_power} =  DCS Api Post Blade Power  ${APPLIANCE_IP}  ${blade_id}

TestCase Verify Gen9 server memory
   [Tags]    OVF2104-DCS-tbird-4-5
   Power off Server  ${ENC1SHBAY5}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY5}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${ENC1SHBAY5}'"
   ${subR} =     Get From Dictionary        ${resp['members'][0]}    subResources
   Run Keyword If  ${subR}!=None   Fail Verify tbird Gen9 server memory failed

   Power on Server  ${ENC1SHBAY5}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY5}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${ENC1SHBAY5}'"
   ${subR} =     Get From Dictionary        ${resp['members'][0]}    subResources
   Run Keyword If  ${subR}!=None  Fail Verify tbird Gen9 server memory failed

   Power off Server  ${ENC1SHBAY3}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY3}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${ENC1SHBAY5}'"
   ${subR} =     Get From Dictionary        ${resp['members'][0]}    subResources
   Run Keyword If  ${subR}!=None  Fail Verify tbird Gen9 server memory failed

   Power on Server  ${ENC1SHBAY3}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY3}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${ENC1SHBAY5}'"
   ${subR} =     Get From Dictionary        ${resp['members'][0]}    subResources
   Run Keyword If  ${subR}!=None  Fail Verify tbird Gen9 server memory failed

TestCase Gen10 Server with expand=all with api=800 should not have subresources
   [Tags]    OVF2104-DCS-tbird-6
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC1SHBAY6}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all  api=800
   Dictionary Should Not Contain Key  ${resp}  subResources  msg=test passed

TestCase Server with expand=none
   [Tags]    OVF2104-DCS-tbird-7
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC1SHBAY6}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=none
   ${subR} =     Get From Dictionary        ${resp}    subResources
   Run Keyword If  ${subR}==None   Fail expand=none returns None

TestCase Simulate Faulty Dimm on Condor
   [Tags]    OVF2104-DCS-tbird-8
   ${processor} =    Set Variable    1
   ${dimm} =    Set Variable    1
   ${blade_id} =    Get Blade Id  Condor
   DCS Api Post Blade Set DimmMemoryFault  ${APPLIANCE_IP}  ${blade_id}  ${processor}  ${dimm}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY6}
   Wait for task2  ${resp}   timeout=1000    interval=10
   Wait Until Keyword Succeeds  180  10  Memory Dimm Health Check  ${enc1_sy660['server']}     Critical

TestCase Clear Faulty Dimm on Condor
   [Tags]    OVF2104-DCS-tbird-9
   ${processor} =    Set Variable    1
   ${dimm} =    Set Variable    1
   ${blade_id} =    Get Blade Id  Condor
   DCS Api Post Blade Clear DimmMemoryFault  ${APPLIANCE_IP}  ${blade_id}  ${processor}  ${dimm}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY6}
   Wait for task2  ${resp}   timeout=1000    interval=10
   Wait Until Keyword Succeeds  180  10  Memory Dimm Health Check  ${enc1_sy660['server']}     OK

TestCase Remove DIMM and verify
    [Tags]    OVF2104-DCS-tbird-10
    ${processor} =    Set Variable    1
    ${dimm} =    Set Variable    3
    ${blade_id} =    Get Blade Id  Condor
    DCS Api Post Blade Remove Dimm   ${APPLIANCE_IP}  ${blade_id}  ${processor}  ${dimm}
    Power on server  SH:${ENC1SHBAY6}
    ${resp} =  Refresh Server Hardware  ${ENC1SHBAY6}
    Wait for task2  ${resp}   timeout=1000    interval=10
    Wait Until Keyword Succeeds  180  10  Remove Dimm State Check  ${enc1_sy660['server']}     Absent

Testcase Create profile and check server memory
    [Tags]    OVF2104-DCS-tbird-11
    Power off Servers in Profiles    ${gen10_server_profiles}
    Create Gen10 Server Profiles
    Should Match DCS Gen10 server memory  ${enc1_sy660}

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Create Gen10 Server Profiles
    [Documentation]  Create Gen10 Server Profiles
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{gen10_server_profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      log        ${resp}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2400    interval=15

Verify Internal External Storage with RIS
    [Documentation]  Verify Internal (With I) and external Storage drives details with RIS
    Power on Servers in Profiles  ${server_profile}
    Run Keyword and Ignore Error    Wait for Servers in Profiles to reach POST State  ${server_profile}
    Verify RIS Nodes for List  ${ris_nodes_create}

Edit Gen10-Sy660 Server Profile
    [Documentation]  Edit profile, add more LS options
    Power off Servers in Profiles    ${server_profile}
	${resp} = 	Edit Server Profile	${edit_profile_add_moreLS}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]  cleanup
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Remove All Server Profile Templates
    Fusion Api Logout Appliance

Get Blade Id
    [Documentation]  Get condor id
    [Arguments]        ${blade_name}
    ${dcs_enc1} =  DCS Api Get Enc1  ${APPLIANCE_IP}
    Log  ${dcs_enc1}    console=True
    ${targets} =    Set Variable    ${dcs_enc1['InstanceInfo']['targets']}
    ${entities} =    Set Variable    ${targets[0]['EntityInstance']}
    Log  ${entities}    console=True
    :FOR    ${entity}    IN    @{entities}
    \       ${blade_id} =    Run Keyword If  '${entity['type']}'=='${blade_name}'  Set Variable    ${entity['name']}
    \       Exit for loop If	'${blade_id}' != 'None'
    Log  ${blade_id}    console=True
    [Return]   ${blade_id}

Memory Dimm Health Check
    [Documentation]  Dimm health status check
    [Arguments]        ${server}    ${status}
    ${subR} =     Get Server Hardware Subresources        ${server}
    ${memory} =     Get From Dictionary     ${subR}     Memory
    ${m_status} =     Get From Dictionary   ${memory['data'][0]}    Status
    ${m_health} =     Get From Dictionary   ${m_status}     Health
    Should Match    ${m_health}     ${status}

Remove Dimm State Check
    [Documentation]  Remove Dimm State Check
    [Arguments]        ${server}    ${state}
    ${dimm} =    Set Variable    3
    ${subR} =     Get Server Hardware Subresources        ${server}
    ${memory} =     Get From Dictionary        ${subR}    Memory
    ${m_status} =     Get From Dictionary        ${memory['data'][${dimm}-1]}    Status
    ${m_State} =     Get From Dictionary        ${m_status}    State
    Should Match    ${m_State}     ${state}
