#!/usr/local/bin/python
import json


class ApplianceTrapDestination(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, id=None, api=None, headers=None):
        ''' Adds or updates the specified trap forwarding destination.
            The trap destination associated with the given id will be
            updated if a trap destination with that id already exists.
            If the given id is not found, then a trap destination will
            be created with the given id.
        '''
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/trap-destinations/%s' % (self.fusion_client._host, id)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def validate(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/trap-destinations/validation' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, id=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/trap-destinations/%s' % (self.fusion_client._host, id)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, id=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        if id:
            uri = 'https://%s/rest/appliance/trap-destinations/%s' % (self.fusion_client._host, id)
        else:
            uri = 'https://%s/rest/appliance/trap-destinations%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def put(self, body, id, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://{}/rest/appliance/trap-destinations/{}'. format(self.fusion_client._host, id)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response
