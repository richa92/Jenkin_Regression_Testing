#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class StorageVolumeAttachment(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, uri=None, api=None, headers=None, param=''):
        '''
        param: ?query=storageVolumeUri eq '/rest/storage-volumes/9c794aad-0ad2-41ba-86fc-a657012169c0' AND ownerUri eq '/rest/server-profiles/cb3b7bee-ddbd-47c3-9d76-593edffbd055'
        '''
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        else:
            uri = 'https://%s/rest/storage-volume-attachments%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def patch(self, body, param='', api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/storage-volume-attachments%s' % (self.fusion_client._host, param)
        response = self.fusion_client.patch(uri=uri, headers=headers, body=json.dumps(body))
        return response
