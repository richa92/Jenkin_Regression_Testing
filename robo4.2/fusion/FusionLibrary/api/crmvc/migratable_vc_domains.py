import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class MigratableVcDomain(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def make_body(self, credentialDict, migrationVars=None, iloLicenseType='OneViewNoiLO', api=None, headers=None):
        body = {'type': 'migratable-vc-domains',
                'category': 'migratable-vc-domains',
                'iloLicenseType': iloLicenseType,
                'credentials': {
                    'oaIpAddress': credentialDict['oaIpAddress'],
                    'oaUsername': credentialDict['oaUsername'],
                    'oaPassword': credentialDict['oaPassword'],
                    'vcmIpAddress': credentialDict['vcmIpAddress'],
                    'vcmUsername': credentialDict['vcmUsername'],
                    'vcmPassword': credentialDict['vcmPassword'],
                    'type': 'EnclosureCredentials'}
                }

        versionType = {'300': 'MigratableVcDomainV300',
                       '500': 'MigratableVcDomainV300',
                       '600': 'MigratableVcDomainV300'}

        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()

        if str(headers['X-Api-Version']) in versionType:
            body['type'] = versionType[str(headers['X-Api-Version'])]

        if migrationVars:
            for key, value in migrationVars.iteritems():
                body[key] = value
        return body

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/migratable-vc-domains' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def build_create(self, credentialDict, migrationVars=None, iloLicenseType='OneViewNoiLO', api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/migratable-vc-domains' % (self.fusion_client._host)
        body = self.make_body(credentialDict, migrationVars, iloLicenseType)
        response = self.create(body, api, headers)
        return response

    def get(self, uri, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if param:
            uri = 'https://%s%s/%s' % (self.fusion_client._host, uri, param)
        else:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def update(self, uri, body=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()

        versionBody = {'300': self._make_body_300,
                       '500': self._make_body_500,
                       '600': self._make_body_500}

        if not body:
            body = {'migrationState': 'Migrated', 'type': 'migratable-vc-domains'}
            if str(headers['X-Api-Version']) in versionBody:
                body = versionBody[str(headers['X-Api-Version'])](body)
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, uri=None, api=None, headers=None):
        # TODO
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            param = '?&filter="\'name\' == \'%s\'"' % (name)
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

    def _make_body_300(self, body):
        '''
        This modifies and or remove attributes as needed for X-Api-Version 300
        '''
        body['type'] = 'MigratableVcDomainV300'
        body['acknowledgements'] = [{'key': 'VirtualConnectBackup'}, {'key': 'ResourcesNotModified'}, {'key': 'InServiceMigration'}, {'key': 'Bios'}, {'key': 'Sriov'}, {'key': 'ProfileNotMigrated'}]
        return body

    def _make_body_500(self, body):
        '''
        This modifies and or remove attributes as needed for X-Api-Version 500
        '''
        body['type'] = 'MigratableVcDomainV300'
        body['acknowledgements'] = [{'key': 'VirtualConnectBackup'}, {'key': 'ResourcesNotModified'}, {'key': 'InServiceMigration'}, {'key': 'Bios'}, {'key': 'Sriov'}, {'key': 'ProfileNotMigrated'}, {'key': 'LatentServerError'}]
        return body
