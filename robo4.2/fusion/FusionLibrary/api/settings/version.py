#!/usr/local/bin/python


class Version(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, api=None, headers=None):
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/version' % (self.fusion_client._host)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def set(self, api=None):
        """
        Sets the X-API-Version header to the specified value for all future requests.
        If no value is supplied, the value of ${X-API-Version} is used
        if it exists else the appliances current version is queried and used
        :param api:
        :return:
        """
        return self.fusion_client.set_def_api_version(api=api)
