#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class Svmc(object):

    def __init__(self, svmc_client):
        self.svmc_client = svmc_client

    def get(self, uri=None, api=None, headers=None):

        if api:
            headers = self.svmc_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.svmc_client._headers
        elif not uri:
            uri = 'https://%s/svmc' % (self.svmc_client._host)
        response = self.svmc_client.get(uri=uri, headers=headers)
        return response

    def create(self, uri, body, api=None, headers=None):
        if api:
            headers = self.svmc_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.svmc_client._headers
        elif not uri:
            uri = 'https://%s/svmc' % (self.svmc_client._host)

        response = self.svmc_client.post(uri=uri, api=api, headers=headers, body=json.dumps(body))
        return response

    def update(self, body, uri, api=None, headers=None):
        if api:
            headers = self.svmc_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.svmc_client._headers
        elif not uri:
            uri = 'https://%s/svmc' % (self.svmc_client._host)
        response = self.svmc_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, name=None, uri=None, api=None, headers=None):
        if api:
            headers = self.svmc_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.svmc_client._headers
        elif not uri:
            uri = 'https://%s/svmc' % (self.svmc_client._host)

        response = self.svmc_client.delete(uri=uri, headers=headers)
        return response
