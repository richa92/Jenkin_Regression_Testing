#!/usr/local/bin/python
import json
import os
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.api import common


class BuildPlans(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
#         if (headers['X-Api-Version'] == '800'):
#             body['type'] = 'OeBuildPlanV6'   
        uri = 'https://%s%s' % (self.i3s_client._host, common.uris.get('buildplan'))                              
        response = self.i3s_client.post(uri=uri, headers=headers, body=json.dumps(body)) 
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s/%s' % (self.i3s_client._host, common.uris.get('buildplan'), uri)
        else:
            uri = 'https://%s%s%s' % (self.i3s_client._host, common.uris.get('buildplan'), param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response

    def update(self, api, body=None, uri=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if (headers['X-Api-Version'] == '500'):
            body['type'] = 'OeBuildPlanV5'
        uri = 'https://%s%s%s' % (self.i3s_client._host, uri, param)
        response = self.i3s_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, name=None, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s%s' % (self.i3s_client._host, uri, param)
        elif name:
            param2 = '?&filter="\'name\' == \'%s\'"' % (name)
            response = self.get(api=api, headers=headers, param=param2)
            if response['count'] == 0:
                logger._log('buildplan %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s%s' % (self.i3s_client._host, response['members'][0]['uri'], param)
        response = self.i3s_client.delete(uri=uri, headers=headers)
        return response

    