"""
Creating a post and delete call modules to add and delete tasks

"""
import json


class OvsTask(object):

    """
    Class has a POST and DELETE method to handle tasks entries.
    """

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def delete(self, uri=None, api=None, auth=None, headers=None, param=''):
        """
        Method will be used in ovs_api.py keywords file to create a Keyword for DELETE Task call
        This is a private api call to delete task for testing purpose only and requires a Trusted Token
        Added an Auth argument in the method so that the trusted token to  api call http_headers can be added
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        self.fusion_client._sessionID = auth
        self.fusion_client._http.headers['auth'] = auth
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        else:
            uri = 'https://%s/rest/tasks%s' % (self.fusion_client._host, param)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def create_task(self, body, api=None, auth=None, headers=None):
        """
        Method will be used in ovs_api.py keywords file to create a Keyword for POST Task call
        This is a private api call to add task for testing purpose only and requires a Trusted Token
        Added an Auth argument in the method so that the trusted token to  api call http_headers can be added
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        self.fusion_client._sessionID = auth
        self.fusion_client._http.headers['auth'] = auth
        uri = 'https://%s/rest/tasks' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response
