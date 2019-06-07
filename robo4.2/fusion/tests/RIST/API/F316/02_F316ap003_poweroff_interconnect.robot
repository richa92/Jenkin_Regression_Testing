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

02_F316ap003_poweroff_interconnect

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      PowerOff Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${body}=                        Create List                     ${power_body}
    ${response}=                    fusion api patch interconnect       uri=${ICMBayUri}     body=${body}
    Should Be Equal                 '${response["status_code"]}'    '202'    msg=REST API wrong, can't poweroff interconnect!

    ${task}=                        wait for Task   ${response}     240s    5s
    should be equal as strings      ${task["taskState"]}     Completed    msg=task not finish well!
    ${ICPowerOff}=                  Get from Dictionary     ${InterconnectBay}      PowerOff
    Wait For Power State            240s    5s      ${ICMBayUri}        ${ICPowerOff}
    Fusion Api Logout Appliance


