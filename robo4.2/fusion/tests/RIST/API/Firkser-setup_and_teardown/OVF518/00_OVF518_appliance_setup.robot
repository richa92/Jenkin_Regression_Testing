*** Settings ***
Documentation  Setup for OVF518 Test Suite

Library  	        BuiltIn
Library		        FusionLibrary
Library		        Collections
Library             json
Resource            ./../../../../../Resources/api/fusion_api_resource.txt
Resource            ./../../global_variables.robot
Variables           ./../../OVF518/${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

Suite Teardown      Run Keywords    Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}     ${None}
${DATA_FILE}        ${None}

*** Test Cases ***
01 Initialize Ethernet Networks
    Add Ethernet Networks from variable  ${ethernet_networks}

02 Initialize FCoE Networks
    Add FCoE Networks from variable  ${fcoe_networks}

03 Initialize Fibre Channel Networks
    Add FC Networks from variable  ${fc_networks}

04 Initialize Logical Interconnect Groups
     ${ligs} =  Get Variable Value  ${ligs}
     Run Keyword If  ${ligs} is not ${null}  Run Keyword for Dict  ${ligs}  Add LIG from variable

05 Initialize Enclosure Group
    ${egs} =  Get Variable Value  ${egs}
    Run Keyword If  ${egs} is not ${null}  Run Keyword for Dict  ${egs}  Add Enclosure Group from variable

06 Initialize Logical Enclosures
    Add Logical Enclosure from list  ${les}

07 Add the Storage Systems
	${resplist} =  Add Storage Systems Async  ${storage_systems}
	Wait for task2  ${resplist}  timeout=300  interval=10

08 Edit StoreServ Storage Systems
	${resplist} =  Edit Storage Systems Async  ${storage_systems}
	Wait for task2  ${resplist}  timeout=300  interval=10

09 Edit the Storage Pools to Managed
	${resplist} =  Edit Storage Pools Async  ${storage_pools}
	Wait for task2  ${resplist}  timeout=300  interval=10

10 Create the Storage Volumes
	${resplist} =  Add Storage Volumes Async  ${storage_volumes}
	Wait for task2  ${resplist}  timeout=300  interval=10

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
