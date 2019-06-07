*** Settings ***
Documentation       Cannot enable emergency login with invalid values when smart card only login is disabled
Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             OperatingSystem
Library             Process
Library             SSHLibrary
Library             String
Library             Dialogs
Library             BuiltIn
Library             json
Library             Collections
Resource            ./../../../../Resources/api/common/common.txt
Resource            ./keywords.txt
Variables           ${DATA_FILE}


*** Variables ***
${emergencytype_item}    emergencyLocalLoginType

*** Test Cases ***
Enable emergency login with invalid values when smart card only login is disabled
    [Documentation]    when disable smart card only login , user cannot enable emergency login with invalid values
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    :For    ${item}    IN    @{invalid_emergencytype_list}
    \    ${logindomains_globalsettings_body} =  Update authentication body    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${logindomains_globalsettings_body}
    \    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot enable emergency login with invalid values when smart card only login is disabled
    \    Should be equal    '${resp['message']}'    '${errorMessages['Invalid_emergency_values']}'    msg=The error message is not correct
    Fusion Api Logout Appliance