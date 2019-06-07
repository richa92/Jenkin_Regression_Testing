#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.api import common
import os


class AuditLog(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def download(self, uri=None, api=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s/rest/audit-logs/download' % (self.i3s_client._host)
        platform = os.name
        if (platform == 'nt'):
            localfile= '%s' % (common.auditlog.get('al_win_downloadtolocation'))
        else:
            localfile= '%s' % (common.auditlog.get('al_linux_downloadtolocation'))
        response = self.i3s_client.get_file(uri=uri, localfile=localfile, headers=self.i3s_client._headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s/rest/audit-logs%s' % (self.i3s_client._host, param)
        response = self.i3s_client.get(uri=uri, headers=self.i3s_client._headers)
        return response