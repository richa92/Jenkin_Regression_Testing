# !/usr/local/bin/python
"""
certificate_authority.py
"""
import json


class CertificateAuthority(object):
    """
    This is class for Performing
    revoke,get,add,delete and upload
    operations on CA certificates
    """

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def revoke(self, name=None, api=None, headers=None):
        """
        Performing revoke operations on CA certificates
        :param name:
        :param api:
        :param headers:
        :return:
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/ca/%s' % (self.fusion_client._host, name)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def get(self, uri=None, api=None, headers=None, param=''):
        """
        Performing get operations on CA certificates
        :param name:
        :param api:
        :param headers:
        :param param:
        :return:
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        if uri:
            uri = 'https://%s%s%s' % (self.fusion_client._host, uri, param)
        else:
            uri = 'https://%s/rest/certificates/ca/%s' % (self.fusion_client._host, param)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def add(self, body, api=None, headers=None):
        """
        Performing add operations on CA certificates
        :param body:
        :param api:
        :param headers:
        :return:
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/ca/' % (self.fusion_client._host)
        response = self.fusion_client.post(uri=uri, headers=headers, body=json.dumps(body))
        return response

    def delete(self, FriendlyName, api=None, headers=None):
        """
        Performing delete operations on CA certificates
        :param FriendlyName:
        :param api:
        :param headers:
        :return:
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/certificates/ca/%s' % (self.fusion_client._host, FriendlyName)
        response = self.fusion_client.delete(uri=uri, headers=headers)
        return response

    def upload(self, aliasname, localfile=None, api=None,
               headers=None, f_type='application/pkix-crl'):
        """
        Performing upload operations on CA certificates
        :param aliasname:
        :param localfile:
        :param api:
        :param headers:
        :param type:
        :return:
        """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        headers['Content-Type'] = 'multipart/form-data'
        uri = 'https://%s/rest/certificates/ca/%s/crl' % (self.fusion_client._host, aliasname)
        response = self.fusion_client.put_file(uri=uri, localfile=localfile,
                                               headers=headers, f_type=f_type)
        return response
