*** Settings ***
Documentation    Tests to verify status of Enclosures, Servers
...              Interconnects, Uplink Sets, Fan and Power Supply.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
All Enclosure Status Should Be OK or Warning
    [Documentation]  Verify status of all Enclosures post upgrade
    ...  Verify status of all Interconnects
    ...  Verify status of all SAS Interconnects
    ...  Verify status of all Servers
    ...  Verify status of all Uplink Set
    ...  Verify status of all Fan
    ...  Verify status of all PS
    [Tags]      ENCS-STATUS  C7000
    All Enclosures Status Should Be OK or Warning
    All Interconnects Status Should Be OK or Warning
    All Servers Status Should Be OK or Warning
    All Uplink Set Status Should Be OK or Warning
    All Fan Status Should Be OK or Warning
    All Power Supply Status Should Be OK or Warning

Refresh Enclosure
    [Documentation]  Refresh Enclosure
    [Tags]      REFRESH  T-BIRD  C7000
    ${responses}=  Refresh Enclosures Async   ${refresh_enclosures}
    Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=6000    interval=20

All Enclosure Status Should Be OK or Warning - Tbird
    [Documentation]  Verify status of all Enclosures
    ...  Verify status of all Interconnects
    ...  Verify status of all SAS Interconnects
    ...  Verify status of all Servers
    ...  Verify status of all Uplink Set
    ...  Verify status of all Fan
    ...  Verify status of all PS
    [Tags]      ENCS-STATUS  T-BIRD
    Wait Until Keyword Succeeds    10m    30s    All Enclosures Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Interconnects Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All SAS Interconnects Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Servers Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Uplink Set Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Fan Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Power Supply Status Should Be OK or Warning