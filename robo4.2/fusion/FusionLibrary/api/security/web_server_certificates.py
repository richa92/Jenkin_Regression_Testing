#!/usr/local/bin/python
import json


class WebServerCertificate(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def post(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/https/certificaterequest' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def put(self, body, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/https%s' % (self.fusion_client._host, param)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/https' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
