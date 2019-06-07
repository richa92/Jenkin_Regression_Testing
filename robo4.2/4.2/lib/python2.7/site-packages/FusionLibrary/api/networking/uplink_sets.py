import json
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger


class UplinkSet(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, param='', api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/uplink-sets%s' % (self.fusion_client._host, param)
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
                logger._log('UplinkSet %s does not exist' % (name), level='WARN')
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
            uri = 'https://%s/rest/uplink-sets%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    @staticmethod
    def _make_primary_port_location_dict(bay, port, enclosure='1'):
        return {'locationEntries':
                [{'type': 'Enclosure', 'value': enclosure},
                 {'type': 'Bay', 'value': str(bay)},
                 {'type': 'Port', 'value': port}]
                }

    @staticmethod
    def _make_port_config_info_dict(bay, port, enclosure='1',
                                    desiredSpeed='Auto', **kwargs):
        dto = {'location': {
               'locationEntries':
               [{'type': 'Enclosure', 'value': enclosure},
                {'type': 'Bay', 'value': str(bay)},
                {'type': 'Port', 'value': port}]},
               'desiredSpeed': desiredSpeed}

        for key in kwargs:
            if key not in dto:
                dto[key] = kwargs[key]

        return dto

    @staticmethod
    def _make_body_101(body):
        if 'type' in body and body['type'] is None:
            body['type'] = 'uplink-setV3'
        return body

    @staticmethod
    def _make_body_300(body):
        if 'type' in body and body['type'] is None:
            body['type'] = 'uplink-setV300'
        return body

    @staticmethod
    def _make_body_600(body):
        if 'type' in body and body['type'] is None:
            body['type'] = 'uplink-setV4'
        return body

    @staticmethod
    def _make_body_800(body):
        if 'type' not in body or body['type'] is None:
            body['type'] = 'uplink-setV4'
        return body

    @staticmethod
    def _make_body_1000(body):
        if 'type' not in body or body['type'] is None:
            body['type'] = 'uplink-setV5'
        return body

    @staticmethod
    def _make_body_1200(body):
        if 'type' not in body or body['type'] is None:
            body['type'] = 'uplink-setV6'
        return body

    def make_body(self, api, us):
        if not api:
            if BuiltIn().get_variable_value("${X-API-VERSION}") is not None:
                api = BuiltIn().get_variable_value("${X-API-VERSION}")
            else:
                api = self.fusion_client._currentVersion()

        dto = {'name': us.get('name', None),
               'type': us.get('type', None),
               'ethernetNetworkType': us.get('ethernetNetworkType', None),
               'connectionMode': us.get('connectionMode', 'Auto'),
               'fcNetworkUris': us.get('fcNetworkUris', []),
               'fcoeNetworkUris': us.get('fcoeNetworkUris', []),
               'logicalInterconnectUri': us.get('logicalInterconnectUri', None),
               'networkUris': us.get('networkUris', []),
               'networkType': us.get('networkType', None),
               'primaryPortLocation': us.get('primaryPortLocation', None),
               'portConfigInfos': us.get('portConfigInfos', []),
               'nativeNetworkUri': us.get('nativeNetworkUri', None),
               'lacpTimer': us.get('lacpTimer', 'Short'),
               'manualLoginRedistributionState': us.get('manualLoginRedistributionState', None),
               }

        if not isinstance(us, dict):
            msg = "Body other than type dict is not supported by UplinkSet.make_body()"
            raise Exception(msg)

        for key in us:
            # check if key is in the known dto body, otherwise leave it alone
            # this allows new elements to be passed and negative testing
            if key not in dto:
                dto[key] = us[key]

        us = dto

        """
        # Special handling
        NOTE: these two keys require a shorthand format in order to be translated for you:

            'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': 'Q1', 'desiredSpeed': 'Auto'},
                                {'enclosure': ENC1, 'bay': '3', 'port': 'Q2', 'desiredSpeed': 'Auto'}]
            'primaryPortLocation' : {'enclosure': ENC1, 'bay': '3', 'port': 'Q1'}
        """
        if us['portConfigInfos'] is not None:
            if isinstance(us['portConfigInfos'], list):
                us['portConfigInfos'] = [self._make_port_config_info_dict(**pci)
                                         for pci in us['portConfigInfos']]

        if us['primaryPortLocation'] is not None:
            us['primaryPortLocation'] = self._make_primary_port_location_dict(**us['primaryPortLocation'])

        ver = {'101': self._make_body_101,
               '199': self._make_body_101,
               '200': self._make_body_101,
               '299': self._make_body_300,
               '300': self._make_body_300,
               '400': self._make_body_300,
               '500': self._make_body_300,
               '600': self._make_body_600,
               '800': self._make_body_800,
               '1000': self._make_body_1000,
               '1200': self._make_body_1200
               }

        if str(api) in ver:
            return ver[str(api)](us)
        else:
            msg = "API version %s is not supported by UplinkSet.make_body()" % (str(api))
            raise Exception(msg)
