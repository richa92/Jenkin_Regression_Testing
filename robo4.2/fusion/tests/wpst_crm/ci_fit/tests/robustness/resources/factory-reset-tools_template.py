APPLIANCE_IP = '15.186.9.XX'
EMAIL_TO = 'email@hpe.com'

# Fusion defaults
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

FACTORY_RESET_ENCS = '/ci/bin/tbird/appliance-hal.sh factory-reset-enclosures'
APPLIANCE_FACTORY_RESET_TIMEOUT = '60m'
APPLIANCE_FACTORY_RESET_SLEEP = '30s'
NEW_ADMINISTRATOR_CREDENTIAL = {
    "newPassword": FUSION_PASSWORD,
    "oldPassword": "admin",
    "userName": FUSION_USERNAME
}
# Get trusted component token - needed if you don't have devmode-package installed
GET_TRUSTED_TOKEN = 'psql -A -t --dbname=cidb --user=postgres -c "select session_id from session.session where username=\'erm\'";'
