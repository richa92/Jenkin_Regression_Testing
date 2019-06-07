*** Settings ***
Documentation        Can delete all OUD boxes
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
Delete all OID boxes
    [Documentation]    It should success to delete all OID boxes from appliance
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${blank_list}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to delete all OID boxes from OV
    Check updated 2FA validation configurations    ${cert_OID}    ${blank_list}
    Fusion Api Logout Appliance
