*** Settings ***
Resource  ../resource.txt
Documentation    This utility is to be used to clean up a system to bring it back to initial state for the next
...              test run.
Suite Setup         Setup
Suite Teardown      Teardown

*** Test Cases ***
Teardown All Profiles
    [Documentation]  Remove all Profiles and Profile Template configurations in OneView Appliance
    [Tags]    Profiles
    Teardown Profiles

Teardown All Logical Elements and Networking
    [Documentation]  Remove all Logical elements and Network configurations in OneView Appliance
    [Tags]    Networking
    Teardown Logical Elements
    Teardown Networking

Teardown All Storage
    [Documentation]  Remove all storage system configurations in OneView Appliance
    [Tags]    Storage
    Teardown Storage

Teardown System
    [Documentation]  Remove all system level configuratons in OneView Appliance
    [Tags]    System
    Teardown System

*** Keywords ***
Setup
    [Documentation]  Login and check flags
    Run Keyword and Ignore Error        Write To ciDebug Log    TEARDOWN
    Log                 [TEARDOWN]      console=True
    Fusion Api Login Appliance          ${APPLIANCE_IP}         ${admin_credentials}
    Run Keyword If    '${initialConfigSuccess}'!='${TRUE}' or '${performanceSuiteSuccess}'!='${TRUE}' or '${ciFitSuiteSuccess}'!='${TRUE}'
    ...    Fail    "Suite execution failed, Skipping Tear down"
    Run Keyword If    '${skipTeardown}' == '${TRUE}'
    ...    Fail    "'skipTeardown' flag is set. Omitting Teardown suite."

Teardown
    [Documentation]    Get Errors if failure occured during teardown.
    Run Keyword If    '${SUITE_STATUS}' == 'FAIL'    Get Errors
