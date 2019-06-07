from copy import deepcopy

FABRIC_DUMP_WAIT = '5m'

# download directory
SD_DIR = '/var/tmp'

OV_APPLIANCE_DIR = 'appliance/ci/'

OV_APPLIANCE_LOG = \
    OV_APPLIANCE_DIR + 'logs/ciDebug.log'

Fabric_name = 'plexxi_fabric'

CFM_DUMP_DIR = 'composable-cloud/var/tmp/support-dumps-fabric/' + Fabric_name + '/'

CFM_LOG_PATTERN = '* ' + CFM_DUMP_DIR + 'composable-fabric-manager-support-bundle-*.tar.gz*'

UNENCRYPT_ERRCODE = 'FB-UN-7890'
ENCRYPT_ERRCODE = 'FB-EN'

FABRIC_SD_UNENCRYPT_RB = {'errorCode': UNENCRYPT_ERRCODE, 'encrypt': 'false'}
FABRIC_SD_ENCRYPT_RB = {'errorCode': ENCRYPT_ERRCODE, 'encrypt': 'true'}

appliance_ip = '15.186.20.236'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

cfm_ip = '15.186.17.206'
cfm_credentials = {'userName': 'admin', 'password': 'plexxi'}

oneview_config = {
    "host": appliance_ip,
    "username": admin_credentials['userName'],
    "password": admin_credentials['password'],
    "enabled": True,
    "verify_ssl": True,
    "name": "HPE OneView Configuration"
}

fabric_claim_request = [{"op": "replace", "path": "/state", "value": "Adding"}]

err_rb_list = [
    {
        'exp_error': 'CRM_SUPPORT_DUMP_VALIDATION_ERROR',
        'rb': {'errorCode': 'FB345678901'}
    },
    {
        'exp_error': 'CRM_SUPPORT_DUMP_VALIDATION_ERROR',
        'rb': {'errorCode': ''}
    },
    {
        'exp_error': 'CRM_SUPPORT_DUMP_VALIDATION_ERROR',
        'rb': {'encrypt': 'false'}
    },
    {
        'exp_error': 'CRM_SUPPORT_DUMP_VALIDATION_ERROR',
        'rb': {'errorCode': 'FB_4567890'}
    },
    {
        'exp_error': 'CRM_SUPPORT_DUMP_VALIDATION_ERROR',
        'rb': {'errorCode': 'F$'}
    },
    {
        'exp_error': 'CRM_SUPPORT_DUMP_VALIDATION_ERROR',
        'rb': {'errorCode': 'FB+'}
    },
    {
        'exp_error': 'CRM_SUPPORT_DUMP_VALIDATION_ERROR',
        'rb': {'errorCode': 'F!%&?=(*@}'}
    }
]
