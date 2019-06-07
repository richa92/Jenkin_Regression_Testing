#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from docutils.parsers.rst.directives import body


class I3SApplianceFirmware(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def upload(self, localfile, api=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers.copy()
        headers['Content-Type'] = 'multipart/form-data'
        uri = 'https://%s/rest/appliance/firmware/image' % (self.i3s_client._host)
        response = self.i3s_client.post_file(uri=uri, localfile=localfile, headers=headers)
        return response

    def update(self, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers.copy()
        uri = 'https://%s/rest/appliance/firmware/pending%s' % (self.i3s_client._host, param)
        response = self.i3s_client.put(uri=uri, headers=headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s/rest/appliance/firmware%s' % (self.i3s_client._host, param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response