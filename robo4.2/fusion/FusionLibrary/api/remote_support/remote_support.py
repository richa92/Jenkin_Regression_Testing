#!/usr/local/bin/python
import json


class RemoteSupport(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def update(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/support' % (self.fusion_client._host)
        response = self.fusion_client.patch(uri=uri, headers=headers, body=json.dumps(body))
        return response