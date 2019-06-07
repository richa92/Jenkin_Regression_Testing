#!/usr/local/bin/python
import json


class LoginDomainsGlobalSettings(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if 'X-Api-Version' not in headers:
            self.fusion_client.set_def_api_version()
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/logindomains/global-settings%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def put(self, body, param='', api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if 'X-Api-Version' not in headers:
            self.fusion_client.set_def_api_version()
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/logindomains/global-settings%s' % (self.fusion_client._host, param)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response
