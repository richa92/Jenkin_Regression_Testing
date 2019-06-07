admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

######################################
add_scope_uri = '/rest/scopes'
add_scope_body = {'type': 'ScopeV2', 'name': 'MyRISTScope', 'description': 'Sample Scope description'}
test_scope_name = 'MyRISTScope'
update_scope_resource = {"op": "add", "path": "/scopeUris/-", "value": []}
######################################

# Enclosures wpst22
ENC1 = 'wpst22'

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1

enclosures = [
    {
        "type": "EnclosureC7000",
        "name": "wpst22",
        "enclosureTypeUri": "/rest/enclosures/09USE320440A",
        "managerBays":
            [
                {"bayNumber": 1, "linkPortState": "Unlinked", "mgmtPortStatus": "OK", "linkPortStatus": "OK"},
                {"bayNumber": 2, "linkPortState": None, "mgmtPortStatus": None, "linkPortStatus": None}
            ],
        "deviceBays":
            [
                {
                    "category": "device-bays",
                    "model": "BL465c Gen8",
                    "coveredByProfile": None,
                    "bayPowerState": "On",
                    "coveredByDevice": "SH:wpst22, bay 1",
                    "deviceFormFactor": "SingleHeightSingleWide",
                    "availableForHalfHeightDoubleWideProfile": False,
                    "ipv4Setting": None,
                    "availableForFullHeightProfile": False,
                    "changeState": "None",
                    "profileUri": None,
                    "availableForHalfHeightProfile": True,
                    "deviceBayType": "SY12000DeviceBay",
                    "powerAllocationWatts": 98,
                    "availableForFullHeightDoubleWideProfile": False,
                    "devicePresence": "Present",
                    "type": "DeviceBayV300",
                    "deviceUri": "/rest/server-hardware/39343336-3537-5355-4533-31383332414C",
                    "bayNumber": 1,
                    "serialConsole": True
                }
            ],
    }
]