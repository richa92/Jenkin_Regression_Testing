*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***

Edit Logical Interconnect Group
    [Tags]    EDITLIG
    [Documentation]        Edit LIG
    ${responses} =      Edit LIG    ${update_ligs}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=200    interval=5
    Verify Resources for List  ${expected_ligs_updated}

Update LE From Group
    [Tags]    UPDATELE
    [Documentation]        Invoke update from group on LE
    Update Logical Enclosure from Group from list   ${logical_enclosure}    timeout=2000    interval=10
    Verify Resources for List  ${expected_logical_enclosure}

Get LE Support Dump
    [Tags]    SUPPORTDUMP
    [Documentation]        Create and Download LE Support Dump
    Create And Download Logical Enclosure Support Dump  ${le_support_dump}  ${VERIFY}