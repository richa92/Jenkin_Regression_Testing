#!/usr/local/bin/python
import logging
import time
import pprint
import string
import re
from operator import itemgetter

from RoboGalaxyLibrary.utilitylib import logging as logger
import requests
from requests.auth import AuthBase
from requests.adapters import HTTPAdapter
from robot.libraries.BuiltIn import BuiltIn

from vcutils import Timer, Timeout

libLogger = "api-logger"
TaskCompletedStates = ['Error', 'Warning', 'Completed', 'Terminated', 'Killed']
TaskPendingStates = ['New', 'Starting', 'Running', 'Suspended', 'Stopping']

uris = {
    # ------------------------------------
    # CI Controller
    # ------------------------------------
    # deprecated URLs?
    'applConfig': "/rest/appliance/configuration/networkconfig",
    'applTimeZone': "/rest/appliance/configuration/timeconfig/timezone",
    'applNtp': "/rest/appliance/configuration/timeconfig/ntp",
    'applNodeVersion': "/rest/appliance/nodeinfo/version",
    # ------------------------------------
    'applNetConfig': "/rest/appliance/network-interfaces",
    'applGlobalSettings': "/rest/global-settings",
    'eulaStatus': "/rest/appliance/eula/status",
    'eulaSave': "/rest/appliance/eula/save",
    'serviceAccess': "/rest/appliance/settings/enableServiceAccess",
    'applianceNetworkInterfaces': "/rest/appliance/network-interfaces",
    'healthStatus': "/rest/appliance/health-status",
    'version': "/rest/version",
    'supportDump': "/rest/appliance/support-dumps",
    'backups': "/rest/backups",
    'dev-read-community-str': "/rest/appliance/device-read-community-string",
    'licenses': "/rest/licenses",
    'state': "/controller-state.json",
    'shutdown': "/rest/appliance/shutdown",
    # ------------------------------------
    # Security
    # ------------------------------------
    'loginSessions': "/rest/login-sessions",
    'users': "/rest/users",
    'userRole': "/rest/users/role",
    'changePassword': "/rest/users/changePassword",
    'roles': "/rest/roles",
    # ------------------------------------
    # Environment
    # ------------------------------------
    # ------------------------------------
    # Systems
    # ------------------------------------
    'servers': '/rest/server-hardware',
    'enclosures': '/rest/enclosures',
    'enclosureGroups': '/rest/enclosure-groups',
    'enclosurePreview': '/rest/enclosure-preview',
    'fwUpload': '/rest/firmware-bundles',
    'fwDrivers': '/rest/firmware-drivers',
    # ------------------------------------
    # Connectivity
    # ------------------------------------
    'conn': '/rest/connections',
    'ct': '/rest/connection-templates',
    'default-ct': '/rest/connection-templates/defaultConnectionTemplate',
    'enet': '/rest/ethernet-networks',
    'enetBulk': '/rest/ethernet-networks/bulk',
    'fcnet': '/rest/fc-networks',
    'fcoenet': '/rest/fcoe-networks',
    'nset': '/rest/network-sets',
    'li': '/rest/logical-interconnects',
    'lig': '/rest/logical-interconnect-groups',
    'ic': '/rest/interconnects',
    'ictype': '/rest/interconnect-types',
    'us': '/rest/uplink-sets',
    'ld': '/rest/logical-downlinks',
    'idpool': '/rest/id-pools',
    'vmac-pool': '/rest/id-pools/vmac',
    'vwwn-pool': '/rest/id-pools/vwwn',
    'vsn-pool': '/rest/id-pools/vsn',
    # ------------------------------------
    #  Server Profiles
    # ------------------------------------
    'profiles': '/rest/server-profiles',
    # ------------------------------------
    #  Health
    # ------------------------------------
    'alerts': '/rest/alerts',
    'events': '/rest/events',
    'audit-logs': '/rest/audit-logs',
    # ------------------------------------
    #  Searching and Indexing
    # ------------------------------------
    'resource': '/rest/index/resources',
    'association': '/rest/index/associations',
    'tree': '/rest/index/trees',
    'search-suggestion': '/rest/index/search-suggestions',
    # ------------------------------------
    #  Logging and Tracking
    # ------------------------------------
    'task': '/rest/tasks',
    # ------------------------------------
    #  Storage
    # ------------------------------------
    'storage-systems': '/rest/storage-systems',
    'host-types': '/rest/storage-systems/host-types',
    'managed-ports': '/managed-ports',  # Complete URI: /rest/storage-systems/{arrayID}/managed-ports
    'storage-pools': '/rest/storage-pools',
    'storage-volumes': '/rest/storage-volumes',
    'attachable-volumes': '/rest/storage-volumes/attachable-volumes',
    'volume-templates': '/rest/storage-volume-templates',
    'connectabe-templates': '/rest/storage-volume-templates/connectable-volume-templates',
    'volume-attachments': '/rest/storage-volume-attachments',
    'attachment-paths': '/paths',  # Complete URI: /rest/storage-volume-attachments/{attachmentID}/paths
    'providers': '/rest/fc-sans/providers',
    'managed-SANS': '/rest/fc-sans/managed-sans',
    # ------------------------------------
    #  Migration Manager
    # ------------------------------------
    'domain-compatibility': '/rest/migration-manager/domain-compatibility',
    'activity-events': '/rest/events',
    'activity-tasks': '/rest/tasks'
}


class CicAuth(AuthBase):

    def __init__(self, sessionid):
        self.sessionid = sessionid

    def __call__(self, r):
        r.headers['auth'] = self.sessionid
        return r


class connection(object):

    def __init__(self, ip, sessionId):
        self._sessionId = CicAuth(sessionId)
        # self._sessionId = sessionId
        self._cred = None
        self._ip = ip
        # Fusion Release    Min Supported Version   Appliance Current Version
        # 1.0               1                       3
        # 1.01              1                       3
        # 1.05              1                       4
        # 1.10              1                       101
        # 1.20              1                       120

        if BuiltIn().get_variable_value("${X-API-VERSION}"):
            self._apiVersion = BuiltIn().get_variable_value("${X-API-VERSION}")
        else:
            self._apiVersion = 120
        self._headers = {'X-API-Version': self._apiVersion,
                         'Accept': 'application/json, */*',
                         'Accept-language': 'en_US',
                         'Content-Type': 'application/json'}
        self._uris = uris  # TODO: need remove global uris from methods
        # self._headers['auth'] = sessionId
        self._http = requests.Session()
        # requires Python 2.7.4+ and Requests 1.2.3 +
        self._http.mount('http://', HTTPAdapter(max_retries=3))
        self._http.mount('https://', HTTPAdapter(max_retries=3))

    def delete(self, uri, headers):
        log = logging.getLogger(libLogger)
        try:
            log.debug('\nURL\tDELETE %s\nHeader %s\n' % (uri, headers))
            resp = self._http.delete(uri, auth=self._sessionId, headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to DELETE: %s" \
                % (uri)
            raise Exception(msg, e)
        if resp.status_code not in (200, 201, 202, 204):
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(resp.text))
            msg = "Status %d received from DELETE %s" \
                % (resp.status_code, uri)
            raise Exception(msg, resp.text)
        else:
            if resp.content:
                log.debug('\nStatus %d\nResponse Body %s' % (resp.status_code, pprint.PrettyPrinter().pformat(resp.json())))
                return resp.json()
            else:
                return resp

    def get(self, uri, headers):
        # This method automatically gets ALL resources. Use a filter if less are desired
        log = logging.getLogger(libLogger)
        x = 0
        members = []
        response = {}

        while True:
            try:
                log.debug('\nURL\tGET %s\nHeader %s\n' % (uri, headers))
                re = self._http.get(uri, auth=self._sessionId, headers=headers, verify=False)
                resp = re.json()
                log.debug('\nStatus %d\nResponse Headers %s\nResponse Body %s' % (re.status_code, re.headers, pprint.PrettyPrinter().pformat(resp)))

                if isinstance(resp, dict):
                    if 'nextPageUri' in resp:
                        if x == 0:
                            response = re.json()
                        else:
                            # add members
                            response['members'] += resp['members']
                        x += 1
                        count = resp['count']
                        total = resp['total']

                        if resp['nextPageUri']:
                            nextPageUri = resp['nextPageUri']
                            uri = string.Template("https://$ip$uri")
                            uri = uri.substitute(ip=self._ip, uri=nextPageUri)
                        else:
                            response['count'] = response['total']
                            break
                    else:
                        response = resp
                        break
                else:
                    break

            except Exception as e:
                msg = "Exception occured while attempting to GET: %s" \
                    % (uri)
                raise Exception(msg, e)

            if re.status_code != 200:
                log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(re.json()))
                msg = "Status %d received from GET %s" \
                    % (re.status_code, uri)
                raise Exception(msg, re.text)
            else:
                log.debug('\nStatus %d\nResponse Body %s' % (re.status_code, pprint.PrettyPrinter().pformat(re.json())))

        return response

    def put(self, uri, headers, body=None):
        log = logging.getLogger(libLogger)
        try:
            log.debug('\nURL\tPUT %s\nHeader %s\nBody %s\n' % (uri, headers, body))
            resp = self._http.put(uri, auth=self._sessionId, data=body, headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to PUT: %s" \
                % (uri)
            raise Exception(msg, e)
        if resp.status_code not in (200, 201, 202):
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(resp.text))
            msg = "Status %d received from PUT %s" \
                % (resp.status_code, uri)
            raise Exception(msg, resp.text)

        else:
            # This is needed for operations that create a task with no content (such as setNetworkInterfaces())
            # In this case, resp.json() returns an error, so instead just return the whole response object

            if resp.content:
                log.debug('\nStatus %d\nResponse Body %s' % (resp.status_code, pprint.PrettyPrinter().pformat(resp.json())))
                return resp.json()
            else:
                return resp

    def post(self, uri, headers, body=None):
        log = logging.getLogger(libLogger)
        try:
            log.debug('\nURL\tPOST %s\nHeader %s\nBody %s\n' % (uri, headers, body))
            resp = self._http.post(uri, auth=self._sessionId, data=body, headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to POST: %s" \
                % (uri)
            raise Exception(msg, e)
        if resp.status_code not in (200, 201, 202):
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(resp.text))
            msg = "Status %d received from POST %s" \
                % (resp.status_code, uri)
            raise Exception(msg, resp.text)
        else:
            # This is needed for operations that create a task with no content (such as setNetworkInterfaces())
            # In this case, resp.json() returns an error, so instead just return the whole response object

            if resp.content:
                log.debug('\nStatus %d\nResponse Body %s' % (resp.status_code, pprint.PrettyPrinter().pformat(resp.json())))
                return resp.json()
            else:
                return resp

    ###########################################################################
    # Login/Logout to/from appliance
    ###########################################################################
    # These are not in use yet.  At some point, we can use these methods to
    # replace the current login method in cicsecuritymodule
    # Ex. in DCU or robustness test, use these methods below to
    # con = connection(applianceIP)
    # credential = {'userName': applianceUser, 'password': appliancePassword}
    # con.login(credential)
    # encGroupBase = EncGrpBase(con)
    #
    # class EncGrpBase(object):
    # def __init__(self, con):
    #    self.con = con

    def login(self, cred):
        global uri
        self._cred = cred
        try:
            resp = self.post(uri=uri['loginSessions'], headers=self._headers, body=self._cred)
        except Exception:
            raise
        auth = resp['sessionID']
        # Add the auth ID to the headers dictionary
        self._headers['auth'] = auth

    def logout(self):
        global uri
        # resp, body = self.do_http(method, uri['loginSessions'] \
        #                        , body, self._headers)
        try:
            self.delete(uri['loginSessions'])
        except Exception:
            raise

        del self._headers['auth']

        return None

    ###########################################################################
    # Tasks
    ###########################################################################


class TaskBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)
        self.ip = ip
        self.sessionId = sessionId
        self.timer = Timer()
        self.logger = logger

    def getTask(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uri)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def waitTask(self, uri, interval=2, time_out=3600, hasChildren=False):
        # TODO: implement timeout
        # global fileLogger
        log = logging.getLogger(libLogger)

        # taskBase = TaskBase(ip=ip, sessionId=authToken)
        running = True

        t = re.compile('(?i)Warning|Unknown|Terminated|Killed|Error|Completed')

        maxId = 0
        count = 0

        timer = Timer('waitTask', time_out)
        timer.start()

        while running:
            # task = taskBase.getTask(uri=uri)
            task = self.getTask(uri=uri)
            resource = ""

            if 'associatedResource' in task:
                # Check if this task has an associated resource
                if task['associatedResource']['resourceUri']:
                    resource = "for: " + task['associatedResource']['resourceName']
            else:
                # Check if this task has an associated resource uri
                if 'associatedResourceUri' in task:
                    resource = "for: " + task['associatedResourceUri']

            if count == 0:
                if task['taskState'] != 'Completed':
                    self.logger._log_to_console_and_log_file(" Task: [%s:%s] is: %s\t%s" % (task['name'], task['category'], task['taskState'].ljust(10), resource))

            for x in sorted(task['progressUpdates'], key=itemgetter('id')):
                if int(x['id']) > maxId:
                    if x['statusUpdate']:
                        self.logger._log_to_console_and_log_file(" Task: [%s:%s] is: %s\tStatus: %s" % (task['name'], task['category'], task['taskState'].ljust(10), x['statusUpdate']))
                    maxId = int(x['id'])

            if t.match(task['taskState']):
                running = False
                self.logger._log_to_console_and_log_file(" Task: [%s:%s] is: %s\t%s" % (task['name'], task['category'], task['taskState'].ljust(10), resource))
                break
            else:
                time.sleep(interval)
            # TODO: Need to modify to display task state update without duplicate
            if hasChildren and count == 0:
                parenttask = self.getTask(uri + '?view=tree')
                if len(parenttask['children']) > 0:
                    for x in parenttask['children']:
                        resource = ""
                        if 'associatedResource' in x['resource']:
                            # Check if this task has an associated resource
                            if x['resource']['associatedResource']['resourceUri']:
                                resource = "for: " + x['resource']['associatedResource']['resourceName']
                        else:
                            # Check if this task has an associated resource uri
                            if 'associatedResourceUri' in x['resource']:
                                resource = "for: " + x['resource']['associatedResource']['associatedResourceUri']
                        self.logger._log_to_console_and_log_file("   Task: [%s:%s] is: %s\t%s" % (x['resource']['name'], x['resource']['category'], x['resource']['taskState'].ljust(10), resource))
                        """
                        if not t.match(x['resource']['taskState']):
                            self.logger._log_to_console_and_log_file("....Children task [%s] is : %s" %(x['resource']['name'],x['resource']['taskState']))
                            self.waitTask(uri=x['resource']['uri'], interval=2)
                        else:
                            childrenResource = self.getTask(x['resource']['associatedResourceUri'])
                            self.logger._log_to_console_and_log_file("....Children task [%s:%s] is : %s" %(x['resource']['name'], childrenResource['name'], x['resource']['taskState']))
                        """

            count += 1
            try:
                timer.elapse()
            except Timeout as e:
                msg = " Task: [%s:%s] %s: timed out" % (task['name'], task['category'], resource)
                raise Exception(msg, e)

        timer.stop()
