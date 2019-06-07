#!/usr/local/bin/python
import json
from RoboGalaxyLibrary.utilitylib import logging as logger
from docutils.parsers.rst.directives import body
from i3SLibrary.api import common


class DeploymentGroup(object):

    def __init__(self, i3s_client):
        self.i3s_client = i3s_client

    def get(self, uri=None, api=None, headers=None):
        if api:
            headers = self.i3s_client._set_req_api_version(api=api)
        elif not headers:
            headers = self.i3s_client._headers
        if uri:
            uri = 'https://%s%s' % (self.i3s_client._host, uri)
        else:
            uri = 'https://%s%s' % (self.i3s_client._host, common.uris.get('deploymentgrp'))
        response = self.i3s_client.get(uri=uri, headers=self.i3s_client._headers)
        return response