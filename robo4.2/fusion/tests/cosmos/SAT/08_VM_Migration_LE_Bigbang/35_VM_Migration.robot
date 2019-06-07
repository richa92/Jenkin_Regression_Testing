*** Settings ***
Documentation    VM migration one host to another
...     TAGS:                   EXECUTION
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown
Library                         OperatingSystem

*** Test Cases ***
VM Migration One Host To Another During LE BigBang Firmware Update
    [Tags]    MIGRATE    C7000
    [Documentation]     VM Migration one host to another during LE BigBang Firmware Update
    Power off ALL servers  PressAndHold
    All Server Power State Should Be  Off
    ${response} =  LE BigBang Firmware Update before VM Migration      ${expected_logical_enclosure}   ${spp_version}
    VM Migration    ${vmotion}
    Check status of LE Firmware Update    ${response}

Download LE Support Dump - Post VM Migration
    [Tags]    LESD  C7000
    [Documentation]        Create and Download LE Support Dump - Post VM Migration
    Get LE Support Dump  ${le_support_dump_postexec}  ${TEST NAME}

Download Support Dump - Post VM Migration
    [Tags]   DOWNLOAD-OVSD   C7000
    [Documentation]    Get And Download Oneview Support Dump - Post VM Migration
    Get Support Dump  ${support_dump}   ${TEST NAME}