*** Settings ***
Documentation
...     This Test Suite is used for Blade Remove/Re-Insert(Synergy) EfuseReset (Synergy,C7K) cases including OS boot volume and storage path validations.
...     Test Data is defined in Python Data Variable file.
...     TAGS:   RESET, RESET-SERVER, C7000, EFUSE-ON, EFUSE-ON-SERVER, EFUSE-OFF-SERVER
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test cases ***
Reset Server
   [Documentation]     IC Reset Server
   [Tags]   RESET   RESET-SERVER   C7000
   :FOR  ${reset}  IN  @{reset_server}
   \  Wait Until Keyword Succeeds    ${timeout}    ${interval}   Reset Server Hardware Should Be Successful  ${reset['host']}  ${reset['user']}  ${reset['password']}  ${reset['device']}  ${reset['bay_number']}  Successfully
   \  sleep   400s
   \  Wait Until Keyword Succeeds    6000s    ${interval}   Wait for Server-Profile to be in OK state   ${reset['server_name']}
   Power On Server Profile And Wait For POST State  ${reset_server}

Ping IP Post Reset-Server, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]   RESET   POST-RESET-SERVER   C7000
   [Documentation]     Ping IP Post Reset, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   :FOR  ${win_bay7_os_server}  IN   @{win_bay7_os_servers}
   \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active    ${win_bay7_os_server}   02

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

Windows Server Should Be Pinging And Volume Should Be Active After EfuseOn And EfuseOff Bay8
    [Documentation]  Pinging post EfuseOn EfuseOff and checking multipath and pinging of the Windows servers
    [Tags]   POST-EFUSE-SERVER   T-BIRD
    Power On Server Profile And Wait For POST State   ${windows_os_servers}
    :FOR  ${win_os_server}  IN   @{windows_os_servers}
    \    Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   04

RHEL Server Should Be Pinging And Volume Multipath Should Be Active After EfuseOn And EfuseOff Bay1
    [Documentation]  Pinging post EfuseOn EfuseOff and checking multipath and pinging of the RHEL servers
    [Tags]   POST-EFUSE-SERVER   T-BIRD
    Power On Server Profile And Wait For POST State  ${rhel_os_servers}
    Wait Until Keyword Succeeds    ${timeout}    ${interval}   RHEL Server Should Be Pinging And Volume Should Be Active   ${rhel_os_servers}   84

Hotplug Synergy Blade Natasha Bay 1
    [Documentation]     Synergy ICM Efuse Reset for Natasha Bay 1
    [Tags]   NATASHA-HOTPLUG-BAY1  T-BIRD
    :FOR  ${bhp}  IN  @{blade_hotplug_natasha_bay1}
    \    Efuse Synergy Device  EFuseOn  ${bhp['encl_serial']}  ${bhp['device_type']}   ${bhp['device_bay']}
    \    Sleep  120s
    \    Efuse Synergy Device  EFuseOff  ${bhp['encl_serial']}  ${bhp['device_type']}   ${bhp['device_bay']}
    \    Sleep  240s
    \   Wait Until Keyword Succeeds    ${timeout}    ${interval}   Wait for Server-Profile to be in OK state   ${bhp['serverHardwareUri']}
    Sleep  300s
    Power On Server Profile And Wait For POST State  ${sp_natasha_bay1}
    Run Keyword And Continue On Failure   RHEL Server Should Be Pinging And Volume Should Be Active   ${sp_natasha_bay1}   0
