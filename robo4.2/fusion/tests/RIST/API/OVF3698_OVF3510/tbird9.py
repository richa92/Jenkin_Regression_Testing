admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Enclosures
ENC1 = 'CN744502CG'

# Potash interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1

verify_enc = [{"type": "EnclosureV7", "name": ENC1,
               "category": "enclosures",
               "refreshState": "NotRefreshing",
               "enclosureType": "SY12000",
               "uuid": "000000CN744502CG",
               "serialNumber": "CN744502CG",
               "partNumber": "000000-010",
               "licensingIntent": "NotApplicable",
               "deviceBayCount": 12,
               "interconnectBayCount": 6,
               "fanBayCount": 10,
               "powerSupplyBayCount": 6,
               "applianceBays": [
                    {
                    "bayNumber": 1,
                    "model": "Synergy Composer II",
                    "devicePresence": "Present",
                    "status": "OK",
                    "serialNumber": "9V76NP0054",
                    "partNumber": "872957-B21",
                    "sparePartNumber": "879540-001",
                    "bayPowerState": "Unknown",
                    "poweredOn": True
                    },
                    {
                    "bayNumber": 2,
                    "model": None,
                    "devicePresence": "Absent",
                    "status": None,
                    "serialNumber": None,
                    "partNumber": None,
                    "sparePartNumber": None,
                    "bayPowerState": "Unknown",
                    "poweredOn": False
                    }
                    ],
               "applianceBayCount": 2}]
