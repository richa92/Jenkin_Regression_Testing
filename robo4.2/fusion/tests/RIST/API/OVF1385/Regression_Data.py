######################################
from RoboGalaxyLibrary import BuiltIn

MIGRATATION_VC_DOMAINS_TYPE = 'MigratableVcDomainV300'

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}

vc_backup_file = {
    "WPST23": "vc-config-backup_wpst23.conf",
}

vc_backup_file_uefi = {
    "WPST23": "vc-config-backup_wpst23_uefi.conf",
}

vc_backup_file_uefi_mchap = {
    "WPST23": "vc-config-backup_wpst23_uefi_mchap.conf",
}

vc_backup_file_uefi_tunnel = {
    "WPST23": "vc-config-backup_wpst23_uefi_tunnel.conf",
}

migrationBody = {
    "migrationState": "Migrated",
    "uri": None,
    "category": "migratable-vc-domains",
    "type": MIGRATATION_VC_DOMAINS_TYPE,
    "acknowledgements": [{"key": "VirtualConnectBackup"},
                         {"key": "ResourcesNotModified"},
                         {"key": "LatentServerError"},
                         {"key": "InServiceMigration"},
                         {"key": "ProfileNotMigrated"},
                         {"key": "Bios"}]
}

migratingBody = [{"op": "replace", "path": "/migrationState", "value": "Migrating"}]

all_hardware_info = {
    "WPST23": {
        "category": "migratable-vc-domains",
        "iloLicenseType": "OneViewNoiLO",
        "enclosureGroupUri": None,
        "type": MIGRATATION_VC_DOMAINS_TYPE,
        "credentials": {
            "oaIpAddress": "wpst23-oa1.vse.rdlabs.hpecorp.net",
            "oaUsername": "Administrator",
            "oaPassword": "hpvse14",
            "vcmIpAddress": "16.125.72.98",
            "vcmUsername": "Administrator",
            "vcmPassword": "CBB30FPZ",
            "type": "EnclosureCredentials"
        }
    },
}

# Generate credentials information
vc_credentials = {}
oa_credentials = {}
for key in all_hardware_info.keys():
    vc_credentials[key] = {
        "vcmIpAddress": all_hardware_info[key]['credentials'].get("vcmIpAddress"),
        "vcmUsername": all_hardware_info[key]['credentials'].get("vcmUsername"),
        "vcmPassword": all_hardware_info[key]['credentials'].get("vcmPassword"),
    }
    oa_credentials[key] = {
        "oaIpAddress": all_hardware_info[key]['credentials'].get("oaIpAddress"),
        "oaUsername": all_hardware_info[key]['credentials'].get("oaUsername"),
        "oaPassword": all_hardware_info[key]['credentials'].get("oaPassword"),
    }

expect_sever_hardware = {
    "WPST23": {
        "name": ["wpst23, bay 1", "wpst23, bay 2", "wpst23, bay 3", "wpst23, bay 4", "wpst23, bay 5", "wpst23, bay 6",
                 "wpst23, bay 7"]
    },
}

expect_sever_profiles = {
    "WPST23": {"name": ["Profile_bay5_F1385"]},
}
expect_iscsi_info = {
    "iscsi": {
        "initiatorNameSource": "UserDefined",
        "initiatorName": "iqn.2015-02.com.hpe:oneview-wpst23-bay5-dhcp",
        "bootTargetName": "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:1141:wpst23-bay5-dhcp2",
        "bootTargetLun": "0",
        "firstBootTargetIp": "192.168.21.59",
        "firstBootTargetPort": "3260",
        "chapLevel": "None"
    }
}

expect_iscsi_info_mchap = {
    "iscsi": {
        "initiatorNameSource": "UserDefined",
        "initiatorName": "iqn.2015-02.com.hpe:oneview-wpst23-bay5-dhcp",
        "bootTargetName": "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:1141:wpst23-bay5-dhcp2",
        "bootTargetLun": "0",
        "firstBootTargetIp": "192.168.21.59",
        "firstBootTargetPort": "3260",
        "chapLevel": "MutualChap",
        "chapName": "iqn.2015-02.com.hpe:oneview-wpst23-bay5-dhcp",
        "mutualChapName": "iqn.2015-02.com.hpe:oneview-wpst23-bay5-dhcp"
    }
}
