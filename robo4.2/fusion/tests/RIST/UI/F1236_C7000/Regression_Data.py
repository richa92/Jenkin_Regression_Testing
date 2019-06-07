admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Firmware Bundles
OldSnap6SPP = '/rest/firmware-drivers/SPPgen9snap6_2016_0825_153'
Snap6SPP = '/rest/firmware-drivers/SPP2016100_2016_1015_191'

# iLO Update Bins
iLO230 = 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_230_p37_checked.bin'
iLO240 = 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_240_p12_checked.bin'
iLO250 = 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_250.bin'

iloUserName = 'Administrator'
iloPassword = 'hpvse1-ilo'

Gen8BLName = 'wpst22, bay 1'
Gen9BLName = 'wpst22, bay 5'
Gen8DLName = 'wpstdl18-ilo'
Gen9DLName = 'wpstdl50-ilo'
Gen8BLIP = '16.125.73.242'
Gen9BLIP = '16.125.75.249'
Gen8DLIP = '16.125.79.40'
Gen9DLIP = '16.114.212.3'

# Firmware Bundles List
OldSnap6 = [
    {
        'SPPFileName': 'SPPgen9snap6.2016_0825.153.iso',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen9Snap6/',
        'SPPFileMD5': 'c2e3d4bc2290619041fe0ceeb8364c34',
        'FirmwareBundleURI': OldSnap6SPP
    }
]
Snap6 = [
    {
        'SPPFileName': 'SPPgen9snap6.2016_0617.118.iso',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen9Snap6/',
        'SPPFileMD5': 'b9d7e9d34d94d4298e0c9a606f293c72',
        'FirmwareBundleURI': Snap6SPP
    }
]
# Server Hardware Update iLO List
GEN8BL230Server = [
    {
        'server name': Gen8BLName,
        'iloIP': Gen8BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO230
    }
]
GEN8BL240Server = [
    {
        'server name': Gen8BLName,
        'iloIP': Gen8BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO240
    }
]
GEN8BL250Server = [
    {
        'server name': Gen8BLName,
        'iloIP': Gen8BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO250
    }
]
GEN8DL230Server = [
    {
        'server name': Gen8DLName,
        'iloIP': Gen8DLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO230
    }
]
GEN8DL240Server = [
    {
        'server name': Gen8DLName,
        'iloIP': Gen8DLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO240
    }
]
GEN8DL250Server = [
    {
        'server name': Gen8DLName,
        'iloIP': Gen8DLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO250
    }
]
GEN9BL230Server = [
    {
        'server name': Gen9BLName,
        'iloIP': Gen9BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO230
    }
]
GEN9BL240Server = [
    {
        'server name': Gen9BLName,
        'iloIP': Gen9BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO240
    }
]
GEN9BL250Server = [
    {
        'server name': Gen9BLName,
        'iloIP': Gen9BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO250
    }
]
GEN9DL230Server = [
    {
        'server name': Gen9DLName,
        'iloIP': Gen9DLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO230
    }
]
GEN9DL240Server = [
    {
        'server name': Gen9BLName,
        'iloIP': Gen9BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO240
    }
]
GEN9DL250Server = [
    {
        'server name': Gen9BLName,
        'iloIP': Gen9BLIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPassword,
        'firmwareURI': iLO250
    }
]
GEN8DLServer = [
    {
        'hostname': Gen8DLIP,
        'licensingIntent': 'OneView',
        'username': iloUserName,
        'password': iloPassword,
        'force': True,
        'configurationState': 'Managed'
    }
]
GEN9DLServer = [
    {
        'hostname': Gen9DLIP,
        'licensingIntent': 'OneView',
        'username': iloUserName,
        'password': iloPassword,
        'force': True,
        'configurationState': 'Managed'
    }
]
