*** Settings ***
Documentation
...     This Test Suite used for Efuse On/Off for Synergy ICMs (Natasha).
...     Test Data is defined in Python Data Variable file.
...     TAGS:   ICM-OFF, ICM-ON, T-BIRD.
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Run Keyword If Any Tests Failed  Get LE Support Dump  ${le_support_dump_postexec}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test cases ***
EfuseOn Synergy ICM Natasha Bay1
    [Documentation]     Synergy ICM Efuse On for Natasha bay 1
    [Tags]  NATASHA  NATASHA-ON-BAY1  T-BIRD
    :FOR  ${icm}  IN  @{efuse_interconnect_natasha_bay1}
    \    ${uri}=  Get Sas Interconnect URI  ${icm['name']}
    \    Log  \n\n Natasha: ${icm['encl_serial']}, interconnect ${icm['device_bay']} URI: ${uri} \n  console=true
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
    \    Log  \n\n Natasha: ${icm['encl_serial']}, interconnect ${icm['device_bay']} URI: ${uri} \n  console=true
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