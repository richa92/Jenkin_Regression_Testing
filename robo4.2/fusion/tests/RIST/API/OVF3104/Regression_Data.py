admin_cred = {
    'userName': 'administrator',
    'password': 'wpsthpvse1',
    'authLoginDomain': 'LOCAL'}

ssh_cred = {'username': 'root', 'password': 'hpvse1'}

AD_cred = {'userName': 'Administrator', 'password': 'Wpsthpvse1234'}

AD_user = {
    'userName': 'oneview',
    'password': 'Admin@123',
    'authLoginDomain': 'ADSERVER'}

ordinary_user = {
    'userName': 'test',
    'password': '!QAZ2wsx',
    'authLoginDomain': 'LOCAL'}


root_ca = {
    "members": [
        {
            "certificateDetails": {
                "aliasName": "root_CA",
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQPMm63L7kEbJKQ0QpKb/udzANBgkqhkiG9w0BAQUFADBJ\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRow\nGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xODA1MjUwOTI5NTRaFw0yMzA1\nMjUwOTM5NTNaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ\nFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsi5cFUBbB7yIqshTXWG98bb195qg3qNnvZ\nT6HDldEPryc0Tt5UXbMsI1swvQzDcbgOIGS51/fJlS68Dguu5cV03207grkpFfRl\n8AAyrxeftWW+4x8Hy2sp4WFsEOM3hwKBIYOUhBrzyUZUv3u/nj8bMPJ52UEyvqiT\n/XqgEFlCTdFX3vGMRVowN9jARFfA9AMACby8kGHkt+lsBbC0QEuMWiBd55mqlf3o\nlvbb+EWh1nd+mVfu4ghuVr4ztY1SjyXcs6Ji71LGjidhI2js/Kc/Mu8zqlitf1q2\nPrUobXXAln3Yq99tWLaAx+WgAZ3ZBJYwHHzR3HqPHe52lqun4wIDAQABo4GRMIGO\nMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8E\nBTADAQH/MB0GA1UdDgQWBBSl4IMWKKfP1EKAPFWvgFReUVq2ozASBgkrBgEEAYI3\nFQEEBQIDAwADMCMGCSsGAQQBgjcVAgQWBBR/wd/nomlY2SxW+cy7T5VoLZMT/zAN\nBgkqhkiG9w0BAQUFAAOCAQEAmLl8cFATJyUZ979i3ZhMcj1WV1QhlP3eU3bsKgkW\nD/n9Q2SbgWSbKw08m8F9KetBEmZdvAmfojcOPAww/xQrxc9gLCfpUhnaUDe4fpcV\nuAnU+S3osPj3CL5W9pIkeaXol/Dnj9BmNbD5OxvxtZbEF8E353ikcytMTKggIT4S\n3Bst+ayI3m1gI4KA9ZKjR4USxZ5TM7E/kJJZNtK0aVniWc7o2WhECw2dUe2ZzufQ\nR+DfY56kTewvTiVAA2w5/+85Ywf/8V1yy4E6Di6h63FN/LUXX2lZKnMftekjjuWz\nzH1KNRrV8HG2hvN8FqkVTAcnWEWyjr7omTLi+0bDhI1BVw==\n-----END CERTIFICATE-----",
                "type": "CertificateDetailV2"},
            "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

intermediate_ca = {
    "members": [
        {
            "certificateDetails": {
                "aliasName": "inter_CA",
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFxjCCA66gAwIBAgIQd3KakM5hSbtCt6HeUrMtDDANBgkqhkiG9w0BAQwFADBi\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRMwEQYKCZImiZPyLGQBGRYDaHBlMRQwEgYK\nCZImiZPyLGQBGRYEc2hxYTEgMB4GA1UEAxMXc2hxYS1XSU4tSDMwOVVQSTFMTVYt\nQ0EwHhcNMTcxMDI1MDczMjM1WhcNMjIxMDI1MDc0MjMxWjBiMRMwEQYKCZImiZPy\nLGQBGRYDY29tMRMwEQYKCZImiZPyLGQBGRYDaHBlMRQwEgYKCZImiZPyLGQBGRYE\nc2hxYTEgMB4GA1UEAxMXc2hxYS1XSU4tSDMwOVVQSTFMTVYtQ0EwggIiMA0GCSqG\nSIb3DQEBAQUAA4ICDwAwggIKAoICAQCfo7FQ/8i57s5TsS1tIljdZ9zrVzpVmW5c\n8lC3QXoUCcnwon28kKd7hlQTUJ/H1IJDEwe4tLVK4IDsXyjI3knIJm0KvnYv0eGn\nxgYB2EqmPQB/yGXXZ9/TVeaPdMNXf7pWGD+B9bZZ6tCbAyanvzBCCvqF/B/t+UpX\nrRjXKkuy2hOfHlHUiQDxBdMW6GOHJTRfovfguYGeVyxkGAhYPjNZckHNfm/gyy6H\nZZTCuCUrcK5j//lPtnOAFXQOGB8G2+L/BCs4gAl7PmekuFxGEfwq6CWhGYPKP7ZL\nAoQte1tkaWr9UNcL7sx4C/cOas/whsTqovUTNKgQw4BqGeuhWH07TBBoPoWO6l9B\nsPTgT0plbxV0y6A/Dgr+8j5i23vIlmahdGlECIzVCSO4ZPA9/vrD+hxatV1wV1Df\ndBjP76wKNyco0Jl3U0usUpDgfybE5P3u6G6Wvi1pCjbFsla3Y0nvJdpn4/fOz0dU\n/36C2aOBx/2PJeclp9rXBT90FQcbUZ+2Dm2200IQvygvzpvLfu9bxepeczQxSV6i\ncpbnTArW2vSzbPpM7eQUuP+XxRRnaCfA2Gq85150YmY7Jj0NIIPTahXd/6V8x/Z6\np25VWmyWYac0Y0DFWpNgjAydmOBJbCYyzX7YaS3SQ7sfOnZQhucDSPYqELPFaE5n\n+TjE5xz1TwIDAQABo3gwdjALBgNVHQ8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAd\nBgNVHQ4EFgQUwY03EWWrdVZqR+7H/epcRf65Gm0wEgYJKwYBBAGCNxUBBAUCAwEA\nATAjBgkrBgEEAYI3FQIEFgQUD92mD1Ro/8WlkG5LXQ5QS52y9vYwDQYJKoZIhvcN\nAQEMBQADggIBAD0pwqitPy21n3IJTcYKeE9PnctcCpePORF5WPQnhq5xRoxJVOGk\nj+z/GHRTTLU0gedSoMpaut/dobWA9xJ3AcfVr9ev/8yp9lz+OeSe4ZT+WXAVxKLn\nLElUDDNmCm+Ceu6CtEER28axx2lZJuy/beRtIMrkbBqn1xbw3phsVhS7Z9/61AEB\nQQSI/E9EUG14zQNKIBQ7KdqH/alDrA6AJevQL8IUmbugagPYALmtLMiyqeAQiOHc\nIkn2M6v8AMhuKzhF3RHzE756z/38qaUFGfJ7Utk/lzzBYHFRDK0c+m58YLONP9Yn\nmYPftI/gJLKlQucavOaee0MZxcPzNg0uvi/J6g3Xnq/XN3zSUloe+wNotI+4lWYO\nkcuyqOPomjSmlfBQBCapCmwe8L273IrFli5wJTm5Zo9GsPCOK79Q0bvGEImNXWcV\n8fmTZtQbc3TpHM8XoxpSqvhJmXvat7c0OdS0FCmiAZe/ioIfK/ehKI4UC7BH5Xni\nyvPPZXIw9u7B6BUqPcAZxH/vlEN3IDMOUPxFgsK3TiMK7p/4MWJ0lg89h0CxiiJ9\nnGtzDTp60iYdHTzWKGxQEqrcV6yQJAswMpIl/D0p5oy++ad8+G11RQ9aBPfnr6Tz\nL63WGXud+NwNw8Q5BH8Dy6dh9tex91LWWtqN6daf9+EjFYtHcHen8EfC\n-----END CERTIFICATE-----",
                "type": "CertificateDetailV2"},
            "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

user_ad = {"name": "userad",
           "credential": AD_cred,
           "authProtocol": "AD",
           "orgUnits": [],
           "userNamingAttribute": "UID",
           "baseDN": "DC=wpstAD,DC=com",
           "directoryServers": [{"type": "LoginDomainDirectoryServerInfoDto",
                                 "directoryServerSSLPortNumber": "636",
                                 "directoryServerIpAddress": "16.125.77.30",
                                 "directoryServerCertificateStatus": "",
                                 "serverStatus": "",
                                 "directoryServerCertificateBase64Data": ""}],
           "type": "LoginDomainConfigV600",
           "authnType": "CREDENTIAL",
           "directoryBindingType": "USER_ACCOUNT"}

service_ad = {"name": "ADSERVER",
              "credential": AD_cred,
              "authProtocol": "AD",
              "orgUnits": [],
              "userNamingAttribute": "UID",
              "baseDN": "DC=wpstAD,DC=com",
              "directoryServers": [{"type": "LoginDomainDirectoryServerInfoDto",
                                    "directoryServerSSLPortNumber": "636",
                                    "directoryServerIpAddress": "16.125.77.30",
                                    "directoryServerCertificateStatus": "",
                                    "serverStatus": "",
                                    "directoryServerCertificateBase64Data": ""}],
              "type": "LoginDomainConfigV600",
              "authnType": "CREDENTIAL",
              "directoryBindingType": "SERVICE_ACCOUNT"}

change_ad = {"name": "ADSERVER",
             "credential": AD_cred,
             "authProtocol": "AD",
             "orgUnits": [],
             "userNamingAttribute": "UID",
             "baseDN": "DC=wpstAD,DC=com",
             "directoryServers": [{"type": "LoginDomainDirectoryServerInfoDto",
                                    "directoryServerSSLPortNumber": "636",
                                    "directoryServerIpAddress": "16.125.77.30",
                                    "directoryServerCertificateStatus": "",
                                    "serverStatus": "",
                                    "directoryServerCertificateBase64Data": ""}],
             "type": "LoginDomainConfigV600",
             "authnType": "CREDENTIAL",
             "directoryBindingType": "SERVICE_ACCOUNT"}

mapping_role = {
    "type": "LoginDomainGroupCredentials",
    "group2PermissionPerGroup": {
        "type": "LoginDomainGroupPermission",
        "loginDomain": "ADSERVER",
        "egroup": "CN=OVGroup,OU=OVUser,DC=wpstAD,DC=com",
        "permissions": [
            {
                "roleName": "Infrastructure administrator",
                "scopeUri": None}]},
    "credentials": AD_cred
}

USER_AND_PERMISSION_TYPE = 'UserAndPermissions'

ordinary_user_body = {"type": "%s" % USER_AND_PERMISSION_TYPE,
                      "userName": "test",
                      "fullName": "",
                      "password": "!QAZ2wsx",
                      "emailAddress": "",
                      "officePhone": "",
                      "mobilePhone": "",
                      "enabled": True,
                      "permissions": [
                          {"roleName": "Server administrator",
                           "scopeUri": None}]}

enable_2fa = {"twoFactorAuthenticationEnabled": True}

disable_local_login1 = {"allowLocalLogin": False,
                        "emergencyLocalLoginEnabled": False,
                        "emergencyLocalLoginType": None}

disable_local_login2 = {"allowLocalLogin": False,
                        "defaultLoginDomain": {
                            "type": "LoginDomainConfigInfoDto",
                            "loginDomain": "0",
                            "name": "LOCAL",
                            "category": None,
                            "uri": ""
                        }}

enable_emergency_login1 = {
    "emergencyLocalLoginEnabled": True,
    "emergencyLocalLoginType": "APPLIANCE_CONSOLE_ONLY"}

enable_emergency_login2 = {
    "emergencyLocalLoginType": "NETWORK_AND_APPLIANCE_CONSOLE"}

enable_emergency_login3 = {
    "emergencyLocalLoginEnabled": True,
    "emergencyLocalLoginType": "NETWORK_AND_APPLIANCE_CONSOLE"}

enable_smart_card_only_login1 = {
    "strictTwoFactorAuthentication": True,
    "allowLocalLogin": True}

enable_smart_card_only_login2 = {
    "strictTwoFactorAuthentication": True,
    "allowLocalLogin": False}

enable_smart_card_only_login3 = {
    "allowLocalLogin": False,
    "emergencyLocalLoginEnabled": False,
    "strictTwoFactorAuthentication": True}

enable_smart_card_only_login4 = {
    "allowLocalLogin": False,
    "emergencyLocalLoginEnabled": True,
    "emergencyLocalLoginType": "NETWORK_AND_APPLIANCE_CONSOLE",
    "strictTwoFactorAuthentication": True}

enable_smart_card_only_login5 = {
    "allowLocalLogin": False,
    "emergencyLocalLoginEnabled": True,
    "emergencyLocalLoginType": "APPLIANCE_CONSOLE_ONLY",
    "strictTwoFactorAuthentication": True}

enable_smart_card_only_login6 = {"allowLocalLogin": False,
                                 "emergencyLocalLoginEnabled": False,
                                 "strictTwoFactorAuthentication": True,
                                 "twoFactorAuthenticationEnabled": False}

enable_smart_card_only_login7 = {"allowLocalLogin": False,
                                 "emergencyLocalLoginEnabled": False,
                                 "strictTwoFactorAuthentication": True,
                                 "twoFactorAuthenticationEnabled": True}

disable_smart_card_only_login = {"strictTwoFactorAuthentication": False}

invalid_smart_card_only_login = {"allowLocalLogin": False,
                                 "emergencyLocalLoginEnabled": False,
                                 "strictTwoFactorAuthentication": None,
                                 "twoFactorAuthenticationEnabled": True}

enable_local_login = {"allowLocalLogin": True}

validation_body = {"type": "LoginCertificateConfigDto",
                   "subjectPatterns": ["E=(.*)"],
                   "subjectAlternateNamePatterns": [],
                   "certificateDomainIdentifier": "Issuer",
                   "validationOids": [
                       {"1.3.6.1.4.1.311.20.2.2": "Smart Card Logon",
                        "1.3.6.1.5.5.7.3.2": "Client Authentication"}],
                   "certificateDomainIdentifierPattern": "DC=(.*)"}

default_2FA_validation = {
    "type": "LoginCertificateConfigDto",
    "subjectPatterns": [],
    "subjectAlternateNamePatterns": ["OtherName.UPN=(.*)"],
    "certificateDomainIdentifier": "Subject",
    "certificateDomainIdentifierPattern": "DC=(.*)",
    "validationOids": [
        {
            "1.3.6.1.4.1.311.20.2.2": "Smart Card Logon",
            "1.3.6.1.5.5.7.3.2": "Client Authentication"}],
    "category": "Users",
    "uri": "/rest/logindomains/logincertificates"}

reset_auth_settings = {"twoFactorAuthenticationEnabled": False,
                       "defaultLoginDomain": {
                           "type": "LoginDomainConfigInfoDto",
                           "name": "LOCAL",
                           "uri": "",
                           "loginDomain": "0"}
                       }

errorMessages = {
    "Fail_Enable_2FA_only_login1": "When smart card only login is specified for two factor authentication, local login must be disabled and \"Appliance console only\" must be specified if emergency local login is enabled.",
    "Fail_Enable_2FA_only_login2": "Enabling smart card only login is not allowed when two factor authentication is disabled.",
    "Fail_Local_login1": "Log in using your directory user name and password or use smart card if smart card only login is enabled.",
    "Fail_Local_login2": "Local user authentication is disabled by the administrator.",
    "Directory_login_error": "Cannot login as active directory user using credentials when smart card only login is enabled.",
    "Null_smart_card_only_login_error": "Smart card only login value cannot be null.",
    "Fail_Enable_Emergency_Login": "Emergency local login access is only available when local login is disabled.",
    "Fail_disable_local_login": "Could not configure allow local login setting to false while the default directory is LOCAL.",
    "Invalid_emergency_values": "Invalid JSON data type.",
    "None_emergency_type": "Emergency local login type is required."}

destination_path = '/root/automation_tools/OVF3104_auto'

setup_evn_commands = {
    'command1': 'unzip %s/curl_tool.zip -d %s' % (destination_path, destination_path),
    'command2': 'rpm -ivh %s/curl_tool/libcurl-7.54.1-1.hpe.x86_64.rpm --force' % destination_path,
    'command3': 'rpm -ivh %s/curl_tool/curl-7.54.1-1.hpe.x86_64.rpm --force' % destination_path,
    'command4': 'rpm -ivh %s/curl_tool/libssh2-1.8.0-2.0.hpe.rhel6.x86_64.rpm --force' % destination_path}

clear_evn_commands = {
    'command1': 'rm -rf %s/curl_tool' % destination_path,
    'command2': 'rm -rf %s/curl_tool.zip' % destination_path,
    'command3': 'rm -rf %s/OVF3104_auto_client-cert.pem' % destination_path}

curl_commands = {
    'part1': 'curl -v -i -X POST -H "Accept-Language:en-US" -H "X-Api-Version:',
    'part2': '" --cert %s/OVF3104_auto_client-cert.pem:\'123456\' https://' % destination_path,
    'part3': '/rest/login-sessions/smartcards -k',
    'part4': 'curl -v -i -X PUT -H "Accept-Language:en-US" -H "X-Api-Version:',
    'part5': '" -H "Auth:',
    'part6': '" -H "Accept:application/json" -H "Content-Type:application/json" -d \'',
    'part7': '\' https://',
    'part8': '/rest/logindomains/global-settings -k',
    'part9': 'curl -v -i -X GET -H "Accept-Language:en-US" -H "X-Api-Version:',
    'part10': '" https://'}

invalid_emergencytype_list = [
    {"emergencyLocalLoginType": "network_and_appliance_console"},
    {"emergencyLocalLoginType": "appliance_console_only"},
    {"emergencyLocalLoginType": "network and appliance console"},
    {"emergencyLocalLoginType": "NETWORK AND APPLIANCE CONSOLE"},
    {"emergencyLocalLoginType": "appliance console only"},
    {"emergencyLocalLoginType": "APPLIANCE CONSOLE ONLY"},
    {"emergencyLocalLoginType": "dfdfgfgfgfg"},
    {"emergencyLocalLoginType": "     "},
    {"emergencyLocalLoginType": ""}]

null_emergencyType = {"emergencyLocalLoginType": None}

edit_login_message1 = {
    "allowLocalLogin": False,
    "emergencyLocalLoginEnabled": False,
    "emergencyLocalLoginType": None,
    "strictTwoFactorAuthentication": True,
    "twoFactorAuthenticationEnabled": True,
    "loginMessage": {
        "type": "LoginMessageVersion600",
        "acknowledgment": True,
        "message": "This management appliance is a company owned asset and provided for the exclusive use of authorized personnel. Unauthorized use or abuse of this system may lead to corrective action including termination, civil and/or criminal penalties.\n\n*dfgfgfgf\n   *fghfghghg\n*gfghgh\n\n[Google](www.google.com)\n\n*fgfgfgfg*",
        "category": "users",
        "uri": "/rest/logindomains/global-settings"},
}

edit_login_message2 = {
    "allowLocalLogin": False,
    "emergencyLocalLoginEnabled": False,
    "emergencyLocalLoginType": None,
    "strictTwoFactorAuthentication": False,
    "twoFactorAuthenticationEnabled": True,
    "loginMessage": {
        "type": "LoginMessageVersion600",
        "acknowledgment": True,
        "message": "This management appliance is a company owned asset and provided for the exclusive use of authorized personnel. Unauthorized use or abuse of this system may lead to corrective action including termination, civil and/or criminal penalties.\n\n*dfgfgfgf\n   *fghfghghg\n*gfghgh",
        "category": "users",
        "uri": "/rest/logindomains/global-settings"},
}

reset_login_message = {
    "allowLocalLogin": False,
    "emergencyLocalLoginEnabled": False,
    "strictTwoFactorAuthentication": False,
    "twoFactorAuthenticationEnabled": True,
    "loginMessage": {
        "type": "LoginMessageVersion600",
        "acknowledgment": False,
        "message": "This management appliance is a company owned asset and provided for the exclusive use of authorized personnel. Unauthorized use or abuse of this system may lead to corrective action including termination, civil and/or criminal penalties.",
        "category": "users",
        "uri": "/rest/logindomains/global-settings"},
}
