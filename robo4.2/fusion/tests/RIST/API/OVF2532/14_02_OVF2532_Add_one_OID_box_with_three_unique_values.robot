*** Settings ***
Documentation        Can add one OID box with three unique values
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
Add one OID box with three unique values
    [Documentation]    Add a new OID value to the default OID box, it should success
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[3:4]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to add one box with 3 OIDs
    Check updated 2FA validation configurations    ${cert_OID}    ${OIDs[3:4]}
    Fusion Api Logout Appliance