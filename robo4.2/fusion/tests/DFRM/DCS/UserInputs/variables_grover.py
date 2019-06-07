""" DFRM - Grover or Natasha-J variables and constants file."""
# Grover (Natasha J) Keywords
# Constants or Varibales
NATASHA_J_PROD_NAME = 'Synergy 24Gb SAS Interconnect Module'
NATASHA_J_PART_NO = '755986-B21'
NATASHA_J_ICM_TYPE = 'Synergy 24Gb SAS Interconnect Module'
# LIG Payload
GROVER_DUALDOMAIN_LIG_PAYLOAD = {
    "type": "sas-logical-interconnect-groupV2",
    "description": None,
    "status": None,
    "state": None,
    "eTag": None,
    "created": None,
    "modified": None,
    "category": None,
    "uri": None,
    "interconnectMapTemplate": {
            "interconnectMapEntryTemplates": [{
                "logicalLocation": {
                    "locationEntries": [{
                        "type": "Bay",
                        "relativeValue": 1
                    }, {
                        "type": "Enclosure",
                        "relativeValue": 1
                    }]
                },
                "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy24GbSASInterconnectModule",
                "enclosureIndex": 1
            }, {
                "logicalLocation": {
                    "locationEntries": [{
                        "type": "Bay",
                        "relativeValue": 4
                    }, {
                        "type": "Enclosure",
                        "relativeValue": 1
                    }]
                },
                "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy24GbSASInterconnectModule",
                "enclosureIndex": 1
            }]
    },
    "name": "LIG_Grover",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": 1,
    "initialScopeUris": []
}

GROVER_SINGLEDOMAINBAY1_LIG_PAYLOAD = {
    "type": "sas-logical-interconnect-groupV2",
    "description": None,
    "status": None,
    "state": None,
    "eTag": None,
    "created": None,
    "modified": None,
    "category": None,
    "uri": None,
    "interconnectMapTemplate": {
            "interconnectMapEntryTemplates": [{
                "logicalLocation": {
                    "locationEntries": [{
                        "type": "Bay",
                        "relativeValue": 1
                    }, {
                        "type": "Enclosure",
                        "relativeValue": 1
                    }]
                },
                "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy24GbSASInterconnectModule",
                "enclosureIndex": 1
            }]
    },
    "name": "LIG_Grover",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": 1,
    "initialScopeUris": []
}
GROVER_SINGLEDOMAINBAY4_LIG_PAYLOAD = {
    "type": "sas-logical-interconnect-groupV2",
    "description": None,
    "status": None,
    "state": None,
    "eTag": None,
    "created": None,
    "modified": None,
    "category": None,
    "uri": None,
    "interconnectMapTemplate": {
            "interconnectMapEntryTemplates": [{
                "logicalLocation": {
                    "locationEntries": [{
                        "type": "Bay",
                        "relativeValue": 4
                    }, {
                        "type": "Enclosure",
                        "relativeValue": 1
                    }]
                },
                "permittedInterconnectTypeUri": "/rest/sas-interconnect-types/Synergy24GbSASInterconnectModule",
                "enclosureIndex": 1
            }]
    },
    "name": "LIG_Grover",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": 1,
    "initialScopeUris": []
}
