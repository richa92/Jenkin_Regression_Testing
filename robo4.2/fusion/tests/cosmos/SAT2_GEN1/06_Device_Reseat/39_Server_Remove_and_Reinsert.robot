*** Settings ***
Documentation
...     This Test Suite is used for Blade Remove/Re-Insert(Synergy) EfuseReset cases including OS boot volume and active volume validations.
...     Test Data is defined in Python Data Variable file.
...     TAGS:   RESET, RESET-SERVER, C7000, EFUSE-ON, EFUSE-ON-SERVER, EFUSE-OFF-SERVER
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test cases ***
Synergy Blade Server EfuseOn for Bays
    [Documentation]     Synergy Blade EfuseOn for Bays
    [Tags]  EFUSE-ON   EFUSE-ON-SERVER   T-BIRD
    :FOR  ${bladeserver}  IN  @{efuse_blade_servers}
    \   Efuse Synergy Device  EFuseOn  ${bladeserver['encl_serial']}  ${bladeserver['device_type']}   ${bladeserver['device_bay']}
    \   Sleep   180s
    \   Wait Until Keyword Succeeds    ${timeout}    ${interval}   Verify Availability of Server Hardware URI   ${bladeserver['name']}

Synergy Blade Server EfuseOff for Bays
    [Documentation]     Synergy Blade EfuseOff for Bays
    [Tags]  EFUSE-OFF   EFUSE-OFF-SERVER   T-BIRD
    :FOR  ${bladeserver}  IN  @{efuse_blade_servers}
    \   Efuse Synergy Device  EFuseOff  ${bladeserver['encl_serial']}  ${bladeserver['device_type']}   ${bladeserver['device_bay']}
    \   Wait Until Keyword Succeeds    ${timeout}    ${interval}   Wait for Server-Profile to be in OK state   ${bladeserver['name']}
    \   Sleep  360s

ESXi Server Should Be Pinging And Volume Should Be Active After EfuseOn And EfuseOff Bay8
    [Documentation]  Pinging post EfuseOn EfuseOff and checking multipath and pinging of the ESXi servers
    [Tags]   POST-EFUSE-SERVER   T-BIRD
    Power On Server Profile And Wait For POST State   ${esxi_os_servers}
    :FOR  ${esxi_os_server}  IN   @{esxi_os_servers}
    \    Run Keyword And Continue On Failure   ESXi Server Should Be Pinging And Volume Should Be Active   ${esxi_os_server}