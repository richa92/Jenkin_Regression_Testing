"""
This file is used to define different environment variables used  to run API feature tests
on Ring1, Ring2, DCS
"""
from copy import deepcopy
from robot.libraries.BuiltIn import BuiltIn
try:
    TEST_RING = BuiltIn().get_variable_value("${X_TEST_RING}")
except:    # noqa
    TEST_RING = 'DCS'

if TEST_RING == 'Ring1':
    # ## Onview Appliance Ring1
    # IPv4
    APPLIANCE1_IP = '16.114.210.227'
    APPLIANCE2_IP = '16.114.210.228'
    APPLIANCE_VIP = '16.114.209.223'
    APPLIANCE_HOSTNAME = "fvt-ring1.vse.rdlabs.hpecorp.net"
    IPV4_TYPE = 'STATIC'
    IPV4_SUBNET = "255.255.240.0"
    IPV4_GATEWAY = "16.114.208.1"
    # IPv6
    IPV6_TYPE = 'UNCONFIGURE'
    IPV6_SUBNET = None
    IPV6_GATEWAY = None
    # Enclosures
    ENC1 = 'CN754406XL'
    ENC2 = 'CN754404R6'
    ENC3 = 'CN754406WB'
    licenses = [
        {
            'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
        },
        {
            'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
        },
    ]
elif TEST_RING == 'Ring2':
    # ## Onview Appliance Ring2
    # IPv4
    APPLIANCE1_IP = '16.114.210.229'
    APPLIANCE2_IP = '16.114.210.230'
    APPLIANCE_VIP = '16.114.209.231'
    APPLIANCE_HOSTNAME = "fvt-ring2.vse.rdlabs.hpecorp.net"
    IPV4_TYPE = 'STATIC'
    IPV4_SUBNET = "255.255.240.0"
    IPV4_GATEWAY = "16.114.208.1"
    # IPv6
    IPV6_TYPE = 'UNCONFIGURE'
    IPV6_SUBNET = None
    IPV6_GATEWAY = None
    # Enclosures
    ENC1 = 'CN75120D7B'
    ENC2 = 'CN75120D77'
    ENC3 = 'CN750163KD'
    licenses = [
        {
            'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
        },
        {
            'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
        },
    ]
else:
    # ## Onview Appliance DCS
    # IPv4
    APPLIANCE1_IP = '16.114.213.38'
    APPLIANCE2_IP = '16.114.213.39'
    APPLIANCE_VIP = '16.114.218.122'
    APPLIANCE_HOSTNAME = "fvt-dcs.vse.rdlabs.hpecorp.net"
    IPV4_TYPE = 'STATIC'
    IPV4_SUBNET = "255.255.240.0"
    IPV4_GATEWAY = "16.114.208.1"
    # IPv6
    IPV6_TYPE = 'UNCONFIGURE'
    IPV6_SUBNET = None
    IPV6_GATEWAY = None
    # License

# ## Credentials ##
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
# cliq_credentials = {
#     'mgmt_ip': '16.71.149.173',
#     'username': 'admin',
#     'password': 'admin'}
hpmctp_credentials = {
    'ip': '16.114.216.129',
    'username': 'root',
    'password': 'hpvse1'
}
network_credentials = {'userName': 'Networkadmin', 'password': 'wpsthpvse1'}
server_credentials = {'userName': 'Serveradmin', 'password': 'wpsthpvse1'}

# Common credentails will be used in all features # START #
ADMIN_CREDENTIALS_COMMON = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ILO_CREDENTIALS_COMMON = {'username': 'Administrator', 'password': 'hpvse123'}
HPMCTP_CREDENTIALS_COMMON = {
    'ip': '16.114.216.129',
    'username': 'root',
    'password': 'hpvse1'
}
NETWORK_CREDENTIALS_COMMON = {'userName': 'Networkadmin', 'password': 'wpsthpvse1'}
SERVER_CREDENTIALS_COMMON = {'userName': 'Serveradmin', 'password': 'wpsthpvse1'}
# Common credentails will be used in all features # END #

# ## NTP ##
NTP_SERVER = '16.110.135.123'
NTP_SERVER_HOSTNAME = 'ntp.hpecorp.net'

# ## DNS ##
# IPv4
IPV4_DNS1 = "16.125.25.81"
IPV4_DNS2 = "16.125.25.82"
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

# ## STORAGE SYSTEMS ##
# StoreServ
STORESERV1_NAME = 'wpst3par-7200-7-srv'
STORESERV1_HOSTNAME = 'wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net'
STORESERV1_POOL1 = 'FVT_Tbird_reg1_r1'
STORESERV1_POOL2 = 'FVT_Tbird_reg1_r5'
STORESERV1_POOL3 = 'FVT_Tbird_reg1_r6'
STORESERV1_MANAGED_DOMAIN = 'Tbird_Regression_Domain'
STORESERV1_CREDENTIALS = {'username': 'fusionadm', 'password': 'hpvse1'}

STORESERV2_NAME = "fvt3par-8400-1-srv"
STORESERV2_POOL1 = 'FC_r1'
STORESERV2_POOL5 = 'FC_r5'
# STORESERV2_MANAGED_DOMAIN = 'NO DOMAIN'

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

# ## Networks
FCOE_DOMAIN = "NO DOMAIN"

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
CARBON_LIG_NAME = 'LIG_CARBON'
EG_NAME = 'EG1'
LE_NAME = 'LE1'
