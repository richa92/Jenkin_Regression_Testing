#!/usr/local/bin/python


class StartupProgress(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, host, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        if 'X-Api-Version' not in headers:
            self.fusion_client.set_def_api_version()
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/progress' % (host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
