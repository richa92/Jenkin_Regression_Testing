import json


class Ping(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def ping(self, body=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/reachable' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response
