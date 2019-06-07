#!/usr/local/bin/python


class ServiceAccess(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def save(self, host, status='enabled', api=None, headers=None):
        # api-doc states that this is a boolean but not.
        # a defect was opened and to workaround it, string is being used instead of boolean here.
        # OVD15974 [CI-FIT] Api-doc and actual behavior not matching up for PUT /rest/appliance/settings/enableServiceAccess request body
        body = {'enabled': 'true', 'disabled': 'false'}
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/appliance/settings/enableServiceAccess' % (host)
        response = self.fusion_client.put(uri=uri, headers=headers, body=body[status])
        return response

    def get(self, host=None, uri=None, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s' % (self.fusion_client._host, uri)
        else:
            uri = 'https://%s/rest/appliance/settings/serviceaccess' % (self.fusion_client._host)
        if host:
            uri = 'https://%s/rest/appliance/settings/serviceaccess' % (host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
