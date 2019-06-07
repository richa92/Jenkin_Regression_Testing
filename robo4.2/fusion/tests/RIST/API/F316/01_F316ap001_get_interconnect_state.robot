*** Settings ***
Documentation       F316 REST API test cases

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

01_F316ap001_get_interconnect_state

    Fusion Api Login Appliance      ${APPLIANCE_IP}  ${admin_credentials}
    log to console and logfile      Get Interconnect Status

    ${ICMBay}=                      Get from Dictionary        ${InterconnectBay}   interconnectUri
    ${ICMBayUri}=                   Get IC URI    ${ICMBay}
    log to console and logfile      ICMbay is ${ICMBay}, URI is ${ICMBayUri}
    ${response}=                    Fusion Api Get Interconnect         ${ICMBayUri}

    Should Be Equal                 '${response["status_code"]}'    '200'   msg=REST API wrong, can't get interconnect state!
    ${ICstate}=                     Get from Dictionary     ${InterconnectBay}  state
    Should Be Equal                 ${response["state"]}    ${ICstate}      msg=Interconnect State should be Monitored!
    Should Be Equal                 ${response["enclosureName"]}        ${ENC1}     msg=Enclosure name is wrong!
    ${ICdefaultPower}=              Get from Dictionary     ${InterconnectBay}      defaultPowerState
    Should Be Equal                 ${response["powerState"]}       ${ICdefaultPower}   msg=Interconnect default power state should be On!
    ${ICdefaultUIDPower}=           Get from Dictionary     ${InterconnectBay}    defaultUIDPowerState
    Should Be Equal                 ${response["uidState"]}     ${ICdefaultUIDPower}    msg=Interconnect default UID state should be Off!
    Should Contain                  ${response}     partNumber

    Fusion Api Logout Appliance



