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

09_F316ap008_disable_root_access

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      Disable RootAccess Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${RAPWDisable}=                 Get from Dictionary        ${InterconnectBay}   disablePW
    Set to Dictionary	            ${password_body}	       value=${RAPWDisable}
    ${body}=                        Create List                     ${password_body}
    ${response}=                    fusion api patch interconnect       uri=${ICMBayUri}   body=${body}
    Should Be Equal                 '${response["status_code"]}'    '202'    msg=REST API wrong, can't disable rootaccess of interconnect!
    ${task}=                        wait for Task   ${response}     240s    5s
    Should Be Equal As Strings      ${task["taskState"]}     Completed    msg=task not finish well!

    log to console and logfile      check ICM status, poweron ICM
    ${response_check}=              Fusion Api Get Interconnect         ${ICMBayUri}

    Run Keyword If  "${response_check['powerState']}"!="On"      Power On ICM    ${ICMBay}

    Fusion Api Logout Appliance
