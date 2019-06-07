import json


class RemoteSyslog(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/logs/remoteSyslog/logconfig' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def update(self, body, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        ''' the api reference for 4.10 has the following uri for remote_syslog '''
        uri = 'https://%s/rest/remote-syslog/%s' % (self.fusion_client._host, param)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, logId, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/logs/remoteSyslog/%s%s' % (self.fusion_client._host, id, param)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        ''' the api reference for 4.10 has the following uri for remote-syslog '''
        uri = 'https://%s/rest/remote-syslog/%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
