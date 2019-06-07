# Workaround while changes for template.py is still in progress
SERVER_POWERON_WAIT_TIMEOUT = '60m'
SERVER_POWERON_WAIT_INTERVAL = '2s'

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

# Fusion Interconnect Decoder Ring
CARBON = 'Virtual Connect SE 16Gb FC Module for Synergy'
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NITRO = 'Virtual Connect SE 100Gb F32 Module for Synergy'
HAFNIUM_ICM_MODELS = [POTASH, NITRO]

# Server default credentials
SERVER_USERNAME = 'root'
SERVER_PASSWORD = 'rootpwd'

# Hafnium detault credentials
HAFNIUM_USERNAME = 'root'
HAFNIUM_PASSWORD = 'UnoVista'

# Server tools directory
SERVER_TOOLS_DIR = '/root/tools'

# Server scripts directory
SERVER_SCRIPTS_DIR = SERVER_TOOLS_DIR + '/scripts'

# MeatGrinder location
MEATGRINDER_DIR = SERVER_TOOLS_DIR + '/LinuxMG_2.610_x86-64'

# Multipath script
MULTIPATH_SCRIPT = SERVER_SCRIPTS_DIR + '/check-multipath.sh'

# Check Bonds script
CHECK_BONDS_SCRIPT = SERVER_SCRIPTS_DIR + '/check_bonds.py'
SERVER_HAFILE = SERVER_SCRIPTS_DIR + '/HA_ipaddr.conf'

# CHECK_MULTIPATH: IPs to check for multipath
# Example from Eagle11 setup:
# CHECK_MULTIPATH = {'192.168.1.140':2, '192.168.1.200':3, '172.18.25.2':4, '192.168.1.190':4, '192.168.11.103':4, '192.168.1.125':2, '192.168.1.105':2, '192.168.1.150':4, '192.168.1.158':4, '192.168.1.128':4}

# CHECK_READONLY: IPs to check for readonly FS
# Example from Eagle11 setup:
# CHECK_READONLY = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# HINT: For ease of collecting these IPs, use tools/tcs/get-pxe-ip.sh
# CHECK_MEATGRINDER: IPs to check for error in the latest MeatGrinder log
# Example from Eagle11 setup:
# CHECK_MEATGRINDER = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# PING_HAFILE: Sequential ping will be run as part of the test using the HA file provided in this variable
# Example from Eagle11 setup:
# PING_HAFILE = '/root/ci-fit/fusion/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr.conf'

# Parallel ICM reset

Parallel_Aside = ['3', '1', '2']

Parallel_Bside = ['6', '4', '5']
