#!/usr/local/bin/python


class ApplianceState(object):

    def __init__(self, fusion_client):
        self.fusion_client = fusion_client

    def get(self, appliance):
        uri = 'https://%s/controller-state.json' % appliance
        response = self.fusion_client.post(uri=uri)
        return response
