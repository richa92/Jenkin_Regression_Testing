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

Test Setup      LDAPServer Pre-Condition suite         ${OpenLDAP_self_signed_server_name}         ${OpenLDAP_Backup_DBConfig_CMD}         ${OpenLDAP_ModifyDB_KeyLength_LessThan_1024_Cert_CMD}
Test Teardown   LDAPServer Post-Condition suite        ${OpenLDAP_self_signed_server_name}         ${OpenLDAP_Restore_DBConfig_CMD}

*** Variables ***

${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Add a remote server which the certificate key length is less than 1024
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Log  Getting Remote Server Certificate and validating the trust status   console=yes
    :FOR    ${host}   IN  @{Key_length_less_than_1024}
    \  ${rsp} =    Fusion API Get Remote Certificate   ${host}
    \  Should BE Equal As Strings  ${rsp['message']}   ${Invalid_key_length}   msg=Validating the error message is right.
    \  Log  Validating recommended actions message    console=yes
    \  Should BE Equal As Strings  ${rsp['recommendedActions'][0]}  ${Invalid_certificate_less_than_1024}   msg=Validating the recommended actions is right.
