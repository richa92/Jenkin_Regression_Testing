
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

WEB_PROXY = [
    {"type": "ProxyServerV2",
     "server": "16.114.220.207",
     "port": "443",
     "username": None,
     "password": None,
     "credUri": None,
     "communicationProtocol": "HTTPS"}
]

NO_WEB_PROXY = {"type": "ProxyServerV2",
                "server": None,
                "port": 0,
                "username": None,
                "password": None,
                "credUri": None,
                "communicationProtocol": "HTTPS"}

WEB_PROXY_ALIAS_NAME = "vse.rdlabs.hpecorp.net"

WEB_PROXY_CA_CERT = {
    "type": "CertificateAuthorityInfo",
    "certificateDetails": {
        "type": "CertificateDetailV2",
        "version": "3",
        "serialNumber": "f7:44:3c:e0:a4:46:1f:85",
        "base64Data": "-----BEGIN CERTIFICATE-----\nMIIEOTCCAyGgAwIBAgIJAPdEPOCkRh+FMA0GCSqGSIb3DQEBCwUAMGsxCzAJBgNV\nBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8x\nGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEZMBcGA1UEAwwQSFAgVGVzdEhlYWQg\nUm9vdDAgFw0xNzA3MTExNjU2NTdaGA8yMTE3MDYxNzE2NTY1N1owazELMAkGA1UE\nBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEY\nMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDDBBIUCBUZXN0SGVhZCBS\nb290MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvE4KDi5VgPJxpd06\nZw2MXvaIJ7EjlNqSY9o03Xdun7bqD5z9HRqTHEktfKSi8vjfmk8Pl3KfsZtaElRV\n/jqk37DJTpPbo9bMyllCnfM8VDjR+XQFWcVzQGTY7HNdJhvtYM/cUIDeAr+ZLS4Z\nt2zWavhz4Y3spU9rZUs83UWr1n7qvKko0jotbPWoW0fQF9pswdBmuC49bMIttxZT\nTApJUtLMPYP78LkiZvVMCiPbij4IpSTjN8NQvwEZfIOz37JY8/uoF+OrIJxLH10a\njPedtB3c+3VoM7m5nI/m6UFtd2cbR4UH7bmHYwcoxomUu2ayIm7xKxHWdDJaqNpQ\nPPG7XwIDAQABo4HdMIHaMB0GA1UdDgQWBBQ7AXEPVngoxprW2lyf3FbBbIxtoTCB\nnQYDVR0jBIGVMIGSgBQ7AXEPVngoxprW2lyf3FbBbIxtoaFvpG0wazELMAkGA1UE\nBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEY\nMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDDBBIUCBUZXN0SGVhZCBS\nb290ggkA90Q84KRGH4UwCwYDVR0PBAQDAgG2MAwGA1UdEwQFMAMBAf8wDQYJKoZI\nhvcNAQELBQADggEBAHkSNxBy8ITvz5P+suv7TtEPeh8SWTMN25EFI6Tnj4DebcwM\nshjbHw7PiZ9Gt6t+F1nxRUi/p0wK1QUCuT2GgG6IfwTXpjqInpfYJIpO5gfoLRfF\nDPGkm7Q9WGGgV30HOXExoQ+DRnYwmIAr9mALVHQ2vwpXEJhRbFoXjH5UyYOk82Ax\nVK8bjGS+Ed7tT+Zrk3IsPNz5UnBVMBpXinb//wbrvwYGSkuY8QH9wk5DA3xUCck2\n58YzRpb47raLS8QHLDzvavhgmE/OTXKrlFaSv/TMbWQpNGxNZBQNQmncFZY7A+8b\nENne4zlTXQsHoyIWc40kHarHSW22ICj7aIVZJtA=\n-----END CERTIFICATE-----",
        "signatureAlgorithm": "SHA256WITHRSA",
        "issuer": "HP TestHead Root",
        "validFrom": "2017-07-11T16:56:57.000Z",
        "validUntil": "2117-06-17T16:56:57.000Z",
        "expiresInDays": "36380",
        "certPath": {
            "HP TestHead Root$CRL not found": "CUSTOM_ROOT"
        },
        "publicKey": "RSA Public Key\n            modulus: bc4e0a0e2e5580f271a5dd3a670d8c5ef68827b12394da9263da34dd776e9fb6ea0f9cfd1d1a931c492d7ca4a2f2f8df9a4f0f97729fb19b5a125455fe3aa4dfb0c94e93dba3d6ccca59429df33c5438d1f9740559c5734064d8ec735d261bed60cfdc5080de02bf992d2e19b76cd66af873e18deca54f6b654b3cdd45abd67eeabca928d23a2d6cf5a85b47d017da6cc1d066b82e3d6cc22db716534c0a4952d2cc3d83fbf0b92266f54c0a23db8a3e08a524e337c350bf01197c83b3dfb258f3fba817e3ab209c4b1f5d1a8cf79db41ddcfb756833b9b99c8fe6e9416d77671b478507edb987630728c68994bb66b2226ef12b11d674325aa8da503cf1bb5f\n    public exponent: 10001\n",
        "aliasName": "HP TestHead Root",
        "commonName": "HP TestHead Root",
        "alternativeName": None,
        "basicConstraints": "Subject Type=CA, Path Length Constraint=None",
        "enhancedKeyUsage": None,
        "keyUsage": "digitalSignature,keyEncipherment,dataEncipherment,keyCertSign,cRLSign",
        "dnQualifier": None,
        "name": None,
        "initials": None,
        "givenName": None,
        "surname": None,
        "contactPerson": None,
        "organizationalUnit": None,
        "organization": "Hewlett-Packard",
        "locality": "Palo Alto",
        "locationState": "California",
        "country": "US",
        "email": None,
        "crlDistributionEndPoints": None,
        "sha1Fingerprint": "c8:bd:46:f1:f5:77:05:81:43:6e:bb:0c:b6:ce:f2:93:27:1f:40:19",
        "sha256Fingerprint": "be:4e:7b:08:66:dc:b1:14:5b:0e:f5:25:25:5b:63:61:20:10:31:16:d7:66:77:4c:05:24:9d:39:7e:47:d3:b5",
        "sha384Fingerprint": "f1:0a:20:18:4e:3d:40:28:be:43:92:95:4b:e5:e6:b0:73:07:ab:5d:3a:65:e4:f6:b6:a6:b2:88:bb:8d:21:47:c1:43:94:3e:a1:81:83:0d:4b:d6:72:09:35:11:92:db",
        "state": "CRL not found",
        "status": "WARNING",
        "description": None,
        "created": "2017-11-07T18:00:20.539Z",
        "modified": "2017-11-07T18:00:20.539Z",
        "eTag": "2017-11-07T18:00:20.539Z",
        "category": "appliance",
        "uri": "/rest/certificates/ca/HP TestHead Root"
    },
    "certRevocationConfInfo": {
        "crlSize": None,
        "crlExpiry": None,
        "crlConf": {
            "crlDpList": [
                "Locate any server certificate issued by this CA. Find the CRL distribution point from the certificate.                                            Download the CRL file from the URL. Upload the file to the appliance."
            ]
        }
    },
    "subjectName": "CN=HP TestHead Root,O=Hewlett-Packard,L=Palo Alto,ST=California,C=US",
    "certStatus": "GOOD",
    "certType": "CUSTOM_ROOT",
    "expiryDate": "2117-06-17T16:56:57.000Z",
    "category": "appliance",
    "uri": "/rest/certificates/ca/HP TestHead Root"
}

WEB_PROXY_CERT = {
    "type": "CertificateInfoV2",
    "certificateDetails": [
        {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIID6zCCAtOgAwIBAgICSvowDQYJKoZIhvcNAQELBQAwazELMAkGA1UEBhMCVVMx\r\nEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UE\r\nCgwPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDDBBIUCBUZXN0SGVhZCBSb290MCAX\r\nDTE3MDcxMTE2NTY1N1oYDzIxMTcwNjE3MTY1NjU3WjBxMQswCQYDVQQGEwJVUzET\r\nMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQK\r\nDA9IZXdsZXR0LVBhY2thcmQxHzAdBgNVBAMMFnZzZS5yZGxhYnMuaHBlY29ycC5u\r\nZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDNDLgopI+m/pLvx/q+\r\n9URbY5K009D++WyLH36UF+KPczI7c6l62Kk4uN+gZHrs3IEAHtfwQ9rjUknwW+WW\r\nl6CEP0a+xr8CxCJ/1TxnhUUdGB5yRnSJn5AH9iDHdL3dw4Vv3seO7S8ovEBh8n/V\r\njEQoX8eI2ldA1LF9Dc2/vqzDzFmyFUQ3d2EG7R/3nlTUFAjWdRVfy7JiltwsrGWK\r\n4JwC6p1inA10zcHPhtxDXD+AqfblW0n9YCi+Vdw8xM61yF1h4M8NevnsbS1SSIr4\r\n+HG9SrjTx3Yflnzmw7glhFJ4H3U9kL1/b/1E0NeqLyESn8/DSSFL/7NWUxVdkn5u\r\nj02TAgMBAAGjgZAwgY0wCQYDVR0TBAIwADALBgNVHQ8EBAMCBLAwEwYDVR0lBAww\r\nCgYIKwYBBQUHAwEwEQYJYIZIAYb4QgEBBAQDAgZAMCgGA1UdHwQhMB8wHaAboBmG\r\nF2h0dHA6Ly9sb2NhbGhvc3QvY2EuY3JsMCEGA1UdEQQaMBiCFnZzZS5yZGxhYnMu\r\naHBlY29ycC5uZXQwDQYJKoZIhvcNAQELBQADggEBADo+1NnwbigQR0DELz69x96p\r\nVaHRgmHjWkUG7NUJlmwJU+mw6hxoy+JIVzqT8ktN7Q/3uM1UIB10QtjQBdtzgc1M\r\nZeSz7R6A7Y7aaQzfQqL765B1st+/2KtDPAd/sRC3O6HF24pIKxYnSMv+1Vt1oWA6\r\ntr3eBPYBtEMCRRGw4QP2ukX3fE13OdBCz71dqC7qWR84EIGN3MXu6GhN8SkNERSP\r\n+OCbHGWDRE9RcAvOBlZBde3i/7KI0GxuYdz+U6PRzOO2HehEAJ6fEbCUbtIa8jfj\r\ncJ3ZE3Y1HTmM3p8eJlhe1KwlIU4mfMKldsK+iFIfagR1yguCyX5/wt2Cl0w0Epg=\r\n-----END CERTIFICATE-----",
            "aliasName": "Web-Proxy",
            "type": "CertificateDetailV2"},
        {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIEOTCCAyGgAwIBAgIJAPdEPOCkRh+FMA0GCSqGSIb3DQEBCwUAMGsxCzAJBgNV\r\nBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8x\r\nGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEZMBcGA1UEAwwQSFAgVGVzdEhlYWQg\r\nUm9vdDAgFw0xNzA3MTExNjU2NTdaGA8yMTE3MDYxNzE2NTY1N1owazELMAkGA1UE\r\nBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEY\r\nMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDDBBIUCBUZXN0SGVhZCBS\r\nb290MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvE4KDi5VgPJxpd06\r\nZw2MXvaIJ7EjlNqSY9o03Xdun7bqD5z9HRqTHEktfKSi8vjfmk8Pl3KfsZtaElRV\r\n/jqk37DJTpPbo9bMyllCnfM8VDjR+XQFWcVzQGTY7HNdJhvtYM/cUIDeAr+ZLS4Z\r\nt2zWavhz4Y3spU9rZUs83UWr1n7qvKko0jotbPWoW0fQF9pswdBmuC49bMIttxZT\r\nTApJUtLMPYP78LkiZvVMCiPbij4IpSTjN8NQvwEZfIOz37JY8/uoF+OrIJxLH10a\r\njPedtB3c+3VoM7m5nI/m6UFtd2cbR4UH7bmHYwcoxomUu2ayIm7xKxHWdDJaqNpQ\r\nPPG7XwIDAQABo4HdMIHaMB0GA1UdDgQWBBQ7AXEPVngoxprW2lyf3FbBbIxtoTCB\r\nnQYDVR0jBIGVMIGSgBQ7AXEPVngoxprW2lyf3FbBbIxtoaFvpG0wazELMAkGA1UE\r\nBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEY\r\nMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRkwFwYDVQQDDBBIUCBUZXN0SGVhZCBS\r\nb290ggkA90Q84KRGH4UwCwYDVR0PBAQDAgG2MAwGA1UdEwQFMAMBAf8wDQYJKoZI\r\nhvcNAQELBQADggEBAHkSNxBy8ITvz5P+suv7TtEPeh8SWTMN25EFI6Tnj4DebcwM\r\nshjbHw7PiZ9Gt6t+F1nxRUi/p0wK1QUCuT2GgG6IfwTXpjqInpfYJIpO5gfoLRfF\r\nDPGkm7Q9WGGgV30HOXExoQ+DRnYwmIAr9mALVHQ2vwpXEJhRbFoXjH5UyYOk82Ax\r\nVK8bjGS+Ed7tT+Zrk3IsPNz5UnBVMBpXinb//wbrvwYGSkuY8QH9wk5DA3xUCck2\r\n58YzRpb47raLS8QHLDzvavhgmE/OTXKrlFaSv/TMbWQpNGxNZBQNQmncFZY7A+8b\r\nENne4zlTXQsHoyIWc40kHarHSW22ICj7aIVZJtA=\r\n-----END CERTIFICATE-----",
            "aliasName": "HP TestHead Root",
            "type": "CertificateDetailV2"}]}
