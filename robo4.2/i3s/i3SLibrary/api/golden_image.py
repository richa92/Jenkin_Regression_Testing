#!/usr/local/bin/python
import json
import os
from RoboGalaxyLibrary.utilitylib import logging as logger
from i3SLibrary.api import common


class GoldenImage(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def add(self, file, param, api=None, headers=None):
        ''' Save the contents of header before modifying the same'''
        header_org = self.i3s_client._headers
        self.i3s_client._headers = {}
        self.i3s_client._headers = self.i3s_client.set_def_api_version()
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        # Get the platform name
        platform = os.name
        if (platform == 'nt'):
            if (file == "valid_file"):
                localfile = '%s' % (common.goldenimageuploadfile.get('valid_file_nt'))
            elif (file == "invalid_file"):
                localfile = '%s' % (common.goldenimageuploadfile.get('invalid_file_nt'))
            else:
                logger._log_to_console_and_log_file("No file specified\n")
                localfile = ""
        else:
            if (file == "valid_file"):
                localfile = '%s' % (common.goldenimageuploadfile.get('valid_file_linux'))
            elif (file == "invalid_file"):
                localfile = '%s' % (common.goldenimageuploadfile.get('invalid_file_linux'))
            else:
                logger._log_to_console_and_log_file("No file specified\n")
                localfile = ""
        uri = 'https://%s%s/%s' % (self.i3s_client._host, common.uris.get('goldenimage'), param)
        response = self.i3s_client.post_file(uri=uri, localfile=localfile, headers=self.i3s_client._headers)
        self.i3s_client._headers = header_org
        return response
    
    def create(self, body, api=None, headers=None):
        """Golden Image Capture method."""
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        uri = 'https://%s%s' % (self.i3s_client._host, common.uris.get('goldenimage'))
        response = self.i3s_client.post(uri=uri, headers=headers,
                                        body=json.dumps(body))
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s/%s' % (self.i3s_client._host, common.uris.get('goldenimage'), uri)
        else:
            uri = 'https://%s%s%s' % (self.i3s_client._host, common.uris.get('goldenimage'), param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        return response

    def getvolume(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s%s/%s' % (self.i3s_client._host, common.uris.get('goldenvolume'), param)
        response = self.i3s_client.get(uri=uri, headers=headers)
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
                logger._log('Goldenimage %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s%s' % (self.i3s_client._host, response['members'][0]['uri'], param)
        response = self.i3s_client.delete(uri=uri, headers=headers)
        return response

    def download(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s%s/%s' % (self.i3s_client._host, common.uris.get('goldenimage'), param)
        response = self.i3s_client.get(uri=uri, headers=headers)
        param1 = 'download'
        localfile = '%s' % (common.goldenimagedownloadfile.get('gi_valid_download_file'))
        if (len(response['members']) != 0):
            for goldimage in response['members']:
                if 'id' in goldimage:
                    gi_downloaduri = 'https://%s%s/%s/%s' % (self.i3s_client._host, common.uris.get('goldenimage'), param1, str(goldimage['id']))
                    gi_size = goldimage['size']
                else:
                    logger._warn(
                        "Get GI failed... no goldimage exists..check for parameters")
                    return
        response = self.i3s_client.get_file(uri=gi_downloaduri, localfile=localfile, headers=self.i3s_client._headers)
        gi_download_size = int(response['headers']['Content-Length'])
        if (gi_size == gi_download_size):
            logger._log_to_console_and_log_file("\n Size of goldenimage downloaded matches with the uploaded image, successful download...\n")
        else:
            logger._log_to_console_and_log_file("\n Size of goldenimage downloaded does not match with the uploaded image, download failed...\n")
            response['status_code'] = 503
        return response
