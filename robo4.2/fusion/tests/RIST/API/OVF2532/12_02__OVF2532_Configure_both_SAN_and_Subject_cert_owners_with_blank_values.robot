*** Settings ***
Documentation        Cannnot configure both SAN and Subject cert owners with blank values
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


*** Test Cases ***
Configure both SAN and Subject cert owners with blank values
    [Documentation]    Cannot configure both SAN and Subject cert owners with blank vlaues
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${both_cert_owners_blank}
    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot configure both SAN and Subject certificate owners with blank values
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Empty_Subject_cert_owner_error']}'    msg=Show incorrect error message when configure two cert owners with blank values
    Fusion Api Logout Appliance