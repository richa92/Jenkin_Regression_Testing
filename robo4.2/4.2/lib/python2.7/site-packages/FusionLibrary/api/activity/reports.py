""" Reports """


class Report(object):
    """ Report methods """

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, reportId=None, api=None, headers=None):
        """ Get report(s) """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/reports/%s' % (self.fusion_client._host, reportId)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response

    def save(self, reportId=None, api=None, headers=None):
        """ Save report """
        if api:
            headers = self.fusion_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.fusion_client._headers.copy()
        uri = 'https://%s/rest/reports/%s/save' % (self.fusion_client._host, reportId)
        response = self.fusion_client.get(uri=uri, headers=headers)
        return response
