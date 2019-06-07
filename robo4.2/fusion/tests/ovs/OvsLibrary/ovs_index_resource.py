"""
Creating a post call modules to add index entry to index.node db

"""
import json


class OvsIndexResource(object):

    """
    Class has a POST method to inject entries in index.node DB.
    """

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, api=None, auth=None, headers=None, param=''):
        """
        Method will be used in ovs_api.py keywords file to create a Keyword for POST call
        This is a private api call to add entry in index.node db for testing purpose only and requires a Trusted Token
        Added an Auth argument in the method so that the trusted token to  api call http_headers can be added

        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        self.fusion_client._sessionID = auth
        self.fusion_client._http.headers['auth'] = auth
        uri = 'https://%s/rest/index/resources%s' % (self.fusion_client._host, param)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response
