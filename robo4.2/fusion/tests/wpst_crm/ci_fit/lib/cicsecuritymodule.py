#!/usr/local/bin/python
import json
import re
import string
import logging
from common import *
from common import connection
import pprint
libLogger = "api-logger"


class LoginSession(object):

    def __init__(self, ip, uname, pw):
        self.con = connection(ip=ip, sessionId=None)
        self.uname = uname
        self.pw = pw

    def post(self):
        global uris
        log = logging.getLogger(libLogger)
        data = {'userName': self.uname, 'password': self.pw}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('loginSessions'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response['sessionID']


class UsersBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getUsers(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('users'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('users'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getRoles(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('roles'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('roles'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def createUser(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        # 'type': 'UserAndRoles',
        data = {'type': 'UserAndRoles', 'userName': reqBody['name'], 'password': reqBody['pw'],
                'fullName': reqBody['fullname'], 'emailAddress': reqBody['email'],
                'officePhone': reqBody['ophone'], 'mobilePhone': reqBody['mphone'],
                'roles': [reqBody['role']], 'enabled': 'true'}
        uri = 'https://%s%s' % (self.con._ip, uris.get('users'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def deleteUser(self, user):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('users'), user)
        response = self.con.delete(uri=uri, headers=headers)
        return response

# deprecated for API version 4 or greater
    def createUserRole(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        data = {'userName': reqBody['name'], 'roles': [reqBody['role']]}
        uri = 'https://%s%s' % (self.con._ip, uris.get('roles'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response
