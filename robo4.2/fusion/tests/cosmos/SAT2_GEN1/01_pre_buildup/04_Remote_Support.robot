*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for  Enable Remote Support Test.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown


*** Test Cases ***
Enable Remote support
    [Documentation]    Initiate remote support registration
    [Tags]    REM   T-BIRD  C7000
    Initiate Remote Support Registration
