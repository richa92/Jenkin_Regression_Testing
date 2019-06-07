
def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'
Ad1_Name = 'user1_160'
Egroup_DnsAdmin = 'CN=DnsAdmins,CN=Users,DC=fvttest,DC=com'
Egroup_Domain_Admin = 'CN=Domain Admins,CN=Users,DC=fvttest,DC=com'
Login_Message = 'This management appliance is a company owned asset and provided for the exclusive use of authorized personnel. Unauthorized use or abuse of this system may lead to corrective action including termination, civil and/or criminal penalties.'
Root_Ca_Cert = '-----BEGIN CERTIFICATE-----\nMIIF6DCCBNCgAwIBAgIKEbj0JgAAAAAABDANBgkqhkiG9w0BAQ0FADBDMRMwEQYKCZImiZPyLGQB\nGRYDY29tMRcwFQYKCZImiZPyLGQBGRYHZnZ0dGVzdDETMBEGA1UEAxMKZnZ0dGVzdC1DQTAeFw0x\nNzA2MTIxODQxNTBaFw0xODA2MTIxODQxNTBaMCYxJDAiBgNVBAMTG1dJTi1ITktMNjJROFVFRi5m\ndnR0ZXN0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOhuAp9lMdu1BeoBX12T\nb89PDonJsub0F/4a7L69E2AfypzS02KvMtI9LtpFuHE/t5ejZ3RIZk/gfUv/R5VNDZZZvZdauXJI\nOE2LOt4dpwDh1/WosPUKYwYF3NwMqUk9Rayv7aUGAWMW7VZT4bSxdsQENQCv1FaiRpRsNnzZXRtY\nbGaKW5U4ZvXhF0T4QKEVs/jVjGHlQdmAHCZ6IAPKlHf9zyB8Lw/zD/T8RHXu4ecB0MdtntBQt3sL\n3eC29vqMs4zU54gFVr7h5RA5DZv8qFqANoIFS58pWxkG1gF3U/BqrB1fibXRZif4AcdRDb0uw79x\niWgIaiyZqxIC1beM7rECAwEAAaOCAvkwggL1MC8GCSsGAQQBgjcUAgQiHiAARABvAG0AYQBpAG4A\nQwBvAG4AdAByAG8AbABsAGUAcjAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwEwDgYDVR0P\nAQH/BAQDAgWgMHgGCSqGSIb3DQEJDwRrMGkwDgYIKoZIhvcNAwICAgCAMA4GCCqGSIb3DQMEAgIA\ngDALBglghkgBZQMEASowCwYJYIZIAWUDBAEtMAsGCWCGSAFlAwQBAjALBglghkgBZQMEAQUwBwYF\nKw4DAgcwCgYIKoZIhvcNAwcwHQYDVR0OBBYEFBxR9mX1uCz3CF60pe9sBGUFQPtCMB8GA1UdIwQY\nMBaAFKtA6WundwMMheHOuochDbcwRwtGMIHQBgNVHR8EgcgwgcUwgcKggb+ggbyGgblsZGFwOi8v\nL0NOPWZ2dHRlc3QtQ0EsQ049V0lOLUhOS0w2MlE4VUVGLENOPUNEUCxDTj1QdWJsaWMlMjBLZXkl\nMjBTZXJ2aWNlcyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPWZ2dHRlc3QsREM9Y29t\nP2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFzcz1jUkxEaXN0cmlidXRp\nb25Qb2ludDCBvAYIKwYBBQUHAQEEga8wgawwgakGCCsGAQUFBzAChoGcbGRhcDovLy9DTj1mdnR0\nZXN0LUNBLENOPUFJQSxDTj1QdWJsaWMlMjBLZXklMjBTZXJ2aWNlcyxDTj1TZXJ2aWNlcyxDTj1D\nb25maWd1cmF0aW9uLERDPWZ2dHRlc3QsREM9Y29tP2NBQ2VydGlmaWNhdGU/YmFzZT9vYmplY3RD\nbGFzcz1jZXJ0aWZpY2F0aW9uQXV0aG9yaXR5MEcGA1UdEQRAMD6gHwYJKwYBBAGCNxkBoBIEEBhE\ngp7kr8VAv4oJlHqlcnuCG1dJTi1ITktMNjJROFVFRi5mdnR0ZXN0LmNvbTANBgkqhkiG9w0BAQ0F\nAAOCAQEAJYt5+Jiz2+Mjp2ilADMu7Egtq2ExkubkKOLM5dW/Iml3RegX+93xQeOiDt/WOmbT3bnf\nnq7E3um6I915GytRDV7nWCDBzGmmlo61CndXbDYENjK79Qm6tRV5l5+eIIwDhMtPgjfLnDUFPMnJ\ns0QmoeCM+2AOB+Ft5LRStjq9CicqtaG30kjbu0GcYtQYOb0BEK5uMgVtKqbXU5VZY/erRwI47D7P\nXdObE92mtriADCGuQ1qAIWPCmYJ39tQhVmgUCFBx1Skflpu3JMQS6opvfW3y3KVfioZWNyR9ImBb\nNhI42qYv9kQOr8U8x69sE3CMHzzOnASYQufVrVFA/NoeJA==\n-----END CERTIFICATE-----'
Root_Ca_Cert_160 = "-----BEGIN CERTIFICATE-----\nMIIDYTCCAkmgAwIBAgIQfZx0uREVrJpP1jyeH+KYsDANBgkqhkiG9w0BAQ0FADBD\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRcwFQYKCZImiZPyLGQBGRYHZnZ0dGVzdDET\nMBEGA1UEAxMKZnZ0dGVzdC1DQTAeFw0xNzA2MTIwODQ4MjBaFw0yMjA2MTIwODU4\nMTlaMEMxEzARBgoJkiaJk/IsZAEZFgNjb20xFzAVBgoJkiaJk/IsZAEZFgdmdnR0\nZXN0MRMwEQYDVQQDEwpmdnR0ZXN0LUNBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A\nMIIBCgKCAQEAvTX/1WO49Ex0fuXCwW5gvmNorn1Be1wtIzbrUErJE8HOxCuS9aKr\nuuFDA3q2SAU4ynO6SwAnSiywwVYMqJUgJM+Rcq66aq0aw0A4Eq2W1bZwilhOyhOb\nCYoZ2i3+seNJAgCkBuKidSEu7+x6+D2moeS1L3Hkh2+ymok5+ifLn6OmrMwFhb4m\n4QJGELbPsB0a09uLmZ8lf3tSIRmNsFGNyqREWDtfHxTuVJBUkZ8RPDeIc/AQJlTV\n0nHdNnxy/kCpziZTEQtI9xOM0EJqfdXBc76N+Lu3ui4I9x+BchS5IL5RyqB4TtUr\nJrp8S2ldlDNwIqa5Gpq1DSfKYXfy+r+eOwIDAQABo1EwTzALBgNVHQ8EBAMCAYYw\nDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUq0Dpa6d3AwyF4c66hyENtzBHC0Yw\nEAYJKwYBBAGCNxUBBAMCAQAwDQYJKoZIhvcNAQENBQADggEBAGmNqXSdoTH22CyI\njB7/N3HeCEEs75I1xTGUplyk4HWIQi8hUYKdnWU3WHHWzLNuKIQJCyldurMb5vsq\nRjR2wdOON1lfMnFHoOCSTJ4kwK1lQyIhXbqTxoq79o6HUeojUQpk+x8j6iF9UKbk\nlFzweYI/hwav28pHDBXwR7lWq9yVbhG1lEkWmmdd9FPTiKqVPm6ItG43MbH/a40l\n78yTO8GW3RpHJ+gGb6OizgLzkJ281zyKpqixeVzDQUx7Ak/6pm6Ir3mT1tw04bwS\n8e4JIA+aZft7XLVjl+bRGmPT6Wm9U6ERj+oLPgb4437XDtWizYJAkqHtojiGpMsj\nbVXO/YU=\n-----END CERTIFICATE-----"
admin_credentials_ack_true = {'userName': 'Administrator', 'password': 'hpvse123', 'loginMsgAck': 'true', 'authLoginDomain': 'LOCAL'}
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123', 'authLoginDomain': 'LOCAL'}
ad_credentials_ack_true = {'userName': 'user1', 'password': '12iso*help', 'loginMsgAck': 'true', 'authLoginDomain': Ad1_Name}
ad_credentials = {'userName': 'user1', 'password': '12iso*help', 'authLoginDomain': Ad1_Name}
ad_credentials_invalid_password = {'userName': 'user1', 'password': 'invalidPassword', 'authLoginDomain': Ad1_Name}
ad_credentials_invalid_username = {'userName': 'userMismatch', 'password': '12iso*help', 'authLoginDomain': Ad1_Name}
admin_credentials_invalid_username = {'userName': 'Admin', 'password': 'hpvse123', 'authLoginDomain': 'LOCAL'}
admin_credentials_invalid_password = {'userName': 'Administrator', 'password': 'invalidPassword', 'authLoginDomain': 'LOCAL'}
admin = {'userName': 'Administrator', 'password': 'hpvse123'}

RootCA_signed_certs_trust_body = {
    'members': [
        {
            'certificateDetails': {
                'aliasName': 'user1_160',
                'base64Data': Root_Ca_Cert_160,
                'type': 'CertificateDetailV2'
            },
            'type': 'CertificateAuthorityInfo'
        }
    ],
    'type': 'CertificateAuthorityInfoCollection'
}

edit_global_settings_ack_true = {'allowLocalLogin': True,
                                 'defaultLoginDomain': {
                                     'type': 'LoginDomainConfigInfoDto',
                                     'name': Ad1_Name,
                                     'uri': '',
                                     'loginDomain': '0'
                                 },
                                 'twoFactorAuthenticationEnabled': True,
                                 'strictTwoFactorAuthentication': False,
                                 'loginMessage': {
                                     'acknowledgment': True,
                                     'message': Login_Message,
                                     'type': 'LoginMessageVersion600'
                                 },
                                 'technicianEnabled': True
                                 }

edit_global_settings_ack_false = {'allowLocalLogin': True,
                                  'defaultLoginDomain': {
                                      'type': 'LoginDomainConfigInfoDto',
                                      'name': Ad1_Name,
                                      'uri': '',
                                      'loginDomain': '0'
                                  },
                                  'twoFactorAuthenticationEnabled': True,
                                  'strictTwoFactorAuthentication': False,
                                  'loginMessage': {
                                      'acknowledgment': False,
                                      'message': Login_Message,
                                      'type': 'LoginMessageVersion600'
                                  },
                                  'technicianEnabled': True
                                  }

edit_global_settings_enable_only_ad = {'allowLocalLogin': False,
                                       'defaultLoginDomain': {
                                           'type': 'LoginDomainConfigInfoDto',
                                           'name': Ad1_Name,
                                           'uri': '',
                                           'loginDomain': ''
                                       },
                                       'twoFactorAuthenticationEnabled': False,
                                       'strictTwoFactorAuthentication': False,
                                       'loginMessage': {
                                           'acknowledgment': False,
                                           'message': Login_Message,
                                           'type': 'LoginMessageVersion600'
                                       },
                                       'technicianEnabled': True,
                                       'emergencyLocalLoginType': None,
                                       'emergencyLocalLoginEnabled': False
                                       }

edit_global_settings_enable_local_ad = {'allowLocalLogin': True,
                                        'defaultLoginDomain': {
                                            'type': 'LoginDomainConfigInfoDto',
                                            'name': 'LOCAL',
                                            'uri': '',
                                            'loginDomain': '0'
                                        },
                                        'twoFactorAuthenticationEnabled': False,
                                        'strictTwoFactorAuthentication': False,
                                        'loginMessage': {
                                            'acknowledgment': False,
                                            'message': Login_Message,
                                            'type': 'LoginMessageVersion600'
                                        },
                                        'technicianEnabled': True
                                        }

edit_global_settings_local_disable = {'allowLocalLogin': False,
                                      'defaultLoginDomain': {
                                          'type': 'LoginDomainConfigInfoDto',
                                          'name': Ad1_Name,
                                          'uri': '',
                                          'loginDomain': ''
                                      },
                                      'twoFactorAuthenticationEnabled': True,
                                      'strictTwoFactorAuthentication': False,
                                      'loginMessage': {
                                          'acknowledgment': False,
                                          'message': Login_Message,
                                          'type': 'LoginMessageVersion600'
                                      },
                                      'technicianEnabled': True,
                                      'emergencyLocalLoginType': None,
                                      'emergencyLocalLoginEnabled': False
                                      }

group_role_dns_admin = {'type': 'LoginDomainGroupCredentials',
                        'group2PermissionPerGroup': {
                            'type': 'LoginDomainGroupPermission',
                            'loginDomain': Ad1_Name,
                            'egroup': Egroup_DnsAdmin,
                            'permissions': [
                                {
                                    'roleName': 'Infrastructure administrator',
                                    'scopeUri': None
                                }
                            ]
                        },
                        'credentials': {
                            'userName': 'user1',
                            'password': ''
                        }
                        }

group_role_domain_admins = {'type': 'LoginDomainGroupCredentials',
                            'group2PermissionPerGroup': {
                                'type': 'LoginDomainGroupPermission',
                                'loginDomain': Ad1_Name,
                                'egroup': Egroup_Domain_Admin,
                                'permissions': [
                                    {
                                        'roleName': 'Infrastructure administrator',
                                        'scopeUri': None
                                    }
                                ]
                            },
                            'credentials': {
                                'userName': 'user1',
                                'password': ''
                            }
                            }

login_cert_issuer = {'type': 'LoginCertificateConfigDto',
                     'subjectPatterns': [
                         'CN=(.*)'
                     ],
                     'subjectAlternateNamePatterns': [

                     ],
                     'certificateDomainIdentifier': 'Issuer',
                     'validationOids': [
                         {
                             '1.3.6.1.5.5.7.3.2': 'Client Authentication',
                             '1.3.6.1.4.1.311.20.2.2': 'Smart Card Logon'
                         }
                     ],
                     'certificateDomainIdentifierPattern': 'DC=(.*)'
                     }

login_cert_invalid_oid = {'type': 'LoginCertificateConfigDto',
                          'subjectPatterns': [
                              'CN=(.*)'
                          ],
                          'subjectAlternateNamePatterns': [

                          ],
                          'certificateDomainIdentifier': 'Issuer',
                          'validationOids': [
                              {
                                  '1.3.6.1.5.5.7.3.2.0.1': 'Client Authentication',
                                  '1.3.6.1.4.1.311.20.2.2': 'Smart Card Logon'
                              }
                          ],
                          'certificateDomainIdentifierPattern': 'DC=(.*)'
                          }

login_cert_wrong_subject = {'type': 'LoginCertificateConfigDto',
                            'subjectPatterns': [
                                'E=(.*)'
                            ],
                            'subjectAlternateNamePatterns': [

                            ],
                            'certificateDomainIdentifier': 'Issuer',
                            'validationOids': [
                                {
                                    '1.3.6.1.5.5.7.3.2': 'Client Authentication',
                                    '1.3.6.1.4.1.311.20.2.2': 'Smart Card Logon'
                                }
                            ],
                            'certificateDomainIdentifierPattern': 'DC=(.*)'
                            }


login_cert_subject = {'type': 'LoginCertificateConfigDto',
                      'subjectPatterns': [
                          'CN=(.*)'
                      ],
                      'subjectAlternateNamePatterns': [

                      ],
                      'certificateDomainIdentifier': 'Subject',
                      'validationOids': [
                          {
                              '1.3.6.1.5.5.7.3.2': 'Client Authentication',
                              '1.3.6.1.4.1.311.20.2.2': 'Smart Card Logon'
                          }
                      ],
                      'certificateDomainIdentifierPattern': 'DC=(.*)'
                      }

add_directory = {'name': Ad1_Name,
                 'credential': {
                     'userName': 'user1',
                     'password': '12iso*help'
                 },
                 'authProtocol': 'AD',
                 'orgUnits': [

                 ],
                 'userNamingAttribute': 'UID',
                 'baseDN': 'dc=fvttest,dc=com',
                 'directoryServers': [
                     {
                         'type': 'LoginDomainDirectoryServerInfoDto',
                         'directoryServerSSLPortNumber': '636',
                         'directoryServerIpAddress': '15.212.136.160',
                         'directoryServerCertificateStatus': '',
                         'serverStatus': '',
                         'directoryServerCertificateBase64Data': Root_Ca_Cert
                     }
                 ],
                 'type': 'LoginDomainConfigV600',
                 'authnType': 'CREDENTIAL',
                 'directoryBindingType': 'SERVICE_ACCOUNT'
                 }
