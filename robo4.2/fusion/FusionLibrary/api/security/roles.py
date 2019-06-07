#!/usr/local/bin/python
import json


class Roles(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, uri=None, api=None, headers=None, param=''):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/roles%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def add_role_to_group(self, body, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/logindomains/grouptorolemapping' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def del_role_from_group(self, domain=None, group=None, uri=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()

        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        elif domain and group:
            uri = "https://%s/rest/logindomains" % (self.fusion_client._host)
            response = self.fusion_client.get(uri=uri, headers=headers)
            domains = json.loads(response['_content'])
            for adomain in domains:
                if adomain['name'] == domain:
                    logdom_id = adomain['loginDomain']
                    break
            else:
                return None

            group_no_space = group.replace(' ', '$_sp_$')
            uri = 'https://%s/rest/logindomains/grouptorolemapping/%s/%s' % (self.fusion_client._host, logdom_id, group_no_space)

        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response
