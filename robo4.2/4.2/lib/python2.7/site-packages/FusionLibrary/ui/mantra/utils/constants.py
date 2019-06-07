# (C) Copyright 2014 Hewlett-Packard Development Company, L.P.


class mantraConstants(object):

    CLUSTER_HOST = "Clusters"
    CS700_ARRAY = "Cs700 Array"
    CS700_ENCLOSURE = "Cs700 Enclosure"
    CS700_SAN_SWITCH = "Cs700 San Switch"
    CS700_TOR = "Cs700 Tor"
    HOSTS = "Hosts"
    INTERCONNECTS = "Interconnects"
    MANAGEMENT_SERVER = "Management Server"
    PDU = "Pdu"
    RACK = "Rack"
    SERVERS = "Servers"

    # PROXY
    HTTP_PROXY = "http_proxy=http://proxy.houston.hp.com:8080"
    HTTPS_PROXY = "https_proxy=https://proxy.houston.hp.com:8080"

    EMPTY_OVERVIEW_CONTENTS_MESSAGE = "none"


class DCSConstants(object):
    FAN_OP_STATUS_LIST = ["OP_STATUS_NON_RECOVERABLE_ERROR", "OP_STATUS_NON_RECOVERABLE_DEGRADED", "OP_STATUS_OK"]
    DCS_PORT = ":9990"
    DCS_REST_INSTANCES = "/dcs/rest/schematic/instances"

    HTTP_STATUS_CODE_OK = 200


class mantraSyncConstants(object):

    COMPLIANCE_SYNC_TIME = 180
    SYSTEM_PROFILE_TASK_TIMEOUT = 15
