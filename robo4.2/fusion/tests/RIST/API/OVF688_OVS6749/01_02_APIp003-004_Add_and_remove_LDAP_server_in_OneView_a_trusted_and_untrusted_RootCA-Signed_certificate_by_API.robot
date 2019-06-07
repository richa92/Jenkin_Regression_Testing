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

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
Test Teardown   LDAPServer_Post_RootCASignCert_TC_Execution        ${OpenLDAP_rootCA_server_name}         ${OpenLDAP_Restore_DBConfig_CMD}

*** Variables ***

${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Add and remove LDAP server in OneView a trusted and untrusted rootCA-signed certificate by API
    ${rsp} =  Fetch Remote LDAP Server And Validate The RootCA Trusted Status As Expected  ${OpenLDAP_RootCASigned_Cert_CMDS}   False
    Should Be True   ${rsp}     msg=The certificate has been added in trust store
    Trust RootCA_signed Or SubCA_signed Certificate  ${LDAP_RootCA_signed_certs_trust_body}
    ${rsp} =  Fetch Remote LDAP Server And Validate The RootCA Trusted Status As Expected  ${OpenLDAP_RootCASigned_Cert_CMDS}   True
    Should Be True   ${rsp}      msg=The certificate hasn't been added in trust store
    ${response}=  Add Active Directory  ${OpenLDAP_rootCA_signed_1024_4096_certs}
    Wait For Task2    ${response}    timeout=60    interval=5
