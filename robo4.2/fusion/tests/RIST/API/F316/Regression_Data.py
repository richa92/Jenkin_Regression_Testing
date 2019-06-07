admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

######################################
power_body = {"op": "replace", "path": "/powerState", "value": "Off"}
reset_body = {"op": "replace", "path": "/deviceResetState", "value": "Reset"}
powerUID_body = {"op": "replace", "path": "/uidState", "value": "Off"}
password_body = {"op": "replace", "path": "/rootAccessState", "value": "Enable"}
######################################

# Enclosures                            Tbird4
ENC1 = 'CN744502D4'
ICBAY = '%s, interconnect 3' % ENC1
# Interconnects
# Create SP and update firmware using Gen 9 snap 6 as the baseline and configure local storage
InterconnectBay = {
    "state": "Monitored",
    "interconnectUri": ICBAY,
    "description": "InterconnectBay",
    "productName": "Synergy 40Gb F8 Switch",
    "defaultPowerState": "On",
    "defaultUIDPowerState": "Off",
    "PowerOn": "On",
    "PowerOff": "Off",
    "UIDPowerOn": "On",
    "UIDPowerOff": "Off",
    "enablePW": "Enable",
    "disablePW": "Disable",
    "raPW": "rootAccessPassword"
}
