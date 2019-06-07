from FusionLibrary.libs.utils.common import get_firmware_bundle

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
task_states = ['Warning', 'Completed']
verify_interconnect = ['wpst32, interconnect 1', 'wpst32, interconnect 5']
enc_name = "wpst32"
icm_name = "wpst32, interconnect 1"
enc_fw = "4.70"
icm_fw = "4.60"
enc_managed_state = "Configured"
ilo_managed_state = "NoProfileApplied"
vc_managed_state = "Configured"

spp_folder = r'Z:\firmware\SPP\Gen10Snap1'
spp_prefix = 'SPP2017070'
fw_bundle = get_firmware_bundle(spp_folder, spp_prefix)

# Firmware Bundles
Snap1SPP = '/rest/firmware-drivers/SPP2016100_2016_0917_171'
FirmwareVersion = '2017.07.0'
le_name = 'wpst32'

# LE firmware data
firmware_data = {
    "firmwareBaselineUri": Snap1SPP,
    "firmwareUpdateOn": "SharedInfrastructure",
    "forceInstallFirmware": True,
    "logicalInterconnectUpdateMode": "Parallel"
}

# Firmware Bundles List
Snap1 = [
    {
        'SPPFileName': 'SPPGen10Snap1.2016_0901.20.iso',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen10Snap1/',
        'SPPFileMD5': 'b9d7e9d34d94d4298e0c9a606f293c72',
        'FirmwareBundleURI': Snap1SPP
    }
]
ValidateFirmwares = [
    "Online ROM Flash Component for Linux - HPE Synergy 480 Gen10 (I42) Compute Module ",
    "Online ROM Flash Component for Windows x64 - HPE Synergy 660 Gen10 (I43) Compute Module",
    "Online ROM Flash Component for Linux - HPE ProLiant DL380 Gen10 (U30) Servers",
    "Online ROM Flash Component for Windows x64 - HPE ProLiant BL460c Gen10 (I41) Servers"
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
wpst26Encls = [
    {
        'hostname': '16.114.209.54',
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
WPST32Encls = [
    {
        'hostname': 'wpst32-oa1.vse.rdlabs.hpecorp.net',
        'name': 'wpst32',
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
Managed26 = [
    {
        'hostname': 'wpst26-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst32',
        'force': True,
        'licensingIntent': 'OneView'
    }
]
Managed32 = [
    {
        'hostname': 'wpst32-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst32',
        'force': True,
        'licensingIntent': 'OneView'
    }
]
Managed32WithSPP = [
    {
        'hostname': 'wpst32-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst32',
        'force': True,
        'licensingIntent': 'OneView',
        'firmwareBaselineUri': FirmwareVersion,
        'forceInstallFirmware': False,
        'updateFirmwareOn': 'EnclosureOnly'
    }
]
MonitoredC7000 = [
    {
        'hostname': 'wpst32-oa1.vse.rdlabs.hpecorp.net',
        'username': 'Administrator',
        'password': 'hpvse14',
        'enclosureGroupUri': 'EG:GRP-wpst32',
        'force': True,
        'state': 'Monitored',
        'licensingIntent': 'OneView'
    }
]
