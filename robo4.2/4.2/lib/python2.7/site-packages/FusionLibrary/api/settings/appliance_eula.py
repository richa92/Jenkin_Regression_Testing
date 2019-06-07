#!/usr/local/bin/python
import json


class ApplianceEula(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def save(self, host, supportAccess='yes', api=None, headers=None):
        body = {'supportAccess': supportAccess}
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/eula/save' % (host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def status(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/eula/status' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
