from dto import APPLIANCE_CSR_TYPE   # pylint: disable=import-error

admin_cred = {
    'userName': 'administrator',
    'password': 'wpsthpvse1',
    'authLoginDomain': 'local'}

remote_server_IP = '16.125.76.222'

remote_server_cred = {'username': 'root', 'password': 'hpvse1'}

root_ca = {
    "members": [
        {"certificateDetails": {
            "aliasName": "rootca",
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIEczCCA1ugAwIBAgIJAI7XSzQ4TOj1MA0GCSqGSIb3DQEBCwUAMGsxCzAJBgNV\r\nBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8x\r\nGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEZMBcGA1UEAwwQSFAgVGVzdEhlYWQg\r\nUm9vdDAgFw0xODA3MDIxOTQ4MTBaGA8yMTE4MDYwODE5NDgxMFowazELMAkGA1UE\r\nBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEY\r\nMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDDBBIUCBUZXN0SGVhZCBS\r\nb290MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq7vV/Y0rKa650fMj\r\nYPe8ZU7Y57YzeOkGcqUwf9yZSrsXO8OQaMs+U6adALWQFE0u/lJ0NABIixDUJHhy\r\nK1u1OKfI/kCdTmCdZWWjv2MaW7QYGRWehvnJQ82fR+MwaohALwKThswtgoHrv9Cf\r\nYPxlCZVag5nIeJKjjVopoG8lCFskaIab0yhGvI+F9VZecsXdGhKt94g1fzmMXus1\r\nqaiLqN0EDtdsRuEWvmzjcA9NQp+KMwnBLm2Bq2hdtVWZGFmvZLqcJY8vGe4QAWzU\r\n/QbvxOm5ezvKB0eFimZ2Du/3+lMJG3K+wi6Z8XeNFhCPLaa7bEJls4jDtxyjDCIY\r\nGtWtHQIDAQABo4IBFjCCARIwHQYDVR0OBBYEFCUnG1Uad+e8hggNN3YAUdTFmfVB\r\nMIGdBgNVHSMEgZUwgZKAFCUnG1Uad+e8hggNN3YAUdTFmfVBoW+kbTBrMQswCQYD\r\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRv\r\nMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxGTAXBgNVBAMMEEhQIFRlc3RIZWFk\r\nIFJvb3SCCQCO10s0OEzo9TALBgNVHQ8EBAMCAbYwDAYDVR0TBAUwAwEB/zA2Bggr\r\nBgEFBQcBAQQqMCgwJgYIKwYBBQUHMAGGGmh0dHA6Ly9sb2NhbGhvc3Q6MjU2MC9v\r\nY3NwMA0GCSqGSIb3DQEBCwUAA4IBAQBZ0vMd6CHrVJU5XBPhNcjreLJlddOQ1UAr\r\nEU4UMETNKcGjbvnT5nF96mRcVZVS9QyVkongG1JNHavzK0/t1GPSql8rlfZvXHnD\r\nVEssWIxhTexWGq2PPQOdlrICd9ptZx2IBPgXGchj1WcQV4fQtMjKtHNzSIf9od/m\r\nDQ/LFQMcvnLzKq3X+i8oR3EvQpsQMhrIpvDM79ZyVtl2EC0R0oqSHNn3H0UKoM8b\r\n0LAVpip5DUrrtO/2CXjl12m78hggUC1YRReLjS6fLk0vcz6/B9fm+CdCYSyuJyE2\r\n9IrHhIp7/hgZIBsapgZpsuuSHhTESSu0+MsbQlKeUzf+dzej5gof\r\n-----END CERTIFICATE-----",
            "type": "CertificateDetailV2"},
         "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

intermediate_ca = {
    "members": [
        {"certificateDetails": {
            "aliasName": "intermediateca",
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIEHjCCAwagAwIBAgICFXswDQYJKoZIhvcNAQELBQAwazELMAkGA1UEBhMCVVMx\nEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UE\nCgwPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDDBBIUCBUZXN0SGVhZCBSb290MCAX\nDTE4MDUyNTA2MTczN1oYDzIxMTgwNTAxMDYxNzM3WjBuMQswCQYDVQQGEwJVUzET\nMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQK\nDA9IZXdsZXR0LVBhY2thcmQxHDAaBgNVBAMME0hQIFRlc3RIZWFkIGludGVyLTEw\nggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDlwK8MPMfVo9brybbUSczb\nr1bPf1RD4xabeGJqXjzirVB9Hx3t4322HZZrSMmC8ucf/IW6/3nc3HtCw3QV+vWi\ndO23giEWEdzUBHcFQYg5ELdmzOej6h2XxKUd7KJECPXHt1kBgg/x+RtOfMsI2MKf\n+lE6svDCw366qWIRhqb9xwW+UEA2BSFGOaaomzKHUiu4TPeWbt2ueZnBfH9tVF5S\neWh8HjWypkt+u8jApOKRMFsoIyWG/+shSpFCfKKSgrOZ1hPgz/R5UlWWT1A4Kt81\njovtjGVviZYo5YgYtRqwutfH2/s7YY/ryGUV8B3NlNl7lJt0IIbt1Ilm5VXyNREX\nAgMBAAGjgcYwgcMwHQYDVR0OBBYEFA/h4lbacupoCDK2ivyhQHlEnLumMB8GA1Ud\nIwQYMBaAFEDFWJxv6TT0W4rLcziIWMOMyuNnMA8GA1UdEwEB/wQFMAMBAf8wDgYD\nVR0PAQH/BAQDAgGGMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3Qv\nY2EuY3JsMDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2Fs\naG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQELBQADggEBAEk9/hA3sq2DAE++DLTi\ng5MyXDSqHIG26YjE4MfNdm7BTP6Dzb29wNoiarPiuHkDv5TGiB1XcF+ZegUz8uAQ\nFXigiG/6WBMHin2ewAmVTlpaOG7Phj34wgicpXzmtVtaxHaroU4X9BVOpf4zm6KH\nlaru7v5xlhDKTnhon8rVwi7GZt6ddIkj882kpqOXflwY5D+GcikdBJMRABjomudh\n3mfKIMZ4X79gxLA7Kfmn2V2TF3/7EIyUCK2xJww/cQdwpnlfyES3don046nd2mIG\ny6CdJbBDaPTOuBytFtTgNhtKTBXqSj8RYShIZ9ujjcMyf+R9lhJCME7/Tz/PCpmL\nyjY=\n-----END CERTIFICATE-----",
            "type": "CertificateDetailV2"},
         "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

ca_cert_body = {
    "members": [
        {"certificateDetails": {
            "aliasName": "",
            "base64Data": "",
            "type": "CertificateDetailV2"},
         "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

ca_csr_cert_body = {
    "members": [
        {"certificateDetails": {
            "aliasName": "CSRrootca",
            "base64Data": "",
            "type": "CertificateDetailV2"},
         "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

self_signed_leaf_cert = {
    "certificateDetails": [
        {
            "aliasName": "leaf_cert",
            "base64Data": '-----BEGIN CERTIFICATE-----\nMIIDzTCCArWgAwIBAgIJAN2m6mDN6pPYMA0GCSqGSIb3DQEBCwUAMH0xCzAJBgNV\r\nBAYTAklOMQwwCgYDVQQIDANLQVIxDDAKBgNVBAcMA0JORzEMMAoGA1UECgwDSFBF\r\nMQ0wCwYDVQQLDARSSVNUMQ0wCwYDVQQDDARUZXN0MSYwJAYJKoZIhvcNAQkBFhdz\r\nYW50b3NocmV2YW5ha2lAaHBlLmNvbTAeFw0xODA2MjExNjAxMjFaFw0yMTA0MTAx\r\nNjAxMjFaMH0xCzAJBgNVBAYTAklOMQwwCgYDVQQIDANLQVIxDDAKBgNVBAcMA0JO\r\nRzEMMAoGA1UECgwDSFBFMQ0wCwYDVQQLDARSSVNUMQ0wCwYDVQQDDARUZXN0MSYw\r\nJAYJKoZIhvcNAQkBFhdzYW50b3NocmV2YW5ha2lAaHBlLmNvbTCCASIwDQYJKoZI\r\nhvcNAQEBBQADggEPADCCAQoCggEBANeoPjG5ar9SC0joYDEX+Rzc7iN+GF+0ouHv\r\nI6DqIWDmSTUEukOAL0rif6GkQ45RD2OfUqy/hPWSx6KLW4rX1Myhqk+kGA/6f91f\r\nLK36zZj5VXpYcrxBmQMXQhX2mZtfEqH56spbtqo8s5ndQddlB+vFQOAgp9bgIEbz\r\ntBkQx4FhXW+eF2ZxxAR4dxOQ/YtvHiXDrMV1SlzTyILEj86hei++wQ+gZ9AkCzC5\r\n/UNvg2cD91xP3Oom01mKJSgQ9op3i/gjGgQpDw9+pEmyl4uininiDXFKe8ObZN7G\r\n0OTboVS7gRfE7SLO489MVoPQfcY/rhLLlYJHiZfKfGT80ggOzCsCAwEAAaNQME4w\r\nHQYDVR0OBBYEFNslLsWUZiiWvGLsEp7ox1JFc+l3MB8GA1UdIwQYMBaAFNslLsWU\r\nZiiWvGLsEp7ox1JFc+l3MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEB\r\nAAjc5YRIJ1LumB+ew2cKJpAzbM04crIYkDacgZTubtlRUviLYfj9HxFSXVvVnnH9\r\nx7rXNgfni9j3T6imJIFd70irtrSF0E5MAZW2KbJh7y2EyRulE370oM6EVs2Qs09q\r\nR6Wr6pP/OTcpALPPZM9kyddiy1n7npXJH5eQ53rSQqJt+zqlD5N/ISbTBh1CrTry\r\nto6WaE0KDp5XrALozbMs1BWQbAQIgHLFYvd1DD+bMdo0/7HNQBY3kw2mYblPZt5J\r\n3uALhbqZ5n3pi+DARSBYMSQIA2OV9TcmmREp0Y0YKfPJCG9oeb/C8R2Zo/38UQrL\r\n/RA15bYF7P6wYNIUniWQqIg=\r\n-----END CERTIFICATE-----',
            "type": "CertificateDetailV2"}],
    "type": "CertificateInfoV2"}

basic_body = {"country": "US",
              "state": "California",
              "locality": "Palo Alto",
              "organization": "Hewlett Packard Enterprise",
              "organizationalUnit": "",
              "contactPerson": "",
              "email": "",
              "surname": "",
              "givenName": "",
              "initials": "",
              "dnQualifier": "",
              "type": "CertificateDtoV3"}

validation_body1 = {
    "type": "CertValidationConfig",
    "okToReboot": True,
    "certValidationConfig": {
        "global.allow.invalidCRL": False,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.allow.noCRL": False,
        "global.enforceStrictTrust": True,
        "global.enableHostNameVerification": True,
        "global.disableAlertForCRL": False,
        "global.checkCertificateRevocation": True,
        "global.validateCertificate": True}}

validation_body2 = {
    "type": "CertValidationConfig",
    "okToReboot": True,
    "certValidationConfig": {
        "global.allow.invalidCRL": True,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.allow.noCRL": True,
        "global.enforceStrictTrust": True,
        "global.enableHostNameVerification": True,
        "global.disableAlertForCRL": True,
        "global.checkCertificateRevocation": True,
        "global.validateCertificate": True}}

check_validation_body1 = {
    "type": "CertValidationConfig",
    "okToReboot": False,
    "certValidationConfig": {
        "global.allow.invalidCRL": False,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.allow.noCRL": False,
        "global.enforceStrictTrust": True,
        "global.enableHostNameVerification": True,
        "global.disableAlertForCRL": False,
        "global.checkCertificateRevocation": True,
        "global.validateCertificate": True}}

check_validation_body2 = {
    "type": "CertValidationConfig",
    "okToReboot": False,
    "certValidationConfig": {
        "global.allow.invalidCRL": True,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.allow.noCRL": True,
        "global.enforceStrictTrust": True,
        "global.enableHostNameVerification": True,
        "global.disableAlertForCRL": True,
        "global.checkCertificateRevocation": True,
        "global.validateCertificate": True}}

rabbitmq_client_cert_body = {
    "commonName": "default",
    "type": "RabbitMqClientCertV2"}

alert_messages = {
    "Add_Cert_Name": "Add",
    "Add_CA_Cert": "Successfully added certificate(s).",
    "Add_leaf_Cert": "Successfully added certificate(s). : leaf_cert",
    "CRL_NOT_FOUND_For_root_CA": "The CRL is not found for CA Certificate whose aliasName is rootca",
    "CRL_NOT_FOUND_For_intermediate_CA": "The CRL is not found for CA Certificate whose aliasName is intermediateca",
    "Untrusted_for_intermediate_CA": "CA certificate with alias name intermediateca is not trusted",
    "Remove_Cert_Name": "Delete",
    "Remove_root_CA": "Successfully deleted certificate. : rootca",
    "Remove_intermediate_CA": "Successfully deleted certificate. : intermediateca",
    "Remove_leaf_cert": "Successfully deleted certificate. : leaf_cert",
    "Create_Selfsigned_Appliance_Cert_Name": "Certificate SelfSigned Configuration.",
    "Create_Selfsigned_Appliance_Cert": "Successfully regenerated selfSigned certificate.",
    "CRL_NOT_FOUND_Resolution": "Locate any server certificate issued by this CA. Find the CRL distribution point from the certificate.\nDownload the CRL file from the URL. Upload the file to the appliance.",
    "Untrusted_Resolution": "Add the certificate and retry the operation. To add the missing certificate you can use import certificate option under Settings -> Security -> Manage certificates.",
    "Revoked_for_intermediate_CA": "CA certificate with alias name intermediateca is revoked",
    "Revoked_Resolution": "Delete the revoked certificate from the appliance, regenerate a new certificate and add the new certificate to the appliance with the same alias name.",
    "Create_csr_Name": "Create certificate signing request",
    "Create_csr_statusUpdate": "The certificate signing request is created successfully.",
    "Import_casinged_appliancecert_Name": "Certificate Import Signed Configuration.",
    "Import_casinged_appliancecert": "Successfully imported appliance signed certificate(s).",
    "Create_rabbitmq_client_cert": "RabbitMQ client certificate generation",
    "Create_rabbitmq_client_cert_details": "Successfully created client certificate."}

CA_cert_error = 'Unable to retrieve the input certificate. No matching certificate found for the specified alias.'

leaf_cert_error = 'Not Found'

alert_uri = '/rest/alerts?filter="alertState EQ \'Locked\'"&filter="healthCategory EQ \'Certificate Management\'"'

appliance_cert_csr_body = {"type": APPLIANCE_CSR_TYPE,
                           "country": "US",
                           "state": "California",
                           "locality": "Palo Alto",
                           "organization": "Hewlett Packard Enterprise",
                           "commonName": "",
                           "organizationalUnit": "",
                           "alternativeName": "",
                           "contactPerson": "",
                           "email": "",
                           "surname": "",
                           "givenName": "",
                           "initials": "",
                           "dnQualifier": "",
                           "unstructuredName": "",
                           "challengePassword": "",
                           "cnsaCertRequested": False}

ca_signed_appliance_cert = {
    "base64Data": "",
    "type": "CertificateDtoV3"
}

server_alerts = {"part1": "WebServer certificate with alias name ",
                 "part2": "Rabbitmq server certificate with alias name ",
                 "part3": " is revoked",
                 "part4": " is not trusted"}

curl_commands = ['curl -v -i -X Get -H "X-Api-Version:',
                 '" -H "Auth:',
                 '" https://',
                 '/rest/certificates/status']

destination_path = '/root/automation_tools/OVF664_auto/appliance_cert'
CSR_path = '/root/OVF2422/certtool'
CA_signed_CSR_path = '/root/OVF2422/certtool/signed_certificate'
revoke_path = '/root/automation_tools/OVF664_auto/revoke_appliance_cert'
applns_revoke_path = '/root/OVF2422/certtool/crls_ca'

generate_appliance_cert_commands = {'part1': '%s/change_appliance_configuration.sh' % destination_path,
                                    'part2': '%s/appliance.csr' % destination_path,
                                    'part3': '%s/generate_revoke_appliance_cert.sh' % destination_path,
                                    'part4': 'cat %s/ca.crt' % destination_path,
                                    'part5': 'cat %s/Inter_1.crt' % destination_path,
                                    'part6': 'cat %s/server_client.cer' % CA_signed_CSR_path,
                                    'part7': '%s/crlFile-ca.crl' % revoke_path,
                                    'part8': 'cd %s; python clean.py' % CSR_path,
                                    'part9': '%s/localhostcsr.req' % CSR_path,
                                    'part10': 'cat %s/ca.cer' % CA_signed_CSR_path,
                                    'part11': 'cd %s; python CA_sign_appliance.py' % CSR_path,
                                    'part12': 'cat %s/CA.cer' % revoke_path,
                                    'part13': 'cat %s/inter-1.cer' % revoke_path,
                                    'part14': '%s/crlFile-ca.crl' % applns_revoke_path,
                                    'part15': '/ci/bin/gen-certificate-status.sh'}
