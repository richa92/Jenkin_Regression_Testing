"""
    PushData2Alm
    Process Robot Framework 'output.xml' files and create corresponding
    entities in ALM.
"""

from cgi import escape
from datetime import datetime
from os.path import join, exists
from re import sub
from urllib import quote_plus
from xml.dom.minidom import parseString
import logging
import re
import sys

from dateutil.parser import parse
import argparse
import requests

import xml.etree.ElementTree as ET


requests.packages.urllib3.disable_warnings()    # @UndefinedVariable

log = logging.getLogger('alm_lib')
logging.basicConfig(format='%(asctime)-15s,%(levelname)s,%(name)s,%(message)s')
log.setLevel(logging.INFO)


class AlmAuthenticationError(Exception):
    pass


class EntityError(Exception):
    pass


class Entity:

    """ Entity class encapsulates an ALM REST Entity. """

    def __init__(self, entity_type):
        self.fields = {}
        self.path = ""
        self.type = entity_type

    def __eq(self, ocmp):
        return self.fields == ocmp.fields

    @staticmethod
    def from_xml(xml_string):
        """
        Name
            from_xml
        Description
            Creates an entity from the RAW XML
        Parameters
            xml_string - An xml string of <Entity></Entity> type.
            See ALM REST API reference.
        Returns
            Entity object
        """
        entity = Entity(None)
        dom = parseString(xml_string)
        for ent in dom.getElementsByTagName('Entity'):
            entity.type = ent.getAttribute('Type')
            for field in ent.getElementsByTagName('Field'):
                if len(field.childNodes) != 0:
                    if not field.childNodes[0].childNodes:
                        entity.fields[field.getAttribute('Name')] = None
                    else:
                        entity.fields[field.getAttribute('Name')] = \
                            field.childNodes[0].childNodes[0].nodeValue
        return entity

    @staticmethod
    def from_json(json_entity):
        """
        Name
            from_json
            Description
            Creates an entity from the RAW JSON
        Parameters
            json_entity - An json entity.
            See ALM REST API reference.
        Returns
            Entity object
        """
        entity = Entity(None)
        entity.type = str(json_entity['Type'])
        for item in json_entity['Fields']:
            entity.fields[item['Name']] = str(item['values'][0]['value']) if len(item['values']) > 0 and 'value' in item['values'][0] else None
        return entity

    def to_xml(self):
        """ convert the entity to XML - suitable for put or post """
        estr = '<Entity Type="%s"><Fields>' % self.type
        for k, v in self.fields.iteritems():
            if v is None:
                val = ''
            else:
                val = v
            estr += '<Field Name="%s">' % k
            estr += '<Value>%s</Value>' % val
            estr += '</Field>'
        estr += '</Fields></Entity>'
        return estr


class EntityType(object):

    """ EntityType enum used in REST queries """
    TESTSET = 'test-set'
    TESTSETS = 'test-sets'
    TEST = 'test'  # testplan
    TESTS = 'tests'
    RUNS = 'runs'
    TESTINSTANCE = 'test-instance'  # testlab
    TESTINSTANCES = 'test-instances'
    TESTLABFOLDERS = 'test-set-folders'
    TESTLABFOLDER = 'test-set-folder'
    TESTPLANFOLDERS = 'test-folders'
    TESTPLANFOLDER = 'test-folder'
    RUN = 'run'
    RUNSTEPS = 'run-steps'
    RUNSTEP = 'run-step'
    DESIGNSTEP = 'design-step'
    DESIGNSTEPS = 'design-steps'


class FieldType(object):

    """ FieldType enum """
    DESCRIPTION = 'comment'
    ENVIRONMENT = 'user-10'
    BROWSER = 'user-03'


class RunStatus(object):

    """ RunStatus enum """
    BLOCKED = "Blocked"
    FAILED = "Failed"
    NA = "N/A"
    NORUN = "No Run"
    NOTCOMPLETED = "Not Completed"
    PASSED = "Passed"
    REPAIR = "Repair"


class StepStatus(RunStatus):
    pass


class AlmConnectionException(Exception):
    pass


class Alm:

    """ The main ALM REST API Class library """

    PATH_SEPARATOR = "\\"

    _invalid_run_fields = ['run-ver-stamp', 'vc-lokedby', 'vc-status', 'last-modified']

    def __init__(self, url, domain, project, username, password):
        """
        Init constructor.
        Parameters: url: ALM URL such as https://qc1d.atlanta.hp.com
                    domain: project domain
                    project: project name
                    username
                    password
        """

        self._username = username
        self._password = password
        self._url = url
        self._domain = domain
        self._project = project
        self._session = None
        self._connected = False
        self._headers = {}
        self.connect()

    def connect(self):
        """ Connect to ALM
            Authenticating in ALM 12 is a 2 step process.  The first step involves a GET from the authenticate endpoint.
            This will return an LWSSO Cookie, which must be placed in the headers of subsequent requests.
            Step 2 is a POST to the site-session endpoint to obtain the QCSession token which will also be used on all requetst.
        """
        self.session = requests.Session()
        self._headers = {}
        uri = self._url + '/qcbin/authentication-point/authenticate'
        log.info('Connecting to %s as %s' % (uri, self._username))
        res = self.session.get(uri, auth=(self._username, self._password), verify=False)

        if res.status_code != 200:
            raise AlmAuthenticationError('Authentication unsuccessful.  Status code={0} Message="{1}"'.format(res.status_code, res.text))

        # now post to the site-sessions endpioint to get the QCSession token
        res = self.session.post(self._url + '/qcbin/rest/site-session', headers=self._headers)
        if res.status_code != 201 and res.status_code != 200:
            raise AlmAuthenticationError('Failed to retrieve QCSession Token.  Status code={0} Message="{1}"'.format(res.status_code, res.text))
        self._headers['Set-Cookie'] = res.cookies['QCSession']

        self._connected = True
        return self._connected

    def disconnect(self):
        uri = self._url + '/qcbin/authentication-point/logout'
        log.info('Logging out using %s' % uri)
        req = self.session.get(uri)
        if req.status_code == 200:
            self._connected = False
            self._headers = {}      # discard the QCSession token
        else:
            raise Exception('Logout unsuccessful.  Status code=%s Message="%s"'
                            % (req.status_code, req.text))

    def is_connected(self):
        return self._connected

    def normalize_path(self, path):
        """
        Name
            normalize_path
        Description
            Normalize the path for folder queries
        Parameters
            An ALM path to a folder, test, testset
        Returns
        """
        return sub(r'\\+', r'\\', path).strip().strip(r'\\')

    def get_entity(self, entity_type, query=None, page_size='max'):
        """
        Name
            get_entity
        Description
            Get_entity returns a list of entities of the specified
            entity type.
        Parameters
            entity_type: the entity type enum
            query: an ALM REST query (SEE DOCS)
            page_size: number of entities to return
        Returns
        """
        qs = ''
        if query is not None:
            qs = '&query={%s}' % query
        qurl = '%s/qcbin/rest/domains/%s/projects/%s/%s?alt=application/json&page-size=%s%s' % \
            (self._url, self._domain, self._project, entity_type, page_size, qs)
        for retry in range(1, 11):
            try:
                result = self.session.get(qurl, headers=self._headers)
                break
            except requests.exceptions.SSLError as ex:
                log.info("Failure {0} while to connect to ALM: {1}".format(retry, ex.message))
                self.connect()
                continue
            break
        entities = result.json()['entities']
        element_list = []
        for ent in entities:
            log.debug("Working on {0} of {1}".format(len(element_list), len(entities)))
            el = Entity.from_json(ent)
            element_list.append(el)

        return element_list

    def create_entity(self, entity_type, entity, collection=None):
        """
        Name
            Create entity in ALM
        Description
            Creates an entity of the specified type and provided entity object.
        Parameters
            entity_type: the entity type enum
            entity: the entity object
        Returns

        """
        body = entity.to_xml()
        if collection is not None:
            qurl = '%s/qcbin/rest/domains/%s/projects/%s/%s/%s' % \
                (self._url, self._domain, self._project, entity_type, collection)
        else:
            qurl = '%s/qcbin/rest/domains/%s/projects/%s/%s' % \
                (self._url, self._domain, self._project, entity_type)
        log.debug('create_entity: %s' % qurl)
        log.debug(parseString(body).toprettyxml())

        headers = self._headers
        headers['Content-Type'] = 'application/xml'
        retry = 1
        while retry <= 10:
            try:
                res = self.session.post(qurl, data=body, headers=headers)
                if res.status_code != 201:
                    raise Exception('Failed to create %s - code=%s message=%s' %
                                    (entity_type, res.status_code, res.text))
                break
            except requests.exceptions.SSLError as ex:
                log.warn("Exception while attempting to create entity: {0}.  Retry {1}".format(ex.message, retry))
                self.connect()

        return Entity.from_xml(res.text)

    def update_entity(self, entity_type, entity):
        """
        update_entity calls a put with the updated entity object.
        Parameters
            entity_type: the entity type
            entity: the entity object
        Returns
            The updated entity
        """
        # remove invalid fields
        for field in self._invalid_run_fields:
            if field in entity.fields:
                entity.fields.pop(field)

        qurl = '%s/qcbin/rest/domains/%s/projects/%s/%s/%s' % \
            (self._url, self._domain, self._project, entity_type, entity.fields['id'])
        log.debug('update_entity: %s' % qurl)
        body = entity.to_xml()
        log.debug(parseString(body).toprettyxml())
        try:
            headers = self._headers
            headers['Content-Type'] = 'application/xml'
            res = self.session.put(qurl, data=body, headers=headers)
            log.debug(res.text)
        except Exception as ex:
            log.warn("Failure while updating entity.")
            log.warn(ex.message)

        if res.status_code != 200:
            raise Exception('Failed to update entity - code=%s message=%s' %
                            (res.status_code, res.text))
        return self.get_entity(entity_type, query='id[=%s]' % entity.fields['id'])[0]

    def delete_entity(self, entity_type, entity):
        """
        Name
            delete_entity
        Description
            Delete an entity in ALM
        Parameters
            entity_type: the type
            entity: the entity reference
        Returns
        """
        eid = entity.fields['id']
        qurl = '%s/qcbin/rest/domains/%s/projects/%s/%s/%s' % \
            (self._url, self._domain, self._project, entity_type, eid)
        log.debug('delete_entity: %s' % qurl)
        res = self.session.delete(qurl, headers=self._headers)
        if res.status_code != 201:
            raise Exception('Failed to delete entity - code=%s message=%s' %
                            (res.status_code, res.text))

    def create_folder(self, ftype, path):
        """
        Name
            create_folder
        Description
            create a folder corresponding with the entity path
        Parameters
            ftype: the entity type
            path: the path to the folder
        Returns
            an entity
        """
        path = self.normalize_path(path)
        tok = path.split('\\')
        cur_path = ""
        parent_id = 0
        for fld in tok:
            cur_path = join(cur_path, fld)
            cur_folder = self.get_folder(ftype, cur_path)
            if cur_folder is not None:
                parent_id = cur_folder.fields['id']
            else:
                ft = EntityType.TESTPLANFOLDER if ftype == EntityType.TESTPLANFOLDERS else EntityType.TESTLABFOLDER
                ent = Entity(ft)
                ent.fields['parent-id'] = parent_id
                ent.fields['name'] = fld
                log.info('Creating "{0} - parentId={1}"'.format(cur_path, parent_id))
                cur_folder = self.create_entity(ftype, ent)
                parent_id = cur_folder.fields['id']

        return cur_folder

    def create_test_plan_folder(self, path):
        log.info('Creating test plan folder "{0}"'.format(path))
        path = self.normalize_path(path)
        if not path.startswith('Subject'):
            path = join('Subject', path)
        return self.create_folder(EntityType.TESTPLANFOLDERS, path)

    def create_test_lab_folder(self, path):
        log.info('Creating test lab folder "{0}"'.format(path))
        path = self.normalize_path(path)
        return self.create_folder(EntityType.TESTLABFOLDERS, path)

    def get_folder(self, ftype, path):
        """
        Name
            get_folder
        Description
            Retrieve a folder corresponding with the entity path
        Parameters
            type: the entity type
            path: the path to the folder
        Returns
            an entity
        """
        path = self.normalize_path(path)
        tok = path.split('\\')
        cur_path = ""
        parent_id = 0
        for fld in tok:
            cur_path += fld
            query = "parent-id[%s];name['%s']" % (parent_id, quote_plus(fld))
            e = self.get_entity(ftype, query)
            if len(e) == 0:
                return None
            parent_id = e[0].fields['id']
        return e[0]

    def get_test_plan_folder(self, path):
        """
        Name
            get_test_plan_folder
        Description
            Get a test plan folder
        Parameters
            path: The ALM path to the folder
        Returns
            entity
        """
        log.info('Getting test plan folder "%s"' % path)
        path = self.normalize_path(path)
        if not path.startswith('Subject'):
            path = join('Subject', path)
        return self.get_folder(EntityType.TESTPLANFOLDERS, path)

    def get_test_lab_folder(self, path):
        """
        Name
            get_test_lab_folder
        Description
            Get the test lab folder
        Parameters
            path: The ALM path to the folder
        Returns
            entity
        """
        log.info('Getting test lab folder "%s"' % path)
        return self.get_folder(EntityType.TESTLABFOLDERS, path)

    def get_test_set(self, path):
        """
        Name
            get_test_set
        Description
            Get a test set entity
        Parameters
            path: The ALM path to the test set (inclusive)
        Returns
            test set entity
        """
        path = self.normalize_path(path)
        log.info('Getting test set "%s"' % path)
        folder = path[:path.rindex(self.PATH_SEPARATOR)]
        test_set = path[path.rindex(self.PATH_SEPARATOR) + 1:]
        test_lab_folder = self.get_test_lab_folder(folder)
        if test_lab_folder is None:
            return None
        query = "parent-id[%s];name['%s']" % (test_lab_folder.fields['id'],
                                              test_set)
        testset = self.get_entity(EntityType.TESTSETS, query)
        if len(testset) == 0:
            return None
        return testset[0]

    def get_test(self, path):
        """
        Name
            get_test
        Description
            Get a test entity
        Parameters
            path: The ALM path to the test (inclusive)
        Returns
            test entity
        """
        log.info('Getting test "%s"' % path)
        folder = path[:path.rindex(self.PATH_SEPARATOR)]
        test_set = path[path.rindex(self.PATH_SEPARATOR) + 1:]
        tpf = self.get_test_plan_folder(folder)
        if tpf is None:
            raise EntityError("Test plan folder '{0}' does not exist.".format(folder))
        query = "parent-id[%s];name['%s']" % (tpf.fields['id'], test_set)
        tests = self.get_entity(EntityType.TESTS, query)
        return tests

    def create_test(self, test_plan_folder_path, name):
        """
        Name
            create_test
        Description
            Creates a test in ALM with the supplied path and entity
        Parameters
            test_plan_folder_path: The path
            test_entity: the test entity
        Returns
        """
        log.info('Creating test "%s"' % join(test_plan_folder_path, name))
        tpf = self.get_test_plan_folder(test_plan_folder_path)
        if tpf is None:
            raise Exception('Failed to find test plan folder "%s"' % test_plan_folder_path)
        test_entity = Entity(EntityType.TEST)
        test_entity.fields['name'] = name
        if 'user-template-01' in test_entity.fields:
            test_entity.fields['user-template-01'] = 'HP'
        test_entity.fields['subtype-id'] = 'VAPI-XP-TEST'
        test_entity.fields['parent-id'] = tpf.fields['id']
        return self.create_entity(EntityType.TESTS, test_entity)

    def get_test_design_steps(self, test):
        """
        Name
            get_test_design_steps
        Description
            Get a list of design steps
        Parameters
            test:             the test entity or path
        Returns
            List of entity
        """
        # if a path was passed, get the test
        if isinstance(test, str):
            test = self.get_test(test)
        return self.get_entity(EntityType.DESIGNSTEPS, query="parent-id[%s]" % test.fields['id'])

    def create_test_design_step(self, test, name, description='', expected_result='', order=None):
        """
        Name
            create_test_design_step
        Description
            Create a design step
        Parameters
            test:             the test entity or path
            name:             the test design step name
            description:     (Optional) The test design description
            expected_result: (Optional) The expected result
            order:           (Optional) The step order (defaults to last)
        Returns
            entity
        """
        # if a path was passed, get the test
        if isinstance(test, str):
            test = self.get_test(test)

        design_step = Entity(EntityType.DESIGNSTEP)
        design_step.fields['parent-id'] = test.fields['id']
        design_step.fields['name'] = name
        design_step.fields['description'] = description
        design_step.fields['expected'] = expected_result
        if order is not None:
            design_step.fields['order'] = order
        return self.create_entity(EntityType.DESIGNSTEPS, design_step)

    def get_test_config(self, test, name=None):
        """
        Name
            get_test_config
        Description
            get a test config
        Parameters
            test: the test entity
            name: (optional) the test name
        Returns
            entity
        """
        log.info('Getting test config "%s"' % test.fields['name'])
        query = 'parent-id[%s]' % test.fields['id']
        if name is not None:
            query += ";name[='%s']" % name
        ent = self.get_entity('test-configs', query)
        if len(ent) == 0:
            return None
        else:
            return ent[0]

    def create_test_set(self, path, description=''):
        """
        Name
            create_test_set
        Description
            Create a test set
        Parameters
            folder: The path to the test set
            name: The test set name
            description: (optional) the description
        Returns
            entity
        """
        log.info('Creating test set "%s"' % path)
        path = self.normalize_path(path)
        folder = path[:path.rindex(self.PATH_SEPARATOR)]
        name = path[path.rindex(self.PATH_SEPARATOR) + 1:]
        test_lab_folder = self.get_test_lab_folder(folder)
        if test_lab_folder is None:
            raise EntityError("Failed to find test lab folder '" + folder + "'")
        test_set = Entity(EntityType.TESTSET)
        test_set.fields['name'] = name
        test_set.fields['description'] = description
        if 'user-template-01' in test_set.fields:
            test_set.fields['user-template-01'] = 'HP'
        test_set.fields['subtype-id'] = 'hp.qc.test-set.default'
        test_set.fields['parent-id'] = test_lab_folder.fields['id']
        return self.create_entity(EntityType.TESTSETS, test_set)

    def get_test_instance(self, test_set, test=None):
        """
        Name
            get_test_instance
        Description
            Get a test instance entity
        Parameters
            test_set: a test set entity
            test: a test entity
        Returns
            entity
        """
        if test is None:
            query = 'cycle-id[%s]' % test_set.fields['id']
        else:
            log.info('Getting test instance "%s"' % test.fields['name'])
            query = 'cycle-id[%s];test-id[%s]' % (test_set.fields['id'],
                                                  test.fields['id'])
        return self.get_entity(EntityType.TESTINSTANCES, query)

    def create_test_instance(self, test_set, test, test_config=None, order=None):
        """
        Name
            create_test_instance
        Description
            Creates a test instance
        Parameters
            test_set: the test set entity
            test: the test entity
            test_config: (optional) the test config entity
            order: (optional) the test instance order
        Returns
            The test instance entity
        """
        log.info('Creating test instance "%s"' % test.fields['name'])
        if order is None:
            order = len(self.get_test_instance(test_set, test)) + 1
        test_instance = Entity(EntityType.TESTINSTANCE)
        test_instance.fields['cycle-id'] = test_set.fields['id']
        test_instance.fields['test-id'] = test.fields['id']
        test_instance.fields['test-config-id'] = \
            self.get_test_config(test).fields['id']
        test_instance.fields['test-order'] = order
        test_instance.fields['subtype-id'] = 'hp.qc.test-instance.MANUAL'
        return self.create_entity(EntityType.TESTINSTANCES, test_instance)

    def get_run(self, test_instance, name=None, query=None):
        """
        Name
            get_run
        Description
            Get a list of run  entities
        Parameters
            test_instance: the test instance entity
            name: (optional) the name
        Returns
            Entity
        """
        q = "test-instance.id['%s']" % test_instance.fields['id']
        if name is not None:
            q += ";name[='%s']" % name
        if query is not None:
            q += ";%s" % query
        return self.get_entity('runs', q)

    def create_run(self, test_instance, name=None):
        """
        Name
            create_run
        Description
            Create a new run
        Parameters
            test_instance: the test instance entity
            name: (optional) the run name (defaults to date/time)
        Returns
            Entity
        """
        log.info('Creating run')
        if name is None:
            name = datetime.now().strftime('Run_%Y%m%d_%H%M%S')
        run = Entity(EntityType.RUN)
        run.fields['name'] = name
        run.fields['test-id'] = test_instance.fields['test-id']
        run.fields['cycle-id'] = test_instance.fields['cycle-id']
        run.fields['testcycl-id'] = test_instance.fields['id']
        run.fields['status'] = 'No Run'
        run.fields['subtype-id'] = 'hp.qc.run.MANUAL'
        run.fields['owner'] = self._username
        return self.create_entity(EntityType.RUNS, run)

    def delete_run(self, run):
        """
        Name
            delete_run
        Description
            Delete a run
        Parameters
            run: The run Entity
        Returns
        """
        log.info("Deleting run")
        self.delete_entity(EntityType.RUNS, run)

    def get_run_steps(self, run_id):
        """
        Name
            get_run_steps
        Description
            Retrieve the steps for a run
        Parameters
            run_id: The ALM ID of the run
        Returns
            List of Entities
        """
        qurl = '%s/qcbin/rest/domains/%s/projects/%s/runs/%s/run-steps?alt=application/json&page-size=max' % \
            (self._url, self._domain, self._project, run_id)
        result = self.session.get(qurl, headers=self._headers)
        entities = [x for x in result.json()['entities'] if len(x['Fields']) > 1]   # apparent bug in json method returns an extra element
        element_list = []
        for ent in entities:
            log.debug("Working on {0} of {1}".format(len(element_list), len(entities)))
            el = Entity.from_json(ent)
            element_list.append(el)

        return element_list

    def create_run_step(self, run, name, description='', expected_result='', order=None, status=RunStatus.NORUN, execution_date=None, execution_time=None):
        """
        Name
            create_run_step
        Description
            Create a run step
        Parameters
            test:             the test entity or path
            name:             the test design step name
            description:     (Optional) The test design description
            expected_result: (Optional) The expected result
            order:           (Optional) The step order (defaults to last)
        Returns
            entity
        """
        # if a path was passed, get the test
        if not isinstance(run, Entity):
            raise EntityError("Run is not an entity")

        run_step = Entity(EntityType.RUNSTEP)
        run_step.fields['parent-id'] = run.fields['id']
        run_step.fields['name'] = name
        run_step.fields['description'] = description
        run_step.fields['expected'] = expected_result
        run_step.fields['execution-date'] = execution_date
        run_step.fields['execution-time'] = execution_time
        if status is not None:
            run_step.fields['status'] = status
        if order is not None:
            run_step.fields['order'] = order
        return self.create_entity("/runs/{0}/".format(run.fields['id']), entity=run_step, collection=EntityType.RUNSTEPS)

    def upload_attachment(self, entity_type, eid, file_name):
        """
        Name
            upload_attachment
        Description
            Uploads an attachment to the supplied entity
        Parameters
            entity_type: the entity type enum
            id: the integer id of the entity
            file_name: the name of the file in the local filesystem
        Returns
        """
        log.info('Uploading attachment to %s id=%s' % (entity_type, eid))
        with open(file_name, 'rb') as fin:
            bin_data = fin.read()
        qurl = '%s/qcbin/rest/domains/%s/projects/%s/%s/%s/attachments' % \
            (self._url, self._domain, self._project, entity_type, eid)
        log.info('upload_attachment: %s' % qurl)
        headers = self._headers
        headers['Content-Type'] = 'multipart/form-data; boundary=uploadboundary'
        body = '''--uploadboundary
Content-Disposition: form-data; name="filename"

%s
--uploadboundary
Content-Disposition: form-data; name="file"; filename="%s"

%s
--uploadboundary--''' % (file_name, file_name, bin_data)
        log.debug('headers:{0}'.format(headers))
        # log.debug('body:{0}'.format(body))
        rsp = self.session.post(qurl, data=body, headers=headers)
        if rsp.status_code != 201:
            raise Exception('Failed to upload %s - code=%s message=%s' %
                            (file_name, rsp.status_code, rsp.text))

    def get_attachments(self, entity_type, eid):
        """
        Name
            get_attachments
        Description
            get all of the attachments for the supplied entity
        Parameters
            entity_type: the entity type enum
            id: the entity ID
        Returns
            Entity list
        """
        return self.get_entity(entity_type + '/' + str(eid) + '/attachments')

    def download_attachment(self, entity_type, eid, file_name, local_file_name):
        """
        Name
            download_attachment
        Description
            download an attachment
        Parameters
            entity_type: the entity type enum
            id: the entity ID
            file_name: the name of the attachment in ALM
            local_file_name: the name of the file in the local filesystem
        Returns
        """
        qurl = '%s/qcbin/rest/domains/%s/projects/%s/%s/%s/attachments/%s' % \
            (self._url, self._domain, self._project, entity_type, id, file_name)
        log.info('download_attachment: %s' % qurl)
        res = self.session.get(qurl)
        if res.status_code != 200:
            raise Exception('Failed to download attachment - code=%s message=%s' %
                            (res.status_code, res.text))
        with open(local_file_name, 'wb') as fout:
            fout.write(res.text)

    def set_test_set_field(self, test_set_path, fields):
        """
            Set the text for a particular field in a test set
        """
        # locate the test set
        test_set = self.get_test_set(test_set_path)
        if test_set is None:
            raise 'Failed to locate test set "%s"' % (test_set_path)

        for field_name, text in fields:
            log.info('Updating {0}'.format(field_name))
            _text = text
            # is the text a path to a file?
            if exists(text):
                log.info('Opening {0}'.format(text))
                with open(text, 'r') as fin:
                    _text = escape(fin.read())

            log.info('Updated {0} {1}'.format(test_set_path, field_name))

            # set the field and update the entity
            test_set.fields[field_name] = _text
        ent = self.update_entity(EntityType.TESTSETS, test_set)

        return ent


ALM = 'https://qc4f.austin.hpecorp.net:8443'


log = logging.getLogger('post_robot')
logging.basicConfig(format='%(asctime)-15s,%(levelname)s,%(name)s,%(message)s')
log.setLevel(logging.INFO)


class ElementType(object):
    SUITE = 'suite'
    TEST = 'test'


class RobotTest(object):

    def __init__(self, element, suite, path, metadata):
        rep = re.compile(":")
        self.suite = rep.sub(' ', suite).strip()
        self.path = rep.sub(' ', path).strip()
        self.id = element.attrib['id'].strip()
        self.name = rep.sub(' ', element.attrib['name']).strip()
        self.metadata = metadata
        try:
            self.doc = element.find('doc').text
        except:
            self.doc = ""
        status = element.find('status')
        self.status = str(status.attrib['status'])
        self.starttime = parse(status.attrib['starttime'])
        self.endtime = parse(status.attrib['endtime'])
        self.date = self.starttime.strftime('%Y-%m-%d')
        self.time = self.starttime.strftime('%H:%M:%S')
        self.duration = (self.endtime - self.starttime).total_seconds()

    def __repr__(self):
        return self.name


def get_tests(element):
    suite_name = element.attrib['name'].encode()
    path = element.attrib['source'].encode() if 'source' in element.attrib else '\\'
    path = path[:path.rindex("\\") + 1]
    log.info(path)
    ret = []
    root = element
    suites = element.findall('./suite')

    # a suite with a single test will yield no child suites.  In this case, we use the root element as the list.
    if len(suites) == 0:
        suites = [root]

    # now, iterate through the suites/tests and construct the data structure
    for suite in suites:
        log.info("{0} {1}".format(suite.attrib['id'], suite.attrib['name']))

        # find the metadata
        suite_metadata = {}
        for meta in suite.findall('.//metadata'):
            for item in meta.findall('item'):
                suite_metadata[item.attrib['name']] = item.text

        for test in suite.findall('.//test'):
            log.info("\t{0} - {1}".format(test.attrib['id'], test.attrib['name']))
            ret.append(RobotTest(test,
                                 suite.attrib['name'].encode().replace(suite_name, ""),
                                 suite.attrib['source'].encode().replace(path, "").strip('.txt'),
                                 suite_metadata))
    return ret


def scrub(txt):
    regex = re.compile("\s+")
    return regex.sub(' ', txt.replace('&', ' and '))


def main():  # pylint: disable=R0914,R0912
    """ Main entry point """

    err = False
    test_set_path = ''
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-u', '--username', help='ALM username', required=True)
    parser.add_argument('-p', '--password', help='ALM password', required=True)
    parser.add_argument('--server', help='Optional ALM server url.  Example: https://server_url:port    Default is "https://qc4f.austin.hp.com:8443"', required=False, default=ALM)
    parser.add_argument('-d', '--domain', help='ALM domain.  Example: TSG_ESSN', required=True)
    parser.add_argument('-pr', '--project', help='ALM project.  Example: Cosmos', required=True)
    parser.add_argument('-l', '--testlabpath', help='test lab path.  Example: Sandbox\test', required=True)
    parser.add_argument('-t', '--testplanpath', help='test plan path.  Example: Sandbox\tests', required=True)
    parser.add_argument('-ts', '--testset', help='the name of the test set', required=False)
    parser.add_argument('-r', '--runname', help='the name of the run', required=False)
    parser.add_argument('-e', '--environment', help='environment details (text or filename) - can be HTML', default=None)
    parser.add_argument('xmlfile', metavar='path\\output.xml', type=str, nargs='+', help='The Robot Framework output.xml file.  This can be located anywhere, named differently, and you can pass in multiple files.')

    args = parser.parse_args()

    for xfile in args.xmlfile:
        if not xfile.startswith("http") and not exists(xfile):
            sys.stderr.write("ERROR: Failed to find %s\n" % xfile)
            err = True

    if err:
        sys.exit(1)

    alm = Alm(args.server, args.domain, args.project, args.username, args.password)

    if args.testplanpath is None:
        args.testplanpath = r"Cosmos test Cases\General Release\Automation"

    log.info('ALM test plan path: %s' % args.testplanpath)
    log.info('ALM test lab path:  %s' % args.testlabpath)

    tpf = alm.get_test_plan_folder(args.testplanpath)
    if tpf is None:
        raise IOError("Failed to find test plan path: %s" % args.testplanpath)
    try:
        tlf = alm.get_test_lab_folder(args.testlabpath)
    except:
        raise IOError("Failed to get Test Lab Folder: %s" % args.testlabpath)
    if tlf is None:
        raise Exception("Failed to find test lab path: %s" % args.testlabpath)

    for xfile in args.xmlfile:
        log.info("Reading %s" % xfile)
        tree = ET.parse(xfile)
        root = tree.getroot().find('suite')
        suite_name = root.attrib['name']
        suite_status = "Passed" if root.find('status').attrib['status'] == "PASS" else "Failed"
        suite_start_date = parse(root.find('status').attrib['starttime']).date()
        suite_start_time = parse(root.find('status').attrib['starttime']).strftime("%H:%M:%S")
        tests = get_tests(root)
        metadata = {}
        for meta in root.findall('.//metadata'):
            for item in meta.findall('item'):
                metadata[item.attrib['name']] = item.text

        # get or create the test lab folder
        test_plan_folder = join(args.testplanpath, suite_name)
        tpf = alm.get_test_plan_folder(test_plan_folder)
        if tpf is None:
            tpf = alm.create_test_plan_folder(test_plan_folder)

        # get or create the test set
        if args.testset is not None:
            test_set_path = join(args.testlabpath, args.testset)
        else:
            test_set_path = join(args.testlabpath, suite_name)
        test_set = alm.get_test_set(test_set_path)
        if test_set is None:
            test_set = alm.create_test_set(test_set_path)

        # create the test
        test_path = join(test_plan_folder, suite_name)
        test = alm.get_test(test_path)
        if len(test) == 0:
            test = alm.create_test(test_plan_folder, suite_name)
        else:
            test = test[0]

        # get or create the test instance
        test_instance = alm.get_test_instance(test_set, test)
        if len(test_instance) == 0:
            test_instance = alm.create_test_instance(test_set, test)
        if isinstance(test_instance, list):
            test_instance = test_instance[0]

        # create run - if no name was specified, default to the execution date/time
        if args.runname is None:
            run_name = "Run {0} {1}".format(suite_start_date.strftime("%Y-%m-%d"), suite_start_time)
        else:
            run_name = args.runname
        start_date = tests[0].date
        start_time = tests[0].time
        duration = sum([t.duration for t in tests])
        run_path = args.testlabpath + "\\" + test.fields['name'] + "\\" + run_name
        run = alm.get_run(test_instance, run_name, query="execution-date[='%s'];execution-time[='%s']" % (start_date, start_time))
        if len(run) != 0:
            log.warn("Test run '%s' exists with date %s %s.  Skipping." % (run_path, start_date, start_time))
            continue

        alm_run = Entity(EntityType.RUN)
        log.info("Creating run '%s'" % run_path)
        alm_run.fields['name'] = run_name
        alm_run.fields['owner'] = args.username
        alm_run.fields['test-id'] = test.fields['id']
        alm_run.fields['testcycl-id'] = test_instance.fields['id']
        alm_run.fields['cycle-id'] = test_set.fields['id']
        alm_run.fields['duration'] = int(duration)

        # set the browser and OS info
        if "Browser Name" in metadata:
            alm_run.fields[FieldType.BROWSER] = metadata["Browser Name"]
        if "Browser Version" in metadata:
            alm_run.fields[FieldType.BROWSER] += " %s" % (metadata["Browser Version"])
        if "OS Release" in metadata:
            alm_run.fields['os-name'] = metadata["OS Release"]
        if "OS Version" in metadata:
            alm_run.fields['os-build'] = metadata["OS Version"]
        if "Host" in metadata:
            alm_run.fields['host'] = metadata["Host"]
        alm_run.fields['subtype-id'] = 'hp.qc.run.MANUAL'
        alm_run = alm.create_entity(EntityType.RUNS, alm_run)
        alm_run.fields['status'] = suite_status
        alm_run = alm.update_entity(EntityType.RUNS, alm_run)
        # set the date/time again because it gets reset to current date/time
        alm_run.fields['execution-date'] = start_date
        alm_run.fields['execution-time'] = start_time
        alm_run = alm.update_entity(EntityType.RUNS, alm_run)

        # create steps
        # iterate through the suite tests
        for rf_test in tests:
            rf_test.name = scrub(rf_test.name)
            log.info("Creating run step: {0}".format(rf_test.name))
            if rf_test.name == "":
                continue
            # create the run step
            status = StepStatus.PASSED if rf_test.status == "PASS" else StepStatus.FAILED
            alm.create_run_step(alm_run, rf_test.name, description=rf_test.doc, status=status, execution_date=rf_test.date, execution_time=rf_test.time)

        # set the date and time for the test instance
        test_instance = alm.get_test_instance(test_set, test)[0]
        test_instance.fields['exec-date'] = suite_start_date
        test_instance.fields['exec-time'] = suite_start_time
        alm.update_entity(EntityType.TESTINSTANCES, test_instance)
    log.info("Done.")


if __name__ == '__main__':
    main()
