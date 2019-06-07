*** Settings ***
Documentation        OV should send corrent alerts for CA certs and CA signed leaf certs when enable 'Notify absence or expiry of CRLs'
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
Check CRL not found for intermediate CA cert
    [Documentation]    Should show CRL NOT Found alert for intermediate CA cert when enable 'Notify absence or expiry of CRLs'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Get CA Certificate    ${intermediateca_uri}
    Should Not Be Empty    ${resp['certificateDetails']}    msg=Fail to retrieve intermediate CA cert
    Check Alert    ${alert_messages['CRL_NOT_FOUND_For_intermediate_CA']}    ${alert_messages['CRL_NOT_FOUND_Resolution']}
    ${resp} =  Update Certificate Validation Configuration    ${validation_body2}
    Should Be True    ${resp}    msg=Failed to update certificate validation configuration
    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Check certificate validation configuration as expected    ${check_validation_body2}
    Fusion Api Logout Appliance
