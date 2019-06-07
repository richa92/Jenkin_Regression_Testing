admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Firmware Bundles
Snap1SPP = '/rest/firmware-drivers/SPP2016100_2016_0917_171'
FirmwareVersion = '2017.07.0'
le_name = 'wpst32'

# Hardware add error message
OAFirmwareError = "The enclosure's OA firmware version is 3.71 which is below the minimum supported version for managing an enclosure. A firmware bundle containing OA firmware version 4.01 or newer is not available."
OAFirmwareResolution = "Add a firmware bundle. Or,manually update the OA firmware."
DLFirmwareError = "below the minimum supported version for managing server hardware. A firmware bundle containing iLO firmware"
DLFirmwareResolution = "Add a firmware bundle. Or,manually update the iLO firmware."

# Firmware Bundles List
Snap1 = [
    {
        'SPPFileName': 'SPPGen10Snap1.2016_0901.20.iso',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen10Snap1/',
        'SPPFileMD5': 'b9d7e9d34d94d4298e0c9a606f293c72',
        'FirmwareBundleURI': Snap1SPP
    }
]
G7BLServer = [
    {
        'server name': 'wpst26, bay 9',
        'iloIP': '16.125.75.213',
        'iloUserName': 'Administrator',
        'iloPassword': 'hpvse1-ilo',
        'firmwareURI': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo3/ilo3_157.bin'
    }
]
G8BLServer = [
    {
        'server name': 'wpst32, bay 1',
        'iloIP': '16.114.220.24',
        'iloUserName': 'Administrator',
        'iloPassword': 'hpvse1-ilo',
        'firmwareURI': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_120.bin'
    }
]
G9BLServer = [
    {
        'server name': 'wpst32, bay 5',
        'iloIP': '16.114.221.82',
        'iloUserName': 'Administrator',
        'iloPassword': 'hpvse1-ilo',
        'firmwareURI': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_202.bin'
    }
]
G9SYServer = [
    {
        'server name': 'CN744502D4, bay 1',
        'iloIP': '16.114.213.103',
        'iloUserName': 'Administrator',
        'iloPassword': 'hpvse123',
        'firmwareURI': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_202.bin'
    }
]
G7DLServer = [
    {
        'server name': 'wpstdl54-ilo',
        'iloIP': '16.114.212.7',
        'iloUserName': 'Administrator',
        'iloPassword': 'hpvse1-ilo',
        'firmwareURI': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo3/ilo3_157.bin',
        'hostname': '16.114.212.7',
        'username': 'Administrator',
        'password': 'hpvse1-ilo',
        'force': True,
        'licensingIntent': 'OneView',
        'configurationState': 'Managed'
    }
]
G7DLAdd = [
    {
        'hostname': '16.114.212.7',
        'username': 'Administrator',
        'password': 'hpvse1-ilo',
        'force': True,
        'licensingIntent': 'OneView',
        'configurationState': 'Managed'
    }
]
G8DLServer = [
    {
        'server name': 'wpstdl18-ilo',
        'iloIP': '16.125.79.40',
        'iloUserName': 'Administrator',
        'iloPassword': 'hpvse1-ilo',
        'firmwareURI': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_120.bin',
        'hostname': '16.125.79.40',
        'username': 'Administrator',
        'password': 'hpvse1-ilo',
        'force': True,
        'licensingIntent': 'OneView',
        'configurationState': 'Managed'
    }
]
G8DLAdd = [
    {
        'hostname': '16.125.79.40',
        'username': 'Administrator',
        'password': 'hpvse1-ilo',
        'force': True,
        'licensingIntent': 'OneView',
        'configurationState': 'Managed'
    }
]
G9DLServer = [
    {
        'server name': 'wpstdl60-ilo',
        'iloIP': '16.114.212.14',
        'iloUserName': 'Administrator',
        'iloPassword': 'hpvse1-ilo',
        'firmwareURI': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo4/ilo4_202.bin',
        'hostname': '16.114.212.14',
        'username': 'Administrator',
        'password': 'hpvse1-ilo',
        'force': True,
        'licensingIntent': 'OneView',
        'configurationState': 'Managed'
    }
]
G9DLAdd = [
    {
        'hostname': '16.114.212.14',
        'username': 'Administrator',
        'password': 'hpvse1-ilo',
        'force': True,
        'licensingIntent': 'OneView',
        'configurationState': 'Managed'
    }
]
Wpst26 = [
    {
        'hostname': '16.125.79.45',
        'username': 'Administrator',
        'password': 'hpvse14',
        'force_update': 'FORCE',
        'firmware_url': 'http://wpstwork4.vse.rdlabs.hpecorp.net/firmware/oa/hpoa371_20130219.bin',
        'vc_firmware_url': 'http://wpstwork4.vse.rdlabs.hpecorp.net/firmware/vc/vcfwall361_20140404.bin',
        'method': 'health',
        'enclosureGroupUri': 'EG:GRP-wpst26',
        'force': True,
        'licensingIntent': 'OneView'
    }
]
Wpst32 = [
    {
        'hostname': '16.114.209.54',
        'username': 'Administrator',
        'password': 'hpvse14',
        'force_update': 'FORCE',
        'firmware_url': 'http://wpstwork4.vse.rdlabs.hpecorp.net/firmware/oa/hpoa371_20130219.bin',
        'vc_firmware_url': 'http://wpstwork4.vse.rdlabs.hpecorp.net/firmware/vc/vcfwall361_20140404.bin',
        'method': 'health',
        'enclosureGroupUri': 'EG:GRP-wpst32',
        'force': True,
        'licensingIntent': 'OneView'
    }
]
ManagedC7000 = [
    {
        'hostname': 'wpst26-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst26',
        'force': True,
        'licensingIntent': 'OneView'
    }
]
MonitoredC7000 = [
    {
        'hostname': 'wpst26-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst26',
        'force': True,
        'state': 'Monitored',
        'licensingIntent': 'OneView'
    }
]
