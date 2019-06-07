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
Test Teardown   Remove Active Directory And All CA Certificates   ${AD_rootCA_server_name}   ${Delete_rootCA_signed}

*** Variables ***

${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Add and remove AD server in OneView a trusted and untrusted rootCA-signed certificate by API
    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${AD_rootCA_signed}   False
    Should Be True   ${rsp}     msg=The certificate has been added in trust store
    Trust RootCA_signed Or SubCA_signed Certificate  ${AD_RootCA_signed_certs_trust_body}
    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${AD_rootCA_signed}   True
    Should Be True   ${rsp}     msg=The certificate hasn't been added in trust store
    ${response}=  Add Active Directory  ${AD_rootCA_signed_certs}
    Wait For Task2    ${response}    timeout=60    interval=5
