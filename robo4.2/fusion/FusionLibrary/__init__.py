"""
FusionLibrary instance
"""
from dateutil.parser import parse as parse_date
from dateutil import tz
import datetime
from collections import namedtuple
from git import Repo
import socket
from time import sleep
import json
from Queue import Queue
from threading import Thread
import os
import uuid
from SSHLibrary import SSHLibrary
import sys

from robot import version as robot_version
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from RoboGalaxyLibrary.ui.common import ui_lib
from FusionLibrary.version import get_version
from FusionLibrary.keywords.fusion_api import FusionAPIKeywords
from FusionLibrary.keywords.hellfire_api import SVMCAPIKeywords
from FusionLibrary.keywords.hellfire_api import HellfireAPIKeywords
from FusionLibrary.keywords.fusion_sanmanager_ui import FusionSanmanagerUIKeywords
from FusionLibrary.keywords.fusion_san_ui import FusionSanUIKeywords
from FusionLibrary.keywords.fusion_ui import FusionUIKeywords
from FusionLibrary.keywords.mantra_ui import MantraUIKeywords
# from FusionLibrary.keywords.hal_api import HalAPIKeywords
from FusionLibrary.keywords.dcs_api import DCSAPIKeywords
from FusionLibrary.keywords.fusion_srm_api import FusionSRMOaApiKeywords
from FusionLibrary.keywords.fusion_srm_api import FusionSRMIloApiKeywords
from FusionLibrary.keywords.fusion_pmsan_ui import FusionPMSanUiKeywords
from FusionLibrary.cli.oa.oa_operation import OACLIKeywords
from FusionLibrary.cli.oneview.fusion_operation import FusionCLIKeywords
from FusionLibrary.cli.traffic.keywords import TrafficLibraryKeywords
from FusionLibrary.keywords.tru import TRUKeywords
from FusionLibrary.libs.utils.elk import ElkQueueWriter
from FusionLibrary.keywords.cpt.payload_generator import CptPayloadGenerator
from FusionLibrary.keywords.network.config_generator import NetworkConfigGenerator

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))
__version__ = get_version()

# These  constants define the endpoint for activity logging
DEFAULT_ACTIVITY_LOGGING_SERVER = 'http://rist-elk.vse.rdlabs.hpecorp.net:9200'
DEFAULT_ACTIVITY_INDEX_NAME = "fusionlibrary-activity"


def _get_host_variable():
    """
    find the variable that contains the OV ip
    :return:
    """
    # typical OneView IP variables
    glist = ['${APPLIANCE_IP}', '${IP}', '${FUSION_IP}', '${OV_IP}', '${OV}', '${ONEVIEW}', '${ONEVIEW_IP}']
    for k, v in BuiltIn().get_variables().iteritems():
        if k.upper() in [i.upper() for i in glist]:
            return v


class FusionLibrary(
        FusionAPIKeywords,
        FusionAPIKeywords.ActiveUserSessionsKeywords,
        FusionAPIKeywords.AlertKeywords,
        FusionAPIKeywords.AuditLogKeywords,
        FusionAPIKeywords.AuthorizationsKeywords,
        FusionAPIKeywords.ApplianceDeviceReadCommunityKeywords,
        FusionAPIKeywords.ApplianceEulaKeywords,
        FusionAPIKeywords.ApplianceFactoryResetKeywords,
        FusionAPIKeywords.ApplianceFirmwareKeywords,
        FusionAPIKeywords.ApplianceHealthStatusKeywords,
        FusionAPIKeywords.ApplianceNetworkInterfacesKeywords,
        FusionAPIKeywords.ApplianceNodeInformationKeywords,
        FusionAPIKeywords.ApplianceShutdownKeywords,
        FusionAPIKeywords.ApplianceStateKeywords,
        FusionAPIKeywords.ApplianceSupportDumpKeywords,
        FusionAPIKeywords.ApplianceTimeAndLocaleConfigurationKeywords,
        FusionAPIKeywords.ApplianceTrapDestinationKeywords,
        FusionAPIKeywords.ApplianceSnmpv3TrapDestinationKeywords,
        FusionAPIKeywords.ApplianceSnmpv3TrapForwardingUserKeywords,
        FusionAPIKeywords.ApplianceUpgrade,
        FusionAPIKeywords.BackupKeywords,
        FusionAPIKeywords.CertificateAuthorityKeywords,
        FusionAPIKeywords.CertificateValidationConfigurationKeywords,
        FusionAPIKeywords.CertificateClientRabbitMqKeywords,
        FusionAPIKeywords.ClientCertificateKeywords,
        FusionAPIKeywords.ConnectionsKeywords,
        FusionAPIKeywords.ConnectionTemplateKeywords,
        FusionAPIKeywords.DatacenterKeywords,
        FusionAPIKeywords.DeviceManagerKeywords,
        FusionAPIKeywords.DeploymentManagerKeywords,
        FusionAPIKeywords.DriveEnclosureKeywords,
        FusionAPIKeywords.DomainsKeywords,
        FusionAPIKeywords.EmailNotificationKeywords,
        FusionAPIKeywords.EnclosureKeywords,
        FusionAPIKeywords.RackManagerKeywords,
        FusionAPIKeywords.EnclosureGroupKeywords,
        FusionAPIKeywords.EthernetNetworkKeywords,
        FusionAPIKeywords.EventKeywords,
        FusionAPIKeywords.FabricKeywords,
        FusionAPIKeywords.FabricManagerKeywords,
        FusionAPIKeywords.FcNetworkKeywords,
        FusionAPIKeywords.FcoeNetworkKeywords,
        FusionAPIKeywords.FirmwareBundleKeywords,
        FusionAPIKeywords.FirmwareDriverKeywords,
        FusionAPIKeywords.GlobalSettingsKeywords,
        FusionAPIKeywords.HaNodesKeywords,
        FusionAPIKeywords.HypervisorManagerKeywords,
        FusionAPIKeywords.HypervisorClusterProfileKeywords,
        FusionAPIKeywords.HypervisorHostProfileKeywords,
        FusionAPIKeywords.HypervisorHostKeywords,
        FusionAPIKeywords.HypervisorClustersKeywords,
        FusionAPIKeywords.IdPoolKeywords,
        FusionAPIKeywords.IdPoolsIpv4RangeKeywords,
        FusionAPIKeywords.IdPoolsIpv4SubnetKeywords,
        FusionAPIKeywords.IdPoolsVmacRangeKeywords,
        FusionAPIKeywords.IdPoolsVsnRangeKeywords,
        FusionAPIKeywords.IdPoolsVwwnRangeKeywords,
        FusionAPIKeywords.IndexAssociationKeywords,
        # FusionAPIKeywords.IndexResourceKeywords,
        FusionAPIKeywords.IndexResourceKeywords,
        # FusionAPIKeywords.IndexSearchSuggestionKeywords,
        # FusionAPIKeywords.IndexTreeKeywords,
        FusionAPIKeywords.InterconnectLinkTopologyKeywords,
        FusionAPIKeywords.InterconnectKeywords,
        FusionAPIKeywords.InterconnectTypesKeywords,
        FusionAPIKeywords.InternalLinkSetKeywords,
        # FusionAPIKeywords.LabelKeywords,
        FusionAPIKeywords.LicensesKeywords,
        FusionAPIKeywords.SecurityStandardsKeywords,
        FusionAPIKeywords.LoginDetailsKeywords,
        FusionAPIKeywords.LoginDomainKeywords,
        FusionAPIKeywords.LogicalDownlinkKeywords,
        FusionAPIKeywords.LoginDomainsGlobalSettingsKeywords,
        FusionAPIKeywords.LoginDomainsLoginCertificatesKeywords,
        FusionAPIKeywords.LoginDomainsGroupToRoleMappingKeywords,
        FusionAPIKeywords.LoginSessionKeywords,
        FusionAPIKeywords.LogicalInterconnectKeywords,
        FusionAPIKeywords.LogicalInterconnectGroupKeywords,
        FusionAPIKeywords.LogicalSwitchGroupKeywords,
        FusionAPIKeywords.LogicalSwitchKeywords,
        FusionAPIKeywords.LogicalEnclosureKeywords,
        FusionAPIKeywords.ManagedSanKeywords,
        FusionAPIKeywords.MetricStreamingKeywords,
        FusionAPIKeywords.NetworkSetKeywords,
        FusionAPIKeywords.MigratableVcDomainKeywords,
        FusionAPIKeywords.PingKeywords,
        FusionAPIKeywords.PowerDeviceKeywords,
        FusionAPIKeywords.ProviderKeywords,
        FusionAPIKeywords.RackKeywords,
        FusionAPIKeywords.RemoteSyslogKeywords,
        FusionAPIKeywords.RemoteSupportKeywords,
        FusionAPIKeywords.ConfigurationKeywords,
        FusionAPIKeywords.ReportKeywords,
        FusionAPIKeywords.RestoreKeywords,
        FusionAPIKeywords.RolesKeywords,
        FusionAPIKeywords.SasInterconnectsKeywords,
        FusionAPIKeywords.SasInterconnectTypesKeywords,
        FusionAPIKeywords.SasLogicalInterconnectGroupKeywords,
        FusionAPIKeywords.SasLogicalInterconnectKeywords,
        FusionAPIKeywords.ServerHardwareTypesKeywords,
        FusionAPIKeywords.ServerHardwareKeywords,
        FusionAPIKeywords.ServerProfileKeywords,
        FusionAPIKeywords.ServerProfileTemplateKeywords,
        FusionAPIKeywords.ServiceAccessKeywords,
        FusionAPIKeywords.SessionsKeywords,
        FusionAPIKeywords.StartupProgressKeywords,
        FusionAPIKeywords.StoragePoolKeywords,
        FusionAPIKeywords.StorageSystemKeywords,
        FusionAPIKeywords.StorageVolumeKeywords,
        FusionAPIKeywords.StorageVolumeTemplateKeywords,
        FusionAPIKeywords.StorageVolumeAttachmentKeywords,
        FusionAPIKeywords.SwitchKeywords,
        FusionAPIKeywords.SwitchTypesKeywords,
        FusionAPIKeywords.TaskKeywords,
        FusionAPIKeywords.UplinkSetKeywords,
        FusionAPIKeywords.UserKeywords,
        FusionAPIKeywords.VersionKeywords,
        FusionAPIKeywords.SasLogicalJbodsKeywords,
        FusionAPIKeywords.SasLogicalJbodAttachmentsKeywords,
        FusionAPIKeywords.WebServerCertificateKeywords,
        FusionAPIKeywords.HalAPIKeywords,
        FusionAPIKeywords.PermAPIKeywords,
        FusionAPIKeywords.ProxyServerKeywords,
        FusionAPIKeywords.IPKeywords,
        FusionAPIKeywords.ScopeKeywords,
        FusionAPIKeywords.RepositoryKeywords,
        FusionAPIKeywords.SshAccessKeywords,
        FusionAPIKeywords.ApplianceCertificateKeywords,
        FusionAPIKeywords.RemoteCertificateKeywords,
        FusionAPIKeywords.ServerCertificateKeywords,
        FusionAPIKeywords.CertificateStatusKeywords,
        FusionUIKeywords,
        MantraUIKeywords,
        FusionSRMOaApiKeywords,
        FusionSRMIloApiKeywords,
        FusionSanmanagerUIKeywords,
        FusionSanUIKeywords,
        DCSAPIKeywords,
        FusionPMSanUiKeywords,
        HellfireAPIKeywords.InfrastructureVmsKeywords,
        HellfireAPIKeywords.StoreVirtualVsaClusterKeywords,
        OACLIKeywords,
        FusionCLIKeywords,
        HellfireAPIKeywords,
        SVMCAPIKeywords,
        TrafficLibraryKeywords,
        TrafficLibraryKeywords.VspLibraryKeywords,
        TrafficLibraryKeywords.PingTrafficLibraryKeywords,
        TrafficLibraryKeywords.IPerfTrafficLibraryKeywords,
        TrafficLibraryKeywords.IOMeterLibraryKeywords,
        FusionAPIKeywords.OSDeploymentServerKeywords,
        TRUKeywords,
        CptPayloadGenerator,
        NetworkConfigGenerator):
    """ Main FusionLibrary keyword class definition """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LISTENER_API_VERSION = 2
    FILTER_LIBRARIES = ['BuiltIn', 'Collections', 'Dialogs', 'OperatingSystem', 'SSHLibrary', 'String', 'XML']
    MAX_QUEUE = 1000        # max elk data queue size

    # Elk data encapsulation object
    ElkItem = namedtuple("ElkItem", "obj_type, data")

    def _gather_repo_info(self):
        """
        Private method to initialize variables pertaining to Test repository
        :return: None
        """
        try:
            # Invalid error would be thrown if path is not source_root
            repo = Repo(os.path.dirname(THIS_DIR))
            self.repo_commit = str(repo.rev_parse('HEAD'))
            self.repo_branch_name = repo.git.rev_parse('--abbrev-ref',
                                                       '--symbolic-full-name',
                                                       '@{u}')
            del repo
        except:     # noqa
            pass

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.elk_queue_writer = None
        self.hostname = socket.gethostname()
        self.uuid = str(uuid.uuid1())
        self._ov = None
        self._ssh = None
        self.activity_queue = None
        self.log_activity = False
        self.log_activity_to_cidebug_log = False
        self.queue_writer = None
        self.repo_commit = 'Not Found'
        self.repo_branch_name = 'Not identified'
        self._gather_repo_info()

        logger._log_to_console_and_log_file("Fusion library version %s" % __version__)
        for base in FusionLibrary.__bases__:
            base.__init__(self)

    def __logging_activity(self):
        """
        This private method handles writing to the ElkWriter thread
        if logging is enabled.
            Note: log activity with -v LOG_ACTIVITY:True
        """
        # initialize and start the activity logging queue
        self.log_activity = BuiltIn().get_variable_value("${LOG_ACTIVITY}")
        if self.log_activity == 'False':
            return False
        # initialize queue and queue writer
        if not self.activity_queue:
            self.activity_queue = Queue(maxsize=self.MAX_QUEUE)
        if not self.queue_writer:
            host = BuiltIn().get_variable_value("${ACTIVITY_LOGGING_SERVER}")
            index = BuiltIn().get_variable_value("${ACTIVITY_INDEX_NAME}")
            if not host:
                host = DEFAULT_ACTIVITY_LOGGING_SERVER
            if not index:
                index = DEFAULT_ACTIVITY_INDEX_NAME
            self.queue_writer = ElkQueueWriter(host, index, self.activity_queue)
            self.queue_writer.start()
        return True

    def __logging_activity_to_cidebug_log(self):
        """
        This private method handles writing to the /ci/logs/ciDebug.log file on the appliance
        if logging is enabled.
            Note: log activity with -v LOG_ACTIVITY_TO_CIDEBUG:True
        """
        # initialize and start the activity logging queue
        self.log_activity_to_cidebug_log = BuiltIn().get_variable_value("${LOG_ACTIVITY_TO_CIDEBUG}")
        if not self.log_activity_to_cidebug_log:
            return False
        # get the appliance host and open ssh session
        if not self._ov:
            self._ov = _get_host_variable()
        if not self._ssh:
            self.__create_ssh_connection_and_login(self._ov)
        return True

    def __create_ssh_connection_and_login(self, host, username='root', password='hpvse1'):
        """ Create a new SSH connection and log in """
        try:
            self._ssh = SSHLibrary()
            self._ssh.set_default_configuration(timeout='15 seconds', term_type='xterm', prompt='#')
            self._ssh.open_connection(host)
            self._ssh.login(username, password)
        except:     # noqa
            e = sys.exc_info()[0]
            logger._log_to_console_and_log_file("unable to connect ssh: {} {}".format(host, e))
            self._ssh = None

    def __run_ssh_commands(self, cmds):
        """ Run an SSH command """
        if self._ssh is not None:
            if self._ssh.get_connection(host=True) is not None:
                try:
                    self._ssh.write(cmds)
                except:     # noqa
                    e = sys.exc_info()[0]
                    logger._log_to_console_and_log_file("unable to write to ssh: {} {}".format(cmds, e))
                    self._ssh.close_connection()
                    self._ssh = None
            else:
                logger.info("no ssh: session {}".format(cmds))
                self._ssh.close_connection()
                self._ssh = None

    def _write_log(self, ltype, stat, attrs):
        """ Write a log entry """
        name = None
        if 'longname' in attrs:
            name = attrs['longname']
        elif 'kwname' in attrs:
            name = attrs['kwname']
        return """date +"%Y-%m-%d %H:%M:%S.%N %Z,INFO,ROBO,{},{},{},{}" >> /ci/logs/ciDebug.log""".format(self.uuid,
                                                                                                          ltype.upper(),
                                                                                                          name,
                                                                                                          stat.upper())

    def _add_data_to_attrs(self, name, attrs):
        """
        Add additional data to suite/test/keyword attributes for Elk logging.
        """
        metadata = BuiltIn().get_variable_value("&{SUITE METADATA}")
        if not self._ov:
            self._ov = _get_host_variable()
        if 'kwname' in attrs:
            attrs['name'] = attrs['kwname']
            del attrs['kwname']
        else:
            attrs['name'] = name
        attrs['suiteName'] = BuiltIn().get_variable_value("${SUITE_NAME)")
        attrs['suiteSource'] = BuiltIn().get_variable_value("${SUITE_SOURCE)")
        attrs['testName'] = BuiltIn().get_variable_value("${TEST_NAME)")
        attrs['oneViewIp'] = self._ov
        attrs['oneViewVersion'] = metadata.get("OneView Version")
        if 'starttime' in attrs:
            attrs['starttime'] = parse_date(attrs['starttime']).replace(tzinfo=tz.tzlocal()).astimezone(tz.tzutc()).isoformat()
        if 'endtime' in attrs:
            attrs['endtime'] = parse_date(attrs['endtime']).replace(tzinfo=tz.tzlocal()).astimezone(tz.tzutc()).isoformat()
        attrs['@timestamp'] = attrs.get('starttime')
        attrs['hostname'] = self.hostname
        attrs['runId'] = self.uuid
        attrs['gitCommitId'] = self.repo_commit
        attrs['gitRemoteBranch'] = self.repo_branch_name
        return attrs

    def _start_suite(self, name, attrs):  # pylint: disable=unused-argument
        """
        This listener logs suite start
        """
        if self.__logging_activity_to_cidebug_log():
            self.__run_ssh_commands(self._write_log('suite', 'started', attrs))
        BuiltIn().set_global_variable("${RUN_UUID}", self.uuid)

    def _end_suite(self, name, attrs):  # pylint: disable=unused-argument
        """
        This listener logs suite activity
        """
        if self.__logging_activity_to_cidebug_log():
            self.__run_ssh_commands(self._write_log('suite', 'ended', attrs))
            self._ssh.close_connection()

        if self.__logging_activity():
            # If the queue is full, don't write anything (since queue.put blocks, it would halt the test).
            # Otherwise, write the name and attrs to Elk
            if not self.activity_queue.full():
                self.activity_queue.put_nowait(self.ElkItem('suite', self._add_data_to_attrs(name, attrs)))
            if attrs.get('id') == 's1':
                # In order to process all queue items before the test suite exits,
                # it's necessary to wait for the queue to become empty or until the timer expires.
                # Otherwise, the test will exit before the queue is fully written.
                start = datetime.datetime.now()
                while not self.activity_queue.empty() and (datetime.datetime.now() - start).total_seconds() < 10.0:
                    sleep(1)

    def _start_test(self, name, attrs):  # pylint: disable=unused-argument
        """
        This listener logs test activity
        """
        if self.__logging_activity_to_cidebug_log():
            self.__run_ssh_commands(self._write_log('test case', 'started', attrs))

    def _end_test(self, name, attrs):
        """
        This listener logs test activity
        """
        if self.__logging_activity_to_cidebug_log():
            self.__run_ssh_commands(self._write_log('test case', 'ended', attrs))

        # If the queue is full, don't write anything (since queue.put blocks, it would halt the test).
        # Otherwise, write the name and attrs to Elk
        if self.__logging_activity() and not self.activity_queue.full():
            self.activity_queue.put_nowait(self.ElkItem('test', self._add_data_to_attrs(name, attrs)))

    def _start_keyword(self, name, attrs):  # pylint: disable=unused-argument
        """
        This listener logs keyword activity
        """
        if self.__logging_activity_to_cidebug_log():
            # filter out libraries and keyword types we're not interested in
            if attrs.get('libname') not in self.FILTER_LIBRARIES and attrs.get('type') not in ['For', 'For Item']:
                self.__run_ssh_commands(self._write_log('keyword', 'started', attrs))

    def _end_keyword(self, name, attrs):
        """
        This listener logs keyword activity
        """
        if self.__logging_activity_to_cidebug_log():
            # filter out libraries and keyword types we're not interested in
            if attrs.get('libname') not in self.FILTER_LIBRARIES and attrs.get('type') not in ['For', 'For Item']:
                self.__run_ssh_commands(self._write_log('keyword', 'ended', attrs))

        if self.__logging_activity():
            # filter out libraries and keyword types we're not interested in
            if attrs.get('libname') not in self.FILTER_LIBRARIES and attrs.get('type') not in ['For', 'For Item']:
                if not self.activity_queue.full():
                    self.activity_queue.put_nowait(self.ElkItem('keyword', self._add_data_to_attrs(name, attrs)))
