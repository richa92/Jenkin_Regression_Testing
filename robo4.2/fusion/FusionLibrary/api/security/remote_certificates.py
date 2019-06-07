#!/usr/local/bin/python


class RemoteCertificate(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, host, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Requestername'] = 'AUTHN'
        uri = 'https://%s/rest/certificates/https/remote/%s%s' % (self.fusion_client._host, host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def trust(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/servers' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response
