*** Settings ***
Documentation   First Time Setup and Add license to OneView
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***

First Time Setup
    [Documentation]     Configure First time setup for OneView Appliance
    [Tags]    FTS
    First Time Setup  ${DATA}  ${admin_credentials['password']}
    Wait For Appliance To Become Pingable  ${APPLIANCE_IP}

Add Licenses
    [Documentation]     Add Licenses to OneView
    [Tags]    SETUP     LICENSES
    Run Keyword If  ${licenses} is not ${null}      Add Licenses from variable  ${licenses}  ${VERIFY}