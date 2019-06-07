*** Settings ***
Documentation
...     This Test Suite uses ADdmin credentials for LI firmware Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   LI-FW-UPDATE
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Logical Interconnect Firmware Update on odd-even Interconnect-2
    [Tags]              LI2-UPDATE-OE  C7000
    [Documentation]     LI Firmware on odd-even Interconnect update and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_2_oe}  ${spp_version_li}

Logical Interconnect Firmware Update on Parallel Interconnect-2
    [Tags]              LI2-UPDATE-PA  C7000
    [Documentation]     LI Firmware update on Parallel Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_2_pa}  ${spp_version_li}

Logical Interconnect Firmware Update on Serial Interconnect-2
    [Tags]              LI2-UPDATE-SE  C7000
    [Documentation]     LI Firmware update on Serial Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_2_se}  ${spp_version_li}

Logical Interconnect Firmware Update on Parallel Interconnect-Carbon
    [Tags]              T-BIRD  CARBON-PA
    [Documentation]     LI Firmware update on Parallel Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${spp_version_li}   ${bp_spp_name}     SAT_TB_data_variable.get_spp_name_version   ${sppname}
    :For  ${update}  in  @{logical_interconnect_carbon_pa}
    \    Set to dictionary   ${update}   sppUri   ${spp_version_li}
    Log   ${logical_interconnect_carbon_pa}   console=True
    LI Firmware Update  ${logical_interconnect_carbon_pa}  ${spp_version_li}
    Sleep   3m

Logical Interconnect Firmware Update on PairProtect Interconnect-Carbon
    [Tags]              T-BIRD  CARBON-PP
    [Documentation]     LI Firmware update on PairProtect Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${spp_version_li}   ${bp_spp_name}     SAT_TB_data_variable.get_spp_name_version   ${sppname}
    :For  ${update}  in  @{logical_interconnect_carbon_pa}
    \    Set to dictionary   ${update}   sppUri   ${spp_version_li}
    Log   ${logical_interconnect_carbon_pa}   console=True
    LI Firmware Update  ${logical_interconnect_carbon_pa}  ${spp_version_li}