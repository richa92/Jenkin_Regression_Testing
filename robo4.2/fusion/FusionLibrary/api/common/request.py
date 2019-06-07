#!/usr/local/bin/python
"""
request.py
This module uses the requests module and provides the HttpVerbs class that has
methods to perform CRUD operations to a ReST interface

#############################################################################
The information contained herein is subject to change without notice.
The only warranties for HP products and services are set forth in the
express warranty statements accompanying such products and services.
Nothing herein should be construed as constituting an additional warranty.
HPE shall not be liable for technical or editorial errors or omissions
contained herein.

(C) Copyright 2019 Hewlett Packard Enterprise Development Company, L.P.
#############################################################################
"""
import json
import logging
from operator import itemgetter
import os
import re
import requests
from requests.adapters import HTTPAdapter
from requests.packages import urllib3
from requests_toolbelt import MultipartEncoder
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.libraries.BuiltIn import BuiltIn
import time
libLogger = "api-logger"


class HttpVerbs(object):
    """
    Wrapper object around HTTP verbs
    """
    def __init__(self):
        """
        Initialization method
        """
        urllib3.disable_warnings()
        self._http = requests.Session()

        # requires Python 2.7.4+ and Requests 1.2.3 +
        self._http.mount('http://', HTTPAdapter(max_retries=3))
        self._http.mount('https://', HTTPAdapter(max_retries=3))

        self._sessionID = None
        self._cred = None
        self._headers = {'Accept': 'application/json, */*',
                         'Accept-language': 'en_US',
                         'Content-Type': 'application/json'}
        self._host = ""
        self._active_sessions = {}
        self._last_request = None   # store the last request\response object

    def suppress_urllib3_warnings(self):
        """
        Method that sets the warning level in urllib3 library
        :return:
        """
        logging.getLogger("urllib3").setLevel(logging.ERROR)

    def _set_req_api_version(self, api=None):
        """
        Method to insert X-API-VERSION in the HTTP Headers
        :param api:
        :return:
        """
        headers = self._headers.copy()
        if api:
            headers['X-Api-Version'] = str(api)
        return headers

    def set_def_api_version(self, api=None):
        """
        Method that defines the X-API-VERSION based on user - input or the
        latest supported version in OneView
        :param api:
        :return:
        """
        if not api:
            try:   # allows non-RG uses of FusionLibrary
                if BuiltIn().get_variable_value("${X-API-VERSION}") is not None:
                    api = str(BuiltIn().get_variable_value("${X-API-VERSION}"))
                else:
                    api = self._currentVersion()
            except:
                api = self._currentVersion()

        self._headers['X-Api-Version'] = str(api)
        return self._headers

    def _validateVersion(self, api_version):
        """
        Method to perform X-API-Version validation
        :param api_version:
        :return:
        """
        uri = 'https://{}/rest/version'.format(self._host)
        resp = self._http.get(uri, verify=False)
        version = resp.json()

        if 'minimumVersion' in version:
            if api_version < version['minimumVersion']:
                raise Exception('Unsupported API Version')

        if 'currentVersion' in version:
            if api_version > version['currentVersion']:
                raise Exception('Unsupported API Version')

    def _currentVersion(self):
        """
        Configures the X-API-Version to the supported version
        :return:
        """
        uri = 'https://{}/rest/version'.format(self._host)
        headers = self._headers
        version = self.get(uri, headers=headers)

        if 'currentVersion' in version:
            return str(version['currentVersion'])

    def _json(self, body):
        """
        Customized JSON decoder
        :param body:
        :return:
        """
        if body:
            if isinstance(body, dict):
                try:
                    body = json.dumps(body)
                except Exception as e:
                    msg = "Exception occurred converting dict to json"
                    raise Exception(msg, e)
            elif isinstance(body, str):
                try:
                    body = json.loads(body)
                except Exception as e:
                    msg = "Exception occurred converting str to json"
                    raise Exception(msg, e)
            else:
                _ = "Unsupported request body type: {}.".format(type(body))
                _ += " Must be str or dict"
                raise Exception(_)
        return body

    def _log_request(self, uri, op, headers, body=None):
        """
        Method to log debug information about request
        :param uri: URI - URL passed to the HTTP verb
        :param op: PATCH | PUT | DELETE | GET | POST
        :param headers: Headers passed to the function
        :param body: Payload
        :return: None
        """
        log = logging.getLogger(libLogger)
        log.debug('URI\t {} {}'.format(op, uri))
        log.debug('Request Headers {}\nHTTP Headers {}'.format(
            json.dumps(headers, sort_keys=True, indent=4,
                       separators=(',', ': ')),
            json.dumps(self._http.headers._store, sort_keys=True, indent=4,
                       separators=(',', ': '))))
        if body:
            log.debug('Body\n{}'.format(
                json.dumps(json.loads(body), sort_keys=True, indent=4,
                           separators=(',', ': '))))

    @staticmethod
    def _return_response_dict(resp):
        """
        Method to log the received response object information
        :param resp: Response Object
        :return: DICT
        """
        log = logging.getLogger(libLogger)
        log.debug('Status {}\nResponse Headers {}'.format(
            resp.status_code, json.dumps(dict(**resp.headers), sort_keys=True,
                                         indent=4, separators=(',', ': '))))
        r = dict({'status_code': resp.status_code, 'headers': resp.headers})
        if resp.content:
            try:
                if isinstance(resp.json(), dict):
                    log.debug('Response Body {}'.format(
                        json.dumps(resp.json(), sort_keys=True, indent=4,
                                   separators=(',', ': '))))
                    r.update(resp.json())
            except ValueError:
                log.debug('Ignore: Encountered a value error')
                log.debug('Raw content:\n {}'.format(resp.text))
                pass

        return r

    # ##########################################################################
    # HTTP verbs
    # ##########################################################################

    def delete(self, uri, headers=None):
        """
        Wrapper around the HTTP verb DELETE
        :param uri:
        :param headers:
        :return:
        """
        if not headers:
            headers = self._headers

        try:
            self._log_request(uri, 'DELETE', headers)
            resp = self._http.delete(uri, headers=headers, verify=False)
            self._last_request = resp
        except Exception as e:
            m = "Exception occurred while attempting to DELETE: {}".format(uri)
            raise Exception(m, e)

        return self._return_response_dict(resp)

    def get(self, uri, headers=None):
        """
        Wrapper around the HTTP verb GET
        :param uri:
        :param headers:
        :return:
        """
        # This method automatically gets ALL resources. Use a filter if less are
        # desired
        if not headers:
            headers = self._headers

        x = 0
        response = dict()
        lastreq_list = list()
        while True:
            try:
                self._log_request(uri, 'GET', headers)
                r = self._http.get(uri, headers=headers, verify=False)
                lastreq_list.append(r)
                self._last_request = lastreq_list

                resp = r.json()
                self._return_response_dict(r)
                if isinstance(resp, dict):
                    if 'nextPageUri' in resp:
                        if x == 0:
                            response = r.json()
                            response['headers'] = headers
                            response['status_code'] = r.status_code
                        else:
                            # add members
                            response['members'] += resp['members']
                        x += 1
                        if resp['nextPageUri']:
                            next_page = resp['nextPageUri']
                            uri = 'https://%s%s' % (self._host, next_page)
                        else:
                            response['count'] = response['total']
                            break
                    else:
                        response = resp
                        response['headers'] = headers
                        response['status_code'] = r.status_code
                        break
                else:
                    response = r.__dict__
                    break

            except Exception as e:
                logger.info(r.content)
                msg = "Exception occurred while attempting to GET: %s" % uri
                raise Exception(msg, e)

        return response

    def patch(self, uri, headers=None, body=None):
        """
        Wrapper around the HTTP PATCH verb
        :param uri:
        :param headers:
        :param body:
        :return:
        """
        if not headers:
            headers = self._headers
        try:
            self._log_request(uri, 'PATCH', headers, body)
            resp = self._http.patch(uri, data=body, headers=headers,
                                    verify=False)
            self._last_request = resp
            return self._return_response_dict(resp)
        except Exception as e:
            msg = "Exception occurred while attempting to PATCH: %s" % uri
            raise Exception(msg, e)

    def put(self, uri, headers=None, body=None):
        """
        Wrapper around the HTTP PUT verb
        :param uri:
        :param headers:
        :param body:
        :return:
        """
        if not headers:
            headers = self._headers
        try:
            self._log_request(uri, 'PUT', headers, body)
            resp = self._http.put(uri, data=body, headers=headers, verify=False)
            self._last_request = resp
            return self._return_response_dict(resp)
        except Exception as e:
            msg = "Exception occurred while attempting to PUT: %s" % uri
            raise Exception(msg, e)

    def post(self, uri, headers=None, body=None, cert=None):
        """
        Wrapper around HTTP POST verb
        :param uri:
        :param headers:
        :param body:
        :param cert:
        :return:
        """
        if not headers:
            headers = self._headers

        try:
            self._log_request(uri, 'POST', headers, body)
            resp = self._http.post(uri, data=body, headers=headers,
                                   verify=False, cert=cert)
            self._last_request = resp
            return self._return_response_dict(resp)
        except Exception as e:
            msg = "Exception occurred while attempting to POST: %s" % uri
            raise Exception(msg, e)

    def get_file(self, uri, localfile, headers=None, chunk_size=1024):
        """
        Wrapper for retrieving a file
        :param uri:
        :param localfile:
        :param headers:
        :param chunk_size:
        :return:
        """
        try:
            self._log_request(uri, 'GET FILE', headers)
            resp = self._http.get(uri, headers=headers, stream=True,
                                  verify=False)
            self._last_request = resp

            with open(localfile, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
            return resp.__dict__

        except Exception as e:
            msg = "Exception occurred while attempting to GET FILE: %s" % uri
            raise Exception(msg, e)

    def put_file(self, uri, localfile, headers=None,
                 f_type='application/pkix-crl'):
        """
        Wrapper for uploading a file
        :param uri:
        :param localfile:
        :param headers:
        :param f_type:
        :return:
        """
        filename = os.path.split(localfile)
        filename = filename[1]
        files = MultipartEncoder(fields={'file': (filename,
                                                  open(localfile, 'rb'),
                                                  f_type)})
        headers['Content-Type'] = files.content_type

        try:
            self._log_request(uri, 'PUT FILE', headers)
            resp = self._http.put(uri, headers=headers, data=files,
                                  verify=False)
            self._last_request = resp
            return self._return_response_dict(resp)
        except Exception as e:
            msg = "Exception occurred while attempting to PUT FILE: %s" % uri
            raise Exception(msg, e)

    def post_file(self, uri, localfile, headers=None,
                  f_type='application/octet-stream'):
        """
        Wrapper for Posting a file
        :param uri:
        :param localfile:
        :param headers:
        :param f_type:
        :return:
        """
        # TODO:    handle multiple files
        filename = os.path.split(localfile)
        filename = filename[1]
        files = MultipartEncoder(fields={'file': (filename,
                                                  open(localfile, 'rb'),
                                                  f_type)})
        headers['Content-Type'] = files.content_type
        headers['uploadfilename'] = filename

        try:
            self._log_request(uri, 'POST FILE', headers)
            resp = self._http.post(uri, headers=headers, data=files,
                                   verify=False)
            self._last_request = resp
            return self._return_response_dict(resp)
        except Exception as e:
            msg = "Exception occurred while attempting to POST FILE: %s" % uri
            raise Exception(msg, e)

    # ##########################################################################
    # Tasks
    # ##########################################################################

    def wait4task(self, task, interval=2, tout=120, verbose=False):
        """
        Waits till all the task reached the desired state
        :param task:
        :param interval:
        :param tout:
        :param verbose:
        :return:
        """
        taskuri = task
        t = re.compile('(?i)Warning|Unknown|Terminated|Killed|Error|Completed')

        max_id = 0
        count = 0
        while True:
            uri = 'https://%s%s' % (self._host, taskuri)
            task = self.get(uri)
            resource = ""

            if 'associatedResource' in task:
                if task['associatedResource']['resourceUri']:
                    resource = "for: " + \
                               task['associatedResource']['resourceName']
            else:
                if 'associatedResourceUri' in task \
                        and task['associatedResourceUri']:
                    resource = "for: " + task['associatedResourceUri']

            if count == 0:
                if task['taskState'] != 'Completed':
                    if verbose:
                        logger.info('Task: {}:{} is {}\t{}'.format(
                            task['category'], task['name'],
                            task['taskState'].ljust(10), resource))

            for x in sorted(task['progressUpdates'], key=itemgetter('id')):
                if int(x['id']) > max_id:
                    if x['statusUpdate']:
                        if verbose:
                            logger.info("Task: {}:{} is {}\t{}".format(
                                task['category'], task['name'],
                                task['taskState'].ljust(10), x['statusUpdate']))
                    max_id = int(x['id'])

            if t.match(task['taskState']):
                if verbose:
                    logger.info('Task: {}:{} is {}\t{}'.format(
                        task['category'], task['name'],
                        task['taskState'].ljust(10), resource))
                break
            else:
                time.sleep(interval)

            count += interval

            if count > tout:
                m = 'Task timeout reached. Wiated {}'.format(tout)
                m += ' seconds for task to complete'
                raise Exception(m)
