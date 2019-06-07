from FusionLibrary.libs.utils.common import get_firmware_bundle
from FusionLibrary.libs.utils.common import get_firmware_version_by_file_name

Certificate_Type = "CertificateDetailV2"
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
enclosure_errorCode = "CANNOT_COMMUNICATE_WITH_ENCLOSURE"
Team_Name = "SHQA"
Ring = "TBird13"

c7000enclosureName_info = [
    {
        u'nonCompatibilityKey': u'The device does not support the compatible protocols and cipher suites for the requested cryptography mode. After a successful mode switch operation, it is likely that this device will become unmanaged or unreachable.',
        u'nonCompatibilityAction': u'Remove the device from OneView before changing the cryptography mode or leave the cryptography mode at its current setting.'
    }
]

tbirdenclosureName_info = [
    {
        u'nonCompatibilityKey': u'Certificate is not signed with the requested cryptography mode compliant signature algorithm or public key algorithm/keysize.',
        u'nonCompatibilityAction': u'Regenerate the certificate signed with a compliant digital signature algorithm or public key algorithm/keysize.'
    }
]

spp_folder_lower = r'Z:\firmware\SPP\SHQA_Regression\Lower'
spp_folder_higher = r'Z:\firmware\SPP\SHQA_Regression\Higher'
fw_bundle_lower = get_firmware_bundle(spp_folder_lower)
fw_bundle_higher = get_firmware_bundle(spp_folder_higher)
firmwareVersion_lower = get_firmware_version_by_file_name(fw_bundle_lower)
firmwareVersion_higher = get_firmware_version_by_file_name(fw_bundle_higher)
le_name = 'LE_SYNERGY'

firmwareUpdateOn = "EnclosureOnly"
forceInstallFirmware = True
logicalInterconnectUpdateMode = "Orchestrated"
alidateIfLIFirmwareUpdateIsNonDisruptive = False
updateFirmwareOnUnmanagedInterconnect = True

Issuer_IP = '16.114.221.17'
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
cert_tool_path = '/root/automation_tools/cert_tool'
signature_algorithm_sha1 = "sha1"
signature_algorithm_sha256 = "sha256"
signature_algorithm_sha384 = "sha384"

enclosure_csr = {
    "type": "CertificateDtoV2",
    "commonName": "EM123",
    "organization": "Hewlett Packard Enterprise",
    "organizationalUnit": "EML",
    "country": "PR",
    "state": "Aguada",
    "locality": "Mamey"}

add_flm_rootcacert = {
    "members": [
        {
            "certificateDetails": {
                "aliasName": None,
                "base64Data": "",
                "type": Certificate_Type},
            "type": "CertificateAuthorityInfo"}],
    "type": "CertificateAuthorityInfoCollection"}

enclosure_put = {"type": "CertificateDataV2", "base64Data": ""}

compliancevalidator = {
    "host": "",
    "port": "443",
    "securityMode": "",
    "trustBy": "CERTIFICATE"
}
