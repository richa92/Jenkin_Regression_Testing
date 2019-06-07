#!/usr/local/bin/python
from i3SLibrary.api import common


class OsVolumes(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s/%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s%s%s' % (self.i3s_client._host, common.uris.get('osvolumes'), param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response
