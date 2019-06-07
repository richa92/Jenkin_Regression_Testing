#!/usr/local/bin/python
import json


class ProxyServer(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def add(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/proxy-config' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/proxy-config' % (self.fusion_client._host)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/proxy-config' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
