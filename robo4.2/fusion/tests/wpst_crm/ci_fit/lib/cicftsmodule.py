#!/usr/local/bin/python
import json
import re
import string
import ast
from common import *
from common import connection
import logging

libLogger = "api-logger"


class ApplianceConfigBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getNetworkInterfaces(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('applNetConfig'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    '''
    This method sets the network-interface config, time and locale in one call.
    '''

    def setNetworkInterfaces(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('applNetConfig'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(reqBody))
        # NEW - return the TaskV2 URL from the location response header
        return response.headers['location']


class ServiceAccessBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def setServiceAccess(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('serviceAccess'))
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response


class FtsBase(object):

    def __init__(self, ip, sessionId=None):
        self.con = connection(ip=ip, sessionId=sessionId)

    def changeInitialPassword(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        data = {'userName': reqBody['name'], 'oldPassword': reqBody['oldPassword'],
                'newPassword': reqBody['newPassword']}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('changePassword'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def saveEula(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        data = {'supportAccess': reqBody['agree']}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('eulaSave'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response
