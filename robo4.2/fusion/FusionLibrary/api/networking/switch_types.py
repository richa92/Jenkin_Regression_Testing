#!/usr/local/bin/python


class SwitchTypes(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/switch-types%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
