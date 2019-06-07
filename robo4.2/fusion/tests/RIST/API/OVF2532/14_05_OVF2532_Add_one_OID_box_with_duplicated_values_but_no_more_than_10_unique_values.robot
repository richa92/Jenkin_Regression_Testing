*** Settings ***
Documentation        Can add one OID box with duplicated values but no more than 10 unique ones
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              String
Library              Dialogs
Library              BuiltIn
Library              json
Library              Collections
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${cert_OID}    validationOids


*** Test Cases ***
Add one OID box with duplicated values but no more than 10 unique ones
    [Documentation]    Change the default OID box with duplicated values but no more than 10 unique ones, it should success
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[5:6]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to add one OID box with duplicated values but no more than 10 unique ones
    Check updated 2FA validation configurations    ${cert_OID}    ${OIDs[5:6]}
    Fusion Api Logout Appliance
