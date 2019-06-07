'''' Image Streamer deploymentplan '''
# !/usr/local/bin/python

import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.api import common


class DeploymentPlan(object):
    ''' DeploymentPlan class to handle CRUD operations '''

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def create(self, body, api=None, headers=None):
        ''' Method for creating a deployment plan '''
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s%s/' % (self.i3s_client._host, common.uris.get('oedeploymentplan'))
        response = self.i3s_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        ''' Method for getting a deployment plan '''
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s%s%s' % (self.i3s_client._host, common.uris.get('oedeploymentplan'), param)        
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response

    def update(self, api, body=None, uri=None, headers=None, param=''):
        ''' Method for updating a deployment plan '''
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s%s%s' % (self.i3s_client._host, uri, param)
        response = self.i3s_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, name=None, uri=None, api=None, headers=None, param=''):
        ''' Method for deleting a deployment plan '''
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
                logger._log('Deployment Plan %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s%s' % (self.i3s_client._host, response['members'][0]['uri'], param)
        response = self.i3s_client.delete(uri=uri, headers=headers)
        return response
