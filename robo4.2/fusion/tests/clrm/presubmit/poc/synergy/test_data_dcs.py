# #####################################s
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
# #####################################
CERTIFICATE = {
    "certificateDetails": [{
        "aliasName": "Vcenter",
        "base64Data": "",
        "type": "CertificateDetailV2"
    }],
    "type": "CertificateInfoV2"
}

CERTIFICATE_scvmm = {
    "certificateDetails": [{
        "aliasName": "Vcenter",
        "base64Data": "",
        "type": "CertificateDetailV2"
    }],
    "type": "CertificateInfoV2"
}

FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'

vCenter = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_update = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '444', 'version': '5.1.0'}]

scvmm = [{'username': 'dcs', 'password': 'dcs', 'type': 'SCVMM', 'name': 'SCVMM', 'port': '443', 'version': '5.1.0'}]

scvmm_update = [{'username': 'dcs', 'password': 'dcs', 'type': 'SCVMM', 'name': 'SCVMM', 'port': '444', 'version': '5.1.0'}]

FEATURE_TOGGLES = ["OVF206_HypervisorManager_SBAC", "OVF205_ClusterProfileSBAC", "OVF217_CentralizedScope", "OVF2_SBAC_Core", "API_Version_600", "OVF167_Scope_Admin_Roles", "OVF23_ScopeRestrictionsEnabledPerCategory", "OVF218_Server_Profile_Roles", "OVF1160_Server_Profile_Architect_Role", "OVF1563_ClusterProfilesUI", "OVF1040_CLRM_Enable_Public_API"]
