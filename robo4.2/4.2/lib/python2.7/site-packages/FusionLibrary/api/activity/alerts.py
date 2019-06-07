""" Alert Keywords """
import json


class Alert(object):
    """ Alert Keywords """
    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def update(self, body, uri, api=None, headers=None):
        """ Update method """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, uri=None, api=None, headers=None, param=''):
        """ Delete method """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            # deletes all alerts
            uri = 'https://%s/rest/alerts%s' % (self.fusion_client._host, param)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def delete_changelog(self, alertId=None, api=None, headers=None):
        """ """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/alerts/%s' % (self.fusion_client._host, alertId)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        """ Get method """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/alerts%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
