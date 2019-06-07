ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

SSH_SERVER = "16.114.210.117"
SSH_USERNAME = "root"
SSH_PASSWD = "hpvse1"
ROOT_DIR = "/root/automation_tools/fipsovs1860"
SETUP_SH = "ovs1860_setup.sh"
CLEANUP_SH = "ovs1860_cleanup.sh"

ca_cert_body = {
    "members": [
        {"certificateDetails": {
            "aliasName": "testca1",
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIEczCCA1ugAwIBAgIJAPaPd1RPrjyjMA0GCSqGSIb3DQEBCwUAMGsxCzAJBgNV\nBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRIwEAYDVQQHEwlQYWxvIEFsdG8x\nGDAWBgNVBAoTD0hld2xldHQtUGFja2FyZDEZMBcGA1UEAxMQSFAgVGVzdEhlYWQg\nUm9vdDAgFw0xODEyMDcwNTA1MDhaGA8yMTE4MTExMzA1MDUwOFowazELMAkGA1UE\nBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExEjAQBgNVBAcTCVBhbG8gQWx0bzEY\nMBYGA1UEChMPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDExBIUCBUZXN0SGVhZCBS\nb290MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwaSAk/7rAMtRw464\n3bLgLcnUf7uKRulcGIrv0M9a6iVoMmLtyewyNgFAC41R95vZ5abEK/CIQ5SB7BdK\nsQ0ywYERpd8ql9Tb2nQ/b08wUET7abjo+MssvTMFne6gYiydIp+7XM1uRmnIUNea\nhVf7ZnyF5g9ZqBD3kWYtxJAxvy03IbVGwtILqSY3uNzFwKn1XBdXO57itEuUrRKH\nDASAYHyxZopbga+dx+Vi5lkCZ0LX2IBNQP8xoHyOO/4idttHuJmVo/OjIHVDR236\n2d2SdVXx74Vb/UZsKJ4FtMDYrOJeufcA/TyOha7ETdzqjunfxDb98pTIykdjSCED\nMgF7DQIDAQABo4IBFjCCARIwHQYDVR0OBBYEFFqnSt0wx27rCaFGtT5opDv8nUmC\nMIGdBgNVHSMEgZUwgZKAFFqnSt0wx27rCaFGtT5opDv8nUmCoW+kbTBrMQswCQYD\nVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTESMBAGA1UEBxMJUGFsbyBBbHRv\nMRgwFgYDVQQKEw9IZXdsZXR0LVBhY2thcmQxGTAXBgNVBAMTEEhQIFRlc3RIZWFk\nIFJvb3SCCQD2j3dUT648ozALBgNVHQ8EBAMCAbYwDAYDVR0TBAUwAwEB/zA2Bggr\nBgEFBQcBAQQqMCgwJgYIKwYBBQUHMAGGGmh0dHA6Ly9sb2NhbGhvc3Q6MjU2MC9v\nY3NwMA0GCSqGSIb3DQEBCwUAA4IBAQA1JGg5yTbKlSV9nys9gMJLARLMxq8zP+Jy\nET/uD8YuQXSMP+zvhxgH1k67kfOTMmnn4n6Tnsn9fT/i58KjjsjDA/yatzLwo/CD\nqUIE0WzW/mIELtOb1wMLatusD0PlojxC4MoOSMe735JnPL6/3b9/7Y2eOanLi+pJ\n6fDdeZubFvvJ7ivNMEo49rV4QxGxin8Z9z9ae+hWxMUnwZKlFd2e9nCkz2N/8FbP\nG047RO+Gy31K5KyC4cwwYTVXjEbC85E1VSMHF0D4AkhAphl5SF4kJ56rrSSQM0f9\nL78nIAFqLcr6CyHyn1s34g6HelG9sbUdqVbU81RCM5q2DEtr8DOA\n-----END CERTIFICATE-----",
            "type": "CertificateDetailV2"},
         "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

RESULT_DIR = "/tmp/ovs1860"
FOLDER = "OVF2072_OVS1860"
CA1_ALIASNAME = "testca1"
CA2_ALIASNAME = "testca2"
CA1_ORIG_DER_CRL_FILE = "origderca1.crl"
CA1_ORIG_PEM_CRL_FILE = "origpemca1.crl"
CA1_NEW_DER_CRL_FILE = "newderca1.crl"
CA1_NEW_PEM_CRL_FILE = "newpemca1.crl"
CA1_MAL_CRL_FILE = "malca1.crl"
CA2_ORIG_DER_CRL_FILE = "origderca2.crl"
CA2_ORIG_PEM_CRL_FILE = "origpemca2.crl"
CA2_NEW_DER_CRL_FILE = "newderca2.crl"
CA2_NEW_PEM_CRL_FILE = "newpemca2.crl"

generate_appliance_cert_commands = {'part1': '{0}/{1}'.format(RESULT_DIR, CA1_ORIG_PEM_CRL_FILE),
                                    'part2': '{0}/{1}'.format(RESULT_DIR, CA1_NEW_DER_CRL_FILE),
                                    'part3': '{0}/{1}'.format(RESULT_DIR, CA1_NEW_PEM_CRL_FILE),
                                    'part4': '{0}/{1}'.format(RESULT_DIR, CA1_MAL_CRL_FILE),
                                    'part5': '{0}/{1}'.format(RESULT_DIR, CA2_ORIG_DER_CRL_FILE),
                                    'part6': '{0}/{1}'.format(RESULT_DIR, CA2_NEW_DER_CRL_FILE)}

ERR_MSG_WRONG_DETIAL = "CRL is not in valid X509 format."
ERR_MSG_WRONG_RECOMMAND = "Provide a valid X509 CRL and try again."
ERR_MSG_SIGNED_DETIAL = "Uploaded CRL is not signed by the specified CA."
ERR_MSG_SIGNED_RECOMMAND = "Supply CRL signed by the specified CA."
ERR_MSG_DUPLICATE_DETIAL = "Same CRL already exists on the appliance"
ERR_MSG_DUPLICATE_RECOMMAND = "Provide a different CRL."
ERR_MSG_OLDER_DETIAL = "newer CRL exists on the appliance."
ERR_MSG_OLDER_RECOMMAND = "Provide a newer CRL."
