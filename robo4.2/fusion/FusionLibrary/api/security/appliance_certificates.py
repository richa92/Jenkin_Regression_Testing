#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class ApplianceCertificate(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def put(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/certs/server/' % (self.fusion_client._host)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/certs/server/' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
