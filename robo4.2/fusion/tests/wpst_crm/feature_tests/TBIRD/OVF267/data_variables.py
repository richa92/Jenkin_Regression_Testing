import os
import sys
sys.path.append(os.path.dirname(__file__))

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
#FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC


appliance_ip = '15.245.131.12'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}


frame = 3

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': 'hpcorp',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.248.0',
               'ipv4Gateway': '15.245.128.1',
               'ipv4NameServers': ['16.110.135.52'],
               'virtIpv4Addr': '15.245.131.152',
               'app1Ipv4Addr': '15.245.131.153',
               'app2Ipv4Addr': '15.245.131.154',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'feature.usa.hpe.com',
               'confOneNode': True,
               'domainName': 'usa.hpe.com',
               'aliasDisabled': True,
               }],
             }