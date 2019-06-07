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

06_F316ap006_poweroff_UID_interconnect

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      PowerOn Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${ICPowerUIDOff}=               Get from Dictionary     ${InterconnectBay}      UIDPowerOff
    Set to Dictionary	            ${powerUID_body}	            value=${ICPowerUIDOff}
    ${body}=                        Create List                     ${powerUID_body}
    ${response}=                    fusion api patch interconnect       uri=${ICMBayUri}     body=${body}
    Should Be Equal                 '${response["status_code"]}'    '202'    msg=REST API wrong, can't poweroff UID interconnect!

    ${task}=                        wait for Task   ${response}     240s    5s
    Should Be Equal As Strings      ${task["taskState"]}     Completed    msg=task not finish well!
    Wait For PowerUID State         240s    5s      ${ICMBayUri}        ${ICPowerUIDOff}
    Fusion Api Logout Appliance



