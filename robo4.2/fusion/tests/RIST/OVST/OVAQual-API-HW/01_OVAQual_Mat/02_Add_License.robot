*** Settings ***
Documentation    Tests to do add license
Resource                        ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***

Add Licenses
    [Tags]  SETUP       LICENSES
    [Documentation]     Add Licenses to OneView
    ${licenses} =   Get Variable Value  ${licenses}
    Run Keyword If  ${licenses} is not ${null}      Add Licenses from variable  ${licenses}     ${VERIFY}