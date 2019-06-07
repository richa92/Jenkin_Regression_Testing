'''
FusionLibrary API keywords

'''

from FusionLibrary.api.common.request import HttpVerbs
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.healthmonitor import IPy
from FusionLibrary.api.activity.tasks import Task
from FusionLibrary.api.activity.alerts import Alert
from FusionLibrary.api.activity.audit_logs import AuditLog
from FusionLibrary.api.activity.events import Event
from FusionLibrary.api.data_services.metric_streaming import MetricStreaming
from FusionLibrary.api.data_services.remotesyslog import RemoteSyslog
from FusionLibrary.api.activity.reports import Report
from FusionLibrary.api.external_managers.deployment_managers import DeploymentManager
from FusionLibrary.api.external_managers.hypervisor_managers import HypervisorManager
from FusionLibrary.api.facilities.datacenters import Datacenter
from FusionLibrary.api.facilities.power_devices import PowerDevice
from FusionLibrary.api.facilities.racks import Rack
from FusionLibrary.api.fc_sans.device_managers import DeviceManager
from FusionLibrary.api.fc_sans.managed_sans import ManagedSan
from FusionLibrary.api.fc_sans.providers import Provider
from FusionLibrary.api.hypervisors.hypervisor_cluster_profiles import HypervisorClusterProfiles
from FusionLibrary.api.hypervisors.hypervisor_clusters import HypervisorClusters
from FusionLibrary.api.hypervisors.hypervisor_host_profiles import HypervisorHostProfiles
from FusionLibrary.api.hypervisors.hypervisor_hosts import HypervisorHosts
from FusionLibrary.api.networking.connection_templates import ConnectionTemplate
from FusionLibrary.api.networking.ethernet_networks import EthernetNetwork
from FusionLibrary.api.networking.fabrics import Fabric
from FusionLibrary.api.networking.fc_networks import FcNetwork
from FusionLibrary.api.networking.fcoe_networks import FcoeNetwork
from FusionLibrary.api.networking.interconnect_types import InterconnectTypes
from FusionLibrary.api.networking.interconnects import Interconnect
from FusionLibrary.api.networking.interconnect_link_topology import InterconnectLinkTopology
from FusionLibrary.api.networking.internal_link_sets import InternalLinkSets
from FusionLibrary.api.networking.logical_downlinks import LogicalDownlink
from FusionLibrary.api.networking.logical_interconnects import LogicalInterconnect
from FusionLibrary.api.networking.logical_interconnect_groups import LogicalInterconnectGroup
from FusionLibrary.api.networking.logical_switch_groups import LogicalSwitchGroup
from FusionLibrary.api.networking.logical_switches import LogicalSwitch
from FusionLibrary.api.networking.network_sets import NetworkSet
from FusionLibrary.api.networking.sas_interconnect_types import SasInterconnectTypes
from FusionLibrary.api.networking.sas_interconnects import SasInterconnects
from FusionLibrary.api.networking.sas_logical_interconnect_groups import SasLogicalInterconnectGroup
from FusionLibrary.api.networking.sas_logical_interconnects import SasLogicalInterconnect
from FusionLibrary.api.networking.switches import Switch
from FusionLibrary.api.networking.switch_types import SwitchTypes
from FusionLibrary.api.networking.uplink_sets import UplinkSet
from FusionLibrary.api.crmvc.migratable_vc_domains import MigratableVcDomain
from FusionLibrary.api.search.index_associations import IndexAssociation
from FusionLibrary.api.search.index_resources import IndexResource
# from FusionLibrary.api.search.index_search_suggestions import IndexSearchSuggestion
# from FusionLibrary.api.search.index_trees import IndexTrees
# from FusionLibrary.api.search.lables import Label
from FusionLibrary.api.security.active_user_sessions import ActiveUserSessions
from FusionLibrary.api.security.authorizations import Authorizations
from FusionLibrary.api.security.certificate_authority import CertificateAuthority
from FusionLibrary.api.security.certificate_validation_configuration import CertificateValidationConfiguration
from FusionLibrary.api.security.certificates_client_rabbitmq import CertificatesClientRabbitMq
from FusionLibrary.api.security.client_certificates import ClientCertificate
from FusionLibrary.api.security.security_standards import SecurityStandards
from FusionLibrary.api.security.login_details import LoginDetails
from FusionLibrary.api.security.login_domains_global_settings import LoginDomainsGlobalSettings
from FusionLibrary.api.security.login_domains_login_certificates import LoginDomainsLoginCertificates
from FusionLibrary.api.security.login_domains_group_to_role_mapping import LoginDomainsGroupToRoleMapping
from FusionLibrary.api.security.login_domains import LoginDomain
from FusionLibrary.api.security.login_sessions import LoginSession
from FusionLibrary.api.security.roles import Roles
from FusionLibrary.api.security.sessions import Sessions
from FusionLibrary.api.security.users import User
from FusionLibrary.api.security.appliance_certificates import ApplianceCertificate
from FusionLibrary.api.security.remote_certificates import RemoteCertificate
from FusionLibrary.api.security.server_certificates import ServerCertificate
from FusionLibrary.api.security.certificates_status import CertificateStatus
from FusionLibrary.api.security.web_server_certificates import WebServerCertificate
from FusionLibrary.api.servers.connections import Connections
from FusionLibrary.api.servers.enclosures import Enclosure
from FusionLibrary.api.servers.rackmanagers import RackManager
from FusionLibrary.api.servers.enclosure_groups import EnclosureGroup
from FusionLibrary.api.servers.id_pools_ipv4_subnet import IdPoolsIpv4Subnet
from FusionLibrary.api.servers.id_pools_ipv4_ranges import IdPoolsIpv4Range
from FusionLibrary.api.servers.id_pools_vmac_ranges import IdPoolsVmacRange
from FusionLibrary.api.servers.id_pools_vsn_ranges import IdPoolsVsnRange
from FusionLibrary.api.servers.id_pools_vwwn_ranges import IdPoolsVwwnRange
from FusionLibrary.api.servers.id_pools import IdPool
from FusionLibrary.api.servers.logical_enclosures import LogicalEnclosure
from FusionLibrary.api.servers.server_hardware_types import ServerHardwareTypes
from FusionLibrary.api.servers.server_hardware import ServerHardware
from FusionLibrary.api.servers.server_profiles import ServerProfile
from FusionLibrary.api.servers.server_profile_templates import ServerProfileTemplate
from FusionLibrary.api.settings.appliance_device_read_community_string import ApplianceDeviceReadCommunityString
from FusionLibrary.api.settings.appliance_eula import ApplianceEula
from FusionLibrary.api.settings.appliance_factory_reset import ApplianceFactoryReset
from FusionLibrary.api.settings.appliance_firmware import ApplianceFirmware
from FusionLibrary.api.settings.appliance_health_status import ApplianceHealthStatus
from FusionLibrary.api.settings.appliance_network_interfaces import ApplianceNetworkInterfaces
from FusionLibrary.api.settings.appliance_node_information import ApplianceNodeInformation
from FusionLibrary.api.settings.appliance_shutdown import ApplianceShutdown
from FusionLibrary.api.settings.appliance_state import ApplianceState
from FusionLibrary.api.settings.appliance_support_dumps import ApplianceSupportDump
from FusionLibrary.api.settings.appliance_upgrade import ApplianceUpgrade
from FusionLibrary.api.settings.appliance_time_and_locale_configuration import ApplianceTimeAndLocaleConfiguration
from FusionLibrary.api.settings.appliance_trap_destinations import ApplianceTrapDestination
from FusionLibrary.api.settings.appliance_snmpv3_trap_destinations import ApplianceSnmpv3TrapDestination
from FusionLibrary.api.settings.appliance_snmpv3_trap_forwarding_users import ApplianceSnmpv3TrapForwardingUser
from FusionLibrary.api.settings.backups import Backup
from FusionLibrary.api.settings.domains import Domains
from FusionLibrary.api.settings.email_notification import EmailNotification
from FusionLibrary.api.settings.firmware_bundles import FirmwareBundle
from FusionLibrary.api.settings.firmware_drivers import FirmwareDriver
from FusionLibrary.api.settings.global_settings import GlobalSettings
from FusionLibrary.api.settings.ha_nodes import HaNodes
from FusionLibrary.api.settings.licenses import Licenses
from FusionLibrary.api.settings.ping import Ping
from FusionLibrary.api.settings.proxy_server import ProxyServer
from FusionLibrary.api.settings.restores import Restore
from FusionLibrary.api.settings.service_access import ServiceAccess
from FusionLibrary.api.settings.startup_progress import StartupProgress
from FusionLibrary.api.settings.version import Version
from FusionLibrary.api.storage.drive_enclosures import DriveEnclosures
from FusionLibrary.api.storage.sas_logical_jbod_attachments import SasLogicalJbodAttachments
from FusionLibrary.api.storage.sas_logical_jbods import SasLogicalJbods
from FusionLibrary.api.storage.storage_pools import StoragePool
from FusionLibrary.api.storage.storage_systems import StorageSystem
from FusionLibrary.api.storage.storage_volume_templates import StorageVolumeTemplate
from FusionLibrary.api.storage.storage_volumes import StorageVolume
from FusionLibrary.api.storage.storage_volume_attachment import StorageVolumeAttachment
from FusionLibrary.api.remote_support.remote_support import RemoteSupport
from FusionLibrary.api.remote_support.configuration import Configuration
from FusionLibrary.api.settings.scopes import Scope
from FusionLibrary.api.settings.repositories import Repository
from FusionLibrary.api.i3s_osds.os_deploymentserver import OSDeploymentServer

from FusionLibrary.api.settings.ssh_access import SshAccess
import json
import re
import time
import paramiko
from robot.libraries.BuiltIn import BuiltIn
from operator import itemgetter
import random
from FusionLibrary.api.networking.fabric_manager import FabricManager


class FusionAPIKeywords(object):

    """Library for all Fusion API keywords.

    = Table of contents =

    - `Usage`
    - `Examples`
    - `Importing`
    - `Keywords`

    = Usage =

    This library contains all of the Fusion API keywords. All keywords allow the user to specify the ${X_API_VERSION},
    and to override the default request headers.  Therefore, these are not documented within each keyword.

    = Examples =

    Each section has its own example section, but here is a basic example:

    | `Fusion API Login Appliance`       | ${APPLIANCE_IP} | ${admin_credentials} |               |
    | `Fusion API Get Appliance Status ` |                 |                      |               |

    = generic keywords =

    """

    def __init__(self):
        self.fusion_client = HttpVerbs()

    def fusion_api_get_headers(self):
        """ Return the client headers """
        return self.fusion_client._headers.copy()

    def fusion_api_get_resource(self, uri, api=None, headers=None):
        """ Returns any single fusion resource by uri

        `generic keywords`
           Example:
           | ${resource} =  | Fusion Api Get Resource | /rest/ethernet-networks/26a3c661-cd44-4322-b939-6e1bd222c035 | <api> | <headers> |
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        return self.fusion_client.get(uri, headers)

    def fusion_api_delete_resource(self, uri, api=None, headers=None):
        """ Deletes any single fusion resource by uri
           Example:
           | ${resource} =    | Fusion Api Delete Resource | /rest/ethernet-networks/26a3c661-cd44-4322-b939-6e1bd222c035 | <api> | <headers> |
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        return self.fusion_client.delete(uri, headers)

    def fusion_api_generic_post(self, body, uri, api=None, headers=None):
        """ Issues a POST to the specified uri, passing the supplied body
           Example:
           | ${resource} =    | Fusion Api Generic POST | <body> | <uri> | <api> | <headers> |
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        return self.fusion_client.post(uri=uri, body=json.dumps(body), headers=headers)

    def fusion_api_generic_put(self, body, uri, api=None, headers=None):
        """ Issues a PUT to the specified uri, passing the supplied body
           Example:
           | ${resource} =    | Fusion Api Generic PUT | <uri> | <body> | <api> | <headers> |
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        return self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))

    def fusion_api_generic_patch(self, body, uri, api=None, headers=None):
        """ Issues a PATCH to the specified uri, passing the supplied body
           Example:
           | ${resource} =    | Fusion Api Generic PATCH | <uri> | <body> | <api> | <headers> |
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        return self.fusion_client.patch(uri=uri, headers=headers, body=json.dumps(body))

    def fusion_api_get_dict_from_list(self, listofDict, key, value):
        """
        Takes a list of dictionaries and returns the (first) dictionary that contains the given key value pair
        """
        for d in listofDict:
            if d[key] == value:
                return d
        return {}

    def fusion_api_validate_response(self, respDict, valDict):
        """
        Compares the TOP LEVEL keys and values (using regex) of a response Dict vs. validation Dict and returns a dictionary
        containing overall success, as well as detailed list of keys\values\success.
        """
        success = True
        returnDict = {}
        keys = []
        for key in valDict:
            if not valDict[key]:
                continue
            # logger._log_to_console_and_log_file('key: %s' % (key))
            keyDict = {'key': key, 'expected': valDict[
                key], 'actual': respDict[key], 'success': True}
            if key in respDict:
                pattern = re.compile(str(valDict[key]))
                # if not re.search(str(valDict[key]), str(respDict[key])):
                # t = re.compile('(?i)Warning|Unknown|Terminated|Killed|Error|Completed')

                if not re.search(pattern, str(respDict[key])):

                    success = False
                    keyDict['success'] = False
            else:
                success = False
                keyDict['success'] = False
            keys.append(keyDict)

        returnDict['success'] = success
        returnDict['keys'] = keys
        return returnDict

    def fusion_api_validate_response_follow(self, expected, response, uriCache={}, wordy=False, depth=0,
                                            disable_dict_sorting=False,
                                            disable_list_sorting=False,
                                            called_by_logged=False):
        """
        Compares the entire response body (json dict) with the previously created expected (dict).
        Only the items in the expected are evaluated.  Extra items in the response are ignored except in the case
        of a list [] type.  Lists are verified to have the same number of items.

        When originally written, this function would fail on the first DTO error found.  A request to validate the
        entire DTO was asked for.  To enable validation of the entire DTO, use a pybot command line variable VALIDATE_ENTIRE_DTO
        pybot -v APPLIANCE_IP:16.114.211.88 -v DATA_FILE:Regression_Data.py -v VALIDATE_ENTIRE_DTO:True  SomeTest.robot

        To compare URI there are three options.  For example if the response contains:

            "coveredByDevice": "/rest/drive-enclosures/b8f43c88-b8a2-4594-8868-edd594ef1391",

        then in the expected you can have any of the following
            "coveredByDevice": "/rest/drive-enclosures/b8f43c88-b8a2-4594-8868-edd594ef1391",
                This does a literal compare.  Probably not very useful for URI's as they change constantly

        or  "coveredByDevice": "DE:0000A66103, bay 6",
            The ':' signifies that the name '0000A66103, bay 6' should match the name from a get of the actual URI,

        or  "coveredByDevice": "REGEX: "/rest/drive-enclosures/\w{8}(-\w{4}){3}-\w{12}",
            Used to regex match the response uri.


        Currently the easiest way to create the expect dic is to do a GET on the resource then edit the results.
        Remove items you don't want to validate (eTag, created, modified, etc) and update "uri" items with one of
        the above matching methods.

        By default, this function sorts dictionaries and iterates through lists to find if any matches exist. For this
        reason, two booleans (disable_dict_sorting & disable_list_sorting) was added that can be passed in that will
        disable automatic sorting of dictionaries or lists and will compare the data and response in their current order.

        called_by_logged is an internal thing that is used to indicate that for This Test File, This Test Case we have
        already logged who called Fusaion API Validate Response Follow.
        Generates on line of: ${SUITE NAME} ---> In Test Case:  ${TEST NAME}, key: some_key, depth recursion_depth
        """

        tabs = '\t' * depth

        try:
            TEST_NAME = BuiltIn().get_variable_value("${TEST NAME}")
        except:
            TEST_NAME = "Suite Setup"

        SUITE_NAME = BuiltIn().get_variable_value("${SUITE NAME}")

        keyValueErrors = 0
        if BuiltIn().get_variable_value("${VALIDATE_ENTIRE_DTO}"):
            VALIDATE_ENTIRE_DTO = BuiltIn().get_variable_value("${VALIDATE_ENTIRE_DTO}")
        else:
            VALIDATE_ENTIRE_DTO = False

        CALLED_BY_LOGGED_MESSAGE = "First fail in this Fusion API Validate Response Follow.\nSuite Name: %s, TEST CASE: %s at key: %s, depth: %s"

        for key in expected.keys():
            if wordy:
                logger.info(("%sKey: %s" % (tabs, key)), also_console=False)

            if expected[key] is None and response[key] is None:
                logger.info(("%sExpected and response are None: Key %s" % (tabs, key)), also_console=False)
            elif expected[key] is None and response[key] is not None:
                if (isinstance(response[key], str) or isinstance(response[key], unicode)) and response[key] == '':
                    logger.info(("%sExpected is None and response is empty string: Key %s" % (tabs, key)), also_console=False)
                else:
                    if not called_by_logged:
                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                        called_by_logged = True
                    logger.warn("%sExpected is None but something returned in response: Key %s" % (tabs, key))
                    if VALIDATE_ENTIRE_DTO:
                        keyValueErrors += 1
                    else:
                        if depth == 0:
                            return False
                        else:
                            return False, called_by_logged
            elif expected[key] is not None and response[key] is None:
                if (isinstance(expected[key], str) or isinstance(expected[key], unicode)) and expected[key] == '':
                    logger.info((
                        "%sExpected is empty string and response is None: Key %s" % (tabs, key)), also_console=False)
                else:
                    if not called_by_logged:
                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                        called_by_logged = True
                    logger.warn("%sExpected something but response is None: Key %s" % (tabs, key))
                    if VALIDATE_ENTIRE_DTO:
                        keyValueErrors += 1
                    else:
                        if depth == 0:
                            return False
                        else:
                            return False, called_by_logged

            if isinstance(expected[key], list):
                if len(expected[key]) == 0 and len(response[key]) == 0:
                    continue
                elif len(expected[key]) == 0 and len(response[key]) != 0:
                    if not called_by_logged:
                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                        called_by_logged = True
                    logger.warn("%sFor key %s, Expected is empty but actual is not" % (tabs, key))
                    if VALIDATE_ENTIRE_DTO:
                        keyValueErrors += 1
                    else:
                        if depth == 0:
                            return False
                        else:
                            return False, called_by_logged
                elif len(expected[key]) != 0 and len(response[key]) == 0:
                    if not called_by_logged:
                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                        called_by_logged = True
                    logger.warn("%sFor key %s, Actual is empty but expcted is not" % (tabs, key))
                    if VALIDATE_ENTIRE_DTO:
                        keyValueErrors += 1
                    else:
                        if depth == 0:
                            return False
                        else:
                            return False, called_by_logged

                if (key in response) and isinstance(response[key], list) and (len(expected[key]) == len(response[key])):
                    # Lists of dictionaries can return in any order.  Try to sort
                    if isinstance(expected[key][0], dict):
                        # logger.info(("Pre sort Res: %s" % response[key][0])
                        # logger.info(("Pre sort Exp: %s" % expected[key][0])
                        if not disable_dict_sorting:
                            if "name" in expected[key][0] and expected[key][0]["name"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: name") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('name'))
                                expected[key] = sorted(expected[key], key=itemgetter('name'))
                            if "userName" in expected[key][0] and expected[key][0]["userName"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: userName") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('userName'))
                                expected[key] = sorted(expected[key], key=itemgetter('userName'))
                            elif "portName" in expected[key][0] and expected[key][0]["portName"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: portName") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('portName'))
                                expected[key] = sorted(expected[key], key=itemgetter('portName'))
                            elif "bayNumber" in expected[key][0] and expected[key][0]["bayNumber"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: bayNumber") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('bayNumber'))
                                expected[key] = sorted(expected[key], key=itemgetter('bayNumber'))
                            elif "enclosureIndex" in expected[key][0] and expected[key][0]["enclosureIndex"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: enclosureIndex") % tabs, also_console=False)
                                # First sort on logicalLocation as a dict if it exists, then enclosureIndex.
                                # Order of first sort is maintained in the second sort
                                if "logicalLocation" in expected[key][0] and expected[key][0]["logicalLocation"] is not None:
                                    response[key] = sorted(response[key], key=itemgetter('logicalLocation'))
                                    expected[key] = sorted(expected[key], key=itemgetter('logicalLocation'))
                                response[key] = sorted(response[key], key=itemgetter('enclosureIndex'))
                                expected[key] = sorted(expected[key], key=itemgetter('enclosureIndex'))
                            elif "connectionId" in expected[key][0] and expected[key][0]["connectionId"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: connectionId") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('connectionId'))
                                expected[key] = sorted(expected[key], key=itemgetter('connectionId'))
                            elif "id" in expected[key][0] and expected[key][0]["id"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: id") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('id'))
                                expected[key] = sorted(expected[key], key=itemgetter('id'))
                            elif "relativeValue" in expected[key][0] and expected[key][0]["relativeValue"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: relativeValue") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('relativeValue'))
                                expected[key] = sorted(expected[key], key=itemgetter('relativeValue'))
                            elif "serialNumber" in expected[key][0] and expected[key][0]["serialNumber"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: serialNumber") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('serialNumber'))
                                expected[key] = sorted(expected[key], key=itemgetter('serialNumber'))
                            elif "deviceSlot" in expected[key][0] and expected[key][0]["deviceSlot"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: deviceSlot") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('deviceSlot'))
                                expected[key] = sorted(expected[key], key=itemgetter('deviceSlot'))
                            elif "type" in expected[key][0] and expected[key][0]["type"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: type") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('type'))
                                expected[key] = sorted(expected[key], key=itemgetter('type'))
                            elif "iSCSIBootAttemptInstance" in expected[key][0] and expected[key][0]["iSCSIBootAttemptInstance"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: iSCSIBootAttemptInstance") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('iSCSIBootAttemptInstance'))
                                expected[key] = sorted(expected[key], key=itemgetter('iSCSIBootAttemptInstance'))
                            elif "iSCSIAttemptInstance" in expected[key][0] and expected[key][0]["iSCSIAttemptInstance"] is not None:
                                if wordy:
                                    logger.info(("%sSorting List of Dict by: iSCSIAttemptInstance") % tabs, also_console=False)
                                response[key] = sorted(response[key], key=itemgetter('iSCSIAttemptInstance'))
                                expected[key] = sorted(expected[key], key=itemgetter('iSCSIAttemptInstance'))
                            else:
                                # sort on a key with "name" in it, if it has an actual value
                                randomkey = "changeme"
                                for namekey in expected[key][0].keys():
                                    if (re.match(r'.*name', namekey, re.I)) and (expected[key][0][namekey] is not None):
                                        randomkey = namekey
                                        break

                                # if randomkey not changed then just sort on a random key and hope for the best
                                if randomkey == "changeme":
                                    randomkey = random.choice(expected[key][0].keys())
                                if wordy:
                                    logger.info(("%sSorting List of Dict by random: %s" % (tabs, namekey)), also_console=False)
                                response[key] = sorted(response[key], key=itemgetter(randomkey))
                                expected[key] = sorted(expected[key], key=itemgetter(randomkey))

                    for i in xrange(0, len(expected[key])):
                        if isinstance(expected[key][i], dict) or isinstance(expected[key][i], list):
                            results, called_by_logged = self.fusion_api_validate_response_follow(expected[key][i], response[key][i], uriCache, wordy, depth + 1, called_by_logged=called_by_logged)
                            if not results:
                                if VALIDATE_ENTIRE_DTO:
                                    keyValueErrors += 1
                                else:
                                    if depth == 0:
                                        return False
                                    else:
                                        return False, called_by_logged
                        elif isinstance(expected[key][i], int):
                            if expected[key][i] == response[key][i]:
                                if wordy:
                                    logger.info(("%ssimple %s == %s" % (tabs, expected[key][i], response[key][i])), also_console=False)
                            else:
                                if not called_by_logged:
                                    logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                    called_by_logged = True
                                logger.warn("%ssimple %s != %s" % (tabs, expected[key][i], response[key][i]))
                                if VALIDATE_ENTIRE_DTO:
                                    keyValueErrors += 1
                                else:
                                    if depth == 0:
                                        return False
                                    else:
                                        return False, called_by_logged
                        else:
                            words = expected[key][i].split(":")
                            if len(words) < 2:
                                match = False
                                if not disable_list_sorting:
                                    for j in xrange(0, len(response[key])):
                                        if expected[key][i] == response[key][j]:
                                            logger.info(("%sfound item in list.  Will remove 1 matching item: [%s]" % (tabs, expected[key][i])), also_console=False)
                                            response[key].pop(j)
                                            match = True
                                            break
                                    if not match:
                                        if not called_by_logged:
                                            logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                            called_by_logged = True
                                        logger.warn("%sDidn't find item in list: [%s]" % (tabs, expected[key][i]))
                                        if VALIDATE_ENTIRE_DTO:
                                            keyValueErrors += 1
                                        else:
                                            if depth == 0:
                                                return False
                                            else:
                                                return False, called_by_logged
                                elif disable_list_sorting:
                                    if expected[key][i] == response[key][i]:
                                        logger.info(("%sFound matching item: [%s]" % (tabs, expected[key][i])), also_console=False)
                                        match = True
                                        break
                                    if not match:
                                        if not called_by_logged:
                                            logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                            called_by_logged = True
                                        logger.warn("%sActual value [%s] doesn't match expected value [%s]" % (tabs, response[key][i], expected[key][i]))
                                        if VALIDATE_ENTIRE_DTO:
                                            keyValueErrors += 1
                                        else:
                                            if depth == 0:
                                                return False
                                            else:
                                                return False, called_by_logged
                            elif words[0] == "REGEX":
                                match = False
                                exp = ":".join(words[1:])
                                for j in xrange(0, len(response[key])):
                                    if re.search(exp, response[key][j], re.M | re.I):
                                        logger.info(("%sfound item in list: [%s]" % (tabs, exp)), also_console=False)
                                        match = True
                                        break
                                if not match:
                                    if not called_by_logged:
                                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                        called_by_logged = True
                                    logger.warn("%sDidn't match item in list: [%s]" % (tabs, exp))
                                    if VALIDATE_ENTIRE_DTO:
                                        keyValueErrors += 1
                                    else:
                                        if depth == 0:
                                            return False
                                        else:
                                            return False, called_by_logged
                            else:
                                match = False
                                for j in xrange(0, len(response[key])):
                                    if re.search('/rest/', response[key][j]):
                                        resp = self.fusion_api_get_resource(str(response[key][j]))
                                        if resp['name'] == words[1]:
                                            logger.info(("%sfound item in list: [%s]" % (tabs, words[1])), also_console=False)
                                            match = True
                                            break
                                    elif expected[key][i] == response[key][j]:
                                        if wordy:
                                            logger.info(("%ssimple %s == %s" % (tabs, expected[key][i], response[key][i])), also_console=False)
                                        match = True
                                        break
                                if not match:
                                    if not called_by_logged:
                                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                        called_by_logged = True
                                    logger.warn("%sDidn't find item via uri lookup %s: [exp: %s != ret: %s]" % (tabs, str(response[key][j]), words[1], resp['name']))
                                    if VALIDATE_ENTIRE_DTO:
                                        keyValueErrors += 1
                                    else:
                                        if depth == 0:
                                            return False
                                        else:
                                            return False, called_by_logged
                else:
                    if not called_by_logged:
                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                        called_by_logged = True
                    logger.warn("%sList item not in Res or diff len list: %s" % (tabs, key))
                    if VALIDATE_ENTIRE_DTO:
                        keyValueErrors += 1
                    else:
                        if depth == 0:
                            return False
                        else:
                            return False, called_by_logged

                continue

            if isinstance(expected[key], dict):
                if key in response:
                    results, called_by_logged = self.fusion_api_validate_response_follow(expected[key], response[key], uriCache, wordy, depth + 1, called_by_logged=called_by_logged)
                    if not results:
                        if VALIDATE_ENTIRE_DTO:
                            keyValueErrors += 1
                        else:
                            if depth == 0:
                                return False
                            else:
                                return False, called_by_logged
                    continue
                else:
                    if not called_by_logged:
                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                        called_by_logged = True
                    logger.warn("%sDict item not in Res: %s" % (tabs, key))
                    if VALIDATE_ENTIRE_DTO:
                        keyValueErrors += 1
                    else:
                        if depth == 0:
                            return False
                        else:
                            return False, called_by_logged

            # only str, int, bool, unicode left
            if key in response:
                if (isinstance(response[key], str) or isinstance(response[key], unicode)) and re.search(r'/rest/', response[key], re.I):
                    words = expected[key].split(":")
                    compare_as_is = False
                    compare_as_regex = False
                    if len(words) < 2:
                        if wordy:
                            logger.info(("%sExpected did not split into type,name: %s" % (tabs, expected[key])), also_console=False)
                            logger.info(("%swill compare as is.") % tabs, also_console=False)
                        compare_as_is = True
                        exp_name = words[0]
                    else:
                        if key == 'serverHardwareTypeUri':
                            if words[0] == "SHT":
                                logger.info(("%sSHT lookup.  Call 'Get Server Hardware Type URI By Name And Mezz' for: %s" % (tabs, expected[key])), also_console=False)
                                sht_uri = BuiltIn().run_keyword("Get Server Hardware Type URI By Name And Mezz", ":".join(words[1:]))
                            else:   # support for SHT Uri lookup by ServerHardware (SH:wpst14, bay 1)
                                logger.info(("SH lookup for SHT: %s" % expected[key]), also_console=False)
                                sh_resp = BuiltIn().run_keyword("Get Resource", expected[key])
                                sht_uri = sh_resp['serverHardwareTypeUri']

                            sht_resp = self.fusion_api_get_resource(sht_uri)
                            exp_name = sht_resp['name']
                        else:
                            if words[0] == "REGEX":
                                compare_as_regex = True
                            exp_name = ":".join(words[1:])

                    if wordy:
                        logger.info(("%sResponse has URI, get uri: %s" % (tabs, response[key])), also_console=False)
                        logger.info(("%sExpecting name: %s" % (tabs, exp_name)), also_console=False)

                    if compare_as_regex:
                        found = re.search(exp_name, response[key], re.M | re.I)
                        msg = "[" + key + "] " + exp_name + " vs " + response[key]
                        if found:
                            if wordy:
                                logger.info(("%sregex match %s" % (tabs, msg)), also_console=False)
                            continue
                        else:
                            if not called_by_logged:
                                logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                called_by_logged = True
                            logger.warn("%sregex not match %s" % (tabs, msg))
                            if VALIDATE_ENTIRE_DTO:
                                keyValueErrors += 1
                            else:
                                if depth == 0:
                                    return False
                                else:
                                    return False, called_by_logged
                    elif compare_as_is:
                        msg = "[" + key + "] " + expected[key] + " vs " + response[key]
                        if expected[key] != response[key]:
                            if not called_by_logged:
                                logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                called_by_logged = True
                            logger.warn("%ssimple != %s" % (tabs, msg))
                            if VALIDATE_ENTIRE_DTO:
                                keyValueErrors += 1
                            else:
                                if depth == 0:
                                    return False
                                else:
                                    return False, called_by_logged
                        else:
                            if wordy:
                                logger.info(("%ssimple == %s" % (tabs, msg)), also_console=False)
                            continue
                    else:
                        if response[key] in uriCache:
                            if wordy:
                                msg = "[" + key + "] " + response[key] + " --> " + uriCache[response[key]]
                                logger.info(("%suriCache lookup %s" % (tabs, msg)), also_console=False)
                            resp_name = uriCache[response[key]]
                        else:
                            resp = self.fusion_api_get_resource(str(response[key]))
                            resp_name = resp['name']
                            uriCache[response[key]] = resp_name
                            if wordy:
                                msg = response[key] + " --> " + resp_name
                                logger.info(("%sGET uri and save in cache %s" % (tabs, msg)), also_console=False)

                        if resp_name != exp_name:
                            msg = "[" + key + "] " + exp_name + " vs " + resp_name
                            if not called_by_logged:
                                logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                                called_by_logged = True
                            logger.warn("%sExpected Name does not match URI name: %s" % (tabs, msg))
                            if VALIDATE_ENTIRE_DTO:
                                keyValueErrors += 1
                            else:
                                if depth == 0:
                                    return False
                                else:
                                    return False, called_by_logged
                elif (isinstance(expected[key], str) or isinstance(expected[key], unicode)) and (expected[key].find("REGEX:") > -1):
                    words = expected[key].split(":")
                    pattern = ":".join(words[1:])
                    found = re.search(pattern, str(response[key]), re.M | re.I)
                    msg = "[" + key + "] " + pattern + " vs " + str(response[key])
                    if found:
                        if wordy:
                            logger.info(("%sregex match %s" % (tabs, msg)), also_console=False)
                        continue
                    else:
                        logger.warn("%sregex not match %s" % (tabs, msg))
                        if VALIDATE_ENTIRE_DTO:
                            keyValueErrors += 1
                        else:
                            if depth == 0:
                                return False
                            else:
                                return False, called_by_logged
                elif (isinstance(expected[key], str) or isinstance(expected[key], unicode)) and (expected[key].find("RANGE:") > -1):
                    words = expected[key].split(":")
                    wmin = words[1]
                    wmax = words[2]
                    msg = wmin + " - " + wmax + ":" + str(response[key])
                    if (int(response[key]) >= int(wmin)) and (int(response[key]) <= int(wmax)):
                        if wordy:
                            logger.info(("%s%s Value in Range: %s" % (tabs, key, msg)), also_console=False)
                        continue
                    else:
                        logger.warn("%s%s Value NOT in Range: %s" % (tabs, key, msg))
                        if VALIDATE_ENTIRE_DTO:
                            keyValueErrors += 1
                        else:
                            if depth == 0:
                                return False
                            else:
                                return False, called_by_logged

                elif str(expected[key]) != str(response[key]):
                    msg = "[" + key + "] " + str(expected[key]) + " vs " + str(response[key])
                    if "name" != key and "name" in expected:
                        msg = "@ dict name=%s : %s" % (str(expected["name"]), msg)
                    if not called_by_logged:
                        logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                        called_by_logged = True
                    logger.warn("%ssimple != %s" % (tabs, msg))
                    if VALIDATE_ENTIRE_DTO:
                        keyValueErrors += 1
                    else:
                        if depth == 0:
                            return False
                        else:
                            return False, called_by_logged
                else:
                    if wordy:
                        logger.info(("%sExpected match response: %s" % (tabs, expected[key])), also_console=False)

            else:
                if not called_by_logged:
                    logger.warn(CALLED_BY_LOGGED_MESSAGE % (SUITE_NAME, TEST_NAME, key, depth))
                    called_by_logged = True
                logger.warn("%sResponse does not have key %s:" % (tabs, key))
                if VALIDATE_ENTIRE_DTO:
                    keyValueErrors += 1
                else:
                    if depth == 0:
                        return False
                    else:
                        return False, called_by_logged

        if keyValueErrors:
            logger.warn("%sDTO had %s failing keys:" % (tabs, keyValueErrors))
            if depth == 0:
                return False
            else:
                return False, called_by_logged

        else:
            if depth == 0:
                return True
            else:
                return True, called_by_logged

    class ActiveUserSessionsKeywords(object):

        """Active User Sessions API keywords.

        = Table of contents =

        - `Keywords`

        """

        def __init__(self):
            self.usersessions = ActiveUserSessions(self.fusion_client)

        def fusion_api_get_active_user_sessions(self, param='', api=None, headers=None):
            """Gets a default or paginated collection of Active User Sessions.
            [Arguments]
            param: query parameters
            Example
            |${resp} = |Fusion Api Get Active User Sessions | <param> | <api> | <headers>|
            """
            return self.usersessions.get(api=api, headers=headers, param=param)

    class AlertKeywords(object):
        """ Alert """
        def __init__(self):
            self.alert = Alert(self.fusion_client)

        def fusion_api_update_alert(self, body, uri, api=None, headers=None):
            """Updates an alert.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Update Alert  | <body> | <uri> | <api> | <headers>
            """
            return self.alert.update(body, uri, api, headers)

        def fusion_api_delete_alert(self, uri=None, api=None, headers=None, param=''):
            """Deletes an alert in bulk based on uri. If uri is not specified, ALL alerts are deleted
            [Arguments]
            uri: The uri of the network to delete
            [Example]
            ${resp} = Fusion Api Delete Alert  | <uri> | <api> | <headers>
            """
            return self.alert.delete(uri, api, headers, param=param)

        def fusion_api_delete_alert_changelog(self, alertId=None, api=None, headers=None):
            """Deletes an alert's changelog based on alertId.
            [Arguments]
            alertId: The ID of the alert to delete the changelog from
            [Example]
            ${resp} = Fusion Api Delete Alert Changelog | <alertId> | <api> | <headers>
            """
            return self.alert.delete(alertId, api, headers)

        def fusion_api_get_alerts(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Alerts.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Alert | <uri> | <param> | <api> | <headers>
            """
            return self.alert.get(uri=uri, api=api, headers=headers, param=param)

    class ApplianceDeviceReadCommunityKeywords(object):
        """ ApplianceDeviceReadCommunityKeywords """
        def __init__(self):
            self.rc = ApplianceDeviceReadCommunityString(self.fusion_client)

        def fusion_api_update_appliance_read_community_string(self, body, api=None, headers=None):
            """Update the device read community string. This results in an update of the community string on all the rack-mounted servers and devices in an enclosure.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Appliance Read Community String  | <body> | <api> | <headers>
            """
            return self.rc.update(body, api, headers)

        def fusion_api_get_appliance_read_community_string(self, api=None, headers=None):
            """Retrieves the global community string.
            [Example]
            ${resp} = Fusion Api Get Appliance Read Community String | <api> | <headers>
            """
            return self.rc.get(api=api, headers=headers)

    class ApplianceEulaKeywords(object):
        """ EULA """
        def __init__(self):
            self.eula = ApplianceEula(self.fusion_client)

        def fusion_api_save_eula(self, host, supportAccess='yes', api=None, headers=None):
            """Agrees\Disagrees with the EULA
            [Arguments]
            host: REQUIRED The IP or hostname of the appliance
            supportAccess: yes\no. Defaults to yes
            [Example]
            ${resp} = Fusion Api Save Eula  | <host> | <'yes'/'no'> | <api> | <headers>
            """
            return self.eula.save(host, supportAccess, api, headers)

        def fusion_api_eula_status(self, api=None, headers=None):
            """Retrieves the EULA status
            [Example]
            ${resp} =     Fusion Api Eula Status  | <api> | <headers>
            """

            return self.eula.save(api, headers)

    class ApplianceFactoryResetKeywords(object):
        """ Factory reset """
        def __init__(self):
            self.appfactoryreset = ApplianceFactoryReset(self.fusion_client)

        def fusion_api_appliance_factory_reset(self, mode=None, api=None, headers=None):
            """Start the factory reset operation. The network settings my be preserved if the query parameter is set to PRESERVE_NETWORK.
            [Arguments]
            mode: FULL Resets all customer data and network settings to defaults. PRESERVE_NETWORK Resets all customer data to defaults, but preserves the appliance network settings. RECOVERY Only allowed to recover from an internal error. Clears most customer data, as well as the appliance network settings.
            [Example]
            ${resp} = Fusion Api Appliance Factory Reset | <mode> | <api> | <headers>
            """
            return self.appfactoryreset.reset(mode, api, headers)

    class ApplianceFirmwareKeywords(object):
        """ Firmware """
        def __init__(self):
            self.appfirmware = ApplianceFirmware(self.fusion_client)

        def fusion_api_get_appliance_firmware_upgrade_status(self, api=None, headers=None):
            """Gets the status of the upgrade task once after the upgrade completes
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Appliance Firmware Upgrade Status | <api> | <headers>
            """
            param = '/notification'
            return self.appfirmware.get(api=api, headers=headers, param=param)

        def fusion_api_upgrade_appliance_firmware(self, localfile, api=None, headers=None):
            """Initiate upgrade task using uploaded upgrade image
            [Arguments]
            localfile: REQUIRED the filename of the .bin patch file
            [Example]
            ${resp} = Fusion Api Upgrade Appliance Firmware   | <localfile> | <api> | <headers>
            """
            param = '?file=%s' % localfile
            return self.appfirmware.update(api, headers, param)

        def fusion_api_upload_appliance_firmware(self, localfile, api=None, headers=None):
            """Uploads a .bin patch to the appliance
            [Arguments]
            localfile: REQUIRED the filename of the .bin patch file
            [Example]
            ${resp} = Fusion Api Upload Appliance Firmware   | <localfile> | <api> | <headers>
            """
            return self.appfirmware.upload(localfile, api, headers)

    class ApplianceHealthStatusKeywords(object):
        """ Health status """
        def __init__(self):
            self.health = ApplianceHealthStatus(self.fusion_client)

        def fusion_api_appliance_health_status(self, api=None, headers=None):
            """Retrieves the Appliance Health status
            [Example]
            ${resp} =     Fusion Api Appliance Health Status  | <api> | <headers>
            """
            return self.health.save(api, headers)

    class ApplianceNetworkInterfacesKeywords(object):
        """ Network interfaces """
        def __init__(self):
            self.interfaces = ApplianceNetworkInterfaces(self.fusion_client)

        def fusion_api_create_appliance_interfaces_payload(self, body=None, api=None):
            """Returns a valid request body dictionary to pass to fusion_api_configure_appliance_interfaces
            [Arguments]
            body: REQUIRED a dictionary containing required request body elements
            [Example]
            ${resp} = Fusion Api Create Appliance Interfaces Payload   | <body> | <api>
            """
            return self.interfaces.make_body(body, api)

        def fusion_api_configure_appliance_interfaces(self, body=None, api=None, headers=None):
            """Configures appliance interfaces, time, and locale
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Appliance Interfaces   | <body> | <api> | <headers>
            """
            return self.interfaces.configure(body, api, headers)

        def fusion_api_get_appliance_interfaces(self, api=None, headers=None):
            """Returns appliance interfaces, time, and locale
            [Example]
            ${resp} = Fusion Api Get Appliance Interfaces  | <body> | <api> | <headers>
            """
            return self.interfaces.get(api, headers)

        def fusion_api_get_appliance_interface_mac(self, device, api=None, headers=None):
            """Returns MAC address of the appliance interface specified by <device>.
            [Arguments]
            device: REQUIRED eth0, eth1...
            [Example]
            ${resp} = Fusion Api Get Appliance Interface Mac  | eth0 | <api> | <headers>
            """
            return self.interfaces.get_device_mac(device, api, headers)

        def fusion_api_get_appliance_interface_attribute(self, device='eth0', attribute='macAddress', api=None, headers=None):
            """Returns MAC address of the appliance interface specified by <device>.
            [Arguments]
            device: REQUIRED eth0, eth1...
            [Example]
            ${macAddress} = Fusion Api Get Appliance Interface Attribute | eth0 | macAddress | <api> | <headers>
            ${hostname} = Fusion Api Get Appliance Interface Attribute | eth0 | hostname | <api> | <headers>
            """
            return self.interfaces.get_device_attribute(device, attribute, api, headers)

    class ApplianceNodeInformationKeywords(object):
        """ Node information """
        def __init__(self):
            self.info = ApplianceNodeInformation(self.fusion_client)

        def fusion_api_get_appliance_status(self, api=None, headers=None):
            """Gets the appliance's status information
            [Example]
            ${resp} = Fusion Api Get Appliance Status  | <api> | <headers>
            """
            return self.info.get_status(api=api, headers=headers)

        def fusion_api_get_appliance_version(self, api=None, headers=None):
            """Gets the appliance's version information
            [Example]
            ${resp} = Fusion Api Get Appliance Version  | <api> | <headers>
            """
            return self.info.get_version(api=api, headers=headers)

    class ApplianceShutdownKeywords(object):
        """ Shutdown """
        def __init__(self):
            self.appshutdown = ApplianceShutdown(self.fusion_client)

        def fusion_api_appliance_shutdown(self, mode=None, api=None, headers=None):
            """Start the factory reset operation. The network settings my be preserved if the query parameter is set to PRESERVE_NETWORK.
            [Arguments]
            mode: HALT Shuts down and powers off the appliance. REBOOT Restarts the appliance.
            [Example]
            ${resp} = Fusion Api Appliance Shutdown | <mode> | <api> | <headers>
            """
            return self.appshutdown.shutdown(mode, api, headers)

    class ApplianceStateKeywords(object):
        """ Appliance state """
        def __init__(self):
            self.appstate = ApplianceState(self.fusion_client)

        def fusion_api_get_appliance_state(self, appliance):
            """Get appliance state
            [Example]
            ${resp} = Fusion Api Get Appliance State | <appliance>
            """
            return self.appstate.get(appliance)

    class ApplianceSupportDumpKeywords(object):
        """ Support dump """
        def __init__(self):
            self.dump = ApplianceSupportDump(self.fusion_client)

        def fusion_api_create_support_dump(self, body, api=None, headers=None):
            """Generates the support dump in a synchronous manner.The support dump can be encrypted or unencrypted by setting the encrypt flag.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Support Dump | <body> | <api> | <headers>
            """
            return self.dump.create(body=body, api=api, headers=headers)

        def fusion_api_download_support_dump(self, uri, localfile, api=None, headers=None):
            """Retrieves the specified support dump and saves it locally.
            [Arguments]
            uri: REQUIRED The uri of the support dump file
            localfile: REQUIRED The canonical filename to save to locally
            [Example]
            ${resp} = Fusion Api Download Support Dump | <uri> | <localfile> | <api> | <headers>
            """
            return self.dump.get(uri=uri, localfile=localfile, api=api, headers=headers)

    class ApplianceUpgrade(object):
        """ Upgrade """
        def __init__(self):
            self.upgrade = ApplianceUpgrade(self.fusion_client)

        def fusion_api_download_upgrade_file(self, uri, localfile, api=None, headers=None, chunk_size=1024):
            """Download .bin patch from external server.
            [Arguments]
            uri: the update bin repo url
            localfile: REQUIRED the filename of the .bin patch file
            [Example]
            ${resp} = Fusion Api Download Upgrade File | <repo> | <localfile> | <api> | <headers> | <chunk_size>
            """

            return self.upgrade.get(uri, localfile, api, headers=headers, chunk_size=int(chunk_size))

    class ApplianceTimeAndLocaleConfigurationKeywords(object):
        """ Time and local """
        def __init__(self):
            self.timeandlocale = ApplianceTimeAndLocaleConfiguration(self.fusion_client)

        def fusion_api_configure_appliance_time_and_locale(self, body=None, api=None, headers=None):
            """Configures appliance time and locale
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Configure Appliance Time and Locale    | <body> | <api> | <headers>
            """
            return self.timeandlocale.configure(body, api, headers)

        def fusion_api_get_appliance_time_and_locale(self, api=None, headers=None):
            """Returns appliance time, and locale
            [Example]
            ${resp} = Fusion Api Get Appliance Interfaces  | <body> | <api> | <headers>
            """
            return self.timeandlocale.get(api, headers)

    class ApplianceTrapDestinationKeywords(object):
        """ Trap destination """
        def __init__(self):
            self.trap = ApplianceTrapDestination(self.fusion_client)

        def fusion_api_get_appliance_trap_destinations(self, id=None, param='', api=None, headers=None):  # pylint: disable=W0622
            """Returns appliance trap destinations
            [Example]
            ${resp} = Fusion Api Get Appliance Trap Destinations | <id> |  <param> | <api> | <headers>
            """
            return self.trap.get(id=id, param=param, api=api, headers=headers)

        def fusion_api_validate_appliance_trap_destination(self, body=None, api=None, headers=None):
            """Validates appliance trap destinations
            [Example]
            ${resp} = Fusion Api Get Appliance Trap Destinations | <body> | <api> | <headers>
            """
            return self.trap.validate(body=body, api=api, headers=headers)

        def fusion_api_add_or_update_appliance_trap_destination(self, body=None, id=None, api=None, headers=None):  # pylint: disable=W0622
            """ Adds or updates the specified trap forwarding destination.
            The trap destination associated with the given id will be
            updated if a trap destination with that id already exists.
            If the given id is not found, then a trap destination will
            be created with the given id.
            [Example]
            ${resp} = Fusion Api Add Or Update Appliance Trap Destination | <body>  | <id> | <api> | <headers>
            """
            return self.trap.create(body=body, id=id, api=api, headers=headers)

        def fusion_api_update_appliance_trap_destination(self, body, id, api=None, headers=None):  # pylint: disable=W0622
            """ Updates the specified trap forwarding destination.
            The trap destination associated with the given id will be
            updated if a trap destination with that id already exists.
            [Example]
            ${resp} = Fusion Api Update Appliance Trap Destination | <body>  | <id> | <api> | <headers>
            """
            return self.trap.put(body=body, id=id, api=api, headers=headers)

        def fusion_api_delete_appliance_trap_destination(self, id=None, api=None, headers=None):  # pylint: disable=W0622
            """Deletes the trap destination associated with id
            [Example]
            ${resp} = Fusion Api Delete Appliance Trap Destination | <body>  | <id> | <api> | <headers>
            """
            return self.trap.delete(id=id, api=api, headers=headers)

    class ApplianceSnmpv3TrapDestinationKeywords(object):
        """ SNMP v3 trap destination """
        def __init__(self):
            self.snmpv3trap = ApplianceSnmpv3TrapDestination(self.fusion_client)

        def fusion_api_get_appliance_snmpv3_trap_destinations(self, id=None, param='', api=None, headers=None):  # pylint: disable=W0622
            """Returns appliance SNMPv3 trap destinations
            [Example]
            ${resp} = Fusion Api Get Appliance SNMPv3 Trap Destinations | <id> |  <param> | <api> | <headers>
            """
            return self.snmpv3trap.get(id=id, param=param, api=api, headers=headers)

        def fusion_api_add_appliance_snmpv3_trap_destination(self, body=None, api=None, headers=None):
            """ Adds SNMPv3 trap forwarding destination.
            [Example]
            ${resp} = Fusion Api Add Appliance SNMPv3 Trap Destination | <body>  | <api> | <headers>
            """
            return self.snmpv3trap.create(body=body, api=api, headers=headers)

        def fusion_api_edit_appliance_snmpv3_trap_destination(self, body=None, id=None, api=None, headers=None):  # pylint: disable=W0622
            """Edits the SNMPv3 trap destination associated with id
            [Example]
            ${resp} = Fusion Api Edit Appliance SNMPv3 Trap Destination | <body> | <id> | <api> | <headers>
            """
            return self.snmpv3trap.put(body=body, id=id, api=api, headers=headers)

        def fusion_api_delete_appliance_snmpv3_trap_destination(self, id=None, api=None, headers=None):  # pylint: disable=W0622
            """Deletes the SNMPv3 trap destination associated with id
            [Example]
            ${resp} = Fusion Api Delete Appliance SNMPv3 Trap Destination | <id> | <api> | <headers>
            """
            return self.snmpv3trap.delete(id=id, api=api, headers=headers)

    class ApplianceSnmpv3TrapForwardingUserKeywords(object):
        """ SNMP v3 trap forwarding """
        def __init__(self):
            self.snmpv3user = ApplianceSnmpv3TrapForwardingUser(self.fusion_client)

        def fusion_api_get_appliance_snmpv3_trap_forwarding_users(self, id=None, param='', api=None, headers=None):  # pylint: disable=W0622
            """Returns appliance SNMPv3 trap forwarding users
            [Example]
            ${resp} = Fusion Api Get Appliance SNMPv3 Trap Forwarding Users | <id> |  <param> | <api> | <headers>
            """
            return self.snmpv3user.get(id=id, param=param, api=api, headers=headers)

        def fusion_api_add_appliance_snmpv3_trap_forwarding_user(self, body=None, api=None, headers=None):
            """ Adds SNMPv3 trap forwarding user.
            [Example]
            ${resp} = Fusion Api Add Appliance SNMPv3 Trap Forwarding User | <body> | <api> | <headers>
            """
            return self.snmpv3user.create(body=body, api=api, headers=headers)

        def fusion_api_edit_appliance_snmpv3_trap_forwarding_user(self, body=None, id=None, api=None, headers=None):  # pylint: disable=W0622
            """Edits SNMPv3 trap forwarding user associated with id
            [Example]
            ${resp} = Fusion Api Edit Appliance SNMPv3 Trap Forwarding User | <id | <api> | <headers>
            """
            return self.snmpv3user.put(body=body, id=id, api=api, headers=headers)

        def fusion_api_delete_appliance_snmpv3_trap_forwarding_user(self, id=None, api=None, headers=None):  # pylint: disable=W0622
            """Deletes the SNMPv3 trap forwarding user associated with id
            [Example]
            ${resp} = Fusion Api Delete Appliance SNMPv3 Trap Forwarding User | <id | <api> | <headers>
            """
            return self.snmpv3user.delete(id=id, api=api, headers=headers)

    class AuditLogKeywords(object):
        """ Audit log """
        def __init__(self):
            self.log = AuditLog(self.fusion_client)

    class AuthorizationsKeywords(object):
        """ Authorizations """
        def __init__(self):
            self.auth = Authorizations(self.fusion_client)

        def fusion_api_check_authorization(self, body=None, api=None, headers=None, sessionID=None):
            """Checks if a user has permissions on a specific category and action.
            Returns "true" if user has permissions on the specified category and action, "false" if user does not have permissions.
            [Arguments]
            body: a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Check Authorization  | <body> | <api> | <headers> | <sessionID>
            """
            return self.auth.check(body=body, api=api, headers=headers, sessionID=sessionID)

        def fusion_api_get_authorization_category_actions(self, api=None, headers=None, resource_uri='', sessionID=None,):
            """Retrieves a list of category and actions
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Authorization Category Actions | <api> | <headers> | <resource_uri> |<sessionID>
            """
            param = '/category-actions%s' % resource_uri
            return self.auth.get(api=api, param=param, headers=headers, sessionID=sessionID)

        def fusion_api_get_authorization_role_category_actions(self, api=None, headers=None, sessionID=None):
            """Retrieves a list of all roles and associated category and actions.
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Authorization Role Category Actions | <api> | <headers>| <sessionID>
            """
            param = '/role-category-actions'
            return self.auth.get(api=api, param=param, headers=headers, sessionID=sessionID)

        def fusion_api_get_authorization_permission_actions(self, api=None, headers=None, category_action='', sessionID=None):
            """Lists the user session permissions that would authorize a particular action and resource category.
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Authorization Permission Actions | <api> | <headers> | <category_action> | <sessionID>
            """
            param = '/authorizing-permissions%s' % category_action
            return self.auth.get(api=api, param=param, headers=headers, sessionID=sessionID)

        def fusion_api_list_permission_scopes(self, api=None, headers=None, resource_uri='', sessionID=None):
            """Lists the permission scope.
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Authorization Permission Actions | <api> | <headers> | <resource_uri> | <sessionID>
            """
            param = '/association-scopes%s' % resource_uri
            return self.auth.get(api=api, param=param, headers=headers, sessionID=sessionID)

        def fusion_api_list_permission_scopes_auth_creation_resource(self, api=None, headers=None, resource_uri='', sessionID=None):
            """Lists the permission scope.
            [Arguments]
            [Example]
            ${resp} = Fusion Api list Permission Scopes Auth Creation Resource | <api> | <headers> | <resource_uri> | <sessionID>
            """
            param = '/associator-scopes%s' % resource_uri
            return self.auth.get(api=api, param=param, headers=headers, sessionID=sessionID)

    class BackupKeywords(object):
        """ Backup """
        def __init__(self):
            self.backup = Backup(self.fusion_client)

        def fusion_api_cancel_backup(self, backup, api=None, headers=None):
            """Cancels an in-progress backup. The backup URI may be obtained from the task returned when starting a backup, or by listing the backups
            [Arguments]
            backup: REQUIRED The uri of the backup file
            [Example]
            ${resp} = Fusion Api Cancel Backup | <uri> | <api> | <headers>
            """
            return self.backup.cancel(backup=backup, api=api, headers=headers)

        def fusion_api_create_backup(self, api=None, headers=None):
            """Create a new appliance backup. Any existing backup on the appliance is removed.
            [Example]
            ${resp} = Fusion Api Create Backup | <api> | <headers>
            """
            return self.backup.create(api=api, headers=headers)

        def fusion_api_get_backup(self, param='', api=None, headers=None, uri=None):
            """Retrieve the details for any current appliance backup.
            [Arguments]
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Backup | <param> | <api> | <headers> | <uri> |
            """
            return self.backup.get(param=param, api=api, headers=headers, uri=uri)

        def fusion_api_download_backup(self, uri, localfile, api=None, headers=None):
            """Retrieves the specified backup and saves it locally.
            [Arguments]
            uri: REQUIRED The uri of the backup file
            localfile: REQUIRED The canonical filename to save to locally
            [Example]
            ${resp} = Fusion Api Download Backup | <uri> | <localfile> | <api> | <headers>
            """
            return self.backup.download(uri=uri, localfile=localfile, api=api, headers=headers)

        def fusion_api_upload_backup(self, localfile, api=None, headers=None):
            """Uploads the specified backup file.
            [Arguments]
            localfile: REQUIRED The canonical filename of the local file to upload
            [Example]
            ${resp} = Fusion Api Upload Backup | <localfile> | <api> | <headers>
            """
            return self.backup.upload(localfile=localfile, api=api, headers=headers)

        def fusion_api_update_backup_config(self, body, api=None, headers=None):
            """Updates the remote server configuration and the automatic backup schedule for backup.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Backup Config | <localfile> | <api> | <headers>
            """
            return self.backup.update(body, api=api, headers=headers)

    class CertificateAuthorityKeywords(object):
        """ Certificate authority """
        def __init__(self):
            self.ca = CertificateAuthority(self.fusion_client)

        def fusion_api_get_ca_certificate(self, uri=None, api=None, headers=None, param=''):
            """Retrieves the ca certificate by aliasname or get the ca certificates list.
            [Example]
            ${resp} = Fusion Api Get Ca Certificate | <uri> | <api> | <headers> | <param>
            """
            return self.ca.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_internal_ca_crl(self, api=None, headers=None):
            """Retrieves the contents of the CRL file maintained by the internal CA; in Base-64 encoded format, in the form of a string.
            [Example]
            ${resp} = Fusion Api Get Internal Ca Crl | <api> | <headers>
            """
            param = '/ca/crl'
            return self.ca.get(api=api, param=param, headers=headers)

        def fusion_api_revoke_certificate(self, name=None, api=None, headers=None):
            """Revokes a certificate signed by the internal CA.
            [Arguments]
            name: the name of the certificate to revoke
            [Example]
            ${resp} = Fusion Api Revoke Certificate | <name> | <api> | <headers>
            """
            return self.ca.revoke(name=name, api=api, headers=headers)

        def fusion_api_import_external_ca_certificates(self, body, api=None, headers=None):
            """Import external certificates into OneView
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Import External CA Certificates | <body> | <api> | <headers>
            """
            return self.ca.add(body, api=api, headers=headers)

        def fusion_api_remove_external_ca_certificates(self, aliasName, api=None, headers=None):
            """Remove external CA Certificates in Oneview
            [Arguments]
            aliasname: CA certificate's aliasname
            [Example]
            {resp} = Fusion Api Remove External CA Certificates | <aliasname> | <api> | <headers>
            """
            return self.ca.delete(aliasName, api=api, headers=headers)

        def fusion_api_upload_crl_by_aliasname(self, alias_name, localfile, api=None, headers=None):
            """
            [Arguments]
            aliasname: CA certificate's aliasname
            localfile: crl file path
            [Example]
            ${resp} = Fusion Api Upload CRL By Aliasname | <aliasname> | <localfile> | <api> | <headers>
            """
            return self.ca.upload(alias_name, localfile, api=api, headers=headers)

    class CertificateValidationConfigurationKeywords(object):
        """ Certificate Validation Configuration """
        def __init__(self):
            self.cv = CertificateValidationConfiguration(self.fusion_client)

        def fusion_api_get_certificate_validation_configuration(self, api=None, headers=None):
            """
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Certificate Validation Configuration | <api> | <headers>
            """
            return self.cv.get(api=api, headers=headers)

        def fusion_api_update_certificate_validation_configuration(self, config, api=None, headers=None):
            """
            [Arguments]
            Config = {
                "type": "CertValidationConfig",
                "certValidationConfig": {
                    "global.enforceStrictTrust": True,
                    "global.validateCertificate": True,
                    "global.allow.invalidCRL": True,
                    "global.checkCertificateRevocation": False,
                    "global.allow.noCRL": True
                },
                "okToReboot": "true"
            }
            [Example]
            ${resp} = Fusion Api Update Certificate Validation Configuration | <config> | <api> | <headers>
            """
            return self.cv.put(config, api=api, headers=headers)

    class WebServerCertificateKeywords(object):
        """ Web server certificate """
        def __init__(self):
            self.wsc = WebServerCertificate(self.fusion_client)

        def fusion_api_get_appliance_certificate(self, api=None, headers=None):
            """Get web server certificate information
            [Arguments]:
            [Example]
            ${resp} = Fusion Api Get Appliance Certificate | <api> | <headers>
            """
            return self.wsc.get(api=api, headers=headers)

        def fusion_api_generate_certificate_signing_request(self, body, api=None, headers=None):
            """Generate certificate signing request used to get certificate
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Generate Certificate Signing Request | <body> | <api> | <headers>
            """
            return self.wsc.post(body, api=api, headers=headers)

        def fusion_api_import_appliance_certificate(self, body, api=None, headers=None, param=''):
            """Used to import appliance certificate into OneView
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Import Appliance Certificate | <body> | <api> | <headers> | <param>
            """
            return self.wsc.put(body, api=api, headers=headers, param=param)

    class CertificateClientRabbitMqKeywords(object):
        """ Rabbit client certificate """
        def __init__(self):
            self.rabmq = CertificatesClientRabbitMq(self.fusion_client)

        def fusion_api_create_rabbitmq_client_certificate(self, body, uri=None, api=None, headers=None, param=''):
            """ Generates a self signed certificate or an internal CA signed certificate for RabbitMq clients.
            This is an asynchronous call. It is recommended that you poll for completion of the task and then use GET
            on the Task returned as part of Location header in the response body to get the certificate and the key.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
              ${resp} = Fusion Api Create Rabbitmq Client Certificates | <uri> | <body> | <api> | <headers>
            """
            return self.rabmq.post(body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_rabbitmq_client_certificate(self, param='', api=None, headers=None):
            """ Retrieve internal CA signed Rabbitmq client certificate.
            [Example]
              ${resp} = Fusion Api Get Rabbitmq Client Certificates | <param> | <api> | <headers>
            """
            return self.rabmq.get(param=param, api=api, headers=headers)

    class ConnectionsKeywords(object):
        """ Connections """
        def __init__(self):
            self.conn = Connections(self.fusion_client)

        def fusion_api_get_connections(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Connections
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Connections | <uri> | <param> | <api> | <headers>
            """
            return self.conn.get(uri=uri, api=api, headers=headers, param=param)

    class ConnectionTemplateKeywords(object):
        """ Connection template """
        def __init__(self):
            self.ct = ConnectionTemplate(self.fusion_client)

        def fusion_api_get_connection_templates(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of connection templates
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Connection Templates  | <uri> | <param> | <api> | <headers>
            """
            return self.ct.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_default_connection_template(self, api=None, headers=None):
            """Gets the default network connection template.  During a network create the default
            connection value will be inherited from this template.
            [Example]
            ${resp} = Fusion Api Get Default Connection Template  | <api> | <headers>
            """
            return self.ct.get_default(api=api, headers=headers)

        def fusion_api_update_connection_template(self, body, uri=None, api=None, headers=None):
            """Updates a specific connection template.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: the uri of a specific connection template to retrieve. if omitted, all are returned
            [Example]
            ${resp} = Fusion Api Update Connection Template  | <body> | <uri>  | <api> | <headers>
            """
            return self.ct.update(body, uri=uri, api=api, headers=headers)

        def fusion_api_update_default_connection_template(self, body, api=None, headers=None):
            """Updates the default network connection template.  During a network create the default
            connection value will be inherited from this template.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Default Connection Template  | <body> | <api> | <headers>
            """
            return self.ct.update_default(body, api=api, headers=headers)

    class DatacenterKeywords(object):
        """ Datacenter """
        def __init__(self):
            self.dc = Datacenter(self.fusion_client)

        def fusion_api_add_datacenter(self, body, api=None, headers=None):
            """Creates an Datacenter.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Datacenter  | <body> | <api> | <headers>
            """
            return self.dc.create(body, api, headers)

        def fusion_api_edit_datacenter(self, body, uri, api=None, headers=None):
            """Updates a Datacenter.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Datacenter  | <body> | <uri> | <api> | <headers>
            """
            return self.dc.update(body, uri, api, headers)

        def fusion_api_remove_datacenter(self, name=None, uri=None, api=None, headers=None):
            """Removes Datacenters. If name or uri are not specified, all datacenters are removed.
            [Arguments]
            name: The name of the resource to remove.
            uri: The uri of the resource to remove
            [Example]
            ${resp} = Fusion Api Remove Datacenter  | <name> | <uri> | <api> | <headers>
            """
            return self.dc.delete(name, uri, api, headers)

        def fusion_api_get_datacenter(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Datacenters.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Datacenter  | <uri> | <param> | <api> | <headers>
            """
            return self.dc.get(uri=uri, api=api, headers=headers, param=param)

    class DeviceManagerKeywords(object):
        """ Device manager """
        def __init__(self):
            self.dm = DeviceManager(self.fusion_client)

        def fusion_api_add_san_manager(self, body, providerId=None, uri=None, api=None, headers=None):
            """Adds a SAN Manager.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            providerId:
            [Example]
            ${resp} = Fusion Api Add San Manager  | <body> | <providerId> | <api> | <headers>
            """
            return self.dm.create(body, providerId, uri, api, headers)

        def fusion_api_edit_san_manager(self, body, uri, api=None, headers=None):
            """Updates a SAN Manager.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit San Manager  | <body> | <uri> | <api> | <headers>
            """
            return self.dm.update(body, uri, api, headers)

        def fusion_api_remove_san_manager(self, name=None, uri=None, api=None, headers=None):
            """Removes SAN Managers.
            [Arguments]
            name: The name of the resource to remove.
            uri: The uri of the resource to remove
            [Example]
            ${resp} = Fusion Api Remove San Manager  | <name> | <uri> | <api> | <headers>
            """
            return self.dm.delete(name, uri, api, headers)

        def fusion_api_get_san_manager(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAN Managers.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get San Manager  | <uri> | <param> | <api> | <headers>
            """
            return self.dm.get(uri=uri, api=api, headers=headers, param=param)

    class DriveEnclosureKeywords(object):
        """ Drive enclosure """
        def __init__(self):
            self.drive_enclosure = DriveEnclosures(self.fusion_client)

        def fusion_api_get_drive_enclosure(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Drive Enclosures.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Ethernet Networks  | <uri> | <param> | <api> | <headers>
            """
            return self.drive_enclosure.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_patch_drive_enclosure(self, body, uri, api=None, headers=None):
            """Issues a PATCH request to a drive enclosure. See REST-API docs for valid request bodies
            [Arguments]
            body: REQUIRED a list of dictionary containing patch operations
            [{"op":"replace","path":"/uidState","value":"Off"}]
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Patch Drive Enclosure | <body> | <uri> | <api> | <headers>
            """
            return self.drive_enclosure.patch(body, uri, api, headers)

        def fusion_api_put_drive_enclosure(self, body, uri, param='', api=None, headers=None):
            """Issues a PUT request to a drive enclosure. See REST-API docs for valid request bodies
            [Arguments]
            body: REQUIRED a dictionary containing put operations
            {"refreshState":"RefreshPending","powerState":"On"}
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Patch Drive Enclosure | <body> | <uri> | <api> | <headers>
            """
            return self.drive_enclosure.put(body=body, uri=uri, param=param, api=api, headers=headers)

    class SasLogicalJbodsKeywords(object):
        """ SAS logical JBOD """
        def __init__(self):
            self.sas_logical_jbods = SasLogicalJbods(self.fusion_client)

        def fusion_api_get_sas_logical_jbods(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Sas Logical JBODs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Sas Logical Jbods  | <uri> | <param> | <api> | <headers>
            """
            return self.sas_logical_jbods.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_post_sas_logical_jbods(self, body, api=None, headers=None):
            """
            Creates independent sas logical jbods
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Post Sas Logical Jbods | <body> | <api> | <headers>
            """
            return self.sas_logical_jbods.post(body=body, api=api, headers=headers)

        def fusion_api_delete_sas_logical_jbods(self, uri, api=None, headers=None):
            """Deletes independent sas logical jbods from the appliance based on  uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Sas Logical Jbods | <uri> | <api> | <headers> | <etag>
            """
            return self.sas_logical_jbods.delete(uri=uri, api=api, headers=headers)

        def fusion_api_edit_sas_logical_jbods(self, body, uri, api=None, headers=None):
            """Updates independent sas logical jbods
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Sas Logical Jbods | <body> | <uri> | <api> | <headers> | <etag>
            """
            return self.sas_logical_jbods.put(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_patch_sas_logical_jbods(self, body, uri, api=None, headers=None):
            """Issues a Patch request for independent sas logical jbods.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to modify.
            [Example]
            ${resp} = Fusion Api Patch Sas Logical Jbods | <body> | <uri> | <api> | <headers>
            """
            return self.sas_logical_jbods.patch(body=body, uri=uri, api=api, headers=headers)

    class SasLogicalJbodAttachmentsKeywords(object):
        """ SAS logical JBOD attachment """
        def __init__(self):
            self.sas_logical_jbod_attachments = SasLogicalJbodAttachments(self.fusion_client)

        def fusion_api_get_sas_logical_jbod_attachments(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Sas Logical JBOD Attachments.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Sas Logical Jbod Attachments  | <uri> | <param> | <api> | <headers>
            """
            return self.sas_logical_jbod_attachments.get(uri=uri, api=api, headers=headers, param=param)

    class DomainsKeywords(object):
        """ Domain """
        def __init__(self):
            self.domain = Domains(self.fusion_client)

    class EmailNotificationKeywords(object):
        """ Email notifications """
        def __init__(self):
            self.email = EmailNotification(self.fusion_client)

        def fusion_api_email_config(self, body, api=None, headers=None):
            """Configure the appliance to send an email notification, generated by specified alert filter queries
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Email Config | <body> | <api> | <headers>
            """
            param = "/email-config"
            return self.email.post(body, api, headers, param)

        def fusion_api_send_email(self, body, api=None, headers=None):
            """Sends email from appliance to specified user. Both HTML and text content are embedded in the single email message.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Send Email  | <body> | <api> | <headers>
            """
            param = "/send-email"
            return self.email.post(body, api, headers, param)

        def fusion_api_get_email_config(self, api=None, headers=None, param=''):
            """Retrieve email notification details with configured filters
            [Arguments]
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Email Config  | <api> | <headers> | <param>
            """
            return self.email.get(api=api, headers=headers, param=param)

    class ScopeKeywords(object):
        """ Scopes """
        def __init__(self):
            self.scope = Scope(self.fusion_client)

        def fusion_api_create_scope(self, body, api=None, headers=None):
            """Adds scope to setting page
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add scope | <body>s | <api> | <headers>
            """
            return self.scope.post(body, api, headers)

        def fusion_api_get_scope(self, uri=None, param='', api=None, headers=None):
            """Gets a scope
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Scope  | <uri> | <param> | <api> | <headers>
            """
            return self.scope.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_patch_scope(self, uri, body=None, api=None, headers=None, etag=None):
            """patch a scope
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Update Hardware Scope | <uri> | <body> | <api> | <headers> | <etag>
            """
            return self.scope.patch(uri=uri, body=body, api=api, headers=headers, etag=etag)

        def fusion_api_edit_scope(self, uri, body=None, api=None, headers=None, eTag=None):
            """Edit a scope
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Update Hardware Scope | <uri> | <body> | <api> | <headers> | <eTag>
            """

            return self.scope.put(uri=uri, body=body, api=api, headers=headers, eTag=eTag)

        def fusion_api_delete_scope(self, uri=None, api=None, headers=None):
            """Deletes a Scope from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            etag: the headers value to be modified with etag
            [Example]
            ${resp} = Fusion Api Delete Scope | <uri> | <api> | <headers>
            """
            return self.scope.delete(uri, api, headers)

    class ApplianceCertificateKeywords(object):
        """ Appliance certificates """
        def __init__(self):
            self.appliance_certificate = ApplianceCertificate(self.fusion_client)

        def fusion_api_get_appliance_certificate(self, api=None, headers=None):
            """Fusion API Get Appliance Certificate
            [Example]
            ${resp} = Fusion Api Get Appliance Certificate | <api> | <headers>
            """
            return self.appliance_certificate.get(api, headers)

        def fusion_api_create_appliance_selfsigned_certificate(self, body, api=None, headers=None):
            """Fusion API Create Appliance Selfsigned Certificate
            [Arguments]
            body
            [Example]
            ${resp} = Fusion Api Create Appliance Selfsigned Certificate | <body> | <api> | <headers>
            """
            return self.appliance_certificate.put(body, api, headers)

    class RemoteCertificateKeywords(object):
        """ Remote Certificates """
        def __init__(self):
            self.remote_certificate = RemoteCertificate(self.fusion_client)

        def fusion_api_get_remote_certificate(self, ip, api=None, headers=None):
            """Get Remote Certificate
            [Arguments]
            ip: Remote server IP address or hostname
            [Example]
            ${resp} = Fusion Api Get Remote Certificate | <ip> | <api> | <headers>
            """
            return self.remote_certificate.get(ip, api, headers)

    class ClientCertificateKeywords(object):
        """ Client certificates """
        def __init__(self):
            self.client_certificate = ClientCertificate(self.fusion_client)

        def fusion_api_get_client_certificate(self, ip, api=None, headers=None):
            """Get Client Certificate in One View
            [Arguments]
            ip: Client server IP address or hostname
            [Example]
            ${resp} = Fusion Api Get Client Certificate | <ip> | <api> | <headers>
            """
            return self.client_certificate.get(ip, api, headers)

        def fusion_api_import_client_certificate(self, body, api=None, headers=None):
            """Import Client Certificate to Oneview
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Import Client Certificate | <body> | <api> | <headers>
            """
            return self.client_certificate.post(body, api, headers)

        def fusion_api_update_client_certificate(self, aliasname, body, api=None, headers=None):
            """Update Client Certificate in Oneview
            [Arguments]
            aliasname: Server certificate's aliasname or thumprint
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Client Certificate | <aliasname> | <body> | <api> | <headers>
            """
            return self.client_certificate.put(aliasname, body, api, headers)

        def fusion_api_delete_client_certificate(self, aliasname, api=None, headers=None):
            """Delete Client Certificate in Oneview
            [Arguments]
            aliasname: Server certificate's aliasname or thumprint
            [Example]
            ${resp} = Fusion Api Delete Client Certificate | <aliasname> | <api> | <headers>
            """
            return self.client_certificate.delete(aliasname, api, headers)

        def fusion_api_validator_certificate(self, body, api=None, headers=None):
            """Validator CA or self-signed leaf Certificate or CA signed leaf certificate chain
            [Arguments]
            body: EQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Validator Certificate | <body> | <api> | <headers>
            """
            return self.client_certificate.post_validator(body, api, headers)

    class ServerCertificateKeywords(object):
        """ Server certificates """
        def __init__(self):
            self.server_certificate = ServerCertificate(self.fusion_client)

        def fusion_api_get_server_certificate(self, aliasname, api=None, headers=None):
            """Get Server Certificate in Oneview
            [Arguments]
            aliasname: Server certificate's aliasname or thumprint
            [Example]
            ${resp} = Fusion Api Get Server Certificate | <aliasname> | <api> | <headers>
            """
            return self.server_certificate.get(aliasname, api, headers)

        def fusion_api_import_server_certificate(self, body, api=None, headers=None):
            """Import Server Certificate to Oneview
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Import Server Certificate | <body> | <api> | <headers>
            """
            return self.server_certificate.post(body, api, headers)

        def fusion_api_update_server_certificate(self, aliasname, body, api=None, headers=None):
            """Update Server Certificate in Oneview
            [Arguments]
            aliasname: Server certificate's aliasname or thumprint
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Server Certificate | <aliasname> | <body> | <api> | <headers>
            """
            return self.server_certificate.put(aliasname, body, api, headers)

        def fusion_api_delete_server_certificate(self, aliasname, api=None, headers=None):
            """Delete Server Certificate in Oneview
            [Arguments]
            aliasname: Server certificate's aliasname or thumprint
            [Example]
            ${resp} = Fusion Api Delete Server Certificate | <aliasname> | <api> | <headers>
            """
            return self.server_certificate.delete(aliasname, api, headers)

    class CertificateStatusKeywords(object):
        """ Certificate status """
        def __init__(self):
            self.certificate_status = CertificateStatus(self.fusion_client)

        def fusion_api_get_certificate_status(self, api=None, headers=None):
            """Get Certificate  status in Oneview
            [Example]
            ${resp} = Fusion Api Get Server Certificate | <api> | <headers>
            """
            return self.certificate_status.get(api, headers)

    class RepositoryKeywords(object):
        """ Repository """
        def __init__(self):
            self.repository = Repository(self.fusion_client)

        def fusion_api_add_repository(self, body, api=None, headers=None):
            """Adds repository to setting page
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add repository | <body> | <api> | <headers>
            """
            return self.repository.post(body, api, headers)

        def fusion_api_get_repository(self, uri=None, param='', api=None, headers=None):
            """Get a repository
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Repository  | <uri> | <param> | <api> | <headers>
            """
            return self.repository.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_patch_repository(self, uri, body=None, api=None, headers=None):
            """Patch a repository
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Patch Repository | <uri> | <body> | <api> | <headers>
            """

            return self.repository.patch(uri=uri, body=body, api=api, headers=headers)

        def fusion_api_edit_repository(self, uri, body=None, api=None, headers=None):
            """Edit a repository
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Edit Repository | <uri> | <body> | <api> | <headers>
            """

            return self.repository.put(uri=uri, body=body, api=api, headers=headers)

        def fusion_api_delete_repository(self, uri, api=None, headers=None):
            """Delete a Repository from the appliance based on uri
            [Arguments]
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Repository | <uri> | <api> | <headers>
            """
            return self.repository.delete(uri=uri, api=api, headers=headers)

    class SshAccessKeywords(object):
        """ SSH access """
        def __init__(self):
            self.sshaccess = SshAccess(self.fusion_client)

        def fusion_api_get_ssh_access(self, uri=None, api=None, headers=None):
            """
            Gets the ssh access from appliance
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} =  Fusion Api Get Ssh Access | <uri> | <api> | <headers> |
            """
            return self.sshaccess.get(uri=uri, api=api, headers=headers)

        def fusion_api_edit_ssh_access(self, body, uri=None, api=None, headers=None):
            """
            Edits the ssh access for appliance
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} =  Fusion Api Edit Ssh Access | <body> | <uri> | <api> | <headers> |
            """
            return self.sshaccess.put(body=body, uri=uri, api=api, headers=headers)

    class EnclosureKeywords(object):
        """ Enclosure """
        def __init__(self):
            self.enclosure = Enclosure(self.fusion_client)

        def fusion_api_add_enclosure(self, body, api=None, headers=None):
            """Adds an enclosure to the appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Enclosure | <body>s | <api> | <headers>
            """
            return self.enclosure.add(body, api, headers)

        def fusion_api_edit_enclosure(self, body, uri, api=None, headers=None):
            """Update an enclosure. Currently the only attribute that can be updated is the name.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Enclosure | <body> | <uri> | <api> | <headers>
            """
            return self.enclosure.update(body, uri, api, headers)

        def fusion_api_patch_enclosure(self, body, uri, api=None, headers=None, etag=None):
            """Issues a PATCH request to an enclosure. See REST-API docs for valid request bodies
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Patch Enclosure | <body> | <uri> | <api> | <headers> | etag
            """
            return self.enclosure.patch(body, uri, api, headers, etag)

        def fusion_api_remove_enclosure(self, name=None, uri=None, param='', api=None, headers=None):
            """Removes an enclosure from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            param: you can use param=?force="true" to force remove an enclosure
            [Example]
            ${resp} = Fusion Api Remove Enclosure | <name> | <uri> | <param> | <api> | <headers>
            """
            return self.enclosure.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_enclosures(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Enclosures
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Enclosures  | <uri> | <param> | <api> | <headers>            """
            return self.enclosure.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_refresh_enclosure(self, body={"refreshState": "RefreshPending"}, uri=None, api=None, headers=None):
            """Refreshes a specified Enclosure URI
            [Arguments]
            uri: the uri of the resource to refresh.
            body: Request body to indicate refreshState and other parameters.
            [Example]
            ${resp} = Fusion Api Refresh Enclosure | <body> | <uri> | <api> | <headers>            """
            return self.enclosure.put(body, uri=uri, api=api, headers=headers)

        def fusion_api_import_server_hardware_type_for_enclosure(self, body, uri, api=None, headers=None):
            """ Import server hardware type for a specified Enclosure
            [Arguments]
            uri: the uri of import enclosure server hardware type.
            body: Request body to import enclosure server hardware type
            [Example]
            ${resp} = Fusion Api Import Server Hardware Type For Enclosure  | <body> | <uri> | <api> | <headers>
            """
            return self.enclosure.post(body, uri, api=api, headers=headers)

    class EnclosureGroupKeywords(object):
        """ EG """
        def __init__(self):
            self.enclosure_group = EnclosureGroup(self.fusion_client)

        def fusion_api_create_enclosure_group_payload(self, body, lig_map=None, api=None):
            """Creates the payload required to create an enclosure group
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            lig_map: REQUIRED a dictionary containng the LIG map to be used. eg: {1:"LIG1", 4:"LIG2"}
            [Example]
            ${resp} = Fusion Api Create Enclosure Group Payload | <body> | <lig_map> | <api>
            """
            return self.enclosure_group.make_body(api, body, lig_map)

        def fusion_api_create_enclosure_group(self, body, api=None, headers=None):
            """Creates an enclosure group
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Enclosure Group | <body> | <api> | <headers>
            """
            return self.enclosure_group.create(body, api, headers)

        def fusion_api_edit_enclosure_group(self, body, uri, api=None, headers=None):
            """Update an enclosure group. Currently the only attribute that can be updated is the name.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Enclosure | <body> | <uri> | <api> | <headers>
            """
            return self.enclosure_group.update(body, uri, api, headers)

        def fusion_api_delete_enclosure_group(self, name=None, uri=None, api=None, headers=None):
            """Deletes an enclosure  group from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Enclosure Group | <name> | <uri> | <api> | <headers>
            """
            return self.enclosure_group.delete(name, uri, api, headers)

        def fusion_api_get_enclosure_groups(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Enclosure Groups.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Enclosure Groups  | <uri> | <param> | <api> | <headers>
            """
            return self.enclosure_group.get(uri=uri, api=api, headers=headers, param=param)

    class MigratableVcDomainKeywords(object):
        """ VC domain migration """
        def __init__(self):
            self.migratableVcDomain = MigratableVcDomain(self.fusion_client)

        def fusion_api_create_compatibility_report(self, body, api=None, headers=None):
            """Generate a compatibility report.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Compatibility Report  | <body> | <api> | <headers>
            """
            return self.migratableVcDomain.create(body, api, headers)

        def fusion_api_build_create_compatibility_report(self, credentialDict=None, migrationVars=None, iloLicenseType='OneViewNoiLO', api=None, headers=None):
            """Generate a compatibility report.
            [Arguments]
            credentials: REQUIRED a dictionary containing oa and vcm credentials
            [Example]
            ${resp} = Fusion Api Build Create Compatibility Report | <credentialDict> | <migrationVars> | <iloLicenseType> | <api> | <headers>
            """
            return self.migratableVcDomain.build_create(credentialDict, migrationVars, iloLicenseType, api, headers)

        def fusion_api_get_compatibility_report(self, uri, param='', api=None, headers=None):
            """Gets a compatiblity report.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get Compatibility Report  | <uri> | <param> | <api> | <headers>
            """
            return self.migratableVcDomain.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_import_migratable_vcdomain(self, uri, body=None, api=None, headers=None):
            """
            """
            return self.migratableVcDomain.update(uri, body, api, headers)

        def fusion_api_delete_compatibility_report(self, body, api=None, headers=None):
            """
            """
            return self.migratableVcDomain.delete(body, api, headers)

    class EthernetNetworkKeywords(object):
        """ Ethernet networks """
        def __init__(self):
            self.ethernet_network = EthernetNetwork(self.fusion_client)

        def fusion_api_create_ethernet_network(self, body, api=None, headers=None):
            """Creates an ethernet network.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Ethernet Network  | <body> | <api> | <headers>
            """
            return self.ethernet_network.create(body, api, headers)

        def fusion_api_create_ethernet_bulk_networks(self, body, api=None, headers=None):
            """Creates ethernet networks in bulk based on a VLAN ID range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Ethernet Bulk Networks  | <body> | <api> | <headers>
            """
            return self.ethernet_network.bulk_create(body, api, headers)

        def fusion_api_edit_ethernet_network(self, body, uri, api=None, headers=None):
            """Updates an ethernet network.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Ethernet Network  | <body> | <uri> | <api> | <headers>
            """
            return self.ethernet_network.update(body, uri, api, headers)

        def fusion_api_delete_ethernet_network(self, name=None, uri=None, param='', api=None, headers=None):
            """Deletes ethernet networks in bulk based on name OR uri.
            [Arguments]
            name: The name of the network to delete.
            uri: The uri of the network to delete
            [Example]
            ${resp} = Fusion Api Delete Ethernet Network  | <name> | <uri> | <param> | <api> | <headers>
            """
            return self.ethernet_network.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_ethernet_networks(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Ethernet networks.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Ethernet Networks  | <uri> | <param> | <api> | <headers>
            """
            return self.ethernet_network.get(uri=uri, api=api, headers=headers, param=param)

    class EventKeywords(object):
        """ Events """
        def __init__(self):
            self.event = Event(self.fusion_client)

        def fusion_api_get_events(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Events.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Events | <uri> | <param> | <api> | <headers>
            """
            return self.event.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_events(self, body, api=None, headers=None):
            """Creates an event.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Events  | <body> | <api> | <headers>
            """
            return self.event.create(body, api, headers)

    class FabricKeywords(object):
        """ Fabrics """
        def __init__(self):
            self.fabric = Fabric(self.fusion_client)

        def fusion_api_get_fabric(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Fabrics.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Fabric  | <uri> | <param> | <api> | <headers>
            """
            return self.fabric.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_fabric_reserved_vlan_range(self, uri=None, param='', api=None, headers=None):
            """Gets the reserved vlan ID range for the fabric.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Fabric Reserved Vlan Range  | <uri> | <param> | <api> | <headers>
            """
            param = "/reserved-vlan-range%s" % param
            return self.fabric.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_fabric_reserved_vlan_range(self, body, uri=None, param='', api=None, headers=None):
            """Updates the reserved vlan ID range for the fabric.  Note: this is for Synergy only!
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            param: query parameters.  ex. ?force=true
            [Example]
            ${resp} = Fusion Api Update Fabric Reserved Vlan Range  | <body> | <uri>  | <param> | <api> | <headers>
            """
            param = "/reserved-vlan-range%s" % param
            return self.fabric.put(uri=uri, body=body, api=api, headers=headers, param=param)

        def fusion_api_delete_fabric(self, name=None, uri=None, api=None, headers=None):
            """Deletes a fabric based on name OR uri provided
            [Arguments]
            name: The name of the fabric to remove.
            uri: The uri of the fabric to remove
            [Example]
            ${resp} = Fusion Api Delete Fabric | <name> | <uri> | <api> | <headers>
            """
            return self.fabric.delete(name, uri, api, headers)

        def fusion_api_patch_fabric(self, uri, body, api=None, headers=None):
            """Patch a fabric based on uri provided
            [Arguments]
            uri: The uri of the fabric to patch
            body: The PATCH body to send
            [Example]
            ${resp} = Fusion Api Patch Fabric | <name> | <uri> | <api> | <headers>
            """
            return self.fabric.patch(uri, body, api, headers)

        def fusion_api_create_fabric_support_dump(self, uri, body, api=None, headers=None):
            """Create support dump for the specified fabric uri
            [Arguments]
            uri: The uri of the fabric for which to create support dump
            body: The support dump request body
            [Example]
            ${resp} = Fusion Api Create Fabric Support Dump | <uri> | <body>
            """
            params = '/support-dumps'
            return self.fabric.post(uri, body, api, headers, params)

        def fusion_api_download_fabric_support_dump(self, uri, localfile, api=None, headers=None):
            """Retrieves the specified support dump and saves it locally.
            [Arguments]
            uri: REQUIRED The uri of the support dump file
            localfile: REQUIRED The canonical filename to save locally
            [Example]
            ${resp} = Fusion Api Download Fabric Support Dump | <uri> | <localfile>
            """
            return self.fabric.get_file(uri=uri, localfile=localfile, api=api, headers=headers)

    class FcNetworkKeywords(object):
        """ FC Networks """
        def __init__(self):
            self.fc_network = FcNetwork(self.fusion_client)

        def fusion_api_create_fc_network(self, body, api=None, headers=None):
            """
            Create an FC network
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Fc Network | <body> | <api> | <headers>
            """
            return self.fc_network.create(body, api, headers)

        def fusion_api_edit_fc_network(self, body, uri, api=None, headers=None):
            """Updates an fc network.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Fc Network | <body> | <uri> | <api> | <headers>
            """
            return self.fc_network.update(body, uri, api, headers)

        def fusion_api_delete_fc_network(self, name=None, uri=None, api=None, headers=None):
            """Deletes an fc network from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Fc Network | <name> | <uri> | <api> | <headers>
            """
            return self.fc_network.delete(name, uri, api, headers)

        def fusion_api_get_fc_networks(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of FC networks.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Fc Networks  | <uri> | <param> | <api> | <headers>
            """
            return self.fc_network.get(uri=uri, api=api, headers=headers, param=param)

    class FcoeNetworkKeywords(object):
        """ FCOE networks """
        def __init__(self):
            self.fcoe_network = FcoeNetwork(self.fusion_client)

        def fusion_api_create_fcoe_network(self, body, api=None, headers=None):
            """
            Create an FCoE network
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Fcoe Network | <body> | <api> | <headers>
            """
            return self.fcoe_network.create(body, api, headers)

        def fusion_api_edit_fcoe_network(self, body=None, uri=None, api=None, headers=None):
            """Updates an FCoE network.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Fcoe Network | <body> | <uri> | <api> | <headers>
            """
            return self.fcoe_network.update(body, uri, api, headers)

        def fusion_api_patch_fcoe_network(self, body=None, uri=None, api=None, headers=None):
            """Updates an FCoE network using the PATCH http verb.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Patch Fcoe Network | <body> | <uri> | <api> | <headers>
            """
            return self.fcoe_network.patch(body, uri, api, headers)

        def fusion_api_delete_fcoe_network(self, name=None, uri=None, api=None, headers=None):
            """Deletes an FCoE network from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Fcoe Network | <name> | <uri> | <api> | <headers>
            """
            return self.fcoe_network.delete(name, uri, api, headers)

        def fusion_api_get_fcoe_networks(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of FCoE networks.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Fcoe Networks  | <uri> | <param> | <api> | <headers>
            """
            return self.fcoe_network.get(uri=uri, api=api, headers=headers, param=param)

    class FirmwareBundleKeywords(object):
        """ FW Bundles """
        def __init__(self):
            self.bundle = FirmwareBundle(self.fusion_client)

        def fusion_api_upload_firmware_bundle(self, localfile, api=None, headers=None):
            """Upload an SPP ISO image file or a hotfix file to the appliance.
            [Arguments]
            localfile: REQUIRED the canonical path and filename of the bundle file
            [Example]
            ${resp} = Fusion Api Upload Firmware Bundle   | <localfile> | <api> | <headers>
            """
            return self.bundle.upload(localfile, api, headers)

    class FirmwareDriverKeywords(object):
        """ FW Drivers """
        def __init__(self):
            self.driver = FirmwareDriver(self.fusion_client)

        def fusion_api_get_firmware_driver(self, uri=None, api=None, headers=None, param=''):
            """Get firmware list or firmware from appliance.
            [Arguments]
            uri: When uri is empty, get firmware driver list. When uri is not empty, get firmware driver
            [Example]
            ${resp} = Fusion Api Get Firmware Driver   | <uri> | <api> | <headers> | <param>
            """
            return self.driver.get(uri, api, headers, param)

        def fusion_api_remove_firmware_driver(self, name=None, uri=None, api=None, headers=None):
            """Remove firmware driver from appliance.
            [Arguments]
            name: When name is empty, remove firmware by uri
            [Example]
            ${resp} = Fusion Api Remove Firmware Driver   | <name> | <uri> | <api> | <headers>
            """
            return self.driver.delete(name, uri, api, headers)

        def fusion_api_create_firmware_bundle(self, body, api=None, headers=None):
            """Add a custom SPP to the appliance.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Firmware Bundle   | <body> | <api> | <headers>
            """
            return self.driver.post(body, api, headers)

    class GlobalSettingsKeywords(object):
        """ Global Settings """
        def __init__(self):
            self.settings = GlobalSettings(self.fusion_client)

        def fusion_api_get_global_settings(self, uri=None, api=None, headers=None, param=''):
            """Get global settings
            [Example]
            ${resp} = Fusion Api Get Global Settings   | <uri> | <api> | <headers> | <param>
            """
            return self.settings.get(uri, api, headers, param)

        def fusion_api_update_global_settings(self, body=None, api=None, headers=None):
            """Update global settings
            [Arguments]
            body:[{"name": "alertMax", "type": "SettingV2","value": "true"},]
            [Example]
            ${resp} = Fusion Api Update Global Settings | <body> | <api> | <headers>
            """
            return self.settings.update(body, api, headers)

    class HaNodesKeywords(object):
        """ HA Nodes """
        def __init__(self):
            self.ha_nodes = HaNodes(self.fusion_client)

        def fusion_api_edit_ha_nodes(self, body=None, uri=None, api=None, headers=None):
            """Updates an appliance cluster member in order to activate the standby or to remove it from the appliance cluster.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit HA Nodes | <body> | <uri> | <api> | <headers>
            """
            return self.ha_nodes.update(body, uri, api, headers)

        def fusion_api_patch_ha_nodes(self, body=None, uri=None, api=None, headers=None):
            """Updates an appliance cluster member in order to activate the standby or remove it from the appliance cluster.
            PUT and PATCH are functionally equivalent. For PATCH requests, the request body is an array of operations to apply to the JSON representation of the specified appliance.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Patch HA Nodes | <body> | <uri> | <api> | <headers>
            """
            return self.ha_nodes.patch(body, uri, api, headers)

        def fusion_api_delete_ha_nodes(self, uri=None, api=None, headers=None):
            """Removes an appliance cluster member from the high-availability appliance cluster.
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete HA Nodes  | <uri> | <api> | <headers>
            """
            return self.ha_nodes.delete(uri, api, headers)

        def fusion_api_get_ha_nodes(self, uri=None, param='', api=None, headers=None):
            """Retrieves information about all members of the high-availability appliance cluster.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get HA Nodes  | <uri> | <param> | <api> | <headers>
            """
            return self.ha_nodes.get(uri=uri, api=api, headers=headers, param=param)

    class IdPoolKeywords(object):
        """ ID pool """
        def __init__(self):
            self.idpool = IdPool(self.fusion_client)

        def fusion_api_allocate_pool(self, body, uri, api=None, headers=None):
            """Allocates one or more IDs from a pool. The allocator returned contains the list of allocated ids.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Allocate Pool | <body> | <uri> | <api> | <headers>
            """
            return self.idpool.allocate(body, uri, api, headers)

        def fusion_api_collect_pool(self, body, uri, api=None, headers=None):
            """Collects one or more IDs to be returned to a pool. The collector DTO that is returned contains the list of collected IDs
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Collect Pool | <body> | <uri> | <api> | <headers>
            """
            return self.idpool.collect(body, uri, api, headers)

        def fusion_api_enable_pool(self, body, uri, api=None, headers=None):
            """Sets the pool state to enabled or disabled
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Enable Pool | <body> | <uri> | <api> | <headers>
            """
            return self.idpool.enable(body, uri, api, headers)

        def fusion_api_generate_pool(self, uri, api=None, headers=None):
            """Generates a random range and returns it. Used to generate a range for validation prior to actually creating it.
            [Arguments]
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Generate Pool | <uri> | <api> | <headers>
            """
            return self.idpool.generate(uri, api, headers)

        def fusion_api_get_pool(self, uri=None, api=None, headers=None):
            """Gets a Pool specified by uri.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            [Example]
            ${resp} = Fusion Api Get Pool | <uri> | <api> | <headers>
            """
            return self.idpool.get(uri=uri, api=api, headers=headers)

        def fusion_api_validate_pool(self, body, uri, api=None, headers=None):
            """Validates a set of user specified IDs that you want to reserve in this pool.
            This API can be used to check if the specified IDs can be allocated.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Validate Pool | <body> | <uri> | <api> | <headers>
            """
            return self.idpool.validate(body, uri, api, headers)

    class IdPoolsIpv4RangeKeywords(object):
        """ IPv4 pool range """
        def __init__(self):
            self.ipv4range = IdPoolsIpv4Range(self.fusion_client)

        def fusion_api_create_ipv4_range(self, body, api=None, headers=None):
            """Creates a IPv4 Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Ipv4 Range  | <body> | <api> | <headers>
            """
            return self.ipv4range.create(body, api, headers)

        def fusion_api_edit_ipv4_range(self, body, uri, api=None, headers=None):
            """Updates an IPv4 Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Vmac Range | <body> | <uri> | <api> | <headers>
            """
            return self.ipv4range.update(body, uri, api, headers)

        def fusion_api_delete_ipv4_range(self, name=None, uri=None, api=None, headers=None):
            """Deletes a IPv4 range based on name OR uri.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Ipv4 Range | <name> | <uri> | <api> | <headers>
            """
            return self.ipv4range.delete(name, uri, api, headers)

        def fusion_api_get_ipv4_range(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of IPv4 Ranges.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Ipv4 Range | <uri> | <param> | <api> | <headers>
            """
            return self.ipv4range.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_allocate_ipv4_range(self, body, uri, api=None, headers=None):
            """Allocate an IPv4 Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to allocate .
            [Example]
            ${resp} = Fusion Api Allocate Range | <body> | <uri> | <api> | <headers>
            """
            return self.ipv4range.allocate(body, uri, api, headers)

        def fusion_api_collect_ipv4_range(self, body, uri, api=None, headers=None):
            """Collect an IPv4 Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to allocate .
            [Example]
            ${resp} = Fusion Api Collect Range | <body> | <uri> | <api> | <headers>
            """
            return self.ipv4range.collect(body, uri, api, headers)

        def fusion_api_get_ipv4_range_allocated_fragments(self, uri, api=None, headers=None):
            """Returns all fragments that have been allocated from a IPv4 Range
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get IPv4 Range Allocated Fragments | <uri> | <api> | <headers>
            """
            return self.ipv4range.get(uri=uri, api=api, headers=headers, param='/allocated-fragments')

        def fusion_api_get_ipv4_range_free_fragments(self, uri, api=None, headers=None):
            """Returns all the free fragments in a IPv4 Range.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get Ipv4 Range Free Fragments | <uri> | <api> | <headers>
            """
            return self.ipv4range.get(uri=uri, api=api, headers=headers, param='/free-fragments')

        def fusion_api_patch_ipv4_range(self, body, uri, param='', api=None, headers=None):
            """Patch an IPv4 Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to allocate .
            [Example]
            ${resp} = Fusion Api Patch Ipv4 Range | <body> | <uri> |<param> | <api> | <headers>
            """
            return self.ipv4range.patch(body, uri, param, api, headers)

    class IdPoolsIpv4SubnetKeywords(object):
        """ IPv4 subnet pools """
        def __init__(self):
            self.ipv4subnet = IdPoolsIpv4Subnet(self.fusion_client)

        def fusion_api_create_ipv4_subnet(self, body, sessionID=None, api=None, headers=None):
            """Creates a IPv4 Subnet.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Ipv4 Subnet  | <body> | <api> | <headers>
            """
            return self.ipv4subnet.create(body, sessionID, api, headers)

        def fusion_api_delete_ipv4_subnet(self, name=None, uri=None, api=None, headers=None):
            """Deletes a IPv4 Subnet based on name OR uri.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Ipv4 Subnet | <name> | <uri> | <api> | <headers>
            """
            return self.ipv4subnet.delete(name, uri, api, headers)

        def fusion_api_get_ipv4_subnet(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of IPv4 Subnet.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Ipv4 Subnet | <uri> | <param> | <api> | <headers>
            """
            return self.ipv4subnet.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_edit_ipv4_subnet(self, body, uri, api=None, headers=None):
            """Updates an IPv4 Subnet.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Ipv4 Subnet | <body> | <uri> | <api> | <headers>
            """
            return self.ipv4subnet.update(body, uri, api, headers)

        def fusion_api_allocate_ipv4_subnet(self, body, uri, api=None, headers=None):
            """Allocate an IPv4 Subnet.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to allocate .
            [Example]
            ${resp} = Fusion Api Allocate Subnet | <body> | <uri> | <api> | <headers>
            """
            return self.ipv4subnet.allocate(body, uri, api, headers)

        def fusion_api_collect_ipv4_subnet(self, body, uri, api=None, headers=None):
            """Collect an IPv4 Subnet.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to allocate .
            [Example]
            ${resp} = Fusion Api Collect Subnet | <body> | <uri> | <api> | <headers>
            """
            return self.ipv4subnet.collect(body, uri, api, headers)

        def fusion_api_patch_ipv4_subnet(self, body, uri, param='', api=None, headers=None):
            """Patch an IPv4 Subnet.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to allocate .
            [Example]
            ${resp} = Fusion Api Patch Ipv4 Subnet | <body> | <uri> | <param> |<api> | <headers>
            """
            return self.ipv4subnet.patch(body, uri, param, api, headers)

    class IdPoolsVmacRangeKeywords(object):
        """ VMAC range pools """
        def __init__(self):
            self.vmacrange = IdPoolsVmacRange(self.fusion_client)

        def fusion_api_create_vmac_range(self, body, api=None, headers=None):
            """Creates a VMAC Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Vmac Range  | <body> | <api> | <headers>
            """
            return self.vmacrange.create(body, api, headers)

        def fusion_api_allocate_vmac_range(self, body, uri, api=None, headers=None):
            """Allocates a set of IDs from a vmac range. The allocator returned contains the list of IDs successfully allocated.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Allocate Vmac Range | <body> | <uri> | <api> | <headers>
            """
            return self.vmacrange.allocate(body, uri, api, headers)

        def fusion_api_collect_vmac_range(self, body, uri, api=None, headers=None):
            """Collects a set of IDs back to a vmac range. The collector returned contains the list of IDs successfully collected.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Collect Vmac Range | <body> | <uri> | <api> | <headers>
            """
            return self.vmacrange.collect(body, uri, api, headers)

        def fusion_api_edit_vmac_range(self, body, uri, api=None, headers=None):
            """Updates an VMAC Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Vmac Range | <body> | <uri> | <api> | <headers>
            """
            return self.vmacrange.update(body, uri, api, headers)

        def fusion_api_delete_vmac_range(self, name=None, uri=None, api=None, headers=None):
            """Deletes a VMAC range based on name OR uri.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Vmac Range | <name> | <uri> | <api> | <headers>
            """
            return self.vmacrange.delete(name, uri, api, headers)

        def fusion_api_get_vmac_range(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of VMAC Ranges.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Vmac Range | <uri> | <param> | <api> | <headers>
            """
            return self.vmacrange.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_vmac_range_allocated_fragments(self, uri, api=None, headers=None):
            """Returns all fragments that have been allocated from a VMAC Range
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get Vmac Range Allocated Fragments | <uri> | <api> | <headers>
            """
            return self.vmacrange.get(uri=uri, api=api, headers=headers, param='/allocated-fragments')

        def fusion_api_get_vmac_range_free_fragments(self, uri, api=None, headers=None):
            """Returns all the free fragments in a VMAC Range.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get Vmac Range Free Fragments | <uri> | <api> | <headers>
            """
            return self.vmacrange.get(uri=uri, api=api, headers=headers, param='/free-fragments')

    class IdPoolsVsnRangeKeywords(object):
        """ VSN pool range """
        def __init__(self):
            self.vsnrange = IdPoolsVsnRange(self.fusion_client)

        def fusion_api_create_vsn_range(self, body, api=None, headers=None):
            """Creates a VSN Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Vsn Range  | <body> | <api> | <headers>
            """
            return self.vsnrange.create(body, api, headers)

        def fusion_api_allocate_vsn_range(self, body, uri, api=None, headers=None):
            """Allocates a set of IDs from a VSN range. The allocator returned contains the list of IDs successfully allocated.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Allocate Vsn Range | <body> | <uri> | <api> | <headers>
            """
            return self.vsnrange.allocate(body, uri, api, headers)

        def fusion_api_collect_vsn_range(self, body, uri, api=None, headers=None):
            """Collects a set of IDs back to a VSN range. The collector returned contains the list of IDs successfully collected.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Collect Vsn Range | <body> | <uri> | <api> | <headers>
            """
            return self.vsnrange.collect(body, uri, api, headers)

        def fusion_api_edit_vsn_range(self, body, uri, api=None, headers=None):
            """Updates an VSN Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Vsn Range | <body> | <uri> | <api> | <headers>
            """
            return self.vsnrange.update(body, uri, api, headers)

        def fusion_api_delete_vsn_range(self, name=None, uri=None, api=None, headers=None):
            """Deletes a VSN range based on name OR uri.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Vsn Range | <name> | <uri> | <api> | <headers>
            """
            return self.vsnrange.delete(name, uri, api, headers)

        def fusion_api_get_vsn_range(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of VSN Ranges.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Vsn Range | <uri> | <param> | <api> | <headers>
            """
            return self.vsnrange.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_vsn_range_allocated_fragments(self, uri, api=None, headers=None):
            """Returns all fragments that have been allocated from a VSN Range
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get Vsn Range Allocated Fragments | <uri> | <api> | <headers>
            """
            return self.vsnrange.get(uri=uri, api=api, headers=headers, param='/allocated-fragments')

        def fusion_api_get_vsn_range_free_fragments(self, uri, api=None, headers=None):
            """Returns all the free fragments in a VSN Range.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get Vsn Range Free Fragments | <uri> | <api> | <headers>
            """
            return self.vsnrange.get(uri=uri, api=api, headers=headers, param='/free-fragments')

    class IdPoolsVwwnRangeKeywords(object):
        """ VWWN pool range """
        def __init__(self):
            self.vwwnrange = IdPoolsVwwnRange(self.fusion_client)

        def fusion_api_create_vwwn_range(self, body, api=None, headers=None):
            """Creates a VWWN Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Vwwn Range  | <body> | <api> | <headers>
            """
            return self.vwwnrange.create(body, api, headers)

        def fusion_api_allocate_vwwn_range(self, body, uri, api=None, headers=None):
            """Allocates a set of IDs from a VWWN range. The allocator returned contains the list of IDs successfully allocated.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Allocate Vwwn Range | <body> | <uri> | <api> | <headers>
            """
            return self.vwwnrange.allocate(body, uri, api, headers)

        def fusion_api_collect_vwwn_range(self, body, uri, api=None, headers=None):
            """Collects a set of IDs back to a VWWN range. The collector returned contains the list of IDs successfully collected.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Collect Vwwn Range | <body> | <uri> | <api> | <headers>
            """
            return self.vwwnrange.collect(body, uri, api, headers)

        def fusion_api_edit_vwwn_range(self, body, uri, api=None, headers=None):
            """Updates an VWWN Range.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Vwwn Range | <body> | <uri> | <api> | <headers>
            """
            return self.vwwnrange.update(body, uri, api, headers)

        def fusion_api_delete_vwwn_range(self, name=None, uri=None, api=None, headers=None):
            """Deletes a VWWN range based on name OR uri.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Vwwn Range | <name> | <uri> | <api> | <headers>
            """
            return self.vwwnrange.delete(name, uri, api, headers)

        def fusion_api_get_vwwn_range(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of VWWN Ranges.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Vwwn Range | <uri> | <param> | <api> | <headers>
            """
            return self.vwwnrange.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_vwwn_range_allocated_fragments(self, uri, api=None, headers=None):
            """Returns all fragments that have been allocated from a VWWN Range
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get Vwwn Range Allocated Fragments | <uri> | <api> | <headers>
            """
            return self.vwwnrange.get(uri=uri, api=api, headers=headers, param='/allocated-fragments')

        def fusion_api_get_vwwn_range_free_fragments(self, uri, api=None, headers=None):
            """Returns all the free fragments in a VWWN Range.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve
            [Example]
            ${resp} = Fusion Api Get Vwwn Range Free Fragments | <uri> | <api> | <headers>
            """
            return self.vwwnrange.get(uri=uri, api=api, headers=headers, param='/free-fragments')

    class InterconnectTypesKeywords(object):
        """ IC Types """
        def __init__(self):
            self.ictypes = InterconnectTypes(self.fusion_client)

        def fusion_api_get_interconnect_types(self, param='', api=None, headers=None):
            """Gets a default or paginated collection of Interconnect Types.
            [Arguments]
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Interconnect Types | <param> | <api> | <headers>
            """
            return self.ictypes.get(api=api, headers=headers, param=param)

    class InterconnectKeywords(object):
        """ IC """
        def __init__(self):
            self.ic = Interconnect(self.fusion_client)

        def fusion_api_get_interconnect(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Interconnects.
            [Arguments]
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Interconnect | <param> | <api> | <headers>
            """
            return self.ic.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_interconnect_port_statistics(self, uri, param='', api=None, headers=None):
            """Gets the port statistics details for givenInterconnect
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get Interconnect Port Statistics | <uri> | <param> | <api> | <headers>
            """
            param = '/statistics/%s' % param
            return self.ic.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_patch_interconnect(self, body, uri, param='', api=None, headers=None):
            """Issues an Patch Interconnect request for Potash\Potassium modules
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to modify.
            [Example]
            ${resp} = Fusion Api Patch Interconnect | <body> | <uri> | <param> | <api> | <headers>
            """
            return self.ic.patch(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_interconnect_ports(self, uri, api=None, param='', headers=None):
            """Gets the port details for givenInterconnect
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get  Interconnect Ports | <uri> | <api> | <headers>
            """
            param = '/ports%s' % param
            return self.ic.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_edit_interconnect_ports(self, body, uri, api=None, param='', headers=None):
            """Updates the port details for given Interconnect
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Edit Interconnect Ports | <body> | <uri> | <api> | <headers>
            """
            param = '/update-ports%s' % param
            return self.ic.put(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_clear_interconnect_ports(self, body, uri, api=None, param='', headers=None):
            """Clear  the port  counter details for given Interconnect
            [Arguments]
            uri: REQUIRED the uri of the interconnect to perform the clear port statistics
            [Example]
            ${resp} = Fusion Api clear Interconnect Ports | <body> | <uri> | <api> | <headers>
            """
            param = '/statistics/reset%s' % param
            return self.ic.put(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_reapply_interconnect_configuration(self, uri, api=None, headers=None):
            """Asynchronously applies or re-applies the configuration to the given managed interconnect.
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Reapply Interconnect Configuration | <uri> | <api> | <headers>
            """
            param = '/configuration'
            return self.ic.put(body=None, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_reset_loop_and_pause_flood_protection(self, uri, api=None, headers=None):
            """AResets the Loop protection and the pause flood protection and stats of the managed interconnect.
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Reset Loop and Pause Flood Protection | <uri> | <api> | <headers>
            """
            param = '/resetportprotection'
            return self.ic.put(body=None, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_interconnect_pluggable_module_info(self, uri=None, api=None, param='', headers=None):
            """Gets the port details for givenInterconnect
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get  Interconnect Ports | <uri> | <api> | <headers>
            """
            param = '/pluggableModuleInformation/%s' % param
            return self.ic.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_interconnect_nameservers(self, uri=None, api=None, param='', headers=None):
            """Gets the nameServers details for given Interconnect. This info is for DirectAttach connection info
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get Interconnect NameServers | <uri> | <param> | <api> | <headers>
            """
            param = '/nameServers%s' % param
            return self.ic.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_certificate_info(self, uri=None, api=None, param='', headers=None):
            """Gets the certificate details for givenInterconnect
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get  Certificate Info | <uri> | <api> | <headers>
            """
            param = '/certificates/https/'
            return self.ic.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_upload_certificate_info(self, body, uri=None, api=None, param='', headers=None):
            """Uploads the certificate details for givenInterconnect
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Upload  Certificate Info | <body> | <uri> | <api> | <headers>
            """
            param = '/certificates/https/'
            return self.ic.put(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_certificate_request(self, body, uri=None, api=None, param='', headers=None):
            """Creates the certificate request for givenInterconnect
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Create  Certificate Request | <body> | <uri> | <api> | <headers>
            """
            param = '/certificates/https/certificaterequest'
            return self.ic.post(uri=uri, body=body, api=api, headers=headers, param=param)

    class InterconnectLinkTopologyKeywords(object):
        """ IC Link topology """
        def __init__(self):
            self.ilt = InterconnectLinkTopology(self.fusion_client)

        def fusion_api_get_interconnect_link_topology(self, api=None, headers=None):
            """ GET on /rest/interconnect-link-topologies
            [Example]
            ${resp} = Fusion Api Get Interconnect Link Topology | <api> | <headers>
            """
            return self.ilt.get(api=api, headers=headers)

    class InternalLinkSetKeywords(object):
        """ Internal Link Set """
        def __init__(self):
            self.ils = InternalLinkSets(self.fusion_client)

        def fusion_api_get_internal_link_sets(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Interconnect Link Sets
            [Arguments]
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Internal Link Sets | <param> | <api> | <headers>
            """
            return self.ils.get(uri=uri, api=api, headers=headers, param=param)

    class LicensesKeywords(object):
        """ Licenses """
        def __init__(self):
            self.license = Licenses(self.fusion_client)

        def fusion_api_add_license(self, key=None, license_type='LicenseV500', api=None, headers=None):
            """
            Adds a license to the appliance
            [Arguments]
            key: REQUIRED a string containing the license key to add
            [Example]
            ${resp} = Fusion Api Add License | <key> | <license_type> | <api> | <headers>
            """
            return self.license.add(key, license_type, api, headers)

        def fusion_api_get_licenses(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of licenses.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Licenses | <uri> | <param> | <api> | <headers>
            """
            return self.license.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_remove_license(self, uri=None, api=None, headers=None):
            """Deletes a License from the appliance based on uri
            [Arguments]
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Remove License | <uri> | <api> | <headers>
            """
            return self.license.delete(uri=uri, api=api, headers=headers)

        def fusion_api_remove_all_licenses(self):
            """Deletes All Licenses from the appliance
            [Arguments]
            None
            [Example]
            Fusion API Remove All Licenses
            """

            all_licenses = self.fusion_api_get_licenses()

            for lic in all_licenses['members']:
                response = self.fusion_api_remove_license(uri=lic['uri'])

                if response.status_code != 204:
                    logger._log_to_console_and_log_file("Unable to delete license with key: %s" % lic['key'])
                    logger._log_to_console_and_log_file("Status code of response: %s" % response.status_code)
                    BuiltIn().fail("Expected status code was 204")
                else:
                    logger._log_to_console_and_log_file("Successfully deleted license with key: %s" % lic['key'])

    class LogicalDownlinkKeywords(object):
        """ Logical Downlink """
        def __init__(self):
            self.ld = LogicalDownlink(self.fusion_client)

        def fusion_api_get_logical_downlink(self, uri=None, api=None, headers=None, param=''):
            """Gets a default or paginated collection of Logical Downlinks.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Logical Downlink | <uri> | <param> | <api> | <headers>
            """
            return self.ld.get(uri=uri, api=api, headers=headers, param=param)

    class LogicalInterconnectGroupKeywords(object):
        """ LIG """
        def __init__(self):
            self.lig = LogicalInterconnectGroup(self.fusion_client)

        def fusion_api_create_lig(self, body, api=None, headers=None):
            """
            Creates an LIG
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Lig | <body> | <api> | <headers>
            """
            return self.lig.create(body, api, headers)

        def fusion_api_edit_lig(self, body, uri, api=None, headers=None, etag=None):
            """Updates an LIG
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Lig | <body> | <uri> | <api> | <headers> | <etag>
            """
            return self.lig.update(body, uri, api, headers, etag)

        def fusion_api_create_lig_payload(self, **kwargs):
            """ Create the LIG payload """

            return self.lig.make_body(**kwargs)

        def fusion_api_delete_lig(self, name=None, uri=None, api=None, headers=None, etag=None):
            """Deletes an LIG from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Lig | <name> | <uri> | <api> | <headers> | <etag>
            """
            return self.lig.delete(name=name, uri=uri, api=api, headers=headers, etag=etag)

        def fusion_api_get_lig(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of LIGs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Lig | <uri> | <param> | <api> | <headers>
            """
            return self.lig.get(uri=uri, param=param, api=api, headers=headers)

    class LogicalInterconnectKeywords(object):
        """ LI """
        def __init__(self):
            self.li = LogicalInterconnect(self.fusion_client)

        def fusion_api_delete_li_interconnect(self, location, api=None, headers=None):
            """Deletes an interconnect from a LI location
            [Arguments]
            location: REQUIRED a filter string specifying the interconnect to remove (Ex. ?location=Enclosure:/rest/enclosures/09XXX,Bay:1 )
            [Example]
            ${resp} = Fusion Api Delete Li Interconnect | <location> | <api> | <headers>
            """
            return self.li.delete(location=location, api=api, headers=headers)

        def fusion_api_get_li(self, uri=None, api=None, headers=None, param=''):
            """Gets a default or paginated collection of LIs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            [Example]
            ${resp} = Fusion Api Get Li | <uri> | <api> | <headers>
            """
            return self.li.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_li_ethernet_settings(self, uri, api=None, headers=None):
            """Gets the ethernetSettings for the given LI
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get Li Ethernet Settings | <uri> | <api> | <headers>
            """
            param = '/ethernetSettings'
            return self.li.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_li_fcoe_settings(self, uri, api=None, headers=None):
            """Gets the fcoeSettings for the given LI
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get Li Fcoe Settings | <uri> | <api> | <headers>
            """
            param = '/fcoeSettings'
            return self.li.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_generate_li_forwarding_information_base_dump_file(self, uri, api=None, headers=None):
            """Generates the fowarding information base dump file for the given LI
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Generate Li Forwarding Information Base Dump File | <uri> | <api> | <headers>
            """
            param = '/forwarding-information-base'
            return self.li.post(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_li_forwarding_information_base_dump_file(self, uri, localfile, api=None, headers=None):
            """Gets the fowarding information base dump file for the given LI
            [Arguments]
            uri: REQUIRED the uri of the dump file to retrieve (LI + filename)
            localfile: filter parameters
            [Example]
            ${resp} = Fusion Api Get Li Forwarding Information Base Dump File | <uri> | <localfile> | <api> | <headers>
            """
            return self.li.get_file(uri=uri, localfile=localfile, api=api, headers=headers)

        def fusion_api_get_li_forwarding_information_base(self, uri, param='', api=None, headers=None):
            """Gets the fowarding information base data for the given LI
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: filter parameters
            [Example]
            ${resp} = Fusion Api Get Li Forwarding Information Base | <uri> | <param> | <api> | <headers>
            """
            param = '/forwarding-information-base%s' % param
            return self.li.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_li_internal_vlans(self, uri, param='', api=None, headers=None):
            """Gets the internal VLAN IDs for the provisioned networks on a logical interconnect.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: filter parameters
            [Example]
            ${resp} = Fusion Api Get Li Forwarding Information Base | <uri> | <param> | <api> | <headers>
            """
            param = '/internalVlans%s' % param
            return self.li.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_patch_li(self, body=None, uri=None, api=None, headers=None):
            """Updates an LI using the PATCH http verb.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Patch LI | <body> | <uri> | <api> | <headers>
            """
            return self.li.patch(body, uri, api, headers)

        def fusion_api_get_li_port_monitor_configuration(self, uri, api=None, headers=None):
            """Gets the Port Monitor for the given LI
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get Li Port Monitor Configuration | <uri> | <api> | <headers>
            """
            param = '/port-monitor'
            return self.li.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_li_ethernet_settings(self, body=None, uri=None, api=None, headers=None):
            """Updates the ethernetSettings for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update LI Ethernet Settings | <body> | <uri> | <api> | <headers>
            """
            param = '/ethernetSettings'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_reapply_li_configuration(self, uri, api=None, headers=None):
            """Asynchronously applies or re-applies the logical interconnect configuration to all managed interconnects.
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Reapply LI Configuration | <uri> | <api> | <headers>
            """
            param = '/configuration'
            return self.li.update(body=None, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_li_fcoe_settings(self, body=None, uri=None, api=None, headers=None):
            """Updates the fcoeSettings for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update LI FCoE Settings | <body> | <uri> | <api> | <headers>
            """
            param = '/fcoeSettings'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_li_internal_networks(self, body=None, uri=None, api=None, headers=None):
            """Updates the internalNetworks for the given LI
            [Arguments]
            body: REQUIRED a LIST containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update LI Internal Networks | <body> | <uri> | <api> | <headers>
            """
            param = '/internalNetworks'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_li_port_monitor_configuration(self, body=None, uri=None, api=None, headers=None):
            """Updates the Port Monitor for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update LI Port Monitor Configuration | <body> | <uri> | <api> | <headers>
            """
            param = '/port-monitor'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_li_telemetry_configuration(self, body=None, uri=None, api=None, headers=None):
            """Updates the telemetry configuration for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update LI Telemetry Configuration | <body> | <uri> | <api> | <headers>
            """
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param="")

        def fusion_api_update_from_group(self, uri, api=None, headers=None):
            """Updates the LI to match it's LIG
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update From Group | <uri> | <api> | <headers>
            """
            param = '/compliance'
            return self.li.update(body=None, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_li_upgrade_firmware(self, body=None, uri=None, api=None, param='', headers=None):
            """ Initiate the firmware upgrade task using uploaded upgrade image
            Fusion Api Li Upgrade Firmware
            [Arguments]
            localfile:REQUIRED the filename of the .iso patch file
            [Example]
            ${resp} = Fusion Api LI Upgrade Appliance Firmware   | <localfile> | <api> | <headers>
            """
            param = '/firmware'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_qos_aggregated_configuration(self, body=None, uri=None, api=None, headers=None):
            """Updates the qos-aggregated-configuration for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update qos aggregated configuration| <body> | <uri> | <api> | <headers>
            """
            param = '/qos-aggregated-configuration'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_redistribute_logins(self, body=None, uri=None, api=None, headers=None):
            """Updates the redistribute logins for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update Redistribute Logins| <body> | <uri> | <api> | <headers>
            """
            param = '/redistributeLogins'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_snmp_configuration(self, body=None, uri=None, api=None, headers=None):
            """Updates the snmp_configuration for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update snmp configuration| <body> | <uri> | <api> | <headers>
            """
            param = '/snmp-configuration'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_sflow_configuration(self, body=None, uri=None, api=None, headers=None):
            """Updates the sflow_configuration for the given LI
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update sflow configuration| <body> | <uri> | <api> | <headers>
            """
            param = '/sflow-configuration'
            return self.li.update(body=body, uri=uri, api=api, headers=headers, param=param)

    class LogicalSwitchGroupKeywords(object):
        """ LSG """
        def __init__(self):
            self.lsg = LogicalSwitchGroup(self.fusion_client)

        def fusion_api_create_lsg(self, body, api=None, headers=None):
            """
            Creates an LSG
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Lsg | <body> | <api> | <headers>
            """
            return self.lsg.create(body, api, headers)

        def fusion_api_edit_lsg(self, body, uri, api=None, headers=None):
            """Updates an LSG
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Lsg | <body> | <uri> | <api> | <headers>
            """
            return self.lsg.update(body, uri, api, headers)

        def fusion_api_delete_lsg(self, name=None, uri=None, api=None, headers=None):
            """Deletes an LSG from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Lsg | <name> | <uri> | <api> | <headers>
            """
            return self.lsg.delete(name=name, uri=uri, api=api, headers=headers)

        def fusion_api_get_lsg(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of LSGs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Lsg | <uri> | <param> | <api> | <headers>
            """
            return self.lsg.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_lsg_default_settings(self, api=None, headers=None):
            """Gets the default settings for LSGs.

            [Example]
            ${resp} = Fusion Api Get Lsg Default Settings| <api> | <headers>
            """
            return self.lsg.get(api=api, param='/defaultSettings', headers=headers)

        def fusion_api_get_lsg_setting(self, uri, settingsId=None, api=None, headers=None):
            """Gets a particular LSG setting.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            [Example]
            ${resp} = Fusion Api Get Lsg Setting | <uri> | <settingsId> | <api> | <headers>
            """
            param = '/settings/%s' % (settingsId)
            return self.lsg.get(uri=uri, api=api, param=param, headers=headers)

    class LogicalSwitchKeywords(object):
        """ LS """
        def __init__(self):
            self.ls = LogicalSwitch(self.fusion_client)

        def fusion_api_create_ls(self, body, api=None, headers=None):
            """
            Creates an LS
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create LS | <body> | <api> | <headers>
            """
            return self.ls.post(body, api, headers)

        def fusion_api_delete_ls(self, name=None, uri=None, api=None, headers=None):
            """Deletes an LS
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete LS | <name> | <uri> | <api> | <headers>
            """
            return self.ls.delete(name=name, uri=uri, api=api, headers=headers)

        def fusion_api_get_ls(self, uri=None, api=None, headers=None, param=''):
            """Gets a default or paginated collection of LSs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            [Example]
            ${resp} = Fusion Api Get Li | <uri> | <api> | <headers>
            """
            return self.ls.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_ls(self, body=None, uri=None, api=None, headers=None):
            """Updates an LS
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Update LS | <body> | <uri> | <api> | <headers>
            """
            return self.ls.put(body, uri, api, headers)

    class SecurityStandardsKeywords(object):
        """ Security standards """
        def __init__(self):
            self.security_standards = SecurityStandards(self.fusion_client)

        def fusion_api_create_security_compatibility_report(self, body, uri=None, api=None, headers=None, param='/compatibility-report'):
            """Creates compatibility for the given target mode - FIPS/CNSA
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Security Compatibility Report  | <body> | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.post(uri=uri, api=api, headers=headers, body=body, param=param)

        def fusion_api_update_security_compatibility_report(self, body, uri=None, api=None, headers=None, param='/compatibility-report?force=true'):
            """Updates compatibility for the given target mode
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Security Compatibility Report  | <body> <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.post(uri=uri, api=api, headers=headers, body=body, param=param)

        def fusion_api_get_security_compatibility_report(self, uri=None, api=None, headers=None, param='/compatibility-report'):
            """Get existing compatibility report
            [Example]
            ${resp} = Fusion Api Get Security Compatibility Report  | <uri> | <api> | <headers>
            """
            return self.security_standards.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_delete_security_compatibility_report(self, uri=None, api=None, headers=None, param='/compatibility-report'):
            """Delete existing compatibility report
            [Example]
            ${resp} = Fusion Api Delete Security Compatibility Report  | <uri> | <api> | <headers>
            """
            return self.security_standards.delete(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_change_security_mode(self, body, uri=None, api=None, headers=None, param='/modes/current-mode'):
            """Does Security Mode Change- FIPS/CNSA/LEGACY.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Edit Security Modes  | <body> | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.put(uri=uri, api=api, headers=headers, body=body, param=param)

        def fusion_api_get_security_modes(self, uri=None, api=None, headers=None, param='/modes'):
            """Gets a list of Security modes
            [Example]
            ${resp} = Fusion Api Get Security Modes  | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_current_security_mode(self, uri=None, api=None, headers=None, param='/modes/current-mode'):
            """Gets a list of Security modes
            [Example]
            ${resp} = Fusion Api Get Current Security Mode  | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_security_modeName(self, uri=None, api=None, headers=None, param=''):
            """Gets a list of Security modes
            [Example]
            ${resp} = Fusion Api Get Security ModeName  | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_compliance_validator(self, body, uri=None, api=None, headers=None, param='/compliancevalidator'):
            """Validate device and/or certificate
            [Example]
                ${resp} = Fusion Api Compliance Validator  | <body> | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.post(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_update_security_protocols(self, body, uri=None, api=None, headers=None, param='/protocols'):
            """Update security protocols
            [Example]
                ${resp} = Fusion Api Update Security Protocols  | <body> | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.put(body=body, uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_security_protocols(self, uri=None, api=None, headers=None, param='/protocols'):
            """Get a list of security protocols
            [Example]
            ${resp} = Fusion Api Get Security Protocols  | <uri> | <api> | <headers> | <param>
            """
            return self.security_standards.get(uri=uri, api=api, headers=headers, param=param)

    class LoginDetailsKeywords(object):
        """ Login details """
        def __init__(self):
            self.logindetails = LoginDetails(self.fusion_client)

        def fusion_api_get_login_details(self, api=None, headers=None):
            """This service provides REST APIs to list the login details
            Example:
            |${resp} = |Fusion Api Get Login Details | <api> | <headers>
            """
            return self.logindetails.get(api=api, headers=headers)

    class LoginDomainKeywords(object):
        """ Login domain """
        def __init__(self):
            self.logindomain = LoginDomain(self.fusion_client)

        def fusion_api_add_directory(self, body, api=None, headers=None):
            """Adds a Directory for user authentication
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Directory  | <body> | <api> | <headers>
            """
            return self.logindomain.create(body, api, headers)

        def fusion_api_edit_directory(self, body, uri, api=None, headers=None):
            """Updates a Directory.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Directory | <body> | <uri> | <api> | <headers>
            """
            return self.logindomain.update(body, uri, api, headers)

        def fusion_api_delete_directory(self, name=None, uri=None, api=None, headers=None):
            """Deletes a directory based on name OR uri.
            [Arguments]
            name: The name of the directory to delete.
            uri: The uri of the directory to delete
            [Example]
            ${resp} = Fusion Api Delete Directory | <name> | <uri> | <api> | <headers>
            """
            return self.logindomain.delete(name, uri, api, headers)

        def fusion_api_get_directory(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Directories.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Directory | <uri> | <param> | <api> | <headers>
            """
            return self.logindomain.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_directory_groups(self, body, api=None, headers=None):
            """List Groups for a specified directory configured in the appliance. Group names are returned as list of strings.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Get Directory Groups | <body> | <api> | <headers>
            """
            return self.logindomain.groups(body, api, headers)

        def fusion_api_get_directory_users(self, body, api=None, headers=None):
            """List users who are members of the groups with one or more appliance roles assigned to it.
            User names are returned as list of strings. These Users have login privileges to the appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Get Directory Users | <body> | <api> | <headers>
            """
            return self.logindomain.users(body, api, headers)

        def fusion_api_validate_directory(self, body, api=None, headers=None):
            """Validates a Directory for user authentication
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Validate Directory  | <body> | <api> | <headers>
            """
            return self.logindomain.validate(body, api, headers)

    class LoginDomainsGroupToRoleMappingKeywords(object):
        """ Login domain group to role mapping """
        def __init__(self):
            self.LoginDomainsGroupToRoleMapping = LoginDomainsGroupToRoleMapping(self.fusion_client)

        def fusion_api_assign_roles_to_directory_group(self, body, api=None, headers=None):
            """Assign appliance roles to the directory group. User credentials are required for directory access.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements for Group to Roles Mapping per Group for Validation
            [Example]
            ${resp} = Fusion Api Assign Roles To Directory Group  | <body> | <api> | <headers>
            """
            return self.LoginDomainsGroupToRoleMapping.create(body, api, headers)

        def fusion_api_update_group_role_assignment(self, body, api=None, headers=None):
            """Update role assignment to a directory group.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements for Group to Roles Mapping per Group for Validation
            [Example]
            ${resp} = Fusion Api Update Group Role Assignment | <body> | <api> | <headers>
            """
            return self.LoginDomainsGroupToRoleMapping.update(body, api, headers)

        def fusion_api_delete_group_role_assignment(self, name=None, uri=None, api=None, headers=None):
            """Delete Directory Group Role Assignment.
            [Arguments]
            name: The name of the group to delete.
            uri: The uri of the group to delete
            [Example]
            ${resp} = Fusion Api Delete Group Role Assignment | <name> | <uri> | <api> | <headers>
            """
            return self.LoginDomainsGroupToRoleMapping.delete(name, uri, api, headers)

        def fusion_api_get_group_role_assignment(self, uri=None, param='', api=None, headers=None):
            """Retrieve role assignments for directory group under a directory/all directories group or a specify group.
            [Arguments]
            uri: the uri of the specify directory or group. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Group Role Assignment | <uri> | <param> | <api> | <headers>
            """
            return self.LoginDomainsGroupToRoleMapping.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_validate_group_and_roles(self, body, api=None, headers=None):
            """Validate Group and Roles
            [Arguments]
            body: REQUIRED a dictionary containing request body elements for Group to Roles Mapping per Group for Validation
            [Example]
            ${resp} = Fusion Api Validate Group And Roles  | <body> | <api> | <headers>
            """
            return self.LoginDomainsGroupToRoleMapping.validate(body, api, headers)

    class LoginDomainsLoginCertificatesKeywords(object):
        """ Login domain login certificates """
        def __init__(self):
            self.login_certificates = LoginDomainsLoginCertificates(self.fusion_client)

        def fusion_api_get_login_domains_login_certificates(self, api=None, headers=None, param=''):
            """Get the Login Certificate details
            [Arguments]
            param: query parameters
            [Example]
            | ${resp} = Fusion Api Get Login Certificates  | <api> | <headers> | <param> |
            """
            return self.login_certificates.get(api, headers, param)

        def fusion_api_edit_login_domains_login_certificates(self, body, param='', api=None, headers=None):
            """Put the Login Certificate details to Appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            | ${resp} = Fusion Api Put Login Certificates  | <body> | <param> | <api> | <headers> |
            """
            return self.login_certificates.update(body, param, api, headers)

    class LoginDomainsGlobalSettingsKeywords(object):
        """ LD global settings """
        def __init__(self):
            self.domain_settings = LoginDomainsGlobalSettings(self.fusion_client)

        def fusion_api_get_login_domains_global_settings(self, api=None, headers=None, param=''):
            """Get Login Domains Global Settings for specified appliance
            [Arguments]
            host: Required hostname or IP of appliance
            [Example]
            | ${resp} = Fusion Api Get Login Domains Global Settings  | <api> | <headers> | <param> |
            """
            return self.domain_settings.get(api, headers, param)

        def fusion_api_edit_login_domains_global_settings(self, body, param='', api=None, headers=None):
            """Put Login Domains Global Settings for specified appliance
            [Arguments]
            body: REQUIRED a dictionary containing put operations
            [Example]
            | ${resp} = Fusion Api Edit Login Domains Global Settings  | <body> | <param> | <api> | <headers> |
            """
            return self.domain_settings.put(body, param, api, headers)

    class LoginSessionKeywords(object):
        """ Login session """
        def __init__(self):
            self.loginsession = LoginSession(self.fusion_client)

        def fusion_api_login_appliance(self, host, creds, headers=None):
            """Login to the appliance as the specified user
            [Arguments]
            host: the appliance IP or hostname
            creds: a ditionary containing userName and password attributes
            [Example]
            ${resp} = Fusion Api Login Appliance | <host> | <creds> | <headers>
            """
            # logger._log_to_console_and_log_file("Logging into appliance")
            return self.loginsession.login(host, creds, headers)

        def fusion_api_two_factor_login_appliance(self, host, cert, headers=None):
            """Login to the appliance as the specified user by certificate
            [Arguments]
            host: the appliance IP or hostname
            cert: path to ssl client cert file (.pem), which should contain private key and certificate
            [Example]
            ${resp} = Fusion Api Two Factor Login Appliance | <host> | <cert> | <headers>
            """
            return self.loginsession.login_by_cert(host, cert, headers)

        def fusion_api_logout_appliance(self, headers=None):
            """Logs the current active user out of the appliance
            [Example]
            ${resp} = Fusion Api Logout Appliance
            """
            # logger._log_to_console_and_log_file("Logging out of appliance")
            return self.loginsession.logout(headers)

        def fusion_api_get_active_sessions(self):
            """Returns the list of active user sessions. You can use Fusion Api Switch Active User to any of these users.
            [Example]
            ${resp} = Fusion Api Get Active Sessions
            """
            return self.loginsession.get_active_sessions()

        def fusion_api_get_active_user(self):
            """Returns the current active user
            [Example]
            ${resp} = Fusion Api Get Active User
            """
            return self.loginsession.get_active_user()

        def fusion_api_switch_active_user(self, user):
            """Makes the specified user the active user.
            NOTE: the user must have already logged in
            [Arguments]
            user: Required the user to become the active user
            [Example]
            ${resp} = Fusion Api Switch Active User | <user>
            """
            # logger._log_to_console_and_log_file("Switched to user: %s" % user)
            return self.loginsession.switch_active_user(user)

        def fusion_api_modify_active_permissions(self, body, api=None, headers=None):
            """Returns the new created user session from an existing session, controlling which user assigned permissions are active and inactive
            [Example]
            ${resp} = Fusion Api Modify Active Permissions | <body> | <api> | <headers>
            """
            return self.loginsession.modify_active_permissions(body, api, headers)

        def fusion_api_delete_session(self, api=None, headers=None, sessionId=None):
            """Remove user session by invoking an explicit logout. Session token must be provided in the request header
            [Example]
            ${resp} = Fusion Api Delete Permissions | <api> | <headers> | <sessionId>
            """
            return self.loginsession.delete_session(api, headers, sessionId)

        def fusion_api_set_active_session(self, sessionId):
            """Set the given sessionId as current active sessionID.
            [Arguments]
            sessionId: OTE3ODQxNTUxMjAz9CMw8cGWWMx9urJno6G89gIZkJMneJT0
            Example
            |${resp} = |Fusion Api Set Active Session | sessionId |
            """
            return self.loginsession.set_active_session(sessionId)

    class ManagedSanKeywords(object):
        """ Managed SAN """
        def __init__(self):
            self.ms = ManagedSan(self.fusion_client)

        def fusion_api_update_managed_san(self, body, uri, api=None, headers=None):
            """Updates a Managed SAN.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Update Managed San  | <body> | <uri> | <api> | <headers>
            """
            return self.ms.update(body, uri, api, headers)

        def fusion_api_get_managed_san(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Managed SANs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Managed San  | <uri> | <param> | <api> | <headers>
            """
            return self.ms.get(uri=uri, api=api, headers=headers, param=param)

    class MetricStreamingKeywords(object):
        """ Metric streaming """
        def __init__(self):
            self.metrics = MetricStreaming(self.fusion_client)

        def fusion_api_update_metrics_configuration(self, body, api=None, headers=None):
            """Updates the metrics configuration with the new values. Overwrites the existing configuration.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Metrics Configuraiton  | <body> | <api> | <headers>
            """
            return self.metrics.update(body, api, headers)

        def fusion_api_get_metrics_capability(self, api=None, headers=None):
            """Fetches the list of resource types and supported metrics that OneView is capable of relaying.
            [Example]
            ${resp} = Fusion Api Get Metrics Capability  | <api> | <headers>
            """
            return self.metrics.get(api=api, headers=headers, param='/capability')

        def fusion_api_get_metrics_configuration(self, api=None, headers=None):
            """Fetches the current configuration for which metrics are being relayed.
            [Example]
            ${resp} = Fusion Api Get Metrics Configuration | <api> | <headers>
            """
            return self.metrics.get(api=api, headers=headers, param='/configuration')

    class NetworkSetKeywords(object):
        """ Network set """
        def __init__(self):
            self.network_set = NetworkSet(self.fusion_client)

        def fusion_api_create_network_set(self, body, api=None, headers=None):
            """
            Creates a Network Set
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Network Set | <body> | <api> | <headers>
            """
            return self.network_set.create(body, api, headers)

        def fusion_api_edit_network_set(self, body=None, uri=None, api=None, headers=None):
            """Updates an Network Set
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Network Set | <body> | <uri> | <api> | <headers>
            """
            return self.network_set.update(body, uri, api, headers)

        def fusion_api_delete_network_set(self, name=None, uri=None, api=None, headers=None):
            """Deletes a Network Set from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Network Set | <name> | <uri> | <api> | <headers>
            """
            return self.network_set.delete(name, uri, api, headers)

        def fusion_api_get_network_set(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Network Sets.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Network Set  | <uri> | <param> | <api> | <headers>
            """
            return self.network_set.get(uri=uri, api=api, headers=headers, param=param)

    class PingKeywords(object):
        """ Ping """
        def __init__(self):
            self.ping = Ping(self.fusion_client)

        def fusion_api_ping(self, body, api=None, headers=None):
            """
            Pings an IP address or host name to determine if the IP address or host name is reachable
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Ping | <body> | <api> | <headers>
            """
            return self.ping.ping(body, api, headers)

    class PowerDeviceKeywords(object):
        """ Power device """
        def __init__(self):
            self.pd = PowerDevice(self.fusion_client)

        def fusion_api_add_power_device(self, body, api=None, headers=None):
            """Adds an Power Delivery Device.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Power Device  | <body> | <api> | <headers>
            """
            return self.pd.create(body=body, api=api, headers=headers)

        def fusion_api_discover_power_device(self, body, api=None, headers=None):
            """Add an HPE iPDU and bring all components under management by discovery of its management module.
            Bring the management module under exclusive management by the appliance, configure any management or
            data collection settings, and create a private set of administrative credentials to enable ongoing
            communication and management of the iPDU. Use "force" to claim the device, even if claimed by another management appliance.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Power Device  | <body> | <api> | <headers>
            """
            return self.pd.create(body=body, api=api, headers=headers, param='/discover')

        def fusion_api_edit_power_device(self, body, uri, api=None, headers=None):
            """Updates a Power Delivery Device.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Power Device  | <body> | <uri> | <api> | <headers>
            """
            return self.pd.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_set_power_device_power_state(self, body, uri, api=None, headers=None):
            """Sets the power state of the specified power delivery device. The device must be an HPE Intelligent Outlet.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Set Power Device Power State | <body> | <uri> | <api> | <headers>
            """
            return self.pd.update(body=body, uri=uri, api=api, headers=headers, param='/powerState')

        def fusion_api_set_power_device_uid_state(self, body, uri, api=None, headers=None):
            """Sets the unit identification (UID) light state of the specified power delivery device.
            The device must be an HPE iPDU component with a locator light (HPE Intelligent Load Segment, AC Module,
            HPE Intelligent Outlet Bar, or HPE Intelligent Outlet).
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Set Power Device UID State | <body> | <uri> | <api> | <headers>
            """
            return self.pd.update(body=body, uri=uri, api=api, headers=headers, param='/uidState')

        def fusion_api_refresh_power_device(self, body, uri, api=None, headers=None):
            """Refreshes a given intelligent power delivery device.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Refresh Power Device | <body> | <uri> | <api> | <headers>
            """
            return self.pd.update(body=body, uri=uri, api=api, headers=headers, param='/refreshState')

        def fusion_api_remove_power_device(self, name=None, uri=None, api=None, headers=None):
            """Removes Power Delivery Devices. If name or uri are not specified, all PDDs are removed.
            [Arguments]
            name: The name of the resource to remove.
            uri: The uri of the resource to remove
            [Example]
            ${resp} = Fusion Api Remove Power Device  | <name> | <uri> | <api> | <headers>
            """
            return self.pd.delete(name=name, uri=uri, api=api, headers=headers)

        def fusion_api_remove_power_device_synchronously(self, uri, api=None, headers=None):
            """Removes the specified Power Delivery Device synchronously.
            [Arguments]
            uri: required : The uri of the resource to remove
            [Example]
            ${resp} = Fusion Api Remove Power Device Synchronously  | <uri> | <api> | <headers>
            """
            return self.pd.delete(uri=uri, api=api, headers=headers, param='/synchronous')

        def fusion_api_get_power_device(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Power Delivery Devices.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Power Device  | <uri> | <param> | <api> | <headers>
            """
            return self.pd.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_power_device_power_state(self, uri=None, api=None, headers=None):
            """Gets the power state (on, off or unknown) of the specified power delivery device that supports power control.
            The device must be an HPE Intelligent Outlet.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            [Example]
            ${resp} = Fusion Api Get Power Device Power State  | <uri> | <api> | <headers>
            """
            return self.pd.get(uri=uri, api=api, headers=headers, param='/powerState')

        def fusion_api_get_power_device_uid_state(self, uri=None, api=None, headers=None):
            """Retrieves the unit identification (UID) state (on, off, unknown) of the specified power outlet or extension bar resource.
            The device must be an HPE iPDU component with a locator light (HPE Intelligent Load Segment, AC Module, HPE Intelligent Outlet Bar,
            or HPE Intelligent Outlet).
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            [Example]
            ${resp} = Fusion Api Get Power Device UID State  | <uri> | <api> | <headers>
            """
            return self.pd.get(uri=uri, api=api, headers=headers, param='/uidState')

    class ProviderKeywords(object):
        """ Provider """
        def __init__(self):
            self.provider = Provider(self.fusion_client)

        def fusion_api_get_provider(self, param='', api=None, headers=None):
            """Gets a default or paginated collection of Providers.
            [Arguments]
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Provider | <param> | <api> | <headers>
            """
            return self.provider.get(api=api, headers=headers, param=param)

    class ProxyServerKeywords(object):
        """ Proxy server """
        def __init__(self):
            self.proxyserver = ProxyServer(self.fusion_client)

        def fusion_api_add_proxy_server(self, body, api=None, headers=None):
            """
            Adds a proxy server to the appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Proxy Server | <body> | <api> | <headers>
            """
            return self.proxyserver.add(body, api, headers)

        def fusion_api_delete_proxy_server(self, api=None, headers=None):
            """
            Adds a proxy server to the appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Proxy Server | <body> | <api> | <headers>
            """
            return self.proxyserver.delete(api, headers)

        def fusion_api_get_proxy_server(self, api=None, headers=None):
            """
            Adds a proxy server to the appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Proxy Server | <body> | <api> | <headers>
            """
            return self.proxyserver.get(api, headers)

    class RackKeywords(object):
        """ Rack """
        def __init__(self):
            self.rack = Rack(self.fusion_client)

        def fusion_api_add_rack(self, body, api=None, headers=None):
            """Adds an Rack.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Rack | <body> | <api> | <headers>
            """
            return self.rack.create(body, api, headers)

        def fusion_api_edit_rack(self, body, uri, api=None, headers=None):
            """Updates a Rack.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Rack | <body> | <uri> | <api> | <headers>
            """
            return self.rack.update(body, uri, api, headers)

        def fusion_api_remove_rack(self, name=None, uri=None, api=None, headers=None):
            """Removes a Rack. If name or uri are not specified, all Racks are removed.
            [Arguments]
            name: The name of the resource to remove.
            uri: The uri of the resource to remove
            [Example]
            ${resp} = Fusion Api Remove Rack | <name> | <uri> | <api> | <headers>
            """
            return self.rack.delete(name, uri, api, headers)

        def fusion_api_get_rack(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Racks.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Rack | <uri> | <param> | <api> | <headers>
            """
            return self.rack.get(uri=uri, api=api, headers=headers, param=param)

    class RemoteSyslogKeywords(object):
        """ Remote syslog """
        def __init__(self):
            self.remote_syslog = RemoteSyslog(self.fusion_client)

        def fusion_api_configure_remote_syslog(self, body, api=None, headers=None):
            """Creates remote syslog.  API documentation was incomplete when this was created!
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Configure Remote Syslog  | <body> | <api> | <headers>
            """
            return self.remote_syslog.create(body, api, headers)

        def fusion_api_update_remote_syslog_configuration(self, body, api=None, headers=None, param=None):
            """This handles update for remote syslog configuration. Configures the devices managed by OneView.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Remote Syslog Configuration | <body> | <api> | <headers> | <uri>
            """
            return self.remote_syslog.update(body, api, headers, param)

        def fusion_api_delete_remote_syslog(self, logId, param='', api=None, headers=None):
            """Deletes remote syslog. - API documentation was incomplete when this was created!
            [Arguments]
            logId: REQUIRED The logId to delete
            param: Optional parameter ?force=True
            [Example]
            ${resp} = Fusion Api Delete Remote Syslog  | <logId> | <param> | <api> | <headers>
            """
            return self.remote_syslog.delete(logId, param, api, headers)

        def fusion_api_get_remote_syslog_configuration(self, api=None, headers=None, param=None):
            """Gets current remote syslog configuration.
            [Example]
            ${resp} = Fusion Api Get Remote Syslog Configuration  | <api> | <headers> | <uri>
            """
            return self.remote_syslog.get(api=api, headers=headers, param=param)

    class ReportKeywords(object):
        """ Reports """
        def __init__(self):
            self.report = Report(self.fusion_client)

    class RestoreKeywords(object):
        """ Restore """
        def __init__(self):
            self.restore = Restore(self.fusion_client)

        def fusion_api_restore_backup(self, body, api=None, headers=None):
            """Starts a restore operation with the specified backup file.
               The backup must be uploaded to the appliance prior to running this command.
               Only one restore can run at a time.
            [Arguments]
            body: Request body for the uploaded backup to be restore
            [Example]
            ${resp} = Fusion Api Restore Backup | <body> | <api> | <headers> |
            """
            return self.restore.start(body=body, api=api, headers=headers)

        def fusion_api_get_restore_status(self, param='', uri=None, api=None, headers=None):
            """
            Gets the status of a restore operation in progress.
            [Arguments]
                uri: the uri of the resource to retrieve.
                param: ID of the Backup URI
            [Example]
                ${resp} = Fusion Api Get Restore Status | <param> | <api> | <headers>
            """
            return self.restore.get(uri=uri, api=api, headers=headers, param=param)

    class RolesKeywords(object):
        """ Roles """
        def __init__(self):
            self.roles = Roles(self.fusion_client)

        def fusion_api_get_roles(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Roles.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Roles | <param> | <api> | <headers>
            """
            return self.roles.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_add_role_to_group(self, body, api=None, headers=None):
            """Adds (POST) a role to a group.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Role To Group | <body> | <api> | <headers>
            """
            return self.roles.add_role_to_group(body, api=api, headers=headers)

        def fusion_api_del_role_from_group(self, domain=None, group=None, api=None, headers=None):
            """Removes (DELETE) a role from a login domain.
            [Arguments]
            domain:  Login Domain name
            group:   Group to remove
            [Example]
            ${resp} = Fusion Api Del Role From Group | <domain> <group> | <api> | <headers>
            """
            return self.roles.del_role_from_group(domain, group, api=api, headers=headers)

    class SasInterconnectTypesKeywords(object):
        """ SAS IC Types """
        def __init__(self):
            self.sasictypes = SasInterconnectTypes(self.fusion_client)

        def fusion_api_get_sas_interconnect_types(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAS Interconnect Types.
            [Arguments]
            uri: The uri of the resource to retrieve. If none, then all resources are returned.
            param: query parameters
            [Example]
            ${resp} = |Fusion Api Get SAS Interconnect Types | <uri> | <param> | <api> | <headers>
            """
            return self.sasictypes.get(uri=uri, api=api, headers=headers, param=param)

    class SasInterconnectsKeywords(object):
        """ SAS IC """
        def __init__(self):
            self.sasics = SasInterconnects(self.fusion_client)

        def fusion_api_get_sas_interconnects(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAS Interconnects
            [Arguments]
            uri: The uri of the resource to retrieve. If none, then all resources are returned.
            param: query parameters
            [Example]
            ${resp} = |Fusion Api Get SAS Interconnects | <uri> | <param> | <api> | <headers>
            """
            return self.sasics.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_patch_sas_interconnect(self, body=None, uri=None, api=None, headers=None):
            """Updates a SAS Interccnnect network using the PATCH http verb.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = |Fusion Api Patch SAS Interconnect | <body> | <uri> | <api> | <headers>
            """
            return self.sasics.patch(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_sas_interconnect(self, name=None, uri=None, api=None, headers=None):
            """Deletes a SAS Interconnect from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = | Fusion Api Delete SAS Interconnect | <name> | <uri> | <api> | <headers>
            """
            return self.sasics.delete(name=name, uri=uri, api=api, headers=headers)

        def fusion_api_refresh_sas_interconnect(self, body=None, uri=None, param='', api=None, headers=None):
            """Refreshes a SAS Interconnect using the PATCH http verb.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            param: query parameters
            [Example]
            ${resp} = |Fusion Api Patch SAS Interconnect | <body> | <uri> | <param> | <api> | <headers>
            """
            param = "/refreshState%s" % param
            return self.sasics.patch(body=body, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_put_sas_interconnects(self, body=None, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAS Interconnects
            [Arguments]
            uri: The uri of the resource to retrieve. If none, then all resources are returned.
            param: query parameters
            [Example]
            ${resp} = |Fusion Api Get SAS Interconnects | <uri> | <param> | <api> | <headers>
            """
            return self.sasics.put(body=body, uri=uri, param=param, api=api, headers=headers)

    class SasLogicalInterconnectGroupKeywords(object):
        """ SAS LIG """
        def __init__(self):
            self.saslig = SasLogicalInterconnectGroup(self.fusion_client)

        def fusion_api_create_sas_lig(self, body, api=None, headers=None):
            """
            Creates an LIG
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = | Fusion Api Create SAS Lig | <body> | <api> | <headers>
            """
            return self.saslig.create(body, api, headers)

        def fusion_api_edit_sas_lig(self, body, uri, api=None, headers=None):
            """Updates an LIG
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = | Fusion Api Edit SAS Lig | <body> | <uri> | <api> | <headers>
            """
            return self.saslig.update(body, uri, api, headers)

        def fusion_api_create_sas_lig_payload(self, body, api=None):
            """ Creates a completed SAS LIG request body
            [Arguments]
             body: a dictionary object containing all the request body elements (see example)
            [Example]
            ${body} = | Fusion Api Create SAS Lig Payload | <body> | <uri> | <api> | <headers>
            ${resp} = | Fusion Api Create Lig | ${body}

            body = {'name': 'SLIG1',
                    'state': 'Active'
                    'type': 'sas-logical-interconnect-group',
                    'enclosureType': 'SY12000',
                    'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex':, 1, 'bay': 1, 'type': 'HP Synthesis 12Gb SAS Storage Switch'},
                                                {'enclosure': 1, 'enclosureIndex':, 1, 'bay': 2, 'type': 'HP Synthesis 12Gb SAS Storage Switch'},
                                               ],
                    }
            """
            return self.saslig.make_body(body=body, api=api)

        def fusion_api_delete_sas_lig(self, name=None, uri=None, api=None, headers=None):
            """Deletes a SAS LIG from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = | Fusion Api Delete SAS Lig | <name> | <uri> | <api> | <headers>
            """
            return self.saslig.delete(name=name, uri=uri, api=api, headers=headers)

        def fusion_api_get_sas_lig(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAS LIGs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get SAS Lig | <uri> | <param> | <api> | <headers>
            """
            return self.saslig.get(uri=uri, param=param, api=api, headers=headers)

    class SasLogicalInterconnectKeywords(object):
        """ SAS LI """
        def __init__(self):
            self.sasli = SasLogicalInterconnect(self.fusion_client)

        def fusion_api_delete_sas_li(self, name=None, uri=None, api=None, headers=None):
            """Deletes a SAS LI
            [Arguments]
            uri: a filter string specifying the interconnect to remove (Ex. ?location=Enclosure:/rest/enclosures/09XXX,Bay:1 )
            name: the name of the SAS LI to remove
            [Example]
            ${resp} = | Fusion Api Delete SAS LI | <name> | <uri> | <api> | <headers>
            """
            return self.sasli.delete(name=name, uri=uri, api=api, headers=headers)

        def fusion_api_get_sas_li(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAS LIs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = | Fusion Api Get SAS LI | <uri> | <param> | <api> | <headers>
            """
            return self.sasli.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_sas_li_firmware(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAS LI firmware.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = | Fusion Api Get SAS LI Firmware | <uri> | <param> | <api> | <headers>
            """
            param = "/firmware%s" % param
            return self.sasli.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_update_sas_li_firmware(self, body=None, uri=None, api=None, headers=None):
            """Updates firmware version at SAS LI level
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resourceto patch.
            [Example]
            ${resp} = Fusion Api Le Firmware Update| <body> | <uri> | <api> | <headers>
            """
            param = "/firmware"    # put method expecting a param
            return self.sasli.put(body=body, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_sas_li_logical_drive_enclosures(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of SAS LI LDEs.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = | Fusion Api Get SAS LI Logical Drive Enclosures | <uri> | <param> | <api> | <headers>
            """
            param = "/logical-drive-enclosures%s" % param
            return self.sasli.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_patch_sas_li(self, body=None, uri=None, api=None, headers=None):
            """Updates an SAS LI using the PATCH http verb.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]

            ${resp} = | Fusion Api Patch SAS LI | <body> | <uri> | <api> | <headers>
            """
            return self.sasli.patch(body, uri, api, headers)

        def fusion_api_update_sas_li_from_group(self, uri=None, api=None, headers=None):
            """Updates the SAS LI to match its SAS LIG
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update SAS LI From Group | <uri> | <param> | <api> | <headers>
            """
            param = '/compliance'
            return self.sasli.put(body=None, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_reapply_sas_li_configuration(self, uri, api=None, headers=None):
            """Asynchronously applies or re-applies the SAS logical interconnect configuration to all managed interconnects.
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Reapply SAS LI Configuration | <uri> | <api> | <headers>
            """
            param = '/configuration'
            return self.sasli.put(body=None, uri=uri, api=api, headers=headers, param=param)

    class ServerHardwareKeywords(object):
        """ Server hardware """
        def __init__(self):
            self.sh = ServerHardware(self.fusion_client)

        def fusion_api_add_server_hardware(self, body, api=None, headers=None, param=''):
            """add a Server Hardware resource.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Server Hardware | <body> | <api> | <headers> | <param>
            """
            return self.sh.post(body, api, headers, param)

        def fusion_api_delete_server_hardware(self, name=None, uri=None, api=None, headers=None):
            """add a Server Hardware resource.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api delete Server Hardware | <name> |<uri> | <api> | <headers>
            """
            return self.sh.delete(name, uri, api, headers)

        def fusion_api_edit_server_hardware(self, body, uri, api=None, headers=None):
            """Updates a Server Hardware resource.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Server Hardware | <body> | <uri> | <api> | <headers>
            """
            return self.sh.update(body, uri, api, headers)

        def fusion_api_edit_server_hardware_environmental_config(self, body, uri, api=None, headers=None):
            """Sets the calibrated max power of an unmanaged or unsupported server hardware resource.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Server Hardware Environmental Config | <body> | <uri> | <api> | <headers>
            """
            return self.sh.update(body, uri, api, headers, param='/environmentalConfiguration')

        def fusion_api_edit_server_hardware_mp_firmware_version(self, body, uri, api=None, headers=None):
            """Sets the mpFirmwareVersion for a server hardware resource.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Server Hardware Mp Firmware Version | <body> | <uri> | <api> | <headers>
            """
            return self.sh.update(body, uri, api, headers, param='/mpFirmwareVersion')

        def fusion_api_edit_server_hardware_power_state(self, body, uri, api=None, headers=None):
            """Requests a power operation to change the power state of the physical server.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Server Hardware Power State | <body> | <uri> | <api> | <headers>
            """
            return self.sh.update(body, uri, api, headers, param='/powerState')

        def fusion_api_get_server_hardware(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Server Hardware.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware | <uri> | <param> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_server_hardware_firmware_compliance(self, body, api=None, headers=None):
            """Gets firmware compliance list of Server Hardware.
            [Arguments]
            body: {"serverUUID":"*","firmwareBaselineId":"*"}
            [Example]
            ${resp} = Fusion Api Get Server Hardware Firmware Compliance| <body> | <api> | <headers>
            """
            return self.sh.post(body=body, param='/firmware-compliance', api=api, headers=headers)

        def fusion_api_get_server_hardware_bios(self, uri, api=None, headers=None):
            """Retrieves the list of BIOS/UEFI settings of the server hardware resource.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Bios | <uri> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param='/bios')

        def fusion_api_get_server_hardware_firmware(self, uri, api=None, headers=None):
            """Retrieves the list of firmware settings of the server hardware resource.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Firmware | <uri> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param='/firmware')

        def fusion_api_get_server_hardware_environmental_config(self, uri, api=None, headers=None):
            """Gets the settings that describe the environmental configuration
            (supported feature set, calibrated minimum & maximum power, location & dimensions, ...) of the server hardware resource.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Environmental Config | <uri> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param='/environmentalConfiguration')

        def fusion_api_get_server_hardware_ilo_sso_url(self, uri, api=None, headers=None):
            """Retrieves the URL to launch a Single Sign-On (SSO) session for the iLO web interface
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Ilo Sso Url | <uri> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param='/iloSsoUrl')

        def fusion_api_get_server_hardware_java_remote_console_url(self, uri, api=None, headers=None):
            """Generates a Single Sign-On (SSO) session for the iLO Java Applet console and returns the URL to launch it.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Java Remote Console Url | <uri> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param='/javaRemoteConsoleUrl')

        def fusion_api_get_server_hardware_remote_console_url(self, uri, api=None, headers=None):
            """Generates a Single Sign-On (SSO) session for the iLO Integrated Remote Console Application (IRC) and returns the URL to launch it.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Remote Console Url | <uri> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param='/remoteConsoleUrl')

        def fusion_api_get_server_hardware_utilization(self, uri, api=None, headers=None):
            """Retrieves historical utilization data for the specified resource, metrics, and time span.
            [Arguments]
            uri: REQUIRED the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Utilization | <uri> | <api> | <headers>
            """
            return self.sh.get(uri=uri, api=api, headers=headers, param='/utilization')

        def fusion_api_patch_server_hardware(self, body, uri, api=None, headers=None):
            """Issues a PATCH request. See REST-API docs for valid request bodies
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} | Fusion Api Patch Server Hardware | <body> | <uri> | <api> | <headers>
            """
            return self.sh.patch(body, uri, api, headers)

        def fusion_api_refresh_server_hardware(self, body={"refreshState": "RefreshPending"}, uri=None, api=None, headers=None):
            """Refreshes a specified Server hardware URI
            [Arguments]
            uri: the uri of the resource to refresh.
            body: Request body to indicate refreshState and other parameters.
            [Example]
            ${resp} = Fusion Api Refresh Server Hardware | <body> | <uri> | <api> | <headers>"""
            return self.sh.update(body, uri=uri, api=api, headers=headers, param='/refreshState')

    class LogicalEnclosureKeywords(object):
        """ LE """
        def __init__(self):
            self.logical_enclosure = LogicalEnclosure(self.fusion_client)

        def fusion_api_create_logical_enclosure_payload(self,
                                                        name,
                                                        api=None,
                                                        enclosureGroupUri=None,
                                                        enclosureUris=[],
                                                        firmwareBaselineUri="",
                                                        forceInstallFirmware=0):
            """Returns request body required to create a Logical Enclosure
            [Arguments]
            name: REQUIRED the name of the Logical Enclosure
            enclosureGroupUri: REQUIRED URI of Enclosure Group to be used.
            enclosureUris : Required An array consisting the URI of the Enclosure to be used.
            [Example]
            ${resp} = Fusion Api Create Logical Enclosure Payload | <name> | <api> | <enclosureGroupUri> | <enclosureUris> | >firmwareBaselineUri> | <forceInstallFirmware>
            """
            return (self.logical_enclosure.make_body(name=name,
                                                     api=api,
                                                     enclosureGroupUri=enclosureGroupUri,
                                                     enclosureUris=enclosureUris,
                                                     firmwareBaselineUri=firmwareBaselineUri,
                                                     forceInstallFirmware=forceInstallFirmware))

        def fusion_api_create_logical_enclosure(self, body, api=None, headers=None):
            """Creates a new Logical Enclosure
            [Arguments]
            body: REQUIRED the request body with Logical Enclosure details.
            [Example]
            ${resp} = Fusion Api Create Logical Enclosure | <body> | <api> | <headers>
            """
            return self.logical_enclosure.create(body=body, api=api, headers=headers)

        def fusion_api_get_logical_enclosure(self, uri=None, api=None, headers=None, param=''):
            """Returns an existing Logical Enclosure
            [Arguments]
            [Example]
            ${resp} = Fusion Api Get Logical Enclosure | <uri> | <api> | <headers> | <param>
            """
            return self.logical_enclosure.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_delete_logical_enclosure(self, name=None, uri=None, param='', api=None, headers=None):
            """Removes an existing Logical Enclosure
            [Arguments]
            [Example]
            ${resp} = Fusion Api Delete Logical Enclosure | <name> | <uri> | <param> | <api> | <headers>
            """
            return self.logical_enclosure.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_logical_enclosure_support_dump(self, body, id=None, api=None, headers=None):  # pylint: disable=W0622
            """Triggers a support dump for an existing Logical Enclosure
            [Arguments]
            body: REQUIRED the request body for Logical Enclosure Support Dump.
            id: REQUIRED Logical Enclosure ID.
            [Example]
            ${resp} = Fusion Api Get Logical Enclosure Support Dump | <body> | <id> | <api> | <headers>
            """
            return self.logical_enclosure.get_support_dump(body=body, le_id=id, api=api, headers=headers)

        def fusion_api_update_logical_enclosure(self, body, uri, param='', api=None, headers=None, etag=None):
            """Update an logical enclosure.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Update Logical Enclosure | <body> | <uri> | <param> | <api> | <headers> | <eTag>
            """
            return self.logical_enclosure.put(body, uri, param, api, headers, etag)

        def fusion_api_update_logical_enclosure_from_group(self, uri=None, api=None, headers=None):
            """Updates the logical enclosure to match its enclosure group
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Update Logical Enclosure from Group| <uri> | param | <api> | <headers>
            """
            param = '/updateFromGroup'
            return self.logical_enclosure.put(body=None, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_reapply_le_configuration(self, uri, api=None, headers=None):
            """Asynchronously appliesor re-applies the logical enclosure configuration to all managed LEs.
            [Arguments]
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Reapply Le Configuration | <uri> | <api> | <headers>
            """
            param = '/configuration'
            return self.logical_enclosure.put(body=None, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_le_firmware_update(self, body=None, uri=None, api=None, headers=None, etag=None):
            """Updates firmware version at LE level
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resourceto patch.
            [Example]
            ${resp} = Fusion Api Le Firmware Update| <body> | <uri> | <api> | <headers>
            """
            return self.logical_enclosure.patch(body, uri, api, headers, etag)

    class IndexResourceKeywords(object):
        """ Index resource """
        def __init__(self):
            self.index_resource = IndexResource(self.fusion_client)

        def fusion_api_index_resource(self, uri=None, api=None, headers=None):
            """The index/resources resource provides APIs for managing index resources, including retrieving,
            creating/updating, and deleting index resources.To make searches faster, the index stores
            an index resource for each resource. Index resources contain normal search parameters such as name,
            category, status, state, description and so on. They also contain attributes, with searchable
            data from the resource.
            [Arguments]
            uri: REQUIRED string containing the required resource URI to Query
            [Example]
            https://{appl}/rest/index/resources?userQuery="Running"          //Case Insensitive
            Usage:
            ${resp} = fusion_api_index_resource | <uri> | <api> | <headers>
            """
            return self.index_resource.get(uri, api, headers)

    class IndexAssociationKeywords(object):
        """ Index Associations """
        def __init__(self):
            self.index_association = IndexAssociation(self.fusion_client)

        def fusion_api_get_index_association(self, uri=None, api=None, headers=None):
            """The index/association/resources resource provides APIs for managing index association resources, including retrieving,
            creating/updating, and deleting index association resources.To make searches faster, the index stores
            an index resource for each resource. Index resources contain normal search parameters such as name,
            category, status, state, description and so on. They also contain attributes, with searchable
            data from the resource.
            [Arguments]
            uri: REQUIRED string containing the required resource URI to Query
            [Example]
            https://{appl}/rest/index/association/resources?userQuery="Running"          //Case Insensitive
            Usage:
            ${resp} = fusion_api_index_association_resource | <uri> | <api> | <headers>
            """
            return self.index_association.get(uri, api, headers)

    class ServerHardwareTypesKeywords(object):
        """ SHT """
        def __init__(self):
            self.types = ServerHardwareTypes(self.fusion_client)

        def fusion_api_edit_server_hardware_types(self, body, uri, api=None, headers=None):
            """Updates a Server Hardware Type.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Server Hardware Type | <body> | <uri> | <api> | <headers>
            """
            return self.types.update(body, uri, api, headers)

        def fusion_api_get_server_hardware_types(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Server Hardware Types.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Hardware Types | <uri> | <param> | <api> | <headers>
            """
            return self.types.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_delete_server_hardware_types(self, name=None, uri=None, api=None, headers=None):
            """Deletes server hardware types in bulk based on name OR uri. If name AND uri are omitted, ALL shts are deleted.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            param: you can use param=?force="true" to force remove an enclosure
            [Example]
            ${resp} = Fusion Api Delete Server Hardware Types | <name> | <uri> | <param> | <api> | <headers>
            """
            return self.types.delete(name=name, uri=uri, api=api, headers=headers)

    class ServerProfileKeywords(object):
        """ Server profile """
        def __init__(self):
            self.profile = ServerProfile(self.fusion_client)

        def fusion_api_create_server_profile(self, body, api=None, headers=None, param=''):
            """Creates a Server Profile.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            param: ?force=<comma-separated list of flags for ignoring specific warnings>
                   Calls may use "all" (or "true") to pass all ignore flags, or "none" (or "false") to pass none of them.
                   The supported comman-separated list of flags are:
                   ignoreSANWarnings: When provided, the operation will ignore warnings for non-critical issues detected in the SAN storage configuration.
                   ignoreServerHealth: When provided, the operation will ignore the check to verify that the selected server's health is OK.
                   Default is none
            [Example]
            ${resp} = Fusion Api Create Server Profile | <body> | <api> | <headers>
            """
            return self.profile.create(body, api, headers, param=param)

        def fusion_api_edit_server_profile(self, body, uri, api=None, headers=None, param=''):
            """Updates a Server Profile.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            param: ?force=<comma-separated list of flags for ignoring specific warnings>
                   Calls may use "all" (or "true") to pass all ignore flags, or "none" (or "false") to pass none of them.
                   The supported comman-separated list of flags are:
                   ignoreSANWarnings: When provided, the operation will ignore warnings for non-critical issues detected in the SAN storage configuration.
                   ignoreServerHealth: When provided, the operation will ignore the check to verify that the selected server's health is OK.
                   Default is none
            [Example]
            ${resp} = Fusion Api Edit Server Profile | <body> | <uri> | <api> | <headers> | <param>
            """
            return self.profile.update(body, uri, api, headers, param=param)

        def fusion_api_delete_server_profile(self, name=None, uri=None, param='', api=None, headers=None):
            """Deletes server profiles in bulk based on name OR uri. If name AND uri are omitted, ALL profiles are deleted.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            param: ?force=<comma-separated list of flags for ignoring specific warnings>
                   Calls may use "all" (or "true") to pass all ignore flags, or "none" (or "false") to pass none of them.
                   The supported comman-separated list of flags are:
                   ignoreSANWarnings: When provided, the operation will ignore warnings for non-critical issues detected in the SAN storage configuration.
                   ignoreServerHealth: When provided, the operation will ignore the check to verify that the selected server's health is OK.
                   Default is none
            [Example]
            ${resp} = Fusion Api Delete Server Profile | <name> | <uri> | <param> | <api> | <headers>
            """
            return self.profile.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_server_profiles(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Server Profiles.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Profiles  | <uri> | <param> | <api> | <headers>
            """
            return self.profile.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_patch_server_profile(self, body, uri, api=None, headers=None):
            """Patches a Server Profile.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Patch Server Profile | <body> | <uri> | <api> | <headers>
            """
            return self.profile.patch(body, uri, api, headers)

        def fusion_api_get_server_profiles_available_networks(self, uri=None, param='', api=None, headers=None):
            """Retrieves the list of Ethernet networks, Fibre Channel networks and network sets that are available to a server profile along with their respective ports.
            [Arguments]
            param: optional parameters
                    enclosureGroupUri: The URI of the enclosure group associated with the resource
                    functionType: The FunctionType (Ethernet or FibreChannel) to filter the list of networks returned
                    FunctionType:
                        Values:
                            Ethernet Specifies that the connection is to an Ethernet network or a network set.
                            FibreChannel Specifies that the connection is to a Fibre Channel network.
                    serverHardwareTypeUri: The URI of the server hardware type associated with the resource
                    serverHardwareUri
            [Example]
            ${resp} = Fusion Api Get Server Profiles Available Networks | <uri> | <param> | <api> | <headers>
            """
            param = '/available-networks%s' % param
            return self.profile.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_server_profiles_available_storage_system(self, uri=None, param='', api=None, headers=None):
            """Retrieve a specific storage system and its associated volumes that are available to the server profile based on the given server hardware type and enclosure group.
            [Arguments]
            param: REQUIRED parameters
                    enclosureGroupUri: The URI of the enclosure group associated with the resource
                    serverHardwareTypeUri: The URI of the server hardware type associated with the resource
                    storageSystemId: The storage system ID associated with the resource
            [Example]
            ${resp} = Fusion Api Get Server Profiles Available Storage System | <uri> | <param> | <api> | <headers>
            """
            param = '/available-storage-system%s' % param
            return self.profile.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_server_profiles_available_storage_systems(self, uri=None, param='', api=None, headers=None):
            """Retrieves the list of the storage systems and their associated volumes that are available to the server profile based on the given server hardware type and enclosure group.
            [Arguments]
            param: REQUIRED parameters
                    enclosureGroupUri: The URI of the enclosure group associated with the resource
                    serverHardwareTypeUri: The URI of the server hardware type associated with the resource
            [Example]
            ${resp} = Fusion Api Get Server Profiles Available Storage Systems | <uri> | <param> | <api> | <headers>
            """
            param = '/available-storage-systems%s' % param
            return self.profile.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_server_profiles_available_targets(self, uri=None, param='', api=None, headers=None):
            """Retrieves a list of the target servers and empty device bays that are available for assignment to the server profile. This replaces the /rest/server-profiles/available-servers API.
            [Arguments]
            param: optional parameters
                    enclosureGroupUri: The URI of the enclosure group associated with the resource
                    profileUri: The URI of the server profile associated with the resource
                    serverHardwareTypeUri: The URI of the server hardware type associated with the resource

            [Example]
            ${resp} = Fusion Api Get Server Profiles Available Targets | <uri> | <param> | <api> | <headers>
            """
            param = '/available-targets%s' % param
            return self.profile.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_server_profiles_profile_ports(self, uri=None, param='', api=None, headers=None):
            """Retrieves the port model associated with a server or server hardware type and enclosure group.
            [Arguments]
            param: optional parameters
                    enclosureGroupUri: The URI of the enclosure group associated with the resource
                    serverHardwareTypeUri: The URI of the server hardware type associated with the resource
                    serverHardwareUri:
            [Example]
            ${resp} = Fusion Api Get Server Profiles Profile Ports | <uri> | <param> | <api> | <headers>
            """
            param = '/profile-ports%s' % param
            return self.profile.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_server_profile_new_template(self, uri, api=None, headers=None):
            """A server profile template object will be returned with the configuration based on this profile.
            [Arguments]
            uri: REQUIRED  the uri of the profile

            [Example]
            ${resp} = Fusion Api Get Server Profile New Template  | <uri> | <api> | <headers>
            """
            return self.profile.get(uri=uri, api=api, headers=headers, param="/new-profile-template")

    class ServerProfileTemplateKeywords(object):
        """ SPT """
        def __init__(self):
            self.profile_template = ServerProfileTemplate(self.fusion_client)

        def fusion_api_create_server_profile_template(self, body, api=None, headers=None):
            """Creates a Server Profile Template.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Server Profile Template | <body> | <api> | <headers>
            """
            return self.profile_template.create(body, api, headers)

        def fusion_api_edit_server_profile_template(self, body, uri, api=None, headers=None):
            """Updates a Server Profile Template.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Server Profile Template | <body> | <uri> | <api> | <headers>
            """
            return self.profile_template.update(body, uri, api, headers)

        def fusion_api_delete_server_profile_template(self, name=None, uri=None, api=None, headers=None):
            """Deletes server profile templates bulk based on name OR uri. If name AND uri are omitted, ALL templates are deleted.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Server Profile Template| <name> | <uri> | <api> | <headers>
            """
            return self.profile_template.delete(name, uri, api, headers)

        def fusion_api_get_server_profile_templates(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Server Profile Templates.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Server Profile Templates  | <uri> | <param> | <api> | <headers>
            """
            return self.profile_template.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_server_profile_template_new_profile(self, uri, api=None, headers=None):
            """A profile object will be returned with the configuration based on this template.
            [Arguments]
            uri: REQUIRED  the uri of the profile template

            [Example]
            ${resp} = Fusion Api Get Server Profile Template New Profile  | <uri> | <api> | <headers>
            """
            return self.profile_template.get(uri=uri, api=api, headers=headers, param="/new-profile")

    class ServiceAccessKeywords(object):
        """ Service access """
        def __init__(self):
            self.service_access = ServiceAccess(self.fusion_client)

        def fusion_api_set_service_access(self, host, status='enabled', api=None, headers=None):
            """Enables\disables service access on the appliance
            [Arguments]
            host: REQUIRED the IP or hostname of the appliance
            status: Enabled\Disabled.  defaults to Enabled
            [Example]
            ${resp} = Fusion Api Set Service Access | <host> | <status> | <api> | <headers>
            """
            return self.service_access.save(host, status, api, headers)

        def fusion_api_get_service_access(self, host=None, api=None, headers=None):
            """Retrieves the current service access setting from the appliance
            [Arguments]
            host: Is optional and only to be used in the case of not having logged in
            [Example]
            ${resp} = Fusion Api Get Service Access | <host> | <api> | <headers>
            """
            return self.service_access.get(host, api, headers)

    class SessionsKeywords(object):
        """ Sessions """
        def __init__(self):
            self.sessions = Sessions(self.fusion_client)

        def fusion_api_get_session_info(self, api=None, headers=None, param='', sessionID=None):
            """Retrieves the user session.
            [Arguments]
            host: REQUIRED the IP or hostname of the appliance
            [Example]
            ${resp} = Fusion Api Get Session Info | <host> | <api> | <headers> | <param> | <sessionID> |
            """
            return self.sessions.get(api, headers, param, sessionID)

    class StartupProgressKeywords(object):
        """ Startup progress """
        def __init__(self):
            self.progress = StartupProgress(self.fusion_client)

        def fusion_api_get_startup_progress(self, host, api=None, headers=None):
            """Gets the status of the appliance startup. This API does not require authorization.
            [Arguments]
            host: REQUIRED the IP or hostname of the appliance
            [Example]
            ${resp} = Fusion Api Get Startup Progress Access | <host> | <api> | <headers>
            """
            return self.progress.get(host, api, headers)

    class StoragePoolKeywords(object):
        """ Storage pool """
        def __init__(self):
            self.pool = StoragePool(self.fusion_client)

        def fusion_api_get_storage_pools(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of storage Pools.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Storage Pools  | <uri> | <param> | <api> | <headers>
            """
            return self.pool.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_edit_storage_pool(self, body, uri, api=None, headers=None):
            """
            Creates a storage pool
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Edit Storage Pool | <body> | uri | <api> | <headers>
            """
            return self.pool.update(body, uri, api=api, headers=headers)

        def fusion_api_delete_storage_pool(self, uri=None, api=None, headers=None):
            """Deletes storage pool based on name OR uri.
            [Arguments]
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Storage Pool | <uri> | <api> | <headers>
            """
            return self.pool.delete(uri=uri, api=api, headers=headers)

    class StorageSystemKeywords(object):
        """ Storage system """
        def __init__(self):
            self.system = StorageSystem(self.fusion_client)

        def fusion_api_get_storage_system(self, uri=None, param='', api=None, headers=None):
            """Gets a collection of Storage systems.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Storage System  | <uri> | <param> | <api> | <headers>
            """
            return self.system.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_storage_system(self, body, api=None, headers=None):
            """
            Creates a storage system
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Storage System | <body> | <api> | <headers>
            """
            return self.system.create(body=body, api=api, headers=headers)

        def fusion_api_update_storage_system(self, body, uri, api=None, headers=None):
            """
            Updates a storage system
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Storage System | <body> | <uri> | <api> | <headers>
            """
            return self.system.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_storage_system(self, uri=None, api=None, headers=None):
            """Deletes storage systems based on name OR uri.
            [Arguments]
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Storage System | <uri> | <api> | <headers>
            """
            return self.system.delete(uri=uri, api=api, headers=headers)

        def fusion_api_storage_system_get_reachable_ports(self, uri=None, param='', api=None, headers=None):
            """
            Returns Reachable Ports of Specified Storage System
            [Arguments]
            uri: The uri of the Storage System
            param: query parameters
            [Example]
            ${resp} = Fusion Api Storage System Get Reachable Ports  | <uri> | <param> | <api> | <headers>
            """
            return self.system.get_reachable_ports(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_storage_system_get_templates(self, uri=None, param='', api=None, headers=None):
            """
            Returns Templates of Specified Storage System
            [Arguments]
            uri: The uri of the Storage System
            param: query parameters
            [Example]
            ${resp} = Fusion Api Storage System Get Templates  | <uri> | <param> | <api> | <headers>
            """
            return self.system.get_templates(uri=uri, api=api, headers=headers, param=param)

    class StorageVolumeTemplateKeywords(object):
        """ Storage volume template """
        def __init__(self):
            self.template = StorageVolumeTemplate(self.fusion_client)

        def fusion_api_create_storage_volume_template(self, body, api=None, headers=None):
            """
            Createsa storage volume template
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Storage Volume template | <body> | <api> | <headers>
            """
            return self.template.create(body=body, api=api, headers=headers)

        def fusion_api_edit_storage_volume_template(self, body, uri, api=None, headers=None):
            """
            Edits a storage volume template
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Edit Storage Volume Template | <body> | <uri> | <api> | <headers>
            """
            return self.template.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_get_storage_volumes_template(self, uri=None, param='', api=None, headers=None):
            """Gets a collection of Storage Volumes template.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Storage Volumes template  | <uri> | <param> | <api> | <headers>
            """
            return self.template.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_delete_storage_volume_template(self, name=None, uri=None, api=None, headers=None):
            """Deletes storage volumes template based on name OR uri.
            [Arguments]
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete Storage Volume template | <uri> | <api> | <headers>
            """
            return self.template.delete(name=name, uri=uri, api=api, headers=headers)

    class StorageVolumeKeywords(object):
        """ Storage volume """
        def __init__(self):
            self.volume = StorageVolume(self.fusion_client)

        def fusion_api_create_storage_volume(self, body, api=None, headers=None):
            """
            Createsa storage volume
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Storage Volume | <body> | <api> | <headers>
            """
            return self.volume.create(body=body, api=api, headers=headers)

        def fusion_api_update_storage_volume(self, body, uri, api=None, headers=None):
            """
            update storage volume
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Storage Volume | <body> | <uri> | <api> | <headers>
            """
            return self.volume.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_get_storage_volumes(self, uri=None, param='', api=None, headers=None):
            """Gets a collection of Storage Volumes.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Storage Volumes  | <uri> | <param> | <api> | <headers>
            """
            return self.volume.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_delete_storage_volume(self, name=None, uri=None, param='', api=None, headers=None):
            """Deletes storage volumes based on name OR uri.
            [Arguments]
            uri: The uri of the resource to delete
            param: ?suppressDeviceUpdates=true only remove the volume from Oneview only.
                   ?suppressDeviceUpdates=false remove the volume from Oneview and StorageSystem.
            [Example]
            ${resp} = Fusion Api Delete Storage Volume | <uri> | <param> | <api> | <headers>
            """
            return self.volume.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_add_existing_storage_volume(self, body, api=None, headers=None):
            """
            Add existing storage volume on the storage system into Oneview
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Existing Storage Volume | <body> | <api> | <headers>
            """
            return self.volume.add_existing(body=body, api=api, headers=headers)

    class StorageVolumeAttachmentKeywords(object):
        """ Storage volume attachment """
        def __init__(self):
            self.volume_attachment = StorageVolumeAttachment(self.fusion_client)

        def fusion_api_get_storage_volume_attachments(self, uri=None, param='', api=None, headers=None):
            """ Get storage volume attachments.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Storage Volume Attachments  | <uri> | <param> | <api> | <headers>
            """
            return self.volume_attachment.get(uri=uri, param=param, api=api, headers=headers)

        def fusion_api_patch_storage_volume_attachments(self, body, param='', api=None, headers=None):
            """ Create, update, and delete volume attachments via patch
            [Arguments]
            body: payload
            param: ex. ?dryrun=true
            [Example]
            ${resp} = Fusion Api Patch Storage Volume Attachments  | <body> | <param> | <api> | <headers>
            """
            return self.volume_attachment.patch(body=body, param=param, api=api, headers=headers)

    class SwitchKeywords(object):
        """ Switch """
        def __init__(self):
            self.switch = Switch(self.fusion_client)

        def fusion_api_add_switch(self, body, api=None, headers=None):
            """Adds a Switch.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Switch | <body> | <api> | <headers>
            """
            return self.switch.create(body, api, headers)

        def fusion_api_edit_switch(self, body, uri, api=None, headers=None):
            """Updates a Switch.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Switch | <body> | <uri> | <api> | <headers>
            """
            return self.switch.update(body, uri, api, headers)

        def fusion_api_refresh_switch(self, uri, api=None, headers=None):
            """Refreshes a Switch based on uri provided
            [Arguments]
            uri: REQUIRED The uri of the resource to refresh
            [Example]
            ${resp} = Fusion Api Refresh Switch | <uri> | <api> | <headers>
            """
            return self.switch.refresh(uri, api, headers)

        def fusion_api_remove_switch(self, name=None, uri=None, api=None, headers=None):
            """Removes a Switch based on name OR uri provided
            [Arguments]
            name: The name of the resource to remove.
            uri: The uri of the resource to remove
            [Example]
            ${resp} = Fusion Api Remove Switch | <name> | <uri> | <api> | <headers>
            """
            return self.switch.delete(name, uri, api, headers)

        def fusion_api_get_switch(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Switches.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Switch | <uri> | <param> | <api> | <headers>
            """
            return self.switch.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_switches_without_ports(self, uri=None, api=None, headers=None):
            """ Gets a default or paginated collection of Switches without ports info
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all switches are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Switches Without Ports| <uri> | <api> | <headers>
            """
            return self.switch.get(uri=uri, api=api, headers=headers, param='/withoutPorts')

    class SwitchTypesKeywords(object):
        """ Switch types """
        def __init__(self):
            self.swtypes = SwitchTypes(self.fusion_client)

        def fusion_api_get_switch_types(self, param='', api=None, headers=None):
            """Gets a default or paginated collection of Switch Types.
            [Arguments]
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Switch Types | <param> | <api> | <headers>
            """
            return self.swtypes.get(api=api, headers=headers, param=param)

    class TaskKeywords(object):
        """ Tasks """
        def __init__(self):
            self.task = Task(self.fusion_client)

        def fusion_api_create_task(self, body, api=None, headers=None):
            """
            Creates a Task
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Task | <body> | <api> | <headers>
            """
            return self.task.create(body, api, headers)

        def fusion_api_update_task(self, body, uri, api=None, headers=None):
            """Updates an Task
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Update Task | <body> | <uri> | <api> | <headers>
            """
            return self.task.update(body, uri, api, headers)

        def fusion_api_get_task(self, param='', uri=None, api=None, headers=None):
            """Gets a default or paginated collection of Tasks.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Task  | <uri> | <param> | <api> | <headers>
            """
            if uri is not None:
                # update fully qualified URL to relative URI
                uri = re.sub('^https://\d*.\d*.\d*.\d*', '', uri)
            return self.task.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_wait_for_task_to_complete(self, uri=None, api=None, headers=None, retries=5, sleep_time=5, param=''):
            """ Wait for a task to complete """
            task_attempts = 0
            for _ in range(0, retries):
                time.sleep(sleep_time)
                task_attempts += 1
                response = self.task.get(uri=uri, api=api, headers=headers, param=param)
                if response["percentComplete"] == 100:
                    break
                if task_attempts == retries:
                    raise Exception(
                        "Task did not complete after %d tries." % retries)
            return response

    class UplinkSetKeywords(object):
        """ Uplink sets """
        def __init__(self):
            self.uplink_set = UplinkSet(self.fusion_client)

        def fusion_api_create_uplink_set(self, body, param='', api=None, headers=None):
            """
            Creates a Uplink Set
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Uplink Set | <body> | <api> | <headers>
            """
            return self.uplink_set.create(body, param, api, headers)

        def fusion_api_create_uplink_set_payload(self, us, api=None):
            """

            :param us:  A dictionary containing the seed request body parameters
            necessary to create an uplink set, but can contain ANY data you want to send.
            NOTE: these two keys require a shorthand format in order to be translated for you:

            'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': 'Q1', 'desiredSpeed': 'Auto'},
                                {'enclosure': ENC1, 'bay': '3', 'port': 'Q2', 'desiredSpeed': 'Auto'}]
            'primaryPortLocation' : {'enclosure': ENC1, 'bay': '3', 'port': 'Q1'}

            :return:  an updated uplink-set request body ready to POST
            """
            return self.uplink_set.make_body(api=api, us=us)

        def fusion_api_edit_uplink_set(self, body, uri, api=None, headers=None):
            """Updates an Uplink Set
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit Uplink Set | <body> | <uri> | <api> | <headers>
            """
            return self.uplink_set.update(body, uri, api, headers)

        def fusion_api_delete_uplink_set(self, name=None, uri=None, api=None, headers=None):
            """Deletes an Uplink Set from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Delete Uplink Set | <name> | <uri> | <api> | <headers>
            """
            return self.uplink_set.delete(name, uri, api, headers)

        def fusion_api_get_uplink_set(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Uplink Sets.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Uplink Set  | <uri> | <param> | <api> | <headers>
            """
            return self.uplink_set.get(uri=uri, api=api, headers=headers, param=param)

    class UserKeywords(object):
        """ Users """
        def __init__(self):
            self.user = User(self.fusion_client)

        def fusion_api_add_user(self, body, api=None, headers=None):
            """
            Adds a User
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add User | <body> | <api> | <headers>
            """
            return self.user.create(body, api, headers)

        def fusion_api_edit_user(self, body, uri, api=None, headers=None):
            """Updates an User
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} = Fusion Api Edit User | <body> | <uri> | <api> | <headers>
            """
            return self.user.update(body, uri, api, headers)

        def fusion_api_change_administrator_password(self, host, body, api=None, headers=None):
            """Changes the initial Administrator password
            [Arguments]
            host: REQUIRED the IP or hostname of the appliance
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Change Administrator Password | <host> | <body> | <api> | <headers>
            """
            return self.user.change_administrator_password(host, body, api, headers)

        def fusion_api_remove_user(self, name=None, uri=None, api=None, headers=None):
            """Removes a User from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            [Example]
            ${resp} = Fusion Api Remove User | <name> | <uri> | <api> | <headers>
            """
            return self.user.delete(name, uri, api, headers)

        def fusion_api_get_user(self, uri=None, param='', api=None, headers=None):
            """Gets a default or paginated collection of Users.
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get User | <uri> | <param> | <api> | <headers>
            """
            return self.user.get(uri=uri, api=api, headers=headers, param=param)

    class VersionKeywords(object):
        """ Version """
        def __init__(self):
            self.version = Version(self.fusion_client)

        def fusion_api_get_appliance_api_versions(self, api=None, headers=None):
            """Gets the appliance's supported API versions
            [Example]
            ${resp} = Fusion Api Get Appliance Api Versions | <api> | <headers>
            """
            return self.version.get(api=api, headers=headers)

        def fusion_api_set_default_api_version(self, api=None):
            """Sets the X-API-Version header to the specified value for all future requests.
            If no value is supplied, the value of ${X-API-Version} is used
            if it exists else the appliances current version is queried and used
            [Example]
            ${resp} = |Fusion Api Set Default Api Version | <api> |
            """
            return self.version.set(api=api)

    class HalAPIKeywords(object):
        """ HAL API """
        def hal_api_perform_discover(self, fusion_ip, retries=5):
            """ Send a Discover rest call to the HAL Test Webapp on Fusion

            Example:
            | HAL API Perform Discover | ${FUSION_IP} |
            | HAL API Perform Discover | ${FUSION_IP} | 2 |
            """
            url = "https://%s/perm/rest/tbird/pemOperation" % fusion_ip

            # Payload
            data = {"PemOperation": "discover",
                    "operationParameters": {},
                    "SN": BuiltIn().get_variable_value("${ENC_SERIAL_NUMBER}")}
            # These parameters are suggested but do not seem required.
            # data["username"] = "admin"
            # data["password"] = "mypassword"
            # data["force"] = "false"

            # return self.fusion_client.post(url, data, header)
            # Retry in case rest call fails the first time.
            # Currently calls to the webapp fail intermittently when using a
            # DCS enclosure.
            discovery_attempts = 0
            for _ in range(0, retries):
                discovery_attempts += 1
                response = self.fusion_client.post(url, body=json.dumps(data))
                if response['status_code'] == 200:
                    break
                if discovery_attempts == retries:
                    raise Exception(
                        "Failed to properly discover the enclosure after %d tries." % retries)
                time.sleep(5)
            if discovery_attempts > 1:
                logger._warn(
                    "%d attempts were needed to properly discover the enclosure; this operation should only take one attempt." % discovery_attempts)
            return response

        def hal_api_perform_post_action(self, fusion_ip, action=None, parameters=None, retries=5):
            """ Send a POST rest call to the HAL Test Webapp on Fusion

            Example:
            | HAL API Perform Post Action | ${FUSION IP} | ChassisUidControl | {"UidState":"on"} | |
            | HAL API Perform Post Action | ${FUSION IP} |  ChassisMidplaneFruAction |  | 10 |
            """
            url = "https://" + fusion_ip + \
                "/perm/rest/tbird/pemOperation"

            # Build Payload and initialize
            data = {"PemOperation": "performAction",
                    "ActionName": "",
                    "ActionParameters": {},
                    "SN": BuiltIn().get_variable_value("${ENC_SERIAL_NUMBER}")}
            if action is not None:
                data["ActionName"] = action
            if parameters is not None:
                data["ActionParameters"] = parameters

            # Retry in case rest call fails.
            # Currently calls to the webapp fail intermittently.
            attempts = 0
            for _ in range(0, retries):
                attempts += 1
                response = self.fusion_client.post(url, body=json.dumps(data))
                if isinstance(response, dict):
                    # Normally, the response is returned in the form of a dict
                    # If the status code is 200, it worked; don't make more attempts
                    if response['status_code'] == 200:
                        break
                else:
                    # In this case, the HAPI received invalid data and chose to return a zero-length response.
                    # This string may contain something like "<Response: [200]>"
                    # but it is probably not incredibly useful to validate.
                    # Return a dict since Robot Framework doesn't deal well with return values that could be either a dict or a string.
                    return {"response_string": response}
            if attempts > 1:
                logger._warn(
                    "%d attempts were made; this operation should only take one attempt." % attempts)
            return response

        def hal_api_get_resource(self, fusion_ip, em_ip, resource, option='', retries=5, header=None):
            """ """
            return self.hal_api_get_em_ris(fusion_ip, em_ip, resource, option, retries, header)

        def hal_api_get_em_ris(self, fusion_ip, em_ip, resource, option='', retries=5, header=None):  # pylint: disable=unused-argument
            """ Send a GET rest call to the EM RIS interface through the Fusion appliance

            Example:

            | HAL API Get Resource | ${FUSION IP} | ${EM_IP} | /rest/v1/BladeFru/1/ | |
            | HAL API Get Resource | ${FUSION IP} | ${EM_IP} | /rest/v1/Chassis/1/  | 10 |
            """
            dcs = BuiltIn().get_variable_value("${DCS}")
            nic = BuiltIn().get_variable_value("${FUSION_NIC}")

            # Assume Auth Token is passed in header
            if not header:
                auth = BuiltIn().get_variable_value("${EMSessionID}", "NotAuthorized")
                header = '-H "X-Auth-Token:%s" ' % auth
            auth = header
            header = '-H "X-Auth-Token:' + auth + '\"'

            ssh = paramiko.client.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            if dcs == 'true':
                command = '/usr/bin/curl -ik ' + header + option + ' https://' + em_ip + resource
            else:
                command = '/usr/bin/curl -ik ' + header + option + ' https://' + em_ip + "%" + nic + resource
            try:
                logger._log('Logging into EM to run curl %s' % command)
                ssh.connect(fusion_ip, username='root', password='hpvse1', timeout=30.0)
                output = ssh.exec_command(command)
            except paramiko.BadHostKeyException:
                logger._warn("Not able to connect because of BadKeyException.  Need to clean up .ssh directory")
            except paramiko.AuthenticationException:
                logger._warn("Not able to connect because of Authentication")
            except paramiko.SSHException:
                logger._warn("Not able to connect because of SSHException")
            except:
                logger._warn("Not able to connect and run %s" % command)

            stdoutl = list(output[1])
            stderrl = list(output[2])
            stdout = "".join(stdoutl)
            stderr = "".join(stderrl)
            logger._log("--- stdout ---")
            logger._log(stdout)
            logger._log("--- stderr ---")
            logger._log(stderr)
            logger._log("---        ---")

            response = {'status_code': 0}
            response['_content'] = ''
            if stdout.find('HTTP') > -1:
                retcode = re.sub('.*HTTP/1\.1 (\d+).*', '\g<1>', stdout)[:3]
                respstr = re.sub('[^{]*(.*)', '\g<1>', stdout)
                if int(retcode) != 200:
                    logger._warn("RIS call was not OK")
                else:
                    resource = '[{"executionTime":0,"risResources": { "%s" : %s' % (resource, respstr) + '},"service":"%s"}]' % fusion_ip
                    response['_content'] = resource

                response['status_code'] = int(retcode)
            else:
                logger._log("RIS call returned no response")

            return response

        def hal_api_post_em_ris(self, fusion_ip, em_ip, resource, data=None, header=None, retries=5):  # pylint: disable=unused-argument
            """ Send a POST rest call to the EM RIS interface through the Fusion appliance

            Example:

            | HAL API Post Resource | ${FUSION IP} | ${EM_IP} | /rest/v1/BladeFru/1/ | |
            | HAL API Post Resource | ${FUSION IP} | ${EM_IP} | /rest/v1/Chassis/1/  | 10 |
            """
            dcs = BuiltIn().get_variable_value("${DCS}")
            nic = BuiltIn().get_variable_value("${FUSION_NIC}")
            ssh = paramiko.client.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if not header:
                header = '-H "Content-Type:application/json"'

            if dcs:
                command = '/usr/bin/curl %s -X POST %s -k https://' % (header, data) + em_ip + resource
            else:
                command = '/usr/bin/curl %s -X POST %s -k http://' % (header, data) + em_ip + "%" + nic + resource

            try:
                logger._log('Logging into EM to run: %s' % command)
                ssh.connect(fusion_ip, username='root', password='hpvse1', timeout=30.0)
                output = ssh.exec_command(command)
            except paramiko.BadHostKeyException:
                logger._warn("Not able to connect because of BadKeyException")
            except paramiko.AuthenticationException:
                logger._warn("Not able to connect because of Authentication")
            except paramiko.SSHException:
                logger._warn("Not able to connect because of SSHException")
            except:
                logger._warn("Not able to connect and run %s" % command)

            stdoutl = list(output[1])
            stderrl = list(output[2])
            stdout = "".join(stdoutl)
            stderr = "".join(stderrl)
            logger._log("--- stdout ---")
            logger._log(stdout)
            logger._log("--- stderr ---")
            logger._log(stderr)
            logger._log("---        ---")

            response = {'status_code': 0}
            response['_content'] = ''

            if stdout.find('HTTP') > -1:
                retcode = re.sub('.*HTTP/1\.1 (\d+).*', '\g<1>', stdout)[:3]
                respstr = re.sub('[^{]*(.*)', '\g<1>', stdout)
                if int(retcode) != 202:
                    logger._warn("RIS call was not OK")
                    logger._log("Response:\n" + respstr)
                else:
                    resource = '[{"executionTime":0,"risResources": { "%s" : %s' % (resource, respstr) + '},"service":"%s"}]' % fusion_ip
                    response['_content'] = resource

                response['status_code'] = int(retcode)
            else:
                logger._log("RIS call returned no response")

            return response

    class PermAPIKeywords(object):
        """ Perm API """
        def perm_api_perform_claim(self, fusion_ip, fusion_claim_ip, retries=5):
            """ Send a Claim call to the Perm Webapp on Fusion

            Example:
            | PERM API Perform Claim | ${FUSION_IP} | ${FUSION_CLAIM_IP} |
            | PERM API Perform Claim | ${FUSION_IP} | ${FUSION_CLAIM_IP} | 2 |
            """

            # Build URL
            url = "https://" + fusion_ip + "/perm/rest/resources/atlas/tbird/fts?ipAddress=" + fusion_claim_ip
            response = None
            # Retry in case rest call fails.
            # Currently calls to the webapp fail intermittently.
            attempts = 0
            for _ in range(0, retries):
                attempts += 1
                response = self.fusion_client.get(url)
                # Expect to get the following response upon successful 'fts' call:
                # response{ 'fts': True , 'ipAddress: <fusion_claim_ip>' }
                # 'fts':  Status code of perm call to 'fts'.  True = Success.  False = Failure
                # 'ipAddress':  Should be fusion_claim_ip
                if 'fts' in response and response['fts'] is True and 'ipAddress' in response and response['ipAddress'] != '':
                    break
            if attempts > 1:
                logger._warn("%d attempts were made; this operation should only take one attempt." % attempts)
            return response

    class IPKeywords(object):
        """ IP addresses """
        def ip_address_match(self, ip1, ip2):
            """ Compare two IP addresses.  Return True if they are equal.  False otherwise

            Example:
            |${status}= | IP Address Match | ${IP1} | ${IP2} |
            """

            # Build IP objects
            converted_ip1 = IPy.IP(ip1)
            converted_ip2 = IPy.IP(ip2)
            if converted_ip1 == converted_ip2:
                return True
            else:
                return False

    class DeploymentManagerKeywords(object):
        """ Deployment manager """
        def __init__(self):
            self.dep_mgr = DeploymentManager(self.fusion_client)

        def fusion_api_get_deployment_manager(self, uri=None, param='', api=None, headers=None):
            """Gets a Deployment Manager.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Deployment Manager  | <uri> | <param> | <api> | <headers>
            """
            return self.dep_mgr.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_deployment_manager(self, body, api=None, headers=None):
            """Creates a Deployment Manager.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Deployment Manager  | <body> | <api> | <headers>
            """
            return self.dep_mgr.create(body=body, api=api, headers=headers)

        def fusion_api_update_deployment_manager(self, body=None, uri=None, api=None, headers=None):
            """Updates a Deployment Manager.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Deployment Manager  | <uri> | <param> | <api> | <headers>
            """
            return self.dep_mgr.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_deployment_manager(self, name=None, uri=None, api=None, headers=None):
            """Deletes a Deployment Manager.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Delete Deployment Manager  | <uri> | <param> | <api> | <headers>
            """
            return self.dep_mgr.delete(name=name, uri=uri, api=api, headers=headers)

    class HypervisorManagerKeywords(object):
        """ Hypervisor manager """
        def __init__(self):
            self.hypervisor_mgr = HypervisorManager(self.fusion_client)

        def fusion_api_get_hypervisor_manager(self, uri=None, param='', api=None, headers=None):
            """Gets a hypervisor Manager.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
           [Example]
            ${resp} = Fusion Api Get Hypervisor Manager  | <uri> | <param> | <api> | <headers>
            """
            return self.hypervisor_mgr.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_hypervisor_manager(self, body, api=None, headers=None):
            """Creates a hypervisor Manager.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create hypervisor Manager  | <body> | <api> | <headers>
            """
            return self.hypervisor_mgr.create(body=body, api=api, headers=headers)

        def fusion_api_update_hypervisor_manager(self, body=None, uri=None, api=None, headers=None):
            """Updates a hypervisor Manager.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update hypervisor Manager  | <uri> | <param> | <api> | <headers>
            """
            return self.hypervisor_mgr.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_hypervisor_manager(self, name=None, uri=None, api=None, headers=None):
            """Deletes a hypervisor Manager.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Delete hypervisor Manager  | <uri> | <param> | <api> | <headers>
            """
            return self.hypervisor_mgr.delete(name=name, uri=uri, api=api, headers=headers)

    class HypervisorClustersKeywords(object):
        """ Hypervisor Clusters """
        def __init__(self):
            self.hypervisor_clusters = HypervisorClusters(self.fusion_client)

        def fusion_api_get_hypervisor_clusters(self, uri=None, param='', api=None, headers=None):
            """Gets a Hypervisor clusters.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
           [Example]
            ${resp} = Fusion Api Get Hypervisor Clusters | <uri> | <param> | <api> | <headers>
            """
            return self.hypervisor_clusters.get(uri=uri, api=api, headers=headers, param=param)

    class HypervisorClusterProfileKeywords(object):
        """ Hypervisor cluster profile """
        def __init__(self):
            self.cluster_profile = HypervisorClusterProfiles(self.fusion_client)

        def fusion_api_get_hypervisor_cluster_profile(self, uri=None, param='', api=None, headers=None):
            """Gets a Hypervisor cluster profile.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
           [Example]
            ${resp} = Fusion Api Get Hypervisor Cluster Profile | <uri> | <param> | <api> | <headers>
            """
            return self.cluster_profile.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_create_hypervisor_cluster_profile(self, body, api=None, headers=None):
            """Creates a hypervisor cluster profile.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Hypervisor Cluster Profile  | <body> | <api> | <headers>
            """
            return self.cluster_profile.create(body=body, api=api, headers=headers)

        def fusion_api_update_hypervisor_cluster_profile(self, uri=None, body=None, api=None, headers=None):
            """Updates a hypervisor cluster profile.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Hypervisor Cluster Profile | <uri> | <body> | <api> | <headers>
            """
            return self.cluster_profile.update(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_hypervisor_cluster_profile(self, name=None, uri=None, api=None, headers=None):
            """Deletes a hypervisor cluster profile.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
            [Example]
            ${resp} = Fusion Api Delete Hypervisor Cluster Profile | <uri> | <api> | <headers>
            """
            return self.cluster_profile.delete(name, uri, api, headers)

        def fusion_api_create_virtual_switch_layout(self, body, api=None, headers=None):
            """Creates a virtual switch layout.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Virtual Switch Layout  | <body> | <api> | <headers>
            """
            return self.cluster_profile.create(body=body, api=api, headers=headers, param='/virtualswitch-layout')

    class HypervisorHostProfileKeywords(object):
        """ Hypervisor host profile """
        def __init__(self):
            self.host_profile = HypervisorHostProfiles(self.fusion_client)

        def fusion_api_get_hypervisor_host_profile(self, uri=None, param='', api=None, headers=None):
            """Gets a Hypervisor host profile.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
           [Example]
            ${resp} = Fusion Api Get Hypervisor Host Profile | <uri> | <param> | <api> | <headers>
            """
            return self.host_profile.get(uri, api, headers, param)

        def fusion_api_update_hypervisor_host_profile(self, uri=None, body=None, api=None, headers=None):
            """Updates a hypervisor host profile.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Update Hypervisor Host Profile | <uri> | <body> | <api> | <headers>
            """
            return self.host_profile.update(body, uri, api, headers)

    class HypervisorHostKeywords(object):
        """ Hypervisor host """
        def __init__(self):
            self.hypervisor_host = HypervisorHosts(self.fusion_client)

        def fusion_api_get_hypervisor_host(self, uri=None, param='', api=None, headers=None):  # pylint: disable=unused-argument
            """Gets a Hypervisor host profile.
            [Arguments]
            uri: the uri of the resource to retrieve.
            param: query parameters
           [Example]
            ${resp} = Fusion Api Get Hypervisor Host | <uri> | <param> | <api> | <headers>
            """
            return self.hypervisor_host.get(uri, api, headers, param='')

    class RemoteSupportKeywords(object):
        """ Remote support """
        def __init__(self):
            self.remote_support = RemoteSupport(self.fusion_client)

        def fusion_api_edit_remote_support(self, body, api=None, headers=None):
            """Edit the remote support to initiate remote support registration
            [Example]
            ${resp} = Fusion Api Edit Remote Support | <body> | <api> | <headers>
            """
            return self.remote_support.update(body, api=api, headers=headers)

    class ConfigurationKeywords(object):
        """ Configuration """
        def __init__(self):
            self.configuration = Configuration(self.fusion_client)

        def fusion_api_get_configuration(self, uri=None, param='', api=None, headers=None):
            """Get the remote support configuration details
            [Example]
            ${resp} = Fusion Api Get Configuration | <name> | <api> | <headers>
            """
            return self.configuration.get(uri=uri, api=api, headers=headers, param=param)

    class OSDeploymentServerKeywords(object):
        """ OS Deployment """
        def __init__(self):
            self.osds = OSDeploymentServer(self.fusion_client)

        def fusion_api_create_os_deploymentserver(self, body, api=None, headers=None):
            """Create OS Deployment Server.
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create OS Deployment Server | <body> | <api> | <headers>
            """
            return self.osds.create(body, api, headers)

        def fusion_api_delete_os_deploymentserver(self, name=None, uri=None, param='', api=None, headers=None):
            """Delete OS Deployment server.
            [Arguments]
            name: The name of the resource to delete.
            uri: The uri of the resource to delete
            [Example]
            ${resp} = Fusion Api Delete OS Deployment Server | <name> | <uri> | <param> | <api> | <headers>
            """
            return self.osds.delete(name=name, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_os_deploymentserver(self, uri=None, param='', api=None, headers=None):
            """Gets value of the OS Deployment Server is available
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get OS Deployment Server  | <uri> | <param> | <api> | <headers>
            """
            return self.osds.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_i3sappliance_uri(self, uri=None, param='', api=None, headers=None):
            """Gets value of an i3s appliance
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get OS Deployment Server  | <uri> | <param> | <api> | <headers>
            """
            return self.osds.geti3suri(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_i3scluster_ip(self, uri=None, param='', api=None, headers=None):
            """Gets a primary cluster ipv4 ip
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            """
            return self.osds.geti3sclusterip(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_get_os_deploymentplan(self, uri=None, param='', api=None, headers=None):
            """Gets OS Deployment Plan
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get OS Deployment Plan  | <uri> | <param> | <api> | <headers>
            """
            return self.osds.getosdp(uri=uri, api=api, headers=headers, param=param)

    class FabricManagerKeywords(object):
        """ Fabric manager """
        def __init__(self):
            self.fabricmanager = FabricManager(self.fusion_client)

        def fusion_api_create_fabric_manager(self, body, api=None, headers=None):
            """Adds Fabric Manager to One View
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Create Fabric Manager | <body> | <api> | <headers>
            """
            return self.fabricmanager.post(body, api, headers)

        def fusion_api_get_fabric_manager(self, uri=None, param='', api=None, headers=None):
            """Gets the Fabric Manager details for the provided name or list of all Fabric Managers if name is not provided
            [Arguments]
            uri: URI of the FM resource to get
            param: URI parameter if any
            [Example]
            ${resp} = Fusion Api Get Fabric Manager | <uri> | <param> | <api> | <headers>
            """
            return self.fabricmanager.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_delete_fabric_manager(self, name, uri=None, api=None, headers=None):
            """Deletes the Fabric Manager
            [Arguments]
            name: REQUIRED a name of the Fabric Manager to be deleted
            [Example]
            ${resp} = Fusion Api Delete Fabric Manager | <name> | <api> | <headers>
            """
            return self.fabricmanager.delete(name=name, uri=uri, api=api, headers=headers)

        def fusion_api_edit_fabric_manager(self, body, uri, api=None, headers=None):
            """Edits Fabric Manager
            [Arguments]
            uri: REQUIRED a Uri of the existing Fabric Manager
            body: REQUIRED a dictionary containing request body elements
            """
            return self.fabricmanager.put(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_get_fabric_manager_tenants(self, uri, name=None, param='', api=None, headers=None):
            """Gets Tenants for the provided Fabric Manager
            [Arguments]
            uri: REQUIRED a Uri of the exisiting Fabric Manager
            name: REQUIRED a name of the tenant
            """
            param = '/tenants/'
            if name:
                param += '?&filter="\'name\' == \'%s\'"' % (name)
            return self.fabricmanager.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_fabric_manager_refresh(self, body, uri, api=None, headers=None):
            """Initiates Fabric Manager Refresh using Snapshot API
            [Arguments]
            uri: REQUIRED a Uri of the exisiting Fabric Manager
            """
            param = '/snapshot/'
            return self.fabricmanager.put(body=body, uri=uri, param=param, api=api, headers=headers)

        def fusion_api_get_fabric_manager_report(self, uri, api=None, headers=None):
            """Gets Reports for Fabric Manager
            [Arguments] Uri of the existing Fabric Manager or Tenant
            """
            param = '/report/'
            return self.fabricmanager.get(uri=uri, api=api, headers=headers, param=param)

        def fusion_api_fabric_manager_remediate(self, body, uri, api=None, headers=None):  # pylint: disable=unused-argument
            """Remediates Fabric Manager inconsistencies(Automatic only) for the provided resource.
            [Arguments]
            uri: Required a Uri of the FM resource with inconsistencies
            body: Body containing the details of remediation
            """
            param = '/compliance/'

            return self.fabricmanager.put(body=body, uri=uri, api=None, headers=None, param=param)

    class RackManagerKeywords(object):
        """ Rackmanagers basic operations to
        support import,refresh and remove
        """
        def __init__(self):
            self.rackmanager = RackManager(self.fusion_client)

        def fusion_api_add_rack_manager(self, body, api=None, headers=None):
            """Adds an rackmaager to the appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Rack Manager | <body> | <api> | <headers>
            """
            return self.rackmanager.post(body, api, headers)

        def fusion_api_get_rack_manager(self, uri=None, api=None, headers=None):
            """Gets a Rack Manager
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            [Example]
            ${resp} = Fusion Api Get Rack Manager | <uri> | <api> | <headers>
            """
            return self.rackmanager.get(uri=uri, api=api, headers=headers)

        def fusion_api_patch_rack_manager(self, body, uri, api=None, headers=None):
            """Issues a PATCH request. See REST-API docs for valid request bodies
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update.
            [Example]
            ${resp} | Fusion Api Patch Rack Manager | <body> | <uri> | <api> | <headers>
            """
            return self.rackmanager.patch(body=body, uri=uri, api=api, headers=headers)

        def fusion_api_delete_rack_manager(self, uri, name=None, param='', api=None, headers=None):
            """Deletes Rack Manager from the appliance based on  uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            param: you can use param=?force="true" to force remove an rack manager
            [Example]
            ${resp} = Fusion Api Delete Rack Manager | <uri> | <name> | <param> | <api> | <headers>
            """
            return self.rackmanager.delete(uri=uri, name=name, param=param, api=api, headers=headers)