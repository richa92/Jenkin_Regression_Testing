add_ethernet = {
     'name':None,
     'vlanId':None,
     'purpose': 'General',
     'smartLink':False,
     'privateNetwork':False,
     'connectionTemplateUri':None,
     'created': None,
     'modified': None,
     'status': 'OK',
     'state': None,
     'type': 'ethernet-networkV3',
     'uri':None,
     'category': 'ethernet-networks',
     'eTag': None,
     'description': None,
     'ethernetNetworkType': 'Tagged'
    }

add_fcoenet = {
    'name':None,
    'type': 'fcoe-network',
    'status': 'OK',
    'description': None,
    'created': None,
    'uri':None,
    'vlanId':None,
    'fabricUri':None,
    'managedSanUri':None,
    'modified': None,
    'state': None,
    'eTag': None,
    'connectionTemplateUri':None,
    'category': 'fcoe-networks',
         }

def get_variables():

    variables = {
    "DTO_ETHERNET_ADD": add_ethernet,
    "DTO_FCOENET_ADD": add_fcoenet
}

    return variables