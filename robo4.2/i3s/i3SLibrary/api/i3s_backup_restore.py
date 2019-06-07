#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from docutils.parsers.rst.directives import body
from i3SLibrary.api import common


class BackupRestore(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def add(self, localfile, api=None, headers=None):
        self.i3s_client._headers={}
        self.i3s_client._headers = self.i3s_client.set_def_api_version()
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s%s/' %(self.i3s_client._host, common.uris.get('backup'))
        logger._log("Value in upload backup URI is" +str(uri))           
        response = self.i3s_client.post_file(uri=uri, localfile=localfile, headers=self.i3s_client._headers)          
        return response
    
    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers        
        if uri:            
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:            
            uri = 'https://%s/rest/artifact-bundles/backups/%s' % (self.i3s_client._host, param)        
        response = self.i3s_client.get(uri=uri, headers=self.i3s_client._headers)        
        return response
    
    def download(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s%s' % (self.i3s_client._host, param)
        localfile= '%s' % (common.backup.get('bk_downloadtolocation'))
        response = self.i3s_client.get_file(uri=uri, localfile=localfile, headers=self.i3s_client._headers)
        return response
    
    def create(self, body, api=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s/rest/artifact-bundles/backups' % (self.i3s_client._host)                                     
        response = self.i3s_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response
    
    def extract(self, api, body=None, uri=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)            
        elif not headers:            
            headers = self.i3s_client._headers        
        uri = 'https://%s/rest/artifact-bundles/backups/archive' % (self.i3s_client._host)        
        response = self.i3s_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response