from FusionLibrary.libs.utils.common import get_firmware_bundle
from FusionLibrary.libs.utils.common import get_firmware_version_by_file_name

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
task_states = ['Warning', 'Completed']

spp_folder = r'Z:\firmware\SPP\SHQA_Regression'
fw_bundle = get_firmware_bundle(spp_folder)
FirmwareVersion = get_firmware_version_by_file_name(fw_bundle)

le_name = 'LE_SYNERGY'
