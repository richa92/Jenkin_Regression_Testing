*** Settings ***
Documentation
...     Description : Create LJBODs, Create Profiles with existing LJBODs, EFUSE SAS ICs, check alerts, ReApply SASLI config
...     Rally: OVF4571, OVS30593
...     Test dependencies - DUAL SAS IC LI
...     HW requirements :
...         Server Hardware Type(s):
...                 SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA
...                 SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA
...         Interconnects
...                 Potash/Chloride fabric
...                 2 SAS ICs
...         Local Storage: BigBird
...         Uplinks/Connections - N/A
...         SAN Managers: N/A
...         Shared Keywords Created (Resources\api\sas_logical_jbods.txt), modified CreateProfile payload
...                Add Logical JBODs Async, Delete Logical JBODs Async, Patch Logical JBOD


Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
#${APPLIANCE_IP}         ${FUSION_IP}
#${DATA_FILE}        ./Dcs_Data.py
#&{admin_credentials}         userName=${FUSION_ADMIN_LOGIN}         password=${FUSION_ADMIN_PASSWORD}

*** Test Cases ***
Create SAS LJBODs
    [Tags]    OVF4571-ljb
    Add Logical JBODs Async     ${ljbs}
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${ljb1_name}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${ljb2_name}  state  Configured
    Reapply SAS Logical Interconnect Configuration By Name and Verify     ${SASLI}

PowerOff ICM1 check alert on ljbod
    [Tags]    OVF4571-powerOff-ICM1
    Delete All Alerts by Param  param=?filter=description like '*Dual domain connectivity to the logical JBOD is lost.*'
    Power Off Sas Interconnects from list     ${sasic_bay1}
    Wait Until Keyword Succeeds    2m    10s    Verify Sas Interconnect  ${sasic1_dict}  powerState=Off
    Wait Until Keyword Succeeds  2m  5s  Get Alert By Param  param=?filter=description like '*Dual domain connectivity to the logical JBOD is lost.*'

PowerOn ICM1
    [Tags]    OVF4571-powerOn-ICM1
    Power On Sas Interconnects from list     ${sasic_bay1}
    Wait Until Keyword Succeeds    6m    10s    Verify Sas Interconnect  ${sasic1_dict}  powerState=On
    ${resp} = 	Refresh SAS Interconenct By Name    ${ENC1SASICBAY1}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    ${uri} = 	Get Sas Interconnect URI    ${ENC1SASICBAY1}
    Wait Until Keyword Succeeds    6 min    5s    IC reached state    ${uri}    Configured
    ${resp} = 	Refresh SAS Interconenct By Name    ${ENC1SASICBAY4}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    ${uri} = 	Get Sas Interconnect URI    ${ENC1SASICBAY4}
    Wait Until Keyword Succeeds    6 min    5s    IC reached state    ${uri}    Configured
    Reapply SAS Logical Interconnect Configuration By Name and Verify       ${SASLI}

create profiles
    [Tags]    OVF4571-sp
    Create Server Profiles

From Dual to Single domain EfuseOn SAS ICM1 and Check Alert
    [Tags]    OVF4571-EfuseOn-ICM1
    Delete All Alerts by Param  param=?filter=description like 'The interconnect in bay 1 has been removed.'
    Delete All Alerts by Param  param=?filter=description like '*Dual domain connectivity to the logical JBOD is lost.*'
    EfuseOn SAS IC     ${sasic1_dict}
    Wait Until Keyword Succeeds    180s    10s    Get Alert By Param   param=?filter=description like '*Dual domain connectivity to logical JBOD is lost.*'
    Wait Until Keyword Succeeds    180s    10s    Get Alert By Param   param=?filter=description like 'The health of one or more SAS logical JBODs has degraded*'

From Single to NO SAS IC EfuseOn SAS ICM4 and Check Alert
    [Tags]    OVF4571-EfuseOn-ICM4
    Delete All Alerts by Param  param=?filter=description like 'The interconnect in bay 4 has been removed.'
    Delete All Alerts by Param  param=?filter=description like 'The logical JBOD*lost connectivity*'
    Delete All Alerts by Param  param=?filter=description like 'The health of one or more SAS logical JBODs has degraded*'
    EfuseOn SAS IC     ${sasic4_dict}
    Wait Until Keyword Succeeds    180s    10s    Get Alert By Param   param=?filter=description like 'The logical JBOD*lost connectivity*'

Check SAS ICMs and LJBODs Configured
    [Tags]    OVF4571-check
    EfuseOff SAS ICM1 and Check Alert
    EfuseOff SAS ICM4 and Check Alert
    Reapply SAS Logical Interconnect Configuration By Name and Verify       ${SASLI}
    ${uri} = 	Get Sas Interconnect URI    ${ENC1SASICBAY1}
    Wait Until Keyword Succeeds    6 min    5s    IC reached state    ${uri}    Configured
    ${uri} = 	Get Sas Interconnect URI    ${ENC1SASICBAY4}
    Wait Until Keyword Succeeds    6 min    5s    IC reached state    ${uri}    Configured
    Wait Until Keyword Succeeds    4 min    5s    Check Resource Attribute     SASLJBOD:${ljb1_name}  state  Configured
    Wait Until Keyword Succeeds    4 min    5s    Check Resource Attribute     SASLJBOD:${ljb1_name}  status  OK
    Wait Until Keyword Succeeds    4 min    5s    Check Resource Attribute     SASLJBOD:${ljb2_name}  state  Configured
    Wait Until Keyword Succeeds    4 min    5s    Check Resource Attribute     SASLJBOD:${ljb2_name}  status  OK

From Dual to no SAS IC
    [Tags]    OVF4571-EfuseOnAndOff-bothSAS
    Delete All Alerts by Param  param=?filter=description like 'A mismatch between the logical interconnect configuration and the interconnect configuration has been detected*'
    EfuseOn both SAS IC
    Wait Until Keyword Succeeds    180s    10s    Get Alert By Param   param=?filter=description like 'The logical JBOD*lost connectivity*'
    EfuseOff SAS ICM1 and Check Alert
    EfuseOff SAS ICM4 and Check Alert

*** Keywords ***
Delete SAS LJBODs
    [Documentation]  delete LJBODs
    Delete Logical JBODs Async     ${ljbs}

Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${profiles}
    ${resp} =    Remove Server Profiles from variable    ${profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Delete SAS LJBODs
    Reapply SAS Logical Interconnect Configuration By Name and Verify       ${SASLI}

Create Server Profiles
    [Documentation]  Create Server Profiles
    @{resplist} =    Create List
    :FOR	${profile}	IN	@{profiles}
	\    ${resp} =    Add Server Profile    ${profile}
	\    Append To List    ${resplist}    ${resp}
    Wait For Task2	${resplist}    timeout=4800    interval=20

EfuseOn SAS IC
    [Documentation]  EfuseOn SAS IC and Check Alert
    [Tags]  Efuse  Neg
    [Arguments]  ${sasic_bay}
    ${name} =  Get From Dictionary  ${sasic_bay}  name
	${uri} = 	Get Sas Interconnect URI     ${name}
    ${enc} =    Fetch from left     ${name}    ,
    ${bay} =    Fetch from right    ${name}    ${SPACE}
	Log    Waiting for ICM in Bay:${bay} to reach state:Configured
    Wait Until Keyword Succeeds     6 min   5s      IC reached state    ${uri}    Configured
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEON SAS IC]
    Get EM IP    ${enc}
    Get EM Token    ${enc}
    Efuse ICM   EFuseOn     ${bay}

EfuseOff SAS IC and Check Alert
    [Documentation]  EfuseOff SAS IC and Check Alert
    [Tags]  Efuse  Neg
	[Arguments]  ${sasic_bay}
    ${name} =  Get From Dictionary  ${sasic_bay}  name
    ${enc} =    Fetch from left     ${name}    ,
    ${bay} =    Fetch from right    ${name}    ${SPACE}
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEOFF SAS IC]
    Get EM IP    ${enc}
    Get EM Token    ${enc}
    Efuse ICM   EFuseOff     ${bay}
    Wait Until Keyword Succeeds    240s    10s    Get Alert By Param   param=?filter=description like 'An interconnect has been inserted in bay ${bay}.'

Get Interconnect Id
    [Documentation]  Get interconnect id
    [Arguments]        ${ic_name}
    ${dcs_enc1} =  DCS Api Get Enc1  ${APPLIANCE_IP}
    Log  ${dcs_enc1}    console=True
    ${targets} =    Set Variable    ${dcs_enc1['InstanceInfo']['targets']}
    ${entities} =    Set Variable    ${targets[0]['EntityInstance']}
    Log  ${entities}    console=True
    :FOR    ${entity}    IN    @{entities}
    \       ${ic_id} =    Run Keyword If  '${entity['type']}'=='${ic_name}'  Set Variable    ${entity['name']}
    \       Exit for loop If	'${ic_id}' != 'None'
    Log  ${ic_id}    console=True
    [Return]   ${ic_id}

Clean Up
    [Documentation]  cleanup
    Power off Servers in Profiles    ${profiles}
    ${resp} =    Remove Server Profiles from variable    ${profiles}
    Wait For Task2	${resp}	   timeout=4200	interval=5
    Delete SAS LJBODs
    Reapply SAS Logical Interconnect Configuration By Name and Verify       ${SASLI}
    Fusion Api Logout Appliance

EfuseOn both SAS IC
    [Documentation]  EfuseOn both SAS IC
    ${name1} =  Get From Dictionary  ${sasic1_dict}  name
    ${name4} =  Get From Dictionary  ${sasic4_dict}  name
	${uri1} = 	Get Sas Interconnect URI     ${name1}
	${uri4} = 	Get Sas Interconnect URI     ${name4}
    ${enc} =    Fetch from left     ${name1}    ,
    ${bay1} =    Fetch from right    ${name1}    ${SPACE}
    ${bay4} =    Fetch from right    ${name4}    ${SPACE}
    Wait Until Keyword Succeeds     6 min   5s      IC reached state    ${uri1}    Configured
    Wait Until Keyword Succeeds     6 min   5s      IC reached state    ${uri4}    Configured
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEON both SAS IC]
    Get EM IP    ${enc}
    ${EM_TOKEN} =  Get EM Token    ${enc}
    log     EM TOKEN: ${EM_TOKEN}
    Efuse ICM   EFuseOn     ${bay1}
    log     EM TOKEN: ${EM_TOKEN}
    Efuse ICM   EFuseOn     ${bay4}

EfuseOff SAS ICM1 and Check Alert
    [Documentation]  EfuseOff SAS ICM1
    Delete All Alerts by Param  param=?filter=description like 'An interconnect has been inserted in bay 1.'
    EfuseOff SAS IC and Check Alert     ${sasic1_dict}
    ${uri} = 	Get Sas Interconnect URI    ${ENC1SASICBAY1}
    Wait Until Keyword Succeeds    6 min    5s    IC reached state    ${uri}    Configured

EfuseOff SAS ICM4 and Check Alert
    [Documentation]  EfuseOff SAS ICM4
    Delete All Alerts by Param  param=?filter=description like 'An interconnect has been inserted in bay 4.'
    EfuseOff SAS IC and Check Alert     ${sasic4_dict}
    ${uri} = 	Get Sas Interconnect URI    ${ENC1SASICBAY4}
    Wait Until Keyword Succeeds    6 min    5s    IC reached state    ${uri}    Configured
