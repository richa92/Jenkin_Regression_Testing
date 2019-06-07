admin_cred = {
    'userName': 'administrator',
    'password': 'wpsthpvse1',
    'authLoginDomain': 'LOCAL'}

remote_server_IP = '15.114.112.61'

ssh_cred = {'username': 'root', 'password': 'hpvse1'}

rabbitmq_client_cert_body = {"commonName": "default", "type": "RabbitMqClientCertV2"}

cmd = 'cat /ci/data/security/certs/rabbitmq-server.crt'

internal_rabbitmq_server_cert_issuer = 'Issuer: C=US, ST=California, L=Palo Alto, O=Hewlett Packard Enterprise, CN=Infrastructure Management Certificate Authority'

incorrect_rootca = '-----BEGIN CERTIFICATE-----\nMIID+zCCAuOgAwIBAgIJAK5CpL7LomO9MA0GCSqGSIb3DQEBCwUAMIGVMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRv\nMSMwIQYDVQQKDBpIZXdsZXR0IFBhY2thcmQgRW50ZXJwcmlzZTE4MDYGA1UEAwwv\nSW5mcmFzdHJ1Y3R1cmUgTWFuYWdlbWVudCBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkw\nHhcNMTcxMjIwMDcyOTAwWhcNMjcxMjIxMDcyOTAwWjCBlTELMAkGA1UEBhMCVVMx\nEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEjMCEGA1UE\nCgwaSGV3bGV0dCBQYWNrYXJkIEVudGVycHJpc2UxODA2BgNVBAMML0luZnJhc3Ry\ndWN0dXJlIE1hbmFnZW1lbnQgQ2VydGlmaWNhdGUgQXV0aG9yaXR5MIIBIjANBgkq\nhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2wlSSxKLVfK/+3JGDEVk153hAqsHxwYu\nEH8UcymffaJNiThGaCMp2zAnEkHXM6LRLIGeysOl0Syn08GNnfb6iKd9x+2iL1kJ\n7TdfFpmXMi6g7fj3JLlq6OW7kRAuTbRcoNTXkFMJlq8BsFA45ZR55c5ItrVoCapQ\nPx+XV8ae23H9uUrR2BeeN72vgVkFU7Ylma1V0KEw7/rXbTlga5GIX9RlLdA10SIa\nYDV6O6A3duCxEKpFThKZ3FUlwjtv9AUh7dNMdduCmarehJXt3Exf8SFj2NFASSkm\nFyP8/d744gQwW+bjcxVbasZar3ah32FF0Tted03Dr9Nf4bWoiI+SJwIDAQABo0ww\nSjA6BgNVHREEMzAxgi9JbmZyYXN0cnVjdHVyZSBNYW5hZ2VtZW50IENlcnRpZmlj\nYXRlIEF1dGhvcml0eTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBK\nAm+VTAVGnYBOH9NYiSzae7rPmn8mldL8O+R+7baWTufi/KnRV33sS2v9dPerD2qX\ntXDBBKDtGUukmaXLR1v0Tr305OZmtnqe9edEfV/JNmYWun7j+2msHSmp7KHqZ97i\nKQQZ4KNQOz0CJsJ29gO/C4FxwpcK1HXDvVhL13gsEdkRXW2XrUjfbE7/MLrrqEWL\nXHsFdHXMMfzVqtn+vf2NDpDyGmRjNEPvyK+Yja9klJB8pZIdj4q53NBfwh6zqE1K\nhFEc1AbLcVTSk79DXpu1BU/iUWtt1Rz69giW10qganVCLEIPLomzsmGC/wlW7T1c\ngT6ldOwCXC4iwOqxSyuS\n-----END CERTIFICATE-----'

ca_cert_body = {
    "members": [
        {"certificateDetails": {
            "aliasName": "",
            "base64Data": "",
            "type": "CertificateDetailV2"},
         "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

leaf_cert_body = {
    "certificateDetails": [
        {
            "aliasName": "",
            "base64Data": "",
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

appliance_cert_csr_body = {"type": "CertificateSigningRequest",
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
                           "cnsaCertRequested": True}

ca_signed_appliance_cert = {
    "base64Data": "",
    "type": "CertificateDtoV3"
}

destination_path1 = '/root/automation_tools/OVF664_auto/cert_tool'

destination_path2 = '/root/automation_tools/OVF664_auto/sctest'

rabbitmq_client_cert_path = '/root/automation_tools/OVF664_auto/rabbitmq_certs'

linux_commands = {'part1': '%s/change_cert_days.sh 58 4' % destination_path1,
                  'part2': '%s/appliance.req' % destination_path1,
                  'part3': '%s/generate_revoke_appliance_cert_beibei.sh 2 3072 rsa sha384 1' % destination_path1,
                  'part4': 'cat %s/chain_certs/ca.cer rootca.cer' % destination_path1,
                  'part5': 'cat %s/chain_certs/inter-1.cer' % destination_path1,
                  'part6': 'cat %s/signed_certificate/server_client.cer' % destination_path1,
                  'part7': 'cat %s/chain_certs/concatenated.cer' % destination_path1,
                  'part8': '%s/clean_beibei.sh' % destination_path1,
                  'part9': 'cat %s/rabbitmq_client.cer' % rabbitmq_client_cert_path,
                  'part10': 'cat %s/rabbitmq_client.key' % rabbitmq_client_cert_path,
                  'part11': 'cat %s/ca.cer' % rabbitmq_client_cert_path,
                  'part12': 'cat %s/correct_chain_without_root_ca.cer' % rabbitmq_client_cert_path,
                  'part13': 'cat %s/incorrect_chain_without_root_ca.cer' % rabbitmq_client_cert_path,
                  'part14': 'cat %s/error_client_name.cer' % rabbitmq_client_cert_path,
                  'part15': '%s/ca.crl' % rabbitmq_client_cert_path}

disable_certificate_revocation_checking = {
    "type": "CertValidationConfig",
    "okToReboot": True,
    "certValidationConfig":
        {"global.validateCertificate": True,
         "global.checkCertificateRevocation": False,
         "global.allow.invalidCRL": True,
         "global.allow.noCRL": True,
         "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
         "global.disableAlertForCRL": True}
}

enable_certificate_revocation_checking = {
    "type": "CertValidationConfig",
    "okToReboot": True,
    "certValidationConfig": {
        "global.enforceStrictTrust": True,
        "global.disableAlertForCRL": True,
        "global.checkCertificateRevocation": True,
        "global.enableHostNameVerification": True,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.validateCertificate": True,
        "global.allow.noCRL": True,
        "global.allow.invalidCRL": True
    }
}

errorMessages_for_changed_rabbitmq_certs = ['Fail to regenerate new internal ca signed rabbitmq client cert',
                                            'Fail to regenerate new internal ca signed rabbitmq client cert key',
                                            'Fail to regenerate new internal root ca cert',
                                            'Fail to regenerate new internal ca signed rabbitmq server cert'
                                            ]
