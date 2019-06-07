*** Settings ***
Documentation       OVF1071 C7000 Add Storage Resources - volumes templates and volumes
Suite Setup         OVF1071 C7000 ASR Setup
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF1071 C7000 ASR Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}

OVF1071 C7000 ASR Create the Storage Volume Templates
    ${resplist} =  Add Storage Volume Templates Async  ${storage_volume_templates}

OVF1071 C7000 ASR Create the Storage Volumes
	${resplist} =  Add Storage Volumes Async  ${storage_volumes}
	wait for task2  ${resplist}  timeout=300  interval=10

*** Keywords ***
OVF1071 C7000 ASR Setup
    [Documentation]    OVF1071 C7000 Add Storage Resource Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF1071 C7000 ASR
    Log    ${feature} Suite Setup: Start Check preconditions    console=true
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Check enclsoures state
    Log    ${feature} Suite Setup: Start check enclosures state.    console=true
    :FOR    ${enclosure}  IN  @{enclosures_expected}
	\   ${start_state} =  Get Resource Attribute	 ENC:${enclosure['name']}  state
	\   Log    ${feature} Suite Setup: The enclosure ${enclosure['name']} start state is ${start_state}    console=true
	\   CONTINUE FOR LOOP IF    '${start_state}'=='Configured'
	\   ${resp} =  Refresh enclosure  ${enclosure}
	\   Wait for Task2  ${resp}  600  10
	\   Check Resource Attribute	 ENC:${enlcosure}  state  Configured
	Log    ${feature} Suite Setup: Finish check enclosures state.    console=true

    # Verify the interconnects state
    Log    ${feature} Suite Setup: Start verify the interconnects state    console=true
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Verify Interconnects from list  ${interconnects_expected}  state=Configured
    Log    ${feature} Suite Setup : Finish verify the interconnects state    console=true

    # Check SAN Managers state and status
    Log    ${feature} Suite Setup: Start check SAN Managers state and status.    console=true
    ${san_managers} =  Fusion Api Get San Manager
    :FOR    ${sm}  IN  @{san_managers['members']}
    \   Should match regexp  ${sm['state']}  Managed
    \   Should match regexp  ${sm['status']}  OK
    Log    ${feature} Suite Setup: Finish check SAN Managers state and status.    console=true

    # Check Storage systems state and status
    Log    ${feature} Suite Setup: Start check storage systems state and status.    console=true
    :FOR    ${ss}  IN  @{storage_systems}
    \   Log    Checking the storage system ${ss['name']}    console=true
    \   Check Resource Attribute  SSYS:${ss['name']}  state  Managed
    \   Check Resource Attribute  SSYS:${ss['name']}  status  OK
    Log    ${feature} Suite Setup: Finish check storage systems state and status.    console=true
