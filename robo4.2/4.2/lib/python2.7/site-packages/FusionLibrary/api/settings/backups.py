#!/usr/local/bin/python
import json


class Backup(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def cancel(self, backup=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/backups/%s' % (self.fusion_client._host, backup)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def create(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/backups' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers)
        return response

    def upload(self, localfile, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/backups/archive' % (self.fusion_client._host)
        response = self.fusion_client.post_file(uri=uri, localfile=localfile, headers=headers)
        return response

    def download(self, uri=None, localfile=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Accept'] = 'application/octet-stream;q=0.8,application/json'
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.get_file(uri=uri, localfile=localfile, headers=headers)
        return response

    def get(self, param='', api=None, headers=None, uri=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/backups%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def update(self, body, uri=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/backups/config' % (self.fusion_client._host)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response
