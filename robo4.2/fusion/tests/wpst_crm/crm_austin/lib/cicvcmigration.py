#!/usr/local/bin/python
# (C) Copyright 2013 Hewlett-Packard Development Company, L.P.
# import requests
import json
import warnings
# from FusionLibrary.api.crmvc.cicutils import ResourceBase
# from FusionLibrary.api.wpst_crm.lib.common import uris
# from RoboGalaxyLibrary.utilitylib import logging as logger
# there are some annoying warning with paramiko so we import the warnings
# module and ignore them
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

from common import connection, TaskBase


libLogger = "api-logger"

# import pdb


class VcMigrationMgr (object):

    def __init__(self, ip, sessionId, version='V2'):
        self.ip = ip
        self.sessionId = sessionId
        self.con = connection(ip=self.ip, sessionId=self.sessionId)
        self.version = version
        self.uriDict = dict()
        self.uriDict = {'V1': {'type': 'domain-compatibility', 'category': 'domain-compatibility', 'domainCompatibilityUri': 'rest/domain-compatibility'},
                        'V2': {'migrationState': 'Migrated', 'type': 'migratable-vc-domains', 'category': 'migratable-vc-domains', 'domainCompatibilityUri': 'rest/migratable-vc-domains'}}

        self._setRestVersion(version)
        self.migrationData = {'name': {'encGrp': 'enclosureGroupName', 'lig': 'logicalInterconnectGroupName'},
                              'uri': {'encGrp': 'enclosureGroupUri', 'lig': 'logicalInterconnectGroupUri'}}

    def _setRestVersion(self, version=None):

        if (version == 'V1'):
            logger._log_to_console_and_log_file(
                'Setting VC Migration Manager Rest Interface to V1')
            self.restVersion = 'V1'
        else:
            logger._log_to_console_and_log_file(
                'Setting VC Migration Manager Rest Interface to V2')
            self.restVersion = 'V2'

    def _getRestInterface(self, version=None):
        restDict = dict()
        if not version == self.version:
            restDict = self.uriDict[self.restVersion]
        else:
            restDict = self.uriDict[self.restVersion]

        return restDict

    def createDomainCompatibility(self, reqBody, migrationVars=None, iloLicenseType='OneViewNoiLO', watchTask=True, version=None):
        global uris

        restDict = self._getRestInterface(version)

        data = {'type': restDict['type'], 'category': restDict['category'], 'iloLicenseType': iloLicenseType,
                'credentials': {'oaIpAddress': reqBody['oaIpAddress'], 'oaUsername': reqBody['oaUsername'], 'oaPassword': reqBody['oaPassword'],
                                'vcmIpAddress': reqBody['vcmIpAddress'], 'vcmUsername': reqBody['vcmUsername'], 'vcmPassword': reqBody['vcmPassword'],
                                'type': 'EnclosureCredentials'}}
        if migrationVars:
            for key, value in migrationVars.iteritems():
                data[key] = value

        headers = self.con._headers.copy()
        uri = 'https://%s/%s' % (self.con._ip,
                                 restDict['domainCompatibilityUri'])
        response = self.con.post(
            uri=uri, headers=headers, body=json.dumps(data))

        if watchTask:
            self.task = TaskBase(ip=self.ip, sessionId=self.sessionId)
            self.task.waitTask(uri=response['uri'], interval=10)
            taskResponse = self.task.getTask(uri=response['uri'])
            associatedResourceUri = taskResponse[
                'associatedResource']['resourceUri']
            return associatedResourceUri
        else:
            self.task = TaskBase(ip=self.ip, sessionId=self.sessionId)
            taskResponse = self.task.getTask(uri=response['uri'])
            if taskResponse['associatedResource']['resourceUri'] is None:
                return ''
            else:
                return taskResponse['associatedResource']['resourceUri']

    def getDomainCompatibilitybyId(self, uriid, detail=True):
        global uris

        headers = self.con._headers.copy()
        if detail:
            uri = 'https://%s%s%s' % (self.con._ip, uriid, '/?view=detail')
        else:
            uri = 'https://%s%s' % (self.con._ip, uriid)

        response = self.con.get(uri=uri, headers=headers)
        return response

    def renameEncGroup(self, uri, name):
        global uris

        headers = self.con._headers.copy()
        data = {'name': name, 'type': 'EnclosureGroupV2'}
        uri = 'https://%s%s' % (self.con._ip, uri['enclosureGroupUri'])
        response = self.con.put(
            uri=uri, headers=headers, body=json.dumps(data))
        return response

    def _importDomainCompatibilitybyId(self, uriid, watchTask=True):
        global uris
        headers = self.con._headers.copy()
        uri = 'https://%s%s/import' % (self.con._ip, uriid)
        response = self.con.get(uri=uri, headers=headers)
        if watchTask:
            self.task = TaskBase(ip=self.ip, sessionId=self.sessionId)
            self.task.waitTask(
                uri=response['uri'], interval=20, time_out=1200, hasChildren=True)

    def importDomainCompatibilitybyId(self, uriid, watchTask=True):
        global uris

        if self.restVersion == 'V2':
            uriInfo = self._getRestInterface(self.restVersion)
            data = {'migrationState': uriInfo[
                'migrationState'], 'type': uriInfo['type']}
            headers = self.con._headers.copy()
            uri = 'https://%s%s' % (self.con._ip, uriid)
            body = json.dumps(data)
            response = self.con.put(
                uri=uri, headers=headers, body=json.dumps(data))

            if watchTask:
                self.task = TaskBase(ip=self.ip, sessionId=self.sessionId)
                self.task.waitTask(
                    uri=response['uri'], interval=20, time_out=1200, hasChildren=True)
        else:
            self._importDomainCompatibilitybyId(uriid=uriid, watchTask=True)

    def getActivityTasks(self, count, Filter=None):
        global uris
        headers = self.con._headers.copy()
        if filter == "\"\"":
            uri = 'https://%s%s?&sort=created:descending' % (
                self.con._ip, uris.get('activity-tasks'))
        else:
            uri = 'https://%s%s?&sort=created:descending&filter=%s' % (
                self.con._ip, uris.get('activity-tasks'), Filter)
        response = self.con.get(uri=uri, headers=headers)

        return response

    def getReports(self):
        reports = dict()
        headers = self.con._headers.copy()
        response = dict()
        items = 1

        while 'errorCode' not in response.keys():
            uri = 'https://%s%s%s' % (self.con._ip, '/rest/reports/', items)
            response = self.con.get(uri=uri, headers=headers)

            if 'errorCode' not in response.keys():
                reports[response['name']] = response
            items = items + 1
        return reports
