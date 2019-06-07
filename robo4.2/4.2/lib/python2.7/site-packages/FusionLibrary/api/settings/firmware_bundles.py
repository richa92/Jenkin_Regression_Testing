#!/usr/local/bin/python
import ntpath


class FirmwareBundle(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def upload(self, localfile, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Content-Type'] = 'multipart/form-data'
        path, filename = ntpath.split(localfile)
        headers['uploadfilename'] = filename
        uri = 'https://%s/rest/firmware-bundles' % (self.fusion_client._host)
        response = self.fusion_client.post_file(uri=uri, localfile=localfile, headers=headers)
        return response
