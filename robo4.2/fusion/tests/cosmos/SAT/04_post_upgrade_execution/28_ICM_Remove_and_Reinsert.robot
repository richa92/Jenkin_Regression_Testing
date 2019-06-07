*** Settings ***
Documentation
...     This Test Suite used for Efuse On/Off for Synergy and C7000 ICMs (Carbon, Potash, Etc) and will check the Pinging and multipath configuration of server after Efuse On/Off.
...     Test Data is defined in Python Data Variable file.
...     TAGS:   ICM-OFF, ICM-ON, C7000, T-BIRD.
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Run Keyword If Any Tests Failed  Get LE Support Dump  ${le_support_dump_postexec}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test cases ***
Power - Off IC Efuse
    [Documentation]     IC Efuse Power - Off
    [Tags]  ICM-OFF   C7000
    :FOR  ${icm}  IN  @{efuse_interconnect}
    \  Wait Until Keyword Succeeds    ${timeout}    ${interval}   Poweroff Interconnect Should Be Successful  ${icm['host']}  ${icm['user']}  ${icm['password']}  ${icm['device']}  ${icm['bay_number']}   powered off
    \  Wait for Interconnect to go Critical or Ok   ${icm['inter_name']}  Critical

Ping IP Post Efuse, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]      POST-ICM-OFF   C7000
    [Documentation]     Ping IP Post Efuse, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    :FOR  ${win_os_server}  IN   @{win_os_servers}
    \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   01

Power - ON IC Efuse
    [Documentation]     IC Efuse Power - ON
    [Tags]  ICM-ON   C7000
    :FOR  ${icm}  IN  @{efuse_interconnect}
    \  Wait Until Keyword Succeeds    ${timeout}    ${interval}   Poweron Interconnect Should Be Successful  ${icm['host']}  ${icm['user']}  ${icm['password']}  ${icm['device']}  ${icm['bay_number']}    powered on
    \  ${responses} =    Refresh Enclosures Async    ${enclosures}
    \  Wait For Task2  ${responses}     timeout=1200    interval = 10
    \  Wait for Interconnect to go Critical or Ok   ${icm['inter_name']}  OK

EfuseOn Synergy ICM Potash Bay 3
    [Documentation]     Synergy IC Efuse On for Potash Bay 3
    [Tags]  SYS-PRE-IC-On  POTASH-ON  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_potash_bay3}
    \   Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   120s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Absent

Windows Server Should Be Pinging And Volume Should Be Active After EfuseOn Bay3
    [Documentation]  Pinging post efuse and checking mutipath of the Windows servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    :FOR  ${win_os_server}  IN   @{windows_os_servers}
    \   ${sh}=    Get From Dictionary    ${win_os_server}    serverHardwareUri
    \   ${power_status} =   Get Server Power    ${sh}
    \   Run Keyword If   '${power_status}'== 'Off'     Run Keywords    Power on server   ${sh}   AND   Wait for Server to reach POST state     ${sh}   timeout=${timeout}     AND    Sleep   1200s
    \   Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   02

EfuseOff Synergy ICM Potash Bay 3
    [Documentation]     Synergy IC Efuse Off for Potash Bay 3
    [Tags]  SYS-PRE-IC-Off  POTASH-OFF  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_potash_bay3}
    \   Efuse Synergy Device  EFuseOff  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   15m
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Configured|Monitored
    \   Sleep   600s
    \   ${target_uplinksets}=    Get Uplink Sets
    \   # Featch the required attributes from uplink set
    \   Get Data From Uplink Sets And Validate At Oneview   ${target_uplinksets}   ${target_uplinksets_attributes}

Windows Server Should Be Pinging And Volume Should Be Active After EfuseOff Bay3
    [Documentation]  Pinging post efuse and checking mutipath of the Windows servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    :FOR  ${win_os_server}  IN   @{windows_os_servers}
    \   ${sh}=    Get From Dictionary    ${win_os_server}    serverHardwareUri
    \   ${power_status} =   Get Server Power    ${sh}
    \   Run Keyword If   '${power_status}'== 'Off'     Run Keywords    Power on server   ${sh}   AND   Wait for Server to reach POST state     ${sh}   timeout=${timeout}
    \   Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   04

EfuseOn Synergy ICM Potash Bay 6
    [Documentation]     Synergy IC Efuse On for Potash Bay 6
    [Tags]  SYS-PRE-IC-On  POTASH-ON  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_potash_bay6}
    \   Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   360s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Absent

Windows Server Should Be Pinging And Volume Should Be Active After EfuseOn Bay6
    [Documentation]  Pinging post efuse and checking mutipath of the Windows servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    :FOR  ${win_os_server}  IN   @{windows_os_servers}
    \   ${sh}=    Get From Dictionary    ${win_os_server}    serverHardwareUri
    \   ${power_status} =   Get Server Power    ${sh}
    \   Run Keyword If   '${power_status}'== 'Off'     Run Keywords    Power on server   ${sh}   AND   Wait for Server to reach POST state     ${sh}   timeout=${timeout}
    \   Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   02

EfuseOff Synergy ICM Potash Bay 6
    [Documentation]     Synergy IC Efuse Off for Potash Bay 6
    [Tags]  SYS-PRE-IC-Off  POTASH-OFF  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_potash_bay6}
    \   Efuse Synergy Device  EFuseOff  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   15m
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Configured|Monitored
    \   Sleep   600s
    \   ${target_uplinksets}=    Get Uplink Sets
    \   # Featch the required attributes from uplink set
    \   Get Data From Uplink Sets And Validate At Oneview   ${target_uplinksets}   ${target_uplinksets_attributes}

Windows Server Should Be Pinging And Volume Should Be Active After EfuseOff Bay6
    [Documentation]  Pinging post efuse and checking mutipath of the Windows servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    :FOR  ${win_os_server}  IN   @{windows_os_servers}
    \   ${sh}=    Get From Dictionary    ${win_os_server}    serverHardwareUri
    \   ${power_status} =   Get Server Power    ${sh}
    \   Run Keyword If   '${power_status}'== 'Off'     Run Keywords    Power on server   ${sh}   AND   Wait for Server to reach POST state     ${sh}   timeout=${timeout}
    \   Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   04

EfuseOn Synergy ICM Carbon Bay1
    [Documentation]     Synergy ICM Efuse On for Carbon bay 1
    [Tags]  SYS-PRE-IC-On  CARBON-ON-BAY1  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_carbon_bay1}
    \   Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   120s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Absent

RHEL Server Should Be Pinging And Volume Multipath Should Be Active After EfuseOn Bay1
    [Documentation]  Pinging post efuse and checking mutipath of the RHEL servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    Power On Server Profile And Wait For POST State  ${rhel_os_servers}
    Run Keyword And Continue On Failure   RHEL Server Should Be Pinging And Volume Should Be Active   ${rhel_os_servers}   42

EfuseOff Synergy ICM Carbon Bay1
    [Documentation]     Synergy IC Efuse Off for Carbon bay 1
    [Tags]  SYS-PRE-IC-Off  CARBON-OFF-BAY1  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_carbon_bay1}
    \   Efuse Synergy Device  EFuseOff  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   240s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Configured|Monitored
    \   Sleep   300s
    \   ${target_uplinksets}=    Get FC Uplink Sets
    \   # Featch the required attributes from uplink set
    \   Get Data From Uplink Sets And Validate At Oneview   ${target_uplinksets}   ${target_uplinksets_attributes}

RHEL Server Should Be Pinging And Volume Multipath Should Be Active After EfuseOff Bay1
    [Documentation]  Pinging post efuse and checking mutipath of the RHEL servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    Power On Server Profile And Wait For POST State  ${rhel_os_servers}
    Run Keyword And Continue On Failure   RHEL Server Should Be Pinging And Volume Should Be Active   ${rhel_os_servers}   84

EfuseOn Synergy ICM Carbon Bay4
    [Documentation]     Synergy ICM Efuse On for Carbon bay 4
    [Tags]  SYS-PRE-IC-On  CARBON-ON-BAY4  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_carbon_bay4}
    \   Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   120s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Absent

RHEL Server Should Be Pinging And Volume Multipath Should Be Active After EfuseOn Bay4
    [Documentation]  Pinging post efuse and checking mutipath of the RHEL servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    Power On Server Profile And Wait For POST State  ${rhel_os_servers}
    Run Keyword And Continue On Failure   RHEL Server Should Be Pinging And Volume Should Be Active   ${rhel_os_servers}   42

EfuseOff Synergy ICM Carbon Bay4
    [Documentation]     Synergy IC Efuse Off for Carbon bay4
    [Tags]  SYS-PRE-IC-Off  CARBON-OFF-BAY4  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_carbon_bay4}
    \   Efuse Synergy Device  EFuseOff  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   240s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Configured|Monitored
    \   Sleep   300s
    \   ${target_uplinksets}=    Get FC Uplink Sets
    \   # Featch the required attributes from uplink set
    \   Get Data From Uplink Sets And Validate At Oneview   ${target_uplinksets}   ${target_uplinksets_attributes}

RHEL Server Should Be Pinging And Volume Multipath Should Be Active After EfuseOff Bay4
    [Documentation]  Pinging post efuse and checking mutipath of the RHEL servers
    [Tags]           T-BIRD-CHECK  T-BIRD
    Power On Server Profile And Wait For POST State  ${rhel_os_servers}
    Run Keyword And Continue On Failure   RHEL Server Should Be Pinging And Volume Should Be Active   ${rhel_os_servers}   84

EfuseOn Synergy ICM Natasha Bay1
    [Documentation]     Synergy ICM Efuse On for Natasha bay 1
    [Tags]  NATASHA  NATASHA-ON-BAY1  T-BIRD
    :FOR  ${icm}  IN  @{efuse_interconnect_natasha_bay1}
    \    ${uri}=  Get Sas Interconnect URI  ${icm['name']}
    \    Log  \n\n Natasha: ${icm['name']} URI: ${uri} \n  console=true
    \    Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \    Sleep  30s
    \    ${count}=  Verify Availability of Sas Interconnect URI  ${icm['name']}
    \    Run Keyword If  $count!=0  FAIL  Failed to Remove

EfuseOff Synergy ICM Natasha Bay1
    [Documentation]     Synergy IC Efuse Off for Natasha bay 1
    [Tags]  NATASHA  NATASHA-OFF-BAY1  T-BIRD
    :FOR  ${icm}  IN  @{efuse_interconnect_natasha_bay1}
    \   Efuse Synergy Device  EFuseOff  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   ${ic}=  Wait Until Keyword Succeeds    2m    30s   Get Sas Interconnect URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Configured|Monitored

EfuseOn Synergy ICM Natasha Bay4
    [Documentation]     Synergy ICM Efuse On for Natasha bay 4
    [Tags]  NATASHA  NATASHA-ON-BAY4  T-BIRD
    :FOR  ${icm}  IN  @{efuse_interconnect_natasha_bay4}
    \    ${uri}=  Get Sas Interconnect URI  ${icm['name']}
    \    Log  \n\n Natasha: ${icm['name']} URI: ${uri} \n  console=true
    \    Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \    Sleep  30s
    \    ${count}=  Verify Availability of Sas Interconnect URI  ${icm['name']}
    \    Run Keyword If  $count!=0  FAIL  Failed to Remove

EfuseOff Synergy ICM Natasha Bay4
    [Documentation]     Synergy IC Efuse Off for Natasha bay 4
    [Tags]  NATASHA  NATASHA-OFF-BAY4  T-BIRD
    :FOR  ${icm}  IN  @{efuse_interconnect_natasha_bay4}
    \   Efuse Synergy Device  EFuseOff  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   ${ic}=  Wait Until Keyword Succeeds    2m    30s   Get Sas Interconnect URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Configured|Monitored
