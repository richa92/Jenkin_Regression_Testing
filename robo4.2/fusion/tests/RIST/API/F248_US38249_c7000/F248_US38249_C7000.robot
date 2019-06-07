*** Settings ***
Documentation       F248 US38249 ICM alerts with Profiles for C7000
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
#Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables 		    ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		${None}

*** Test Cases ***
Appliance Login
    [Documentation]  Appliance Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Create Server Profile Disable down link and check alert
    [Documentation]  Create Server Profile Disable down link and check alert
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 1*'
    Power Off Server  ${ENC1SHBAY1}
    Create Bay1 Server Profile
    Disable Downlink Port
    Wait Until Keyword Succeeds  90s  5s  Get Alert By Param  param=?filter=description like 'An error has occurred on connection 1*'

Create Bay4 Server Profiles
    [Documentation]  Create Bay4 Server Profiles
    Power Off Server  ${ENC1SHBAY4}
    Create Bay4 Server Profiles

Disable Uplink Port and check alert
    [Documentation]  Disable Uplink Port and check alert
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 1*'
    Disable Uplink Port
    Wait Until Keyword Succeeds  90s  5s  Get Alert By Param  param=?filter=description like 'An error has occurred on connection 1*'

Enable both uplink and downlink
   [Documentation]  Enable both uplink and downlink
   Enable both uplink and downlink

*** Keywords ***
Create Bay1 Server Profile
    [Documentation]  Create Bay1 Server Profile
    ${resp} = 	Add Server Profile	${profile_with_DownlinkPort_down}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=300	interval=5

Create Bay4 Server Profiles
    [Documentation]  Create Bay4 Server Profiles
    ${resp} = 	Add Server Profile	${bay4_profile}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=300	interval=5

Power Off check alert and Power ON IC
    [Documentation]  Power Off check alert and Power ON IC
    Remove All Alerts  param=?filter=description like 'Interconnect is powered off. One or more server profile connections is affected.*'
    Power Off Interconnects from list    ${potash_on}
    Wait Until Keyword Succeeds    5m    10s    Verify Interconnects from list  ${potash_off}
    Wait Until Keyword Succeeds  60s  5s  Get Alert By Param  param=?filter=description like 'Interconnect is powered off. One or more server profile connections is affected.*'
    Power On Interconnects from list    ${potash_off}
    Wait Until Keyword Succeeds    10m    10s    Verify Interconnects from list  ${potash_on}

EfuseOn IC check alert
    [Documentation]  EfuseOn IC check alert
    [Tags]  Efuse  Neg
    Remove All Alerts  param=?filter=description like 'The interconnect module is absent*'
    Remove All Alerts  param=?filter=description like 'An error has occurred on connection 3*'
	${uri} = 	Get IC URI     ${ENC1ICBAY3}
    ${enc} =    Fetch from left     ${ENC1ICBAY3}    ,
    ${bay} =    Fetch from right    ${ENC1ICBAY3}    ${SPACE}
	Log to console and logfile  	\t Waiting for ICM in Bay:${bay} to reach state:Configured
    Wait Until Keyword Succeeds     3 min   5s      IC reached state    ${uri}    Configured
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEON Potash IC]
    Get EM IP
    Get EM Token    ${enc}
    Efuse ICM   EFuseOn     ${bay}
	Log to console and logfile  	\t Waiting for ICM in Bay:${bay} to reach state:Absent
    Wait Until Keyword Succeeds  90s  5s  Get Alert By Param  param=?filter=description like 'The interconnect module is absent*'
    Wait Until Keyword Succeeds  90s  5s  Get Alert By Param  param=?filter=description like 'An error has occurred on connection 3*'

EfuseOff IC
    [Documentation]  EfuseOff IC
    [Tags]  Efuse  Neg
	${uri} = 	Get IC URI     ${ENC1ICBAY3}
    ${enc} =    Fetch from left     ${ENC1ICBAY3}    ,
    ${bay} =    Fetch from right    ${ENC1ICBAY3}    ${SPACE}
	Log to console and logfile  	\t Waiting for ICM in Bay:${bay} to reach state:Absent
    Wait Until Keyword Succeeds     3 min   5s      IC reached state    ${uri}    Absent
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEOFF Potash IC]
    Get EM IP
    Get EM Token    ${enc}
    Efuse ICM   EFuseOff     ${bay}
	Log to console and logfile  	\t Waiting for ICM in Bay:${bay} to reach state:Configured

Get Potash Port URI
    [Documentation]  Get Potash Port URI
    ${uri} = 	Get IC URI     ${ENC1ICBAY3}
    Log to console and logfile  	${uri}
    Get IC Port URI     ${ENC1ICBAY3}   ${DownLinkPort}

Disable Uplink Port
    [Documentation]  Disable Uplink Port
    ${uri} = 	Get IC URI     ${ENC1ICBAY1}
    Update IC Port     ${ENC1ICBAY1}   ${UpLinkPort}   ${disable_uplink}

Disable Downlink Port
    [Documentation]  Disable Downlink Port
    ${uri} = 	Get IC URI     ${ENC1ICBAY1}
    Update IC Port     ${ENC1ICBAY1}   ${DownLinkPort}   ${disable_downlink}

Enable both uplink and downlink
    [Documentation]  Enable both uplink and downlink
    ${uri} = 	Get IC URI     ${ENC1ICBAY1}
    Update IC Port     ${ENC1ICBAY1}   ${UpLinkPort}   ${enable_uplink}
    ${uri} = 	Get IC URI     ${ENC1ICBAY1}
    Update IC Port     ${ENC1ICBAY1}   ${DownLinkPort}   ${enable_downlink}
    Sleep       180s
