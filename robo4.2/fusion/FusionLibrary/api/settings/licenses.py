#!/usr/local/bin/python
import json


class Licenses(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    # X-API-Version = ALL
    def add(self, key=None, license_type='LicenseV500', api=None, headers=None):
        body = {'type': license_type, 'key': key}
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/licenses' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, uri=None, param=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/licenses%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def delete(self, uri=None, license_id=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()

        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/licenses/%s' % (self.fusion_client._host, license_id)

        response = self.fusion_client.delete(uri=uri, headers=headers)

        return response
