*** Settings ***
Documentation        Can add at most 5 OID boxes with correct values
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
Add 5 OID boxes with correct values
    [Documentation]    It should success to add no more than 5 OID boxes
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[0:5]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to add 5 OID boxes
    Check updated 2FA validation configurations    ${cert_OID}    ${OIDs[0:5]}
    Fusion Api Logout Appliance
