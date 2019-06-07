#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class Provider(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/fc-sans/providers%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
