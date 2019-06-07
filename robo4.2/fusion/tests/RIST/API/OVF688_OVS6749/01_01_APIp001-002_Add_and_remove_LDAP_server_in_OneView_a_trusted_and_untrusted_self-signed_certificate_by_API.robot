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

Test Setup      LDAPServer Pre-Condition suite        ${OpenLDAP_self_signed_server_name}         ${OpenLDAP_Backup_DBConfig_CMD}         ${OpenLDAP_ModifyDB_SelfSigned_Cert_CMD}
Test Teardown   LDAPServer_Post_SelfSignCert_TC_Execution        ${OpenLDAP_self_signed_server_name}         ${OpenLDAP_Restore_DBConfig_CMD}

*** Variables ***

${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Add and remove LDAP server in OneView a trusted and untrusted self-signed certificate by API
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${OpenLDAP_self_signed}   False
    Should Be True   ${rsp}     msg=The certificate has been added in trust store
    Trust Self_signed Certificate  ${OpenLDAP_self_signed_certs_trust_body}
    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${OpenLDAP_self_signed}   True
    Should Be True   ${rsp}    msg=The certificate hasn't been added in trust store
    ${response}=  Add Active Directory  ${OpenLDAP_self_signed_certs}
    Wait For Task2    ${response}    timeout=60    interval=5
