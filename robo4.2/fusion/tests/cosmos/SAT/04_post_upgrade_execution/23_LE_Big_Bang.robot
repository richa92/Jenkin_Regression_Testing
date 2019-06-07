*** Settings ***
Documentation
...     This Test Suite uses AD server Group User credentials for LE Big Bang Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   LE-BIGBANG
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
BigBang Firmware Update Gen9 Gen10 And Validate
    [Tags]              LE-BIGBANG  LE-BIGBANG-GEN10  C7000  4.0  3.10
    [Documentation]     BigBang firmware update for Gen9, Gen10 servers and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LE BigBang Firmware Update      ${expected_logical_enclosure}   ${spp_version}

BigBang Firmware Update Gen8 And Validate
    [Tags]              LE-BIGBANG  LE-BIGBANG-GEN8  C7000  4.0  3.10
    [Documentation]     BigBang firmware update for Gen8 and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    LE BigBang Firmware Update      ${expected_logical_enclosure_gen8}   ${spp_version_gen8}

BigBang Firmware Update should be completed successfully - Tbird
    [Tags]              LE-BIGBANG-TB  LE-BIGBANG-GEN10  T-BIRD
    [Documentation]     BigBang firmware update for Gen9, Gen10 servers and validate the firmware versions
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${buildup_spp_version}   ${bp_spp_name}     SAT_TB_data_variable.get_spp_name_version   ${sppname}
    Log   ${buildup_spp_version}   console=True
    LE BigBang Firmware Update - Tbird    ${le_firmware_update}   ${buildup_spp_version}
    Sleep   4m

Check And Wait For Server Hardware To Complete Refresh
     [Tags]              SH-REFRESH   C7000  T-BIRD
     [Documentation]     Check And Wait For Server Hardware To Complete Refresh
     Wait For ALL Servers Complete Refresh

Download LE Support Dump - Post Upgrade Execution
    [Tags]    LESD  C7000  T-BIRD
    [Documentation]        Create and Download LE Support Dump - Post Upgrade Execution
    Get LE Support Dump  ${le_support_dump_postexec}  ${TEST NAME}

Download Support Dump - Post Upgrade Execution
    [Tags]   DOWNLOAD-OVSD  T-BIRD   C7000
    [Documentation]    Get And Download Oneview Support Dump - Post Upgrade Execution
    Get Support Dump  ${support_dump}   ${TEST NAME}