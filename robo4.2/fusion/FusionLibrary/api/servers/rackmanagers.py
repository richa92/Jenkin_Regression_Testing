#!/usr/local/bin/python
"""Adding support for RackManager
Performs POST, PATCH and DELETE requests
"""
import json


class RackManager(object):
    """ RackManager basic operations
     This includes import,refresh and
     remove operation
    """
    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def post(self, body, api=None, headers=None):
        """Adds an Rackmanager to the appliance
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            [Example]
            ${resp} = Fusion Api Add Rackmanager | <body>s | <api> | <headers>
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/rack-managers' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def patch(self, body, uri, api=None, headers=None, etag=None):
        """Issues a PATCH request to a Rackmanager
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Patch Rackmanager | <body> | <uri> | <api> | <headers> | etag
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if etag:
            headers['If-Match'] = str(etag)
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.patch(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def put(self, body, uri, api=None, headers=None):
        """Update a rackmanager. Currently the only attribute that can be updated is the name
            [Arguments]
            body: REQUIRED a dictionary containing request body elements
            uri: REQUIRED the uri of the resource to update
            [Example]
            ${resp} = Fusion Api Edit Rackmanager | <body> | <uri> | <api> | <headers>
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, uri, name=None, api=None, headers=None, param=''):
        """Removes an Rackmanager from the appliance based on name OR uri
            [Arguments]
            name: a dictionary containing request body elements
            uri: the uri of the resource to remove.
            param: you can use param=?force="true" to force remove a rackmanager
            [Example]
            ${resp} = Fusion Api Delete Rackmanager | <name> | <uri> | <param> | <api> | <headers>
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        elif name:
             param2 = '?&filter="\'name\' == \'%s\'"' % (name)
             response = self.get(api=api, headers=headers, param=param2)
             if response['count'] == 0:
                logger._log('Rackmanager %s does not exist' % (name), level='WARN')
                return
             elif response['count'] > 1:
                    msg = "Filter %s returned more than one result" % (name)
                    raise Exception(msg)
             else:
                    uri = 'https://%s%s%s' % (self.fusion_client._host, response['members'][0]['uri'], param)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        """Gets Rackmanager
            [Arguments]
            uri: the uri of the resource to retrieve. if omitted, all are returned
            param: query parameters
            [Example]
            ${resp} = Fusion Api Get Rackmanager  | <uri> | <param> | <api> | <headers>
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/rack-managers%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response