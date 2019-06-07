*** Settings ***
Documentation   Reset Plexxi Switches.
...             This will basically disassociate the Plexxi switches from Composable Fabric Manager.
...             The reset process will clear the settings and fabric ownership of the switches so it can join the fabric. Ultimately clears the Ring UUID.

Resource        ../resource.txt
Resource        ../plexxi.txt

Variables       ../${DATA_FILE}

Suite Setup     Set Log Level   ${SUITE_LOG_LEVEL}

*** Test Cases ***
Perform Clear Fabric On Plexxi Switches
    [Tags]    20    PLEXXI_CLEAR_FABRIC
    ${plexxi_switches_credentials} =   Get Variable Value   ${PLEXXI_SWITCHES_CREDENTIALS}   &{EMPTY}
    Run Keyword If   ${plexxi_switches_credentials} == &{EMPTY}   Fail   msg=PLEXXI_SWITCHES_CREDENTIALS is not defined. Please check that the variable is defined in your data file and try again.
    ${plexxi_switches} =   Get Dictionary Values   ${plexxi_switches_credentials}
    :FOR   ${swCred}   IN   @{plexxi_switches}
    \    Open Connection   ${swCred['hostname']}
    \    Login   ${swCred['username']}   ${swCred['password']}   delay=1.5s
    # Getting fabricInfo before reset
    \    Log    \nGetting fabricInfo BEFORE reset of ${swCred['hostname']}...    console=${CONSOLE}
    \    ${stdout}   ${stderr}   ${rc} =   Execute Command   /opt/plexxi/bin/fabricInfo   return_stderr=True   return_rc=True
    \    Log    ${stdout}    console=${CONSOLE}
    \    ${status}    ${value}    Run Keyword And Ignore Error    Should Match Regexp    ${stdout}    Ring UUID:\\s\\[\\]
    \    Run Keyword If    '${status}'=='PASS'    Log    ${swCred['hostname']} Already cleared    console=${CONSOLE}
    \    Run Keyword If    '${status}'=='FAIL'    Clear Fabric    ${swCred}
    \    Close All Connections
