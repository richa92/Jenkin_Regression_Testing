"""Variables for working with the One View instance

    = Usage =
    | *** Settings ***      |
    | variables | ../resource/open_switch_variables.py |
    | pybot --variablefile ../resource/open_switch_variables.py |
"""

TOR_SWITCH_IP = '172.17.15.80'
SESSION_ALIAS = 'OPS_SESSION'
LOGIN_TOKEN = 'Actual Value set dynamically at suite setup'
NETOP_USER = 'netop'
SSH_TIMEOUT = 5

VLANS_URL = '/rest/v1/system/bridges/bridge_normal/vlans/'
INTERFACES_URL = '/rest/v1/system/interfaces/'
DEFAULT_VLAN_URL = '/rest/v1/system/bridges/bridge_normal/vlans/DEFAULT_VLAN_1'

EXP_INITIAL_PORT_COUNT = 0
EXP_INITIAL_VLAN_COUNT = 1
