*** Settings ***
Documentation       OVF1072 OVF1073 C7000 Delete Storage Resources - volumes templates and volumes
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF1072 OVF1073 C7000 DSR Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}

OVF1072 OVF1073 C7000 DSR Delete Storage Resources
    # Export the existing storage volumes
    ${resplist}=  Remove Storage Volumes Async   ${existing_storage_volumes}  param=?suppressDeviceUpdates=true
    wait for task2  ${resplist}  timeout=120  interval=10
    # Remove the storage volumes
    ${resplist}=  Remove Storage Volumes Async   ${storage_volumes}  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10
    # Remove storage volume temaplates
	${resplist} =  Remove ALL Storage Volume Templates Async