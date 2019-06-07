*** Settings ***
Documentation       OVF1071 C7000 Delete Storage Resources - volumes templates and volumes
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF1071 C7000 DSR Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}

OVF1071 C7000 DSR Delete Storage Resources
    # Remove the storage volumes
    ${resplist}=  Remove Storage Volumes Async   ${storage_volumes}  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10
    # Remove the storage volumes templates
	${resplist} =  Remove ALL Storage Volume Templates Async
