#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.api.networking.logical_interconnect_groups import LogicalInterconnectGroup


class EnclosureGroup(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    # X-API-Version = 4
    def _make_body_4(self, body):
        return {'name': body.get('name', "EG default"),
                'type': 'EnclosureGroup',
                'stackingMode': 'Enclosure',
                'interconnectBayMappings': [{'interconnectBay': N,
                                             'logicalInterconnectGroupUri': body.get('logicalInterconnectGroupUri', None)}
                                            for N in range(1, 9)],
                }

    # X-API-Version = 101
    def _make_body_101(self, body):
        return {'name': body.get('name', "EG default"),
                'type': 'EnclosureGroupV2',
                'stackingMode': 'Enclosure',
                'interconnectBayMappingCount': 8,
                'configurationScript': body.get('configurationScript', None),
                'interconnectBayMappings': [{'interconnectBay': N,
                                             'logicalInterconnectGroupUri': body.get('logicalInterconnectGroupUri', None)}
                                            for N in range(1, 9)],
                }

    # X-API-Version = 200
    def _make_body_200(self, body):
        return {'name': body.get('name', "EG default"),
                'type': 'EnclosureGroupV200',
                'stackingMode': 'Enclosure',
                'ipAddressingMode': body.get('ipAddressingMode'),
                'enclosureTypeUri': body.get('enclosureTypeUri', None),
                'interconnectBayMappings': [{'interconnectBay': N,
                                             'logicalInterconnectGroupUri': body.get('ligs').get(N, None)}
                                            for N in range(1, 7)],
                }

    # X-API-Version = 300
    def _make_body_300(self, body):
        return {'name': body.get('name', "EG default"),
                'type': 'EnclosureGroupV300',
                'stackingMode': 'Enclosure',
                'ipAddressingMode': body.get('ipAddressingMode'),
                'enclosureTypeUri': body.get('enclosureTypeUri', None),
                'interconnectBayMappings': [{'interconnectBay': N,
                                             'logicalInterconnectGroupUri': body.get('ligs').get(N, None)}
                                            for N in range(1, 7)],
                }

    # X-API-Version = 500
    def _make_body_500(self, body):
        return {'name': body.get('name', "EG default"),
                'type': 'EnclosureGroupV400',
                'stackingMode': 'Enclosure',
                'ipAddressingMode': body.get('ipAddressingMode'),
                'enclosureTypeUri': body.get('enclosureTypeUri', None),
                'interconnectBayMappings': [{'interconnectBay': N,
                                             'logicalInterconnectGroupUri': body.get('ligs').get(N, None)}
                                            for N in range(1, 7)],
                }

    def make_body(self, api, body, lig_map):

        lig_grps = LogicalInterconnectGroup(self.fusion_client)
        ligs = lig_grps.get()
        body['ligs'] = {}

        if not api:
            api = self.fusion_client._currentVersion()

        for i in lig_map.keys():
            found_lig = 0
            for lig in ligs['members']:
                found_lig += 1
                if lig['name'] == lig_map[i]:
                    # Replace logicalInterconnectGroup name with uri.
                    body['ligs'][i] = lig['uri']
                    break
            if not found_lig:
                logger._log('Lig %s does not exist' % (lig_map[i]), level='WARN')

        ver = {3: self._make_body_4,
               4: self._make_body_4,
               101: self._make_body_101,
               199: self._make_body_101,
               200: self._make_body_200,
               299: self._make_body_300,
               300: self._make_body_300,
               500: self._make_body_500}

        # run the corresponding function
        if api in ver:
            return ver[api](body)
        else:
            # TODO: might want special handling other than Exception
            msg = "API version %d is not supported" % (api)
            raise Exception(msg)

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/enclosure-groups' % (self.fusion_client._host)
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

    def delete(self, name=None, uri=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        elif name:
            param = '?&filter="\'name\' == \'%s\'"' % (name)
            response = self.get(api=api, headers=headers, param=param)
            if response['count'] == 0:
                logger._log('Enclosure Group %s does not exist' % (name), level='WARN')
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
            uri = 'https://%s/rest/enclosure-groups%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
