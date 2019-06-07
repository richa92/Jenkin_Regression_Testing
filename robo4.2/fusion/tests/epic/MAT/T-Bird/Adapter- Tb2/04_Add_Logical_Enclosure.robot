*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***
Add Logical Enclosure
    [Tags]      ADDLE
    [Documentation]        Add Logical Enclosure(s) to OneView
    Add Logical Enclosure from lists    ${logical_enclosure}
    Verify Resources for List           ${expected_logical_enclosure}

Verify Enclosure
    [Tags]      VERIFY1
    [Documentation]        Verify Configured Enclosures
    Verify Resources for List    ${configured_enclosures}

Refresh Enclosure
    [Tags]      REFRESH
    [Documentation]        Refresh Enclosures passed in the data file
    ${responses}=  Refresh Enclosures Async   ${configured_enclosures}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=5000    interval=20

Verify Enclosure After Refresh
    [Tags]      VERIFY2
    [Documentation]        Verify Configured Enclosures after Refresh
    Verify Resources for List    ${configured_enclosures}

