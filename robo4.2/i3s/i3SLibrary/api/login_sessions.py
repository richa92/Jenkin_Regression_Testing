#!/usr/local/bin/python
from RoboGalaxyLibrary.utilitylib import logging as logger
import json


class LoginSession(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def login(self, host, sessionID, api=None, headers=None):
        self.i3s_client._host = host
        if not headers:
            headers = self.i3s_client._headers
        if 'X-Api-Version' not in headers:
            if api:
                headers = self.i3s_client._set_req_api_version(api=api)
            else:
                headers = self.i3s_client.set_def_api_version()
        self.i3s_client._sessionID = sessionID
        self.i3s_client._http.headers['auth'] = sessionID        
        return

    def logout(self, headers=None):
        if not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s/rest/login-sessions' % (self.i3s_client._host)
        resp = self.i3s_client.delete(uri=uri, headers=headers)
        # The session auth (self.i3s_client._http.headers['auth']) is left in place, but is now invalid.
        # You must login again, or switch users
        self.i3s_client._active_sessions.pop(self.i3s_client._cred['userName'], None)
        self.i3s_client._sessionID = None
        self.i3s_client._cred = None
        return resp

    def get_active_user(self):
        return self.i3s_client._cred['userName']

    def get_active_sessions(self):
        return self.i3s_client._active_sessions

    def switch_active_user(self, user):
        if not self.i3s_client._cred['userName'] == user:
            self.i3s_client._sessionID = self.i3s_client._active_sessions[user]['sessionID']
            self.i3s_client._http.headers['auth'] = self.i3s_client._sessionID
            self.i3s_client._cred = {'userName': user, 'password': self.i3s_client._active_sessions[user]['password']}
