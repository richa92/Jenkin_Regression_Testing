#!/usr/local/bin/python
import json


class Authorizations(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def check(self, body, api=None, headers=None, sessionID=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        if sessionID:
            headers['auth'] = sessionID
        uri = 'https://%s/rest/authz/validator' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, api=None, headers=None, param='', sessionID=None):
        '''
        set param=/category-actions, /role-category-actions in keywords
        '''
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        if sessionID:
            headers['auth'] = sessionID
        uri = 'https://%s/rest/authz%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
