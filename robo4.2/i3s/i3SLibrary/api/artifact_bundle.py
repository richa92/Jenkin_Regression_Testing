#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from docutils.parsers.rst.directives import body
from i3SLibrary.api import common


class ArtifactBundle(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s/rest/artifact-bundles' % (self.i3s_client._host)                                     
        response = self.i3s_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response
        
    def add(self, localfile, api=None, headers=None):
        header_org = self.i3s_client._headers
        self.i3s_client._headers={}
        self.i3s_client._headers = self.i3s_client.set_def_api_version()
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s%s/' %(self.i3s_client._host, common.uris.get('artifactbundle'))             
        response = self.i3s_client.post_file(uri=uri, localfile=localfile, headers=self.i3s_client._headers)          
        self.i3s_client._headers = header_org          
        return response
    
    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers        
        if uri:            
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:            
            uri = 'https://%s/rest/artifact-bundles%s' % (self.i3s_client._host, param)        
        response = self.i3s_client.get(uri=uri, headers=headers)        
        return response
            
    def download(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers        
        if uri:            
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:            
            uri = 'https://%s/rest/artifact-bundles%s' % (self.i3s_client._host, param)              
        response = self.i3s_client.get(uri=uri, headers=headers)        
        param1= '/rest/artifact-bundles/download'
        localfile= '%s' % (common.artifactbundle.get('ab_downloadtolocation'))        
        if (len(response ['members']) != 0):
            for  ab in response['members']:
                if 'artifactsbundleID' in ab:
                    ab_downloaduri = 'https://%s%s/%s' %(self.i3s_client._host, param1, str(ab['artifactsbundleID']))
                    ab_size=ab['size']
                else:
                    logger._warn(
                                 "Get AB failed... no AB exists..check for parameters")
                    return
        response = self.i3s_client.get_file(uri=ab_downloaduri, localfile=localfile, headers=self.i3s_client._headers)            
        ab_download_size=int(response['headers']['Content-Length'])
        if (ab_size == ab_download_size):
            logger._log_to_console_and_log_file("\n Size of the artifactbundle downloaded matches with the uploaded image, successful download...\n")
        else:
            logger._log_to_console_and_log_file("\n Size of artifactbundle downloaded doesnot match with the uploaded image, download failed...\n")
            response['status_code'] = 503
        return response
        
    
    def extract(self, uri=None, api=None, headers=None):
        ''' Save the contents of header before modifying the same'''
        header_org = self.i3s_client._headers
        self.i3s_client._headers={}
        self.i3s_client._headers = self.i3s_client.set_def_api_version()               
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)            
        elif not headers:
            headers = self.i3s_client._headers
        
        headers = {
                         'Content-Type': 'text/plain;charset=UTF-8'
                         }    
        param = '?extract=true&forceImport=true'
        uri = 'https://%s%s%s' % (self.i3s_client._host, uri, param)
        logger._log_to_console_and_log_file("Value in uri for extract is " +str(uri))        
        response = self.i3s_client.put(uri=uri, headers=headers)
        self.i3s_client._headers = header_org 
        return response

    def update(self, api, body=None, uri=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)            
        elif not headers:            
            headers = self.i3s_client._headers        
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
                logger._log('ArtifactBundle %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s%s' % (self.i3s_client._host, response['members'][0]['uri'], param)
        
        response = self.i3s_client.delete(uri=uri, headers=headers)
        return response    