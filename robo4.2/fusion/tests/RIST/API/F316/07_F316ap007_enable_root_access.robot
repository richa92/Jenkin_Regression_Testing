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

07_F316ap007_enable_root_access

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      Enable RootAccess of Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${body}=                        Create List                ${password_body}
    ${response}=                    fusion api patch interconnect       uri=${ICMBayUri}   body=${body}
    Should Be Equal                 '${response["status_code"]}'    '202'    msg=REST API wrong, can't enable rootaccess of interconnect!
    ${task}=                        wait for Task   ${response}     240s    5s
    Should Be Equal As Strings      ${task["taskState"]}     Completed    msg=task not finish well!
    Fusion Api Logout Appliance



