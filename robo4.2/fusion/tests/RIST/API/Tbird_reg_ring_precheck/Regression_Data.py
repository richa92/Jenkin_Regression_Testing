admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3


# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Other interconnects
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC3ICBAY6 = '%s, interconnect 6' % ENC1
ENC3ICBAY3 = '%s, interconnect 3' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

enclosures = [{"name": ENC1},
              {"name": ENC2},
              {"name": ENC3}]


server_hardware = [{"name": ENC1SHBAY3},
                   {"name": ENC1SHBAY5},
                   {"name": ENC1SHBAY6},
                   {"name": ENC1SHBAY7},
                   {"name": ENC2SHBAY1},
                   {"name": ENC3SHBAY1},
                   {"name": ENC3SHBAY5}]


drive_enclosures = [{
    "name": ENC1DEBAY1,
    "category": "drive-enclosures",
    "state": "Monitored",
    "interconnectBaySet": 1,
    "interconnectUri": [
        "SasIC:CN754406XL, interconnect 4",
        "SasIC:CN754406XL, interconnect 1"
    ],
    "type": "drive-enclosure",
    "enclosureUri": "ENC:CN754406XL",
    "status": "REGEX:(OK|Warning)"}]

sasics = [{
    "category": "sas-interconnects",
    "type": "sas-interconnect",
    "enclosureUri": "ENC:CN754406XL",
    "status": "OK",
    "description": None,
    "productName": "Synergy 12Gb SAS Connection Module",
    "partNumber": "755985-B21",
    "interconnectLocation": {
        "locationEntries": []
    },
    "powerState": "On",
    "name": "CN754406XL, interconnect 1",
    "portCount": 12,
    "serialNumber": "TWT546W05L",
    "uri": "SasIC:CN754406XL, interconnect 1",
    "enclosureName": "CN754406XL",

},
    {
    "category": "sas-interconnects",
    "type": "sas-interconnect",
    "enclosureUri": "ENC:CN754406XL",
    "status": "OK",
    "description": None,
    "productName": "Synergy 12Gb SAS Connection Module",
    "partNumber": "755985-B21",
    "interconnectLocation": {
        "locationEntries": []
    },
    "powerState": "On",
    "name": "CN754406XL, interconnect 4",
    "portCount": 12,
    "serialNumber": "TWT546W05S",
    "uri": "SasIC:CN754406XL, interconnect 4",
    "enclosureName": "CN754406XL",

}]
Potash_ICs = [{"name": ENC1ICBAY3},
              {"name": ENC2ICBAY6}]

Other_ICs = [{"name": ENC1ICBAY6},
             {"name": ENC2ICBAY3},
             {"name": ENC3ICBAY6},
             {"name": ENC3ICBAY3}]
