Directory_Type = "LoginDomainConfigV600"
DirectoryGroup_Type = "LoginDomainGroupCredentials"
Certificate_Type = "CertificateDetailV2"
iPdu_Repo_Cert_Type = "CertificateInfoV2"
IPDU182_IP = "16.125.33.182"
REPO_IP = "16.114.219.161"
GEN6_IP = "16.114.212.10"
GEN7_IP = "16.114.212.7"
ADIP = "16.125.77.30"
LDIP = "16.125.76.222"
fcoe_domain = "NO DOMAIN"
fc_domain = "Tbird_Regression_Domain"
providerId = "0aa1f4e1-3b5e-4233-af1a-f849dc64da69"
storage_id = "/1645395"
managedDomain = "NO DOMAIN"
dump_filename = "supportdump.sdmp"
ok_status = "OK"

LD_cred = {'userName': 'wpstuser', 'password': 'P@ssw0rd'}
AD_cred = {'userName': 'oneview', 'password': 'Admin@123'}

ldap_root_ca = "LDAPRootCA"
ldap_intermedia_ca = "LDAPIntermediateCA"
ad_root_ca = "ADRootCA"
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
IPDU_SERVER_CA_SIGN_PDU = ["%s, PDU 1" % IPDU182_IP]
add_ldap_rootcacert = {
    "members": [
        {
            "certificateDetails": {
                "aliasName": ldap_root_ca,
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIECjCCAvKgAwIBAgIJAO9jxxrDwwEjMA0GCSqGSIb3DQEBCwUAMIGRMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRv\nMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEW\nMBQGCgmSJomT8ixkARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTAeFw0x\nODA1MjIxNjI0MjBaFw0yODAyMTkxNjI0MjBaMIGRMQswCQYDVQQGEwJVUzETMBEG\nA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9I\nZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEWMBQGCgmSJomT8ixk\nARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTCCASIwDQYJKoZIhvcNAQEB\nBQADggEPADCCAQoCggEBAO2qMOGXDpsyb25et7r4ya0R1d5DfB5wo6HipxtyRL2H\nkMfvhyHB7izNdxbdUmJW6Zf3FkDB/bTolEjMPgAwFdfMOTk5T5fbF+eUDsHnk3Zz\nBBzHQuQ+r6Z+K2Av9P7+pOkOUrkjt28pcFYeYZeYHQ1iUIFb9IVRut0bf+8XDlCU\nTgYK2KmzKyPISBas/3KgngjdY1F9zccW/wIBaHou77vM9ozOxdT6qjP+hmMx9WJY\nE7gzMQT8+9Gyh0XZzhrKqPFHHj12ztKHlknMDP9kv9esVPIUyD3viBVjdnmpEE+S\ny62wuVdGsJhJbyyM2peOTS/LoFW0bcg2Sbr9WWrjNkECAwEAAaNjMGEwHQYDVR0O\nBBYEFJgJWnvnI/CINkmuoBpQqYx5jPR5MB8GA1UdIwQYMBaAFJgJWnvnI/CINkmu\noBpQqYx5jPR5MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMA0GCSqG\nSIb3DQEBCwUAA4IBAQA4HfPrPCmW10uYSL7suwlKLfk+5nRqQU5U5emKi0YAXzuL\nIKg7cdjQIZin01Zu6VbXXW8Kx7gof8X98UFXC1fWe0o/z3H5Y/C67we/NkUkhwmz\nDZB6SA7HJcslMCPJGIgV2UEyDA/ZN1rmSh5UeX1fzBBgW1NzgTwH8J2IR9j+LRbo\n/ujN7sNMUP47XAyjIe8mTMwC7mXOhdYYl432EPunRSNMHdXn2i37lTPoT19fIhDy\nN5eDbQAqXtviOHDtHbd1kZM0+RxZY9BDrLu4NpzrSXIWXsk6HKASuUf3i+chXZZ0\neDd8PulIMpKtQslgoDJyGnClYn4RxOdMPjwu5Qvn\n-----END CERTIFICATE-----",
                "type": Certificate_Type},
            "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

add_ldap_intermediatecacert = {
    "members": [
        {
            "certificateDetails": {
                "aliasName": ldap_intermedia_ca,
                "base64Data": "-----BEGIN CERTIFICATE-----\n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\n-----END CERTIFICATE-----",
                "type": Certificate_Type},
            "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

add_ldap = {
    "name": "TestLdap",
    "credential": LD_cred,
    "authProtocol": "LDAP",
    "orgUnits": [
        "OU=Users",
        "ou=People",
        "ou=Groups"],
    "userNamingAttribute": "UID",
    "baseDN": "dc=ldapfc,dc=com",
    "directoryServers": [
        {
            "type": "LoginDomainDirectoryServerInfoDto",
                    "directoryServerSSLPortNumber": "636",
                    "directoryServerIpAddress": LDIP,
                    "directoryServerCertificateStatus": "",
                    "serverStatus": "",
                    "directoryServerCertificateBase64Data": ""}],
    "type": Directory_Type,
    "authnType": "CREDENTIAL",
    "directoryBindingType": "USER_ACCOUNT"}

ldap_group = {
    "type": DirectoryGroup_Type,
    "group2PermissionPerGroup": {
        "type": "LoginDomainGroupPermission",
        "loginDomain": "TestLdap",
        "egroup": "cn=FUSION_ADMIN,ou=Groups,dc=ldapfc,dc=com",
        "permissions": [
            {
                "roleName": "Server administrator",
                "scopeUri": None}]},
    "credentials": LD_cred
}

ldap_user = {
    'userName': 'wpstuser',
    'password': 'P@ssw0rd',
    'authLoginDomain': 'TestLdap'}

add_ad_rootcacert = {
    "members": [
        {
            "certificateDetails": {
                "aliasName": ad_root_ca,
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQPMm63L7kEbJKQ0QpKb/udzANBgkqhkiG9w0BAQUFADBJ\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRow\nGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xODA1MjUwOTI5NTRaFw0yMzA1\nMjUwOTM5NTNaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ\nFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsi5cFUBbB7yIqshTXWG98bb195qg3qNnvZ\nT6HDldEPryc0Tt5UXbMsI1swvQzDcbgOIGS51/fJlS68Dguu5cV03207grkpFfRl\n8AAyrxeftWW+4x8Hy2sp4WFsEOM3hwKBIYOUhBrzyUZUv3u/nj8bMPJ52UEyvqiT\n/XqgEFlCTdFX3vGMRVowN9jARFfA9AMACby8kGHkt+lsBbC0QEuMWiBd55mqlf3o\nlvbb+EWh1nd+mVfu4ghuVr4ztY1SjyXcs6Ji71LGjidhI2js/Kc/Mu8zqlitf1q2\nPrUobXXAln3Yq99tWLaAx+WgAZ3ZBJYwHHzR3HqPHe52lqun4wIDAQABo4GRMIGO\nMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8E\nBTADAQH/MB0GA1UdDgQWBBSl4IMWKKfP1EKAPFWvgFReUVq2ozASBgkrBgEEAYI3\nFQEEBQIDAwADMCMGCSsGAQQBgjcVAgQWBBR/wd/nomlY2SxW+cy7T5VoLZMT/zAN\nBgkqhkiG9w0BAQUFAAOCAQEAmLl8cFATJyUZ979i3ZhMcj1WV1QhlP3eU3bsKgkW\nD/n9Q2SbgWSbKw08m8F9KetBEmZdvAmfojcOPAww/xQrxc9gLCfpUhnaUDe4fpcV\nuAnU+S3osPj3CL5W9pIkeaXol/Dnj9BmNbD5OxvxtZbEF8E353ikcytMTKggIT4S\n3Bst+ayI3m1gI4KA9ZKjR4USxZ5TM7E/kJJZNtK0aVniWc7o2WhECw2dUe2ZzufQ\nR+DfY56kTewvTiVAA2w5/+85Ywf/8V1yy4E6Di6h63FN/LUXX2lZKnMftekjjuWz\nzH1KNRrV8HG2hvN8FqkVTAcnWEWyjr7omTLi+0bDhI1BVw==\n-----END CERTIFICATE-----",
                "type": Certificate_Type},
            "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

add_ad = {"name": "TestAD",
          "credential": AD_cred,
          "authProtocol": "AD",
          "orgUnits": [],
          "userNamingAttribute": "UID",
          "baseDN": "DC=wpstAD,DC=com",
                    "directoryServers": [{"type": "LoginDomainDirectoryServerInfoDto",
                                          "directoryServerSSLPortNumber": "636",
                                          "directoryServerIpAddress": ADIP,
                                          "directoryServerCertificateStatus": "",
                                          "serverStatus": "",
                                          "directoryServerCertificateBase64Data": ""}],
                    "type": Directory_Type,
                    "authnType": "CREDENTIAL",
                    "directoryBindingType": "USER_ACCOUNT"}

ad_group = {
    "type": DirectoryGroup_Type,
    "group2PermissionPerGroup": {
        "type": "LoginDomainGroupPermission",
        "loginDomain": "TestAD",
        "egroup": "CN=OVGroup,OU=OVUser,DC=wpstAD,DC=com",
        "permissions": [
            {
                "roleName": "Server administrator",
                "scopeUri": None}]},
    "credentials": AD_cred
}

ad_user = {
    'userName': 'oneview',
    'password': 'Admin@123',
    'authLoginDomain': 'TestAD'}

addGen6requestody = {
    "hostname": GEN6_IP,
    "username": "Administrator",
    "password": "hpvse1-ilo",
    "force": True,
    "licensingIntent": "OneViewStandard",
    "configurationState": "Monitored",
    "initialScopeUris": []}

addGen7requestody = {
    "hostname": GEN7_IP,
    "username": "Administrator",
    "password": "hpvse1-ilo",
    "force": True,
    "licensingIntent": "OneViewStandard",
    "configurationState": "Monitored",
    "initialScopeUris": []}

support_dump = {
    "encrypt": True,
    "errorCode": "CI",
    "userName": "administrator",
    "password": "mypassword",
    "dump": "support"}

add_repo_cert = {
    "type": iPdu_Repo_Cert_Type,
    "certificateDetails": [
        {
            "base64Data": "",
            "aliasName": REPO_IP,
            "type": Certificate_Type}]}

add_ipdu_cert = {"type": iPdu_Repo_Cert_Type,
                 "certificateDetails": [{"base64Data": "",
                                         "aliasName": IPDU182_IP,
                                         "type": Certificate_Type}]}

add_ipdu = {
    "hostname": IPDU182_IP,
    "username": "admin",
    "password": "admin",
    "force": True}

add_repo = {
    "repositoryName": "TestRepo",
    "repositoryURI": "https://%s/webdav" % REPO_IP,
    "userName": "Administrator",
    "password": "Lsdt4acsl",
    "base64Data": ""}

add_sammanager = {"connectionInfo": [{"name": "Host",
                                      "displayName": "Host",
                                      "required": True,
                                      "value": "16.125.65.9",
                                      "valueFormat": "IPAddressOrHostname",
                                      "valueType": "String"},
                                     {"name": "Port",
                                      "displayName": "Port",
                                      "required": True,
                                      "value": 5989,
                                      "valueFormat": "None",
                                      "valueType": "Integer"},
                                     {"name": "Username",
                                      "displayName": "Username",
                                      "required": True,
                                      "value": "Administrator",
                                      "valueFormat": "None",
                                      "valueType": "String"},
                                     {"name": "Password",
                                      "displayName": "Password",
                                      "required": True,
                                      "value": "password",
                                      "valueFormat": "SecuritySensitive",
                                      "valueType": "String"},
                                     {"name": "UseSsl",
                                      "displayName": "UseSsl",
                                      "required": True,
                                      "value": True,
                                      "valueFormat": "None",
                                      "valueType": "Boolean"}]}

add_storagesystem = {
    "family": "StoreServ",
    "hostname": "wpst3par-7200-5-srv.vse.rdlabs.hpecorp.net",
    "username": "fusionadm",
    "password": "hpvse1"}

ValidateFirmwares = ["2018.06.19.00"]

FirmwareVersions = ["2018.06.19.00"]
