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

03_F316ap002_poweron_interconnect

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      PowerOn Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${ICPowerOn}=                   Get from Dictionary     ${InterconnectBay}      PowerOn
    Set to Dictionary	            ${power_body}	                value=${ICPowerOn}
    ${body}=                        Create List                     ${power_body}
    log to console and logfile  ${body}
    ${response}=                    fusion api patch interconnect       uri=${ICMBayUri}     body=${body}
    Should Be Equal                 '${response["status_code"]}'    '202'    msg=REST API wrong, can't poweron interconnect!

    ${task}=                        wait for Task   ${response}     240s    5s
    Should Be Equal As Strings      ${task["taskState"]}     Completed    msg=task not finish well!
    Wait For Power State            240s    5s      ${ICMBayUri}        ${ICPowerOn}
    Fusion Api Logout Appliance



