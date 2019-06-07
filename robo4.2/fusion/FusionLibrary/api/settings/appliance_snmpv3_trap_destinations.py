#!/usr/local/bin/python
import json


class ApplianceSnmpv3TrapDestination(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, api=None, headers=None):
        ''' Adds SNMPv3 trap forwarding destination.
        '''
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/snmpv3-trap-forwarding/destinations' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def put(self, body=None, id=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/snmpv3-trap-forwarding/destinations/%s' % (self.fusion_client._host, id)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, id=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/appliance/snmpv3-trap-forwarding/destinations/%s' % (self.fusion_client._host, id)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, id=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        if id:
            uri = 'https://%s/rest/appliance/snmpv3-trap-forwarding/destinations/%s' % (self.fusion_client._host, id)
        else:
            uri = 'https://%s/rest/appliance/snmpv3-trap-forwarding/destinations%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
