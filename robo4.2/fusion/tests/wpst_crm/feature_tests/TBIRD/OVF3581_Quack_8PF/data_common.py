admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

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
# DF REVISIT SERVER_BOOT_SHORT_WAIT = '3min'
SERVER_BOOT_SHORT_WAIT = '5min'
SERVER_BOOT_WAIT = '8min'
BFS_SERVER_BOOT_WAIT = '15min'
# change to 3min in F; changed to 5min @pb132
UPLINK_STATUS_WAIT = '5min'
UPLINK_LAG_WAIT = '1min'
UPLINK_SHORT_WAIT = '60s'
SP_CREATE_WAIT = '10m'
SPT_CREATE_WAIT = '5m'

# 0 sec is not enough for nameServer to be updated after enable back downlink
SUBPORT_STATUS_WAIT = '240s'
CONN_DEPLOY_WAIT = '300s'
DEL_SP_QUIESCE = '60s'

HA_SYNC_WAIT = '90s'

# FA environment
REMOVE_IC_WAIT = '5m'
POWEROFF_IC_WAIT = '3m'
INSERT_IC_WAIT = '30m'
ADD_PORT_WAIT = '240s'

OPSPEED8 = 'Speed8G'
OPSPEED4 = 'Speed4G'

ENET_Q_SPEED = 'Speed40G'
ENET_Q_SPLIT_SPEED = 'Speed10G'

CHLORIDE10 = 'CL10'
CHLORIDE20 = 'CL20'

SP_TYPE = 'ServerProfileV10'
SPT_TYPE = 'ServerProfileTemplateV6'


# return profile connection requested bw not to exceed the max bandwidth
def get_enet_rbw(cl_type, total_conn):
    if cl_type == CHLORIDE10:
        max_bw = 10000
    else:
        max_bw = 20000
    rbw = max_bw / total_conn
    return rbw
