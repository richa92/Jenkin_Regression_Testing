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
from operator import itemgetter, attrgetter
libLogger = "api-logger"

import pdb


class ConnTempBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def createConnTemp(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'connection-template', 'name': reqBody['name'],
                'bandwidth': {'maximumBandwidth': reqBody['maxband'],
                              'typicalBandwidth': reqBody['typband']}}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('ct'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getConnTemp(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('ct'), uri)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getDefConnTemp(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('default-ct'))
        response = self.con.get(uri=uri, headers=headers)

        return response

    def updateConnTemp(self, reqBody, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        data = {'type': 'connection-template', 'name': reqBody['name'],
                'bandwidth': {'maximumBandwidth': reqBody['maxband'],
                              'typicalBandwidth': reqBody['typband']}, 'eTag': reqBody['eTag']}
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('ct'), uri)
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def updateDefConnTemp(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        data = {'type': 'connection-template',
                'bandwidth': {'maximumBandwidth': reqBody['maximumBandwidth'],
                              'typicalBandwidth': reqBody['typicalBandwidth']}, 'name': 'defaultConnectionTemplate'}
        uri = 'https://%s%s' % (self.con._ip, uris.get('default-ct'))
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response


class NetworkBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def createEthNet(self, reqBody, vlan, name):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'ethernet-networkV2', 'vlanId': vlan, 'purpose': reqBody['purpose'],
                'name': name, 'smartLink': reqBody['smart'],
                'privateNetwork': reqBody['private'], 'ethernetNetworkType': reqBody['ethernetNetworkType']}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('enet'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def createBulkEthNet(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'bulk-ethernet-network', 'vlanIdRange': reqBody['vlanIdRange'], 'purpose': reqBody['purpose'],
                'namePrefix': reqBody['prefix'], 'smartLink': reqBody['smart'],
                'privateNetwork': reqBody['private']}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('enetBulk'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def createFcNet(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        mlr = None
        if reqBody['autoLoginRedistribution'] == 'manual':
            mlr = 'false'
        else:
            mlr = 'true'

        if 'san' in reqBody:
            data = {'type': 'fc-networkV2', 'name': reqBody['name'],
                    'linkStabilityTime': reqBody['linkStabilityTime'],
                    'autoLoginRedistribution': mlr,
                    'managedSanUri': reqBody['san'],
                    'fabricType': reqBody['fabricType']}
        else:
            data = {'type': 'fc-networkV2', 'name': reqBody['name'],
                    'linkStabilityTime': reqBody['linkStabilityTime'],
                    'autoLoginRedistribution': mlr,
                    'fabricType': reqBody['fabricType']}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('fcnet'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getEthNets(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('enet'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('enet'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getFcNets(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('fcnet'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('fcnet'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def deleteFcNet(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('fcnet'), uri)
        response = self.con.delete(uri=uri, headers=headers)
        return response

    def getEthNet(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s%s' % (self.con._ip, uris.get('enet'), uri)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def deleteEthNet(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('enet'), uri)
        response = self.con.delete(uri=uri, headers=headers)
        return response


class NetworkSetBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getNetworkSet(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('nset'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('nset'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def createNetworkSet(self, reqBody, networkUris, nativeNwUri):
        global uris
        log = logging.getLogger(libLogger)
        if nativeNwUri == "null":
            data = {'type': 'network-set', 'name': reqBody['name'],
                    'networkUris': networkUris}
        else:
            data = {'type': 'network-set', 'name': reqBody['name'], 'nativeNetworkUri': nativeNwUri,
                    'networkUris': networkUris}
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('nset'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def deleteNwSet(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('nset'), uri)
        response = self.con.delete(uri=uri, headers=headers)
        return response


class LogicalIntGrpBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def createLogicalIntGrp(self, reqBody):
        global uris
        log = logging.getLogger(libLogger)
        data = reqBody
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('lig'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getLogicalIntGrp(self, filter):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('lig'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('lig'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def updateLogicalIntGrp(self, reqBody, interconnectId):
        global uris
        log = logging.getLogger(libLogger)
        data = reqBody
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('lig'), interconnectId)
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def deleteLogicalIntGrp(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('lig'), uri)
        response = self.con.delete(uri=uri, headers=headers)
        return response


class UplinkSetBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def createUplinkSet(self, reqBody, networkUris, portConfigInfos, primaryPortLocation,
                        logIntUri, natNetUri, fcNetworkUris, networkType, mlrstate):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'uplink-set', 'name': reqBody['name'], 'networkUris': networkUris,
                'portConfigInfos': portConfigInfos, 'networkType': networkType,
                'primaryPortLocation': primaryPortLocation, 'logicalInterconnectUri': logIntUri,
                'connectionMode': reqBody['connectionMode'], 'nativeNetworkUri': natNetUri,
                'fcNetworkUris': fcNetworkUris, 'state': None, 'description': None, 'status': None,
                'uri': None, 'category': None, 'modified': None, 'created': None, 'eTag': None,
                'manualLoginRedistributionState': mlrstate, 'reachability': None}

        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('us'))
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))
        return response

    def getUplinkSet(self, filter=None):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        if filter:
            uri = 'https://%s%s?%s' % (self.con._ip, uris.get('us'), filter)
        else:
            uri = 'https://%s%s' % (self.con._ip, uris.get('us'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    # b.    To trigger MLR distribution, the user will set the MLR state to DISTRIBUTING in the DTO.
    def triggerMLR(self, uplinkSetUri, reqBody, networkUris, portConfigInfos, primaryPortLocation,
                   logIntUri, natNetUri, fcNetworkUris, networkType):
        global uris
        log = logging.getLogger(libLogger)
        data = {'type': 'uplink-set', 'name': reqBody['name'], 'networkUris': networkUris,
                'portConfigInfos': portConfigInfos, 'networkType': networkType,
                'primaryPortLocation': primaryPortLocation, 'logicalInterconnectUri': logIntUri,
                'mode': reqBody['mode'], 'nativeNetworkUri': natNetUri,
                'fcNetworkUris': fcNetworkUris, 'state': None, 'description': None, 'status': None,
                'uri': None, 'category': None, 'modified': None, 'created': None, 'eTag': None,
                'manualLoginRedistributionState': 'DISTRIBUTING', 'reachability': None}

        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('us'))
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response


class InterconnectBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getInterconnect(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uri)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getInterconnects(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('ic'))
        response = self.con.get(uri=uri, headers=headers)
        return response

    def getInterconnectStates(self):
        try:
            interconnects = InterconnectBase.getInterconnects(self)
            icCollection = dict()
            icCollection['type'] = interconnects['type']
            icMembers = []

            for ic in interconnects['members']:
                locationEntries = ic['interconnectLocation']['locationEntries']
                for x in xrange(len(ic['interconnectLocation']['locationEntries'])):
                    if ic['interconnectLocation']['locationEntries'][x]['type'] == 'Bay':
                        bay = ic['interconnectLocation']['locationEntries'][x]['value']

                ports = ic['ports']

                icDict = dict()
                icDict['bay'] = bay
                icDict['type'] = ic['type']
                icDict['model'] = ic['model']
                icDict['state'] = ic['state']
                icDict['uri'] = ic['uri']
                icDict['locationEntries'] = locationEntries

                portInfo = []
                for p in sorted(ports, key=itemgetter('portStatus', 'portName')):
                    portInfoDict = dict()
                    portInfoDict['portName'] = p['portName']
                    portInfoDict['portId'] = p['portId']
                    portInfoDict['portType'] = p['portType']
                    portInfoDict['configPortTypes'] = p['configPortTypes']
                    portInfoDict['portHealthStatus'] = p['portHealthStatus']
                    portInfoDict['portStatus'] = p['portStatus']
                    portInfoDict['portStatusReason'] = p['portStatusReason']
                    portInfoDict['bayNumber'] = p['bayNumber']
                    portInfoDict['lagId'] = p['lagId']
                    portInfoDict['state'] = p['state']
                    portInfoDict['status'] = p['portStatusReason']
                    portInfo.append(portInfoDict)

                icDict['ports'] = portInfo
                icMembers.append(icDict)
                icCollection['members'] = icMembers

            return icCollection

        except Exception as e:
            msg = "Exception occured while attempting to build the interconnects state collection"
            raise Exception(msg)

    def getInterconnectTypes(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('ictype'))
        response = self.con.get(uri=uri, headers=headers)
        return response


class PoolsBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def createRange(self, category, ptype, start, end, count):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()

        catIdRange = "id-range-" + ptype.upper()

        data = {}
        data['type'] = 'Range'
        data['rangeCategory'] = category
        data['category'] = catIdRange
        data['allocatedIdCount'] = 0
        data['freeIdCount'] = 0
        data['endAddress'] = None
        data['startAddress'] = None
        data['uri'] = None
        data['reservedIdCount'] = 0
        data['allocatorUri'] = None
        data['collectorUri'] = None
        data['name'] = ptype.upper()
        data['enabled'] = True
        data['prefix'] = None

        if category == "CUSTOM":
            data['totalCount'] = count
            data['freeIdCount'] = count
            data['endAddress'] = end
            data['startAddress'] = start

        uri = 'https://%s%s/%s/ranges/' % (self.con._ip, uris.get('idpool'), ptype.lower())
        response = self.con.post(uri=uri, headers=headers, body=json.dumps(data))

        return response

    def enableRange(self, uri, enabled):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        data = {'type': 'Range', 'enabled': enabled}
        uri = 'https://%s%s' % (self.con._ip, uri)
        response = self.con.put(uri=uri, headers=headers, body=json.dumps(data))
        return response

    # There are 3 types of pools: VMAC, VWWN, and VSN.  Each pool type contains ranges.  Pool object contains a reference to it's ranges in rangeUris.
    def getPool(self, ptype):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s' % (self.con._ip, uris.get('idpool'), ptype.lower())
        response = self.con.get(uri=uri, headers=headers)
        return response

    # There are 3 types of pools: VMAC, VWWN, and VSN.  Each pool type contains ranges.  Pool object contains a reference to it's ranges in rangeUris.
    def getRange(self, uri):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uri)
        response = self.con.get(uri=uri, headers=headers)
        return response

    def deleteVmacRange(self, uuid):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s/%s' % (self.con._ip, uris.get('vmac-pool'), 'ranges', uuid)
        response = self.con.delete(uri=uri, headers=headers)
        return response

    def deleteVwwnRange(self, uuid):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s/%s' % (self.con._ip, uris.get('vwwn-pool'), 'ranges', uuid)
        response = self.con.delete(uri=uri, headers=headers)
        return response

    def deleteVsnRange(self, uuid):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s/%s/%s' % (self.con._ip, uris.get('vsn-pool'), 'ranges', uuid)
        response = self.con.delete(uri=uri, headers=headers)
        return response


class LogicalInterconnectBase(object):

    def __init__(self, ip, sessionId):
        self.con = connection(ip=ip, sessionId=sessionId)

    def getLogicalInterconnects(self):
        global uris
        log = logging.getLogger(libLogger)
        headers = self.con._headers.copy()
        uri = 'https://%s%s' % (self.con._ip, uris.get('li'))
        response = self.con.get(uri=uri, headers=headers)
        return response


class CreateLISupportDump(object):

    def __init__(self, ip, uri, sessionID):
        con = connection(ip=ip, sessionId=sessionID)
        self.ip = con._ip
        self.sessionID = con._sessionId
        self.headers = con._headers
        self.uri = uri

    def createLISupportDump(self, uri, ip, sessionID):
        log = logging.getLogger(libLogger)
        headers = self.headers.copy()
        headers['errorCode'] = 'LI'
        headers['encrypt'] = 'true'

        data = {'errorCode': "LI"}
        supportDumpTaskURL = string.Template("https://$ip/$uri/support-dumps")
        supportDumpTaskURL = supportDumpTaskURL.substitute(ip=self.ip, uri=self.uri)

        try:
            r = requests.post(supportDumpTaskURL, auth=self.sessionID, data=json.dumps(data), headers=headers, verify=False)
        except Exception as e:
            msg = "Exception occured while attempting to create support dump of logical interconnct!"
            raise Exception(msg, e)

        if r.status_code != 200:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            msg = "Status %d received from create logical interconnect support dump." \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            log.debug('\nResponse Body %s' % pprint.PrettyPrinter().pformat(r.json()))
            return r.json()


class GetLISupportDump(object):

    def __init__(self, ip, liSupportDumpURI, sessionID, liSupportDumpFileSize):
        con = connection(ip=ip, sessionId=sessionId)
        self.ip = con._ip
        self.sessionID = con._sessionId
        self.headers = con._headers
        self.liSupportDumpDownloadURI = liSupportDumpURI
        self.liSupportDumpFileSize = liSupportDumpFileSize

    def downloadLISupportDump(self, liSupportDumpURI, ip, sessionID, liSupportDumpFileSize):
        log = logging.getLogger(libLogger)
        fileSize = self.liSupportDumpFileSize
        headers = {'Accept': 'application/json', 'Accept-language': 'en_US', 'Accept': 'application/octet-stream;q=0.8', 'Accept': 'application/json', 'X-API-Version': '1'}

        fileNameList = liSupportDumpURI.split("/", 7)
        fileNameLocation = len(fileNameList) - 1
        fileName = fileNameList[fileNameLocation]
        downURL = string.Template("https://$ip$liSupportDumpURI")
        downURL = downURL.substitute(ip=self.ip, liSupportDumpURI=self.liSupportDumpDownloadURI)

        # TODO - Remove print and exit statements
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
            msg = "Exception occured while attempting to start download of logical interconnect support dump file from appliance!"
            raise Exception(msg, e)
            print "ERROR"

        if r.status_code != 200:
            msg = "Status %d received from download of the logical interconnect support dump file to the appliance." \
                % (r.status_code)
            raise Exception(msg, r.text)
        else:
            print "Downloaded of: %s complete, size: %d." % (fileName, totalBlocks)
