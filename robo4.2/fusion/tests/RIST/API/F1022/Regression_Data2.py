LOGICAL_ENCLOSURE_TYPE = 'LogicalEnclosureV4'
UPLINK_SET_TYPE = 'uplink-setV5'

ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

newLicenses = {'licenseType': 'Synergy 8Gb FC Upgrade',
               'license': [{'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
                           {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}],
               'invalidLicense': [{'key': 'YYYY D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]
               }

Enclosure_Tbird = 'CN75120D7B, CN75120D77, CN750163KD'   # Tbird15 Ring

Enclosure_list = ["ENC:" + enclosure.strip(' ') for enclosure in Enclosure_Tbird.split(',')]
LIG_name = 'LIG_POTASH'
FC_Name = 'FA1'
EG_name = 'EG_SYNERGY'
LE_name = 'LE_SYNERGY'
LI_name = '%s-%s' % (LE_name, LIG_name)
US_name = 'fc_uplink'

logical_enc_put = {
    "type": LOGICAL_ENCLOSURE_TYPE,
    "name": LE_name,
    "enclosureGroupUri": "EG:" + EG_name,
    "enclosureUris": Enclosure_list,
    "enclosures": {
        Enclosure_Tbird.split(',')[0].strip(' '): {
            "enclosureUri": Enclosure_Tbird.split(',')[0].strip(' '),
            "interconnectBays": [{"bayNumber": 1, "licenseIntent": "No"},
                                 {"bayNumber": 2, "licenseIntent": "No"},
                                 {"bayNumber": 3, "licenseIntent": "Yes"},
                                 {"bayNumber": 4, "licenseIntent": "No"},
                                 {"bayNumber": 5, "licenseIntent": "No"},
                                 {"bayNumber": 6, "licenseIntent": "No"}
                                 ]
        },
        Enclosure_Tbird.split(',')[1].strip(' '): {
            "enclosureUri": Enclosure_Tbird.split(',')[1].strip(' '),
            "interconnectBays": [{"bayNumber": 1, "licenseIntent": "No"},
                                 {"bayNumber": 2, "licenseIntent": "No"},
                                 {"bayNumber": 3, "licenseIntent": "No"},
                                 {"bayNumber": 4, "licenseIntent": "No"},
                                 {"bayNumber": 5, "licenseIntent": "No"},
                                 {"bayNumber": 6, "licenseIntent": "Yes"}
                                 ]
        },
        Enclosure_Tbird.split(',')[2].strip(' '): {
            "enclosureUri": Enclosure_Tbird.split(',')[2].strip(' '),
            "interconnectBays": [{"bayNumber": 1, "licenseIntent": "No"},
                                 {"bayNumber": 2, "licenseIntent": "No"},
                                 {"bayNumber": 3, "licenseIntent": "No"},
                                 {"bayNumber": 4, "licenseIntent": "No"},
                                 {"bayNumber": 5, "licenseIntent": "No"},
                                 {"bayNumber": 6, "licenseIntent": "No"}
                                 ]
        }
    },
    "firmware": {
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
    },
    "deploymentManagerSettings": {
        "osDeploymentSettings": {
            "deploymentModeSettings": None,
            "manageOSDeployment": False
        }
    }
}

fc_uplinkset = {
    "type": UPLINK_SET_TYPE,
    "name": US_name,
    "portConfigInfos": [
        {"desiredSpeed": "Auto",
         "location": {"locationEntries": [
             {"value": "Q2:1", "type": "Port"},
             {"value": 3, "type": "Bay"},
             {"value": "ENC:%s" % Enclosure_Tbird.split(',')[0].strip(' '), "type": "Enclosure"}]
         }
         }
    ],
    "networkType": "FibreChannel",
    "primaryPortLocation": None,
    "reachability": None,
    "manualLoginRedistributionState": "Supported",
    "logicalInterconnectUri": "EG:%s" % LI_name,
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "networkUris": [],
    "fcNetworkUris": ["FC:%s" % FC_Name],
    "fcoeNetworkUris": []
}
