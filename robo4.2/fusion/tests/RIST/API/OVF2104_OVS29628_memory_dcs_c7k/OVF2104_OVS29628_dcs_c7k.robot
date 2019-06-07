*** Settings ***
Documentation                   Using DCS c7k schema - C7000_4Encl - OVF2104 server memory inventory tests, positive and negative fault injection tests
...                            -  Add DCS Base Resources networks
...                            -  Add Potash LIG, SAS LIG, create EG, and LE
...                            -  Gen10 Condor with backplane connections to Mezz1, create with external and internal LS
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
${DATA_FILE}        ./Dcs_Data_c7k.py
&{admin_credentials}         userName=${FUSION_ADMIN_LOGIN}         password=${FUSION_ADMIN_PASSWORD}

*** Test Cases ***
Add Base Resources
    [Tags]    OVF2104-DCS-c7k-ABR
	Add Ethernet Networks from variable	${ethernet_networks}
	Add FC Networks from variable  ${fc_networks}
#	Add Network Sets from variable  ${network_sets}
    Add LIG from list  ${ligs}
    Add Enclosure Group from list  ${enc_groups}
    Add Enclosures from variable  ${enclosures}   timeout=25min

TestCase Check Configured Gen10 server memory with Power On
    [Tags]    OVF2104-DCS-c7k-2
    Power off Server  SH:${ENC4SHBAY5}
    ${resp} =  Refresh Server Hardware  ${ENC4SHBAY5}
    Wait for task2  ${resp}   timeout=1000    interval=10
    Should Match DCS Gen10 server memory  ${enc4_bl460}
    Power on server  SH:${ENC4SHBAY5}
    ${resp} =  Refresh Server Hardware  ${ENC4SHBAY5}
    Wait for task2  ${resp}   timeout=1000    interval=10
    Should Match DCS Gen10 server memory  ${enc4_bl460}
    ${dcs_status} =  DCS Api Get Status  ${APPLIANCE_IP}
    ${dcs_instances} =  DCS Api Get Instances  ${APPLIANCE_IP}
    ${dcs_schematic} =  DCS Api Get Schematic  ${APPLIANCE_IP}
    ${blade_id} =    Get C7k Blade Id  BL460cGen10
    ${dcs_bl460c} =  DCS Api Get Blade  ${APPLIANCE_IP}  ${blade_id}
    ${dcs_bl460c_power} =  DCS Api Post Blade Power  ${APPLIANCE_IP}  ${blade_id}
    ${resp} =  Refresh Server Hardware  ${ENC4SHBAY5}
    Wait for task2  ${resp}   timeout=1000    interval=10
    Should Match DCS Gen10 server memory  ${enc4_bl460}

TestCase Verify Gen9 server memory
   [Tags]    OVF2104-DCS-c7k-3-4
   Power off Server  ${ENC3SHBAY1}
   ${resp} =  Refresh Server Hardware  ${ENC3SHBAY1}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC3SHBAY1}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all
   ${subR} =     Get From Dictionary        ${resp}    subResources
   Run Keyword If  ${subR}!=None   Fail Verify tbird Gen9 server memory failed

   Power on Server  ${ENC3SHBAY1}
   ${resp} =  Refresh Server Hardware  ${ENC3SHBAY1}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC3SHBAY1}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all
   ${subR} =     Get From Dictionary        ${resp}    subResources
   Run Keyword If  ${subR}!=None  Fail Verify tbird Gen9 server memory failed

   Power off Server  ${ENC3SHBAY3}
   ${resp} =  Refresh Server Hardware  ${ENC3SHBAY3}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC3SHBAY3}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all
   ${subR} =     Get From Dictionary        ${resp}    subResources
   Run Keyword If  ${subR}!=None   Fail Verify tbird Gen9 server memory failed

   Power on Server  ${ENC3SHBAY3}
   ${resp} =  Refresh Server Hardware  ${ENC3SHBAY3}
   Wait for task2  ${resp}   timeout=1000    interval=10
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC3SHBAY3}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all
   ${subR} =     Get From Dictionary        ${resp}    subResources
   Run Keyword If  ${subR}!=None  Fail Verify tbird Gen9 server memory failed

TestCase Gen8 Server with expand=all with api=800 should not have subresources
   [Tags]    OVF2104-DCS-c7k-5
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC1SHBAY4}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all  api=800
   Dictionary Should Not Contain Key  ${resp}  subResources  msg=test passed

TestCase Server with expand=none
   [Tags]    OVF2104-DCS-c7k-6
   ${sh_uuid} =  Get Resource Attribute  SH:${ENC4SHBAY5}  uuid
   ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=none
   ${subR} =     Get From Dictionary        ${resp}    subResources
   Run Keyword If  ${subR}==None   Fail expand=none returns None

TestCase Simulate Faulty Dimm on BL460 Gen10
   [Tags]    OVF2104-DCS-c7k-7
   ${processor} =    Set Variable    1
   ${dimm} =    Set Variable    1
   ${blade_id} =    Get C7k Blade Id  BL460cGen10
   DCS Api Post Blade Set DimmMemoryFault  ${APPLIANCE_IP}  ${blade_id}  ${processor}  ${dimm}
   ${resp} =  Refresh Server Hardware  ${ENC4SHBAY5}
   Wait for task2  ${resp}   timeout=1000    interval=10
   Wait Until Keyword Succeeds      180     10      Dimm Health Check      ${enc4_bl460['server']}     Critical

TestCase Clear Faulty Dimm on BL460 Gen10
   [Tags]    OVF2104-DCS-c7k-8
   ${processor} =    Set Variable    1
   ${dimm} =    Set Variable    1
   ${blade_id} =    Get C7k Blade Id  BL460cGen10
   DCS Api Post Blade Clear DimmMemoryFault  ${APPLIANCE_IP}  ${blade_id}  ${processor}  ${dimm}
   ${resp} =  Refresh Server Hardware  ${ENC4SHBAY5}
   Wait for task2  ${resp}   timeout=1000    interval=10
   Wait Until Keyword Succeeds  180  10  Dimm Health Check  ${enc4_bl460['server']}     OK

TestCase Remove DIMM and verify
    [Tags]    OVF2104-DCS-c7k-9
    ${processor} =    Set Variable    1
    ${dimm} =    Set Variable    2
    ${blade_id} =    Get C7k Blade Id  BL460cGen10
    DCS Api Post Blade Remove Dimm   ${APPLIANCE_IP}  ${blade_id}  ${processor}  ${dimm}
    ${resp} =  Refresh Server Hardware  ${ENC4SHBAY5}
    Wait for task2  ${resp}   timeout=1000    interval=10
    Wait Until Keyword Succeeds  180  10  DCS Memory State Check  ${enc4_bl460}     CollectedStale
    Wait Until Keyword Succeeds  180  20  Should Match DCS Gen10 server memory  ${enc4_bl460}

TestCase Remove Server and add back server and verify subresources
    [Tags]    OVF2104-DCS-c7k-10
    ${timeout} =    Set Variable    1000
    ${interval} =    Set Variable    10
    ${location} =    Set Variable    Encl4, bay 5.
    ${bay_num} =    Set Variable    5
    ${enc_id} =    Get Last Enc Id
    ${enc_id} =    Set Variable    Enclosure-${enc_id}
    ${blade_id} =    Get C7k Blade Id  BL460cGen10
    DCS Api Post Remove Blade   ${APPLIANCE_IP}  ${enc_id}  ${bay_num}
    ${blade_id_num} =    Fetch From Right   ${blade_id}     -
    DCS Api Post Add Blade      ${APPLIANCE_IP}     ${enc_id}       ${blade_id_num}     ${bay_num}
    ${task} =  Get task by param  param=?filter="'name'='Add' AND taskStatus='Add server: ${location}'"&sort=created:descending&count=1
    log   The Add server task for server ${blade_id} is ${task}    console=True
    Wait for task2  ${task}  ${timeout}  ${interval}
    Wait Until Keyword Succeeds   ${timeout}  ${interval}  Check Resource Attribute    SH:${ENC4SHBAY5}  status  (?i)OK|Warning
    Sleep  180s
    ${resp} =  Refresh Server Hardware  ${ENC4SHBAY5}
    Wait for task2  ${resp}  ${timeout}  ${interval}
    Wait Until Keyword Succeeds  180  10  DCS Memory State Check  ${enc4_bl460}     CollectedStale
    ${subR} =     Get Server Hardware Subresources        ${enc4_bl460['server']}
    Should Match DCS Gen10 server memory    ${enc4_bl460}

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

Get C7k Blade Id
    [Documentation]  Get c7k blade id
    [Arguments]        ${blade_name}
    ${schema} =  DCS Api Get Schematic  ${APPLIANCE_IP}
    Log  ${schema}    console=True
    ${schema_encs} =    Set Variable    ${schema['Schematic']['Enclosures']['Enclosure']}

    :FOR    ${enc}    IN    @{schema_encs}
    \       ${blades} =    Set Variable    ${enc['DeviceBay']}

    ${all_blades} =   Create List
    :FOR    ${bay}    IN    @{blades}
    \       Append to List  ${all_blades}     ${bay}
    Log  ${all_blades}    console=True

    :FOR    ${blade}    IN    @{all_blades}
    \       ${bl} =    Set Variable    ${blade['Blade']}
    \       ${bl_name} =    Set Variable    ${bl['Name']}
    \       ${bl_name} =    Fetch From Left    ${bl_name}    -
    \       ${blade_id} =    Run Keyword If  '${bl_name}'=='${blade_name}'  Set Variable    ${bl['Name']}
    \       Exit for loop If	'${blade_id}' != 'None'
    Log  ${blade_id}    console=True
    [Return]   ${blade_id}

Get Last Enc Id
    [Documentation]  Get c7k last enc id
    ${schema} =  DCS Api Get Schematic  ${APPLIANCE_IP}
    ${schema_encs} =    Set Variable    ${schema['Schematic']['Enclosures']['Enclosure']}
    :FOR    ${enc}    IN    @{schema_encs}
    \       ${enc_id} =    Set Variable    ${enc['ID']}
    [Return]   ${enc_id}

Dimm Health Check
    [Documentation]  Dimm health status check
    [Arguments]        ${server}    ${status}
    ${subR} =     Get Server Hardware Subresources        ${server}
    ${memory} =     Get From Dictionary     ${subR}     Memory
    ${m_status} =     Get From Dictionary   ${memory['data'][0]}    Status
    ${m_health} =     Get From Dictionary   ${m_status}     Health
    Should Match    ${m_health}     ${status}

Clean Up
    [Documentation]  cleanup
    Fusion Api Logout Appliance