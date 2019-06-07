*** Settings ***
Documentation    Tests to Remove and Add Enclosure's to oneview appliance.
Resource                          ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

Add Monitored Enclosure and Verify
    [Tags]    MONITORED-ENCLOSURE
    [Documentation]    Add Monitored Enclosure
    ${resp} =    Run Keyword And Return Status    Remove All Enclosures async  ${VERIFY}  timeout=720
    Log All Warning and Critical Alerts
    Run Keyword If    '${resp}' == 'False'    FAIL    Failed to remove enclosures
    ${responses}=    Run Keyword If    ${monitored_enclosures} is not ${null}    Add Enclosures from variable Async  ${monitored_enclosures}
    Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure   Wait For Task2   ${responses}   timeout=900    interval=5
    Log All Warning and Critical Alerts
    #Wait for Remote support state to be enabled in Enclosure   ${expected_monitored_enclosures}  500s  60s
    Run Keyword If    ${expected_monitored_enclosures} is not ${null}    Verify Enclosures from list    ${expected_monitored_enclosures}    state=Monitored

*** Keywords ***
Wait for Remote support state to be enabled in Enclosure
    [Documentation]    Wait for Remote support state to be enabled in Enclosure
    [Arguments]  ${enclosure}  ${TIMEOUT}  ${POLLING_INTERVAL}
    Wait Until Keyword Succeeds    ${TIMEOUT}    ${POLLING_INTERVAL}    Get Enclosure and verify remote support   ${enclosure}

Get Enclosure and verify remote support
    [Documentation]    Get Enclosure and verify remote support is enabled
    [Arguments]   ${enclosure}
    :FOR  ${enc}  IN  @{enclosure}
    \   ${getenc} =    Fusion Api Get Enclosures  param=?filter="'name'=='${enc['name']}'"
    \   Run Keyword If  '${getenc['members'][0]['supportState']}' == 'Enabled'  Log  Remote Support for ${enc['name']} is ${getenc['members'][0]['supportState']}  console=yes
    \   ...   ELSE  FAIL
