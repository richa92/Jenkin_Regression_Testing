#!/usr/local/bin/python
import requests
import json
import re
import string
from common import *
import logging
import pprint
import time
libLogger = "api-logger"


class ArrayBase (object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addArray(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        data = {'ip_hostname': reqBody['ip'],
                'username': reqBody['username'],
                'password': reqBody['password']}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('storage-systems'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getArrays(self, arrayUri=None, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        if arrayUri:
            uri = 'https://%s%s/%s' % (self.con._ip, uris.get('storage-systems'), arrayUri)
        elif filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('storage-systems'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('storage-systems'))

        response = self.con.get(uri=uri, headers=headers)
        return response

    def updateArray(self, arrayUri, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('storage-systems'), arrayUri)
        headers = self.con._headers.copy()
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response

    def removeArray(self, arrayUri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s%s' % (self.con._ip, uris.get('storage-systems'), arrayUri)
        response = self.con.delete(uri=uri, headers=headers)
        return response

    # TODOtyler remove these two functions?
    def updatePorts(self, reqBody):
        log = logging.getLogger(libLogger)

    def getPorts(self, portUri=None):
        log = logging.getLogger(libLogger)

    # TODOtyler add refresh call?


class PoolBase (object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addPools(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        # TODOtyler can one pool be added when multiResource=true? does that parameter need to exist?
        uri = 'https://%s%s/?multiResource=true' % (self.con._ip, uris.get('storage-pools'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response

    def getPools(self, poolUri=None, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        if poolUri:
            uri = 'https://%s%s/%s' % (self.con._ip, uris.get('storage-pools'), poolUri)
        elif filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('storage-pools'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('storage-pools'))

        response = self.con.get(uri=uri, headers=headers)
        return response

    def removePool(self, poolUri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('storage-pools'))
        response = self.con.delete(uri=uri, headers=headers)
        return response

    # TODOtyler add refresh call?


class VolumeBase (object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addVolume(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        # Set request body, headers, and request URL
        data = {'name': reqBody['name'],
                'description': reqBody['description'],
                'type': 'StorageVolume',
                'templateUri': reqBody['templateUri'], 'provisioningParameters':
                {'storagePoolUri': reqBody['storagePoolUri'], 'requestedCapacity': reqBody['capacity'],
                 'provisionType': reqBody['type'], 'shareable': reqBody['share']}
                }
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('storage-volumes'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getVolumes(self, volumeUri=None, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        if volumeUri:
            uri = 'https://%s%s/%s' % (self.con._ip, uris.get('storage-volumes'), volumeUri)
        elif filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('storage-volumes'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('storage-volumes'))

        response = self.con.get(uri=uri, headers=headers)
        return response

    # getAttachableVols HAS NOT BEEN TESTED
    def getAttachableVols(self, sanIds):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        # Create the query string
        query = "[?query=\"availableNetworks IN ["
        fcnet = uris.get('fcnet')
        for san in sanIds:
            sanUri = '\'%s/%s\',' % (fcnet, san)
        query = query[:-1]
        query += "]\"]"

        uri = 'https://%s%s%s' % (self.con._ip, uris.get('attachable-volumes'), query)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def updateVolume(self, volumeUri, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, volumeUri)
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response

    def removeVolume(self, volumeUri, exportOnly=False):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if exportOnly:
            headers['exportOnly'] = 'true'

        uri = 'https://%s%s' % (self.con._ip, volumeUri)
        response = self.con.delete(uri=uri, headers=headers)
        return response

    def getVolAttached(self, volumeAttachedUri=None, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        if volumeAttachedUri:
            uri = 'https://%s%s/%s' % (self.con._ip, uris.get('volume-attachments'), volumeAttachedUri)
        elif filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('volume-attachments'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('volume-attachments'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def addVolAttachments(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        # Set request body, headers, and request URL
        # As per the mocks arrayports will never be passed manually in 1.1.
        data = {'storageVolumeUri': reqBody['volUri'],
                'serverProfileUri': reqBody['serverprofileUri'],
                'osType': reqBody['ostype'],
                'lun': reqBody['lunNum'], 'paths':
                [{'hostPort': reqBody['hostport'], 'arrayPorts': [],
                  'expectedNetworkUri': reqBody['expectedNetworkUri'], 'enabled': reqBody['enabled'], 'transport': reqBody['transport']}]
                }
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('volume-attachments'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def updateVolAttachments(self, volumeAttachUri, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, volumeAttachUri)
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response

    def removeVolAttachments(self, volumeAttachUri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, volumeAttachUri, '?force=true')
        response = self.con.delete(uri=uri, headers=headers)
        return response


class TemplateBase (object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addTemplate(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        # Set request body, headers, and request URL
        data = {'name': reqBody['name'],
                'description': reqBody['description'],
                'type': 'StorageVolumeTemplate',
                'provisioning':
                {'storagePoolUri': reqBody['storagePoolUri'], 'capacity': reqBody['capacity'],
                 'provisionType': reqBody['provisionType'], 'shareable': reqBody['share'], }
                }
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('volume-templates'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getTemplates(self, templateUri=None, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        if templateUri:
            uri = 'https://%s%s/%s' % (self.con._ip, uris.get('volume-templates'), templateUri)
        elif filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('volume-templates'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('volume-templates'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def updateTemplate(self, templateUri, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('volume-templates'), templateUri)
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response

    def removeTemplate(self, templateUri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('volume-templates'), templateUri)
        response = self.con.put(uri=uri, headers=headers)
        return response


class SANManagerBase (object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def addSANManager(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        # Set request body, headers, and request URL
        data = {'connectionInfo': [
                {'name': 'Host', 'displayName': 'Host',
                 'required': 'true', 'value': reqBody['host'],
                 'valueType':'String', 'valueFormat':'IPAddressOrHostname'},
                {'name': 'Port', 'displayName': 'Port',
                 'required': 'true', 'value': reqBody['port'],
                 'valueType':'Integer', 'valueFormat':'None'},
                {'name': 'Username', 'displayName': 'Username',
                 'required': 'true', 'value': reqBody['username'],
                 'valueType':'String', 'valueFormat':'None'},
                {'name': 'Password', 'displayName': 'Password',
                 'required': 'true', 'value': reqBody['password'],
                 'valueType':'String', 'valueFormat':'SecuritySensitive'},
                {'name': 'UseSsl', 'displayName': 'UseSsl',
                 'required': 'true', 'value': reqBody['usessl'],
                 'valueType':'Boolean', 'valueFormat':'None'}]
                }

        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, (reqBody['devicemanagerUri']))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getProvider(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        uri = 'https://%s%s' % (self.con._ip, uris.get('providers'))
        response = self.con.get(uri=uri, headers=headers)

        return response

    def getSANs(self, managedSansUri=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        if managedSansUri:
            uri = 'https://%s%s/%s' % (self.con._ip, managedSansUri)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('managed-SANS'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def removeSANManager(self, SANManagerUri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, SANManagerUri)
        response = self.con.delete(uri=uri, headers=headers)
        return response
