*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${serveradmin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Logical Enclosure Update
    [Tags]  LEUPDATE    BIGBANG
    Power off ALL servers   PressAndHold
    :FOR    ${enc}    IN      @{encl}
    \   Update Logical Enclosure Firmware   ${enc['name']}   ${FirmwareVersion}

#Power on Servers and Verify Network connectivity
#    [Tags]    VERIFYCONNECTIVITY    PASSTRAFFIC
#    Power on Servers in Profiles    ${server_profiles}
#    Sleep   5m
#    ${profiles} =   Fusion Api Get Server Profiles
#    :FOR    ${profile}  IN  @{profiles['members']}
#    \   Log to console and logfile    ${profile}
#    \   Get Ethernet Connections IPs from Server Profiles and Ping  ${profile}
