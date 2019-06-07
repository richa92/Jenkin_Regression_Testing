
###########################################################################
# Data_Variables.py
# All the required data and user input needs to be specified in this file
# before triggerring the sFlow Automation Suite.
###########################################################################

APPLIANCE_IP = '90.1.0.102'

Appliance_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

OV_root_usr = 'root'
OV_root_pwd = 'hpvse1'
PotashUserName = 'OneView'
INTERCONNECT1 = 'SGH724SERS, interconnect 4'
INTERCONNECT2 = 'SGH724SERY, interconnect 1'

OneViewPrompt = '~]#'
SWITCH_PROMPT = 'OneView#'

#------------------------------------------------------------
IVR_VLAN = 'vlan1250'
IVR_IPV4 = '10.10.1.5'
IVR_IPV4_SUBNET_MASK = '255.255.255.0'
#------------------------------------------------------------
RECEIVER_INDEX = 1     # Supported Values 1-3
RECEIVER_NAME = 'Receiver1'
RECEIVER_ADDRESS = '0A0A011E'    #Address should be given in HEX format.
#------------------------------------------------------------
COUNTER_POLLER_INTERFACE = 'FortyGigE 0/0/1'    # Only physical Interface should be given as Input, No S-channels.
COUNTER_POLLER_INTERFACE_2 = 'FortyGigE 1/0/1'    # Only physical Interface should be given as Input, No S-channels.
COUNTER_POLLER_INTERVAL = 20    # Starts from 20
#------------------------------------------------------------
FLOW_SAMPLER_INTERFACE = 'FortyGigE 0/0/1'    # Only physical Interface should be given as Input, No S-channels.
FLOW_SAMPLER_INTERFACE_2 = 'FortyGigE 1/0/1'    # Only physical Interface should be given as Input, No S-channels.
#------------------------------------------------------------