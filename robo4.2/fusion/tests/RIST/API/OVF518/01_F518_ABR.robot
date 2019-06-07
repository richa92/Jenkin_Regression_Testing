*** Settings ***
Documentation   Negative tests: Attempt to create a profile with a connection on a non-VC
...             network and an unspecified port Id.

Library  	        BuiltIn
Library		        FusionLibrary
Library		        Collections
Library             json
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./../global_variables.robot
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In
...                 AND     Set Suite Variable      ${WFT2_CONTINUE_ON_ERROR}   ${TRUE}

Suite Teardown      Run Keywords    Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}     ${None}
${DATA_FILE}        ${None}

*** Test Cases ***
Add Base Resources
	Add Ethernet Networks from variable	   ${ethernet_networks}
	Add FC Networks from variable    ${fc_networks}
    Add FCoE Networks from variable    ${fcoe_networks}
    Add LIG from list    ${ligs}
    Add Enclosure Group from list    ${egs}
    Add Storage Volumes Async    ${storage_volumes}

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
