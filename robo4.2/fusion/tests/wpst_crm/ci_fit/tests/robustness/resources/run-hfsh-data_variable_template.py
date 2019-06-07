# For IPv6, use this '[your:ipv6:addr]'
APPLIANCE_IP = '15.186.9.xx'


# Your local repo toplevel
TOPLEVEL_DIR = '/root/ci-fit/virtualenv/fusion-410/fusion'

# SSHLibrary related variables
SSH_READ_WAIT = '2.0s'

FUSION_USERNAME = 'Administrator'
FUSION_PASSWORD = 'hpvse123'

FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'

FUSION_PROMPT = '#'
FUSION_TIMEOUT = 180
FUSION_NIC = 'bond0'
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

HF_USERNAME = 'root'
HF_PASSWORD = 'UnoVista'
ICM_SCRIPTS_DIR = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/interconnect/scripts'
ICM_PASSWD_SCRIPT = 'get-icm-passwd.sh'

ENC_SERIAL = 'MXQ65202KW'
ICM_BAY_NUMBER = '3'
ICM_NAME = ENC_SERIAL + ', interconnect ' + ICM_BAY_NUMBER
SRC_INTERFACE = 'eth0'

ENC_ICM_PASSWD = {
    ENC_SERIAL + '_' + ICM_BAY_NUMBER: {
        'EnclosureSN': ENC_SERIAL,
        'ipv6LinkLocal': 'fe80::5eb9:1ff:fe28:cebd',
        'Bay': ICM_BAY_NUMBER
    }
}

HFSH_COMMANDS = ['show clock', 'show interface description', 'show clock', 'show etherchannel summary', 'show clock']
