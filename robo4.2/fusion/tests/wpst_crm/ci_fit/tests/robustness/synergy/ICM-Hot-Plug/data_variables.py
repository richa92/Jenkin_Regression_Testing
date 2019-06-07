# Fusion defaults
#FUSION_IP = '15.199.230.101'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
#FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

#Multipath IP to number of expected paths mapping.
#This needs to be set to the appropriate server IP you have in your test environment with its corresponding number of multipath.
#Example below for 10.1.3.2:
#[root@VCUTTT0000 ~]# ifconfig bond0
#bond0     Link encap:Ethernet  HWaddr B2:99:99:00:00:03
#          inet addr:10.1.3.2  Bcast:10.1.3.255  Mask:255.255.255.0
#          inet6 addr: fe80::b099:99ff:fe00:3/64 Scope:Link
#          UP BROADCAST RUNNING MASTER MULTICAST  MTU:1500  Metric:1
#          RX packets:2244913 errors:0 dropped:0 overruns:0 frame:0
#          TX packets:1026 errors:0 dropped:0 overruns:0 carrier:0
#          collisions:0 txqueuelen:0
#          RX bytes:152607069 (145.5 MiB)  TX bytes:90743 (88.6 KiB)
#
#[root@VCUTTT0000 ~]# multipath -ll
#mpatha (360002ac000000000000000360000326a) dm-0 3PARdata,VV
#size=40G features='0' hwhandler='0' wp=rw
#`-+- policy='round-robin 0' prio=1 status=active
#  |- 2:0:0:0 sda 8:0  active ready running
#  `- 3:0:0:0 sdb 8:16 active ready running
#[root@VCUTTT0000 ~]#
#SERVER_IPS = {'10.1.3.2':2, '10.2.37.3':3, '10.3.25.3':4, '10.4.13.2':4, '10.5.1.2':4, '10.2.37.2':2,  '10.1.3.3':2, '10.5.1.3':4, '10.3.25.2':4, '10.4.13.3':4}
SERVER_IPS = {}
