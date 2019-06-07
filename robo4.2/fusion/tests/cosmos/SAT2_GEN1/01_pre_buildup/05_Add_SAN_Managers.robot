*** Settings ***
Documentation
...     This Test Suite uses AD Storage group user credentials to add SAN Manager.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_storage_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add San Manager Async
    [Tags]    ADDSANMANAGER  T-BIRD  C7000
    ${responses}=  Add San Managers Async  ${san_managers}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=120    interval=5
    Verify Resources for List  ${expected_san_managers}

