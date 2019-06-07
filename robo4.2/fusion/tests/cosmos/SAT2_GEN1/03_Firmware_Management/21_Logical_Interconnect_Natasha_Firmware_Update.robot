*** Settings ***
Documentation
...     This Test Suite uses ADdmin credentials for LI firmware Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   LI-FW-UPDATE
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
All Interconnect Status Should Be OK or Warning - Tbird
    [Documentation]    Verify status of all Interconnects
    [Tags]      INTERCONNECT-STATUS  T-BIRD
    Wait Until Keyword Succeeds    3m    30s    All Interconnects Status Should Be OK or Warning

Logical Interconnect Firmware Update on Parallel Interconnect-Natasha
    [Tags]              T-BIRD  NATASHA-PA
    [Documentation]     LI Firmware update on Parallel Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    Update SAS Logical Interconnect Firmware  ${logical_interconnect_natasha_pa[0]['name']}  ${logical_interconnect_natasha_pa[0]['sppName']}  ${logical_interconnect_natasha_pa[0]['fwActivationMode']}  timeout=1800
    Sleep   3m

Logical Interconnect Firmware Update on Orchestrated Interconnect-Natasha
    [Tags]              T-BIRD  NATASHA-PP
    [Documentation]     LI Firmware update on Orchestrated Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    Update SAS Logical Interconnect Firmware  ${logical_interconnect_natasha_pp[0]['name']}  ${logical_interconnect_natasha_pp[0]['sppName']}  ${logical_interconnect_natasha_pp[0]['fwActivationMode']}  timeout=1800