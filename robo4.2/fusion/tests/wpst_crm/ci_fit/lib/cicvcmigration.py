#!/usr/local/bin/python
import requests
import json
from common import *
from common import connection
import logging
libLogger = "api-logger"

import pdb


class VcMigrationMgr (object):

    def __init__(self, ip, sessionId):
        self.ip = ip
        self.sessionId = sessionId
        self.con = connection(ip=self.ip, sessionId=self.sessionId)

    def createDomainCompat(self, reqBody, watchTask=False):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'domain-compatibility', 'category': 'domain-compatibility',
                'credentials': {'oaIpAddress': reqBody['oaIpAddress'], 'oaUsername': reqBody['oaUsername'], 'oaPassword': reqBody['oaPassword'],
                                'vcmIpAddress': reqBody['vcmIpAddress'], 'vcmUsername': reqBody['vcmUsername'], 'vcmPassword': reqBody['vcmPassword'],
                                'type': 'VCMDataCredentials'}}

        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('domain-compatibility'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))

        if watchTask:
            self.task = TaskBase(ip=self.ip, sessionId=self.sessionId)
            self.task.waitTask(uri=response['uri'], interval=2)
        return

    def getDomainCompat(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('domain-compatibility'))
        response = self.con.get(uri=uri, headers=headers)
        return response
