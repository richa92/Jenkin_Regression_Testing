#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class EthernetNetwork(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    # X-API-Version = 4
    def _make_body_4(self, network):
        return {'type': 'ethernet-network',
                'vlanId': network.get('vlan', 0),
                'purpose': network.get('purpose', "General"),
                'name': network.get('name', "net_default"),
                'smartLink': network.get('smart', True),
                'privateNetwork': network.get('private', False)}

    # X-API-Version = 101
    def _make_body_101(self, network):
        return {'type': 'ethernet-networkV2',
                'vlanId': network.get('vlan', 0),
                'purpose': network.get('purpose', "General"),
                'name': network.get('name', "net_default"),
                'smartLink': network.get('smart', True),
                'privateNetwork': network.get('private', False),
                'connectionTemplateUri': network.get('connectionTemplateUri', None),
                'ethernetNetworkType': network.get('ethernetNetworkType', "Tagged")}

    def make_body(self, api, network):
        # TODO:  Update to support API version 3 (connection template uri)
        ver = {4: self._make_body_4,
               101: self._make_body_101,
               199: self._make_body_101}

        # run the corresponding function
        if api in ver:
            return ver[api](network)
        else:
            # TODO: might want special handling other than Exception
            msg = "API version %d is not supported" % (api)
            raise Exception(msg)

    def make_bulk_body(self, api, network):
        return {'type': 'bulk-ethernet-network',
                'vlanIdRange': network.get('vlanIdRange', "None"),
                'purpose': network.get('purpose', "General"),
                'namePrefix': network.get('namePrefix', "net"),
                'smartLink': network.get('smart', True),
                'privateNetwork': network.get('private', False),
                'bandwidth': network.get('bandwidth', None)}

    def bulk_create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/ethernet-networks/bulk' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/ethernet-networks' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def update(self, body, uri, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, name=None, uri=None, param='', api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        elif name:
            param = '?&filter="\'name\' == \'%s\'"%s ' % (name, param)
            response = self.get(api=api, headers=headers, param=param)
            if response['count'] == 0:
                logger._log('Network %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s' % (self.fusion_client._host, response['members'][0]['uri'])
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/ethernet-networks%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
