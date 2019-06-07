*** Settings ***
Documentation    Tests to do First time setup, Configure NTP server and add license
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***

First Time Setup
    [Tags]    FTS
    [Documentation]     Configure First time setup for OneView Appliance
    First Time Setup  ${DATA}  ${admin_credentials['password']}
    Wait For Appliance To Become Pingable  ${APPLIANCE_IP}

Configure Network Time Server
    [Tags]   NTP
    [Documentation]    Configure NTP server
    ${resp} =    Configure Appliance Time and Locale    ${timeandlocale}
    Wait for task2  ${resp}  timeout=60  interval=10

Add Licenses
    [Tags]    SETUP     LICENSES
    [Documentation]     Add Licenses to OneView
    ${licenses} =   Get Variable Value  ${licenses}
    Run Keyword If  ${licenses} is not ${null}      Add Licenses from variable  ${licenses}  ${VERIFY}