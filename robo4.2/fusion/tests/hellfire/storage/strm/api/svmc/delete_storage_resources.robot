*** Settings ***
Documentation    This test is using the fusion/hellfire client. It deletes the volumes and
...              storage system using SVMC. IT DOES USE SVMC.
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
${DATA_FILE}        Regression_Data.py

*** Test Cases ***
Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}
    
Delete Server Profile
    ${resplist} =  Remove Server Profile   ${profile1_create}
    wait for task2  ${resplist}  timeout=300  interval=10

Delete Storage Resources using SVMC
    #Remove the storage volumes
    ${resplist}=  Remove All Storage Volumes Using SVMC Async   param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=300  interval=10
    #Remove the storage systems
	${resplist} =  Remove ALL Storage Systems Using SVMC Async  
     wait for task2  ${resplist}  timeout=300  interval=10
     
