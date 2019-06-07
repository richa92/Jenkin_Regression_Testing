#!/usr/local/bin/python


class ApplianceNodeInformation(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get_status(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/nodeinfo/status' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def get_version(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/nodeinfo/version' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
