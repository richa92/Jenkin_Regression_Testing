'''
FVT API keywords
'''
from robot.libraries.BuiltIn import BuiltIn
import copy

fusionlib = BuiltIn().get_library_instance('FusionLibrary')


def fvt_api_get_logical_interconnect_group_by_name(name=None):
    """Get Logical Interconnect Group By Name
    [Arguments]
    name: logical interconnect group name
    [Example]
    {resp} = Fvt Api Get Logical Interconnect Group By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_lig(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_logical_interconnect_by_name(name=None):
    """Get Logical Interconnect By Name
    [Arguments]
    name: logical interconnect name
    [Example]
    {resp} = Fvt Api Get Logical Interconnect By Name	name
    """
    resp = fusionlib.fusion_api_get_li()
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_interconnect_by_name(name=None):
    """Get Interconnect By Name
    [Arguments]
    name: interconnect name
    [Example]
    {resp} = Fvt Api Get Interconnect By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_interconnect(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_interconnect_by_uri(uri=None):
    """Get Interconnect By Uri
    [Arguments]
    uri: interconnect uri
    [Example]
    {resp} = Fvt Api Get Interconnect By Uri	uri
    """
    resp = fusionlib.fusion_api_get_interconnect()
    return next((item for item in resp['members'] if item['uri'] == uri), None)


def fvt_api_get_ethernet_network_by_name(name=None):
    """Get Ethernet Network By Name
    [Arguments]
    name: ethernet network name
    [Example]
    {resp} = Fvt Api Get Ethernet Network By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_ethernet_networks(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_fc_network_by_name(name=None):
    """Get FC Network By Name
    [Arguments]
    name: fc network name
    [Example]
    {resp} = Fvt Api Get FC Network By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_fc_networks(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_fcoe_network_by_name(name=None):
    """Get FCoE Network By Name
    [Arguments]
    name: fcoe network name
    [Example]
    {resp} = Fvt Api Get FCoE Network By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_fcoe_networks(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_network_set_by_name(name=None):
    """Get Network Set By Name
    [Arguments]
    name: network set name
    [Example]
    {resp} = Fvt Api Get Network Set By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_network_set(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_network_set_uris(networkSetList):
    """Get Network Set Uris
    [Arguments]
    networkSetList: list of network sets
    [Example]
    {resp} = Fvt Api Get Network Set Uris	networkSetList
    """
    resp = fusionlib.fusion_api_get_network_set()
    members = {x['name']: x['uri'] for x in resp['members']}
    return [members[x] for x in set(members) & set(networkSetList)]


def fvt_api_get_enclosure_group_by_name(name=None):
    """Get Enclosure Group By Name
    [Arguments]
    name: enclosure group name
    [Example]
    {resp} = Fvt Api Get Enclosure Group By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_enclosure_groups(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_enclosure_by_name(name=None):
    """Get Enclosure By Name
    [Arguments]
    name: enclosure name
    [Example]
    {resp} = Fvt Api Get Enclosure By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_enclosures(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_logical_enclosure_by_name(name=None):
    """Get Logical Enclosure By Name
    [Arguments]
    name: logical enclosure name
    [Example]
    {resp} = Fvt Api Get Logical Enclosure By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_logical_enclosure(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_server_profile_by_name(name=None):
    """Get Server Profile By Name
    [Arguments]
    name: server profile name
    [Example]
    {resp} = Fvt Api Get Server Profile By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_server_profiles(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_server_profile_template_by_name(name=None):
    """Get Server Profile Template By Name
    [Arguments]
    name: server profile template name
    [Example]
    {resp} = Fvt Api Get Server Profile Template By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_server_profile_templates(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_server_hardware_by_name(name=None):
    """Get Server Hardware By Name
    [Arguments]
    name: server hardware name
    [Example]
    {resp} = Fvt Api Get Server Hardware By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_server_hardware(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)


def fvt_api_get_uplink_set_by_name(name=None):
    """Get Uplink Set By Name
    [Arguments]
    name: uplink set name
    [Example]
    {resp} = Fvt Api Get Uplink Set By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_uplink_set(param=param)
    if resp['count'] != 0:
        return resp['members'][0]
    return None


def fvt_api_check_internal_vlan_exist(networkUri, liUri):
    """Check Internal Vlan Exist
    [Arguments]
    networkUri: network uri
    liUri:	LI uri
    [Example]
    {resp} = Fvt Api Check Internal Vlan Exist	networkUri	liUri
    """
    resp = fusionlib.fusion_api_get_li_internal_vlans(uri=liUri)
    if resp['count'] == 0:
        return None

    members = resp['members']
    for item in members:
        if item['generalNetworkUri'] == networkUri:
            return networkUri
    return None


def fvt_api_get_ethernet_networks_uris(networkList):
    """Get Ethernet Networks Uris
    [Arguments]
    networkList: list of networks
    [Example]
    {resp} = Fvt Api Get Ethernet Networks Uris	networkList
    """
    resp = fusionlib.fusion_api_get_ethernet_networks()
    members = {x['name']: x['uri'] for x in resp['members']}
    return [members[x] for x in set(members) & set(networkList)]


def fvt_copy_dictionary(dc=None):
    """Copy Dictionary
    [Arguments]
    dc: dictionary to be copied
    [Example]
    {resp} = Fvt Copy Dictionary	dc
    """
    return copy.deepcopy(dc)


def fvt_api_update_logical_enclosure_from_group(body=None, uri=None):
    """Update Logical Enclosure From Group
    [Arguments]
    body: request dto
    uri:  logical enclosure uri
    [Example]
    {resp} = Fvt Api Update Logical Enclosure From Group	body	uri
    """
    param = '/updateFromGroup'
    return fusionlib.logical_enclosure.put(body=body, uri=uri, param=param)


def fvt_api_get_interconnect_port_by_name(interconnect=None, port=None):
    """Get Interconnect Port By Name
    [Arguments]
    interconnect: interconnect the port belongs to
    port:  	port name
    [Example]
    {resp} = Fvt Api Get Interconnect Port By Name	interconnect	port
    """
    resp = fvt_api_get_interconnect_by_name(interconnect)
    return next((item for item in resp['ports'] if item['name'] == port), None)


def fvt_api_get_fabric_by_name(name=None):
    """Get Fabric By Name
    [Arguments]
    name: fabric name
    [Example]
    {resp} = Fvt Api Get Fabric By Name	name
    """
    param = "?filter=\"'name' = '%s'\"" % (name)
    resp = fusionlib.fusion_api_get_fabric(param=param)
    return next((item for item in resp['members'] if item['name'] == name), None)
