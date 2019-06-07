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

08_F316ap009_get_root_access_password

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      Get RootAccess Password Interconnect
    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    ${ICMBayPW}=                    Get from Dictionary     ${InterconnectBay}      raPW
    ${ICM_password}=                Set Variable        ${ICMBayUri}/${ICMBayPW}
    ${response}=                    Fusion Api Get Interconnect         ${ICM_password}
    Should Be Equal                 '${response["status_code"]}'    '200'    msg=REST API wrong, can't get rootaccess password of interconnect!
    Should Contain                  ${response}                   password   msg=Get Password of interconnect fail, there should be a password!
    Should Not Be Equal             ${response["password"]}       null       msg=Get Password of interconnect fail, Password should not be null!
    Fusion Api Logout Appliance



