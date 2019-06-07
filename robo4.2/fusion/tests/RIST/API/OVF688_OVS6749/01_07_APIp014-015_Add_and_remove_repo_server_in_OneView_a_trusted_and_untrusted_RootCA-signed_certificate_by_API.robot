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
Test Teardown   Run Keyword And Ignore Error
...             Remove All Repo Servers And All CA Certificates  ${Repo_server_rootCA_server_name}   ${Delete_repo_server_RootCA}

*** Variables ***

${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Add and remove Repo_server in OneView a trusted and untrusted RootCA-signed certificate by API
    Pass Execution If  '${SECURITY_MODE}' != 'LEGACY'
    ...                message=External Repo is unsupported on FIPS/CNSA, skip this case

    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${Repo_server_rootCA_signed}   False
    Should Be True   ${rsp}     msg=The certificate has been added in trust store
    Trust RootCA_signed Or SubCA_signed Certificate  ${Repo_RootCA_signed_certs_trust_body}
    ${rsp} =  Fetch Remote Server And Validate The Trusted Status As Expected  ${Repo_server_rootCA_signed}   True
    Should Be True   ${rsp}     msg=The certificate hasn't been added in trust store
    ${resp} =   Add Repository  ${Repo_server_rootCA_certs}
    Wait For Task2           ${resp}     120    5
