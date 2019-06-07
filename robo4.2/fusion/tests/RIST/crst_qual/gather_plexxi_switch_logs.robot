*** Settings ***
Documentation   Gather Plexxi Switch Logs.
...             This test will log into the switches and generate the switch logs.

Library   Collections
Library   SSHLibrary  timeout=300 seconds
Library   FusionLibrary

Variables       ${DATA_FILE}

*** Test Cases ***
Gather Plexxi Switch Logs
    ${PLEXXI_SWITCHES_CREDENTIALS} =   Get Variable Value   ${PLEXXI_SWITCHES_CREDENTIALS}   &{EMPTY}
    Run Keyword If   ${PLEXXI_SWITCHES_CREDENTIALS} == &{EMPTY}   Fail   msg=PLEXXI_SWITCHES_CREDENTIALS is not defined. Please check that the variable is defined in your data file and try again.
    ${plexxi_switches} =   Get Dictionary Values   ${PLEXXI_SWITCHES_CREDENTIALS}
    :FOR   ${swCred}   IN   @{plexxi_switches}
    \    Open Connection   ${swCred['hostname']}
    \    Login   ${swCred['username']}   ${swCred['password']}   delay=1.5s
    # Getting fabricInfo before reset
    \    Log To Console   \nGenerating Switch logs for ${swCred['hostname']}...
    \    Write   sudo px-shell
    \    ${o} =   Read   delay=1.5s
    \    Should Contain   ${o}   [sudo] password for ${swCred['username']}:
    \    Write   ${swCred['password']}
    \    Sleep   1.5s
    \    ${o} =   Read Until Regexp   .*\>
    \    Write   enable
    \    ${o} =   Read Until Regexp   .*\#
    \    Write  support log-bundle
    \    ${o} =   Read Until Regexp   .*\#
    \    Should Contain   ${o}  \(On disk: \/usr\/share\/px-shell\/log-bundle.tar.gz\)
    \    Log To Console   Successfully saved Plexxi switch logs to /usr/share/px-shell/log-bundle.tar.gz
    \    Close All Connections
