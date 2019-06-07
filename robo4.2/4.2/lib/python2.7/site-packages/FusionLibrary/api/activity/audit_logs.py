""" Audit logs keywords """
import json


class AuditLog(object):
    """ Audit logs keywords """
    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def create(self, body=None, api=None, headers=None):
        """ Create audit log item """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/audit-logs' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def download(self, api=None, headers=None):
        """ Download the audit logs """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/audit-logs/download' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def get(self, api=None, headers=None):
        """ Get the audit logs """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers
        uri = 'https://%s/rest/audit-logs' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
