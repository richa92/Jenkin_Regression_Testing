*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to Refresh and Verify Enclosure.
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
#Variables                       ./data_variables_tbird.py

*** Test Cases ***

Refresh Enclosure
    [Tags]      REFRESH
    [Documentation]        Refresh Enclosure
    ${responses}=  Refresh Enclosures Async   ${encs_monitor}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}  timeout=1000    interval=20

#Verify Enclosure
#    [Tags]      VERIFY
#    [Documentation]  Verify Servers, Interconnects of Monitored Enclosure
#    Verify Resources for List     ${encs_monitor}
#    Verify Resources for List     ${server_monitor}
#    Verify Resources for List     ${interconnects_monitor}
#    Verify Resources for List     ${sasinterconnects_monitor}