#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class ClientCertificate(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def post(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['requestername'] = 'DEFAULT'
        uri = 'https://%s/rest/certificates' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def put(self, aliasname, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['requestername'] = 'DEFAULT'
        uri = 'https://%s/rest/certificates/%s' % (self.fusion_client._host, aliasname)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, aliasname, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['requestername'] = 'DEFAULT'
        uri = 'https://%s/rest/certificates/%s%s' % (self.fusion_client._host, aliasname, param)
        logger.info(uri)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def delete(self, aliasname, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['requestername'] = 'DEFAULT'
        uri = 'https://%s/rest/certificates/%s%s' % (self.fusion_client._host, aliasname, param)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def post_validator(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/validator' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response