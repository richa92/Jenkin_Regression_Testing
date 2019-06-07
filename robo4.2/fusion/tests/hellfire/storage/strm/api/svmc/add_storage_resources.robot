*** Settings ***
Documentation    This test is using the fusion/hellfire client. It imports a storage
...              system and creates a volume. IT DOES USE SVMC.
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Resource            ${CURDIR}\\..\\..\\..\\..\\..\\..\\Resources\\api\\fusion_api_resource.txt
Resource			${CURDIR}\\..\\..\\..\\..\\..\\..\\Resources\\api\\hellfire_api_resource.txt

Variables 		    ${CURDIR}\\..\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		16.71.130.119
${SVMC_IP}          15.116.0.220
${uri}              v1/internal/registrations/group
${uri2}             v1.5/clusters
${api}              400

${DATA_FILE}         Regression_Data.py


*** Test Cases ***
Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}
    
Add Ethernet Network
    [Tags]    SETUP		Ethernet Network
    [Documentation]		Add Ethernet network to hellfire Oneview VM	
	Add Ethernet Networks from variable	${ethernet_networks}
	Wait Until Keyword Succeeds  120s  10s  Check Resource Attribute  ETH:networke  status   OK

Add the Storage Systems using SVMC
    [Tags]    SETUP    Storage system using SVMC
    [Documentation]		Add SV storage system to hellfire Oneview VM using SVMC	
    ${mgmtgrpid} =  Get Cluster Information   ${uri2}   ${SVMC_IP}  ${svmc_auth}  ${STOREVIRTUAL1_NAME}   
	${resplist} =  Add Storage System Using SVMC  ${storageSystem}  ${APPLIANCE_IP}  ${mgmtgrpid}   ${SVMC_IP}
	Wait for task2  ${resplist}  timeout=300  interval=10 
    ${resp} =	Edit Storage System   ${storage_System_put}    
	Wait for task2  ${resp}  timeout=300  interval=10
	
Create the Storage Volumes using SVMC
    [Tags]    SETUP		Storage Volumes using SVMC
    [Documentation]		Create SV volumes on hellfire Oneview VM using SVMC	     
	${resplist} =  Add Storage Volumes Using SVMC Async  ${storage_volumes}  ${api}
	Wait for task2  ${resplist}  timeout=300  interval=10
