#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class FirmwareDriver(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/firmware-drivers%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def post(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/firmware-drivers' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, name=None, uri=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        elif name:
            param = '?&filter="\'name\' == \'%s\'"' % (name)
            response = self.get(api=api, headers=headers, param=param)
            if response['count'] == 0:
                logger._log('SPP %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s' % (self.fusion_client._host, response['members'][0]['uri'])
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response
