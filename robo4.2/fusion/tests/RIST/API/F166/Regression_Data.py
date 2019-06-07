######################################
from RoboGalaxyLibrary import BuiltIn

MIGRATATION_VC_DOMAINS_TYPE = 'MigratableVcDomainV300'

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}

vc_backup_file = {"WPST26": "vc-config-backup_wpst26.conf",
                  "WPST261": "vc-config-backup_wpst26_1.conf",
                  "WPST22": "vc-config-backup_wpst22.conf",
                  }

migrationBody = {"migrationState": "Migrated",
                 "uri": None,
                 "category": "migratable-vc-domains",
                 "type": MIGRATATION_VC_DOMAINS_TYPE,
                 "acknowledgements": [{"key": "VirtualConnectBackup"},
                                      {"key": "ResourcesNotModified"},
                                      {"key": "ProfileNotMigrated"},
                                      {"key": "InServiceMigration"},
                                      {"key": "LatentServerError"},
                                      {"key": "Bios"}]
                 }

migratingBody = [{"op": "replace", "path": "/migrationState", "value": "Migrating"}]


all_hardware_info = {"WPST26": {"category": "migratable-vc-domains",
                                "iloLicenseType": "OneViewNoiLO",
                                "enclosureGroupUri": None,
                                "type": MIGRATATION_VC_DOMAINS_TYPE,
                                "credentials": {"oaIpAddress": "wpst26-oa1.vse.rdlabs.hpecorp.net",
                                                "oaUsername": "Administrator",
                                                "oaPassword": "hpvse14",
                                                "vcmIpAddress": "16.125.69.247",
                                                "vcmUsername": "Administrator",
                                                "vcmPassword": "5CSCNW6X",
                                                "type": "EnclosureCredentials"}
                                },
                     "WPST22": {"category": "migratable-vc-domains",
                                "iloLicenseType": "OneViewNoiLO",
                                "enclosureGroupUri": None,
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

expect_sever_hardware = {"WPST26": {"name": ["wpst26, bay 1", "wpst26, bay 2", "wpst26, bay 3", "wpst26, bay 4", "wpst26, bay 5", "wpst26, bay 7", "wpst26, bay 8", "wpst26, bay 9", "wpst26, bay 10"]},
                         "WPST22": {"name": ["wpst22, bay 1", "wpst22, bay 2", "wpst22, bay 3", "wpst22, bay 4", "wpst22, bay 5", "wpst22, bay 6", "wpst22, bay 8"]}
                         }
expect_sever_profiles = {"WPST26": {"name": ["Profile_bay2gen8", "Profile_bay3", "Profile_bay5", "Profile_bay8", "Profile_bay10"]},
                         "WPST22": {"name": ["Profile_bay5gen9"]}
                         }
PXE_bay8_profiles = "Profile_bay8"
PXE_bay10_profiles = "Profile_bay10"

wpst22Encls = [
    {
        'hostname': 'wpst22-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'force_update': 'FORCE',
        'method': 'health',
        'enclosureGroupUri': 'EG:GRP-wpst22',
        'force': True,
        'licensingIntent': 'OneView'
    }
]

Monitored22 = [
    {"hostname": "wpst22-oa1.vse.rdlabs.hpecorp.net",
     "username": "Administrator",
     "password": "hpvse14",
     "enclosureGroupUri": None,
     "force": False,
     "licensingIntent": "OneViewStandard",
     "initialScopeUris": [],
     "state": "Monitored"
     }
]

wpst26Encls = [
    {
        'hostname': 'wpst26-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'force_update': 'FORCE',
        'method': 'health',
        'enclosureGroupUri': 'EG:GRP-wpst26',
        'force': True,
        'licensingIntent': 'OneView'
    }
]

Monitored26 = [
    {"hostname": "wpst26-oa1.vse.rdlabs.hpecorp.net",
     "username": "Administrator",
     "password": "hpvse14",
     "enclosureGroupUri": None,
     "force": False,
     "licensingIntent": "OneViewStandard",
     "initialScopeUris": [],
     "state": "Monitored"
     }
]
