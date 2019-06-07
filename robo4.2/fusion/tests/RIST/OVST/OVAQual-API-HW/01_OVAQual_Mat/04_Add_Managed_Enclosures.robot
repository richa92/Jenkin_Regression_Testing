*** Settings ***
Documentation    Tests to Add Enclosure's to oneview appliance.
Resource                         ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

Add Managed Enclosure and Verify
    [Tags]    SETUP    ENCLOSURE
    [Documentation]    Add Enclosures to OneView
    ${responses}=  Run Keyword If    ${enclosures} is not ${null}  Add Non-Existing Enclosures from variable Async  ${enclosures}
    ${reslength}=    get length   ${responses}
    Run Keyword If    '${reslength}' is not '${0}'   Run Keyword And Continue On Failure   Wait For Task2  ${responses}     timeout=1200    interval=10
    Run Keyword If    '${reslength}' is not '${0}'   Sleep  180s
    Log All Warning and Critical Alerts
    Run Keyword If    ${expected_enclosures} is not ${null}    Verify Enclosures from list  ${expected_enclosures}  state=Configured

Verify LE
    [Tags]      VERIFY    LE
    [Documentation]      Verify LE created by OneView during enclosure import
    :FOR    ${le}  IN  @{expected_logical_enclosure}
    \   ${verify_le}=   Verify C7000 Logical Enclosure    ${le}
    \   Run Keyword If  '${verify_le}'!='True'  Run Keyword And Continue On Failure    Fail   Verify Logical Enclosure Failed for Enclosure ${le['name']}    WARN
