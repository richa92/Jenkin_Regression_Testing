# #############################################################################
# RISClientDEA.py
# This module provides a wrapper for Requests HTTP Verbs, and additional functions for interface with RIS
#
# #############################################################################
# The information contained herein is subject to change without notice.
# The only warranties for HP products and services are set forth in the
# express warranty statements accompanying such products and services.
# Nothing herein should be construed as constituting an additional warranty.
# HP shall not be liable for technical or editorial errors or omissions
# contained herein.
#
# #############################################################################

import requests
from requests.packages import urllib3
from requests.adapters import HTTPAdapter
from RoboGalaxyLibrary.utilitylib import logging as logger
import pprint
import json


class PERISClient(object):

    def __init__(self, host=None, proxy=None, http=False):
        self._http = requests.Session()
        self._http.mount('http://', HTTPAdapter(max_retries=3))  # requires Python 2.7.4+ and Requests 1.2.3 +
        self._http.mount('https://', HTTPAdapter(max_retries=3))  # requires Python 2.7.4+ and Requests 1.2.3 +
        self._sessionID = None
        self._cred = None
        self._headers = {'Accept': 'application/json, */*',
                         'Accept-language': 'en_US',
                         'Content-Type': 'application/json'}
        self._host = host

        # leaving below here in case we need to test more than 1 active sessions
#         self._active_sessions = {}
#         self.session_uri = []

        self._session_uri = None
        self._session_index = None
        self._base_url = 'https://'
        if http:
            self._base_url = 'http://'
        if proxy:
            self._http.proxies = proxy
        else:
            self._http.proxies = None
            self._http.trust_env = False
        # Disable the one-time warning thrown by urllib3 when bypassing SSL cert
        urllib3.disable_warnings()

    def set_host(self, host):
        self._host = host

    def get_host(self):
        return self._host

    def get_user(self):
        if self._cred is not None:
            return self._cred['UserName']

    def get_password(self):
        if self._cred is not None:
            return self._cred['Password']

    def clear_token(self):
        self._sessionID = None
        self._headers['X-Auth-Token'] = self._sessionID

    def get_token(self):
        return self._sessionID

    def set_token(self, tokenID):
        self._sessionID = tokenID
        self._headers['X-Auth-Token'] = self._sessionID

    def update_headers(self, key, value):
        self._headers[key] = value

    def update_index(self, value):
        self._session_index = value

    def set_base_url(self, base_url):
        self._base_url = base_url + '://'

    def close_session(self):
        self._http.close()

    # leaving below here in case we need to test more than 1 active sessions
#     def get_active_sessions(self):
#         return self._active_sessions

    def _request(self, op, uri, headers=None, data=None, stream=False, etag=None, if_none_match=None, legacy=False, xauthtoken=None, username=None, password=None, timeout=180):
        if headers == "no_auth_token":
            headers = {'Accept': 'application/json, */*',
                       'Accept-language': 'en_US',
                       'Content-Type': 'application/json'}
        elif headers == "no_auth_token_with_secret":
            headers = {'Accept': 'application/json, */*',
                       'Accept-language': 'en_US',
                       'Content-Type': 'application/json',
                       'X-Secret': 'secret'}
        elif headers == "Staging":
            headers = {'Accept': 'application/json, */*',
                       'Accept-language': 'en_US',
                       'Content-Type': 'application/octet-stream',
                       'X-Stage-Only': 1}
            headers['X-Auth-Token'] = self._sessionID
        elif headers == "Dummy1":
            headers = {'Accept': 'application/json, */*',
                       'Accept-language': 'en_US',
                       'Content-Type': 'application/octet-stream',
                       'X-Dummy': 1}
            headers['X-Auth-Token'] = self._sessionID
        elif headers == "Dummy2":
            headers = {'Accept': 'application/json, */*',
                       'Accept-language': 'en_US',
                       'Content-Type': 'application/octet-stream',
                       'X-Dummy': 1,
                       'X-Stage-Only': 1}
            headers['X-Auth-Token'] = self._sessionID
        elif headers == "more_than_four_headers":
            headers = {'Accept': 'application/json, */*',
                       'Accept-language': 'en_US',
                       'Content-Type': 'application/octet-stream',
                       'X-Dummy1': 1,
                       'X-Stage-Only': 1,
                       'X-Dummy2': 1,
                       'X-Dummy3': 1,
                       'X-Dummy4': 1}
            headers['X-Auth-Token'] = self._sessionID
        elif headers == "long_headers":
            header_name = "X-Stage"
            padchar = 'A'
            current_length = len(header_name)
            if current_length < 1024:
                for i in range(1024 - current_length):
                    header_name = header_name + padchar
            headers = {'Accept': 'application/json, */*',
                       'Accept-language': 'en_US',
                       'Content-Type': 'application/octet-stream',
                       header_name: 1,
                       'X-Stage-Only': 1
                       }
            headers['X-Auth-Token'] = self._sessionID
        elif headers:
            headers['X-Auth-Token'] = self._sessionID
        else:
            headers = self._headers
        logger._debug('uri %s' % uri)
        logger._debug('base %s' % self._base_url)
        logger._debug('host %s' % self._host)
        uri = self._base_url + self._host + uri
        # Below check for legacy support of some existing calls made to HPCIManager which did not encode the data.
        if isinstance(data, dict):
            data = json.dumps(data)
        try:
            logger._debug('\n%s %s\nRequest Header: %s\nRequest Body: %s\n' % (op, uri, pprint.PrettyPrinter().pformat(headers), data))
            resp = self._http.request(op, uri, data=data, headers=headers, verify=False, stream=stream, timeout=timeout)
            logger._debug('\nStatus: %d' % resp.status_code)
            logger._debug('\nResp Header: %s' % resp.headers)
            # Below code for debugging purposes.  Won't work for calls to Diags since that returns raw text instead of json
            # TODO: add condition to check for call to Diags and print raw text instead of json
            # if resp.status_code == 200 and op == 'GET' and stream == False:
            #    logger._debug('\nBody: %s' % resp.json())
        except Exception as e:
            msg = "Exception occurred while attempting to %s: %s" % (op, uri)
            raise Exception(msg, e)
        return resp

    def delete(self, uri, headers=None):
        return self._request('DELETE', uri, headers=headers)

    def get(self, uri, headers=None, stream=False):
        return self._request('GET', uri, headers=headers, stream=stream)

    def post(self, uri, data=None, headers=None, stream=False, timeout=180):
        return self._request('POST', uri, data=data, headers=headers, stream=stream, timeout=timeout)

    def patch(self, uri, data=None, headers=None):
        return self._request('PATCH', uri, data=data, headers=headers)

    def put(self, uri, data=None, headers=None):
        return self._request('PUT', uri, data=data, headers=headers)

