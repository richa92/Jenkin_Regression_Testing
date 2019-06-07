import json


class ApplianceSupportDump(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/appliance/support-dumps' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, uri, localfile, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Content-Type'] = 'application/octet-stream'
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.get_file(uri=uri, localfile=localfile, headers=headers)
        return response
