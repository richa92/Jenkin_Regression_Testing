"""
This module does a GET of all pages\members for a resource, which is very fast, and then
creates a dictionary of name: uri values that can be quickly traversed.

Currently, it supports: ETH, FC, and FCOE networks, as these are heavily used in
uplink sets and network sets. Other resource types could also be added for performance gains.

The 'get' method is called by:
Get Ethernet URIs
Get FC URIs
Get FCoE URIs.
"""
from robot.libraries.BuiltIn import BuiltIn


def __x():
    pass


class Uris(object):

    def __init__(self):
        self.lib = BuiltIn().get_library_instance('FusionLibrary')
        self.methods = {'ETH': self.lib.fusion_api_get_ethernet_networks,
                        'FC': self.lib.fusion_api_get_fc_networks,
                        'FCOE': self.lib.fusion_api_get_fcoe_networks}

    def get(self, rtype, names):
        if names is not None and isinstance(names, list) and str(rtype).upper() in self.methods:
            resp = self.methods[rtype]()
            members = {x['name']: x['uri'] for x in resp['members']}
            return [members[x] for x in set(members).intersection(set(names))]
        else:
            return []
