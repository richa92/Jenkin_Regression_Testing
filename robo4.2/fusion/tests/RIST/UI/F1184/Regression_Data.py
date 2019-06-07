admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Firmware Bundles
OldSnap6SPP = '/rest/firmware-drivers/SPPgen9snap6_2016_0825_153'
Snap6SPP = '/rest/firmware-drivers/SPP2016100_2016_1015_191'

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
