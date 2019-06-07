*** Settings ***
Documentation        OV should send revoked alert for intermediate CA cert
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
${rootca_uri}     /rest/certificates/ca/rootca
${intermediateca_uri}    /rest/certificates/ca/intermediateca


*** Test Cases ***
Check revoked alert for intermediate CA cert
    [Documentation]    Should show revoked alert for intermediate CA cert when remove its parent CA certs
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Get CA Certificate    ${rootca_uri}
    Should Not Be Empty    ${resp['certificateDetails']}    msg=Fail to retrieve root CA cert
    ${resp} =  Fusion Api Get CA Certificate    ${intermediateca_uri}
    Should Not Be Empty    ${resp['certificateDetails']}    msg=Fail to retrieve intermediate CA cert
    ${upload_crl} =  Fusion Api Upload Crl By Aliasname    rootca    ${CURDIR}/appliance_cert.crl
    Wait For Task2    ${upload_crl}    3min     5    msg=Fail to upload CRL file to root CA cert
    Check Alert    ${alert_messages['Revoked_for_intermediate_CA']}    ${alert_messages['Revoked_Resolution']}

    Log    \n-Removing Revoked root CA certificate to OV    console=yes
    ${resp} =  Fusion Api Remove External CA Certificates    rootca
    Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove root CA cert
    Wait For Task2    ${resp}    2min    5

    Log    \n-Add root CA certificate to OV    console=yes
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    base64Data    ${all_related_certs[0]}
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    aliasName    rootca
    Log    ${ca_cert_body}
    ${add_rootca} =  Fusion Api Import External Ca Certificates    ${ca_cert_body}
    Wait For Task2    ${add_rootca}    300    5
    ${retrieve_rootca} =  Run Keyword And Return Status    Fusion Api Get CA Certificate    ${rootca_uri}
    Should Be Equal    '${retrieve_rootca}'    '${True}'    msg=Cannot find the root CA certificate}
    Fusion Api Logout Appliance
