#!/usr/local/bin/python
import json


class ApplianceFirmware(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def upload(self, localfile, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Content-Type'] = 'multipart/form-data'
        uri = 'https://%s/rest/appliance/firmware/image' % (self.fusion_client._host)
        response = self.fusion_client.post_file(uri=uri, localfile=localfile, headers=headers)
        return response

    def update(self, api=None, headers=None, param=''):
        ''' add param=/pending, /verificationKey, /verificationKeyFile to keywords for related PUT functions'''
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/appliance/firmware/pending%s' % (self.fusion_client._host, param)
        response = self.fusion_client.put(uri=uri, headers=headers)
        return response

    def delete(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/appliance/firmware/pending' % (self.fusion_client._host)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        ''' add param=document-content/{tarFileName}.{suffix}/{documentType},
            /notification, /pending, /verificationKey in keywords
        '''
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/appliance/firmware%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
