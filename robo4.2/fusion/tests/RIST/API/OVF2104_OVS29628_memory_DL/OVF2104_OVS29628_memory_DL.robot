*** Settings ***
Documentation                   Gen10 Server memory inventory tests
...                               -  For DL160 and DL180 Gen10
...                               -  Remove Base Resources

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

#Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
#Resource            ../global_variables.robot
#Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${SKIPSETUP}                    ${False}
${SKIPTEARDOWN}                 ${False}
${VERBOSE}                      ${False}

#${APPLIANCE_IP}             16.114.219.103    # appliance IP
${TPWPORT}        17988             # ToxiProxy Webserver port

# ToxyProxy setup variables for iLO module to OV toxics
${DEVICE_IP}      16.114.212.95    # Managed device iLO IP. DL180
${DEVICE_PORT}    6001              # dedicated tcp port for the proxy traffic
${ILO_PXY_NAME} =     ${DEVICE_PORT}proxy
${TX_NAME} =      ${DEVICE_PORT}latency_toxic
${TP}             16.114.213.18    # Dedicated IP for ToxiProxy managed device testing
${TPCIDR}         20                # cidr for the Dedicated IP

# ToxyProxy setup variables for RM to RM toxics
${PXY_NAME} =     RM-RM-Proxy
${RMRMPORT} =     8080
${TX_URL} =     server-hardware
${TX_TYPE} =     http_latency
${TX_NAME} =     ${TX_URL}_${TX_TYPE}_toxic

*** Test Cases ***
TestCase Add Gen10 servers as managed
    [Tags]    OVF2104-DL
    Add Gen10 DL servers as managed

TestCase Check Backward Compatibility
    [Tags]    OVF2104-TC-5-8
    ${sh_uuid} =  Get Resource Attribute  SH:${risnode160['server']}  uuid
    ${resp} =     Fusion Api Get Server Hardware        param=/${sh_uuid}?expand=all  api=800
    Should Not Contain     ${resp}  'subResources'

TestCase refresh server get collection state for all 3 components while refresh is happening
    [Tags]    OVF2104-TC-5-9
    Power off Server  SH:${risnode160['server']}
    Power on server  SH:${risnode160['server']}
    ${resp} =     Refresh Server Hardware  SH:${risnode160['server']}
    ${i} =    Set Variable    0
    :FOR    ${i}    IN    @{1,2,3,4,5}
    \    ${subresources} =     Get Server Hardware Subresources        ${risnode160['server']}
    \    Log    ${subResources['Memory']['collectionState']}
    \    Log    ${subResources['MemoryList']['collectionState']}
    \    Log    ${subResources['AdvancedMemoryProtection']['collectionState']}
    \    Sleep    10s
    Wait For Task2   ${resp}   timeout=1200   interval=5

TestCase Check Gen10 DL server memory
   [Tags]    OVF2104-TC-5-10-withoutSP
   Power on Servers in Profiles  ${gen10_DL_server_profiles}
   Refresh Gen10 DLs
   Should Match Gen10 Servers Memory   ${ris_nodes}

TestCase Check Gen10 DL server memory after profile create, power ON and refresh
   [Tags]    OVF2104-TC-5-10-withSP
   Power off Servers in Profiles    ${gen10_DL_server_profiles}
   Create Gen10 DL Server Profiles with Local storage
   Power on Servers in Profiles  ${gen10_DL_server_profiles}
   Refresh Gen10 DLs
   Should Match Gen10 Servers Memory   ${ris_nodes}

TestCase Check Gen10 DL server memory with RM to RM increasing latency toxics
    [Tags]    OVF2104-DL-5-11
    [Setup]      RMtoRM Proxy setup   proxy=${PXY_NAME}

    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    :FOR    ${latency}   IN RANGE    1000   1301   100
    \    ${resp} =    Toxiproxy create a new toxic   proxy=${PXY_NAME}
    \    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"logfilename":"${TX_NAME}.log", "urlsubstr":"${TX_URL}", "latency":${latency},"jitter":1}}
    \    Power off Servers in Profiles    ${gen10_DL_server_profiles}
    \    Power on Servers in Profiles  ${gen10_DL_server_profiles}
    \    Refresh Gen10 DLs
    \    Should Match Gen10 Servers Memory   ${ris_nodes}
    \    Power off Servers in Profiles    ${gen10_DL_server_profiles}
    \    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    \    ${resp} =    ToxiProxy Remove an active toxic    ${PXY_NAME}   ${TX_NAME}
    \    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    RMtoRM Suite Teardown

TestCase Check Gen10 DL server memory with increasing latency toxics
    [Tags]    OVF2104-DL-5-12
    [Setup]      Proxy setup   proxy=${ILO_PXY_NAME}

    ${resp} =    Toxiproxy create a new toxic   proxy=${ILO_PXY_NAME}
    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"latency":50,"jitter":1}}

    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    :FOR    ${latency}   IN RANGE    1000   1301   100
    \    ${resp} =    Toxiproxy update an active toxic   proxy=${ILO_PXY_NAME}    toxic=${TX_NAME}
    \    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"latency":${latency},"jitter":1}}
    \    Power on Servers in Profiles  ${gen10_DL_server_profiles}
    \    Refresh Gen10 DLs
    \    Should Match Gen10 Server Memory   ${ris_node180}
    \    Power off Servers in Profiles    ${gen10_DL_server_profiles}
    \    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    TP Suite Teardown

#Remove toxin
#    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
#    ${resp} =    ToxiProxy Remove an active toxic    ${ILO_PXY_NAME}   ${TX_NAME}

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${gen10_DL_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_DL_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]  Clean Up
    Power off Servers in Profiles    ${gen10_DL_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_DL_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Remove All Server Profile Templates
    Fusion Api Logout Appliance

Create Gen10 DL Server Profiles with Local storage
    [Documentation]  Create Gen10 DL Server Profiles with Local storage
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{gen10_DL_server_profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=2400    interval=15

Refresh Gen10 DLs
    [Documentation]  Refresh Gen10 DLs
    @{responses} =    Create List
    :FOR    ${risnode}    IN    @{ris_nodes}
    \      ${resp} =     Refresh Server Hardware  SH:${risnode['server']}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=10000    interval=15

Add Gen10 DL servers as managed
    [Documentation]    Add Gen10 DL servers as managed
    ${resps}=    Add Server hardware from variable    ${Gen10_DLs}
    Wait For Task2    ${resps}  timeout=10m  interval=5

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

Test Setup
    [Documentation]   test setup for all test cases
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance        ${APPLIANCE_IP}    ${admin_credentials}
    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}

Test Teardown
    [Documentation]   test teardown for all test cases
    Fusion Api Logout appliance

Proxy setup
    [Documentation]   steps to setup and create a proxy
    [Arguments]    ${proxy}
    TP Suite Setup
    Test Setup
    ToxiProxy add iptable file for managed device testing    ${APPLIANCE_IP}   ${APPLIANCE_IP}   ${DEVICE_IP}   ${TP}    ${DEVICE_PORT}
    Start toxiproxy webserver
    ${pxy} =     ToxiProxy build proxy json    name=${proxy}
    ...                                        listen=${TP}:${DEVICE_PORT}
    ...                                        upstream=${DEVICE_IP}:443
    # ...                                        transport=tcp
    ${resp} =    ToxiProxy Create a new proxy    ${pxy}

Start ToxiProxy Webserver
    [Documentation]   Start ToxiProxy Webserver
    ${resp} =    ToxiProxy start webserver on appliance and open firewall port    ${APPLIANCE_IP}    ${TPWPORT}
    ${resp} =    Toxiproxy connect    ${APPLIANCE_IP}    ${TPWPORT}
    ${resp} =    Toxiproxy get version
    log   \n${resp}   console=True

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

RMtoRM Suite Teardown
    [Documentation]   RMtoRM suite teardown
    Return from keyword if   ${SKIPTEARDOWN} is ${True}
    ToxiProxy stop webserver on appliance    ${APPLIANCE_IP}
    ToxiProxy update listen.conf on appliance for RM to RM testing    ${APPLIANCE_IP}   80
