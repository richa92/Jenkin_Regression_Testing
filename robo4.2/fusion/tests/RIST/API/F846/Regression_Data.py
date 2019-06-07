######################################
from RoboGalaxyLibrary import BuiltIn

MIGRATATION_VC_DOMAINS_TYPE = 'MigratableVcDomainV300'

ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

vc_backup_file = {"WPST26": "vc-config-backup_wpst26.conf",
                  "WPST23": "vc-config-backup_wpst23.conf",
                  "WPST22": "vc-config-backup_wpst22.conf",
                  }

migrationBody = {"migrationState": "Migrated",
                 "uri": None,
                 "category": "migratable-vc-domains",
                 "type": MIGRATATION_VC_DOMAINS_TYPE,
                 "acknowledgements": [{"key": "VirtualConnectBackup"},
                                      {"key": "ResourcesNotModified"},
                                      {"key": "LatentServerError"},
                                      {"key": "InServiceMigration"},
                                      {"key": "ProfileNotMigrated"}]
                 }

all_hardware_info = {"WPST26": {"category": "migratable-vc-domains",
                                "iloLicenseType": "OneView",
                                "enclosureGroupName": "Test",
                                "type": MIGRATATION_VC_DOMAINS_TYPE,
                                "credentials": {"oaIpAddress": "wpst26-oa1.vse.rdlabs.hpecorp.net",
                                                "oaUsername": "Administrator",
                                                "oaPassword": "hpvse14",
                                                "vcmIpAddress": "16.125.69.247",
                                                "vcmUsername": "Administrator",
                                                "vcmPassword": "5CSCNW6X",
                                                "type": "EnclosureCredentials"}
                                },
                     "WPST23": {"category": "migratable-vc-domains",
                                "iloLicenseType": "OneView",
                                "enclosureGroupName": "Test",
                                "type": MIGRATATION_VC_DOMAINS_TYPE,
                                "credentials": {"oaIpAddress": "wpst23-oa1.vse.rdlabs.hpecorp.net",
                                                "oaUsername": "Administrator",
                                                "oaPassword": "hpvse14",
                                                "vcmIpAddress": "16.125.72.98",
                                                "vcmUsername": "Administrator",
                                                "vcmPassword": "CBB30FPZ",
                                                "type": "EnclosureCredentials"}

                                },
                     "WPST22": {"category": "migratable-vc-domains",
                                "iloLicenseType": "OneView",
                                "enclosureGroupName": "Test",
                                "type": MIGRATATION_VC_DOMAINS_TYPE,
                                "credentials": {"oaIpAddress": "wpst22-oa1.vse.rdlabs.hpecorp.net",
                                                "oaUsername": "Administrator",
                                                "oaPassword": "hpvse14",
                                                "vcmIpAddress": "16.125.77.72",
                                                "vcmUsername": "Administrator",
                                                "vcmPassword": "WB6RFMPG",
                                                "type": "EnclosureCredentials"}
                                }
                     }

# Generate credentials information
vc_credentials = {}
oa_credentials = {}
for key in all_hardware_info.keys():
    vc_credentials[key] = {"vcmIpAddress": all_hardware_info[key]['credentials'].get("vcmIpAddress"),
                           "vcmUsername": all_hardware_info[key]['credentials'].get("vcmUsername"),
                           "vcmPassword": all_hardware_info[key]['credentials'].get("vcmPassword"),
                           }
    oa_credentials[key] = {"oaIpAddress": all_hardware_info[key]['credentials'].get("oaIpAddress"),
                           "oaUsername": all_hardware_info[key]['credentials'].get("oaUsername"),
                           "oaPassword": all_hardware_info[key]['credentials'].get("oaPassword"),
                           }


expect_sever_hardware_types = {"WPST26": {"name": ["BL420c Gen8 1", "BL460c G7 1", "BL465c G7 1", "BL460c Gen8 1", "BL465c Gen8 1", "BL460c Gen9 1", "BL660c Gen8 1", "BL660c Gen9 1"]},
                               "WPST23": {"name": ["BL420c Gen8 1", "BL465c Gen8 1", "BL465c Gen8 2", "BL460c Gen9 1"]},
                               "WPST22": {"name": ["BL420c Gen8 1", "BL465c Gen8 1", "BL465c Gen8 2", "BL460c Gen9 1", "BL460c Gen10 1"]}
                               }

expect_sever_profiles = {"WPST26": {"name": ["Profile_bay1", "Profile_bay3", "Profile_bay5", "Profile_bay7", "Profile_bay8", "Profile_bay10"]},
                         "WPST23": {"name": ["Profile_bay1", "Profile_bay2", "Profile_bay3", "Profile_bay4", "Profile_bay5"]},
                         "WPST22": {"name": ["Profile_bay1", "Profile_bay2", "Profile_bay3", "Profile_bay4", "Profile_bay5"]}
                         }
