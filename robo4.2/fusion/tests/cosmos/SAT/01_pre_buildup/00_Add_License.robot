*** Settings ***
Documentation    Tests to do First time setup, Configure NTP server and add license
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add Licenses
    [Tags]    SETUP     LICENSES  T-BIRD  C7000
    [Documentation]     Add Licenses to OneView
    ${licenses} =   Get Variable Value  ${licenses}
    Run Keyword If  ${licenses} is not ${null}      Add Licenses from variable  ${licenses}  ${VERIFY}