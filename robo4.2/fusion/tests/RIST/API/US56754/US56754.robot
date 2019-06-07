*** Settings ***
Documentation       iLO reset to default behavior for Synergy
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}
Suite Setup         Login-Add Frame-Setup-Create Profile
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

${NoSetupJustLogin}    False
${SkipVIPC}            False
${SkipFREM}            False
${SkipREEB}            False
${SkipVOOME}           False
${DoPause}             False

*** Test Cases ***
Verify Initial Profile Connections Then Remove Profile
    [Documentation]    Profile should be created and server powered on.
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Pass Execution If    '${SkipVIPC}'=='True'    Instructed to Skip VIPC
    Run Keyword If    ${DoPause}==True    Pause Execution    Ready to Verify Initial Profile?

    ${profile} =    Get Resource    SP:${profile['name']}
    ${connections} =    Get From Dictionary    ${profile}    connections
    ${new_ris_node} =    Copy Dictionary    ${ris_original}
    ${num_connections} =    Get Length    ${connections}

    # Blade must Fully get to "FinishedPost" before Original MAC are removed.
    # Currently just getting to "InPostDiscoveryComplete" as no OS is installed.
#    :FOR    ${index}    In Range    ${num_connections}
#    \    Remove From List    ${new_ris_node['validate']['PhysicalPorts']}    0

    :FOR    ${connection}    in    @{connections}
    \    ${thisMac} =    Get From Dictionary    ${connection}    mac
    \    ${dict} =    Create Dictionary    MacAddress=${thisMac}
    \    Append To List    ${new_ris_node['validate']['PhysicalPorts']}    ${dict}

    Log    nrn_v_PP:${new_ris_node['validate']['PhysicalPorts']}    console=true
    Log    nrn:${new_ris_node}    console=true
    Log    ris_original:${ris_original}    console=true

    Wait Until Keyword Succeeds    5 min    20 sec    Verify RIS Node    ${new_ris_node}    ${True}

    # now remove the profile
    Power off Server    SH:${SERVER_NAME}
    ${resp} =    Remove Server Profile    ${profile}    force=${True}
    Wait For Task2    ${resp}	   timeout=600	interval=20

    Run Keyword If    ${DoPause}==True    Pause Execution    Really Ready to Delete LE?


Factory Reset EM
    Pass Execution If    '${SkipFREM}'=='True'    Instructed to Skip FREM
    Run Keyword If    ${DoPause}==True    Pause Execution    Ready to FREM?

    GET EM IP    ${FRAME}
    Get EM Token    ${FRAME}

    Run Keyword If    ${DoPause}==True    Pause Execution    Really Ready for Factory Reset?

    # Not sure why it takes so long for OV to genereate the communication alert.
    ${alert} =   catenate    SEPARATOR= or description like
    ...    'Communication failed. The connection to the enclosure has timed out.'
    ...    'Communication failed. An unexpected problem was encountered managing the enclosure.'
    ...    'HPE OneView is unable to communicate with the enclosure''s link modules. An unexpected problem was encountered managing the enclosure.'
    ...    'HPE OneView is unable to communicate with the enclosure''s link modules. The connection to the enclosure has timed out.'

    Delete All Alerts by Param  param=?filter=description like ${alert}

    Factory Reset Active FLM

    Wait Until Keyword Succeeds     60 min    60 sec    Get Alert By Param     param=?filter=description like ${alert}
    Wait Until Keyword Succeeds     2 min    15 sec    Get FLM Factory Password    ${EM_IP}

Remove LE
    ${uri} =  Get Logical Enclosure URI    ${LE_NAME}
    ${resp} = 	fusion api delete logical enclosure  uri=${uri}  param=?force=True
    Wait For Task2    ${resp}	   timeout=900	interval=20

Remove Enclosure Efuse Blade
    Pass Execution If    '${SkipREEB}'=='True'    Instructed to Skip REEB
    Run Keyword If    ${DoPause}==True    Pause Execution    REEB?

    Remove Enclosure    ${FRAME}

    # Now that the Frame is no longer in OneView, need to use Factory Default method of getting IP and Session
    ${password} =    Get FLM Factory Password    ${FLM_IPv6[0]}
    ${session} =    Get Session From Factory Password    ${FLM_IPv6[0]}    ${password}
    ${active} =   Is This FLM Active  ${FLM_IPv6[0]}    ${session}

    # the Session value we have is from FLM1.  If FLM2 is Active then we need a new Session so just re-get
    ${active} =    Set Variable If    '${active}'=='No'    ${FLM_IPv6[1]}    ${FLM_IPv6[0]}
    ${session} =    Get Session From Factory Password    ${active}    ${password}

    # Redefine Suite Variables EM calls
    Set Suite Variable    ${EM_IP}    ${active}
    Set Suite Variable    ${EM_TOKEN}    ${session}

    Efuse Server Blade    ${SERVER_NAME}    EFuseOn
    Sleep    15s    # Don't like sleep but not sure what to spin on.    Yet.
    Efuse Server Blade    ${SERVER_NAME}    EFuseOff

    Wait Until Keyword Succeeds    10 min    20 sec    Verify RIS Node    ${PostStateDiscoveryComplete}    ${True}       ${iLO_IP}

Verify Only Original MAC Exists

    Pass Execution If    '${SkipVOOME}'=='True'    Instructed to Skip VOOME
    Run Keyword If    ${DoPause}==True    Pause Execution    Ready to VOOME

    Power off Server    SH:${SERVER_NAME}
    Power on Server    SH:${SERVER_NAME}
    Wait Until Keyword Succeeds    10 min    20 sec    Verify RIS Node    ${PostStateDiscoveryComplete}    ${True}       ${iLO_IP}
    
    Log    original ris node:${ris_original['validate']['PhysicalPorts']}    console=true
    Wait Until Keyword Succeeds    5 min    10 sec    Verify RIS Node    ${ris_original}    ${True}   ${iLO_IP}

*** Keywords ***
Login-Add Frame-Setup-Create Profile
    [Documentation]    Login-Add Frame-Setup-Create Profile
    Set Log Level	DEBUG
    Set Suite Variable    ${FUSION_IP}    ${APPLIANCE_IP}
    Log    FUSION_IP: ${FUSION_IP}    console=true
    Log Variables    level=INFO

    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    Return from Keyword If    '${NoSetupJustLogin}'=='True'

    # Post Factory Reset Determine Active FLM.  Must know the FLM physical addresses already ${FLM_IPv6}
    # A simple REST GET of the enclosure can be used post add to OV to get active FLM
    ${password} =    Get FLM Factory Password    ${FLM_IPv6[0]}
    ${session} =    Get Session From Factory Password    ${FLM_IPv6[0]}    ${password}
    ${isactive} =    Is This FLM Active    ${FLM_IPv6[0]}    ${session}
    ${active} =    Set Variable if    '${isactive}'=='No'    ${FLM_IPv6[1]}    ${FLM_IPv6[0]}

    # Add Resources
    Add Ethernet Networks from variable	${ethernet_networks}
   	Add LIG from list  ${lig}
    Add Enclosure Group from list  ${eg}
    ${encs} = 	Get Enclosure    ${FRAME}

    ${resp} =    Add Remote Enclosure    ${active}
    Wait For Task2    ${resp}	   timeout=900	interval=20

    Add Logical Enclosure from list    ${le}

    Power off Server    SH:${SERVER_NAME}
    ${resp} = 	Add Server Profile    ${profile}
    Wait For Task2    ${resp}	   timeout=600	interval=5
    Power on Server    SH:${SERVER_NAME}
    Wait Until Keyword Succeeds    10 min    20 sec    Verify RIS Node    ${PostStateDiscoveryComplete}    ${True}

Efuse Server Blade
    [Documentation]    Efuse Server Blade
    [Tags]  Efuse  Neg
  	[Arguments]	       ${ENCBAY}    ${action}

    ${enc} =    Fetch from left     ${ENCBAY}    ,
    ${bay} =    Fetch from right    ${ENCBAY}    ${SPACE}

    Log    enc:${enc}    console=true
    Log    bay:${bay}    console=true
    Log    action:${action}    console=true

    Efuse Blade   ${action}     ${bay}

Get Active FLM
    [Documentation]    Get Active FLM
    [Arguments]  ${frame}
	${enc} =    Get Enclosure    ${frame}
    :FOR     ${flm}     IN    @{enc['managerBays']}
    \    ${role} =    Get From Dictionary    ${flm}    role
    \    ${ipv6} =    Get From Dictionary    ${flm}    ipAddress
    \    ${bay} =    Get From Dictionary    ${flm}    bayNumber
    \    Return From Keyword If    '${role}'=='Active'    ${ipv6}

Clean up
    [Documentation]    Clean up
    ${resp} =    Delete Resource    EG:${EG_NAME}
    Wait For Task2    ${resp}	   timeout=30	interval=20
    ${resp} =    Delete Resource    LIG:${LIG_NAME}
    Wait For Task2    ${resp}	   timeout=60	interval=20
    Fusion Api Logout Appliance