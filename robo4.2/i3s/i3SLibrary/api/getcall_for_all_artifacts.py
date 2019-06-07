'''
i3S API - Get call for all artifacts
'''
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.api import common

import json
import time

class GetCallForArtifacts(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def i3s_get_goldenimage(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s/rest/golden-images%s' % (self.i3s_client._host, param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response
    
    def i3s_get_planscript(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s/rest/plan-scripts%s' % (self.i3s_client._host, param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response
    
    def i3s_get_buildplan(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s/rest/build-plans%s' % (self.i3s_client._host, param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response
    
    def i3s_get_deploymentplan(self, uri=None, api=None, headers=None, param=''):
        logger._log_to_console("Value in dp param in getcall for all artifacts is" +str(param))
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
            logger._log_to_console("Value in dp uri in if of getcall for all artifacts is" +str(uri))
        else:
            uri = 'https://%s/rest/deployment-plans/%s' % (self.i3s_client._host, param)        
            logger._log_to_console("Value in dp uri in else of getcall for all artifacts is" +str(uri))
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response
    
    def i3s_get_statelessserver(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s/rest/statelessserver/%s' % (self.i3s_client._host, param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response
    
    