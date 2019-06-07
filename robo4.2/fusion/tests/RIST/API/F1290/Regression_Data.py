admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

######################################
add_scope_uri = '/rest/scopes'
add_scope_body = {'type': 'ScopeV2', 'name': 'MyRISTScope', 'description': 'Sample Scope description'}
test_scope_name = 'MyRISTScope'
update_scope_resource = {"op": "add", "path": "/scopeUris/-", "value": []}
######################################

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

SH1 = 'CN754404R6, bay 1'

enclosures = [
    {
        "type": "EnclosureV400",
        "name": "CN754406XL",
        "enclosureTypeUri": "/rest/enclosures/000000CN754406XL",
        "managerBays":
            [
                {"bayNumber": 1, "linkPortState": "Unlinked", "mgmtPortStatus": "OK", "linkPortStatus": "OK"},
                {"bayNumber": 2, "linkPortState": None, "mgmtPortStatus": None, "linkPortStatus": None}
            ],
        "deviceBays":
            [
                {
                    "category": "device-bays",
                    "model": "Synergy 480 Gen9",
                    "coveredByProfile": None,
                    "bayPowerState": "On",
                    "coveredByDevice": "SH:tbird16, bay 1",
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
                    "deviceUri": "/rest/server-hardware/36343537-3338-4E43-3735-343430343454",
                    "bayNumber": 1,
                    "serialConsole": True
                }
            ],
    }
]
