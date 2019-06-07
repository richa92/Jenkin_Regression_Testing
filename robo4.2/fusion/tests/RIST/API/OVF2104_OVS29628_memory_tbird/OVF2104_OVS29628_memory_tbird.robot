*** Settings ***
Documentation                   Server memory inventory tests
...                               -  For servers Gen10 Sy480, Sy660, Gen9 Sy480 and Sy660
...                               -  Checks for subresources data, collection states
...                               -  Remove Base Resources

Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

#Resource            ./../../../../Resources/api/fusion_api_resource.txt
#Resource            ../global_variables.robot
#Variables 		    ${DATA_FILE}

Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py
${SKIPSETUP}                    ${False}
${SKIPTEARDOWN}                 ${False}
${VERBOSE}                      ${False}

${IP}             16.114.209.223     # appliance IP
${TPWPORT}        17988             # ToxiProxy Webserver port
#${TP}             fe80::5b49:861f:e732:ce2d    # Dedicated IP for ToxiProxy managed device testing
#${TPCIDR}         64                # cidr for the Dedicated IP
#
#${DEVICE_IP}      FE80::32E1:71FF:FE64    # Managed device iLO IP. DL160
#${DEVICE_PORT}    6001              # dedicated tcp port for the proxy traffic
#${PXY_NAME} =     ${DEVICE_PORT}proxy
#${TX_NAME} =      ${DEVICE_PORT}latency_toxic

${RM_PXY_NAME} =     RM-RM-Proxy
${RMRMPORT} =     8080
${TX_URL} =     server-hardware
${TX_TYPE} =     http_latency
${TX_NAME} =     ${TX_URL}_${TX_TYPE}_toxic

*** Test Cases ***
TestCase Check Gen10 server memory with Power On
    [Tags]    OVF2104-TC-4-1-4-2
    Power on Servers in Profiles    ${gen10_server_profiles}
    ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1000    interval=5
    Should Match Gen10 servers memory  ${ris_nodes_in_profiles}

TestCase Verify Gen10 server memory with Power Off
   [Tags]    OVF2104-TC-4-3
   Power off Servers in Profiles    ${gen10_server_profiles}
   ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
   Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=500    interval=5
   Should Match Gen10 servers memory  ${ris_nodes_in_profiles}

TestCase Verify Gen9 server memory
   [Tags]    OVF2104-TC-4-4-4-5
   ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${ENC1SHBAY3}'"
   ${subR} =     Get From Dictionary        ${resp['members'][0]}    subResources
   Run Keyword If  ${subR}!=None  Verify tbird Gen9 server memory failed

   Power off Server  ${ENC1SHBAY3}
   Power on Server  ${ENC1SHBAY3}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY3}
   Wait for task2  ${resp}   timeout=180    interval=10

   Reset Server Hardware iLO and Wait for System Refresh to Finish  ${ENC1SHBAY3}

   ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${ENC1SHBAY3}'"
   ${subR} =     Get From Dictionary        ${resp['members'][0]}    subResources
   Run Keyword If  ${subR}!=None  Verify tbird Gen9 server memory failed

TestCase Verify Gen10 server memory after power on
   [Tags]    OVF2104-TC-4-8-4-9
   Power off Servers in Profiles    ${gen10_server_profiles}
   Create Gen10 Server Profiles
   Power on Servers in Profiles    ${gen10_server_profiles}
   ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
   Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1200    interval=5
   Should Match Gen10 servers memory  ${ris_nodes_in_profiles}
   Reset Servers in Profiles  ${gen10_server_profiles}  powerControl=ColdBoot
   Reset Tbird Servers iLOs in Profiles  ${gen10_server_profiles}
   Reset Server Hardware iLO via cpqlocfg and Wait for Refresh to Finish  ${ENC1SHBAY8}
   Should Match Gen10 servers memory  ${ris_nodes_in_profiles}

TestCase Gen10 SH with api800 subresources should not be there
    [Tags]    OVF2104-TC-4-10
    ${sh_uuid} =  Get Resource Attribute  SH:${ENC2SHBAY6}  uuid
    ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all  api=800
    Dictionary Should Not Contain Key   ${resp}   subResources

TestCase refresh server get collection state for all 3 components while refresh is happening
    [Tags]    OVF2104-TC-4-12
    Power on Server  SH:${ENC2SHBAY6}
    ${resp} =     Refresh Server Hardware  SH:${ENC2SHBAY6}
    ${i} =    Set Variable    0
    :FOR    ${i}    IN    @{1,2,3,4,5}
    \    ${subresources} =     Get Server Hardware Subresources        ${ENC2SHBAY6}
    \    Log    ${subResources['Memory']['collectionState']}
    \    Log    ${subResources['MemoryList']['collectionState']}
    \    Log    ${subResources['AdvancedMemoryProtection']['collectionState']}
    \    Sleep    10s
    Wait For Task2   ${resp}   timeout=1200   interval=5

TestCase Gen10 GET SH without expand all
    [Tags]    OVF2104-TC-4-15-4-16
    ${sh_uuid1} =  Get Resource Attribute  SH:${ENC2SHBAY6}  uuid
    ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid1}
    ${subR1} =     Get From Dictionary        ${resp}    subResources
    Run Keyword If  ${subR1}== 'None'  Fail  msg=suresources is not None for Gen10 SY660
    ${sh_uuid2} =  Get Resource Attribute  SH:${ENC1SHBAY8}  uuid
    ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid2}
    ${subR2} =     Get From Dictionary        ${resp}    subResources
    Run Keyword If  ${subR2}== 'None'  Fail  msg=suresources is not None for Gen10 SY480

TestCase Get all SH ILO_IPs
    ${ilo_ips} =     Get All Server Hardwares iLO IPs
    log        ${ilo_ips}

TestCase Check Gen10 server memory with RM to RM increasing latency toxics
    [Setup]      RMtoRM Proxy setup   proxy=${RM_PXY_NAME}

    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    :FOR    ${latency}   IN RANGE    1000   1301   100
    \    ${resp} =    Toxiproxy create a new toxic   proxy=${RM_PXY_NAME}
    \    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"logfilename":"${TX_NAME}.log", "urlsubstr":"${TX_URL}", "latency":${latency},"jitter":1}}
    \    Power off Servers in Profiles    ${gen10_server_profiles}
    \    Power on Servers in Profiles  ${gen10_server_profiles}
    \    ${responses} =     Refresh Servers in Profiles    ${gen10_server_profiles}
    \    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=2000    interval=5
    \    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    \    ${resp} =    ToxiProxy Remove an active toxic    ${RM_PXY_NAME}   ${TX_NAME}
    \    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}

#TestCase Check Gen10 server memory with ilo to OV increasing latency toxics
#    [Setup]      Proxy setup   proxy=${PXY_NAME}
#
#    ${resp} =    Toxiproxy create a new toxic   proxy=${PXY_NAME}
#    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"latency":1000,"jitter":1}}
#
#    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
##    :FOR    ${latency}   IN RANGE    1000   5001   1000
#    \    ${resp} =    Toxiproxy update an active toxic   proxy=${PXY_NAME}    toxic=${TX_NAME}
#    \    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"latency":${latency},"jitter":1}}
#    \    Power on Servers in Profiles  ${gen10_DL_server_profiles}
#    \    Refresh Gen10 DLs
#    \    Should Match Gen10 Server Memory   ${ris_node160}
#
*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]  Clean Up
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Remove All Server Profile Templates
    Fusion Api Logout Appliance

Verify tbird Gen9 server memory
    [Documentation]  Verify tbird Gen9 server memory
    Run Keyword If    ${verify_gen9_servers} is not ${None}        Verify Resources For list    ${verify_gen9_servers}

Verify tbird Gen10 servers memory
    [Documentation]  Verify tbird Gen10 servers memory
    :FOR    ${ris}    IN    @{ris_nodes}
    \      Verify Gen10 server memory   ${ris}

Create Gen10 Server Profiles
    [Documentation]  Create Gen10 Server Profiles
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{gen10_server_profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      log        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=2400    interval=15

Get All Server Hardwares iLO IPs
    [Documentation]  Get All Server Hardwares iLO IPs
    ${servers}=      Fusion Api Get Server Hardware
    ${ilo_list}=     Create List
    :FOR    ${server}    IN    @{servers['members']}
    \       ${server_name}=    Set Variable    ${server["name"]}
    \       ${ilo}=    Get Server Hardware iLO IP    ${server_name}
    \       ${dict} =  create dictionary
    \       set to dictionary   ${dict}  name=${server_name}
    \       set to dictionary   ${dict}  ip=${ilo}
    \       Append To List    ${ilo_list}  ${dict}
    [Return]  ${ilo_list}

Reset Servers in Profiles
    [Documentation]    Reset servers defined in profiles.
    ...                    Reset Servers in Profiles  ${profiles}  powerControl=ColdBoot
    [Arguments]     ${profiles}  ${powerControl}=Reset
    ${resplist} =  create list
    Log      Resetting Servers in Profiles    console=True
    :FOR    ${profile}    IN    @{profiles}
    \   ${sh_name} =  Get From Dictionary  ${profile}  serverHardwareUri
#    \   Reset Server  ${sh_name}  ${powerControl}  - nothing is returned from reset server - need to check
    \   ${resp} =  Reset Server  ${sh_name}  ${powerControl}
    \   append to list  ${resplist}  ${resp}
    [return]  ${resplist}

Reset Tbird Servers iLOs in Profiles
    [Documentation]    Reset Tbird Servers iLOs in Profiles
    ...                    Reset Tbird Servers iLOs in Profiles  ${profiles}
    [Arguments]     ${profiles}
    Log      Resetting Servers iLOs in Profiles    console=True
    :FOR    ${profile}    IN    @{profiles}
    \   ${sh_name} =  Get From Dictionary  ${profile}  serverHardwareUri
    \   Reset Server Hardware iLO and Wait for System Refresh to Finish  ${sh_name}  timeout=1200  interval=10

Refresh Servers in Profiles
    [Documentation]    Refresh servers defined in profiles.
    [Arguments]     ${profiles}
    ${resplist} =  create list
    Log      Refreshing Servers in Profiles    console=True
    :FOR    ${profile}    IN    @{profiles}
    \   ${sh} =  Get From Dictionary  ${profile}  serverHardwareUri
    \   ${resp} =  Refresh Server Hardware  ${sh}
    \   append to list  ${resplist}  ${resp}
    [return]  ${resplist}

RMtoRM Proxy setup
    [Documentation]   RMtoRM Proxy setup
    [Arguments]    ${proxy}
    Return from keyword if   ${SKIPSETUP} is ${True}
    ToxiProxy install on appliance    ${APPLIANCE_IP}
    Test Setup
    # update listen.conf
    ${resp} =    ToxiProxy update listen.conf on appliance for RM to RM testing    ${APPLIANCE_IP}   ${RMRMPORT}
    Start toxiproxy webserver
    ${pxy} =     ToxiProxy build proxy json    name=${proxy}
    ...                                        listen=0.0.0.0:80
    ...                                        upstream=0.0.0.0:8080
    ${resp} =    ToxiProxy Create a new proxy    ${pxy}
    Log   ${proxy} created successfully    console=True

Test Setup
    [Documentation]   test setup for all test cases
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance        ${APPLIANCE_IP}    ${admin_credentials}
    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}

Start ToxiProxy Webserver
    [Documentation]   Start ToxiProxy Webserver
    ${resp} =    ToxiProxy start webserver on appliance and open firewall port    ${APPLIANCE_IP}    ${TPWPORT}
    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    ${resp} =    Toxiproxy get version
    log   \n${resp}   console=True

RMtoRM Suite Teardown
    [Documentation]   RMtoRM suite teardown
    Return from keyword if   ${SKIPTEARDOWN} is ${True}
    ToxiProxy stop webserver on appliance    ${APPLIANCE_IP}
    ToxiProxy update listen.conf on appliance for RM to RM testing    ${APPLIANCE_IP}   80

TP Suite Setup
    [Documentation]   TP suite setup
    Return from keyword if   ${SKIPSETUP} is ${True}
    ToxiProxy install on appliance    ${APPLIANCE_IP}
    ToxiProxy add IP to appliance for managed device testing    ${APPLIANCE_IP}    ${TP}   ${TPCIDR}

TP Suite Teardown
    [Documentation]   TP suite teardown
    Return from keyword if   ${SKIPTEARDOWN} is ${True}
    ToxiProxy stop webserver on appliance    ${APPLIANCE_IP}
    ToxiProxy remove iptables files on appliance    ${APPLIANCE_IP}

Test Teardown
    [Documentation]   test teardown for all test cases
    Fusion Api Logout appliance