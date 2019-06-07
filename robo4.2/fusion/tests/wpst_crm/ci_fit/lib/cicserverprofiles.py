#!/usr/local/bin/python
import requests
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


class ProfileBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def createProfile(self, profile, connections,
                      bootorder, firmware, bios, localstorage=None, sanstorage=None):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'ServerProfileV3', 'name': profile['profile'], 'description': profile['description'],
                'serverHardwareUri': profile['serverHardwareUri'], 'serverHardwareTypeUri': profile['serverHardwareTypeUri'],
                'enclosureGroupUri': profile['enclosureGroupUri'], 'connectionSettings': {'connections': connections},
                'macType': profile['mac'], 'serialNumberType': profile['serial'], 'wwnType': profile['wwn'],
                'firmware': firmware, 'bios': bios, 'boot': bootorder, 'sanStorage': sanstorage}

        if localstorage:
            data['localStorage'] = localstorage

        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('profiles'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def deleteProfile(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('profiles'), uri)
        response = self.con.delete(uri=uri, headers=headers)
        return response

    def deleteProfiles(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('profiles'), filter)
        else:
            uri = 'https://%s%s?filter=' % (self.con._ip, uris.get('profiles'))
        response = self.con.delete(uri=uri, headers=headers)
        return response

    def assignProfile(self, profile):
        global uris
        log = logging.getLogger(libLogger)

        data = {'type': 'ServerProfileV3', 'name': profile['name'], 'description': profile['description'],
                'serverHardwareUri': profile['serverHardwareUri'], 'serverHardwareTypeUri': profile['serverHardwareTypeUri'],
                'enclosureGroupUri': profile['enclosureGroupUri'], 'connectionSettings': {'connections': profile['connectionSettings']['connections']},
                'macType': profile['macType'], 'serialNumberType': profile['serialNumberType'], 'wwnType': profile['wwnType'],
                'firmware': profile['firmware'], 'bios': profile['bios'], 'boot': profile['boot'],
                'localStorage': profile['localStorage'], 'sanStorage': profile['sanStorage']}
        headers = self.con._headers.copy()
        headers['if-match'] = profile['eTag']

        uri = 'https://%s%s' % (self.con._ip, profile['uri'])
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def unassignProfile(self, profile):
        global uris
        log = logging.getLogger(libLogger)

        data = {'type': 'ServerProfileV3', 'name': profile['name'], 'description': profile['description'],
                'serverHardwareUri': None, 'serverHardwareTypeUri': profile['serverHardwareTypeUri'],
                'enclosureGroupUri': profile['enclosureGroupUri'], 'connectionSettings': {'connections': profile['connectionSettings']['connections']},
                'macType': profile['macType'], 'serialNumberType': profile['serialNumberType'], 'wwnType': profile['wwnType'],
                'firmware': profile['firmware'], 'bios': profile['bios'], 'boot': profile['boot'],
                'localStorage': profile['localStorage'], 'sanStorage': profile['sanStorage']}

        headers = self.con._headers.copy()
        headers['if-match'] = profile['eTag']

        uri = 'https://%s%s' % (self.con._ip, profile['uri'])
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getProfile(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uri)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getProfiles(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('profiles'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('profiles'))
        response = self.con.get(uri=uri, headers=headers)
        return response
