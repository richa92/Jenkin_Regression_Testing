*** Settings ***
Documentation       This is a sample test suite demonstrating OS network
...                 configuration custom keywords
Library             FusionLibrary
Library             Collections
Variables           test_data.py
Suite Setup         Prepare Test Environment
Suite Teardown      Cleanup Test Environment

*** Variables ***
${SP_URL}           /rest/server-profile/testUrl

*** Keywords ***
Prepare Test Environment
    [Documentation]    Prepares the environment for running tests
    ...                Fails there is an obstacle
    ${r}    ${s}=    Fusion Api Login Appliance    ${OV['host']}    ${OV['cred']}
    Should Be Equal    ${r['status_code']}    ${200}    Login Failure

Cleanup Test Environment
    [Documentation]     Perform test artifact removal
    Fusion Api Logout Appliance

*** Test Cases ***
Verify RHEL Ethernet Configuration
    &{body}=    Create Payload For OS Networks Configuration    ${SP_URL}
    ...                                                         ${HOST['rhel'}}
    ...                                                         ${RHEL_NP_1}
    Should Not be Empty    ${body}
    Dictionary Should Contain Key    ${body}    host
    Dictionary Should Contain Key    ${body}    config
    Dictionary Should Contain Item    ${body['host']}     os
    ...                                ${HOST['rhel']['os']}
