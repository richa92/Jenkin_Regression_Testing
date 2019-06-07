*** Settings ***
Documentation    ICM Failover Scenarios
Resource                        resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test cases ***
Power-Off IC Efuse A Side
   [Documentation]     IC Efuse Power-Off
   [Tags]  PRE-IC-OFF-A  C7000
   :FOR  ${icm}  IN  @{efuse_interconnect_a_side}
   \  Wait Until Keyword Succeeds    ${timeout}    ${interval}   Poweroff Interconnect Should Be Successful  ${icm['host']}  ${icm['user']}  ${icm['password']}  ${icm['device']}  ${icm['bay_number']}  ${icm['inter_name']}   powered off
   \  Sleep  2m  #For Sychronisation of interconnect

Power-On IC Efuse A Side
   [Documentation]     IC Efuse Power-On
   [Tags]  PRE-IC-ON-A   C7000
   :FOR  ${icm}  IN  @{efuse_interconnect_a_side}
   \  Wait Until Keyword Succeeds    ${timeout}    ${interval}   Poweron Interconnect Should Be Successful  ${icm['host']}  ${icm['user']}  ${icm['password']}  ${icm['device']}  ${icm['bay_number']}  ${icm['inter_name']}   powered on
   \  Sleep  2m  #For Sychronisation of interconnects

Power-Off IC Efuse B Side
   [Documentation]     IC Efuse Power-Off
   [Tags]  PRE-IC-OFF-B   C7000
   :FOR  ${icm}  IN  @{efuse_interconnect_b_side}
   \  Wait Until Keyword Succeeds    ${timeout}    ${interval}   Poweroff Interconnect Should Be Successful  ${icm['host']}  ${icm['user']}  ${icm['password']}  ${icm['device']}  ${icm['bay_number']}  ${icm['inter_name']}   powered off
   \  Sleep  2m  #For Sychronisation of interconnects

Power-On IC Efuse B Side
   [Documentation]     IC Efuse Power-On
   [Tags]  PRE-IC-ON-B   C7000
   :FOR  ${icm}  IN  @{efuse_interconnect_b_side}
   \  Wait Until Keyword Succeeds    ${timeout}    ${interval}   Poweron Interconnect Should Be Successful  ${icm['host']}  ${icm['user']}  ${icm['password']}  ${icm['device']}  ${icm['bay_number']}  ${icm['inter_name']}   powered on
   \  Sleep  2m  #For Sychronisation of interconnects

EfuseOn Synergy
   [Documentation]     Synergy IC Efuse On
   [Tags]  SYNERGY  SYS-PRE-Efuse-On
   :FOR  ${icm}  IN  @{efuse_interconnect}
   \   EfuseSynergy  EFuseOn  ${icm['encl_serial']}  ${icm['interconnect_bay']}  Absent
   \    Sleep  10m  #For Sychronisation of interconnects

EfuseOff Synergy
   [Documentation]     Synergy IC Efuse Off
   [Tags]  SYNERGY  SYS-PRE-Efuse-Off
   :FOR  ${icm}  IN  @{efuse_interconnect}
   \   EfuseSynergy  EFuseOff  ${icm['encl_serial']}  ${icm['interconnect_bay']}  Configured|Monitored
   \    Sleep  10m  #For Sychronisation of interconnects

Power-On ICM
    [Documentation]    Interconnects Power On from OV
    [Tags]  PWR-ON
    Power On Interconnects from list  ${icm_sidea}

Power-Off ICM
    [Documentation]    Interconnects Power Off from OV
    [Tags]  PWR-OFF
    Power Off Interconnects from list  ${icm_sidea}