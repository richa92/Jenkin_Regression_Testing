*** Settings ***
Documentation        OV should send revoked alert for CA signed appliance cert
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
${CA_cert_uri}     /rest/certificates/ca/HP TestHead Certificate Authority


*** Test Cases ***
Check revoked alert for CA signed appliance cert
    [Documentation]    Should show revoked alert for CA signed appliance cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${upload_crl} =  Fusion Api Upload Crl By Aliasname    CSRrootca    ${CURDIR}/rootcrl_cert.crl
    Wait For Task2    ${upload_crl}    3min     5    msg=Fail to upload CRL file to root CA
    Manually trigger the status API    ${APPLIANCE_IP}    ${remote_server_cred}
    ${get_appliance_cert} =  Fusion Api Get Appliance Certificate
    Should Not Be Equal    ${get_appliance_cert['commonName']}    ${get_appliance_cert['issuer']}    msg=The current appliance cert is self-signed
  #  ${resp} =  Fusion Api Get CA Certificate    ${CA_cert_uri}
  #  Should Not Be Empty    ${resp['certificateDetails']}    msg=Fail to retrieve related CA cert
  #  ${resp} =  Fusion Api Upload Crl By Aliasname     HP TestHead Certificate Authority    ${CURDIR}/appliance_cert.crl
  #  Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to upload crl file to related CA
    ${server_alert} =  Server Alert With Aliasname    ${get_appliance_cert['commonName']}    ${server_alerts['part3']}
    Check Alert    ${server_alert[0]}    ${alert_messages['Revoked_Resolution']}
    Fusion Api Logout Appliance
