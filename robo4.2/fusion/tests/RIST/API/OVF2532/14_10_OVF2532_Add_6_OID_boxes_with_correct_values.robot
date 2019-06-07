*** Settings ***
Documentation        Cannot add 6 OID boxes with correct values
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library		         SSHLibrary
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
Add 6 OID boxes with correct values
    [Documentation]    It should fail to add 6 OID boxes
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[0:6]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot add 6 OID boxes
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['OID_error2']}'    msg= Show incorrect error message when fail to add 6 OID boxes to OV
    Fusion Api Logout Appliance
