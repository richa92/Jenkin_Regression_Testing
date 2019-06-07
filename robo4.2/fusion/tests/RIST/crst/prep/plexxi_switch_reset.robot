*** Settings ***
Documentation   Reset Plexxi Switches.
...             This will basically disassociate the Plexxi switches from Composable Fabric Manager.
...             The reset process will clear the settings and fabric ownership of the switches so it can join the fabric. Ultimately clears the Ring UUID.
...
...             Example:
...             pybot -d /tmp/logs/crst/prep/plexxi_switch_reset -L TRACE -V /root/ci-fit/config_files/medium_rack_ov420.py plexxi_switch_reset.robot

Library   Collections
Library   SSHLibrary
Library   FusionLibrary

*** Variables ***

*** Test Cases ***
Perform Reset On Plexxi Switches
    ${PLEXXI_SWITCHES_CREDENTIALS} =   Get Variable Value   ${PLEXXI_SWITCHES_CREDENTIALS}   &{EMPTY}
    Run Keyword If   ${PLEXXI_SWITCHES_CREDENTIALS} == &{EMPTY}   Fail   msg=PLEXXI_SWITCHES_CREDENTIALS is not defined. Please check that the variable is defined in your data file and try again.
    ${plexxi_switches} =   Get Dictionary Values   ${PLEXXI_SWITCHES_CREDENTIALS}
    :FOR   ${swCred}   IN   @{plexxi_switches}
    \   Open Connection   ${swCred['ip']}
    \   Login   ${swCred['username']}   ${swCred['password']}   delay=1.5s
    # Getting fabricInfo before reset
    \   Log To Console   \nGetting fabricInfo BEFORE reset of ${swCred['ip']}...
    \   ${stdout}   ${stderr}   ${rc} =   Execute Command   /opt/plexxi/bin/fabricInfo   return_stderr=True   return_rc=True
    \   Log To Console   ${stdout}
    \   Close All Connections

    # Resetting switch using the last switch used for fabricInfo above
    Open Connection   ${swCred['ip']}
    Login   ${swCred['username']}   ${swCred['password']}   delay=1.5s
    Log To Console   \nResetting ${swCred['ip']}...   no_newline=${True}
    Write Bare   sudo su -\r\n
    ${o} =   Read   delay=1.5s
    Should Contain   ${o}   sudo su -
    Should Contain   ${o}   [sudo] password for admin:
    Write   ${swCred['password']}
    Sleep   1.5s
    ${o} =   Read Until Regexp   root@.*:~\#
    Write   px-shell\r\n
    ${o} =   Read Until Regexp   .*\>
    Write   enable
    ${o} =   Read Until Regexp   .*\#
    Write   fabric clear-fabric-id
    ${o} =   Read   delay=2s
    Should Contain   ${o}   Are you sure you want to clear the fabric UUID\? \(y\/n\):
    Write   y
    ${o} =   Read Until Regexp   .*\#
    Write   exit
    ${o} =   Read Until Regexp   root@.*:~\#
    # Generating token
    Write   generateToken -r
    ${o} =   Read Until Regexp   root@.*:~\#
    Log To Console   [DONE]
    Close All Connections

    :FOR   ${swCred}   IN   @{plexxi_switches}
    \   Open Connection   ${swCred['ip']}
    \   Login   ${swCred['username']}   ${swCred['password']}   delay=1.5s
    # Getting fabricInfo after reset
    \   Log To Console   \nGetting fabricInfo AFTER reset of ${swCred['ip']}...
    \   ${stdout}   ${stderr}   ${rc} =   Execute Command   /opt/plexxi/bin/fabricInfo   return_stderr=True   return_rc=True
    \   Log To Console   ${stdout}
    \   Close All Connections

*** Keywords ***

