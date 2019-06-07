*** Settings ***
Documentation        Cannot add a blank OID box
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
Add a blank OID box
    [Documentation]    It should fail to add a blank OID box
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[8:9]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '400'    msg= Cannot add blank OID box to OV
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Blank_OID_BOX']}'    msg= Show incorrect error message when fail to add a blank OID box
    Fusion Api Logout Appliance
