#!/usr/local/bin/python

import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class Scope(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def post(self, body=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/scopes' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, uri=None, param='', api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/scopes%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def delete(self, uri=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)

        elif not headers:
            headers = self.fusion_client._headers.copy()
            headers['If-Match'] = '*'

        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)

        response = self.fusion_client.delete(uri=uri, headers=headers)

        return response

    def patch(self, uri=None, body=None, api=None, headers=None, etag=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
            headers["Content-Type"] = "application/json-patch+json"
        if etag:
            headers['If-Match'] = str(etag)
        uri = 'https://%s%s' % (self.fusion_client._host, uri)

        response = self.fusion_client.patch(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def put(self, body, uri, api=None, headers=None, eTag=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()

        if eTag:
            headers['If-Match'] = eTag
        else:
            headers['If-Match'] = "*"
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response
