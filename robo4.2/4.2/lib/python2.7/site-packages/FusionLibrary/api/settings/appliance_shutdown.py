#!/usr/local/bin/python


class ApplianceShutdown(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def shutdown(self, mode=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/appliance/shutdown?type=%s' % (self.fusion_client._host, mode)
        response = self.fusion_client.post(uri=uri, headers=headers)
        return response
