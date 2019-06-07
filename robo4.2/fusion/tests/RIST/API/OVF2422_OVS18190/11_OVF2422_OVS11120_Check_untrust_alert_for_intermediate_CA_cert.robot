*** Settings ***
Documentation        OV should send untrusted alert for intermediate CA cert when remove its parent CA certs
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
Resource             ./../../../../Resources/api/activity/tasks.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${intermediateca_uri}    /rest/certificates/ca/intermediateca


*** Test Cases ***
Check untrusted alert for intermediate CA cert
    [Documentation]    Should show untrusted alert for intermediate CA cert when remove its parent CA certs
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Get CA Certificate    ${intermediateca_uri}
    Should Not Be Empty    ${resp['certificateDetails']}    msg=Fail to retrieve intermediate CA cert
    Check Alert    ${alert_messages['Untrusted_for_intermediate_CA']}    ${alert_messages['Untrusted_Resolution']}
    Fusion Api Logout Appliance
