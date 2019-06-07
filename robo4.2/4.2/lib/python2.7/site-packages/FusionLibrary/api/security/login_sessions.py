#!/usr/local/bin/python
import json
from RoboGalaxyLibrary import BuiltIn


class LoginSession(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def login(self, host, cred, api=None, headers=None):
        self.fusion_client._host = host
        self.fusion_client._cred = cred
        # automatically set OneView version in Suite MetaData
        resp = self.fusion_client.get("https://%s/rest/appliance/nodeinfo/version" % host)
        ver = 'no build metadata'
        if 'softwareVersion' in resp:
            ver = resp['softwareVersion']
        try:
            BuiltIn().set_suite_metadata("OneView Version", ver, top=True)   # parent suite
            BuiltIn().set_suite_metadata("OneView Version", ver)
        except:
            pass   # allows non-RG uses of FusionLibrary

        if not headers:
            headers = self.fusion_client._headers.copy()

        if 'X-Api-Version' not in headers:
            if api:
                headers = self.fusion_client._set_req_api_version(api=api)
            else:
                headers = self.fusion_client.set_def_api_version()

        uri = 'https://%s/rest/login-sessions' % (self.fusion_client._host)
        resp = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(self.fusion_client._cred))
        sessionID = None
        if 'sessionID' in resp:
            self.fusion_client._active_sessions[cred['userName']] = {'password': cred['password'], 'sessionID': resp['sessionID']}
            self.fusion_client._sessionID = resp['sessionID']
            self.fusion_client._http.headers['auth'] = resp['sessionID']
            sessionID = resp['sessionID']
        return resp, sessionID

    def login_by_cert(self, host, cert, api=None, headers=None):
        self.fusion_client._host = host
        # automatically set OneView version in Suite MetaData
        resp = self.fusion_client.get("https://%s/rest/appliance/nodeinfo/version" % host)
        ver = 'no build metadata'
        if 'softwareVersion' in resp:
            ver = resp['softwareVersion']
        try:
            BuiltIn().set_suite_metadata("OneView Version", ver, top=True)   # parent suite
            BuiltIn().set_suite_metadata("OneView Version", ver)
        except:
            pass   # allows non-RG uses of FusionLibrary

        if not headers:
            headers = self.fusion_client._headers.copy()

        if 'X-Api-Version' not in headers:
            if api:
                headers = self.fusion_client._set_req_api_version(api=api)
            else:
                headers = self.fusion_client.set_def_api_version()

        uri = 'https://%s/rest/login-sessions/smartcards' % (self.fusion_client._host)
        resp = self.fusion_client.post(uri=uri, headers=headers, cert=cert)
        sessionID = None
        if 'sessionID' in resp:
            self.fusion_client._active_sessions[resp['username']] = {'cert': cert, 'sessionID': resp['sessionID']}
            self.fusion_client._sessionID = resp['sessionID']
            self.fusion_client._http.headers['auth'] = resp['sessionID']
            sessionID = resp['sessionID']
        return resp, sessionID

    def logout(self, headers=None):
        if not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/login-sessions' % (self.fusion_client._host)
        resp = self.fusion_client.delete(uri=uri, headers=headers)
        # The session auth (self.fusion_client._http.headers['auth']) is left in place, but is now invalid.
        # You must login again, or switch users
        self.fusion_client._active_sessions.pop(self.fusion_client._cred['userName'], None)
        self.fusion_client._sessionID = None
        self.fusion_client._cred = None
        return resp

    def modify_active_permissions(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/login-sessions/auth-token' % (self.fusion_client._host)
        resp = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return resp

    def delete_session(self, api=None, headers=None, sessionId=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if sessionId:
            headers['auth'] = sessionId
        uri = 'https://%s/rest/login-sessions' % (self.fusion_client._host)
        resp = self.fusion_client.delete(uri=uri, headers=headers)
        return resp

    def get_active_user(self):
        return self.fusion_client._cred['userName']

    def get_active_sessions(self):
        return self.fusion_client._active_sessions

    def set_active_session(self, sessionId):
        self.fusion_client._sessionID = sessionId
        self.fusion_client._http.headers['auth'] = self.fusion_client._sessionID

    def switch_active_user(self, user):
        if self.fusion_client._cred is None or not self.fusion_client._cred['userName'] == user:
            self.fusion_client._sessionID = self.fusion_client._active_sessions[user]['sessionID']
            self.fusion_client._http.headers['auth'] = self.fusion_client._sessionID
            self.fusion_client._cred = {'userName': user, 'password': self.fusion_client._active_sessions[user]['password']}
