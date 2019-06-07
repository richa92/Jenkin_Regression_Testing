import json
from RoboGalaxyLibrary.utilitylib import logging as logger


class LogicalEnclosure(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/logical-enclosures' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def put(self, body, uri, param='', api=None, headers=None, etag=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if etag:
            headers['If-Match'] = str(etag)
        uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def patch(self, body, uri, api=None, headers=None, etag=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if etag:
            headers['If-Match'] = str(etag)
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.patch(uri=uri, headers=headers, body=json.dumps(body))
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
                logger._log('Logical Enclosure %s does not exist' % (name), level='WARN')
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
            uri = 'https://%s/rest/logical-enclosures%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def make_body(self,
                  name,
                  api=None,
                  enclosureGroupUri=None,
                  enclosureUris=[],
                  firmwareBaselineUri="",
                  forceInstallFirmware=0):

        body = {'name': name,
                'enclosureGroupUri': enclosureGroupUri,
                'enclosureUris': enclosureUris,
                'firmwareBaselineUri': firmwareBaselineUri,
                'forceInstallFirmware': forceInstallFirmware}

        # API-Version handling
        if not api:
            api = self.fusion_client._currentVersion()

        ver = {200: self._make_body_200,
               299: self._make_body_299,
               300: self._make_body_300}

        # run the corresponding function
        if api in ver:
            body = ver[api](body)
        else:
            # TODO: might want special handling other than Exception
            msg = "API version %d is not supported" % (api)
            raise Exception(msg)
        return body

    # X-API-Version = 200
    def _make_body_200(self, body):
        return body

    def _make_body_299(self, body):
        return body

    def _make_body_300(self, body):
        return body

    def get_support_dump(self, body, le_id, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if le_id:
            uri = 'https://%s/rest/logical-enclosures/%s/support-dumps' % (self.fusion_client._host, le_id)
        else:
            msg = "Logical Enclosure id is required for support dump"
            raise Exception(msg)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response
