*** Settings ***
Documentation        Cannot add one OID box with 11 unique values
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
Add one OID box with 11 unique values
    [Documentation]    Change the default OID box with 11 unique values, it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[6:7]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '400'    msg= Shouldn't set OID box with 11 unique values
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['OID_error1']}'    msg= Show incorrect error message when set OID box with 11 unique values
    Fusion Api Logout Appliance
