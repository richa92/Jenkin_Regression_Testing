class ApplianceUpgrade(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, uri, localfile, api=None, headers=None, chunk_size=1024):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Accept'] = 'application/octet-stream;q=0.8,application/json'
        response = self.fusion_client.get_file(uri=uri, localfile=localfile, headers=headers, chunk_size=chunk_size)
        return response
