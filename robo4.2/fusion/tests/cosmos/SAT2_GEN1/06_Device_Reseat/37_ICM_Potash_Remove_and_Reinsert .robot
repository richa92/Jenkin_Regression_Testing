*** Settings ***
Documentation
...     This Test Suite used for Efuse On/Off for Synergy ICMs (Potash) and will check the Pinging and active volume configuration of server after Efuse On/Off.
...     Test Data is defined in Python Data Variable file.
...     TAGS:   ICM-OFF, ICM-ON, T-BIRD.
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Run Keyword If Any Tests Failed  Get LE Support Dump  ${le_support_dump_postexec}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test cases ***
EfuseOn Synergy ICM Potash Bay 3
    [Documentation]     Synergy IC Efuse On for Potash Bay 3
    [Tags]  SYS-PRE-IC-On  POTASH-ON  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_potash_bay3}
    \   Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   120s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Absent

ESXi Server Should Be Pinging And Volume Should Be Active After EfuseOn And EfuseOff Bay8
    [Documentation]  Pinging post EfuseOn EfuseOff and checking multipath and pinging of the ESXi servers
    [Tags]   POST-EFUSE-SERVER   T-BIRD
    Power On Server Profile And Wait For POST State   ${esxi_os_servers}
    :FOR  ${esxi_os_server}  IN   @{esxi_os_servers}
    \    Run Keyword And Continue On Failure   ESXi Server Should Be Pinging And Volume Should Be Active   ${esxi_os_server}

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

ESXi Server Should Be Pinging And Volume Should Be Active After EfuseOn And EfuseOff Bay8
    [Documentation]  Pinging post EfuseOn EfuseOff and checking multipath and pinging of the ESXi servers
    [Tags]   POST-EFUSE-SERVER   T-BIRD
    Power On Server Profile And Wait For POST State   ${esxi_os_servers}
    :FOR  ${esxi_os_server}  IN   @{esxi_os_servers}
    \    Run Keyword And Continue On Failure   ESXi Server Should Be Pinging And Volume Should Be Active   ${esxi_os_server}

EfuseOn Synergy ICM Potash Bay 6
    [Documentation]     Synergy IC Efuse On for Potash Bay 6
    [Tags]  SYS-PRE-IC-On  POTASH-ON  T-BIRD
    :FOR  ${icm}  IN  @{interconnect_potash_bay6}
    \   Efuse Synergy Device  EFuseOn  ${icm['encl_serial']}  ${icm['device_type']}   ${icm['device_bay']}
    \   Sleep   360s
    \   ${ic}=  Get IC URI  ${icm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      IC should reach desired state    ${ic}    Absent

ESXi Server Should Be Pinging And Volume Should Be Active After EfuseOn And EfuseOff Bay8
    [Documentation]  Pinging post EfuseOn EfuseOff and checking multipath and pinging of the ESXi servers
    [Tags]   POST-EFUSE-SERVER   T-BIRD
    Power On Server Profile And Wait For POST State   ${esxi_os_servers}
    :FOR  ${esxi_os_server}  IN   @{esxi_os_servers}
    \    Run Keyword And Continue On Failure   ESXi Server Should Be Pinging And Volume Should Be Active   ${esxi_os_server}

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

ESXi Server Should Be Pinging And Volume Should Be Active After EfuseOn And EfuseOff Bay8
    [Documentation]  Pinging post EfuseOn EfuseOff and checking multipath and pinging of the ESXi servers
    [Tags]   POST-EFUSE-SERVER   T-BIRD
    Power On Server Profile And Wait For POST State   ${esxi_os_servers}
    :FOR  ${esxi_os_server}  IN   @{esxi_os_servers}
    \    Run Keyword And Continue On Failure   ESXi Server Should Be Pinging And Volume Should Be Active   ${esxi_os_server}