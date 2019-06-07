*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for Add Logical Enclosure, Verify Enclosure and Refresh Enclosure.
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
#Variables                       ./data_variables_tbird.py

*** Variables ***
${Le_Create_Timeout}            30 minutes

*** Test Cases ***

Add Logical Enclosure
    [Tags]      ADDLOGICALENCLOSURE
    [Documentation]  Add Logical Enclosure to OneView
    Add Logical Enclosure from lists    ${logical_enclosure}
    Verify Resources for List           ${expected_logical_enclosure}

#Verify Enclosure
#    [Tags]      VERIFY
#    [Documentation]  Verify Servers, Interconnects of Monitored Enclosure
#    Verify Resources for List     ${encs_configured}
#    Verify Resources for List     ${server_configured}
#    Verify Resources for List     ${interconnects_configured}
#    Verify Resources for List     ${sasinterconnects_configured}
