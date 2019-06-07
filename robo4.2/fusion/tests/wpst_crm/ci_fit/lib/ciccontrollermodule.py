#!/usr/local/bin/python
import requests
import json
import string
import ast
from common import *
from common import connection
import logging
import os
import pprint

libLogger = "api-logger"


class NetworkConfig(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getNodeName(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('applConfig'))
        response = self.con.get(uri=uri, headers=headers)
        return response


class VersionBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getNodeVersion(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('applNodeVersion'))
        response = self.con.get(uri=uri, headers=headers)
        return response


class BackupAppliance(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)
        self.sessionID = self.con._sessionId

    def backupAppliance(self):
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        backupTaskURL = 'https://%s/rest/backups' % (self.con._ip)

        try:
            response = self.con.post(backupTaskURL, headers=headers)

        except Exception as e:
            msg = "Exception occured while attempting to start backup of appliance!"
            raise Exception(msg, e)

        if response.status_code != 202:
            msg = "Status %d received from starting the appliance backup!" \
                % (response.status_code)
            raise Exception(msg, response.text)
        else:
            return response.headers['Location']

    def getBackupDownloadURI(self, downloadUri):
        headers = self.con._headers.copy()
        ip = self.con._ip

        backupDownloadURL = string.Template("https://$ip$downloadUri")
        backupDownloadURL = backupDownloadURL.substitute(ip=ip, downloadUri=downloadUri)
        try:
            response = self.con.get(backupDownloadURL, headers=headers)
        except Exception as e:
            msg = "Exception occured while attempting to start backup of appliance!"
            raise Exception(msg, e)

        if response['status'] != 'SUCCEEDED':
            msg = "Status %d received from starting the appliance backup!" \
                % (response)
        else:
            return response['downloadUri']

    def getBackupDownloadURIOLD(self, downloadUri):
        log.debug("In getBackupDownloadURI method")
        headers = self.con._headers.copy()
        self.downloadUri = downloadUri
        backupDownloadURL = string.Template("https://$ip$downloadUri")
        backupDownloadURL = backupDownloadURL.substitute(ip=self.con._ip, downloadUri=downloadUri)
        log.debug("downloadURI: %s" % (download.Uri))
        r = self.con.get(backupDownloadURL, headers=headers)
        log.debug("r: %s" % (r))

    def getBackupData(self, backupURI):
        self.backupLocation = backupURI
        log = logging.getLogger(libLogger)
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Accept': 'application/octet-stream;q=0.8', 'Accept': 'application/json', 'X-API-Version': '1'}
        downloadURL = string.Template("https://$ip$backupURI")
        downloadURL = downloadURL.substitute(ip=self.con._ip, backupURI=self.backupLocation)

        try:
            r = requests.get(downloadURL, auth=self.sessionID, headers=headers, verify=False, stream=True)
        except Exception as e:
            msg = "Exception occured while attempting to download backup of appliance!"
            raise Exception(msg, e)

        if r.status_code != 200:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            msg = "Status %d received from getting the backup" \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            return r.json()

    def downloadBackupFile(self, backupURI, sessionId, backupFilename):
        self.backupLocation = backupURI
        self.backupURI = backupURI
        self.backupFilename = backupFilename
        fileName = backupFilename
        self.sessionId = sessionId
        headers = {'Auth': sessionId, 'Accept': 'application/octetstream;q=0.8', 'Accept': 'application/json', 'X-API-Version': '200'}
        totalBlocks = 0
        chunk_size = 1024

        backupDownloadURL = string.Template("https://$ip$backupUri")
        backupDownloadURL = backupDownloadURL.substitute(ip=self.con._ip, backupUri=backupURI)

        try:
            r = requests.get(backupDownloadURL, headers=headers, stream=True, verify=False)
            with open(fileName, 'wb') as f:
                f.write(r.content)

        except Exception as e:
            msg = "Exception occured while attempting to download backup of appliance!"
            raise Exception(msg, e)

        if r.status_code != 200:
            msg = "Status %d received from getting the backup" \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            return r.status_code


class RestoreAppliance(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)
        self.sessionId = self.con._sessionId

    def uploadBackupFile(self, backupfile, sessionId):
        headers = {'Auth': sessionId, 'Accept': 'application/json', 'Accept-language': 'en_US', 'X-API-Version': '200'}
        restoreTaskURL = string.Template("https://$ip/rest/backups/archive")
        restoreTaskURL = restoreTaskURL.substitute(ip=self.con._ip)
        try:
            r = requests.post(restoreTaskURL, headers=headers, files={'file': open(backupfile, 'rb')}, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to start upload of backup file to appliance!"
            raise Exception(msg, e)

        if r.status_code != 200:
            msg = "Status %d received from upload of the backup file to the appliance." \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            return r.json()

    def restoreAppliance(self, restoreURI, sessionId):
        headers = {'Auth': sessionId, 'Accept': 'application/json', 'Accept-language': 'en_US', 'X-API-Version': '200', 'Content-Type': 'application/json'}
        data = {'type': "RESTORE", 'uriOfBackupToRestore': restoreURI}
        restoreURL = string.Template("https://$ip/restore/rest/resources")
        restoreURL = restoreURL.substitute(ip=self.con._ip)
        try:
            r = requests.post(restoreURL, data=json.dumps(data), headers=headers, verify=False, stream=True)
        except Exception as e:
            msg = "Exception occured while attempting to start restore of the appliance!"
            raise Exception(msg, e)

        if r.status_code != 202:
            msg = "Status %d received from starting the restore task." \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            return r.json()

    def restoreApplianceOLD(self, restoreURI):
        self.restoreURI = restoreURI
        log = logging.getLogger(libLogger)
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'X-API-Version': '1', 'Content-Type': 'application/json'}
        data = {'type': "RESTORE", 'uriOfBackupToRestore': restoreURI}
        restoreURL = string.Template("https://$ip/restore/rest/resources")
        restoreURL = restoreURL.substitute(ip=self.con._ip)

        try:
            r = requests.post(restoreURL, data=json.dumps(data), auth=self.sessionID, headers=headers, verify=False, stream=True)
        except Exception as e:
            msg = "Exception occured while attempting to start restore of the appliance!"
            raise Exception(msg, e)

        if r.status_code != 200:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            msg = "Status %d received from starting the restore task." \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            return r.json()


class TimeConfigBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def setTimeZone(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('applTimeZone'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response

    def setNtp(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('applNtp'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(reqBody))
        return response


class PowerAppliance(object):

    def __init__(self, ip, sessionID):
        self.con = connection(ip=ip, sessionId=sessionID)

    def rebootAppliance(self, ip, sessionID):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s?type=REBOOT' % (self.con._ip, uris.get('shutdown'))
        response = self.con.post(uri=uri, headers=headers)
        return response

    def shutdownAppliance(self, ip, sessionID):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s?type=HALT' % (self.con._ip, uris.get('shutdown'))
        response = self.con.post(uri=uri, headers=headers)
        return response


class CreateSupportDump(object):

    def __init__(self, ip, sessionID):
        self.con = connection(ip=ip, sessionId=sessionID)

    def createSupportDump(self, ip, sessionID):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        headers['errorCode'] = 'Appliance'
        headers['encrypt'] = 'true'
        data = {'errorCode': "CI100"}
        uri = 'https://%s%s' % (self.con._ip, uris.get('supportDumps'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response


class GetSupportDump(object):

    def __init__(self, ip, sessionID, supportDumpURI, supportDumpFileSize):
        con = connection(ip=ip, sessionId=sessionID)
        self.con._ip = con._ip
        self.sessionID = con._sessionId
        self.headers = con._headers
        self.supportDumpDownloadURI = supportDumpURI
        self.supportDumpFileSize = supportDumpFileSize

    def downloadSupportDumpFile(self, ip, sessionID, supportDumpURI, supportDumpFileSize):
        log = logging.getLogger(libLogger)
        fileSize = self.supportDumpFileSize
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Accept': 'application/octet-stream;q=0.8', 'Accept': 'application/json', 'X-API-Version': '1'}
        fileNameList = supportDumpURI.split("/", 7)
        fileNameLocation = len(fileNameList) - 1
        fileName = fileNameList[fileNameLocation]
        downURL = string.Template("https://$ip$supportDumpDownloadURI")
        downURL = downURL.substitute(ip=self.con._ip, supportDumpDownloadURI=self.supportDumpDownloadURI)

        try:
            totalBlocks = 0
            print "downURL = %s" % (downURL)
            with open(fileName, "wb") as f:
                r = requests.get(downURL, auth=self.sessionID, headers=headers, verify=False, stream=True)
                print "Downloading: %s" % (fileName)
                for block in r.iter_content(1024):
                    if not block:
                        print "NOT BLOCK!!!"
                        exit(1)
                    f.write(block)
                    totalBlocks = totalBlocks + len(block)
        except Exception as e:
            msg = "Exception occured while attempting to start download of support dump file from appliance!"
            raise Exception(msg, e)

        if r.status_code != 200:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            msg = "Status %d received from download of the support dump file to the appliance." \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            print "Downloaded of: %s complete, size: %d." % (fileName, totalBlocks)


class ControllerState(object):

    def __init__(self, ip, sessionId=None):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getState(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('state'))
        response = self.con.get(uri=uri, headers=headers)
        return response
