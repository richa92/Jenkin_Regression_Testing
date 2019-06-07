*** Settings ***
Documentation    Tests to verify status of Enclosures, Servers
...              Interconnects, Uplink Sets, Fan and Power Supply.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Run Keyword If Any Tests Failed  Get LE Support Dump  ${le_support_dump_prebuildup}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
All Enclosure Status Should Be OK or Warning - C7000
    [Documentation]  Verify status of all Enclosures
    ...  Verify status of all Interconnects
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

Re-Apply SAS LI Coniguration
    [Documentation]  Re- Apply SAS LI Configuration.This test suite makes sure to removes logical JBODS if found
    [Tags]   SAS-LI  T-BIRD
    Reapply SAS Logical Interconnect Configuration By Name and Verify  ${sas_li_name}

All Enclosure Status Should Be OK or Warning - Tbird
    [Documentation]  Verify status of all Enclosures
    ...  Verify status of all Interconnects
    ...  Verify status of all SAS Interconnects
    ...  Verify status of all Servers
    ...  Verify status of all Uplink Set
    ...  Verify status of all Fan
    ...  Verify status of all PS
    [Tags]      ENCS-STATUS   T-BIRD
    Wait Until Keyword Succeeds    10m    30s    All Enclosures Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Interconnects Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All SAS Interconnects Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Servers Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Uplink Set Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Fan Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Power Supply Status Should Be OK or Warning