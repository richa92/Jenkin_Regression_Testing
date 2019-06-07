*** Settings ***
Documentation
...     This Test Suite uses AD Server Group User credentials for Enclosure Management Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add EG
    [Tags]      SETUP       EG  C7000
    [Documentation]     Add Enclosure Group to OneView
    Run Keyword If  ${enc_groups_postupgrade} is not ${null}     Add Enclosure Group from variable async    ${enc_groups_postupgrade}  ${VERIFY}  ${expected_encgroups_postupgrade}
    :FOR    ${eg}    IN    @{enc_groups_postupgrade}
    \    ${configScript} =    Evaluate     ${eg}.get("configurationScript")
    \    Run Keyword If    '${configScript}'=='None'    Continue For Loop
    \    ${script} =   Get Enclosure Group Configuration Script  ${eg['name']}
    \    Run Keyword If    ${script['_content']}!="${eg['configurationScript']}"    Fail    Configuration Script mismatch for Enclosure Group ${eg['name']}
    :FOR    ${eg}    IN    @{enc_groups}
    \    ${configScript} =    Evaluate     ${eg}.get("configurationScript")
    \    Run Keyword If    '${configScript}'=='None'    Continue For Loop
    \    ${script} =   Get Enclosure Group Configuration Script  ${eg['name']}
    \    Run Keyword If    ${script['_content']}!="${eg['configurationScript']}"    Fail    Configuration Script mismatch for Enclosure Group ${eg['name']}

Update EG Config Script
    [Tags]    EG-SCRIPT    C7000
    [Documentation]    Edit Configuration Script
    :FOR    ${eg}    IN    @{enc_groups_updated}
    \    ${response} =    Edit Enclosure Group Configuration Script    ${eg['name']}    ${eg['configurationScript']}
    \    ${script} =   Get Enclosure Group Configuration Script  ${eg['name']}
    \    Should Be Equal    ${script['_content']}    "${eg['configurationScript']}"

Update LE from Group
    [Tags]    LE-UPDATE    C7000
    [Documentation]    Update Logical Enclosure from Group
    Update Logical Enclosure from Group  ${update_logical_enclosure_from_group}  ${VERIFY}

Add Managed Enclosure and Verify
    [Tags]    SETUP    ENCLOSURE  C7000
    [Documentation]    Add Enclosures to OneView post upgrade
    ${responses}=   Run Keyword If    ${enclosures_postupgrade} is not ${null}   Run Keyword And Continue On Failure   Add Non-Existing Enclosures from variable Async  ${enclosures_postupgrade}
    ${reslength}=    get length   ${responses}
    Run Keyword If    '${reslength}' is not '${0}'   Run Keyword And Continue On Failure   Wait For Task2  ${responses}     timeout=1200    interval=10
    Run Keyword If    '${reslength}' is not '${0}'   Sleep  180s
    Run Keyword If     ${expected_enclosures_postupgrade} is not ${null}    Verify Enclosures from list  ${expected_enclosures_postupgrade}  state=Configured
