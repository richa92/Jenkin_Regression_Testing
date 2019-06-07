*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${serveradmin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Add Enclosure
    [Tags]    ADD-ENC
    [Documentation]     Add Enclosures to OneView
    ${responses}=  Run Keyword If   ${enclosures} is not ${null}    Add Non-Existing Enclosures from variable Async  ${enclosures}
    ${reslength}=    get length   ${responses}
    Run Keyword If    '${reslength}' is not '${0}'   Wait For Task2  ${responses}     timeout=1500    interval=10
    Run Keyword If    '${reslength}' is not '${0}'   Sleep  180s
    Run Keyword If  ${expected_enclosures} is not ${null}   Verify Enclosures from list  ${expected_enclosures}  state=Configured