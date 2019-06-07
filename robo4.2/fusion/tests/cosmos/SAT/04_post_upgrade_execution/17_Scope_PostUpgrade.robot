*** Settings ***
Documentation
...     This Test Suite validates creation of Scopes, assigning scopes to AD Users and verification of scopes.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   SP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Create Scope
   [Tags]    Scope  T-BIRD  C7000
   [Documentation]    Create Scopes with Resources
   ${responses}=   Create Scopes   ${scopes_postupgrade}
   Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}
   Verify Resources for List  ${expected_scopes_post}

Add Active Directory Groups with Scope
    [Documentation]     Add Active Directory groups with Scope assigned
    [TAGS]    ADD-AD-GRP  T-BIRD  C7000
    Run Keyword If  ${adgroup_withscope} is not ${null}     Add Active Directory Group And Assign Role  ${adgroup_withscope_post}    ${VERIFY}  ${expected_adgroup_withscope_postupgrade}