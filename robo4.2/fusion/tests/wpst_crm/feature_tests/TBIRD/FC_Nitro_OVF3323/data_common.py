admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

SAN_NPIV_OUT_FILE = '/tmp/npiv.txt'
DA_ATTACHED_DEV_OUTFILE_PREFIX = '/tmp/da_ns_attdev_'
DA_ATTACHED_DEV_OUTFILE_SUFFIX = '.txt'
THREEPAR_NS_CMD = 'showportdev ns'

# portStatus
LINKED = 'Linked'
UNLINKED = 'Unlinked'
SUBPORT_OK = 'Ok'

# portStatusReason
SMARTLINK = 'SmartLink'
ACTIVE = 'Active'
DISABLED = 'AdminDisabled'

# lagStates
LACP = ['LacpActivity', 'Aggregation', 'Synchronization', 'Collecting', 'Distributing']

# stackingDomainRole
MASTER = 'Master'
SUBORDINATE = 'Subordinate'

# For traffic verification: pattern matching for ping statistics and allowed loss
NT_ZERO_PERCENT_LOSS = 'Lost = * (0% loss)'
LINUX_ZERO_PERCENT_LOSS = '0% packet loss'

# For S-Channel LAG connection, most of the time is 0 or 1 packet loss, rarely 2, set to 2
ALLOWED_PACKET_LOSS_SCHANNEL_LAG = 2

# Wait time for reaching stable state
SERVER_BOOT_SHORT_WAIT = '3min'
# Gen9 server is much slower than Gen10 server; ESXi servers took longer to boot
SERVER_BOOT_WAIT = '5min'
# SERVER_BOOT_WAIT = '8min' ESXi server took long to come up around 10 min
# BFS_SERVER_BOOT_WAIT = '12min'
# WS BFS server took shorter than Linux
BFS_SERVER_BOOT_WAIT = '6min'
# change to 3min in F, change to 5min for Nitro
# UPLINK_STATUS_WAIT = '3min'
# change to 6min - OV PB32 HF61 took more than 5min for DA uplinks
UPLINK_STATUS_WAIT = '6min'
UPLINK_SHORT_WAIT = '60s'
SP_CREATE_WAIT = '10m'
SPT_CREATE_WAIT = '5m'
LOGIN_WAIT = '1m'
UPLINK_SPEED_WAIT = '3m'
UPLINK_ERROR_WAIT = '2m'

# 0 sec is not enough for nameServer to be updated after enable back downlink
SUBPORT_STATUS_WAIT = '240s'
CONN_DEPLOY_WAIT = '300s'

HA_SYNC_WAIT = '60s'
LI_DLS_CHANGE_WAIT = '60s'
DLS_LANE_CHANGE_WAIT = '90s'
DLS_UPGRADE_OUTAGE_WAIT = '90s'
DLS_DOWNGRADE_OUTAGE_WAIT = '90s'
# First time after LI DLS change, took more than 90s for servers DL p speed to change
# especially for Quag2 server to 50Gb
SERVERS_INIT_DLS_WAIT = '4m'
IC_SHORT_WAIT = '60s'

# FA environment
REMOVE_IC_WAIT = '5m'
POWEROFF_IC_WAIT = '5m'
INSERT_IC_WAIT = '15m'
ADD_PORT_WAIT = '240s'
RESET_IC_WAIT = '10m'
UFG_WAIT = '15m'

# uplink speed
OPSPEED8 = 'Speed8G'
OPSPEED16 = 'Speed16G'
OPSPEED32 = 'Speed32G'
OPSPEED2 = 'Speed2G'
OPSPEED4 = 'Speed4G'
OPSPEED2_5 = 'Speed2_5G'
OPSPEED10 = 'Speed10G'

# profile connection requested bandwidth
RBW2 = '2000'
RBW4 = '4000'
RBW8 = '8000'
RBW9 = '9000'
RBW16 = '16000'
RBW32 = '32000'

NITRO_MODEL = 'Virtual Connect SE 100Gb F32 Module for Synergy'
NITRO_PART = '867796-B21'
CL50_MODEL = 'Synergy 50Gb Interconnect Link Module'

SP_TYPE = 'ServerProfileV10'

CHLORIDE10 = 'CL10'
CHLORIDE20 = 'CL20'

###############################
# speed change error msg
###############################
# DF REVIST: move to data_common
MSG_CRM_SPEED_CHANGE_SP_RBW_EXCEED_PHYSICAL_BW = \
    'The requested logical interconnect downlink speed of \d+ Gb/s is less than the sum of all ' + \
    'requested bandwidth settings for connections on the downlink ports associated with this ' + \
    'logical interconnect.'
