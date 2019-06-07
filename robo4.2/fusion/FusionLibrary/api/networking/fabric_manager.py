#!/usr/local/bin/python

import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from robot.libraries.BuiltIn import BuiltIn


class FabricManager(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def post(self, body=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/fabric-managers' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        else:
            uri = 'https://%s/rest/fabric-managers%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def delete(self, name=None, uri=None, param='', api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        elif name:
            param = '?&filter="\'name\' == \'%s\'"%s ' % (name, param)
            response = self.get(api=api, headers=headers, param=param)
            if response['count'] == 0:
                logger._log('FM %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s' % (self.fusion_client._host, response['members'][0]['uri'])
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def put(self, body, uri, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def create_fabric_manager_remediate_body(self,
                                             uri,
                                             li_compliance_id=None,
                                             us_compliance_id=None,
                                             nw_compliance_id=None,
                                             nw_set_compliance_id=None,
                                             pvlan_compliance_id=None):
        """
        Creates body for Fabric Manager Remediate API
        """
        if nw_compliance_id is None:
            nw_compliance_list = []
        elif type(nw_compliance_id) is list:
            nw_compliance_list = nw_compliance_id
        else:
            nw_compliance_list = [nw_compliance_id]

        if pvlan_compliance_id is None:
            pvlan_compliance_list = []
        elif type(pvlan_compliance_id) is list:
            pvlan_compliance_list = pvlan_compliance_id
        else:
            pvlan_compliance_list = [pvlan_compliance_id]

        if us_compliance_id is None and nw_set_compliance_id is None:
            us_compliance_list = []
        else:
            us_compliance_list = [{'networks': nw_compliance_list,
                                   'uplinkSetComplianceId': us_compliance_id,
                                   'privateVlansComplianceId': pvlan_compliance_list
                                   }]

        if li_compliance_id is None:
            li_compliance_list = []
        else:
            li_compliance_list = [{'logicalInterconnectComplianceId': li_compliance_id,
                                   'uplinkSets': us_compliance_list
                                   }]

        if nw_set_compliance_id is None:
            nw_set_compliance_list = []
        elif type(nw_set_compliance_id) is list:
            nw_set_compliance_list = nw_set_compliance_id
        else:
            nw_set_compliance_list = [nw_set_compliance_id]

        tenant_list = [{'tenantUri': uri,
                        'networkSets': nw_set_compliance_list,
                        'logicalInterconnects': li_compliance_list
                        }]

        remediate_body = {'tenants': tenant_list,
                          'type': 'RemediateFabricManagerV2'
                          }

        if BuiltIn().get_variable_value("${X-API-VERSION}") is not None:
            api = BuiltIn().get_variable_value("${X-API-VERSION}")
        else:
            api = self.fusion_client._currentVersion()

        ver = {'800': self._make_remediate_body_800,
               '1000': self._make_remediate_body_1000
               }
        if str(api) in ver:
            remediate_body = ver[str(api)](remediate_body)
        else:
            msg = "API version %s is not supported in fabric_manager.create_fabric_manager_remediate_body()" % (str(api))
            raise Exception(msg)

        return remediate_body

    def _make_remediate_body_800(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 800
        '''
        body['type'] = 'RemediateFabricManager'

        for tenant in body['tenants']:
            for li in tenant['logicalInterconnects']:
                for us in li['uplinkSets']:
                    del us['privateVlansComplianceId']
        return body

    def _make_remediate_body_1000(self, body):
        '''
        This modifies\removes the elements that are not valid for API version 1000
        '''
        body['type'] = 'RemediateFabricManagerV2'
        return body
