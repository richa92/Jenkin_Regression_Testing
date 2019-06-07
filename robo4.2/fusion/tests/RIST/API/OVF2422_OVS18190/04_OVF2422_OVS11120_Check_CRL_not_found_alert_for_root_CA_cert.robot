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
${rootca_uri}    /rest/certificates/ca/rootca


*** Test Cases ***
Check CRL not found for root CA cert
    [Documentation]    Should show CRL NOT Found alert for root CA cert when enable 'Notify absence or expiry of CRLs'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Get CA Certificate    ${rootca_uri}
    Should Not Be Empty    ${resp['certificateDetails']}    msg=Fail to retrieve root CA cert
    ${resp} =  Update Certificate Validation Configuration    ${validation_body1}
    Should Be True    ${resp}    msg=Failed to update certificate validation configuration
    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Check certificate validation configuration as expected    ${check_validation_body1}
    Check Alert    ${alert_messages['CRL_NOT_FOUND_For_root_CA']}    ${alert_messages['CRL_NOT_FOUND_Resolution']}
    Fusion Api Logout Appliance
