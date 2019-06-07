*** Settings ***
Documentation        Can add one OID box with one value
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
Add one OID box with one value
    [Documentation]    Change the default OID box with one value, it should success
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    @{index_list} =  Create List    1    2
    ${index} =  Set Variable    1
    :For    ${index}    IN    @{index_list}
    \    ${index_next} =  Evaluate    ${index}+1
    \    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[${index}:${index_next}]}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg= Fail to to add one box with only one OID
    \    Check updated 2FA validation configurations    ${cert_OID}    ${OIDs[${index}:${index_next}]}
    Fusion Api Logout Appliance
