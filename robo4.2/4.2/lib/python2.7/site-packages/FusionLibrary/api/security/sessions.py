#!/usr/local/bin/python
import json


class Sessions(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def update_idle_timeout(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Session-Id'] = self.fusion_client._sessionID
        uri = 'https://%s/rest/sessions/idle-timeout' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, api=None, headers=None, param='', sessionID=None):
        '''
        set param=/idle-timeout, /users in keywords
        '''
        # TODO: Add logic for Session-Keepalive:true

        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if sessionID:
            headers['Session-Id'] = sessionID
        else:
            headers['Session-Id'] = self.fusion_client._sessionID
        uri = 'https://%s/rest/sessions%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
