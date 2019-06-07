*** Settings ***
Documentation       F248 US38249 CRM alerts, Activity Alerts, profile Alerts
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
#Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Setup         Run Keywords    Set Log Level	DEBUG
...          AND                Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...          AND                Create Server Profiles

*** Variables ***
${APPLIANCE_IP}		'16.114.211.81'

#${DATA_FILE}         Regression_Data.py
${DATA_FILE}         tbird8_variables.py

*** Test Cases ***
Appliance Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

# Test - Connection failure due to disabled downlink
Disable Downlink Port on Server and check alert
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 1.* port 5 subport a is unlinked*'
    Disable Downlink Port
    Wait Until Keyword Succeeds  10m  20s  Get Alert By Param  param=?filter=description like 'An error has occurred on connection 1.* port 5 subport a is unlinked*'

# Test - Connection failure due to disabled uplink
Disable FC Uplink Port on Server and check alert
     Remove All Alerts  param=?filter=description like 'An error has occurred on connection 2.*'
     Disable Uplink Port
     Wait Until Keyword Succeeds  10m  20s  Get Alert By Param  param=?filter=description like 'An error has occurred on connection 2.*'

#Test  - Enable both uplink and downlink
Enable both uplink and downlink
    Enable both uplink and downlink

#Test - EfuseOn IC check alert
EfuseOn IC check alert
    EfuseOn IC check alert

#EfuseOff IC
EfuseOff IC
    EfuseOff IC

*** Keywords ***
Power Off check alert and Power ON IC
    [Documentation]  Power Off check alert and Power ON IC
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 2.*'
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 1.* port 5 subport a is unlinked*'
    Power Off Interconnects from list    ${potash_on}
    Wait Until Keyword Succeeds    10m    10s    Verify Interconnects from list  ${potash_off}
    Wait Until Keyword Succeeds  7m  5s  Get Alert By Param  param=?filter=description like 'An error has occurred on connection 2.*'
    Power On Interconnects from list    ${potash_off}
    Wait Until Keyword Succeeds    15m    30s    Verify Interconnects from list  ${potash_on}
    Wait Until Keyword Succeeds    30m    30s    Verify Interconnects from list  ${potash_on_configured}
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 2.*'
    Sleep       180s

EfuseOn IC check alert
    [Documentation]  EfuseOn IC check alert
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 2.*'
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 1.* port 5 subport a is unlinked*'
    [Tags]  Efuse  Neg
	${uri} = 	Get IC URI     ${ENC1ICBAY3}
    ${enc} =    Fetch from left     ${ENC1ICBAY3}    ,
    ${bay} =    Fetch from right    ${ENC1ICBAY3}    ${SPACE}
	Log    \t Waiting for ICM in Bay:${bay} to reach state:Configured    console=true
    Wait Until Keyword Succeeds     7m   5s      IC reached state    ${uri}    Configured
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEON Potash IC]
    Get EM IP
    Get EM Token    ${enc}
    Efuse ICM   EFuseOn     ${bay}
	Log    \t Waiting for ICM in Bay:${bay} to reach state:Absent    console=true
    Sleep       180s
    Wait Until Keyword Succeeds  7m  5s  Get Alert By Param  param=?filter=description like 'The interconnect module is absent*'
    Wait Until Keyword Succeeds  7m  5s  Get Alert By Param  param=?filter=description like 'An error has occurred on connection 1*'

EfuseOff IC
    [Documentation]  EfuseOff IC
    [Tags]  Efuse  Neg
	${uri} = 	Get IC URI     ${ENC1ICBAY3}
    ${enc} =    Fetch from left     ${ENC1ICBAY3}    ,
    ${bay} =    Fetch from right    ${ENC1ICBAY3}    ${SPACE}
	Log    \t Waiting for ICM in Bay:${bay} to reach state:Absent    console=true
    Wait Until Keyword Succeeds     10m   5s      IC reached state    ${uri}    Absent
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEOFF Potash IC]
    Get EM IP
    Get EM Token    ${enc}
    Efuse ICM   EFuseOff     ${bay}
	Log    \t Waiting for ICM in Bay:${bay} to reach state:Configured    console=true
    Wait Until Keyword Succeeds    15m    30s    Verify Interconnects from list  ${potash_on}
    Wait Until Keyword Succeeds    30m    30s    Verify Interconnects from list  ${potash_on_configured}

Get Potash Port URI
    [Documentation]  Get Potash Port URI
    ${uri} = 	Get IC URI     ${ENC1ICBAY3}
    Log    ${uri}    console=true
    Create IC Port URI     ${ENC1ICBAY3}   ${DownLinkPort}

Disable Uplink Port
    [Documentation]  Disable Uplink Port
    ${uri} = 	Get IC URI     ${ENC1ICBAY3}
    Update IC Port     ${ENC1ICBAY3}   ${UpLinkPort}   ${disable_uplink}

Disable Downlink Port
    [Documentation]  Disable Downlink Port
    ${uri} = 	Get IC URI     ${ENC1ICBAY3}
    Update IC Port     ${ENC1ICBAY3}   ${DownLinkPort}   ${disable_downlink}

Enable both uplink and downlink
    [Documentation]  Enable both uplink and downlink
    ${uri} = 	Get IC URI     ${ENC1ICBAY3}
    Update IC Port     ${ENC1ICBAY3}   ${UpLinkPort}   ${enable_uplink}
    ${uri} = 	Get IC URI     ${ENC1ICBAY3}
    Update IC Port     ${ENC1ICBAY3}   ${DownLinkPort}   ${enable_downlink}
    Sleep       180s

Create Server Profiles
    [Documentation]  Create Server Profiles
    Power off All Servers  control=PressAndHold
    :FOR	${server_profile}	IN	@{server_profiles}
	\		${resp} = 	Add Server Profile	${server_profile}
    \		log to console		${resp}
	\      Wait For Task2	${resp}    timeout=2400    interval=20

