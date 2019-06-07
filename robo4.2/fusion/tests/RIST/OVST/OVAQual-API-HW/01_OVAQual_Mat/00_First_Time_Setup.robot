*** Settings ***
Documentation    First Time Setup
Resource         ../resource.txt
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***

First Time Setup
    [Tags]    FTS
    [Documentation]    Configure First time setup for OneView Appliance
    First Time Setup    ${DATA}    ${admin_credentials['password']}
    Wait For Appliance To Become Pingable    ${APPLIANCE_IP}