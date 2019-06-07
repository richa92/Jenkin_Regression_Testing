*** Settings ***
Documentation                   F316 REST API test cases

Library				FusionLibrary
Library			    RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./keywords.txt
Variables  			./Regression_Data.py

*** Variables ***
${APPLIANCE_IP}     unknown

*** Test Cases ***

05_F316ap005_poweron_UID_interconnect

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      PowerOn Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${ICPowerUIDOn}=                Get from Dictionary     ${InterconnectBay}      UIDPowerOn
    Set to Dictionary	            ${powerUID_body}	                value=${ICPowerUIDOn}
    ${body}=                        Create List                     ${powerUID_body}
    log to console and logfile      ${body}
    ${response}=                    fusion api patch interconnect       uri=${ICMBayUri}     body=${body}
    Should Be Equal                 '${response["status_code"]}'    '202'    msg=REST API wrong, can't poweron UID interconnect!
    log to console and logfile      ${response}
    ${task}=                        wait for Task   ${response}     240s    5s
    log to console and logfile      ${task}
    Should Be Equal As Strings      ${task["taskState"]}     Completed    msg=task not finish well!
    Wait For PowerUID State            240s    5s      ${ICMBayUri}        ${ICPowerUIDOn}
    Fusion Api Logout Appliance



