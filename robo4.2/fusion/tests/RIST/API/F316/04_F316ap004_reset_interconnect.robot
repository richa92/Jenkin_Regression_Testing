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

04_F316ap004_reset_interconnect

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      Reset Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${body}=                        Create List                     ${reset_body}
    ${response}=                    fusion api patch interconnect       uri=${ICMBayUri}   body=${body}
    Should Be Equal                 '${response["status_code"]}'    '202'    msg=REST API wrong, can't reset interconnect!

    ${task}=                        wait for Task   ${response}     240s    5s
    should be equal as strings      ${task["taskState"]}     Completed    msg=task not finish well!
    ${ICPowerOn}=                   Get from Dictionary     ${InterconnectBay}      PowerOn
    Wait For Power State            240s    5s      ${ICMBayUri}        ${ICPowerOn}
    Fusion Api Logout Appliance



