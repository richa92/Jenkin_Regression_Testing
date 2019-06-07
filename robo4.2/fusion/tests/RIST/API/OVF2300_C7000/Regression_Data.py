admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
backupuser_credentials = {'userName': 'BackupUser', 'password': 'wpsthpvse1'}
user = {
    "enabled": "true", "password": "wpsthpvse1",
    "permissions": [{"roleName": "Backup administrator"}],
    "type": "UserAndPermissions", "userName": "BackupUser"
}
ssh_server_ip = '15.114.112.61'
appliance_interface = {
    "type": "ApplianceNetworkConfigurationV2",
    "applianceNetworks": [{
        "activeNode": 1,
        "unconfigure": False,
        "hostname": "ci-005056b473c8.hp.cn",
        "macAddress": "00:50:56:b4:73:c8",
        "confOneNode": True,
        "interfaceName": "",
        "ipv4Type": "DHCP",
        "ipv6Type": "UNCONFIGURE",
        "overrideIpv4DhcpDnsServers": True,
        "searchDomains": [],
        "ipv6NameServers":["", ""],
        "aliasDisabled":True
    }]
}
'''###########################################compatibility report data###########################################'''
expected_count_FIPS_report = 4
expected_count_CNSA_report = 7
expected_WEBSERVER_CERTIFICATE_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Certificate is not signed with the requested cryptography mode compliant signature algorithm or public key algorithm/keysize.',
    u'nonCompatibilityAction': u'The certificate will be regenerated with a compliant digital signature algorithm or public key algorithm/keysize.'
}]
expected_WEBSERVER_CERTIFICATE_CAsigned_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Certificate is not signed with the requested cryptography mode compliant signature algorithm or public key algorithm/keysize.',
    u'nonCompatibilityAction': u'Regenerate or re-import the certificate signed with a compliant digital signature algorithm or public key algorithm/keysize.'
}]

expected_RABBITMQ_SERVER_CERTIFICATE_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Certificate is not signed with the requested cryptography mode compliant signature algorithm or public key algorithm/keysize.',
    u'nonCompatibilityAction': u'The certificate will be regenerated with a compliant digital signature algorithm or public key algorithm/keysize.'
}]
expected_RABBITMQ_SERVER_CERTIFICATE_CAsigned_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Certificate is not signed with the requested cryptography mode compliant signature algorithm or public key algorithm/keysize.',
    u'nonCompatibilityAction': u'Regenerate or re-import the certificate signed with a compliant digital signature algorithm or public key algorithm/keysize.'
}]

expected_RABBITMQ_CLIENT_CERTIFICATE_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Certificate is not signed with the requested cryptography mode compliant signature algorithm or public key algorithm/keysize.',
    u'nonCompatibilityAction': u'The certificate will be regenerated with a compliant digital signature algorithm or public key algorithm/keysize. Any users of rabbitmq need to start using this newly generated client certificate. '}]
expected_Power_Delivery_Devices_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'HPE Intelligent Modular PDUs do not support the compatible protocols and cipher suites in FIPS/CNSA mode.Existing PDUs will become unmanaged and import of a new PDU will not be supported if a mode switch is done to FIPS/CNSA mode.',
    u'nonCompatibilityAction': u'Continue switching to a high security mode if it is acceptable to not manage HPE Intelligent modular PDUs.'
}]
expected_Remote_Support_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Remote Support is incompatible.', u'nonCompatibilityAction': u'Turn off Remote Support to maintain compliance.'
}]
expected_All_Storage_Devices_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Storage systems are currently not supported for FIPS/CNSA security compliance; communication to storage devices managed by the appliance will continue in non-compliant mode',
    u'nonCompatibilityAction': u'Unmanage storage systems from the appliance if FIPS/CNSA compliance is required'
}]
expected_Firmware_drivers_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Firmware update using the "Firmware only" option is currently unsupported for Gen10 servers which are in a high security mode (FIPS/CNSA/high security).',
    u'nonCompatibilityAction': u'Select one of the Smart Update Tools options as the firmware installation method in the server profile and ensure that the Smart Update Tools version 2.1.0 or above is installed on the OS and it has been configured with the iLO credentials. Alternatively, the "Firmware only" option can be selected with the iLO in a Production mode.'
}]
expected_External_repositories_nonCompatibilityDetails = [{
    u'nonCompatibilityKey': u'Remote repositories are unsupported in FIPS/CNSA modes.',
    u'nonCompatibilityAction': u'Upload the SPPs to the internal repository to perform firmware updates.'
}]

'''########################################### compliance validator ###########################################'''
apache_validate_data_fips = {"host": "16.114.218.169", "port": "443", "securityMode": "FIPS", "trustBy": "CERTIFICATE"}
host = "15.114.114.1"
port = "443"
mode = "FIPS"
'''########################################### others ###########################################'''
csr_body = {
    "type": "CertificateSigningRequest",
    "country": "US",
    "state": "California",
    "locality": "Palo Alto",
    "organization": "Hewlett Packard Enterprise",
    "commonName": "ci-005056b40365.vse.rdlabs.hpecorp.net",
    "organizationalUnit": "",
    "alternativeName": "16.114.218.91,ci-005056b40365.vse.rdlabs.hpecorp.net,ci-005056b40365",
    "cnsaCertRequested": False
}
cert_body_example = {
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {"base64Data": "", "type": "CertificateDetailV2", "aliasName": ""}
    }],
    "type": "CertificateAuthorityInfoCollection"
}
