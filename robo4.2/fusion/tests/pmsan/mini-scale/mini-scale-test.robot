*** Settings ***
Documentation   This script creates 14 assigned profiles with 50 StoreServ volumes on each blade of the first enclosure
...             = USAGE =
...             | pybot | -v  APPLIANCE_IP:<IP> | -v DATA_FILE:demo-1000.txt | .\mini-scale-test.robot |
...             = Variables =
...             | APPLIANCE_IP | Required; IP address of the OneView appliance to use |
...             | CONFIG_FILE  | The data file to use for test run.  Contains variable definitions that may vary from system to system. |
Library         FusionLibrary
Resource        ../../../Resources/api/fusion_api_resource.txt
Variables       ${DATA_FILE}
Suite Setup     Setup
Suite Teardown  Logout

*** Variables ***
${FEATURE}                      PM SAN mini-scale test
${WFT2_CONTINUE_ON_ERROR}       ${TRUE}

*** Test Cases ***
CSAT PM SAN Create the profiles
    ${RESPLIST}=  Add Server Profiles from variable	 ${CSAT_PROFILES_TO_POST}
    Wait For Task2  ${RESPLIST}   timeout=1800    interval=10

*** Keywords ***
Setup
    [Documentation]    Setup - power off all servers and remove any existing profiles.  Create 50 shared volumes.
    Set Log Level	TRACE
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${ADMIN_CREDENTIALS}

    Log    ${FEATURE} Suite Setup: Start force remove all profiles    console=true
    Power Off Servers in Profiles  ${CSAT_PROFILES_TO_POST}

    ${resplist} =  Remove All Server Profiles Async  force=${True}
    Wait for Task2  ${RESPLIST}  timeout=900  interval=10

    Log    ${FEATURE} Suite Setup: Finish force remove all profiles    console=true

    ${resplist} =  Add Storage Volumes Async  ${STORAGE_VOLUMES}
    wait for task2  ${RESPLIST}  timeout=300  interval=10

Logout
    [Documentation]   Just Logout
    Fusion Api Logout Appliance