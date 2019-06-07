"""Variables for working with the VC ToR POC code base
"""

TOR_TEMPLATE_NAME = "Video"
BLUE_VLAN_NAME = "blue"
PURPLE_VLAN_NAME = "purple"
BLUE_VLAN_ID = "19"
PURPLE_VLAN_ID = "15"
TOR_TEMPLATE_URL = "/rest/racktemplates"
TOR_URL = "/rest/vcrack"

VIDEO_CLIENT_ADDRESS = "172.17.209.116"
OLDIE_PING_ADDRESS = "1.1.15.1"
COMEDY_PING_ADDRESS = "1.1.19.1"
PING_VERIFY_PROMPT = "$"
PING_VERIFY_USER = "vctor"
PING_VERIFY_PASSWORD = "skyline!"


def _define_network(vlanid, name):
    network = {
        "vlanId": vlanid,
        "purpose": "General",
        "name": name,
        "ethernetNetworkType": "Tagged",
        "type": "ethernet-networkV300",
        "smartLink": False,
        "privateNetwork": False
    }
    return network


def _network_identifier(name, vlanid):
    netid = {
        "network_name": name,
        "network_id":  "not-set",
        "vlan_id": vlanid
    }
    return netid


def _define_links(name, port):
    links = {
        "name": name,
        "port": port,
        "networktype": "ethernet",
        "networks":  "not-set"
    }
    return links


BLUE_NETWORK_DETAILS = _define_network(BLUE_VLAN_ID, BLUE_VLAN_NAME)
PURPLE_NETWORK_DETAILS = _define_network(PURPLE_VLAN_ID, PURPLE_VLAN_NAME)

BLUE_NETWORK_IDENTIFIER = _network_identifier(BLUE_VLAN_NAME, BLUE_VLAN_ID)
PURPLE_NETWORK_IDENTIFIER = _network_identifier(PURPLE_VLAN_NAME, PURPLE_VLAN_ID)

UP_LINK = _define_links("Out To World", "11")
OLDIES = _define_links("Oldies", "15")
COMEDY = _define_links("Comedy", "19")
VIDEO_CLIENT = _define_links("Video Client", "16")

TOR_TEMPLATE = {
    "category": "racktemplates",
    "name": TOR_TEMPLATE_NAME,
    "type": "ToR",
    "uplinkSets": "not-set",
    "downlinkSets": "not-set"
}

TOR_DETAILS = {
    "category": "vcracks",
    "name": "Roseville",
    "torip":  "not-set",
    "template": TOR_TEMPLATE_NAME,
    "servers": ""
}
