# Conditional exclusion list for Compatibility Report and Resource JSON Compare
conditionalExcL = [
    {
        # Brief description: exclude attributes in excList that are under the "credentials" attribute list of dictionary value(s)
        'path': '.credentials',
        'excList': ['oaIpAddress', 'vcmIpAddress']
    },
    {
        # Brief description: exclude attributes in excList that is under toplevel(represented by ".") of JSON data with "uri" value of "/rest/migratable-vc-domains*"
        #                    "*" is wildcard/any character(s)
        'taggedKeys': {'uri': '/rest/migratable-vc-domains*'},
        'taggedKeys_operator': 'AND',
        'taggedKeys_path': '.',
        'excList': ['enclosureIp', 'enclosureName', 'enclosureGroupName', 'enclosureSerialNumber', 'logicalInterconnectGroupName']
    },
    {
        # Brief description: exclude attributes in excList that are under the "itemCount" attribute list of dictionary value(s)
        'path': '.itemCount',
        'excList': ['interconnectCount', 'serverCount']
    },
    {
        # Brief description: exclude attributes in excList that is under ethNets->members of JSON data where "internalVlanId" is 0 AND "name" has a value of "net_448-E"
        #                    "*" is wildcard/any index location or value in the list
        'taggedKeys': {'internalVlanId': 0, 'name': 'net_448-E'},
        'taggedKeys_operator': 'AND',
        'taggedKeys_path': '.ethNets.members[*]',
        'excList': ['internalVlanId']
    },
    {
        # Brief description: exclude attributes in excList that is under ethNets->members->connections of JSON data where "portId" is "Lom 1:*' AND "networkUri_ADD" has a value of "NetSet_2S1409P9XS*"
        #                    "*" is wildcard/any index location or value in the list for path. Any character for dictionary values in taggedKeys
        'taggedKeys': {'portId': 'Lom 1:*', "networkUri_ADD": "NetSet_2S1409P9XS*"},
        'taggedKeys_operator': 'AND',
        'taggedKeys_path': '.profiles.members[*].connections[*]',
        'excList': ['portId']
    }
]

