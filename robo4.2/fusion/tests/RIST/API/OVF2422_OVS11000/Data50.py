admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

filename = "crlFile-ca.crl"

DefaultConfig = {
    "type": "CertValidationConfig",
    "certValidationConfig": {
        "global.enforceStrictTrust": True,
        "global.validateCertificate": True,
        "global.allow.invalidCRL": True,
        "global.checkCertificateRevocation": True,
        "global.allow.noCRL": True,
        "global.disableAlertForCRL": True,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.enableHostNameVerification": True
    },
    "okToReboot": "true"
}

ConfigurationP02 = {
    "type": "CertValidationConfig",
    "certValidationConfig": {
        "global.enforceStrictTrust": True,
        "global.validateCertificate": False,
        "global.allow.invalidCRL": True,
        "global.checkCertificateRevocation": True,
        "global.allow.noCRL": True,
        "global.disableAlertForCRL": True,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.enableHostNameVerification": True
    },
    "okToReboot": "true"
}

ConfigurationP06 = {
    "type": "CertValidationConfig",
    "certValidationConfig": {
        "global.enforceStrictTrust": True,
        "global.validateCertificate": True,
        "global.allow.invalidCRL": True,
        "global.checkCertificateRevocation": True,
        "global.allow.noCRL": True,
        "global.disableAlertForCRL": True,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.enableHostNameVerification": True
    },
    "okToReboot": "true"
}

ConfigurationP07 = {
    "type": "CertValidationConfig",
    "certValidationConfig": {
        "global.enforceStrictTrust": True,
        "global.validateCertificate": True,
        "global.allow.invalidCRL": True,
        "global.checkCertificateRevocation": False,
        "global.allow.noCRL": True,
        "global.disableAlertForCRL": False,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.enableHostNameVerification": True
    },
    "okToReboot": "true"
}

ConfigurationP10 = {
    "type": "CertValidationConfig",
    "certValidationConfig": {
        "global.enforceStrictTrust": True,
        "global.validateCertificate": True,
        "global.allow.invalidCRL": True,
        "global.checkCertificateRevocation": False,
        "global.allow.noCRL": True,
        "global.disableAlertForCRL": False,
        "global.enableExpiryCheckForSelfSignedLeafAtConnect": False,
        "global.enableHostNameVerification": True
    },
    "okToReboot": "true"
}

ExpiredCert = [{
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIEFDCCAvygAwIBAgIBATANBgkqhkiG9w0BAQsFADBlMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTESMBAGA1UEBxMJUGFsbyBBbHRvMRgwFgYDVQQKEw9IZXdsZXR0LVBhY2thcmQxEzARBgNVBAMTCkhQRVJvb3RDQTEwHhcNMTYwODAxMDUyNTA3WhcNMTYwODAyMDUyNTA3WjBiMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTESMBAGA1UEBxMJUGFsbyBBbHRvMRgwFgYDVQQKEw9IZXdsZXR0LVBhY2thcmQxEDAOBgNVBAMTB0ludGVyLTEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDZzoh+qOEfyZH30w6k6FoWfDQ4dd6L+eWP7xkkqJxBnAPjHE95qf1snf2C0DGNVYpJM6xTmSzhp/iX1g22BTRJdSs+H/JYQZrG56f7FaEufJvrf+bE8lFUhPc16yeHwx/XYTjUtyt7IT1wz8qvXuD7f+Jr/tGtoh1TknFCgsDNEkJH10jHrym/mJhI1veTZKyt03olwDstxUH15pzVcy3RexvcKpQjbKEovJr9j8S/vdFBNH89rsno2iw+Xd2DseDnhkmvP7ErOgsgXoV3BhGa9Z+2UOdpzi/TQcRGbjUrxsTxplWS0MqITwlwzLLGJm4Yn011lH9DbqE1G/5gg1BdAgMBAAGjgdEwgc4wHQYDVR0OBBYEFG6dthKd0BqvzP50Y10h19I9qsBLMB8GA1UdIwQYMBaAFNzl41p4QbAYSUxMlj+X8J8uS5LoMBIGA1UdEwEB/wQIMAYBAf8CAQMwDgYDVR0PAQH/BAQDAgGGMCwGA1UdHwQlMCMwIaAfoB2GG2h0dHA6Ly8xOTIuMTY4LjIuMTEwL2NhLmNybDA6BggrBgEFBQcBAQQuMCwwKgYIKwYBBQUHMAGGHmh0dHA6Ly8xNS4xNTQuMTAwLjQ1OjI1NjAvb2NzcDANBgkqhkiG9w0BAQsFAAOCAQEAZ6eCQkasBtUtEEDHiV2co+VW7jtNI3lXdwv1ZL2fjhMO58WGhPVRszCClTv9pq6L1qswVpaA4LQNsDb8R9L4g/Id2AsbL/I0ByTcr9POiAW1pEyeemUvH4EfepJVxTIOL9s+gEvQrIdf+TI6uf8TGDLdB11QhGpoL644U6fyO18hDm4EmRJaxrrmZ/gp1yHUJbmD0TOXZ9Z19RTtq60OqG28ErN7Gau3f5/4tK+HRGV2TkTIkerBdzFINbp+baDKFN+f095THgeMsyInWKZX30NODegc75oxENHdLQc5eM3O6CkGmduwVL3uaN6Z8EWRttUGFIw24HzSfG1D8VJGxg==\n-----END CERTIFICATE-----",
            "aliasName": "root CA 1",
            "type": "CertificateDetailV2"
        }
    }],
    "type": "CertificateAuthorityInfoCollection"
}]

IntermediateCert = [{
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFEzCCA3ugAwIBAgICZ0gwDQYJKoZIhvcNAQEMBQAwZzELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRUwEwYDVQQDDAxIUEVfIGludGVyLTIwIBcNMTcxMjExMDk1MzM5WhgPMjExNzExMTcwOTUzMzlaMGcxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEVMBMGA1UEAwwMSFBFXyBpbnRlci0zMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAz608mf0FQWWEXSY6iyeXrZdOYvtpwgIt+IK75XuJw9+CvcncaZ1IHMHkVslDfZ3gFKatE314ivNRU54yE4sMAZ4ZOSlHcI1WqqqIGkbkPohAI7HdVrzY3WFGFbLPCAoPo74DKaJEcEYoNbsY1Bfd9IQwCRgG3LI+yHuW8xlzeuDIOOm4x2qtXcmsRCFcrM2vHi10tboABLIBWO1ryY8efSv2/+X/VYpOHEkoLPV8W4SNsoNJIWje3JKU6XutGoU5GH7U6Rqok4KFvVgAM9ODwyTyAKhn59h5alQ6JUnqDmcTWO/IVXGr0EDQZNWjcb3SvKv6cWzbyDoxJqTgZ+2Y0iNncH3ksO5mEiccGJeEIIevA4aJJ2hpOxN/Bto3GaLJ8nK0h1tm6GckJa+zTJrRxIGkL7b1deOZkBhVfmm2Ww7C+LnXv0TXFFpECFQ56uCWvw76+BSPYizUW2gCrioU/cPzM6kvyG8JF9dvFFrYnWT276efcJ+y67DJdV3kCF83AgMBAAGjgcYwgcMwHQYDVR0OBBYEFOJXKeqXuySlKGdAWZW+/NxBBzqOMB8GA1UdIwQYMBaAFHwpwd7ZKaLCs5ucP6VYL5eDxZIEMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3QvY2EuY3JsMDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBAJtYnv6/SmIqy3q4x5WFu/0bvLgLZ+Y0HLP53T3hdbgQJKWtuTs2OFX0LFAAQrDZkoC5262ft8Mw1sKLS34R6mVN0AZbblmQS0KGInw3M0RBe4TB3u2eSvaqBMXcWNNBCqsCerxv9e+HRBTjAkUUB2cEvhEHpuB0b5rVkXQgXPfaic2WTTCmsMY5pVYFF61kd0dwfYgpLJTo24r5gzo3ujYOatjfH9gnzyS7+92IFd+5VlKxHqdMAJsGrRiFjJIKdanFCioYQX7GOvtqYp5oXSVIRU6Ai5lSWgpzHeqjOaz5lGEe03puGJr8mw59gNvl+ur3YLupJcaOst7CAo+6Cz48IQB9a/pgkCy5Eg0u2g24PyfQ2uhWpYVabKJHThji/558vU/h8wDi3rcVE5zqtqnG6vAqOLAtAUXr5iKhD4XpXBNtMo+78DZM8r9L5vJ6KnW72TrBFQBdx0pQ+kLuGHbO3GeaCdote0dVIheR8hwOdtS2fVxqgCmc0+4AebFO2Q==\n-----END CERTIFICATE-----",
            "aliasName": "root CA 1",
            "type": "CertificateDetailV2"
        }
    }],
    "type": "CertificateAuthorityInfoCollection"
}]

RootCA = [{
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFXjCCA8agAwIBAgIJAKPLacrOGmdUMA0GCSqGSIb3DQEBDAUAMGQxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDESMBAGA1UEAwwJSFBFXyBSb290MCAXDTE3MTIxMTEwMDA0M1oYDzIxMTcxMTE3MTAwMDQzWjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBANSvTzRRvYAWbNN+nq1YAbTD/fUOKLkCGMICmLrWt+4KiTn8VqBT/1nRJA78NI5p0zuMeTHLlkc9IkY30gbiZT5KBJPIwb+umVxUXp8/IgBSwCL/vH64fe7LFoNfBH17F70+YzilONHEsMPs78J+9OMPrdHTJitiZ0yyRjyswWT0wo++5SJPY1gBcjzUWKfMvUz6Jy/RZ1Z1JQ6tABEjC7SWDmTej+wUKBRtm5nrdMhNkPl/2ngeEkWlA4qE2zZPg2i8E9ZzthC8T4ZJRxGz3iG4b6GdOLVeSLWHXs2zh66zHatk7M/mSZbZwjDJcjTRN1ZeDHJt0Zw2iKRHdnJjJyOzUSIvDPYMTp/SZiTKr7qBrW6dHUW3O9dMUrRgIqpRFtKmIMtFCHb/1WfmxytIIoSjfAPR3oSKOEVTh4GhdadSfEAlh0+Wz4u0SsQW+CZ5WYNgFzpDsFeOPoQidOW/bajBfbag1Zsj7uGEVsi6Azto8jaFOGQwlsSpqxd3Fp8oiQIDAQABo4IBDzCCAQswHQYDVR0OBBYEFHBNNshl72UD7D+Wdf5o7U+8HHsaMIGWBgNVHSMEgY4wgYuAFHBNNshl72UD7D+Wdf5o7U+8HHsaoWikZjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdIIJAKPLacrOGmdUMAsGA1UdDwQEAwIBtjAMBgNVHRMEBTADAQH/MDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBALE0qbKz/jIp3LJTbe1ejnpdK7aBYQJUv0D33Vj2YOOJJ1QTs1uxCQPlGh3WIlUta45yPAc/3IMgIIP/6nzmKEPEaayY+OwHfQa83sLDkd3/TIXN09nIklVqN9GPrSiEjd9L63bG116xxl4q6YIvBPf+OLWfcPtls5ZCE7ZUSQn1ScZqy4xddowlnTW8u50r2AFzwmInQIAKGmE5co1e+RIx98+mYJFrx53B952RMkWnPjJwpQsLBxvHjjPq93KPE7uw3Ln3HZb9Wbn/TuedzgfZh3DoTw6VGxkVfgCe2SU8NwngblRhujrzRJwsO3/Xq9jh12LEnqHZBRL4nNOISA28NmfPud/KhGHi1BBnlwJgKqkRbJbhrUsQymnj5ndLsnuMLv0Og/lwc/beWDcAOcZb1gTLzWwbAaWMN0OFURTXkGQKZi8Aa8qcrt+UqzswAXYYV7puKXwOzKSEOXfRDiB3FwoSIna4q1DZGvTD/aNYPmAPyB5zCa2q51zDJ+nGfA==\n-----END CERTIFICATE-----",
            "aliasName": "shqa-WIN-D1VNB3UQSP2-CA",
            "type": "CertificateDetailV2"
        }
    }],
    "type": "CertificateAuthorityInfoCollection"
}]

SubCA = [{
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFEDCCA3igAwIBAgICN/wwDQYJKoZIhvcNAQEMBQAwZDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRIwEAYDVQQDDAlIUEVfIFJvb3QwIBcNMTcxMjExMTAwMDQ3WhgPMjExNzExMTcxMDAwNDdaMGcxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEVMBMGA1UEAwwMSFBFXyBpbnRlci0xMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA17efte/bG7Pc6uexyB4SY9gicGa3Sl3auex/EARuyOfa7awYfmZAZ0FgPD5KZxIHMuxv67djoXqOnAzmvbEM0P+2eWotFZWIIcFXGKgWvuNOsaEcgRWslqCzLx29UJGD507VbqWgiTS6z16g7gsvClurgqDy7V7PSyzNkQTA+skbD8nXz9cy0ADv2+QaUawLjyjEgDGvftMIk1gqhG9JRA7SCtnzk+pgjMtpjS368+u3ldjUYNWv6H4/+mgXYGrebl/s+pKJ/EApZzYbG1p5aJPzvwG2gMrGB+lHP2WOfWimgG8S4nhc3+ZkQtAVDu4tXCsrC6UDO7jT5GQsc1vZlw9geN2oKZgIt7K/WA4n8wKmHLO2rvWNuFWtdbFCBdQoFfMajcgquwl19C/0vLOcFQgRpgxK3Lsv1p+r+oyf1RzQ4Zz+5zxgM1IrG5PXp5+TgEa7zA4ClPrM0LO+x472cl21Oqi+QZtePwJAC0Ll6Ut57mHpj+h5o6SRsoBzWq8TAgMBAAGjgcYwgcMwHQYDVR0OBBYEFJvYMaKmiA0dWokYc4SKF96U47GFMB8GA1UdIwQYMBaAFHBNNshl72UD7D+Wdf5o7U+8HHsaMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3QvY2EuY3JsMDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBAJGg1s07VJArPLe0Ms8ljDapdTuQx5gSSBxbTh+n+RvYUCIa/om8tx/0XwOOWWWpviHJ14kOKJ1NKOV6r/pf4O1S+QpXbJN8YS/6YMbryWxdvEdl55UcLSNYX5N+gYDTqChZALO6rzMAxHAN5fvlludeCecbaM65WN/p4sDPoFa5of2I1jLV4GMqqHsAQzfjauh0IQogtLBNNh7GWwXeIU4lWPg8xiVurRnFbIF4TZxKJoYTzlNyxhK1Psray5+gKMLRZZ2fUXMVWyU3n/Z03ufKbr/a9hoiRrF6TyfLjOinxmSdBgoCvldBk6xrqLwNg/kToJKAxuBNfIAvlwZstAIz26QeBQwZbbFNszs7hS0movN1nFS5WMKj1QDjhBJhO2Aia31uw5tY9Wjysh6DMT6skIF0kFMzSEMUUZF5Gdpf/ak4BAcahXaNeBFuB6bfJh1JFsJYoI+jaJfOwJJyc7+LS2vDZJ6ZDVsnaqGSY6LHcgmz8GRRtXT5d0OL9+N7Gg==\n-----END CERTIFICATE-----",
            "aliasName": "inter 1",
            "type": "CertificateDetailV2"
        }
    }],
    "type": "CertificateAuthorityInfoCollection"
}]

RevocationCerts = [
    {
        "members": [{
            "type": "CertificateAuthorityInfo",
            "certificateDetails": {
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFXjCCA8agAwIBAgIJAKPLacrOGmdUMA0GCSqGSIb3DQEBDAUAMGQxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDESMBAGA1UEAwwJSFBFXyBSb290MCAXDTE3MTIxMTEwMDA0M1oYDzIxMTcxMTE3MTAwMDQzWjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBANSvTzRRvYAWbNN+nq1YAbTD/fUOKLkCGMICmLrWt+4KiTn8VqBT/1nRJA78NI5p0zuMeTHLlkc9IkY30gbiZT5KBJPIwb+umVxUXp8/IgBSwCL/vH64fe7LFoNfBH17F70+YzilONHEsMPs78J+9OMPrdHTJitiZ0yyRjyswWT0wo++5SJPY1gBcjzUWKfMvUz6Jy/RZ1Z1JQ6tABEjC7SWDmTej+wUKBRtm5nrdMhNkPl/2ngeEkWlA4qE2zZPg2i8E9ZzthC8T4ZJRxGz3iG4b6GdOLVeSLWHXs2zh66zHatk7M/mSZbZwjDJcjTRN1ZeDHJt0Zw2iKRHdnJjJyOzUSIvDPYMTp/SZiTKr7qBrW6dHUW3O9dMUrRgIqpRFtKmIMtFCHb/1WfmxytIIoSjfAPR3oSKOEVTh4GhdadSfEAlh0+Wz4u0SsQW+CZ5WYNgFzpDsFeOPoQidOW/bajBfbag1Zsj7uGEVsi6Azto8jaFOGQwlsSpqxd3Fp8oiQIDAQABo4IBDzCCAQswHQYDVR0OBBYEFHBNNshl72UD7D+Wdf5o7U+8HHsaMIGWBgNVHSMEgY4wgYuAFHBNNshl72UD7D+Wdf5o7U+8HHsaoWikZjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdIIJAKPLacrOGmdUMAsGA1UdDwQEAwIBtjAMBgNVHRMEBTADAQH/MDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBALE0qbKz/jIp3LJTbe1ejnpdK7aBYQJUv0D33Vj2YOOJJ1QTs1uxCQPlGh3WIlUta45yPAc/3IMgIIP/6nzmKEPEaayY+OwHfQa83sLDkd3/TIXN09nIklVqN9GPrSiEjd9L63bG116xxl4q6YIvBPf+OLWfcPtls5ZCE7ZUSQn1ScZqy4xddowlnTW8u50r2AFzwmInQIAKGmE5co1e+RIx98+mYJFrx53B952RMkWnPjJwpQsLBxvHjjPq93KPE7uw3Ln3HZb9Wbn/TuedzgfZh3DoTw6VGxkVfgCe2SU8NwngblRhujrzRJwsO3/Xq9jh12LEnqHZBRL4nNOISA28NmfPud/KhGHi1BBnlwJgKqkRbJbhrUsQymnj5ndLsnuMLv0Og/lwc/beWDcAOcZb1gTLzWwbAaWMN0OFURTXkGQKZi8Aa8qcrt+UqzswAXYYV7puKXwOzKSEOXfRDiB3FwoSIna4q1DZGvTD/aNYPmAPyB5zCa2q51zDJ+nGfA==\n-----END CERTIFICATE-----",
                "aliasName": "shqa-WIN-D1VNB3UQSP2-CA",
                "type": "CertificateDetailV2"
            }
        }],
        "type": "CertificateAuthorityInfoCollection"
    },
    {
        "members": [
            {
                "type": "CertificateAuthorityInfo",
                "certificateDetails": {
                    "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFEDCCA3igAwIBAgICN/wwDQYJKoZIhvcNAQEMBQAwZDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRIwEAYDVQQDDAlIUEVfIFJvb3QwIBcNMTcxMjExMTAwMDQ3WhgPMjExNzExMTcxMDAwNDdaMGcxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEVMBMGA1UEAwwMSFBFXyBpbnRlci0xMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA17efte/bG7Pc6uexyB4SY9gicGa3Sl3auex/EARuyOfa7awYfmZAZ0FgPD5KZxIHMuxv67djoXqOnAzmvbEM0P+2eWotFZWIIcFXGKgWvuNOsaEcgRWslqCzLx29UJGD507VbqWgiTS6z16g7gsvClurgqDy7V7PSyzNkQTA+skbD8nXz9cy0ADv2+QaUawLjyjEgDGvftMIk1gqhG9JRA7SCtnzk+pgjMtpjS368+u3ldjUYNWv6H4/+mgXYGrebl/s+pKJ/EApZzYbG1p5aJPzvwG2gMrGB+lHP2WOfWimgG8S4nhc3+ZkQtAVDu4tXCsrC6UDO7jT5GQsc1vZlw9geN2oKZgIt7K/WA4n8wKmHLO2rvWNuFWtdbFCBdQoFfMajcgquwl19C/0vLOcFQgRpgxK3Lsv1p+r+oyf1RzQ4Zz+5zxgM1IrG5PXp5+TgEa7zA4ClPrM0LO+x472cl21Oqi+QZtePwJAC0Ll6Ut57mHpj+h5o6SRsoBzWq8TAgMBAAGjgcYwgcMwHQYDVR0OBBYEFJvYMaKmiA0dWokYc4SKF96U47GFMB8GA1UdIwQYMBaAFHBNNshl72UD7D+Wdf5o7U+8HHsaMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3QvY2EuY3JsMDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBAJGg1s07VJArPLe0Ms8ljDapdTuQx5gSSBxbTh+n+RvYUCIa/om8tx/0XwOOWWWpviHJ14kOKJ1NKOV6r/pf4O1S+QpXbJN8YS/6YMbryWxdvEdl55UcLSNYX5N+gYDTqChZALO6rzMAxHAN5fvlludeCecbaM65WN/p4sDPoFa5of2I1jLV4GMqqHsAQzfjauh0IQogtLBNNh7GWwXeIU4lWPg8xiVurRnFbIF4TZxKJoYTzlNyxhK1Psray5+gKMLRZZ2fUXMVWyU3n/Z03ufKbr/a9hoiRrF6TyfLjOinxmSdBgoCvldBk6xrqLwNg/kToJKAxuBNfIAvlwZstAIz26QeBQwZbbFNszs7hS0movN1nFS5WMKj1QDjhBJhO2Aia31uw5tY9Wjysh6DMT6skIF0kFMzSEMUUZF5Gdpf/ak4BAcahXaNeBFuB6bfJh1JFsJYoI+jaJfOwJJyc7+LS2vDZJ6ZDVsnaqGSY6LHcgmz8GRRtXT5d0OL9+N7Gg==\n-----END CERTIFICATE-----",
                    "aliasName": "inter 1",
                    "type": "CertificateDetailV2"
                }
            }
        ],
        "type": "CertificateAuthorityInfoCollection"
    }
]
