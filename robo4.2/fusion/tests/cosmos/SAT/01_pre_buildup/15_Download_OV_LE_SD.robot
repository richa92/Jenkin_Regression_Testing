*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to download oneview and LE support dump
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Download LE Support Dump - PreBuildup
    [Tags]    LESD  C7000  T-BIRD
    [Documentation]        Create and Download LE Support Dump - Prebuildup
    Get LE Support Dump  ${le_support_dump_prebuildup}  ${TEST NAME}

Download Support Dump - PreBuildup
    [Tags]   DOWNLOAD-OVSD  T-BIRD   C7000
    [Documentation]    Get And Download Oneview Support Dump - PreBuildup
    Get Support Dump  ${support_dump}   ${TEST NAME}