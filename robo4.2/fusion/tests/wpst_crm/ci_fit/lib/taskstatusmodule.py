#!/usr/local/bin/python
from common import *
from common import connection


class CheckTaskStatus(object):

    def __init__(self, ip, sessionID, taskURI):
        self.con = connection(ip=ip, sessionId=sessionID)

    def getTaskStatus(self, ip, sessionID, taskURI):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, taskURI)
        response = self.con.get(uri=uri, headers=headers)
        return response
