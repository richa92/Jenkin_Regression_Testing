import json


class ApplianceTimeAndLocaleConfiguration(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def configure(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/configuration/time-locale' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/configuration/time-locale' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
