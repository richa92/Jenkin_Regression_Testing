*** Settings ***
Documentation
...     This Test Suite uses ADdmin credentials for LI firmware Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   LI-FW-UPDATE
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Logical Interconnect Firmware Update on odd-even Interconnect-3
    [Tags]              LI3-UPDATE-OE  C7000
    [Documentation]     LI Firmware on odd-even Interconnect update and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_3_oe}  ${spp_version_li}

Logical Interconnect Firmware Update on Parallel Interconnect-3
    [Tags]              LI3-UPDATE-PA  C7000
    [Documentation]     LI Firmware update on Parallel Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_3_pa}  ${spp_version_li}

Logical Interconnect Firmware Update on Serial Interconnect-3
    [Tags]              LI3-UPDATE-SE  C7000
    [Documentation]     LI Firmware update on Serial Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LI Firmware Update  ${logical_interconnect_3_se}  ${spp_version_li}

Logical Interconnect Firmware Update on Parallel Interconnect-Potash
    [Tags]              T-BIRD  POTASH-PA
    [Documentation]     LI Firmware update on Parallel Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${spp_version_li}   ${bp_spp_name}     SAT_TB_data_variable.get_spp_name_version   ${sppname}
    :For  ${update}  in  @{logical_interconnect_potash_pa}
    \    Set to dictionary   ${update}   sppUri   ${spp_version_li}
    Log   ${logical_interconnect_potash_pa}   console=True
    LI Firmware Update  ${logical_interconnect_potash_pa}  ${spp_version_li}
    Sleep   3m

Logical Interconnect Firmware Update on PairProtect Interconnect-Potash
    [Tags]              T-BIRD  POTASH-PP
    [Documentation]     LI Firmware update on PairProtect Interconnect and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${spp_version_li}   ${bp_spp_name}     SAT_TB_data_variable.get_spp_name_version   ${sppname}
    :For  ${update}  in  @{logical_interconnect_potash_pp}
    \    Set to dictionary   ${update}   sppUri   ${spp_version_li}
    Log   ${logical_interconnect_potash_pp}   console=True
    LI Firmware Update  ${logical_interconnect_potash_pp}  ${spp_version_li}

Download LE Support Dump - Post LI Firmware Update
    [Tags]    LESD  T-BIRD
    [Documentation]        Create and Download LE Support Dump - Post LI Firmware Update
    Get LE Support Dump  ${le_support_dump_postexec}  ${TEST NAME}

Download Support Dump - Post LI Firmware Update
    [Tags]   DOWNLOAD-OVSD  C7000
    [Documentation]    Get And Download Oneview Support Dump - Post LI Firmware Update
    Get Support Dump  ${support_dump}   ${TEST NAME}