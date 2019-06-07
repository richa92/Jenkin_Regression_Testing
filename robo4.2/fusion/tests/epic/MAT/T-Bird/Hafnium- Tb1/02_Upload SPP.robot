*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for  SPP Upload.
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***

SPP Upload
    [Tags]    ADDSPP
    [Documentation]        Upload SPP bundle to OneView
    Upload Firmware Bundle Async    ${spp_local_path}   ${VERIFY}