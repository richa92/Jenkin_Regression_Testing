#!/usr/local/bin/python
import json
import re
import string
import ast
from common import *
from common import connection
import logging
import pprint
import pdb
libLogger = "api-logger"


class TaskBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getTask(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uri)
        response = self.con.get(uri=uri, headers=headers)
        return response
