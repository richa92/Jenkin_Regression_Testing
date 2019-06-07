*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables_tbird.py

*** Test Cases ***

GET SUPPORT DUMP
    [Tags]    GETSUPPORTDUMP
    [Documentation]     CGET SUPPORT DUMP for OneView Appliance
    ${dumpUri}=  Create Support Dump Batch  ${support_dump}  ${VERIFY}
    Downloading Support Dump  ${dumpUri}  ${VERIFY}
