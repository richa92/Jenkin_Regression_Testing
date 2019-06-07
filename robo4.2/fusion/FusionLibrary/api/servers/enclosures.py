#!/usr/local/bin/python

import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from FusionLibrary.api.servers.enclosure_groups import EnclosureGroup


class Enclosure(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    # X-API-Version = 4
    def _make_body_4(self, enc):
        body = {'hostname': enc.get('hostname', None),
                'username': enc.get('username', None),
                'password': enc.get('password', None),
                'enclosureGroupUri': enc.get('enclosureGroupUri', None),
                'force': enc.get('force', False),
                'licensingIntent': enc.get('licensingIntent', "OneView")}

        if 'firmwareBaselineUri' in enc:
            body['firmwareBaselineUri'] = enc.get('firmwareBaselineUri')
            if 'updateFirmwareOn' in enc:
                body['updateFirmwareOn'] = enc.get('updateFirmwareOn', "EnclosureOnly")

        return body

    # X-API-Version = 101
    def _make_body_101(self, enc):
        body = {'hostname': enc.get('hostname', None),
                'username': enc.get('username', None),
                'password': enc.get('password', None),
                'enclosureGroupUri': enc.get('enclosureGroupUri', None),
                'force': enc.get('force', False),
                'licensingIntent': enc.get('licensingIntent', "OneView")}

        if 'firmwareBaselineUri' in enc:
            body['firmwareBaselineUri'] = enc.get('firmwareBaselineUri')
            if 'updateFirmwareOn' in enc:
                body['updateFirmwareOn'] = enc.get('updateFirmwareOn', "EnclosureOnly")
                body['forceInstallFirmware'] = enc.get('forceInstallFirmware', False)

        return body

    def make_body(self, api, body, enc_grp_name):

        enc_grps = EnclosureGroup(self.fusion_client)
        encgrps = enc_grps.get()

        for encgrp in encgrps['members']:
            if encgrp['name'] == enc_grp_name:
                body['enclosureGroupUri'] = encgrp['uri']
                break
        if 'enclosureGroupUri' not in body:
            logger._log('Enclosure group %s does not exist' % enc_grp_name, level='WARN')

        ver = {3: self._make_body_4,
               4: self._make_body_4,
               101: self._make_body_101}

        # run the corresponding function
        if api in ver:
            return ver[api](body)
        else:
            # TODO: might want special handling other than Exception
            msg = "API version %d is not supported" % (api)
            raise Exception(msg)

    def add(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/enclosures' % (self.fusion_client._host)
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

    def post(self, body, uri, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
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

    def put(self, body, uri, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s%s' % (self.fusion_client._host, uri)
        response = self.fusion_client.put(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, name=None, uri=None, api=None, headers=None, param=''):
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
                logger._log('Enclosure %s does not exist' % (name), level='WARN')
                return
            elif response['count'] > 1:
                msg = "Filter %s returned more than one result" % (name)
                raise Exception(msg)
            else:
                uri = 'https://%s%s%s' % (self.fusion_client._host, response['members'][0]['uri'], param)
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
            uri = 'https://%s/rest/enclosures%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
