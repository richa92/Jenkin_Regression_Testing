#!/usr/local/bin/python
import requests
import json
import re
import string
from common import *
from common import connection
import logging
import pprint
libLogger = "api-logger"


class EncBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addEnc(self, reqBody, encGrpUri):
        global uris
        log = logging.getLogger(libLogger)
        data = {'hostname': reqBody['oahostname'], 'username': reqBody['oausername'],
                'password': reqBody['oapassword'], 'enclosureGroupUri': encGrpUri,
                'licensingIntent': reqBody['licensingintent'], 'force': reqBody['force']}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('enclosures'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def listEnc(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('enclosures'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('enclosures'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getEnc(self, uuid):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('enclosures'), uuid)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def removeEnc(self, encUri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('enclosures'), encUri)
        response = self.con.delete(uri=uri, headers=headers)
        return response


class EncPreview(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def previewEnc(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        data = {'hostname': reqBody['oahostname'], 'username': reqBody['oausername'],
                'password': reqBody['oapassword'], 'ligPrefix': reqBody['group'],
                'force': 'false', 'logicalInterconnectGroupNeeded': 'true'}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('enclosurePreview'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response['logicalInterconnectGroup']


class EncGrpBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addEncGrp(self, encGrpName, ligUri):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'EnclosureGroupV2', 'name': encGrpName, 'interconnectBayMappings':
                [{'interconnectBay': '1', 'logicalInterconnectGroupUri': ligUri},
                 {'interconnectBay': '2', 'logicalInterconnectGroupUri': ligUri},
                 {'interconnectBay': '3', 'logicalInterconnectGroupUri': ligUri},
                 {'interconnectBay': '4', 'logicalInterconnectGroupUri': ligUri},
                 {'interconnectBay': '5', 'logicalInterconnectGroupUri': ligUri},
                 {'interconnectBay': '6', 'logicalInterconnectGroupUri': ligUri},
                 {'interconnectBay': '7', 'logicalInterconnectGroupUri': ligUri},
                 {'interconnectBay': '8', 'logicalInterconnectGroupUri': ligUri}],
                'interconnectBayMappingCount': '8',
                'stackingMode': 'Enclosure'}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('enclosureGroups'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response['uri']

    def listEncGroups(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('enclosureGroups'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('enclosureGroups'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def deleteEncGrp(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('enclosureGroups'), uri)
        response = self.con.delete(uri=uri, headers=headers)
        return response


class ServerHwBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def listServerHw(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('servers'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('servers'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getServer(self, uuid):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('servers'), uuid)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def setServerPower(self, uuid, powerState, powerControl):
        global uris
        log = logging.getLogger(libLogger)
        data = {'powerState': powerState, 'powerControl': powerControl}
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s/powerState' % (self.con._ip, uris.get('servers'), uuid)
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response
'''
class EnclosureDetails(object):
    def __init__(self, ip, uname, pw):
        self.con._ip = ip
        self.uname = uname
        self.pw = pw

    def encDetails(self):
        data = {'userName': self.uname, 'password': self.pw}
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Content-Type': 'application/json'}
        sessionUrl = string.Template("https:/$ip/rest/enclosures?start=0&count=-1")
        sessionUrl = sessionUrl.substitute(ip=self.con._ip)

        # TODO Remove print and exit statements and use the libLogger
        print "sessionUrl = ", sessionUrl
        try:
            r = requests.post(sessionUrl, data=json.dumps(data), headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to gather enclosure details"
            raise Exception(msg, e)

        if r.status_code == 200:
            print r.text
        else:
            print "Error calling request.post for metric URL", r.status_code
            exit (1)
        return r.text


    def encUUID(self):
        data = {'userName': self.uname, 'password': self.pw}
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Content-Type': 'application/json'}
        uuidUrl = string.Template("https://$ip/rest/enclosures?start=0&count=-1")
        uuidUrl = uuidUrl.substitute(ip=self.con._ip)

    try:
        r = requests.get(uuidUrl, auth=self.sessionId, data=jason.dumps(data), headers=headers, verify=False)
        except:
        msg = "Exception occured while attempting to get uuid"
        raise Exception(msg, e)

        # TODO Remove print and exit statements and use the libLogger
        if r.status_code == 200:
            print "uuidUrl worked"
        else:
            print "Error calling request.post for metric URL", r.status_code
            exit (1)

        # TODO Remove re matching and use the dictionary index of the json() response
        if r.text.find("uuid"):
            fields = r.text.split(",")
            encUuidPair = re.sub('[\"}]', '',fields[2])
            print "encUuidPair = ", encUuidPair

            theUuid = encUuidPair.split(":")
            theUuid = re.sub('[\"}]', '',theUuid[1])
            print "found uuid"
        else:
            print "uuid not found"

    return theUuid
'''
