*** Settings ***
Documentation
...     This Test Suite used to Reset Active and Passive FLMs irrespective of their role
...     Test Data is defined in Python Data Variable file.
...     TAGS:   SYS-FLM-Reset, T-BIRD.
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Run Keyword If Any Tests Failed  Get LE Support Dump  ${le_support_dump_postexec}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test cases ***
Reset FLM Frame 3 Bay 1
    [Documentation]     Synergy FLM Reset for Frame 3
    [Tags]  SYS-FLM-Reset  T-BIRD
    :FOR  ${flm}  IN  @{reset_flm_frames_bay1}
    \   ${resp_flmpatch} =   Patch Enclosure  ${flm['name']}  replace  /managerBays/${flm['bay']}/bayPowerState  Reset
    \   Run Keyword If  ${resp_flmpatch} is not ${null}     Wait For Task2   ${resp_flmpatch}   timeout=600    interval=10
    \   ${flm_uri}=  Get Enclosure URI  ${flm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      FLM should reach desired state    ${flm_uri}   ${flm['bay']}    Present
    \   Frame Link Topology Should Be Discovered Without Error
    \   Sleep   360s

Reset FLM Frame 3 Bay 2
    [Documentation]     Synergy FLM Reset for Frame 3
    [Tags]  SYS-FLM-Reset  T-BIRD
    :FOR  ${flm}  IN  @{reset_flm_frames_bay2}
    \   ${resp_flmpatch} =   Patch Enclosure  ${flm['name']}  replace  /managerBays/${flm['bay']}/bayPowerState  Reset
    \   Run Keyword If  ${resp_flmpatch} is not ${null}     Wait For Task2   ${resp_flmpatch}   timeout=600    interval=10
    \   ${flm_uri}=  Get Enclosure URI  ${flm['name']}
    \   Wait Until Keyword Succeeds     ${timeout}   ${interval}      FLM should reach desired state    ${flm_uri}    ${flm['bay']}    Present
    \   Frame Link Topology Should Be Discovered Without Error
    \   Sleep   360s

All Enclosure Status Should Be OK or Warning
    [Documentation]  Verify status of all Enclosures
    ...  Verify status of all Interconnects
    ...  Verify status of all SAS Interconnects
    ...  Verify status of all Servers
    ...  Verify status of all Uplink Set
    ...  Verify status of all Fan
    ...  Verify status of all PS
    [Tags]      SYS-FLM-Reset   T-BIRD
    Wait Until Keyword Succeeds    10m    30s    All Enclosures Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Interconnects Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All SAS Interconnects Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Servers Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Uplink Set Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Fan Status Should Be OK or Warning
    Wait Until Keyword Succeeds    10m    30s    All Power Supply Status Should Be OK or Warning