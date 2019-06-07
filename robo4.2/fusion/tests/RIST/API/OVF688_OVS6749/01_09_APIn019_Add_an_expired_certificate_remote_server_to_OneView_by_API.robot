*** Settings ***
Documentation        OVF688_OVS6749 Validate the Rest API to fetch and trust any server certificate
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables            ${DATA_FILE}

Test Setup      LDAPServer Pre-Condition suite         ${OpenLDAP_self_signed_server_name}         ${OpenLDAP_Backup_DBConfig_CMD}         ${OpenLDAP_ModifyDB_Expired_Cert_CMD}
Test Teardown   LDAPServer Post-Condition suite        ${OpenLDAP_self_signed_server_name}         ${OpenLDAP_Restore_DBConfig_CMD}


*** Variables ***

${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Add an expired certificate remote server to OneView by API
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${Expired_self_signed}   False
    ${rsp} =  Validate The Remote Certificate Is Expired     ${Expired_self_signed}
    Should Be True   ${rsp}     msg=The remote server certificate should be invalid
    Trust Self_signed Certificate  ${Expired_self_signed_certs_trust_body}
    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${Expired_self_signed}   False
    ${response}=  Add Active Directory  ${Expired_self_signed_certs}
    should be equal as numbers  ${response[0]['status_code']}  400  msg= The remote server should have a invalid certificate
    log  ${response[0]['message']} So add directory server failed  console=yes
