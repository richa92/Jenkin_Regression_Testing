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

Logical Interconnect Firmware Update on odd-even Interconnect-1
    [Tags]              LI1-UPDATE-OE  C7000
    [Documentation]     LI Firmware on odd-even Interconnect update and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_1_oe}  ${spp_version_li}

Logical Interconnect Firmware Update on Parallel Interconnect-1
    [Tags]              LI1-UPDATE-PA  C7000
    [Documentation]     LI Firmware update on Parallel Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_1_pa}  ${spp_version_li}

Logical Interconnect Firmware Update on Serial Interconnect-1
    [Tags]              LI1-UPDATE-SE  C7000
    [Documentation]     LI Firmware update on Serial Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_1_se}  ${spp_version_li}

Logical Interconnect Firmware Update on Parallel Interconnect-Natasha
    [Tags]              T-BIRD  NATASHA-PA
    [Documentation]     LI Firmware update on Parallel Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${spp_version_li}   ${bp_spp_name}     SAT_TB_data_variable.get_spp_name_version   ${sppname}
    :For  ${update}  in  @{logical_interconnect_natasha_pa}
    \    Set to dictionary   ${update}   sppname   ${bp_spp_name}
    Log   ${logical_interconnect_natasha_pa}   console=True
    Update SAS Logical Interconnect Firmware  ${logical_interconnect_natasha_pa[0]['name']}  ${bp_spp_name}  ${logical_interconnect_natasha_pa[0]['fwActivationMode']}  timeout=1800
    Sleep   3m

Logical Interconnect Firmware Update on Orchestrated Interconnect-Natasha
    [Tags]              T-BIRD  NATASHA-PP
    [Documentation]     LI Firmware update on Orchestrated Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${spp_version_li}   ${bp_spp_name}     SAT_TB_data_variable.get_spp_name_version   ${sppname}
    :For  ${update}  in  @{logical_interconnect_natasha_pp}
    \    Set to dictionary   ${update}   sppname   ${bp_spp_name}
    Log   ${logical_interconnect_natasha_pp}   console=True
    Update SAS Logical Interconnect Firmware  ${logical_interconnect_natasha_pp[0]['name']}  ${bp_spp_name}  ${logical_interconnect_natasha_pp[0]['fwActivationMode']}  timeout=1800