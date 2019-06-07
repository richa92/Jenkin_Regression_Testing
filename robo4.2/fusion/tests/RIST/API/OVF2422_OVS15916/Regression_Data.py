admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

filename = "crlFile-ca.crl"

certs = [
    {
        "members": [{
            "type": "CertificateAuthorityInfo",
            "certificateDetails": {
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFXjCCA8agAwIBAgIJAKd5kLp5zMhrMA0GCSqGSIb3DQEBDAUAMGQxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDESMBAGA1UEAwwJSFBFXyBSb290MCAXDTE3MTIxMjA4MDQ1MloYDzIxMTcxMTE4MDgwNDUyWjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBANoxNDXxL1zoDopeWPHjkpCOurIaXdWSPxAiIuG0HfruiDid4CDL6zcGQko5ZZYZud99kxChgLjOeOgl9En7DwS/LMXiALLnFyX+8i+7pgURmzDqvydJzilbfSBCTVDPDkvBNfoAiujNMix8pgJlboY+PrgUGGEi2A7DUH5X+oidQLnzaenhSKZIld+QdXf6PLKK8ZtKWYz16Z4cFbMOxpk/jIRZuj3FvztCaqz2nD+B2KZtWcU9oQ5BhD2bqScpuEgGr8apY1fgV2IM01ug3ks6l1GNMBUKxrS4xiuQ9TXMjuk15GvR+fzkGkFm1S6Ufnh5f8e88ht3ch3r6AMyI55vO5vkJSUKnH/B6bFxw0Tn00DytctTb2HoxrCvskh1Hl2HKj4hnsvyJVtYHJmDK77X25JQI25Zhu8xK7D+sIJEdjyd2NcoI1uK2GzLJa9ocJwgEBgKi3NDFI3EApziDLL+f+gvXlwfVengpfx4sGsFHH8zSLZKzI4Cip3KJ3VAdQIDAQABo4IBDzCCAQswHQYDVR0OBBYEFOa7sD06Iw3JTWaOKb906SsL5+92MIGWBgNVHSMEgY4wgYuAFOa7sD06Iw3JTWaOKb906SsL5+92oWikZjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdIIJAKd5kLp5zMhrMAsGA1UdDwQEAwIBtjAMBgNVHRMEBTADAQH/MDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBAGBr65sRBs/IVDGy63zEQq5/vDnT0NUJeg7B0QhT2HZTj89ZHHuS/a72Kt2ya3RN0nE9GE5nQse454sNFG2GtDkeXExV7Kv9YOKg/P9MktbP9ZMtUxDHooh7lm1Z3dPNs2UfTq+m6QLum7C/TX6BgotSu8aq7JF3rUf5KBvUxVAPtPA+BDh6WWFOKSdculaIUj22bf+MBp9oURoXbxEl0pDgYi521PhK2K7sh6h9ptHnpO/x6Xf0DJfiXQcNiI/rLzbrHPQ0DyXn7vDi6aBqpxH1fvhBOORiqUbgJefn0iVTnx7HRUX8SilcF3JW+QvOhenqofXv/i+q+XSv6rUPB9Q7zL5obQ0ON6OH+KUvuZQXoYqwHoKuIgCuzj44R4Y29SKpj2Rt80BZGkW1Q0mQ71VIwQvJlD4Zb0y6e9WyJhQdZzAEwURDX0yYzfTvwUTzXihHtM+udVrulCBSp3CXVNb8Wldtla1EH9QJMlraLRP06es8irhDrFmGL05XvJw8eg==\n-----END CERTIFICATE-----",
                "aliasName": "SHQA_root_filter_test",
                "type": "CertificateDetailV2"
            }}],
        "type": "CertificateAuthorityInfoCollection"
    },
    {
        "members": [{
            "type": "CertificateAuthorityInfo",
            "certificateDetails": {
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFEDCCA3igAwIBAgICcmgwDQYJKoZIhvcNAQEMBQAwZDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRIwEAYDVQQDDAlIUEVfIFJvb3QwIBcNMTcxMjEyMDgwNDU0WhgPMjExNzExMTgwODA0NTRaMGcxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEVMBMGA1UEAwwMSFBFXyBpbnRlci0xMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAxHrfSB40yU8PxAY2+3MuWKwQwHJVJJlSzgifZn6cW0XFMbnlaCjN1X9kklTLqI3yxxGgedNR0yivfLlFCpbKYVbyOXXtx7r0/GX/xSkMK/nqbUtpQE78qjyZKZrZrZ/B//5Dpr6K2H0ezvXXKyJoLufZjzjfa0IqHM5ZRnRO2nyfFa6oUhsJI4sJ/Vqlay/5oyTKkaRN7MIRzXNKmOQyclyeYSPt7wdkp0/eHtzNbHnUQR081dkon1mZ886qqXZBuO6Zb+8fCqOidvLcjMgH+0u0lD0XiiHqhNBiYLkULVuaOS2tpN+XVvS503veBlTeXe2ghmztmMddI1yl2bwZEhKHiMu21jIXMmShdZMpzOgTOTZBo84zrbOB9ch3Qzw8S8G9PJgVB7gKMxaUvu3hyKnV75R1WF7qFAIE8MiC6dXSNoPMdbh5j6O8uviOMHSYy3mv6TF2dBK2xaf1vpdLBaCEc854Scv4PWVMist5GZSDCtf4cVSWf7ZzACfYhEV3AgMBAAGjgcYwgcMwHQYDVR0OBBYEFAYvrqxfTxOUW76BYnT4iwhEUr/+MB8GA1UdIwQYMBaAFOa7sD06Iw3JTWaOKb906SsL5+92MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3QvY2EuY3JsMDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBAEccM5e787g3jdQ04kkCx4To9+P0GsSvWfuPyynLwDsXVJYW867PnKL6IZxWSY9TPlhXN8pCF5ELzIQBceNBdHQz3SyYP5DxryGT1pvJUMOg0YoDf8DnpX2zVpypdWFd8i0AgxHoYBYpBJXT3bZKKa9kgA/N5rXn4XvMvgvtlaIJ03dIRp2WpZlJkm6DztiL7qdGh5k2PM4HOoaMatJ1lPcSMTZ0Ynh4ZfiGvXhXrvkZrkSrbx3Z9/Xg9RVGiU4NDUuA38cWYrZ2oqFS0yGKr43eXwBucYHOu6+Ip3mcNQ77MfYNnXGxMjiH4P3MPmUA641JN4LzlXE6h8jK+Tim2fy5UzftVoiU9zxvOITflhFQgUv/+GVpJONAqf1PA1uwtYDe3UjhyrKm5DvpZW7EZnZEaWqlTsB8T6HNJ6VRpkcStltEY9srCS22jgB+FOVIRH0FoFK6ly6pqNaJ5ONXKGF5R96RB0wH6o6Z7rN5U3TD/OMclYsH63ZlBKgyGlEz3A==\n-----END CERTIFICATE-----",
                "aliasName": "SHQA_inter_1_filter_test",
                "type": "CertificateDetailV2"
            }}],
        "type": "CertificateAuthorityInfoCollection"
    },
    {
        "members": [{
            "type": "CertificateAuthorityInfo",
            "certificateDetails": {
                "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFEzCCA3ugAwIBAgICER8wDQYJKoZIhvcNAQEMBQAwZzELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRUwEwYDVQQDDAxIUEVfIGludGVyLTEwIBcNMTcxMjEyMDgwNDU3WhgPMjExNzExMTgwODA0NTdaMGcxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEVMBMGA1UEAwwMSFBFXyBpbnRlci0yMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAzO4uggJ/KiPV9sy0J584lHy335b/uZTrTd2P0VMPNzQAmN4VNEyhtyKm63+SbXigtZwa/5tWIOlfaF5vYk7hCIHPQLwGaUxHKRmDOuLJHc2gnZ2XgUrx+Y3TP9OqCcyTskG5U0jiRgG8r4ZApw8yS2YkcQTg/uVqwcCql1rJJCmYUbmmyt45nsjdRz+rgHFSAymzdDQKaGeKAQoApO0BAkG9yIGa3XnTFRbMqoeAf89ZHApyUjkTnJH8lyyYTjG0GDsNMvFOOixepsqEkugLTuKWZvDz7j4f8fHjYmOz8JX1y4J4aDvy+QSC0YLYKb2ocZpM972z59VtkAm7OJFaNikJKM3zfSIfZE82XKJO4Pxs8cMghXg6Ik/S5mZmIECjrb2TvTUeZQlNwx3Bp7hf7VT4cmKYKD/9r16lnVc1WrN5kWz5nI39UXhRz8INBgRHBvB19pwUQptvxxtzAzmEQ+vNdjGvphQo45LiHcsqJo9txAoabm7ouFGYfD3fuqa5AgMBAAGjgcYwgcMwHQYDVR0OBBYEFByE33vWoQgn864SxI5xwq/APib0MB8GA1UdIwQYMBaAFAYvrqxfTxOUW76BYnT4iwhEUr/+MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3QvY2EuY3JsMDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBAJA/a0NMPzoFbvLxgNqRqg28lrDN5R73UFOU0NRjzec03jsO/DvwA9VeBFqjfw6OXLPSlvfvWQtev1YCCEMLiVaYML/BPHtb89ALBT6qmgZwuZK2ymhZfP+yZWKfXwfdlvWE//l9GEp/TqAcPmqdB6B4CDRUaQC7kyGZWqPTnVxdJLoUCBedA6qbtb4N91nZv4V0XhlNI97zYg8RCJEn2EntdEcxL3ZtRSuaDn9fzoWNJgsLVw+HJVBhO8es5zx8+xx16QZh5Te/9ZVsQToY7MmuMHKRHLxyV9HVsAUHsQXIr1thdUCX5lTZUhwdb/d3LTYw0eVwDbw08VTEdhaHH37l+of0uxNToelkWq8jsl8E52ENGskD/Jf1Uie5wf/tcpYiAfgLOTCcICXb/Eab2NIuOUmQ0I4QeJO/N7Oq93yTFSe7p/rA/XlcC5i/I+u4LX++Ls0ZgSTfslI+xX6PUw9WmxA0C8Pf/vgPSjJsx8IyZAzRjB+lO4nXRnNzB7evEA==\n-----END CERTIFICATE-----",
                "aliasName": "SHQA_inter_2_filter_test",
                "type": "CertificateDetailV2"
            }}],
        "type": "CertificateAuthorityInfoCollection"
    }
]

RevocationCerts = [{
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFXjCCA8agAwIBAgIJAKPLacrOGmdUMA0GCSqGSIb3DQEBDAUAMGQxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDESMBAGA1UEAwwJSFBFXyBSb290MCAXDTE3MTIxMTEwMDA0M1oYDzIxMTcxMTE3MTAwMDQzWjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBANSvTzRRvYAWbNN+nq1YAbTD/fUOKLkCGMICmLrWt+4KiTn8VqBT/1nRJA78NI5p0zuMeTHLlkc9IkY30gbiZT5KBJPIwb+umVxUXp8/IgBSwCL/vH64fe7LFoNfBH17F70+YzilONHEsMPs78J+9OMPrdHTJitiZ0yyRjyswWT0wo++5SJPY1gBcjzUWKfMvUz6Jy/RZ1Z1JQ6tABEjC7SWDmTej+wUKBRtm5nrdMhNkPl/2ngeEkWlA4qE2zZPg2i8E9ZzthC8T4ZJRxGz3iG4b6GdOLVeSLWHXs2zh66zHatk7M/mSZbZwjDJcjTRN1ZeDHJt0Zw2iKRHdnJjJyOzUSIvDPYMTp/SZiTKr7qBrW6dHUW3O9dMUrRgIqpRFtKmIMtFCHb/1WfmxytIIoSjfAPR3oSKOEVTh4GhdadSfEAlh0+Wz4u0SsQW+CZ5WYNgFzpDsFeOPoQidOW/bajBfbag1Zsj7uGEVsi6Azto8jaFOGQwlsSpqxd3Fp8oiQIDAQABo4IBDzCCAQswHQYDVR0OBBYEFHBNNshl72UD7D+Wdf5o7U+8HHsaMIGWBgNVHSMEgY4wgYuAFHBNNshl72UD7D+Wdf5o7U+8HHsaoWikZjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdIIJAKPLacrOGmdUMAsGA1UdDwQEAwIBtjAMBgNVHRMEBTADAQH/MDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBALE0qbKz/jIp3LJTbe1ejnpdK7aBYQJUv0D33Vj2YOOJJ1QTs1uxCQPlGh3WIlUta45yPAc/3IMgIIP/6nzmKEPEaayY+OwHfQa83sLDkd3/TIXN09nIklVqN9GPrSiEjd9L63bG116xxl4q6YIvBPf+OLWfcPtls5ZCE7ZUSQn1ScZqy4xddowlnTW8u50r2AFzwmInQIAKGmE5co1e+RIx98+mYJFrx53B952RMkWnPjJwpQsLBxvHjjPq93KPE7uw3Ln3HZb9Wbn/TuedzgfZh3DoTw6VGxkVfgCe2SU8NwngblRhujrzRJwsO3/Xq9jh12LEnqHZBRL4nNOISA28NmfPud/KhGHi1BBnlwJgKqkRbJbhrUsQymnj5ndLsnuMLv0Og/lwc/beWDcAOcZb1gTLzWwbAaWMN0OFURTXkGQKZi8Aa8qcrt+UqzswAXYYV7puKXwOzKSEOXfRDiB3FwoSIna4q1DZGvTD/aNYPmAPyB5zCa2q51zDJ+nGfA==\n-----END CERTIFICATE-----",
            "aliasName": "Revocation_root_CA_filter_test",
            "type": "CertificateDetailV2"
        }
    }],
    "type": "CertificateAuthorityInfoCollection"
},
    {"members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFEDCCA3igAwIBAgICN/wwDQYJKoZIhvcNAQEMBQAwZDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExEjAQBgNVBAcMCVBhbG8gQWx0bzEYMBYGA1UECgwPSGV3bGV0dC1QYWNrYXJkMRIwEAYDVQQDDAlIUEVfIFJvb3QwIBcNMTcxMjExMTAwMDQ3WhgPMjExNzExMTcxMDAwNDdaMGcxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDEVMBMGA1UEAwwMSFBFXyBpbnRlci0xMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEA17efte/bG7Pc6uexyB4SY9gicGa3Sl3auex/EARuyOfa7awYfmZAZ0FgPD5KZxIHMuxv67djoXqOnAzmvbEM0P+2eWotFZWIIcFXGKgWvuNOsaEcgRWslqCzLx29UJGD507VbqWgiTS6z16g7gsvClurgqDy7V7PSyzNkQTA+skbD8nXz9cy0ADv2+QaUawLjyjEgDGvftMIk1gqhG9JRA7SCtnzk+pgjMtpjS368+u3ldjUYNWv6H4/+mgXYGrebl/s+pKJ/EApZzYbG1p5aJPzvwG2gMrGB+lHP2WOfWimgG8S4nhc3+ZkQtAVDu4tXCsrC6UDO7jT5GQsc1vZlw9geN2oKZgIt7K/WA4n8wKmHLO2rvWNuFWtdbFCBdQoFfMajcgquwl19C/0vLOcFQgRpgxK3Lsv1p+r+oyf1RzQ4Zz+5zxgM1IrG5PXp5+TgEa7zA4ClPrM0LO+x472cl21Oqi+QZtePwJAC0Ll6Ut57mHpj+h5o6SRsoBzWq8TAgMBAAGjgcYwgcMwHQYDVR0OBBYEFJvYMaKmiA0dWokYc4SKF96U47GFMB8GA1UdIwQYMBaAFHBNNshl72UD7D+Wdf5o7U+8HHsaMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMCgGA1UdHwQhMB8wHaAboBmGF2h0dHA6Ly9sb2NhbGhvc3QvY2EuY3JsMDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBAJGg1s07VJArPLe0Ms8ljDapdTuQx5gSSBxbTh+n+RvYUCIa/om8tx/0XwOOWWWpviHJ14kOKJ1NKOV6r/pf4O1S+QpXbJN8YS/6YMbryWxdvEdl55UcLSNYX5N+gYDTqChZALO6rzMAxHAN5fvlludeCecbaM65WN/p4sDPoFa5of2I1jLV4GMqqHsAQzfjauh0IQogtLBNNh7GWwXeIU4lWPg8xiVurRnFbIF4TZxKJoYTzlNyxhK1Psray5+gKMLRZZ2fUXMVWyU3n/Z03ufKbr/a9hoiRrF6TyfLjOinxmSdBgoCvldBk6xrqLwNg/kToJKAxuBNfIAvlwZstAIz26QeBQwZbbFNszs7hS0movN1nFS5WMKj1QDjhBJhO2Aia31uw5tY9Wjysh6DMT6skIF0kFMzSEMUUZF5Gdpf/ak4BAcahXaNeBFuB6bfJh1JFsJYoI+jaJfOwJJyc7+LS2vDZJ6ZDVsnaqGSY6LHcgmz8GRRtXT5d0OL9+N7Gg==\n-----END CERTIFICATE-----",
            "aliasName": "Revocation_inter_CA_filter_test",
            "type": "CertificateDetailV2"
        }
    }],
    "type": "CertificateAuthorityInfoCollection"}
]

RevokedRoot = [{
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {
            "base64Data": "-----BEGIN CERTIFICATE-----\nMIIFXjCCA8agAwIBAgIJAKPLacrOGmdUMA0GCSqGSIb3DQEBDAUAMGQxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRIwEAYDVQQHDAlQYWxvIEFsdG8xGDAWBgNVBAoMD0hld2xldHQtUGFja2FyZDESMBAGA1UEAwwJSFBFXyBSb290MCAXDTE3MTIxMTEwMDA0M1oYDzIxMTcxMTE3MTAwMDQzWjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBANSvTzRRvYAWbNN+nq1YAbTD/fUOKLkCGMICmLrWt+4KiTn8VqBT/1nRJA78NI5p0zuMeTHLlkc9IkY30gbiZT5KBJPIwb+umVxUXp8/IgBSwCL/vH64fe7LFoNfBH17F70+YzilONHEsMPs78J+9OMPrdHTJitiZ0yyRjyswWT0wo++5SJPY1gBcjzUWKfMvUz6Jy/RZ1Z1JQ6tABEjC7SWDmTej+wUKBRtm5nrdMhNkPl/2ngeEkWlA4qE2zZPg2i8E9ZzthC8T4ZJRxGz3iG4b6GdOLVeSLWHXs2zh66zHatk7M/mSZbZwjDJcjTRN1ZeDHJt0Zw2iKRHdnJjJyOzUSIvDPYMTp/SZiTKr7qBrW6dHUW3O9dMUrRgIqpRFtKmIMtFCHb/1WfmxytIIoSjfAPR3oSKOEVTh4GhdadSfEAlh0+Wz4u0SsQW+CZ5WYNgFzpDsFeOPoQidOW/bajBfbag1Zsj7uGEVsi6Azto8jaFOGQwlsSpqxd3Fp8oiQIDAQABo4IBDzCCAQswHQYDVR0OBBYEFHBNNshl72UD7D+Wdf5o7U+8HHsaMIGWBgNVHSMEgY4wgYuAFHBNNshl72UD7D+Wdf5o7U+8HHsaoWikZjBkMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUhQRV8gUm9vdIIJAKPLacrOGmdUMAsGA1UdDwQEAwIBtjAMBgNVHRMEBTADAQH/MDYGCCsGAQUFBwEBBCowKDAmBggrBgEFBQcwAYYaaHR0cDovL2xvY2FsaG9zdDoyNTYwL29jc3AwDQYJKoZIhvcNAQEMBQADggGBALE0qbKz/jIp3LJTbe1ejnpdK7aBYQJUv0D33Vj2YOOJJ1QTs1uxCQPlGh3WIlUta45yPAc/3IMgIIP/6nzmKEPEaayY+OwHfQa83sLDkd3/TIXN09nIklVqN9GPrSiEjd9L63bG116xxl4q6YIvBPf+OLWfcPtls5ZCE7ZUSQn1ScZqy4xddowlnTW8u50r2AFzwmInQIAKGmE5co1e+RIx98+mYJFrx53B952RMkWnPjJwpQsLBxvHjjPq93KPE7uw3Ln3HZb9Wbn/TuedzgfZh3DoTw6VGxkVfgCe2SU8NwngblRhujrzRJwsO3/Xq9jh12LEnqHZBRL4nNOISA28NmfPud/KhGHi1BBnlwJgKqkRbJbhrUsQymnj5ndLsnuMLv0Og/lwc/beWDcAOcZb1gTLzWwbAaWMN0OFURTXkGQKZi8Aa8qcrt+UqzswAXYYV7puKXwOzKSEOXfRDiB3FwoSIna4q1DZGvTD/aNYPmAPyB5zCa2q51zDJ+nGfA==\n-----END CERTIFICATE-----",
            "aliasName": "Revocation_root_CA_filter_test",
            "type": "CertificateDetailV2"
        }
    }],
    "type": "CertificateAuthorityInfoCollection"
}]

queryCertsP01 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "SHQA_root_filter_test",
    "cert_state": "",
    "cert_expiryDate": ""
}

queryCertsP02 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "filter_test",
    "cert_state": "",
    "cert_expiryDate": ""
}

queryCertsP03 = {
    "cert_type": "CUSTOM_ROOT",
    "cert_status": "",
    "cert_aliasName": "",
    "cert_state": "",
    "cert_expiryDate": ""
}

queryCertsP04 = {
    "cert_type": "INTERMEDIATE",
    "cert_status": "",
    "cert_aliasName": "",
    "cert_state": "",
    "cert_expiryDate": ""
}

queryCertsP05 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "filter_test",
    "cert_state": "CRL not found",
    "cert_expiryDate": ""
}

queryCertsP06 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "",
    "cert_state": "Expired",
    "cert_expiryDate": ""
}

queryCertsP07 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "filter_test",
    "cert_state": "OK",
    "cert_expiryDate": ""
}

queryCertsP08 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "filter_test",
    "cert_state": "Revoked",
    "cert_expiryDate": ""
}

queryCertsP09 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "filter_test",
    "cert_state": "Untrusted",
    "cert_expiryDate": ""
}

queryCertsP10 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "filter_test",
    "cert_state": "",
    "cert_expiryDate": "2117"
}

queryCertsP11 = {
    "cert_type": "",
    "cert_status": "",
    "cert_aliasName": "filter_test",
    "cert_state": "",
    "cert_expiryDate": "2117-11-18T08:04:54.000Z"
}

queryCertsP12 = {
    "cert_type": "",
    "cert_status": "WARNING",
    "cert_aliasName": "filter_test",
    "cert_state": "",
    "cert_expiryDate": ""
}

queryCertsP13 = {
    "cert_type": "",
    "cert_status": "CRITICAL",
    "cert_aliasName": "filter_test",
    "cert_state": "",
    "cert_expiryDate": ""
}

queryCertsP14 = {
    "cert_type": "INTERMEDIATE",
    "cert_status": "CRITICAL",
    "cert_aliasName": "filter_test",
    "cert_state": "Untrusted",
    "cert_expiryDate": "2117-11-17T10:00:47.000Z"
}

expectedCountP01 = 1
expectedCountP02 = 3
expectedCountP05 = 3
expectedCountP07 = 4
expectedCountP08 = 1
expectedCountP09 = 1
expectedCountP10 = 4
expectedCountP11 = 1
expectedCountP12 = 3
expectedCountP13 = 1
expectedCountP14 = 1

ca_alias_name = "SHQA_root_filterp01"
