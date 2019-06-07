"""
This file is used to define different environment variables used to run API feature tests
on C7000
"""
from copy import deepcopy
from robot.libraries.BuiltIn import BuiltIn

try:
    APPLIANCE_VIP = BuiltIn().get_variable_value("${APPLIANCE_IP}")
except:  # noqa
    APPLIANCE_VIP = '0.0.0.0'

# ## Onview Appliance
# IPv4
# APPLIANCE1_IP = ''
# APPLIANCE2_IP = ''
# APPLIANCE_VIP = ''
APPLIANCE_HOSTNAME = "FVT-C7000-Regression"
IPV4_TYPE = 'STATIC'
IPV4_SUBNET = "255.255.240.0"
IPV4_GATEWAY = "16.114.208.1"
# IPv6
IPV6_TYPE = 'UNCONFIGURE'
IPV6_SUBNET = None
IPV6_GATEWAY = None
APP1_IPV4_ADDRESS = APPLIANCE_VIP
HOSTNAME = APPLIANCE_HOSTNAME
# Enclosures
ENC1 = 'wpst22'
ENC1_OA1 = "16.125.77.71"
ENC2 = 'wpst23'
ENC2_OA1 = "16.125.77.80"
ENC3 = 'wpst26'
ENC3_OA1 = "16.125.79.45"

# ## License ##

licenses = [
    {
        'key':
            '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 '
            'M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS '
            'FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 '
            'HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'
    },
    {
        'key':
            'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 '
            '74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS '
            'FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 '
            'HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
]

# ## Credentials ##

ADMIN_CREDENTIALS_COMMON = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
OA_CREDENTIALS_COMMON = {'username': 'Administrator', 'password': 'hpvse14'}
ILO_CREDENTIALS_COMMON = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
# cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}

HPMCTP_CREDENTIALS_COMMON = {
    'ip': '16.114.216.129',
    'username': 'root',
    'password': 'hpvse1'
}

# ## NTP ##
NTP_SERVER = '16.110.135.123'
NTP_SERVER_HOSTNAME = 'ntp.hpecorp.net'

# ## DNS ##
# IPv4
IPV4_DNS1 = "16.125.25.81"
IPV4_DNS2 = "16.125.25.82"
IPV4_DNS3 = "16.125.24.20"
DOMAIN_NAME = "vse.rdlabs.hpecorp.net"
# IPv6

# TZ
TIME_ZONE = 'UTC'
LOCALE_EN = 'en_US.UTF-8'

# Reserved location of SPP bundles for FVT Regression testing
spp_path = r'Z:\firmware\SPP\FVT-Regression'

# StRM
#
# ## SAN MANAGERS ##
SAN_MANAGER_BNA = 'Brocade Network Advisor'
SAN_MANAGER_HPE = 'HPE'
SAN_MANAGER_BNA_IP = '16.125.65.9'
SAN_MANAGER_HPE_IP = '16.125.25.45'

FA_SAN_A = 'wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'
FA_SAN_B = 'wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'

# ## STORAGE SYSTEMS ##
# StoreServ
STORESERV1_NAME = 'wpst3par-7200-7-srv'
STORESERV1_HOSTNAME = 'wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net'
STORESERV1_POOL1 = 'FVT_C7000_reg1_r1'
STORESERV1_POOL2 = 'FVT_C7000_reg1_r5'
STORESERV1_POOL3 = 'FVT_C7000_reg1_r6'
STORESERV1_MANAGED_DOMAIN = 'FVT_C7000_reg1'
STORESERV1_CREDENTIALS = {'username': 'fusionadm', 'password': 'hpvse1'}

STORESERV2_NAME = "fvt3par-8400-1-srv"
STORESERV2_POOL1 = 'FC_r1'
STORESERV2_POOL5 = 'FC_r5'
# STORESERV2_MANAGED_DOMAIN = 'NO DOMAIN'

DISCOVERED_DOMAINS = [
    "NO DOMAIN",
    "wpst20",
    "wpst22",
    "wpst23",
    "wpst26",
    "wpst30",
    "wpst31",
    "wpst32",
    "wpst33",
    "wpst34",
    "wpst8",
    "wpst9",
]

# StoreVirtual
STOREVIRTUAL_SLPT_STATIC_NAME = 'VSA_Cluster_173-2'
STOREVIRTUAL_SLPT_STATIC_HOSTNAME = '16.71.149.173'
STOREVIRTUAL_SLPT_STATIC_VIP = '192.168.21.71'
STOREVIRTUAL_SLPT_STATIC_POOL = 'VSA_Cluster_173-2'
STOREVIRTUAL_SLPT_DHCP_NAME = 'VSA_Cluster_116'
STOREVIRTUAL_SLPT_DHCP_HOSTNAME = '16.71.148.116'
STOREVIRTUAL_SLPT_DHCP_VIP = '192.168.21.59'
STOREVIRTUAL_SLPT_DHCP_POOL = 'VSA_Cluster_116'
STOREVIRTUAL_MLPT_NAME = 'VSA84_Storage_Pool'
STOREVIRTUAL_MLPT_HOSTNAME = '16.71.151.84'
STOREVIRTUAL_MLPT_VIP = '16.71.151.84'
STOREVIRTUAL_MLPT_POOL = 'VSA84_Storage_Pool'

STOREVIRTUAL_SLPT_STATIC_CREDENTIALS = {"username": "admin", "password": 'admin'}
STOREVIRTUAL_SLPT_DHCP_CREDENTIALS = {"username": "admin", "password": 'admin'}
STOREVIRTUAL_MLPT_CREDENTIALS = {"username": "admin", "password": 'admin'}

STOREVIRTUAL_SLPT_DHCP_CLIQ_CREDENTIALS = deepcopy(STOREVIRTUAL_SLPT_DHCP_CREDENTIALS)
STOREVIRTUAL_SLPT_DHCP_CLIQ_CREDENTIALS['mgmt_ip'] = STOREVIRTUAL_SLPT_DHCP_HOSTNAME

STOREVIRTUAL_SLPT_STATIC_CLIQ_CREDENTIALS = deepcopy(STOREVIRTUAL_SLPT_STATIC_CREDENTIALS)
STOREVIRTUAL_SLPT_STATIC_CLIQ_CREDENTIALS['mgmt_ip'] = STOREVIRTUAL_SLPT_STATIC_HOSTNAME

STOREVIRTUAL_MLPT_CLIQ_CREDENTIALS = deepcopy(STOREVIRTUAL_MLPT_CREDENTIALS)
STOREVIRTUAL_MLPT_CLIQ_CREDENTIALS['mgmt_ip'] = STOREVIRTUAL_MLPT_HOSTNAME

STOREVIRTUAL_ROOT_VOLUME_TEMPLATE = "Volume root template for StoreVirtual 1.2"
STORESERV_ROOT_VOLUME_TEMPLATE = "Volume root template for StoreServ 3.3.1"

# ## Networks
FCOE_DOMAIN = "NO DOMAIN"

# LIGs and EGs
LIG1_NAME = 'LIG22'
EG1_NAME = 'EG22'
LIG2_NAME = 'LIG23'
EG2_NAME = 'EG23'
LIG3_NAME = 'LIG26'
EG3_NAME = 'EG26'