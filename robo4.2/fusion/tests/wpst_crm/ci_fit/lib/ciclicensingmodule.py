#!/usr/local/bin/python
import json
import re
import string
from common import *
from common import connection
import logging

libLogger = "api-logger"


class LicensesBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addLicense(self, key):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'License', 'key': key}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('licenses'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getLicenses(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('licenses'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('licenses'))
        response = self.con.get(uri=uri, headers=headers)
        return response
