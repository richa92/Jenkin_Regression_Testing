"""
Fusion Library shell
"""
from FusionLibrary import FusionLibrary
import inspect
from pprint import pprint

appliance = '15.245.131.206'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
lib = FusionLibrary()
resp = lib.fusion_api_login_appliance(appliance, admin_credentials)
vers = [120, 200, 201, 300, 400, 500, 600, 800]
api = lib.fusion_api_get_server_hardware()
ips = {x['name']: i['address']
       for x in api['members']
       for i in x['mpHostInfo']['mpIpAddresses'] if i['type'] == 'LinkLocal'}

print(ips)
api = lib.fusion_api_get_ethernet_networks(param="?filter=vlanId eq 1")
idx = lib.fusion_api_get_resource(uri="/rest/index/trees/rest/ethernet-networks/56c51857-388d-4bf3-8d27-b1495b37b64f")

idx2 = lib.fusion_api_get_resource(uri="/rest/index/associations?parenturi=/rest/ethernet-networks/56c51857-388d-4bf3-8d27-b1495b37b64f")
api = lib.fusion_api_get_ethernet_networks(uri="/rest/ethernet-networks/56c51857-388d-4bf3-8d27-b1495b37b64f",
                                           param="&f_an=NETWORKSET_TO_NETWORK")
pass

"""
x = {v: api(api=v)['members'][0] for v in vers}

dto = x[800]
e2 = {'name': 'net_100',
      'purpose': 'General',
      'smartLink': True,
      'privateNetwork': False,
      'connectionTemplateUri': None,
      'ethernetNetworkType': 'Tagged',
      'vlanId': 100}

for k in e2:
    dto[k] = e2[k]
"""

"""
You can now use any of the low level keywords or low level modules directly
"""
"""
list all of the low-level fusion_api keywords
"""
fkw = {k for k, v in inspect.getmembers(lib, predicate=inspect.ismethod)
       if 'fusion_api' in k
       and 'get' in k
       and 'fusion_api_get_active_sessions' not in k}

pprint(fkw)

"""
filter = '?filter=\"alertState=\'Active\'\"&filter=\"healthCategory=\'ConnectionInstance\'\"'
resp = lib.fusion_api_get_resource(uri='/rest/alerts%s' %filter, api='600')
print '----'
pass
Example:  exercise the get user keyword for a bunch of x-api versions
x = {x: lib.fusion_api_get_user(api=x) for x in (1, 2, 100, 200, 300, 400, 500, 501, 600, 700)}
pprint(x)

resps = {}

for kw in fkw:
    for x in range(600, 601):
        try:
            resps[kw] = getattr(lib, kw)(api=x)
        except:
            pass

#x = {getattr(lib, kw)(api=x) for x in range(600, 601) for kw in fkw}
pprint(x)
"""
