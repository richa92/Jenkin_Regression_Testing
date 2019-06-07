*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for  SPP Upload and Add License Tests.
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Add License
    [Tags]      ADDLICENSE
    [Documentation]        Add Licenses to OneView
    Run Keyword If  ${licenses} is not ${null}    Add Licenses from variable    ${licenses}     ${VERIFY}

SPP Upload
    [Tags]    ADDSPP
    [Documentation]        Upload SPP bundle to OneView
    Upload SPP to Fusion    ${APPLIANCE_IP}    ${admin_credentials['userName']}     ${admin_credentials['password']}      ${spp_local_path}
    Verify Resources for List  ${expected_spp}