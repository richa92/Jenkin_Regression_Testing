*** Settings ***
Documentation        2FA configurations should not be changed after backup restore
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              robot.libraries.String
Library              String
Library              Dialogs
Library              BuiltIn
Library              json
Library              Collections
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${cert_OID}    validationOids
${restore_body_item}    uriOfBackupToRestore


*** Test Cases ***
Backup restore for 2FA
    [Documentation]    2FA configurations should not be changed after backup restore
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${status} =  Run Keyword And Return Status    Edit successful 2FA login configurations    ${successful_2FA_validation2}
    Should Be True    ${status}    msg=Fail to edit successful 2FA login validation configurations

    Log    \n-Get 2FA configurations before backup/restore    console=yes
    ${login_global_settings_before_test} =  Fusion Api Get Login Domains Global Settings
    ${login_certificates_before_test} =  fusion api get login domains login certificates
    Remove From Dictionary    ${login_certificates_before_test}    eTag    created    modified    category    uri

    Log    \n-Create backup file    console=yes
    Create backup

    Log    \n-Change 2FA configurations    console=yes
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[4:6]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'  '200'  msg= Fail to add one OID box same with existed ones
    Check updated 2FA validation configurations    ${cert_OID}    ${OIDs[4:6]}

    Log    \n-Restore appliance    console=yes
    Restore Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Log    \n-Get 2FA configurations after backup/restore    console=yes
    ${login_global_settings_after_test} =  Fusion Api Get Login Domains Global Settings
    ${login_certificates_after_test} =  fusion api get login domains login certificates
    Remove From Dictionary    ${login_certificates_after_test}    eTag    created    modified    category    uri
    Should Be Equal    ${login_global_settings_after_test['twoFactorAuthenticationEnabled']}    ${login_global_settings_before_test['twoFactorAuthenticationEnabled']}    msg=2FA configurations is changed after backup restore
    Should Be Equal    ${login_certificates_after_test}    ${login_certificates_before_test}    msg=2FA configurations is changed after backup restore
    Fusion Api Logout Appliance

    ${resp} =  2FA Login    ${curl_commands['part2']}
    Should Be Equal    '${resp}'    '200 OK'    msg=Fail to 2FA login with correct Subject cert owner