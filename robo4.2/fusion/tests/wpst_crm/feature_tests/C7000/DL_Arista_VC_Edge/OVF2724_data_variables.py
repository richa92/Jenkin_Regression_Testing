import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

# APPLIANCE_IP_4_10 = '15.186.17.190'

APPLIANCE_IP_4_0 = '15.186.17.44'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

OV_4_10 = '4.10'
OV_4_00 = '4.00'

'''
DL Server H/W IP's in the order of 2 DL 380, 2 DL 580, 2 DL 360, 2 DL 560

DL 380  1 - RedHat 7.4
DL 380  2 - ESXI
DL 580  1 - Win 2016
DL 580  2 - RedHat 7.4
DL 360  1 - Win2012
DL 360  2 - Win2016
DL 560  1 - Win2012
DL 560  2 - ESXI

'''
# DL_server_names = ['ILO2M2733056Q','ILO2M2733056R','ILOCN771702NH','ILOCN771702NK','ILOMXQ7340093','ILOMXQ733085B','ILOMXQ724053V','ILOMXQ724053L']
# DL_SH_IP = ['15.186.14.42','15.186.15.75','15.186.15.82','15.186.15.55','15.186.15.14','15.186.15.49','15.186.15.59','15.186.15.110']
'''
*** DL Servers for PI 03 ***
2 DL 380 , 2 DL 360
*** DL Servers for PI 03 ***
'''

DL_SH_IP = ['15.186.17.202', '15.186.15.75', '15.186.15.14', '15.186.15.49']

invalid_SH = ['password', '1.1.1.1']
SH_error_msg = ['UNABLE_TO_DISCOVER', 'UNABLE_TO_TRUST_CERT_RACK']

DL_SH_body = {"hostname": "enc-ilo.corp.com",
              "username": "Administrator",
              "password": "hpvse123",
              "force": True,
              "licensingIntent": "OneView",
              # "licensingIntent":"OneViewNoiLO",
              "configurationState": "Managed",
              }

server_models = ['ProLiant DL380 Gen10', 'ProLiant DL360 Gen10']
# 380 360 HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr
# adapter_models = ['HPE FlxFbr 10/25Gb 2p 622FLR-SFP28 Adptr', 'HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr']
adapter_models = ['HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr', 'HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr']
valDict = {'taskState': 'Completed'}

sw_type = 'Ethernet'
slotNumber = '1'
serverState = 'OK'
mphosts_addresses = {'DHCP': '', 'LinkLocal': '', 'Lookup': ''}

bin_410 = 'HPEOneView-fullupdate-4.10.00-SNAPSHOT-0316344.bin'
Upload_Sleep_Time = '2800'
version_Check = '4.10.00-0316344'
switches_IP = ['15.186.17.219', '15.186.17.208']

SHT_names = "DL360 Gen10 1"
