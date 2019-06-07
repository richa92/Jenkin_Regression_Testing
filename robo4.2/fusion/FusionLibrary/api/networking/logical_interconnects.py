import json


class LogicalInterconnect(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        else:
            uri = 'https://%s/rest/logical-interconnects%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def get_file(self, uri, localfile, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Content-Type'] = 'application/octet-stream'
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.get_file(uri=uri, localfile=localfile, headers=headers)
        return response

    def delete(self, location, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest-logical-interconnects/locations/interconnects%s' % (self.fusion_client._host, location)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def patch(self, body, uri, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.patch(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def post(self, uri, body=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def update(self, body, uri, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response
