*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to Teardown the appliance.
...     First Test is to unassign Server Profile before removing all the resources that were added in other EPIC MAT Test Suites.
...     TAGS:                      CLEAN UP
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***

Refresh Enclosure
    [Tags]      REFRESH
    [Documentation]        Refresh Enclosures passed in the data file
    ${responses}=  Refresh Enclosures Async   ${monitored_enclosures}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=5000    interval=20

Verify Enclosure
    [Tags]      VERIFY
    [Documentation]        Verify Monitored Enclosures
    Verify Resources for List    ${monitored_enclosures}