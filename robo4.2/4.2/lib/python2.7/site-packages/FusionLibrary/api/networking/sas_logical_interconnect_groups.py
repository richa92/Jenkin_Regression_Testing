import json
from robot.libraries.BuiltIn import BuiltIn
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.api.networking.sas_interconnect_types import SasInterconnectTypes
import copy


class SasLogicalInterconnectGroup(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/sas-logical-interconnect-groups' % (self.fusion_client._host)
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

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/sas-logical-interconnect-groups%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
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
                logger._log('SAS LIG %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s' % (self.fusion_client._host, response['members'][0]['uri'])
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def make_body(self, body, api=None):
        """
        saslig = { 'name': 'SASLIG1',
                   'type': 'sas-logical-interconnect-group',
                   'enclosureType': 'SY12000',
                   'enclosureIndexes':[1],
                   'interconnectBaySet':'1'
                   'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HPE Synergy 12Gb SAS Connection Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HPE Synergy 12Gb SAS Connection Module'},
                                               ],
                  }

        """
        new_body = copy.deepcopy(body)
        new_body['interconnectMapTemplate'] = self._make_interconnect_map_template_dict(body['interconnectMapTemplate'])

        # API-Version handling
        if not api:
            if BuiltIn().get_variable_value("${X-API-VERSION}") is not None:
                api = BuiltIn().get_variable_value("${X-API-VERSION}")
            else:
                api = self.fusion_client._currentVersion()

        ver = {'299': self._make_body_300,
               '300': self._make_body_300,
               '400': self._make_body_300,
               '500': self._make_body_300,
               '600': self._make_body_300,
               '800': self._make_body_300,
               '1000': self._make_body_300,
               '1200': self._make_body_300}

        if str(api) in ver:
            new_body = ver[str(api)](new_body)
        else:
            msg = "API version %s is not supported" % str(api)
            raise Exception(msg)
        return new_body

    def _make_body_300(self, body):
        # This is the latest request body, no changes needed
        return body

    def _make_interconnect_map_template_dict(self, interconnectMapTemplate):
        template = {'interconnectMapEntryTemplates':
                    [{'logicalLocation':
                      {'locationEntries':
                       [{'type': 'Bay', 'relativeValue': v['bay']},
                        {'type': 'Enclosure', 'relativeValue': v.get('enclosure', 1)}]},
                      'permittedInterconnectTypeUri': v['type'],
                      'enclosureIndex': v.get('enclosureIndex', 1)
                      } for i, v in enumerate(interconnectMapTemplate)],
                    }

        if interconnectMapTemplate:
            # TODO: should check that this object is a dict
            if 'interconnectMapEntryTemplates' in interconnectMapTemplate:  # assume this is an actual template dict already and just return it
                return interconnectMapTemplate
            # TODO: There is probably a more pythonic way to do this check...
            elif 'bay' and 'type' in interconnectMapTemplate.__str__():  # provided bay\interconnect type mapping, build template dict
                itypes = SasInterconnectTypes(self.fusion_client)
                permittedInterconnectTypes = itypes.get()
                for ic in interconnectMapTemplate:
                    if 'uri' in ic.keys():
                        permittedInterconnectTypeUri = ic['uri']
                    else:
                        # Get permittedInterconnectTypeUri
                        permittedInterconnectType = [x for x in permittedInterconnectTypes['members'] if x['name'] == ic['type']]
                        if len(permittedInterconnectType) == 0:
                            raise AssertionError("Interconnect Type Not Found: " + ic['type'])
                        else:
                            permittedInterconnectTypeUri = permittedInterconnectType[0]['uri']
                    for location in template['interconnectMapEntryTemplates']:
                        if location['enclosureIndex'] == ic['enclosureIndex']:
                            entries = location['logicalLocation']['locationEntries']
                            if [x for x in entries if x['type'] == 'Bay' and x['relativeValue'] == int(ic['bay'])]:
                                location['permittedInterconnectTypeUri'] = permittedInterconnectTypeUri
                return template
