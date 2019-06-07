*** Settings ***
Documentation
...     This Test Suite uses AD Server Group User credentials for Enclosure Management Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Run Keyword If Any Tests Failed  Get LE Support Dump  ${le_support_dump_prebuildup}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add EG
    [Tags]      SETUP       EG  C7000  T-BIRD
    [Documentation]     Add Enclosure Group to OneView
    Run Keyword If  ${enc_groups} is not ${null}     Add Enclosure Group from variable async    ${enc_groups}
    Verify Enclosure Group from list    ${expected_encgroups}
    :FOR    ${eg}    IN    @{enc_groups}
    \    ${configScript} =    Evaluate     ${eg}.get("configurationScript")
    \    Run Keyword If    '${configScript}'=='None'    Continue For Loop
    \    ${script} =   Get Enclosure Group Configuration Script  ${eg['name']}
    \    Run Keyword If    ${script['_content']}!="${eg['configurationScript']}"    Fail    Configuration Script mismatch for Enclosure Group ${eg['name']}

Add Managed Enclosure and Verify
    [Tags]    SETUP    ENCLOSURE  C7000
    [Documentation]    Add Enclosures to OneView
    ${responses}=   Run Keyword If    ${enclosures} is not ${null}   Run Keyword And Continue On Failure   Add Non-Existing Enclosures from variable Async  ${enclosures}
    ${reslength}=    get length   ${responses}
    Run Keyword If    '${reslength}' is not '${0}'   Run Keyword And Continue On Failure   Wait For Task2  ${responses}     timeout=1200    interval=10
    Run Keyword If    '${reslength}' is not '${0}'   Sleep  180s
    Run Keyword If     ${expected_enclosures} is not ${null}    Verify Enclosures from list  ${expected_enclosures}  state=Configured

Add Logical Enclosure
    [Tags]      ADDLE   T-BIRD
    Add Logical Enclosure from lists Async    ${logical_enclosure}  ${VERIFY}    expected_logical_enclosure=${expected_logical_enclosure}