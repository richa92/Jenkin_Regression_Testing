#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.api import common
import os

class SupportDump(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s%s' % (self.i3s_client._host, common.uris.get('supportdump'))
        response = self.i3s_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def download(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s%s' % (self.i3s_client._host, param)
        platform = os.name
        if (platform == 'nt'):
            localfile= '%s' % (common.supportdump.get('sd_win_downloadtolocation'))
        else:
            localfile= '%s' % (common.supportdump.get('sd_linux_downloadtolocation'))
        response = self.i3s_client.get_file(uri=uri, localfile=localfile, headers=self.i3s_client._headers)
        return response